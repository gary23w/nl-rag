---
title: "Type safety"
source: https://en.wikipedia.org/wiki/Type_safety
domain: drizzle-orm
license: CC-BY-SA-4.0
tags: drizzle orm, typescript sql orm, type-safe query builder, sql-like schema
fetched: 2026-07-02
---

# Type safety

In computer science, **type safety** is the extent to which a programming language discourages or prevents type errors. Type-safe languages are sometimes also called **strongly** or **strictly typed**. The behaviors classified as type errors by a given programming language are usually those that result from attempts to perform operations on values that are not of the appropriate data type, e.g. trying to add a string to an integer.

Type enforcement can be static (catching potential errors at compile time), dynamic (associating type information with values at run-time and consulting them as needed to detect imminent errors), or a combination of both. Dynamic type enforcement can often run programs that would be invalid under static enforcement, but at the cost of introducing errors at runtime.

In the context of static (compile-time) type systems, type safety usually involves (among other things) a guarantee that the eventual value of any expression will be a legitimate member of that expression's static type. The precise requirement is more subtle than this — see, for example, subtyping and polymorphism for complications.

## Definitions

Intuitively, type soundness is captured by Robin Milner's pithy statement that

Well-typed programs cannot "go wrong".

In other words, if a type system is *sound*, then expressions accepted by that type system must evaluate to a value of the appropriate type (rather than produce a value of some other, unrelated type or crash with a type error). Vijay Saraswat provides the following, related definition:

A language is type-safe if the only operations that can be performed on data in the language are those sanctioned by the type of the data.

However, what precisely it means for a program to be "well typed" or to "go wrong" are properties of its static and dynamic semantics, which are specific to each programming language. Consequently, a precise, formal definition of type soundness depends upon the style of formal semantics used to specify a language. In 1994, Andrew Wright and Matthias Felleisen formulated what has become the standard definition and proof technique for type safety in languages defined by operational semantics, which is closest to the notion of type safety as understood by most programmers. Under this approach, the semantics of a language must have the following two properties to be considered type-sound:

**Progress**

A well-typed program never gets "stuck": every

expression

is either already a

value

or can be reduced towards a value in some well-defined way. In other words, the program never gets into an undefined state where no further transitions are possible.

**Preservation (or subject reduction)**

After each evaluation step, the type of each expression remains the same (that is, its type is

preserved

).

A number of other formal treatments of type soundness have also been published in terms of denotational semantics and structural operational semantics.

## Relation to other forms of safety

In isolation, type soundness is a relatively weak property, as it essentially just states that the rules of a type system are internally consistent and cannot be subverted. However, in practice, programming languages are designed so that well-typedness also entails other, stronger properties, some of which include:

- Prevention of illegal operations. For example, a type system can reject the expression `3 / "Hello, World"` as invalid, because the division operator is not defined for a string divisor.
- Memory safety
  - Type systems can prevent wild pointers that could otherwise arise from a pointer to one type of object being treated as a pointer to another type.
  - More sophisticated type systems, such as those supporting dependent types, can detect and reject out-of-bound accesses, preventing potential buffer overflows.
- Logic errors originating in the semantics of different types. For instance, inches and millimeters may both be stored as integers, but should not be substituted for each other or added. A type system can enforce two different types of integer for them.

## Type-safe and type-unsafe languages

