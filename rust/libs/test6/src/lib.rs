use std::iter;
use std::ffi::CString;
use std::os::raw::c_char;

#[no_mangle]
pub extern fn generate_stars(count: u8) -> *mut c_char {
    let s: String = iter::repeat("*").take(count as usize).collect();
    let c_string = CString::new(s).unwrap();
    let raw = c_string.into_raw();
    println!("output raw pointer:  {:?}", raw);
    raw
}

#[no_mangle]
pub extern fn free_string(raw: *mut c_char) {
    unsafe {
        if raw.is_null() { return }
        println!("raw pointer to free: {:?}", raw);
        CString::from_raw(raw)
    };
}
