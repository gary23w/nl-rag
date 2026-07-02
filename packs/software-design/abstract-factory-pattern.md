---
title: "Abstract factory pattern"
source: https://en.wikipedia.org/wiki/Abstract_factory_pattern
domain: software-design
license: CC-BY-SA-4.0
tags: design pattern, software architecture, software design, refactoring
fetched: 2026-07-02
---

# Abstract factory pattern

The **abstract factory pattern** in software engineering is a design pattern that provides a way to create families of related objects without imposing their concrete classes, by encapsulating a group of individual factories that have a common theme without specifying their concrete classes. According to this pattern, a client software component creates a concrete implementation of the abstract factory and then uses the generic interface of the factory to create the concrete objects that are part of the family. The client does not know which concrete objects it receives from each of these internal factories, as it uses only the generic interfaces of their products. This pattern separates the details of implementation of a set of objects from their general usage and relies on object composition, as object creation is implemented in methods exposed in the factory interface.

Use of this pattern enables interchangeable concrete implementations without changing the code that uses them, even at runtime. However, employment of this pattern, as with similar design patterns, may result in unnecessary complexity and extra work in the initial writing of code. Additionally, higher levels of separation and abstraction can result in systems that are more difficult to debug and maintain.

## Overview

The abstract factory design pattern is one of the 23 patterns described in the 1994 *Design Patterns* book. It may be used to solve problems such as:

- How can an application be independent of how its objects are created?
- How can a class be independent of how the objects that it requires are created?
- How can families of related or dependent objects be created?

Creating objects directly within the class that requires the objects is inflexible. Doing so commits the class to particular objects and makes it impossible to change the instantiation later without changing the class. It prevents the class from being reusable if other objects are required, and it makes the class difficult to test because real objects cannot be replaced with mock objects.

A factory is the location of a concrete class in the code at which objects are constructed. Implementation of the pattern intends to insulate the creation of objects from their usage and to create families of related objects without depending on their concrete classes. This allows for new derived types to be introduced with no change to the code that uses the base class.

The pattern describes how to solve such problems:

- Encapsulate object creation in a separate (factory) object by defining and implementing an interface for creating objects.
- Delegate object creation to a factory object instead of creating objects directly.

This makes a class independent of how its objects are created. A class may be configured with a factory object, which it uses to create objects, and the factory object can be exchanged at runtime.

## Definition

*Design Patterns* describes the abstract factory pattern as "an interface for creating families of related or dependent objects without specifying their concrete classes."

## Usage

The factory determines the concrete type of object to be created, and it is here that the object is actually created. However, the factory only returns a reference (in Java, for instance, by the **new** operator) or a pointer of an abstract type to the created concrete object.

This insulates client code from object creation by having clients request that a factory object create an object of the desired abstract type and return an abstract pointer to the object.

An example is an abstract factory class `DocumentCreator` that provides interfaces to create a number of products (e.g., `createLetter()` and `createResume()`). The system would have any number of derived concrete versions of the `DocumentCreator` class such as`FancyDocumentCreator` or `ModernDocumentCreator`, each with a different implementation of `createLetter()` and `createResume()` that would create corresponding objects such as`FancyLetter` or `ModernResume`. Each of these products is derived from a simple abstract class such as`Letter` or `Resume` of which the client is aware. The client code would acquire an appropriate instance of the `DocumentCreator` and call its factory methods. Each of the resulting objects would be created from the same `DocumentCreator` implementation and would share a common theme. The client would only need to know how to handle the abstract `Letter` or `Resume` class, not the specific version that was created by the concrete factory.

As the factory only returns a reference or a pointer to an abstract type, the client code that requested the object from the factory is not aware of—and is not burdened by—the actual concrete type of the object that was created. However, the abstract factory knows the type of a concrete object (and hence a concrete factory). For instance, the factory may read the object's type from a configuration file. The client has no need to specify the type, as the type has already been specified in the configuration file. In particular, this means:

- The client code has no knowledge of the concrete type, not needing to include any header files or class declarations related to it. The client code deals only with the abstract type. Objects of a concrete type are indeed created by the factory, but the client code accesses such objects only through their abstract interfaces.
- Adding new concrete types is performed by modifying the client code to use a different factory, a modification that is typically one line in one file. The different factory then creates objects of a different concrete type but still returns a pointer of the *same* abstract type as before, thus insulating the client code from change. This is significantly easier than modifying the client code to instantiate a new type. Doing so would require changing every location in the code where a new object is created as well as ensuring that all such code locations have knowledge of the new concrete type, for example, by including a concrete class header file. If all factory objects are stored globally in a singleton object, and all client code passes through the singleton to access the proper factory for object creation, then changing factories is as easy as changing the singleton object.

## Structure

### UML diagram

A sample UML class and sequence diagram for the abstract factory design pattern.

In the above UML class diagram, the `Client` class that requires `ProductA` and `ProductB` objects does not instantiate the `ProductA1` and `ProductB1` classes directly. Instead, the `Client` refers to the `AbstractFactory` interface for creating objects, which makes the `Client` independent of how the objects are created (which concrete classes are instantiated). The `Factory1` class implements the `AbstractFactory` interface by instantiating the `ProductA1` and `ProductB1` classes.

