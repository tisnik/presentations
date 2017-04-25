use std::io;

fn main() {
    let stdin = io::stdin();
    let mut line = String::new();

    stdin.read_line(&mut line);

    println!("Echo: '{}' ({} characters)", line.trim(), line.len());
}

