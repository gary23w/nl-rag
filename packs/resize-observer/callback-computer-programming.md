---
title: "Callback (computer programming)"
source: https://en.wikipedia.org/wiki/Callback_(computer_programming)
domain: resize-observer
license: CC-BY-SA-4.0
tags: resize observer api, element size change callback, content box resize, observe box dimensions
fetched: 2026-07-02
---

# Callback (computer programming)

In computer programming, a **callback** is a programming pattern in which a function reference is passed from one context (consumer) to another (provider) such that the provider can call the function. If the function accesses state or functionality of the consumer, then the call is *back* to the consumer – backwards compared to the normal flow of control in which a consumer calls a provider.

A function that accepts a callback parameter may be designed to call back before returning to its caller. But, more typically, a callback reference is stored by the provider so that it can call the function later (as *deferred*). If the provider invokes the callback on the same thread as the consumer, then the call is *blocking*, a.k.a. *synchronous*. If instead, the provider invokes the callback on a different thread, then the call is *non-blocking*, a.k.a. *asynchronous*.

A callback can be likened to leaving instructions with a tailor for what to do when a suit is ready, such as calling a specific phone number or delivering it to a given address. These instructions represent a callback: a function provided in advance to be executed later, often by a different part of the system and not necessarily by the one that received it.

The difference between a general function reference and a callback can be subtle, and some use the terms interchangeably but distinction generally depends on programming intent. If the intent is like the telephone callback – that the original called party communicates back to the original caller – then it's a callback.

## Use

A blocking callback runs in the execution context of the function that passes the callback. A deferred callback can run in a different context such as during interrupt or from a thread. As such, a deferred callback can be used for synchronization and delegating work to another thread.

### Event handling

A callback can be used for event handling. Often, consuming code registers a callback for a particular type of event. When that event occurs, the callback is called. Callbacks are often used to program the graphical user interface (GUI) of a program that runs in a windowing system. The application supplies a reference to a custom callback function for the windowing system to call. The windowing system calls this function to notify the application of events like mouse clicks and key presses.

### Asynchronous action

A callback can be used to implement asynchronous processing.

A caller requests an action and provides a callback to be called when the action completes which might be long after the request is made.

### Polymorphism

A callback can be used to implement polymorphism. In the following pseudocode, `say_hi` can take either `write_status` or `write_error`.

```mw
from typing import Callable

def write_status(message: str) -> None:
    write(stdout, message)

def write_error(message: str) -> None:
    write(stderr, message)

def say_hi(write: Callable[[str], None]) -> None:
    write("Hello world")
```

## Implementation

The callback technology is implemented differently by programming language.

In assembly, C, C++, Pascal, Modula-2 and other languages, a callback function is stored internally as a function pointer. Using the same storage allows different languages to directly share callbacks without a design-time or runtime interoperability layer. For example, the Windows API is accessible via multiple languages, compilers and assemblers. C++ also allows objects to provide an implementation of the function call operation. The Standard Template Library accepts these objects (called *functors*) as parameters. Many dynamic languages, such as JavaScript, Lua, Python, Perl and PHP, allow a function object to be passed. CLI languages such as C# and Visual Basic (.NET) (VB.NET) provide a type-safe encapsulating function reference known as delegate. Events and event handlers, as used in .NET languages, provide for callbacks. Functional programming languages generally support first-class functions, which can be passed as callbacks to other functions, stored as data or returned from functions.

Many languages, including Perl, Python, Ruby, Smalltalk, C++ (11+), C# and VB.NET (new versions) and most functional languages, support lambda expressions, unnamed functions with inline syntax, that generally act as callbacks. In some languages, including Scheme, ML, JavaScript, Perl, Python, Smalltalk, PHP (since 5.3.0), C++ (11+), Java (since 8), and many others, a lambda can be a closure, i.e., can access variables locally defined in the context in which the lambda is defined. In an object-oriented programming language such as Java versions before function-valued arguments, the behavior of a callback can be achieved by passing an object that implements an interface. The methods of this object are callbacks. In PL/I and ALGOL 60, a callback procedure may need to be able to access local variables in containing blocks, so it is called through an *entry variable* containing both the entry point and context information.

