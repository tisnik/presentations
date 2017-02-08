fn main() {
    let vec2:Vec<Vec<_>> = vec![vec![1,2,3],
                                vec![4],
                                vec![5,6,7,8,]];
    println!("vector has {} items", vec2.len());

    for vec1 in vec2.iter() {
        for i in vec1.iter() {
            print!("{} ", i);
        }
        println!("");
    }

}

