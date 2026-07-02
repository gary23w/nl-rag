---
title: "Anonymous pipe"
source: https://en.wikipedia.org/wiki/Anonymous_pipe
domain: unix-pipes
license: CC-BY-SA-4.0
tags: unix pipes, named pipe, anonymous pipe, mkfifo
fetched: 2026-07-02
---

# Anonymous pipe

In computer science, an **anonymous pipe** is a simplex FIFO communication channel that may be used for one-way interprocess communication (IPC). An implementation is often integrated into the operating system's file IO subsystem. Typically a parent program opens anonymous pipes, and creates a new process that inherits the other ends of the pipes, or creates several new processes and arranges them in a pipeline.

Full-duplex (two-way) communication normally requires two anonymous pipes.

Pipelines are supported in most popular operating systems, from Unix onwards, and are created using the "`|`" character in many shells.

## Unix

Pipelines are an important part of many traditional Unix applications and support for them is well integrated into most Unix-like operating systems. Pipes are created using the `pipe` system call, which creates a new pipe and returns a pair of file descriptors referring to the read and write ends of the pipe. Many traditional Unix programs are designed as filters to work with pipes.

## Microsoft Windows

Like many other device IO and IPC facilities in the Windows API, anonymous pipes are created and configured with API functions that are specific to the IO facility. In this case `CreatePipe` is used to create an anonymous pipe with separate handles for the read and write ends of the pipe. Read and write IO operations on the pipe are performed with the standard IO facility API functions `ReadFile` and `WriteFile`.

On Microsoft Windows, reads and writes to anonymous pipes are always blocking. In other words, a read from an empty pipe will cause the calling thread to wait until at least one byte becomes available or an end-of-file is received as a result of the write handle of the pipe being closed. Likewise, a write to a full pipe will cause the calling thread to wait until space becomes available to store the data being written. Reads may return with fewer than the number of bytes requested (also called a *short read*).

New processes can inherit handles to anonymous pipes in the creation process.
