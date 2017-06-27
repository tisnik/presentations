use std::slice;

#[no_mangle]
pub extern fn sum(items: *const i32, length: usize) -> i32 {
    let numbers = unsafe {
        slice::from_raw_parts(items, length as usize)
    };

    let mut sum:i32 = 0;
    for number in numbers {
        sum += *number
    }
    sum
}

