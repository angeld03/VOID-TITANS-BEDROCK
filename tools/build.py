#!/usr/bin/env python3
"""Validate and package the VOID TITANS Bedrock add-on."""
from __future__ import annotations

import io
import json
import struct
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parents[1]
BP = ROOT / "behavior_pack"
RP = ROOT / "resource_pack"
DIST = ROOT / "dist"


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as stream:
        return json.load(stream)


def png_size(path: Path) -> tuple[int, int]:
    data = path.read_bytes()
    if len(data) < 24 or data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError(f"Invalid PNG file: {path.relative_to(ROOT)}")
    return struct.unpack(">II", data[16:24])


def pack_bytes(folder: Path) -> bytes:
    stream = io.BytesIO()
    with ZipFile(stream, "w", ZIP_DEFLATED) as archive:
        for file in sorted(folder.rglob("*")):
            if file.is_file():
                archive.write(file, file.relative_to(folder).as_posix())
    return stream.getvalue()


def validate() -> int:
    json_files = sorted(BP.rglob("*.json")) + sorted(RP.rglob("*.json"))
    documents = {path: load_json(path) for path in json_files}

    behavior_manifest = documents[BP / "manifest.json"]
    resource_manifest = documents[RP / "manifest.json"]
    behavior_header = behavior_manifest["header"]
    if not any(
        dep["uuid"] == behavior_header["uuid"] and dep["version"] == behavior_header["version"]
        for dep in resource_manifest.get("dependencies", [])
    ):
        raise ValueError("Resource Pack does not depend on the current Behavior Pack UUID/version")

    behavior_entity = documents[BP / "entities" / "void_titan.json"]["minecraft:entity"]
    client_description = documents[RP / "entity" / "void_titan.entity.json"]["minecraft:client_entity"]["description"]
    geometry = documents[RP / "models" / "entity" / "void_titan.geo.json"]["minecraft:geometry"][0]
    animations = documents[RP / "animations" / "void_titan.animation.json"]["animations"]
    controllers = documents[RP / "animation_controllers" / "void_titan.animation_controllers.json"]["animation_controllers"]
    particles = {
        doc["particle_effect"]["description"]["identifier"]
        for path, doc in documents.items()
        if path.parent.name == "particles"
    }

    if behavior_entity["description"]["identifier"] != client_description["identifier"]:
        raise ValueError("Behavior/client entity identifiers do not match")
    if client_description["geometry"]["default"] != geometry["description"]["identifier"]:
        raise ValueError("Client entity geometry identifier does not resolve")

    texture = RP / (client_description["textures"]["default"] + ".png")
    if not texture.is_file():
        raise ValueError(f"Missing entity texture: {texture.relative_to(ROOT)}")

    controller_ref = client_description["scripts"]["animate"][0]
    if controller_ref not in controllers:
        raise ValueError(f"Missing animation controller: {controller_ref}")

    aliases = set(client_description["animations"])
    controller = controllers[controller_ref]
    referenced_particles = set()
    for state in controller["states"].values():
        for animation in state.get("animations", []):
            names = [animation] if isinstance(animation, str) else list(animation.keys())
            missing = set(names) - aliases
            if missing:
                raise ValueError(f"Controller uses undeclared animation aliases: {sorted(missing)}")
        for effect in state.get("particle_effects", []):
            alias = effect["effect"]
            if alias not in client_description.get("particle_effects", {}):
                raise ValueError(f"Undeclared client particle alias: {alias}")
            referenced_particles.add(client_description["particle_effects"][alias])

    declared_animation_ids = set(animations)
    for alias, animation_id in client_description["animations"].items():
        if animation_id not in declared_animation_ids:
            raise ValueError(f"Animation alias {alias} points to missing animation {animation_id}")
    if not referenced_particles.issubset(particles):
        raise ValueError(f"Missing controller particle effects: {sorted(referenced_particles - particles)}")

    bone_names = {bone["name"] for bone in geometry["bones"]}
    for bone in geometry["bones"]:
        parent = bone.get("parent")
        if parent and parent not in bone_names:
            raise ValueError(f"Bone {bone['name']} has missing parent {parent}")
    core = next((b for b in geometry["bones"] if b["name"] == "void_core"), None)
    root = next((b for b in geometry["bones"] if b["name"] == "root"), None)
    if not core or "core" not in core.get("locators", {}):
        raise ValueError("Void core particle locator is missing")
    if not root or "impact" not in root.get("locators", {}):
        raise ValueError("Ground impact locator is missing")

    groups = behavior_entity.get("component_groups", {})
    events = behavior_entity.get("events", {})
    for event_name, definition in events.items():
        nodes = [definition]
        nodes.extend(definition.get("randomize", []))
        nodes.extend(definition.get("sequence", []))
        for node in nodes:
            for operation in ("add", "remove"):
                group_names = node.get(operation, {}).get("component_groups", [])
                missing = set(group_names) - set(groups)
                if missing:
                    raise ValueError(f"Event {event_name} references missing groups: {sorted(missing)}")

    assets = [
        BP / "pack_icon.png",
        RP / "pack_icon.png",
        RP / "textures" / "entity" / "void_titan.png",
        RP / "textures" / "particle" / "void_spark.png",
    ]
    for asset in assets:
        if not asset.is_file():
            raise ValueError(f"Missing required asset: {asset.relative_to(ROOT)}")
        png_size(asset)

    if png_size(texture) != (
        geometry["description"]["texture_width"],
        geometry["description"]["texture_height"],
    ):
        raise ValueError("Entity PNG dimensions do not match geometry texture dimensions")

    return len(json_files)


def main() -> None:
    count = validate()
    DIST.mkdir(exist_ok=True)
    bp_bytes = pack_bytes(BP)
    rp_bytes = pack_bytes(RP)
    (DIST / "VOID-TITANS-Behavior.mcpack").write_bytes(bp_bytes)
    (DIST / "VOID-TITANS-Resources.mcpack").write_bytes(rp_bytes)

    combined = DIST / "VOID-TITANS-BEDROCK.mcaddon"
    with ZipFile(combined, "w", ZIP_DEFLATED) as archive:
        archive.writestr("VOID-TITANS-Behavior.mcpack", bp_bytes)
        archive.writestr("VOID-TITANS-Resources.mcpack", rp_bytes)

    packages = [
        DIST / "VOID-TITANS-Behavior.mcpack",
        DIST / "VOID-TITANS-Resources.mcpack",
        combined,
    ]
    for package in packages:
        with ZipFile(package) as archive:
            corrupt = archive.testzip()
            if corrupt:
                raise RuntimeError(f"Archive test failed: {package.name} contains {corrupt}")

    with ZipFile(combined) as archive:
        expected = {"VOID-TITANS-Behavior.mcpack", "VOID-TITANS-Resources.mcpack"}
        if not expected.issubset(set(archive.namelist())):
            raise RuntimeError("Combined add-on is missing one or more pack archives")

    print(f"Validated {count} JSON documents, pack linkage, entity/model/animation/particle references and required PNG assets.")
    for package in packages:
        print(f"Created {package.relative_to(ROOT)} ({package.stat().st_size:,} bytes)")
    print("Automated archive checks passed. Import and gameplay testing in Minecraft Bedrock are still required.")


if __name__ == "__main__":
    main()
