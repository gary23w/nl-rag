---
title: "Scala (programming language) (part 1/2)"
source: https://en.wikipedia.org/wiki/Scala_(programming_language)
domain: gatling
license: CC-BY-SA-4.0
tags: gatling scala, load testing, performance testing, simulation scripts
fetched: 2026-07-02
part: 1/2
---

# Scala (programming language)

**Scala** (/ˈskɑːlɑː/ *SKAH-lah*) is a strongly statically typed high-level general-purpose programming language that supports both object-oriented programming and functional programming. Designed to be concise, many of Scala's design decisions are intended to address criticism of Java.

Scala source code can be compiled to JVM bytecode and run on a Java virtual machine (JVM). Scala can also be transpiled to JavaScript to run in a browser, or compiled directly to a native executable using Clang. When running on the JVM, Scala provides language interoperability with Java so that libraries written in either language may be referenced directly in Scala or Java code. Like Java, Scala is object-oriented, and uses a syntax termed *curly-brace* which is similar to the language C. Since Scala 3, there is also an option to use the off-side rule (indenting) to structure blocks, and its use is advised. Martin Odersky has said that this turned out to be the most productive change introduced in Scala 3.

Unlike Java, Scala has many features of functional programming languages (like Scheme, Standard ML, and Haskell), including currying, immutability, lazy evaluation, and pattern matching. It also has an advanced type system supporting algebraic data types, covariance and contravariance, higher-order types (but not higher-rank types), anonymous types, operator overloading, optional parameters, named parameters, raw strings, and an experimental exception-only version of algebraic effects that can be seen as a more powerful version of Java's checked exceptions.

The name Scala is a portmanteau of *scalable* and *language*, signifying that it is designed to grow with the demands of its users.


## History

The design of Scala started in 2001 at the École Polytechnique Fédérale de Lausanne (EPFL) (in Lausanne, Switzerland) by Martin Odersky. It followed on from work on Funnel, a programming language combining ideas from functional programming and Petri nets. Odersky formerly worked on Generic Java, and javac, Sun's Java compiler.

After an internal release in late 2003, Scala was released publicly in early 2004 on the Java platform, A second version (v2.0) followed in March 2006.

On 17 January 2011, the Scala team won a five-year research grant of over €2.3 million from the European Research Council. On 12 May 2011, Odersky and collaborators launched Typesafe Inc. (later renamed Lightbend Inc.), a company to provide commercial support, training, and services for Scala. Typesafe received a $3 million investment in 2011 from Greylock Partners.


## Platforms and license

Scala runs on the Java platform (Java virtual machine) and is compatible with existing Java programs. As Android applications are typically written in Java and translated from JVM bytecode into Dalvik bytecode (which may be further translated to native machine code during installation) when packaged, Scala's Java compatibility makes it well-suited to Android development, the more so where functional programming is preferred.

The reference Scala software distribution, including compiler and libraries, is released under the Apache license.

### Other compilers and targets

*Scala.js* is a Scala compiler that compiles to JavaScript, making it possible to write Scala programs that can run in web browsers or Node.js. The compiler, in development since 2013, was announced as no longer experimental in 2015 (v0.6). Version v1.0.0-M1 was released in June 2018 and version 1.1.1 in September 2020.

Scala Native is a Scala compiler that targets the LLVM compiler infrastructure to create executable code that uses a lightweight managed runtime, which uses the Boehm garbage collector. The project is led by Denys Shabalin and had its first release, 0.1, on 14 March 2017. Development of Scala Native began in 2015 with a goal of being faster than just-in-time compilation for the JVM by eliminating the initial runtime compilation of code and also providing the ability to call native routines directly.

A reference Scala compiler targeting the .NET Framework and its Common Language Runtime was released in June 2004, but was officially dropped in 2012.


## Examples

### "Hello World" example

The Hello World program written in Scala 3 has this form:

```mw
@main def main() = println("Hello, World!")
```

Unlike the stand-alone Hello World application for Java, there is no class declaration and nothing is declared to be static.

When the program is stored in file *HelloWorld.scala*, the user compiles it with the command:

```
$ scalac HelloWorld.scala
```

and runs it with

```
$ scala HelloWorld
```

This is analogous to the process for compiling and running Java code. Indeed, Scala's compiling and executing model is identical to that of Java, making it compatible with Java build tools such as Apache Ant.

A shorter version of the "Hello World" Scala program is:

```mw
println("Hello, World!")
```

Scala includes an interactive shell and scripting support. Saved in a file named `HelloWorld2.scala`, this can be run as a script using the command:

```
$ scala HelloWorld2.scala
```

Commands can also be entered directly into the Scala interpreter, using the option **-e**:

```
$ scala -e 'println("Hello, World!")'
```

Expressions can be entered interactively in the REPL:

```mw
$ scala
Welcome to Scala 2.12.2 (Java HotSpot(TM) 64-Bit Server VM, Java 1.8.0_131).
Type in expressions for evaluation. Or try :help.

scala> List(1, 2, 3).map(x => x * x)
res0: List[Int] = List(1, 4, 9)

scala>
```

### Basic example

The following example shows the differences between Java and Scala syntax. The function mathFunction takes an integer, squares it, and then adds the cube root of that number to the natural log of that number, returning the result (i.e., $n^{2/3}+\ln(n^{2})$ ):

