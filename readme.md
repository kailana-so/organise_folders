# Folder organisers

*Required*: Define path before running

## 1) new_folder

This script creates a new folder in a given path and/or sorts folders prefixed with numbers and ensures new folders follow the sequence.

````
# Define the base path where folders are to be managed.
path = "./path/to/directory"
````

### Usage:
````
python3 new_folder.py folder_name [sub_directory_name]
````
    folder_name 
        - Required. 
        - Name of the new folder to create.

    sub_directory_name
        - Optional. 
        - The subdirectory under the main path where the folder will be created.

## 2) reindex_folders

This script creates a folders in the path you provided.

````
# Define the base path where folders are to be managed.
path = "./path/to/directory"
````

### Usage:
````
python3 reindex_folders.py
````

## Step up and exec

For both scripts intial step:

1. Make the Script Executable:
   - Open a terminal.
   - Navigate to the directory where you saved this script.
   - Run the command: 
   ````
   chmod +x new_folder.py
   ````
   ````
   chmod +x reindex_folders.py
   ````
    This command makes the script executable.

Note: The scripts are now executabble from within the directory. Should you want to call the scripts from anywhere, go to correscopnding set 2.

2. Place the Script in Your PATH for Easy Access:
   - Use `echo $PATH` in the terminal to view directories in your PATH variable.
   - Move the script to a directory in your PATH, commonly `~/bin` for Linux/macOS users: 
        `mv new_folder.py ~/bin/`
        or
        `mv reindex_folders.py ~/bin/`
   - If `~/bin` isn't in your PATH or you've chosen another directory, add it by appending `export PATH="$HOME/bin:$PATH"` to your `.bashrc`, `.bash_profile`, `.zshrc`, or equivalent.
   - Apply changes: `source ~/.bashrc` (or corresponding file).

3. Once the script is in your PATH and marked as executable, you can run it from any directory by simply typing:
   ````
   python3 new_folder.py
   ````
   ````
   python3 reindex_folders.py
   ````


#### Notes:
- This guide assumes a Unix-like operating system (Linux/macOS). Windows users may need to adjust these instructions based on their environment.
- Ensure you have the necessary permissions to write to the target directory.
