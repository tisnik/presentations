fn main() {
    let iter1 = 1..;
    let iter2 = iter1.filter(|x| x % 2 == 0);
    let iter3 = iter2.take(10);

    // pruchod sekvenci se ziskanim indexu a hodnoty kazdeho prvku
    for (index,item) in iter3.enumerate() {
	println!("item[{}] = {}", index, item);
    }
}

