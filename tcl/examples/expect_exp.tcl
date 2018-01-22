spawn           (starts a process)
send            (sends to a process)
expect          (waits for output from a process)
interact        (lets you interact with a process)
                - uzivatel muze komunikovat s procesem pomoci klavesnice






















# first give the user some time to logout
exec sleep 4
spawn tip modem
expect {*connected*} {}
send ATZ\r
expect {*OK*} {}
send ATDT[index $argv 1]\r
# modem takes a while to connect
set timeout 60
expect {*CONNECT*} {}

























#!/usr/bin/expect  --
set timeout 30
spawn /usr/local/bin/scp -P 36000 user@ip:/data/myfile  /data1
expect {           
      "password:" {
                send "password\r"
    } "yes/no)?" {
                send "yes\r"
                set timeout -1
    } timeout {
                exit
    } eof {
                exit
    }
}






















expect {
        busy       {puts busy\n ; exp_continue}
        -re "failed|invalid password" abort
        timeout    abort
        connected
    }








expect {
        busy       {puts busy\n ; exp_continue}
        -re "[Ff]ailed|[Ii]nvalid password" abort
        timeout    abort
        connected
    }














set process [spawn /usr/local/bin/scp......]

expect {
   -i $process "password" {......}
}











expect {
    busy               {puts busy\n ; exp_continue}
    failed             abort
    "invalid password" abort
    timeout            abort
    connected
}












expect {
    busy       {puts busy\n ; exp_continue}
    -re "failed|invalid password" abort
    timeout    abort
    connected
}



set CTRLZ \032
interact {
    -reset $CTRLZ {exec kill -STOP [pid]}
    \001   {send_user "you typed a control-A\n";
            send "\001"
           }
    $      {send_user "The date is [exec date]."}
    \003   exit
    foo    {send_user "bar"}
    ~~
}
-reset obnoveni nastaveni terminalu
001- Ctrl+A - posle procesu ^A
$ - zobrazi datum
003- Ctrl+C - ukonceni expectu
~~ - prechod na interaktivni rezim
-re - umozuje zapis regularnich vyrazu
timetout - specifikace doby cekani na uzivatele


expect -re "([Ll]ogin|Username):.*" {
      send "anonymous\r"
  }

set logged_in 0
while {!$logged_in} {
        expect -i $id timeout {
        timedout "in while loop"
        break
    } eof {
        timedout "spawn failed with eof"
        break
    } "Are you sure you want to continue connecting (yes/no)? " {
        send -i $id -- "yes\r"
    } "\[Pp\]assword*" {
        send -i $id -- "$OPTS(passwd)\r"
    } "TERM = (*) " {
        send -i $id -- "$env(TERM)\r"
    } -re $OPTS(prompt) {
        set logged_in 1
    }
}


