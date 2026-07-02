---
title: "Tutorial (part 2/2)"
source: https://trio.readthedocs.io/en/stable/tutorial.html
domain: trio-async
license: CC-BY-SA-4.0
tags: python trio, trio structured concurrency, async nursery python
fetched: 2026-07-02
part: 2/2
---

## Networking with Trio

Now let’s take what we’ve learned and use it to do some I/O, which is where async/await really shines.

The traditional toy application for demonstrating network APIs is an “echo server”: a program that awaits arbitrary data from remote clients, and then sends that same data right back. (Probably a more relevant example these days would be an application that does lots of concurrent HTTP requests, but for that you need an HTTP library such as asks, so we’ll stick with the echo server tradition.)

In this tutorial, we present both ends of the pipe: the client, and the server. The client periodically sends data to the server, and displays its answers. The server awaits connections; when a client connects, it recopies the received data back on the pipe.

### An echo client

To start with, here’s an example echo *client*, i.e., the program that will send some data at our echo server and get responses back:

```python3
 1# echo-client.py
 2
 3import sys
 4import trio
 5
 6# arbitrary, but:
 7# - must be in between 1024 and 65535
 8# - can't be in use by some other program on your computer
 9# - must match what we set in our echo server
10PORT = 12345
11
12
13async def sender(client_stream):
14    print("sender: started!")
15    while True:
16        data = b"async can sometimes be confusing, but I believe in you!"
17        print(f"sender: sending {data!r}")
18        await client_stream.send_all(data)
19        await trio.sleep(1)
20
21
22async def receiver(client_stream):
23    print("receiver: started!")
24    async for data in client_stream:
25        print(f"receiver: got data {data!r}")
26    print("receiver: connection closed")
27    sys.exit()
28
29
30async def parent():
31    print(f"parent: connecting to 127.0.0.1:{PORT}")
32    client_stream = await trio.open_tcp_stream("127.0.0.1", PORT)
33    async with client_stream:
34        async with trio.open_nursery() as nursery:
35            print("parent: spawning sender...")
36            nursery.start_soon(sender, client_stream)
37
38            print("parent: spawning receiver...")
39            nursery.start_soon(receiver, client_stream)
40
41
42trio.run(parent)
```

Note that this code will not work without a TCP server such as the one we’ll implement below.

The overall structure here should be familiar, because it’s just like our last example: we have a parent task, which spawns two child tasks to do the actual work, and then at the end of the `async with` block it switches into full-time parenting mode while waiting for them to finish. But now instead of just calling `trio.sleep()`, the children use some of Trio’s networking APIs.

Let’s look at the parent first:

```python3
30async def parent():
31    print(f"parent: connecting to 127.0.0.1:{PORT}")
32    client_stream = await trio.open_tcp_stream("127.0.0.1", PORT)
33    async with client_stream:
34        async with trio.open_nursery() as nursery:
35            print("parent: spawning sender...")
36            nursery.start_soon(sender, client_stream)
37
38            print("parent: spawning receiver...")
39            nursery.start_soon(receiver, client_stream)
```

First we call `trio.open_tcp_stream()` to make a TCP connection to the server. `127.0.0.1` is a magic IP address meaning “the computer I’m running on”, so this connects us to whatever program on the local computer is using `PORT` as its contact point. This function returns an object implementing Trio’s `Stream` interface, which gives us methods to send and receive bytes, and to close the connection when we’re done. We use an `async with` block to make sure that we do close the connection – not a big deal in a toy example like this, but it’s a good habit to get into, and Trio is designed to make `with` and `async with` blocks easy to use.

Finally, we start up two child tasks, and pass each of them a reference to the stream. (This is also a good example of how `nursery.start_soon` lets you pass positional arguments to the spawned function.)

Our first task’s job is to send data to the server:

```python3
13async def sender(client_stream):
14    print("sender: started!")
15    while True:
16        data = b"async can sometimes be confusing, but I believe in you!"
17        print(f"sender: sending {data!r}")
18        await client_stream.send_all(data)
19        await trio.sleep(1)
```

It uses a loop that alternates between calling `await client_stream.send_all(...)` to send some data (this is the method you use for sending data on any kind of Trio stream), and then sleeping for a second to avoid making the output scroll by too fast on your terminal.

And the second task’s job is to process the data the server sends back:

```python3
22async def receiver(client_stream):
23    print("receiver: started!")
24    async for data in client_stream:
25        print(f"receiver: got data {data!r}")
26    print("receiver: connection closed")
27    sys.exit()
```

It uses an `async for` loop to fetch data from the server. Alternatively, it could use `receive_some`, which is the opposite of `send_all`, but using `async for` saves some boilerplate.

And now we’re ready to look at the server.

### An echo server

As usual, let’s look at the whole thing first, and then we’ll discuss the pieces:

