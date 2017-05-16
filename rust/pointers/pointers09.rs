fn main() {
    let array: [i32; 5] = [1, 2, 3, 4, 5];

    let pointer = array.as_ptr();

    println!("{:?}", array);
    unsafe {
        println!("{}", *pointer);
        println!("{}", *pointer.offset(0));
        println!("{}", *pointer.offset(1));
    }
}

