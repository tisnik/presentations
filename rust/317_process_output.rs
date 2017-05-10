use std::process::Command;
use std::process::Stdio;
use std::io::Read;

fn main() {
    let process = Command::new("ls").arg("-1").stdout(Stdio::piped()).spawn();

    match process {
        Ok(mut child) => {
            println!("spawn ok");
            {
                let mut buffer = String::new();
                let stdout = child.stdout.as_mut().unwrap();
                match stdout.read_to_string(&mut buffer) {
                    Ok(read_bytes) => {
                        println!("read {} bytes", read_bytes);
                        println!("{}", buffer);
                    }
                    Err(err) => {
                        println!("read error: {}", err);
                    }
                }
            }
            match child.wait() {
                Ok(code) => {
                    println!("process exited with code: {}", code);
                }
                Err(err) => {
                    println!("failed to wait on child: {}", err);
                }
            }
        }
        Err(err) => {
            println!("spawn error: {}", err);
        }
    }

}

