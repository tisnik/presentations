use std::f32;

fn main() {
    println!("Max          {}",    f32::MAX);
    println!("Min          {}",    f32::MIN);
    println!("Min pos      {}",    f32::MIN_POSITIVE);
    println!("");
    println!("+Infinity    {}",    f32::INFINITY);
    println!("-Infinity    {}",    f32::NEG_INFINITY);
    println!("NaN          {}",    f32::NAN);
    println!("");
    println!("Digits       {}",    f32::DIGITS);
    println!("Max exponent 10^{}", f32::MAX_10_EXP);
    println!("Min exponent 10^{}", f32::MIN_10_EXP);
    println!("Epsilon      {}",    f32::EPSILON);
    println!("");
    println!("Radix        {}",    f32::RADIX);
    println!("Digits       {}",    f32::MANTISSA_DIGITS);
    println!("Max exponent 2^{}",  f32::MAX_EXP);
    println!("Min exponent 2^{}",  f32::MIN_EXP);
}

