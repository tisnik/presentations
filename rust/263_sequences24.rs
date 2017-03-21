use std::collections::BTreeMap;

fn main() {
    let mut map = BTreeMap::new();

    map.insert("Trachta",      "inspektor");
    map.insert("Hlavacek",     "praktikant");
    map.insert("Bierhanzel",   "tovarnik");
    map.insert("Meyer",        "tovarnik");
    map.insert("Vaclav Kotek", "stevard");

    println!("Trachta: {:?}", map.get("Trachta"));
    println!("Novak:   {:?}", map.get("Novak"));
}

