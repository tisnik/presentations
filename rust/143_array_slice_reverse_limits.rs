fn main() {
    let array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
    let array2 = &array[8..2];

    for i in array2.iter() {
        println!("{}", i);
    }
}

