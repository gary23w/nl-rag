---
title: "Factory method pattern"
source: https://en.wikipedia.org/wiki/Factory_method_pattern
domain: factory-boy
license: CC-BY-SA-4.0
tags: python factory boy, factory boy fixtures, test object factory python
fetched: 2026-07-02
---

# Factory method pattern

In object-oriented programming, the **factory method pattern** is a design pattern that uses factory methods to deal with the problem of creating objects without having to specify their exact classes. Rather than by calling a constructor, this is accomplished by invoking a factory method to create an object. Factory methods can be specified in an interface and implemented by subclasses or implemented in a base class and optionally overridden by subclasses. It is one of the 23 classic design patterns described in the book *Design Patterns* and is subcategorized as a creational pattern.

## Overview

The factory method design pattern solves problems such as:

- How can an object's subclasses redefine its subsequent and distinct implementation? The pattern involves creation of a factory method within the superclass that defers the object's creation to a subclass's factory method.
- How can an object's instantiation be deferred to a subclass? Create an object by calling a factory method instead of directly calling a constructor.

This enables the creation of subclasses that can change the way in which an object is created (for example, by redefining which class to instantiate).

## Definition

According to *Design Patterns: Elements of Reusable Object-Oriented Software*: "Define an interface for creating an object, but let subclasses decide which class to instantiate. Factory method lets a class defer instantiation to subclasses."

Creating an object often requires complex processes not appropriate to include within a composing object. The object's creation may lead to a significant duplication of code, may require information inaccessible to the composing object, may not provide a sufficient level of abstraction or may otherwise not be included in the composing object's concerns. The factory method design pattern handles these problems by defining a separate method for creating the objects, which subclasses can then override to specify the derived type of product that will be created.

The factory method pattern relies on inheritance, as object creation is delegated to subclasses that implement the factory method to create objects. The pattern can also rely on the implementation of an interface.

## Structure

### UML class diagram

In the above UML class diagram, the `Creator` class that requires a `Product` object does not instantiate the `Product1` class directly. Instead, the `Creator` refers to a separate `factoryMethod()` to create a product object, which makes the `Creator` independent of the exact concrete class that is instantiated. Subclasses of `Creator` can redefine which class to instantiate. In this example, the `Creator1` subclass implements the abstract `factoryMethod()` by instantiating the `Product1` class.

## Examples

### Structure

A maze game may be played in two modes, one with regular rooms that are only connected with adjacent rooms, and one with magic rooms that allow players to be transported at random.

`Room` is the base class for a final product (`MagicRoom` or `OrdinaryRoom`). `MazeGame` declares the abstract factory method to produce such a base product. `MagicRoom` and `OrdinaryRoom` are subclasses of the base product implementing the final product. `MagicMazeGame` and `OrdinaryMazeGame` are subclasses of `MazeGame` implementing the factory method producing the final products. Factory methods thus decouple callers (`MazeGame`) from the implementation of the concrete classes. This makes the `new` operator redundant, allows adherence to the open–closed principle and makes the final product more flexible in the event of change.

### Example implementations

#### C++

This C++23 implementation is based on the pre C++98 implementation in the *Design Patterns* book.

```mw
import std;

using std::unique_ptr;

enum class ProductId: char {
    MINE, 
    YOURS
};

// defines the interface of objects the factory method creates.
class Product {
public:
    virtual void print() = 0;
    virtual ~Product() = default;
};

// implements the Product interface.
class ConcreteProductMINE: public Product {
public:
    void print() {
        std::println("this={} print MINE", this);
    }
};

// implements the Product interface.
class ConcreteProductYOURS: public Product {
public:
    void print() {
        std::println("this={} print YOURS", this);
    }
};

// declares the factory method, which returns an object of type Product.
class Creator {
public:
    virtual unique_ptr<Product> create(ProductId id) {
        switch (id) {
            case ProductId::MINE:
                return std::make_unique<ConcreteProductMINE>();
            case ProductId::YOURS:
                return std::make_unique<ConcreteProductYOURS>();
            // repeat for remaining products
            default:
                return nullptr;
        }
    }

    virtual ~Creator() = default;
};

int main(int argc, char* argv[]) {
    unique_ptr<Creator> creator = std::make_unique<Creator>();
    unique_ptr<Product> product = creator->create(ProductId::MINE);
    product->print();

    product = creator->create(ProductId::YOURS);
    product->print();
}
```

The program output is like

```mw
this=0x6e5e90 print MINE
this=0x6e62c0 print YOURS
```

#### C

```mw
// Empty vocabulary of actual object
public interface IPerson
{
    string GetName();
}

public class Villager : IPerson
{
    public string GetName()
    {
        return "Village Person";
    }
}

public class CityPerson : IPerson
{
    public string GetName()
    {
        return "City Person";
    }
}

public enum PersonType
{
    Rural,
    Urban
}

/// <summary>
/// Implementation of Factory - Used to create objects.
/// </summary>
public class PersonFactory
{
    public IPerson GetPerson(PersonType type)
    {
        switch (type)
        {
            case PersonType.Rural:
                return new Villager();
            case PersonType.Urban:
                return new CityPerson();
            default:
                throw new NotSupportedException();
        }
    }
}
```

The above code depicts the creation of an interface called `IPerson` and two implementations called `Villager` and `CityPerson`. Based on the type passed to the `PersonFactory` object, the original concrete object is returned as the interface `IPerson`.

