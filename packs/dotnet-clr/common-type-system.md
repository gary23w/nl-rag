---
title: "Common Type System"
source: https://en.wikipedia.org/wiki/Common_Type_System
domain: dotnet-clr
license: CC-BY-SA-4.0
tags: common language runtime, dotnet framework, common intermediate language, managed code
fetched: 2026-07-02
---

# Common Type System

In Microsoft's .NET Framework, the **Common Type System** (**CTS**) is a standard that specifies how type definitions and specific values of types are represented in computer memory. It is intended to allow programs written in different programming languages to easily share information. As used in programming languages, a type can be described as a definition of a set of values (for example, "all integers between 0 and 10"), and the allowable operations on those values (for example, addition and subtraction).

The specification for the CTS is contained in Ecma standard 335, "Common Language Infrastructure (CLI) Partitions I to VI." The CLI and the CTS were created by Microsoft, and the Microsoft .NET framework is an implementation of the standard.

## Functions of the Common Type System

- To establish a framework that helps enable cross-language integration, type safety, and high performance code execution.
- To provide an object-oriented model that supports the complete implementation of many programming languages.
- To define rules that languages must follow, which helps ensure that objects written in different languages can interact with each other.
- The CTS also defines the rules that ensures that the data types of objects written in various languages are able to interact with each other.
- The CTS also specifies the rules for type visibility and access to the members of a type, i.e. the CTS establishes the rules by which assemblies form scope for a type, and the Common Language Runtime enforces the visibility rules.
- The CTS defines the rules governing type inheritance, virtual methods and object lifetime.
- Languages supported by .NET can implement all or some common data types…

When rounding fractional values, the halfway-to-even ("banker's") method is used by default, throughout the Framework. Since version 2, "Symmetric Arithmetic Rounding" (round halves away from zero) is also available by programmer's option.

- it is used to communicate with other languages

## Type categories

The common type system supports two general categories of types:

**Value types**

Value types

directly contain their data, and instances of value types are either allocated on the

stack

or allocated inline in a structure. Value types can be built-in (implemented by the runtime), user-defined, or enumerations.

**Reference types**

Reference types

store a reference to the value's memory address, and are allocated on the

heap

. Reference types can be self-describing types, pointer types, or interface types. The type of a reference type can be determined from values of self-describing types. Self-describing types are further split into arrays and class types. The class types are user-defined classes, boxed value types, and delegates.

The following example written in Visual Basic .NET shows the difference between reference types and value types:

```mw
Imports System

Class Class1
    Public Value As Integer = 0
End Class 'Class1
 
Class Test
    Shared Sub Main()
        Dim val1 As Integer = 0
        Dim val2 As Integer = val1
        val2 = 123
        Dim ref1 As New Class1()
        Dim ref2 As Class1 = ref1
        ref2.Value = 123
        Console.WriteLine("Values: {0}, {1}", val1, val2)
        Console.WriteLine("Refs: {0}, {1}", ref1.Value, ref2.Value)
    End Sub 'Main
End Class 'Test
```

The output of the above example

```
Values: 0, 123
Refs: 123, 123
```

### Boxing and unboxing

### Boxing

Converting value types to reference types is also known as boxing. As can be seen in the example below, it is not necessary to tell the compiler an Int32 is boxed to an object, because it takes care of this itself.

```mw
Int32 x = 10; 
object o = x ; // Implicit boxing
Console.WriteLine("The Object o = {0}",o); // prints out "The Object o = 10"
```

However, an Int32 can always be explicitly boxed like this:

```mw
Int32 x = 10; 
object o = (object) x; // Explicit boxing
Console.WriteLine("The object o = {0}",o); // prints out "The object o = 10"
```

### Unboxing

The following example intends to show how to unbox a reference type back to a value type. First an Int32 is boxed to an object, and then it is unboxed again. Note that unboxing requires explicit cast.

```mw
Int32 x = 5; 
object o1 = x; // Implicit Boxing
x = (int)o1; // Explicit Unboxing
```
