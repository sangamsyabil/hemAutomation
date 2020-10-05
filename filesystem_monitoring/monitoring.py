"""
A watchdog is a little piece of software that monitors our filesystem looking for any changes (like the creation,
change or deletion of a file or of a directory). When a change occurs, the watchdog report it to us raising a
specific event that we can handle.

For example, let’s suppose you have developed a program that use a configuration file.
Your program could set a watchdog to monitor that file and if the configuration file is modified you could
think to reload it and apply the new configuration at runtime, without the need of restarting your program.

Concept/Code: Hem Raj Regmi (sangamsyabil@gmail.com)
github repository: https://github.com/sangamsyabil/hemAutomation

Happy coding !!!
"""

import argparse
import os
import time
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


def current_time():
    now = datetime.now()
    return now.strftime("%m/%d/%Y, %H:%M:%S")


def on_created(event):
    print(">> [{}] {} has been created!".format(current_time(), event.src_path))


def on_deleted(event):
    print(">> [{}] Please watch out! Someone deleted {}!".format(current_time(), event.src_path))


def on_modified(event):
    print(">> [{}] {} has been modified".format(current_time(), event.src_path))


def on_moved(event):
    print(">> [{}] Someone moved {} to {}".format(current_time(), event.src_path, event.dest_path))


def parse_arguments():
    parser = argparse.ArgumentParser(description='Filesystem check using watchdog')
    parser.add_argument('--path', type=dir_path, default=os.path.join(default_path),
                        help="Provide full path, if not specified it will take 'downloadFiles' as default")
    return parser.parse_args()


def dir_path(path):
    if os.path.isdir(path):
        return path
    else:
        raise argparse.ArgumentTypeError(f"readable_dir:{path} is not a valid path")


def main(args):
    patterns = "*"
    ignore_patterns = ""
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

    my_event_handler.on_created = on_created
    my_event_handler.on_deleted = on_deleted
    my_event_handler.on_modified = on_modified
    my_event_handler.on_moved = on_moved

    go_recursively = True
    my_observer = Observer()
    my_observer.schedule(my_event_handler, args.path, recursive=go_recursively)

    my_observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()


if __name__ == "__main__":
    default_path = "/Users/hemrajregmi/PycharmProjects/random_for_test"
    arsed_args = parse_arguments()
    main(arsed_args)
