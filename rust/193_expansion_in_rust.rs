macro_rules! sqr {
    ($expression:expr) => ($expression * $expression);
}

fn main() {
    println!("{}", sqr!(10));
    println!("{}", sqr!(5+5));

    let x = 2;
    println!("{}", sqr!(x));
    println!("{}", sqr!(x+1));
}

