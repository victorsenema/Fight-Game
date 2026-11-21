import cv2
import numpy as np
from pathlib import Path

from tools.archives_manipulation import json_reader
from tools.data_manager import characters_data_manager


def read_image(image_path: Path):
    return cv2.imdecode(np.fromfile(image_path, np.uint8), cv2.IMREAD_UNCHANGED)

def get_image_info(image_path: Path):
    image = read_image(image_path)
    if image is None:
        return None
    height, width = image.shape[:2]
    return {"width": width, "height": height}


def print_info():
    print_characters_image_info()
    print_stage_image_info()

def print_characters_image_info():
    ROOT = Path(__file__).resolve().parent.parent.parent.parent

    paths = json_reader.get_json_data(ROOT / "data" / "data_paths" / "paths.json")

    for char_name, char_rel_path in paths["characters"].items():
        char_path = ROOT / char_rel_path
        data = json_reader.get_json_data(char_path)
        if data is None:
            continue

        folder = ROOT / characters_data_manager.get_folder(data, char_path)
        sprites = characters_data_manager.get_sprites(data, char_path)
        print(f"\n{char_path.name}")

        char_info = {}
        for anim_name, sheets in sprites.items():
            if isinstance(sheets, str):
                sheets = [sheets]

            for sheet in sheets:
                image_path = folder / sheet

                if not image_path.exists():
                    print(f"  [ERROR] {anim_name}: file does not exist -> {image_path}")
                    continue

                image = read_image(image_path)
                if image is None:
                    print(f"  [ERROR] {anim_name}: couldn't read -> {image_path}")
                    continue

                height, width = image.shape[:2]
                frames = width // height

                char_info[sheet] = {
                    "animation": anim_name,
                    "width": width,
                    "height": height,
                    "frames": frames,
                }
                print(f"  {anim_name:10} {sheet:20} {width}x{height}  "
                      f"frames={frames}")

def print_stage_image_info():
    ROOT = Path(__file__).resolve().parent.parent.parent.parent

    paths = json_reader.get_json_data(ROOT / "data" / "data_paths" / "paths.json")

    for stage_name, stage_rel_path in paths["stages"].items():
        stage_path = ROOT / stage_rel_path
        data = json_reader.get_json_data(stage_path)
        if data is None:
            continue

        for key in ("folder", "variants"):
            if key not in data:
                raise KeyError(f"'{key}' missing in {stage_path}")

        folder = ROOT / data["folder"]
        print(f"\n{stage_name}")

        stage_info = {}
        for variant_name, layers in data["variants"].items():
            print(f"  [{variant_name}]")

            variant_info = {}
            for layer in layers:
                image_path = folder / layer

                if not image_path.exists():
                    print(f"    [ERROR] file does not exist -> {image_path}")
                    continue

                info = get_image_info(image_path)
                if info is None:
                    print(f"    [ERROR] couldn't read -> {image_path}")
                    continue

                variant_info[layer] = info
                print(f"    {layer:15} {info['width']}x{info['height']}")

            stage_info[variant_name] = variant_info