import os
import re
import sys
import yaml

SKILLS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'ai-workforce'))

def validate_skill(file_path):
    print(f"Validating {os.path.relpath(file_path, SKILLS_DIR)}...")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract YAML frontmatter
    match = re.match(r'^---\r?\n(.*?)\r?\n---\r?\n(.*)', content, re.DOTALL)
    if not match:
        print("Error: Missing or invalid YAML frontmatter delimiters ('---') at start.")
        return False
    
    frontmatter_str = match.group(1)
    
    try:
        data = yaml.safe_load(frontmatter_str)
    except Exception as e:
        print(f"Error: Failed to parse YAML frontmatter: {e}")
        return False
    
    if not isinstance(data, dict):
        print("Error: Frontmatter is not a key-value dictionary.")
        return False
    
    # Check required fields
    if 'name' not in data:
        print("Error: Missing required 'name' field in frontmatter.")
        return False
    
    name = data['name']
    if not re.match(r'^[a-z0-9\-]+$', name):
        print(f"Error: Skill name '{name}' must be kebab-case (lowercase, digits, and hyphens only).")
        return False
        
    if 'description' not in data:
        print("Error: Missing required 'description' field in frontmatter.")
        return False
        
    desc = data['description']
    if len(desc) > 1024:
        print(f"Error: Description exceeds 1024 characters ({len(desc)} characters).")
        return False
        
    if '<' in desc or '>' in desc:
        print("Error: Description must not contain XML brackets ('<' or '>').")
        return False
        
    print("Success: Validated successfully.")
    return True

def main():
    success = True
    for root, dirs, files in os.walk(SKILLS_DIR):
        for file in files:
            if file == 'SKILL.md':
                full_path = os.path.join(root, file)
                if not validate_skill(full_path):
                    success = False
                    print("-" * 40)
                    
    if not success:
        sys.exit(1)
    else:
        print("All skills validated successfully.")

if __name__ == '__main__':
    main()
