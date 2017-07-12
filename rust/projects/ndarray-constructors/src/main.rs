#![feature(inclusive_range_syntax)]
#[macro_use(array)]

extern crate ndarray;
use ndarray::Array;
use ndarray::Array1;
use ndarray::Array2;
use ndarray::Array3;


fn zero_1d_array() {
    println!("zero_1d_array");

    let array = Array1::<f32>::zeros((10));
    println!("{}", array);
    println!("{}", array[0]);

    let array_b = Array1::<i8>::zeros(10);
    println!("{}", array_b);
    println!("{}", array_b[0]);

    println!();
}


fn zero_2d_array() {
    println!("zero_2d_array");

    let array = Array2::<f32>::zeros((4, 3));
    println!("{}", array);
    println!("{}", array[[0,0]]);

    println!();
}


fn zero_3d_array() {
    println!("zero_3d_array");

    let array = Array3::<f32>::zeros((4, 3, 2));
    println!("{}", array);
    println!("{}", array[[0,0,0]]);

    println!();
}


fn identity_matrix() {
    println!("identity_matrix");

    let array = Array2::<f32>::eye(4);
    println!("{}", array);
    println!("{}", array[[0,0]]);

    let array = Array2::<i8>::eye(10);
    println!("{}", array);
    println!("{}", array[[0,0]]);

    println!();
}


fn construct_by_range() {
    println!("construct_by_range");

    let array1 = Array::range(0.0, 10.0, 1.0);
    println!("{}", array1);

    let array2 = Array::range(0.0, 10.0, 2.0);
    println!("{}", array2);

    let array3 = Array::range(0.0, 10.0, 1.5);
    println!("{}", array3);

    println!();
}


fn construct_by_range_neg() {
    println!("construct_by_range_neg");

    let array1 = Array::range(10.0, 0.0, -1.0);
    println!("{}", array1);

    let array2 = Array::range(10.0, 0.0, -2.0);
    println!("{}", array2);

    let array3 = Array::range(10.0, 0.0, -1.5);
    println!("{}", array3);

    println!();
}


fn construct_by_linspace() {
    println!("construct_by_linspace");

    let array1 = Array::linspace(1.0, 10.0, 10);
    println!("{}", array1);

    let array2 = Array::linspace(1.0, 10.0, 5);
    println!("{}", array2);

    let array3 = Array::linspace(1.0, 10.0, 3);
    println!("{}", array3);

    println!();
}


fn construct_by_linspace_rev() {
    println!("construct_by_linspace_rev");

    let array1 = Array::linspace(10.0, 1.0, 10);
    println!("{}", array1);

    let array2 = Array::linspace(10.0, 1.0, 5);
    println!("{}", array2);

    let array3 = Array::linspace(10.0, 1.0, 3);
    println!("{}", array3);

    println!();
}


fn construct_array_from_vector() {
    println!("construct_array_from_vector");

    let array1 = Array::from_vec(vec![10, 9, 8, 1]);
    println!("{}", array1);
    println!("{}", array1[0]);

    let array2 = Array::from_vec(vec![10.0, 9.0, 8.0, 1.0]);
    println!("{}", array2);
    println!("{}", array2[0]);

    let array3 = Array::from_vec(vec!["www", "root", "cz"]);
    println!("{}", array3);
    println!("{}", array3[0]);

    println!();
}


fn construct_array_from_iter() {
    println!("construct_array_from_iter");

    let array = Array::from_iter(0..10);
    println!("{}", array);
    println!("{}", array[5]);

    let array_b = Array::from_iter(0...10);
    println!("{}", array_b);
    println!("{}", array_b[5]);

    let array_c = Array::from_iter((0...100).filter(|x| (x % 3 == 0)));
    println!("{}", array_c);
    println!("{}", array_c[5]);

    let array_d = Array::from_iter((0...10).map(|x| (x * 42)));
    println!("{}", array_d);
    println!("{}", array_d[5]);
}


fn array_macro() {
    println!("array_macro");

    let array_a = array![1, 2, 3, 4];

    let array_b = array![[1, 2],
                         [3, 4]];

    let array_c = array![[[1, 2], [3, 4]],
                         [[5, 6], [7, 8]]];

    println!("{}", array_a);
    println!("{}", array_b);
    println!("{}", array_c);
}


fn main() {
    zero_1d_array();
    zero_2d_array();
    zero_3d_array();

    identity_matrix();
    construct_by_range();
    construct_by_range_neg();
    construct_by_linspace();
    construct_by_linspace_rev();

    construct_array_from_vector();
    construct_array_from_iter();
    array_macro();
}
