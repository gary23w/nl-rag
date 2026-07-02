---
title: "Generator (computer programming)"
source: https://en.wikipedia.org/wiki/Generator_(computer_programming)
domain: algebraic-effects
license: CC-BY-SA-4.0
tags: algebraic effect, effect handler, delimited continuation, one-shot continuation
fetched: 2026-07-02
---

# Generator (computer programming)

In computer science, a **generator** is a routine that can be used to control the iteration behaviour of a loop. All generators are also iterators. A generator is very similar to a function that returns an array, in that a generator has parameters, can be called, and generates a sequence of values. However, instead of building an array containing all the values and returning them all at once, a generator *yields* the values one at a time, which requires less memory and allows the caller to get started processing the first few values immediately. In short, a generator *looks like* a function but *behaves like* an iterator.

Generators can be implemented in terms of more expressive control flow constructs, such as coroutines or first-class continuations. Generators, also known as semicoroutines, are a special case of (and weaker than) coroutines, in that they always yield control back to the caller (when passing a value back), rather than specifying a coroutine to jump to; see comparison of coroutines with generators.

## Uses

Generators are usually invoked inside loops. The first time that a generator invocation is reached in a loop, an iterator object is created that encapsulates the state of the generator routine at its beginning, with arguments bound to the corresponding parameters. The generator's body is then executed in the context of that iterator until a special *yield* action is encountered; at that time, the value provided with the *yield* action is used as the value of the invocation expression. The next time the same generator invocation is reached in a subsequent iteration, the execution of the generator's body is resumed after the *yield* action, until yet another *yield* action is encountered. In addition to the *yield* action, execution of the generator body can also be terminated by a *finish* action, at which time the innermost loop enclosing the generator invocation is terminated. In more complicated situations, a generator may be used manually outside of a loop to create an iterator, which can then be used in various ways.

Because generators compute their yielded values only on demand, they are useful for representing streams, such as sequences that would be expensive or impossible to compute at once. These include e.g. infinite sequences and live data streams.

When eager evaluation is desirable (primarily when the sequence is finite, as otherwise evaluation will never terminate), one can either convert to a list, or use a parallel construction that creates a list instead of a generator. For example, in Python a generator `g` can be evaluated to a list `l` via `l = list(g)`, while in F# the sequence expression `seq { ... }` evaluates lazily (a generator or sequence) but `[ ... ]` evaluates eagerly (a list).

In the presence of generators, loop constructs of a language – such as for and while – can be reduced into a single loop ... end loop construct; all the usual loop constructs can then be comfortably simulated by using suitable generators in the right way. For example, a ranged loop like `for x = 1 to 10` can be implemented as iteration through a generator, as in Python's `for x in range(1, 10)`. Further, `break` can be implemented as sending *finish* to the generator and then using `continue` in the loop.

## Languages providing generators

Generators first appeared in CLU (1975), were a prominent feature in the string manipulation language Icon (1977) and are now available in Python (2001), C#, Ruby, PHP, ECMAScript (as of ES6/ES2015), and other languages. In CLU and C#, generators are called *iterators*, and in Ruby, *enumerators*.

### Lisp

The final Common Lisp standard does not natively provide generators, yet various library implementations exist, such as SERIES documented in CLtL2 or pygen.

### CLU

A yield statement is used to implement iterators over user-defined data abstractions.

```mw
string_chars = iter (s: string) yields (char);
  index: int := 1;
  limit: int := string$size (s);
  while index <= limit do
    yield (string$fetch(s, index));
    index := index + 1;
    end;
end string_chars;

for c: char in string_chars(s) do
   ...
end;
```

### Icon

Every expression (including loops) is a generator. The language has many generators built-in and even implements some of the logic semantics using the generator mechanism (logical disjunction or "OR" is done this way).

Printing squares from 0 to 20 can be achieved using a co-routine by writing:

```mw
   local squares, j
   squares := create (seq(0) ^ 2)
   every j := |@squares do
      if j <= 20 then
         write(j)
      else
         break
```

However, most of the time custom generators are implemented with the "suspend" keyword which functions exactly like the "yield" keyword in CLU.

### C

C does not have generator functions as a language construct, but, as they are a subset of coroutines, it is simple to implement them using any framework that implements stackful coroutines, such as libdill. On POSIX platforms, when the cost of context switching per iteration is not a concern, or full parallelism rather than merely concurrency is desired, a very simple generator function framework can be implemented using pthreads and pipes.

### C++

