#!/usr/bin/env python3
"""Validate and package the VOID TITANS Bedrock add-on."""
from __future__ import annotations

import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parents[1]
BP = ROOT / "behavior_pack"
RP = ROOT / "resource_pack"
DIST = ROOT / "dist"


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as stream:
        return json.load(stream)


def write_pack(output: Path, folder: Path, include_folder: bool) -> None:
    with ZipFile(output, "w", ZIP_DEFLATED) as archive:
        for file in sorted(folder.rglob("*")):
            if file.is_file():
                relative = file.relative_to(folder)
                name = f"{folder.name}/{relative}" if include_folder else str(relative)
                archive.write(file, name)


def validate() -> int:
    json_files = list(BP.rglob("*.json")) + list(RP.rglob("*.json"))
    for path in json_files:
        load_json(path)

    behavior_manifest = load_json(BP / "manifest.json")
    resource_manifest = load_json(RP / "manifest.json")
    behavior_uuid = behavior_manifest["header"]["uuid"]
    assert any(dep["uuid"] == behavior_uuid for dep in resource_manifest["dependencies"])

    behavior_entity = load_json(BP / "entities" / "void_titan.json")["minecraft:entity"]
    client_entity = load_json(RP / "entity" / "void_titan.entity.json")["minecraft:client_entity"]["description"]
    geometry = load_json(RP / "models" / "entity" / "void_titan.geo.json")["minecraft:geometry"][0]
    particle = load_json(RP / "particles" / "void_spark_aura.particle.json")["particle_effect"]

    assert behavior_entity["description"]["identifier"] == client_entity["identifier"]
    assert client_entity["geometry"]["default"] == geometry["description"]["identifier"]
    assert client_entity["particle_effects"]["void_aura"] == particle["description"]["identifier"]
    assert any(b.get("name") == "void_core" and "core" in b.get("locators", {}) for b in geometry["bones"])

    assets = [
        BP / "pack_icon.png", RP / "pack_icon.png",
        RP / "textures" / "entity" / "void_titan.png",
        RP / "textures" / "particle" / "void_spark.png",
    ]
    for asset in assets:
        assert asset.is_file(), f"Missing required asset: {asset.relative_to(ROOT)}"
    return len(json_files)


def main() -> None:
    count = validate()
    DIST.mkdir(exist_ok=True)
    write_pack(DIST / "VOID-TITANS-Behavior.mcpack", BP, include_folder=False)
    write_pack(DIST / "VOID-TITANS-Resources.mcpack", RP, include_folder=False)
    with ZipFile(DIST / "VOID-TITANS-BEDROCK.mcaddon", "w", ZIP_DEFLATED) as archive:
        for folder in (BP, RP):
            for file in sorted(folder.rglob("*")):
                if file.is_file():
                    archive.write(file, f"{folder.name}/{file.relative_to(folder)}")

    for package in DIST.glob("*"):
        with ZipFile(package) as archive:
            corrupt = archive.testzip()
            if corrupt:
                raise RuntimeError(f"Archive test failed: {package.name} contains {corrupt}")

    print(f"Validated {count} JSON files and cross-pack references.")
    print("Created packages in dist/. Import and in-game behavior still need testing in Minecraft Bedrock.")


if __name__ == "__main__":
    main()
