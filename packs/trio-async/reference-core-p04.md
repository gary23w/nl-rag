---
title: "Trio’s core functionality (part 4/4)"
source: https://trio.readthedocs.io/en/stable/reference-core.html
domain: trio-async
license: CC-BY-SA-4.0
tags: python trio, trio structured concurrency, async nursery python
fetched: 2026-07-02
part: 4/4
---

## Notes on async generators

Python 3.6 added support for *async generators*, which can use `await`, `async for`, and `async with` in between their `yield` statements. As you might expect, you use `async for` to iterate over them. **PEP 525** has many more details if you want them.

For example, the following is a roundabout way to print the numbers 0 through 9 with a 1-second delay before each one:

```python
async def range_slowly(*args):
    """Like range(), but adds a 1-second sleep before each value."""
    for value in range(*args):
        await trio.sleep(1)
        yield value

async def use_it():
    async for value in range_slowly(10):
        print(value)

trio.run(use_it)
```

Trio supports async generators, but there’s several caveats and it’s very hard to handle them properly. Therefore Trio bundles a helper, `trio.as_safe_channel` that does it for you.

**trio.as_safe_channel(*fn: Callable[[P], AsyncGenerator[T, None]]*) → Callable[[P], AbstractAsyncContextManager[ReceiveChannel[T]]]**

Decorate an async generator function to make it cancellation-safe.

The `yield` keyword offers a very convenient way to write iterators… which makes it really unfortunate that async generators are so difficult to call correctly. Yielding from the inside of a cancel scope or a nursery to the outside violates structured concurrency with consequences explained in **PEP 789**. Even then, resource cleanup errors remain common (**PEP 533**) unless you wrap every call in `aclosing()`.

This decorator gives you the best of both worlds: with careful exception handling and a background task we preserve structured concurrency by offering only the safe interface, and you can still write your iterables with the convenience of `yield`. For example:

```python3
@as_safe_channel
async def my_async_iterable(arg, *, kwarg=True):
    while ...:
        item = await ...
        yield item

async with my_async_iterable(...) as recv_chan:
    async for item in recv_chan:
        ...
```

While the combined async-with-async-for can be inconvenient at first, the context manager is indispensable for both correctness and for prompt cleanup of resources.

The details behind the problems are described in the following sections.

### Finalization

If you iterate over an async generator in its entirety, like the example above does, then the execution of the async generator will occur completely in the context of the code that’s iterating over it, and there aren’t too many surprises.

If you abandon a partially-completed async generator, though, such as by `break`ing out of the iteration, things aren’t so simple. The async generator iterator object is still alive, waiting for you to resume iterating it so it can produce more values. At some point, Python will realize that you’ve dropped all references to the iterator, and will call on Trio to throw in a `GeneratorExit` exception so that any remaining cleanup code inside the generator has a chance to run: `finally` blocks, `__aexit__` handlers, and so on.

So far, so good. Unfortunately, Python provides no guarantees about *when* this happens. It could be as soon as you break out of the `async for` loop, or an arbitrary amount of time later. It could even be after the entire Trio run has finished! Just about the only guarantee is that it *won’t* happen in the task that was using the generator. That task will continue on with whatever else it’s doing, and the async generator cleanup will happen “sometime later, somewhere else”: potentially with different context variables, not subject to timeouts, and/or after any nurseries you’re using have been closed.

If you don’t like that ambiguity, and you want to ensure that a generator’s `finally` blocks and `__aexit__` handlers execute as soon as you’re done using it, then you’ll need to wrap your use of the generator in something like async_generator.aclosing():

```python
# Instead of this:
async for value in my_generator():
    if value == 42:
        break

# Do this:
async with aclosing(my_generator()) as aiter:
    async for value in aiter:
        if value == 42:
            break
```

This is cumbersome, but Python unfortunately doesn’t provide any other reliable options. If you use `aclosing()`, then your generator’s cleanup code executes in the same context as the rest of its iterations, so timeouts, exceptions, and context variables work like you’d expect.

