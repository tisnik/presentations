use std::os::raw::c_float;
use std::os::raw::c_uint;

#[link(name = "ffi5")]
extern {
    fn sum(len: c_uint, arr: *const c_float) -> c_float;
}

fn main() {
    let array : [f32; 5] = [1.0, 2.0, 3.0, 4.0, 5.0];
    unsafe {
        let pointer = array.as_ptr(); 
        let len : u32 = array.len() as u32;
        let s = sum(len, pointer);
        println!("sum = {}", s);
    }
}

