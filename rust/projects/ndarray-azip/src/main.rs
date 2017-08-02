#[macro_use(azip)]
extern crate ndarray;
use ndarray::Array;
use ndarray::Zip;


fn zip_for_1d_array() {
    println!("zip_for_1d_array");

    let vector1 = Array::from_iter(1..11);
    let vector2 = Array::from_iter(1..11);

    let mut result = Array::zeros((10));

    Zip::from(&mut result)
         .and(&vector1)
         .and(&vector2)
         .apply(|result, &vector1, &vector2| {
              *result = vector1 + vector2
         });

    println!("vector1: {}", vector1);
    println!("vector2: {}", vector2);
    println!("result sum: {}", result);

    println!()
}



fn zip_for_1d_array_more_producers() {
    println!("zip_for_1d_array_more_producers");

    let vector1 = Array::from_iter(1..11);
    let vector2 = Array::from_iter(1..11);
    let vector3 = Array::from_vec(vec![1,2,3,1,2,3,1,2,3,1000]);
    let vector4 = Array::from_vec(vec![1,1,1,2,2,2,3,3,3,4]);

    let mut result = Array::zeros((10));

    Zip::from(&mut result)
         .and(&vector1)
         .and(&vector2)
         .and(&vector3)
         .and(&vector4)
         .apply(|result, &vector1, &vector2, &vector3, &vector4| {
              *result = vector1 + vector2 * vector3 / vector4
         });

    println!("vector1: {}", vector1);
    println!("vector2: {}", vector2);
    println!("vector3: {}", vector3);
    println!("vector4: {}", vector4);
    println!("result sum: {}", result);

    println!()
}



fn azip_for_1d_array() {
    println!("azip_for_1d_array");

    let vector1 = Array::from_iter(1..11);
    let vector2 = Array::from_iter(1..11);

    let mut result = Array::zeros((10));

    azip!(mut result, vector1, vector2 in { *result = vector1 + vector2 });

    println!("vector1: {}", vector1);
    println!("vector2: {}", vector2);
    println!("result sum: {}", result);

    let mut result_mul = Array::zeros((10));

    azip!(mut result_mul, vector1, vector2 in { *result_mul = vector1 * vector2 });
    println!("result_mul: {}", result_mul);

    println!()
}



fn main() {
    zip_for_1d_array();
    zip_for_1d_array_more_producers();
    azip_for_1d_array();
}