If you don’t use `aclosing()`, then Trio will do its best anyway, but you’ll have to contend with the following semantics:

- The cleanup of the generator occurs in a cancelled context, i.e., all blocking calls executed during cleanup will raise `Cancelled`. This is to compensate for the fact that any timeouts surrounding the original use of the generator have been long since forgotten.
- The cleanup runs without access to any context variables that may have been present when the generator was originally being used.
- If the generator raises an exception during cleanup, then it’s printed to the `trio.async_generator_errors` logger and otherwise ignored.
- If an async generator is still alive at the end of the whole call to `trio.run()`, then it will be cleaned up after all tasks have exited and before `trio.run()` returns. Since the “system nursery” has already been closed at this point, Trio isn’t able to support any new calls to `trio.lowlevel.spawn_system_task()`.

If you plan to run your code on PyPy to take advantage of its better performance, you should be aware that PyPy is *far more likely* than CPython to perform async generator cleanup at a time well after the last use of the generator. (This is a consequence of the fact that PyPy does not use reference counting to manage memory.) To help catch issues like this, Trio will issue a `ResourceWarning` (ignored by default, but enabled when running under `python -X dev` for example) for each async generator that needs to be handled through the fallback finalization path.

### Cancel scopes and nurseries

Warning

You may not write a `yield` statement that suspends an async generator inside a `CancelScope` or `Nursery` that was entered within the generator.

That is, this is OK:

```python
async def some_agen():
    with trio.move_on_after(1):
        await long_operation()
    yield "first"
    async with trio.open_nursery() as nursery:
        nursery.start_soon(task1)
        nursery.start_soon(task2)
    yield "second"
    ...
```

But this is not:

```python
async def some_agen():
    with trio.move_on_after(1):
        yield "first"
    async with trio.open_nursery() as nursery:
        yield "second"
    ...
```

Async generators decorated with `@asynccontextmanager` to serve as the template for an async context manager are *not* subject to this constraint, because `@asynccontextmanager` uses them in a limited way that doesn’t create problems.

Violating the rule described in this section will sometimes get you a useful error message, but Trio is not able to detect all such cases, so sometimes you’ll get an unhelpful `TrioInternalError`. (And sometimes it will seem to work, which is probably the worst outcome of all, since then you might not notice the issue until you perform some minor refactoring of the generator or the code that’s iterating it, or just get unlucky. There is a draft **PEP 789** with accompanying discussion thread that would at least make it fail consistently.)

The reason for the restriction on cancel scopes has to do with the difficulty of noticing when a generator gets suspended and resumed. The cancel scopes inside the generator shouldn’t affect code running outside the generator, but Trio isn’t involved in the process of exiting and reentering the generator, so it would be hard pressed to keep its cancellation plumbing in the correct state. Nurseries use a cancel scope internally, so they have all the problems of cancel scopes plus a number of problems of their own: for example, when the generator is suspended, what should the background tasks do? There’s no good way to suspend them, but if they keep running and throw an exception, where can that exception be reraised?

For more discussion, see Trio issues 264 (especially this comment) and 638.


## Threads (if you must)

In a perfect world, all third-party libraries and low-level APIs would be natively async and integrated into Trio, and all would be happiness and rainbows.

That world, alas, does not (yet) exist. Until it does, you may find yourself needing to interact with non-Trio APIs that do rude things like “blocking”.

In acknowledgment of this reality, Trio provides two useful utilities for working with real, operating-system level, `threading`-module-style threads. First, if you’re in Trio but need to push some blocking I/O into a thread, there’s `trio.to_thread.run_sync`. And if you’re in a thread and need to communicate back with Trio, you can use `trio.from_thread.run()` and `trio.from_thread.run_sync()`.

### Trio’s philosophy about managing worker threads

