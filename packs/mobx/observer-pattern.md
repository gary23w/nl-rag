---
title: "Observer pattern"
source: https://en.wikipedia.org/wiki/Observer_pattern
domain: mobx
license: CC-BY-SA-4.0 / MIT (mobx.js.org)
tags: mobx, observable state, transparent reactivity, mobx reaction
fetched: 2026-07-02
---

# Observer pattern

In software design and software engineering, the **observer pattern** is a software design pattern in which an object, called the ***subject*** (also known as ***event source*** or ***event stream***), maintains a list of its dependents, called **observers** (also known as ***event sinks***), and automatically notifies them of any state changes, typically by calling one of their methods. The subject knows its observers through a standardized interface and manages the subscription list directly.

This pattern creates a one-to-many dependency where multiple observers can listen to a single subject, but the coupling is typically synchronous and direct—the subject calls observer methods when changes occur, though asynchronous implementations using event queues are possible. Unlike the publish-subscribe pattern, there is no intermediary broker; the subject and observers have direct references to each other.

It is commonly used to implement event handling systems in event-driven programming, particularly in-process systems like GUI toolkits or MVC frameworks. This makes the pattern well-suited to processing data that arrives unpredictably—such as user input, HTTP requests, GPIO signals, updates from distributed databases, or changes in a GUI model.

## Overview

The observer design pattern is a behavioural pattern listed among the 23 well-known "Gang of Four" design patterns that address recurring design challenges in order to design flexible and reusable object-oriented software, yielding objects that are easier to implement, change, test, and reuse.

The observer pattern addresses the following requirements:

- A one-to-many dependency between objects should be defined without making the objects tightly coupled.
- When one object changes state, an open-ended number of dependent objects should be updated automatically.
- An object can notify multiple other objects.

The naive approach would be for one object (subject) to directly call specific methods on each dependent object. This creates tight coupling because the subject must know the concrete types and specific interfaces of all dependent objects, making the code inflexible and hard to extend. However, this direct approach may be preferable in performance-critical scenarios (such as low-level kernel structures or real-time systems) where the overhead of abstraction is unacceptable and compile-time optimization is crucial.

The observer pattern provides a more flexible alternative by establishing a standard notification protocol:

