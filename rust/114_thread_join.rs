use std::thread;

fn main() {
    println!("Starting");
    for i in 1..10 {
        let thr = thread::spawn(move || {println!("Hello from a thread #{}", i);});
        thr.join();
    }
    println!("Stopping");
}

