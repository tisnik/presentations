use std::thread;

fn main() {
    println!("Starting");
    for i in 1..10 {
        thread::spawn(move || {println!("Hello from a thread #{}", i);});
    }
    println!("Stopping");
}

