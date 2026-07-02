---
title: "History of the Actor model"
source: https://en.wikipedia.org/wiki/History_of_the_Actor_model
domain: actor-semantics
license: CC-BY-SA-4.0
tags: actor model, actor semantics, asynchronous message, mailbox concurrency
fetched: 2026-07-02
---

# History of the Actor model

In computer science, the Actor model, first published in 1973, is a mathematical model of concurrent computation.

## Event orderings versus global state

A fundamental challenge in defining the Actor model is that it did not provide for global states so that a computational step could not be defined as going from one global state to the next global state as had been done in all previous models of computation.

In 1963 in the field of Artificial Intelligence, John McCarthy introduced situation variables in logic in the Situational Calculus. In McCarthy and Hayes 1969, a situation is defined as "the complete state of the universe at an instant of time." In this respect, the situations of McCarthy are not suitable for use in the Actor model since it has no global states.

From the definition of an Actor, it can be seen that numerous events take place: local decisions, creating Actors, sending messages, receiving messages, and designating how to respond to the next message received. Partial orderings on such events have been axiomatized in the Actor model and their relationship to physics explored (see Actor model theory).

## Relationship to physics

According to Hewitt (2006), the Actor model is based on physics in contrast with other models of computation that were based on mathematical logic, set theory, algebra, *etc.* Physics influenced the Actor model in many ways, especially quantum physics and relativistic physics. One issue is what can be observed about Actor systems. The question does not have an obvious answer because it poses both theoretical and observational challenges similar to those that had arisen in constructing the foundations of quantum physics. In concrete terms for Actor systems, typically we cannot observe the details by which the arrival order of messages for an Actor is determined (see Indeterminacy in concurrent computation). Attempting to do so affects the results and can even push the indeterminacy elsewhere. *e.g.*, see metastability in electronics. Instead of observing the insides of arbitration processes of Actor computations, we await the outcomes.

## Models prior to the Actor model

The Actor model builds on previous models of computation.

### Lambda calculus

The lambda calculus of Alonzo Church can be viewed as the earliest message passing programming language (see Hewitt, Bishop, and Steiger 1973; Abelson and Sussman 1985). For example, the lambda expression below implements a tree data structure when supplied with parameters for a leftSubTree and rightSubTree. When such a tree is given a parameter message "getLeft", it returns leftSubTree and likewise when given the message "getRight" it returns rightSubTree.

```
 λ(leftSubTree,rightSubTree)
   λ(message)
     if (message == "getLeft") then leftSubTree
     else if (message == "getRight") then rightSubTree
```

However, the semantics of the lambda calculus were expressed using variable substitution in which the values of parameters were substituted into the body of an invoked lambda expression. The substitution model is unsuitable for concurrency because it does not allow the capability of sharing of changing resources. Inspired by the lambda calculus, the interpreter for the programming language Lisp made use of a data structure called an environment so that the values of parameters did not have to be substituted into the body of an invoked lambda expression. This allowed for sharing of the effects of updating shared data structures but did not provide for concurrency.

### Simula

Simula 67 pioneered using message passing for computation, motivated by discrete event simulation applications. These applications had become large and unmodular in previous simulation languages. At each time step, a large central program would have to go through and update the state of each simulation object that changed depending on the state of whichever simulation objects it interacted with on that step. Kristen Nygaard and Ole-Johan Dahl developed the idea (first described in an IFIP workshop in 1967) of having methods on each object that would update its own local state based on messages from other objects. In addition they introduced a class structure for objects with inheritance. Their innovations considerably improved the modularity of programs.

However, Simula used coroutine control structure instead of true concurrency.

### Smalltalk

Alan Kay was influenced by message passing in the pattern-directed invocation of Planner in developing Smalltalk-71. Hewitt was intrigued by Smalltalk-71 but was put off by the complexity of communication that included invocations with many fields including *global*, *sender*, *receiver*, *reply-style*, *status*, *reply*, *operator selector*, *etc.*

In 1972 Kay visited MIT and discussed some of his ideas for Smalltalk-72 building on the Logo work of Seymour Papert and the "little person" model of computation used for teaching children to program. However, the message passing of Smalltalk-72 was quite complex. Code in the language was viewed by the interpreter as simply a stream of tokens. As Dan Ingalls later described it:

The first (token) encountered (in a program) was looked up in the dynamic context, to determine the receiver of the subsequent message. The name lookup began with the class dictionary of the current activation. Failing there, it moved to the sender of that activation and so on up the sender chain. When a binding was finally found for the token, its value became the receiver of a new message, and the interpreter activated the code for that object's class.

Thus the message-passing model in Smalltalk-72 was closely tied to a particular machine model and programming-language syntax that did not lend itself to concurrency. Also, although the system was bootstrapped on itself, the language constructs were not formally defined as objects that respond to **Eval** messages (see discussion below). This led some to believe that a new mathematical model of concurrent computation based on message passing should be simpler than Smalltalk-72.

