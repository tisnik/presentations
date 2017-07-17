fn main() {
    let mut x:f32 = 1.0;
    let mut y:f32 = 0.0;
    for _ in 0..20 {
        y += x;
        x = x / 2.0;
    }
    println!("{}", y);
}

