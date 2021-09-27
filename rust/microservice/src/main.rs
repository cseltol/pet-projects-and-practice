use std::io::prelude::*;
use std::net::{TcpStream, TcpListener};

fn main() {
    let listener = TcpListener::bind("localhost:6000").unwrap();
    for stream in listener.incoming() {
        let stream: TcpStream = stream.unwrap();

        println!("Connection established!");
    }
}
