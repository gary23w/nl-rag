---
title: "Reactor pattern"
source: https://en.wikipedia.org/wiki/Reactor_pattern
domain: web-middleware
license: CC-BY-SA-4.0
tags: web middleware, request pipeline, middleware chain, front controller pattern
fetched: 2026-07-02
---

# Reactor pattern

The **reactor** software design pattern is an event handling strategy that can respond to many potential service requests concurrently. The pattern's key component is an event loop, running in a *single* thread or process, which demultiplexes incoming requests and dispatches them to the correct request handler.

By relying on event-based mechanisms rather than blocking I/O or multi-threading, a reactor can handle many concurrent I/O bound requests with minimal delay. A reactor also allows for easily modifying or expanding specific request handler routines, though the pattern does have some drawbacks and limitations.

With its balance of simplicity and scalability, the reactor has become a central architectural element in several server applications and software frameworks for networking. Derivations such as the **multireactor** and proactor also exist for special cases where even greater throughput, performance, or request complexity are necessary.

## Overview

Practical considerations for the client–server model in large networks, such as the C10k problem for web servers, were the original motivation for the reactor pattern.

A naive approach to handle service requests from many potential endpoints, such as network sockets or file descriptors, is to listen for new requests from within an event loop, then immediately read the earliest request. Once the entire request has been read, it can be processed and forwarded on by directly calling the appropriate handler. An entirely "iterative" server like this, which handles one request from start-to-finish per iteration of the event loop, is logically valid. However, it will fall behind once it receives multiple requests in quick succession. The iterative approach cannot scale because reading the request blocks the server's only thread until the full request is received, and I/O operations are typically much slower than other computations.

One strategy to overcome this limitation is multi-threading: by immediately splitting off each new request into its own worker thread, the first request will no longer block the event loop, which can immediately iterate and handle another request. This "thread per connection" design scales better than a purely iterative one, but it still contains multiple inefficiencies and will struggle past a point. From a standpoint of underlying system resources, each new thread or process imposes overhead costs in memory and processing time (due to context switching). The fundamental inefficiency of each thread waiting for I/O to finish isn't resolved either.

From a design standpoint, both approaches tightly couple the general demultiplexer with specific request handlers too, making the server code brittle and tedious to modify. These considerations suggest a few major design decisions:

1. Retain a single-threaded event handler; multi-threading introduces overhead and complexity without resolving the real issue of blocking I/O
2. Use an event notification mechanism to demultiplex requests only *after* I/O is complete (so I/O is effectively non-blocking)
3. Register request handlers as callbacks with the event handler for better separation of concerns

Combining these insights leads to the reactor pattern, which balances the advantages of single-threading with high throughput and scalability.

## Usage

The reactor pattern can be a good starting point for any concurrent, event-handling problem. The pattern is not restricted to network sockets either; hardware I/O, file system or database access, inter-process communication, and even abstract message passing systems are all possible use-cases.

However, the reactor pattern does have limitations, a major one being the use of callbacks, which make program analysis and debugging more difficult, a problem common to designs with inverted control. The simpler thread-per-connection and fully iterative approaches avoid this and can be valid solutions if scalability or high-throughput are not required.

Single-threading can also become a drawback in use-cases that require maximum throughput, or when requests involve significant processing. Different multi-threaded designs can overcome these limitations, and in fact, some still use the reactor pattern as a sub-component for handling events and I/O.

### Applications

The reactor pattern (or a variant of it) has found a place in many web servers, application servers, and networking frameworks:

- Adaptive Communication Environment (ACE)
- EventMachine
- Netty
- Nginx
- Node.js
- Perl Object Environment
- POCO C++ Libraries
- Spring Framework (version 5 and later)
- Tokio
- Twisted
- Vert.x

## Structure

- (A reactor typically consists of 2 subsystems. Sockets (a.k.a. handles) and a demultiplexer (like select or epoll) are typically provided by the system. The reactive application will provide a dispatcher / event-loop that reacts to handle events by invoking handlers, which are registered as callbacks.)UML 2 component diagram of a reactive application.
- (Before starting the event loop, a reactive application will typically register handles & handlers for specific requests. The event loop will then respond to request-based events by invoking a handler, passing the handle for processing.)UML 2 sequence diagram of a reactive server.

A reactive application consists of several moving parts and will rely on some support mechanisms:

***Handle***

An identifier and interface to a specific request, with IO and data. This will often take the form of a socket, file descriptor, or similar mechanism, which should be provided by most modern operating systems.

***Demultiplexer***

An event notifier that can efficiently monitor the

status

of a handle, then notify other subsystems of a relevant status change (typically an IO handle becoming "ready to read"). Traditionally this role was filled by the

select() system call

, but more contemporary examples include

epoll

,

kqueue

, and

IOCP

.

***Dispatcher***

The actual event loop of the reactive application, this component maintains the registry of valid event handlers, then invokes the appropriate handler when an event is raised.

***Event Handler***

Also known as a request handler, this is the specific logic for processing one type of service request. The reactor pattern suggests registering these dynamically with the dispatcher as callbacks for greater flexibility. By default, a reactor does

not

use multi-threading but invokes a request handler within the same thread as the dispatcher.

***Event Handler Interface***

An abstract interface class, representing the general properties and methods of an event handler. Each specific handler must implement this interface while the dispatcher will operate on the event handlers through this interface.

## Variants

The standard reactor pattern is sufficient for many applications, but for particularly demanding ones, tweaks can provide even more power at the price of extra complexity.

One basic modification is to invoke event handlers in their own threads for more concurrency. Running the handlers in a thread pool, rather than spinning up new threads as needed, will further simplify the multi-threading and minimize overhead. This makes the thread pool a natural complement to the reactor pattern in many use-cases.

Another way to maximize throughput is to partly reintroduce the approach of the "thread per connection" server, with replicated dispatchers / event loops running concurrently. However, rather than the number of connections, one configures the dispatcher count to match the available CPU cores of the underlying hardware.

Known as a multireactor, this variant ensures a dedicated server is fully using the hardware's processing power. Because the distinct threads are long-running event loops, the overhead of creating and destroying threads is limited to server startup and shutdown. With requests distributed across independent dispatchers, a multireactor also provides better availability and robustness; should an error occur and a single dispatcher fail, it will only interrupt requests allocated to that event loop.

For particularly complex services, where synchronous and asynchronous demands must be combined, one other alternative is the proactor pattern. This pattern is more intricate than a reactor, with its own engineering details, but it still makes use of a reactor subcomponent to solve the problem of blocking IO.
