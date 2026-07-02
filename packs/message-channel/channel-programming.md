---
title: "Channel (programming)"
source: https://en.wikipedia.org/wiki/Channel_(programming)
domain: message-channel
license: CC-BY-SA-4.0
tags: message channel api, message port pair, channel messaging, transferable object handoff
fetched: 2026-07-02
---

# Channel (programming)

In computing, a **channel** is a model for interprocess communication and synchronization via message passing. A message may be sent over a channel, and another process or thread is able to receive messages sent over a channel it has a reference to, as a stream. Different implementations of channels may be buffered or not, and either synchronous or asynchronous.

## libthread channels

The multithreading library, libthread, which was first created for the operating system Plan 9, offers inter-thread communication based on fixed-size channels.

## OCaml events

The OCaml event module offers typed channels for synchronization. When the module's send and receive functions are called, they create corresponding send and receive events which can be synchronized.

## Examples

### Lua Love2D

The Love2D library which uses the Lua programming language implements channels with push and pop operations similar to stacks. The pop operation will block so as long as there is data resident on the stack. A demand operation is equivalent to pop, except it will block until there is data on the stack

```mw
-- A string containing code which will be interpreted by a function such as loadstring(),
-- but on the C side to start a native thread.

local threadCode = [[
    love.thread.getChannel("test"):push("Hello world!")
]]

function love.load()
    -- Start the thread.
    
    thread = love.thread.newThread(threadCode)
    thread:start()
    
    -- The thread will block until "Hello world!" is popped off channel test's stack.
    -- Because the channel can be popped from before the thread first executes, there may not be data on the stack.
    -- in that case use :demand() instead of :pop() because :demand() will block until there is data on the stack and then return the data.
    
    print(love.thread.getChannel("test"):demand())
    
    -- The thread can now finish.
end
```

### XMOS XC

The XMOS programming language XC provides a primitive type "Chan" and two operators "<:" and ":>" for sending and receiving data from a channel.

In this example, two hardware threads are started on the XMOS, running the two lines in the "par" block. The first line transmits the number 42 through the channel while the second waits until it is received and sets the value of x. The XC language also allows asynchronous receiving on channels through a select statement.

```mw
chan c;
int x;
par {
  c <: 42;
  c :> x;
}
```

### Go

This snippet of Go code performs similarly to the XC code. First the channel c is created, then a goroutine is spawned which sends 42 through the channel. When the number is put in the channel x is set to 42. Go allows channels to buffer contents, as well as non blocking receiving through the use of a select block.

```mw
c := make(chan int)

go func() {c <- 42}()

x := <- c
```

### Rust

Rust provides asynchronous channels for communication between threads. Channels allow a unidirectional flow of information between two endpoints: the `Sender` and the `Receiver`.

```mw
use std::sync::mpsc;
use std::thread;

fn main() {
    let (tx, rx) = mpsc::channel();

    thread::spawn(move || {
        tx.send(123).unwrap();
    });

    let result = rx.recv();
    println!("{:?}", result);
}
```

## Applications

In addition to their fundamental use for interprocess communication, channels can be used as a primitive to implement various other concurrent programming constructs which can be realized as streams. For example, channels can be used to construct futures and promises, where a future is a one-element channel, and a promise is a process that sends to the channel, fulfilling the future. Similarly, iterators can be constructed directly from channels.

## List of implementations

List of non-standard, library-based implementations of channels

- For Scala:
  - CSO -- Communicating Scala Objects is a complete DSL for channel-based communication and concurrency whose semantic primitives are generalizations of the OCCAM primitives. CSO has been used since 2007 in the teaching of concurrent programming, and relevant lectures can be found with the ThreadCSO implementation.

- For C++:
  - stlab This implementation supports splits, and different merge and zip operations. Different executors can be attached to the individual nodes.

- For Rust:
  - Tokio
  - async-channel
  - crossbeam