If you’ve used other I/O frameworks, you may have encountered the concept of a “thread pool”, which is most commonly implemented as a fixed size collection of threads that hang around waiting for jobs to be assigned to them. These solve two different problems: First, reusing the same threads over and over is more efficient than starting and stopping a new thread for every job you need done; basically, the pool acts as a kind of cache for idle threads. And second, having a fixed size avoids getting into a situation where 100,000 jobs are submitted simultaneously, and then 100,000 threads are spawned and the system gets overloaded and crashes. Instead, the N threads start executing the first N jobs, while the other (100,000 - N) jobs sit in a queue and wait their turn. Which is generally what you want, and this is how `trio.to_thread.run_sync()` works by default.

The downside of this kind of thread pool is that sometimes, you need more sophisticated logic for controlling how many threads are run at once. For example, you might want a policy like “at most 20 threads total, but no more than 3 of those can be running jobs associated with the same user account”, or you might want a pool whose size is dynamically adjusted over time in response to system conditions.

It’s even possible for a fixed-size policy to cause unexpected deadlocks. Imagine a situation where we have two different types of blocking jobs that you want to run in the thread pool, type A and type B. Type A is pretty simple: it just runs and completes pretty quickly. But type B is more complicated: it has to stop in the middle and wait for some other work to finish, and that other work includes running a type A job. Now, suppose you submit N jobs of type B to the pool. They all start running, and then eventually end up submitting one or more jobs of type A. But since every thread in our pool is already busy, the type A jobs don’t actually start running – they just sit in a queue waiting for the type B jobs to finish. But the type B jobs will never finish, because they’re waiting for the type A jobs. Our system has deadlocked. The ideal solution to this problem is to avoid having type B jobs in the first place – generally it’s better to keep complex synchronization logic in the main Trio thread. But if you can’t do that, then you need a custom thread allocation policy that tracks separate limits for different types of jobs, and make it impossible for type B jobs to fill up all the slots that type A jobs need to run.

So, we can see that it’s important to be able to change the policy controlling the allocation of threads to jobs. But in many frameworks, this requires implementing a new thread pool from scratch, which is highly non-trivial; and if different types of jobs need different policies, then you may have to create multiple pools, which is inefficient because now you effectively have two different thread caches that aren’t sharing resources.

Trio’s solution to this problem is to split worker thread management into two layers. The lower layer is responsible for taking blocking I/O jobs and arranging for them to run immediately on some worker thread. It takes care of solving the tricky concurrency problems involved in managing threads and is responsible for optimizations like reusing threads, but has no admission control policy: if you give it 100,000 jobs, it will spawn 100,000 threads. The upper layer is responsible for providing the policy to make sure that this doesn’t happen – but since it *only* has to worry about policy, it can be much simpler. In fact, all there is to it is the `limiter=` argument passed to `trio.to_thread.run_sync()`. This defaults to a global `CapacityLimiter` object, which gives us the classic fixed-size thread pool behavior. (See `trio.to_thread.current_default_thread_limiter()`.) But if you want to use “separate pools” for type A jobs and type B jobs, then it’s just a matter of creating two separate `CapacityLimiter` objects and passing them in when running these jobs. Or here’s an example of defining a custom policy that respects the global thread limit, while making sure that no individual user can use more than 3 threads at a time:

