use std::thread;
use std::io::Read;
use std::io::Write;
use std::net::TcpListener;
use std::net::TcpStream;

fn handler(mut stream:TcpStream) {
    println!("Accepted connection");
    stream.write(b"Entering echo mode...\r\n").unwrap();

    let mut buffer = [0; 16];

    loop {
        match stream.read(&mut buffer) {
            Ok(size) => {
                println!("read: {} bytes", size);
                if size == 0 {
                    println!("no data to read?");
                    break;
                }
                match stream.write(&buffer[0..size]) {
                    Ok(_)  => {}
                    Err(_) => {
                        println!("write error");
                        break;
                    }
                }
            }
            Err(_) => {
                println!("read error");
                break;
            }
        }
    }
    println!("disconnected")
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

