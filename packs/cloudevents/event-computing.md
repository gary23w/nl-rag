---
title: "Event (computing)"
source: https://en.wikipedia.org/wiki/Event_(computing)
domain: cloudevents
license: CC-BY-SA-4.0
tags: cloudevents spec, cloud events format, event envelope format, portable event metadata
fetched: 2026-07-02
---

# Event (computing)

In computing, an **event** is a detectable occurrence or change in state that the system is designed to monitor, such as user input, hardware interrupt, system notification, or change in data or conditions. When associated with an event handler, an event triggers a response. The handler may run synchronously, where the execution thread is blocked until the event handler completes its processing, or asynchronously, where the event may be processed later. Even when synchronous handling appears to block execution, the underlying mechanism in many systems is still asynchronous, managed by the event loop.

Events can be implemented through various mechanisms such as callbacks, message objects, signals, or interrupts, and events themselves are distinct from the implementation mechanisms used. Event propagation models, such as bubbling, capturing, and pub/sub, define how events are distributed and handled within a system. Other key aspects include event loops, event queueing and prioritization, event sourcing, and complex event processing patterns. These mechanisms contribute to the flexibility and scalability of event-driven systems.

## Events vs. messages

In distributed systems, events represent a fact or state change (e.g., *OrderPlaced*) and are typically broadcast asynchronously to multiple consumers, promoting loose coupling and scalability. While events generally don't expect an immediate response, acknowledgment mechanisms are often implemented at the infrastructure level (e.g., Kafka commit offsets, SNS delivery statuses) rather than being an inherent part of the event pattern itself.

In contrast, messages serve a broader role, encompassing commands (e.g., *ProcessPayment*), events (e.g., *PaymentProcessed*), and documents (e.g., *DataPayload*). Both events and messages can support various delivery guarantees, including at-least-once, at-most-once, and exactly-once, depending on the technology stack and implementation. However, exactly-once delivery is often achieved through idempotency mechanisms rather than true, infrastructure-level exactly-once semantics.

Delivery patterns for both events and messages include publish/subscribe (one-to-many) and point-to-point (one-to-one). While request/reply is technically possible, it is more commonly associated with messaging patterns rather than pure event-driven systems. Events excel at state propagation and decoupled notifications, while messages are better suited for command execution, workflow orchestration, and explicit coordination.

Modern architectures commonly combine both approaches, leveraging events for distributed state change notifications and messages for targeted command execution and structured workflows based on specific timing, ordering, and delivery requirements.

## Event evolution strategies

In distributed systems, event evolution poses challenges, such as managing inconsistent event schemas across services and ensuring compatibility during gradual system updates. Event evolution strategies in event-driven architectures (EDA) can ensure that systems can handle changes to events without disruption. These strategies can include versioning events, such as semantic versioning or schema evolution, to maintain backward and forward compatibility. Adapters can translate events between old and new formats, ensuring consistent processing across components. These techniques can enable systems to evolve while remaining compatible and reliable in complex, distributed environments.

## Event semaphore

In computer science, an **event** (also called **event semaphore**) is a type of synchronization mechanism that is used to indicate to waiting processes when a particular condition has become true.

An event is an abstract data type with a Boolean state and the following operations:

- **wait** - when executed, causes the suspension of the executing process until the state of the event is set to true. If the state is already set to true before wait was called, wait has no effect.
- **set** - sets the event's state to true, release all waiting processes.
- **clear** - sets the event's state to false.

Different implementations of events may provide different subsets of these possible operations; for example, the implementation provided by Microsoft Windows provides the operations **wait** (WaitForObject and related functions), **set** (SetEvent), and **clear** (ResetEvent). An option that may be specified during creation of the event object changes the behaviour of SetEvent so that only a single thread is released and the state is automatically returned to false after that thread is released.

Events short of **reset** function, that is, those which can be completed only once, are known as futures. Monitors are, on the other hand, more general since they combine completion signaling with mutex and do not let the producer and consumer to execute simultaneously in the monitor making it an event+critical section.
