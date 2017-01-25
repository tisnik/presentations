fn print_str(message: &str) {
    println!("'{}'", message);
}

fn main() {
    let message = "Hello world!";

    let part1 = &message[0..5];
    let part2 = &message[5..6];
    let part3 = &message[6..12];

    print_str(part1);
    print_str(part2);
    print_str(part3);
}

