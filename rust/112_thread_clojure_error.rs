use std::thread;

fn main() {
    println!("Starting");
    for i in 1..10 {
        thread::spawn(|| {println!("Hello from a thread #{}", i);});
    }
    println!("Stopping");
}

