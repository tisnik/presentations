fn print_str(message: &str) {
    println!("{}", message);
}

fn return_str() -> &str {
    "Hello world!"
}

fn main() {
    let message = return_str();

    print_str(message);
}

