---
title: "Trio’s core functionality (part 1/4)"
source: https://trio.readthedocs.io/en/stable/reference-core.html
domain: trio-async
license: CC-BY-SA-4.0
tags: python trio, trio structured concurrency, async nursery python
fetched: 2026-07-02
part: 1/4
---

# Trio’s core functionality


## Entering Trio

If you want to use Trio, then the first thing you have to do is call `trio.run()`:

**trio.run(*async_fn: Callable[[Unpack[PosArgT]], Awaitable[RetT]]*, **args: Unpack[PosArgT]*, *clock: Clock | None = None*, *instruments: Sequence[Instrument] = ()*, *restrict_keyboard_interrupt_to_checkpoints: bool = False*, *strict_exception_groups: bool = True*) → RetT**

Run a Trio-flavored async function, and return the result.

Calling:

```python3
run(async_fn, *args)
```

is the equivalent of:

```python3
await async_fn(*args)
```

except that `run()` can (and must) be called from a synchronous context.

This is Trio’s main entry point. Almost every other function in Trio requires that you be inside a call to `run()`.

**Parameters:**

- **async_fn** – An async function.
- **args** – Positional arguments to be passed to *async_fn*. If you need to pass keyword arguments, then use `functools.partial()`.
- **clock** – `None` to use the default system-specific monotonic clock; otherwise, an object implementing the `trio.abc.Clock` interface, like (for example) a `trio.testing.MockClock` instance.
- **instruments** (list of `trio.abc.Instrument` objects) – Any instrumentation you want to apply to this run. This can also be modified during the run; see Instrument API.
- **restrict_keyboard_interrupt_to_checkpoints** (*bool*) – What happens if the user hits control-C while `run()` is running? If this argument is False (the default), then you get the standard Python behavior: a `KeyboardInterrupt` exception will immediately interrupt whatever task is running (or if no task is running, then Trio will wake up a task to be interrupted). Alternatively, if you set this argument to True, then `KeyboardInterrupt` delivery will be delayed: it will be *only* be raised at checkpoints, like a `Cancelled` exception. The default behavior is nice because it means that even if you accidentally write an infinite loop that never executes any checkpoints, then you can still break out of it using control-C. The alternative behavior is nice if you’re paranoid about a `KeyboardInterrupt` at just the wrong place leaving your program in an inconsistent state, because it means that you only have to worry about `KeyboardInterrupt` at the exact same places where you already have to worry about `Cancelled`. This setting has no effect if your program has registered a custom SIGINT handler, or if `run()` is called from anywhere but the main thread (this is a Python limitation), or if you use `open_signal_receiver()` to catch SIGINT.
- **strict_exception_groups** (*bool*) – Unless set to False, nurseries will always wrap even a single raised exception in an exception group. This can be overridden on the level of individual nurseries. Setting it to False will be deprecated and ultimately removed in a future version of Trio.

**Returns:**

Whatever `async_fn` returns.

**Raises:**

- **TrioInternalError** – if an unexpected error is encountered inside Trio’s internal machinery. This is a bug and you should let us know.
- **Anything else** – if `async_fn` raises an exception, then `run()` propagates it.


## General principles

### Checkpoints

When writing code using Trio, it’s very important to understand the concept of a *checkpoint*. Many of Trio’s functions act as checkpoints.

A checkpoint is two things:

1. It’s a point where Trio checks for cancellation. For example, if the code that called your function set a timeout, and that timeout has expired, then the next time your function executes a checkpoint Trio will raise a `Cancelled` exception. See Cancellation and timeouts below for more details.
2. It’s a point where the Trio scheduler checks its scheduling policy to see if it’s a good time to switch to another task, and potentially does so. (Currently, this check is very simple: the scheduler always switches at every checkpoint. But this might change in the future.)

When writing Trio code, you need to keep track of where your checkpoints are. Why? First, because checkpoints require extra scrutiny: whenever you execute a checkpoint, you need to be prepared to handle a `Cancelled` error, or for another task to run and rearrange some state out from under you. And second, because you also need to make sure that you have *enough* checkpoints: if your code doesn’t pass through a checkpoint on a regular basis, then it will be slow to notice and respond to cancellation and – much worse – since Trio is a cooperative multi-tasking system where the *only* place the scheduler can switch tasks is at checkpoints, it’ll also prevent the scheduler from fairly allocating time between different tasks and adversely effect the response latency of all the other code running in the same process. (Informally we say that a task that does this is “hogging the run loop”.)

