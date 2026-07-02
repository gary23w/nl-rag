---
title: "Bridge pattern"
source: https://en.wikipedia.org/wiki/Bridge_pattern
domain: software-design
license: CC-BY-SA-4.0
tags: design pattern, software architecture, software design, refactoring
fetched: 2026-07-02
---

# Bridge pattern

The **bridge pattern** is a design pattern used in software engineering that is meant to *"decouple an abstraction from its implementation so that the two can vary independently"*, introduced by the Gang of Four. The *bridge* uses encapsulation, aggregation, and can use inheritance to separate responsibilities into different classes.

When a class varies often, the features of object-oriented programming become very useful because changes to a program's code can be made easily with minimal prior knowledge about the program. The bridge pattern is useful when both the class and what it does vary often. The class itself can be thought of as the *abstraction* and what the class can do as the *implementation*. The bridge pattern can also be thought of as two layers of abstraction.

When there is only one fixed implementation, this pattern is known as the Pimpl idiom in the C++ world.

The bridge pattern is often confused with the adapter pattern, and is often implemented using the object adapter pattern; e.g., in the Java code below.

Variant: The implementation can be decoupled even more by deferring the presence of the implementation to the point where the abstraction is utilized.

## Overview

The Bridge design pattern is one of the twenty-three well-known *GoF design patterns* that describe how to solve recurring design problems to design flexible and reusable object-oriented software, that is, objects that are easier to implement, change, test, and reuse.

What problems can the Bridge design pattern solve?

- An abstraction and its implementation should be defined and extended independently from each other.
- A compile-time binding between an abstraction and its implementation should be avoided so that an implementation can be selected at run-time.

When using subclassing, different subclasses implement an abstract class in different ways. But an implementation is bound to the abstraction at compile-time and cannot be changed at run-time.

What solution does the Bridge design pattern describe?

- Separate an abstraction (`Abstraction`) from its implementation (`Implementor`) by putting them in separate class hierarchies.
- Implement the `Abstraction` in terms of (by delegating to) an `Implementor` object.

This enables to configure an `Abstraction` with an `Implementor` object at run-time. See also the Unified Modeling Language class and sequence diagram below.

## Structure

### UML class and sequence diagram

In the above Unified Modeling Language class diagram, an abstraction (`Abstraction`) is not implemented as usual in a single inheritance hierarchy. Instead, there is one hierarchy for an abstraction (`Abstraction`) and a separate hierarchy for its implementation (`Implementor`), which makes the two independent from each other. The `Abstraction` interface (`operation()`) is implemented in terms of (by delegating to) the `Implementor` interface (`imp.operationImp()`). The UML sequence diagram shows the run-time interactions: The `Abstraction1` object delegates implementation to the `Implementor1` object (by calling `operationImp()` on `Implementor1`), which performs the operation and returns to `Abstraction1`.

### Class diagram

**Abstraction (abstract class)**

defines the abstract interface

maintains the Implementor reference.

**RefinedAbstraction (normal class)**

extends the interface defined by Abstraction

**Implementor (interface)**

defines the interface for implementation classes

**ConcreteImplementor (normal class)**

implements the Implementor interface

## Example

### C

Bridge pattern compose objects in tree structure. It decouples abstraction from implementation. Here abstraction represents the client from which the objects will be called. An example implemented in C# is given below

```mw
namespace Wikipedia.Examples;

using System;

// Helps in providing truly decoupled architecture
interface IBridge
{
    void Function1();
    void Function2();
}

class Bridge1 : IBridge
{
    public void Function1()
    {
        Console.WriteLine("Bridge1.Function1");
    }

    public void Function2()
    {
        Console.WriteLine("Bridge1.Function2");
    }
}

class Bridge2 : IBridge
{
    public void Function1()
    {
        Console.WriteLine("Bridge2.Function1");
    }

    public void Function2()
    {
        Console.WriteLine("Bridge2.Function2");
    }
}

interface IAbstractBridge
{
    void CallMethod1();
    void CallMethod2();
}

class AbstractBridge : IAbstractBridge
{
    public IBridge bridge;

    public AbstractBridge(IBridge bridge)
    {
        this.bridge = bridge;
    }

    public void CallMethod1()
    {
        this.bridge.Function1();
    }

    public void CallMethod2()
    {
        this.bridge.Function2();
    }
}
```

