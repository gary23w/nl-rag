---
title: "multiprocessing (part 2/4)"
source: https://docs.python.org/3/library/multiprocessing.html
domain: multiprocessing-python
license: CC-BY-SA-4.0
tags: python multiprocessing, process pool python, global interpreter lock
fetched: 2026-07-02
part: 2/4
---

## Reference

The `multiprocessing` package mostly replicates the API of the `threading` module.

### Global start method

Python supports several ways to create and initialize a process. The global start method sets the default mechanism for creating a process.

Several multiprocessing functions and methods that may also instantiate certain objects will implicitly set the global start method to the system’s default, if it hasn’t been set already. The global start method can only be set once. If you need to change the start method from the system default, you must proactively set the global start method before calling functions or methods, or creating these objects.

### `Process` and exceptions

***class*multiprocessing.Process(*group=None*, *target=None*, *name=None*, *args=()*, *kwargs={}*, ***, *daemon=None*)**

Process objects represent activity that is run in a separate process. The `Process` class has equivalents of all the methods of `threading.Thread`.

The constructor should always be called with keyword arguments. *group* should always be `None`; it exists solely for compatibility with `threading.Thread`. *target* is the callable object to be invoked by the `run()` method. It defaults to `None`, meaning nothing is called. *name* is the process name (see `name` for more details). *args* is the argument tuple for the target invocation. *kwargs* is a dictionary of keyword arguments for the target invocation. If provided, the keyword-only *daemon* argument sets the process `daemon` flag to `True` or `False`. If `None` (the default), this flag will be inherited from the creating process.

By default, no arguments are passed to *target*. The *args* argument, which defaults to `()`, can be used to specify a list or tuple of the arguments to pass to *target*.

If a subclass overrides the constructor, it must make sure it invokes the base class constructor (`super().__init__()`) before doing anything else to the process.

Note

In general, all arguments to `Process` must be picklable. This is frequently observed when trying to create a `Process` or use a `concurrent.futures.ProcessPoolExecutor` from a REPL with a locally defined *target* function.

Passing a callable object defined in the current REPL session causes the child process to die via an uncaught `AttributeError` exception when starting as *target* must have been defined within an importable module in order to be loaded during unpickling.

Example of this uncatchable error from the child:

```python3
>>> import multiprocessing as mp
>>> def knigit():
...     print("Ni!")
...
>>> process = mp.Process(target=knigit)
>>> process.start()
>>> Traceback (most recent call last):
  File ".../multiprocessing/spawn.py", line ..., in spawn_main
  File ".../multiprocessing/spawn.py", line ..., in _main
AttributeError: module '__main__' has no attribute 'knigit'
>>> process
<SpawnProcess name='SpawnProcess-1' pid=379473 parent=378707 stopped exitcode=1>
```

See The spawn and forkserver start methods. While this restriction is not true if using the `"fork"` start method, as of Python `3.14` that is no longer the default on any platform. See Contexts and start methods. See also gh-132898.

Changed in version 3.3: Added the *daemon* parameter.

**run()**

Method representing the process’s activity.

You may override this method in a subclass. The standard `run()` method invokes the callable object passed to the object’s constructor as the target argument, if any, with sequential and keyword arguments taken from the *args* and *kwargs* arguments, respectively.

Using a list or tuple as the *args* argument passed to `Process` achieves the same effect.

Example:

```python3
>>> from multiprocessing import Process
>>> p = Process(target=print, args=[1])
>>> p.run()
1
>>> p = Process(target=print, args=(1,))
>>> p.run()
1
```

**start()**

Start the process’s activity.

This must be called at most once per process object. It arranges for the object’s `run()` method to be invoked in a separate process.

**join([*timeout*])**

If the optional argument *timeout* is `None` (the default), the method blocks until the process whose `join()` method is called terminates. If *timeout* is a positive number, it blocks at most *timeout* seconds. Note that the method returns `None` if its process terminates or if the method times out. Check the process’s `exitcode` to determine if it terminated.

A process can be joined many times.

A process cannot join itself because this would cause a deadlock. It is an error to attempt to join a process before it has been started.

**name**

The process’s name. The name is a string used for identification purposes only. It has no semantics. Multiple processes may be given the same name.

