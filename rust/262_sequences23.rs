use std::collections::HashMap;

fn print_map(map: &HashMap<&str, &str>) {
    if map.is_empty() {
        println!("empty collection");
    } else {
        for (name, role) in map.iter() {
            println!("{:15} \"{}\"", name, role);
        }
    }
    println!("");
}

fn main() {
    let mut map = HashMap::new();

    print_map(&map);

    map.insert("Trachta",      "inspektor");
    map.insert("Hlavacek",     "praktikant");
    map.insert("Bierhanzel",   "tovarnik");
    map.insert("Meyer",        "tovarnik");
    map.insert("Vaclav Kotek", "stevard");

    print_map(&map);

    for (_, role) in map.iter_mut() {
        *role = "?"
    }

    print_map(&map);
}

