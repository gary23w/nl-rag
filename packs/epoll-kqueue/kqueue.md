---
title: "kqueue"
source: https://en.wikipedia.org/wiki/Kqueue
domain: epoll-kqueue
license: CC-BY-SA-4.0
tags: epoll, kqueue, event notification, i/o multiplexing
fetched: 2026-07-02
---

# kqueue

**Kqueue** is a scalable event notification interface introduced in FreeBSD 4.1 in July 2000, also supported in NetBSD, OpenBSD, DragonFly BSD, and macOS. Kqueue was originally authored in 2000 by Jonathan Lemon, then involved with the FreeBSD Core Team. Kqueue makes it possible for software like nginx to solve the c10k problem. The term "kqueue" refers to its function as a "kernel event queue"

Kqueue provides efficient input and output event pipelines between the kernel and userland. Thus, it is possible to modify event filters as well as receive pending events while using only a single system call to `kevent(2)` per main event loop iteration. This contrasts with older traditional polling system calls such as `poll(2)` and `select(2)` which are less efficient, especially when polling for events on numerous file descriptors.

Kqueue not only handles file descriptor events but is also used for various other notifications such as file modification monitoring, signals, asynchronous I/O events (AIO), child process state change monitoring, and timers which support nanosecond resolution. Furthermore, kqueue provides a way to use user-defined events in addition to the ones provided by the kernel.

Some other operating systems which traditionally only supported `select(2)` and `poll(2)` also currently provide more efficient polling alternatives, such as epoll on Linux and I/O completion ports on Windows and Solaris.

`libkqueue` is a user space implementation of `kqueue(2)`, which translates calls to an operating system's native backend event mechanism.

## API

The function prototypes and types are found in `<sys/event.h>`.

```mw
int kqueue(void);
```

Creates a new kernel event queue and returns a descriptor.

```mw
int kevent(int kq, const struct kevent* changelist, int nchanges, struct kevent* eventlist, int nevents, const struct timespec* timeout);
```

Used to register events with the queue, then wait for and return any pending events to the user. In contrast to epoll, kqueue uses the same function to register and wait for events, and multiple event sources may be registered and modified using a single call. The `changelist` array can be used to pass modifications (changing the type of events to wait for, register new event sources, etc.) to the event queue, which are applied before waiting for events begins. `nevents` is the size of the user supplied `eventlist` array that is used to receive events from the event queue.

```mw
EV_SET(kev, ident, filter, flags, fflags, data, udata);
```

A macro that is used for convenient initialization of a `struct kevent` object.
