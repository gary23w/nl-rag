---
title: "Function composition (computer science)"
source: https://en.wikipedia.org/wiki/Function_composition_(computer_science)
domain: plug-elixir
license: CC-BY-SA-4.0
tags: plug elixir specification, elixir middleware composition, erlang web adapter, plug connection pipeline
fetched: 2026-07-02
---

# Function composition (computer science)

In computer science, **function composition** is an act or mechanism to combine simple functions to build more complex ones. Like the usual composition of functions in mathematics, the result of each function is passed as the argument of the next, and the result of the last one is the result of the whole.

Programmers frequently apply functions to results of other functions, and almost all programming languages allow it. In some cases, the composition of functions is interesting as a function in its own right, to be used later. Such a function can always be defined but languages with first-class functions make it easier.

The ability to easily compose functions encourages factoring (breaking apart) functions for maintainability and code reuse. More generally, big systems might be built by composing whole programs.

Narrowly speaking, function composition applies to functions that operate on a finite amount of data, each step sequentially processing it before handing it to the next. Functions that operate on potentially infinite data (a stream or other codata) are known as filters, and are instead connected in a pipeline, which is analogous to function composition and can execute concurrently.

## Composing function calls

For example, suppose we have two functions f and g, as in *z* = *f*(*y*) and *y* = *g*(*x*). Composing them means we first compute *y* = *g*(*x*), and then use y to compute *z* = *f*(*y*). Here is the example in the C language:

```mw
float x, y, z;
// ...
y = g(x);
z = f(y);
```

The steps can be combined if we don't give a name to the intermediate result:

```mw
z = f(g(x));
```

Despite differences in length, these two implementations compute the same result. The second implementation requires only one line of code and is colloquially referred to as a "highly composed" form. Readability and hence maintainability is one advantage of highly composed forms, since they require fewer lines of code, minimizing a program's "surface area". DeMarco and Lister empirically verify an inverse relationship between surface area and maintainability. On the other hand, it may be possible to overuse highly composed forms. A nesting of too many functions may have the opposite effect, making the code less maintainable.

In a stack-based language, functional composition is even more natural: it is performed by concatenation, and is usually the primary method of program design. The above example in Forth:

```
g f
```

Which will take whatever was on the stack before, apply g, then f, and leave the result on the stack. See postfix composition notation for the corresponding mathematical notation.

## Naming the composition of functions

Now suppose that the combination of calling f() on the result of g() is frequently useful, and which we want to name foo() to be used as a function in its own right.

In most languages, we can define a new function implemented by composition. Example in C:

```mw
float foo(float x) {
    return f(g(x));
}
```

(the long form with intermediates would work as well.) Example in Forth:

```
  : foo g f ;
```

In languages such as C, the only way to create a new function is to define it in the program source, which means that functions can't be composed at run time. An evaluation of an arbitrary composition of *predefined* functions, however, is possible:

```mw
#include <stdio.h>

typedef int FXN(int);

int f(int x) { return x + 1; }
int g(int x) { return x * 2; }
int h(int x) { return x - 3; }

int eval(FXN *fs[], int size, int x)
{
   for (int i = 0; i < size; i++) x = (*fs[i])(x);

   return x;
}

int main()
{
   // ((6 + 1) * 2) - 3 = 11
   FXN *arr[] = {f, g, h};
   printf("%d\n", eval(arr, 3, 6));

   // ((6 - 3) * 2) + 1 = 7
   arr[2] = f;  arr[0] = h;
   printf("%d\n", eval(arr, 3, 6));
}
```

## First-class composition

In functional programming languages, function composition can be naturally expressed as a higher-order function or operator. In other programming languages you can write your own mechanisms to perform function composition.

### Haskell

In Haskell, the example *foo* = *f*  ∘  *g* given above becomes:

```
foo = f . g
```

using the built-in composition operator (.) which can be read as *f after g* or *g composed with f*.

The composition operator  ∘   itself can be defined in Haskell using a lambda expression:

```mw
(.) :: (b -> c) -> (a -> b) -> a -> c
f . g = \x -> f (g x)
```

The first line describes the type of (.) - it takes a pair of functions, *f*,  *g* and returns a function (the lambda expression on the second line). Note that Haskell doesn't require specification of the exact input and output types of f and g; the a, b, c, and x are placeholders; only the relation between *f*,  *g* matters (f must accept what g returns). This makes (.) a polymorphic operator.

A polymorphic operator with multiple arguments, in Haskell's point-free notation

```mw
f g x y
```

is

```mw
(.).(.)
```

where the parameter names are immaterial, as stated above. Michal Ševčík credits CScalfani with a systematic exposition for function composition using additional parameters.

### Lisp

Variants of Lisp, especially Scheme, the interchangeability of code and data together with the treatment of functions lend themselves extremely well for a recursive definition of a variadic compositional operator.

```mw
(define (compose . fs)
  (if (null? fs) (lambda (x) x) ; if no argument is given, evaluates to the identity function
      (lambda (x) ((car fs) ((apply compose (cdr fs)) x)))))

; examples
(define (add-a-bang str)
  (string-append str "!"))

(define givebang
  (compose string->symbol add-a-bang symbol->string))

(givebang 'set) ; ===> set!

; anonymous composition
((compose sqrt - sqr) 5) ; ===> 0+5i
```

