fn foo() {
    println!("foo");
}

fn bar(argument:i32) {
    println!("{}", argument);
}

fn baz(argument1:i32, argument2:i32) {
    println!("{} {}", argument1, argument2);
}

fn main() {
    foo();
    bar(42);
    baz(1, 2);
}

