fn main() {
    let array: [i32; 5] = [1, 2, 3, 4, 5];

    let pointer: *const i32 = &array[1] as *const i32;

    println!("{:?}", array);
    unsafe {
        println!("{}", *pointer);
        println!("{}", *pointer.offset(-1));
        println!("{}", *pointer.offset(1));
    }
}

