#!/usr/bin/env python

from prompt_toolkit import Application, HTML
from prompt_toolkit.layout.containers import Window
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.layout import Layout, HSplit, VSplit
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.widgets import *


# naformátovaná zpráva
message = HTML("<ansired>Hello</ansired> <ansiblue>world!</ansiblue>")

# widget
widget = Label(message)

# struktura obrazovky
root = Box(Frame(widget))

# správce rozvržení
layout = Layout(container=root)

# napojení na klávesové zkratky
key_bindings = KeyBindings()


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
