# Jednoduchy Echo_Server
#
# Na vybranem portu se otevre socket a posleze se ve smycce akceptuje
# spojeni a na vystup se kopiruji data prijata od klienta
#

# Zakladni nastaveni serveru
#
# Argumenty:
#   - cislo portu serveru
proc Echo_Server {port} {
    # vytvoreni socketu a registrace prikazu
    # ktery se zavola s trojici parametru:
    #   - instance socketu
    #   - klientova IP adresa
    #   - port otevreny na klientu
    set s [socket -server EchoAccept $port]
    puts "Cekam na pripojeni klienta..."
    # vstup do smycky udalosti
    # se specifikaci globalni promenne
    vwait forever
}

# Prikaz zavolany pri navazovani spojeni s klientem
# ihned pote, co je socket vytvoren ve VM TCL
#
# Argumenty:
#   - instance socketu
#   - klientova IP adresa
#   - port otevreny na klientu
proc EchoAccept {sock addr port} {
    global echo

    # Informace o pripojeni
    puts "Vytvoreni pripojeni $sock od klienta na IP adrese $addr a portu $port"
    set echo(addr,$sock) [list $addr $port]

    # Presmerovani vystupu prikazu "put"
    fconfigure $sock -buffering line

    # Nastaveni callback funkce zavolane pri prijmu dat
    fileevent $sock readable [list Echo $sock]
}

# Tento prikaz je zavolany ve chvili, kdy je mozne cist data
# poslana klientem na server
proc Echo {sock} {
    global echo

    # Test, zda klient nepozaduje ukoncit pripojeni ci
    # zda nedoslo k nejake chybe na lince
    if {[eof $sock] || [catch {gets $sock line}]} {
        close $sock
        puts "Ukonceni pripojeni klienta $echo(addr,$sock)"
        unset echo(addr,$sock)
    } else {
        # pokud klient posle "end", server se ukonci
        if [string compare $line end] {
            puts $sock "Odpoved serveru pres socket $sock: $line"
        } else {
            # posleme posledni zpravu klientovi
            puts $sock "Ukonceni prace serveru"
            close $sock
            global forever
            set forever 42
        }
    }
}

# spusteni serveru
Echo_Server 12345

