fn main() {
    // iterator (povsimnete si, ze je nemenny)
    let iter = 1..11;

    // pruchod sekvenci se ziskanim indexu a hodnoty kazdeho prvku
    for (index,item) in iter.enumerate() {
	println!("item[{}] = {}", index, item);
    }
}

