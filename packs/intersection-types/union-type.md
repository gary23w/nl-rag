---
title: "Union type"
source: https://en.wikipedia.org/wiki/Union_type
domain: intersection-types
license: CC-BY-SA-4.0
tags: intersection type, union type, type intersection, principal typing
fetched: 2026-07-02
---

# Union type

In computer science, a **union** is a value that may have any of multiple representations or formats within the same area of memory, or a variable that may hold such a data structure. Some programming languages support a **union type** for such a data type. In other words, a union type specifies the permitted types that may be stored in its instances, e.g., `float` and `int`. In contrast with a record, which could be defined to contain both a float *and* an integer, a union can hold only one at a time.

A union can be pictured as a chunk of memory that is used to store variables of different data types. Once a new value is assigned to a field, the existing data is overwritten with the new data. The memory area storing the value has no intrinsic type (other than just bytes or words of memory), but the value can be treated as one of several abstract data types, having the type of the value that was last written to the memory area.

In type theory, a union has a sum type; this corresponds to disjoint union in mathematics.

Depending on the language and type, a union value may be used in some operations, such as assignment and comparison for equality, without knowing its specific type. Other operations may require that knowledge, either by some external information, or by the use of a tagged union.

## Untagged unions

Because of the limitations of their use, untagged unions are generally only provided in untyped languages or in a type-unsafe way (as in C). They have the advantage over simple tagged unions of not requiring space to store a data type tag.

The name "union" stems from the type's formal definition. If a type is considered as the set of all values that that type can take on, a union type is simply the mathematical union of its constituting types, since it can take on any value any of its fields can. Also, because a mathematical union discards duplicates, if more than one field of the union can take on a single common value, it is impossible to tell from the value alone which field was last written.

However, one useful programming function of unions is to map smaller data elements to larger ones for easier manipulation. A data structure consisting, for example, of 4 bytes and a 32-bit integer, can form a union with an unsigned 64-bit integer, and thus be more readily accessed for purposes of comparison etc.

## Unions in various programming languages

### ALGOL 68

ALGOL 68 has tagged unions, and uses a case clause to distinguish and extract the constituent type at runtime. A union containing another union is treated as the set of all its constituent possibilities, and if the context requires it a union is automatically coerced into the wider union. A union can explicitly contain no value, which can be distinguished at runtime. An example is:

```
 mode node = union (real, int, string, void);
 
 node n := "abc";
 
 case n in
   (real r):   print(("real:", r)),
   (int i):    print(("int:", i)),
   (string s): print(("string:", s)),
   (void):     print(("void:", "EMPTY")),
   out         print(("?:", n))
 esac
```

The syntax of the C/C++ union type and the notion of casts was derived from ALGOL 68, though in an untagged form.

### C/C++

In C and C++, untagged unions are expressed nearly exactly like structures (structs), except that each data member is located at the same memory address. The data members, as in structures, need not be primitive values, and in fact may be structures or even other unions. C++ (since C++11) also allows for a data member to be any type that has a full-fledged constructor/destructor and/or copy constructor, or a non-trivial copy assignment operator. For example, it is possible to have the standard C++ string as a member of a union.

The primary use of a union is allowing access to a common location by different data types, for example hardware input/output access, bitfield and word sharing, or type punning. Unions can also provide low-level polymorphism. However, there is no checking of types, so it is up to the programmer to be sure that the proper fields are accessed in different contexts. The relevant field of a union variable is typically determined by the state of other variables, possibly in an enclosing struct.

One common C programming idiom uses unions to perform what C++ calls a `reinterpret_cast`, by assigning to one field of a union and reading from another, as is done in code which depends on the raw representation of the values. A practical example is the method of computing square roots using the IEEE representation. This is not, however, a safe use of unions in general.

> Structure and union specifiers have the same form. [ . . . ] The size of a union is sufficient to contain the largest of its members. The value of at most one of the members can be stored in a union object at any time. A pointer to a union object, suitably converted, points to each of its members (or if a member is a bit-field, then to the unit in which it resides), and vice versa.

