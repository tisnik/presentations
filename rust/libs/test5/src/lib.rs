use std::ffi::CStr;
use std::os::raw::c_char;

#[no_mangle]
pub extern "C" fn print_string(what: *const c_char) -> () {
    unsafe {
        let c_string = CStr::from_ptr(what).to_str().unwrap();
        println!("{:?}", c_string);
    }
}
