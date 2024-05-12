#!/usr/bin/python3

import os
import sys

# Prints the path of the Python interpreter being used to execute this script
print(sys.executable)

# Define the base path where folders are to be managed
path = "<PATH>"

def reindex_folders(p):
    """
    Reindexes all folders within the specified path by assigning or reassigning
    an index based on their sorted order.

    Parameters:
    - p (str): The path where the folders to be reindexed are located.
    """

    # Retrieve a list of all directories (ignoring files)
    all_dirs = [d for d in os.listdir(p) if os.path.isdir(os.path.join(p, d))]
    
    # Optionally, sort the directories alphabetically before reindexing
    sorted_dirs = sorted(all_dirs)

    # Log the reindexing process
    print("The following folder(s) will be reindexed:")
    for i, dir in enumerate(sorted_dirs, start=1):
        # Construct the new directory name using the new index
        newDir = f"{i}_{dir}"
        # Check if directory already starts with an index
        if dir.split("_")[0].isdigit():
            # Split once on '_' and reconstruct with the new index
            parts = dir.split("_", 1)
            newDir = f"{i}_{parts[1]}"
        print(f"{dir} > {newDir}")
        # Rename the directory to reflect its new index
        os.rename(os.path.join(p, dir), os.path.join(p, newDir))
    print("Reindexing completed.")

# Ensure the base path exists
if not os.path.exists(path):
    print(f"Error: The specified path '{path}' does not exist.")
    sys.exit(1)

# Execute the folder creation and reindexing function
reindex_folders(path)
