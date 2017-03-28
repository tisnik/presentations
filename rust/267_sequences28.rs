use std::collections::BTreeSet;

fn print_hashset(set: &BTreeSet<&str>) {
    for item in set {
        println!("{}", item);
    }
}

fn main() {
    let mut set = BTreeSet::new();

    set.insert("podporucik");
    set.insert("inspektor");
    set.insert("praktikant");
    set.insert("tovarnik");
    set.insert("tovarnik");
    set.insert("stevard");
    set.insert("podkoni");

    print_hashset(&set);
}

