extern crate rand;
use rand::Rng;

fn main() {
    let mut rng = rand::thread_rng();
    for _ in 1..11 {
        println!("{:>5}  {:02x}", rng.gen::<i8>(), rng.gen::<u8>())
    }
}
