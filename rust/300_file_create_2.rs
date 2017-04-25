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

fn main() {
    match File::create("test.txt") {
        Ok(fout) => {
            write_message_to_file(&fout);
        }
        Err(error) => {
            println!("file create error: {}", error);
        }
    }
}

