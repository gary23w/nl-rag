---
title: "Lazy evaluation"
source: https://en.wikipedia.org/wiki/Lazy_evaluation
domain: nix-language
license: CC-BY-SA-4.0
tags: nix language, nix lang, nixos, nixpkgs, nix expression
fetched: 2026-07-02
---

# Lazy evaluation

In programming language theory, **lazy evaluation**, or **call-by-need**, is an evaluation strategy which delays the evaluation of an expression until its value is needed (non-strict evaluation) and which avoids repeated evaluations (by the use of sharing).

The benefits of lazy evaluation include:

- The ability to define control flow (structures) as abstractions instead of primitives.
- The ability to define potentially infinite data structures. This allows for more straightforward implementation of some algorithms.
- The ability to define partly defined data structures where some elements are errors. This allows for rapid prototyping.

Lazy evaluation is often combined with memoization, as described in Jon Bentley's *Writing Efficient Programs*. After a function's value is computed for that parameter or set of parameters, the result is stored in a lookup table that is indexed by the values of those parameters; the next time the function is called, the table is consulted to determine whether the result for that combination of parameter values is already available. If so, the stored result is simply returned. If not, the function is evaluated, and another entry is added to the lookup table for reuse.

Lazy evaluation is difficult to combine with imperative features such as exception handling and input/output, because the order of operations becomes indeterminate.

The opposite of lazy evaluation is eager evaluation, sometimes known as strict evaluation. Eager evaluation is the evaluation strategy employed in most programming languages.

## History

Lazy evaluation was introduced for lambda calculus by Christopher Wadsworth. For programming languages, it was independently introduced by Peter Henderson and James H. Morris and by Daniel P. Friedman and David S. Wise.

## Applications

Delayed evaluation is used particularly in functional programming languages. When using delayed evaluation, an expression is not evaluated as soon as it gets bound to a variable, but when the evaluator is forced to produce the expression's value. That is, a statement such as `x = expression;` (i.e. the assignment of the result of an expression to a variable) clearly calls for the expression to be evaluated and the result is placed in `x`, but what actually is in `x` is irrelevant until there is a need for its value via a reference to `x` in some later expression whose evaluation could itself be deferred, though eventually the rapidly growing tree of dependencies would be pruned to produce some symbol rather than another for the outside world to see.

Lazy evaluation is fundamental in big data frameworks such as Apache Spark, where computations on distributed datasets are delayed until results are explicitly needed, allowing for execution optimizations and reduction of unnecessary processing.

### Control structures

Lazy evaluation allows control structures to be defined normally, and not as primitives or compile-time techniques. For example, one can define if-then-else and short-circuit evaluation operators:

```mw
ifThenElse True b c = b
ifThenElse False b c = c

-- or
True || b = True
False || b = b

-- and
True && b = b
False && b = False
```

These have the usual semantics, i.e., `ifThenElse a b c` evaluates (a), then if and only if (a) evaluates to true does it evaluate (b), otherwise it evaluates (c). That is, exactly one of (b) or (c) will be evaluated. Similarly, for `EasilyComputed || LotsOfWork`, if the easy part gives **True** the lots of work expression could be avoided. Finally, when evaluating `SafeToTry && Expression`, if *SafeToTry* is **false** there will be no attempt at evaluating the *Expression*.

Conversely, in an eager language the above definition for `ifThenElse a b c` would evaluate (a), (b), and (c) regardless of the value of (a). This is not the desired behavior, as (b) or (c) may have side effects, take a long time to compute, or throw errors. It is usually possible to introduce user-defined lazy control structures in eager languages as functions, though they may depart from the language's syntax for eager evaluation: Often the involved code bodies need to be wrapped in a function value, so that they are executed only when called.

### Working with infinite data structures

Delayed evaluation has the advantage of being able to create calculable infinite lists without infinite loops or size matters interfering in computation. The actual values are only computed when needed. For example, one could create a function that creates an infinite list (often called a *stream*) of Fibonacci numbers. The calculation of the *n*-th Fibonacci number would be merely the extraction of that element from the infinite list, forcing the evaluation of only the first n members of the list.

Take for example this trivial program in Haskell:

```mw
numberFromInfiniteList :: Int -> Int
numberFromInfiniteList n =  infinity !! n - 1
    where infinity = [1..]

main = print $ numberFromInfiniteList 4
```

