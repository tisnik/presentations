use std::collections::BTreeMap;

fn print_map(map: &BTreeMap<&str, &str>) {
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
    let mut map = BTreeMap::new();

    print_map(&map);

    map.insert("Trachta",      "inspektor");
    map.insert("Hlavacek",     "praktikant");
    map.insert("Bierhanzel",   "tovarnik");
    map.insert("Meyer",        "tovarnik");
    map.insert("Vaclav Kotek", "stevard");

    print_map(&map);

    map.insert("Bierhanzel",   "neobsazen");
    map.insert("Meyer",        "neobsazen");

    print_map(&map);

    map.remove("Bierhanzel");
    map.remove("Meyer");

    print_map(&map);

    map.clear();

    print_map(&map);
}

