" ---------------------------------------------
" Vim8 example script #7 - timers
"
" How to use it:
" 1) start new Vim session
" 2) open this script in it
" 3) call :source %
" ---------------------------------------------

function! PrintMessage(message)
    echo a:message
endfunction

call PrintMessage("normal call")

let timer1 = timer_start(1000, 'PrintMessage', {'repeat':6})
echo "timer" timer1 "created"

let timer2 = timer_start(3300, 'PrintMessage')
echo "timer" timer2 "created"

let timer3 = timer_start(4400, 'PrintMessage')
echo "timer" timer3 "created"

let timer4 = timer_start(5500, 'PrintMessage')
echo "timer" timer4 "created"

