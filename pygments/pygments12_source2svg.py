#!/usr/bin/env python

from sys import argv, exit

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import SvgFormatter

if len(argv) <= 1:
    print("Usage: pygments12_source2svg.py FILENAME > DRAWING.svg")
    exit(1)

with open(argv[1], "r") as fin:
    code = fin.read()
    print(highlight(code, PythonLexer(), SvgFormatter()))
