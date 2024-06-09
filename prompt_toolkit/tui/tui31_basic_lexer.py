#!/usr/bin/env python

from pygments import lex
from pygments.token import Token
from pygments.lexers.basic import CbmBasicV2Lexer

from prompt_toolkit import Application
from prompt_toolkit.layout.containers import Window
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.layout import Layout, HSplit, VSplit
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.key_binding.bindings.focus import focus_next, focus_previous
from prompt_toolkit.application.current import get_app
from prompt_toolkit.widgets import *
from prompt_toolkit.lexers import PygmentsLexer


# napojení na klávesové zkratky
key_bindings = KeyBindings()
key_bindings.add("s-tab")(focus_previous)
key_bindings.add("tab")(focus_next)


@key_bindings.add("escape")
def on_exit_selected(event=None):
    """Callback funkce volaná při stisku klávesy Esc."""
    get_app().exit()


@key_bindings.add("f10")
def on_f10_pressed(event=None):
    """Callback funkce volaná při stisku klávesy F10."""
    get_app().layout.focus(menu.window)


lexer = PygmentsLexer(CbmBasicV2Lexer)
text_area = TextArea(focusable=True, multiline=True, wrap_lines=False, lexer=lexer)

file_menu = MenuItem("File", children=[MenuItem("Exit", handler=on_exit_selected)])
menu = MenuContainer(text_area, menu_items=[file_menu])

layout = Layout(menu, focused_element=text_area)


def main():
    # vytvoření aplikace s textovým uživatelským rozhraním
    application = Application(
        layout=layout, key_bindings=key_bindings, full_screen=True
    )

    # spuštění aplikace
    application.run()


if __name__ == "__main__":
    main()
