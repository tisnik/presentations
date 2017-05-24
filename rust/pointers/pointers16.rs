use std::ptr;

fn main() {
    let mut x = 0;
    let pointer: *mut i32 = &mut x;
    let y = 42;

    println!("{:p}", pointer);
    println!("{}", x);

    unsafe {
        ptr::write(pointer, y);
    }
    println!("{}", x);
}