So when you’re doing code review on a project that uses Trio, one of the things you’ll want to think about is whether there are enough checkpoints, and whether each one is handled correctly. Of course this means you need a way to recognize checkpoints. How do you do that? The underlying principle is that any operation that blocks has to be a checkpoint. This makes sense: if an operation blocks, then it might block for a long time, and you’ll want to be able to cancel it if a timeout expires; and in any case, while this task is blocked we want another task to be scheduled to run so our code can make full use of the CPU.

But if we want to write correct code in practice, then this principle is a little too sloppy and imprecise to be useful. How do we know which functions might block? What if a function blocks sometimes, but not others, depending on the arguments passed / network speed / phase of the moon? How do we figure out where the checkpoints are when we’re stressed and sleep deprived but still want to get this code review right, and would prefer to reserve our mental energy for thinking about the actual logic instead of worrying about checkpoints?

Don’t worry – Trio’s got your back. Since checkpoints are important and ubiquitous, we make it as simple as possible to keep track of them. Here are the rules:

- Regular (synchronous) functions never contain any checkpoints.
- If you call an async function provided by Trio (`await <something in trio>`), and it doesn’t raise an exception, then it *always* acts as a checkpoint. (If it does raise an exception, it might act as a checkpoint or might not.)
  - This includes async iterators: If you write `async for ... in <a trio object>`, then there will be at least one checkpoint in each iteration of the loop, and it will still checkpoint if the iterable is empty.
  - Partial exception for async context managers: Both the entry and exit of an `async with` block are defined as async functions; but for a particular type of async context manager, it’s often the case that only one of them is able to block, which means only that one will act as a checkpoint. This is documented on a case-by-case basis.
    - `trio.open_nursery()` is a further exception to this rule.
- Third-party async functions / iterators / context managers can act as checkpoints; if you see `await <something>` or one of its friends, then that *might* be a checkpoint. So to be safe, you should prepare for scheduling or cancellation happening there.

The reason we distinguish between Trio functions and other functions is that we can’t make any guarantees about third party code. Checkpoint-ness is a transitive property: if function A acts as a checkpoint, and you write a function that calls function A, then your function also acts as a checkpoint. If you don’t, then it isn’t. So there’s nothing stopping someone from writing a function like:

```python
# technically legal, but bad style:
async def why_is_this_async():
    return 7
```

that never calls any of Trio’s async functions. This is an async function, but it’s not a checkpoint. But why make a function async if it never calls any async functions? It’s possible, but it’s a bad idea. If you have a function that’s not calling any async functions, then you should make it synchronous. The people who use your function will thank you, because it makes it obvious that your function is not a checkpoint, and their code reviews will go faster.

(Remember how in the tutorial we emphasized the importance of the “async sandwich”, and the way it means that `await` ends up being a marker that shows when you’re calling a function that calls a function that … eventually calls one of Trio’s built-in async functions? The transitivity of async-ness is a technical requirement that Python imposes, but since it exactly matches the transitivity of checkpoint-ness, we’re able to exploit it to help you keep track of checkpoints. Pretty sneaky, eh?)

A slightly trickier case is a function like:

```python
async def sleep_or_not(should_sleep):
    if should_sleep:
        await trio.sleep(1)
    else:
        pass
```

Here the function acts as a checkpoint if you call it with `should_sleep` set to a true value, but not otherwise. This is why we emphasize that Trio’s own async functions are *unconditional* checkpoints: they *always* check for cancellation and check for scheduling, regardless of what arguments they’re passed. If you find an async function in Trio that doesn’t follow this rule, then it’s a bug and you should let us know.

Inside Trio, we’re very picky about this, because Trio is the foundation of the whole system so we think it’s worth the extra effort to make things extra predictable. It’s up to you how picky you want to be in your code. To give you a more realistic example of what this kind of issue looks like in real life, consider this function:

```python
async def recv_exactly(sock, nbytes):
    data = bytearray()
    while nbytes > 0:
        # recv() reads up to 'nbytes' bytes each time
        chunk = await sock.recv(nbytes)
        if not chunk:
            raise RuntimeError("socket unexpected closed")
        nbytes -= len(chunk)
        data += chunk
    return data
```

