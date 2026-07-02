---
title: "Trio’s core functionality (part 3/4)"
source: https://trio.readthedocs.io/en/stable/reference-core.html
domain: trio-async
license: CC-BY-SA-4.0
tags: python trio, trio structured concurrency, async nursery python
fetched: 2026-07-02
part: 3/4
---

## Synchronizing and communicating between tasks

Trio provides a standard set of synchronization and inter-task communication primitives. These objects’ APIs are generally modelled off of the analogous classes in the standard library, but with some differences.

### Blocking and non-blocking methods

The standard library synchronization primitives have a variety of mechanisms for specifying timeouts and blocking behavior, and of signaling whether an operation returned due to success versus a timeout.

In Trio, we standardize on the following conventions:

- We don’t provide timeout arguments. If you want a timeout, then use a cancel scope.
- For operations that have a non-blocking variant, the blocking and non-blocking variants are different methods with names like `X` and `X_nowait`, respectively. (This is similar to `queue.Queue`, but unlike most of the classes in `threading`.) We like this approach because it allows us to make the blocking version async and the non-blocking version sync.
- When a non-blocking method cannot succeed (the channel is empty, the lock is already held, etc.), then it raises `trio.WouldBlock`. There’s no equivalent to the `queue.Empty` versus `queue.Full` distinction – we just have the one exception that we use consistently.

### Fairness

These classes are all guaranteed to be “fair”, meaning that when it comes time to choose who will be next to acquire a lock, get an item from a queue, etc., then it always goes to the task which has been waiting longest. It’s not entirely clear whether this is the best choice, but for now that’s how it works.

As an example of what this means, here’s a small program in which two tasks compete for a lock. Notice that the task which releases the lock always immediately attempts to re-acquire it, before the other task has a chance to run. (And remember that we’re doing cooperative multi-tasking here, so it’s actually *deterministic* that the task releasing the lock will call `acquire()` before the other task wakes up; in Trio releasing a lock is not a checkpoint.) With an unfair lock, this would result in the same task holding the lock forever and the other task being starved out. But if you run this, you’ll see that the two tasks politely take turns:

```python
# fairness-demo.py

import trio

async def loopy_child(number, lock):
    while True:
        async with lock:
            print(f"Child {number} has the lock!")
            await trio.sleep(0.5)

async def main():
    async with trio.open_nursery() as nursery:
        lock = trio.Lock()
        nursery.start_soon(loopy_child, 1, lock)
        nursery.start_soon(loopy_child, 2, lock)

trio.run(main)
```

### Broadcasting an event with `Event`

***class*trio.Event**

A waitable boolean value useful for inter-task synchronization, inspired by `threading.Event`.

An event object has an internal boolean flag, representing whether the event has happened yet. The flag is initially False, and the `wait()` method waits until the flag is True. If the flag is already True, then `wait()` returns immediately. (If the event has already happened, there’s nothing to wait for.) The `set()` method sets the flag to True, and wakes up any waiters.

This behavior is useful because it helps avoid race conditions and lost wakeups: it doesn’t matter whether `set()` gets called just before or after `wait()`. If you want a lower-level wakeup primitive that doesn’t have this protection, consider `Condition` or `trio.lowlevel.ParkingLot`.

Note

Unlike `threading.Event`, `trio.Event` has no `clear` method. In Trio, once an `Event` has happened, it cannot un-happen. If you need to represent a series of events, consider creating a new `Event` object for each one (they’re cheap!), or other synchronization methods like channels or `trio.lowlevel.ParkingLot`.

**is_set() → bool**

Return the current value of the internal flag.

**set() → None**

Set the internal flag value to True, and wake any waiting tasks.

**statistics() → EventStatistics**

Return an object containing debugging information.

Currently the following fields are defined:

- `tasks_waiting`: The number of tasks blocked on this event’s `wait()` method.

***await*wait() → None**

Block until the internal flag value becomes True.

If it’s already True, then this method returns immediately.

***class*trio.EventStatistics(*tasks_waiting: int*)**

An object containing debugging information.

Currently the following fields are defined:

- `tasks_waiting`: The number of tasks blocked on this event’s `trio.Event.wait()` method.

### Using channels to pass values between tasks

*Channels* allow you to safely and conveniently send objects between different tasks. They’re particularly useful for implementing producer/consumer patterns.

The core channel API is defined by the abstract base classes `trio.abc.SendChannel` and `trio.abc.ReceiveChannel`. You can use these to implement your own custom channels, that do things like pass objects between processes or over the network. But in many cases, you just want to pass objects between different tasks inside a single process, and for that you can use `trio.open_memory_channel()`:

**trio.open_memory_channel(*max_buffer_size*)**

