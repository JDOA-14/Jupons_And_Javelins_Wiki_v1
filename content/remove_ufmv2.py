import os

# Cleaned path with terminal escape characters removed
VAULT_DIR = "/Users/jamesadams/Documents/DnD Player Wiki/DnD Player Wiki"
TARGET_STRING = "_UFMv2"

def remove_suffix_from_names():
    if not os.path.exists(VAULT_DIR):
        print(f"Directory not found: {VAULT_DIR}")
        return

    # topdown=False is critical: it processes deepest files/folders first.
    # This prevents the script from losing track of files when a parent folder is renamed.
    for root, dirs, files in os.walk(VAULT_DIR, topdown=False):
        
        # 1. Rename files
        for file_name in files:
            if TARGET_STRING in file_name:
                old_file_path = os.path.join(root, file_name)
                new_file_name = file_name.replace(TARGET_STRING, "")
                new_file_path = os.path.join(root, new_file_name)
                os.rename(old_file_path, new_file_path)
                print(f"Renamed file: '{file_name}' -> '{new_file_name}'")

        # 2. Rename directories
        for dir_name in dirs:
            if TARGET_STRING in dir_name:
                old_dir_path = os.path.join(root, dir_name)
                new_dir_name = dir_name.replace(TARGET_STRING, "")
                new_dir_path = os.path.join(root, new_dir_name)
                os.rename(old_dir_path, new_dir_path)
                print(f"Renamed folder: '{dir_name}' -> '{new_dir_name}'")

if __name__ == "__main__":
    print("Starting batch rename...")
    remove_suffix_from_names()
    print("Batch rename complete!")
