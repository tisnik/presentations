use std::thread;
use std::time;

fn delay(ms : u64) {
    let amount = time::Duration::from_millis(ms);
    thread::sleep(amount);
}

fn main() {
    for i in 1..10 {
        println!("counting: {}", i);
        delay(1000);
    }
}

