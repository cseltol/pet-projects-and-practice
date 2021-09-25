use crate::BitcoinBlock::{Block, Genesis};

enum BitcoinBlock {
    Block(i32, Box<BitcoinBlock>),
    Genesis,
}

// Box<T>
fn main() {
    let x = Box::new(7);
    println!("x := {}", x); 
    
    let genesis_block = Genesis;
    let first_block = Block(1, Box::new(genesis_block));
    let second_block = Block(2, Box::new(first_block));

    print_block(second_block);
}

fn print_block(block: BitcoinBlock) {
    match block {
        Genesis => println!("Genesis Block"),
        Block(id, prev_block_in_box) => {
            println!("Block id := {}", id);
            let prev_block = *prev_block_in_box;
            match prev_block {
                Genesis => println!("Previous Block is Genesis Block"),
                Block(id, _) => println!("Previous Block ID := {}", id),
            }
        }
    }
}
