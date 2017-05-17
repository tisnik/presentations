fn main() {
    let mut value1: i32 = 1;
    let mut value2: i32 = 3;

    let mut pointer: *const i32;

    pointer = &value1;
    println!("{}", unsafe {*pointer});
    value1 = 2;
    println!("{}", unsafe {*pointer});

    pointer = &value2;
    println!("{}", unsafe {*pointer});
    value2 = 4;
    println!("{}", unsafe {*pointer});
}