Open a channel for passing objects between tasks within a process.

Memory channels are lightweight, cheap to allocate, and entirely in-memory. They don’t involve any operating-system resources, or any kind of serialization. They just pass Python objects directly between tasks (with a possible stop in an internal buffer along the way).

Channel objects can be closed by calling `aclose` or using `async with`. They are *not* automatically closed when garbage collected. Closing memory channels isn’t mandatory, but it is generally a good idea, because it helps avoid situations where tasks get stuck waiting on a channel when there’s no-one on the other side. See Clean shutdown with channels for details.

Memory channel operations are all atomic with respect to cancellation, either `receive` will successfully return an object, or it will raise `Cancelled` while leaving the channel unchanged.

**Parameters:**

**max_buffer_size** (*int**or**math.inf*) – The maximum number of items that can be buffered in the channel before `send()` blocks. Choosing a sensible value here is important to ensure that backpressure is communicated promptly and avoid unnecessary latency; see Buffering in channels for more details. If in doubt, use 0.

**Returns:**

A pair `(send_channel, receive_channel)`. If you have trouble remembering which order these go in, remember: data flows from left → right.

In addition to the standard channel methods, all memory channel objects provide a `statistics()` method, which returns an object with the following fields:

- `current_buffer_used`: The number of items currently stored in the channel buffer.
- `max_buffer_size`: The maximum number of items allowed in the buffer, as passed to `open_memory_channel()`.
- `open_send_channels`: The number of open `MemorySendChannel` endpoints pointing to this channel. Initially 1, but can be increased by `MemorySendChannel.clone()`.
- `open_receive_channels`: Likewise, but for open `MemoryReceiveChannel` endpoints.
- `tasks_waiting_send`: The number of tasks blocked in `send` on this channel (summing over all clones).
- `tasks_waiting_receive`: The number of tasks blocked in `receive` on this channel (summing over all clones).

Note

If you’ve used the `threading` or `asyncio` modules, you may be familiar with `queue.Queue` or `asyncio.Queue`. In Trio, `open_memory_channel()` is what you use when you’re looking for a queue. The main difference is that Trio splits the classic queue interface up into two objects. The advantage of this is that it makes it possible to put the two ends in different processes without rewriting your code, and that we can close the two sides separately.

`MemorySendChannel` and `MemoryReceiveChannel` also expose several more features beyond the core channel interface:

***class*trio.MemorySendChannel(**args: object*, ***kwargs: object*)**

***await*aclose() → None**

Close this send channel object asynchronously.

See `MemorySendChannel.close`.

**clone() → MemorySendChannel[SendType]**

Clone this send channel object.

This returns a new `MemorySendChannel` object, which acts as a duplicate of the original: sending on the new object does exactly the same thing as sending on the old object. (If you’re familiar with `os.dup`, then this is a similar idea.)

However, closing one of the objects does not close the other, and receivers don’t get `EndOfChannel` until *all* clones have been closed.

This is useful for communication patterns that involve multiple producers all sending objects to the same destination. If you give each producer its own clone of the `MemorySendChannel`, and then make sure to close each `MemorySendChannel` when it’s finished, receivers will automatically get notified when all producers are finished. See Managing multiple producers and/or multiple consumers for examples.

**Raises:**

**trio.ClosedResourceError** – if you already closed this `MemorySendChannel` object.

**close() → None**

Close this send channel object synchronously.

All channel objects have an asynchronous `aclose` method. Memory channels can also be closed synchronously. This has the same effect on the channel and other tasks using it, but `close` is not a trio checkpoint. This simplifies cleaning up in cancelled tasks.

Using `with send_channel:` will close the channel object on leaving the with block.

***await*send(*value: SendType*) → None**

See `SendChannel.send`.

Memory channels allow multiple tasks to call `send` at the same time.

**send_nowait(*value: SendType*) → None**

Like `send`, but if the channel’s buffer is full, raises `WouldBlock` instead of blocking.

**statistics() → MemoryChannelStatistics**

Returns a `MemoryChannelStatistics` for the memory channel this is associated with.

***class*trio.MemoryReceiveChannel(**args: object*, ***kwargs: object*)**

***await*aclose() → None**

Close this receive channel object asynchronously.

See `MemoryReceiveChannel.close`.

**clone() → MemoryReceiveChannel[ReceiveType]**

Clone this receive channel object.

This returns a new `MemoryReceiveChannel` object, which acts as a duplicate of the original: receiving on the new object does exactly the same thing as receiving on the old object.

However, closing one of the objects does not close the other, and the underlying channel is not closed until all clones are closed. (If you’re familiar with `os.dup`, then this is a similar idea.)

