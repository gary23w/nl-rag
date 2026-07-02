---
title: "State pattern"
source: https://en.wikipedia.org/wiki/State_pattern
domain: software-design
license: CC-BY-SA-4.0
tags: design pattern, software architecture, software design, refactoring
fetched: 2026-07-02
---

# State pattern

The **state pattern** is a behavioral software design pattern that allows an object to alter its behavior when its internal state changes. This pattern is close to the concept of finite-state machines. The state pattern can be interpreted as a strategy pattern, which is able to switch a strategy through invocations of methods defined in the pattern's interface.

The state pattern is used in computer programming to encapsulate varying behavior for the same object, based on its internal state. This can be a cleaner way for an object to change its behavior at runtime without resorting to conditional statements and thus improve maintainability.

## Overview

The state design pattern is one of twenty-three design patterns documented by the Gang of Four that describe how to solve recurring design problems. Such problems cover the design of flexible and reusable object-oriented software, such as objects that are easy to implement, change, test, and reuse.

The state pattern is set to solve two main problems:

- An object should change its behavior when its internal state changes.
- State-specific behavior should be defined independently. That is, adding new states should not affect the behavior of existing states.

Implementing state-specific behavior directly within a class is inflexible because it commits the class to a particular behavior and makes it impossible to add a new state or change the behavior of an existing state later, independently from the class, without changing the class. In this, the pattern describes two solutions:

- Define separate (state) objects that encapsulate state-specific behavior for each state. That is, define an interface (state) for performing state-specific behavior, and define classes that implement the interface for each state.
- A class delegates state-specific behavior to its current state object instead of implementing state-specific behavior directly.

This makes a class independent of how state-specific behavior is implemented. New states can be added by defining new state classes. A class can change its behavior at run-time by changing its current state object.

## Structure

In the accompanying Unified Modeling Language (UML) class diagram, the `Context` class doesn't implement state-specific behavior directly. Instead, `Context` refers to the `State` interface for performing state-specific behavior (`state.handle()`), which makes `Context` independent of how state-specific behavior is implemented. The `ConcreteStateA` and `ConcreteStateB` classes implement the `State` interface, that is, implement (encapsulate) the state-specific behavior for each state. The UML sequence diagram shows the run-time interactions:

The `Context` object delegates state-specific behavior to different `State` objects. First, `Context` calls `handle(this)` on its current (initial) state object (`ConcreteStateA`), which performs the operation and calls `setState(ConcreteStateB)` on `Context` to change context's current state to `ConcreteStateB`. The next time, `Context` again calls `handle(this)` on its current state object (`ConcreteStateB`), which performs the operation and changes context's current state to `ConcreteStateA`.

## Example

This is a C++ example demonstrating the state pattern.

```mw
import std;

using std::unique_ptr;

// Abstract State
class FanState {
public:
    virtual void handleButtonPress(class Fan& fan) const = 0;
    virtual ~FanState() = default;
};

// Context
class Fan {
private:
    unique_ptr<FanState> currentState;
public:
    explicit Fan(unique_ptr<FanState> state):
        currentState{state} {}

    void setState(unique_ptr<FanState> state) noexcept {
        currentState = state;
    }

    void pressButton() noexcept {
        currentState->handleButtonPress(*this);
    }
};

// Concrete States
class OffState : public FanState {
public:
    void handleButtonPress(Fan& fan) const override {
        std::println("Fan is OFF -> Switching to LOW speed.");
        fan.setState(std::make_unique<LowSpeedState>());
    }
};

class LowSpeedState : public FanState {
public:
    void handleButtonPress(Fan& fan) const override {
        std::println("Fan is on LOW speed -> Switching to HIGH speed.");
        fan.setState(std::make_unique<HighSpeedState>());
    }
};

class HighSpeedState : public FanState {
public:
    void handleButtonPress(Fan& fan) const override {
        std::println("Fan is on HIGH speed -> Turning OFF.");
        fan.setState(std::make_unique<OffState>());
    }
};

int main() {
    Fan fan(std::unique_ptr<OffState>());

    // Simulate pressing the button several times
    fan.pressButton(); // OFF -> LOW
    fan.pressButton(); // LOW -> HIGH
    fan.pressButton(); // HIGH -> OFF
    fan.pressButton(); // OFF -> LOW

    return 0;
}
```
