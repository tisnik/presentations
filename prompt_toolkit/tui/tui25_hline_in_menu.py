#!/usr/bin/env python

from prompt_toolkit import Application
from prompt_toolkit.layout import Layout, HSplit, VSplit
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.key_binding.bindings.focus import focus_next, focus_previous
from prompt_toolkit.application.current import get_app
from prompt_toolkit.widgets import *


def message(msg):
    text_area.text += msg + "\n"


def on_new_selected():
    message("'New' menu item selected")


def on_open_selected():
    message("'Open' menu item selected")


def on_save_selected():
    message("'Save' menu item selected")


def on_exit_selected():
    get_app().exit()


text_area = TextArea(focusable=False)

file_menu = MenuItem(
    "File",
    children=[
        MenuItem("New", handler=on_new_selected),
        MenuItem("Open", handler=on_open_selected),
        MenuItem("Save", handler=on_save_selected),
        MenuItem("-", disabled=True),
        MenuItem("Exit", handler=on_exit_selected),
    ],
)

edit_menu = MenuItem(
    "Edit",
    children=[
        MenuItem("Cut"),
        MenuItem("Copy"),
        MenuItem("Paste"),
        MenuItem("-", disabled=True),
        MenuItem("Select all"),
    ],
)

format_menu = MenuItem("Format", children=[MenuItem("Word wrap")])

view_menu = MenuItem(
    "View", children=[MenuItem("Status bar"), MenuItem("Line numbers")]
)

help_menu = MenuItem(
    "Help",
    children=[MenuItem("Content"), MenuItem("-", disabled=True), MenuItem("About")],
)

main_menu = [file_menu, edit_menu, format_menu, view_menu, help_menu]

menu = MenuContainer(text_area, menu_items=main_menu)


layout = Layout(menu)

# napojení na klávesové zkratky
key_bindings = KeyBindings()
key_bindings.add("s-tab")(focus_previous)
key_bindings.add("tab")(focus_next)


@key_bindings.add("escape")
def on_escape_press(event):
    """Callback funkce volaná při stisku klávesy Esc."""
    print("\n\n[escape]\n\n")
    event.app.exit()


def main():
    # vytvoření aplikace s textovým uživatelským rozhraním
    application = Application(
        layout=layout, key_bindings=key_bindings, full_screen=True
    )

    # spuštění aplikace
    application.run()


if __name__ == "__main__":
    main()
