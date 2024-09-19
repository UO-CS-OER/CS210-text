"""Extract directory tree from path, in form compatible with Treemap project.
Example for "Recursive Data" chapter of Introduction to Computer Science open text.

Students are _not_ required or expected to be familiar with the Python functions
for manipulating files, directories, and paths, but should be able to grasp how
this program builds a recursive (nested) structure of dictionaries to represent
the directory (folder) structure.

"""
import json
import os

import logging
logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

# Recursive type for nested dict representation of directory containing
# file sizes at the leaves.
FileSizes = int | dict[str, 'FileSizes']

def sizes(path: str) -> FileSizes:
    """Represent nesting by recursive dictionaries"""
    log.debug(f"Exploring {path}")
    if os.path.isfile(path):
        # The base case ...
        size = os.path.getsize(path)
        log.debug(f"getsize returned {size}")
        return size
    elif os.path.isdir(path):
        # The recursive case ...
        # a directory that may contain other files and directories
        log.debug("Directory")
        contents = {}  # Build a directory representing sizes of enclosed files and directories
        # List them in sorted order
        for item in sorted(os.listdir(path)):
            name = os.path.basename(item)  # Just the last part of the path
            contents[name] = sizes(os.path.join(path, item))
        log.debug(f"Directory represented as {contents}")
        return contents
    else:
        # "Hidden" files may be identified as neither files nor directories
        # Unclear how or whether to represent them ... we'll treat them as empty
        log.warning(f"Neither isfile nor isdir for {path}")
        return 0

def main(root=None):
    """Print JSON representation of directory tree"""
    if root is None:
        root = os.getcwd()
    tree = sizes(root)
    as_json = json.dumps(tree,indent=4)
    print(as_json)

if __name__ == "__main__":
    main()



