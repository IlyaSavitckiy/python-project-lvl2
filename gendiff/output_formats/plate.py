"""Function comparing 2 files and making diff in a plate JSON-like format"""


from gendiff.compare import is_extensions_correct, is_extensions_same, transform_file, extensions


def generate_diff(first_file, second_file):
    """Take 2 files, compare them and build a diff in a JSON-like format

    Args:
        first_file: some file
        second_file: some file

    Returns:
        diff of 2 files in a JSON-like format
    """
    if not is_extensions_same(first_file, second_file):
        print('Sorry, we can compare only files with the same extension')
        return
    if not is_extensions_correct(first_file):
        print('Sorry, we can work only with JSON extension')
        return
    file1 = transform_file(first_file)
    file2 = transform_file(second_file)
    list_of_diffs = ['{\n', ]
    for key, value in file1.items():
        if key in file2:
            if value == file2[key]:
                list_of_diffs.append('   {key}: {value}\n'.format(key=key, value=value))
            else:
                list_of_diffs.append(' - {key}: {value}\n'.format(key=key, value=value))
                list_of_diffs.append(' + {key}: {value}\n'.format(key=key, value=file2[key]))
        else:
            list_of_diffs.append(' - {key}: {value}\n'.format(key=key, value=value))
    for key, value in file2.items():
        if key not in file1:
            list_of_diffs.append(' + {key}: {value}\n'.format(key=key, value=value))
    list_of_diffs.append('}')
    diff = ''.join(list_of_diffs)
    return diff
