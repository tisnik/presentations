use std::env;

fn main() {
    let env_vars = env::vars_os();

    let min = env_vars.count() % 5;
    let max = min + 5;

    println!("min: {}", min);
    println!("max: {}", max);

    let array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
    let array2 = &array[min..max];
   
    for i in array2.iter() {
        println!("{}", i);
    }
}

