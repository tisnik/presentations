use std::io::BufRead;
use std::io::BufReader;
use std::fs::File;

fn read_content(fin: &File) {
    let reader = BufReader::new(fin);

    for line in reader.lines() {
        match line {
            Ok(content) => {
                println!("{}", content);
            }
            Err(error) => {
                println!("stdin read error: {}", error);
            }
        }
    }
}

fn main() {
    match File::open("/etc/passwd") {
        Ok(fin) => {
            read_content(&fin);
        }
        Err(error) => {
            println!("file open error: {}", error);
        }
    }
}

