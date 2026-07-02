---
title: "Functions"
source: https://dart.dev/language/functions
domain: dart
license: CC-BY-4.0
tags: dart language, dart sdk, dartlang
fetched: 2026-07-02
---

# Functions

Everything about functions in Dart.

Dart is a true object-oriented language, so even functions are objects and have a type, Function. This means that functions can be assigned to variables or passed as arguments to other functions. You can also call an instance of a Dart class as if it were a function. For details, see Callable objects.

Here's an example of implementing a function:

dart

```dart
bool isNoble(int atomicNumber) {
  return _nobleGases[atomicNumber] != null;
}
```

Although Effective Dart recommends type annotations for public APIs, the function still works if you omit the types:

dart

```dart
isNoble(atomicNumber) {
  return _nobleGases[atomicNumber] != null;
}
```

For functions that contain just one expression, you can use a shorthand syntax:

dart

```dart
bool isNoble(int atomicNumber) => _nobleGases[atomicNumber] != null;
```

The `=> *expr*` syntax is a shorthand for `{ return *expr*; }`. The `=>` notation is sometimes referred to as *arrow* syntax.

## Parameters

#

A function can have any number of *required positional* parameters. These can be followed either by *named* parameters or by *optional positional* parameters (but not both).

You can use trailing commas when you pass arguments to a function or when you define function parameters.

### Named parameters

#

Named parameters are optional unless they're explicitly marked as `required`.

When defining a function, use `{*param1*, *param2*, …}` to specify named parameters. If you don't provide a default value or mark a named parameter as `required`, their types must be nullable as their default value will be `null`:

dart

```dart
/// Sets the [bold] and [hidden] flags ...
void enableFlags({bool? bold, bool? hidden}) {
  ...
}
```

When calling a function, you can specify named arguments using `*paramName*: *value*`. For example:

dart

```dart
enableFlags(bold: true, hidden: false);
```

To define a default value for a named parameter besides `null`, use `=` to specify a default value. The specified value must be a compile-time constant. For example:

dart

```dart
/// Sets the [bold] and [hidden] flags ...
void enableFlags({bool bold = false, bool hidden = false}) {
  ...
}

// bold will be true; hidden will be false.
enableFlags(bold: true);
```

If you instead want a named parameter to be mandatory, requiring callers to provide a value for the parameter, annotate them with `required`:

dart

```dart
const Scrollbar({super.key, required Widget child});
```

If someone tries to create a `Scrollbar` without specifying the `child` argument, then the analyzer reports an issue.

You might want to place positional arguments first, but Dart doesn't require it. Dart allows named arguments to be placed anywhere in the argument list when it suits your API:

dart

```dart
repeat(times: 2, () {
  ...
});
```

### Optional positional parameters

#

Wrapping a set of function parameters in `[]` marks them as optional positional parameters. If you don't provide a default value, their types must be nullable as their default value will be `null`:

dart

```dart
String say(String from, String msg, [String? device]) {
  var result = '$from says $msg';
  if (device != null) {
    result = '$result with a $device';
  }
  return result;
}
```

Here's an example of calling this function without the optional parameter:

dart

```dart
assert(say('Bob', 'Howdy') == 'Bob says Howdy');
```

And here's an example of calling this function with the third parameter:

dart

```dart
assert(
  say('Bob', 'Howdy', 'smoke signal') ==
      'Bob says Howdy with a smoke signal',
);
```

To define a default value for an optional positional parameter besides `null`, use `=` to specify a default value. The specified value must be a compile-time constant. For example:

dart

```dart
String say(String from, String msg, [String device = 'carrier pigeon']) {
  var result = '$from says $msg with a $device';
  return result;
}

assert(say('Bob', 'Howdy') == 'Bob says Howdy with a carrier pigeon');
```

### Parameter modifiers

#

In Dart 3.13 and later, you can't use modifiers like `final` or `var` for normal function parameters. These keywords are now reserved exclusively for primary constructors to declare instance fields.

If you wish to enforce immutability for function parameters, use lints like `parameter_assignments` instead of the `final` keyword in the signature.

## The main() function

#

Every app must have a top-level `main()` function, which serves as the entrypoint to the app. The `main()` function returns `void` and has an optional `List<String>` parameter for arguments.

Here's a simple `main()` function:

dart

```dart
void main() {
  print('Hello, World!');
}
```

Here's an example of the `main()` function for a command-line app that takes arguments:

args.dart

dart

```dart
// Run the app like this: dart run args.dart 1 test
void main(List<String> arguments) {
  print(arguments);

  assert(arguments.length == 2);
  assert(int.parse(arguments[0]) == 1);
  assert(arguments[1] == 'test');
}
```

You can use the args library to define and parse command-line arguments.