| // Java: int mathFunction(int num) { int numSquare = num*num; return (int) (Math.cbrt(numSquare) + Math.log(numSquare)); } |   |
|---|---|
| // Scala: Direct conversion from Java // no import needed; scala.math // already imported as `math` def mathFunction(num: Int): Int = var numSquare: Int = num*num return (math.cbrt(numSquare) + math.log(numSquare)). asInstanceOf[Int] | // Scala: More idiomatic // Uses type inference, omits `return` statement, // uses `toInt` method, declares numSquare immutable import math.* def mathFunction(num: Int) = val numSquare = num*num (cbrt(numSquare) + log(numSquare)).toInt |

Some syntactic differences in this code are:

- Scala does not require semicolons (;) to end statements.
- Value types are capitalized (sentence case): `Int, Double, Boolean` instead of `int, double, boolean`.
- Parameter and return types follow, as in Pascal, rather than precede as in C.
- Methods must be preceded by `def`.
- Local or class variables must be preceded by `val` (indicates an immutable variable) or `var` (indicates a mutable variable).
- The `return` operator is unnecessary in a function (although allowed); the value of the last executed statement or expression is normally the function's value.
- Instead of the Java cast operator `(Type) foo`, Scala uses `foo.asInstanceOf[Type]`, or a specialized function such as `toDouble` or `toInt`.
- Function or method `foo()` can also be called as just `foo`; method `thread.send(signo)` can also be called as just `thread send signo`; and method `foo.toString()` can also be called as just `foo toString`.

These syntactic relaxations are designed to allow support for domain-specific languages.

Some other basic syntactic differences:

- Array references are written like function calls, e.g. `array(i)` rather than `array[i]`. (Internally in Scala, the former expands into array.apply(i) which returns the reference)
- Generic types are written as e.g. `List[String]` rather than Java's `List<String>`.
- Instead of the pseudo-type `void`, Scala has the actual singleton class `Unit` (see below).

### Example with classes

The following example contrasts the definition of classes in Java and Scala.

| // Java: public class Point { private double x, y; public Point(double x, double y) { this.x = x; this.y = y; } public Point(double x, double y, boolean addToGrid) { this(x, y); if (addToGrid) grid.addPoint(this); } public Point() { this(0.0, 0.0); } private void addPoint(Point p) { x += p.x; y += p.y; } public double getX() { return x; } public double getY() { return y; } double distanceToPoint(Point other) { return distanceBetweenPoints(x, y, other.x, other.y); } private static Point grid = new Point(); static double distanceBetweenPoints( double x1, double y1, double x2, double y2) { return Math.hypot(x1 - x2, y1 - y2); } } | // Scala class Point( var x: Double, var y: Double, addToGrid: Boolean = false ): import Point.* def += (p: Point) = x += p.x y += p.y if (addToGrid) grid += this def this() = this(0.0, 0.0) def distanceToPoint(other: Point) = distanceBetweenPoints(x, y, other.x, other.y) end Point object Point: private val grid = new Point() def distanceBetweenPoints(x1: Double, y1: Double, x2: Double, y2: Double) = math.hypot(x1 - x2, y1 - y2) |
|---|---|

The code above shows some of the conceptual differences between Java and Scala's handling of classes:

