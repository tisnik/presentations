macro_rules! power {
    ($base:expr)                 => ($base*$base);
    ($base:expr, $exponent:expr) => (($base as i32).pow($exponent));
}

fn main() {
    for base in 0..10 {
         println!("{:4} {:4} {:4}", base, power!(base), power!(base, 3));
    }
}

