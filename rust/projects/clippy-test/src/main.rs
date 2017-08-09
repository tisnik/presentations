fn main() {
    print!("Hello, world!\n");

    let mut a = 123456789;
    let mut b = 123i32;

    println!("{}", a);
    println!("{}", b);

    a = a + 1;
    println!("{}", a);

    b = 2 * b;
    println!("{}", b);

    let foo = 42;
    println!("{}", foo);

    let pi = 3.14;
    println!("{}", pi);

    let e = 2.718;
    println!("{}", e);

    let s = 1.4142;
    println!("{}", s);

    let x = true;

    if x == true {
        println!("T");
    }

    if x == false {
        println!("nil");
    }

    println!("{}",
        match x {
            true => 1,
            false => 2
        }
    );
}
