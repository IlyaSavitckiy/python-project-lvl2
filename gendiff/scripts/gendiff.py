"""Module."""

import argparse


def main():
    """Generate main function."""
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args()


if __name__ == '__main__':
    main()