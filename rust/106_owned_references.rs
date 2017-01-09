use std::rc::Rc;

struct Complex {
    real: f32,
    imag: f32,
}

impl Complex {

    fn new(real: f32, imag: f32) -> Complex {
        println!("Constructing complex number: {:}+{:}i", real, imag);
        Complex{real:real, imag:imag}
    }

    fn print(&self) {
        println!("complex number: {:?}+{:?}i", self.real, self.imag);
    }

}

impl Drop for Complex {
    fn drop(&mut self) {
        println!("Dropping complex number: {:}+{:}i", self.real, self.imag);
    }
}

struct ComplexNumberOwner {
    id: i32,
    value: Rc<Complex>
}

impl ComplexNumberOwner {
    fn print(&self) {
        println!("owner: number #{} with value {}+{}i", self.id, self.value.real, self.value.imag);
    }
}

fn main() {
    let c1 = Rc::new(Complex::new(1.0, 1.0));
    let c2 = Rc::new(Complex::new(2.0, 2.0));

    let owner1 = ComplexNumberOwner{id:1, value: c1.clone()};
    let owner2 = ComplexNumberOwner{id:2, value: c1.clone()};
    let owner3 = ComplexNumberOwner{id:3, value: c1.clone()};
    let owner4 = ComplexNumberOwner{id:4, value: c2.clone()};

    owner1.print();
    owner2.print();
    owner3.print();
    owner4.print();
}

