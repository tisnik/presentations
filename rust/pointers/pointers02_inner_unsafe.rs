fn main() {
    let value: i32 = 42;

    let reference: &i32 = &value;
    let pointer: *const i32 = &value;

    println!("{}", value);
    println!("{}", reference);
    println!("{:?}", pointer);

    println!("{}", unsafe {*pointer});
}

