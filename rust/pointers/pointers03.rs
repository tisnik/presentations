fn main() {
    let mut value: i32 = 42;

    let pointer: *const i32 = &value;

    println!("{}", value);
    println!("{:?}", pointer);

    unsafe {
        println!("{}", *pointer);
    }

    value = 100;
    println!("{}", value);
    println!("{:?}", pointer);

    unsafe {
        println!("{}", *pointer);
    }

}

