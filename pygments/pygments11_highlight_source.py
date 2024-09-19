#!/usr/bin/env python

from sys import argv, exit

from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PythonLexer

if len(argv) <= 1:
    print("Usage: pygments11_highlight_source.py FILENAME")
    exit(1)

with open(argv[1], "r") as fin:
    code = fin.read()
    print(highlight(code, PythonLexer(), TerminalFormatter()))