```python3
 1# echo-server.py
 2
 3import trio
 4from itertools import count
 5
 6# Port is arbitrary, but:
 7# - must be in between 1024 and 65535
 8# - can't be in use by some other program on your computer
 9# - must match what we set in our echo client
10PORT = 12345
11
12CONNECTION_COUNTER = count()
13
14
15async def echo_server(server_stream):
16    # Assign each connection a unique number to make our debug prints easier
17    # to understand when there are multiple simultaneous connections.
18    ident = next(CONNECTION_COUNTER)
19    print(f"echo_server {ident}: started")
20    try:
21        async for data in server_stream:
22            print(f"echo_server {ident}: received data {data!r}")
23            await server_stream.send_all(data)
24        print(f"echo_server {ident}: connection closed")
25    # FIXME: add discussion of (Base)ExceptionGroup to the tutorial, and use
26    # exceptiongroup.catch() here. (Not important in this case, but important
27    # if the server code uses nurseries internally.)
28    except Exception as exc:
29        # Unhandled exceptions will propagate into our parent and take
30        # down the whole program. If the exception is KeyboardInterrupt,
31        # that's what we want, but otherwise maybe not...
32        print(f"echo_server {ident}: crashed: {exc!r}")
33
34
35async def main():
36    await trio.serve_tcp(echo_server, PORT)
37
38
39# We could also just write 'trio.run(trio.serve_tcp, echo_server, PORT)', but real
40# programs almost always end up doing other stuff too and then we'd have to go
41# back and factor it out into a separate function anyway. So it's simplest to
42# just make it a standalone function from the beginning.
43trio.run(main)
```

Let’s start with `main`, which is just one line long:

```python3
35async def main():
36    await trio.serve_tcp(echo_server, PORT)
```

What this does is call `serve_tcp()`, which is a convenience function Trio provides that runs forever (or at least until you hit control-C or otherwise cancel it). This function does several helpful things:

- It creates a nursery internally, so that our server will be able to handle multiple connections at the same time.
- It listens for incoming TCP connections on the specified `PORT`.
- Whenever a connection arrives, it starts a new task running the function we pass (in this example it’s `echo_server`), and passes it a stream representing that connection.
- When each task exits, it makes sure to close the corresponding connection. (That’s why you don’t see any `async with server_stream` in the server – `serve_tcp()` takes care of this for us.)

So `serve_tcp()` is pretty handy! This part works pretty much the same for any server, whether it’s an echo server, HTTP server, SSH server, or whatever, so it makes sense to bundle it all up together in a helper function like this.

Now let’s look at `echo_server`, which handles each client connection – so if there are multiple clients, there might be multiple calls to `echo_server` running at the same time. This is where we implement our server’s “echo” behavior. This should be pretty straightforward to understand, because it uses the same stream functions we saw in the last section:

```python3
15async def echo_server(server_stream):
16    # Assign each connection a unique number to make our debug prints easier
17    # to understand when there are multiple simultaneous connections.
18    ident = next(CONNECTION_COUNTER)
19    print(f"echo_server {ident}: started")
20    try:
21        async for data in server_stream:
22            print(f"echo_server {ident}: received data {data!r}")
23            await server_stream.send_all(data)
24        print(f"echo_server {ident}: connection closed")
25    # FIXME: add discussion of (Base)ExceptionGroup to the tutorial, and use
26    # exceptiongroup.catch() here. (Not important in this case, but important
27    # if the server code uses nurseries internally.)
28    except Exception as exc:
29        # Unhandled exceptions will propagate into our parent and take
30        # down the whole program. If the exception is KeyboardInterrupt,
31        # that's what we want, but otherwise maybe not...
32        print(f"echo_server {ident}: crashed: {exc!r}")
```

The argument `server_stream` is provided by `serve_tcp()`, and is the other end of the connection we made in the client: so the data that the client passes to `send_all` will come out here. Then we have a `try` block discussed below, and finally the server loop which alternates between reading some data from the socket and then sending it back out again (unless the socket was closed, in which case we quit).

So what’s that `try` block for? Remember that in Trio, like Python in general, exceptions keep propagating until they’re caught. Here we think it’s plausible there might be unexpected exceptions, and we want to isolate that to making just this one task crash, without taking down the whole program. For example, if the client closes the connection at the wrong moment then it’s possible this code will end up calling `send_all` on a closed connection and get a `BrokenResourceError`; that’s unfortunate, and in a more serious program we might want to handle it more explicitly, but it doesn’t indicate a problem for any *other* connections. On the other hand, if the exception is something like a `KeyboardInterrupt`, we *do* want that to propagate out into the parent task and cause the whole program to exit. To express this, we use a `try` block with an `except Exception:` handler.

In general, Trio leaves it up to you to decide whether and how you want to handle exceptions, just like Python in general.

### Try it out

