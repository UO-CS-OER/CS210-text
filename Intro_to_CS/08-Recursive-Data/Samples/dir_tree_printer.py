"""Recursive data structure example:  Print a directory tree"""

import os

def print_directory_tree(path: str, level: int):
    """Represent nesting by indentation"""
    name = os.path.basename(path)  # Just the last part of the path
    if os.path.isfile(path):
        # The base case ...
        # no recursive call
        print(f"{leader(level)}{name}")
    elif os.path.isdir(path):
        # The recursive case ...
        # a directory that may contain other files and directories
        print(f"{leader(level)}{name}")
        for content in os.listdir(path):
            print_directory_tree(os.path.join(path, content), level + 1)
    else:
        # "Hidden" files may be identified as neither files nor directories
        print(f"{leader(level)}[Hidden: {name}]")

def leader(level: int) -> str:
    """A leader in typography is a series of characters
    that are used as a visual aid to connect items on a page.
    [per Wikipedia]
    """
    if level == 0:
        return ""
    return "|   " * (level - 1) + "|–– "

# Print directory (folder) tree from current working directory
print_directory_tree(os.getcwd(), level=0)

"""Example output
foo
|–– bar
|   |–– baz
|–– foobar
"""