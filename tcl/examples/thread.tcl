package require Thread

set threadTestPart1 {
    set threadId }

set threadTestPart2 {
    set i 10
    while {[incr i -1] >=0} {
        puts "thread $threadId counter $i"
        after 100
    }
    return $threadId }

set threadTestA $threadTestPart1"A"$threadTestPart2
set threadTestB $threadTestPart1"B"$threadTestPart2
set threadTestC $threadTestPart1"C"$threadTestPart2

puts $threadTestA
puts $threadTestB
puts $threadTestC

set ta [thread::create]
set tb [thread::create]
set tc [thread::create]

thread::send -async $ta $threadTestA threadFinish
thread::send -async $tb $threadTestB threadFinish
thread::send -async $tc $threadTestC threadFinish

vwait threadFinish
vwait threadFinish
vwait threadFinish

puts $threadFinish

