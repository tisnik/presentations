#!/usr/bin/tclsh

puts "executing..."
set result [exec ls -1 | wc -l]
puts "result: $result"

