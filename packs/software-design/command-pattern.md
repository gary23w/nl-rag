---
title: "Command pattern"
source: https://en.wikipedia.org/wiki/Command_pattern
domain: software-design
license: CC-BY-SA-4.0
tags: design pattern, software architecture, software design, refactoring
fetched: 2026-07-02
---

# Command pattern

In object-oriented programming, the **command pattern** is a behavioral design pattern in which an object is used to encapsulate all information needed to perform an action or trigger an event at a later time. This information includes the method name, the object that owns the method and values for the method parameters.

Four terms always associated with the command pattern are *command*, *receiver*, *invoker* and *client*. A *command* object knows about *receiver* and invokes a method of the receiver. Values for parameters of the receiver method are stored in the command. The receiver object to execute these methods is also stored in the command object by aggregation. The *receiver* then does the work when the `execute()` method in *command* is called. An *invoker* object knows how to execute a command, and optionally does bookkeeping about the command execution. The invoker does not know anything about a concrete command, it knows only about the command *interface*. Invoker object(s), command objects and receiver objects are held by a *client* object. The *client* decides which receiver objects it assigns to the command objects, and which commands it assigns to the invoker. The client decides which commands to execute at which points. To execute a command, it passes the command object to the invoker object.

Using command objects makes it easier to construct general components that need to delegate, sequence or execute method calls at a time of their choosing without the need to know the class of the method or the method parameters. Using an invoker object allows bookkeeping about command executions to be conveniently performed, as well as implementing different modes for commands, which are managed by the invoker object, without the need for the client to be aware of the existence of bookkeeping or modes.

The central ideas of this design pattern closely mirror the semantics of first-class functions and higher-order functions in functional programming languages. Specifically, the invoker object is a higher-order function of which the command object is a first-class argument.

## Overview

The command design pattern is one of the twenty-three well-known *GoF design patterns* that describe how to solve recurring design problems to design flexible and reusable object-oriented software, that is, objects that are easier to implement, change, test, and reuse.

Using the command design pattern can solve these problems:

- Coupling the invoker of a request to a particular request should be avoided. That is, hard-wired requests should be avoided.
- It should be possible to configure an object (that invokes a request) with a request.

Implementing (hard-wiring) a request directly into a class is inflexible because it couples the class to a particular request at compile-time, which makes it impossible to specify a request at run-time.

Using the command design pattern describes the following solution:

- Define separate (command) objects that encapsulate a request.
- A class delegates a request to a command object instead of implementing a particular request directly.

This enables one to configure a class with a command object that is used to perform a request. The class is no longer coupled to a particular request and has no knowledge (is independent) of how the request is carried out.

See also the UML class and sequence diagram below.

## Structure

### UML class and sequence diagram

In the above UML class diagram, the `Invoker` class doesn't implement a request directly. Instead, `Invoker` refers to the `Command` interface to perform a request (`command.execute()`), which makes the `Invoker` independent of how the request is performed. The `Command1` class implements the `Command` interface by performing an action on a receiver (`receiver1.action1()`).

The UML sequence diagram shows the run-time interactions: The `Invoker` object calls `execute()` on a `Command1` object. `Command1` calls `action1()` on a `Receiver1` object, which performs the request.

### UML class diagram

## Uses

**GUI buttons and menu items**

In

Swing

and

Borland

Delphi

programming, an

Action

is a command object. In addition to the ability to perform the desired command, an

Action

may have an associated icon,

keyboard shortcut

,

tooltip

text, and so on. A toolbar button or menu item component may be completely initialized using only the

Action

object.

**Macro recording**

If all user actions are represented by command objects, a program can record a sequence of actions simply by keeping a list of the command objects as they are executed. It can then "play back" the same actions by executing the same command objects again in sequence. If the program embeds a scripting engine, each command object can implement a

toScript()

method, and user actions can then be easily recorded as scripts.

**Mobile code**

Using languages such as Java where code can be streamed/slurped from one location to another via URLClassloaders and Codebases the commands can enable new behavior to be delivered to remote locations (EJB Command, Master Worker).

**Multi-level undo**

If all user actions in a program are implemented as command objects, the program can keep a stack of the most recently executed commands. When the user wants to undo a command, the program simply pops the most recent command object and executes its

undo()

method.

**Networking**

It is possible to send whole command objects across the network to be executed on the other machines, for example player actions in computer games.

**Parallel processing**

Where the commands are written as tasks to a shared resource and executed by many threads in parallel (possibly on remote machines; this variant is often referred to as the Master/Worker pattern)

**Progress bars**

Suppose a program has a sequence of commands that it executes in order. If each command object has a

getEstimatedDuration()

method, the program can easily estimate the total duration. It can show a progress bar that meaningfully reflects how close the program is to completing all the tasks.

**Thread pools**

A typical, general-purpose thread pool class might have a public

addTask()

method that adds a work item to an internal queue of tasks waiting to be done. It maintains a pool of threads that execute commands from the queue. The items in the queue are command objects. Typically these objects implement a common interface such as

java.lang.Runnable

that allows the thread pool to execute the command even though the thread pool class itself was written without any knowledge of the specific tasks for which it would be used.

**Transactional behavior**

Similar to undo, a

database engine

or software installer may keep a list of operations that have been or will be performed. Should one of them fail, all others can be reversed or discarded (usually called

rollback

). For example, if two database tables that refer to each other must be updated, and the second update fails, the transaction can be rolled back, so that the first table does not now contain an invalid reference.

**Wizards**

Often a wizard presents several pages of configuration for a single action that happens only when the user clicks the "Finish" button on the last page. In these cases, a natural way to separate user interface code from application code is to implement the wizard using a command object. The command object is created when the wizard is first displayed. Each wizard page stores its GUI changes in the command object, so the object is populated as the user progresses. "Finish" simply triggers a call to

execute()

. This way, the command class will work.

## Example

This C++23 implementation is based on the pre C++98 implementation in the book.

```mw
import std;

using std::shared_ptr;
using std::unique_ptr;

// Abstract command
class Command {
protected:
    Command() = default;
public:
    // declares an interface for executing an operation.
    virtual void execute() = 0;
    virtual ~Command() = default;
};

// Concrete command
template <typename Receiver>
class SimpleCommand : public Command {
private:
    Receiver* receiver;
    Action action;
public:
    using Action = void (Receiver::*)();

    // defines a binding between a Receiver object and an action.
    SimpleCommand(shared_ptr<Receiver> receiver, Action action):
        receiver{receiver.get()}, action{action} {}

    SimpleCommand(const SimpleCommand&) = delete;
    const SimpleCommand& operator=(const SimpleCommand&) = delete;

    // implements execute by invoking the corresponding operation(s) on Receiver.
    virtual void execute() {
        (receiver->*action)();
    }
};

// Receiver
class MyClass {
public:
    // knows how to perform the operations associated with carrying out a request. Any class may serve as a Receiver.
    void action() {
        std::println("MyClass::action called");
    }
};

int main(int argc, char* argv[]) {
    shared_ptr<MyClass> receiver = std::make_shared<MyClass>();
    // ...
    unique_ptr<Command> command = std::make_unique<SimpleCommand<MyClass>>(receiver, &MyClass::action);
    // ...
    command->execute();
}
```

The program output is

```mw
MyClass::action called
```
