---
title: "Operator overloading"
source: https://en.wikipedia.org/wiki/Operator_overloading
domain: ad-hoc-polymorphism
license: CC-BY-SA-4.0
tags: ad hoc polymorphism, function overloading, type class, operator overloading
fetched: 2026-07-02
---

# Operator overloading

In computer programming, **operator overloading**, sometimes termed *operator ad hoc polymorphism*, is a specific case of polymorphism, where different operators have different implementations depending on their arguments. Operator overloading is generally defined by a programming language, a programmer, or both.

## Rationale

Operator overloading is syntactic sugar, and is used because it allows programming using notation nearer to the target domain and allows user-defined types a similar level of syntactic support as types built into a language. It is common, for example, in scientific computing, where it allows computing representations of mathematical objects to be manipulated with the same syntax as on paper.

Operator overloading does not change the expressive power of a language (with functions), as it can be emulated using function calls. For example, consider variables `a`, `b` and `c` of some user-defined type, such as matrices:

`a + b * c`

In a language that supports operator overloading, and with the usual assumption that the `*` operator has higher precedence than the `+` operator, this is a concise way of writing:

`Add(a, Multiply(b, c))`

However, the former syntax reflects common mathematical usage.

## Examples

In this case, the addition operator is overloaded to allow addition on a user-defined type `Time` in C++:

```mw
Time operator+(const Time& lhs, const Time& rhs) {
    Time temp = lhs;
    temp.seconds += rhs.seconds;
    temp.minutes += temp.seconds / 60;
    temp.seconds %= 60;
    temp.minutes += rhs.minutes;
    temp.hours += temp.minutes / 60;
    temp.minutes %= 60;
    temp.hours += rhs.hours;
    return temp;
}
```

Addition is a binary operation, which means it has two operands. In C++, the arguments being passed are the operands, and the `temp` object is the returned value.

The operation could also be defined as a class method, replacing `lhs` by the hidden `this` argument; However, this forces the left operand to be of type `Time`:

```mw
// The "const" right before the opening curly brace means that `this` is not modified.
Time Time::operator+(const Time& rhs) const {
    Time temp = *this;  // `this` should not be modified, so make a copy.
    temp.seconds += rhs.seconds;
    temp.minutes += temp.seconds / 60;
    temp.seconds %= 60;
    temp.minutes += rhs.minutes;
    temp.hours += temp.minutes / 60;
    temp.minutes %= 60;
    temp.hours += rhs.hours;
    return temp;
}
```

Note that a unary operator defined as a class method would receive no apparent argument (it only works from `this`):

```mw
bool Time::operator!() const {
    return hours == 0 && minutes == 0 && seconds == 0;
}
```

The less-than (<) operator is often overloaded to sort a structure or class:

```mw
class IntegerPair {
private:
    int x;
    int y;
public:
    explicit IntegerPair(int x = 0, int y = 0):
        x{x}, y{y} {}

    bool operator<(const IntegerPair& p) const {
        if (x == p.x) {
            return y < p.y;
        }
        return x < p.x;
    }
};
```

Like with the previous examples, in the last example operator overloading is done within the class. In C++, after overloading the less-than operator (`operator<`), standard sorting functions can be used to sort some classes.

Starting in C++20 with the introduction of the three-way comparison operator (`operator<=>`), all the order operators can be defined by just defining that operator. The three-way comparison operator exists in many languages, including C++, Python, Rust, Swift, and PHP. Other languages, such as Java and C# instead use a method `Comparable.compareTo()`.

```mw
import std;

using std::strong_ordering;

class IntegerPair {
private:
    int x;
    int y;
public:
    explicit IntegerPair(int x = 0, int y = 0):
        x{x}, y{y} {}

    // can be auto-generated with = default;
    strong_ordering operator<(const IntegerPair& p) const {
        if (strong_ordering cmp = x <=> p.x; cmp != strong_ordering::equal) {
            return cmp;
        }
        return y <=> p.y;
    }
};
```

## Criticisms

Operator overloading has been criticized because it allows programmers to reassign the semantics of operators depending on the types of their operands. For example, the use of the `<<` operator in C++ `a << b` shifts the bits in the variable `a` left by `b` bits if `a` and `b` are of an integer type, but if `a` is an output stream then the above code will attempt to write a `b` to the stream. Because operator overloading allows the original programmer to change the usual semantics of an operator and to catch any subsequent programmers by surprise, it is considered good practice to use operator overloading with care (the creators of Java decided not to use this feature, although not necessarily for this reason).

Another, more subtle, issue with operators is that certain rules from mathematics can be wrongly expected or unintentionally assumed. For example, the commutativity of + (i.e. that `a + b == b + a`) does not always apply; an example of this occurs when the operands are strings, since + is commonly overloaded to perform a concatenation of strings (i.e. `"bird" + "song"` yields `"birdsong"`, while `"song" + "bird"` yields `"songbird"`). A typical counter to this argument comes directly from mathematics: While + is commutative on integers (and more generally any complex number), it is not commutative for other "types" of variables. In practice, + is not even always associative, for example with floating-point values due to rounding errors. Another example: In mathematics, multiplication is commutative for real and complex numbers but not commutative in matrix multiplication.

