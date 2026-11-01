# Python Virtual Environments & Package Management

## 1. What is a virtual environment?

A virtual environment creates an isolated Python environment for a particular project.

- Keeps project dependencies separate.
- Prevents dependency conflicts between projects.
- Avoids installing project packages into the global Python environment.
- Allows different projects to use different package versions.

> A virtual environment isolates Python packages and dependencies. It does not install a separate copy of the Python interpreter itself.

## 2. Complete workflow (Windows CMD)

### Step 1: Create a virtual environment

```cmd
python -m venv .venv
```

- `venv` is Python's built-in module.
- `.venv` is the environment folder name. You can choose another name.

### Step 2: Activate the virtual environment

For Windows CMD:

```cmd
.\.venv\Scripts\activate
```

After activation, the terminal displays `(.venv)` at the beginning of the prompt.

### Step 3: Check installed packages

```cmd
pip list
```

Displays packages installed in the active environment.

### Step 4: Export dependencies to `requirements.txt`

```cmd
pip freeze > requirements.txt
```

Saves installed packages and their exact versions in `requirements.txt`.

Example:

```text
Django==5.2.0
requests==2.32.3
```

### Step 5: Install dependencies from `requirements.txt`

```cmd
pip install -r requirements.txt
```

Installs all packages listed in the file.

### Step 6: Install a package

```cmd
pip install django
```

### Step 7: Uninstall a package

```cmd
pip uninstall django
```

### Step 8: Deactivate the virtual environment

```cmd
deactivate
```

Returns the terminal to its normal, non-virtual-environment state.

## 3. Verify the active Python interpreter

```cmd
where python
```

Or use Python directly:

```cmd
python -c "import sys; print(sys.executable)"
```

When the environment is active, the first Python path should point to:

```text
.venv\Scripts\python.exe
```


## 5. Quick revision

| Command | Purpose |
|---|---|
| `python -m venv .venv` | Create a virtual environment |
| `.\.venv\Scripts\activate` | Activate (Windows CMD) |
| `pip list` | List installed packages |
| `pip freeze` | Show installed packages with versions |
| `pip freeze > requirements.txt` | Export dependencies |
| `pip install django` | Install a package |
| `pip install -r requirements.txt` | Install dependencies from a file |
| `pip uninstall django` | Uninstall a package |
| `deactivate` | Deactivate the environment |
| `where python` | Locate Python executables (Windows CMD) |

## 6. Important difference: `pip list` vs `pip freeze`

- `pip list` displays installed packages in a readable table.
- `pip freeze` produces package requirements in a format suitable for `requirements.txt`, including pinned versions.

## 7. Other terminal activation commands

| Terminal | Activation command |
|---|---|
| Windows CMD | `.\.venv\Scripts\activate` |
| Windows PowerShell | `.\.venv\Scripts\Activate.ps1` |
| Git Bash | `source .venv/Scripts/activate` |

---

**Remember:** Activate the project's virtual environment before installing or running project dependencies. Each project can have its own `.venv` and `requirements.txt`.
