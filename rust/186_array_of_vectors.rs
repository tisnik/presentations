fn main() {
    let array:[Vec<i32>;4] = [vec![1],
                              vec![2,3],
                              vec![4,5,6],
                              vec![7,8,9,0]];

    println!("array has {} items", array.len());

    for vec1 in array.iter() {
        for i in vec1.iter() {
            print!("{} ", i);
        }
        println!("");
    }

}

