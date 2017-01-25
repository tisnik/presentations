fn print_str(message: &'static str) {
    println!("{}", message);
}

fn main() {
    let message : &'static str = "Hello world!";
    print_str(message);
    print_str(message);
    print_str(message);
}

