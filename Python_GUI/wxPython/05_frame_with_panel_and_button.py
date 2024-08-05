#!/usr/bin/env python

from wx import ID_ANY, App, Button, Frame, Panel


class MainFrame(Frame):
    def __init__(self, parent, id, title):
        # zavolání konstruktoru předka (kompatibilní s Pythonem 2.x)
        super(MainFrame, self).__init__(parent, id, title, size=(320, 240))

        # vytvoření panelu
        panel = Panel(self, ID_ANY)

        # vytvoření tlačítka s jeho vložením do panelu
        x = y = 20
        button = Button(panel, ID_ANY, "Press me", (x, y))

        # zobrazení hlavního okna aplikace
        self.Show(True)


# vytvoření instance objektu představujícího běžící aplikaci
app = App()

# vytvoření hlavního okna se specifikací jeho vlastností a titulku
# okno se automaticky zobrazí
frame = MainFrame(None, ID_ANY, "wxPython!")

# vstup do smyčky pro čtení a zpracování událostí (event loop)
app.MainLoop()
