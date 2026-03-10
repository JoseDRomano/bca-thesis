import os

def delete_files_by_extension(extensions):
    # Get the directory where the script is currently running
    current_dir = os.getcwd()
    
    print(f"Cleaning up files in: {current_dir}")
    
    # Ensure extensions start with a dot
    ext_list = [ext if ext.startswith('.') else f'.{ext}' for ext in extensions]
    
    deleted_count = 0
    
    for filename in os.listdir(current_dir):
        # Check if the file ends with any of the specified extensions
        if any(filename.lower().endswith(ext.lower()) for ext in ext_list):
            file_path = os.path.join(current_dir, filename)
            
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    print(f"Deleted: {filename}")
                    deleted_count += 1
            except Exception as e:
                print(f"Error deleting {filename}: {e}")

    print(f"--- Cleanup complete. {deleted_count} files removed. ---")

if __name__ == "__main__":
    target_extensions = ['acn', 'acr', 'alg', 'aux', 'bbl', 'bcf', 'glg','glo','gls','ist','lof', 'slg','slo','sls','toc']
    
    # Safety confirmation
    confirm = input(f"Delete all {target_extensions} files in {os.getcwd()}? (y/n): ")
    if confirm.lower() == 'y':
        delete_files_by_extension(target_extensions)
    else:
        print("Operation cancelled.")