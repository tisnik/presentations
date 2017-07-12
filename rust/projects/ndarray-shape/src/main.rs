extern crate ndarray;
use ndarray::Array;


fn construct_from_shape_vec() {
    println!("from_shape_vec");

    let array = Array::from_shape_vec((6), vec![1,2,3,4,5,6]).unwrap();
    println!("{}\n", array);

    let array_b = Array::from_shape_vec((2,3), vec![1,2,3,4,5,6]).unwrap();
    println!("{}\n", array_b);

    let array_c = Array::from_shape_vec((3,2), vec![1,2,3,4,5,6]).unwrap();
    println!("{}\n", array_c);

    let array_d = Array::from_shape_vec((1,6), vec![1,2,3,4,5,6]).unwrap();
    println!("{}\n", array_d);

    let array_e = Array::from_shape_vec((2,2,2), vec![1,2,3,4,5,6,7,8]).unwrap();
    println!("{}\n", array_e);

    println!();
}


fn reshape_array() {
    println!("reshape_array");

    let array = Array::from_iter(0..12);
    println!("{}\n", array);

    let array_b = Array::from_iter(0..12).into_shape((3,4)).unwrap();
    println!("{}\n", array_b);

    let array_c = Array::from_iter(0..12).into_shape((4,3)).unwrap();
    println!("{}\n", array_c);

    let array_d = Array::from_iter(0..12).into_shape((12,1)).unwrap();
    println!("{}\n", array_d);

    let array_e = Array::from_iter(0..12).into_shape((2,2,3)).unwrap();
    println!("{}\n", array_e);

    let array_f = Array::from_iter(0..12).into_shape((2,3,2)).unwrap();
    println!("{}\n", array_f);

    let array_g = Array::from_iter(0..12).into_shape((3,2,2)).unwrap();
    println!("{}\n", array_g);

    let array_h = Array::from_iter(0..16).into_shape((2, 2, 2, 2)).unwrap();
    println!("{}\n", array_h);

    println!();
}


fn main() {
    reshape_array();
    construct_from_shape_vec();
}
