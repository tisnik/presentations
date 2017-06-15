use std::mem;

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
    fn print_struct(s:TestStruct) -> ();
}

fn main() {
    let s : TestStruct = TestStruct{a:1, b:1000, c:255, d:10000, e:127, f:3.14};
    println!("sizeof on Rust side = {} bytes", mem::size_of::<TestStruct>());
    unsafe {
        print_struct(s);
    }
}

