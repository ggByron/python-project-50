#!/usr/bin/env python3
from gendiff.gendiff import generate_diff
from gendiff.cli import cli


def main():
    first_file, second_file, file_format = cli()
    print(generate_diff(first_file, second_file, file_format))


if __name__ == '__main__':
    main()
