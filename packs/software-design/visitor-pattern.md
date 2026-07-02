---
title: "Visitor pattern"
source: https://en.wikipedia.org/wiki/Visitor_pattern
domain: software-design
license: CC-BY-SA-4.0
tags: design pattern, software architecture, software design, refactoring
fetched: 2026-07-02
---

# Visitor pattern

A **visitor pattern** is a software design pattern that separates the algorithm from the object structure. Because of this separation, new operations can be added to existing object structures without modifying the structures. It is one way to follow the open/closed principle in object-oriented programming and software engineering.

In essence, the visitor allows adding new virtual functions to a family of classes, without modifying the classes. Instead, a visitor class is created that implements all of the appropriate specializations of the virtual function. The visitor takes the instance reference as input, and implements the goal through double dispatch.

Programming languages with sum types and pattern matching obviate many of the benefits of the visitor pattern, as the visitor class is able to both easily branch on the type of the object and generate a compiler error if a new object type is defined which the visitor does not yet handle.

## Overview

The Visitor design pattern is one of the twenty-three *Gang of Four design patterns*.

### Problems the pattern can solve

- It should be possible to define a new operation for (some) classes of an object structure without changing the classes.

When new operations are needed frequently and the object structure consists of many unrelated classes, it's inflexible to add new subclasses each time a new operation is required because "distributing all these operations across the various node classes leads to a system that's hard to understand, maintain, and change."

### Solution described by the pattern

- Define a separate (visitor) object that implements an operation to be performed on elements of an object structure.
- Clients traverse the object structure and call a *dispatching operation accept (visitor)* on an element — that "dispatches" (delegates) the request to the "accepted visitor object". The visitor object then performs the operation on the element ("visits the element").

This makes it possible to create new operations independently from the classes of an object structure by adding new visitor objects.

See also the UML class and sequence diagram below.

## Definition

The Gang of Four defines the Visitor as:

> Represent[ing] an operation to be performed on elements of an object structure. Visitor lets you define a new operation without changing the classes of the elements on which it operates.

The nature of the Visitor makes it an ideal pattern to plug into public APIs, thus allowing its clients to perform operations on a class using a "visiting" class without having to modify the source.

## Advantages

Moving operations into visitor classes is beneficial when

- many unrelated operations on an object structure are required,
- the classes that make up the object structure are known and not expected to change,
- new operations need to be added frequently,
- an algorithm involves several classes of the object structure, but it is desired to manage it in one single location,
- an algorithm needs to work across several independent class hierarchies.

A drawback to this pattern, however, is that it makes extensions to the class hierarchy more difficult, as new classes typically require a new `visit` method to be added to each visitor.

## Application

Consider the design of a 2D computer-aided design (CAD) system. At its core, there are several types to represent basic geometric shapes like circles, lines, and arcs. The entities are ordered into layers, and at the top of the type hierarchy is the drawing, which is simply a list of layers, plus some added properties.

A fundamental operation on this type hierarchy is saving a drawing to the system's native file format. At first glance, it may seem desirable to add local save methods to all types in the hierarchy. But it can also be useful to save drawings to other file formats. Adding ever more methods for saving into many different file formats can complicate the original geometric data structure.

A naive way to solve this would be to maintain separate functions for each file format. Such a save function would take a drawing as input, traverse it, and encode into that specific file format. As this is done for each added different format, duplication between the functions accumulates. For example, saving a circle shape in a raster format requires very similar code no matter what specific raster form is used, and is different from other primitive shapes. The case for other primitive shapes like lines and polygons is similar. Thus, the code becomes a large outer loop traversing through the objects, with a large decision tree inside the loop querying the type of the object. Another problem with this approach is that it is very easy to miss a shape in one or more savers, or a new primitive shape is introduced, but the save routine is implemented only for one file type and not others, leading to code extension and maintenance problems. As the versions of the same file grows it becomes more complicated to maintain it.

Instead, the visitor pattern can be applied. It encodes the logical operation (i.e. save(image_tree)) on the whole hierarchy into one class (i.e. Saver) that implements the common methods for traversing the tree and describes virtual helper methods (i.e. save_circle, save_square, etc.) to be implemented for format specific behaviors. In the case of the CAD example, such format specific behaviors would be implemented by a subclass of Visitor (i.e. SaverPNG). As such, all duplication of type checks and traversal steps is removed. Additionally, the compiler now complains if a shape is omitted since it is now expected by the common base traversal/save function.

### Iteration loops

