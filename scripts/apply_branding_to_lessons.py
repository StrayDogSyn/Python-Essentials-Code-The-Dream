"""
Apply consistent StrayDog branding to all lesson HTML files.
Adds favicon, watermark class, and footer to all lesson pages.
"""

import os
import re
from pathlib import Path

# Define the branding components
FAVICON_LINE = '    <link rel="icon" type="image/png" href="../assets/brands/favicon-straydog.png">'

FOOTER_HTML = '''
    <footer class="sd-footer">
        <img class="sd-footer-gear" src="../assets/brands/stray-gear.png" alt="StrayDog" aria-hidden="true">
        <div class="sd-credits">
            Enhanced curriculum for the Returned Citizen community by <a href="https://www.straydog-syndications-llc.com/" target="_blank" rel="noopener">StrayDog Syndications LLC</a>
        </div>
        <div class="sd-links">
            <a href="https://github.com/StrayDogSyn/Python-Essentials-Code-The-Dream" target="_blank" rel="noopener" aria-label="View on GitHub">
                <svg class="sd-github" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path></svg>
            </a>
        </div>
    </footer>
'''


def apply_branding_to_file(file_path):
    """Apply branding updates to a single HTML file."""
    print(f"Processing: {file_path.name}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    changes_made = []
    
    # 1. Add favicon if not present
    if 'favicon-straydog.png' not in content:
        # Find the meta description or viewport tag
        meta_pattern = r'(<meta name="description"[^>]*>)'
        if re.search(meta_pattern, content):
            content = re.sub(
                meta_pattern,
                r'\1\n' + FAVICON_LINE,
                content,
                count=1
            )
            changes_made.append("Added favicon")
    
    # 2. Add watermark class to body if not present
    if '<body>' in content and 'class="sd-watermark"' not in content:
        content = content.replace('<body>', '<body class="sd-watermark">')
        changes_made.append("Added watermark class to body")
    
    # 3. Update existing footer or add new footer
    if 'sd-footer' in content:
        # Add footer gear logo if not present
        if 'sd-footer-gear' not in content:
            # Add gear logo after <footer class="sd-footer">
            footer_pattern = r'(<footer class="sd-footer">)\s*(<div class="sd-credits">)'
            if re.search(footer_pattern, content):
                content = re.sub(
                    footer_pattern,
                    r'\1\n        <img class="sd-footer-gear" src="../assets/brands/stray-gear.png" alt="StrayDog" aria-hidden="true">\n        \2',
                    content
                )
                changes_made.append("Added footer gear logo")
        
        # Update footer text
        old_text_pattern = r'Created with care by'
        new_text = 'Enhanced curriculum for the Returned Citizen community by'
        if old_text_pattern in content:
            content = content.replace(old_text_pattern, new_text)
            changes_made.append("Updated footer text")
    else:
        # Add footer before closing </div> and <script> if not present
        # Try multiple patterns
        patterns = [
            r'(</main>\s*</div>)\s*(<script>)',  # Pattern 1: </main></div><script>
            r'(</div>\s*</div>)\s*(<script>)',    # Pattern 2: </div></div><script>
            r'(</section>\s*</main>\s*</div>)\s*(<script>)',  # Pattern 3: </section></main></div><script>
        ]
        
        footer_added = False
        for pattern in patterns:
            if re.search(pattern, content):
                content = re.sub(pattern, r'\1\n' + FOOTER_HTML + r'\n\n    \2', content, count=1)
                changes_made.append("Added footer")
                footer_added = True
                break
        
        if not footer_added:
            # Last resort: add before </body>
            if '</body>' in content and '<footer' not in content:
                content = content.replace('</body>', FOOTER_HTML + '\n</body>')
                changes_made.append("Added footer (before body)")
                footer_added = True
    
    # Only write if changes were made
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ Updated: {', '.join(changes_made)}")
        return True
    else:
        print(f"  • No changes needed")
        return False


def main():
    """Apply branding to all lesson HTML files."""
    script_dir = Path(__file__).parent
    lesson_dir = script_dir.parent / 'lesson-plans'
    
    if not lesson_dir.exists():
        print(f"Error: Lesson directory not found at {lesson_dir}")
        return
    
    lesson_files = sorted(lesson_dir.glob('lesson_week*.html'))
    
    if not lesson_files:
        print("No lesson files found!")
        return
    
    print(f"Found {len(lesson_files)} lesson files\n")
    
    updated_count = 0
    for lesson_file in lesson_files:
        if apply_branding_to_file(lesson_file):
            updated_count += 1
    
    print(f"\n{'='*50}")
    print(f"Complete! Updated {updated_count}/{len(lesson_files)} files")
    print(f"{'='*50}")


if __name__ == '__main__':
    main()
