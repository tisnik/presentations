fn foo() -> ! {
    panic!("This function never returns!");
}

fn main() {
    foo();
}

