fn print_str(message: &str) {
    println!("{}", message);
}

fn main() {
    let mut message = "Hello world!";
    print_str(message);
    message = "Something else";
    print_str(message);
    print_str(message);
}

