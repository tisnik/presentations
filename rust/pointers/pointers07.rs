// WARNING: this example is really ugly, use it as an example how NOT to make programs

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
    let pointer: *mut Complex;

    {
        let mut value: Complex = Complex::new(1.0, 2.0);
        pointer = &mut value;

        println!("{:?}", value);
        unsafe {
            println!("{:?}", *pointer);
        }

        value.real = 10.0;
        value.imag = 20.0;

        println!("{:?}", value);
        unsafe {
            println!("{:?}", *pointer);
        }

        unsafe {
            (*pointer).real = 20.0;
            (*pointer).imag = 40.0;
        }
        println!("{:?}", value);
        unsafe {
            println!("{:?}", *pointer);
        }
    }

    // !!!
    unsafe {
        (*pointer).real = -1.1;
        (*pointer).imag = -2.2;
        println!("{:?}", *pointer);
    }
}

