"""
This program manages files and stores into their respective folders.

Concept/Code: Hem Raj Regmi (sangamsyabil@gmail.com)
github repository: https://github.com/sangamsyabil/hemAutomation

Happy coding !!!
"""

import argparse
import os
import shutil

default_location = "/Users/hemrajregmi/PycharmProjects/random_for_test"


def parse_arguments():
    parser = argparse.ArgumentParser(description='Organize any folder with python')
    parser.add_argument('--path', type=dir_path, default=os.path.join(default_location),
                        help="Provide full path to organize, if not specified it will take 'Downloads' as default")

    return parser.parse_args()


def dir_path(path):
    if os.path.isdir(path):
        return path
    else:
        raise argparse.ArgumentTypeError(f"readable_dir:{path} is not a valid path")


def manage_files(args):
    """
    A function to sort the files folder into their respective categories
    """
    os.chdir(args.path)
    all_files = [f for f in os.listdir(args.path) if os.path.isfile(os.path.join(args.path, f))]

    if len(all_files) > 0:
        print("Total new files: " + str(len(all_files)) + ", Optimizing " + str(args.path))
        file_types = []
        file_type_folder = {}

        for file_name in all_files:
            file_ext = file_name.split(".")[1]
            if file_ext not in file_types:
                file_types.append(file_ext)
                new_folder_name = args.path + "/" + file_ext + "_folder"
                file_type_folder[str(file_ext)] = str(new_folder_name)

                if os.path.isdir(new_folder_name):
                    continue
                else:
                    os.mkdir(new_folder_name)

        for file_name in all_files:
            src_path = args.path + "/" + file_name
            file_ext = file_name.split(".")[1]
            if file_ext in file_type_folder.keys():
                dest_path = file_type_folder[str(file_ext)]
                shutil.move(src_path, dest_path)
                print(src_path + " >>> " + dest_path)
        print("Success!")
    else:
        print("No new files to optimized in " + str(args.path))


def main():
    parsed_args = parse_arguments()
    manage_files(parsed_args)


if __name__ == "__main__":
    main()
