#!/usr/bin/wish
button .prvni -text "First button" -command {exit}
button .druhy -text "Second button" -command {exit}
button .treti -text "Third button" -command {exit}
button .ctvrty -text "Fourth button" -command {exit}
grid .prvni -column 1 -row 1
grid .druhy -column 3 -row 1
grid .treti -column 1 -row 2
grid .ctvrty -column 4 -row 2

