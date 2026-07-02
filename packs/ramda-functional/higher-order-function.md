---
title: "Higher-order function"
source: https://en.wikipedia.org/wiki/Higher-order_function
domain: ramda-functional
license: CC-BY-SA-4.0
tags: ramda functional, point-free style, javascript currying, immutable pipeline
fetched: 2026-07-02
---

# Higher-order function

In mathematics and computer science, a **higher-order function** (**HOF**) is a function that does at least one of the following:

- takes one or more functions as arguments (i.e. a procedural parameter, which is a parameter of a procedure that is itself a procedure),
- returns a function as its result.

All other functions are *first-order functions*. In mathematics higher-order functions are also termed *operators* or *functionals*. The differential operator in calculus is a common example, since it maps a function to its derivative, also a function. Higher-order functions should not be confused with other uses of the word "functor" throughout mathematics, see Functor (disambiguation).

In the untyped lambda calculus, all functions are higher-order; in a typed lambda calculus, from which most functional programming languages are derived, higher-order functions that take one function as argument are values with types of the form $(\tau _{1}\to \tau _{2})\to \tau _{3}$ .

## General examples

- map function, found in many functional programming languages, is one example of a higher-order function. It takes arguments as a function *f* and a collection of elements, and as the result, returns a new collection with *f* applied to each element from the collection.
- sort, which take a comparison function as a parameter, allowing the programmer to separate the sorting algorithm from the comparisons of the items being sorted. The C standard function `qsort` is an example of this.
- filter function, that takes a collection and a function that returns true or false, and returns a new collection that is the elements of the parameter collection where the function returned true.
- fold (including foldl and foldr)
- scan
- apply
- Function composition
- Integration
- Callback
- Tree traversal
- Montague grammar, a semantic theory of natural language, uses higher-order functions

## Support in programming languages

### Direct support

*The examples are not intended to compare and contrast programming languages, but to serve as examples of higher-order function syntax*

In the following examples, the higher-order function `twice` takes a function, and applies the function to some value twice. If `twice` has to be applied several times for the same `f` it preferably should return a function rather than a value. This is in line with the "don't repeat yourself" principle.

#### APL

```mw
      twice←{⍺⍺ ⍺⍺ ⍵}

      plusthree←{⍵+3}

      g←{plusthree twice ⍵}
    
      g 7
13
```

Or in a tacit manner:

```mw
      twice←⍣2

      plusthree←+∘3

      g←plusthree twice
    
      g 7
13
```

#### C++

Using `std::function` in C++11:

```mw
import std;

auto twice = [](const std::function<int(int)>& f) -> auto {
    return [f](int x) -> int {
        return f(f(x));
    };
};

auto plusThree = [](int i) -> int {
    return i + 3;
};

int main() {
    auto g = twice(plusThree);

    std::println("{}", g(7)); // 13
}
```

Or, with generic lambdas provided by C++14:

```mw
import std;

auto twice = [](const auto& f) -> auto {
    return [f](int x) -> int {
        return f(f(x));
    };
};

auto plusThree = [](int i) -> int {
    return i + 3;
};

int main() {
    auto g = twice(plusThree);

    std::println("{}", g(7)); // 13
}
```

#### C

Using just delegates:

```mw
using System;

public class Program
{
    public static void Main(string[] args)
    {
        Func<Func<int, int>, Func<int, int>> twice = f => x => f(f(x));

        Func<int, int> plusThree = i => i + 3;

        var g = twice(plusThree);

        Console.WriteLine(g(7)); // 13
    }
}
```

Or equivalently, with static methods:

```mw
using System;

public class Program
{
    private static Func<int, int> Twice(Func<int, int> f)
    {
        return x => f(f(x));
    }

    private static int PlusThree(int i) => i + 3;

    public static void Main(string[] args)
    {
        var g = Twice(PlusThree);

        Console.WriteLine(g(7)); // 13
    }
}
```

#### Clojure

```mw
(defn twice [f]
  (fn [x] (f (f x))))

(defn plus-three [i]
  (+ i 3))

(def g (twice plus-three))

(println (g 7)) ; 13
```

#### ColdFusion Markup Language (CFML)

```mw
twice = function(f) {
    return function(x) {
        return f(f(x));
    };
};

plusThree = function(i) {
    return i + 3;
};

g = twice(plusThree);

writeOutput(g(7)); // 13
```

#### Common Lisp

```mw
(defun twice (f)                                                                
  (lambda (x) (funcall f (funcall f x))))                                       
                                                                                
(defun plus-three (i)                                                           
  (+ i 3))                                                                      
                                                                                
(defvar g (twice #'plus-three))                                                 
                                                                                
(print (funcall g 7))
```

#### D