If called with an `nbytes` that’s greater than zero, then it will call `sock.recv` at least once, and `recv` is an async Trio function, and thus an unconditional checkpoint. So in this case, `recv_exactly` acts as a checkpoint. But if we do `await recv_exactly(sock, 0)`, then it will immediately return an empty buffer without executing a checkpoint. If this were a function in Trio itself, then this wouldn’t be acceptable, but you may decide you don’t want to worry about this kind of minor edge case in your own code.

If you do want to be careful, or if you have some CPU-bound code that doesn’t have enough checkpoints in it, then it’s useful to know that `await trio.sleep(0)` is an idiomatic way to execute a checkpoint without doing anything else, and that `trio.testing.assert_checkpoints()` can be used to test that an arbitrary block of code contains a checkpoint.

### Thread safety

The vast majority of Trio’s API is *not* thread safe: it can only be used from inside a call to `trio.run()`. This manual doesn’t bother documenting this on individual calls; unless specifically noted otherwise, you should assume that it isn’t safe to call any Trio functions from anywhere except the Trio thread. (But see below if you really do need to work with threads.)


## Time and clocks

Every call to `run()` has an associated clock.

By default, Trio uses an unspecified monotonic clock, but this can be changed by passing a custom clock object to `run()` (e.g. for testing).

You should not assume that Trio’s internal clock matches any other clock you have access to, including the clocks of simultaneous calls to `trio.run()` happening in other processes or threads!

The default clock is currently implemented as `time.perf_counter()` plus a large random offset. The idea here is to catch code that accidentally uses `time.perf_counter()` early, which should help keep our options open for changing the clock implementation later, and (more importantly) make sure you can be confident that custom clocks like `trio.testing.MockClock` will work with third-party libraries you don’t control.

**trio.current_time() → float**

Returns the current time according to Trio’s internal clock.

**Returns:**

The current time.

**Return type:**

float

**Raises:**

**RuntimeError** – if not inside a call to `trio.run()`.

***await*trio.sleep(*seconds: float*) → None**

Pause execution of the current task for the given number of seconds.

**Parameters:**

**seconds** (*float*) – The number of seconds to sleep. May be zero to insert a checkpoint without actually blocking.

**Raises:**

**ValueError** – if *seconds* is negative or NaN.

***await*trio.sleep_until(*deadline: float*) → None**

Pause execution of the current task until the given time.

The difference between `sleep()` and `sleep_until()` is that the former takes a relative time and the latter takes an absolute time according to Trio’s internal clock (as returned by `current_time()`).

**Parameters:**

**deadline** (*float*) – The time at which we should wake up again. May be in the past, in which case this function executes a checkpoint but does not block.

**Raises:**

**ValueError** – if deadline is NaN.

***await*trio.sleep_forever() → NoReturn**

Pause execution of the current task forever (or until cancelled).

Equivalent to calling `await sleep(math.inf)`, except that if manually rescheduled this will raise a `RuntimeError`.

**Raises:**

**RuntimeError** – if rescheduled

If you’re a mad scientist or otherwise feel the need to take direct control over the PASSAGE OF TIME ITSELF, then you can implement a custom `Clock` class:

***class*trio.abc.Clock**

The interface for custom run loop clocks.

***abstractmethod*current_time() → float**

Return the current time, according to this clock.

This is used to implement functions like `trio.current_time()` and `trio.move_on_after()`.

**Returns:**

The current time.

**Return type:**

float

***abstractmethod*deadline_to_sleep_time(*deadline: float*) → float**

Compute the real time until the given deadline.

This is called before we enter a system-specific wait function like `select.select()`, to get the timeout to pass.

For a clock using wall-time, this should be something like:

```python3
return deadline - self.current_time()
```

but of course it may be different if you’re implementing some kind of virtual clock.

**Parameters:**

**deadline** (*float*) – The absolute time of the next deadline, according to this clock.

**Returns:**

The number of real seconds to sleep until the given deadline. May be `math.inf`.

**Return type:**

float

***abstractmethod*start_clock() → None**

Do any setup this clock might need.

Called at the beginning of the run.


## Cancellation and timeouts

Trio has a rich, composable system for cancelling work, either explicitly or when a timeout expires.

### A simple timeout example

In the simplest case, you can apply a timeout to a block of code:

```python
with trio.move_on_after(30):
    result = await do_http_get("https://...")
    print("result is", result)
print("with block finished")
```

We refer to `move_on_after()` as creating a “cancel scope”, which contains all the code that runs inside the `with` block. If the HTTP request takes more than 30 seconds to run, then it will be cancelled: we’ll abort the request and we *won’t* see `result is ...` printed on the console; instead we’ll go straight to printing the `with block finished` message.

