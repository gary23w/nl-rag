---
title: "Signals and slots"
source: https://en.wikipedia.org/wiki/Signals_and_slots
domain: pyqt-binding
license: CC-BY-SA-4.0
tags: pyqt binding, python qt wrapper, sip generated binding, qt widgets python
fetched: 2026-07-02
---

# Signals and slots

**Signals and slots** is a language construct introduced in Qt for communication between objects which makes it easy to implement the observer pattern while avoiding boilerplate code. The concept is that GUI widgets, and other objects, can send signals containing event information which can be received by other objects using special member functions known as slots. This is similar to C/C++ function pointers, but the signal/slot system ensures the type-correctness of callback arguments.

The signal/slot system fits well with the way graphical user interfaces are designed. Similarly, the signal/slot system can be used for other non-GUI usages, for example asynchronous I/O (including sockets, pipes, serial devices, etc.) event notification or to associate timeout events with appropriate object instances and methods or functions. It is easy to use and no registration/deregistration/invocation code need to be written, because Qt's metaobject compiler (MOC) automatically generates the needed infrastructure.

A spreadsheet programs update system could be implemented using signals and slots such that when a cell is changed, its dependent cells are notified/updated.

## Alternative implementations

There are some implementations of signal/slot systems based on C++ templates, which don't require the extra metaobject compiler, as used by Qt, such as libsigc++, sigslot, vdk-signals, nano-signal-slot, neosigslot, Signals, boost.signals2, Synapse, Cpp::Events, Platinum, JBroadcaster and KDBindings. Common Language Infrastructure (CLI) languages such as C# also supports a similar construct although with a different terminology and syntax: events play the role of signals, and delegates are the slots. Another implementation of signals exists for ActionScript 3.0, inspired by C# events and signals/slots in Qt. Additionally, a delegate can be a local variable, much like a function pointer, while a slot in Qt must be a class member declared as such. The C based GObject system also provides similar functionality via GSignal. In D it is implemented by std.signals.
