use std::ptr;

fn main() {
    let pointer: *mut i32 = ptr::null_mut();

    println!("{:p}", pointer);

    unsafe {
        *pointer = 42;
    }
}

