---
title: "Event loop"
source: https://en.wikipedia.org/wiki/Event_loop
domain: uvicorn-asgi
license: CC-BY-SA-4.0
tags: python uvicorn, uvicorn asgi server, asgi worker python
fetched: 2026-07-02
---

# Event loop

In software, an **event loop** is an algorithm that continually dispatches control flow for events. The loop requests the next event from an event provider (which generally blocks the loop until an event occurs), and when an event is received, invokes its associated event handler. When the event loop is the central event dispatcher of a program, as it often is, it is called the **main loop** or **main event loop**.

In modern environments such as web browsers and server runtimes, the event loop is a fundamental mechanism that enables asynchronous execution by continuously monitoring and dispatching events or messages from a queue when the main program thread is idle. In JavaScript, the event loop allows non-blocking handling of tasks such as user interactions, timers, and I/O operations despite the language being single-threaded.

The same algorithm can be used to process inbound messages, a superset of events. In this context, the algorithm is called a **message loop**, **message dispatcher**, or **message pump**. A common use for a message loop is message passing inter-process communication where the message queue is maintained outside of the program (such as by the operating system).

Typically, a program that operates in a graphical user interface (GUI) environment uses an event loop, and due to the predominance of GUI environments, most modern applications have a main event loop.

In the following pseudocode, `get_next_message()` is a placeholder for a function that is typically provided by the operating system that blocks until a message is available. Thus, the loop only repeats when there is a message to process.

```
loop
    message := get_next_message()
    process_message(message)
while message != quit
```

## Alternatives

Many programs include an event loop in the high-level design; a main event loop, but there are alternative designs.

A program can exit as soon as it completes the actions that it's designed to do without external (i.e. user) interaction. Often, such a program has optional behavior that is set up before the program starts such as via the command-line interface (CLI) or environment variables. Utility software is often of this nature.

Even if a program provides for user interaction, it might not use an event loop. A program that provides an internal CLI does include a command processor that is similar to an event loop in that it dispatches to command handlers based on user input.

## Examples

### HTML/JavaScript

A web page and its JavaScript typically run in a single-threaded web browser process. The browser process deals with messages from a queue one at a time. A JavaScript function or another browser event might be associated with a given message. When the browser process has finished with a message, it proceeds to the next message in the queue.

In JavaScript environments, the event loop works with separate queues — including a task queue and a microtask queue — to manage asynchronous operations such as timers, promise callbacks, and DOM events. When the call stack is empty, the event loop selects the next task from these queues to execute.

### Windows applications

In Windows, a process that interacts with the user must accept and react to incoming messages, which is almost inevitably done by a message loop in that process. In Windows, a message is equated to an event created and imposed upon the operating system. An event can be user interaction, network traffic, system processing, timer activity, inter-process communication, among others. For non-interactive, I/O only events, Windows has I/O completion ports. I/O completion port loops run separately from the Message loop, and do not interact with the Message loop out of the box.

The heart of most Win32 applications is the WinMain() function, which calls GetMessage() in a loop. GetMessage() blocks until a message (event), is received (with function PeekMessage() as a non-blocking alternative). After some optional processing, it will call DispatchMessage(), which dispatches the message to the relevant handler, also known as WindowProc. Normally, messages that have no special WindowProc() are dispatched to DefWindowProc, the default one. DispatchMessage() calls the WindowProc of the HWND handle of the message (registered with the RegisterClass() function).

More recent versions of Windows guarantee that messages will be delivered to an application's message loop in the order that they were perceived by the system and its peripherals. This guarantee is essential when considering the design consequences of multithreaded applications. However, some messages have different rules, such as messages that are always received last, or messages with a different documented priority.

### Xlib event loop

X applications using Xlib directly are built around the `XNextEvent` family of functions; `XNextEvent` blocks until an event appears on the event queue, whereupon the application processes it appropriately. The Xlib event loop only handles window system events; applications that need to be able to wait on other files and devices could construct their own event loop from primitives such as `ConnectionNumber`, but in practice tend to use multithreading.