C++11 allows foreach loops to be applied to any class that provides the `begin` and `end` functions. It is then possible to write generator-like classes by defining both the iterable methods (`begin` and `end`) and the iterator methods (`operator!=`, `operator++` and `operator*`) in the same class. For example, it is possible to write the following program with a basic range implementation:

```mw
import std;

class Range {
private:
    int last;
public:
    explicit Range(int end):
        last{end} {}

    class Iterator {
    private:
        int iter;
    public:
        explicit Iterator(int start):
            iter{start} {}

        [[nodiscard]]
        int operator*() const noexcept {
            return iter;
        }

        [[nodiscard]]
        Iterator& operator++() noexcept {
            ++iter;
            return *this;
        }

        [[nodiscard]]
        bool operator!=(const Iterator& other) const noexcept {
            return iter != other.iter;
        }
    };

    [[nodiscard]]
    Iterator begin() const noexcept {
        return Iterator(0); // Start iteration from 0
    }

    [[nodiscard]]
    Iterator end() const noexcept {
        return Iterator(last); // End iteration at 'last'
    }
};

int main() {
    for (int i: Range(10)) {
        std::println("{}", i);
    }
    return 0;
}
```

Furthermore, C++20 formally introduced support for coroutines, which can be used to implement generators. C++23 introduced `std::generator` in the standard library, making it much easier to implement generators. For example, a basic range generator can be implemented as:

```mw
import std;

using std::generator;

generator<int> range(int n) noexcept {
    for (int i = 0; i < n; ++i) {
        co_yield i;
    }
}
```

It can be iterated using foreach loops:

```mw
import std;

using std::generator;

generator<int> range(int n) noexcept {
    for (int i = 0; i < n; ++i) {
        co_yield i;
    }
}

int main() {
    for (int i: range(10)) {
        std::println("{}", i);
    }
    return 0;
}
```

### C

An example C# 2.0 generator (the `yield` is available since C# version 2.0): Both of these examples utilize generics, but this is not required. yield keyword also helps in implementing custom stateful iterations over a collection as discussed in this discussion.

```mw
using System.Collections.Generics;

// Method that takes an iterable input (possibly an array)
// and returns all even numbers.
public static IEnumerable<int> GetEven(IEnumerable<int> numbers)
{
    foreach (int number in numbers)
    {
        if ((number % 2) == 0)
        {
            yield return number;
        }
    }
}
```

It is possible to use multiple `yield return` statements and they are applied in sequence on each iteration:

```mw
using System.Collections.Generics;

public class CityCollection : IEnumerable<string>
{
    public IEnumerator<string> GetEnumerator()
    {
        yield return "New York";
        yield return "Paris";
        yield return "London";
    }
}
```

### Perl

Perl does not natively provide generators, but support is provided by the Coro::Generator module which uses the Coro co-routine framework. Example usage:

```mw
use strict;
use warnings;
# Enable generator { BLOCK } and yield
use Coro::Generator;
# Array reference to iterate over
my $chars = ['A'...'Z'];

# New generator which can be called like a coderef.
my $letters = generator {
    my $i = 0;
    for my $letter (@$chars) {
        # get next letter from $chars
        yield $letter;
    }
};

# Call the generator 15 times.
print $letters->(), "\n" for (0..15);
```

### Raku

Example parallel to Icon uses Raku (formerly/aka Perl 6) Range class as one of several ways to achieve generators with the language.

Printing squares from 0 to 20 can be achieved by writing:

```mw
for (0 .. *).map(* ** 2) -> $i {
    last if $i > 20;
    say $i
}
```

However, most of the time custom generators are implemented with "gather" and "take" keywords in a lazy context.

### Tcl

In Tcl 8.6, the generator mechanism is founded on named coroutines.

```mw
proc generator {body} {
    coroutine gen[incr ::disambiguator] apply {{script} {
        # Produce the result of [generator], the name of the generator
        yield [info coroutine]
        # Do the generation
        eval $script
        # Finish the loop of the caller using a 'break' exception
        return -code break
    }} $body
}

# Use a simple 'for' loop to do the actual generation
set count [generator {
    for {set i 10} {$i <= 20} {incr i} {
        yield $i
    }
}]

# Pull values from the generator until it is exhausted
while 1 {
    puts [$count]
}
```

### Haskell

In Haskell, with its lazy evaluation model, every datum created with a non-strict data constructor is generated on demand. For example,

```mw
countFrom :: Integer -> [Integer]
countFrom n = n : countFrom (n + 1)

from10to20 :: [Integer]
from10to20 = takeWhile (<= 20) $ countFrom 10

primes :: [Integer]
primes = 2 : 3 : nextPrime 5
  where
    nextPrime n
        | notDivisible n = n : nextPrime (n + 2)
        | otherwise = nextPrime (n + 2)
    notDivisible n =
        all ((/= 0) . (rem n)) $ takeWhile ((<= n) . (^ 2)) $ tail primes
```

