fn main() {
    let array = [[1,2,3,4],
                 [5,6,7,8],
                 [9,10,11,12]];

    println!("array has {} items", array.len());

    for vector in &array {
        for item in vector.iter() {
            print!("{}\t", item);
        }
        println!("");
    }
}

