---
title: "Trio’s core functionality (part 2/4)"
source: https://trio.readthedocs.io/en/stable/reference-core.html
domain: trio-async
license: CC-BY-SA-4.0
tags: python trio, trio structured concurrency, async nursery python
fetched: 2026-07-02
part: 2/4
---

## Tasks let you do multiple things at once

One of Trio’s core design principles is: *no implicit concurrency*. Every function executes in a straightforward, top-to-bottom manner, finishing each operation before moving on to the next – *like Guido intended*.

But, of course, the entire point of an async library is to let you do multiple things at once. The one and only way to do that in Trio is through the task spawning interface. So if you want your program to walk *and* chew gum, this is the section for you.

### Nurseries and spawning

Most libraries for concurrent programming let you start new child tasks (or threads, or whatever) willy-nilly, whenever and where-ever you feel like it. Trio is a bit different: you can’t start a child task unless you’re prepared to be a responsible parent. The way you demonstrate your responsibility is by creating a nursery:

```python
async with trio.open_nursery() as nursery:
    ...
```

And once you have a reference to a nursery object, you can start children in that nursery:

```python
async def child():
    ...

async def parent():
    async with trio.open_nursery() as nursery:
        # Make two concurrent calls to child()
        nursery.start_soon(child)
        nursery.start_soon(child)
```

This means that tasks form a tree: when you call `run()`, then this creates an initial task, and all your other tasks will be children, grandchildren, etc. of the initial task.

Essentially, the body of the `async with` block acts like an initial task that’s running inside the nursery, and then each call to `nursery.start_soon` adds another task that runs in parallel. Two crucial things to keep in mind:

- If any task inside the nursery finishes with an unhandled exception, then the nursery immediately cancels all the tasks inside the nursery.
- Since all of the tasks are running concurrently inside the `async with` block, the block does not exit until *all* tasks have completed. If you’ve used other concurrency frameworks, then you can think of it as, the de-indentation at the end of the `async with` automatically “joins” (waits for) all of the tasks in the nursery.
- Once all the tasks have finished, then:
  - The nursery is marked as “closed”, meaning that no new tasks can be started inside it.
  - Any unhandled exceptions are re-raised inside the parent task, grouped into a single `BaseExceptionGroup` or `ExceptionGroup` exception.

Since all tasks are descendents of the initial task, one consequence of this is that `run()` can’t finish until all tasks have finished.

Note

A return statement will not cancel the nursery if it still has tasks running:

```python
async def main():
    async with trio.open_nursery() as nursery:
        nursery.start_soon(trio.sleep, 5)
        return

trio.run(main)
```

This code will wait 5 seconds (for the child task to finish), and then return.

### Child tasks and cancellation

In Trio, child tasks inherit the parent nursery’s cancel scopes. So in this example, both the child tasks will be cancelled when the timeout expires:

```python
with trio.move_on_after(TIMEOUT):
    async with trio.open_nursery() as nursery:
        nursery.start_soon(child1)
        nursery.start_soon(child2)
```

Note that what matters here is the scopes that were active when `open_nursery()` was called, *not* the scopes active when `start_soon` is called. So for example, the timeout block below does nothing at all:

```python
async with trio.open_nursery() as nursery:
    with trio.move_on_after(TIMEOUT):  # don't do this!
        nursery.start_soon(child)
```

Why is this so? Well, `start_soon()` returns as soon as it has scheduled the new task to start running. The flow of execution in the parent then continues on to exit the `with trio.move_on_after(TIMEOUT):` block, at which point Trio forgets about the timeout entirely. In order for the timeout to apply to the child task, Trio must be able to tell that its associated cancel scope will stay open for at least as long as the child task is executing. And Trio can only know that for sure if the cancel scope block is outside the nursery block.

You might wonder why Trio can’t just remember “this task should be cancelled in `TIMEOUT` seconds”, even after the `with trio.move_on_after(TIMEOUT):` block is gone. The reason has to do with how cancellation is implemented. Recall that cancellation is represented by a `Cancelled` exception, which eventually needs to be caught by the cancel scope that caused it. (Otherwise, the exception would take down your whole program!) In order to be able to cancel the child tasks, the cancel scope has to be able to “see” the `Cancelled` exceptions that they raise – and those exceptions come out of the `async with open_nursery()` block, not out of the call to `start_soon()`.

