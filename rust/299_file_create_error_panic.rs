use std::io::prelude::*;
use std::fs::File;

fn main() {
    let mut fout = File::create("/bin/test.txt").unwrap();
    let written = fout.write(b"Hello, world!\n").unwrap();
    println!("{} bytes written", written);
}

