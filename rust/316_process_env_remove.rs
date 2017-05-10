use std::process::Command;

fn main() {
    let process = Command::new("ls").env_remove("PATH").spawn();

    match process {
        Ok(mut child) => {
            println!("spawn ok");
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

