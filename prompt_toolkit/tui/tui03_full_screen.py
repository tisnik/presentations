#!/usr/bin/env python

from prompt_toolkit import Application


def main():
    # vytvoření aplikace s textovým uživatelským rozhraním
    application = Application(full_screen=True)

    # spuštění aplikace
    application.run()


if __name__ == "__main__":
    main()
