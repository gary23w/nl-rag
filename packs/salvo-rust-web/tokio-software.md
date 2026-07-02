---
title: "Tokio (software)"
source: https://en.wikipedia.org/wiki/Tokio_(software)
domain: salvo-rust-web
license: CC-BY-SA-4.0
tags: salvo rust framework, rust web server framework, rust handler tree, salvo flexible middleware
fetched: 2026-07-02
---

# Tokio (software)

**Tokio** is a software library for the Rust programming language. It provides a runtime and functions that enable the use of asynchronous I/O, allowing for concurrency in regards to task completion.

Tokio was released in August 2016 for Rust, a general-purpose programming language. Developed by Carl Lerche, Tokio began as a network application framework and supports features such as socket listening and broadcasting, allowing messages to be transferred between computers.

## History

Tokio began in August 2016 by Carl Lerche as a network application framework for Rust built on futures, allowing for network-based middleware and a non-blocking, or asynchronous, implementation of readiness interest to the reactor. Tokio was inspired by Finagle, a Scala-based asynchronous remote procedure call (RPC) system developed at Twitter for Java virtual machines (JVM), allowing distributed systems to communicate within a JVM. Tokio utilizes the lower-level Rust crate `mio`, itself using system calls such as epoll (Linux), kqueue (FreeBSD), and the input/output completion port (IOCP) API (Windows). For Linux it can also use io_uring via tokio-uring. The name "Tokio" is derived from Tokyo and mio, and the Tokio logo vaguely resembles the city emblem of Tokyo. The preliminary version of Tokio was released in January 2017, followed by a full release in December 2020. In 2017, Tokio received a grant from the Mozilla Open Source Support fund. In April 2021, Tokio funded its first paid contributor, Alice Ryhl, for her work both developing the project and assisting its users.

While Rust has supported asynchronous functions since version 1.39, released in November 2019, it provides no facilities to execute them, requiring an external runtime for that purpose. Tokio provides a runtime that uses a multi-threaded work stealing scheduler. Rust's futures are lazily evaluated, requiring functions to call `.await` before they do any work. When `.await` is invoked, Tokio's runtime may pause the original future until its I/O completes, and unpauses a different task that is ready for further processing.

Users of Tokio include the development teams behind Discord and AWS Lambda. The JavaScript and TypeScript runtime Deno uses Tokio under the hood, in comparison to the JavaScript runtime Node.js, which uses the libuv library.

## Features

### Runtime

Tokio allows for the execution of asynchronous functions in Rust through its built-in runtime, which may be initialized via the `#[tokio::main]` macro. For example:

```mw
use std::error::Error;

#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let url = "https://en.wikipedia.org/";
    let text = reqwest::get(url).await?.text().await?;
    println!("{}", text);
    Ok(())
}
```

Here, the `reqwest` crate is used to request the HyperText Markup Language (HTML) for English Wikipedia. After `reqwest::get` is called to initialize the asynchronous request, `.await` will hand over control to the runtime, which then drives all the I/O operations of the request to completion before resuming the `main` function after the `.await`.

A simple example of a TCP echo server is as follows:

```mw
use std::error::Error;
use tokio::io::{AsyncBufReadExt, AsyncWriteExt, BufReader};
use tokio::net::TcpListener;

#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    // Run a server on port 8080.
    let listener = TcpListener::bind("localhost:8080").await?;

    loop {
        // Wait for a new connection from a client.
        let (mut stream, _remote_addr) = listener.accept().await?;

        // Spawn a new asynchronous task to handle the connection.
        tokio::spawn(async move {
            let (reader, mut writer) = stream.split();
            let mut reader = BufReader::new(reader);

            // While there is data to be read from the stream…
            while !reader.fill_buf().await.unwrap().is_empty() {
                // Write the data back.
                writer.write_all(reader.buffer()).await.unwrap();
            }
        });
    }
}
```

This code makes use of the `tokio::spawn` function to create an asynchronous task (implemented as a stackless coroutine), allowing each connection to be handled separately in the same process, as the runtime ensures that tasks run in the background automatically. Importantly however, the runtime multiplexes the tasks’ execution on a single thread pool (whose size is by default equal to the number of processors on the system), and so in comparison to the approach of spawning a separate thread for each task, fewer resources are consumed.

### Asynchronous I/O and timers

Tokio provides several I/O and timing primitives that work natively inside its runtime. The `TcpListener` structure used above contains a Transmission Control Protocol (TCP) socket listener that is registered with the runtime, allowing it to be used asynchronously; similarly, the `tokio::time::sleep` function can be used to suspend a task's execution for a certain duration of time, and again this is implemented by registration with the runtime.

### Synchronization primitives

Tokio also provides several generic synchronization primitives suitable for use in an asynchronous context, including locks, semaphores, barriers and channels. Unlike the I/O and timer primitives, these work even outside of the runtime context.

### Blocking thread pool

To facilitate interopability with traditional synchronous code, Tokio provides as part of its runtime a thread pool on which synchronous I/O operations may run. In particular, `tokio::task::spawn_blocking` creates a task which runs in this pool, and is allowed to perform blocking operations—this is unlike `tokio::spawn`, which may only run asynchronous code. For example, this is used to implement filesystem operations, as many platforms do not provide native asynchronous filesystem APIs (an exception to this is Linux's `io_uring`, however support for this exists only in the external `tokio_uring` library and is not yet built in).