— ANSI/ISO 9899:1990 (the ANSI C standard) Section 6.5.2.1

#### Anonymous union

In C++, C11, and as a non-standard extension in many compilers, unions can also be anonymous. Their data members do not need to be referenced, are instead accessed directly. They have some restrictions as opposed to traditional unions: in C11, they must be a member of another structure or union, and in C++, they can not have methods or access specifiers.

Simply omitting the class-name portion of the syntax does not make a union an anonymous union. For a union to qualify as an anonymous union, the declaration must not declare an object. Example:

```mw
union {
    float f;
    uint32_t d; // Assumes float is 32 bits wide
};

f = 3.14f;
printf("Hexadecimal representation of 3.14f: %x\n", u.d);
```

Anonymous unions are also useful in C `struct` definitions to provide a sense of namespacing.

#### Transparent union

In compilers such as GCC, Clang, and IBM XL C for AIX, a `transparent_union` attribute is available for union types. Types contained in the union can be converted transparently to the union type itself in a function call, provided that all types have the same size. It is mainly intended for function with multiple parameter interfaces, a use necessitated by early Unix extensions and later re-standardisation.

### COBOL

In COBOL, union data items are defined in two ways. The first uses the RENAMES (66 level) keyword, which effectively maps a second alphanumeric data item on top of the same memory location as a preceding data item. In the example code below, data item PERSON-REC is defined as a group containing another group and a numeric data item. PERSON-DATA is defined as an alphanumeric data item that renames PERSON-REC, treating the data bytes continued within it as character data.

```mw
  01  PERSON-REC.
      05  PERSON-NAME.
          10  PERSON-NAME-LAST    PIC X(12).
          10  PERSON-NAME-FIRST   PIC X(16).
          10  PERSON-NAME-MID     PIC X.
      05  PERSON-ID               PIC 9(9) PACKED-DECIMAL.
  
  01  PERSON-DATA                 RENAMES PERSON-REC.
```

The second way to define a union type is by using the REDEFINES keyword. In the example code below, data item VERS-NUM is defined as a 2-byte binary integer containing a version number. A second data item VERS-BYTES is defined as a two-character alphanumeric variable. Since the second item is *redefined* over the first item, the two items share the same address in memory, and therefore share the same underlying data bytes. The first item interprets the two data bytes as a binary value, while the second item interprets the bytes as character values.

```mw
  01  VERS-INFO.
      05  VERS-NUM        PIC S9(4) COMP.
      05  VERS-BYTES      PIC X(2)
                          REDEFINES VERS-NUM
```

### Pascal

In Pascal, there are two ways to create unions. One is the standard way through a variant record. The second is a nonstandard means of declaring a variable as absolute, meaning it is placed at the same memory location as another variable or at an absolute address. While all Pascal compilers support variant records, only some support absolute variables.

For the purposes of this example, the following are all integer types: a **byte** consists of 8 bits, a **word** is 16 bits, and an **integer** is 32 bits.

The following example shows the non-standard absolute form:

```mw
var
    A: Integer;
    B: array[1..4] of Byte absolute A;
    C: Integer absolute 0;
```

In the first example, each of the elements of the array B maps to one of the specific bytes of the variable A. In the second example, the variable C is assigned to the exact machine address 0.

In the following example, a record has variants, some of which share the same location as others:

```mw
type
     Shape = (Circle, Square, Triangle);
     Dimensions = record
        case Figure: Shape of 
           Circle: (Diameter: real);
           Square: (Width: real);
           Triangle: (Side: real; Angle1, Angle2: 0..360)
        end;
```

### PL/I

In PL/I the original term for a union was *cell*, which is still accepted as a synonym for union by several compilers. The union declaration is similar to the structure definition, where elements at the same level within the union declaration occupy the same storage. Elements of the union can be any data type, including structures and array. Here vers_num and vers_bytes occupy the same storage locations.

```mw
  1  vers_info         union,
     5 vers_num        fixed binary,
     5 vers_bytes      pic '(2)A';
```