```mw
import std.stdio : writeln;

alias twice = (f) => (int x) => f(f(x));

alias plusThree = (int i) => i + 3;

void main()
{
    auto g = twice(plusThree);

    writeln(g(7)); // 13
}
```

#### Dart

```mw
int Function(int) twice(int Function(int) f) {
    return (x) {
        return f(f(x));
    };
}

int plusThree(int i) {
    return i + 3;
}

void main() {
    final g = twice(plusThree);
    
    print(g(7)); // 13
}
```

#### Elixir

In Elixir, you can mix module definitions and anonymous functions

```mw
defmodule Hof do
    def twice(f) do
        fn(x) -> f.(f.(x)) end
    end
end

plus_three = fn(i) -> i + 3 end

g = Hof.twice(plus_three)

IO.puts g.(7) # 13
```

Alternatively, we can also compose using pure anonymous functions.

```mw
twice = fn(f) ->
    fn(x) -> f.(f.(x)) end
end

plus_three = fn(i) -> i + 3 end

g = twice.(plus_three)

IO.puts g.(7) # 13
```

#### Erlang

```mw
or_else([], _) -> false;
or_else([F | Fs], X) -> or_else(Fs, X, F(X)).

or_else(Fs, X, false) -> or_else(Fs, X);
or_else(Fs, _, {false, Y}) -> or_else(Fs, Y);
or_else(_, _, R) -> R.

or_else([fun erlang:is_integer/1, fun erlang:is_atom/1, fun erlang:is_list/1], 3.23).
```

In this Erlang example, the higher-order function `or_else/2` takes a list of functions (`Fs`) and argument (`X`). It evaluates the function `F` with the argument `X` as argument. If the function `F` returns false then the next function in `Fs` will be evaluated. If the function `F` returns `{false, Y}` then the next function in `Fs` with argument `Y` will be evaluated. If the function `F` returns `R` the higher-order function `or_else/2` will return `R`. Note that `X`, `Y`, and `R` can be functions. The example returns `false`.

#### F

```mw
let twice f = f >> f

let plus_three = (+) 3

let g = twice plus_three

g 7 |> printf "%A" // 13
```

#### Go

```mw
package main

import "fmt"

func twice(f func(int) int) func(int) int {
	return func(x int) int {
		return f(f(x))
	}
}

func main() {
	plusThree := func(i int) int {
		return i + 3
	}

	g := twice(plusThree)

	fmt.Println(g(7)) // 13
}
```

Notice a function literal can be defined either with an identifier (`twice`) or anonymously (assigned to variable `plusThree`).

#### Groovy

```mw
def twice = { f, x -> f(f(x)) }
def plusThree = { it + 3 }
def g = twice.curry(plusThree) 
println g(7) // 13
```

#### Haskell

```mw
twice :: (Int -> Int) -> (Int -> Int)
twice f = f . f

plusThree :: Int -> Int
plusThree = (+3)

main :: IO ()
main = print (g 7) -- 13
  where
    g = twice plusThree
```

#### J

Explicitly,

```mw
   twice=.     adverb : 'u u y'

   plusthree=. verb   : 'y + 3'
   
   g=. plusthree twice
   
   g 7
13
```

or tacitly,

```mw
   twice=. ^:2

   plusthree=. +&3
   
   g=. plusthree twice
   
   g 7
13
```

#### Java (1.8+)

Using just functional interfaces:

```mw
import java.util.function.*;

class Main {
    public static void main(String[] args) {
        Function<IntUnaryOperator, IntUnaryOperator> twice = f -> f.andThen(f);

        IntUnaryOperator plusThree = i -> i + 3;

        var g = twice.apply(plusThree);

        System.out.println(g.applyAsInt(7)); // 13
    }
}
```

Or equivalently, with static methods:

```mw
import java.util.function.*;

class Main {
    private static IntUnaryOperator twice(IntUnaryOperator f) {
        return f.andThen(f);
    }

    private static int plusThree(int i) {
        return i + 3;
    }

    public static void main(String[] args) {
        var g = twice(Main::plusThree);

        System.out.println(g.applyAsInt(7)); // 13
    }
}
```

#### JavaScript

With arrow functions:

```mw
"use strict";

const twice = f => x => f(f(x));

const plusThree = i => i + 3;

const g = twice(plusThree);

console.log(g(7)); // 13
```

Or with classical syntax:

```mw
"use strict";

function twice(f) {
  return function (x) {
    return f(f(x));
  };
}

function plusThree(i) {
  return i + 3;
}

const g = twice(plusThree);

console.log(g(7)); // 13
```

#### Julia

```mw
julia> function twice(f)
           function result(x)
               return f(f(x))
           end
           return result
       end
twice (generic function with 1 method)

julia> plusthree(i) = i + 3
plusthree (generic function with 1 method)

julia> g = twice(plusthree)
(::var"#result#3"{typeof(plusthree)}) (generic function with 1 method)

julia> g(7)
13
```