## Example code

### C

Callbacks have a wide variety of uses, for example in error signaling: a Unix program might not want to terminate immediately when it receives SIGTERM, so to make sure that its termination is handled properly, it would register the cleanup function as a callback.

```mw
#include <signal.h>
#include <stdlib.h>

#include <fcntl.h>
#include <sys/types>

struct Data {
    // ...
};

static struct Data data = {
    // initialize contents here
};
static volatile sigatomic_t flag = 0;

void cleanupHandler(int signum) {
    flag = 1;
    int saveFile = open("savefile.dat", O_WRONLY | O_CREATO, S_IWUSR); 
    write(saveFile, data, sizeof data);
    close(saveFile);
}

int main(void) {
    signal(cleanupHandler, SIGTERM);
    doStuff(); 
}
```

Another common use for callbacks in C is with C standard library functions used for sorting (`qsort()`) and searching (`lsearch()`, `bsearch()`) where a comparator function is passed as an argument to the routine to determine the collation order.

```mw
#include <stdlib.h>

struct Person {
    char name[20];
    int age;
};

Person people[1000];

// Collates people by age
int compareAges(struct Person* p1, struct Person* p2) {
    return p2->age - p1->age;
}

int main(void) {
    // ...
    int numberOfPeople = /* some number here */;

    qsort(numberOfPeople, sizeof (struct Person), people, compareAges);
    // ...
}
```

Callbacks may also be used to control whether a function acts or not: Xlib allows custom predicates to be specified to determine whether a program wishes to handle an event. In the following C code, function `printNumber()` uses parameter `getNumber` as a blocking callback. `printNumber()` is called with `getAnswerToMostImportantQuestion()` which acts as a callback function. When run the output is: "Value: 42".

```mw
#include <stdio.h>
#include <stdlib.h>

void printNumber(int (*getNumber)(void)) {
    int val = getNumber();
    printf("Value: %d\n", val);
}

int getAnswerToMostImportantQuestion(void) {
    return 42;
}

int main(void) {
    printNumber(getAnswerToMostImportantQuestion);
    return 0;
}
```

### C++

In C++, functors can be used in addition to function pointer. A functor is an object with `operator()` defined. For example, the objects in `std::views` are functors. This is an example of using functors in C++:

```mw
import std;

class MyCallback {
public:
    void operator()(int x) {
        std::println("Callback called with value: {}", x);
    }
};

template <typename Callback>
void performOperation(int a, Callback callback) {
    std::println("Performing operation on: {}", a);
    callback(a);
}

int main() {
    MyCallback callback;
    int value = 10;
    performOperation(value, callback);
    
    return 0;
}
```

`std::function<R(Args...)>` is a type-erased wrapper for any callable objects, introduced in C++11:

```mw
import std;

using std::function;

void performOperation(int a, function<void(int)> callback) {
    std::println("Performing operation on: {}", a);
    callback(a);
}

int main() {
    int value = 10;
    performOperation(value, [](int x) -> void {
        std::println("Callback called with value: {}", x);
    });

    return 0;
}
```

### C

In the following C# code, method `Helper.PerformAction` uses parameter `callback` as a blocking callback. `Helper.PerformAction` is called with `Log` which acts as a callback function. When run, the following is written to the console: "Callback was: Hello world".

```mw
namespace Wikipedia.Examples;

using System;

class Helper
{
    public void PerformAction(Action<string> callback)
    {
        callback("Hello world");
    }
}

public class Main
{
    static void Log(string str)
    {
        Console.WriteLine($"Callback was: {str}");
    }

    static void Main(string[] args)
    {
        Helper helper = new();
        helper.PerformAction(Log);
    }
}
```

### JavaScript

In the following JavaScript code, function `calculate` uses parameter `operate` as a blocking callback. `calculate` is called with `multiply` and then with `sum` which act as callback functions.

