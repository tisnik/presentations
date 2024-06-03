#!/usr/bin/env python

from wx import App, Frame, Button, ID_ANY


class MainFrame(Frame):
    def __init__(self, parent, id, title):
        # zavolání konstruktoru předka (kompatibilní s Pythonem 2.x)
        super(MainFrame, self).__init__(parent, id, title, size=(320, 240))

        # vytvoření tlačítka s jeho přímým vložením do rámce
        x = y = 20
        button = Button(self, ID_ANY, "Press me", (x, y))

        # zobrazení hlavního okna aplikace
        self.Show(True)


# vytvoření instance objektu představujícího běžící aplikaci
app = App()

# vytvoření hlavního okna se specifikací jeho vlastností a titulku
# okno se automaticky zobrazí
frame = MainFrame(None, ID_ANY, "wxPython!")

# vstup do smyčky pro čtení a zpracování událostí (event loop)
app.MainLoop()
