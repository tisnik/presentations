use std::io::Write;
use std::net::TcpListener;
use std::net::TcpStream;

fn handler(mut stream:TcpStream) {
    println!("Accepted connection");
    stream.write(b"Server response...\r\n").unwrap();
}

fn main() {
    let listener = TcpListener::bind("127.0.0.1:1234").unwrap();

    let tcp_stream_iter = listener.incoming();

    for tcp_stream in tcp_stream_iter {
        if tcp_stream.is_ok() {
            handler(tcp_stream.unwrap());
        } else {
            println!("connection failed");
        }
    }
}

