use std::env;

fn print_env_var(name:&str) {
    match env::var(name) {
        Ok(val) => println!("{}: {:?}", name, val),
        Err(e)  => println!("couldn't interpret {}: {}", name, e),
    }
}

fn main() {
    print_env_var("PATH");
    print_env_var("HOME");
    print_env_var("DISPLAY");
    print_env_var("SPECIAL");
}

