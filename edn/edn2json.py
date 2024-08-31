#!/usr/bin/env python3

# Converts structured data from EDN format into JSON format.

import json
import sys

import edn_format

# Check if command line argument is specified (it is mandatory).
if len(sys.argv) < 2:
    print("Usage:")
    print("  edn2json.py input_file.edn")
    print("Example:")
    print("  edn2json.py report.edn")
    sys.exit(1)

# First command line argument should contain name of input EDN file.
filename = sys.argv[1]


# Taken from https://github.com/swaroopch/edn_format/issues/76#issuecomment-749618312
def edn_to_map(x):
    if isinstance(x, edn_format.ImmutableDict):
        return {edn_to_map(k): edn_to_map(v) for k, v in x.items()}
    elif isinstance(x, edn_format.ImmutableList):
        return [edn_to_map(v) for v in x]
    elif isinstance(x, edn_format.Keyword):
        return x.name
    else:
        return x


# Try to open the EDN file specified.
with open(filename, "r") as edn_input:
    # open the EDN file and parse it
    payload = edn_format.loads(edn_input.read())
    print(json.dumps(edn_to_map(payload), indent=2))
