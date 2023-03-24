#!/bin/python
import re
import sys
import os
import shutil

def dict_to_attr_access(code_string):
    """Replace dictionary accesses with attribute accesses in a string of Python code"""

    # Use regex to find all dictionary accesses in the code
    pattern = r'(\w+)\[(\'|")(\w+)(\'|")\]'
    matches = re.findall(pattern, code_string)

    # Replace each dictionary access with an attribute access
    for match in matches:
        old_access = match[0] + '[' + match[1] + match[2] + match[3] + ']'
        new_access = match[0] + '.' + match[2]
        code_string = code_string.replace(old_access, new_access)

    return code_string


# Get the path to the code file, selection start and end positions
if len(sys.argv) != 6:
    print("Usage: python dict_to_access.py <file_path> <start_line> <start_col> <end_line> <end_col>")
    sys.exit(1)

file_path = sys.argv[1]
try:
    selection_start_line = int(sys.argv[2])
    selection_start_column = int(sys.argv[3])
    selection_end_line = int(sys.argv[4])
    selection_end_column = int(sys.argv[5])
except ValueError:
    print("Invalid argument type. Line and column arguments must be integers.")
    sys.exit(1)

# Read the contents of the code file
with open(file_path, 'r') as f:
    code = f.read()

# Split the code into lines and get the selected lines
lines = code.split('\n')
selected_lines = lines[selection_start_line-1 : selection_end_line]

# Get the non selected text within the first and last selected lines
first_line_text = selected_lines[0][:selection_start_column-1]
last_line_text = selected_lines[-1][selection_end_column:]

# Remove the old selected text and replace it with the modified code
selected_text = '\n'.join(selected_lines)
selected_text = selected_text.replace(first_line_text, '')
selected_text = selected_text.replace(last_line_text, '')
modified_text = dict_to_attr_access(selected_text)

if modified_text == selected_text:
    print("No changes made.")
    sys.exit(0)

# Create a backup of the original file
backup_path = file_path + ".bak"
shutil.copy2(file_path, backup_path)

# Construct the modified code and write it back to the file
modified_lines = modified_text.split('\n')
modified_lines[0] = first_line_text + modified_lines[0]
modified_lines[-1] = modified_lines[-1] + last_line_text
modified_text = '\n'.join(lines[:selection_start_line-1] + modified_lines + lines[selection_end_line:])

with open(file_path, 'w') as f:
    f.write(modified_text)