Note

Note that this is a single 30 second timeout for the entire body of the `with` statement. This is different from what you might have seen with other Python libraries, where timeouts often refer to something more complicated. We think this way is easier to reason about.

How does this work? There’s no magic here: Trio is built using ordinary Python functionality, so we can’t just abandon the code inside the `with` block. Instead, we take advantage of Python’s standard way of aborting a large and complex piece of code: we raise an exception.

Here’s the idea: whenever you call a cancellable function like `await trio.sleep(...)` or `await sock.recv(...)` – see Checkpoints – then the first thing that function does is to check if there’s a surrounding cancel scope whose timeout has expired, or otherwise been cancelled. If so, then instead of performing the requested operation, the function fails immediately with a `Cancelled` exception. In this example, this probably happens somewhere deep inside the bowels of `do_http_get`. The exception then propagates out like any normal exception (you could even catch it if you wanted, but that’s generally a bad idea), until it reaches the `with move_on_after(...):`. And at this point, the `Cancelled` exception has done its job – it’s successfully unwound the whole cancelled scope – so `move_on_after()` catches it, and execution continues as normal after the `with` block. And this all works correctly even if you have nested cancel scopes, because every `Cancelled` object carries an invisible marker that makes sure that the cancel scope that triggered it is the only one that will catch it.

### Handling cancellation

Pretty much any code you write using Trio needs to have some strategy to handle `Cancelled` exceptions – even if you didn’t set a timeout, then your caller might (and probably will).

You can catch `Cancelled`, but you shouldn’t! Or more precisely, if you do catch it, then you should do some cleanup and then re-raise it or otherwise let it continue propagating (unless you encounter an error, in which case it’s OK to let that propagate instead). To help remind you of this fact, `Cancelled` inherits from `BaseException`, like `KeyboardInterrupt` and `SystemExit` do, so that it won’t be caught by catch-all `except Exception:` blocks.

It’s also important in any long-running code to make sure that you regularly check for cancellation, because otherwise timeouts won’t work! This happens implicitly every time you call a cancellable operation; see below for details. If you have a task that has to do a lot of work without any I/O, then you can use `await sleep(0)` to insert an explicit cancel+schedule point.

Here’s a rule of thumb for designing good Trio-style (“trionic”?) APIs: if you’re writing a reusable function, then you shouldn’t take a `timeout=` parameter, and instead let your caller worry about it. This has several advantages. First, it leaves the caller’s options open for deciding how they prefer to handle timeouts – for example, they might find it easier to work with absolute deadlines instead of relative timeouts. If they’re the ones calling into the cancellation machinery, then they get to pick, and you don’t have to worry about it. Second, and more importantly, this makes it easier for others to reuse your code. If you write a `http_get` function, and then I come along later and write a `log_in_to_twitter` function that needs to internally make several `http_get` calls, I don’t want to have to figure out how to configure the individual timeouts on each of those calls – and with Trio’s timeout system, it’s totally unnecessary.

Of course, this rule doesn’t apply to APIs that need to impose internal timeouts. For example, if you write a `start_http_server` function, then you probably should give your caller some way to configure timeouts on individual requests.

### Cancellation semantics

You can freely nest cancellation blocks, and each `Cancelled` exception “knows” which block it belongs to. So long as you don’t stop it, the exception will keep propagating until it reaches the block that raised it, at which point it will stop automatically.

Here’s an example:

```python
print("starting...")
with trio.move_on_after(5):
    with trio.move_on_after(10):
        await trio.sleep(20)
        print("sleep finished without error")
    print("move_on_after(10) finished without error")
print("move_on_after(5) finished without error")
```

In this code, the outer scope will expire after 5 seconds, causing the `sleep()` call to return early with a `Cancelled` exception. Then this exception will propagate through the `with move_on_after(10)` line until it’s caught by the `with move_on_after(5)` context manager. So this code will print:

```
starting...
move_on_after(5) finished without error
```

The end result is that Trio has successfully cancelled exactly the work that was happening within the scope that was cancelled.

Looking at this, you might wonder how you can tell whether the inner block timed out – perhaps you want to do something different, like try a fallback procedure or report a failure to our caller. To make this easier, `move_on_after()`´s `__enter__` function returns an object representing this cancel scope, which we can use to check whether this scope caught a `Cancelled` exception:

