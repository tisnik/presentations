use std::ffi::CString;
use std::os::raw::c_char;

#[link(name = "ffi4")]
extern {
    fn string_length(str: *const c_char) -> i32;
}

fn test(string :&'static str) {
    match CString::new(string) {
        Ok(string) => {
            let pointer = string.as_ptr();
            println!("Rust side pointer: {:p}", pointer);
            unsafe {
                println!("string length = {}", string_length(pointer));
            }
        }
        Err(error) => {
            println!("CString::new() error: {:?}", error);
        }
    }
}

fn main() {
    test("Hello world!");
    test("");
    test("ěščřžýáíé");
}