The visitor pattern may be used for iteration over container-like data structures just like Iterator pattern but with limited functionality. For example, iteration over a directory structure could be implemented by a function class instead of more conventional loop pattern. This would allow deriving various useful information from directories content by implementing a visitor functionality for every item while reusing the iteration code. It's widely employed in Smalltalk systems and can be found in C++ as well. A drawback of this approach, however, is that you can't break out of the loop easily or iterate concurrently (in parallel i.e. traversing two containers at the same time by a single `i` variable). The latter would require writing additional functionality for a visitor to support these features.

## Structure

### UML class and sequence diagram

In the UML class diagram above, the `ElementA` class doesn't implement a new operation directly. Instead, `ElementA` implements a *dispatching operation* `accept(visitor)` that "dispatches" (delegates) a request to the "accepted visitor object" (`visitor.visitElementA(this)`). The `Visitor1` class implements the operation (`visitElementA(e:ElementA)`). `ElementB` then implements `accept(visitor)` by dispatching to `visitor.visitElementB(this)`. The `Visitor1` class implements the operation (`visitElementB(e:ElementB)`).

The UML sequence diagram shows the run-time interactions: The `Client` object traverses the elements of an object structure (`ElementA,ElementB`) and calls `accept(visitor)` on each element. First, the `Client` calls `accept(visitor)` on `ElementA`, which calls `visitElementA(this)` on the accepted `visitor` object. The element itself (`this`) is passed to the `visitor` so that it can "visit" `ElementA` (call `operationA()`). Thereafter, the `Client` calls `accept(visitor)` on `ElementB`, which calls `visitElementB(this)` on the `visitor` that "visits" `ElementB` (calls `operationB()`).

### Class diagram

## Details

