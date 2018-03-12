#!/usr/bin/env python
# vim: set fileencoding=utf-8

import sys

# import modulu pro GUI
from PySide import QtGui


def main():
    for key in QtGui.QStyleFactory.keys():
        print(key)


if __name__ == '__main__':
    main()
