#!/usr/bin/python3


import os
import sys
print(sys.executable)


# Define the base path where folders are to be managed.
path = "<PATH>"

# Extract folder name from command line arguments.
try:
    name = sys.argv[1]
except IndexError:
    print("Error: Folder name argument is missing.")
    sys.exit(1)

# Initialize subdirectory name as empty by default.
sub_dir = ""

# Check for the optional subdirectory argument.
if len(sys.argv) == 3:
    # Validate subdirectory name does not contain a path separator to avoid unintended directory traversal.
    if "/" in sys.argv[2]:
        raise ValueError("Invalid subdirectory name - found '/'. Please provide a valid subdirectory name.")
    sub_dir = sys.argv[2]

def new_folder(p, n, s):
    """
    Creates a new folder and reindexes existing folders if necessary.

    Parameters:
    - p (str): The base path where the folder will be created.
    - n (str): The name of the new folder.
    - s (str): The subdirectory under the base path, if any.
    """
    # Retrieve a list of existing directories, filtering out non-prefixed or hidden ones.
    prefixed_dir_list = [item for item in os.listdir(p) if item.startswith("_") and not item.startswith('.')]

    # Sort the list based on the numeric prefix.
    try:
        sorted_prefixed_dir_list = sorted(prefixed_dir_list, key=lambda x: int(x.split("_")[0]))
    except ValueError:
        print("Warning: Some folders could not be sorted due to non-numeric prefixes.")

    # Determine the full path where the new folder will be created.
    full_path = os.path.join(p, s) if s else p

    # Create the folder within the specified path or subdirectory.
    if s:
        print(f"Adding '{s}' to the path")
        os.makedirs(os.path.join(full_path, n), exist_ok=True)
        print(f"Folder created: {os.path.join(full_path, n)}")
    else:
        print(f"A new folder will be created in: {full_path}")

        # Determine the index for the new folder.
        has_new_prefix = "_" in n
        idx = int(n.split("_")[0]) if has_new_prefix else len(sorted_prefixed_dir_list) + 1

        # Construct the new folder name with the correct index.
        new_name = f"{idx}_{n}" if not has_new_prefix else n

        # Create the new folder.
        os.makedirs(os.path.join(full_path, new_name), exist_ok=True)
        print(f"Folder created: {os.path.join(full_path, new_name)}")

    print("Operation completed successfully.")

# Ensure the base path exists.
if not os.path.exists(path):
    print(f"Error: The specified path '{path}' does not exist.")
    sys.exit(1)

# Execute the folder creation and reindexing function.
new_folder(path, name, sub_dir)