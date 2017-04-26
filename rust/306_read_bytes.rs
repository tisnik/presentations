use std::io::Read;
use std::io::Write;
use std::fs::File;

fn write_message_to_file(mut fout: &File) {
    match fout.write(b"Hello, world!\n") {
        Ok(written) => {
            println!("{} bytes written", written);
        }
        Err(error) => {
            println!("write error: {}", error);
        }
    }
}

fn create_hello_world_file(file_name: &str) {
    match File::create(file_name) {
        Ok(fout) => {
            write_message_to_file(&fout);
        }
        Err(error) => {
            println!("file create error: {}", error);
        }
    }
}

fn read_one_byte(mut fin: &File) -> bool {
    let mut buffer = [0; 1];
    
    match fin.read(&mut buffer) {
        Ok(size) => {
            if size > 0 {
                println!("Read: '{}' = {}", buffer[0] as char, buffer[0]);
            }
            size > 0
        }
        Err(error) => {
            println!("file read error: {}", error);
            false
        }
    }
}

fn main() {
    create_hello_world_file("test.txt");

    let fin = File::open("test.txt").unwrap();

    while read_one_byte(&fin)
    {}
}