```python
class CombinedLimiter:
     def __init__(self, first, second):
         self._first = first
         self._second = second

     async def acquire_on_behalf_of(self, borrower):
         # Acquire both, being careful to clean up properly on error
         await self._first.acquire_on_behalf_of(borrower)
         try:
             await self._second.acquire_on_behalf_of(borrower)
         except:
             self._first.release_on_behalf_of(borrower)
             raise

     def release_on_behalf_of(self, borrower):
         # Release both, being careful to clean up properly on error
         try:
             self._second.release_on_behalf_of(borrower)
         finally:
             self._first.release_on_behalf_of(borrower)

# Use a weak value dictionary, so that we don't waste memory holding
# limiter objects for users who don't have any worker threads running.
USER_LIMITERS = weakref.WeakValueDictionary()
MAX_THREADS_PER_USER = 3

def get_user_limiter(user_id):
    try:
        return USER_LIMITERS[user_id]
    except KeyError:
        per_user_limiter = trio.CapacityLimiter(MAX_THREADS_PER_USER)
        global_limiter = trio.current_default_thread_limiter()
        # IMPORTANT: acquire the per_user_limiter before the global_limiter.
        # If we get 100 jobs for a user at the same time, we want
        # to only allow 3 of them at a time to even compete for the
        # global thread slots.
        combined_limiter = CombinedLimiter(per_user_limiter, global_limiter)
        USER_LIMITERS[user_id] = combined_limiter
        return combined_limiter

async def run_sync_in_thread_for_user(user_id, sync_fn, *args):
    combined_limiter = get_user_limiter(user_id)
    return await trio.to_thread.run_sync(sync_fn, *args, limiter=combined_limiter)
```

### Putting blocking I/O into worker threads

***await*trio.to_thread.run_sync(*sync_fn: Callable[[Unpack[Ts]], RetT]*, **args: Unpack[Ts]*, *thread_name: str | None = None*, *abandon_on_cancel: bool = False*, *limiter: CapacityLimiter | None = None*) → RetT**

Convert a blocking operation into an async operation using a thread.

These two lines are equivalent:

```python3
sync_fn(*args)
await trio.to_thread.run_sync(sync_fn, *args)
```

except that if `sync_fn` takes a long time, then the first line will block the Trio loop while it runs, while the second line allows other Trio tasks to continue working while `sync_fn` runs. This is accomplished by pushing the call to `sync_fn(*args)` off into a worker thread.

From inside the worker thread, you can get back into Trio using the functions in `trio.from_thread`.

**Parameters:**

- **sync_fn** – An arbitrary synchronous callable.
- ***args** – Positional arguments to pass to sync_fn. If you need keyword arguments, use `functools.partial()`.
- **abandon_on_cancel** (*bool*) – Whether to abandon this thread upon cancellation of this operation. See discussion below.
- **thread_name** (*str*) – Optional string to set the name of the thread. Will always set `threading.Thread.name`, but only set the os name if pthread.h is available (i.e. most POSIX installations). pthread names are limited to 15 characters, and can be read from `/proc/<PID>/task/<SPID>/comm` or with `ps -eT`, among others. Defaults to `{sync_fn.__name__|None} from {trio.lowlevel.current_task().name}`.
- **limiter** (*None**, or**CapacityLimiter-like object*) – An object used to limit the number of simultaneous threads. Most commonly this will be a `CapacityLimiter`, but it could be anything providing compatible `acquire_on_behalf_of()` and `release_on_behalf_of()` methods. This function will call `acquire_on_behalf_of` before starting the thread, and `release_on_behalf_of` after the thread has finished. If None (the default), uses the default `CapacityLimiter`, as returned by `current_default_thread_limiter()`.

**Cancellation handling**: Cancellation is a tricky issue here, because neither Python nor the operating systems it runs on provide any general mechanism for cancelling an arbitrary synchronous function running in a thread. This function will always check for cancellation on entry, before starting the thread. But once the thread is running, there are two ways it can handle being cancelled:

- If `abandon_on_cancel=False`, the function ignores the cancellation and keeps going, just like if we had called `sync_fn` synchronously. This is the default behavior.
- If `abandon_on_cancel=True`, then this function immediately raises `Cancelled`. In this case **the thread keeps running in background** – we just abandon it to do whatever it’s going to do, and silently discard any return value or errors that it raises. Only use this if you know that the operation is safe and side-effect free. (For example: `trio.socket.getaddrinfo()` uses a thread with `abandon_on_cancel=True`, because it doesn’t really affect anything if a stray hostname lookup keeps running in the background.) The `limiter` is only released after the thread has *actually* finished – which in the case of cancellation may be some time after this function has returned. If `trio.run()` finishes before the thread does, then the limiter release method will never be called at all.

