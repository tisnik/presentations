// balicek gcc zajisti preklad a vytvoreni knihovny za nas
extern crate gcc;

fn main() {
    // preklad a vytvoreni knihovny
    gcc::compile_library("libffi4.a", &["src/ffi4.c"]);
}