The initial name is set by the constructor. If no explicit name is provided to the constructor, a name of the form ‘Process-N1:N2:…:Nk’ is constructed, where each Nk is the N-th child of its parent.

**is_alive()**

Return whether the process is alive.

Roughly, a process object is alive from the moment the `start()` method returns until the child process terminates.

**daemon**

The process’s daemon flag, a Boolean value. This must be set before `start()` is called.

The initial value is inherited from the creating process.

When a process exits, it attempts to terminate all of its daemonic child processes.

Note that a daemonic process is not allowed to create child processes. Otherwise a daemonic process would leave its children orphaned if it gets terminated when its parent process exits. Additionally, these are **not** Unix daemons or services, they are normal processes that will be terminated (and not joined) if non-daemonic processes have exited.

In addition to the `threading.Thread` API, `Process` objects also support the following attributes and methods:

**pid**

Return the process ID. Before the process is spawned, this will be `None`.

**exitcode**

The child’s exit code. This will be `None` if the process has not yet terminated.

If the child’s `run()` method returned normally, the exit code will be 0. If it terminated via `sys.exit()` with an integer argument *N*, the exit code will be *N*.

If the child terminated due to an exception not caught within `run()`, the exit code will be 1. If it was terminated by signal *N*, the exit code will be the negative value *-N*.

**authkey**

The process’s authentication key (a byte string).

When `multiprocessing` is initialized the main process is assigned a random string using `os.urandom()`.

When a `Process` object is created, it will inherit the authentication key of its parent process, although this may be changed by setting `authkey` to another byte string.

See Authentication keys.

**sentinel**

A numeric handle of a system object which will become “ready” when the process ends.

You can use this value if you want to wait on several events at once using `multiprocessing.connection.wait()`. Otherwise calling `join()` is simpler.

On Windows, this is an OS handle usable with the `WaitForSingleObject` and `WaitForMultipleObjects` family of API calls. On POSIX, this is a file descriptor usable with primitives from the `select` module.

Added in version 3.3.

**interrupt()**

Terminate the process. Works on POSIX using the `SIGINT` signal. Behavior on Windows is undefined.

By default, this terminates the child process by raising `KeyboardInterrupt`. This behavior can be altered by setting the respective signal handler in the child process `signal.signal()` for `SIGINT`.

Note: if the child process catches and discards `KeyboardInterrupt`, the process will not be terminated.

Note: the default behavior will also set `exitcode` to `1` as if an uncaught exception was raised in the child process. To have a different `exitcode` you may simply catch `KeyboardInterrupt` and call `exit(your_code)`.

Added in version 3.14.

**terminate()**

Terminate the process. On POSIX this is done using the `SIGTERM` signal; on Windows `TerminateProcess()` is used. Note that exit handlers and finally clauses, etc., will not be executed.

Note that descendant processes of the process will *not* be terminated – they will simply become orphaned.

Warning

If this method is used when the associated process is using a pipe or queue then the pipe or queue is liable to become corrupted and may become unusable by other process. Similarly, if the process has acquired a lock or semaphore etc. then terminating it is liable to cause other processes to deadlock.

**kill()**

Same as `terminate()` but using the `SIGKILL` signal on POSIX.

Added in version 3.7.

**close()**

Close the `Process` object, releasing all resources associated with it. `ValueError` is raised if the underlying process is still running. Once `close()` returns successfully, most other methods and attributes of the `Process` object will raise `ValueError`.

Added in version 3.7.

Note that the `start()`, `join()`, `is_alive()`, `terminate()` and `exitcode` methods should only be called by the process that created the process object.

Example usage of some of the methods of `Process`:

```pycon
>>> import multiprocessing, time, signal
>>> mp_context = multiprocessing.get_context('spawn')
>>> p = mp_context.Process(target=time.sleep, args=(1000,))
>>> print(p, p.is_alive())
<...Process ... initial> False
>>> p.start()
>>> print(p, p.is_alive())
<...Process ... started> True
>>> p.terminate()
>>> time.sleep(0.1)
>>> print(p, p.is_alive())
<...Process ... stopped exitcode=-SIGTERM> False
>>> p.exitcode == -signal.SIGTERM
True
```

