use std::slice;

#[no_mangle]
pub extern fn sum(items: *const i32, length: usize) -> i32 {
    let numbers = unsafe {
        assert!(!items.is_null());

        slice::from_raw_parts(items, length as usize)
    };

    numbers.iter().fold(0, |acc, v| acc + v)
}

