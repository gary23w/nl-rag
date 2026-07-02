---
title: "Async/await"
source: https://en.wikipedia.org/wiki/Async/await
domain: poem-rust-web
license: CC-BY-SA-4.0
tags: poem rust framework, rust openapi framework, rust async web, poem endpoint middleware
fetched: 2026-07-02
---

# Async/await

In computer programming, the **async/await pattern** is a syntactic feature of many programming languages that allows an asynchronous, non-blocking function to be structured in a way similar to an ordinary synchronous function.

It is semantically related to the concept of a coroutine and is often implemented using similar techniques, and is primarily intended to provide opportunities for the program to execute other code while waiting for a long-running, asynchronous task to complete, usually represented by promises or similar data structures. The feature is found in C#, C++, Python, F#, Hack, Julia, Dart, Kotlin, Rust, Nim, JavaScript, and Swift.

## History

F# added asynchronous workflows with await points in version 2.0 in 2007. This influenced the async/await mechanism added to C#.

Haskell lead developer Simon Marlow created the async package in 2010.

Microsoft first released a version of C# with async/await in the Async CTP (2011). It was later officially released in C# 5 (2012).

Python added support for async/await with version 3.5 in 2015 adding 2 new keywords, `async` and `await`.

TypeScript added support for async/await with version 1.7 in 2015.

JavaScript added support for async/await in 2017 as part of ECMAScript 2017 JavaScript edition.

Rust added support for async/await with version 1.39.0 in 2019 using the `async` keyword and the `.await` postfix operator, both introduced in the 2018 edition of the language.

C++ added support for async/await with version 20 in 2020 with 3 new keywords `co_return`, `co_await`, `co_yield`.

Swift added support for async/await with version 5.5 in 2021, adding 2 new keywords `async` and `await`. This was released alongside a concrete implementation of the Actor model with the `actor` keyword which uses async/await to mediate access to each actor from outside.

## Example

The C# function below, which downloads a resource from a URI and returns the resource's length, uses this async/await pattern:

```mw
using System;
using System.Net.Http;
using System.Threading.Tasks;

public async Task<int> FindSizeOfPageAsync(Uri uri) 
{
    HttpClient client = new();
    byte[] data = await client.GetByteArrayAsync(uri);
    return data.Length;
}
```

- First, the `async` keyword indicates to C# that the method is asynchronous, meaning that it may use an arbitrary number of `await` expressions and will bind the result to a promise.
- The return type, `Task<T>`, is C#'s analogue to the concept of a promise, and here is indicated to have a result value of type `int`.
- The first expression to execute when this method is called will be `new HttpClient().GetByteArrayAsync(uri)`, which is another asynchronous method returning a `Task<byte[]>`. Because this method is asynchronous, it will not download the entire batch of data before returning. Instead, it will begin the download process using a non-blocking mechanism (such as a background thread), and immediately return an unresolved, unrejected `Task<byte[]>` to this function.
- With the `await` keyword attached to the `Task`, this function will immediately proceed to return a `Task<int>` to its caller, who may then continue on with other processing as needed.
- Once `GetByteArrayAsync()` finishes its download, it will resolve the `Task` it returned with the downloaded data. This will trigger a callback and cause `FindPageSizeAsync()` to continue execution by assigning that value to `data`.
- Finally, the method returns `data.Length`, a simple integer indicating the length of the array. The compiler re-interprets this as resolving the `Task` it returned earlier, triggering a callback in the method's caller to do something with that length value.

