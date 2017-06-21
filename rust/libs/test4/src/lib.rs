#[repr(C)]
pub struct Complex {
    real: f32,
    imag: f32,
}

#[no_mangle]
pub extern fn add_complex(c1: Complex, c2: Complex) -> Complex {
    Complex {real: c1.real + c2.real, imag: c1.imag + c2.imag}
}

#[no_mangle]
pub extern fn add_complex_mut(c1: &mut Complex, c2: Complex) -> () {
    c1.real += c2.real;
    c1.imag += c2.imag;
}
