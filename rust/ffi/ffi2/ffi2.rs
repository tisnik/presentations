#[link(name = "ffi2")]
extern {
    fn add(x:i32, y:i32) -> i32;
}

fn main() {
    let x:i32 = 1;
    let y:i32 = 2;
    let z = unsafe { add(x, y) };
    println!("{} + {} = {}", x, y, z);
}

