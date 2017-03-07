fn main() {
    let value = 42;
    println!("|{}|", value);
    println!("|{:.10}|", value);
    println!("|{:.>10}|", value);
    println!("|{:.<10}|", value);
    println!("|{:.^10}|", value);

    let str = "hello";
    println!("|{}|", str);
    println!("|{:20}|", str);
    println!("|{:_>20}|", str);
    println!("|{:_<20}|", str);
    println!("|{:_^20}|", str);
}

