---
title: "Lamport timestamp"
source: https://en.wikipedia.org/wiki/Lamport_timestamp
domain: distributed-systems
license: CC-BY-SA-4.0
tags: distributed system, distributed computing, cap theorem, consistency model, eventual consistency
fetched: 2026-07-02
---

# Lamport timestamp

The **Lamport timestamp** algorithm is a simple logical clock algorithm used to determine the order of events in a distributed computer system. As different nodes or processes will typically not be perfectly synchronized, this algorithm is used to provide a partial ordering of events with minimal overhead, and conceptually provide a starting point for the more advanced vector clock method. The algorithm is named after its creator, Leslie Lamport.

Distributed algorithms such as resource synchronization often depend on some method of ordering events to function. For example, consider a system with two processes and a disk. The processes send messages to each other, and also send messages to the disk requesting access. The disk grants access in the order the messages were *received*. For example process A sends a message to the disk requesting write access, and then sends a read instruction message to process B . Process B receives the message, and as a result sends its own read request message to the disk. If there is a timing delay causing the disk to receive both messages at the same time, it can determine which message *happened-before* the other: A *happens-before* B if one can get from A to B by a sequence of moves of two types: moving forward while remaining in the same process, and following a message from its sending to its reception. A logical clock algorithm provides a mechanism to determine facts about the order of such events. Note that if two events happen in different processes that do not exchange messages directly or indirectly via third-party processes, then we say that the two processes are concurrent, that is, nothing can be said about the ordering of the two events.

Lamport invented a simple mechanism by which the *happened-before* ordering can be captured numerically. A Lamport logical clock is a numerical software counter value maintained in each process.

Conceptually, this logical clock can be thought of as a clock that only has meaning in relation to messages moving between processes. When a process receives a message, it re-synchronizes its logical clock with that sender. The above-mentioned vector clock is a generalization of the idea into the context of an arbitrary number of parallel, independent processes.

## Algorithm

The algorithm follows some simple rules:

1. A process increments its counter before each local event (e.g., message sending event);
2. When a process sends a message, it includes its counter value with the message after executing step 1;
3. On receiving a message, the counter of the recipient is updated, if necessary, to the greater of its current counter and the timestamp in the received message. The counter is then incremented by 1 before the message is considered received.

In pseudocode, the algorithm for sending is:

```
# event is known
time = time + 1;
# event happens
send(message, time);
```

The algorithm for receiving a message is:

```
(message, timestamp) = receive();
time = max(timestamp, time) + 1;
```

## Considerations

For every two different events a and b occurring in the same process, and $C(x)$ being the timestamp for a certain event x , it is necessary that $C(a)$ never equals $C(b)$ .

Therefore it is necessary that:

- The logical clock be set so that there is a minimum of one clock "tick" (increment of the counter) between events a and b ;
- In a multi-process or multi-threaded environment, it might be necessary to attach the process ID (PID) or any other unique ID to the timestamp so that it is possible to differentiate between events a and b which may occur simultaneously in different processes.

## Causal ordering

For any two events, a and b , if there is any way that a could have influenced b , then the Lamport timestamp of a will be less than the Lamport timestamp of b . It’s also possible to have two events where we can’t say which came first; when that happens, it means that they couldn’t have affected each other. If a and b can’t have any effect on each other, then it doesn’t matter which one came first.

## Implications

A Lamport clock may be used to create a partial ordering of events between processes. Given a logical clock following these rules, the following relation is true: if $a\rightarrow b$ then $C(a)<C(b)$ , where $\rightarrow \,$ means *happened-before*.

This relation only goes one way, and is called the *clock consistency condition*: if one event comes before another, then that event's logical clock comes before the other's. The *strong clock consistency condition*, which is two way (if $C(a)<C(b)$ then $a\rightarrow b$ ), can be obtained by other techniques such as vector clocks. Using only a simple Lamport clock, only a partial causal ordering can be inferred from the clock.

