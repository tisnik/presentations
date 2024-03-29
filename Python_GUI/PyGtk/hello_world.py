
#
#  (C) Copyright Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

import pygtk

pygtk.require("2.0")
import gtk


def delete_event(widget, event, data=None):
    print "delete event occurred"
    return False


def destroy(widget, data=None):
    print "destroy signal occurred"
    gtk.main_quit()


window = gtk.Window(gtk.WINDOW_TOPLEVEL)
window.connect("delete_event", delete_event)
window.connect("destroy", destroy)

label = gtk.Label("Hello world!")
window.add(label)
label.show()

window.show()
gtk.main()