In the function numberFromInfiniteList, the value of infinity is an infinite range, but until an actual value (or more specifically, a specific value at a certain index) is needed, the list is not evaluated, and even then, it is only evaluated as needed (i.e., only to the desired index). Provided the programmer is careful, the program completes normally. However, certain calculations may result in the program attempting to evaluate an infinite number of elements; for example, requesting the length of the list or trying to sum the elements of the list with a fold operation would result in the program either failing to terminate or running out of memory.

As another example, the list of all Fibonacci numbers can be written in the programming language Haskell as:

```mw
 fibs = 0 : 1 : zipWith (+) fibs (tail fibs)
```

In Haskell syntax, "`:`" prepends an element to a list, `tail` returns a list without its first element, and `zipWith` uses a specified function (in this case addition) to combine corresponding elements of two lists to produce a third.

### List-of-successes pattern

### Other uses

In computer windowing systems, the painting of information to the screen is driven by *expose events* which drive the display code at the last possible moment. By doing this, windowing systems avoid computing unnecessary display content updates.

Another example of laziness in modern computer systems is copy-on-write page allocation or demand paging, where memory is allocated only when a value stored in that memory is changed.

Laziness can be useful for high performance scenarios. An example is the Unix mmap function, which provides *demand driven* loading of pages from disk, so that only those pages actually touched are loaded into memory, and unneeded memory is not allocated.

MATLAB implements *copy on edit*, where arrays which are copied have their actual memory storage replicated only when their content is changed, possibly leading to an *out of memory* error when updating an element afterwards instead of during the copy operation.

## Performance

The number of beta reductions to reduce a lambda term with call-by-need is not larger than the number needed by call-by-value or call-by-name reduction. With certain programs the number of steps may be much smaller, for example a specific family of lambda terms using Church numerals take an infinite amount of steps with call-by-value (i.e. never complete), an exponential number of steps with call-by-name, but only a polynomial number with call-by-need. Call-by-need embodies two optimizations - never repeat work (similar to call-by-value), and never perform unnecessary work (similar to call-by-name). Lazy evaluation can also lead to reduction in memory footprint, since values are created when needed.

In practice, lazy evaluation may cause significant performance issues compared to eager evaluation. For example, on modern computer architectures, delaying a computation and performing it later is slower than performing it immediately . This can be alleviated through strictness analysis. Lazy evaluation can also introduce memory leaks due to unevaluated expressions.

## Implementation

Some programming languages delay evaluation of expressions by default, and some others provide functions or special syntax to delay evaluation. In KRC, Miranda, and Haskell, evaluation of function arguments is delayed by default. In many other languages, evaluation can be delayed by explicitly suspending the computation using special syntax (as with Scheme's "`delay`" and "`force`" and OCaml's "`lazy`" and "`Lazy.force`") or, more generally, by wrapping the expression in a thunk. The object representing such an explicitly delayed evaluation is called a *lazy future.* Raku uses lazy evaluation of lists, so one can assign infinite lists to variables and use them as arguments to functions, but unlike Haskell and Miranda, Raku does not use lazy evaluation of arithmetic operators and functions by default.

## Laziness and eagerness

### Controlling eagerness in lazy languages

In lazy programming languages such as Haskell, although the default is to evaluate expressions only when they are demanded, it is possible in some cases to make code more eager—or conversely, to make it more lazy again after it has been made more eager. This can be done by explicitly coding something which forces evaluation (which may make the code more eager) or avoiding such code (which may make the code more lazy). *Strict* evaluation usually implies eagerness, but they are technically different concepts.

However, there is an optimisation implemented in some compilers called strictness analysis, which, in some cases, allows the compiler to infer that a value will always be used. In such cases, this may render the programmer's choice of whether to force that particular value or not, irrelevant, because strictness analysis will force strict evaluation.

In Haskell, marking constructor fields strict means that their values will always be demanded immediately. The `seq` function can also be used to demand a value immediately and then pass it on, which is useful if a constructor field should generally be lazy. However, neither of these techniques implements *recursive* strictness—for that, a function called `deepSeq` was invented.

Also, pattern matching in Haskell 98 is strict by default, so the `~` qualifier has to be used to make it lazy.

### Simulating laziness in eager languages

#### C++

In C++, the `std::ranges` library uses lazy range adaptors.

```mw
import std;

using std::vector;
using std::ranges::to;
using std::views::filter;
using std::views::iota;
using std::views::transform;

vector<int> v = iota(1, 1'000'000) // lazily generate ints from 1 to 1,000,000
    | filter([](int x) -> bool { return x % 2 == 0; }) // filter out odd numbers, keeping evens
    | transform([](int x) -> int { return x * x; }) // square each value
    | to<vector>(); // convert the range back to a vector<int>
```

