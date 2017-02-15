macro_rules! trace {
    ($expression:expr) => (
        println!("{} = {}", $expression, $expression);
    )
}

fn main() {
    trace!(1+2);

    let x = 6;
    let y = 7;

    trace!(x*y);
}

