#!/usr/bin/env python3
"""
Fix JSON syntax errors in Jupyter notebooks.
"""

import json
import re
from pathlib import Path

def fix_week1_session1():
    """Fix the missing comma in week1/session1 notebook."""
    file_path = Path(r"c:\Users\EHunt\Repos\Python\CTD\python-essentials-v2\sessions\week1\session1_intro_to_python.ipynb")
    
    print(f"Fixing {file_path.name}...")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix the missing },  before line 186
    # The pattern is:   ]
    #   { (should be   ]
    # },
    #   {)
    content = content.replace(
        '   ]\n  {\n   "cell_type": "markdown",\n   "metadata": {},\n   "source": [\n    "**Activity:** Create two variables',
        '   ]\n  },\n  {\n   "cell_type": "markdown",\n   "metadata": {},\n   "source": [\n    "**Activity:** Create two variables'
    )
    
    # Validate the fix
    try:
        json.loads(content)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Fixed {file_path.name}")
        return True
    except json.JSONDecodeError as e:
        print(f"❌ Still has errors in {file_path.name}: {e}")
        return False

def fix_week5_session2():
    """Fix the extra data in week5/session2 notebook."""
    file_path = Path(r"c:\Users\EHunt\Repos\Python\CTD\python-essentials-v2\sessions\week5\session2_data_cleaning_validation_group.ipynb")
    
    print(f"Fixing {file_path.name}...")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find where valid JSON ends
    try:
        # Try to find the end of valid JSON
        decoder = json.JSONDecoder()
        obj, idx = decoder.raw_decode(content)
        
        # If there's extra content, remove it
        if idx < len(content):
            extra = content[idx:].strip()
            if extra:
                print(f"   Removing {len(extra)} extra characters after JSON")
                content = content[:idx]
                
                # Pretty print the JSON
                with open(file_path, 'w', encoding='utf-8', newline='\n') as f:
                    json.dump(obj, f, indent=1, ensure_ascii=False)
                print(f"✅ Fixed {file_path.name}")
                return True
        else:
            print(f"✅ No extra data found in {file_path.name}")
            return True
            
    except json.JSONDecodeError as e:
        print(f"❌ Could not fix {file_path.name}: {e}")
        return False

def main():
    """Main function."""
    print("=" * 80)
    print("FIXING JUPYTER NOTEBOOK JSON ERRORS")
    print("=" * 80)
    print()
    
    success1 = fix_week1_session1()
    print()
    success2 = fix_week5_session2()
    
    print()
    print("=" * 80)
    if success1 and success2:
        print("✅ All notebooks fixed successfully!")
        return True
    else:
        print("❌ Some notebooks still have errors")
        return False

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
