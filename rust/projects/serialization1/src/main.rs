#[macro_use]
extern crate bincode;

use bincode::{serialize, deserialize, Infinite};

fn main() {
    let x:i32 = 0x12345678;

    let serialized: Vec<u8> = serialize(&x, Infinite).unwrap();

    for i in &serialized {
        println!("{:x}", i);
    }

    let deserialized: i32 = deserialize(&serialized[..]).unwrap();

    println!("deserialized value: 0x{:x}", deserialized);
}

