import json

from collections import namedtuple


def click_element(element):
    return element.click()


def remove_whitespace(string):
    """Remove leading and trailing whitespace from a string."""
    return string.strip()


def insert_newline():
    """Print a newline."""
    print('\n')


def convert_to_string(content=""):
    """Convert content to a string."""
    return str(content)


def convert_dictionary_to_json(content="", extra_options=None):
    """Convert a dictionary to JSON."""
    data = json.dumps(content, indent=2, ensure_ascii=False, **extra_options)
    return data


def convert_dictionary_to_generic_object(dictionary, name='GenericDict'):
    """Convert a dictionary to a generic object."""
    return namedtuple(name, dictionary.keys())(**dictionary)