## Functions as first-class objects

#

You can pass a function as a parameter to another function. For example:

dart

```dart
void printElement(int element) {
  print(element);
}

var list = [1, 2, 3];

// Pass printElement as a parameter.
list.forEach(printElement);
```

You can also assign a function to a variable, such as:

dart

```dart
var loudify = (msg) => '!!! ${msg.toUpperCase()} !!!';
assert(loudify('hello') == '!!! HELLO !!!');
```

This example uses an anonymous function. More about those in the next section.

## Function types

#

You can specify the type of a function, which is known as a *function type*. A function type is obtained from a function declaration header by replacing the function name by the keyword `Function`. Moreover, you are allowed to omit the names of positional parameters, but the names of named parameters can't be omitted. For example:

dart

```dart
void greet(String name, {String greeting = 'Hello'}) =>
    print('$greeting $name!');

// Store `greet` in a variable and call it.
void Function(String, {String greeting}) g = greet;
g('Dash', greeting: 'Howdy');
```

## Anonymous functions

#

Though you name most functions, such as `main()` or `printElement()`, you can also create functions without names. These functions are called *anonymous functions*, *lambdas*, or *closures*.

An anonymous function resembles a named function as it has:

- Zero or more parameters, comma-separated
- Optional type annotations between parentheses.

The following code block contains the function's body:

dart

```dart
([[Type] param1[, ...]]) {
  codeBlock;
}
```

The following example defines an anonymous function with an untyped parameter, `item`. The anonymous function passes it to the `map` function. The `map` function, invoked for each item in the list, converts each string to uppercase. Then, the anonymous function passed to `forEach`, prints each converted string with its length.

dart

```dart
const list = ['apples', 'bananas', 'oranges'];

var uppercaseList = list.map((item) {
  return item.toUpperCase();
}).toList();
// Convert to list after mapping

for (var item in uppercaseList) {
  print('$item: ${item.length}');
}
```

Click **Run** to execute the code.

```
void main() {
  const list = ['apples', 'bananas', 'oranges'];

  var uppercaseList = list.map((item) {
    return item.toUpperCase();
  }).toList();
  // Convert to list after mapping

  for (var item in uppercaseList) {
    print('$item: ${item.length}');
  }
}
```

If the function contains only a single expression or return statement, you can shorten it using arrow notation. Paste the following line into DartPad and click **Run** to verify that it is functionally equivalent.

dart

```dart
var uppercaseList = list.map((item) => item.toUpperCase()).toList();
uppercaseList.forEach((item) => print('$item: ${item.length}'));
```

## Lexical scope

#

Dart determines the scope of variables based on the layout of its code. A programming language with this feature is termed a lexically scoped language. You can "follow the curly braces outwards" to see if a variable is in scope.

**Example:** A series of nested functions with variables at each scope level:

dart

```dart
bool topLevel = true;

void main() {
  var insideMain = true;

  void myFunction() {
    var insideFunction = true;

    void nestedFunction() {
      var insideNestedFunction = true;

      assert(topLevel);
      assert(insideMain);
      assert(insideFunction);
      assert(insideNestedFunction);
    }
  }
}
```

The `nestedFunction()` method can use variables from every level, all the way up to the top level.

## Lexical closures

#

A function object that can access variables in its lexical scope when the function sits outside that scope is called a *closure*.

Functions can close over variables defined in surrounding scopes. In the following example, `makeAdder()` captures the variable `addBy`. Wherever the returned function goes, it remembers `addBy`.

dart

```dart
/// Returns a function that adds [addBy] to the
/// function's argument.
Function makeAdder(int addBy) {
  return (int i) => addBy + i;
}

void main() {
  // Create a function that adds 2.
  var add2 = makeAdder(2);

  // Create a function that adds 4.
  var add4 = makeAdder(4);

  assert(add2(3) == 5);
  assert(add4(3) == 7);
}
```

## Tear-offs

#

When you refer to a function, method, or named constructor without parentheses, Dart creates a *tear-off*. This is a closure that takes the same parameters as the function and invokes the underlying function when you call it. If your code needs a closure that invokes a named function with the same parameters as the closure accepts, don't wrap the call in a lambda. Use a tear-off.

dart

```dart
var charCodes = [68, 97, 114, 116];
var buffer = StringBuffer();
```

good

dart

```dart
// Function tear-off
charCodes.forEach(print);

// Method tear-off
charCodes.forEach(buffer.write);
```

bad

dart

```dart
// Function lambda
charCodes.forEach((code) {
  print(code);
});

// Method lambda
charCodes.forEach((code) {
  buffer.write(code);
});
```

## Testing functions for equality

#

Here's an example of testing top-level functions, static methods, and instance methods for equality:

