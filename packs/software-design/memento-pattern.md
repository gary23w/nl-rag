---
title: "Memento pattern"
source: https://en.wikipedia.org/wiki/Memento_pattern
domain: software-design
license: CC-BY-SA-4.0
tags: design pattern, software architecture, software design, refactoring
fetched: 2026-07-02
---

# Memento pattern

The **memento pattern** is a software design pattern in the field of object-oriented programming that allows reverting the state of an object. Uses of this design pattern include undo, version control, and serialization.

The memento pattern is implemented with three objects: the *originator*, a *caretaker* and a *memento*. The originator is some object that has an internal state. The caretaker is going to do something to the originator, but wants to be able to easily bring back the prior state. The caretaker first asks the originator for a memento object. Then it does whatever operation (or sequence of operations) it was going to do. To roll back to the state before the operations, it returns the memento object to the originator. The memento object itself is immutable. When using this pattern, care should be taken if the originator may change other objects or resources—the memento pattern operates on a single object.

One classic example of this pattern is the pseudorandom number generator (PRNG). In this case, each consumer of the PRNG serves as a caretaker who can initialize the PRNG (the originator) with a particular seed (the memento) to produce an identical sequence of pseudorandom numbers.

## Structure

### UML class and sequence diagram

In the above UML class diagram, the `Caretaker` class refers to the `Originator` class for saving (`createMemento()`) and restoring (`restore(memento)`) originator's internal state. The `Originator` class implements (1) `createMemento()` by creating and returning a `Memento` object that stores originator's current internal state and (2) `restore(memento)` by restoring state from the passed in `Memento` object.

The UML sequence diagram shows the run-time interactions: (1) Saving originator's internal state: The `Caretaker` object calls `createMemento()` on the `Originator` object, which creates a `Memento` object, saves its current internal state (`setState()`), and returns the `Memento` to the `Caretaker`. (2) Restoring originator's internal state: The `Caretaker` calls `restore(memento)` on the `Originator` object and specifies the `Memento` object that stores the state that should be restored. The `Originator` gets the state (`getState()`) from the `Memento` to set its own state.

## Java example

The following Java program illustrates the "undo" usage of the memento pattern.

```mw
package org.wikipedia.examples;

import java.util.ArrayList;
import java.util.List;

class Originator {
    private String state;
    // The class could also contain additional data that is not part of the
    // state saved in the memento..
 
    public void set(String state) {
        this.state = state;
        System.out.printf("Originator: Setting state to %s%n", state);
    }
 
    public Memento saveToMemento() {
        System.out.println("Originator: Saving to Memento.");
        return new Memento(this.state);
    }
 
    public void restoreFromMemento(Memento memento) {
        this.state = memento.getSavedState();
        System.out.printf("Originator: State after restoring from Memento: %s%n", state);
    }
 
    public static class Memento {
        private final String state;

        public Memento(String stateToSave) {
            state = stateToSave;
        }
 
        // accessible by outer class only
        private String getSavedState() {
            return state;
        }
    }
}
 
class Caretaker {
    public static void main(String[] args) {
        List<Originator.Memento> savedStates = new ArrayList<Originator.Memento>();
 
        Originator originator = new Originator();
        originator.set("State1");
        originator.set("State2");
        savedStates.add(originator.saveToMemento());
        originator.set("State3");
        // We can request multiple mementos, and choose which one to roll back to.
        savedStates.add(originator.saveToMemento());
        originator.set("State4");
 
        originator.restoreFromMemento(savedStates.get(1));   
    }
}
```

The output is:

```
Originator: Setting state to State1
Originator: Setting state to State2
Originator: Saving to Memento.
Originator: Setting state to State3
Originator: Saving to Memento.
Originator: Setting state to State4
Originator: State after restoring from Memento: State3
```

This example uses a String as the state, which is an immutable object in Java. In real-life scenarios the state will almost always be a mutable object, in which case a copy of the state must be made.

It must be said that the implementation shown has a drawback: it declares an internal class. It would be better if this memento strategy could apply to more than one originator.

There are mainly three other ways to achieve Memento:

1. Serialization.
2. A class declared in the same package.
3. The object can also be accessed via a proxy, which can achieve any save/restore operation on the object.

## C# example

