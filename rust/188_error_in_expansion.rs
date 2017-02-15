macro_rules! hello_world {
    () => (
        foobar("Hello!");
    )
}

fn main() {
    hello_world!();
}