The visitor pattern requires a programming language that supports single dispatch, as common object-oriented languages (such as C++, Java, Smalltalk, Objective-C, Swift, JavaScript, Python and C#) do. Under this condition, consider two objects, each of some class type; one is termed the *element*, and the other is *visitor*.

### Objects

#### Visitor

The *visitor* declares a `visit` method, which takes the element as an argument, for each class of element. *Concrete visitors* are derived from the visitor class and implement these `visit` methods, each of which implements part of the algorithm operating on the object structure. The state of the algorithm is maintained locally by the concrete visitor class.

#### Element

The *element* declares an `accept` method to accept a visitor, taking the visitor as an argument. *Concrete elements*, derived from the element class, implement the `accept` method. In its simplest form, this is no more than a call to the visitor's `visit` method. Composite elements, which maintain a list of child objects, typically iterate over these, calling each child's `accept` method.

#### Client

The *client* creates the object structure, directly or indirectly, and instantiates the concrete visitors. When an operation is to be performed which is implemented using the Visitor pattern, it calls the `accept` method of the top-level element(s).

### Methods

#### Accept

When the `accept` method is called in the program, its implementation is chosen based on both the dynamic type of the element and the static type of the visitor. When the associated `visit` method is called, its implementation is chosen based on both the dynamic type of the visitor and the static type of the element, as known from within the implementation of the `accept` method, which is the same as the dynamic type of the element. (As a bonus, if the visitor can't handle an argument of the given element's type, then the compiler will catch the error.)

#### Visit

Thus, the implementation of the `visit` method is chosen based on both the dynamic type of the element and the dynamic type of the visitor. This effectively implements double dispatch. For languages whose object systems support multiple dispatch, not only single dispatch, such as Common Lisp or C# via the Dynamic Language Runtime (DLR), implementation of the visitor pattern is greatly simplified (a.k.a. Dynamic Visitor) by allowing use of simple function overloading to cover all the cases being visited. A dynamic visitor, provided it operates on public data only, conforms to the open/closed principle (since it does not modify extant structures) and to the single responsibility principle (since it implements the Visitor pattern in a separate component).

In this way, one algorithm can be written to traverse a graph of elements, and many different kinds of operations can be performed during that traversal by supplying different kinds of visitors to interact with the elements based on the dynamic types of both the elements and the visitors.

## Examples

### C

This example declares a separate `ExpressionPrintingVisitor` class that takes care of the printing. If the introduction of a new concrete visitor is desired, a new class will be created to implement the Visitor interface, and new implementations for the Visit methods will be provided. The existing classes (Literal and Addition) will remain unchanged.

```mw
namespace Wikipedia.Examples;

using System;

interface IVisitor
{
    void Visit(Literal literal);  
    void Visit(Addition addition);
}

class ExpressionPrintingVisitor : IVisitor
{
    public void Visit(Literal literal)
    {
        Console.WriteLine(literal.Value);
    }

    public void Visit(Addition addition)
    {
        double leftValue = addition.Left.GetValue();
        double rightValue = addition.Right.GetValue();
        double sum = addition.GetValue();
        Console.WriteLine($"{leftValue} + {rightValue} = {sum}");
    }
 }

abstract class Expression
{
    public abstract void Accept(IVisitor visitor);
   
    public abstract double GetValue();
}

class Literal : Expression
{
    public Literal(double value)
    {
        this.Value = value;
    }

    public double Value { get; set; }

    public override void Accept(IVisitor visitor)
    {
        visitor.Visit(this);
    }
 
    public override double GetValue()
    {
        return Value;
    }
}

class Addition : Expression
{
    public Addition(Expression left, Expression right)
    {
        Left = left;
        Right = right;
    }

    public Expression Left { get; set; }
    public Expression Right { get; set; }

    public override void Accept(IVisitor visitor)
    {
        Left.Accept(visitor);
        Right.Accept(visitor);
        visitor.Visit(this);
    }
  
    public override double GetValue()
    {
        return Left.GetValue() + Right.GetValue();
    }
}

public static class Program
{
    public static void Main(string[] args)
    {
        // Emulate 1 + 2 + 3
        Addition e = new(
            new Addition(
                new Literal(1),
                new Literal(2)
            ),
            new Literal(3)
        );

        ExpressionPrintingVisitor printingVisitor = new();
        e.Accept(printingVisitor);
        Console.ReadKey();
    }
}
```

### Smalltalk

In this case, it is the object's responsibility to know how to print itself on a stream. The visitor here is then the object, not the stream.

```mw
"There's no syntax for creating a class. Classes are created by sending messages to other classes."
WriteStream subclass: #ExpressionPrinter
    instanceVariableNames: ''
    classVariableNames: ''
    package: 'Wikipedia'.

ExpressionPrinter>>write: anObject
    "Delegates the action to the object. The object doesn't need to be of any special
    class; it only needs to be able to understand the message #putOn:"
    anObject putOn: self.
    ^ anObject.

Object subclass: #Expression
    instanceVariableNames: ''
    classVariableNames: ''
    package: 'Wikipedia'.

Expression subclass: #Literal
    instanceVariableNames: 'value'
    classVariableNames: ''
    package: 'Wikipedia'.

Literal class>>with: aValue
    "Class method for building an instance of the Literal class"
    ^ self new
        value: aValue;
        yourself.

Literal>>value: aValue
  "Setter for value"
  value := aValue.

Literal>>putOn: aStream
    "A Literal object knows how to print itself"
    aStream nextPutAll: value asString.

Expression subclass: #Addition
    instanceVariableNames: 'left right'
    classVariableNames: ''
    package: 'Wikipedia'.

Addition class>>left: a right: b
    "Class method for building an instance of the Addition class"
    ^ self new
        left: a;
        right: b;
        yourself.

Addition>>left: anExpression
    "Setter for left"
    left := anExpression.

Addition>>right: anExpression
    "Setter for right"
    right := anExpression.

Addition>>putOn: aStream
    "An Addition object knows how to print itself"
    aStream nextPut: $(.
    left putOn: aStream.
    aStream nextPut: $+.
    right putOn: aStream.
    aStream nextPut: $).

Object subclass: #Program
    instanceVariableNames: ''
    classVariableNames: ''
    package: 'Wikipedia'.

Program>>main
    | expression stream |
    expression := Addition
                    left: (Addition
                            left: (Literal with: 1)
                            right: (Literal with: 2))
                    right: (Literal with: 3).
    stream := ExpressionPrinter on: (String new: 100).
    stream write: expression.
    Transcript show: stream contents.
    Transcript flush.
```

### Go

Go does not support method overloading, so the visit methods need different names. A typical visitor interface might be

```mw
type Visitor interface {
	visitWheel(wheel Wheel) string
	visitEngine(engine Engine) string
	visitBody(body Body) string
	visitCar(car Car) string
}
```

### Java

The following example is in the language Java, and shows how the contents of a tree of nodes (in this case describing the components of a car) can be printed. Instead of creating `print` methods for each node subclass (`Wheel`, `Engine`, `Body`, and `Car`), one visitor class (`CarElementPrintVisitor`) performs the required printing action. Because different node subclasses require slightly different actions to print properly, `CarElementPrintVisitor` dispatches actions based on the class of the argument passed to its `visit` method. `CarElementDoVisitor`, which is analogous to a save operation for a different file format, does likewise.

#### Diagram

(UML diagram of the Visitor pattern example with Car Elements)
