import os
import string

# set name of output file
output_file = "output.json" 
ignored_dirs = ["__pycache__", "codebase_jsonify"]
ignored_files = ["README.md", "LICENSE", ".gitignore"]

def clean_file_content(file_content: str): 
    '''
    Clean up a file's content to optimize for GPT input
    Meaning, remove trailing whitespace characters and replace newlines with \n, unter anderem.
    '''
    # chars that are not [a-z], [A-Z] and digits
    special_chars = [c for c in string.printable if not c.isalnum() and not c.isspace()] 

    file_content = file_content.replace('\n', '\\n') # replace newlines with \n
    file_content = " ".join(file_content.split()) # remove multipe whitespaces

    for char in special_chars: 
        v1 = ' ' + char + ' '
        v2 = ' ' + char
        v3 = char + ' '

        file_content = file_content.replace(v1, char) # ex: replace " = " with "="
        file_content = file_content.replace(v2, char) # ex: replace " =" with "="
        file_content = file_content.replace(v3, char) # ex: replace "= " with "="

        return file_content

def check_dir(dir: str): 
    '''
    Check whether a directory should be traversed
    '''
    good = True
    good &= dir not in ignored_dirs # not an ignored dir
    good &= dir[0] != '.' # ignore dotfolders

    return good

def check_file(filename: str): 
    '''
    Check whether a file should be included
    '''
    good = True
    good &= filename not in ignored_files
    good &= filename != output_file # no need to show the file we just created

    return good
