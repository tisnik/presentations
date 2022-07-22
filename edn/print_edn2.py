#!/usr/bin/env python3

# Converts structured data from EDN format into JSON format.

import sys
import edn_format

from edn_format import tag, TaggedElement


@tag("user")
class User(TaggedElement):
    def __init__(self, value):
        print("This is user:", value)
        self.value = value


@tag("complex")
class Complex(TaggedElement):
    def __init__(self, value):
        print("This is complex number:", value)


# Check if command line argument is specified (it is mandatory).
if len(sys.argv) < 2:
    print("Usage:")
    print("  print_edn.py input_file.edn")
    print("Example:")
    print("  print_edn.py report.edn")
    sys.exit(1)

# First command line argument should contain name of input EDN file.
filename = sys.argv[1]


# Try to open the EDN file specified.
with open(filename, "r") as edn_input:
    # open the EDN file and parse it
    payload = edn_format.loads(edn_input.read())
    print(payload)
