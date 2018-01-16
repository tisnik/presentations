#!/usr/bin/tclsh

set glob_x 1

proc test1 {} {puts $glob_x}
proc test2 {} {global glob_x; puts $glob_x}
proc test3 {} {global glob_x; set glob_x 2}
proc test4 {} {set glob_x 3}

puts "$glob_x"
#test1
test2
test3
puts "$glob_x"
test4
puts "$glob_x"

