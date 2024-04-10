#!/usr/bin/env python

import sys

# import modulu pro GUI
from PySide import QtGui


def main():
    for key in QtGui.QStyleFactory.keys():
        print(key)


if __name__ == "__main__":
    main()
