extern crate ndarray;
use ndarray::Array;
use std::fmt;


struct Complex {
    real: f32,
    imag: f32,
}


impl Complex {
    fn new(real: f32, imag: f32) -> Complex {
        Complex{real:real, imag:imag}
    }

    fn abs(&self) -> f32 {
        (self.real * self.real + self.imag * self.imag).sqrt()
    }
}


impl fmt::Debug for Complex {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{}+{}i", self.real, self.imag)
    }
}


fn map_complex() {
    println!("map_complex");

    let vector1 = Array::from_vec(vec![Complex::new(0.0, 0.0),
                                       Complex::new(1.0, 0.0),
                                       Complex::new(0.0, 1.0),
                                       Complex::new(1.0, 1.0),
                                       Complex::new(100.0, 100.0)]);

    let vector2 = vector1.map(|x| Complex::abs(x));

    println!("vector1: {:?}", vector1);
    println!("vector2: {:?}", vector2);

    println!()
}


fn map_complex_2d() {
    println!("map_complex_2d");

    let array1 = Array::from_shape_vec((3,3), vec![Complex::new(0.0, 0.0),
                                                   Complex::new(1.0, 0.0),
                                                   Complex::new(2.0, 0.0),
                                                   Complex::new(0.0, 1.0),
                                                   Complex::new(1.0, 1.0),
                                                   Complex::new(2.0, 1.0),
                                                   Complex::new(0.0, 2.0),
                                                   Complex::new(1.0, 2.0),
                                                   Complex::new(2.0, 2.0)]).unwrap();

    let array2 = array1.map(|x| Complex::abs(x));

    println!("vector1:\n{:?}\n", array1);
    println!("vector2:\n{:?}\n", array2);

    println!()
}


fn main() {
    map_complex();
    map_complex_2d();
}
