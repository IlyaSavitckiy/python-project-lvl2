"""Engine of function to generate diff between 2 files."""


from gendiff.compare import is_extensions_correct, is_extensions_same
from gendiff.output_formats.plate import generate_diff


def run(first_file, second_file):
    """Take 2 files from cli and print a diff between them.

    Args:
        first_file: some file
        second_file: some file
    """
    if not is_extensions_same(first_file, second_file):
        print('Sorry, we can compare only files with the same extension')
        return
    if not is_extensions_correct(first_file):
        print('Sorry, we can work only with JSON extension')
        return
    print(generate_diff(first_file, second_file))