Very few programs use Xlib directly. In the more common case, GUI toolkits based on Xlib usually support adding events. For example, toolkits based on Xt Intrinsics have `XtAppAddInput()` and `XtAppAddTimeout()`.

It is not safe to call Xlib functions from a signal handler, because the X application may have been interrupted in an arbitrary state, e.g. within `XNextEvent`. See [1] for a solution for X11R5, X11R6 and Xt.

### GLib event loop

The GLib event loop was originally created for use in GTK but is now used in non-GUI applications as well, such as D-Bus. The resource polled is the collection of file descriptors the application is interested in; the polling block will be interrupted if a signal arrives or a timeout expires (e.g. if the application has specified a timeout or idle task). While GLib has built-in support for file descriptor and child termination events, it is possible to add an event source for any event that can be handled in a prepare-check-dispatch model.[2]

Application libraries that are built on the GLib event loop include GStreamer and the asynchronous I/O methods of GnomeVFS, but GTK remains the most visible client library. Events from the windowing system (in X, read off the X socket) are translated by GDK into GTK events and emitted as GLib signals on the application's widget objects.

### macOS Core Foundation run loops

Exactly one CFRunLoop is allowed per thread, and arbitrarily many sources and observers can be attached. Sources then communicate with observers through the run loop, with it organising queueing and dispatch of messages.

The CFRunLoop is abstracted in Cocoa as an NSRunLoop, which allows any message (equivalent to a function call in non-reflective runtimes) to be queued for dispatch to any object.

### File-based

In Unix, the everything is a file paradigm leads to a file-based event loop. Reading from and writing to files, inter-process communication, network communication, and device control are all achieved using file I/O, with the target identified by a file descriptor. The select and poll system calls allow a set of file descriptors to be monitored for a change of state, e.g. when data becomes available to be read.

For example, consider a program that reads from a continuously updated file and displays its contents in the X Window System, which communicates with clients over a socket (either Unix domain or Berkeley):

```mw
def main():
    file_fd = open("logfile.log")
    x_fd = open_display()
    construct_interface()
    while True:
        rlist, _, _ = select.select([file_fd, x_fd], [], []):
        if file_fd in rlist:
            data = file_fd.read()
            append_to_display(data)
            send_repaint_message()
        if x_fd in rlist:
            process_x_messages()
```

### Signal-based

In Unix, a signal is an asynchronous event that is handled by a signal handler which runs while the rest of the task is suspended. If a signal is received and handled while the task is blocking in `select()`, select will return early with EINTR; if a signal is received while the task is CPU bound, the task will be suspended between instructions until the signal handler returns.

A way to handle a signal is for signal handlers to set a global flag and have the event loop check for the flag immediately before and after the `select()` call; if it is set, handle the signal in the same manner as with events on file descriptors. Unfortunately, this gives rise to a race condition: if a signal arrives immediately between checking the flag and calling `select()`, it will not be handled until `select()` returns for some other reason (for example, being interrupted by a frustrated user).

The solution arrived at by POSIX is the `pselect()` call, which is similar to `select()` but takes an additional `sigmask` parameter, which describes a *signal mask*. This allows an application to mask signals in the main task, then remove the mask for the duration of the `select()` call such that signal handlers are only called while the application is I/O bound. However, implementations of `pselect()` have not always been reliable; versions of Linux prior to 2.6.16 do not have a `pselect()` system call, forcing glibc to emulate it via a method prone to the very same race condition `pselect()` is intended to avoid.

An alternative, more portable solution, is to convert asynchronous events to file-based events using the *self-pipe trick*, where "a signal handler writes a byte to a pipe whose other end is monitored by `select()` in the main program". In Linux kernel version 2.6.22, a new system call `signalfd()` was added, which allows receiving signals via a special file descriptor.

### JavaScript and Asynchronous Execution

In environments such as web browsers and Node.js, the event loop is central to asynchronous program behavior. JavaScript runs on a single thread for execution, but host environments provide APIs for non-blocking operations, such as timers, network requests, and user events. Completed asynchronous operations are placed in queues, and the event loop repeatedly checks whether the call stack is empty to schedule queued callbacks. This enables JavaScript applications to remain responsive while handling multiple asynchronous tasks.
