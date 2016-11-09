fn foo() -> i32 {
    42
}

fn bar(argument:i32) -> i32 {
    return argument * 2;
}

fn baz(argument:i32) -> i32 {
    argument * 2
}

fn main() {
    let f1 = foo;
    let f2 = bar;
    let f3 = baz;
    println!("{}", f1());
    println!("{}", f2(21));
    println!("{}", f3(21));
}

