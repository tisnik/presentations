proc increment {} {
    global x
    incr x
}
trace add variable x write write_x
trace add variable x read read_x
trace add execution increment enter increment_enter
trace add execution increment leave increment_leave
proc write_x args {
    global x
    puts "... write $x to x"
}
proc read_x args {
    global x
    puts "... read $x from x"
}
proc increment_enter args {
    puts "... enter to function increment"
}
proc increment_leave args {
    puts "... leave from function increment"
}
set x 0
while {$x<10} {
    increment
    puts $x
}

