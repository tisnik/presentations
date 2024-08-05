#!/usr/bin/env python

from wx import (
    CANCEL,
    EVT_BUTTON,
    EVT_CLOSE,
    ICON_QUESTION,
    ID_ANY,
    ID_OK,
    OK,
    App,
    Button,
    Frame,
    MessageDialog,
    Panel,
)


def onButtonPress(event):
    print("Pressed...")


class MainFrame(Frame):
    def __init__(self, parent, id, title):
        # zavolání konstruktoru předka (kompatibilní s Pythonem 2.x)
        super(MainFrame, self).__init__(parent, id, title, size=(320, 240))

        # vytvoření panelu
        panel = Panel(self, ID_ANY)

        # vytvoření tlačítka s jeho vložením do panelu
        x = y = 20
        button = Button(panel, ID_ANY, "Press me", (x, y))
        button.Bind(EVT_BUTTON, onButtonPress)

        # navázání metody na událost EVT_CLOSE
        self.Bind(EVT_CLOSE, self.onClose)

        # zobrazení hlavního okna aplikace
        self.Show(True)

    def onClose(self, event):
        dialog = MessageDialog(
            self, "Close app?", "Confirm Exit", OK | CANCEL | ICON_QUESTION
        )
        result = dialog.ShowModal()
        dialog.Destroy()
        if result == ID_OK:
            self.Destroy()


# vytvoření instance objektu představujícího běžící aplikaci
app = App()

# vytvoření hlavního okna se specifikací jeho vlastností a titulku
# okno se automaticky zobrazí
frame = MainFrame(None, ID_ANY, "wxPython!")

# vstup do smyčky pro čtení a zpracování událostí (event loop)
app.MainLoop()
