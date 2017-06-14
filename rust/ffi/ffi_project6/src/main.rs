#[derive(Debug)]
#[repr(C)]
struct TestStruct {
    a: u8,
    b: i32,
    c: u8,
    d: i32,
    e: u8,
    f: f32
}

extern {
    fn print_struct(s: *const TestStruct) -> ();
    fn change_struct(s: *const TestStruct) -> ();
}

fn main() {
    let s : TestStruct = TestStruct{a:1, b:1000, c:255, d:10000, e:127, f:3.14};
    println!("original value: {:?}", s);
    unsafe {
        let pointer = &s;
        print_struct(pointer);
        change_struct(pointer);
        print_struct(pointer);
    }
    println!("changed value: {:?}", s);
}

