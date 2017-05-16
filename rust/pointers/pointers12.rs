fn main() {
    let mut array: [i32; 5] = [1, 2, 3, 4, 5];

    let pointer: *mut i32 = array.as_mut_ptr();

    println!("{:?}", array);
    unsafe {
        *pointer = 100;
        *pointer.offset(2) = 200;
    }
    println!("{:?}", array);
}