An alternative to a union declaration is the DEFINED attribute, which allows alternative declarations of storage, however the data types of the base and defined variables must match.

### Rust

Rust implements both tagged and untagged unions. In Rust, tagged unions are implemented using the `enum` keyword. Unlike enumerated types in most other languages, enum variants in Rust can contain additional data in the form of a tuple or struct, making them tagged unions rather than simple enumerated types.

Rust also supports untagged unions using the `union` keyword. The memory layout of unions in Rust is undefined by default, but a union with the `#[repr(C)]` attribute will be laid out in memory exactly like the equivalent union in C. Reading the fields of a union can only be done within an `unsafe` function or block, as the compiler cannot guarantee that the data in the union will be valid for the type of the field; if this is not the case, it will result in undefined behavior.

## Syntax and example

### C

In C, the syntax is:

```mw
union <name> {
    <datatype>  <1st variable name>;
    <datatype>  <2nd variable name>;
    .
    .
    .
    <datatype>  <nth variable name>;
} <union variable name>;
```

A structure can also be a member of a union, as the following example shows:

```mw
union {
    struct {  
        int a;
        float b;
        char c;
    } svar;
    int d;
} uvar;
```

This example defines a variable `uvar` as a union which contains two members, a structure named `svar` (which in turn contains three members), and an integer variable named `d`.

Unions may occur within structures and arrays, and vice versa:

```mw
#define N 10000

struct {  
    int flags;
    char *name;
    int utype;
    union {
        int ival;
        float fval;
        char *sval;
    } u;
} symtab[N];
```

The number `ival` is referred to by `symtab[i].u.ival` and the string `sval` by `symtab[i].u.sval`.

### C++

C++ supports unions like C, but they are difficult to use safely in C++. For the two main purposes of unions, idiomatic C++ has alternatives:

1. Type punning via unions like `union { uint32_t x; float y; }` to map from a floating-point value to its binary representation as an integer can be done with `reinterpret_cast`.
2. For non-POD types, unions require explicit construction and destruction, making them cumbersome to use safely. `std::variant`, introduced in C++17, acts as a tagged union, avoiding this complication.

```mw
#include <cmath>
#include <cstdint>
#include <stdexcept>
#include <variant>

uint32_t encode_float_as_binary(float f) noexcept {
	return reinterpret_cast<uint32_t&>(f);
}

bool is_integral(std::variant<int, float>& v) {
	if (int* _ = std::get_if<int>(&v)) {
		return true;
	} else if (float* f = std::get_if<float>(&v)) {
		return std::modff(*f, nullptr) == 0;
	}
	throw std::invalid_argument("Invalid variant input!");
}
```

### C

Until C# 15, there were no union types in C#. The closest way to emulate them was through records and pattern matching.

```mw
namespace Wikipedia.Examples;

using System;

abstract record Shape;
record Circle(double Radius) : Shape;
record Rectangle(double Width, double Height) : Shape;

public class Example
{
    public static double Area(Shape s) => s switch
    {
        Circle c => Math.PI * c.Radius * c.Radius,
        Rectangle r => r.Width * r.Height,
        _ => throw new NotSupportedException()
    };
}
```

They could also be closely simulated using low-level layout. The following demonstrates such a union, where the fields occupy the same memory, but is not type-safe. It is best used for interoperability, serialization, and unsafe manipulation.

```mw
using System.Runtime.InteropServices;

// closest to C union IntFloatUnion { int i; float f; };
[StructLayout(LayoutKind.Explicit)]
struct IntFloatUnion
{
    [FieldOffset(0)]
    public int IntValue;

    [FieldOffset(0)]
    public float FloatValue;
}
```

In C# 15, unions were introduced to the language, as can be demonstrated by the following:

```mw
public record class Car(string Model);
public record class Bicycle(string Model);
public record class Bus(string Model);

public union Vehicle(Car, Bicycle, Bus);

Vehicle car = new Car("Tesla Model 3");
Console.WriteLine(car.Value); // Car { Model = Tesla Model 3 }

Vehicle bike = new Bicycle("Giant Escape 3");
Console.WriteLine(bike.Value); // Bicycle { Model = Giant Escape 3 }

Vehicle bus = new Bus("Volvo 9700");
Console.WriteLine(bus.Value); // Bus { Model = Volvo 9700 }

Vehicle v = /* some vehicle here */;
string model = v switch
{
    Car c => c.Model,
    Bicycle bk => b.Model,
    Bus bs => bs.Model,
};
```