***exception*multiprocessing.ProcessError**

The base class of all `multiprocessing` exceptions.

***exception*multiprocessing.BufferTooShort**

Exception raised by `Connection.recv_bytes_into()` when the supplied buffer object is too small for the message read.

If `e` is an instance of `BufferTooShort` then `e.args[0]` will give the message as a byte string.

***exception*multiprocessing.AuthenticationError**

Raised when there is an authentication error.

***exception*multiprocessing.TimeoutError**

Raised by methods with a timeout when the timeout expires.

### Pipes and Queues

When using multiple processes, one generally uses message passing for communication between processes and avoids having to use any synchronization primitives like locks.

For passing messages one can use `Pipe()` (for a connection between two processes) or a queue (which allows multiple producers and consumers).

The `Queue`, `SimpleQueue` and `JoinableQueue` types are multi-producer, multi-consumer FIFO queues modelled on the `queue.Queue` class in the standard library. They differ in that `Queue` lacks the `task_done()` and `join()` methods introduced into Python 2.5’s `queue.Queue` class.

If you use `JoinableQueue` then you **must** call `JoinableQueue.task_done()` for each task removed from the queue or else the semaphore used to count the number of unfinished tasks may eventually overflow, raising an exception.

One difference from other Python queue implementations, is that `multiprocessing` queues serializes all objects that are put into them using `pickle`. The object returned by the get method is a re-created object that does not share memory with the original object.

Note that one can also create a shared queue by using a manager object – see Managers.

Note

`multiprocessing` uses the usual `queue.Empty` and `queue.Full` exceptions to signal a timeout. They are not available in the `multiprocessing` namespace so you need to import them from `queue`.

Note

When an object is put on a queue, the object is pickled and a background thread later flushes the pickled data to an underlying pipe. This has some consequences which are a little surprising, but should not cause any practical difficulties – if they really bother you then you can instead use a queue created with a manager.

1. After putting an object on an empty queue there may be an infinitesimal delay before the queue’s `empty()` method returns `False` and `get_nowait()` can return without raising `queue.Empty`.
2. If multiple processes are enqueuing objects, it is possible for the objects to be received at the other end out-of-order. However, objects enqueued by the same process will always be in the expected order with respect to each other.

Warning

If a process is killed using `Process.terminate()` or `os.kill()` while it is trying to use a `Queue`, then the data in the queue is likely to become corrupted. This may cause any other process to get an exception when it tries to use the queue later on.

Warning

As mentioned above, if a child process has put items on a queue (and it has not used `JoinableQueue.cancel_join_thread`), then that process will not terminate until all buffered items have been flushed to the pipe.

This means that if you try joining that process you may get a deadlock unless you are sure that all items which have been put on the queue have been consumed. Similarly, if the child process is non-daemonic then the parent process may hang on exit when it tries to join all its non-daemonic children.

Note that a queue created using a manager does not have this issue. See Programming guidelines.

For an example of the usage of queues for interprocess communication see Examples.

**multiprocessing.Pipe(*duplex=True*)**

Returns a pair `(conn1, conn2)` of `Connection` objects representing the ends of a pipe.

If *duplex* is `True` (the default) then the pipe is bidirectional. If *duplex* is `False` then the pipe is unidirectional: `conn1` can only be used for receiving messages and `conn2` can only be used for sending messages.

The `send()` method serializes the object using `pickle` and the `recv()` re-creates the object.

***class*multiprocessing.Queue([*maxsize*])**

Returns a process shared queue implemented using a pipe and a few locks/semaphores. When a process first puts an item on the queue a feeder thread is started which transfers objects from a buffer into the pipe.

Instantiating this class may set the global start method. See Global start method for more details.

The usual `queue.Empty` and `queue.Full` exceptions from the standard library’s `queue` module are raised to signal timeouts.

`Queue` implements all the methods of `queue.Queue` except for `task_done()`, `join()`, and `shutdown()`.

**qsize()**

Return the approximate size of the queue. Because of multithreading/multiprocessing semantics, this number is not reliable.

Note that this may raise `NotImplementedError` on platforms like macOS where `sem_getvalue()` is not implemented.

**empty()**

Return `True` if the queue is empty, `False` otherwise. Because of multithreading/multiprocessing semantics, this is not reliable.

