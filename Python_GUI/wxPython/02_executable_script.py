#!/usr/bin/env python

from wx import App, Frame, ID_ANY

# vytvoření instance objektu představujícího běžící aplikaci
app = App()

# vytvoření hlavního okna se specifikací jeho vlastností a titulku
frame = Frame(None, ID_ANY, "wxPython!")

# zobrazení hlavního okna aplikace
frame.Show(True)

# vstup do smyčky pro čtení a zpracování událostí (event loop)
app.MainLoop()
