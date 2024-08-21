"""This module is designed to be imported by importer.py.
Its "symbols"  (names of functions and variables) will be
visible as attributes of the module.
"""

STEP_SIZE = 5

def step(i: int) -> int:
    return i + STEP_SIZE