A factory method is just an addition to the `PersonFactory` class. It creates the object of the class through interfaces but also allows the subclass to decide which class is instantiated.

```mw
public interface IProduct
{
    string GetName();
    bool SetPrice(double price);
}

public class Phone : IProduct
{
    private double _price;

    public string GetName()
    {
        return "Apple TouchPad";
    }

    public bool SetPrice(double price)
    {
        _price = price;
        return true;
    }
}

/* Almost same as Factory, just an additional exposure to do something with the created method */
public abstract class ProductAbstractFactory
{
    protected abstract IProduct MakeProduct();

    public IProduct GetObject() // Implementation of Factory Method.
    {
        return this.MakeProduct();
    }
}

public class PhoneConcreteFactory : ProductAbstractFactory
{
    protected override IProduct MakeProduct()
    {
        IProduct product = new Phone();
        // Do something with the object after receiving it
        product.SetPrice(20.30);
        return product;
    }
}
```

In this example, `MakeProduct` is used in `concreteFactory`. As a result, `MakeProduct()` may be invoked in order to retrieve it from the `IProduct`. Custom logic could run after the object is obtained in the concrete factory method. `GetObject` is made abstract in the factory interface.

#### Java

This Java example is similar to one in the book *Design Patterns.*

The `MazeGame` uses `Room` but delegates the responsibility of creating `Room` objects to its subclasses that create the concrete classes. The regular game mode could use this template method:

```mw
public abstract class Room {
    abstract void connect(Room room);
}

public class MagicRoom extends Room {
    public void connect(Room room) {}
}

public class OrdinaryRoom extends Room {
    public void connect(Room room) {}
}

public abstract class MazeGame {
     private final List<Room> rooms = new ArrayList<>();

     public MazeGame() {
          Room room1 = makeRoom();
          Room room2 = makeRoom();
          room1.connect(room2);
          rooms.add(room1);
          rooms.add(room2);
     }

     abstract protected Room makeRoom();
}
```

The `MazeGame` constructor is a template method that adds some common logic. It refers to the `makeRoom()` factory method that encapsulates the creation of rooms such that other rooms can be used in a subclass. To implement the other game mode that has magic rooms, the `makeRoom` method may be overridden:

```mw
public class MagicMazeGame extends MazeGame {
    @Override
    protected MagicRoom makeRoom() {
        return new MagicRoom();
    }
}

public class OrdinaryMazeGame extends MazeGame {
    @Override
    protected OrdinaryRoom makeRoom() {
        return new OrdinaryRoom();
    }
}

MazeGame ordinaryGame = new OrdinaryMazeGame();
MazeGame magicGame = new MagicMazeGame();
```

#### PHP

This PHP example shows interface implementations instead of subclassing (however, the same can be achieved through subclassing). The factory method can also be defined as `public`and called directly by the client code (in contrast to the previous Java example).

```mw
/* Factory and car interfaces */

interface CarFactory
{
    public function makeCar(): Car;
}

interface Car
{
    public function getType(): string;
}

/* Concrete implementations of the factory and car */

class SedanFactory implements CarFactory
{
    public function makeCar(): Car
    {
        return new Sedan();
    }
}

class Sedan implements Car
{
    public function getType(): string
    {
        return 'Sedan';
    }
}

/* Client */

$factory = new SedanFactory();
$car = $factory->makeCar();
print $car->getType();
```

#### Python

This Python example employs the same as did the previous Java example.

```mw
from abc import ABC, abstractmethod

class MazeGame(ABC):
    def __init__(self) -> None:
        self.rooms = []
        self._prepare_rooms()

    def _prepare_rooms(self) -> None:
        room1 = self.make_room()
        room2 = self.make_room()

        room1.connect(room2)
        self.rooms.append(room1)
        self.rooms.append(room2)

    def play(self) -> None:
        print(f"Playing using {self.rooms[0]}")

    @abstractmethod
    def make_room(self):
        raise NotImplementedError("You should implement this!")

class MagicMazeGame(MazeGame):
    def make_room(self) -> "MagicRoom":
        return MagicRoom()

class OrdinaryMazeGame(MazeGame):
    def make_room(self) -> "OrdinaryRoom":
        return OrdinaryRoom()

class Room(ABC):
    def __init__(self) -> None:
        self.connected_rooms = []

    def connect(self, room: "Room") -> None:
        self.connected_rooms.append(room)

class MagicRoom(Room):
    def __str__(self) -> str:
        return "Magic room"

class OrdinaryRoom(Room):
    def __str__(self) -> str:
        return "Ordinary room"

ordinaryGame = OrdinaryMazeGame()
ordinaryGame.play()

magicGame = MagicMazeGame()
magicGame.play()
```

## Uses

- In ADO.NET, IDbCommand.CreateParameter is an example of the use of factory method to connect parallel class hierarchies.
- In Qt, QMainWindow::createPopupMenu Archived 2015-07-19 at the Wayback Machine is a factory method declared in a framework that can be overridden in application code.
- In Java, several factories are used in the javax.xml.parsers package, such as javax.xml.parsers.DocumentBuilderFactory or javax.xml.parsers.SAXParserFactory.
- In the HTML5 DOM API, the Document interface contains a createElement() factory method for creating specific elements of the HTMLElement interface.
