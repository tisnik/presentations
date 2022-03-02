import pygtk

pygtk.require("2.0")
import gtk


window = gtk.Window(gtk.WINDOW_TOPLEVEL)

label = gtk.Label("Hello world!")
window.add(label)
label.show()

window.show()
gtk.main()