The Bridge classes are the Implementation that uses the same interface-oriented architecture to create objects. On the other hand, the abstraction takes an instance of the implementation class and runs its method. Thus, they are completely decoupled from one another.

### Crystal

```mw
abstract class DrawingAPI
  abstract def draw_circle(x : Float64, y : Float64, radius : Float64)
end

class DrawingAPI1 < DrawingAPI
  def draw_circle(x : Float, y : Float, radius : Float)
    "API1.circle at #{x}:#{y} - radius: #{radius}"
  end
end

class DrawingAPI2 < DrawingAPI
  def draw_circle(x : Float64, y : Float64, radius : Float64)
    "API2.circle at #{x}:#{y} - radius: #{radius}"
  end
end

abstract class Shape
  protected getter drawing_api : DrawingAPI

  def initialize(@drawing_api)
  end

  abstract def draw
  abstract def resize_by_percentage(percent : Float64)
end

class CircleShape < Shape
  getter x : Float64
  getter y : Float64
  getter radius : Float64

  def initialize(@x, @y, @radius, drawing_api : DrawingAPI)
    super(drawing_api)
  end

  def draw
    @drawing_api.draw_circle(@x, @y, @radius)
  end

  def resize_by_percentage(percent : Float64)
    @radius *= (1 + percent/100)
  end
end

class BridgePattern
  def self.test
    shapes = [] of Shape
    shapes << CircleShape.new(1.0, 2.0, 3.0, DrawingAPI1.new)
    shapes << CircleShape.new(5.0, 7.0, 11.0, DrawingAPI2.new)

    shapes.each do |shape|
      shape.resize_by_percentage(2.5)
      puts shape.draw
    end
  end
end

BridgePattern.test
```

Output

```
API1.circle at 1.0:2.0 - radius: 3.075
API2.circle at 5.0:7.0 - radius: 11.275
```

### C++

```mw
import std;

using std::string;
using std::vector;

class DrawingAPI {
public:
    virtual ~DrawingAPI() = default;
    virtual string drawCircle(float x, float y, float radius) const = 0;
};

class DrawingAPI01: public DrawingAPI {
public:
    [[nodiscard]]
    string drawCircle(float x, float y, float radius) const override {
        return std::format("API01.circle at {}:{} - radius: {}", x, y, radius); 
    }
};

class DrawingAPI02: public DrawingAPI {
public:
    [[nodiscard]]
    string drawCircle(float x, float y, float radius) const override {
        return std::format("API02.circle at {}:{} - radius: {}", x, y, radius);
    }
};

class Shape {
protected:
    const DrawingAPI& drawingApi;
public:
    Shape(const DrawingAPI& api):
        drawingApi{api} {}

    virtual ~Shape() = default;

    virtual string draw() const = 0;
    virtual float resizeByPercentage(const float percent) noexcept = 0;
};

class CircleShape: public Shape {
private:
    float x;
    float y;
    float radius;
public:    
    CircleShape(const DrawingAPI& api, float x, float y, float radius): 
        Shape(api), x{x}, y{y}, radius{radius} {}

    [[nodiscard]]
    string draw() const override {
        return drawingApi.drawCircle(x, y, radius);
    }

    [[nodiscard]]
    float resizeByPercentage(float percent) noexcept override {
        return radius *= (1.0f + percent / 100.0f);
    }
};

int main(int argc, char* argv[]) {
    const DrawingAPI01 api1;
    const DrawingAPI02 api2;
    vector<CircleShape> shapes { 
        CircleShape{api1, 1.0f, 2.0f, 3.0f}, 
        CircleShape{api2, 5.0f, 7.0f, 11.0f} 
    }; 

    for (CircleShape& shape: shapes) {
        shape.resizeByPercentage(2.5);
        std::println("{}", shape.draw());
    }

    return 0;
}
```

