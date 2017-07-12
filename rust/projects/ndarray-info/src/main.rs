extern crate ndarray;
use ndarray::Array;


fn array_info() {
    println!("array_len_and_shape");

    let array = Array::from_iter(0..12);
    println!("length:     {}", array.len());
    println!("dimensions: {}", array.ndim());
    println!("dimension:  {:?}", array.dim());
    println!("shape:      {:?}", array.shape());
    println!("strides:    {:?}\n", array.strides());

    let array_b = Array::from_iter(0..12).into_shape((1,12)).unwrap();
    println!("length:     {}", array_b.len());
    println!("dimensions: {}", array_b.ndim());
    println!("dimension:  {:?}", array_b.dim());
    println!("shape:      {:?}", array_b.shape());
    println!("strides:    {:?}\n", array_b.strides());

    let array_c = Array::from_iter(0..12).into_shape((4,3)).unwrap();
    println!("length:     {}", array_c.len());
    println!("dimensions: {}", array_c.ndim());
    println!("dimension:  {:?}", array_c.dim());
    println!("shape:      {:?}", array_c.shape());
    println!("strides:    {:?}\n", array_c.strides());

    let array_d = Array::from_iter(0..12).into_shape((2,3,2)).unwrap();
    println!("length:     {}", array_d.len());
    println!("dimensions: {}", array_d.ndim());
    println!("dimension:  {:?}", array_d.dim());
    println!("shape:      {:?}", array_d.shape());
    println!("strides:    {:?}\n", array_d.strides());

    let array_e = Array::from_iter(0..16).into_shape((2,2,2,2)).unwrap();
    println!("length:     {}", array_e.len());
    println!("dimensions: {}", array_e.ndim());
    println!("dimension:  {:?}", array_e.dim());
    println!("shape:      {:?}", array_e.shape());
    println!("strides:    {:?}\n", array_e.strides());

    println!();
}


fn main() {
    array_info();
}
