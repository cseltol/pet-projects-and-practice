use std::thread;
use std::time::Duration;

fn main() {

    let v = vec![42, 62, 92];

    let handle_vec = thread::spawn(move || {
        thread::sleep(Duration::from_millis(1000));
        println!("Here's a vector: {:?}", v);
    });


    let handle = thread::spawn(|| {
        for i in 1..10 {
            println!("Number {} from the child thread", i);
            thread::sleep(Duration::from_millis(1000));
        }
    });
    // Will block main thread
    // handle.join().unwrap();

    for i in 1..5 {
        println!("Number {} from the main thread", i);
        thread::sleep(Duration::from_millis(1000));
    }

    handle.join().unwrap();
    handle_vec.join().unwrap();
}