This is useful for communication patterns that involve multiple consumers all receiving objects from the same underlying channel. See Managing multiple producers and/or multiple consumers for examples.

Warning

The clones all share the same underlying channel. Whenever a clone `receive()`s a value, it is removed from the channel and the other clones do *not* receive that value. If you want to send multiple copies of the same stream of values to multiple destinations, like `itertools.tee()`, then you need to find some other solution; this method does *not* do that.

**Raises:**

**trio.ClosedResourceError** – if you already closed this `MemoryReceiveChannel` object.

**close() → None**

Close this receive channel object synchronously.

All channel objects have an asynchronous `aclose` method. Memory channels can also be closed synchronously. This has the same effect on the channel and other tasks using it, but `close` is not a trio checkpoint. This simplifies cleaning up in cancelled tasks.

Using `with receive_channel:` will close the channel object on leaving the with block.

***await*receive() → ReceiveType**

See `ReceiveChannel.receive`.

Memory channels allow multiple tasks to call `receive` at the same time. The first task will get the first item sent, the second task will get the second item sent, and so on.

**receive_nowait() → ReceiveType**

Like `receive`, but if there’s nothing ready to receive, raises `WouldBlock` instead of blocking.

**statistics() → MemoryChannelStatistics**

Returns a `MemoryChannelStatistics` for the memory channel this is associated with.

***class*trio.MemoryChannelStatistics(*current_buffer_used: int*, *max_buffer_size: int | float*, *open_send_channels: int*, *open_receive_channels: int*, *tasks_waiting_send: int*, *tasks_waiting_receive: int*)**

#### A simple channel example

Here’s a simple example of how to use memory channels:

```python3
import trio

async def main():
    async with trio.open_nursery() as nursery:
        # Open a channel:
        send_channel, receive_channel = trio.open_memory_channel(0)
        # Start a producer and a consumer, passing one end of the channel to
        # each of them:
        nursery.start_soon(producer, send_channel)
        nursery.start_soon(consumer, receive_channel)

async def producer(send_channel):
    # Producer sends 3 messages
    for i in range(3):
        # The producer sends using 'await send_channel.send(...)'
        await send_channel.send(f"message {i}")

async def consumer(receive_channel):
    # The consumer uses an 'async for' loop to receive the values:
    async for value in receive_channel:
        print(f"got value {value!r}")

trio.run(main)
```

If you run this, it prints:

```
got value "message 0"
got value "message 1"
got value "message 2"
```

And then it hangs forever. (Use control-C to quit.)

#### Clean shutdown with channels

Of course we don’t generally like it when programs hang. What happened? The problem is that the producer sent 3 messages and then exited, but the consumer has no way to tell that the producer is gone: for all it knows, another message might be coming along any moment. So it hangs forever waiting for the 4th message.

Here’s a new version that fixes this: it produces the same output as the previous version, and then exits cleanly. The only change is the addition of `async with` blocks inside the producer and consumer:

```python3
import trio

async def main():
    async with trio.open_nursery() as nursery:
        send_channel, receive_channel = trio.open_memory_channel(0)
        nursery.start_soon(producer, send_channel)
        nursery.start_soon(consumer, receive_channel)

async def producer(send_channel):
    async with send_channel:
        for i in range(3):
            await send_channel.send(f"message {i}")

async def consumer(receive_channel):
    async with receive_channel:
        async for value in receive_channel:
            print(f"got value {value!r}")

trio.run(main)
```

The really important thing here is the producer’s `async with` . When the producer exits, this closes the `send_channel`, and that tells the consumer that no more messages are coming, so it can cleanly exit its `async for` loop. Then the program shuts down because both tasks have exited.

We also added an `async with` to the consumer. This isn’t as important, but it can help us catch mistakes or other problems. For example, suppose that the consumer exited early for some reason – maybe because of a bug. Then the producer would be sending messages into the void, and might get stuck indefinitely. But, if the consumer closes its `receive_channel`, then the producer will get a `BrokenResourceError` to alert it that it should stop sending messages because no-one is listening.

If you want to see the effect of the consumer exiting early, try adding a `break` statement to the `async for` loop – you should see a `BrokenResourceError` from the producer.

#### Managing multiple producers and/or multiple consumers

You can also have multiple producers, and multiple consumers, all sharing the same channel. However, this makes shutdown a little more complicated.

For example, consider this naive extension of our previous example, now with two producers and two consumers:

