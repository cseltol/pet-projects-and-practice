// Strings are similar to Vecs
// because they have alot of same methods and etc.
fn main() {
    // capacity
    // let mut push_string = String::with_capacity(4587520);
    // let mut capacity_counter = 0;

    // for _ in 0..100_000 {
    //     let capacity = push_string.capacity();
    //     if capacity != capacity_counter {
    //         println!("{}", capacity);
    //         capacity_counter = capacity;
    //     }
    //     push_string.push_str("push something");   
    // }
    // push_string.shrink_to_fit(); // if you want to add 1 more obj, capacity will double 
    // println!("Length: {}", push_string.capacity());

    // let mut my_str = String::from(".daer ot drah tib elttil a si gnirts sihT");
    // loop {
    //     let pop_res = my_str.pop();
    //     match pop_res {
    //         Some(char ) => print!("{}", char),
    //         None => break
    //     }
    // }

    let mut my_string = String::from("Age 18 Height: 185 Weight 70");
    my_string.retain(|char| char.is_alphabetic() || char == ' ');
    dbg!(my_string); // also we can use println!()
}
