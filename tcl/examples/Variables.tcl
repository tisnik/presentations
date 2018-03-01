#!/usr/bin/tclsh

puts "Global variables"
puts [info globals]
#puts [info globals "x*"]

set xxx 0
set xxy 0

puts "Global variables after 'set'"
puts [info globals]

unset xxx
unset xxy

puts "Global variables after 'unset'"
puts [info globals]
#puts [info globals "x*"]