```python3
# This example usually crashes!

import trio
import random

async def main():
    async with trio.open_nursery() as nursery:
        send_channel, receive_channel = trio.open_memory_channel(0)
        # Start two producers
        nursery.start_soon(producer, "A", send_channel)
        nursery.start_soon(producer, "B", send_channel)
        # And two consumers
        nursery.start_soon(consumer, "X", receive_channel)
        nursery.start_soon(consumer, "Y", receive_channel)

async def producer(name, send_channel):
    async with send_channel:
        for i in range(3):
            await send_channel.send(f"{i} from producer {name}")
            # Random sleeps help trigger the problem more reliably
            await trio.sleep(random.random())

async def consumer(name, receive_channel):
    async with receive_channel:
        async for value in receive_channel:
            print(f"consumer {name} got value {value!r}")
            # Random sleeps help trigger the problem more reliably
            await trio.sleep(random.random())

trio.run(main)
```

The two producers, A and B, send 3 messages apiece. These are then randomly distributed between the two consumers, X and Y. So we’re hoping to see some output like:

```
consumer Y got value '0 from producer B'
consumer X got value '0 from producer A'
consumer Y got value '1 from producer A'
consumer Y got value '1 from producer B'
consumer X got value '2 from producer B'
consumer X got value '2 from producer A'
```

However, on most runs, that’s not what happens – the first part of the output is OK, and then when we get to the end the program crashes with `ClosedResourceError`. If you run the program a few times, you’ll see that sometimes the traceback shows `send` crashing, and other times it shows `receive` crashing, and you might even find that on some runs it doesn’t crash at all.

Here’s what’s happening: suppose that producer A finishes first. It exits, and its `async with` block closes the `send_channel`. But wait! Producer B was still using that `send_channel`… so the next time B calls `send`, it gets a `ClosedResourceError`.

Sometimes, though if we’re lucky, the two producers might finish at the same time (or close enough), so they both make their last `send` before either of them closes the `send_channel`.

But, even if that happens, we’re not out of the woods yet! After the producers exit, the two consumers race to be the first to notice that the `send_channel` has closed. Suppose that X wins the race. It exits its `async for` loop, then exits the `async with` block… and closes the `receive_channel`, while Y is still using it. Again, this causes a crash.

We could avoid this by using some complicated bookkeeping to make sure that only the *last* producer and the *last* consumer close their channel endpoints… but that would be tiresome and fragile. Fortunately, there’s a better way! Here’s a fixed version of our program above:

```python3
import trio
import random

async def main():
    async with trio.open_nursery() as nursery:
        send_channel, receive_channel = trio.open_memory_channel(0)
        async with send_channel, receive_channel:
            # Start two producers, giving each its own private clone
            nursery.start_soon(producer, "A", send_channel.clone())
            nursery.start_soon(producer, "B", send_channel.clone())
            # And two consumers, giving each its own private clone
            nursery.start_soon(consumer, "X", receive_channel.clone())
            nursery.start_soon(consumer, "Y", receive_channel.clone())

async def producer(name, send_channel):
    async with send_channel:
        for i in range(3):
            await send_channel.send(f"{i} from producer {name}")
            # Random sleeps help trigger the problem more reliably
            await trio.sleep(random.random())

async def consumer(name, receive_channel):
    async with receive_channel:
        async for value in receive_channel:
            print(f"consumer {name} got value {value!r}")
            # Random sleeps help trigger the problem more reliably
            await trio.sleep(random.random())

trio.run(main)
```

This example demonstrates using the `MemorySendChannel.clone` and `MemoryReceiveChannel.clone` methods. What these do is create copies of our endpoints, that act just like the original – except that they can be closed independently. And the underlying channel is only closed after *all* the clones have been closed. So this completely solves our problem with shutdown, and if you run this program, you’ll see it print its six lines of output and then exits cleanly.

Notice a small trick we use: the code in `main` creates clone objects to pass into all the child tasks, and then closes the original objects using `async with`. Another option is to pass clones into all-but-one of the child tasks, and then pass the original object into the last task, like:

```python
# Also works, but is more finicky:
send_channel, receive_channel = trio.open_memory_channel(0)
nursery.start_soon(producer, "A", send_channel.clone())
nursery.start_soon(producer, "B", send_channel)
nursery.start_soon(consumer, "X", receive_channel.clone())
nursery.start_soon(consumer, "Y", receive_channel)
```

But this is more error-prone, especially if you use a loop to spawn the producers/consumers.

Just make sure that you don’t write:

```python
# Broken, will cause program to hang:
send_channel, receive_channel = trio.open_memory_channel(0)
nursery.start_soon(producer, "A", send_channel.clone())
nursery.start_soon(producer, "B", send_channel.clone())
nursery.start_soon(consumer, "X", receive_channel.clone())
nursery.start_soon(consumer, "Y", receive_channel.clone())
```

Here we pass clones into the tasks, but never close the original objects. That means we have 3 send channel objects (the original + two clones), but we only close 2 of them, so the consumers will hang around forever waiting for that last one to be closed.

