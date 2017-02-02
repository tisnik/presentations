fn main() {
    let array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    ];

    println!("array has {} items", array.len());

    for i in &array {
        println!("{}", i);
    }
}

