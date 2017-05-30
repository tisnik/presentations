use std::ffi::CString;
use std::os::raw::c_char;

#[link(name = "ffi3")]
extern {
    fn string_length(str: *const c_char) -> i32;
}

fn main() {
    match CString::new("Hello world!") {
        Ok(string) => {
            let pointer = string.as_ptr();
            unsafe {
                println!("string length = {}", string_length(pointer));
            }
        }
        Err(error) => {
            println!("CString::new() error: {:?}", error);
        }
    }
}

