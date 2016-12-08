use std::fmt::Debug;

struct Complex<T: Debug> {
    real: T,
    imag: T,
}

impl<T: Debug> Complex<T> {

    fn new(real: T, imag: T) -> Complex<T> {
        Complex{real:real, imag:imag}
    }

    fn print(&self) {
        println!("complex number: {:?}+{:?}i", self.real, self.imag);
    }

}

fn main() {
    let c1 = Complex::new(3, 4);
    let c2 = Complex::new(3.3f32, 4.4f32);
    let c3 = Complex::new(5.0f64, 6.0f64);
    c1.print();
    c2.print();
    c3.print();
}

