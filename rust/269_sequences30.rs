use std::collections::HashSet;

fn print_hashset(set: &HashSet<&str>) {
    for item in set {
        println!("{}", item);
    }
}

fn main() {
    let mut set1 = HashSet::new();
    let mut set2 = HashSet::new();

    set1.insert("podporucik");
    set1.insert("inspektor");
    set1.insert("praktikant");
    set1.insert("tovarnik");

    set2.insert("tovarnik");
    set2.insert("stevard");
    set2.insert("podkoni");
    set2.insert("inspektor");

    println!("Set1");
    print_hashset(&set1);

    println!("\nSet2");
    print_hashset(&set2);

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

