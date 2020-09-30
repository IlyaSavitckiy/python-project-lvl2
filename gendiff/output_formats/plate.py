"""Function comparing 2 files and making diff in a plate JSON-like format."""


from gendiff.compare import transform_file


def find_nonmodified(key, dict1, dict2):
    """Find if values of key in dict1 and dict2 are the same.

    Args:
        key: key to look for
        dict1: some dictionary
        dict2: some dictionary

    Returns:
        nonmodified data in str format
    """
    value1 = dict1.get(key)
    value2 = dict2.get(key)
    if value1 == value2:
        return '   {0}: {1}\n'.format(key, value1)


def find_deleted(key, dict1, dict2):
    """Find if key from dict1 not in dict2.

    Args:
        key: key to look for
        dict1: some dictionary
        dict2: some dictionary

    Returns:
        deleted data in str format
    """
    if key not in dict2:
        return ' - {0}: {1}\n'.format(key, dict1.get(key))


def find_new(key, dict1, dict2):
    """Find if key from dict2 not in dict1.

    Args:
        key: key to look for
        dict1: some dictionary
        dict2: some dictionary

    Returns:
        new data in str format
    """
    if key not in dict1:
        return ' + {0}: {1}\n'.format(key, dict2.get(key))


def find_modified(key, dict1, dict2):
    """Find if value of key is modified.

    Args:
        key: key to look for
        dict1: some dictionary
        dict2: some dictionary

    Returns:
        datas before and after modifying in str format
    """
    value1 = dict1.get(key)
    value2 = dict2.get(key)
    if value1 and value2 and value1 != value2:
        return ' - {0}: {1}\n + {2}: {3}\n'.format(key, value1, key, value2)


def generate_diff(first_file, second_file):
    """Take 2 files, compare them and build a diff in a JSON-like format.

    Args:
        first_file: some file
        second_file: some file

    Returns:
        diff of 2 files in a JSON-like format
    """
    file1 = transform_file(first_file)
    file2 = transform_file(second_file)
    list_of_diffs = list(filter(
        lambda it: it, map(
            lambda key: find_nonmodified(key, file1, file2), file1.keys(),
        ),
    ))
    list_of_diffs += list(filter(
        lambda it: it, map(
            lambda key: find_deleted(key, file1, file2), file1.keys(),
        ),
    ))
    list_of_diffs += list(filter(
        lambda it: it, map(
            lambda key: find_new(key, file1, file2), file2.keys(),
        ),
    ))
    list_of_diffs += list(filter(
        lambda it: it, map(
            lambda key: find_modified(key, file1, file2), file1.keys(),
        ),
    ))
    return ''.join(['{\n'] + list_of_diffs + ['}'])
