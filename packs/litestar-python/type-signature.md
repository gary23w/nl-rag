---
title: "Type signature"
source: https://en.wikipedia.org/wiki/Type_signature
domain: litestar-python
license: CC-BY-SA-4.0
tags: litestar python framework, asgi python framework, python type hints api, litestar dependency injection
fetched: 2026-07-02
---

# Type signature

In computer science, a **type signature** or **type annotation** defines the inputs and outputs of a function, subroutine or method. A type signature includes the number, types, and order of the function's arguments. One important use of a type signature is for function overload resolution, where one particular definition of a function to be called is selected among many overloaded forms.

## Examples

### C/C++

In C and C++, the type signature is declared by what is commonly known as a function prototype. In C/C++, a function declaration reflects its use; for example, a function pointer with the signature `(int)(char, double)` would be called as:

```mw
char c;
double d;
int retVal = (*fPtr)(c, d);
```

### Erlang

In Erlang, type signatures may be optionally declared, as:

```mw
-spec function_name(type1(), type2(), ...) -> out_type().
```

For example:

```mw
-spec is_even(number()) -> boolean().
```

### Haskell

A type signature in Haskell generally takes the following form:

```mw
functionName :: arg1Type -> arg2Type -> ... -> argNType
```

Notice that the type of the result can be regarded as everything past the first supplied argument. This is a consequence of currying, which is made possible by Haskell's support for first-class functions; this function requires two inputs where one argument is supplied and the function is "curried" to produce a function for the argument not supplied. Thus, calling `f x`, where `f :: a -> b -> c`, yields a new function `f2 :: b -> c` that can be called `f2 b` to produce `c`.

The actual type specifications can consist of an actual type, such as `Integer`, or a general type variable that is used in parametric polymorphic functions, such as `a`, or `b`, or `anyType`. So we can write something like: `functionName :: a -> a -> ... -> a`

Since Haskell supports higher-order functions, functions can be passed as arguments. This is written as: `functionName :: (a -> a) -> a`

This function takes in a function with type signature `a -> a` and returns data of type `a` out.

### Java

In the Java virtual machine, *internal type signatures* are used to identify methods and classes at the level of the virtual machine code.

Example: The method `String String.substring(int, int)` is represented in bytecode as `Ljava/lang/String.substring(II)Ljava/lang/String;` .

The signature of the `main` method looks like this:

```mw
public static void main(String[] args);
```

And in the disassembled bytecode, it takes the form of `Lsome/package/Main/main:([Ljava/lang/String;)V`

The method signature for the `main()` method contains three modifiers:

- `public` indicates that the `main()` method can be called by any object.
- `static` indicates that the `main()` method is a class method.
- `void` indicates that the `main()` method has no return value.

## Signature

A function signature consists of the function prototype. It specifies the general information about a function like the name, scope and parameters. Many programming languages use name mangling in order to pass along more semantic information from the compilers to the linkers. In addition to mangling, there is an excess of information in a function signature (stored internally to most compilers) which is not readily available, but may be accessed.

Understanding the notion of a function signature is an important concept for all computer science studies.

- Modern object orientation techniques make use of interfaces, which are essentially templates made from function signatures.
- C++ uses function overloading with various signatures.

The practice of multiple inheritance requires consideration of the function signatures to avoid unpredictable results. Computer science theory, and the concept of polymorphism in particular, make much use of the concept of function signature.

In the C programming language, a signature is roughly equivalent to its prototype definition.

In the ML family of programming languages, "signature" is used as a keyword referring to a construct of the module system that plays the role of an interface.

## Method signature

In computer programming, especially object-oriented programming, a method is commonly identified by its unique **method signature**, which usually includes the method name and the number, types, and order of its parameters. A method signature is the smallest type of a method.

### Examples

#### C

In C, the method signature is the method name and the number and type of its parameters, but it is possible to have variadic parameters, but these are not type-safe.

```mw
int printf(const char* fmt, ...);
```

Manipulation of these parameters can be done by using the routines in the standard library header `<stdarg.h>`.

#### C++

In C++, in addition to the C-style function return type appearing before, the return type may also follow the parameter list, which is referred to as a trailing return type. The difference is only syntactic; in either case, the resulting signature is identical.

If using variadic templates:

```mw
void doSomething(auto&&... args);
```

Note `void doSomething(auto... args);` is equivalent to `template <typename... Ts> void doSomething(Ts... args);`.

#### C

Similar to the syntax of C, method signatures in C# are composed of a name and the number and type of its parameters, where the last parameter may be an array of values:

```mw
void Add(out int sum, params int[] value);
[...]
Add(out sum, 3, 5, 7, 11, -1);  // sum == 25
```

#### Java

In Java, a method signature is composed of a name and the number, type, and order of its parameters. Return types and thrown exceptions are not considered to be a part of the method signature, nor are the names of parameters; they are ignored by the compiler for checking method uniqueness.

The method signatures help distinguish overloaded methods (methods with the same name) in a class. Return types are not included in overloading. Only method signatures should be used to distinguish overloaded methods.

For example, the following two methods have different signatures:

```mw
void doSomething(String[] x); // doSomething(String[])
void doSomething(String x); // doSomething(String)
```

The following two methods both have the same signature:

```mw
int doSomething(int x); // doSomething(int)
void doSomething(int y) throws Exception; // doSomething(int)
```

Variadic parameters in Java are represented with ellipses on the final parameter. These behave identically to an array, but in the JVM bytecode the method is marked variadic.

```mw
void doSomething(String... x); // equivalent to doSomething(String[])
```

#### Julia

In Julia, function signatures take the following form:

```mw
commission(sale::Int, rate::Float64)::Float64
```

The types in the arguments are used for the multiple dispatch. The return type is validated when the function returns a value, and a runtime exception is raised if the type of the value does not agree with the specified type.

Abstract types are allowed and are encouraged for implementing general behavior that is common to all subtypes. The above function can therefore be rewritten as follows. In this case, the function can accept any Integer and Real subtypes accordingly.

```mw
commission(sale::Integer, rate::Real)::Real
```

Types are completely optional in function arguments. When unspecified, it is equivalent to using the type Any, which is the super-type of all types. It is idiomatic to specify argument types but not return type.

#### Objective-C

In the Objective-C programming language, method signatures for an object are declared in the interface header file. For example,

```mw
- (id)initWithInt:(int)value;
```

defines a method `initWithInt` that returns a general object (an `id`) and takes one integer argument. Objective-C only requires a type in a signature to be explicit when the type is not `id`; this signature is equivalent:

```mw
- initWithInt:(int)value;
```

#### Rust

In Rust, function signatures take the following form:

```mw
fn commission(sale: u32, rate: f64) -> f64;
```
