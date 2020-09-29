"""Engine of function to generate diff between 2 files."""


from gendiff.output_formats.plate import generate_diff
from gendiff.cli import cli


def run():
    """Take 2 files from cli and print a diff between them."""
    first_file, second_file = cli()
    print(generate_diff(first_file, second_file))
