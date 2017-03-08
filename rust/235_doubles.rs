use std::f64;

fn main() {
    println!("Max          {}",    f64::MAX);
    println!("Min          {}",    f64::MIN);
    println!("Min pos      {}",    f64::MIN_POSITIVE);
    println!("");
    println!("+Infinity    {}",    f64::INFINITY);
    println!("-Infinity    {}",    f64::NEG_INFINITY);
    println!("NaN          {}",    f64::NAN);
    println!("");
    println!("Digits       {}",    f64::DIGITS);
    println!("Max exponent 10^{}", f64::MAX_10_EXP);
    println!("Min exponent 10^{}", f64::MIN_10_EXP);
    println!("Epsilon      {}",    f64::EPSILON);
    println!("");
    println!("Radix        {}",    f64::RADIX);
    println!("Digits       {}",    f64::MANTISSA_DIGITS);
    println!("Max exponent 2^{}",  f64::MAX_EXP);
    println!("Min exponent 2^{}",  f64::MIN_EXP);
}

