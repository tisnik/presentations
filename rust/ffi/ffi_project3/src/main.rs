use std::mem;

#[repr(C)]
struct TestStruct {
    a: u8,
    b: u8,
    c: u8,
    d: i32,
    e: i32,
    f: f32
}

extern {
    fn print_struct(s:TestStruct) -> ();
}

fn main() {
    let s : TestStruct = TestStruct{a:1, b:255, c:42, d:10000, e:-10000, f:3.14};
    println!("sizeof on Rust side = {} bytes", mem::size_of::<TestStruct>());
    unsafe {
        print_struct(s);
    }
}

