use std::ptr;

#[derive(Debug)]
struct Complex {
    real: f32,
    imag: f32,
}

impl Complex {
    fn new(real: f32, imag: f32) -> Complex {
        println!("Constructing complex number: {:}+{:}i", real, imag);
        Complex{real:real, imag:imag}
    }
}

impl Drop for Complex {
    fn drop(&mut self) {
        println!("Dropping complex number: {:}+{:}i", self.real, self.imag);
    }
}

fn main() {
    let mut value: Complex = Complex::new(1.0, 2.0);
    let value2: Complex = Complex::new(100.0, 200.0);
    let pointer: *mut Complex = &mut value;

    println!("{:p}", pointer);
    println!("{:?}", value);

    value = value2;
    println!("{:p}", pointer);
    println!("{:?}", value);
}

