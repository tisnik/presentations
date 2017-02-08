fn main() {
    let vec2:Vec<[i32;3]> = vec![[1,2,3],
                                 [4,5,6],
                                 [7,8,9]];
    println!("vector has {} items", vec2.len());

    for array in vec2.iter() {
        for i in array.iter() {
            print!("{} ", i);
        }
        println!("");
    }

}