#### Buffering in channels

When you call `open_memory_channel()`, you have to specify how many values can be buffered internally in the channel. If the buffer is full, then any task that calls `send()` will stop and wait for another task to call `receive()`. This is useful because it produces *backpressure*: if the channel producers are running faster than the consumers, then it forces the producers to slow down.

You can disable buffering entirely, by doing `open_memory_channel(0)`. In that case any task that calls `send()` will wait until another task calls `receive()`, and vice versa. This is similar to how channels work in the classic Communicating Sequential Processes model, and is a reasonable default if you aren’t sure what size buffer to use. (That’s why we used it in the examples above.)

At the other extreme, you can make the buffer unbounded by using `open_memory_channel(math.inf)`. In this case, `send()` *always* returns immediately. Normally, this is a bad idea. To see why, consider a program where the producer runs more quickly than the consumer:

```python3
# Simulate a producer that generates values 10x faster than the
# consumer can handle them.

import trio
import math

async def producer(send_channel):
    count = 0
    while True:
        # Pretend that we have to do some work to create this message, and it
        # takes 0.1 seconds:
        await trio.sleep(0.1)
        await send_channel.send(count)
        print("Sent message:", count)
        count += 1

async def consumer(receive_channel):
    async for value in receive_channel:
        print("Received message:", value)
        # Pretend that we have to do some work to handle this message, and it
        # takes 1 second
        await trio.sleep(1)

async def main():
    send_channel, receive_channel = trio.open_memory_channel(math.inf)
    async with trio.open_nursery() as nursery:
        nursery.start_soon(producer, send_channel)
        nursery.start_soon(consumer, receive_channel)

trio.run(main)
```

If you run this program, you’ll see output like:

```
Sent message: 0
Received message: 0
Sent message: 1
Sent message: 2
Sent message: 3
Sent message: 4
Sent message: 5
Sent message: 6
Sent message: 7
Sent message: 8
Sent message: 9
Received message: 1
Sent message: 10
Sent message: 11
Sent message: 12
...
```

On average, the producer sends ten messages per second, but the consumer only calls `receive` once per second. That means that each second, the channel’s internal buffer has to grow to hold an extra nine items. After a minute, the buffer will have ~540 items in it; after an hour, that grows to ~32,400. Eventually, the program will run out of memory. And well before we run out of memory, our latency on handling individual messages will become abysmal. For example, at the one minute mark, the producer is sending message ~600, but the consumer is still processing message ~60. Message 600 will have to sit in the channel for ~9 minutes before the consumer catches up and processes it.

Now try replacing `open_memory_channel(math.inf)` with `open_memory_channel(0)`, and run it again. We get output like:

```
Sent message: 0
Received message: 0
Received message: 1
Sent message: 1
Received message: 2
Sent message: 2
Sent message: 3
Received message: 3
...
```

Now the `send` calls wait for the `receive` calls to finish, which forces the producer to slow down to match the consumer’s speed. (It might look strange that some values are reported as “Received” before they’re reported as “Sent”; this happens because the actual send/receive happen at the same time, so which line gets printed first is random.)

Now, let’s try setting a small but nonzero buffer size, like `open_memory_channel(3)`. what do you think will happen?

I get:

```
Sent message: 0
Received message: 0
Sent message: 1
Sent message: 2
Sent message: 3
Received message: 1
Sent message: 4
Received message: 2
Sent message: 5
...
```

So you can see that the producer runs ahead by 3 messages, and then stops to wait: when the consumer reads message 1, it sends message 4, then when the consumer reads message 2, it sends message 5, and so on. Once it reaches the steady state, this version acts just like our previous version where we set the buffer size to 0, except that it uses a bit more memory and each message sits in the buffer for a bit longer before being processed (i.e., the message latency is higher).

Of course real producers and consumers are usually more complicated than this, and in some situations, a modest amount of buffering might improve throughput. But too much buffering wastes memory and increases latency, so if you want to tune your application you should experiment to see what value works best for you.

**Why do we even support unbounded buffers then?** Good question! Despite everything we saw above, there are times when you actually do need an unbounded buffer. For example, consider a web crawler that uses a channel to keep track of all the URLs it still wants to crawl. Each crawler runs a loop where it takes a URL from the channel, fetches it, checks the HTML for outgoing links, and then adds the new URLs to the channel. This creates a *circular flow*, where each consumer is also a producer. In this case, if your channel buffer gets full, then the crawlers will block when they try to add new URLs to the channel, and if all the crawlers got blocked, then they aren’t taking any URLs out of the channel, so they’re stuck forever in a deadlock. Using an unbounded channel avoids this, because it means that `send()` never blocks.

### Lower-level synchronization primitives

