#!/usr/bin/env python

from prompt_toolkit import Application
from prompt_toolkit.application.current import get_app
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.key_binding.bindings.focus import focus_next, focus_previous
from prompt_toolkit.layout import HSplit, Layout, VSplit
from prompt_toolkit.widgets import *

# napojení na klávesové zkratky
key_bindings = KeyBindings()
key_bindings.add("s-tab")(focus_previous)
key_bindings.add("tab")(focus_next)


def message(msg):
    text_area.text += msg + "\n"


@key_bindings.add("c-n")
def on_new_selected(event=None):
    message("'New' menu item selected")


@key_bindings.add("c-o")
def on_open_selected(event=None):
    message("'Open' menu item selected")


@key_bindings.add("c-s")
def on_save_selected(event=None):
    message("'Save' menu item selected")


@key_bindings.add("c-x")
def on_exit_selected(event=None):
    get_app().exit()


text_area = TextArea(focusable=False)

main_menu = [
    MenuItem(
        "File",
        children=[
            MenuItem("New   <Ctrl-N>", handler=on_new_selected),
            MenuItem("Open  <Ctrl-O>", handler=on_open_selected),
            MenuItem("Save  <Ctrl-S>", handler=on_save_selected),
            MenuItem("-", disabled=True),
            MenuItem("Exit  <Ctrl-X>", handler=on_exit_selected),
        ],
    ),
    MenuItem(
        "Edit",
        children=[
            MenuItem("Cut"),
            MenuItem("Copy"),
            MenuItem("Paste"),
            MenuItem("-", disabled=True),
            MenuItem("Select all"),
        ],
    ),
    MenuItem("Format", children=[MenuItem("Word wrap")]),
    MenuItem(
        "View",
        children=[
            MenuItem(
                "Status bar", children=[MenuItem("Enabled"), MenuItem("Disabled")]
            ),
            MenuItem("Line numbers", children=[MenuItem("Yes"), MenuItem("No")]),
        ],
    ),
    MenuItem(
        "Help",
        children=[MenuItem("Content"), MenuItem("-", disabled=True), MenuItem("About")],
    ),
]

menu = MenuContainer(text_area, menu_items=main_menu)

layout = Layout(menu)


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
