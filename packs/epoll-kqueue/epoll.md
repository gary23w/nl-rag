---
title: "epoll"
source: https://en.wikipedia.org/wiki/Epoll
domain: epoll-kqueue
license: CC-BY-SA-4.0
tags: epoll, kqueue, event notification, i/o multiplexing
fetched: 2026-07-02
---

# epoll

**`epoll`** is a Linux kernel system call for a scalable I/O event notification mechanism, first introduced in version 2.5.45 of the Linux kernel in October, 2002. Its function is to monitor multiple file descriptors to see whether I/O is possible on any of them. It is meant to replace the older POSIX `select(2)` and `poll(2)` system calls, to achieve better performance in more demanding applications, where the number of watched file descriptors is large (unlike the older system calls, which operate in *O*(*n*) time, `epoll` operates in *O*(1) time).

`epoll` is similar to FreeBSD's `kqueue`, in that it consists of a set of user-space functions, each taking a file descriptor argument denoting the configurable kernel object, against which they cooperatively operate. `epoll` uses a red–black tree (RB-tree) data structure to keep track of all file descriptors that are currently being monitored.

## API

```mw
int epoll_create1(int flags);
```

Creates an `epoll` object and returns its file descriptor. The `flags` parameter allows epoll behavior to be modified. It has only one valid value, `EPOLL_CLOEXEC`. `epoll_create()` is an older variant of `epoll_create1()` and is deprecated as of Linux kernel version 2.6.27 and glibc version 2.9.

```mw
int epoll_ctl(int epfd, int op, int fd, struct epoll_event* event);
```

Controls (configures) which file descriptors are watched by this object, and for which events. `op` can be ADD, MODIFY or DELETE.

```mw
int epoll_wait(int epfd, struct epoll_event* events, int maxevents, int timeout);
```

Waits for any of the events registered for with `epoll_ctl`, until at least one occurs or the timeout elapses. Returns the occurred events in `events`, up to `maxevents` at once. `maxevents` is the maximum number of `epoll_event`/file descriptors to be monitored. In most case, `maxevents` is set to the value of the size of `*events` argument (`struct epoll_event* events` array).

## Triggering modes

`epoll` provides both edge-triggered and level-triggered modes. In edge-triggered mode, a call to `epoll_wait` will return only when a new event is enqueued with the `epoll` object, while in level-triggered mode, `epoll_wait` will return as long as the condition holds.

For instance, if a pipe registered with `epoll` has received data, a call to `epoll_wait` will return, signaling the presence of data to be read. Suppose, the reader only consumed part of data from the buffer. In level-triggered mode, further calls to `epoll_wait` will return immediately, as long as the pipe's buffer contains data to be read. In edge-triggered mode, however, `epoll_wait` will return only once new data is written to the pipe.

## Bugs

Bryan Cantrill pointed out that `epoll` had mistakes that could have been avoided, had it learned from its predecessors: input/output completion ports, event ports (Solaris) and kqueue. However, a large part of his criticism was addressed by `epoll`'s `EPOLLONESHOT` and `EPOLLEXCLUSIVE` options. `EPOLLONESHOT` was added in version 2.6.2 of the Linux kernel mainline, released in February 2004. `EPOLLEXCLUSIVE` was added in version 4.5, released in March 2016.
