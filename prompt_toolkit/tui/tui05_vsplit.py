#!/usr/bin/env python

from prompt_toolkit import HTML, Application
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout import Layout, VSplit
from prompt_toolkit.layout.containers import Window
from prompt_toolkit.layout.controls import FormattedTextControl

# naformátované zprávy
message1 = HTML("<ansired>Hello</ansired>")
message2 = HTML("<ansiblue>world!</ansiblue>")
message3 = HTML("<ansiyellow>(Esc to quit)</ansiyellow>")

# ovládací prvky s naformátovaným textem
text1 = FormattedTextControl(text=message1)
text2 = FormattedTextControl(text=message2)
text3 = FormattedTextControl(text=message3)

# okna obsahující jediný ovládací prvek
window1 = Window(content=text1)
window2 = Window(content=text2)
window3 = Window(content=text3)

# správce rozvržení
vsplit = VSplit([window1, window2, window3])
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
