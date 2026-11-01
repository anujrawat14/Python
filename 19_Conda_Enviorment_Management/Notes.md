# Conda — Notes

## 1. What is Conda?

Conda is an open-source package and environment manager.

It helps us:
- Create isolated environments.
- Install and manage packages.
- Manage different Python versions.
- Avoid dependency conflicts between projects.
- Reproduce project environments on another computer.

## 2. What is Anaconda?

Anaconda is a Python distribution that includes Conda and many commonly used data-science packages.

**Remember:**
- Anaconda = Python distribution.
- Conda = Environment and package manager.

## 3. What is an Environment?

An environment is an isolated workspace containing:
- A Python interpreter.
- Installed packages.
- Their dependencies.

Example:

```cmd
conda create --name py310 python=3.10
```

This creates an environment named `py310` with Python 3.10.

## 4. What is the Base Environment?

`base` is Conda's default environment.

Important points:
- It is created during Conda installation.
- It contains Conda and its default packages.
- Avoid installing every project dependency into base.
- Create separate environments for different projects.

## 5. Environment Isolation

Different projects may require different Python versions or package versions.

Example:

| Environment | Python | Purpose |
|---|---|---|
| base | 3.14.6 | Conda base |
| py310 | 3.10.22 | Python 3.10 practice |

Each environment maintains its own packages.

## 6. Conda Package Management

Conda can install packages and manage their dependencies.

Example:

```cmd
conda install numpy pandas seaborn
```

To check installed packages:

```cmd
conda list
```

Conda can also use pip:

```cmd
python -m pip install requests
```

Use pip inside the currently activated Conda environment when a package is unavailable through Conda.

## 7. Environment Configuration

### environment.yml

A YAML file that describes a Conda environment.

It can contain:
- Environment name.
- Python version.
- Conda dependencies.
- Pip dependencies.

Export:

```cmd
conda env export > environment.yml
```

Recreate:

```cmd
conda env create -f environment.yml
```

This helps reproduce the environment on another computer.

## 8. Conda vs pip

| Conda | pip |
|---|---|
| Environment manager | Package installer |
| Installs packages | Installs Python packages |
| Can manage non-Python dependencies | Primarily manages Python packages |
| Can manage Python versions | Does not manage Python versions |

## 9. Conda vs venv

| Conda | venv |
|---|---|
| Separate installation | Built into Python |
| Manages environments and packages | Manages environments |
| Can manage non-Python dependencies | Python packages only |
| Useful for data science | Useful for general Python projects |

## 10. Important Best Practices

1. Keep the base environment clean.
2. Create separate environments for projects.
3. Select the correct Python interpreter in VS Code.
4. Export dependencies before sharing a project.
5. Avoid mixing Conda and pip unnecessarily.
6. Check the active environment before installing packages.

## 11. My Current Conda Setup

**Installation path:**

```text
C:\Users\anujr\anaconda3
```

**Base Python:** 3.14.6

**Created environment:** `py310`

**Environment path:**

```text
C:\Users\anujr\anaconda3\envs\py310
```

**Python version:** 3.10.22

**Installed package:** Seaborn

## 12. Remember

- `conda` manages environments and packages.
- `base` is the default environment.
- `conda activate` switches environments.
- `conda deactivate` exits the active environment.
- `conda list` displays installed packages.
- `environment.yml` helps reproduce an environment.
- - don't use pip with conda