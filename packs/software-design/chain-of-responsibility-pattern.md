---
title: "Chain-of-responsibility pattern"
source: https://en.wikipedia.org/wiki/Chain-of-responsibility_pattern
domain: software-design
license: CC-BY-SA-4.0
tags: design pattern, software architecture, software design, refactoring
fetched: 2026-07-02
---

# Chain-of-responsibility pattern

In object-oriented design, the **chain-of-responsibility pattern** is a behavioral design pattern consisting of a source of command objects and a series of **processing objects**. Each processing object contains logic that defines the types of command objects that it can handle; the rest are passed to the next processing object in the chain. A mechanism also exists for adding new processing objects to the end of this chain.

In a variation of the standard chain-of-responsibility model, some handlers may act as dispatchers, capable of sending commands out in a variety of directions, forming a *tree of responsibility*. In some cases, this can occur recursively, with processing objects calling higher-up processing objects with commands that attempt to solve some smaller part of the problem; in this case recursion continues until the command is processed, or the entire tree has been explored. An XML interpreter might work in this manner.

This pattern promotes the idea of loose coupling.

The chain-of-responsibility pattern is structurally nearly identical to the decorator pattern, the difference being that for the decorator, all classes handle the request, while for the chain of responsibility, exactly one of the classes in the chain handles the request. This is a strict definition of the Responsibility concept in the *Gang of Four Design Patterns* book. However, many implementations (such as loggers below, or UI event handling, or servlet filters in Java, etc.) allow several elements in the chain to take responsibility.

## Overview

The Chain of Responsibility design pattern is one of the twenty-three well-known Gang of Four design patterns that describe common solutions to recurring design problems when designing flexible and reusable object-oriented software, that is, objects that are easier to implement, change, test, and reuse.

### Problems

The Chain of Responsibility pattern solves:

- Coupling the sender of a request to its receiver should be avoided.
- It should be possible that more than one receiver can handle a request.

Implementing a request directly within the class that sends the request is inflexible because it couples the class to a particular receiver and makes it impossible to support multiple receivers.

### Solution

- Define a chain of receiver objects having the responsibility, depending on run-time conditions, to either handle a request or forward it to the next receiver on the chain (if any).

This enables us to send a request to a chain of receivers without having to know which one handles the request. The request gets passed along the chain until a receiver handles the request. The sender of a request is no longer coupled to a particular receiver.

See also the UML class and sequence diagram below.

## Structure

### UML class and sequence diagram

In the above UML class diagram, the `Sender` class doesn't refer to a particular receiver class directly. Instead, `Sender` refers to the `Handler` interface for handling a request (`handler.handleRequest()`), which makes the `Sender` independent of which receiver handles the request. The `Receiver1`, `Receiver2`, and `Receiver3` classes implement the `Handler` interface by either handling or forwarding a request (depending on run-time conditions). The UML sequence diagram shows the run-time interactions: In this example, the `Sender` object calls `handleRequest()` on the `receiver1` object (of type `Handler`). The `receiver1` forwards the request to `receiver2`, which in turn forwards the request to `receiver3`, which handles (performs) the request.

## Example

This C++23 implementation is based on the pre C++98 implementation in the book.

```mw
import std;

using std::shared_ptr;

enum class Topic: char {
    NO_HELP_TOPIC = 0,
    PRINT_TOPIC = 1,
    PAPER_ORIENTATION = 2,
    APPLICATION_TOPIC = 3,
    PAPER_ORIENTATION_TOPIC = 4,
    // more topics
};

// Abstract handler
// defines an interface for handling requests.
class HelpHandler {
private:
    HelpHandler* successor;
    Topic topic;
public:
    explicit HelpHandler(HelpHandler* h = nullptr, Topic t = Topic::NO_HELP_TOPIC):
        successor{h}, topic{t} {}

    [[nodiscard]]
    virtual bool hasHelp() const noexcept {
        return topic != Topic::NO_HELP_TOPIC;
    }

    virtual void setHandler(HelpHandler* h, Topic t) {
        successor = h;
        topic = t;
    }

    virtual void handleHelp() const {
        std::println("HelpHandler::handleHelp called");
        // (optional) implements the successor link.
        if (successor) {
            successor->handleHelp();
        }
    }

    virtual ~HelpHandler() = default;

    HelpHandler(const HelpHandler&) = delete;
    HelpHandler& operator=(const HelpHandler&) = delete;
};

class Widget: public HelpHandler {
private:
    Widget* parent;
protected:
    explicit Widget(Widget* w, Topic t = Topic::NO_HELP_TOPIC):
        HelpHandler(w, t), parent{w} {
        parent = w;
    }
public:
    Widget(const Widget&) = delete;
    Widget& operator=(const Widget&) = delete;
};

// Concrete handler
// handles requests it is responsible for.
class Button: public Widget {
public:
    explicit Button(shared_ptr<Widget> h, Topic t = Topic::NO_HELP_TOPIC):
        Widget(h.get(), t) {}

    void handleHelp() const override {
        // If the Concrete handler can handle the request, it does so.
        // Otherwise, it forwards the request to its successor.
        std::println("Button::handleHelp called");
        if (hasHelp()) {
            // handles requests it is responsible for.
        } else {
            // can access its successor.
            HelpHandler::handleHelp();
        }
    }
};

// Concrete handler
class Dialog: public Widget {
public:
    explicit Dialog(shared_ptr<HelpHandler> h, Topic t = Topic::NO_HELP_TOPIC):
        Widget(nullptr) {
        setHandler(h.get(), t);
    }

    void handleHelp() const override {
        std::println("Dialog::handleHelp called");
        // Widget operations that Dialog overrides...
        if(hasHelp()) {
            // offer help on the dialog
        } else {
            HelpHandler::handleHelp();
        }
    }
};

class Application: public HelpHandler {
public:
    explicit Application(Topic t):
        HelpHandler(nullptr, t) {}

    void handleHelp() const override {
        std::println("Application::handleHelp called");
        // show a list of help topics
    }
};

int main(int argc, char* argv[]) {
    shared_ptr<Application> application = std::make_shared<Application>(Topic::APPLICATION_TOPIC);
    shared_ptr<Dialog> dialog = std::make_shared<Dialog>(application, Topic::PRINT_TOPIC);
    shared_ptr<Button> button = std::make_shared<Button>(dialog, Topic::PAPER_ORIENTATION_TOPIC);

    button->handleHelp();
    return 0;
}
```

## Implementations

### Cocoa and Cocoa Touch

The Cocoa and Cocoa Touch frameworks, used for OS X and iOS applications respectively, actively use the chain-of-responsibility pattern for handling events. Objects that participate in the chain are called *responder* objects, inheriting from the `NSResponder` (OS X)/`UIResponder` (iOS) class. All view objects (`NSView`/`UIView`), view controller objects (`NSViewController`/`UIViewController`), window objects (`NSWindow`/`UIWindow`), and the application object (`NSApplication`/`UIApplication`) are responder objects.

Typically, when a view receives an event which it can't handle, it dispatches it to its superview until it reaches the view controller or window object. If the window can't handle the event, the event is dispatched to the application object, which is the last object in the chain. For example:

- On OS X, moving a textured window with the mouse can be done from any location (not just the title bar), unless on that location there's a view which handles dragging events, like slider controls. If no such view (or superview) is there, dragging events are sent up the chain to the window which does handle the dragging event.
- On iOS, it's typical to handle view events in the view controller which manages the view hierarchy, instead of subclassing the view itself. Since a view controller lies in the responder chain after all of its managed subviews, it can intercept any view events and handle them.
