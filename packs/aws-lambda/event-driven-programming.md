---
title: "Event-driven programming"
source: https://en.wikipedia.org/wiki/Event-driven_programming
domain: aws-lambda
license: CC-BY-SA-4.0
tags: aws lambda, serverless function, lambda function, function as a service
fetched: 2026-07-02
---

# Event-driven programming

In computer programming, **event-driven programming** is a programming paradigm in which the flow of the program is determined by external events. User interface (UI) events from keyboards and mice, touchpads and touchscreens, and external sensor inputs are common cases. Events may also be programmatically generated, such as from messages from other programs, notifications from other threads, or other network events.

Event-driven programming is the dominant paradigm used in graphical user interface (GUI) applications and network servers.

In an event-driven application, there is generally an event loop that listens for events and then triggers a callback function when one of those events is detected.

Event-driven programs can be written in any programming language, although the task is easier in languages that provide high-level abstractions.

Although they do not exactly fit the event-driven model, interrupt handling and exception handling have many similarities.

It is important to differentiate between event-driven and message-driven (aka queue-driven) paradigms: event-driven services (e.g. AWS SNS) are decoupled from their consumers, whereas message/queue-driven services (e.g. AWS SQS) are coupled with their consumers.

## Event loop

Because the event loop that retrieves and dispatches events is common amongst applications, many programming frameworks provide an implementation of an event loop, and the application developer only needs to write the event handlers.

RPG, an early programming language from IBM, whose 1960s design concept was similar to event-driven programming discussed above, provided a built-in main I/O loop (known as the "program cycle") where the calculations responded in accordance with "indicators" (flags) that were set earlier in the cycle.

### Event handlers

The actual logic is contained in event handler routines. These routines handle the events to which the main program will respond. For example, a single mouse-click on a "Save" command button in a GUI program might trigger a routine to save data to a database. An "Exit" button might trigger a routine to exit the program. The event loop receives events from all such command buttons and other GUI elements, dispatching the appropriate event handler routine for each button.

Event handler routines need to be bound to specific events, so the event loop can dispatch the correct routine in response to the event. Many IDEs simplify this process by providing the programmer with an event handling template for each specific event (such as a button click), allowing the programmer to focus on writing the event-handling code.

In a sequential program, keeping track of execution order and history is normally trivial. But in an event-driven program, event handlers execute non-sequentially in response to external events. Special attention and planning is required to correctly structure the event handlers to work when called in any order.

## Common uses

Most existing GUI architectures use event-driven programming. Windows has the message loop. The Java AWT framework processes all UI changes on a single thread, called the Event dispatching thread. Similarly, all UI updates in the Java framework JavaFX occur on the JavaFX Application Thread.

Most network servers and frameworks such as Node.js are also event-driven.

## Interrupt and exception handling
