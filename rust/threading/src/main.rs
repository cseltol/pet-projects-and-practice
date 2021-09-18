use std::thread;

fn main() {
    let handle: thread::JoinHandle<i32> = thread::spawn(|| {
        println!("Hello, world!");
        42
    });
    let value = handle.join().unwrap();
    assert_eq!(value, 42)
}