Open a few terminals, run `echo-server.py` in one, run `echo-client.py` in another, and watch the messages scroll by! When you get bored, you can exit by hitting control-C.

Some things to try:

- Open several terminals, and run multiple clients at the same time, all talking to the same server.
- See how the server reacts when you hit control-C on the client.
- See how the client reacts when you hit control-C on the server.

### Flow control in our echo client and server

Here’s a question you might be wondering about: why does our client use two separate tasks for sending and receiving, instead of a single task that alternates between them – like the server has? For example, our client could use a single task like:

```python
# Can you spot the two problems with this code?
async def send_and_receive(client_stream):
    while True:
        data = ...
        await client_stream.send_all(data)
        received = await client_stream.receive_some()
        if not received:
            sys.exit()
        await trio.sleep(1)
```

It turns out there are two problems with this – one minor and one major. Both relate to flow control. The minor problem is that when we call `receive_some` here we’re not waiting for *all* the data to be available; `receive_some` returns as soon as *any* data is available. If `data` is small, then our operating systems / network / server will *probably* keep it all together in a single chunk, but there’s no guarantee. If the server sends `hello` then we might get `hello`, or `he` `llo`, or `h` `e` `l` `l` `o`, or … bottom line, any time we’re expecting more than one byte of data, we have to be prepared to call `receive_some` multiple times.

And where this would go especially wrong is if we find ourselves in the situation where `data` is big enough that it passes some internal threshold, and the operating system or network decide to always break it up into multiple pieces. Now on each pass through the loop, we send `len(data)` bytes, but read less than that. The result is something like a memory leak: we’ll end up with more and more data backed up in the network, until eventually something breaks.

Note

If you’re curious *how* things break, then you can use `receive_some`'s optional argument to put a limit on how many bytes you read each time, and see what happens.

We could fix this by keeping track of how much data we’re expecting at each moment, and then keep calling `receive_some` until we get it all:

```python
expected = len(data)
while expected > 0:
    received = await client_stream.receive_some(expected)
    if not received:
        sys.exit(1)
    expected -= len(received)
```

This is a bit cumbersome, but it would solve this problem.

There’s another problem, though, that’s deeper. We’re still alternating between sending and receiving. Notice that when we send data, we use `await`: this means that sending can potentially *block*. Why does this happen? Any data that we send goes first into an operating system buffer, and from there onto the network, and then another operating system buffer on the receiving computer, before the receiving program finally calls `receive_some` to take the data out of these buffers. If we call `send_all` with a small amount of data, then it goes into these buffers and `send_all` returns immediately. But if we send enough data fast enough, eventually the buffers fill up, and `send_all` will block until the remote side calls `receive_some` and frees up some space.

Now let’s think about this from the server’s point of view. Each time it calls `receive_some`, it gets some data that it needs to send back. And until it sends it back, the data that is sitting around takes up memory. Computers have finite amounts of RAM, so if our server is well behaved then at some point it needs to stop calling `receive_some` until it gets rid of some of the old data by doing its own call to `send_all`. So for the server, really the only viable option is to alternate between receiving and sending.

But we need to remember that it’s not just the client’s call to `send_all` that might block: the server’s call to `send_all` can also get into a situation where it blocks until the client calls `receive_some`. So if the server is waiting for `send_all` to finish before it calls `receive_some`, and our client also waits for `send_all` to finish before it calls `receive_some`,… we have a problem! The client won’t call `receive_some` until the server has called `receive_some`, and the server won’t call `receive_some` until the client has called `receive_some`. If our client is written to alternate between sending and receiving, and the chunk of data it’s trying to send is large enough (e.g. 10 megabytes will probably do it in most configurations), then the two processes will deadlock.

Moral: Trio gives you powerful tools to manage sequential and concurrent execution. In this example we saw that the server needs `send` and `receive_some` to alternate in sequence, while the client needs them to run concurrently, and both were straightforward to implement. But when you’re implementing network code like this then it’s important to think carefully about flow control and buffering, because it’s up to you to choose the right execution mode!

Other popular async libraries like Twisted and `asyncio` tend to paper over these kinds of issues by throwing in unbounded buffers everywhere. This can avoid deadlocks, but can introduce its own problems and in particular can make it difficult to keep memory usage and latency under control. While both approaches have their advantages, Trio takes the position that it’s better to expose the underlying problem as directly as possible and provide good tools to confront it head-on.

Note

If you want to try and make the deadlock happen on purpose to see for yourself, and you’re using Windows, then you might need to split the `send_all` call up into two calls that each send half of the data. This is because Windows has a somewhat unusual way of handling buffering.


## When things go wrong: timeouts, cancellation and exceptions in concurrent tasks

TODO: give an example using `fail_after()`

TODO: explain `Cancelled`

TODO: explain how cancellation is also used when one child raises an exception

TODO: maybe a brief discussion of `KeyboardInterrupt` handling?