The `default` value of a union is `null`, but if all types in the union are non-nullable, then a `switch` expression need not check for `null`.

### Java

Union types do not exist in Java, although they can be somewhat emulated using interfaces.

```mw
// "Shape" can be thought of as a union of "Circle", "Rectangle",
// and other types that implement "Shape"
// we can explicitly restrict what is in the union using a sealed interface
sealed interface Shape permits Circle, Rectangle {}

record Circle(double radius) implements Shape {}

record Rectangle(double width, double height) implements Shape {}

class Example {
    double area(Shape s) {
        return switch (s) {
            case Circle(double r) -> Math.PI * r * r;
            case Rectangle(double w, double h) -> w * h;
        };
    }
}
```

A `catch` clause can declare a union of multiple exception types. This syntax resembles union type syntax in other languages, but does not actually introduce a new type. The effective type of the exception parameter is the most specific common supertype of the alternatives. The catch clause only catches exceptions of the declared types, no other subclasses of the common supertype.

```mw
class FooException extends RuntimeException {
    String name() {
        return "Foo";
    }
}

class BarException extends RuntimeException {
    String name() {
        return "Bar";
    }
}

void main() {
    try {
        throw Math.random() < 0.5 ? new FooException() : new BarException();
    } catch (FooException | BarException e) {
        // e has type RuntimeException, the common supertype of FooException and BarException
        System.out.println(e);
        e.printStackTrace();
        // System.out.println(e.name());
        // Because there is no name() method in RuntimeException, this fails to compile
    }
}
```

### PHP

Union types were introduced in PHP 8.0. The values are implicitly "tagged" with a type by the language, and may be retrieved by "gettype()".

```mw
class Example
{
    private int|float $foo;

    public function squareAndAdd(float|int $bar): int|float
    {
        return $bar ** 2 + $this->foo;
    }
}
```

### Python

Support for typing was introduced in Python 3.5. The new syntax for union types were introduced in Python 3.10.

```mw
from typing import Union

class Example:
    foo: int = 0

    # old style:
    def square_and_add(self, bar: Union[int, float]) -> Union[int, float]:
        return bar ** 2 + self.foo

    # new style:
    def square_and_add(self, bar: int | float) -> int | float:
        return bar ** 2 + self.foo
```

### TypeScript

Union types are supported in TypeScript. The values are implicitly "tagged" with a type by the language, and may be retrieved using a `typeof` call for primitive values and an `instanceof` comparison for complex data types. Types with overlapping usage (e.g. a slice method exists on both strings and arrays, the plus operator works on both strings and numbers) don't need additional narrowing to use these features.

```mw
function successor(n: number | bigint): number | bigint {
    // types that support the same operations don't need narrowing
    return ++n;
}

function dependsOnParameter(v: string | string[] | number) {
    // distinct types need narrowing
    if (v instanceof Array) {
        // do something
    } else if (typeof(v) === "string") {
        // do something else
    } else {
        // has to be a number
    }
}
```

### Rust

Tagged unions in Rust use the `enum` keyword, and can contain tuple and struct variants:

```mw
enum Foo {
	Bar(i32),
	Baz { x: String, y: i32 },
}
```

Untagged unions in Rust use the `union` keyword:

```mw
union Foo {
	bar: i32,
	baz: bool,
}
```

Reading from the fields of an untagged union results in undefined behavior if the data in the union is not valid as the type of the field, and thus requires an `unsafe` block:

```mw
let x = Foo { bar: 10 };
let y = unsafe { x.bar }; // This will set y to 10, and does not result in undefined behavior.
let z = unsafe { x.baz }; // This results in undefined behavior, as the value stored in x is not a valid bool.
```
