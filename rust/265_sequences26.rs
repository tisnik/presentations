use std::collections::HashMap;
use std::collections::BTreeMap;

fn print_hashmap_keys(map: &HashMap<&str, &str>) {
    for key in map.keys() {
        println!("{}", key);
    }
}

fn print_btreemap_keys(map: &BTreeMap<&str, &str>) {
    for key in map.keys() {
        println!("{}", key);
    }
}

fn main() {
    let mut map1 = HashMap::new();
    let mut map2 = BTreeMap::new();

    map1.insert("Zdenek",       "podporucik");
    map1.insert("Trachta",      "inspektor");
    map1.insert("Hlavacek",     "praktikant");
    map1.insert("Bierhanzel",   "tovarnik");
    map1.insert("Meyer",        "tovarnik");
    map1.insert("Vaclav Kotek", "stevard");
    map1.insert("Ales",         "podkoni");

    print_hashmap_keys(&map1);

    println!("-------------------------------");

    map2.insert("Zdenek",       "podporucik");
    map2.insert("Trachta",      "inspektor");
    map2.insert("Hlavacek",     "praktikant");
    map2.insert("Bierhanzel",   "tovarnik");
    map2.insert("Meyer",        "tovarnik");
    map2.insert("Vaclav Kotek", "stevard");
    map2.insert("Ales",         "podkoni");

    print_btreemap_keys(&map2);
}

