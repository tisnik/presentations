use std::collections::HashMap;

fn get_role_name(role: Option<&&str>) -> String {
    match role {
        None            => "neobsazeno".to_string(),
        Some(role_name) => role_name.to_string()
    }
}

fn print_role(map: &HashMap<&str, &str>, name: &str) -> () {
    let role = map.get(name);
    println!("{}: {}", name, get_role_name(role));
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

