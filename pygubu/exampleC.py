"""Pygubu and Tkinter: changing style."""

# Example12.py

import tkinter as tk
from tkinter import messagebox, ttk

import pygubu


class Example12App(pygubu.TkApplication):
    """Class representing a Tkinter based application."""

    def _create_ui(self):
        """Construct and initializes all UI-related data structures."""
        # step #1: Create a builder
        self.builder = builder = pygubu.Builder()

        # step #2: Load an ui file
        builder.add_from_file("exampleC.ui")

        # step #2B: Specify path to images and other resources
        builder.add_resource_path(".")

        # step #3: Create the mainwindow
        self.mainwindow = builder.get_object("MainWindow", self.master)

        # step #4: Configure callbacks
        builder.connect_callbacks(self)

        root.bind("<Control-q>", lambda event: self.on_quit_button_click())

    def on_quit_button_click(self):
        root.destroy()


if __name__ == "__main__":
    # needed to have a menu
    root = tk.Tk()

    # style
    style = ttk.Style()

    # run the application
    app = Example12App(root)
    app.run()
