#!/usr/bin/env python3
"""
Validate all Jupyter notebooks in the sessions directory.
Checks for JSON syntax errors and reports any issues.
"""

import json
import os
from pathlib import Path

def validate_notebook(notebook_path):
    """
    Validate a Jupyter notebook file.
    
    Args:
        notebook_path: Path to the notebook file
        
    Returns:
        tuple: (is_valid, error_message, cell_count)
    """
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            nb = json.load(f)
            
        # Check basic notebook structure
        if 'cells' not in nb:
            return False, "Missing 'cells' key", 0
            
        if 'metadata' not in nb:
            return False, "Missing 'metadata' key", 0
            
        cell_count = len(nb['cells'])
        return True, None, cell_count
        
    except json.JSONDecodeError as e:
        return False, f"JSON syntax error: {e}", 0
    except Exception as e:
        return False, f"Error: {e}", 0

def main():
    """Main function to validate all notebooks."""
    base_dir = Path(r"c:\Users\EHunt\Repos\Python\CTD\python-essentials-v2\sessions")
    
    print("=" * 80)
    print("JUPYTER NOTEBOOK VALIDATION REPORT")
    print("=" * 80)
    print()
    
    valid_count = 0
    invalid_count = 0
    invalid_notebooks = []
    
    # Find all notebook files
    notebooks = sorted(base_dir.rglob("*.ipynb"))
    
    for notebook_path in notebooks:
        relative_path = notebook_path.relative_to(base_dir.parent.parent)
        is_valid, error_msg, cell_count = validate_notebook(notebook_path)
        
        if is_valid:
            print(f"✅ {relative_path}")
            print(f"   Cells: {cell_count}")
            valid_count += 1
        else:
            print(f"❌ {relative_path}")
            print(f"   Error: {error_msg}")
            invalid_count += 1
            invalid_notebooks.append((str(relative_path), error_msg))
        print()
    
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total notebooks: {valid_count + invalid_count}")
    print(f"Valid: {valid_count}")
    print(f"Invalid: {invalid_count}")
    
    if invalid_notebooks:
        print()
        print("NOTEBOOKS REQUIRING FIXES:")
        for path, error in invalid_notebooks:
            print(f"  - {path}")
            print(f"    {error}")
    
    return invalid_count == 0

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
