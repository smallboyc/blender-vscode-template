# Blender + VSCode Starter Template

This repo is a **starter template** for developing Blender scripts and add-ons directly from VSCode, instead of using Blender's built-in text editor.

## Why this template?

Coding in Blender's text editor works, but it's limited: no real autocompletion, no linting, no proper project management. This template sets up an environment that gives you:

- **Autocompletion** and type checking on `bpy` and other Blender modules
- The ability to talk **from VSCode to Blender** using dedicated commands, without leaving your editor
- A clean, isolated Python environment (venv)

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
- Choose the interpreter located in `.venv`

### 6. Configure workspace settings

If the `.vscode` folder doesn't exist yet at the root of the project, create it, then add (or create) the `.vscode/settings.json` file with:

```json
{
  "python.analysis.diagnosticSeverityOverrides": {
    "reportMissingModuleSource": "none"
  }
}
```

This disables a cosmetic Pylance warning related to the `bpy` stubs (the module has no real source code).

## Usage

Once the environment is set up, two main commands let you interact with Blender from VSCode via the command palette (`Ctrl+Shift+P` / `Cmd+Shift+P`):

- **`Blender: Start`** — launches a Blender instance connected to VSCode
- **`Blender: Run Script`** — runs the current script directly inside the open Blender instance

This lets you iterate quickly on your code without manually copy-pasting into Blender's text editor.

## Project structure

```
.
├── .vscode/
│   └── settings.json
├── env/
├── .gitignore
├── main.py
├── requirements.txt
└── README.md
```

## Notes

- The autocompletion provided by `fake-bpy-module` is **static**: it helps while writing code, but the script still needs to run inside Blender (via the extension) to be actually tested.
- Remember to activate the venv each time you open a new terminal session if you want to install or check packages manually.