#!/usr/bin/env python3
import argparse
from gendiff.gendiff import generate_diff
from gendiff.cli import cli


def main():
    first_file, second_file, format = cli()
    print(generate_diff(first_file, second_file, format))


if __name__ == '__main__':
    main()
