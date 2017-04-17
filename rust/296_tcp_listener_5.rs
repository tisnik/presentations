use std::thread;
use std::io::Read;
use std::io::Write;
use std::net::TcpListener;
use std::net::TcpStream;

fn utf8_to_string(bytes: &[u8]) -> String {
    let vector: Vec<u8> = Vec::from(bytes);
    String::from_utf8(vector).unwrap()
}

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
                } else {
                    let response = utf8_to_string(&buffer[0..size]);
                    println!("read: {:?}: '{}'", &buffer[0..size], response);
                    match stream.write(&buffer[0..size]) {
                        Ok(_)  => {}
                        Err(error) => {
                            println!("write error {:?}", error);
                            break;
                        }
                    }
                }
            }
            Err(error) => {
                println!("read error {:?}", error);
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
            Err(error) => {
                println!("connection failed: {}", error);
            }
        }
    }
}