dart

```dart
void foo() {} // A top-level function

class A {
  static void bar() {} // A static method
  void baz() {} // An instance method
}

void main() {
  Function x;

  // Comparing top-level functions.
  x = foo;
  assert(foo == x);

  // Comparing static methods.
  x = A.bar;
  assert(A.bar == x);

  // Comparing instance methods.
  var v = A(); // Instance #1 of A
  var w = A(); // Instance #2 of A
  var y = w;
  x = w.baz;

  // These closures refer to the same instance (#2),
  // so they're equal.
  assert(y.baz == x);

  // These closures refer to different instances,
  // so they're unequal.
  assert(v.baz != w.baz);
}
```

## Return values

#

All functions return a value. If no return value is specified, the statement `return null;` is implicitly appended to the function body.

dart

```dart
foo() {}

assert(foo() == null);
```

To return multiple values in a function, aggregate the values in a record.

dart

```dart
(String, int) foo() {
  return ('something', 42);
}
```

## Getters and setters

#

Every property access (top-level, static, or instance) is an invocation of a getter or a setter. A variable implicitly creates a getter and, if it's mutable, a setter. This is why when you access a property, you're actually calling a small function in the background. Reading a property calls a getter function, and writing one calls a setter function, even in cases where the property is declared a variable.

However, you can also declare getters and setters explicitly with the `get` and `set` keywords respectively. This allows a property's value to be computed when it's read or written.

The purpose of using getters and setters is to create a clear separation between the client (the code that uses the property) and the provider (the class or library that defines it). The client asks for or sets a value without needing to know if that value is stored in a simple variable or calculated on the spot. This gives the provider the freedom to change how the property works.

For example, because the value of the property might not be stored anywhere, it could be computed each time the getter is called. Another example is that when a value is stored in a private variable, and public access is only allowed by calling a getter or a setter.

The following example showcases this, with the `secret` getter and setter providing indirect access to the private variable `_secret` with its own manipulations on the assigned and retrieved values.

dart

```dart
// Defines a variable `_secret` that is private to the library since
// its identifier starts with an underscore (`_`).
String _secret = 'Hello';

// A public top-level getter that
// provides read access to [_secret].
String get secret {
  print('Getter was used!');
  return _secret.toUpperCase();
}

// A public top-level setter that
// provides write access to [_secret].
set secret(String newMessage) {
  print('Setter was used!');
  if (newMessage.isNotEmpty) {
    _secret = newMessage;
    print('New secret: "$newMessage"');
  }
}

void main() {
  // Reading the value calls the getter.
  print('Current message: $secret');

  /*
  Output:
  Getter was used!
  Current message: HELLO
  */

  // Assigning a value calls the setter.
  secret = 'Dart is fun';

  // Reading it again calls the getter to show the new computed value
  print('New message: $secret');

  /*
  Output:
  Setter was used! New secret: "Dart is fun"
  Getter was used!
  New message: DART IS FUN
  */
}
```

## Generators

#

When you need to lazily produce a sequence of values, consider using a *generator function*. Dart has built-in support for two kinds of generator functions:

- **Synchronous** generator: Returns an `Iterable` object.
- **Asynchronous** generator: Returns a `Stream` object.

To implement a **synchronous** generator function, mark the function body as `sync*`, and use `yield` statements to deliver values:

dart

```dart
Iterable<int> naturalsTo(int n) sync* {
  int k = 0;
  while (k < n) yield k++;
}
```

To implement an **asynchronous** generator function, mark the function body as `async*`, and use `yield` statements to deliver values:

dart

```dart
Stream<int> asynchronousNaturalsTo(int n) async* {
  int k = 0;
  while (k < n) yield k++;
}
```

If your generator is recursive, you can improve its performance by using `yield*`:

dart

```dart
Iterable<int> naturalsDownFrom(int n) sync* {
  if (n > 0) {
    yield n;
    yield* naturalsDownFrom(n - 1);
  }
}
```

## External functions

#

An external function is a function whose body is implemented separately from its declaration. Include the `external` keyword before a function declaration, like so:

dart

```dart
external void someFunc(int i);
```

An external function's implementation can come from another Dart library, or, more commonly, from another language. In interop contexts, `external` introduces type information for foreign functions or values, making them usable in Dart. Implementation and usage is heavily platform specific, so check out the interop docs on, for example, C or JavaScript to learn more.

External functions can be top-level functions, instance methods, getters or setters, or non-redirecting constructors. An instance variable can be `external` too, which is equivalent to an external getter and (if the variable is not `final`) an external setter.

Unless stated otherwise, the documentation on this site reflects Dart 3.12.2. Page last updated on 2026-05-26. View source or report an issue.