Personally, I find that events and channels are usually enough to implement most things I care about, and lead to easier to read code than the lower-level primitives discussed in this section. But if you need them, they’re here. (If you find yourself reaching for these because you’re trying to implement a new higher-level synchronization primitive, then you might also want to check out the facilities in `trio.lowlevel` for a more direct exposure of Trio’s underlying synchronization logic. All of classes discussed in this section are implemented on top of the public APIs in `trio.lowlevel`; they don’t have any special access to Trio’s internals.)

***class*trio.CapacityLimiter(*total_tokens: int | float*)**

An object for controlling access to a resource with limited capacity.

Sometimes you need to put a limit on how many tasks can do something at the same time. For example, you might want to use some threads to run multiple blocking I/O operations in parallel… but if you use too many threads at once, then your system can become overloaded and it’ll actually make things slower. One popular solution is to impose a policy like “run up to 40 threads at the same time, but no more”. But how do you implement a policy like this?

That’s what `CapacityLimiter` is for. You can think of a `CapacityLimiter` object as a sack that starts out holding some fixed number of tokens:

```python3
limit = trio.CapacityLimiter(40)
```

Then tasks can come along and borrow a token out of the sack:

```python3
# Borrow a token:
async with limit:
    # We are holding a token!
    await perform_expensive_operation()
# Exiting the 'async with' block puts the token back into the sack
```

And crucially, if you try to borrow a token but the sack is empty, then you have to wait for another task to finish what it’s doing and put its token back first before you can take it and continue.

Another way to think of it: a `CapacityLimiter` is like a sofa with a fixed number of seats, and if they’re all taken then you have to wait for someone to get up before you can sit down.

By default, `trio.to_thread.run_sync()` uses a `CapacityLimiter` to limit the number of threads running at once; see `trio.to_thread.current_default_thread_limiter` for details.

If you’re familiar with semaphores, then you can think of this as a restricted semaphore that’s specialized for one common use case, with additional error checking. For a more traditional semaphore, see `Semaphore`.

Note

Don’t confuse this with the “leaky bucket” or “token bucket” algorithms used to limit bandwidth usage on networks. The basic idea of using tokens to track a resource limit is similar, but this is a very simple sack where tokens aren’t automatically created or destroyed over time; they’re just borrowed and then put back.

***await*acquire() → None**

Borrow a token from the sack, blocking if necessary.

**Raises:**

**RuntimeError** – if the current task already holds one of this sack’s tokens.

**acquire_nowait() → None**

Borrow a token from the sack, without blocking.

**Raises:**

- **WouldBlock** – if no tokens are available.
- **RuntimeError** – if the current task already holds one of this sack’s tokens.

***await*acquire_on_behalf_of(*borrower: Task | object*) → None**

Borrow a token from the sack on behalf of `borrower`, blocking if necessary.

**Parameters:**

**borrower** – A `trio.lowlevel.Task` or arbitrary opaque object used to record who is borrowing this token; see `acquire_on_behalf_of_nowait()` for details.

**Raises:**

**RuntimeError** – if `borrower` task already holds one of this sack’s tokens.

**acquire_on_behalf_of_nowait(*borrower: Task | object*) → None**

Borrow a token from the sack on behalf of `borrower`, without blocking.

**Parameters:**

**borrower** – A `trio.lowlevel.Task` or arbitrary opaque object used to record who is borrowing this token. This is used by `trio.to_thread.run_sync()` to allow threads to “hold tokens”, with the intention in the future of using it to allow deadlock detection and other useful things

**Raises:**

- **WouldBlock** – if no tokens are available.
- **RuntimeError** – if `borrower` already holds one of this sack’s tokens.

***property*available_tokens*: int | float***

The amount of capacity that’s available to use.

***property*borrowed_tokens*: int***

The amount of capacity that’s currently in use.

**release() → None**

Put a token back into the sack.

**Raises:**

**RuntimeError** – if the current task has not acquired one of this sack’s tokens.

**release_on_behalf_of(*borrower: Task | object*) → None**

Put a token back into the sack on behalf of `borrower`.

**Raises:**

**RuntimeError** – if the given borrower has not acquired one of this sack’s tokens.

**statistics() → CapacityLimiterStatistics**

Return an object containing debugging information.

Currently the following fields are defined:

- `borrowed_tokens`: The number of tokens currently borrowed from the sack.
- `total_tokens`: The total number of tokens in the sack. Usually this will be larger than `borrowed_tokens`, but it’s possibly for it to be smaller if `total_tokens` was recently decreased.
- `borrowers`: A list of all tasks or other entities that currently hold a token.
- `tasks_waiting`: The number of tasks blocked on this `CapacityLimiter`’s `acquire()` or `acquire_on_behalf_of()` methods.

