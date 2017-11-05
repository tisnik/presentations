#!/usr/bin/env python

from appJar import gui
import tkinter


image_data = """
R0lGODlhFgAWAPZJAAAAAHgCAYcHBYgZGZUJA5cRCpsYEpkkFpkrJKQLBKgYBaQQELQCArEYGKQo
Fq4yFrUlBrAoE7g5F6g0J6Y2NqlMO6lJRrVLRLpSSLZaWbxpacg1B9U7BMwpKMw5ONQnJ9w4OMlH
FttDBtFOFudJBPNPAPdTAMFbTsZmV8J3d+FiYut9fauCebGHfqyLhK6cnLaMhL+Si7ynp8mIiMaW
j86Skt+KitGZmcSsq92trd6yrd+ysuuIh+6oqOS7reW3svKqqurDtM7OztjY2OTMyujT0/DExOjo
6Pj4+P///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5
BAEAAEkALAAAAAAWABYAAAf+gEmCg4SFg0hIgz0rIB+Oj5AdjypANoI8Rjs5mzs7Pz2boZw9HoId
N6ipqquoOQ2CDDOyLy81sreztTM3C7CyOEdHMriyMsE4MzW9SQwpKURIR0gyzs7G0UQpM8sMGt5F
wUc43sbB2RozBoIJGe0aRMFFOMDmGu0pBevt+/BHQ/9DiOzTkIKAoAUUKFS4gAEDEYABUZyoMIFA
AYNJFhAQQEBBBAkuILaAoCDBxgICDm7sCIEFRCFCWJAkQMBAyiQGaCZQ0CLYEB8+YA4ZqaDmzZwd
Y4QLQoKEj39HYkBIcOAoTRpLSZQwUSLIkGA0FDgIIOgATR/RgojQypVEEGlMP8SSRXLgogIfQTZw
WNuUA4cgcQk4SInEQl0FECDoFbFWBIcNG0gqmDDXQgUHDyRICBFihOcRnDU/mICAbJIBAVKrXs16
taHXsAUFAgA7
"""

app = gui()


def onMenuItemSelect(menuItem):
    if menuItem == "Quit":
        app.stop()


app.setSticky("news")

fileMenu = ["Quit"]
app.addMenuList("File", fileMenu, onMenuItemSelect)

app.addLabel("label", "Image loaded from data (string)")
app.addImageData("image", image_data)

app.go()
