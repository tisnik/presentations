fn main() {
    let value: i32 = 42;

    let pointer: *mut i32 = &mut value;

    println!("{}", value);
    unsafe {
        println!("{}", *pointer);
    }

    value = 1;

    println!("{}", value);
    unsafe {
        println!("{}", *pointer);
    }

    unsafe {
        *pointer = 20;
    }
    println!("{}", value);
    unsafe {
        println!("{}", *pointer);
    }
}

