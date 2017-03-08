use std::env;

fn main() {
    let exename = env::args().nth(0);
    let arguments = env::args().count();

    println!("exename:   {}", exename.unwrap());
    println!("arguments: {}", arguments);
}