#### Java

In Java, lazy evaluation can be done by using objects that have a method to evaluate them when the value is needed. The body of this method must contain the code required to perform this evaluation. Since the introduction of lambda expressions in Java SE8, Java has supported a compact notation for this. The following example generic interface provides a framework for lazy evaluation:

```mw
interface Lazy<T> {
    T eval();
}
```

The `Lazy` interface with its `eval()` method is equivalent to the `Supplier` interface with its `get()` method in the `java.util.function` library.

Each class that implements the `Lazy` interface must provide an `eval` method, and instances of the class may carry whatever values the method needs to accomplish lazy evaluation. For example, consider the following code to lazily compute and print 210:

```mw
Lazy<Integer> a = () -> 1;
for (int i = 0; i < 10; i++) {
    Lazy<Integer> b = a;
    a = () -> b.eval() + b.eval();
}
System.out.println("a = " + a.eval());
```

In the above, the variable a initially refers to a lazy integer object created by the lambda expression `() -> 1`. Evaluating this lambda expression is similar to constructing a new instance of an anonymous class that implements `Lazy<Integer>` with an eval method returning 1.

Each iteration of the loop links a to a new object created by evaluating the lambda expression inside the loop. Each of these objects holds a reference to another lazy object, b, and has an eval method that calls `b.eval()` twice and returns the sum. The variable b is needed here to meet Java's requirement that variables referenced from within a lambda expression be effectively final.

This is an inefficient program because this implementation of lazy integers does not memoize the result of previous calls to eval. It also involves considerable autoboxing and unboxing. What may not be obvious is that, at the end of the loop, the program has constructed a linked list of 11 objects and that all of the actual additions involved in computing the result are done in response to the call to `a.eval()` on the final line of code. This call recursively traverses the list to perform the necessary additions.

We can build a Java class that memoizes a lazy object as follows:

```mw
class Memo<T> implements Lazy<T> {
    private Lazy<T> lazy;  // a lazy expression, eval sets it to null
    private T memo; // the memorandum of the previous value

    public Memo(Lazy<T> lazy) {
        this.lazy = lazy;
    }

    public T eval() {
        if (lazy != null) {
            memo = lazy.eval();
            lazy = null;
        }
        return memo;
    }
}
```

This allows the previous example to be rewritten to be far more efficient. Where the original ran in time exponential in the number of iterations, the memoized version runs in linear time:

```mw
Lazy<Integer> a = () -> 1;
for (int i = 0; i < 10; i++) {
    Lazy<Integer> b = a;
    a = new Memo<Integer>(() -> b.eval() + b.eval());
}
System.out.printf("a = %s%n", a.eval());
```

Java's lambda expressions are just syntactic sugar. Anything that can be written with a lambda expression can be rewritten as a call to construct an instance of an anonymous inner class implementing the interface, and any use of an anonymous inner class can be rewritten using a named inner class, and any named inner class can be moved to the outermost nesting level.

#### JavaScript

In JavaScript, lazy evaluation can be simulated by using a generator. For example, the stream of all Fibonacci numbers can be written, using memoization, in the following TypeScript code:

```mw
/**
 * Generator functions return generator objects, which reify lazy evaluation.
 * @return {!Generator<bigint>} A non-null generator of integers.
 */
function* fibonacciNumbers(): Generator<bigint, never, unknown> {
    let memo: [bigint, bigint] = [1n, -1n]; // create the initial state (e.g. a vector of "negafibonacci" numbers)
    while (true) { // repeat indefinitely
        memo = [memo[0] + memo[1], memo[0]]; // update the state on each evaluation
        yield memo[0]; // yield the next value and suspend execution until resumed
    }
}

const stream: Generator<bigint, never, unknown> = fibonacciNumbers(); // create a lazy evaluated stream of numbers
const first10: bigint[] = Array.from(new Array(10), () => stream.next().value); // evaluate only the first 10 numbers
console.log(first10); // the output is [0n, 1n, 1n, 2n, 3n, 5n, 8n, 13n, 21n, 34n]
```

#### Kotlin

In Kotlin variables can be initialized lazily using the `lazy{}` function to initialize Delegated properties with the `by` clause like so:

```mw
var flipped = true

val pizzaReady : Boolean by lazy {
    println("I'll check if the pizza is ready right now.")
    // if this runs more than once then it will output false.
    flipped = !flipped
    !flipped
}

fun main() {
    println("Is my pizza ready?")
    assert(pizzaReady) // does not crash
    println("is it still ready though?")
    assert(pizzaReady) // still doesn't crash
}
```