Warning

You should not use this function to call long-running CPU-bound functions! In addition to the usual GIL-related reasons why using threads for CPU-bound work is not very effective in Python, there is an additional problem: on CPython, CPU-bound threads tend to “starve out” IO-bound threads, so using threads for CPU-bound work is likely to adversely affect the main thread running Trio. If you need to do this, you’re better off using a worker process, or perhaps PyPy (which still has a GIL, but may do a better job of fairly allocating CPU time between threads).

**Returns:**

Whatever `sync_fn(*args)` returns.

**Raises:**

**Exception** – Whatever `sync_fn(*args)` raises.

**trio.to_thread.current_default_thread_limiter() → CapacityLimiter**

Get the default `CapacityLimiter` used by `trio.to_thread.run_sync`.

The most common reason to call this would be if you want to modify its `total_tokens` attribute.

### Getting back into the Trio thread from another thread

**trio.from_thread.run(*afn: Callable[[Unpack[Ts]], Awaitable[RetT]]*, **args: Unpack[Ts]*, *trio_token: TrioToken | None = None*) → RetT**

Run the given async function in the parent Trio thread, blocking until it is complete.

**Returns:**

Whatever `afn(*args)` returns.

Returns or raises whatever the given function returns or raises. It can also raise exceptions of its own:

**Raises:**

- **RunFinishedError** – if the corresponding call to `trio.run()` has already completed, or if the run has started its final cleanup phase and can no longer spawn new system tasks.
- **Cancelled** – If the original call to `trio.to_thread.run_sync()` is cancelled (if *trio_token* is None) or the call to `trio.run()` completes (if *trio_token* is not None) while `afn(*args)` is running, then *afn* is likely to raise `trio.Cancelled`.
- **RuntimeError** – if you try calling this from inside the Trio thread, which would otherwise cause a deadlock, or if no `trio_token` was provided, and we can’t infer one from context.
- **TypeError** – if `afn` is not an asynchronous function.

**Locating a TrioToken**: There are two ways to specify which `trio.run` loop to reenter:

> - Spawn this thread from `trio.to_thread.run_sync`. Trio will automatically capture the relevant Trio token and use it to re-enter the same Trio task.
> - Pass a keyword argument, `trio_token` specifying a specific `trio.run` loop to re-enter. This is useful in case you have a “foreign” thread, spawned using some other framework, and still want to enter Trio, or if you want to use a new system task to call `afn`, maybe to avoid the cancellation context of a corresponding `trio.to_thread.run_sync` task. You can get this token from `trio.lowlevel.current_trio_token()`.

**trio.from_thread.run_sync(*fn: Callable[[Unpack[Ts]], RetT]*, **args: Unpack[Ts]*, *trio_token: TrioToken | None = None*) → RetT**

Run the given sync function in the parent Trio thread, blocking until it is complete.

**Returns:**

Whatever `fn(*args)` returns.

Returns or raises whatever the given function returns or raises. It can also raise exceptions of its own:

**Raises:**

- **RunFinishedError** – if the corresponding call to `trio.run` has already completed.
- **RuntimeError** – if you try calling this from inside the Trio thread, which would otherwise cause a deadlock or if no `trio_token` was provided, and we can’t infer one from context.
- **TypeError** – if `fn` is an async function.

**Locating a TrioToken**: There are two ways to specify which `trio.run` loop to reenter:

> - Spawn this thread from `trio.to_thread.run_sync`. Trio will automatically capture the relevant Trio token and use it when you want to re-enter Trio.
> - Pass a keyword argument, `trio_token` specifying a specific `trio.run` loop to re-enter. This is useful in case you have a “foreign” thread, spawned using some other framework, and still want to enter Trio, or if you want to use a new system task to call `fn`, maybe to avoid the cancellation context of a corresponding `trio.to_thread.run_sync` task.

