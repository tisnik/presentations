extern crate ndarray;
use ndarray::Array;


fn map_for_1d_array() {
    println!("map_for_1d_array");

    let vector1 = Array::from_iter(0..12);

    let vector2 = vector1.map(|x| 2* *x);

    let vector3 = vector1.map(|x| *x % 2);

    let vector4 = vector1.map(|x| *x % 2 == 0);

    println!("vector1: {}", vector1);
    println!("vector2: {}", vector2);
    println!("vector3: {}", vector3);
    println!("vector4: {}", vector4);

    println!()
}


fn mapv_for_1d_array() {
    println!("mapv_for_1d_array");

    let vector1 = Array::from_iter(0..12);

    let vector2 = vector1.mapv(|x| 2*x);

    let vector3 = vector1.mapv(|x| x % 2);

    let vector4 = vector1.mapv(|x| x % 2 == 0);

    println!("vector1: {}", vector1);
    println!("vector2: {}", vector2);
    println!("vector3: {}", vector3);
    println!("vector4: {}", vector4);

    println!()
}


fn map_for_1d_array_auto_deref() {
    println!("map_for_1d_array_auto_deref");

    let vector1 = Array::from_iter(0..12);

    let vector2 = vector1.map(|x| 2*x);

    let vector3 = vector1.map(|x| x % 2);

    let vector4 = vector1.map(|x| x % 2 == 0);

    println!("vector1: {}", vector1);
    println!("vector2: {}", vector2);
    println!("vector3: {}", vector3);
    println!("vector4: {}", vector4);

    println!()
}


fn map_for_2d_array() {
    println!("map_for_2d_array");

    let array1 = Array::from_iter(0..12).into_shape((3,4)).unwrap();

    let array2 = array1.map(|x| 2* *x);

    let array3 = array1.map(|x| *x % 2);

    let array4 = array1.map(|x| *x % 2 == 0);

    println!("array1:\n{}\n", array1);
    println!("array2:\n{}\n", array2);
    println!("array3:\n{}\n", array3);
    println!("array4:\n{}\n", array4);

    println!()
}


fn map_for_3d_array() {
    println!("map_for_3d_array");

    let array1 = Array::from_iter(0..27).into_shape((3,3,3)).unwrap();

    let array2 = array1.map(|x| 2* *x);

    let array3 = array1.map(|x| *x % 2);

    let array4 = array1.map(|x| *x % 2 == 0);

    println!("array1:\n{}\n", array1);
    println!("array2:\n{}\n", array2);
    println!("array3:\n{}\n", array3);
    println!("array4:\n{}\n", array4);

    println!()
}


fn main() {
    map_for_1d_array();
    mapv_for_1d_array();
    map_for_1d_array_auto_deref();
    map_for_2d_array();
    map_for_3d_array();
}
