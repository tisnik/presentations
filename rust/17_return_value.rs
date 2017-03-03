fn foo() -> i32 {
    42
}

fn bar(argument :i32) -> i32 {
    return argument * 2;
}

fn baz(argument :i32) -> i32 {
    argument * 2
}

fn main() {
    println!("{}", foo());
    println!("{}", bar(21));
    println!("{}", baz(21));
}

