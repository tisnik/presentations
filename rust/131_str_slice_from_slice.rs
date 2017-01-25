fn print_str(message: &str) {
    println!("'{}'", message);
}

fn main() {
    let message = "Hello world!";

    let part = &message[0..10][2..5];
    print_str(part);
}