## Catalog

A classification of some common programming languages is made according to whether their operators are overloadable by the programmer and whether the operators are limited to a predefined set.

| Operators | Not overloadable | Overloadable |
|---|---|---|
| New definable | ML Prolog | ALGOL 68 Clojure Eiffel Fortran F# Haskell Julia R Scala Smalltalk Swift |
| Limited set | BASIC C Go Java JavaScript Modula-2 Objective-C Pascal TypeScript Visual Basic | Ada C# C++ D Dart Groovy Kotlin Lua MATLAB Object Pascal (Free Pascal, Delphi (since 2005)) PHP Perl Python Ruby Rust Visual Basic .NET |

## Timeline of operator overloading

### 1960s

The ALGOL 68 specification allowed operator overloading.

Extract from the ALGOL 68 language specification (page 177) where the overloaded operators ¬, =, ≠, and **abs** are defined:

```
10.2.2. Operations on Boolean Operands
a) op ∨ = (bool a, b) bool:( a | true | b );
b) op ∧ = (bool a, b) bool: ( a | b | false );
c) op ¬ = (bool a) bool: ( a | false | true );
d) op = = (bool a, b) bool:( a∧b ) ∨ ( ¬b∧¬a );
e) op ≠ = (bool a, b) bool: ¬(a=b);
f) op abs = (bool a)int: ( a | 1 | 0 );
```

Note that no special declaration is needed to *overload* an operator, and the programmer is free to create new operators. For dyadic operators their priority compared to other operators can be set:

```
 prio max = 9;
 
 op max = (int a, b) int: ( a>b | a | b );
 op ++ = ( ref int a ) int: ( a +:= 1 );
```

### 1980s

Ada supports overloading of operators from its inception, with the publication of the Ada 83 language standard. However, the language designers chose to preclude the definition of new operators. Only extant operators in the language may be overloaded, by defining new functions with identifiers such as "+", "*", "&" etc. Subsequent revisions of the language (in 1995 and 2005) maintain the restriction to overloading of extant operators.

In C++, operator overloading is more refined than in ALGOL 68.

### 1990s

Java language designers at Sun Microsystems chose to omit overloading. When asked about operator overloading, Brian Goetz of Oracle responded "Value types first, then we can talk about it.", suggesting that it could potentially be added after Project Valhalla.

Python allows operator overloading through the implementation of methods with special names. For example, the addition (+) operator can be overloaded by implementing the method `obj.__add__(self, other)`.

Ruby allows operator overloading as syntactic sugar for simple method calls.

Lua allows operator overloading as syntactic sugar for method calls with the added feature that if the first operand doesn't define that operator, the method for the second operand will be used.

### 2000s

Microsoft added operator overloading to C# in 2001 and to Visual Basic .NET in 2003. C# operator overloading is very similar in syntax to C++ operator overloading:

```mw
public class Fraction
{
    private int numerator;
    private int denominator;

    // ...

    public static Fraction operator +(Fraction lhs, Fraction rhs)
        => new Fraction(lhs.numerator * rhs.denominator + rhs.numerator * lhs.denominator, lhs.denominator * rhs.denominator);
}
```

Scala treats all operators as methods and thus allows operator overloading by proxy.

### 2010s

In Raku, the definition of all operators is delegated to lexical functions, and so, using function definitions, operators can be overloaded or new operators added. For example, the function defined in the Rakudo source for incrementing a Date object with "`+`" is:

```mw
multi infix:<+>(Date:D $d, Int:D $x) {
    Date.new-from-daycount($d.daycount + $x)
}
```

Since "multi" was used, the function gets added to the list of multidispatch candidates, and "`+`" is only overloaded for the case where the type constraints in the function signature are met. While the capacity for overloading includes `+`, `*`, `>=`, the postfix and term `i`, and so on, it also allows for overloading various brace operators: `[x, y]`, `x[y]`, `x{y}`, and `x(y)`.

Kotlin has supported operator overloading since its creation by overwriting specially named functions (like `plus()`, `inc()`, `rangeTo()`, etc.)

```mw
data class Point(val x: Int, val y: Int) {
    operator fun plus(other: Point): Point {
        return Point(this.x + other.x, this.y + other.y)
    }
}
```

Because both Kotlin and Java compile to .class, when converted back to Java this will just be represented as:

```mw
public class Point {
    // fields and constructor...

    public Point plus(Point other) {
        return new Point(this.x + other.x, this.y + other.y);
    }
}
```

Operator overloading in Rust is accomplished by implementing the traits in `std::ops`.

```mw
use std::ops::Add;

#[derive(Debug)]
struct Point {
    x: i32,
    y: i32
}

impl Point {
    pub fn new(x: i32, y: i32) -> Self {
        Point {x, y}
    }
}

impl Add for Point {
    type Output = Point;

    fn add(self, other: Point) -> Point {
        Point {
            x: self.x + other.y,
            y: self.y + other.y
        }
    }
}

fn main() {
    let p1: Point = Point::new(1, 2);
    let p2: Point = Point::new(3, 4);
    let sum: Point = p1 + p2;
    println!("Sum of p1 and p2: {:?}", sum);
}
```
