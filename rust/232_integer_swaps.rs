fn main() {
    let value:u32 = 0xcafebabe;

    println!("{:x}", value);
    println!("{:x}", value.swap_bytes());
    println!("{:x}", u32::from_le(value));
    println!("{:x}", u32::from_be(value));
}

