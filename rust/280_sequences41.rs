use std::collections::LinkedList;

#[derive(Clone)]
struct Complex {
    real: f32,
    imag: f32,
}

impl Complex {
    fn new(real: f32, imag: f32) -> Complex {
        Complex{real:real, imag:imag}
    }
    fn print(&self) {
        println!("complex number: {:}+{:}i", self.real, self.imag);
    }
}

impl Drop for Complex {
    fn drop(&mut self) {
        println!("Dropping complex number: {:}+{:}i", self.real, self.imag);
    }
}

fn print_list(list: &LinkedList<Complex>) {

    if list.is_empty() {
        println!("list is empty");
    } else {
        println!("list has {} items", list.len());
    }

    for item in list.iter() {
        item.print();
    }
}

fn main() {
    let list: LinkedList<Complex> = vec![Complex::new(0.0, 0.0),
                                         Complex::new(1.0, 1.0),
                                         Complex::new(2.0, 2.0)].into_iter().collect();

    print_list(&list);

    println!("exit from main()");
}

