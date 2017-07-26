extern crate ndarray;
use ndarray::Array;


fn array_operators() {
    println!("array_operators");

    let array1 = Array::range(0.0, 10.0, 1.0);
    let array2 = Array::range(0.0, 5.0, 0.5);

    println!("array1: {}", array1);
    println!("array2: {}", array2);

    println!("add:    {}", &array1 + &array2);
    println!("sub:    {}", &array1 - &array2);
    println!("mul:    {}", &array1 * &array2);
    println!("div:    {}", &array1 / &array2);

    println!();
}



fn array_2D_operators() {
    println!("array_2D_operators");

    let array1 = Array::from_iter(10..30).into_shape((4,5)).unwrap();
    let array2 = Array::from_iter(100..120).into_shape((4,5)).unwrap();

    println!("array1:\n{}\n", array1);
    println!("array2:\n{}\n", array2);

    println!("add:\n{}\n", array1 * array2);

    println!();
}



fn array_consume_operators() {
    println!("array_consume_operators");

    let array1 = Array::range(0.0, 10.0, 1.0);
    let array2 = Array::range(0.0, 5.0, 0.5);

    println!("array1: {}", array1);
    println!("array2: {}", array2);

    let result = array1 + array2;

    println!("result: {}", result);

    println!();
}


fn array_in_place_operators() {
    println!("array_in_place_operators");

    let array1 = Array::range(0.0, 10.0, 1.0);
    let mut array2 = Array::range(0.0, 5.0, 0.5);

    println!("array1: {}", array1);
    println!("array2: {}", array2);

    array2 += &array1;

    println!("result: {}", array2);

    println!();
}


fn array_broadcasting() {
    println!("array_broadcasting");

    let array1 = Array::from_iter(0..12).into_shape((3,4)).unwrap();
    let array2 = Array::from_iter(0..4);

    println!("array1:\n{}\n", array1);
    println!("array2:\n{}\n", array2);

    let result = array1 * array2;
    println!("result:\n{}", result);

    println!();
}


fn main() {
    array_operators();
    array_2D_operators();
    array_consume_operators();
    array_in_place_operators();
    array_broadcasting();
}