However, via the contrapositive, it's true that $C(a)\nless C(b)$ implies $a\nrightarrow b$ . So, for example, if $C(a)\geq C(b)$ then a cannot have *happened-before* b .

Another way of putting this is that $C(a)<C(b)$ means that a may have *happened-before* b , or be incomparable with b in the *happened-before* ordering, but a did not happen after b .

Nevertheless, Lamport timestamps can be used to create a total ordering of events in a distributed system by using some arbitrary mechanism to break ties (e.g., the ID of the process). The caveat is that this ordering is artificial and cannot be depended on to imply a causal relationship.

## Lamport's logical clock in distributed systems

In a distributed system, it is not possible in practice to synchronize time across entities (typically thought of as processes) within the system; hence, the entities can use the concept of a logical clock based on the events through which they communicate.

If two entities do not exchange any messages, then they probably do not need to share a common clock; events occurring on those entities are termed concurrent events.

Among the processes on the same local machine we can order the events based on the local clock of the system.

When two entities communicate by message passing, then the send event is said to *happen-before* the receive event, and the logical order can be established among the events.

A distributed system is said to have partial order if we can have a partial order relationship among the events in the system. If "totality", i.e., causal relationship among all events in the system, can be established, then the system is said to have total order.

A single entity cannot have two events occur simultaneously. If the system has total order we can determine the order among all events in the system. If the system has partial order between processes, which is the type of order Lamport's logical clock provides, then we can only tell the ordering between entities that interact. Lamport addressed ordering two events with the same timestamp (or counter): "To break ties, we use any arbitrary total ordering < of the processes." Thus two timestamps or counters may be the same within a distributed system, but in applying the logical clocks algorithm events that occur will always maintain at least a strict partial ordering.

Lamport clocks lead to a situation where all events in a distributed system are totally ordered. That is, if $a\rightarrow b$ , then we can say a actually happened before b .

Note that with Lamport’s clocks, nothing can be said about the actual time of a and b . If the logical clock says $C(a)<C(b)$ , that does not mean in reality that a actually happened before b in terms of real time.

Lamport clocks show non-causality, but do not capture all causality. Knowing $a\rightarrow c$ and $b\rightarrow c$ shows c did not cause a or b but we cannot say which initiated c .

This kind of information can be important when trying to replay events in a distributed system (such as when trying to recover after a crash). If one node goes down, and we know the causal relationships between messages, then we can replay those messages and respect the causal relationship to get that node back up to the state it needs to be in.

## Alternatives to potential causality

The happened-before relation captures potential causality, not true causality. In 2011–2012, Munindar Singh proposed a declarative, multiagent approach based on true causality called information protocols. An information protocol specifies the constraints on communications between the agents that constitute a distributed system. However, instead of specifying message ordering (e.g., via a state machine, a common way of representing protocols in computing), an information protocol specifies the information dependencies between the communications that agents (the protocol's endpoints) may send. An agent may send a communication in a local state (its communication history) only if the communication and the state together satisfy the relevant information dependencies. For example, an information protocol for an e-commerce application may specify that to send a quote with parameters ID (a uniquifier), item, and price, seller must already know the ID and item from its state but can generate whatever price it wants. A remarkable thing about information protocols is that although emissions are constrained, receptions are not. Specifically, agents may receive communications in any order whatsoever – receptions simply bring information and there is no point delaying them. This means that information protocols can be enacted over unordered communication services such as UDP.

The bigger idea is that of application semantics, the idea of designing distributed systems based on the content of the messages, an idea implicated in the end-to-end principle. Current approaches largely ignore semantics and focus on providing application-agnostic ("syntactic") message delivery and ordering guarantees in communication services, which is where ideas like potential causality help. But if we had a suitable way of doing application semantics, then we wouldn't need such communication services. An unordered, unreliable communication service would suffice. The real value of the information protocols approach is that it provides the foundations for an application semantics approach.
