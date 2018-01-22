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