```python
with trio.move_on_after(5) as cancel_scope:
    await trio.sleep(10)
print(cancel_scope.cancelled_caught)  # prints "True"
```

The `cancel_scope` object also allows you to check or adjust this scope’s deadline, explicitly trigger a cancellation without waiting for the deadline, check if the scope has already been cancelled, and so forth – see `CancelScope` below for the full details.

Cancellations in Trio are “level triggered”, meaning that once a block has been cancelled, *all* cancellable operations in that block will keep raising `Cancelled`. This helps avoid some pitfalls around resource clean-up. For example, imagine that we have a function that connects to a remote server and sends some messages, and then cleans up on the way out:

```python
with trio.move_on_after(TIMEOUT):
    conn = make_connection()
    try:
        await conn.send_hello_msg()
    finally:
        await conn.send_goodbye_msg()
```

Now suppose that the remote server stops responding, so our call to `await conn.send_hello_msg()` hangs forever. Fortunately, we were clever enough to put a timeout around this code, so eventually the timeout will expire and `send_hello_msg` will raise `Cancelled`. But then, in the `finally` block, we make another blocking operation, which will also hang forever! At this point, if we were using `asyncio` or another library with “edge-triggered” cancellation, we’d be in trouble: since our timeout already fired, it wouldn’t fire again, and at this point our application would lock up forever. But in Trio, this *doesn’t* happen: the `await conn.send_goodbye_msg()` call is still inside the cancelled block, so it will also raise `Cancelled`.

Of course, if you really want to make another blocking call in your cleanup handler, Trio will let you; it’s trying to prevent you from accidentally shooting yourself in the foot. Intentional foot-shooting is no problem (or at least – it’s not Trio’s problem). To do this, create a new scope, and set its `shield` attribute to `True`:

```python
with trio.move_on_after(TIMEOUT):
    conn = make_connection()
    try:
        await conn.send_hello_msg()
    finally:
        with trio.move_on_after(CLEANUP_TIMEOUT, shield=True) as cleanup_scope:
            await conn.send_goodbye_msg()
```

So long as you’re inside a scope with `shield = True` set, then you’ll be protected from outside cancellations. Note though that this *only* applies to *outside* cancellations: if `CLEANUP_TIMEOUT` expires then `await conn.send_goodbye_msg()` will still be cancelled, and if `await conn.send_goodbye_msg()` call uses any timeouts internally, then those will continue to work normally as well. This is a pretty advanced feature that most people probably won’t use, but it’s there for the rare cases where you need it.

### Cancellation and primitive operations

We’ve talked a lot about what happens when an operation is cancelled, and how you need to be prepared for this whenever calling a cancellable operation… but we haven’t gone into the details about which operations are cancellable, and how exactly they behave when they’re cancelled.

Here’s the rule: if it’s in the `trio` namespace, and you use `await` to call it, then it’s cancellable (see Checkpoints above). Cancellable means:

- If you try to call it when inside a cancelled scope, then it will raise `Cancelled`.
- If it blocks, and while it’s blocked then one of the scopes around it becomes cancelled, it will return early and raise `Cancelled`.
- Raising `Cancelled` means that the operation *did not happen*. If a Trio socket’s `send` method raises `Cancelled`, then no data was sent. If a Trio socket’s `recv` method raises `Cancelled` then no data was lost – it’s still sitting in the socket receive buffer waiting for you to call `recv` again. And so forth.

There are a few idiosyncratic cases where external constraints make it impossible to fully implement these semantics. These are always documented. There is also one systematic exception:

- Async cleanup operations – like `__aexit__` methods or async close methods – are cancellable just like anything else *except* that if they are cancelled, they still perform a minimum level of cleanup before raising `Cancelled`.

For example, closing a TLS-wrapped socket normally involves sending a notification to the remote peer, so that they can be cryptographically assured that you really meant to close the socket, and your connection wasn’t just broken by a man-in-the-middle attacker. But handling this robustly is a bit tricky. Remember our example above where the blocking `send_goodbye_msg` caused problems? That’s exactly how closing a TLS socket works: if the remote peer has disappeared, then our code may never be able to actually send our shutdown notification, and it would be nice if it didn’t block forever trying. Therefore, the method for closing a TLS-wrapped socket will *try* to send that notification – and if it gets cancelled, then it will give up on sending the message, but *will* still close the underlying socket before raising `Cancelled`, so at least you don’t leak that resource.

