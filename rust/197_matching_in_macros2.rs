macro_rules! power {
    ($base:expr)                 => ($base*$base);
    ($base:expr, $exponent:expr) => (($base as i32).pow($exponent));
}

fn main() {
    for base in 0..10 {
        for exponent in 2..6 {
             print!("{:5}  ", power!(base, exponent));
        }
        println!("");
    }
}

