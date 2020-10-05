"""
Walking through a folder tree and searching for large files or folders.
Printing the files with their absolute path with their size in MB
So that you can review and remove if no longer needed.

Concept/Code: Hem Raj Regmi (sangamsyabil@gmail.com)
github repository: https://github.com/sangamsyabil/hemAutomation

Happy coding !!!
"""

import argparse
import os
import operator
import re
from functools import reduce

from tabulate import tabulate

default_location = "/Users/hemrajregmi/PycharmProjects/"
SCREEN_WIDTH = 80
centered = operator.methodcaller('center', SCREEN_WIDTH)
HEADER = ["File Name", "Size in MB"]


def main(args):
    if args.preview:
        preview_only(args.path)
    else:
        table_data = []
        temp = re.findall(r'\d+', args.display)
        min_file_size = list(map(int, temp))
        if min_file_size:
            for file_name, file_size in search_folder(args.path, min_file_size[0]):
                table_data.append([file_name, file_size / (1024 ** 2)])

            print("\nFiles larger than {} MB in location: {} ... ".format(min_file_size[0], args.path))

        display_result(sort_table(table_data, args.sort))


def sort_table(sub_list, sort):
    value = False if sort == 'asc' else True

    # Key is set to sort using second element of sub list, lambda has been used.
    return sorted(sub_list, reverse=value, key=lambda x: x[1])


def preview_only(location):
    print(centered("-" * int(SCREEN_WIDTH / 2.5) + " Folder Tree " + "-" * int(SCREEN_WIDTH / 2.5)))

    d = {}
    root_dir = location.rstrip(os.sep)
    start = location.rfind(os.sep) + 1
    for path, dirs, files in os.walk(root_dir):
        folders = path[start:].split(os.sep)
        subdir = dict.fromkeys(files)
        parent = reduce(dict.get, folders[:-1], d)
        parent[folders[-1]] = subdir

    pretty_print(d)
    print(centered("-" * SCREEN_WIDTH))


def search_folder(location, min_file_size):
    for path, dirs, files in os.walk(location):
        for file_name in files:
            try:
                size_bytes = os.path.getsize(os.path.join(path, file_name))
                if min_file_size * 1024 ** 2 <= size_bytes:
                    yield os.path.join(path, file_name), size_bytes
            except FileNotFoundError:
                pass


def display_result(contents):
    print(tabulate(contents, headers=HEADER, tablefmt="psql"))


def pretty_print(d, indent=0):
    for key, value in d.items():
        print('\t' * indent + str(key))
        if isinstance(value, dict):
            pretty_print(value, indent + 1)
        else:
            print('\t' * (indent + 1) + str(value))


def parse_arguments():
    sort_order = ['asc', 'dsc']

    parser = argparse.ArgumentParser(description='Walking through a folder tree and searching for a large files')
    parser.add_argument('--path', type=dir_path, default=os.path.join(default_location),
                        help="Provide full path, if not specified it will take 'downloadFiles' as default")
    parser.add_argument('-p', '--preview', type=str2bool, default=False,
                        help="Want to list all folder and file tree? [True, False] or [Yes, No] or [1, 0] or [Y, N]")
    parser.add_argument('-d', '--display', default="larger_than_5",
                        help="Available options: Either just a number or any string combinations. E.g. 20, larger_than_20, larger-than-5-mb etc.")
    parser.add_argument('-s', '--sort', choices=sort_order, default='dsc',
                        help="Sort file according to ascending or descending order [asc / dsc]")
    return parser.parse_args()


def dir_path(path):
    if os.path.isdir(path):
        return path
    else:
        raise argparse.ArgumentTypeError(f"readable_dir:{path} is not a valid path")


def str2bool(value):
    if isinstance(value, bool):
        return value
    if value.lower() in ('yes', 'y', 'true', 't', '1'):
        return True
    elif value.lower() in ('no', 'n', 'false', 'f', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError("Boolean Value Expected [True, False] or [Yes, No] or [1, 0] or [Y, N]")


if __name__ == "__main__":
    arsed_args = parse_arguments()
    main(arsed_args)
