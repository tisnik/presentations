#!/usr/bin/env python

import math
import sys

# import "jádra" frameworku Qt i modulu pro GUI
from PySide import QtCore, QtGui


# funkce pro vykreslení úsečky zadanou barvou
def drawDashedLine(qPainter, color, x1, y1, x2, y2, pattern, width=0):
    # vytvoření pera a nastavení barvy kreslení
    pen = QtGui.QPen(QtGui.QColor(*color))

    # změna šířky pera
    pen.setWidth(width)

    # změna typu čáry
    pen.setStyle(QtCore.Qt.CustomDashLine)
    pen.setDashPattern(pattern)

    # kreslit se bude právě vytvořeným perem
    qPainter.setPen(pen)

    # vykreslení úsečky
    qPainter.drawLine(x1, y1, x2, y2)


# nový widget bude odvozen od obecného hlavního okna
class MainWindow(QtGui.QMainWindow):

    # rozměry rastrového obrázku
    IMAGE_WIDTH = 320
    IMAGE_HEIGHT = 240

    def __init__(self):
        # zavoláme konstruktor předka
        super(MainWindow, self).__init__()

        self.prepareImage()
        # konfigurace GUI + přidání widgetu do okna
        self.prepareGUI()

    def prepareImage(self):
        # vytvoření instance třídy QImage
        self.image = QtGui.QImage(
            MainWindow.IMAGE_WIDTH, MainWindow.IMAGE_HEIGHT, QtGui.QImage.Format_RGB32
        )

        # vytvoření objektu typu QPainter s předáním
        # reference na "pokreslovaný" objekt
        qp = QtGui.QPainter(self.image)

        # konstanty s n-ticemi představujícími základní barvy
        BLACK = (0, 0, 0)
        BLUE = (0, 0, 255)
        CYAN = (0, 255, 255)
        GREEN = (0, 255, 0)
        YELLOW = (255, 255, 0)
        RED = (255, 0, 0)
        MAGENTA = (255, 0, 255)
        WHITE = (255, 255, 255)

        # Vykreslení čar různým stylem
        drawDashedLine(qp, YELLOW, 10, 10, 160, 10, [1, 1])
        drawDashedLine(qp, YELLOW, 10, 20, 160, 20, [1, 10])
        drawDashedLine(qp, YELLOW, 10, 30, 160, 30, [10, 1])
        drawDashedLine(qp, YELLOW, 10, 40, 160, 40, [10, 10])
        drawDashedLine(qp, YELLOW, 10, 50, 160, 50, [10, 1, 10, 5])
        drawDashedLine(qp, YELLOW, 10, 60, 160, 60, [5, 5])

        qp.setRenderHint(QtGui.QPainter.Antialiasing)

        # Vykreslení čar s různým sklonem
        for i in range(1, 90, 5):
            # převod ze stupňů na radiány
            angle = math.radians(i)
            radius = 150
            # výpočet koncových bodů úseček
            x = radius * math.sin(math.radians(i))
            y = radius * math.cos(math.radians(i))
            # vykreslení jedné úsečky
            drawDashedLine(
                qp,
                WHITE,
                MainWindow.IMAGE_WIDTH - 1,
                0,
                MainWindow.IMAGE_WIDTH - x,
                y,
                [5, 5],
            )

        # vykreslení čar různou šířkou
        for i in range(1, 10):
            drawDashedLine(qp, WHITE, 10 + i * 15, 90, 10 + i * 15, 230, [5, 5], i)

        # vytvoření instance třídy QPixmap z objektu QImage
        self.pixmap = QtGui.QPixmap.fromImage(self.image)

    def prepareGUI(self):
        # velikost okna nezadávejte ručně - špatně se počítá kvůli toolbaru
        # self.resize(256, 300)
        self.setWindowTitle("QPainter")

        # tlačítko Quit
        quitAction = QtGui.QAction(
            QtGui.QIcon("icons/application-exit.png"), "&Quit", self
        )
        quitAction.triggered.connect(self.close)
        quitAction.setStatusTip("Quit the application")
        quitAction.setShortcut("Ctrl+Q")

        # nástrojový pruh
        self.toolbar = self.addToolBar("title")
        self.toolbar.setMovable(False)

        # přidání tlačítka na nástrojový pruh
        self.toolbar.addAction(quitAction)

        # doprostřed okna přidáme návěští s rastrovým obrázkem
        self.addLabelWithPixmap()

        # zobrazení hlavního okna
        self.show()

    def addLabelWithPixmap(self):
        # vytvoření návěští
        label = QtGui.QLabel("test")
        # přiřazení rastrového obrázku k návěští
        label.setPixmap(self.pixmap)
        # vložení návěští do hlavního okna
        self.setCentralWidget(label)

    def run(self, app):
        # zobrazení okna na obrazovce
        self.show()
        # vstup do smyčky událostí (event loop)
        app.exec_()


def main():
    app = QtGui.QApplication(sys.argv)
    MainWindow().run(app)


if __name__ == "__main__":
    main()
