fn classify(x:i32) -> &'static str {
    match x {
        0 => "zero",
        1 => "one",
        2 => "two",
        3 => "three",
        _ => "something else",
    }
}

fn main() {
    for x in 0..10 {
        println!("{}:{}", x, classify(x))
    }
}