May raise an `OSError` on closed queues. (not guaranteed)

**full()**

Return `True` if the queue is full, `False` otherwise. Because of multithreading/multiprocessing semantics, this is not reliable.

**put(*obj*[, *block*[, *timeout*]])**

Put obj into the queue. If the optional argument *block* is `True` (the default) and *timeout* is `None` (the default), block if necessary until a free slot is available. If *timeout* is a positive number, it blocks at most *timeout* seconds and raises the `queue.Full` exception if no free slot was available within that time. Otherwise (*block* is `False`), put an item on the queue if a free slot is immediately available, else raise the `queue.Full` exception (*timeout* is ignored in that case).

Changed in version 3.8: If the queue is closed, `ValueError` is raised instead of `AssertionError`.

**put_nowait(*obj*)**

Equivalent to `put(obj, False)`.

**get([*block*[, *timeout*]])**

Remove and return an item from the queue. If optional args *block* is `True` (the default) and *timeout* is `None` (the default), block if necessary until an item is available. If *timeout* is a positive number, it blocks at most *timeout* seconds and raises the `queue.Empty` exception if no item was available within that time. Otherwise (block is `False`), return an item if one is immediately available, else raise the `queue.Empty` exception (*timeout* is ignored in that case).

Changed in version 3.8: If the queue is closed, `ValueError` is raised instead of `OSError`.

**get_nowait()**

Equivalent to `get(False)`.

`multiprocessing.Queue` has a few additional methods not found in `queue.Queue`. These methods are usually unnecessary for most code:

**close()**

Close the queue: release internal resources.

A queue must not be used anymore after it is closed. For example, `get()`, `put()` and `empty()` methods must no longer be called.

The background thread will quit once it has flushed all buffered data to the pipe. This is called automatically when the queue is garbage collected.

**join_thread()**

Join the background thread. This can only be used after `close()` has been called. It blocks until the background thread exits, ensuring that all data in the buffer has been flushed to the pipe.

By default if a process is not the creator of the queue then on exit it will attempt to join the queue’s background thread. The process can call `cancel_join_thread()` to make `join_thread()` do nothing.

**cancel_join_thread()**

Prevent `join_thread()` from blocking. In particular, this prevents the background thread from being joined automatically when the process exits – see `join_thread()`.

A better name for this method might be `allow_exit_without_flush()`. It is likely to cause enqueued data to be lost, and you almost certainly will not need to use it. It is really only there if you need the current process to exit immediately without waiting to flush enqueued data to the underlying pipe, and you don’t care about lost data.

Note

This class’s functionality requires a functioning shared semaphore implementation on the host operating system. Without one, the functionality in this class will be disabled, and attempts to instantiate a `Queue` will result in an `ImportError`. See bpo-3770 for additional information. The same holds true for any of the specialized queue types listed below.

***class*multiprocessing.SimpleQueue**

It is a simplified `Queue` type, very close to a locked `Pipe`.

Instantiating this class may set the global start method. See Global start method for more details.

**close()**

Close the queue: release internal resources.

A queue must not be used anymore after it is closed. For example, `get()`, `put()` and `empty()` methods must no longer be called.

Added in version 3.9.

**empty()**

Return `True` if the queue is empty, `False` otherwise.

Always raises an `OSError` if the SimpleQueue is closed.

**get()**

Remove and return an item from the queue.

**put(*item*)**

Put *item* into the queue.

***class*multiprocessing.JoinableQueue([*maxsize*])**

`JoinableQueue`, a `Queue` subclass, is a queue which additionally has `task_done()` and `join()` methods.

Instantiating this class may set the global start method. See Global start method for more details.

**task_done()**

Indicate that a formerly enqueued task is complete. Used by queue consumers. For each `get()` used to fetch a task, a subsequent call to `task_done()` tells the queue that the processing on the task is complete.

If a `join()` is currently blocking, it will resume when all items have been processed (meaning that a `task_done()` call was received for every item that had been `put()` into the queue).

Raises a `ValueError` if called more times than there were items placed in the queue.

**join()**

Block until all items in the queue have been gotten and processed.

