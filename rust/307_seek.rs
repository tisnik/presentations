use std::io::Read;
use std::io::Write;
use std::io::Seek;
use std::io::SeekFrom;
use std::fs::File;
use std::io::Error;

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

fn print_position(pos: Result<u64, Error>) {
    println!("position in file: {}", pos.unwrap());
}

fn main() {
    create_hello_world_file("test.txt");

    let mut fin = File::open("test.txt").unwrap();

    read_one_byte(&fin);

    let position = fin.seek(SeekFrom::Start(7));
    read_one_byte(&fin);
    print_position(position);

    let position = fin.seek(SeekFrom::End(-2));
    read_one_byte(&fin);
    print_position(position);

    let position = fin.seek(SeekFrom::Current(-2));
    read_one_byte(&fin);
    print_position(position);
}

