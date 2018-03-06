#!/usr/bin/tclsh

puts "Argument count: $argc"

puts "Argument list:"
set i 0

foreach arg $argv {
    incr i
    puts "$i ... $arg"
}

