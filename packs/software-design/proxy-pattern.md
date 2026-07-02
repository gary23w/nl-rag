---
title: "Proxy pattern"
source: https://en.wikipedia.org/wiki/Proxy_pattern
domain: software-design
license: CC-BY-SA-4.0
tags: design pattern, software architecture, software design, refactoring
fetched: 2026-07-02
---

# Proxy pattern

In computer programming, the **proxy pattern** is a software design pattern which is a class functioning as an interface to something else. The proxy could interface to anything: a network connection, a large object in memory, a file, or some other resource that is expensive or impossible to duplicate. In short, a proxy is a wrapper or agent object that is being called by the client to access the real serving object behind the scenes. Use of the proxy can simply be forwarding to the real object, or can provide additional logic. In the proxy, extra functionality can be provided, for example caching when operations on the real object are resource intensive, or checking preconditions before operations on the real object are invoked. For the client, usage of a proxy object is similar to using the real object, because both implement the same interface.

## Overview

The proxy design pattern is one of the twenty-three well-known *GoF design patterns* that describe how to solve recurring design problems to design flexible and reusable object-oriented software, that is, objects that are easier to implement, change, test, and reuse.

### Problem

The proxy design pattern is used to solve such problems:

- The access to an object should be controlled.
- Additional functionality should be provided when accessing an object.

When accessing sensitive objects, for example, it should be possible to check that clients have the needed access rights.

### Solution

Define a separate `Proxy` object that

- can be used as a substitute for another object (`Subject`), and
- implements additional functionality to control the access to this subject.

This makes it possible to work through a `Proxy` object to perform additional functionality when accessing a subject, like checking the access rights of clients accessing a sensitive object.

To act as a substitute for a subject, a proxy must implement the `Subject` interface. Clients can't tell whether they work with a subject or its proxy.

See also the UML class and sequence diagram below.

## Structure

### UML class and sequence diagram

In the above UML class diagram, the `Proxy` class implements the `Subject` interface so that it can act as substitute for `Subject` objects. It maintains a reference (`realSubject`) to the substituted object (`RealSubject`) so that it can forward requests to it (`realSubject.operation()`).

The sequence diagram shows the run-time interactions: The `Client` object works through a `Proxy` object that controls the access to a `RealSubject` object. In this example, the `Proxy` forwards the request to the `RealSubject`, which performs the request.

### Class diagram

## Possible usage scenarios

### Remote proxy

In distributed object communication, a local object represents a remote object (one that belongs to a different address space). The local object is a proxy for the remote object, and method invocation on the local object results in remote method invocation on the remote object. An example would be an ATM implementation, where the ATM might hold proxy objects for bank information that exists in the remote server.

### Virtual proxy

In place of a complex or heavy object, a skeleton representation may be advantageous in some cases. When an underlying image is huge in size, it may be represented using a virtual proxy object, loading the real object on demand.

### Protection proxy

A protection proxy might be used to control access to a resource based on access rights.

## Example

The following is an example of the proxy design pattern in C++:

```mw
import std;

using std::string;
using std::unique_ptr;

// Subject Interface
class Image {
public:
    virtual void display() const = 0;
    virtual ~Image() = default;
};

// Real Subject (expensive to load)
class RealImage : public Image {
private:
    string filename;
public:
    explicit RealImage(const string& file):
        filename{file} {
        loadFromDisk();
    }

    void display() const override {
        std::println("Displaying image: {}", filename);
    }

private:
    void loadFromDisk() const {
        std::println("Loading image from disk: {}", filename);
    }
};

// Proxy (controls access to RealImage)
class ProxyImage : public Image {
private:
    string filename;
    mutable unique_ptr<RealImage> realImage; // lazily created
public:
    explicit ProxyImage(const string& file):
        filename{file} {}

    void display() const override {
        if (!realImage) {
            std::println("(Proxy) Loading image on demand...");
            realImage = std::make_unique<RealImage>(filename);
        }
        realImage->display();
    }
};

// Client code
int main() {
    Image* img = new ProxyImage("photo.png");

    // First display (should load)
    img->display();

    // Second display (should use cached image)
    img->display();

    delete img;
    return 0;
}
```
