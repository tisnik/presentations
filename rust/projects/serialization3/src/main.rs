#[macro_use]
extern crate bincode;

use std::fs::File;

use bincode::{serialize_into, Infinite};

fn serialize_value(mut fout: &File, value: i32) {
    match serialize_into(&mut fout, &value, Infinite) {
        Ok(_) => {
            println!("successfully serialized into file");
        }
        Err(error) => {
            println!("serialization error: {}", error);
        }
    }
}

fn main() {
    let x:i32 = 0x12345678;

    match File::create("test.bin") {
        Ok(fout) => {
            serialize_value(&fout, x);
        }
        Err(error) => {
            println!("file create error: {}", error);
        }
    }
}