If you want a timeout to apply to one task but not another, then you need to put the cancel scope in that individual task’s function – `child()`, in this example.

### Errors in multiple child tasks

Normally, in Python, only one thing happens at a time, which means that only one thing can go wrong at a time. Trio has no such limitation. Consider code like:

```python
async def broken1():
    d = {}
    return d["missing"]

async def broken2():
    seq = range(10)
    return seq[20]

async def parent():
    async with trio.open_nursery() as nursery:
        nursery.start_soon(broken1)
        nursery.start_soon(broken2)
```

`broken1` raises `KeyError`. `broken2` raises `IndexError`. Obviously `parent` should raise some error, but what? The answer is that both exceptions are grouped in an `ExceptionGroup`. `ExceptionGroup` and its parent class `BaseExceptionGroup` are used to encapsulate multiple exceptions being raised at once.

To catch individual exceptions encapsulated in an exception group, the `except*` clause was introduced in Python 3.11 (**PEP 654**). Here’s how it works:

```python
try:
    async with trio.open_nursery() as nursery:
        nursery.start_soon(broken1)
        nursery.start_soon(broken2)
except* KeyError as excgroup:
    for exc in excgroup.exceptions:
        ...  # handle each KeyError
except* IndexError as excgroup:
    for exc in excgroup.exceptions:
        ...  # handle each IndexError
```

If you want to reraise exceptions, or raise new ones, you can do so, but be aware that exceptions raised in `except*` sections will be raised together in a new exception group.

But what if you can’t use Python 3.11, and therefore `except*`, just yet? The same exceptiongroup library which backports `ExceptionGroup` also lets you approximate this behavior with exception handler callbacks:

```python
from exceptiongroup import catch

def handle_keyerrors(excgroup):
    for exc in excgroup.exceptions:
        ...  # handle each KeyError

def handle_indexerrors(excgroup):
    for exc in excgroup.exceptions:
        ...  # handle each IndexError

with catch({
    KeyError: handle_keyerrors,
    IndexError: handle_indexerrors
}):
    async with trio.open_nursery() as nursery:
        nursery.start_soon(broken1)
        nursery.start_soon(broken2)
```

The semantics for the handler functions are equal to `except*` blocks, except for setting local variables. If you need to set local variables, you need to declare them inside the handler function(s) with the `nonlocal` keyword:

```python
def handle_keyerrors(excgroup):
    nonlocal myflag
    myflag = True

myflag = False
with catch({KeyError: handle_keyerrors}):
    async with trio.open_nursery() as nursery:
        nursery.start_soon(broken1)
```

#### Designing for multiple errors

Structured concurrency is still a relatively new design pattern, but there are a few approaches we’ve identified for how you (or your users) might want to handle groups of exceptions. Note that the final pattern, simply raising an `ExceptionGroup`, is the most common - and nurseries automatically do that for you.

**First**, you might want to ‘defer to’ a particular exception type, raising just that if there is any such instance in the group. For example: `KeyboardInterrupt` has a clear meaning for the surrounding code, could reasonably take priority over errors of other types, and whether you have one or several of them doesn’t really matter.

This pattern can often be implemented using a decorator or a context manager, such as `trio_util.multi_error_defer_to()` or `trio_util.defer_to_cancelled()`. Note however that re-raising a ‘leaf’ exception will discard whatever part of the traceback is attached to the `ExceptionGroup` itself, so we don’t recommend this for errors that will be presented to humans.

**Second**, you might want to treat the concurrency inside your code as an implementation detail which is hidden from your users - for example, abstracting a protocol which involves sending and receiving data to a simple receive-only interface, or implementing a context manager which maintains some background tasks for the length of the `async with` block.

The simple option here is to `raise MySpecificError from group`, allowing users to handle your library-specific error. This is simple and reliable, but doesn’t completely hide the nursery. *Do not* unwrap single exceptions if there could ever be multiple exceptions though; that always ends in latent bugs and then tears.

