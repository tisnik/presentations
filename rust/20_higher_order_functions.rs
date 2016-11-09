fn square(x:u32) -> u32 {
    x*x
}

fn main() {
    let sequence = 0..10;
    let squares = sequence.map(square);
    for n in squares {
        println!("{}", n);
    }
}

