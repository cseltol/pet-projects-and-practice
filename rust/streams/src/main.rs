use std::{task::{Context, Poll}};
use async_std::task::block_on;
use futures::{SinkExt, StreamExt, channel::mpsc};

/// The Stream trait is similar to Future but
/// can yield multiple values before completing,
/// similar to the Iterator trait from the standart libary

trait Stream {
    /// The type of the value yielded by the stream
    type Item;
    /// Attempt to resolve the next item in the stream
    /// Returns 'Poll::Pending' if not ready,
    /// and 'Poll::Ready(None)' if the stream has completed
    fn poll_next(self: std::pin::Pin<&mut Self>,
    cx: &mut Context<'_>)
    -> Poll<Option<Self::Item>>;
}

/// One common example of Stream is the Receiver
/// for the channel type from features crate
async fn send_recv(nums: Vec<i32>) {
    const BUFFER_SIZE: usize = 10;
    let (mut tx, mut rx) = mpsc::channel::<i32>(BUFFER_SIZE);

    for i in nums.clone() {
        tx.send(i).await.unwrap();
    }
    drop(tx);
    // 'StreamExt::next' is similar to 'Iterator::next',
    // but returns a type that implements 'Future<Output = Option<T>>'.
    for i in nums {
        assert_eq!(Some(i), rx.next().await);
    }
    assert_eq!(None, rx.next().await);
    println!("There are no errors!");
}

fn main() {
    let v = vec![1, 2, 3, 42, 92];
    let f = send_recv(v);
    block_on(f);

    println!("Hello, world!");
}
