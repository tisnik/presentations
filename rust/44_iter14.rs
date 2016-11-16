fn main() {
    let iter1 = 1..;

    // pruchod sekvenci se ziskanim indexu a hodnoty kazdeho prvku
    for (index,item) in iter1.enumerate() {
	println!("item[{}] = {}", index, item);
    }
}