#### Kotlin

```mw
fun twice(f: (Int) -> Int): (Int) -> Int {
    return { f(f(it)) }
}

fun plusThree(i: Int) = i + 3

fun main() {
    val g = twice(::plusThree)

    println(g(7)) // 13
}
```

#### Lua

```mw
function twice(f)
  return function (x)
    return f(f(x))
  end
end

function plusThree(i)
  return i + 3
end

local g = twice(plusThree)

print(g(7)) -- 13
```

#### MATLAB

```mw
function result = twice(f)
result = @(x) f(f(x));
end

plusthree = @(i) i + 3;

g = twice(plusthree)

disp(g(7)); % 13
```

#### OCaml

```mw
let twice f x =
  f (f x)

let plus_three =
  (+) 3

let () =
  let g = twice plus_three in

  print_int (g 7); (* 13 *)
  print_newline ()
```

#### PHP

```mw
<?php

declare(strict_types=1);

function twice(callable $f): Closure {
    return function (int $x) use ($f): int {
        return $f($f($x));
    };
}

function plusThree(int $i): int {
    return $i + 3;
}

$g = twice('plusThree');

echo $g(7), "\n"; // 13
```

or with all functions in variables:

```mw
<?php

declare(strict_types=1);

$twice = fn(callable $f): Closure => fn(int $x): int => $f($f($x));

$plusThree = fn(int $i): int => $i + 3;

$g = $twice($plusThree);

echo $g(7), "\n"; // 13
```

Note that arrow functions implicitly capture any variables that come from the parent scope, whereas anonymous functions require the `use` keyword to do the same.

#### Perl

```mw
use strict;
use warnings;

sub twice {
    my ($f) = @_;
    sub {
        $f->($f->(@_));
    };
}

sub plusThree {
    my ($i) = @_;
    $i + 3;
}

my $g = twice(\&plusThree);

print $g->(7), "\n"; # 13
```

or with all functions in variables:

```mw
use strict;
use warnings;

my $twice = sub {
    my ($f) = @_;
    sub {
        $f->($f->(@_));
    };
};

my $plusThree = sub {
    my ($i) = @_;
    $i + 3;
};

my $g = $twice->($plusThree);

print $g->(7), "\n"; # 13
```

#### Python

```mw
def twice(f: Callable[Any]) -> Any:
    def result(x: Any) -> Any:
        return f(f(x))
    return result

plus_three: Callable[int] = lambda i: i + 3

g: int = twice(plus_three)
    
print(g(7))
# prints 13
```

Python decorator syntax is often used to replace a function with the result of passing that function through a higher-order function. E.g., the function `g` could be implemented equivalently:

```mw
@twice
def g(i: int) -> int:
    return i + 3

print(g(7))
# prints 13
```

#### R

```mw
twice <- \(f) \(x) f(f(x))

plusThree <- function(i) i + 3

g <- twice(plusThree)

> g(7)
[1] 13
```

#### Raku

```mw
sub twice(Callable:D $f) {
    return sub { $f($f($^x)) };
}

sub plusThree(Int:D $i) {
    return $i + 3;
}

my $g = twice(&plusThree);

say $g(7); # 13
```

In Raku, all code objects are closures and therefore can reference inner "lexical" variables from an outer scope because the lexical variable is "closed" inside of the function. Raku also supports "pointy block" syntax for lambda expressions which can be assigned to a variable or invoked anonymously.

#### Ruby

```mw
def twice(f)
  ->(x) { f.call(f.call(x)) }
end

plus_three = ->(i) { i + 3 }

g = twice(plus_three)

puts g.call(7) # 13
```

#### Rust

```mw
fn twice(f: impl Fn(i32) -> i32) -> impl Fn(i32) -> i32 {
    move |x| f(f(x))
}

fn plus_three(i: i32) -> i32 {
    i + 3
}

fn main() {
    let g = twice(plus_three);

    println!("{}", g(7)) // 13
}
```

#### Scala

```mw
object Main {
  def twice(f: Int => Int): Int => Int =
    f compose f

  def plusThree(i: Int): Int =
    i + 3

  def main(args: Array[String]): Unit = {
    val g = twice(plusThree)

    print(g(7)) // 13
  }
}
```

#### Scheme

```mw
(define (compose f g) 
  (lambda (x) (f (g x))))

(define (twice f) 
  (compose f f))

(define (plus-three i)
  (+ i 3))

(define g (twice plus-three))

(display (g 7)) ; 13
(display "\n")
```

#### Swift

```mw
func twice(_ f: @escaping (Int) -> Int) -> (Int) -> Int {
    return { f(f($0)) }
}

let plusThree = { $0 + 3 }

let g = twice(plusThree)

print(g(7)) // 13
```

#### Tcl

