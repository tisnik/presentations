#[macro_use]
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


fn mut_array() {
    println!("mut_array");

    let mut array = Array2::<i32>::zeros((3,3));

    println!("array:\n{}", array);

    {
        let mut view = array.view_mut();
        view[[1,1]] = 42;
    }

    println!("array:\n{}", array);

    println!();
}


fn slice_1d_array() {
    println!("slice_1d_array");

    let array = Array::from_iter(0..12);
    println!("array:\n{}", array);

    let slice = array.slice(s![3..8]);
    println!("slice:\n{}", slice);

    let slice2 = array.slice(s![..8]);
    println!("slice:\n{}", slice2);

    let slice3 = array.slice(s![3..]);
    println!("slice:\n{}", slice3);

    let slice4 = array.slice(s![..]);
    println!("slice:\n{}", slice4);
}


fn slice_2d_array() {
    println!("slice_2d_array");

    let array = Array::from_iter(0..12).into_shape((3,4)).unwrap();
    println!("array:\n{}", array);

    let slice = array.slice(s![.., 1..3]);
    println!("slice:\n{}", slice);

    let slice2 = array.slice(s![1..2, 3..4]);
    println!("slice:\n{}", slice2);

    let slice3 = array.slice(s![1.., 1..]);
    println!("slice:\n{}", slice3);

    let slice4 = array.slice(s![.., ..]);
    println!("slice:\n{}", slice4);
}


fn main() {
    array_view();
    mut_array();
    slice_1d_array();
    slice_2d_array();
}