```mw
function calculate(a, b, operate) {
    return operate(a, b);
}
function multiply(a, b) {
    return a * b;
}
function sum(a, b) {
    return a + b;
}
// outputs 20
alert(calculate(10, 2, multiply));
// outputs 12
alert(calculate(10, 2, sum));
```

The collection method `.each()` of the jQuery library uses the function passed to it as a blocking callback. It calls the callback for each item of the collection. For example:

```mw
$("li").each(function(index) {
  console.log(index + ": " + $(this).text());
});
```

Deferred callbacks are commonly used for handling events from the user, the client and timers. Examples can be found in `addEventListener`, Ajax and `XMLHttpRequest`.

In addition to using callbacks in JavaScript source code, C functions that take a function are supported via js-ctypes.

### Julia

In the following Julia code, function `calculate` accepts a parameter `operate` that is used as a blocking callback. `calculate` is called with `square` which acts as a callback function.

```mw
julia> square(val) = val^2
square (generic function with 1 method)
julia> calculate(operate, val) = operate(val)
calculate (generic function with 1 method)
julia> calculate(square, 5)
25
```

### Kotlin

In the following Kotlin code, function `askAndAnswer` uses parameter `getAnswer` as a blocking callback. `askAndAnswer` is called with `getAnswerToMostImportantQuestion` which acts as a callback function. Running this will tell the user that the answer to their question is "42".

```mw
fun main() {
    print("Enter the most important question: ")
    val question = readLine()
    askAndAnswer(question, ::getAnswerToMostImportantQuestion)
}

fun getAnswerToMostImportantQuestion(): Int {
    return 42
}

fun askAndAnswer(question: String?, getAnswer: () -> Int) {
    println("Question: $question")
    println("Answer: ${getAnswer()}")
}
```

### Lua

In this Lua code, function `calculate` accepts the `operation` parameter which is used as a blocking callback. `calculate` is called with both `add` and `multiply`, and then uses an anonymous function to divide.

```mw
function calculate(a, b, operation)
    return operation(a, b)
end

function multiply(a, b)
    return a * b
end

function add(a, b)
    return a + b
end

print(calculate(10, 20, multiply)) -- outputs 200
print(calculate(10, 20, add)) -- outputs 30
-- an example of a callback using an anonymous function
print(calculate(10, 20, function(a, b)
    return a / b -- outputs 0.5
end))
```

### Python

In the following Python code, function `calculate` accepts a parameter `operate` that is used as a blocking callback. `calculate` is called with `square` which acts as a callback function.

```mw
def square(val: int) -> int:
    return val ** 2

def calculate(operate: Callable[[int], int], val: int) -> int:
    return operate(val)

# prints: 25
print(calculate(square, 5))
```

### Rebol and Red

The following Rebol and Red code demonstrates callback use.

- As alert requires a string, form produces a string from the result of calculate
- The get-word! values (i.e., :calc-product and :calc-sum) trigger the interpreter to return the code of the function rather than evaluate with the function.
- The datatype! references in a block! [float! integer!] restrict the type of values passed as arguments.

```mw
Red [Title: "Callback example"]

calculate: func [
    num1 [number!] 
    num2 [number!] 
    callback-function [function!]
][
    callback-function num1 num2
]

calc-product: func [
    num1 [number!] 
    num2 [number!]
][
    num1 * num2
]

calc-sum: func [
    num1 [number!] 
    num2 [number!]
][
    num1 + num2
]

; alerts 75, the product of 5 and 15
alert form calculate 5 15 :calc-product

; alerts 20, the sum of 5 and 15
alert form calculate 5 15 :calc-sum
```

### Rust

Rust have the `Fn`, `FnMut` and `FnOnce` traits.

```mw
fn call_with_one<F>(func: F) -> usize
    where F: Fn(usize) -> usize {
    func(1)
}

let double = |x| x * 2;
assert_eq!(call_with_one(double), 2);
```
