use std::collections::HashMap;

fn print_role(map: &HashMap<&str, &str>, name: &str) -> () {
    let role = map.get(name);
    match role {
        None            => println!("{}: neobsazeno", name),
        Some(role_name) => println!("{}: {}", name, role_name)
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

