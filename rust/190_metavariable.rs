macro_rules! trace {
    ($expression:expr) => (
        println!("{:?}", $expression);
    )
}

fn main() {
    trace!(1+2);
}

