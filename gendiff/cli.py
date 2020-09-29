"""Cli for programm."""


import argparse
def cli():
    """Takes 2 files from cl, parse and return them

    Returns:
        2 parsed files
    """
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    return args.first_file, args.second_file
