use std::collections::HashMap;

fn print_role(map: &HashMap<&str, &str>, name: &str) -> () {
    let role = map.get(name);
    if role.is_none() {
        println!("{}: neobsazeno", name);
    } else {
        println!("{}: {}", name, role.unwrap());
    }
}

fn main() {
    let mut map = HashMap::new();

    map.insert("Trachta",      "inspektor");
    map.insert("Hlavacek",     "praktikant");
    map.insert("Bierhanzel",   "tovarnik");
    map.insert("Meyer",        "tovarnik");
    map.insert("Vaclav Kotek", "stevard");

    print_role(&map, "Trachta");
    print_role(&map, "Novak");
}

