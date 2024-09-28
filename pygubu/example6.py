"""Pygubu and Tkinter: changing style."""

# Example6.py

import tkinter as tk
from tkinter import ttk

import pygubu


class Example6App(pygubu.TkApplication):
    """Class representing a Tkinter based application."""

    def _create_ui(self):
        """Construct and initializes all UI-related data structures."""
        # step #1: Create a builder
        self.builder = builder = pygubu.Builder()

        # step #2: Load an ui file
        builder.add_from_file("example6.ui")

        # step #2B: Specify path to images and other resources
        builder.add_resource_path(".")

        # step #3: Create the mainwindow
        self.mainwindow = builder.get_object("MainWindow", self.master)

        # step #4: Configure callbacks
        builder.connect_callbacks(self)

        root.bind("<Control-q>", lambda event: self.on_button_exit_click())

    def on_button_clam_click(self):
        style.theme_use("clam")

    def on_button_alt_click(self):
        style.theme_use("alt")

    def on_button_default_click(self):
        style.theme_use("default")

    def on_button_classic_click(self):
        style.theme_use("classic")

    def on_button_exit_click(self):
        root.destroy()


if __name__ == "__main__":
    # needed to have a menu
    root = tk.Tk()

    # style
    style = ttk.Style()

    # run the application
    app = Example6App(root)
    app.run()
