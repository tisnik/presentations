extern crate ndarray;
use ndarray::Array;


fn fold_for_1d_array() {
    println!("fold_for_1d_array");

    let vector1 = Array::from_iter(1..11);

    let sum = vector1.fold(0, |acc, value| acc+value);

    let product = vector1.fold(1, |acc, value| acc*value);

    println!("vector1: {}", vector1);
    println!("sum: {}", sum);
    println!("product: {}", product);

    println!()
}


fn fold_for_2d_array() {
    println!("fold_for_2d_array");

    let array = Array::from_shape_vec((3,3), vec![1,2,3,4,5,6,7,8,9]).unwrap();

    let sum = array.fold(0, |acc, value| acc+value);
    let sum_offset = array.fold(1000, |acc, value| acc+value);

    let product = array.fold(1, |acc, value| acc*value);

    println!("array:\n{}\n", array);
    println!("sum: {}", sum);
    println!("sum_offset: {}", sum_offset);
    println!("product: {}", product);

    println!()
}




fn main() {
    fold_for_1d_array();
    fold_for_2d_array();
}