where `(:)` is a non-strict list constructor, *cons*, and `$` is just a *"called-with"* operator, used for parenthesization. This uses the standard adaptor function,

```mw
takeWhile p [] = []
takeWhile p (x:xs) | p x = x : takeWhile p xs
                   | otherwise = []
```

which walks down the list and stops on the first element that doesn't satisfy the predicate. If the list has been walked before until that point, it is just a strict data structure, but if any part hadn't been walked through before, it will be generated on demand. List comprehensions can be freely used:

```mw
squaresUnder20 = takeWhile (<= 20) [x * x | x <- countFrom 10]
squaresForNumbersUnder20 = [x * x | x <- takeWhile (<= 20) $ countFrom 10]
```

### Racket

Racket provides several related facilities for generators. First, its for-loop forms work with *sequences*, which are a kind of a producer:

```mw
(for ([i (in-range 10 20)])
  (printf "i = ~s\n" i))
```

and these sequences are also first-class values:

```mw
(define 10-to-20 (in-range 10 20))
(for ([i 10-to-20])
  (printf "i = ~s\n" i))
```

Some sequences are implemented imperatively (with private state variables) and some are implemented as (possibly infinite) lazy lists. Also, new struct definitions can have a property that specifies how they can be used as sequences.

But more directly, Racket comes with a generator library for a more traditional generator specification. For example,

```mw
#lang racket
(require racket/generator)
(define (ints-from from)
  (generator ()
    (for ([i (in-naturals from)]) ; infinite sequence of integers from 0
      (yield i))))
(define g (ints-from 10))
(list (g) (g) (g)) ; -> '(10 11 12)
```

Note that the Racket core implements powerful continuation features, providing general (re-entrant) continuations that are composable, and also delimited continuations. Using this, the generator library is implemented in Racket.

### PHP

The community of PHP implemented generators in PHP 5.5. Details can be found in the original Request for Comments: Generators.

Infinite Fibonacci sequence:

```mw
function fibonacci(): Generator
{
    $last = 0;
    $current = 1;
    yield 1;
    while (true) {
        $current = $last + $current;
        $last = $current - $last;
        yield $current;
    }
}

foreach (fibonacci() as $number) {
    echo $number, "\n";
}
```

Fibonacci sequence with limit:

```mw
function fibonacci(int $limit): Generator 
{
    yield $a = $b = $i = 1;
 
    while (++$i < $limit) {
        yield $a = ($b = $a + $b) - $a;
    }
}

foreach (fibonacci(10) as $number) {
    echo "$number\n";
}
```

Any function which contains a yield statement is automatically a generator function.

### Ruby

Ruby supports generators (starting from version 1.9) in the form of the built-in Enumerator class.

```mw
# Generator from an Enumerator object
chars = Enumerator.new(['A', 'B', 'C', 'Z'])

4.times { puts chars.next }

# Generator from a block
count = Enumerator.new do |yielder|
  i = 0
  loop { yielder.yield i += 1 }
end

100.times { puts count.next }
```

### Java

Java has had a standard interface for implementing iterators since its early days, and since Java 5, the "foreach" construction makes it easy to loop over objects that provide the `java.lang.Iterable` interface. (The Java collections framework and other collections frameworks, typically provide iterators for all collections.)

```mw
import java.util.stream.Stream;

record Pair(int a, int b) {};

Iterable<Integer> myIterable = Stream.iterate(new Pair(1, 1), p -> new Pair(p.b, p.a + p.b))
    .limit(10)
    .map(p -> p.a)::iterator;

myIterable.forEach(System.out::println);
```

Or get a `java.util.Iterator` from the Java 8 super-interface `java.util.stream.BaseStream` of `java.util.stream.Stream` interface.

```mw
import java.util.Iterator;
import java.util.stream.Stream;

record Pair(int a, int b) {};

// Save the iterator of a stream that generates fib sequence
// Stream::iterate generates the Fibonacci sequence
Iterator<Integer> myGenerator = Stream.iterate(new Pair(1, 1), p -> new Pair(p.b, p.a + p.b))
    .map(p -> p.a).iterator();

// Print the first 5 elements
for (int i = 0; i < 5; i++) {
    System.out.println(myGenerator.next());
}

System.out.println("done with first iteration");

// Print the next 5 elements
for (int i = 0; i < 5; i++) {
    System.out.println(myGenerator.next());
}
```

Output:

