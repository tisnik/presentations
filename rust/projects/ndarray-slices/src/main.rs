#[macro_use]
extern crate ndarray;
use ndarray::Array;
use ndarray::Array2;


fn slice_1d_array() {
    println!("slice_1d_array");

    let array = Array::from_iter(0..12);
    println!("original array:\n{}\n", array);

    let slice = array.slice(s![3..8]);
    println!("slice 3..8:\n{}\n", slice);

    let slice2 = array.slice(s![..8]);
    println!("slice ..8:\n{}\n", slice2);

    let slice3 = array.slice(s![3..]);
    println!("slice 3..:\n{}\n", slice3);

    let slice4 = array.slice(s![..]);
    println!("slice ..:\n{}\n", slice4);

    let slice5 = array.slice(s![3..4]);
    println!("slice 3..4:\n{}\n", slice5);

    let slice6 = array.slice(s![4..4]);
    println!("slice 4..4:\n{}\n", slice6);
}


fn slice_1d_array_negative_indexes() {
    println!("slice_1d_array_negative_indexes");

    let array = Array::from_iter(0..12);
    println!("original array:\n{}\n", array);

    let slice = array.slice(s![-10..-1]);
    println!("slice -10..-1:\n{}\n", slice);

    let slice2 = array.slice(s![..-1]);
    println!("slice2 ..-1:\n{}\n", slice2);

    let slice3 = array.slice(s![..-8]);
    println!("slice ..-8:\n{}\n", slice3);

    let slice4 = array.slice(s![-3..]);
    println!("slice -3..:\n{}\n", slice4);

    let slice5 = array.slice(s![-1..]);
    println!("slice -1..:\n{}\n", slice5);
}


fn slice_1d_array_explicit_step() {
    println!("slice_1d_array_explicit_step");

    let array = Array::from_iter(0..12);
    println!("original array:\n{}\n", array);

    let slice = array.slice(s![3..8;2]);
    println!("slice 3..8;2:\n{}\n", slice);

    let slice2 = array.slice(s![..8;2]);
    println!("slice ..8;2:\n{}\n", slice2);

    let slice3 = array.slice(s![3..;2]);
    println!("slice 3..;2:\n{}\n", slice3);

    let slice4 = array.slice(s![..;2]);
    println!("slice ..;2:\n{}\n", slice4);
}


fn slice_1d_array_negative_step() {
    println!("slice_1d_array_negative_step");

    let array = Array::from_iter(0..12);
    println!("original array:\n{}\n", array);

    let slice = array.slice(s![3..8;-2]);
    println!("slice 3..8;-2:\n{}\n", slice);

    let slice2 = array.slice(s![..8;-2]);
    println!("slice ..8;-2:\n{}\n", slice2);

    let slice3 = array.slice(s![3..;-2]);
    println!("slice 3..;-2:\n{}\n", slice3);

    let slice4 = array.slice(s![..;-2]);
    println!("slice ..;-2:\n{}\n", slice4);

    let slice5 = array.slice(s![..;-1]);
    println!("slice ..;-1:\n{}\n", slice5);
}


fn slice_2d_array() {
    println!("slice_2d_array");

    let array = Array::from_iter(10..30).into_shape((4,5)).unwrap();
    println!("original array:\n{}\n", array);

    let slice = array.slice(s![.., 1..3]);
    println!("slice: .., 1..3\n{}\n", slice);

    let slice2 = array.slice(s![1..2, 3..4]);
    println!("slice: 1..2, 3..4\n{}\n", slice2);

    let slice3 = array.slice(s![1.., 1..]);
    println!("slice: 1.., 1..\n{}\n", slice3);

    let slice4 = array.slice(s![.., ..]);
    println!("slice: .., ..\n{}\n", slice4);

    let slice5 = array.slice(s![..-1, ..-1]);
    println!("slice: ..-1, ..-1\n{}\n", slice5);
}


fn slice_2d_array_explicit_steps() {
    println!("slice_2d_array_explicit_steps");

    let array = Array::from_iter(10..30).into_shape((4,5)).unwrap();
    println!("original array:\n{}\n", array);

    let slice = array.slice(s![..;2, 1..3]);
    println!("slice: ..;2, 1..3\n{}\n", slice);

    let slice2 = array.slice(s![1..2;-1, 3..4;-1]);
    println!("slice: 1..2;-1, 3..4;-1\n{}\n", slice2);

    let slice3 = array.slice(s![1..;2, 1..;2]);
    println!("slice: 1..;2, 1..;2\n{}\n", slice3);

    let slice4 = array.slice(s![.., ..;-1]);
    println!("slice: .., ..;-1\n{}\n", slice4);

    let slice5 = array.slice(s![..;-1, ..;-1]);
    println!("slice: ..;-1, ..;-1\n{}\n", slice5);

    let slice6 = array.slice(s![..;-1, ..]);
    println!("slice: ..;-1, ..\n{}\n", slice6);
}


fn main() {
    slice_1d_array();
    slice_1d_array_negative_indexes();
    slice_1d_array_explicit_step();
    slice_1d_array_negative_step();
    slice_2d_array();
    slice_2d_array_explicit_steps();
}