You can run this example yourself by going to the Kotlin Playground.

##### Verification

To verify that the program lazily loaded `isThePizzaReady` instead of initializing it beforehand as true we need to check the output of the program.

```mw
Is my pizza ready?
I'll check if the pizza is ready right now.
is it still ready though?
```

As we can see when the program reads from `isThePizzaReady` it prints out a statement we put inside the lazy code block on line 4. We can also verify that it did not run the lazy block twice and reused the previous output of it via the fact that:

1. The program did not throw an exception, the assert function will throw an `AssertError`if the output of `isThePizzaReady` is false. which can only happen if the lazy block is executed more than once.
2. The statement on line 4 does not execute more than once.

#### Python

In Python 2.x the `range()` function computes a list of integers. The entire list is stored in memory when the first assignment statement is evaluated, so this is an example of eager or immediate evaluation:

```mw
r = range(10)
print r
# prints [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print r[3]
# prints 3
```

In Python 3.x the `range()` function returns a generator which computes elements of the list on demand. Elements are only generated when they are needed (e.g., when `print(r[3])` is evaluated in the following example), so this is an example of lazy or deferred evaluation:

```mw
r: Iterator[int] = range(10)
print(r)
# prints range(0, 10)
print(r[3])
# prints 3
```

This change to lazy evaluation saves execution time for large ranges which may never be fully referenced and memory usage for large ranges where only one or a few elements are needed at any time.

In Python 2.x is possible to use a function called `xrange()` which returns an object that generates the numbers in the range on demand. The advantage of `xrange` is that generated object will always take the same amount of memory.

```mw
r = xrange(10)
print r
# prints xrange(10)
lst = [x for x in r]
print lst
# prints [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

From version 2.2 forward, Python manifests lazy evaluation by implementing iterators (lazy sequences) unlike tuple or list sequences. For instance (Python 2):

```mw
numbers: Iterator[int] = range(10)
iterator: Iterator[int] = iter(numbers)
print(numbers)
# prints [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(iterator)
# prints <listiterator object at 0xf7e8dd4c>
print(iterator.next())
# prints 0
```

The above example shows that lists are evaluated when called, but in case of

iterator

, the first element '0' is printed when need arises.

#### .NET

In the .NET framework, it is possible to do lazy evaluation using the class `System.Lazy<T>`. The class can be easily exploited in F# using the `lazy` keyword, while the `force` method will force the evaluation. There are also specialized collections like `Microsoft.FSharp.Collections.Seq` that provide built-in support for lazy evaluation.

```mw
let fibonacci = Seq.unfold (fun (x, y) -> Some(x, (y, x + y))) (0I,1I)
fibonacci |> Seq.nth 1000
```

In C# and VB.NET, the class `System.Lazy<T>` is directly used.

```mw
using System;

public int Sum()
{
    int a = 0;
    int b = 0; 
    Lazy<int> x = new(() => a + b);
    a = 3;
    b = 5;
    return x.Value; // returns 8
}
```

Or with a more practical example:

```mw
using System;

// recursive calculation of the n'th fibonacci number
public int Fib(int n)
{
   return (n == 1) ? 1 : (n == 2) ? 1 : Fib(n - 1) + Fib(n - 2);
}

public void Main()
{
    Console.WriteLine("Which Fibonacci number do you want to calculate?");
    int n = Int32.Parse(Console.ReadLine()); 
    Lazy<int> fib = new(() => Fib(n)); // function is prepared, but not executed
    bool execute; 
    if (n > 100)
    {
        Console.WriteLine("This can take some time. Do you really want to calculate this large number? [y/n]");
        execute = (Console.ReadLine() == "y"); 
    }
    else 
    {
        execute = true;
    }

    if (execute) 
    {
        Console.WriteLine(fib.Value); // number is only calculated if needed
    }
}
```

Another way is to use the `yield` keyword:

```mw
using System.Collections.Generic;

// eager evaluation 
public IEnumerable<int> Fibonacci(int x)
{
    IList<int> fibs = new List<int>();

    int prev = -1;
    int next = 1;
    for (int i = 0; i < x; i++)
    {
        int sum = prev + next;
        prev = next;
        next = sum;
        fibs.Add(sum); 
    }
    return fibs;
}

// lazy evaluation 
public IEnumerable<int> LazyFibonacci(int x)
{
    int prev = -1;
    int next = 1;
    for (int i = 0; i < x; i++)
    {
        int sum = prev + next;
        prev = next;
        next = sum;
        yield return sum;
    }
}
```
