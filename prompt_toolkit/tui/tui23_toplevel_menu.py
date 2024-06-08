#!/usr/bin/env python

from prompt_toolkit import Application
from prompt_toolkit.layout import Layout, HSplit, VSplit
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.key_binding.bindings.focus import focus_next, focus_previous
from prompt_toolkit.application.current import get_app
from prompt_toolkit.widgets import *


text_area = TextArea(focusable=False)

file_menu = MenuItem("File")
edit_menu = MenuItem("Edit")
format_menu = MenuItem("Format")
view_menu = MenuItem("View")
help_menu = MenuItem("Help")

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
