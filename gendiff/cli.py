import argparse


def cli():
    parser = argparse.ArgumentParser(
        usage='%(prog)s [options] [format] <filepath1> <filepath2>',
        description='Compares two configuration'
        'files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')

    parser.add_argument(
        '-f',
        '--format',
        choices=['stylish', 'plain', 'json'],
        help='set format of output',
        default='stylish'
    )
    args = parser.parse_args()

    return args.first_file, args.second_file, args.format