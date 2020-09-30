#!/usr/bin/env python3
"""Main script to get a diff between 2 files."""


import argparse

from gendiff.engine import run


def main():
    """Start script."""
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    run(args.first_file, args.second_file)


if __name__ == '__main__':
    main()
