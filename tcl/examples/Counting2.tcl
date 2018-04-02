#!/usr/bin/tclsh

set x 0
while {$x < 10} {
    incr x
    set y 0
    while {$y < 10} {
        incr y
        puts -nonewline [expr $x*$y]\t
    }
    puts ""
}
