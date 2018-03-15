proc test1 {varname} {
    set varname [expr 1+2]
}

test1 p1
puts $p1

















proc test2 {varname} {
    upvar #0 $varname p
    set p [expr 1+2]
}

test2 p2
puts $p2






proc test3 {varname} {
    global $varname
    set $varname [expr 1+2]
}

test2 p2
puts $p2




proc setvar {varname value} {
     set $varname $value
}

setvar xxx yyy
yyy
puts $xxx
can't read "xxx": no such variable

proc setvar {varname value} {
    upvar 1 $varname p
    set p $value
}

setvar xxx yyy
yyy
puts $xxx
yyy