```mw
1
1
2
3
5
done with first iteration
8
13
21
34
55
```

### XL

In XL, iterators are the basis of 'for' loops:

```mw
import IO = XL.UI.CONSOLE

iterator IntegerIterator (var out Counter : integer; Low, High : integer) written Counter in Low..High is
    Counter := Low
    while Counter <= High loop
        yield
        Counter += 1

// Note that I needs not be declared, because declared 'var out' in the iterator
// An implicit declaration of I as an integer is therefore made here
for I in 1..5 loop
    IO.WriteLn "I=", I
```

### F

F# provides generators via *sequence expressions,* since version 1.9.1. These can define a sequence (lazily evaluated, sequential access) via `seq { ... }`, a list (eagerly evaluated, sequential access) via `[ ... ]` or an array (eagerly evaluated, indexed access) via `[| ... |]` that contain code that generates values. For example,

```mw
seq { for b in 0 .. 25 do
          if b < 15 then
              yield b * b }
```

forms a sequence of squares of numbers from 0 to 14 by filtering out numbers from the range of numbers from 0 to 25.

### Python

Generators were added to Python in version 2.2 in 2001. An example generator:

```mw
import itertools
from typing import Iterator

def countfrom(n: int) -> Iterator[int]:
    while True:
        yield n
        n += 1

# Example use: printing out the integers from 10 to 20.
# Note that this iteration terminates normally, despite
# countfrom() being written as an infinite loop.

for i in countfrom(10):
    if i <= 20:
        print(i)
    else:
        break

# Another generator, which produces prime numbers indefinitely as needed.

def primes() -> Iterator[int]:
    """Generate prime numbers indefinitely as needed."""
    yield 2
    n: int = 3
    p: list[int] = [2]
    while True:
        # If dividing n by all the numbers in p, up to and including sqrt(n),
        # produces a non-zero remainder then n is prime.
        if all(n % f > 0 for f in itertools.takewhile(lambda f: f * f <= n, p)):
            yield n
            p.append(n)
        n += 2
```

In Python, a generator can be thought of as an iterator that contains a frozen stack frame. Whenever `next()` is called on the iterator, Python resumes the frozen frame, which executes normally until the next `yield` statement is reached. The generator's frame is then frozen again, and the yielded value is returned to the caller.

PEP 380 (implemented in Python 3.3) adds the `yield from` expression, allowing a generator to delegate part of its operations to another generator or iterable.

#### Generator expressions

Python has a syntax modeled on that of list comprehensions, called a generator expression that aids in the creation of generators. The following extends the first example above by using a generator expression to compute squares from the `itertools.count()` generator function:

```mw
from typing import Generator

squares: Generator[int, None, None] = (n * n for n in itertools.count(2))

for j in squares:
    if j <= 20:
        print(j)
    else:
        break
```

### ECMAScript

ECMAScript 6 (a.k.a. Harmony) introduced generator functions.

An infinite Fibonacci sequence can be written using a function generator:

```mw
function* fibonacci(limit) {
    let [prev, curr] = [0, 1];
    while (!limit || curr <= limit) {
        yield curr;
        [prev, curr] = [curr, prev + curr];
    }
}

// bounded by upper limit 10
for (const n of fibonacci(10)) {
    console.log(n);
}

// generator without an upper bound limit
for (const n of fibonacci()) {
    console.log(n);
    if (n > 10000) break;
}

// manually iterating
let fibGen = fibonacci();
console.log(fibGen.next().value); // 1
console.log(fibGen.next().value); // 1
console.log(fibGen.next().value); // 2
console.log(fibGen.next().value); // 3
console.log(fibGen.next().value); // 5
console.log(fibGen.next().value); // 8

// picks up from where you stopped
for (const n of fibGen) {
    console.log(n);
    if (n > 10000) break;
}
```

### R

The iterators package can be used for this purpose.

```mw
library(iterators)

# Example ------------------
abc <- iter(c('a','b','c'))
nextElem(abc)
```

### Smalltalk

Example in Pharo Smalltalk:

The Golden ratio generator below returns to each invocation 'goldenRatio next' a better approximation to the Golden Ratio.

```mw
goldenRatio := Generator on: [ :g | | x y z r | 
	x := 0.
	y := 1.
	[  
		z := x + y.
		r := (z / y) asFloat.
		x := y.
		y := z.
		g yield: r
	] repeat	
].

goldenRatio next.
```

The expression below returns the next 10 approximations.

```mw
Character cr join: ((1 to: 10) collect: [ :dummy | ratio next ]).
```

See more in A hidden gem in Pharo: Generator.