This will probably be clearer with an example. Here we demonstrate how to spawn a child thread, and then use a memory channel to send messages between the thread and a Trio task:

```python3
import trio

def thread_fn(receive_from_trio, send_to_trio):
    while True:
        # Since we're in a thread, we can't call methods on Trio
        # objects directly -- so we use trio.from_thread to call them.
        try:
            request = trio.from_thread.run(receive_from_trio.receive)
        except trio.EndOfChannel:
            trio.from_thread.run(send_to_trio.aclose)
            return
        else:
            response = request + 1
            trio.from_thread.run(send_to_trio.send, response)

async def main():
    send_to_thread, receive_from_trio = trio.open_memory_channel(0)
    send_to_trio, receive_from_thread = trio.open_memory_channel(0)

    async with trio.open_nursery() as nursery:
        # In a background thread, run:
        #   thread_fn(receive_from_trio, send_to_trio)
        nursery.start_soon(
            trio.to_thread.run_sync, thread_fn, receive_from_trio, send_to_trio
        )

        # prints "1"
        await send_to_thread.send(0)
        print(await receive_from_thread.receive())

        # prints "2"
        await send_to_thread.send(1)
        print(await receive_from_thread.receive())

        # When we close the channel, it signals the thread to exit.
        await send_to_thread.aclose()

        # When we exit the nursery, it waits for the background thread to
        # exit.

trio.run(main)
```

Note

The `from_thread.run*` functions reuse the host task that called `trio.to_thread.run_sync()` to run your provided function, as long as you’re using the default `abandon_on_cancel=False` so Trio can be sure that the task will remain around to perform the work. If you pass `abandon_on_cancel=True` at the outset, or if you provide a `TrioToken` when calling back in to Trio, your functions will be executed in a new system task. Therefore, the `current_task()`, `current_effective_deadline()`, or other task-tree specific values may differ depending on keyword argument values.

You can also use `trio.from_thread.check_cancelled()` to check for cancellation from a thread that was spawned by `trio.to_thread.run_sync()`. If the call to `run_sync()` was cancelled, then `check_cancelled()` will raise `trio.Cancelled()`. It’s like `trio.from_thread.run(trio.sleep, 0)`, but much faster.

**trio.from_thread.check_cancelled() → None**

Raise `trio.Cancelled` if the associated Trio task entered a cancelled status.

> Only applicable to threads spawned by `trio.to_thread.run_sync`. Poll to allow `abandon_on_cancel=False` threads to raise `Cancelled` at a suitable place, or to end abandoned `abandon_on_cancel=True` threads sooner than they may otherwise.

**Raises:**

- **Cancelled** – If the corresponding call to `trio.to_thread.run_sync` has had a delivery of cancellation attempted against it, regardless of the value of `abandon_on_cancel` supplied as an argument to it.
- **RuntimeError** – If this thread is not spawned from `trio.to_thread.run_sync`.

Note

To be precise, `check_cancelled()` checks whether the task running `trio.to_thread.run_sync()` has ever been cancelled since the last time it was running a `trio.from_thread.run()` or `trio.from_thread.run_sync()` function. It may raise `trio.Cancelled` even if a cancellation occurred that was later hidden by a modification to `trio.CancelScope.shield` between the cancelled `CancelScope` and `trio.to_thread.run_sync()`. This differs from the behavior of normal Trio checkpoints, which raise `Cancelled` only if the cancellation is still active when the checkpoint executes. The distinction here is *exceedingly* unlikely to be relevant to your application, but we mention it for completeness.

### Threads and task-local storage

When working with threads, you can use the same `contextvars` we discussed above, because their values are preserved.

This is done by automatically copying the `contextvars` context when you use any of:

- `trio.to_thread.run_sync`
- `trio.from_thread.run`
- `trio.from_thread.run_sync`

That means that the values of the context variables are accessible even in worker threads, or when sending a function to be run in the main/parent Trio thread using `trio.from_thread.run` *from* one of these worker threads.

