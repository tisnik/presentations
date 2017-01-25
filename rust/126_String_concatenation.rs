fn print_str(message: &str) {
    println!("{}", message);
}

fn main() {
    let mut message = "Hello world!".to_string();
    print_str(&message);
    message.push_str("\n42");
    print_str(&message);
    message = message + "\n***";
    print_str(&message);
}

