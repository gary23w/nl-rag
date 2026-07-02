---
title: "Function overloading"
source: https://en.wikipedia.org/wiki/Function_overloading
domain: ad-hoc-polymorphism
license: CC-BY-SA-4.0
tags: ad hoc polymorphism, function overloading, type class, operator overloading
fetched: 2026-07-02
---

# Function overloading

In some programming languages, **function overloading** or **method overloading** is the ability to create multiple functions of the same name with different implementations. Calls to an overloaded function will run a specific implementation of that function appropriate to the context of the call, allowing one function call to perform different tasks depending on context.

## Basic definition

For example, doTask() and doTask(object o) are overloaded functions. To call the latter, an object must be passed as a parameter, whereas the former does not require a parameter, and is called with an empty parameter field. A common error would be to assign a default value to the object in the second function, which would result in an *ambiguous call* error, as the compiler wouldn't know which of the two methods to use.

Another example is a Print(object o) function that executes different actions based on whether it's printing text or photos. The two different functions may be overloaded as Print(text_object T); Print(image_object P). If we write the overloaded print functions for all objects our program will "print", we never have to worry about the type of the object, and the correct function call again, the call is always: Print(something).

## Languages supporting overloading

Languages supporting function overloading include, but are not limited to:

- Ada
- Apex
- C++
- C#
- Clojure
- Crystal
- D
- Delphi
- Elixir
- Swift
- Fortran
- Kotlin
- Java
- Julia
- Nim
- PostgreSQL and PL/SQL
- Scala
- TypeScript
- Visual Basic (.NET)
- Wolfram Language

Languages not supporting function overloading include C, Python, Rust, and Zig.

## Rules in function overloading

- The same function name is used for more than one function definition in a particular module, class or namespace
- The functions must have different type signatures, i.e. differ in the number or the types of their formal parameters (as in C++) or additionally in their return type (as in Ada).

Function overloading is usually associated with statically-typed programming languages that enforce type checking in function calls. An overloaded function is a set of different functions that are callable with the same name. For any particular call, the compiler determines which overloaded function to use and resolves this at compile time. This is true for programming languages such as Java.

Function overloading differs from forms of polymorphism where the choice is made at runtime, e.g. through virtual functions, instead of statically.

**Example: Function overloading in C++**

```mw
import std;

// Volume of a cube.
int volume(int s) {
  return s * s * s;
}

// Volume of a cylinder.
double volume(double r, int h) {
    return std::numbers::pi * r * r * static_cast<double>(h);
}

// Volume of a cuboid (rectangular prism).
long volume(long l, int b, int h) {
    return l * b * h;
}

int main() {
    std::println("{}", volume(10));
    std::println("{}", volume(2.5, 8));
    std::println("{}", volume(100l, 75, 15));
}
```

In the above example, the volume of each component is calculated using one of the three functions named "volume", with selection based on the differing number and type of actual parameters.

## Constructor overloading

Constructors, used to create instances of an object, may also be overloaded in some object-oriented programming languages. Because in many languages the constructor's name is predetermined by the name of the class, it would seem that there can be only one constructor. Whenever multiple constructors are needed, they are to be implemented as overloaded functions. In C++, default constructors take no parameters, instantiating the object members with their appropriate default values, "which is normally zero for numeral fields and empty string for string fields". For example, a default constructor for a restaurant bill object written in C++ might set the tip to 15%:

```mw
Bill(): 
    tip{0.15}, total{0.0} {}
```

The drawback to this is that it takes two steps to change the value of the created Bill object. The following shows creation and changing the values within the main program:

```mw
Bill cafe;
cafe.tip = 0.10;
cafe.total = 4.00;
```

By overloading the constructor, one could pass the tip and total as parameters at creation. This shows the overloaded constructor with two parameters. This overloaded constructor is placed in the class as well as the original constructor we used before. Which one gets used depends on the number of parameters provided when the new Bill object is created (none, or two):

```mw
Bill(double tip, double total): 
    tip{tip}, total{total} {}
```

Now a function that creates a new Bill object could pass two values into the constructor and set the data members in one step. The following shows creation and setting the values:

```mw
Bill cafe(0.10, 4.00);
```

This can be useful in increasing program efficiency and reducing code length.

Another reason for constructor overloading can be to enforce mandatory data members. In this case the default constructor is declared private or protected (or preferably deleted since C++11) to make it inaccessible from outside. For the Bill above total might be the only constructor parameter – since a Bill has no sensible default for total – whereas tip defaults to 0.15.

## Complications

Two issues interact with and complicate function overloading: Name masking (due to scope) and implicit type conversion.

If a function is declared in one scope, and then another function with the same name is declared in an inner scope, there are two natural possible overloading behaviors: the inner declaration masks the outer declaration (regardless of signature), or both the inner declaration and the outer declaration are included in the overload, with the inner declaration masking the outer declaration only if the signature matches. The first is taken in C++: "in C++, there is no overloading across scopes." As a result, to obtain an overload set with functions declared in different scopes, one needs to explicitly import the functions from the outer scope into the inner scope, with the `using` keyword.

Implicit type conversion complicates function overloading because if the types of parameters do not exactly match the signature of one of the overloaded functions, but can match after type conversion, resolution depends on which type conversion is chosen.

These can combine in confusing ways: An inexact match declared in an inner scope can mask an exact match declared in an outer scope, for instance.

For example, to have a derived class with an overloaded function taking a `double` or an `int`, using the function taking an `int` from the base class, in C++, one would write:

```mw
class Base {
public:
    void fn(int i);
};

class Derived: public Base {
public:
    using Base::fn;
    void fn(double d);
};
```

Failing to include the `using` results in an `int` parameter passed to `fn` in the derived class being converted to a double and matching the function in the derived class, rather than in the base class; Including `using` results in an overload in the derived class and thus matching the function in the base class.

## Caveats

If a method is designed with an excessive number of overloads, it may be difficult for developers to discern which overload is being called simply by reading the code. This is particularly true if some of the overloaded parameters are of types that are inherited types of other possible parameters (for example "object"). An IDE can perform the overload resolution and display (or navigate to) the correct overload.

Type-based overloading can also hamper code maintenance, where code updates can accidentally change which method overload is chosen by the compiler.
