"""Functions to work with files."""


import json

EXTENSIONS = {  # noqa: WPS407
    'json': json.load,
}


def get_extension(path_to_file):
    """Take a file and return its extension.

    Args:
        path_to_file: some file with path in str format

    Returns:
        extension of the file in str format
    """
    extension = ''
    for char in reversed(path_to_file):
        if char == '.':
            break
        extension = char + extension
    return extension


def read_file(path_to_file):
    """Open a file with json extension and read it.

    Args:
        path_to_file: path to file with json extension

    Returns:
        data from file with json extension
    """
    extension = get_extension(path_to_file)
    with open(path_to_file) as open_file:
        return EXTENSIONS[extension](open_file)