A function using async/await can use as many `await` expressions as it wants, and each will be handled in the same way (though a promise will only be returned to the caller for the first await, while every other await will utilize internal callbacks). A function can also hold a promise object directly and do other processing first (including starting other asynchronous tasks), delaying awaiting the promise until its result is needed. Functions with promises also have promise aggregation methods that allow the program to await multiple promises at once or in some special pattern (such as C#'s `Task.WhenAll()`, which returns a valueless `Task` that resolves when all of the tasks in the arguments have resolved). Many promise types also have additional features beyond what the async/await pattern normally uses, such as being able to set up more than one result callback or inspect the progress of an especially long-running task.

In the particular case of C#, and in many other languages with this language feature, the async/await pattern is not a core part of the language's runtime, but is instead implemented with lambdas or continuations at compile time. For instance, the C# compiler would likely translate the above code to something like the following before translating it to its IL bytecode format:

```mw
using System;
using System.Net.Http;
using System.Threading.Tasks;

public Task<int> FindSizeOfPageAsync(Uri uri) 
{
    HttpClient client = new();
    Task<byte[]> dataTask = client.GetByteArrayAsync(uri);
    Task<int> afterDataTask = dataTask.ContinueWith((originalTask) => {
        return originalTask.Result.Length;
    });
    return afterDataTask;
}
```

Because of this, if an interface method needs to return a promise object, but itself does not require `await` in the body to wait on any asynchronous tasks, it does not need the `async` modifier either and can instead return a promise object directly. For instance, a function might be able to provide a promise that immediately resolves to some result value (such as C#'s `Task.FromResult()`), or it may simply return another method's promise that happens to be the exact promise needed (such as when deferring to an overload).

One important caveat of this functionality, however, is that while the code resembles traditional blocking code, the code is actually non-blocking and potentially multithreaded, meaning that many intervening events may occur while waiting for the promise targeted by an `await` to resolve. For instance, the following code, while always succeeding in a blocking model without `await`, may experience intervening events during the `await` and may thus find shared state changed out from under it:

```mw
using System;
using System.Diagnostics;
using System.Net.Http;

string name = state.name;
HttpClient client = new();
byte[] data = await client.GetByteArrayAsync(uri);

// Potential failure, as value of state.a may have been changed
// by the handler of potentially intervening event.
Debug.Assert(name == state.name);

return data.Length;
```

## Implementations

### C

The C language does not support await/async. Some coroutine libraries such as *s_task* simulate the keywords await/async with macros.

```mw
#include <stdio.h>
#include "s_task.h"

constexpr int STACK_SIZE = 64 * 1024 / sizeof(int);

// define stack memory for tasks
int g_stack_main[STACK_SIZE];
int g_stack0[STACK_SIZE];
int g_stack1[STACK_SIZE];

void sub_task(__async__, void* arg) {
    int n = (int)(size_t)arg;
    for (int i = 0; i < 5; ++i) {
        printf("task %d, delay seconds = %d, i = %d\n", n, n, i);
        s_task_msleep(__await__, n * 1000);
        // s_task_yield(__await__);
    }
}

void main_task(__async__, void* arg) {
    // create two sub-tasks
    s_task_create(g_stack0, sizeof(g_stack0), sub_task, (void*)1);
    s_task_create(g_stack1, sizeof(g_stack1), sub_task, (void*)2);

    for (int i = 0; i < 4; ++i) {
        printf("task_main arg = %p, i = %d\n", arg, i);
        s_task_yield(__await__);
    }

    // wait for the sub-tasks for exit
    s_task_join(__await__, g_stack0);
    s_task_join(__await__, g_stack1);
}

int main(int argc, char* argv[]) {
    s_task_init_system();

    // create the main task
    s_task_create(g_stack_main, sizeof(g_stack_main), main_task, (void*)(size_t)argc);
    s_task_join(__await__, g_stack_main);
    printf("all task is over\n");
    return 0;
}
```

### C++

In C++, await (named `co_await` in C++ to emphasise its context in coroutines) has been officially merged into C++20. Support for it, coroutines, and the keywords such as `co_await` are available in GCC and MSVC compilers while Clang has partial support. A proper task class, `std::execution::task`, was introduced in C++26. To call it, use `std::execution::sync_wait()`, which returns `std::optional<std::tuple<Ts...>>`.

It is worth noting that `std::promise` and `std::future`, although it would seem that they would be awaitable objects, implement none of the machinery required to be returned from coroutines and be awaited using `co_await`. Programmers must implement a number of public member functions, such as `await_ready`, `await_suspend`, and `await_resume` on the return type in order for the type to be awaited on. Details can be found on cppreference.

```mw
import std;

using std::optional;
using std::tuple;
using std::execution::task;

task<int> add(int a, int b) noexcept {
    co_return a + b;
}

task<int> test() {
    int ret = co_await add(1, 2);
    std::println("Return {}", ret);
    co_return ret;
}

int main(int argc, char* argv[]) {
    optional<tuple<int>> result = std::execution::sync_wait(test());
    std::println("Result: {}", std::get<0>(result).value_or(std::make_tuple(-1)));

    return 0;
}
```

### C

In 2012, C# added the async/await pattern in C# with version 5.0, which Microsoft refers to as the task-based asynchronous pattern (TAP). Async methods usually return either `void`, `Task`, `Task<T>`, `ValueTask` or `ValueTask<T>`. User code can define custom types that async methods can return through custom *async method builders* but this is an advanced and rare scenario. Async methods that return `void` are intended for event handlers; in most cases where a synchronous method would return `void`, returning `Task` instead is recommended, as it allows for more intuitive exception handling (note that `Task<void>` is invalid in C#).

Methods that make use of `await` must be declared with the `async` keyword. In methods that have a return value of type `Task<T>`, methods declared with `async` must have a return statement of type assignable to `T` instead of `Task<T>`; the compiler wraps the value in the `Task<T>` generic. It is also possible to `await` methods that have a return type of `Task` or `Task<T>` that are declared without `async`.

The following async method downloads data from a URL using `await`. Because this method issues a task for each URI before requiring completion with the `await` keyword, the resources can load at the same time instead of waiting for the last resource to finish before starting to load the next.

```mw
namespace Wikipedia.Examples;

using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Threading.Tasks;

public class Example
{
    public async Task<int> SumPageSizesAsync(IEnumerable<Uri> uris) 
    {
        HttpClient client = new();
        int total = 0;
        List<Task<byte[]>> loadUriTasks = new();

        foreach (Uri uri in uris)
        {
            byte[] loadUriTask = client.GetByteArrayAsync(uri);
            loadUriTasks.Add(loadUriTask);
        }

        foreach (Task<byte[]>> loadUriTask in loadUriTasks)
        {
            statusText.Text = $"Found {total} bytes ...";
            byte[] resourceAsBytes = await loadUriTask;
            total += resourceAsBytes.Length;
        }

        statusText.Text = $"Found {total} bytes total";

        return total;
    }

    static async Task Main(string[] args)
    {
        List<Uri> uris = new
        {
            new Uri("https://en.wikipedia.org"),
            new Uri("https://www.microsoft.com"),
            new Uri("https://www.github.com")
        }

        int totalBytes = await SumPageSizesAsync(uris);
        Console.WriteLine($"Total bytes downloaded: {totalbytes}");
    }
}
```

### F

In 2007, F# added asynchronous workflows with version 2.0. The asynchronous workflows are implemented as CE (computation expressions). They can be defined without specifying any special context (like `async` in C#). F# asynchronous workflows append a bang (!) to keywords to start asynchronous tasks.

The following async function downloads data from an URL using an asynchronous workflow:

```mw
let asyncSumPageSizes (uris: #seq<Uri>) : Async<int> = async {
    use httpClient = new HttpClient()
    let! pages = 
        uris
        |> Seq.map(httpClient.GetStringAsync >> Async.AwaitTask)
        |> Async.Parallel
    return pages |> Seq.fold (fun accumulator current -> current.Length + accumulator) 0
}
```

### Java

Java does not have `async` and `await` keywords in the language, however it can be emulated using the `java.util.concurrent` package, such as the class `CompletableFuture` (introduced in Java 8). Asynchronous programming is later improved in Java 21 with the introduction of virtual threads and structured task scopes.

```mw
package org.wikipedia.examples;

import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
import static java.util.concurrent.StructuredTaskScope.ShutdownOnFailure;
import static java.util.concurrent.StructuredTaskScope.Subtask;

public class AsyncExample {
    public String fetchData() {
        // Simulate a time-consuming operation (e.g., network request, database query)
        try {
            Thread.sleep(2000);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        return "Data from remote source";
    }

    public CompletableFuture<String> fetchDataAsync() {
        return CompletableFuture.supplyAsync(() -> fetchData());
    }

    public static void main(String[] args) throws ExecutionException, InterruptedException {
        AsyncExample example = new AsyncExample();

        // Using CompletableFuture (Java 8)
        System.out.println("Starting asynchronous operation...");

        CompletableFuture<String> future = example.fetchDataAsync();

        System.out.println("Doing other work...");

        // Wait for the result (similar to 'await')
        String result = future.get(); 
        System.out.printf("Received result: %s%n", result);

        // Using Virtual Threads (Java 21):
        ExecutorService extor = Executors.newVirtualThreadPerTaskExecutor();
        System.out.println("Starting virtual thread operation...");

        Future<String> fut = extor.submit(() -> {
            return example.fetchData();
        });

        System.out.println("Doing other work...");

        String result = future.get(); 
        System.out.printf("Received result: %s%n", result);
        extor.shutdown();

        // Using StructuredTaskScope (Java 21)
        try (ShutdownOnFailure scope = new ShutdownOnFailure()) {
            Subtask<String> dataTask = scope.fork(example::fetchData);
            
            System.out.println("Doing other work...");

            scope.join(); // wait for all tasks
            scope.throwIfFailed(); // propagate if any exceptions

            String result = future.get(); 
            System.out.printf("Received result: %s%n", result);
        }
    }
}
```

### JavaScript

The await operator in JavaScript (and TypeScript) can only be used from inside an async function or at the top level of a module. If the parameter is a promise, execution of the async function will resume when the promise is resolved (unless the promise is rejected, in which case an error will be thrown that can be handled with normal JavaScript exception handling). If the parameter is not a promise, the parameter itself will be returned immediately.

Many libraries provide promise objects that can also be used with await, as long as they match the specification for native JavaScript promises. However, promises from the jQuery library were not Promises/A+ compatible until jQuery 3.0.

Below is an example (modified from this article):

```mw
interface DBResponse {
    id: string;
    rev?: string;
    ok?: boolean;
}

interface Document {
    _id: string;
    _rev?: string;
    [key: string]: any;
}

interface Database {
    post(doc: object): Promise<DBResponse>;
    get(id: string): Promise<Document>;
}

declare const db: Database;

async function createNewDoc(): Promise<Document> {
    const response: DBResponse = await db.post({});
    const doc: Document = await db.get(response.id);
    return doc;
}

async function main(): Promise<void> {
    try {
        const doc: Document = await createNewDoc();
        console.log(doc);
    } catch (err: Error) {
        console.error("Error creating or fetching document:", err);
    }
}

main();
```

Node.js version 8 includes a utility that enables using the standard library callback-based methods as promises.

### Perl

The Future::AsyncAwait module was the subject of a Perl Foundation grant in September 2018.

### Python

Python 3.5 (2015) has added support for async/await as described in PEP 492 (written and implemented by Yury Selivanov).

```mw
import asyncio

async def main() -> None:
    print("hello")
    await asyncio.sleep(1)
    print("world")

if __name__ == "__main__":
    asyncio.run(main())
```

### Rust

On November 7, 2019, async/await was released on the stable version of Rust. Async functions in Rust desugar to plain functions that return values that implement the Future trait. Currently they are implemented with a finite-state machine.

```mw
// In the crate's Cargo.toml, we need `futures = "0.3.0"` in the dependencies section,
// so we can use the futures crate

extern crate futures; // There is no executor currently in the `std` library.

use std::future::Future;

// This desugars to something like
// `fn async_add_one(num: u32) -> impl Future<Output = u32>`
async fn async_add_one(num: u32) -> u32 {
    num + 1
}

async fn example_task() -> impl Future<Output = ()> {
    let number = async_add_one(5).await;
    println!("5 + 1 = {}", number);
}

fn main() {
    // Creating the Future does not start the execution.
    let future = example_task();

    // The `Future` only executes when we actually poll it, unlike JavaScript.
    futures::executor::block_on(future);
}
```

### Swift

Swift 5.5 (2021) added support for async/await as described in SE-0296.

```mw
func getNumber() async throws -> Int {
    try await Task.sleep(nanoseconds: 1_000_000_000)
    return 42
}

Task {
    let first = try await getNumber()
    let second = try await getNumber()
    print(first + second)
}
```

## Benefits and criticisms

The async/await pattern is especially attractive to language designers of languages that do not have or control their own runtime, as async/await can be implemented solely as a transformation to a state machine in the compiler.

Supporters claim that asynchronous, non-blocking code can be written with async/await that looks almost like traditional synchronous, blocking code. In particular, it has been argued that await is the best way of writing asynchronous code in message-passing programs; in particular, being close to blocking code, readability and the minimal amount of boilerplate code were cited as await benefits.

Critics of async/await note that the pattern tends to cause surrounding code to be asynchronous too; and that its contagious nature splits languages' library ecosystems between synchronous and asynchronous libraries and APIs, an issue often referred to as "function coloring". Alternatives to async/await that do not suffer from this issue are called "colorless". Examples of colorless designs include Go's goroutines and Java's virtual threads.
