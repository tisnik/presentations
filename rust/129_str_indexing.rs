fn print_str(message: &str) {
    println!("{}", message);
}

fn main() {
    let message = "Hello world!";

    for byte in message.as_bytes() {
        println!("{}", byte);
    }

    for char in message.chars() {
        println!("{}", char);
    }

    print_str(message);
}