### Cancellation API details

`move_on_after()` and all the other cancellation facilities provided by Trio are ultimately implemented in terms of `CancelScope` objects.

***class*trio.CancelScope(***, *relative_deadline: float = inf*, *deadline: float = inf*, *shield: bool = False*)**

A *cancellation scope*: the link between a unit of cancellable work and Trio’s cancellation system.

A `CancelScope` becomes associated with some cancellable work when it is used as a context manager surrounding that work:

```python3
cancel_scope = trio.CancelScope()
...
with cancel_scope:
    await long_running_operation()
```

Inside the `with` block, a cancellation of `cancel_scope` (via a call to its `cancel()` method or via the expiry of its `deadline`) will immediately interrupt the `long_running_operation()` by raising `Cancelled` at its next checkpoint.

The context manager `__enter__` returns the `CancelScope` object itself, so you can also write `with trio.CancelScope() as cancel_scope:`.

If a cancel scope becomes cancelled before entering its `with` block, the `Cancelled` exception will be raised at the first checkpoint inside the `with` block. This allows a `CancelScope` to be created in one task and passed to another, so that the first task can later cancel some work inside the second.

Cancel scopes are not reusable or reentrant; that is, each cancel scope can be used for at most one `with` block. (You’ll get a `RuntimeError` if you violate this rule.)

The `CancelScope` constructor takes initial values for the cancel scope’s `deadline` and `shield` attributes; these may be freely modified after construction, whether or not the scope has been entered yet, and changes take immediate effect.

**deadline**

Read-write, `float`. An absolute time on the current run’s clock at which this scope will automatically become cancelled. You can adjust the deadline by modifying this attribute, e.g.:

```python3
# I need a little more time!
cancel_scope.deadline += 30
```

Note that for efficiency, the core run loop only checks for expired deadlines every once in a while. This means that in certain cases there may be a short delay between when the clock says the deadline should have expired, and when checkpoints start raising `Cancelled`. This is a very obscure corner case that you’re unlikely to notice, but we document it for completeness. (If this *does* cause problems for you, of course, then we want to know!)

Defaults to `math.inf`, which means “no deadline”, though this can be overridden by the `deadline=` argument to the `CancelScope` constructor.

**relative_deadline**

Read-write, `float`. The number of seconds remaining until this scope’s deadline, relative to the current time.

Defaults to `math.inf` (“no deadline”). Must be non-negative.

When modified Before entering: sets the deadline relative to when the scope enters. After entering: sets a new deadline relative to the current time.

**Raises:**

**RuntimeError** – if trying to read or modify an unentered scope with an absolute deadline, i.e. when `is_relative` is `False`.

**shield**

Read-write, `bool`, default `False`. So long as this is set to `True`, then the code inside this scope will not receive `Cancelled` exceptions from scopes that are outside this scope. They can still receive `Cancelled` exceptions from (1) this scope, or (2) scopes inside this scope. You can modify this attribute:

```python3
with trio.CancelScope() as cancel_scope:
    cancel_scope.shield = True
    # This cannot be interrupted by any means short of
    # killing the process:
    await sleep(10)

    cancel_scope.shield = False
    # Now this can be cancelled normally:
    await sleep(10)
```

Defaults to `False`, though this can be overridden by the `shield=` argument to the `CancelScope` constructor.

**is_relative()**

Returns None after entering. Returns False if both deadline and relative_deadline are inf.

**cancel()**

Cancels this scope immediately.

The optional `reason` argument accepts a string, which will be attached to any resulting `Cancelled` exception to help you understand where that cancellation is coming from and why it happened.

This method is idempotent, i.e., if the scope was already cancelled then this method silently does nothing.

**cancelled_caught**

Readonly `bool`. Records whether this scope caught a `Cancelled` exception. This requires two things: (1) the `with` block exited with a `Cancelled` exception, and (2) this scope is the one that was responsible for triggering this `Cancelled` exception.

**cancel_called**

Readonly `bool`. Records whether cancellation has been requested for this scope, either by an explicit call to `cancel()` or by the deadline expiring.

This attribute being True does *not* necessarily mean that the code within the scope has been, or will be, affected by the cancellation. For example, if `cancel()` was called after the last checkpoint in the `with` block, when it’s too late to deliver a `Cancelled` exception, then this attribute will still be True.

This attribute is mostly useful for debugging and introspection. If you want to know whether or not a chunk of code was actually cancelled, then `cancelled_caught` is usually more appropriate.