But it also means that as the context is not the same but a copy, if you `set` the context variable value *inside* one of these functions that work in threads, the new value will only be available in that context (that was copied). So, the new value will be available for that function and other internal/children tasks, but the value won’t be available in the parent thread.

If you need to modify values that would live in the context variables and you need to make those modifications from the child threads, you can instead set a mutable object (e.g. a dictionary) in the context variable of the top level/parent Trio thread. Then in the children, instead of setting the context variable, you can `get` the same object, and modify its values. That way you keep the same object in the context variable and only mutate it in child threads.

This way, you can modify the object content in child threads and still access the new content in the parent thread.

Here’s an example:

```python3
import contextvars
import time

import trio

request_state = contextvars.ContextVar("request_state")

# Blocking function that should be run on a thread
# It could be reading or writing files, communicating with a database
# with a driver not compatible with async / await, etc.
def work_in_thread(msg):
    # Only use request_state.get() inside the worker thread
    state_value = request_state.get()
    current_user_id = state_value["current_user_id"]
    time.sleep(3)  # this would be some blocking call, like reading a file
    print(f"Processed user {current_user_id} with message {msg} in a thread worker")
    # Modify/mutate the state object, without setting the entire
    # contextvar with request_state.set()
    state_value["msg"] = msg

# An example "request handler" that does some work itself and also
# spawns some helper tasks in threads to execute blocking code.
async def handle_request(current_user_id):
    # Write to task-local storage:
    current_state = {"current_user_id": current_user_id, "msg": ""}
    request_state.set(current_state)

    # Here the current implicit contextvars context will be automatically copied
    # inside the worker thread
    await trio.to_thread.run_sync(work_in_thread, f"Hello {current_user_id}")
    # Extract the value set inside the thread in the same object stored in a contextvar
    new_msg = current_state["msg"]
    print(
        f"New contextvar value from worker thread for user {current_user_id}: {new_msg}"
    )

# Spawn several "request handlers" simultaneously, to simulate a
# busy server handling multiple requests at the same time.
async def main():
    async with trio.open_nursery() as nursery:
        for i in range(3):
            nursery.start_soon(handle_request, i)

trio.run(main)
```

Running that script will result in the output:

```
Processed user 2 with message Hello 2 in a thread worker
Processed user 0 with message Hello 0 in a thread worker
Processed user 1 with message Hello 1 in a thread worker
New contextvar value from worker thread for user 2: Hello 2
New contextvar value from worker thread for user 1: Hello 1
New contextvar value from worker thread for user 0: Hello 0
```

If you are using `contextvars` or you are using a library that uses them, now you know how they interact when working with threads in Trio.

But have in mind that in many cases it might be a lot simpler to *not* use context variables in your own code and instead pass values in arguments, as it might be more explicit and might be easier to reason about.

Note

The context is automatically copied instead of using the same parent context because a single context can’t be used in more than one thread, it’s not supported by `contextvars`.


## Interactive debugging

When you start an interactive Python session to debug any async program (whether it’s based on `asyncio`, Trio, or something else), every await expression needs to be inside an async function:

```console
$ python
Python 3.10.6
Type "help", "copyright", "credits" or "license" for more information.
>>> import trio
>>> await trio.sleep(1)
File "<stdin>", line 1
SyntaxError: 'await' outside function
>>> async def main():
...     print("hello...")
...     await trio.sleep(1)
...     print("world!")
...
>>> trio.run(main)
hello...
world!
```

This can make it difficult to iterate quickly since you have to redefine the whole function body whenever you make a tweak.

Trio provides a modified interactive console that lets you `await` at the top level. You can access this console by running `python -m trio`:

```console
$ python -m trio
Trio 0.21.0+dev, Python 3.10.6
Use "await" directly instead of "trio.run()".
Type "help", "copyright", "credits" or "license" for more information.
>>> import trio
>>> print("hello..."); await trio.sleep(1); print("world!")
hello...
world!
```

