use std::collections::HashSet;

fn print_hashset(set: &HashSet<&str>) {
    for item in set {
        println!("{}", item);
    }
}

fn main() {
    let mut set = HashSet::new();

    set.insert("podporucik");
    set.insert("inspektor");
    set.insert("praktikant");
    set.insert("tovarnik");
    set.insert("tovarnik");
    set.insert("stevard");
    set.insert("podkoni");

    print_hashset(&set);
}

