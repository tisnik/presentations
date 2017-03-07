fn main() {
    let value = 0.5;

    for w in 1 .. 11 {
        println!("width={}", w);
        for p in 1 .. (w-1) {
            println!("|{:width$.precision$}|", value, width=w, precision=p);
        }
        println!("");
    }
}