- Scala has no static variables or methods. Instead, it has *singleton objects*, which are essentially classes with only one instance. Singleton objects are declared using `object` instead of `class`. It is common to place static variables and methods in a singleton object with the same name as the class name, which is then known as a *companion object*. (The underlying class for the singleton object has a `$` appended. Hence, for `class Foo` with companion object `object Foo`, under the hood there's a class `Foo$` containing the companion object's code, and one object of this class is created, using the singleton pattern.)
- In place of constructor parameters, Scala has *class parameters*, which are placed on the class, similar to parameters to a function. When declared with a `val` or `var` modifier, fields are also defined with the same name, and automatically initialized from the class parameters. (Under the hood, external access to public fields always goes through accessor (getter) and mutator (setter) methods, which are automatically created. The accessor function has the same name as the field, which is why it's unnecessary in the above example to explicitly declare accessor methods.) Alternative constructors can also be declared, as in Java. Code that would go into the default constructor (other than initializing the member variables) goes directly at class level.
- In Scala it is possible to define operators by using symbols as method names. In place of `addPoint`, the Scala example defines `+=`, which is then invoked with infix notation as `grid += this`.
- Default visibility in Scala is `public`.


## Features (with reference to Java)

Scala has the same compiling model as Java and C#, namely separate compiling and dynamic class loading, so that Scala code can call Java libraries.

Scala's operational characteristics are the same as Java's. The Scala compiler generates byte code that is nearly identical to that generated by the Java compiler. In fact, Scala code can be decompiled to readable Java code, with the exception of certain constructor operations. To the Java virtual machine (JVM), Scala code and Java code are indistinguishable. The only difference is one extra runtime library, `scala-library.jar`.

Scala adds a large number of features compared with Java, and has some fundamental differences in its underlying model of expressions and types, which make the language theoretically cleaner and eliminate several *corner cases* in Java. From the Scala perspective, this is practically important because several added features in Scala are also available in C#.

### Syntactic flexibility

As mentioned above, Scala has a good deal of syntactic flexibility, compared with Java. The following are some examples:

- Semicolons are unnecessary; lines are automatically joined if they begin or end with a token that cannot normally come in this position, or if there are unclosed parentheses or brackets.
- Any method can be used as an infix operator, e.g. `"%d apples".format(num)` and `"%d apples" format num` are equivalent. In fact, arithmetic operators like `+` and `<<` are treated just like any other methods, since function names are allowed to consist of sequences of arbitrary symbols (with a few exceptions made for things like parens, brackets and braces that must be handled specially); the only special treatment that such symbol-named methods undergo concerns the handling of precedence.
- Methods `apply` and `update` have syntactic short forms. `foo()`—where `foo` is a value (singleton object or class instance)—is short for `foo.apply()`, and `foo() = 42` is short for `foo.update(42)`. Similarly, `foo(42)` is short for `foo.apply(42)`, and `foo(4) = 2` is short for `foo.update(4, 2)`. This is used for collection classes and extends to many other cases, such as STM cells.
- Scala distinguishes between no-parens (`def foo = 42`) and empty-parens (`def foo() = 42`) methods. When calling an empty-parens method, the parentheses may be omitted, which is useful when calling into Java libraries that do not know this distinction, e.g., using `foo.toString` instead of `foo.toString()`. By convention, a method should be defined with empty-parens when it performs side effects.
- Method names ending in colon (`:`) expect the argument on the left-hand-side and the receiver on the right-hand-side. For example, the `4 :: 2 :: Nil` is the same as `Nil.::(2).::(4)`, the first form corresponding visually to the result (a list with first element 4 and second element 2).
- Class body variables can be transparently implemented as separate getter and setter methods. For `trait FooLike { var bar: Int }`, an implementation may be `object Foo extends FooLike { private var x = 0; def bar = x; def bar_=(value: Int) { x = value }} } }`. The call site will still be able to use a concise `foo.bar = 42`.
- The use of curly braces instead of parentheses is allowed in method calls. This allows pure library implementations of new control structures. For example, `breakable { ... if (...) break() ... }` looks as if `breakable` was a language defined keyword, but really is just a method taking a thunk argument. Methods that take thunks or functions often place these in a second parameter list, allowing to mix parentheses and curly braces syntax: `Vector.fill(4) { math.random }` is the same as `Vector.fill(4)(math.random)`. The curly braces variant allows the expression to span multiple lines.
- For-expressions (explained further down) can accommodate any type that defines monadic methods such as `map`, `flatMap` and `filter`.

By themselves, these may seem like questionable choices, but collectively they serve the purpose of allowing domain-specific languages to be defined in Scala without needing to extend the compiler. For example, Erlang's special syntax for sending a message to an actor, i.e. `actor ! message` can be (and is) implemented in a Scala library without needing language extensions.

### Unified type system

Java makes a sharp distinction between primitive types (e.g. `int` and `boolean`) and reference types (any class). Only reference types are part of the inheritance scheme, deriving from `java.lang.Object`. In Scala, all types inherit from a top-level class `Any`, whose immediate children are `AnyVal` (value types, such as `Int` and `Boolean`) and `AnyRef` (reference types, as in Java). This means that the Java distinction between primitive types and boxed types (e.g. `int` vs. `Integer`) is not present in Scala; boxing and unboxing is completely transparent to the user. Scala 2.10 allows for new value types to be defined by the user.

### For-expressions

Instead of the Java "foreach" loops for looping through an iterator, Scala has `for`-expressions, which are similar to list comprehensions in languages such as Haskell, or a combination of list comprehensions and generator expressions in Python. For-expressions using the `yield` keyword allow a new collection to be generated by iterating over an existing one, returning a new collection of the same type. They are translated by the compiler into a series of `map`, `flatMap` and `filter` calls. Where `yield` is not used, the code approximates to an imperative-style loop, by translating to `foreach`.

A simple example is:

```mw
val s = for (x <- 1 to 25 if x*x > 50) yield 2*x
```

The result of running it is the following vector:

Vector(16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50)

(The expression `1 to 25` is not special syntax. The method `to` is rather defined in the standard Scala library as an extension method on integers, using a technique known as implicit conversions that allows new methods to be added to existing types.)

A more complex example of iterating over a map is:

```mw
// Given a map specifying Twitter users mentioned in a set of tweets,
// and number of times each user was mentioned, look up the users
// in a map of known politicians, and return a new map giving only the
// Democratic politicians (as objects, rather than strings).
val dem_mentions = for 
    (mention, times) <- mentions
    account          <- accounts.get(mention)
    if account.party == "Democratic"
  yield (account, times)
```

Expression `(mention, times) <- mentions` is an example of pattern matching (see below). Iterating over a map returns a set of key-value tuples, and pattern-matching allows the tuples to easily be destructured into separate variables for the key and value. Similarly, the result of the comprehension also returns key-value tuples, which are automatically built back up into a map because the source object (from the variable `mentions`) is a map. If `mentions` instead held a list, set, array or other collection of tuples, exactly the same code above would yield a new collection of the same type.

### Functional tendencies

While supporting all of the object-oriented features available in Java (and in fact, augmenting them in various ways), Scala also provides a large number of capabilities that are normally found only in functional programming languages. Together, these features allow Scala programs to be written in an almost completely functional style and also allow functional and object-oriented styles to be mixed.

Examples are:

- No distinction between statements and expressions
- Type inference
- Anonymous functions with capturing semantics (i.e., closures)
- Immutable variables and objects
- Lazy evaluation
- Delimited continuations (since 2.8)
- Higher-order functions
- Nested functions
- Currying
- Pattern matching
- Algebraic data types (through *case classes*)
- Tuples

#### Everything is an expression

Unlike C or Java, but similar to languages such as Lisp, Scala makes no distinction between statements and expressions. All statements are in fact expressions that evaluate to some value. Functions that would be declared as returning `void` in C or Java, and statements like `while` that logically do not return a value, are in Scala considered to return the type `Unit`, which is a singleton type, with only one object of that type. Functions and operators that never return at all (e.g. the `throw` operator or a function that always exits non-locally using an exception) logically have return type `Nothing`, a special type containing no objects; that is, a bottom type, i.e. a subclass of every possible type. (This in turn makes type `Nothing` compatible with every type, allowing type inference to function correctly.)

Similarly, an `if-then-else` "statement" is actually an expression, which produces a value, i.e. the result of evaluating one of the two branches. This means that such a block of code can be inserted wherever an expression is desired, obviating the need for a ternary operator in Scala:

| // Java: char hexDigit = (char)(x >= 10 ? x + 'A' - 10 : x + '0'); | // Scala: val hexDigit = (if x >= 10 then x + 'A' - 10 else x + '0').toChar |
|---|---|

For similar reasons, `return` statements are unnecessary in Scala, and in fact are discouraged. As in Lisp, the last expression in a block of code is the value of that block of code, and if the block of code is the body of a function, it will be returned by the function.

To make it clear that all functions are expressions, even methods that return `Unit` are written with an equals sign

```mw
def printValue(x: String): Unit = 
  println("I ate a %s".format(x))
```

or equivalently (with type inference, and omitting the unnecessary newline):

```mw
def printValue(x: String) = println("I ate a %s" format x)
```

#### Type inference

Due to type inference, the type of variables, function return values, and many other expressions can typically be omitted, as the compiler can deduce it. Examples are `val x = "foo"` (for an immutable constant or immutable object) or `var x = 1.5` (for a variable whose value can later be changed). Type inference in Scala is essentially local, in contrast to the more global Hindley-Milner algorithm used in Haskell, ML and other more purely functional languages. This is done to facilitate object-oriented programming. The result is that certain types still need to be declared (most notably, function parameters, and the return types of recursive functions), e.g.

```mw
def formatApples(x: Int) = "I ate %d apples".format(x)
```

or (with a return type declared for a recursive function)

```mw
def factorial(x: Int): Int =
  if x == 0 then 1
  else x * factorial(x - 1)
```

#### Anonymous functions

In Scala, functions are objects, and a convenient syntax exists for specifying anonymous functions. An example is the expression `x => x < 2`, which specifies a function with one parameter, that compares its argument to see if it is less than 2. It is equivalent to the Lisp form `(lambda (x) (< x 2))`. Neither the type of x nor the return type need be explicitly specified, and can generally be inferred by type inference; but they can be explicitly specified, e.g., as `(x: Int) => x < 2` or even `(x: Int) => (x < 2): Boolean`.

Anonymous functions behave as true closures in that they automatically capture any variables that are lexically available in the environment of the enclosing function. Those variables will be available even after the enclosing function returns, and unlike in the case of Java's *anonymous inner classes* do not need to be declared as final. (It is even possible to modify such variables if they are mutable, and the modified value will be available the next time the anonymous function is called.)

An even shorter form of anonymous function uses placeholder variables: For example, the following:

list map { x => sqrt(x) }

can be written more concisely as

list map { sqrt(_) }

or even

list map sqrt

#### Immutability

Scala enforces a distinction between immutable and mutable variables. Mutable variables are declared using the `var` keyword and immutable values are declared using the `val` keyword. A variable declared using the `val` keyword cannot be reassigned in the same way that a variable declared using the `final` keyword can't be reassigned in Java. `val`s are only shallowly immutable, that is, an object referenced by a val is not guaranteed to itself be immutable.

Immutable classes are encouraged by convention however, and the Scala standard library provides a rich set of immutable collection classes. Scala provides mutable and immutable variants of most collection classes, and the immutable version is always used unless the mutable version is explicitly imported. The immutable variants are persistent data structures that always return an updated copy of an old object instead of updating the old object destructively in place. An example of this is immutable linked lists where prepending an element to a list is done by returning a new list node consisting of the element and a reference to the list tail. Appending an element to a list can only be done by prepending all elements in the old list to a new list with only the new element. In the same way, inserting an element in the middle of a list will copy the first half of the list, but keep a reference to the second half of the list. This is called structural sharing. This allows for very easy concurrency — no locks are needed as no shared objects are ever modified.

#### Lazy (non-strict) evaluation

Evaluation is strict ("eager") by default. In other words, Scala evaluates expressions as soon as they are available, rather than as needed. However, it is possible to declare a variable non-strict ("lazy") with the `lazy` keyword, meaning that the code to produce the variable's value will not be evaluated until the first time the variable is referenced. Non-strict collections of various types also exist (such as the type `Stream`, a non-strict linked list), and any collection can be made non-strict with the `view` method. Non-strict collections provide a good semantic fit to things like server-produced data, where the evaluation of the code to generate later elements of a list (that in turn triggers a request to a server, possibly located somewhere else on the web) only happens when the elements are actually needed.

#### Tail recursion

Functional programming languages commonly provide tail call optimization to allow for extensive use of recursion without stack overflow problems. Limitations in JVM bytecode complicate tail call optimization on the JVM. In general, a function that calls itself with a tail call can be optimized, but mutually recursive functions cannot. Trampolines have been suggested as a workaround. Trampoline support has been provided by the Scala library with the object `scala.util.control.TailCalls` since Scala 2.8.0 (released 14 July 2010). A function may optionally be annotated with `@tailrec`, in which case it will not compile unless it is tail recursive.

An example of this optimization could be implemented using the factorial definition. For instance, the recursive version of the factorial:

```mw
def factorial(n: Int): Int =
  if n == 0 then 1
  else n * factorial(n - 1)
```

Could be optimized to the tail recursive version like this:

```mw
@tailrec
def factorial(n: Int, accum: Int): Int = 
  if n == 0 then accum
  else factorial(n - 1, n * accum)
```

However, this could compromise composability with other functions because of the new argument on its definition, so it is common to use closures to preserve its original signature:

```mw
def factorial(n: Int): Int =

  @tailrec
  def loop(current: Int, accum: Int): Int = 
  
    if current == 0 then accum
    else loop(current - 1, current * accum)
  
  loop(n, 1) // Call to the closure using the base case
  
end factorial
```

This ensures tail call optimization and thus prevents a stack overflow error.

#### Case classes and pattern matching

Scala has built-in support for pattern matching, which can be thought of as a more sophisticated, extensible version of a switch statement, where arbitrary data types can be matched (rather than just simple types like integers, Booleans and strings), including arbitrary nesting. A special type of class known as a *case class* is provided, which includes automatic support for pattern matching and can be used to model the algebraic data types used in many functional programming languages. (From the perspective of Scala, a case class is simply a normal class for which the compiler automatically adds certain behaviors that could also be provided manually, e.g., definitions of methods providing for deep comparisons and hashing, and destructuring a case class on its constructor parameters during pattern matching.)

An example of a definition of the quicksort algorithm using pattern matching is this:

```mw
def qsort(list: List[Int]): List[Int] = list match 
  case Nil => Nil
  case pivot :: tail =>
    val (smaller, rest) = tail.partition(_ < pivot)
    qsort(smaller) ::: pivot :: qsort(rest)
```

The idea here is that we partition a list into the elements less than a pivot and the elements not less, recursively sort each part, and paste the results together with the pivot in between. This uses the same divide-and-conquer strategy of mergesort and other fast sorting algorithms.

The `match` operator is used to do pattern matching on the object stored in `list`. Each `case` expression is tried in turn to see if it will match, and the first match determines the result. In this case, `Nil` only matches the literal object `Nil`, but `pivot :: tail` matches a non-empty list, and simultaneously *destructures* the list according to the pattern given. In this case, the associated code will have access to a local variable named `pivot` holding the head of the list, and another variable `tail` holding the tail of the list. These variables are read-only, and are semantically very similar to variable bindings established using the `let` operator in Lisp and Scheme.

Pattern matching also happens in local variable declarations. In this case, the return value of the call to `tail.partition` is a tuple — in this case, two lists. (Tuples differ from other types of containers, e.g. lists, in that they are always of fixed size and the elements can be of differing types — although here they are both the same.) Pattern matching is the easiest way of fetching the two parts of the tuple.

The form `_ < pivot` is a declaration of an anonymous function with a placeholder variable; see the section above on anonymous functions.

The list operators `::` (which adds an element onto the beginning of a list, similar to `cons` in Lisp and Scheme) and `:::` (which appends two lists together, similar to `append` in Lisp and Scheme) both appear. Despite appearances, there is nothing "built-in" about either of these operators. As specified above, any string of symbols can serve as function name, and a method applied to an object can be written "infix"-style without the period or parentheses. The line above as written:

qsort(smaller) ::: pivot :: qsort(rest)

could also be written thus:

qsort(rest).::(pivot).:::(qsort(smaller))

in more standard method-call notation. (Methods that end with a colon are right-associative and bind to the object to the right.)

#### Partial functions

In the pattern-matching example above, the body of the `match` operator is a partial function, which consists of a series of `case` expressions, with the first matching expression prevailing, similar to the body of a switch statement. Partial functions are also used in the exception-handling portion of a `try` statement:

```mw
try 
  ...
catch 
  case nfe: NumberFormatException => { println(nfe); List(0) }
  case _ => Nil
```

Finally, a partial function can be used alone, and the result of calling it is equivalent to doing a `match` over it. For example, the prior code for quicksort can be written thus:

```mw
val qsort: List[Int] => List[Int] = 
  case Nil => Nil
  case pivot :: tail =>
    val (smaller, rest) = tail.partition(_ < pivot)
    qsort(smaller) ::: pivot :: qsort(rest)
```

Here a read-only *variable* is declared whose type is a function from lists of integers to lists of integers, and bind it to a partial function. (The single parameter of the partial function is never explicitly declared or named.) However, we can still call this variable exactly as if it were a normal function:

```mw
scala> qsort(List(6,2,5,9))
res32: List[Int] = List(2, 5, 6, 9)
```

### Object-oriented extensions

Scala is a pure object-oriented language in the sense that every value is an object. Data types and behaviors of objects are described by classes and traits. Class abstractions are extended by subclassing and by a flexible mixin-based composition mechanism to avoid the problems of multiple inheritance.

Traits are Scala's replacement for Java's interfaces. Interfaces in Java versions under 8 are highly restricted, able only to contain abstract function declarations. This has led to criticism that providing convenience methods in interfaces is awkward (the same methods must be reimplemented in every implementation), and extending a published interface in a backwards-compatible way is impossible. Traits are similar to mixin classes in that they have nearly all the power of a regular abstract class, lacking only class parameters (Scala's equivalent to Java's constructor parameters), since traits are always mixed in with a class. The `super` operator behaves specially in traits, allowing traits to be chained using composition in addition to inheritance. The following example is a simple window system:

```mw
abstract class Window:
  // abstract
  def draw()

class SimpleWindow extends Window:
  def draw() 
    println("in SimpleWindow")
    // draw a basic window

trait WindowDecoration extends Window

trait HorizontalScrollbarDecoration extends WindowDecoration:
  // "abstract override" is needed here for "super()" to work because the parent
  // function is abstract. If it were concrete, regular "override" would be enough.
  abstract override def draw() 
    println("in HorizontalScrollbarDecoration")
    super.draw()
    // now draw a horizontal scrollbar

trait VerticalScrollbarDecoration extends WindowDecoration:
  abstract override def draw() 
    println("in VerticalScrollbarDecoration")
    super.draw()
    // now draw a vertical scrollbar

trait TitleDecoration extends WindowDecoration:
  abstract override def draw() 
    println("in TitleDecoration")
    super.draw()
    // now draw the title bar
```

A variable may be declared thus:

```mw
val mywin = new SimpleWindow with VerticalScrollbarDecoration with HorizontalScrollbarDecoration with TitleDecoration
```

The result of calling `mywin.draw()` is:

```mw
in TitleDecoration
in HorizontalScrollbarDecoration
in VerticalScrollbarDecoration
in SimpleWindow
```

In other words, the call to `draw` first executed the code in `TitleDecoration` (the last trait mixed in), then (through the `super()` calls) threaded back through the other mixed-in traits and eventually to the code in `Window`, *even though none of the traits inherited from one another*. This is similar to the decorator pattern, but is more concise and less error-prone, as it doesn't require explicitly encapsulating the parent window, explicitly forwarding functions whose implementation isn't changed, or relying on run-time initialization of entity relationships. In other languages, a similar effect could be achieved at compile-time with a long linear chain of implementation inheritance, but with the disadvantage compared to Scala that one linear inheritance chain would have to be declared for each possible combination of the mix-ins.

### Expressive type system

Scala is equipped with an expressive static type system that mostly enforces the safe and coherent use of abstractions. The type system is, however, not sound. In particular, the type system supports:

- Classes and abstract types as object members
- Structural types
- Path-dependent types
- Compound types
- Explicitly typed self references
- Generic classes
- Polymorphic methods
- Upper and lower type bounds
- Variance
- Annotation
- Views

Scala is able to infer types by use. This makes most static type declarations optional. Static types need not be explicitly declared unless a compiler error indicates the need. In practice, some static type declarations are included for the sake of code clarity.

### Type enrichment

A common technique in Scala, known as "enrich my library" (originally termed "pimp my library" by Martin Odersky in 2006; concerns were raised about this phrasing due to its negative connotations and immaturity), allows new methods to be used as if they were added to existing types. This is similar to the C# concept of extension methods but more powerful, because the technique is not limited to adding methods and can, for instance, be used to implement new interfaces. In Scala, this technique involves declaring an implicit conversion from the type "receiving" the method to a new type (typically, a class) that wraps the original type and provides the additional method. If a method cannot be found for a given type, the compiler automatically searches for any applicable implicit conversions to types that provide the method in question.

This technique allows new methods to be added to an existing class using an add-on library such that only code that *imports* the add-on library gets the new functionality, and all other code is unaffected.

The following example shows the enrichment of type `Int` with methods `isEven` and `isOdd`:

```mw
object MyExtensions:
  extension (i: Int)
    def isEven = i % 2 == 0
    def isOdd  = !i.isEven

import MyExtensions.*  // bring implicit enrichment into scope
4.isEven  // -> true
```

Importing the members of `MyExtensions` brings the implicit conversion to extension class `IntPredicates` into scope.


## Concurrency

Scala's standard library includes support for futures and promises, in addition to the standard Java concurrency APIs. Originally, it also included support for the actor model, which is now available as a separate source-available platform Akka licensed by Lightbend Inc. Akka actors may be distributed or combined with software transactional memory (*transactors*). Alternative communicating sequential processes (CSP) implementations for channel-based message passing are Communicating Scala Objects, or simply via JCSP.

An Actor is like a thread instance with a mailbox. It can be created by `system.actorOf`, overriding the `receive` method to receive messages and using the `!` (exclamation point) method to send a message. The following example shows an EchoServer that can receive messages and then print them.

```mw
val echoServer = actor(new Act:
  become:
    case msg => println("echo " + msg)
)

echoServer ! "hi"
```

Scala also comes with built-in support for data-parallel programming in the form of Parallel Collections integrated into its Standard Library since version 2.9.0.

The following example shows how to use Parallel Collections to improve performance.

```mw
val urls = List("https://scala-lang.org", "https://github.com/scala/scala")

def fromURL(url: String) = scala.io.Source.fromURL(url)
  .getLines().mkString("\n")

val t = System.currentTimeMillis()
urls.par.map(fromURL(_)) // par returns parallel implementation of a collection
println("time: " + (System.currentTimeMillis - t) + "ms")
```

Besides futures and promises, actor support, and data parallelism, Scala also supports asynchronous programming with software transactional memory, and event streams.


## Cluster computing

The most well-known open-source cluster-computing solution written in Scala is Apache Spark. Additionally, Apache Kafka, the publish–subscribe message queue popular with Spark and other stream processing technologies, is written in Scala.


## Testing

There are several ways to test code in Scala. ScalaTest supports multiple testing styles and can integrate with Java-based testing frameworks. ScalaCheck is a library similar to Haskell's QuickCheck. specs2 is a library for writing executable software specifications. ScalaMock provides support for testing high-order and curried functions. JUnit and TestNG are popular testing frameworks written in Java.


## Versions

| Version | Released | Features |
|---|---|---|
| 1.0.0-b2 | 8 December 2003 | — |
| 1.1.0-b1 | 19 February 2004 | scala.Enumeration Scala license was changed to the revised BSD license |
| 1.1.1 | 23 March 2004 | Support for Java static inner classes Library class improvements to Iterable, Array, xml.Elem, Buffer |
| 1.2.0 | 9 June 2004 | Views XML literals (to "be dropped in the near future, to be replaced with XML string interpolation") |
| 1.3.0 | 16 September 2004 | Support for Microsoft .NET Method closures Type syntax for parameterless methods changed from `[] T` to `=> T` |
| 1.4.0 | 20 June 2005 | Attributes `match` keyword replaces `match` method Experimental support for runtime types |
| 2.0 | 12 March 2006 | Compiler completely rewritten in Scala Experimental support for Java generics `implicit` and `requires` keywords `match` keyword only allowed infix operator `with` connective is only allowed following an `extends` clause Newlines can be used as statement separators in place of semicolons Regular expression match patterns restricted to sequence patterns only For-comprehensions admit value and pattern definitions Class parameters may be prefixed by val or var Private visibility has qualifiers |
| 2.1.0 | 17 March 2006 | sbaz tool integrated in the Scala distribution `match` keyword replaces `match` method Experimental support for runtime types |
| 2.1.8 | 23 August 2006 | Protected visibility has qualifiers Private members of a class can be referenced from the companion module of the class and vice versa Implicit lookup generalised Typed pattern match tightened for singleton types |
| 2.3.0 | 23 November 2006 | Functions returning `Unit` don't have to explicitly state a return type Type variables and types are distinguished between in pattern matching `All` and `AllRef` renamed to `Nothing` and `Null` |
| 2.4.0 | 9 March 2007 | `private` and `protected` modifiers accept a `[this]` qualifier Tuples can be written with round brackets Primary constructor of a class can now be marked private or protected Attributes changed to annotations with new syntax Self aliases Operators can be combined with assignment |
| 2.5.0 | 2 May 2007 | Type parameters and abstract type members can also abstract over type constructors Fields of an object can be initialized before parent constructors are called Syntax change for comprehensions Implicit anonymous functions (with underscores for parameters) Pattern matching of anonymous functions extended to support any arty |
| 2.6.0 | 27 July 2007 | Existential types Lazy values Structural types |
| 2.7.0 | 7 February 2008 | Java generic types supported by default Case classes functionality extended |
| 2.8.0 | 14 July 2010 | Revision the common, uniform, and all-encompassing framework for collection types. Type specialisation Named and default arguments Package objects Improved annotations |
| 2.9.0 | 12 May 2011 | Parallel collections Thread safe `App` trait replaces `Application` trait `DelayedInit` trait Java interop improvements |
| 2.10 | 4 January 2013 | Value classes Implicit classes String interpolation Futures and promises Dynamic and applyDynamic Dependent method types: `def identity(x: AnyRef): x.type = x // the return type says we return exactly what we got` New bytecode emitter based on ASM: Can target JDK 1.5, 1.6 and 1.7 Emits 1.6 bytecode by default Old 1.5 backend is deprecated A new pattern matcher: rewritten from scratch to generate more robust code (no more exponential blow-up) code generation and analyses are now independent (the latter can be turned off with -Xno-patmat-analysis) Scaladoc improvements Implicits (-implicits flag) Diagrams (-diagrams flag, requires graphviz) Groups (-groups) Modularized language features Parallel collections are now configurable with custom thread pools Akka actors now part of the distribution scala.actors have been deprecated and the akka implementation is now included in the distribution. Performance improvements Faster inliner Range#sum is now O(1) Update of ForkJoin library Fixes in immutable TreeSet/TreeMap Improvements to PartialFunctions Addition of ??? and NotImplementedError Addition of IsTraversableOnce + IsTraversableLike type classes for extension methods Deprecations and cleanup Floating point and octal literal syntax deprecation Removed scala.dbc Experimental features Scala reflection Macros |
| 2.10.2 | 6 June 2013 | — |
| 2.10.3 | 1 October 2013 | — |
| 2.10.4 | 18 March 2014 | — |
| 2.10.5 | 5 March 2015 | — |
| 2.11.0 | 21 April 2014 | Collection performance improvements Compiler performance improvements |
| 2.11.1 | 20 May 2014 | — |
| 2.11.2 | 22 July 2014 | — |
| 2.11.4 | 31 October 2014 | — |
| 2.11.5 | 8 January 2015 | — |
| 2.11.6 | 5 March 2015 | — |
| 2.11.7 | 23 June 2015 | — |
| 2.11.8 | 8 March 2016 | — |
| 2.11.11 | 18 April 2017 | — |
| 2.11.12 | 13 November 2017 | — |
| 2.12.0 | 3 November 2016 | Java 8 required Java 8 bytecode generated Java 8 SAM (Functional interface) language support |
| 2.12.1 | 5 December 2016 | — |
| 2.12.2 | 18 April 2017 | — |
| 2.12.3 | 26 July 2017 | — |
| 2.12.4 | 17 October 2017 | — |
| 2.12.5 | 15 March 2018 | — |
| 2.12.6 | 27 April 2018 | — |
| 2.12.7 | 27 September 2018 | — |
| 2.12.8 | 4 December 2018 | First Scala 2.12 release with the license changed to Apache v2.0 |
| 2.12.9 | 5 August 2019 | — |
| 2.12.10 | 10 September 2019 | — |
| 2.12.11 | 16 March 2020 | — |
| 2.12.12 | 13 July 2020 | — |
| 2.12.13 | 12 January 2021 | — |
| 2.12.14 | 28 May 2021 | — |
| 2.12.15 | 14 September 2021 | — |
| 2.12.16 | 10 June 2022 | — |
| 2.12.17 | 16 September 2022 | — |
| 2.12.18 | 7 June 2023 | — |
| 2.12.19 | 25 February 2024 | — |
| 2.13.0 | 11 June 2019 | Standard collections library redesigned Literal types Partial type unification By-name implicits Compiler optimizations |
| 2.13.1 | 18 September 2019 | — |
| 2.13.2 | 22 April 2020 | — |
| 2.13.3 | 25 June 2020 | — |
| 2.13.4 | 19 November 2020 | — |
| 2.13.5 | 22 February 2021 | — |
| 2.13.6 | 17 May 2021 | — |
| 2.13.7 | 1 November 2021 | — |
| 2.13.8 | 12 January 2022 | — |
| 2.13.9 | 21 September 2022 | — |
| 2.13.10 | 13 October 2022 | — |
| 2.13.11 | 7 June 2023 | — |
| 2.13.12 | 11 September 2023 | — |
| 2.13.13 | 26 February 2024 | — |
| 2.13.14 | 1 May 2024 | — |
| 2.13.15 | 25 September 2024 | — |
| 3.0.0 | 13 May 2021 | — |
| 3.0.1 | 31 July 2021 | — |
| 3.0.2 | 7 September 2021 | — |
| 3.1.0 | 21 October 2021 | — |
| 3.1.1 | 1 February 2022 | — |
| 3.1.2 | 12 April 2022 | — |
| 3.1.3 | 21 June 2022 | — |
| 3.2.0 | 5 September 2022 | — |
| 3.2.1 | 7 November 2022 | — |
| 3.2.2 | 30 January 2023 | — |
| 3.3.0 | 30 May 2023 | — |
| 3.3.1 | 7 September 2023 | — |
| 3.3.2 | 29 February 2024 | — |
| 3.3.3 | 29 February 2024 | — |
| 3.3.8 | 10 June 2026 | — |
| 3.4.0 | 29 February 2024 | — |
| 3.4.1 | 29 March 2024 | — |
| 3.4.2 | 16 May 2024 | — |
| 3.4.3 | 23 August 2024 | — |
| 3.5.0 | 22 August 2024 | — |
| 3.5.1 | 20 September 2024 | — |
| 3.5.2 | 22 October 2024 | — |
| 3.6.2 | 10 December 2024 | — |
| 3.6.3 | 20 January 2025 | Added the `-Yprofile-trace` compiler option |
| 3.6.4 | 7 March 2025 | — |
| 3.7.0 | 7 May 2025 | — |
| 3.7.1 | 4 June 2025 | — |
| 3.7.2 | 1 August 2025 | — |
| 3.7.3 | 9 September 2025 | — |
| 3.7.4 | 11 November 2025 | — |
| 3.8.0 | 16 January 2026 | — |
| 3.8.1 | 22 January 2026 | — |
| 3.8.2 | 24 February 2026 | — |
| 3.8.3 | 31 March 2026 | — |
| 3.8.4 | 5 June 2026 | — |