The UML sequence diagram shows the runtime interactions. The `Client` object calls `createProductA()` on the `Factory1` object, which creates and returns a `ProductA1` object. Thereafter, the `Client` calls `createProductB()` on `Factory1`, which creates and returns a `ProductB1` object.

### Variants

The original structure of the abstract factory pattern, as defined in 1994 in *Design Patterns*, is based on abstract classes for the abstract factory and the abstract products to be created. The concrete factories and products are classes that specialize the abstract classes using inheritance.

A more recent structure of the pattern is based on interfaces that define the abstract factory and the abstract products to be created. This design uses native support for interfaces or protocols in mainstream programming languages to avoid inheritance. In this case, the concrete factories and products are classes that realize the interface by implementing it.

## Example

This C++23 implementation is based on the pre-C++98 implementation in the book.

```mw
import std;

using std::array;
using std::shared_ptr;
using std::unique_ptr;
using std::vector;

enum class Direction: char {
    NORTH, 
    SOUTH, 
    EAST, 
    WEST
};

class MapSite {
public:
    virtual void enter() = 0;
    virtual ~MapSite() = default;
};

class Room: public MapSite {
private:
    int roomNumber;
    shared_ptr<array<MapSite, 4>> sides;
public:
    explicit Room(int n = 0): 
        roomNumber{n} {}

    ~Room() = default;

    Room& setSide(Direction d, MapSite* ms) {
        sides[static_cast<size_t>(d)] = std::move(ms);
        std::println("Room::setSide {} ms", d);
        return *this;
    }

    virtual void enter() override = 0;

    Room(const Room&) = delete;
    Room& operator=(const Room&) = delete;
};

class Wall: public MapSite {
public:
    explicit Wall(int n = 0):
        MapSite(n) {}

    ~Wall() = default;

    void enter() override {
        // ...
    }
};

class Door: public MapSite {
private:
    shared_ptr<Room> room1;
    shared_ptr<Room> room2;
public:
    explicit Door(int n = 0, shared_ptr<Room> r1 = nullptr, shared_ptr<Room> r2 = nullptr): 
        MapSite(n), room1{std::move(r1)}, room2{std::move(r2)} {}

    ~Door() = default;

    void enter() override {
        // ...
    }

    Door(const Door&) = delete;
    Door& operator=(const Door&) = delete;
};

class Maze {
private:
    vector<shared_ptr<Room>> rooms;
public:
    Maze() = default;
    ~Maze() = default;

    Maze& addRoom(shared_ptr<Room> r) {
        std::println("Maze::addRoom {}", reinterpret_cast<void*>(r.get()));
        rooms.push_back(std::move(r));
        return *this;
    }
  
    shared_ptr<Room> roomNo(int n) const {
        for (const Room& r: rooms) {
            // actual lookup logic here...
        }
        return nullptr;
    }
};

class MazeFactory {
public:
    MazeFactory() = default;

    virtual ~MazeFactory() = default;

    [[nodiscard]]
    unique_ptr<Maze> makeMaze() const {
        return std::make_unique<Maze>();
    }

    [[nodiscard]]
    shared_ptr<Wall> makeWall() const {
        return std::make_shared<Wall>();
    }

    [[nodiscard]]
    shared_ptr<Room> makeRoom(int n) const {
        return std::make_shared<Room>(new Room(n));
    }
    
    [[nodiscard]]
    shared_ptr<Door> makeDoor(shared_ptr<Room> r1, shared_ptr<Room> r2) const {
        return std::make_shared<Door>(std::move(r1), std::move(r2));
    }
};

// If createMaze is passed an object as a parameter to use to create rooms, walls, and doors, then you can change the classes of rooms, walls, and doors by passing a different parameter. This is an example of the Abstract Factory (99) pattern.

class MazeGame {
public:
    Maze() = default;
    ~Maze() = default;

    [[nodiscard]]
    unique_ptr<Maze> createMaze(MazeFactory& factory) {
        unique_ptr<Maze> maze = factory.makeMaze();
        shared_ptr<Room> r1 = factory.makeRoom(1);
        shared_ptr<Room> r2 = factory.makeRoom(2);
        shared_ptr<Door> door = factory.makeDoor(r1, r2);
        maze->addRoom(r1)
            .addRoom(r2)
                .setSide(Direction::NORTH, factory.makeWall())
                .setSide(Direction::EAST, door)
                .setSide(Direction::SOUTH, factory.makeWall())
                .setSide(Direction::WEST, factory.makeWall())
                .setSide(Direction::NORTH, factory.makeWall())
                .setSide(Direction::EAST, factory.makeWall())
                .setSide(Direction::SOUTH, factory.makeWall())
                .setSide(Direction::WEST, door);
        return maze;
    }
};

int main(int argc, char* argv[]) {
    MazeGame game;
    unique_ptr<Maze> maze = game.createMaze(MazeFactory());
}
```

The program output is:

```mw
Maze::addRoom 0x1317ed0
Maze::addRoom 0x1317ef0
Room::setSide 0 0x1318340
Room::setSide 2 0x1317f10
Room::setSide 1 0x1318360
Room::setSide 3 0x1318380
Room::setSide 0 0x13183a0
Room::setSide 2 0x13183c0
Room::setSide 1 0x13183e0
Room::setSide 3 0x1317f10
```