The more complex option is to ensure that only one exception can in fact happen at a time. This is *very hard*, for example you’ll need to handle `KeyboardInterrupt` somehow, and we strongly recommend having a `raise PleaseReportBug from group` fallback just in case you get a group containing more than one exception. This is useful when writing a context manager which starts some background tasks, and then yields to user code which effectively runs ‘inline’ in the body of the nursery block. In this case, the background tasks can be wrapped with e.g. the outcome library to ensure that only one exception can be raised (from end-user code); and then you can either `raise SomeInternalError` if a background task failed, or unwrap the user exception if that was the only error.

**Third and most often**, the existence of a nursery in your code is not just an implementation detail, and callers *should* be prepared to handle multiple exceptions in the form of an `ExceptionGroup`, whether with `except*` or manual inspection or by just letting it propagate to *their* callers. Because this is so common, it’s nurseries’ default behavior and you don’t need to do anything.

#### Historical Note: “non-strict” ExceptionGroups

In early versions of Trio, the `except*` syntax hadn’t be dreamt up yet, and we hadn’t worked with structured concurrency for long or in large codebases. As a concession to convenience, some APIs would therefore raise single exceptions, and only wrap concurrent exceptions in the old `trio.MultiError` type if there were two or more.

Unfortunately, the results were not good: calling code often didn’t realize that some function *could* raise a `MultiError`, and therefore handle only the common case - with the result that things would work well in testing, and then crash under heavier load (typically in production). `asyncio.TaskGroup` learned from this experience and *always* wraps errors into an `ExceptionGroup`, as does `anyio`, and as of Trio 0.25 that’s our default behavior too.

We currently support a compatibility argument `strict_exception_groups=False` to `trio.run` and `trio.open_nursery`, which restores the old behavior (although `MultiError` itself has been fully removed). We strongly advise against it for new code, and encourage existing uses to migrate - we consider the option deprecated and plan to remove it after a period of documented and then runtime warnings.

### Spawning tasks without becoming a parent

Sometimes it doesn’t make sense for the task that starts a child to take on responsibility for watching it. For example, a server task may want to start a new task for each connection, but it can’t listen for connections and supervise children at the same time.

The solution here is simple once you see it: there’s no requirement that a nursery object stay in the task that created it! We can write code like this:

```python
async def new_connection_listener(handler, nursery):
    while True:
        conn = await get_new_connection()
        nursery.start_soon(handler, conn)

async def server(handler):
    async with trio.open_nursery() as nursery:
        nursery.start_soon(new_connection_listener, handler, nursery)
```

Notice that `server` opens a nursery and passes it to `new_connection_listener`, and then `new_connection_listener` is able to start new tasks as “siblings” of itself. Of course, in this case, we could just as well have written:

```python
async def server(handler):
    async with trio.open_nursery() as nursery:
        while True:
            conn = await get_new_connection()
            nursery.start_soon(handler, conn)
```

...but sometimes things aren’t so simple, and this trick comes in handy.

One thing to remember, though: cancel scopes are inherited from the nursery, **not** from the task that calls `start_soon`. So in this example, the timeout does *not* apply to `child` (or to anything else):

```python
async def do_spawn(nursery):
    with trio.move_on_after(TIMEOUT):  # don't do this, it has no effect
        nursery.start_soon(child)

async with trio.open_nursery() as nursery:
    nursery.start_soon(do_spawn, nursery)
```

### Custom supervisors

The default cleanup logic is often sufficient for simple cases, but what if you want a more sophisticated supervisor? For example, maybe you have Erlang envy and want features like automatic restart of crashed tasks. Trio itself doesn’t provide these kinds of features, but you can build them on top; Trio’s goal is to enforce basic hygiene and then get out of your way. (Specifically: Trio won’t let you build a supervisor that exits and leaves orphaned tasks behind, and if you have an unhandled exception due to bugs or laziness then Trio will make sure they propagate.) And then you can wrap your fancy supervisor up in a library and put it on PyPI, because supervisors are tricky and there’s no reason everyone should have to write their own.

For example, here’s a function that takes a list of functions, runs them all concurrently, and returns the result from the one that finishes first:

