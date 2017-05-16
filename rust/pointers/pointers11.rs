// WARNING: this example is really ugly, use it as an example how NOT to make programs

fn main() {
    let array: [i32; 5] = [1, 2, 3, 4, 5];

    let pointer: *const i32 = &array[0] as *const i32;

    println!("{:?}", array);
    unsafe {
        println!("{}", *pointer);
        println!("{}", *pointer.offset(1));

        // !!!
        println!("{}", *pointer.offset(10));

        // !!!
        println!("{}", *pointer.offset(-1));

        // !!!
        println!("{}", *pointer.offset(-10));
    }
}

