# Jupyter Notebook in VS Code

## 1. What is Jupyter Notebook?
- Jupyter Notebook is an interactive environment for writing and executing Python code.
- It allows us to execute code in small blocks called **Cells**.
- We can see the output immediately without running the entire file.
- Mainly used for experimentation, data analysis, visualization and Machine Learning.

## 2. What is `.ipynb`?
- `.ipynb` stands for **IPython Notebook**.
- It is the file extension used by Jupyter Notebook.
- It stores:
  - Python code
  - Markdown text and notes
  - Execution outputs
  - Notebook metadata

## 3. Steps to Work with Jupyter in VS Code

1. Install the **Python** and **Jupyter** extensions in VS Code.
2. Open your Python working folder.
3. Press `Ctrl + Shift + P`.
4. Search for `Create: New Jupyter Notebook`.
5. Save the file with `.ipynb` extension.
6. Select the Python interpreter/kernel.
7. Create Code or Markdown cells.
8. Write Python code inside Code cells.
9. Execute cells using `Shift + Enter`.
10. Check the output and fix errors if required.
11. Save the notebook using `Ctrl + S`.

## 4. Types of Cells

### Code Cell
- Used to write and execute Python code.

```python
name = "Anuj"
print(name)
```

### Markdown Cell
- Used to write headings, notes and explanations.
- Supports Markdown formatting.

```markdown
# Python Basics
Learning Jupyter Notebook.
```

## 5. Important Terms

| Term | Meaning |
|---|---|
| Notebook | `.ipynb` file |
| Cell | Individual block of code or text |
| Kernel | Executes Python code and maintains variables in memory |
| Run All | Executes all cells |
| Restart Kernel | Restarts the execution environment and clears variables |
| Clear Outputs | Removes displayed outputs |

## 6. Important Keyboard Shortcuts

| Shortcut | Function |
|---|---|
| `Shift + Enter` | Run cell and move to next |
| `Ctrl + Enter` | Run current cell |
| `Alt + Enter` | Run cell and insert below |
| `A` | Insert cell above (Command Mode) |
| `B` | Insert cell below (Command Mode) |
| `M` | Convert to Markdown |
| `Y` | Convert to Code |
| `D, D` | Delete selected cell |
| `Ctrl + S` | Save notebook |

## 7. Important Points
- Variables remain available between cells while the same kernel is running.
- Cells can execute independently, but execution order matters.
- Restarting the kernel clears variables stored in memory.
- Use `.py` for normal Python development and `.ipynb` for interactive experimentation.

## Workflow

Start  
↓  
Open VS Code  
↓  
Open Python Folder  
↓  
Create `.ipynb` Notebook  
↓  
Select Kernel  
↓  
Create Code / Markdown Cells  
↓  
Write Python Code  
↓  
Run Cells  
↓  
Check Output / Fix Errors  
↓  
Save Notebook  
↓  
End