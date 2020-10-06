"""Engine of programm to generate diff between 2 files."""


from gendiff.files import EXTENSIONS, get_extension, read_file
from gendiff.generate_diff import generate_diff
from gendiff.output_formats import jsonlike


def run(first_file, second_file):
    """Take 2 files from cli and print a diff between them.

    Args:
        first_file: some file
        second_file: some file
    """
    first_file_extension = get_extension(first_file)
    second_file_extension = get_extension(second_file)
    if first_file_extension != second_file_extension:
        print('Sorry, we can compare only files with the same extension')
        return
    # we need to check only one extension, because they are the same
    if first_file_extension not in EXTENSIONS:
        print('Sorry, we can work only with JSON extension')
        return
    print(jsonlike.generate_output(
        generate_diff(
            read_file(first_file),
            read_file(second_file),
        ),
    ))