Output:

```
API01.circle at 1.000000:2.000000 - radius: 3.075000
API02.circle at 5.000000:7.000000 - radius: 11.275000
```

Code requires a C++23 capable compiler, e.g. on Ubuntu 26.06 LTS with g++-15 the following 2-step build is required:

```
g++-15 -std=c++23 -c -fmodules -fmodule-only -fsearch-include-path bits/std.cc
g++-15 -std=c++23 -fmodules -o program program.cpp
```

### Java

The following Java program defines a bank account that separates the account operations from the logging of these operations.

```mw
package org.wikipedia.examples;

// Logger has two implementations: info and warning
@FunctionalInterface
interface Logger {
    void log(String message);
    
    static Logger info() {
        return message -> System.out.printf("info: %s%n", message);
    }
    static Logger warning() {
        return message -> System.out.printf("warning: %s%n", message);
    }
}

abstract class AbstractAccount {
    private Logger logger = Logger.info();
    
    public void setLogger(Logger logger) {
        this.logger = logger;
    }
    
    // the logging part is delegated to the Logger implementation
    protected void operate(String message, boolean result) {
        logger.log(String.format("%s result %s", message, result));
    }
}

class SimpleAccount extends AbstractAccount {
    private int balance;
    
    public SimpleAccount(int balance) {
        this.balance = balance;
    }
    
    public boolean isBalanceLow() {
        return balance < 50;
    }
    
    public void withdraw(int amount) {
        boolean shouldPerform = balance >= amount;
        if (shouldPerform) {
            balance -= amount;
        }
        operate(String.format("withdraw %s", amount, shouldPerform));
    }
}

public class BridgeDemo {
    public static void main(String[] args) {
        SimpleAccount account = new SimpleAccount(100);
        account.withdraw(75);
        
        if (account.isBalanceLow()) {
            // you can also change the Logger implementation at runtime
            account.setLogger(Logger.warning());
        }
        
        account.withdraw(10);
        account.withdraw(100);
    }
}
```

It will output:

```
info: withdraw 75 result true
warning: withdraw 10 result true
warning: withdraw 100 result false
```

### PHP

```mw
interface DrawingAPI
{
    function drawCircle($x, $y, $radius);
}

class DrawingAPI1 implements DrawingAPI
{
    public function drawCircle($x, $y, $radius)
    {
        echo "API1.circle at $x:$y radius $radius.\n";
    }
}

class DrawingAPI2 implements DrawingAPI
{
    public function drawCircle($x, $y, $radius)
    {
        echo "API2.circle at $x:$y radius $radius.\n";
    }
}

abstract class Shape
{
    protected $drawingAPI;

    public abstract function draw();
    public abstract function resizeByPercentage($pct);

    protected function __construct(DrawingAPI $drawingAPI)
    {
        $this->drawingAPI = $drawingAPI;
    }
}

class CircleShape extends Shape
{
    private $x;
    private $y;
    private $radius;

    public function __construct($x, $y, $radius, DrawingAPI $drawingAPI)
    {
        parent::__construct($drawingAPI);
        $this->x = $x;
        $this->y = $y;
        $this->radius = $radius;
    }

    public function draw()
    {
        $this->drawingAPI->drawCircle($this->x, $this->y, $this->radius);
    }

    public function resizeByPercentage($pct)
    {
        $this->radius *= $pct;
    }
}

class Tester
{
    public static function main()
    {
        $shapes = array(
            new CircleShape(1, 3, 7,  new DrawingAPI1()),
            new CircleShape(5, 7, 11, new DrawingAPI2()),
        );

        foreach ($shapes as $shape) {
            $shape->resizeByPercentage(2.5);
            $shape->draw();
        }
    }
}

Tester::main();
```