The count of unfinished tasks goes up whenever an item is added to the queue. The count goes down whenever a consumer calls `task_done()` to indicate that the item was retrieved and all work on it is complete. When the count of unfinished tasks drops to zero, `join()` unblocks.

### Miscellaneous

**multiprocessing.active_children()**

Return list of all live children of the current process.

Calling this has the side effect of “joining” any processes which have already finished.

**multiprocessing.cpu_count()**

Return the number of CPUs in the system.

This number is not equivalent to the number of CPUs the current process can use. The number of usable CPUs can be obtained with `os.process_cpu_count()` (or `len(os.sched_getaffinity(0))`).

When the number of CPUs cannot be determined a `NotImplementedError` is raised.

See also

`os.cpu_count()` `os.process_cpu_count()`

Changed in version 3.13: The return value can also be overridden using the `-X cpu_count` flag or `PYTHON_CPU_COUNT` as this is merely a wrapper around the `os` cpu count APIs.

**multiprocessing.current_process()**

Return the `Process` object corresponding to the current process.

An analogue of `threading.current_thread()`.

**multiprocessing.parent_process()**

Return the `Process` object corresponding to the parent process of the `current_process()`. For the main process, `parent_process` will be `None`.

Added in version 3.8.

**multiprocessing.freeze_support()**

Add support for when a program which uses `multiprocessing` has been frozen to produce an executable. (Has been tested with **py2exe**, **PyInstaller** and **cx_Freeze**.)

One needs to call this function straight after the `if __name__ == '__main__'` line of the main module. For example:

```python3
from multiprocessing import Process, freeze_support

def f():
    print('hello world!')

if __name__ == '__main__':
    freeze_support()
    Process(target=f).start()
```

If the `freeze_support()` line is omitted then trying to run the frozen executable will raise `RuntimeError`.

Calling `freeze_support()` has no effect when the start method is not *spawn*. In addition, if the module is being run normally by the Python interpreter (the program has not been frozen), then `freeze_support()` has no effect.

**multiprocessing.get_all_start_methods()**

Returns a list of the supported start methods, the first of which is the default. The possible start methods are `'fork'`, `'spawn'` and `'forkserver'`. Not all platforms support all methods. See Contexts and start methods.

Added in version 3.4.

**multiprocessing.get_context(*method=None*)**

Return a context object which has the same attributes as the `multiprocessing` module.

If *method* is `None` then the default context is returned. Note that if the global start method has not been set, this will set it to the system default See Global start method for more details. Otherwise *method* should be `'fork'`, `'spawn'`, `'forkserver'`. `ValueError` is raised if the specified start method is not available. See Contexts and start methods.

Added in version 3.4.

**multiprocessing.get_start_method(*allow_none=False*)**

Return the name of start method used for starting processes.

If the global start method is not set and *allow_none* is `False`, the global start method is set to the default, and its name is returned. See Global start method for more details.

The return value can be `'fork'`, `'spawn'`, `'forkserver'` or `None`. See Contexts and start methods.

Added in version 3.4.

Changed in version 3.8: On macOS, the *spawn* start method is now the default. The *fork* start method should be considered unsafe as it can lead to crashes of the subprocess. See bpo-33725.

**multiprocessing.set_executable(*executable*)**

Set the path of the Python interpreter to use when starting a child process. (By default `sys.executable` is used). Embedders will probably need to do something like

```python3
set_executable(os.path.join(sys.exec_prefix, 'pythonw.exe'))
```

before they can create child processes.

Changed in version 3.4: Now supported on POSIX when the `'spawn'` start method is used.

Changed in version 3.11: Accepts a path-like object.

**multiprocessing.set_forkserver_preload(*module_names*)**

Set a list of module names for the forkserver main process to attempt to import so that their already imported state is inherited by forked processes. Any `ImportError` when doing so is silently ignored. This can be used as a performance enhancement to avoid repeated work in every process.

For this to work, it must be called before the forkserver process has been launched (before creating a `Pool` or starting a `Process`).

Only meaningful when using the `'forkserver'` start method. See Contexts and start methods.

Added in version 3.4.

**multiprocessing.set_start_method(*method*, *force=False*)**

