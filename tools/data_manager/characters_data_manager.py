def get_folder(data: dict, json_path=""):
    # If the key doesn't exist raise a KeyError
    # If Just return data["folder"] if it exists will return the data
    # else it will return None
    if "folder" not in data:
        raise KeyError(f"'folder' missing in {json_path}")
    return data["folder"]

def get_sprites(data: dict, json_path=""):
    if "sprites" not in data:
        raise KeyError(f"'sprites' missing in {json_path}")
    return data["sprites"]

def get_sprites_frames_quantity(data: dict, json_path=""):
    if "sprites_frames_quantity" not in data:
        raise KeyError(f"'sprites_frames_quantity' missing in {json_path}")
    return data["sprites_frames_quantity"]
