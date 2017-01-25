fn print_str(message: String) {
    println!("{}", message);
}

fn main() {
    let message = "Hello world!".to_string();
    print_str(message);
    print_str(message);
    print_str(message);
}

