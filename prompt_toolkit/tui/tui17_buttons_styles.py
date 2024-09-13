#!/usr/bin/env python

from prompt_toolkit import Application
from prompt_toolkit.application.current import get_app
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.key_binding.bindings.focus import focus_next, focus_previous
from prompt_toolkit.layout import HSplit, Layout, VSplit
from prompt_toolkit.styles import Style
from prompt_toolkit.widgets import *


def button1_clicked():
    text_area.text += "Button 1 clicked\n"


def button2_clicked():
    text_area.text += "Button 2 clicked\n"


def button3_clicked():
    text_area.text += "Button 3 clicked\n"


def exit_clicked():
    get_app().exit()


button1 = Button("Button 1", handler=button1_clicked)
button2 = Button("Button 2", handler=button2_clicked)
button3 = Button("Button 3", handler=button3_clicked)
button4 = Button("Exit", handler=exit_clicked)

buttons = HSplit([button1, button2, button3, button4])

text_area = TextArea(focusable=False)

# správce rozvržení
root = VSplit(
    [
        Box(Frame(buttons, style="class:button_panel"), padding=2),
        Box(Frame(text_area, title="Events", style="class:edit_panel"), padding=2),
    ]
)

layout = Layout(root)

# napojení na klávesové zkratky
key_bindings = KeyBindings()
key_bindings.add("up")(focus_previous)
key_bindings.add("down")(focus_next)

style = Style(
    [
        ("button_panel", "bg:#ansiblue #ansiwhite"),
        ("edit_panel", "bg:#ansigreen #000000"),
        ("button", "#ansibrightyellow"),
        ("button focused", "bg:#ff0000"),
        ("text-area focused", "bg:#ff0000"),
    ]
)


@key_bindings.add("escape")
def on_escape_press(event):
    """Callback funkce volaná při stisku klávesy Esc."""
    print("\n\n[escape]\n\n")
    event.app.exit()


def main():
    # vytvoření aplikace s textovým uživatelským rozhraním
    application = Application(
        layout=layout, key_bindings=key_bindings, full_screen=True, style=style
    )

    # spuštění aplikace
    application.run()


if __name__ == "__main__":
    main()
