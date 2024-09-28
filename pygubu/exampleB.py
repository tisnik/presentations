"""Pygubu and Tkinter: text entry and validators."""

# Example11.py

import tkinter as tk
from tkinter import messagebox, ttk

import pygubu


class Example11App(pygubu.TkApplication):
    """Class representing a Tkinter based application."""

    def _create_ui(self):
        """Construct and initializes all UI-related data structures."""
        # step #1: Create a builder
        self.builder = builder = pygubu.Builder()

        # step #2: Load an ui file
        builder.add_from_file("exampleB.ui")

        # step #2B: Specify path to images and other resources
        builder.add_resource_path(".")

        # step #3: Create the mainwindow
        self.mainwindow = builder.get_object("MainWindow", self.master)

        # step #4: Configure callbacks
        builder.connect_callbacks(self)

        # step #5: Set variables
        vars = self.builder.tkvariables
        vars["input_text"].set("")

        root.bind("<Control-q>", lambda event: self.on_quit_button_click())

    def on_quit_button_click(self):
        root.destroy()

    def on_button_display_text_click(self):
        vars = self.builder.tkvariables
        text = vars["input_text"].get()

        messagebox.askokcancel("Text entered by user:", text)

    def validate_input_text(self, value):
        if value.isdigit():
            return True
        elif value is "":
            return True
        else:
            return False


if __name__ == "__main__":
    # needed to have a menu
    root = tk.Tk()

    # style
    style = ttk.Style()

    # run the application
    app = Example11App(root)
    app.run()
