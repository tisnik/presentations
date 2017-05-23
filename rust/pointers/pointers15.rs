use std::ptr;

fn main() {
    let mut pointer: *const i32 = ptr::null();

    println!("{:p}", pointer);

    let value: i32 = 42;
    pointer = &value;

    println!("{:p}", pointer);
}

