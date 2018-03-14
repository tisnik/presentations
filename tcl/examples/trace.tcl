trace add ...
trace info ...
trace remove ...
trace variable ...
trace vdelete ...
trace vinfo ...
















trace add execution ...
trace add command ...
trace add variable ...










trace add variable x write tisk_write_x

proc tisk_write_x args {
    global x
    puts "zapis hodnoty $x do promenne x"
}



















trace remove variable x write tisk_write_x



















proc tisk_write_x args {
    puts "zapis hodnoty $x do promenne x"
}



















proc tisk_write_x args {
    #puts "zapis hodnoty $x do promenne x"
    foreach arg $args {
        puts "tisk_write_x: $arg"
    }
}

















trace remove variable x write tisk_write_x

















proc tisk_write_x args {
    global x
    puts "zapis hodnoty $x do promenne x"
}
















trace info variable x













proc test_proc {x y} { return [expr $x+$y]}
trace add execution test_proc enter test_proc_enter
trace add execution test_proc leave test_proc_leave

proc test_proc_enter args { puts "test_proc enter" }
proc test_proc_leave args { puts "test_proc leave" }

proc test_proc_enter args {
    foreach arg $args {
        puts "test_proc_enter: $arg"
    }
}

proc test_proc_leave args {
    foreach arg $args {
        puts "test_proc_leave: $arg"
    }
}

trace info execution test_proc




