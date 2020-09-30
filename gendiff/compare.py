"""Functions to work with files."""


import json


def read_json(path_to_file):
    """Open a file with json extension and read it.

    Args:
        path_to_file: path to file with json extension

    Returns:
        data from file with json extension
    """
    with open(path_to_file) as open_file:
        return json.load(open_file)


extensions = {
    'json': read_json,
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


def is_extensions_same(first_file, second_file):
    """Take 2 files and compare if their extentions are the same.

    Args:
        first_file: some_file with pass in str format
        second_file: some_file with pass in str format

    Returns:
        boolean, true if extensions are the same and false if not
    """
    return get_extension(first_file) == get_extension(second_file)


def is_extensions_correct(path_to_file):
    """Take a file a check if file's extension correct for working with.

    Args:
        path_to_file: some file with pass in str format

    Returns:
        boolean, true if extension is correct
    """
    file_extension = get_extension(path_to_file)
    return file_extension in extensions


def transform_file(path_to_file):
    """Take file and transform it in python dictionary based on file's extension.

    Args:
        path_to_file: some file

    Returns:
        dictionary with data from file
    """
    extension = get_extension(path_to_file)
    return extensions[extension](path_to_file)
