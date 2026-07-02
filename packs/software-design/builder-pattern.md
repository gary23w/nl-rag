---
title: "Builder pattern"
source: https://en.wikipedia.org/wiki/Builder_pattern
domain: software-design
license: CC-BY-SA-4.0
tags: design pattern, software architecture, software design, refactoring
fetched: 2026-07-02
---

# Builder pattern

The **builder pattern** is a design pattern that provides a flexible solution to various object creation problems in object-oriented programming. The builder pattern separates the construction of a complex object from its representation. It is one of the 23 classic design patterns described in the book *Design Patterns* and is sub-categorized as a creational pattern.

## Overview

The builder design pattern solves problems like:

- How can a class (the same construction process) create different representations of a complex object?
- How can a class that includes creating a complex object be simplified?

Creating and assembling the parts of a complex object directly within a class is inflexible. It commits the class to creating a particular representation of the complex object and makes it impossible to change the representation later independently from (without having to change) the class.

The builder design pattern describes how to solve such problems:

- Encapsulate creating and assembling the parts of a complex object in a separate `Builder` object.
- A class delegates object creation to a `Builder` object instead of creating the objects directly.

A class (the same construction process) can delegate to different `Builder` objects to create different representations of a complex object.

## Definition

The intent of the builder design pattern is to separate the construction of a complex object from its representation. By doing so, the same construction process can create different representations.

## Advantages

Advantages of the builder pattern include:

- Allows for variation in a product's internal representation.
- Encapsulates code for construction and representation.
- Provides control over the steps of the construction process.

## Disadvantages

Disadvantages of the builder pattern include:

- A distinct ConcreteBuilder must be created for each type of product.
- Builder classes must be mutable.
- May hamper/complicate dependency injection.
- In many null-safe languages, the builder pattern defers compile-time errors for unset fields to runtime.

## Structure

### UML class and sequence diagram

In the above UML class diagram, the `Director` class doesn't create and assemble the `ProductA1` and `ProductB1` objects directly. Instead, the `Director` refers to the `Builder` interface for building (creating and assembling) the parts of a complex object, which makes the `Director` independent of which concrete classes are instantiated (which representation is created). The `Builder1` class implements the `Builder` interface by creating and assembling the `ProductA1` and `ProductB1` objects. The UML sequence diagram shows the run-time interactions: The `Director` object calls `buildPartA()` on the `Builder1` object, which creates and assembles the `ProductA1` object. Thereafter, the `Director` calls `buildPartB()` on `Builder1`, which creates and assembles the `ProductB1` object.

### Class diagram

**Builder**

Abstract interface for creating objects (product).

**ConcreteBuilder**

Provides implementation for Builder. It is an

object able to construct other objects

. Constructs and assembles parts to build the objects.

## Examples

A C# example:

```mw
namespace Wikipedia.Examples;

/// <summary>
/// Represents a product created by the builder.
/// </summary>
public class Bicycle
{
    public Bicycle(string make, string model, string colour, int height)
    {
        Make = make;
        Model = model;
        Colour = colour;
        Height = height;
    }

    public string Make { get; set; }
    public string Model { get; set; }
    public int Height { get; set; }
    public string Colour { get; set; }
}

/// <summary>
/// The builder abstraction.
/// </summary>
public interface IBicycleBuilder
{
    Bicycle GetResult();

    string Colour { get; set; }
    int Height { get; set; }
}

/// <summary>
/// Concrete builder implementation.
/// </summary>
public class GTBuilder : IBicycleBuilder
{
    public Bicycle GetResult()
    {
        return Height == 29 ? new Bicycle("GT", "Avalanche", Colour, Height) : null;
    }

    public string Colour { get; set; }
    public int Height { get; set; }
}

/// <summary>
/// The director.
/// </summary>
public class MountainBikeBuildDirector
{
    private IBicycleBuilder _builder;

    public MountainBikeBuildDirector(IBicycleBuilder builder)
    {
        _builder = builder;
    }

    public void Construct()
    {
        _builder.Colour = "Red";
        _builder.Height = 29;
    }

    public Bicycle GetResult()
	{
		return this._builder.GetResult();
	}
}

public class Client
{
    public void DoSomethingWithBicycles()
    {
        MountainBikeBuildDirector director = new(new GTBuilder());
        // Director controls the stepwise creation of product and returns the result.
        director.Construct();
        Bicycle myMountainBike = director.GetResult();
    }
}
```

The Director assembles a bicycle instance in the example above, delegating the construction to a separate builder object that has been given to the Director by the Client.