Set the method which should be used to start child processes. The *method* argument can be `'fork'`, `'spawn'` or `'forkserver'`. Raises `RuntimeError` if the start method has already been set and *force* is not `True`. If *method* is `None` and *force* is `True` then the start method is set to `None`. If *method* is `None` and *force* is `False` then the context is set to the default context.

Note that this should be called at most once, and it should be protected inside the `if __name__ == '__main__'` clause of the main module.

See Contexts and start methods.

Added in version 3.4.

Note

`multiprocessing` contains no analogues of `threading.active_count()`, `threading.enumerate()`, `threading.settrace()`, `threading.setprofile()`, `threading.Timer`, or `threading.local`.

### Connection Objects

Connection objects allow the sending and receiving of picklable objects or strings. They can be thought of as message oriented connected sockets.

Connection objects are usually created using `Pipe` – see also Listeners and Clients.

***class*multiprocessing.connection.Connection**

**send(*obj*)**

Send an object to the other end of the connection which should be read using `recv()`.

The object must be picklable. Very large pickles (approximately 32 MiB+, though it depends on the OS) may raise a `ValueError` exception.

**recv()**

Return an object sent from the other end of the connection using `send()`. Blocks until there is something to receive. Raises `EOFError` if there is nothing left to receive and the other end was closed.

**fileno()**

Return the file descriptor or handle used by the connection.

**close()**

Close the connection.

This is called automatically when the connection is garbage collected.

**poll([*timeout*])**

Return whether there is any data available to be read.

If *timeout* is not specified then it will return immediately. If *timeout* is a number then this specifies the maximum time in seconds to block. If *timeout* is `None` then an infinite timeout is used.

Note that multiple connection objects may be polled at once by using `multiprocessing.connection.wait()`.

**send_bytes(*buf*[, *offset*[, *size*]])**

Send byte data from a bytes-like object as a complete message.

If *offset* is given then data is read from that position in *buf*. If *size* is given then that many bytes will be read from *buf*. Very large buffers (approximately 32 MiB+, though it depends on the OS) may raise a `ValueError` exception

**recv_bytes([*maxlength*])**

Return a complete message of byte data sent from the other end of the connection as a string. Blocks until there is something to receive. Raises `EOFError` if there is nothing left to receive and the other end has closed.

If *maxlength* is specified and the message is longer than *maxlength* then `OSError` is raised and the connection will no longer be readable.

Changed in version 3.3: This function used to raise `IOError`, which is now an alias of `OSError`.

**recv_bytes_into(*buf*[, *offset*])**

Read into *buf* a complete message of byte data sent from the other end of the connection and return the number of bytes in the message. Blocks until there is something to receive. Raises `EOFError` if there is nothing left to receive and the other end was closed.

*buf* must be a writable bytes-like object. If *offset* is given then the message will be written into the buffer from that position. Offset must be a non-negative integer less than the length of *buf* (in bytes).

If the buffer is too short then a `BufferTooShort` exception is raised and the complete message is available as `e.args[0]` where `e` is the exception instance.

Changed in version 3.3: Connection objects themselves can now be transferred between processes using `Connection.send()` and `Connection.recv()`.

Connection objects also now support the context management protocol – see Context Manager Types. `__enter__()` returns the connection object, and `__exit__()` calls `close()`.

For example:

```pycon
>>> from multiprocessing import Pipe
>>> a, b = Pipe()
>>> a.send([1, 'hello', None])
>>> b.recv()
[1, 'hello', None]
>>> b.send_bytes(b'thank you')
>>> a.recv_bytes()
b'thank you'
>>> import array
>>> arr1 = array.array('i', range(5))
>>> arr2 = array.array('i', [0] * 10)
>>> a.send_bytes(arr1)
>>> count = b.recv_bytes_into(arr2)
>>> assert count == len(arr1) * arr1.itemsize
>>> arr2
array('i', [0, 1, 2, 3, 4, 0, 0, 0, 0, 0])
```

Warning

The `Connection.recv()` method automatically unpickles the data it receives, which can be a security risk unless you can trust the process which sent the message.

Therefore, unless the connection object was produced using `Pipe()` you should only use the `recv()` and `send()` methods after performing some sort of authentication. See Authentication keys.

Warning

If a process is killed while it is trying to read or write to a pipe then the data in the pipe is likely to become corrupted, because it may become impossible to be sure where the message boundaries lie.

