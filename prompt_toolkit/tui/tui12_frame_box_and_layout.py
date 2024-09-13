#!/usr/bin/env python

from prompt_toolkit import HTML, Application
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout import HSplit, Layout, VSplit
from prompt_toolkit.layout.containers import Window
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.widgets import *

# naformátované zprávy
message1 = HTML("<ansibrightred>Hello</ansibrightred>")
message2 = HTML("<ansibrightyellow>world!</ansibrightyellow>")
message3 = HTML("<ansibrightyellow>(Esc to quit)</ansibrightyellow>")

# widgety
widget1 = Label(message1)
widget2 = Label(message2)
widget3 = Label(message3)

# styl rámce
style = "bg:#ansiblue #ansiwhite"

# správce rozvržení
vsplit = HSplit(
    [
        VSplit([Frame(widget1, style=style), Frame(widget2, style=style)]),
        Frame(widget3, style=style),
    ]
)
layout = Layout(vsplit)

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