```mw
set twice {{f x} {apply $f [apply $f $x]}}
set plusThree {{i} {return [expr $i + 3]}}

# result: 13
puts [apply $twice $plusThree 7]
```

Tcl uses apply command to apply an anonymous function (since 8.6).

#### XACML

The XACML standard defines higher-order functions in the standard to apply a function to multiple values of attribute bags.

```mw
rule allowEntry{
    permit
    condition anyOfAny(function[stringEqual], citizenships, allowedCitizenships)
}
```

The list of higher-order functions in XACML can be found here.

#### XQuery

```mw
declare function local:twice($f, $x) {
  $f($f($x))
};

declare function local:plusthree($i) {
  $i + 3
};

local:twice(local:plusthree#1, 7) (: 13 :)
```

### Alternatives

#### Function pointers

Function pointers in languages such as C, C++, Fortran, and Pascal allow programmers to pass around references to functions. The following C code computes an approximation of the integral of an arbitrary function:

```mw
#include <stdio.h>

double square(double x)
{
    return x * x;
}

double cube(double x)
{
    return x * x * x;
}

/* Compute the integral of f() within the interval [a,b] */
double integral(double f(double x), double a, double b, int n)
{
    int i;
    double sum = 0;
    double dt = (b - a) / n;
    for (i = 0;  i < n;  ++i) {
        sum += f(a + (i + 0.5) * dt);
    }
    return sum * dt;
}

int main()
{
    printf("%g\n", integral(square, 0, 1, 100));
    printf("%g\n", integral(cube, 0, 1, 100));
    return 0;
}
```

The qsort function from the C standard library uses a function pointer to emulate the behavior of a higher-order function.

#### Macros

Macros can also be used to achieve some of the effects of higher-order functions. However, macros cannot easily avoid the problem of variable capture; they may also result in large amounts of duplicated code, which can be more difficult for a compiler to optimize. Macros are generally not strongly typed, although they may produce strongly typed code.

#### Dynamic code evaluation

In other imperative programming languages, it is possible to achieve some of the same algorithmic results as are obtained via higher-order functions by dynamically executing code (sometimes called *Eval* or *Execute* operations) in the scope of evaluation. There can be significant drawbacks to this approach:

- The argument code to be executed is usually not statically typed; these languages generally rely on dynamic typing to determine the well-formedness and safety of the code to be executed.
- The argument is usually provided as a string, the value of which may not be known until run-time. This string must either be compiled during program execution (using just-in-time compilation) or evaluated by interpretation, causing some added overhead at run-time, and usually generating less efficient code.

#### Objects

In object-oriented programming languages that do not support higher-order functions, objects can be an effective substitute. An object's methods act in essence like functions, and a method may accept objects as parameters and produce objects as return values. Objects often carry added run-time overhead compared to pure functions, however, and added boilerplate code for defining and instantiating an object and its method(s). Languages that permit stack-based (versus heap-based) objects or structs can provide more flexibility with this method.

An example of using a simple stack based record in Free Pascal with a function that returns a function:

```mw
program example;

type 
  int = integer;
  Txy = record x, y: int; end;
  Tf = function (xy: Txy): int;
     
function f(xy: Txy): int; 
begin 
  Result := xy.y + xy.x; 
end;

function g(func: Tf): Tf; 
begin 
  result := func; 
end;

var 
  a: Tf;
  xy: Txy = (x: 3; y: 7);

begin  
  a := g(@f);     // return a function to "a"
  writeln(a(xy)); // prints 10
end.
```

The function `a()` takes a `Txy` record as input and returns the integer value of the sum of the record's `x` and `y` fields (3 + 7).

#### Defunctionalization

Defunctionalization can be used to implement higher-order functions in languages that lack first-class functions:

```mw
// Defunctionalized function data structures
template<typename T> struct Add { T value; };
template<typename T> struct DivBy { T value; };
template<typename F, typename G> struct Composition { F f; G g; };

// Defunctionalized function application implementations
template<typename F, typename G, typename X>
auto apply(Composition<F, G> f, X arg) {
    return apply(f.f, apply(f.g, arg));
}

template<typename T, typename X>
auto apply(Add<T> f, X arg) {
    return arg  + f.value;
}

template<typename T, typename X>
auto apply(DivBy<T> f, X arg) {
    return arg / f.value;
}

// Higher-order compose function
template<typename F, typename G>
Composition<F, G> compose(F f, G g) {
    return Composition<F, G> {f, g};
}

int main(int argc, const char* argv[]) {
    auto f = compose(DivBy<float>{ 2.0f }, Add<int>{ 5 });
    apply(f, 3); // 4.0f
    apply(f, 9); // 7.0f
    return 0;
}
```

In this case, different types are used to trigger different functions via function overloading. The overloaded function in this example has the signature `auto apply`.
