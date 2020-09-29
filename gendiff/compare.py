"""Functions to work with files."""


import json


extensions = {
    'json': lambda x: json.load(open(x)),
}


def get_extension(file):
    """Take a file and return its extension

    Args:
        file: some file with path in str format

    Returns:
        extension of the file in str format
    """
    extension = ''
    for char in reversed(file):
        if char == '.':
            break
        extension = char + extension
    return extension


def is_extensions_same(first_file, second_file):
    """Take 2 files and compare if their extentions are the same

    Args:
        first_file: some_file with pass in str format
        second_file: some_file with pass in str format

    Returns:
        boolean, true if extensions are the same and false if not
    """
    return get_extension(first_file) == get_extension(second_file)


def is_extensions_correct(file):
    """Take a file a check if file's extension correct for working in compare function.

    Args:
        file: some file with pass in str format

    Returns:
        boolean, true if extension is correct
    """
    file_extension = get_extension(file)
    return file_extension in extensions


def transform_file(file):
    """Take file and transform it in python dictionary based on file's extension

    Args:
        file: some file

    Returns:
        dictionary with data from file
    """
    extension = get_extension(file)
    return extensions[extension](file)