Output:

```
API1.circle at 1:3 radius 17.5
API2.circle at 5:7 radius 27.5
```

### Scala

```mw
trait DrawingAPI {
  def drawCircle(x: Double, y: Double, radius: Double)
}

class DrawingAPI1 extends DrawingAPI {
  def drawCircle(x: Double, y: Double, radius: Double) = println(s"API #1 $x $y $radius")
}

class DrawingAPI2 extends DrawingAPI {
  def drawCircle(x: Double, y: Double, radius: Double) = println(s"API #2 $x $y $radius")
}

abstract class Shape(drawingAPI: DrawingAPI) {
  def draw()
  def resizePercentage(pct: Double)
}

class CircleShape(x: Double, y: Double, var radius: Double, drawingAPI: DrawingAPI)
    extends Shape(drawingAPI: DrawingAPI) {

  def draw() = drawingAPI.drawCircle(x, y, radius)

  def resizePercentage(pct: Double) { radius *= pct }
}

object BridgePattern {
  def main(args: Array[String]) {
    Seq (
	new CircleShape(1, 3, 5, new DrawingAPI1),
	new CircleShape(4, 5, 6, new DrawingAPI2)
    ) foreach { x =>
        x.resizePercentage(3)
        x.draw()			
      }	
  }
}
```

### Python

```mw
"""
Bridge pattern example.
"""
from abc import ABCMeta, abstractmethod
from typing import NoReturn

NOT_IMPLEMENTED: str = "You should implement this."

class DrawingAPI:
    __metaclass__ = ABCMeta

    @abstractmethod
    def draw_circle(self, x: float, y: float, radius: float) -> NoReturn:
        raise NotImplementedError(NOT_IMPLEMENTED)

class DrawingAPI1(DrawingAPI):
    def draw_circle(self, x: float, y: float, radius: float) -> str:
        return f"API1.circle at {x}:{y} - radius: {radius}"

class DrawingAPI2(DrawingAPI):
    def draw_circle(self, x: float, y: float, radius: float) -> str:
        return f"API2.circle at {x}:{y} - radius: {radius}"

class DrawingAPI3(DrawingAPI):
    def draw_circle(self, x: float, y: float, radius: float) -> str:
        return f"API3.circle at {x}:{y} - radius: {radius}"

class Shape:
    __metaclass__ = ABCMeta

    drawing_api: DrawingAPI = None
    def __init__(self, drawing_api: DrawingAPI) -> None:
        self.drawing_api = drawing_api

    @abstractmethod
    def draw(self) -> NoReturn:
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def resize_by_percentage(self, percent: float) -> NoReturn:
        raise NotImplementedError(NOT_IMPLEMENTED)

class CircleShape(Shape):
    def __init__(self, x: float, y: float, radius: float, drawing_api: DrawingAPI):
        self.x = x
        self.y = y
        self.radius = radius
        super(CircleShape, self).__init__(drawing_api)

    def draw(self) -> str:
        return self.drawing_api.draw_circle(self.x, self.y, self.radius)

    def resize_by_percentage(self, percent: float) -> None:
        self.radius *= 1 + percent / 100

class BridgePattern:
    @staticmethod
    def test() -> None:
        shapes: list[CircleShape] = [
            CircleShape(1.0, 2.0, 3.0, DrawingAPI1()),
            CircleShape(5.0, 7.0, 11.0, DrawingAPI2()),
            CircleShape(5.0, 4.0, 12.0, DrawingAPI3()),
        ]

        for shape in shapes:
            shape.resize_by_percentage(2.5)
            print(shape.draw())

if __name__ == "__main__":
    BridgePattern.test()
```
