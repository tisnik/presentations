use std::thread;
use std::io::Write;
use std::net::TcpListener;
use std::net::TcpStream;

fn handler(mut stream:TcpStream) {
    println!("Accepted connection");
    stream.write(b"Server response...\r\n").unwrap();
}

fn main() {
    let listener = TcpListener::bind("127.0.0.1:1234").unwrap();

    for tcp_stream in listener.incoming() {
        match tcp_stream {
            Ok(tcp_stream) => {
                thread::spawn(|| {
                    handler(tcp_stream);
                });
            }
            Err(e) => {
                println!("connection failed: {}", e);
            }
        }
    }
}

