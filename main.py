import os
import sys

# region ESSENTIAL SETUP -- DO NOT TOUCH --

DEV_FLAG = "<run_path>"
TOOLS_FLAG = "tools"

# Essential : add project root path to python sys.path
project_root = os.path.dirname(os.path.abspath(__file__))

if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Auto unregister tools modules
for module_name in list(sys.modules.keys()):
    if module_name == TOOLS_FLAG or module_name.startswith(f"{TOOLS_FLAG}."):
        del sys.modules[module_name]

# endregion ESSENTIAL SETUP -- DO NOT TOUCH --


# region -- MODULES IMPORT --
from tools.example import print_default_scene_objects

# endregion -- MODULES IMPORT --

if __name__ == DEV_FLAG:
    print_default_scene_objects()
