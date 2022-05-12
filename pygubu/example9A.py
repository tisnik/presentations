"""Pygubu and Tkinter: using check boxes."""

# Example9A.py

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pygubu


class Example9App(pygubu.TkApplication):
    """Class representing a Tkinter based application."""

    def _create_ui(self):
        """Construct and initializes all UI-related data structures."""
        # step #1: Create a builder
        self.builder = builder = pygubu.Builder()

        # step #2: Load an ui file
        builder.add_from_file("example9.ui")

        # step #2B: Specify path to images and other resources
        builder.add_resource_path(".")

        # step #3: Create the mainwindow
        self.mainwindow = builder.get_object("MainWindow", self.master)

        # step #4: Configure callbacks
        builder.connect_callbacks(self)

        root.bind("<Control-q>", lambda event: self.on_quit_button_click())

    def on_quit_button_click(self):
        root.destroy()

    def on_button_display_selections_click(self):
        vars = self.builder.tkvariables

        message = (
            "Checkbutton A: {}\n"
            "Checkbutton B: {}\n"
            "Checkbutton C: {}\n".format(
                vars["checkbutton_a"].get(),
                vars["checkbutton_b"].get(),
                vars["checkbutton_c"].get(),
            )
        )
        messagebox.askokcancel("Selections", message)


if __name__ == "__main__":
    # needed to have a menu
    root = tk.Tk()

    # style
    style = ttk.Style()

    # run the application
    app = Example9App(root)
    app.run()
