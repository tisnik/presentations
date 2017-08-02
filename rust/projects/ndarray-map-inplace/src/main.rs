extern crate ndarray;
use ndarray::Array;


fn mapv_inplace_for_1d_array() {
    println!("mapv_inplace_for_1d_array");

    let mut vector1 = Array::from_iter(0..12);

    println!("vector1: {}", vector1);

    vector1.mapv_inplace(|x| x*2);

    println!("vector1: {}", vector1);

    vector1.mapv_inplace(|x| if x<10 {0} else {1});

    println!("vector1: {}", vector1);

    println!()
}


fn mapv_into_for_1d_array() {
    println!("mapv_into_for_1d_array");

    let vector1 = Array::from_iter(0..12);
    let vector2 = vector1.mapv_into(|x| x*2);
    let vector3 = vector2.mapv_into(|x| if x<10 {0} else {1});

    println!("vector3: {}", vector3);

    println!()
}


fn mapv_inplace_for_2d_array() {
    println!("mapv_inplace_for_2d_array");

    let mut array1 = Array::from_iter(0..12).into_shape((3,4)).unwrap();

    println!("array1:\n{}\n", array1);

    array1.mapv_inplace(|x| if x%2 == 0 {0} else {1});

    println!("array1:\n{}\n", array1);

    println!()
}


fn mapv_inplace_for_3d_array() {
    println!("mapv_inplace_for_3d_array");

    let mut array1 = Array::from_iter(0..27).into_shape((3,3,3)).unwrap();

    println!("array1:\n{}\n", array1);

    array1.mapv_inplace(|x| if x%2 == 0 {0} else {1});

    println!("array1:\n{}\n", array1);

    println!()
}


fn main() {
    mapv_inplace_for_1d_array();
    mapv_inplace_for_2d_array();
    mapv_inplace_for_3d_array();
    mapv_into_for_1d_array();
}
