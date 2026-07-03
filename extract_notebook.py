import json
import os
import sys

def summarize_notebook(filepath):
    print(f"\n{'='*50}\nSummarizing: {filepath}\n{'='*50}")
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        
        for i, cell in enumerate(nb.get('cells', [])):
            cell_type = cell.get('cell_type', 'unknown')
            source = "".join(cell.get('source', []))
            
            if cell_type == 'markdown':
                if source.strip():
                    print(f"--- [Markdown Cell] ---\n{source.strip()}\n")
            elif cell_type == 'code':
                if source.strip():
                    # Just print first 2 lines of code to keep it short but informative
                    lines = source.strip().split('\n')
                    code_snippet = '\n'.join(lines[:3])
                    if len(lines) > 3: code_snippet += '\n...'
                    print(f"--- [Code Cell] ---\n{code_snippet}\n")
    except Exception as e:
        print(f"Error reading {filepath}: {e}")

tasks = [
    r"c:\Users\Vivek Chaurasiya\OneDrive\Desktop\decodelabs_tasks\DecodeLabs Drive Task\Decodelabs_DriveTask.ipynb",
    r"c:\Users\Vivek Chaurasiya\OneDrive\Desktop\decodelabs_tasks\DecodeLabs Task 1\Decodelabs_Task1.ipynb",
    r"c:\Users\Vivek Chaurasiya\OneDrive\Desktop\decodelabs_tasks\DecodeLabs Task 2\Decodelabs_Task2.ipynb",
    r"c:\Users\Vivek Chaurasiya\OneDrive\Desktop\decodelabs_tasks\DecodeLabs Task 3\Decodelabs_Task3.ipynb"
]

for task in tasks:
    summarize_notebook(task)
