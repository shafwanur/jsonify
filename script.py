import os
import json

# Specify the start directory you want to search in
start_directory = "./"

# Output file name as .json
output_file_name = "output"

def root_check(root):
    if len(root) > 3 and root[2] == ".": # remove dotfolders
        return False
    
    return True

# Function to list all folders in a directory
def list_folders(directory):
    folder_list = []
    for root, dirs, files in os.walk(directory):
        if not root_check(root):
            continue
        
        print("root", root)
        print("dirs", dirs)
        print("files", files)
        print()
        # if len(root) > 3 and root[2] == ".": # ignore dotfiles and "dotfolders"
        #     print("ignoring, ", root)
        #     continue

        for dir_name in dirs:
            # if dir
            # print("appending, ", os.path.join(root[2:], dir_name))
            folder_list.append(os.path.join(root[2:], dir_name))

    return folder_list

# Get a list of all folders in the specified directory
folders = list_folders(start_directory)

# Create a JSON representation of the folder list
json_output = json.dumps(folders, indent=4)

# Output the JSON to a file or print it
# You can change the file name as needed
with open(f"{output_file_name}.json", "w") as json_file:
    json_file.write(json_output)

# If you want to print the JSON to the console, you can use this instead:
# print(json_output)
