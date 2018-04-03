expect -re "([Ll]ogin|Username):.*" {
      send "anonymous\r"
  }

glob (globbing)
- napriklad pouzito v lsearch
* - sekvence libovolnych znaku
? - jeden libovolny znak
[]
# Matches
string match f* foo

# Matches
string match f?? foo

# Doesn't match
string match f foo



regexp
([1-9][0-9]{2}-[0-9]{4}) 

.a.a.a
Canada
banana

a{3,5}, the strings "aaa", "aaaa", and "aaaaa"

[a-z0-9_-]+(\.[a-z0-9_-]+)*@[a-z0-9_-]+(\.[a-z0-9_-]+)+


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


