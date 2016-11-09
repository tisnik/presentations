fn clasify(x:i32) -> &'static str {
    match x {
        0         => "zero",
        1 | 2     => "one or two",
        3 ... 5   => "from three to five",
        10 ... 20 => "from ten to twenty",
        _         => "something else",
    }
}

fn main() {
    for x in 0..20 {
        println!("{}:{}", x, clasify(x))
    }
}

