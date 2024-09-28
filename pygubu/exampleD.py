"""Pygubu and Tkinter: changing style."""

# Example13.py

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
        builder.add_from_file("exampleD.ui")

        # step #2B: Specify path to images and other resources
        builder.add_resource_path(".")

        # step #3: Create the mainwindow
        self.mainwindow = builder.get_object("MainWindow", self.master)

        # step #4: Configure callbacks
        builder.connect_callbacks(self)

        root.bind("<Control-q>", lambda event: self.on_quit_button_click())
        root.bind("<Control-d>", lambda event: self.on_draw_button_click())

    def on_quit_button_click(self):
        root.destroy()

    def on_draw_button_click(self):
        canvas = self.builder.get_object("canvas")

        width = canvas.winfo_width()
        height = canvas.winfo_height()
        grid_size = 30

        # draw something onto canvas
        for x in range(0, width, grid_size):
            canvas.create_line(x, 0, x, height, dash=7, fill="gray")
        for y in range(0, height, grid_size):
            canvas.create_line(0, y, width, y, dash=7, fill="gray")

        canvas.create_line(0, 0, 100, 100, fill="red", width=2, dash=8)

        canvas.create_arc(
            100,
            1,
            200,
            100,
            outline="blue",
            start=45,
            extent=180,
            style=tk.ARC,
            width=2,
        )

        canvas.create_oval(200, 1, 300, 100)

        canvas.create_oval(325, 25, 375, 75, fill="#a0a0ff")

        canvas.create_rectangle(50, 125, 150, 175, fill="#a0a0ff")

        canvas.create_text(300, 150, text="Hello world!", font="Helvetica 20")

        canvas.create_polygon(50, 205, 200, 280, 50, 355, fill="#80ff80")

        canvas.create_polygon(
            230, 205, 370, 280, 230, 355, fill="black", outline="red", width="5"
        )


if __name__ == "__main__":
    # needed to have a menu
    root = tk.Tk()

    # style
    style = ttk.Style()

    # run the application
    app = Example12App(root)
    app.run()
