use std::thread;

fn print_hello() {
    println!("Hello from a thread...");
}

fn main() {
    println!("Starting");
    for i in 1..10 {
        thread::spawn(|| print_hello());
    }
    println!("Stopping");
}

