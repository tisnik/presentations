#!/usr/bin/env python

from prompt_toolkit import Application
from prompt_toolkit.layout import Layout, HSplit, VSplit
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.key_binding.bindings.focus import focus_next, focus_previous
from prompt_toolkit.application.current import get_app
from prompt_toolkit.widgets import *


def exit_clicked():
    get_app().exit()


def print_checkbox_status(checkbox, n):
    checked = "checked" if checkbox.checked else "unchecked"
    msg = "Checkbox {n} {s}\n".format(n=n, s=checked)
    text_area.text += msg


def print_hr():
    text_area.text += "-" * 40
    text_area.text += "\n"


def show_status():
    print_checkbox_status(checkbox1, 1)
    print_checkbox_status(checkbox2, 2)
    print_checkbox_status(checkbox3, 3)
    print_hr()


checkbox1 = Checkbox("Checkbox 1")
checkbox2 = Checkbox("Checkbox 2")
checkbox3 = Checkbox("Checkbox 3")
hl = HorizontalLine()
button1 = Button("Show status", handler=show_status)
button2 = Button("Exit", handler=exit_clicked)

buttons = HSplit([checkbox1, checkbox2, checkbox3, hl, button1, hl, button2])

text_area = TextArea(focusable=False)

# správce rozvržení
root = VSplit(
    [
        Box(Frame(buttons, style="bg:#ansiblue #ansiwhite"), padding=2),
        Box(Frame(text_area, title="Events"), padding=2),
    ]
)

layout = Layout(root)

# napojení na klávesové zkratky
key_bindings = KeyBindings()
key_bindings.add("up")(focus_previous)
key_bindings.add("down")(focus_next)


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
