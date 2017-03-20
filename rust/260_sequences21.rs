use std::collections::HashMap;

fn print_map_values(map: &HashMap<&str, &str>) {
    for key in map.values() {
        println!("{}", key);
    }
}

fn main() {
    let mut map = HashMap::new();

    print_map_values(&map);

    map.insert("Trachta",      "inspektor");
    map.insert("Hlavacek",     "praktikant");
    map.insert("Bierhanzel",   "tovarnik");
    map.insert("Meyer",        "tovarnik");
    map.insert("Vaclav Kotek", "stevard");

    print_map_values(&map);
}

