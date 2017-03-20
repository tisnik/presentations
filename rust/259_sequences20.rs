use std::collections::HashMap;

fn print_map_keys(map: &HashMap<&str, &str>) {
    for key in map.keys() {
        println!("{}", key);
    }
}

fn main() {
    let mut map = HashMap::new();

    print_map_keys(&map);

    map.insert("Trachta",      "inspektor");
    map.insert("Hlavacek",     "praktikant");
    map.insert("Bierhanzel",   "tovarnik");
    map.insert("Meyer",        "tovarnik");
    map.insert("Vaclav Kotek", "stevard");

    print_map_keys(&map);
}

