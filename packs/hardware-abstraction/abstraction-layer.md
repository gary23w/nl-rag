---
title: "Abstraction layer"
source: https://en.wikipedia.org/wiki/Abstraction_layer
domain: hardware-abstraction
license: CC-BY-SA-4.0
tags: hardware abstraction, embedded systems
fetched: 2026-07-02
---

# Abstraction layer

In computing, an **abstraction layer** or **abstraction level** is a way of hiding the working details of a subsystem. Examples of software models that use layers of abstraction include the OSI model for network protocols, OpenGL, and other graphics libraries, which allow the separation of concerns to facilitate interoperability and platform independence.

In computer science, an abstraction layer is a generalization of a conceptual model or algorithm, away from any specific implementation. These generalizations arise from broad similarities that are best encapsulated by models that express similarities present in various specific implementations. The simplification provided by a good abstraction layer allows for easy reuse by distilling a useful concept or design pattern so that situations, where it may be accurately applied, can be quickly recognized. Just composing lower-level elements into a construct doesn't count as an abstraction layer unless it shields users from its underlying complexity.

A layer is considered to be on top of another if it depends on it. Every layer can exist without the layers above it, and requires the layers below it to function. Frequently, abstraction layers can be composed into a hierarchy of abstraction levels. The OSI model comprises seven abstraction layers. Each layer of the model encapsulates and addresses a different part of the needs of digital communications, thereby reducing the complexity of the associated engineering solutions.

A famous aphorism of David Wheeler is, "All problems in computer science can be solved by another level of indirection." This is often deliberately misquoted with "abstraction" substituted for "indirection." It is also sometimes misattributed to Butler Lampson. Kevlin Henney's corollary to this is, "...except for the problem of too many layers of indirection."

## Computer architecture

In a computer architecture, a computer system is usually represented as consisting of several abstraction levels, such as:

- software
- programmable logic
- hardware

Programmable logic is often considered part of the hardware, while the logical definitions are also sometimes seen as part of a device's software or firmware. Firmware may include only low-level software, but can also include all software, including an operating system and applications. The software layers can be further divided into hardware abstraction layers, physical and logical device drivers, repositories such as filesystems, operating system kernels, middleware, applications, and others. A distinction can also be made between low-level programming languages like VHDL, machine language, assembly language and a compiled language, interpreter, or script language.

## Input and output

In the Unix operating system, most types of input and output operations are considered to be streams of bytes read from a device or written to a device. This stream of bytes model is used for file I/O, socket I/O, and terminal I/O in order to provide device independence. In order to read and write to a device at the application level, the program calls a function to open the device, which may be a real device, such as a terminal or a virtual device, such as a network port or a file in a file system. The device's physical characteristics are mediated by the operating system, which in turn presents an abstract interface that allows the programmer to read and write bytes from/to the device. The operating system then performs the actual transformation needed to read and write the stream of bytes to the device.

## Graphics

Most graphics libraries, such as OpenGL, provide an abstract graphical device model as an interface. The library is responsible for translating the commands provided by the programmer into the specific device commands needed to draw the graphical elements and objects. The specific device commands for a plotter are different from the device commands for a CRT monitor, but the graphics library hides the implementation and device-dependent details by providing an abstract interface that provides a set of primitives that are generally useful for drawing graphical objects.
