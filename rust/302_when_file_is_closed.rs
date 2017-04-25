use std::io::prelude::*;
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

fn main() {
    create_hello_world_file("test.txt");
    // here the file should be closed
    println!("end of main");
}

