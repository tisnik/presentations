fn main() {
    let value:u32 = 3;

    println!("{:032b}", value);

    println!("");
    for rot in 0..10 {
        println!("{:032b}", value.rotate_left(rot));
    }

    println!("");
    for rot in 0..10 {
        println!("{:032b}", value.rotate_right(rot));
    }

    println!("");
    for rot in 0..10 {
        println!("{:032b}", value << rot);
    }

    println!("");
    for rot in 0..10 {
        println!("{:032b}", value >> rot);
    }
}

