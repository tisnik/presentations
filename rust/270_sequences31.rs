use std::collections::BTreeSet;

fn print_btree_set(set: &BTreeSet<&str>) {
    for item in set {
        println!("{}", item);
    }
}

fn main() {
    let mut set1 = BTreeSet::new();
    let mut set2 = BTreeSet::new();

    set1.insert("podporucik");
    set1.insert("inspektor");
    set1.insert("praktikant");
    set1.insert("tovarnik");

    set2.insert("tovarnik");
    set2.insert("stevard");
    set2.insert("podkoni");
    set2.insert("inspektor");

    println!("Set1");
    print_btree_set(&set1);

    println!("\nSet2");
    print_btree_set(&set2);

    println!("\nUnion");
    for item in set1.union(&set2) {
        println!("{}", item);
    }

    println!("\nIntersetion");
    for item in set1.intersection(&set2) {
        println!("{}", item);
    }

    println!("\nDifference set1-set2");
    for item in set1.difference(&set2) {
        println!("{}", item);
    }

    println!("\nDifference set2-set1");
    for item in set2.difference(&set1) {
        println!("{}", item);
    }

    println!("\nSymmetric difference");
    for item in set1.symmetric_difference(&set2) {
        println!("{}", item);
    }
}

