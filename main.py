import bpy

DEV_FLAG = "<run_path>"

def print_default_scene_objects() -> None:
    for object in bpy.data.objects:
        print(object.name)

if __name__ == DEV_FLAG:
    print_default_scene_objects()