***property*total_tokens*: int | float***

The total capacity available.

You can change `total_tokens` by assigning to this attribute. If you make it larger, then the appropriate number of waiting tasks will be woken immediately to take the new tokens. If you decrease total_tokens below the number of tasks that are currently using the resource, then all current tasks will be allowed to finish as normal, but no new tasks will be allowed in until the total number of tasks drops below the new total_tokens.

***class*trio.Semaphore(*initial_value: int*, ***, *max_value: int | None = None*)**

A semaphore.

A semaphore holds an integer value, which can be incremented by calling `release()` and decremented by calling `acquire()` – but the value is never allowed to drop below zero. If the value is zero, then `acquire()` will block until someone calls `release()`.

If you’re looking for a `Semaphore` to limit the number of tasks that can access some resource simultaneously, then consider using a `CapacityLimiter` instead.

This object’s interface is similar to, but different from, that of `threading.Semaphore`.

A `Semaphore` object can be used as an async context manager; it blocks on entry but not on exit.

**Parameters:**

- **initial_value** (*int*) – A non-negative integer giving semaphore’s initial value.
- **max_value** (*int**or**None*) – If given, makes this a “bounded” semaphore that raises an error if the value is about to exceed the given `max_value`.

***await*acquire() → None**

Decrement the semaphore value, blocking if necessary to avoid letting it drop below zero.

**acquire_nowait() → None**

Attempt to decrement the semaphore value, without blocking.

**Raises:**

**WouldBlock** – if the value is zero.

***property*max_value*: int | None***

The maximum allowed value. May be None to indicate no limit.

**release() → None**

Increment the semaphore value, possibly waking a task blocked in `acquire()`.

**Raises:**

**ValueError** – if incrementing the value would cause it to exceed `max_value`.

**statistics() → ParkingLotStatistics**

Return an object containing debugging information.

Currently the following fields are defined:

- `tasks_waiting`: The number of tasks blocked on this semaphore’s `acquire()` method.

***property*value*: int***

The current value of the semaphore.

***class*trio.Lock**

A classic mutex.

This is a non-reentrant, single-owner lock. Unlike `threading.Lock`, only the owner of the lock is allowed to release it.

A `Lock` object can be used as an async context manager; it blocks on entry but not on exit.

***await*acquire() → None**

Acquire the lock, blocking if necessary.

**Raises:**

**BrokenResourceError** – if the owner of the lock exits without releasing.

**acquire_nowait() → None**

Attempt to acquire the lock, without blocking.

**Raises:**

**WouldBlock** – if the lock is held.

**locked() → bool**

Check whether the lock is currently held.

**Returns:**

True if the lock is held, False otherwise.

**Return type:**

bool

**release() → None**

Release the lock.

**Raises:**

**RuntimeError** – if the calling task does not hold the lock.

**statistics() → LockStatistics**

Return an object containing debugging information.

Currently the following fields are defined:

- `locked`: boolean indicating whether the lock is held.
- `owner`: the `trio.lowlevel.Task` currently holding the lock, or None if the lock is not held.
- `tasks_waiting`: The number of tasks blocked on this lock’s `acquire()` method.

***class*trio.StrictFIFOLock**

A variant of `Lock` where tasks are guaranteed to acquire the lock in strict first-come-first-served order.

An example of when this is useful is if you’re implementing something like `trio.SSLStream` or an HTTP/2 server using h2, where you have multiple concurrent tasks that are interacting with a shared state machine, and at unpredictable moments the state machine requests that a chunk of data be sent over the network. (For example, when using h2 simply reading incoming data can occasionally create outgoing data to send.) The challenge is to make sure that these chunks are sent in the correct order, without being garbled.

One option would be to use a regular `Lock`, and wrap it around every interaction with the state machine:

```python3
# This approach is sometimes workable but often sub-optimal; see below
async with lock:
    state_machine.do_something()
    if state_machine.has_data_to_send():
        await conn.sendall(state_machine.get_data_to_send())
```

But this can be problematic. If you’re using h2 then *usually* reading incoming data doesn’t create the need to send any data, so we don’t want to force every task that tries to read from the network to sit and wait a potentially long time for `sendall` to finish. And in some situations this could even potentially cause a deadlock, if the remote peer is waiting for you to read some data before it accepts the data you’re sending.

`StrictFIFOLock` provides an alternative. We can rewrite our example like:

```python3
# Note: no awaits between when we start using the state machine and
# when we block to take the lock!
state_machine.do_something()
if state_machine.has_data_to_send():
    # Notice that we fetch the data to send out of the state machine
    # *before* sleeping, so that other tasks won't see it.
    chunk = state_machine.get_data_to_send()
    async with strict_fifo_lock:
        await conn.sendall(chunk)
```

