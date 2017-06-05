// build.rs

use std::process::Command;
use std::env;
use std::path::Path;

fn main() {
    let out_dir = env::var("OUT_DIR").unwrap();

    // preklad
    Command::new("gcc").args(&["src/ffi1.c", "-c", "-fPIC", "-o"])
                       .arg(&format!("{}/ffi1.o", out_dir))
                       .status().unwrap();

    // import objektoveho souboru do staticke knihovny
    Command::new("ar").args(&["crus", "libffi1.a", "ffi1.o"])
                      .current_dir(&Path::new(&out_dir))
                      .status().unwrap();

    // predame prekladaci parametry
    println!("cargo:rustc-link-search=native={}", out_dir);
    println!("cargo:rustc-link-lib=static=ffi1");
}

