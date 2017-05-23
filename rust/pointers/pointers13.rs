use std::ptr;

fn main() {
    let pointer: *const i32 = ptr::null();

    println!("{:p}", pointer);
}