Often there is no need to create `CancelScope` object. Trio already includes `cancel_scope` attribute in a task-related `Nursery` object. We will cover nurseries later in the manual.

Trio also provides several convenience functions for the common situation of just wanting to impose a timeout on some code:

***with*trio.move_on_after(*seconds: float*, ***, *shield: bool = False*) → CancelScope*as cancel_scope***

Use as a context manager to create a cancel scope whose deadline is set to now + *seconds*.

The deadline of the cancel scope is calculated upon entering.

**Parameters:**

- **seconds** (*float*) – The timeout.
- **shield** (*bool*) – Initial value for the `shield` attribute of the newly created cancel scope.

**Raises:**

**ValueError** – if `seconds` is less than zero or NaN.

***with*trio.move_on_at(*deadline: float*, ***, *shield: bool = False*) → CancelScope*as cancel_scope***

Use as a context manager to create a cancel scope with the given absolute deadline.

**Parameters:**

- **deadline** (*float*) – The deadline.
- **shield** (*bool*) – Initial value for the `shield` attribute of the newly created cancel scope.

**Raises:**

**ValueError** – if deadline is NaN.

***with*trio.fail_after(*seconds: float*, ***, *shield: bool = False*) → CancelScope*as cancel_scope***

Creates a cancel scope with the given timeout, and raises an error if it is actually cancelled.

This function and `move_on_after()` are similar in that both create a cancel scope with a given timeout, and if the timeout expires then both will cause `Cancelled` to be raised within the scope. The difference is that when the `Cancelled` exception reaches `move_on_after()`, it’s caught and discarded. When it reaches `fail_after()`, then it’s caught and `TooSlowError` is raised in its place.

The deadline of the cancel scope is calculated upon entering.

**Parameters:**

- **seconds** (*float*) – The timeout.
- **shield** (*bool*) – Initial value for the `shield` attribute of the newly created cancel scope.

**Raises:**

- **TooSlowError** – if a `Cancelled` exception is raised in this scope and caught by the context manager.
- **ValueError** – if *seconds* is less than zero or NaN.

***with*trio.fail_at(*deadline: float*, ***, *shield: bool = False*) → CancelScope*as cancel_scope***

Creates a cancel scope with the given deadline, and raises an error if it is actually cancelled.

This function and `move_on_at()` are similar in that both create a cancel scope with a given absolute deadline, and if the deadline expires then both will cause `Cancelled` to be raised within the scope. The difference is that when the `Cancelled` exception reaches `move_on_at()`, it’s caught and discarded. When it reaches `fail_at()`, then it’s caught and `TooSlowError` is raised in its place.

**Parameters:**

- **deadline** (*float*) – The deadline.
- **shield** (*bool*) – Initial value for the `shield` attribute of the newly created cancel scope.

**Raises:**

- **TooSlowError** – if a `Cancelled` exception is raised in this scope and caught by the context manager.
- **ValueError** – if deadline is NaN.

#### Cheat sheet

- If you want to impose a timeout on a function, but you don’t care whether it timed out or not: with trio.move_on_after(TIMEOUT): await do_whatever() # carry on!
- If you want to impose a timeout on a function, and then do some recovery if it timed out: with trio.move_on_after(TIMEOUT) as cancel_scope: await do_whatever() if cancel_scope.cancelled_caught: # The operation timed out, try something else try_to_recover()
- If you want to impose a timeout on a function, and then if it times out then just give up and raise an error for your caller to deal with: with trio.fail_after(TIMEOUT): await do_whatever()

It’s also possible to check what the current effective deadline is, which is sometimes useful:

**trio.current_effective_deadline() → float**

Returns the current effective deadline for the current task.

This function examines all the cancellation scopes that are currently in effect (taking into account shielding), and returns the deadline that will expire first.

One example of where this might be is useful is if your code is trying to decide whether to begin an expensive operation like an RPC call, but wants to skip it if it knows that it can’t possibly complete in the available time. Another example would be if you’re using a protocol like gRPC that propagates timeout information to the remote peer; this function gives a way to fetch that information so you can send it along.

If this is called in a context where a cancellation is currently active (i.e., a blocking call will immediately raise `Cancelled`), then returned deadline is `-inf`. If it is called in a context where no scopes have a deadline set, it returns `inf`.

**Returns:**

the effective deadline, as an absolute time.

**Return type:**

float