### Synchronization primitives

Generally synchronization primitives are not as necessary in a multiprocess program as they are in a multithreaded program. See the documentation for `threading` module.

Note that one can also create synchronization primitives by using a manager object – see Managers.

***class*multiprocessing.Barrier(*parties*[, *action*[, *timeout*]])**

A barrier object: a clone of `threading.Barrier`.

Instantiating this class may set the global start method. See Global start method for more details.

Added in version 3.3.

***class*multiprocessing.BoundedSemaphore([*value*])**

A bounded semaphore object: a close analog of `threading.BoundedSemaphore`.

Instantiating this class may set the global start method. See Global start method for more details.

A solitary difference from its close analog exists: its `acquire` method’s first argument is named *block*, as is consistent with `Lock.acquire()`.

**locked()**

Return a boolean indicating whether this object is locked right now.

Added in version 3.14.

Note

On macOS, this is indistinguishable from `Semaphore` because `sem_getvalue()` is not implemented on that platform.

***class*multiprocessing.Condition([*lock*])**

A condition variable: an alias for `threading.Condition`.

If *lock* is specified then it should be a `Lock` or `RLock` object from `multiprocessing`.

Instantiating this class may set the global start method. See Global start method for more details.

Changed in version 3.3: The `wait_for()` method was added.

***class*multiprocessing.Event**

A clone of `threading.Event`.

Instantiating this class may set the global start method. See Global start method for more details.

***class*multiprocessing.Lock**

A non-recursive lock object: a close analog of `threading.Lock`. Once a process or thread has acquired a lock, subsequent attempts to acquire it from any process or thread will block until it is released; any process or thread may release it. The concepts and behaviors of `threading.Lock` as it applies to threads are replicated here in `multiprocessing.Lock` as it applies to either processes or threads, except as noted.

Note that `Lock` is actually a factory function which returns an instance of `multiprocessing.synchronize.Lock` initialized with a default context.

Instantiating this class may set the global start method. See Global start method for more details.

`Lock` supports the context manager protocol and thus may be used in `with` statements.

**acquire(*block=True*, *timeout=None*)**

Acquire a lock, blocking or non-blocking.

With the *block* argument set to `True` (the default), the method call will block until the lock is in an unlocked state, then set it to locked and return `True`. Note that the name of this first argument differs from that in `threading.Lock.acquire()`.

With the *block* argument set to `False`, the method call does not block. If the lock is currently in a locked state, return `False`; otherwise set the lock to a locked state and return `True`.

When invoked with a positive, floating-point value for *timeout*, block for at most the number of seconds specified by *timeout* as long as the lock can not be acquired. Invocations with a negative value for *timeout* are equivalent to a *timeout* of zero. Invocations with a *timeout* value of `None` (the default) set the timeout period to infinite. Note that the treatment of negative or `None` values for *timeout* differs from the implemented behavior in `threading.Lock.acquire()`. The *timeout* argument has no practical implications if the *block* argument is set to `False` and is thus ignored. Returns `True` if the lock has been acquired or `False` if the timeout period has elapsed.

**release()**

Release a lock. This can be called from any process or thread, not only the process or thread which originally acquired the lock.

Behavior is the same as in `threading.Lock.release()` except that when invoked on an unlocked lock, a `ValueError` is raised.

**locked()**

Return a boolean indicating whether this object is locked right now.

Added in version 3.14.

***class*multiprocessing.RLock**

A recursive lock object: a close analog of `threading.RLock`. A recursive lock must be released by the process or thread that acquired it. Once a process or thread has acquired a recursive lock, the same process or thread may acquire it again without blocking; that process or thread must release it once for each time it has been acquired.

Note that `RLock` is actually a factory function which returns an instance of `multiprocessing.synchronize.RLock` initialized with a default context.

Instantiating this class may set the global start method. See Global start method for more details.

`RLock` supports the context manager protocol and thus may be used in `with` statements.

**acquire(*block=True*, *timeout=None*)**

Acquire a lock, blocking or non-blocking.

