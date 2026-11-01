# Conda — Commands Cheat Sheet

## 1. Basic Commands

| Command | Description |
|---|---|
| `conda --version` | Check Conda version |
| `conda info` | Display Conda configuration |
| `conda info --envs` | Display environment information |
| `conda list` | List installed packages |
| `conda update conda` | Update Conda |

## 2. Environment Commands

### Create environment

```cmd
conda create --name myenv
```

### Create environment with Python version

```cmd
conda create --name py310 python=3.10
```

### List all environments

```cmd
conda env list
```

Alternative:

```cmd
conda info --envs
```

### Activate environment

```cmd
conda activate py310
```

### Deactivate environment

```cmd
conda deactivate
```

### Remove environment

```cmd
conda env remove --name py310
```

### Rename environment

Conda does not provide a simple direct rename command. Create a replacement environment and remove the old one after checking it.

## 3. Package Management Commands

### Install a package

```cmd
conda install numpy
```

### Install multiple packages

```cmd
conda install numpy pandas seaborn
```

### Install a specific package version

```cmd
conda install numpy=2.0
```

### Update a package

```cmd
conda update numpy
```

### Update all packages

```cmd
conda update --all
```

### Remove a package

```cmd
conda remove numpy
```

### List installed packages

```cmd
conda list
```

### Search for a package

```cmd
conda search seaborn
```

## 4. Environment Export and Import

### Export environment

```cmd
conda env export > environment.yml
```

### Export without build-specific details

```cmd
conda env export --no-builds > environment.yml
```

### Create environment from YAML

```cmd
conda env create -f environment.yml
```

### Update an existing environment

```cmd
conda env update -f environment.yml --prune
```

### Export only explicitly installed packages

```cmd
conda env export --from-history > environment.yml
```

## 5. Python Version Commands

### Check Python version

```cmd
python --version
```

### Check active Python executable

```cmd
python -c "import sys; print(sys.executable)"
```

### Create environment with specific Python version

```cmd
conda create --name py311 python=3.11
```

### Install a different Python version into an environment

```cmd
conda install python=3.11
```

## 6. Useful CMD Commands

| Command | Purpose |
|---|---|
| `where conda` | Find Conda executable |
| `where python` | Find Python executable |
| `cd ..` | Go back one folder |
| `dir` | List files and folders |
| `cls` | Clear terminal |

## 7. My Daily Conda Workflow

```cmd
conda env list

conda activate py310

python --version

conda list

conda install seaborn

conda deactivate
```

## 8. Quick Revision

| Task | Command |
|---|---|
| Version | `conda --version` |
| Create | `conda create --name myenv python=3.10` |
| Activate | `conda activate myenv` |
| Deactivate | `conda deactivate` |
| List environments | `conda env list` |
| Install | `conda install package` |
| Remove package | `conda remove package` |
| Update package | `conda update package` |
| List packages | `conda list` |
| Export | `conda env export > environment.yml` |
| Import | `conda env create -f environment.yml` |
| Delete environment | `conda env remove --name myenv` |