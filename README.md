# Blender + VSCode Starter Template

This repo is a **starter template** for developing Blender scripts and add-ons directly from VSCode, instead of using Blender's built-in text editor.

## Why this template?

Coding in Blender's text editor works, but it's limited: no real autocompletion, no linting, no proper project management. This template sets up an environment that gives you:

- **Autocompletion** and type checking on `bpy` and other Blender modules
- The ability to talk **from VSCode to Blender** using dedicated commands, without leaving your editor
- A clean, isolated Python environment (venv)
- An auto-reload mechanism that prevents Blender from caching your custom modules

## Using this template

Don't clone this repo directly if you want to build your own add-on from it, you won't have push access to your own work. Instead:

1. Click the **"Use this template"** button at the top of this repo (not "Fork").
2. GitHub creates a brand new, independent repo under your own account, with no link back to this one.
3. Clone *your* new repo and start working: `main` is yours from the first commit.

This is different from forking: a fork keeps a relationship with the original repo (useful if you plan to contribute back via pull requests), whereas "Use this template" gives you a clean, standalone starting point meant to diverge immediately.

### Pulling future template updates (optional)

Since your repo has no link to this one, you won't get future improvements to the template automatically. If you want to be able to pull them later, add this repo as a second remote in your own project:

```bash
git remote add template https://github.com/smallboyc/blender-vscode-template.git
git fetch template
git merge template/main --allow-unrelated-histories
```

## Prerequisites

- [Blender](https://www.blender.org/) installed on your machine
- [VSCode](https://code.visualstudio.com/) installed
- Python installed on your machine (to create the venv)

## Installation

### 1. Install the "Blender Development" VSCode extension

In VSCode, go to the Extensions tab and install **Blender Development** (by Jacques Lucke).

### 2. Create a virtual environment

At the root of the project:

```bash
python -m venv env
```

### 3. Activate the venv

```bash
# macOS / Linux
source env/bin/activate

# Windows
env\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

This file notably includes `fake-bpy-module`, which provides the stubs needed for `bpy` autocompletion (without actually running Blender).

### 5. Select the venv's Python interpreter

In VSCode:

- `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (macOS)
- Search for **"Python: Select Interpreter"**
- Choose the interpreter located in `env`

## Project structure

```
.
├── .vscode/
│   └── settings.json
├── env/
├── tools/                # Put your custom sub-modules here
│   └── example.py        # Example tool module
├── .gitignore
├── main.py               # <--- The ONLY entry point to run
├── requirements.txt
└── README.md
```

## Usage & Development Workflow

### The `tools` folder

Any custom tools, utilities, or modular scripts you write must be created inside the `tools/` directory (`tools/cameras.py`, `tools/mesh_utils.py`, ...).

To use your tools, import them directly into the `main.py` script:

```python
from tools.example import print_default_scene_object
```

### The `main.py` script (single entry point)

**`main.py` is the only script you should ever run.** It contains a vital, automated system that hooks into Blender's context and handles path management.

Whenever you want to test your changes:

1. Open your workspace and use **`Blender: Start`** via the command palette (`Ctrl+Shift+P` / `Cmd+Shift+P`) to open a Blender instance connected to VSCode.
2. Focus your editor on `main.py`.
3. Run the command **`Blender: Run Script`**.

### Auto-reload feature

Because Blender keeps its Python interpreter alive in the background, it normally caches imports and ignores text changes made to secondary files.

To solve this, `main.py` features a **`DO NOT TOUCH`** region that automatically unregisters and flushes all modules residing inside the `tools/` folder from Blender's memory before every single run. You can safely create, rename, delete, or modify files inside `tools/`; `main.py` ensures Blender always executes your freshest code.

## Notes

- The autocompletion provided by `fake-bpy-module` is **static**: it helps while writing code, but the script still needs to run inside Blender (via the extension) to be actually tested.
- Remember to activate the venv each time you open a new terminal session if you want to install or check packages manually.