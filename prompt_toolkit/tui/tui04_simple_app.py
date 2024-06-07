#!/usr/bin/env python

from prompt_toolkit import Application, HTML
from prompt_toolkit.layout.containers import Window
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.key_binding import KeyBindings


# naformátovaná zpráva
message = HTML("<ansired>Hello</ansired> <ansiblue>world!</ansiblue>")

# ovládací prvek s naformátovaným textem
text = FormattedTextControl(text=message)

# okno obsahující jediný ovládací prvek
window = Window(content=text)

# správce rozvržení
layout = Layout(window)

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
