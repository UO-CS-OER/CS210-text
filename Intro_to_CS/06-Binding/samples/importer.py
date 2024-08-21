"""Demonstration of referencing qualified names
from another module.
"""

import exporter

print(exporter.step(10))
exporter.STEP_SIZE = 20
print(exporter.step(10))