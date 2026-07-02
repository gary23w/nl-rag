---
title: "Actor model theory"
source: https://en.wikipedia.org/wiki/Actor_model_theory
domain: actor-semantics
license: CC-BY-SA-4.0
tags: actor model, actor semantics, asynchronous message, mailbox concurrency
fetched: 2026-07-02
---

# Actor model theory

In theoretical computer science, **Actor model theory** concerns theoretical issues for the Actor model.

Actors are the primitives that form the basis of the Actor model of concurrent digital computation. In response to a message that it receives, an Actor can make local decisions, create more Actors, send more messages, and designate how to respond to the next message received. Actor model theory incorporates theories of the events and structures of Actor computations, their proof theory, and denotational models.

## Events and their orderings

From the definition of an Actor, it can be seen that numerous events take place: local decisions, creating Actors, sending messages, receiving messages, and designating how to respond to the next message received.

However, this article focuses on just those events that are the arrival of a message sent to an Actor.

This article reports on the results published in Hewitt [2006].

Law of Countability

: There are at most countably many events.

### Activation ordering

The activation ordering (`-≈→`) is a fundamental ordering that models one event activating another (there must be energy flow in the message passing from an event to an event which it activates).

- Because of the transmission of energy, the activation ordering is *relativistically invariant*; that is, for all events `e1`.`e2`, if `e1 -≈→ e2`, then the time of `e1` precedes the time of `e2` in the relativistic frames of reference of all observers.
- *Law of Strict Causality for the Activation Ordering*: For no event does `e -≈→ e`.
- *Law of Finite Predecession in the Activation Ordering*: For all events `e1` the set `{e|e -≈→ e1}` is finite.

### Arrival orderings

The arrival ordering of an Actor `x` ( `-x→`) models the (total) ordering of events in which a message arrives at `x`. Arrival ordering is determined by *arbitration* in processing messages (often making use of a digital circuit called an arbiter). The arrival events of an Actor are on its world line. The arrival ordering means that the Actor model inherently has indeterminacy (see Indeterminacy in concurrent computation).

- Because all of the events of the arrival ordering of an actor `x` happen on the world line of `x`, the arrival ordering of an actor is *relativistically invariant*. *I.e.*, for all actors `x` and events `e1`.`e2`, if `e1 -x→ e2`, then the time of `e1` precedes the time of `e2` in the relativistic frames of reference of all observers.
- *Law of Finite Predecession in Arrival Orderings*: For all events `e1` and Actors `x` the set `{e|e -x→ e1}` is finite.

### Combined ordering

The combined ordering (denoted by `→`) is defined to be the transitive closure of the activation ordering and the arrival orderings of all Actors.

- The combined ordering is relativistically invariant because it is the transitive closure of relativistically invariant orderings. *I.e.*, for all events `e1`.`e2`, if `e1→e2`. then the time of `e1` precedes the time of `e2` in the relativistic frames of reference of all observers.
- *Law of Strict Causality for the Combined Ordering*: For no event does `e→e`.

The combined ordering is obviously transitive by definition.

In [Baker and Hewitt 197?], it was conjectured that the above laws might entail the following law:

Law of Finite Chains Between Events in the Combined Ordering

: There are no infinite chains (

i.e.

, linearly ordered sets) of events between two events in the combined ordering →.

### Independence of the Law of Finite Chains Between Events in the Combined Ordering

However, [Clinger 1981] surprisingly proved that the Law of Finite Chains Between Events in the Combined Ordering is independent of the previous laws, *i.e.*,

Theorem. *The Law of Finite Chains Between Events in the Combined Ordering does not follow from the previously stated laws.*

Proof. It is sufficient to show that there is an Actor computation that satisfies the previously stated laws but violates the Law of Finite Chains Between Events in the Combined Ordering.

Consider a computation which begins when an actor

Initial

is sent a

Start

message causing it to take the following actions

1. Create a new actor *Greeter1* which is sent the message `SayHelloTo` with the address of *Greeter1*
2. Send *Initial* the message `Again` with the address of *Greeter1*

Thereafter the behavior of

Initial

is as follows on receipt of an

Again

message with address

Greeter

i

(which we will call the event

Again

i

):

1. Create a new actor *Greeteri+1* which is sent the message `SayHelloTo` with address *Greeteri*
2. Send *Initial* the message `Again` with the address of *Greeteri+1*

Obviously the computation of

Initial

sending itself

Again

messages never terminates.

The behavior of each Actor

Greeter

i

is as follows:

- When it receives a message `SayHelloTo` with address *Greeteri-1* (which we will call the event `**SayHelloToi**`), it sends a `Hello` message to *Greeteri-1*
- When it receives a `Hello` message (which we will call the event `**Helloi**`), it does nothing.

Now it is possible that

Hello

i

-

Greeter

i

→

SayHelloTo

i

every time and therefore

Hello

i

→

SayHelloTo

i

.

Also

Again

i

-≈→

Again

i+1

every time and therefore

Again

i

→

Again

i+1

.

Furthermore all of the laws stated before the Law of Strict Causality for the Combined Ordering are satisfied.

However, there may be an infinite number of events in the combined ordering between

Again

1

and

SayHelloTo

1

as follows:

Again

1

→...→

Again

i

→...

$\infty$

...→

Hello

i

→

SayHelloTo

i

→...→

Hello

1

→

SayHelloTo

1

However, we know from physics that infinite energy cannot be expended along a finite trajectory. Therefore, since the Actor model is based on physics, the Law of Finite Chains Between Events in the Combined Ordering was taken as an axiom of the Actor model.

### Law of Discreteness

The Law of Finite Chains Between Events in the Combined Ordering is closely related to the following law:

Law of Discreteness

: For all events

e

1

and

e

2

, the set

{e|e

1

→e→e

2

}

is finite.

In fact the previous two laws have been shown to be equivalent:

Theorem [Clinger 1981].

The Law of Discreteness is equivalent to the Law of Finite Chains Between Events in the Combined Ordering

(without using the

axiom of choice

.)

The law of discreteness rules out Zeno machines and is related to results on Petri nets [Best *et al.* 1984, 1987].

The Law of Discreteness implies the property of unbounded nondeterminism. The combined ordering is used by [Clinger 1981] in the construction of a denotational model of Actors (see denotational semantics).

## Denotational semantics

Clinger [1981] used the Actor event model described above to construct a denotational model for Actors using power domains. Subsequently, Hewitt [2006] augmented the diagrams with arrival times to construct a technically simpler denotational model that is easier to understand.
