"""
helpers.py
This module contains helper functions that are used throughout the application.

Functions:
|    insert_newline()
|    remove_whitespace(string)
|    find_string_in_element(string, list_element)
|    convert_to_string(content="")
|    convert_to_json(content="")
|    convert_to_object(dictionary, name="GenericDict")
|    print_content_to_file(file, content)
"""

import json

from collections import namedtuple


# Print a newline
def insert_newline():
    print('\n')


# Remove whitespace
def remove_whitespace(string):
    return string.strip()


# Find a string in a list element and return the element
def find_string_in_element(string, list_element):
    for i in list_element:
        if string in i:
            return i
    return None


# Convert to a string
def convert_to_string(content=""):
    return str(content)


# Convert content to JSON
def convert_to_json(content=""):
    data = json.dumps(content, indent=2, ensure_ascii=False)
    return data


# Convert content to an object
def convert_to_object(dictionary, name='GenericDict'):
    return namedtuple(name, dictionary.keys())(**dictionary)


# Save content to a file
def print_content_to_file(file, content):
    with open(file, "w") as file:
        print(content, file=file)