Type safety is usually a requirement for any toy language (i.e., esoteric language) proposed in academic programming language research. However, many languages are too big for human-generated type safety proofs, as they often require checking thousands of cases. Nevertheless, some languages such as Standard ML, which has rigorously defined semantics, have been proved to meet one definition of type safety. Some other languages such as Haskell are *believed* to meet some definition of type safety, provided certain "escape" features are not used (for example Haskell's unsafePerformIO, used to "escape" from the usual restricted environment in which input/output (I/O) is possible, circumvents the type system and so can be used to break type safety.) Type punning is another example of such an "escape" feature. Regardless of the properties of the language definition, certain errors may occur at run-time due to bugs in the implementation, or in linked libraries written in other languages; such errors could render a given implementation type unsafe in certain circumstances. An early version of Sun's Java virtual machine was vulnerable to this sort of problem.

## Strong and weak typing

Programming languages are often colloquially classified as strongly typed or weakly typed (also loosely typed) to refer to certain aspects of type safety. In 1974, Liskov and Zilles defined a strongly-typed language as one in which "whenever an object is passed from a calling function to a called function, its type must be compatible with the type declared in the called function." In 1977, Jackson wrote, "In a strongly typed language each data area will have a distinct type and each process will state its communication requirements in terms of these types." In contrast, a weakly typed language may produce unpredictable results or may perform implicit type conversion.

## Memory management and type safety

Type safety is closely linked to memory safety. For instance, in an implementation of a language that has some type t which allows some bit patterns but not others, a dangling pointer memory error allows writing a bit pattern that does not represent a legitimate member of t into a dead variable of type t , causing a type error when the variable is read. Conversely, if the language is memory-safe, it cannot allow an arbitrary integer to be used as a pointer, hence there must be a separate pointer or reference type.

As a minimal condition, a type-safe language must not allow dangling pointers across allocations of different types. But most languages enforce the proper use of abstract data types defined by programmers even when this is not strictly necessary for memory safety or for the prevention of any kind of catastrophic failure. Allocations are given a type describing its contents, and this type is fixed for the duration of the allocation. This allows type-based alias analysis to infer that allocations of different types are distinct.

Most type-safe languages use garbage collection. Pierce says, "it is extremely difficult to achieve type safety in the presence of an explicit deallocation operation", due to the dangling pointer problem. However Rust is generally considered type-safe and uses a borrow checker to achieve memory safety, instead of garbage collection.

## Type safety in object oriented languages

In object-oriented languages type safety is usually intrinsic in the fact that a type system is in place. This is expressed in terms of class definitions.

A class essentially defines the structure of the objects derived from it and an API as a *contract* for handling these objects. Each time a new object is created it will *comply* with that contract.

Each function that exchanges objects derived from a specific class, or implementing a specific interface, will adhere to that contract: hence in that function the operations permitted on that object will be only those defined by the methods of the class the object implements. This will guarantee that the object integrity will be preserved.

Exceptions to this are object oriented languages that allow dynamic modification of the object structure, or the use of reflection to modify the content of an object to overcome the constraints imposed by the class methods definitions.

## Type safety issues in specific languages

### Ada

Ada was designed to be suitable for embedded systems, device drivers and other forms of system programming, but also to encourage type-safe programming. To resolve these conflicting goals, Ada confines type-unsafety to a certain set of special constructs whose names usually begin with the string Unchecked_. Unchecked_Deallocation can be effectively banned from a unit of Ada text by applying pragma Pure to this unit. It is expected that programmers will use Unchecked_ constructs very carefully and only when necessary; programs that do not use them are type-safe.

The SPARK programming language is a subset of Ada eliminating all its potential ambiguities and insecurities while at the same time adding statically checked contracts to the language features available. SPARK avoids the issues with dangling pointers by disallowing allocation at run time entirely.

Ada2012 adds statically checked contracts to the language itself (in form of pre-, and post-conditions, as well as type invariants).

### C

The C programming language is type-safe in limited contexts; for example, a compile-time error is generated when an attempt is made to convert a pointer to one type of structure to a pointer to another type of structure, unless an explicit cast is used. However, a number of very common operations are non-type-safe; for example, the usual way to print an integer is something like `printf("%d", 12)`, where the `%d` tells `printf` at run-time to expect an integer argument. (Something like `printf("%s", 12)`, which tells the function to expect a pointer to a character-string and yet supplies an integer argument, may be accepted by compilers, but will produce undefined results.) This is partially mitigated by some compilers (such as gcc) checking type correspondences between printf arguments and format strings.

In addition, C, like Ada, provides unspecified or undefined explicit conversions; and unlike in Ada, idioms that use these conversions are very common, and have helped to give C a type-unsafe reputation. For example, the standard way to allocate memory on the heap is to invoke a memory allocation function, such as `malloc`, with an argument indicating how many bytes are required. The function returns a void pointer (`void*`), which the calling code must explicitly or implicitly cast to the appropriate pointer type. Pre-standardized implementations of C required an explicit cast to do so, therefore for an allocation of some `struct Foo`, the code `Foo* foo = (struct Foo*)malloc(sizeof(struct Foo))` became the accepted practice. `malloc()` returns `void*` which does not need to be explicitly cast in C, but in C++ this casting is made mandatory for type safety.

### C++

C++ is generally more type-safe than its predecessor, C, with features like not allowing implicit cast from `void*` to another pointer types and other features like:

- The new operator returning a pointer of type based on operand, while malloc returning a void pointer.
- C++ code can use virtual functions and templates to achieve type-safe polymorphism without void pointers.
- Safer casting operators, such as `dynamic_cast` that perform run-time type checking between pointers and references; while `static_cast` perform compile-time checking between types that are going to be cast one to other, which is generally more safe than C-style casts.
- C++11 strongly-typed enumerations (also known as `enum class`'es) cannot be implicitly converted to or from integers or other enumeration types.
- C++ explicit constructors and C++11 explicit conversion operators prevent implicit type conversions.

### C

C# is type-safe. It has support for untyped pointers, but this must be accessed using the "unsafe" keyword which can be prohibited at the compiler level. It has inherent support for run-time cast validation. Casts can be validated by using the "as" keyword that will return a null reference if the cast is invalid, or by using a C-style cast that will throw an exception if the cast is invalid. See C Sharp conversion operators.

Undue reliance on the object type (from which all other types are derived) runs the risk of defeating the purpose of the C# type system. It is usually better practice to abandon object references in favour of generics, similar to templates in C++ and generics in Java.

### Java

The Java language is designed to enforce type safety. Anything in Java *happens* inside an object and each object is an instance of a class.

To implement the *type safety* enforcement, each object, before usage, needs to be allocated. Java allows usage of primitive types but only inside properly allocated objects.

Sometimes a part of the type safety is implemented indirectly: e.g. the class BigDecimal represents a floating point number of arbitrary precision, but handles only numbers that can be expressed with a finite representation. The operation BigDecimal.divide() calculates a new object as the division of two numbers expressed as BigDecimal.

In this case if the division has no finite representation, as when one computes e.g. 1/3=0.33333..., the divide() method can raise an exception if no rounding mode is defined for the operation. Hence the library, rather than the language, guarantees that the object respects the contract implicit in the class definition.

### Standard ML

Standard ML has rigorously defined semantics and is known to be type-safe. However, some implementations, including Standard ML of New Jersey (SML/NJ), its syntactic variant Mythryl and MLton, provide libraries that offer unsafe operations. These facilities are often used in conjunction with those implementations' foreign function interfaces to interact with non-ML code (such as C libraries) that may require data laid out in specific ways. Another example is the SML/NJ interactive toplevel itself, which must use unsafe operations to execute ML code entered by the user.

### Modula-2

Modula-2 is a strongly-typed language with a design philosophy to require any unsafe facilities to be explicitly marked as unsafe. This is achieved by "moving" such facilities into a built-in pseudo-library called SYSTEM from where they must be imported before they can be used. The import thus makes it visible when such facilities are used. Unfortunately, this was not consequently implemented in the original language report and its implementation. There still remained unsafe facilities such as the type cast syntax and variant records (inherited from Pascal) that could be used without prior import. The difficulty in moving these facilities into the SYSTEM pseudo-module was the lack of any identifier for the facility that could then be imported since only identifiers can be imported, but not syntax.

```mw
IMPORT SYSTEM; (* allows the use of certain unsafe facilities: *)
VAR word : SYSTEM.WORD; addr : SYSTEM.ADDRESS;
addr := SYSTEM.ADR(word);

(* but type cast syntax can be used without such import *)
VAR i : INTEGER; n : CARDINAL;
n := CARDINAL(i); (* or *) i := INTEGER(n);
```

The ISO Modula-2 standard corrected this for the type cast facility by changing the type cast syntax into a function called CAST which has to be imported from pseudo-module SYSTEM. However, other unsafe facilities such as variant records remained available without any import from pseudo-module SYSTEM.

```mw
IMPORT SYSTEM;
VAR i : INTEGER; n : CARDINAL;
i := SYSTEM.CAST(INTEGER, n); (* Type cast in ISO Modula-2 *)
```

A recent revision of the language applied the original design philosophy rigorously. First, pseudo-module SYSTEM was renamed to UNSAFE to make the unsafe nature of facilities imported from there more explicit. Then all remaining unsafe facilities where either removed altogether (for example variant records) or moved to pseudo-module UNSAFE. For facilities where there is no identifier that could be imported, enabling identifiers were introduced. In order to enable such a facility, its corresponding enabling identifier must be imported from pseudo-module UNSAFE. No unsafe facilities remain in the language that do not require import from UNSAFE.

```mw
IMPORT UNSAFE;
VAR i : INTEGER; n : CARDINAL;
i := UNSAFE.CAST(INTEGER, n); (* Type cast in Modula-2 Revision 2010 *)

FROM UNSAFE IMPORT FFI; (* enabling identifier for foreign function interface facility *)
<*FFI="C"*> (* pragma for foreign function interface to C *)
```

### Pascal

Pascal has had a number of type safety requirements, some of which are kept in some compilers. Where a Pascal compiler dictates "strict typing", two variables cannot be assigned to each other unless they are either compatible (such as conversion of integer to real) or assigned to the identical subtype. For example, if you have the following code fragment:

```mw
type
  TwoTypes = record
     I: Integer;
     Q: Real;
  end;

  DualTypes = record
    I: Integer;
    Q: Real;
  end;

var
  T1, T2:  TwoTypes;
  D1, D2:  DualTypes;
```

Under strict typing, a variable defined as TwoTypes is *not compatible* with DualTypes (because they are not identical, even though the components of that user defined type are identical) and an assignment of `T1 := D2;` is illegal. An assignment of `T1 := T2;` would be legal because the subtypes they are defined to *are* identical. However, an assignment such as `T1.Q := D1.Q;` would be legal.

### Common Lisp

In general, Common Lisp is a type-safe language. A Common Lisp compiler is responsible for inserting dynamic checks for operations whose type safety cannot be proven statically. However, a programmer may indicate that a program should be compiled with a lower level of dynamic type-checking. A program compiled in such a mode cannot be considered type-safe.

## C++ examples

The following examples illustrates how C++ cast operators can break type safety when used incorrectly. The first example shows how basic data types can be incorrectly cast:

```mw
#include <iostream>
using namespace std;

int main () {
    int   ival = 5;                              // integer value
    float fval = reinterpret_cast<float&>(ival); // reinterpret bit pattern
    cout << fval << endl;                        // output integer as float
    return 0;
}
```

In this example, `reinterpret_cast` explicitly prevents the compiler from performing a safe conversion from integer to floating-point value. When the program runs it will output a garbage floating-point value. The problem could have been avoided by instead writing `float fval = ival;`

The next example shows how object references can be incorrectly downcast:

```mw
#include <iostream>
using namespace std;

class Parent {
public:
    virtual ~Parent() {} // virtual destructor for RTTI
};

class Child1 : public Parent {
public:
    int a;
};

class Child2 : public Parent {
public:
    float b;
};

int main () {
    Child1 c1;
    c1.a = 5;
    Parent & p = c1;                     // upcast always safe
    Child2 & c2 = static_cast<Child2&>(p); // invalid downcast
    cout << c2.b << endl;          // will output garbage data
    return 0;
}
```

The two child classes have members of different types. When downcasting a parent class pointer to a child class pointer, then the resulting pointer may not point to a valid object of correct type. In the example, this leads to garbage value being printed. The problem could have been avoided by replacing `static_cast` with `dynamic_cast` that throws an exception on invalid casts.
