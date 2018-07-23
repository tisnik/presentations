#!/usr/bin/env python
# vim: set fileencoding=utf-8

from prompt_toolkit import Application


def main():
    # vytvoření aplikace s textovým uživatelským rozhraním
    application = Application()

    # spuštění aplikace
    application.run()


if __name__ == '__main__':
    main()
