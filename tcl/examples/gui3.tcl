#!/usr/bin/wish
# vytvoření popisků
label .name -text "Name"
label .password -text "Password" -background red
label .role -text "Role" -background blue
# textová vstupní pole
entry .nameEntry -textvariable name
entry .passwordEntry -textvariable password
entry .roleEntry -textvariable role
# použití manažera geometrie
grid .name -row 0 -column 0 -sticky w
grid .password -row 1 -column 0 -sticky w
grid .role -row 2 -column 0 -sticky w
grid .nameEntry -row 0 -column 1 -sticky w
grid .passwordEntry -row 1 -column 1 -sticky w
grid .roleEntry -row 2 -column 1 -sticky w

# vytvoříme plátno
canvas .platno -width 256 -height 256
# vložíme plátno do okna
grid .platno -column 3 -row 0
# na plátnu vytvoříme několik objektů
# se změněnými vlastnostmi
.platno create oval 10 10 100 100 -fill red -outline blue -width 3
.platno create line 0 0 255 255 -width 5
.platno create line 0 255 255 0 -dash 123
.platno create text 150 120 -text "Hello world" -fill white -font "Helvetica 20"

