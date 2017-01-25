fn print_str(message: &str) {
    println!("{}", message);
}

fn main() {
    let message1 : String = "Hello".to_string();
    let message2 : String = "world".to_string();

    print_str(&message1);
    print_str(&message2);

    let message = message1 + " " + message2 + "!";

    print_str(&message);
}