### APL

Many dialects of APL feature built in function composition using the symbol `∘`. This higher-order function extends function composition to dyadic application of the left side function such that `A f∘g B` is `A f g B`.

```mw
foo←f∘g
```

Additionally, you can define function composition:

```mw
o←{⍺⍺ ⍵⍵ ⍵}
```

In dialect that does not support inline definition using braces, the traditional definition is available:

```mw
∇ r←(f o g)x
  r←f g x
∇
```

### Raku

Raku like Haskell has a built in function composition operator, the main difference is it is spelled as `∘` or `o`.

```mw
my &foo = &f ∘ &g;
```

Also like Haskell you could define the operator yourself. In fact the following is the Raku code used to define it in the Rakudo implementation.

```mw
# the implementation has a slightly different line here because it cheats
proto sub infix:<∘> (&?, &?) is equiv(&[~]) is assoc<left> {*}

multi sub infix:<∘> () { *.self } # allows `[∘] @array` to work when `@array` is empty
multi sub infix:<∘> (&f) { &f }   # allows `[∘] @array` to work when `@array` has one element
multi sub infix:<∘> (&f, &g --> Block) {
    (&f).count > 1
    ?? -> |args { f |g |args }
    !! -> |args { f g |args }
}

# alias it to the "Texas" spelling ( everything is bigger, and ASCII in Texas )
my &infix:<o> := &infix:<∘>;
```

### Nim

Nim supports uniform function call syntax, which allows for arbitrary function composition through the method syntax `.` operator.

```mw
func foo(a: int): string = $a
func bar(a: string, count: int): seq[string] =
  for i in 0 ..< count:
    result.add(a)
func baz(a: seq[string]) =
  for i in a:
    echo i

# equivalent!
echo foo(5).bar(6).baz()
echo baz(bar(6, foo(5)))
```

### Python

In Python, a way to define the composition for any group of functions, is using functools.reduce function:

```mw
from functools import reduce
from typing import Callable

def compose(*funcs) -> Callable[[int], int]:
    """Compose a group of functions (f(g(h(...)))) into a single composite func."""
    return reduce(lambda f, g: lambda x: f(g(x)), funcs)

# Example
f = lambda x: x + 1
g = lambda x: x * 2
h = lambda x: x - 3

# Call the function x=10 : ((x - 3) * 2) + 1 = 15
print(compose(f, g, h)(10))
```

### JavaScript

In JavaScript we can define it as a function which takes two functions *f* and *g*, and produces a function:

```mw
function o(f, g) {
    return function(x) {
        return f(g(x));
    }
}

// Alternatively, using the rest operator and lambda expressions in ES2015
const compose = (...fs) => (x) => fs.reduceRight((acc, f) => f(acc), x)
```

### C

In C# we can define it as an Extension method which takes Funcs *f* and *g*, and produces a new Func:

```mw
// Call example:
//   var c = f.ComposeWith(g);
//
//   Func<int, bool> g = _ => ...
//   Func<bool, string> f = _ => ...

public static Func<T1, T3> ComposeWith<T1, T2, T3>(this Func<T2, T3> f, Func<T1, T2> g) => x => f(g(x));
```

### Ruby

Languages like Ruby let you construct a binary operator yourself:

```mw
class Proc
  def compose(other_fn)
    ->(*as) { other_fn.call(call(*as)) }
  end
  alias_method :+, :compose
end

f = ->(x) { x * 2 }
g = ->(x) { x ** 3 }
(f + g).call(12) # => 13824
```

However, a native function composition operator was introduced in Ruby 2.6:

```mw
f = proc{|x| x + 2}
g = proc{|x| x * 3}
(f << g).call(3) # -> 11; identical to f(g(3))
(f >> g).call(3) # -> 15; identical to g(f(3))
```

Notions of composition, including the principle of compositionality and composability, are so ubiquitous that numerous strands of research have separately evolved. The following is a sampling of the kind of research in which the notion of composition is central.

- Steele (1994) directly applied function composition to the assemblage of building blocks known as 'monads' in the Haskell programming language.
- Meyer (1988) addressed the software reuse problem in terms of composability.
- Abadi & Lamport (1993) formally defined a proof rule for functional composition that assures a program's safety and liveness.
- Kracht (2001) identified a strengthened form of compositionality by placing it into a semiotic system and applying it to the problem of structural ambiguity frequently encountered in computational linguistics.
- van Gelder & Port (1993) examined the role of compositionality in analog aspects of natural language processing.
- According to a review by Gibbons (2002), formal treatment of composition underlies validation of component assembly in visual programming languages like IBM's Visual Age for the Java language.

## Large-scale composition

Whole programs or systems can be treated as functions, which can be readily composed if their inputs and outputs are well-defined. Pipelines allowing easy composition of filters were so successful that they became a design pattern of operating systems.

Imperative procedures with side effects violate referential transparency and therefore are not cleanly composable. However if one considers the "state of the world" before and after running the code as its input and output, one gets a clean function. Composition of such functions corresponds to running the procedures one after the other. The monad formalism uses this idea to incorporate side effects and input/output (I/O) into functional languages.
