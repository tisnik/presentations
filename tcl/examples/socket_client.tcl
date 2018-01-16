proc Echo_Client {host port} {
    set sock [socket $host $port]
    fconfigure $sock -buffering line
    return $sock
}

set my_socket [Echo_Client localhost 12345]
puts $my_socket "Hello!"
gets $my_socket line_from_server
puts $line_from_server

