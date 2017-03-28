use std::collections::HashSet;

fn print_hashset(set: &HashSet<&str>) {
    for item in set {
        println!("{}", item);
    }
}

fn vec2set(v: Vec<&str>) -> HashSet<&str> {
    v.iter().cloned().collect()
}

fn main() {
    let set1 = vec2set(vec!["podporucik", "inspektor", "praktikant", "tovarnik"]);
    let set2 = vec2set(vec!["tovarnik", "stevard", "podkoni", "inspektor"]);

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