Subsequent versions of the Smalltalk language largely followed the path of using the virtual methods of Simula in the message-passing structure of programs. However Smalltalk-72 made primitives such as integers, floating point numbers, *etc.* into objects. The authors of Simula had considered making such primitives into objects but refrained largely for efficiency reasons. Java at first used the expedient of having both primitive and object versions of integers, floating point numbers, *etc.* The C# programming language (and later versions of Java, starting with Java 1.5) adopted using *boxing* and *unboxing*, a variant of which had been used earlier in some Lisp implementations.

The Smalltalk system went on to become very influential, innovating in bitmap displays, personal computing, the class browser interface, and many other ways. For details see Kay's *The Early History of Smalltalk*. Meanwhile, the Actor efforts at MIT remained focused on developing the science and engineering of higher level concurrency. (See the paper by Jean-Pierre Briot for ideas that were developed later on how to incorporate some kinds of Actor concurrency into later versions of Smalltalk.)

### Petri nets

Prior to the development of the Actor model, Petri nets were widely used to model nondeterministic computation. However, they were widely acknowledged to have an important limitation: they modeled control flow but not data flow. Consequently, they were not readily composable, thereby limiting their modularity. Hewitt pointed out another difficulty with Petri nets: simultaneous action. *I.e.*, the atomic step of computation in Petri nets is a transition in which tokens *simultaneously* disappear from the input places of a transition and appear in the output places. The physical basis of using a primitive with this kind of simultaneity seemed questionable to him. Despite these apparent difficulties, Petri nets continue to be a popular approach to modelling concurrency, and are still the subject of active research.

### Threads, locks, and buffers (channels)

Prior to the Actor model, concurrency was defined in low-level machine terms of threads, locks and buffers(channels). It certainly is the case that implementations of the Actor model typically make use of these hardware capabilities. However, there is no reason that the model could not be implemented directly in hardware without exposing any hardware threads and locks. Also, there is no necessary relationship between the number of Actors, threads, and locks that might be involved in a computation. Implementations of the Actor model are free to make use of threads and locks in any way that is compatible with the laws for Actors.

## Abstracting away implementation details

An important challenge in defining the Actor model was to abstract away implementation details.

For example, consider the following question: "Does each Actor have a queue in which its communications are stored until received by the Actor to be processed?" Carl Hewitt argued against including such queues as an integral part of the Actor model. One consideration was that such queues could themselves be modeled as Actors that received messages to enqueue and dequeue the communications. Another consideration was that some Actors would not use such queues in their actual implementation. *E.g.,* an Actor might have a network of arbiters instead. Of course, there is a mathematical abstraction which is the *sequence* of communications that have been received by an Actor. But this sequence emerged only as the Actor operated. In fact the ordering of this sequence can be indeterminate (see Indeterminacy in concurrent computation).

Another example of abstracting away implementation detail was the question of interpretation: "Should interpretation be an integral part of the Actor model?" The idea of interpretation is that an Actor would be defined by how its program script processed eval messages. (In this way Actors would be defined in a manner analogous to Lisp which was "defined" by a meta-circular interpreter procedure named eval written in Lisp.) Hewitt argued against making interpretation integral to the Actor model. One consideration was that to process the eval messages, the program script of an Actor would itself have a program script (which in turn would have ...)! Another consideration was that some Actors would not use interpretation in their actual interpretation. *E.g.,* an Actor might be implemented in hardware instead. Of course there is nothing wrong with interpretation *per se*. Also implementing interpreters using eval messages is more modular and extensible than the monolithic interpreter approach of Lisp.

## Operational model

Nevertheless, progress developing the model was steady. In 1975, Irene Greif published the first operational model in her dissertation.

## Scheme

Gerald Sussman and Guy Steele then took an interest in Actors and published a paper on their Scheme interpreter in which they concluded "we discovered that the 'actors' and the lambda expressions were identical in implementation." According to Hewitt, the lambda calculus is capable of expressing some kinds of parallelism but, in general, *not* the concurrency expressed in the Actor model. On the other hand, the Actor model is capable of expressing all of the parallelism in the lambda calculus.

## Laws for Actors

Two years after Greif published her operational model, Carl Hewitt and Henry Baker published the Laws for Actors.

## Proof of continuity of computable functions

Using the laws of the Actor model, Hewitt and Baker proved that any Actor that behaves like a function is continuous in the sense defined by Dana Scott (see denotational semantics).

## Specifications and proofs

Aki Yonezawa published his specification and verification techniques for Actors. Russ Atkinson and Carl Hewitt published a paper on specification and proof techniques for serializers providing an efficient solution to encapsulating shared resources for concurrency control.

## Mathematical characterization using domain theory

Finally eight years after the first Actor publication, Will Clinger (building on the work of Irene Greif 1975, Gordon Plotkin 1976, Michael Smyth 1978, Henry Baker 1978, Francez, Hoare, Lehmann, and de Roever 1979, and Milne and Milnor 1979) published the first satisfactory mathematical denotational model incorporating unbounded nondeterminism using domain theory in his dissertation in 1981 (see Clinger's model). Subsequently, Hewitt [2006] augmented the diagrams with arrival times to construct a technically simpler denotational model that is easier to understand. See History of denotational semantics.
