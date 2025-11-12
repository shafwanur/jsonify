import os
import json

from os import listdir

from os.path import isfile, isdir

from helpers import output_file, clean_file_content, check_dir, check_file


def recurse(dir: str = "./"):
    _list = []
    for item in listdir(dir):
        path_to_item = os.path.join(dir, item)
        if isfile(path_to_item):
            if not check_file(item):
                continue

            try:
                with open(path_to_item) as f:
                    file_content = f.read()
                    file_content = clean_file_content(file_content)
                    _list.append({f"{item}": file_content})
            except:
                _list.append({f"{item}": "..."})

    for item in listdir(dir):
        path_to_item = os.path.join(dir, item)
        try:
            if isdir(path_to_item):
                if not check_dir(item):
                    continue

                _list.append(recurse(path_to_item))
        except:
            pass

    return {f"{dir}": _list}


data = recurse()

with open(f"{output_file}", "w") as f:
    json.dump(data, f, indent=2)

print(f"JSON file created in {output_file}!")
