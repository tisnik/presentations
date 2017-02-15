macro_rules! sqr {
    ($expression:expr) => ($expression * $expression);
}

fn getx() -> i32 {
    println!("getx() called");
    2
}

fn main() {
    println!("{}", sqr!(getx()));
}

