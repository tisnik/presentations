// WARNING: this example is really ugly, use it as an example how NOT to make programs

fn main() {
    let pointer: *mut i32;

    {
        let mut value: i32 = 42;

        pointer = &mut value;

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

    // !!!
    unsafe {
        *pointer = 99;
        println!("{}", *pointer);
    }
}

