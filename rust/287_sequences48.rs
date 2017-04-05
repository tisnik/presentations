use std::collections::BinaryHeap;
use std::cmp::Ordering;

#[derive(Clone, Debug)]
struct Complex {
    real: i32,
    imag: i32,
}

impl Complex {
    fn new(real: i32, imag: i32) -> Complex {
        Complex{real:real, imag:imag}
    }
    fn print(&self) {
        println!("complex number: {:}+{:}i", self.real, self.imag);
    }
}

impl Ord for Complex {
    fn cmp(&self, other: &Complex) -> Ordering {
        self.real.cmp(&other.real)
    }
}

impl PartialOrd for Complex {
    fn partial_cmp(&self, other: &Complex) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl PartialEq for Complex {
    fn eq(&self, other: &Complex) -> bool {
        self.real == other.real
    }
}

impl Eq for Complex {}

impl Drop for Complex {
    fn drop(&mut self) {
        println!("Dropping complex number: {:}+{:}i", self.real, self.imag);
    }
}

fn main() {
    let mut heap = BinaryHeap::new();

    heap.push(Complex::new(0, 0));
    heap.push(Complex::new(1, 1));
    heap.push(Complex::new(0, 0));
    heap.push(Complex::new(1, 1));
    heap.push(Complex::new(2, 2));

    println!("max: {:?}", heap.peek());
    for item in &heap {
        item.print();
    }
}

