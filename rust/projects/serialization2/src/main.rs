#[macro_use]
extern crate bincode;

use bincode::{serialize, deserialize, Infinite};

fn main() {
    let x:i32 = 0x12345678;

    match serialize(&x, Infinite) {
        Ok(encoded) => {
            for i in &encoded {
                println!("{:x}", i);
            }
            match deserialize(&encoded) {
                Ok(deserialized) => {
                    let val:i32 = deserialized;
                    println!("deserialized value: 0x{:x}", val);
                }
                Err(error) => {
                    println!("deserialization error: {}", error);
                }
            }
        }
        Err(error) => {
            println!("serialization error: {}", error);
        }
    }
}

