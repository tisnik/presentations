fn main() {
    let array = [[1,2,3,4],
                 [5,6,7,8],
                 [9,10,11,12]];

    println!("array has {} items", array.len());

    for i in 0..array.len() {
        for j in 0..array[i].len() {
            print!("{}\t", array[i][j]);
        }
        println!("");
    }
}

