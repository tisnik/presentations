fn main() {
    let array  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15];
    let vector:Vec<_> = array.iter()
                             .take(10)
                             .filter(|&x| x % 3 ==0)
                             .map(|&x| x*2)
                             .collect();

    println!("vector has {} items", vector.len());

    for item in &vector {
        println!("{}", item);
    }
}

