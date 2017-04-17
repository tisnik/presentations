use std::io::Read;
use std::io::Write;
use std::net::TcpStream;

fn utf8_to_string(bytes: &[u8]) -> String {
    let vector: Vec<u8> = Vec::from(bytes);
    String::from_utf8(vector).unwrap()
}

fn send_message(mut stream:&TcpStream, message: &str) {
    let message_as_bytes = message.as_bytes();

    match stream.write_all(&message_as_bytes) {
        Ok(_) => {
            println!("write ok");
        }
        Err(error) => {
            println!("write error: {}", error);
        }
    }

}

fn receive_message(mut stream:&TcpStream) {
    let mut buffer = [0; 40];
    match stream.read(&mut buffer) {
        Ok(size) => {
            let response = utf8_to_string(&buffer[0..size]);
            println!("read: {} bytes: {:?}\n'{}'", size, &buffer[0..size], response);
            if size == 0 {
                println!("no data to read?");
            }
        }
        Err(_) => {
            println!("read error");
        }
     }
}

fn main() {
    let tcp_stream = TcpStream::connect("127.0.0.1:1234").unwrap();
    println!("{:?}", tcp_stream);

    receive_message(&tcp_stream);
    send_message(&tcp_stream, "Hello\r\n");
    receive_message(&tcp_stream);

    println!("closing stream");
}

