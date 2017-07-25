extern crate ndarray;
use ndarray::Array;
use ndarray::Array2;


fn array_view() {
    println!("array_view");

    let array = Array::from_iter(0..12);
    let view = array.view();

    println!("length:     {}", array.len());
    println!("dimensions: {}", array.ndim());
    println!("dimension:  {:?}", array.dim());
    println!("shape:      {:?}", array.shape());
    println!("strides:    {:?}\n", array.strides());

    println!("length:     {}", view.len());
    println!("dimensions: {}", view.ndim());
    println!("dimension:  {:?}", view.dim());
    println!("shape:      {:?}", view.shape());
    println!("strides:    {:?}\n", view.strides());

    println!();
}

fn four_d_array_view() {
    println!("four_d_array_view");

    let array = Array::from_iter(0..16).into_shape((2,2,2,2)).unwrap();
    let view = array.view();

    println!("length:     {}", array.len());
    println!("dimensions: {}", array.ndim());
    println!("dimension:  {:?}", array.dim());
    println!("shape:      {:?}", array.shape());
    println!("strides:    {:?}\n", array.strides());

    println!("length:     {}", view.len());
    println!("dimensions: {}", view.ndim());
    println!("dimension:  {:?}", view.dim());
    println!("shape:      {:?}", view.shape());
    println!("strides:    {:?}\n", view.strides());

    println!();
}



fn mut_array() {
    println!("mut_array");

    let mut array = Array2::<i32>::zeros((3,3));

    println!("original array:\n{}\n", array);

    {
        let mut view = array.view_mut();
        view[[1,1]] = 42;
        
        // array[[1,1]] = 1000; // uncomment to test the compile-time checks
    }

    println!("array modified via view:\n{}\n", array);

    array[[1,1]] = 1000;

    println!("array modified directly:\n{}\n", array);

    println!();
}



fn main() {
    array_view();
    four_d_array_view();
    mut_array();
}