The memento pattern allows one to capture the internal state of an object without violating encapsulation such that later one can undo/revert the changes if required. Here one can see that the *memento object* is actually used to *revert* the changes made in the object.

```mw
namespace Wikipedia.Examples;

class Memento
{
    private readonly string _savedState;

    private Memento(string stateToSave)
    {
        _savedState = stateToSave;
    }

    public class Originator
    {
        private string _state;
        // The class could also contain additional data that is not part of the
        // state saved in the memento.

        public void Set(string state)
        {
            Console.WriteLine(f"Originator: Setting state to {state}");
            _state = state;
        }

        public Memento SaveToMemento()
        {
            Console.WriteLine("Originator: Saving to Memento.");
            return new Memento(_state);
        }

        public void RestoreFromMemento(Memento memento)
        {
            _state = memento.savedState;
            Console.WriteLine(f"Originator: State after restoring from Memento: {_state}");
        }
    }
}

class Caretaker
{
    static void Main(string[] args)
    {
        List<Memento> savedStates = new();

        Memento.Originator originator = new();
        originator.Set("State1");
        originator.Set("State2");
        savedStates.Add(originator.SaveToMemento());
        originator.Set("State3");
        // We can request multiple mementos, and choose which one to roll back to.
        savedStates.Add(originator.SaveToMemento());
        originator.Set("State4");

        originator.RestoreFromMemento(savedStates[1]);
    }
}
```

## Python example

```mw
"""
Memento pattern example.
"""

class Originator:
    state: str = ""

    def set(self, state: str) -> None:
        print(f"Originator: Setting state to {state}")
        self.state = state

    def save_to_memento(self) -> "Memento":
        return self.Memento(self.state)

    def restore_from_memento(self, memento: "Memento") -> None:
        self.state = memento.get_saved_state()
        print(f"Originator: State after restoring from Memento: {self.state}")

    class Memento:
        state: str

        def __init__(self, state: str) -> None:
            self.state = state

        def get_saved_state(self) -> str:
            return self.state

saved_states: list[Memento] = []
originator: Originator = Originator()

originator.set("State1")
originator.set("State2")
saved_states.append(originator.save_to_memento())

originator.set("State3")
saved_states.append(originator.save_to_memento())

originator.set("State4")

originator.restore_from_memento(saved_states[1])
```

## JavaScript example

```mw
// The Memento pattern is used to save and restore the state of an object.
// A memento is a snapshot of an object's state.
let Memento = {// Namespace: Memento
    savedState : null, // The saved state of the object.

    save : function(state) { // Save the state of an object.
        this.savedState = state;
    },

    restore : function() { // Restore the state of an object.
        return this.savedState;
    }
};

// The Originator is the object that creates the memento.
// defines a method for saving the state inside a memento.
let Originator = {// Namespace: Originator
        state : null, // The state to be stored

        // Creates a new originator with an initial state of null
        createMemento : function() { 
            return {
                state : this.state // The state is copied to the memento.
            };
        },
        setMemento : function(memento) { // Sets the state of the originator from a memento
            this.state = memento.state;
        }
    };

// The Caretaker stores mementos of the objects and
// provides operations to retrieve them.
let Caretaker = {// Namespace: Caretaker
        mementos : [], // The mementos of the objects.
        addMemento : function(memento) { // Add a memento to the collection.
            this.mementos.push(memento);
        },
        getMemento : function(index) { // Get a memento from the collection.
            return this.mementos[index];
        }
    };

let action_step = "Foo"; // The action to be executed/the object state to be stored.
let action_step_2 = "Bar"; // The action to be executed/the object state to be stored.

// set the initial state
Originator.state = action_step;
Caretaker.addMemento(Originator.createMemento());// save the state to the history
console.log("Initial State: " + Originator.state); // Foo

// change the state
Originator.state = action_step_2;
Caretaker.addMemento(Originator.createMemento()); // save the state to the history
console.log("State After Change: " + Originator.state); // Bar

// restore the first state - undo
Originator.setMemento(Caretaker.getMemento(0));
console.log("State After Undo: " + Originator.state); // Foo

// restore the second state - redo
Originator.setMemento(Caretaker.getMemento(1));
console.log("State After Redo: " + Originator.state); // Bar
```
