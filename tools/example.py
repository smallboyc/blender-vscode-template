import bpy


def print_default_scene_objects() -> None:
    for object in bpy.data.objects:
        print(object.name)
