#!/usr/bin/python3
import sys
import os.path
from json_utils import save_to_json_file, load_from_json_file

filename = "add_item.json"
args_list = []

# Check if the file exists
if os.path.exists(filename):
    # If the file is empty, initialize the list to an empty list
    if os.path.getsize(filename) == 0:
        args_list = []
    else:
        # Load the existing list from the file
        args_list = load_from_json_file(filename)

# Append command line arguments to the list
args_list.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(args_list, filename)