```python
async def race(*async_fns):
    if not async_fns:
        raise ValueError("must pass at least one argument")

    winner = None

    async def jockey(async_fn, cancel_scope):
        nonlocal winner
        winner = await async_fn()
        cancel_scope.cancel()

    async with trio.open_nursery() as nursery:
        for async_fn in async_fns:
            nursery.start_soon(jockey, async_fn, nursery.cancel_scope)

    return winner
```

This works by starting a set of tasks which each try to run their function. As soon as the first function completes its execution, the task will set the nonlocal variable `winner` from the outer scope to the result of the function, and cancel the other tasks using the passed in cancel scope. Once all tasks have been cancelled (which exits the nursery block), the variable `winner` will be returned.

Here if one or more of the racing functions raises an unhandled exception then Trio’s normal handling kicks in: it cancels the others and then propagates the exception. If you want different behavior, you can get that by adding a `try` block to the `jockey` function to catch exceptions and handle them however you like.


## Task-local storage

Suppose you’re writing a server that responds to network requests, and you log some information about each request as you process it. If the server is busy and there are multiple requests being handled at the same time, then you might end up with logs like this:

```
Request handler started
Request handler started
Request handler finished
Request handler finished
```

In this log, it’s hard to know which lines came from which request. (Did the request that started first also finish first, or not?) One way to solve this is to assign each request a unique identifier, and then include this identifier in each log message:

```
request 1: Request handler started
request 2: Request handler started
request 2: Request handler finished
request 1: Request handler finished
```

This way we can see that request 1 was slow: it started before request 2 but finished afterwards. (You can also get much fancier, but this is enough for an example.)

Now, here’s the problem: how does the logging code know what the request identifier is? One approach would be to explicitly pass it around to every function that might want to emit logs… but that’s basically every function, because you never know when you might need to add a `log.debug(...)` call to some utility function buried deep in the call stack, and when you’re in the middle of a debugging a nasty problem that last thing you want is to have to stop first and refactor everything to pass through the request identifier! Sometimes this is the right solution, but other times it would be much more convenient if we could store the identifier in a global variable, so that the logging function could look it up whenever it needed it. Except… a global variable can only have one value at a time, so if we have multiple handlers running at once then this isn’t going to work. What we need is something that’s *like* a global variable, but that can have different values depending on which request handler is accessing it.

To solve this problem, Python has a module in the standard library: `contextvars`.

Here’s a toy example demonstrating how to use `contextvars`:

```python3
import random
import trio
import contextvars

request_info = contextvars.ContextVar("request_info")

# Example logging function that tags each line with the request identifier.
def log(msg):
    # Read from task-local storage:
    request_tag = request_info.get()

    print(f"request {request_tag}: {msg}")

# An example "request handler" that does some work itself and also
# spawns some helper tasks to do some concurrent work.
async def handle_request(tag):
    # Write to task-local storage:
    request_info.set(tag)

    log("Request handler started")
    await trio.sleep(random.random())
    async with trio.open_nursery() as nursery:
        nursery.start_soon(concurrent_helper, "a")
        nursery.start_soon(concurrent_helper, "b")
    await trio.sleep(random.random())
    log("Request received finished")

async def concurrent_helper(job):
    log(f"Helper task {job} started")
    await trio.sleep(random.random())
    log(f"Helper task {job} finished")

# Spawn several "request handlers" simultaneously, to simulate a
# busy server handling multiple requests at the same time.
async def main():
    async with trio.open_nursery() as nursery:
        for i in range(3):
            nursery.start_soon(handle_request, i)

trio.run(main)
```

Example output (yours may differ slightly):

```
request 1: Request handler started
request 2: Request handler started
request 0: Request handler started
request 2: Helper task a started
request 2: Helper task b started
request 1: Helper task a started
request 1: Helper task b started
request 0: Helper task b started
request 0: Helper task a started
request 2: Helper task b finished
request 2: Helper task a finished
request 2: Request received finished
request 0: Helper task a finished
request 1: Helper task a finished
request 1: Helper task b finished
request 1: Request received finished
request 0: Helper task b finished
request 0: Request received finished
```

For more information, read the contextvars docs.
