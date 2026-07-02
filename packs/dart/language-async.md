---
title: "Asynchronous programming"
source: https://dart.dev/language/async
domain: dart
license: CC-BY-4.0
tags: dart language, dart sdk, dartlang
fetched: 2026-07-02
---

# Asynchronous programming

Information on writing asynchronous code in Dart.

Dart libraries are full of functions that return `Future` or `Stream` objects. These functions are *asynchronous*: they return after setting up a possibly time-consuming operation (such as I/O), without waiting for that operation to complete.

The `async` and `await` keywords support asynchronous programming, letting you write asynchronous code that looks similar to synchronous code.

## Handling Futures

#

When you need the result of a completed Future, you have two options:

- Use `async` and `await`, as described here and in the asynchronous programming tutorial.
- Use the Future API, as described in the `dart:async` documentation.

Code that uses `async` and `await` is asynchronous, but it looks a lot like synchronous code. For example, here's some code that uses `await` to wait for the result of an asynchronous function:

dart

```dart
await lookUpVersion();
```

To use `await`, code must be in an `async` function—a function marked as `async`:

dart

```dart
Future<void> checkVersion() async {
  var version = await lookUpVersion();
  // Do something with version
}
```

Use `try`, `catch`, and `finally` to handle errors and cleanup in code that uses `await`:

dart

```dart
try {
  version = await lookUpVersion();
} catch (e) {
  // React to inability to look up the version
}
```

You can use `await` multiple times in an `async` function. For example, the following code waits three times for the results of functions:

dart

```dart
var entrypoint = await findEntryPoint();
var exitCode = await runExecutable(entrypoint, args);
await flushThenExit(exitCode);
```

In `await *expression*`, the value of `*expression*` is usually a Future; if it isn't, then the value is automatically wrapped in a Future. This Future object indicates a promise to return an object. The value of `await *expression*` is that returned object. The await expression makes execution pause until that object is available.

**If you get a compile-time error when using `await`, make sure `await` is in an `async` function.** For example, to use `await` in your app's `main()` function, the body of `main()` must be marked as `async`:

dart

```dart
void main() async {
  checkVersion();
  print('In main: version is ${await lookUpVersion()}');
}
```

For an interactive introduction to using futures, `async`, and `await`, see the asynchronous programming tutorial.

## Declaring async functions

#

An `async` function is a function whose body is marked with the `async` modifier.

Adding the `async` keyword to a function makes it return a Future. For example, consider this synchronous function, which returns a String:

dart

```dart
String lookUpVersion() => '1.0.0';
```

If you change it to be an `async` function—for example, because a future implementation will be time consuming—the returned value is a Future:

dart

```dart
Future<String> lookUpVersion() async => '1.0.0';
```

Note that the function's body doesn't need to use the Future API. Dart creates the Future object if necessary. If your function doesn't return a useful value, make its return type `Future<void>`.

For an interactive introduction to using futures, `async`, and `await`, see the asynchronous programming tutorial.

## Handling Streams

#

When you need to get values from a Stream, you have two options:

- Use `async` and an *asynchronous for loop* (`await for`).
- Use the Stream API, as described in the `dart:async` documentation.

An asynchronous for loop has the following form:

dart

```dart
await for (varOrType identifier in expression) {
  // Executes each time the stream emits a value.
}
```

The value of `*expression*` must have type Stream. Execution proceeds as follows:

1. Wait until the stream emits a value.
2. Execute the body of the for loop, with the variable set to that emitted value.
3. Repeat 1 and 2 until the stream is closed.

To stop listening to the stream, you can use a `break` or `return` statement, which breaks out of the for loop and unsubscribes from the stream.

**If you get a compile-time error when implementing an asynchronous for loop, make sure the `await for` is in an `async` function.** For example, to use an asynchronous for loop in your app's `main()` function, the body of `main()` must be marked as `async`:

dart

```dart
void main() async {
  // ...
  await for (final request in requestServer) {
    handleRequest(request);
  }
  // ...
}
```

For more information about Dart's asynchronous programming support, check out the `dart:async` library documentation.

Unless stated otherwise, the documentation on this site reflects Dart 3.12.2. Page last updated on 2025-09-15. View source or report an issue.
