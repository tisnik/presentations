fn main() {
    let value = 42.5;

    for i in 1..20 {
        println!("|{:width$}|", value, width=i);
    }

    for i in 1..20 {
        println!("|{:^width$}|", value, width=i);
    }
}