When invoked with the *block* argument set to `True`, block until the lock is in an unlocked state (not owned by any process or thread) unless the lock is already owned by the current process or thread. The current process or thread then takes ownership of the lock (if it does not already have ownership) and the recursion level inside the lock increments by one, resulting in a return value of `True`. Note that there are several differences in this first argument’s behavior compared to the implementation of `threading.RLock.acquire()`, starting with the name of the argument itself.

When invoked with the *block* argument set to `False`, do not block. If the lock has already been acquired (and thus is owned) by another process or thread, the current process or thread does not take ownership and the recursion level within the lock is not changed, resulting in a return value of `False`. If the lock is in an unlocked state, the current process or thread takes ownership and the recursion level is incremented, resulting in a return value of `True`.

Use and behaviors of the *timeout* argument are the same as in `Lock.acquire()`. Note that some of these behaviors of *timeout* differ from the implemented behaviors in `threading.RLock.acquire()`.

**release()**

Release a lock, decrementing the recursion level. If after the decrement the recursion level is zero, reset the lock to unlocked (not owned by any process or thread) and if any other processes or threads are blocked waiting for the lock to become unlocked, allow exactly one of them to proceed. If after the decrement the recursion level is still nonzero, the lock remains locked and owned by the calling process or thread.

Only call this method when the calling process or thread owns the lock. An `AssertionError` is raised if this method is called by a process or thread other than the owner or if the lock is in an unlocked (unowned) state. Note that the type of exception raised in this situation differs from the implemented behavior in `threading.RLock.release()`.

**locked()**

Return a boolean indicating whether this object is locked right now.

Added in version 3.14.

***class*multiprocessing.Semaphore([*value*])**

A semaphore object: a close analog of `threading.Semaphore`.

Instantiating this class may set the global start method. See Global start method for more details.

A solitary difference from its close analog exists: its `acquire` method’s first argument is named *block*, as is consistent with `Lock.acquire()`.

**get_value()**

Return the current value of semaphore.

Note that this may raise `NotImplementedError` on platforms like macOS where `sem_getvalue()` is not implemented.

**locked()**

Return a boolean indicating whether this object is locked right now.

Added in version 3.14.

Note

On macOS, `sem_timedwait` is unsupported, so calling `acquire()` with a timeout will emulate that function’s behavior using a sleeping loop.

Note

Some of this package’s functionality requires a functioning shared semaphore implementation on the host operating system. Without one, the `multiprocessing.synchronize` module will be disabled, and attempts to import it will result in an `ImportError`. See bpo-3770 for additional information.

### Shared `ctypes` Objects

It is possible to create shared objects using shared memory which can be inherited by child processes.

**multiprocessing.Value(*typecode_or_type*, **args*, *lock=True*)**

Return a `ctypes` object allocated from shared memory. By default the return value is actually a synchronized wrapper for the object. The object itself can be accessed via the *value* attribute of a `Value`.

*typecode_or_type* determines the type of the returned object: it is either a ctypes type or a one character typecode of the kind used by the `array` module. **args* is passed on to the constructor for the type.

If *lock* is `True` (the default) then a new recursive lock object is created to synchronize access to the value. If *lock* is a `Lock` or `RLock` object then that will be used to synchronize access to the value. If *lock* is `False` then access to the returned object will not be automatically protected by a lock, so it will not necessarily be “process-safe”.

Operations like `+=` which involve a read and write are not atomic. So if, for instance, you want to atomically increment a shared value it is insufficient to just do

```python3
counter.value += 1
```

Assuming the associated lock is recursive (which it is by default) you can instead do

```python3
with counter.get_lock():
    counter.value += 1
```

Note that *lock* is a keyword-only argument.

**multiprocessing.Array(*typecode_or_type*, *size_or_initializer*, ***, *lock=True*)**

Return a ctypes array allocated from shared memory. By default the return value is actually a synchronized wrapper for the array.

*typecode_or_type* determines the type of the elements of the returned array: it is either a ctypes type or a one character typecode of the kind used by the `array` module with the exception of `'w'`, which is not supported. In addition, the `'c'` typecode is an alias for `ctypes.c_char`. If *size_or_initializer* is an integer, then it determines the length of the array, and the array will be initially zeroed. Otherwise, *size_or_initializer* is a sequence which is used to initialize the array and whose length determines the length of the array.
