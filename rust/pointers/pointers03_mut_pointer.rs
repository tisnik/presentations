fn main() {
    let value1: i32 = 42;
    let value2: i32 = 100;

    let mut pointer: *const i32;

    println!("{}", value1);

    pointer = &value1;
    println!("{:?}", pointer);
    println!("{}", unsafe {*pointer});

    pointer = &value2;
    println!("{:?}", pointer);
    println!("{}", unsafe {*pointer});
}