1. Define `Subject` and `Observer` objects with standardized interfaces.
2. When a subject changes state, all registered observers are notified and updated automatically.
3. The subject manages its own state while also maintaining a list of observers and notifying them of state changes by calling their `update()` operation.
4. The responsibility of observers is to register and unregister themselves with a subject (in order to be notified of state changes) and to update their state (to synchronize it with the subject's state) when they are notified.

This approach makes subject and observers loosely coupled through interface standardization. The subject only needs to know that observers implement the `update()` method—it has no knowledge of observers' concrete types or internal implementation details. Observers can be added and removed independently at run time.

## Relationship to publish–subscribe

The observer pattern and the publish–subscribe pattern are closely related and often confused, as both support one-to-many communication between components. However, they differ significantly in architecture, degree of coupling, and common use cases.

The table below summarizes the key differences:

| Feature | **Observer Pattern** | **Publish–Subscribe Pattern** |
|---|---|---|
| **Coupling** | *Tightly coupled* — the subject holds direct references to its observers via a standardized interface. | *Loosely coupled* — publishers and subscribers are unaware of each other. |
| **Communication** | *Direct* — the subject calls observer methods, typically synchronously. | *Indirect* — a broker (message bus or event manager) dispatches messages to subscribers. |
| **Knowledge of Participants** | The subject knows its observers. | Publisher and subscriber are decoupled; neither knows about the other. |
| **Scalability** | Suitable for in-process systems like GUI toolkits. | More scalable; supports distributed systems and asynchronous messaging. |
| **Synchronous or Asynchronous** | Typically synchronous but can be asynchronous with event queues. | Typically asynchronous but can be synchronous. |
| **Filtering** | Limited — observers receive all events and filter internally. | Rich filtering — brokers may filter by topic, content, or rules. |
| **Fault Tolerance** | Observer failures can affect the subject. | Failures are isolated; the broker decouples participants. |
| **Typical Usage** | GUI frameworks, MVC architecture, local object notifications. | Microservices, distributed systems, messaging middleware. |

In practice, publish–subscribe systems evolved to address several limitations of the observer pattern. A typical observer implementation creates a tight coupling between the subject and its observers. This may limit scalability, flexibility, and maintainability, especially in distributed environments. Subjects and observers must conform to a shared interface, and both parties are aware of each other’s presence.

To reduce this coupling, publish–subscribe systems introduce a message broker or event bus that intermediates between publishers and subscribers. This additional layer removes the need for direct references, allowing systems to evolve independently. Brokers may also support features like message persistence, delivery guarantees, topic-based filtering, and asynchronous communication.

In some systems, the observer pattern is used internally to implement subscription mechanisms behind a publish–subscribe interface. In other cases, the patterns are applied independently. For example, JavaScript libraries and frameworks often offer both observer-like subscriptions (e.g., via callback registration) and decoupled pub-sub mechanisms (e.g., via event emitters or signals).

Historically, in early graphical operating systems like OS/2 and Microsoft Windows, the terms "publish–subscribe" and "event-driven programming" were often used as synonyms for the observer pattern.

The observer pattern, as formalized in *Design Patterns*, deliberately omits concerns such as unsubscription, notification filtering, delivery guarantees, and message logging. These advanced capabilities are typically implemented in robust message queuing systems, where the observer pattern may serve as a foundational mechanism but is not sufficient by itself.

Related patterns include mediator and singleton.

## Limitations and solutions

### Strong vs. weak references

A common drawback of the observer pattern is the potential for memory leaks, known as the lapsed listener problem. This occurs when a subject maintains strong references to its observers, preventing them from being garbage collected even if they are no longer needed elsewhere. Because the pattern typically requires both explicit registration and deregistration (as in the dispose pattern), forgetting to unregister observers can leave dangling references. This issue can be mitigated by using weak references for observer references, allowing the garbage collector to reclaim observer objects that are no longer in use.

### Throttling and temporal decoupling

In some applications, particularly user interfaces, the subject's state may change so frequently that notifying observers on every change is inefficient or counterproductive. For example, a view that re-renders on every minor change in a data model might become unresponsive or flicker.

In such cases, the observer pattern can be modified to decouple notifications *temporally* by introducing a throttling mechanism, such as a timer. Rather than updating on every state change, the observer polls the subject or is notified at regular intervals, rendering an approximate but stable view of the model.

This approach is commonly used for elements like progress bars, where the underlying process changes state rapidly. Instead of responding to every minor increment, the observer updates the visual display periodically, improving performance and usability.

This form of temporal decoupling allows observers to remain responsive without being overwhelmed by high-frequency updates, while still reflecting the overall trend or progress of the subject’s state.

## Structure

### UML class and sequence diagram

In this UML class diagram, the `Subject` class does not update the state of dependent objects directly. Instead, `Subject` refers to the `Observer` interface (`update()`) for updating state, which makes the `Subject` independent of how the state of dependent objects is updated. The `Observer1` and `Observer2` classes implement the `Observer` interface by synchronizing their state with subject's state.

The UML sequence diagram shows the runtime interactions: The `Observer1` and `Observer2` objects call `attach(this)` on `Subject1` to register themselves. Assuming that the state of `Subject1` changes, `Subject1` calls `notify()` on itself. `notify()` calls `update()` on the registered `Observer1` and `Observer2`objects, which request the changed data (`getState()`) from `Subject1` to update (synchronize) their state.

### UML class diagram

## Example

While the library classes `java.util.Observer` and `java.util.Observable` exist, they have been deprecated in Java 9 because the model implemented was quite limited.

Below is an example written in Java that takes keyboard input and handles each input line as an event. When a string is supplied from `System.in`, the method `notifyObservers()` is then called in order to notify all observers of the event's occurrence, in the form of an invocation of their update methods.

### Java

```mw
package org.wikipedia.examples;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

interface Observer {
    void update(String event);
}
  
class EventSource {
    List<Observer> observers = new ArrayList<>();
  
    public void notifyObservers(String event) {
        observers.forEach(observer -> observer.update(event));
    }
  
    public void addObserver(Observer observer) {
        observers.add(observer);
    }
  
    public void scanSystemIn() {
        Scanner scanner = new Scanner(System.in);
        while (scanner.hasNextLine()) {
            String line = scanner.nextLine();
            notifyObservers(line);
        }
    }
}

public class ObserverDemo {
    public static void main(String[] args) {
        System.out.println("Enter Text: ");
        EventSource eventSource = new EventSource();
        
        eventSource.addObserver(event -> System.out.printf("Received response: %s%n", event));

        eventSource.scanSystemIn();
    }
}
```

### C

C# provides the `IObservable`. and `IObserver` interfaces as well as documentation on how to implement the design pattern.

```mw
namespace Wikipedia.Examples;

using System;
using System.Collections.Generic;

class Payload
{
    internal string Message { get; init; }
}

class Subject : IObservable<Payload>
{
    private readonly List<IObserver<Payload>> _observers = new();

    IDisposable IObservable<Payload>.Subscribe(IObserver<Payload> observer)
    {         
        if (!_observers.Contains(observer))
        {
            _observers.Add(observer);
        }

        return new Unsubscriber(observer, _observers);
    }

    internal void SendMessage(string message)
    {
        foreach (IObserver<Payload> observer in _observers)
        {
            observer.OnNext(new Payload { Message = message });
        }
    }
}

internal class Unsubscriber : IDisposable
{
    private readonly IObserver<Payload> _observer;
    private readonly ICollection<IObserver<Payload>> _observers;

    internal Unsubscriber(
        IObserver<Payload> observer,
        ICollection<IObserver<Payload>> observers)
    {
        _observer = observer;
        _observers = observers;
    }

    void IDisposable.Dispose()
    {
        if (_observer != null && _observers.Contains(_observer))
        {
            _observers.Remove(_observer);
        }
    }
}

internal class Observer : IObserver<Payload>
{
    private string _message;

    public void OnCompleted()
    {
    }

    public void OnError(Exception error)
    {
    }

    public void OnNext(Payload value)
    {
        _message = value.Message;
    }

    internal IDisposable Register(IObservable<Payload> subject)
    {
        return subject.Subscribe(this);
    }
}
```

### C++

This is a C++23 implementation.

```mw
import std;

using std::reference_wrapper;
using std::vector;

class Subject; // Forward declaration for usage in Observer

class Observer {
private:
    // Reference to a Subject object to detach in the destructor
    Subject& subject;
public:
    explicit Observer(Subject& subj):     
        subject{subj} {
        subject.attach(*this);
    }

    virtual ~Observer() {
        subject.detach(*this);
    }
  
    Observer(const Observer&) = delete;
    Observer& operator=(const Observer&) = delete;

    virtual void update(Subject& s) const = 0;
};

// Subject is the base class for event generation
class Subject {
private:
    vector<refObserver> observers;
public:
    using RefObserver = reference_wrapper<const Observer>;
  
    // Notify all the attached observers
    void notify() {
        for (const Observer& x: observers) {
            x.get().update(*this);
        }
    }
  
    // Add an observer
    void attach(const Observer& observer) {
        observers.push_back(observer);
    }
  
    // Remove an observer
    void detach(Observer& observer) {
        observers.remove_if([&observer](const RefObserver& obj) -> bool { 
            return &obj.get() == &observer; 
        });
    }
};

// Example of usage
class ConcreteObserver: public Observer {
public:
    explicit ConcreteObserver(Subject& subj): 
        Observer(subj) {}
  
    // Get notification
    void update(Subject&) const override {
        std::println("Got a notification");
    }
};

int main(int argc, char* argv[]) {
    Subject cs;
    ConcreteObserver co1(cs);
    ConcreteObserver co2(cs);
    cs.notify();
}
```

The program output is:

```mw
Got a notification
Got a notification
```

### Groovy

```mw
class EventSource {
    private observers = []

    private notifyObservers(String event) {
        observers.each { it(event) }
    }

    void addObserver(observer) {
        observers += observer
    }

    void scanSystemIn() {
        var scanner = new Scanner(System.in)
        while (scanner) {
            var line = scanner.nextLine()
            notifyObservers(line)
        }
    }
}

println 'Enter Text: '
var eventSource = new EventSource()

eventSource.addObserver { event ->
    println "Received response: $event"
}

eventSource.scanSystemIn()
```

### Kotlin

```mw
import java.util.Scanner

typealias Observer = (event: String) -> Unit;

class EventSource {
    private var observers = mutableListOf<Observer>()

    private fun notifyObservers(event: String) {
        observers.forEach { it(event) }
    }

    fun addObserver(observer: Observer) {
        observers += observer
    }

    fun scanSystemIn() {
        val scanner = Scanner(System.`in`)
        while (scanner.hasNext()) {
            val line = scanner.nextLine()
            notifyObservers(line)
        }
    }
}
```

```mw
fun main(arg: List<String>) {
    println("Enter Text: ")
    val eventSource = EventSource()

    eventSource.addObserver { event ->
        println("Received response: $event")
    }

    eventSource.scanSystemIn()
}
```

### Delphi

```mw
uses
  System.Generics.Collections, System.SysUtils;

type
  IObserver = interface
    ['{0C8F4C5D-1898-4F24-91DA-63F1DD66A692}']
    procedure Update(const AValue: string);
  end;

type
  TObserverManager = class
  private
    FObservers: TList<IObserver>;
  public
    constructor Create; overload;
    destructor Destroy; override;
    procedure NotifyObservers(const AValue: string);
    procedure AddObserver(const AObserver: IObserver);
    procedure UnregisterObserver(const AObserver: IObserver);
  end;

type
  TListener = class(TInterfacedObject, IObserver)
  private
    FName: string;
  public
    constructor Create(const AName: string); reintroduce;
    procedure Update(const AValue: string);
  end;

procedure TObserverManager.AddObserver(const AObserver: IObserver);
begin
  if not FObservers.Contains(AObserver)
    then FObservers.Add(AObserver);
end;

begin
  FreeAndNil(FObservers);
  inherited;
end;

procedure TObserverManager.NotifyObservers(const AValue: string);
var
  i: Integer;
begin
  for i := 0 to FObservers.Count - 1 do
    FObservers[i].Update(AValue);
end;

procedure TObserverManager.UnregisterObserver(const AObserver: IObserver);
begin
  if FObservers.Contains(AObserver)
    then FObservers.Remove(AObserver);
end;

constructor TListener.Create(const AName: string);
begin
  inherited Create;
  FName := AName;
end;

procedure TListener.Update(const AValue: string);
begin
  WriteLn(FName + ' listener received notification: ' + AValue);
end;

procedure TMyForm.ObserverExampleButtonClick(Sender: TObject);
var
  LDoorNotify: TObserverManager;
  LListenerHusband: IObserver;
  LListenerWife: IObserver;
begin
  LDoorNotify := TObserverManager.Create;
  try
    LListenerHusband := TListener.Create('Husband');
    LDoorNotify.AddObserver(LListenerHusband);
    LListenerWife := TListener.Create('Wife');
    LDoorNotify.AddObserver(LListenerWife);
    LDoorNotify.NotifyObservers('Someone is knocking on the door');
  finally
    FreeAndNil(LDoorNotify);
  end;
end;
```

Output

```
Husband listener received notification: Someone is knocking on the door
Wife listener received notification: Someone is knocking on the door
```

### Python

A similar example in Python:

```mw
from typing import Any

class Subject:
    _observers: list[Observer]

    def __init__(self) -> None:
        self._observers = []

    def register_observer(self, observer: Observer) -> None:
        self._observers.append(observer)

    def notify_observers(self, *args: tuple[Any, ...], **kwargs: dict[str, Any]) -> None:
        for observer in self._observers:
            observer.notify(self, *args, **kwargs)

class Observer:
    def __init__(self, subject: Subject) -> None:
        subject.register_observer(self)

    def notify(self, subject: Subject, *args: tuple[Any, ...], **kwargs: dict[str, Any]) -> None:
        print(f"Got {args}, {kwargs} from {subject}")

subject: Subject = Subject()
observer: Observer = Observer(subject)
subject.notify_observers("test", kw="python")

# prints: Got ('test',) {'kw': 'python'} From <__main__.Observable object at 0x0000019757826FD0>
```

### JavaScript

JavaScript has a deprecated `Object.observe` function that was a more accurate implementation of the observer pattern. This would fire events upon change to the observed object. Without the deprecated `Object.observe` function, the pattern may be implemented with more explicit code:

```mw
let Subject = {
    _state: 0,
    _observers: [],
    add: function(observer) {
        this._observers.push(observer);
    },
    getState: function() {
        return this._state;
    },
    setState: function(value) {
        this._state = value;
        for (let i = 0; i < this._observers.length; i++)
        {
            this._observers[i].signal(this);
        }
    }
};

let Observer = {
    signal: function(subject) {
        let currentValue = subject.getState();
        console.log(currentValue);
    }
}

Subject.add(Observer);
Subject.setState(10);
// Output in console.log - 10
```
