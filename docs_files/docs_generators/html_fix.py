import os
import shutil
import glob

def replace_links() -> None:

    # Replace references to _static/ with the complete URL in all HTML files
    # and remove underscores from filenames
    docs_dir = os.path.abspath('../docs') if os.getcwd().endswith('docs_files') else os.path.abspath('docs')
    
    print("Replacing references to _static/ with the complete URL and removing underscores...")
    
    # Base URL for static files - using GitHub Pages instead of raw.githubusercontent.com
    static_base_url = "https://niccolokadera.github.io/AI_evaluator/docs/static/"
    
    # Find all HTML files in the docs directory
    html_files = glob.glob(os.path.join(docs_dir, '**/*.html'), recursive=True)
    
    # Dictionary to keep track of files that need their underscores removed
    underscore_files = {}
    
    # Map of file references with underscores to versions without underscores
    for html_file in html_files:
        print(f"Processing file: {html_file}")
        
        # Read file content
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # First replace _static/ with the base URL
        content = content.replace('href="_static/', f'href="{static_base_url}')
        content = content.replace('src="_static/', f'src="{static_base_url}')
        content = content.replace('url(_static/', f'url({static_base_url}')
        
        # Now find all references to files with underscores in the URL
        import re
        
        # Pattern for finding URLs that contain underscores in the filename part
        url_patterns = [
            # href=".../_filename.ext"
            r'href="([^"]*?/)?_([^/"]+)"', 
            # src=".../_filename.ext"
            r'src="([^"]*?/)?_([^/"]+)"',
            # url(.../_filename.ext)
            r'url\(([^)]*?/)?_([^/)]+)\)'
        ]
        
        for pattern in url_patterns:
            # Find all matches
            matches = re.findall(pattern, content)
            for match in matches:
                path_prefix = match[0] if match[0] else ''
                filename = match[1]
                
                # Create the old and new references
                old_ref = f'{path_prefix}_' + filename
                new_ref = f'{path_prefix}' + filename
                
                print(f"  - Replacing underscore in URL: {old_ref} -> {new_ref}")
                
                # Store the mapping
                underscore_files[old_ref] = new_ref
        
        # Apply all the replacements for underscored filenames
        for old_ref, new_ref in underscore_files.items():
            content = content.replace(f'"{old_ref}"', f'"{new_ref}"')
            content = content.replace(f'({old_ref})', f'({new_ref})')
        
        # Write the modified content to the file
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
    
    print("Replacement completed.")
    
    # # Also rename the actual files/folders if they exist
    # static_dir = os.path.join(docs_dir, 'static')
    # if os.path.exists(static_dir) and os.path.isdir(static_dir):
    #     print("Renaming files in static directory to remove underscores...")
        
    #     for root, dirs, files in os.walk(static_dir):
    #         # Process files
    #         for f in files:
    #             if f.startswith('_'):
    #                 old_file_path = os.path.join(root, f)
    #                 new_file_name = f[1:]  # Remove leading underscore
    #                 new_file_path = os.path.join(root, new_file_name)
                    
    #                 if os.path.exists(new_file_path):
    #                     os.remove(new_file_path)  # Remove existing file if any
                    
    #                 shutil.move(old_file_path, new_file_path)
    #                 print(f"  - Renamed file: {old_file_path} -> {new_file_path}")
            
    #         # Process directories (collect them first to avoid modifying during iteration)
    #         dirs_to_rename = []
    #         for d in dirs:
    #             if d.startswith('_'):
    #                 old_dir_path = os.path.join(root, d)
    #                 new_dir_name = d[1:]  # Remove leading underscore
    #                 new_dir_path = os.path.join(root, new_dir_name)
    #                 dirs_to_rename.append((old_dir_path, new_dir_path))
            
    #         # Now rename the collected directories
    #         for old_dir, new_dir in dirs_to_rename:
    #             if os.path.exists(new_dir):
    #                 shutil.rmtree(new_dir)  # Remove existing directory if any
                
    #             shutil.move(old_dir, new_dir)
    #             print(f"  - Renamed directory: {old_dir} -> {new_dir}")
    
    # print("All underscores removed from static file references and actual files.")


def moove_html_files() -> None:

    # Paths
    docs_dir = os.path.abspath('../docs')
    html_dir = os.path.join(docs_dir, 'html')
    
    # Check that both directories exist
    if os.path.exists(html_dir) and os.path.isdir(html_dir):
        print("Moving files from docs/html to docs...")
        
        # Copy all files and directories from /docs/html to /docs
        # and remove leading underscores from file and folder names
        for item in os.listdir(html_dir):
            src = os.path.join(html_dir, item)
            
            # Remove leading underscore from the item name if present
            dest_item = item
            if item.startswith('_'):
                dest_item = item[1:]
                print(f"Renaming: {item} -> {dest_item}")
            
            dst = os.path.join(docs_dir, dest_item)
            
            if os.path.isdir(src):
                if os.path.exists(dst):
                    shutil.rmtree(dst)
                
                # For directories, we need to copy the structure but rename files with leading underscores
                shutil.copytree(src, dst)
                
                # Check for files with leading underscores inside the directory
                for root, dirs, files in os.walk(dst):
                    # Process directories first
                    dirs_to_rename = []
                    for d in dirs:
                        if d.startswith('_'):
                            old_dir_path = os.path.join(root, d)
                            new_dir_name = d[1:]
                            new_dir_path = os.path.join(root, new_dir_name)
                            dirs_to_rename.append((old_dir_path, new_dir_path))
                    
                    # Rename directories (outside the loop to avoid affecting the walk)
                    for old_dir, new_dir in dirs_to_rename:
                        if os.path.exists(new_dir):
                            shutil.rmtree(new_dir)
                        shutil.move(old_dir, new_dir)
                        print(f"Renamed directory: {old_dir} -> {new_dir}")
                    
                    # Process files
                    for f in files:
                        if f.startswith('_'):
                            old_file_path = os.path.join(root, f)
                            new_file_name = f[1:]
                            new_file_path = os.path.join(root, new_file_name)
                            if os.path.exists(new_file_path):
                                os.remove(new_file_path)
                            shutil.move(old_file_path, new_file_path)
                            print(f"Renamed file: {old_file_path} -> {new_file_path}")
            else:
                # For individual files
                if os.path.exists(dst):
                    os.remove(dst)
                shutil.copy2(src, dst)
        
        # Remove the html directory after transfer
        shutil.rmtree(html_dir)
        print("Files moved successfully and leading underscores removed.")