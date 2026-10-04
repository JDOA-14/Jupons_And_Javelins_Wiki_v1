import os

# Cleaned path with terminal escape characters removed
TARGET_DIR = "/Users/jamesadams/Documents/DnD Player Wiki/DnD Player Wiki/3. Items/Story Items"

def update_item_frontmatter():
    if not os.path.exists(TARGET_DIR):
        print(f"Directory not found: {TARGET_DIR}")
        print("Please check the path and try again.")
        return

    for root, dirs, files in os.walk(TARGET_DIR):
        for file in files:
            if file.endswith(".md"):
                filepath = os.path.join(root, file)
                
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Check if the file has standard frontmatter
                if not content.startswith("---\n"):
                    print(f"Skipping (No frontmatter): {file}")
                    continue

                # Split the file into 3 parts: empty space before the first ---, the yaml, and the body content
                parts = content.split("---\n", 2)
                if len(parts) < 3:
                    print(f"Skipping (Malformed frontmatter): {file}")
                    continue

                yaml_lines = parts[1].splitlines()
                
                # Update the specific keys if they exist
                for i, line in enumerate(yaml_lines):
                    if line.startswith("rarity:"):
                        yaml_lines[i] = "rarity: Artifact"
                    elif line.startswith("story-item:"):
                        yaml_lines[i] = "story-item: true"
                        
                # Reconstruct the file with the updated frontmatter and untouched body
                new_yaml = "\n".join(yaml_lines)
                new_content = f"---\n{new_yaml}\n---\n{parts[2]}"

                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                print(f"Updated: '{file}'")

if __name__ == "__main__":
    print("Starting Story Items update...")
    update_item_frontmatter()
    print("Update complete!")
