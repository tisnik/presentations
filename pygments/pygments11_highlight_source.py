#!/usr/bin/env python

from sys import argv, exit

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import TerminalFormatter

if len(argv) <= 1:
    print("Usage: pygments11_highlight_source.py FILENAME")
    exit(1)

with open(argv[1], "r") as fin:
    code = fin.read()
    print(highlight(code, PythonLexer(), TerminalFormatter()))