First we do all our interaction with the state machine in a single scheduling quantum (notice there are no `await`s in there), so it’s automatically atomic with respect to other tasks. And then if and only if we have data to send, we get in line to send it – and `StrictFIFOLock` guarantees that each task will send its data in the same order that the state machine generated it.

Currently, `StrictFIFOLock` is identical to `Lock`, but (a) this may not always be true in the future, especially if Trio ever implements more sophisticated scheduling policies, and (b) the above code is relying on a pretty subtle property of its lock. Using a `StrictFIFOLock` acts as an executable reminder that you’re relying on this property.

***class*trio.Condition(*lock: Lock | None = None*)**

A classic condition variable, similar to `threading.Condition`.

A `Condition` object can be used as an async context manager to acquire the underlying lock; it blocks on entry but not on exit.

**Parameters:**

**lock** (*Lock*) – the lock object to use. If given, must be a `trio.Lock`. If None, a new `Lock` will be allocated and used.

***await*acquire() → None**

Acquire the underlying lock, blocking if necessary.

**Raises:**

**BrokenResourceError** – if the owner of the underlying lock exits without releasing.

**acquire_nowait() → None**

Attempt to acquire the underlying lock, without blocking.

**Raises:**

**WouldBlock** – if the lock is currently held.

**locked() → bool**

Check whether the underlying lock is currently held.

**Returns:**

True if the lock is held, False otherwise.

**Return type:**

bool

**notify(*n: int = 1*) → None**

Wake one or more tasks that are blocked in `wait()`.

**Parameters:**

**n** (*int*) – The number of tasks to wake.

**Raises:**

**RuntimeError** – if the calling task does not hold the lock.

**notify_all() → None**

Wake all tasks that are currently blocked in `wait()`.

**Raises:**

**RuntimeError** – if the calling task does not hold the lock.

**release() → None**

Release the underlying lock.

**statistics() → ConditionStatistics**

Return an object containing debugging information.

Currently the following fields are defined:

- `tasks_waiting`: The number of tasks blocked on this condition’s `wait()` method.
- `lock_statistics`: The result of calling the underlying `Lock`s `statistics()` method.

***await*wait() → None**

Wait for another task to call `notify()` or `notify_all()`.

When calling this method, you must hold the lock. It releases the lock while waiting, and then re-acquires it before waking up.

There is a subtlety with how this method interacts with cancellation: when cancelled it will block to re-acquire the lock before raising `Cancelled`. This may cause cancellation to be less prompt than expected. The advantage is that it makes code like this work:

```python3
async with condition:
    await condition.wait()
```

If we didn’t re-acquire the lock before waking up, and `wait()` were cancelled here, then we’d crash in `condition.__aexit__` when we tried to release the lock we no longer held.

**Raises:**

- **RuntimeError** – if the calling task does not hold the lock.
- **BrokenResourceError** – if the owner of the lock exits without releasing, when attempting to re-acquire.

These primitives return statistics objects that can be inspected.

***class*trio.CapacityLimiterStatistics(*borrowed_tokens: int*, *total_tokens: int | float*, *borrowers: list[Task | object]*, *tasks_waiting: int*)**

An object containing debugging information.

Currently the following fields are defined:

- `borrowed_tokens`: The number of tokens currently borrowed from the sack.
- `total_tokens`: The total number of tokens in the sack. Usually this will be larger than `borrowed_tokens`, but it’s possibly for it to be smaller if `trio.CapacityLimiter.total_tokens` was recently decreased.
- `borrowers`: A list of all tasks or other entities that currently hold a token.
- `tasks_waiting`: The number of tasks blocked on this `CapacityLimiter`’s `trio.CapacityLimiter.acquire()` or `trio.CapacityLimiter.acquire_on_behalf_of()` methods.

***class*trio.LockStatistics(*locked: bool*, *owner: Task | None*, *tasks_waiting: int*)**

An object containing debugging information for a Lock.

Currently the following fields are defined:

- `locked` (boolean): indicating whether the lock is held.
- `owner`: the `trio.lowlevel.Task` currently holding the lock, or None if the lock is not held.
- `tasks_waiting` (int): The number of tasks blocked on this lock’s `trio.Lock.acquire()` method.

***class*trio.ConditionStatistics(*tasks_waiting: int*, *lock_statistics: LockStatistics*)**

An object containing debugging information for a Condition.

Currently the following fields are defined:

- `tasks_waiting` (int): The number of tasks blocked on this condition’s `trio.Condition.wait()` method.
- `lock_statistics`: The result of calling the underlying `Lock`s `statistics()` method.
