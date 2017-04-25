use std::io;
use std::io::BufRead;

fn main() {
    let stdin = io::stdin();
    let stdin_lock = stdin.lock();

    for line in stdin_lock.lines() {
        match line {
            Ok(content) => {
                println!("Echo: '{}' ({} characters)", content.trim(), content.len());
            }
            Err(error) => {
                println!("stdin read error: {}", error);
            }
        }
    }
}