If you are an IPython user, you can use IPython’s autoawait function. This can be enabled within the IPython shell by running the magic command `%autoawait trio`. To have `autoawait` enabled whenever Trio installed, you can add the following to your IPython startup files. (e.g. `~/.ipython/profile_default/startup/10-async.py`)

```python3
try:
    import trio
    get_ipython().run_line_magic("autoawait", "trio")
except ImportError:
    pass
```


## Exceptions and warnings

***exception*trio.Cancelled(**args: object*, ***kwargs: object*)**

Raised by blocking calls if the surrounding scope has been cancelled.

You should let this exception propagate, to be caught by the relevant cancel scope. To remind you of this, it inherits from `BaseException` instead of `Exception`, just like `KeyboardInterrupt` and `SystemExit` do. This means that if you write something like:

```python3
try:
    ...
except Exception:
    ...
```

then this *won’t* catch a `Cancelled` exception.

You cannot raise `Cancelled` yourself. Attempting to do so will produce a `TypeError`. Use `cancel_scope.cancel()` instead.

Note

In the US it’s also common to see this word spelled “canceled”, with only one “l”. This is a recent and US-specific innovation, and even in the US both forms are still commonly used. So for consistency with the rest of the world and with “cancellation” (which always has two “l”s), Trio uses the two “l” spelling everywhere.

***exception*trio.TooSlowError**

Raised by `fail_after()` and `fail_at()` if the timeout expires.

***exception*trio.WouldBlock**

Raised by `X_nowait` functions if `X` would block.

***exception*trio.EndOfChannel**

Raised when trying to receive from a `trio.abc.ReceiveChannel` that has no more data to receive.

This is analogous to an “end-of-file” condition, but for channels.

***exception*trio.BusyResourceError**

Raised when a task attempts to use a resource that some other task is already using, and this would lead to bugs and nonsense.

For example, if two tasks try to send data through the same socket at the same time, Trio will raise `BusyResourceError` instead of letting the data get scrambled.

***exception*trio.ClosedResourceError**

Raised when attempting to use a resource after it has been closed.

Note that “closed” here means that *your* code closed the resource, generally by calling a method with a name like `close` or `aclose`, or by exiting a context manager. If a problem arises elsewhere – for example, because of a network failure, or because a remote peer closed their end of a connection – then that should be indicated by a different exception class, like `BrokenResourceError` or an `OSError` subclass.

***exception*trio.BrokenResourceError**

Raised when an attempt to use a resource fails due to external circumstances.

For example, you might get this if you try to send data on a stream where the remote side has already closed the connection.

You *don’t* get this error if *you* closed the resource – in that case you get `ClosedResourceError`.

This exception’s `__cause__` attribute will often contain more information about the underlying error.

***exception*trio.RunFinishedError**

Raised by `trio.from_thread.run` and similar functions if the corresponding call to `trio.run()` has already finished.

***exception*trio.TrioInternalError**

Raised by `run()` if we encounter a bug in Trio, or (possibly) a misuse of one of the low-level `trio.lowlevel` APIs.

This should never happen! If you get this error, please file a bug.

Unfortunately, if you get this error it also means that all bets are off – Trio doesn’t know what is going on and its normal invariants may be void. (For example, we might have “lost track” of a task. Or lost track of all tasks.) Again, though, this shouldn’t happen.

***exception*trio.TrioDeprecationWarning**

Bases: `FutureWarning`

Warning emitted if you use deprecated Trio functionality.

While a relatively mature project, Trio remains committed to refining its design and improving usability. As part of this, we occasionally deprecate or remove functionality that proves suboptimal. If you use Trio, we recommend subscribing to issue #1 to get information about upcoming deprecations and other backwards compatibility breaking changes.

Despite the name, this class currently inherits from `FutureWarning`, not `DeprecationWarning`, because until a 1.0 release, we want these warnings to be visible by default. You can hide them by installing a filter or with the `-W` switch: see the `warnings` documentation for details.
