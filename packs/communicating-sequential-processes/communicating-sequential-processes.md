---
title: "Communicating sequential processes"
source: https://en.wikipedia.org/wiki/Communicating_sequential_processes
domain: communicating-sequential-processes
license: CC-BY-SA-4.0
tags: communicating sequential processes, message passing, rendezvous synchronization, channel communication
fetched: 2026-07-02
---

# Communicating sequential processes

In computer science, **communicating sequential processes** (**CSP**) is a formal language for describing patterns of interaction in concurrent systems. It is a member of the family of mathematical theories of concurrency known as process algebras, or process calculi, based on message passing via channels. CSP was highly influential in the design of the occam programming language and also influenced the design of programming languages such as Limbo, RaftLib, Erlang, Go, Crystal, and Clojure's core.async.

CSP was first described by Tony Hoare in a 1978 article, and has since evolved substantially. CSP has been practically applied in industry as a tool for specifying and verifying the concurrent aspects of a variety of different systems, such as the T9000 Transputer, as well as a secure e-commerce system. The theory of CSP itself is also still the subject of active research, including work to increase its range of practical applicability (e.g., increasing the scale of the systems that can be tractably analyzed).

## History

### Original version

The version of CSP presented in Hoare's original 1978 article was essentially a concurrent programming language rather than a process calculus. It had a substantially different syntax than later versions of CSP, did not possess mathematically defined semantics, and was unable to represent unbounded nondeterminism. Programs in the original CSP were written as a parallel composition of a fixed number of sequential processes communicating with each other strictly through synchronous message-passing. In contrast to later versions of CSP, each process was assigned an explicit name, and the source or destination of a message was defined by specifying the name of the intended sending or receiving process. For example, the process

```
COPY = *[c:character; west?c → east!c]
```

repeatedly receives a character from the process named `west` and sends that character to process named `east`. The parallel composition

```
[west::DISASSEMBLE || X::COPY || east::ASSEMBLE]
```

assigns the names `west` to the `DISASSEMBLE` process, `X` to the `COPY` process, and `east` to the `ASSEMBLE` process, and executes these three processes concurrently.

### Development into process algebra

Following the publication of the original version of CSP, Hoare, Stephen Brookes, and A. W. Roscoe developed and refined the *theory* of CSP into its modern, process algebraic form. The approach taken in developing CSP into a process algebra was influenced by Robin Milner's work on the Calculus of Communicating Systems (CCS) and conversely. The theoretical version of CSP was initially presented in a 1984 article by Brookes, Hoare, and Roscoe, and later in Hoare's book *Communicating Sequential Processes*, which was published in 1985. In September 2006, that book was still the third-most cited computer science reference of all time according to Citeseer (albeit an unreliable source due to the nature of its sampling). The theory of CSP has undergone a few minor changes since the publication of Hoare's book. Most of these changes were motivated by the advent of automated tools for CSP process analysis and verification. Roscoe's *The Theory and Practice of Concurrency* describes this newer version of CSP.

### Applications

An early and important application of CSP was its use for specification and verification of elements of the INMOS T9000 Transputer, a complex superscalar pipelined processor designed to support large-scale multiprocessing. CSP was employed in verifying the correctness of both the processor pipeline and the Virtual Channel Processor, which managed off-chip communications for the processor.

Industrial application of CSP to software design has usually focused on dependable and safety-critical systems. For example, the Bremen Institute for Safe Systems and Daimler-Benz Aerospace modeled a fault-management system and avionics interface (consisting of about 23,000 lines of code) intended for use on the International Space Station in CSP, and analyzed the model to confirm that their design was free of deadlock and livelock. The modeling and analysis process was able to uncover a number of errors that would have been difficult to detect using testing alone. Similarly, Praxis High Integrity Systems applied CSP modeling and analysis during the development of software (approximately 100,000 lines of code) for a secure smart-card certification authority to verify that their design was secure and free of deadlock. Praxis claims that the system has a much lower defect rate than comparable systems.

Since CSP is well-suited to modeling and analyzing systems that incorporate complex message exchanges, it has also been applied to the verification of communications and security protocols. A prominent example of this sort of application is Lowe's use of CSP and the FDR refinement-checker to discover a previously unknown attack on the Needham–Schroeder public-key authentication protocol, and then to develop a corrected protocol able to defeat the attack.

## Informal description

As its name suggests, CSP allows the description of systems in terms of component processes that operate independently, and interact with each other solely through message-passing communication. However, the *"Sequential"* part of the CSP name is now something of a misnomer, since modern CSP allows component processes to be defined both as sequential processes and as the parallel composition of more primitive processes. The relationships between different processes, and the way each process communicates with its environment, are described using various process algebraic operators. Using this algebraic approach, quite complex process descriptions can be easily constructed from a few primitive elements.

### Primitives

CSP provides two classes of primitives in its process algebra: events and primitive processes.

**Events**

Events represent communications or interactions. They are assumed to be instantaneous, and their communication is all that an external ‘environment’ can know about processes. An event is communicated only if the environment allows it. If a process does offer an event and the environment allows it, then that event *must* be communicated. Events may be atomic names (e.g., on, off), compound names (e.g. valve.open, valve.close), or input/output events (e.g., mouse?xy, screen!bitmap). The set of all events is denoted $\Sigma$ .

**Primitive processes**

Primitive processes represent fundamental behaviors: examples include $\mathrm {STOP}$ (the process that immediately deadlocks), and $\mathrm {SKIP}$ (the process that immediately terminates successfully).

### Algebraic operators

CSP has a wide range of algebraic operators. The principal ones are informally given as follows.

**Prefix**

The prefix operator combines an event and a process to produce a new process. For example, $a\to P$ is the process that is willing to communicate event a with its environment and, after a , behaves like the process P .

**Recursion**

Processes can be defined using recursion. Where $F(P)$ is any CSP term involving P , the process $\mu P.F(P)$ defines a recursive process given by the equation $P=F(P)$ . Recursions can also be defined mutually, such as ${\begin{aligned}&P_{u}=up\to P_{d}\\&P_{d}=down\to P_{u}\\\end{aligned}}$ which defines a pair of mutually recursive processes that alternate between communicating $up$ and $down$ .

**Deterministic choice**

The deterministic (or external) choice operator allows the future evolution of a process to be defined as a choice between two component processes and allows the environment to resolve the choice by communicating an initial event for one of the processes. For example, $(a\to P)\ \Box \ (b\to Q)$ is the process that is willing to communicate the initial events a and b and subsequently behaves as either P or Q , depending on which initial event the environment chooses to communicate.

**Nondeterministic choice**

The nondeterministic (or internal) choice operator allows the future evolution of a process to be defined as a choice between two component processes, but does not allow the environment any control over which one of the component processes will be selected. For example, $(a\to P)\sqcap (b\to Q)$ can behave like either $a\to P$ or $b\to Q$ . It can refuse to accept a or b and is only obliged to communicate if the environment offers both a and b .

Nondeterminism can be inadvertently introduced into an ostensibly deterministic choice if the initial events of both sides of the choice are identical. So, for example, $(a\to a\to \mathrm {STOP} )\ \Box \ (a\to b\to \mathrm {STOP} )$ and $a\to {\big (}(a\to \mathrm {STOP} )\sqcap (b\to \mathrm {STOP} ){\big )}$ are equivalent.

**Interleaving**

The interleaving operator represents completely independent concurrent activity. The process $P\;|||\;Q$ behaves as both P and Q simultaneously. The events from both processes are arbitrarily interleaved in time. Interleaving can introduce nondeterminism even if P and Q are both deterministic: if P and Q can both communicate the same event, then $P\;|||\;Q$ nondeterministically chooses which of the two processes communicated that event.

**Interface parallel**

The interface parallel (or generalized parallel) operator represents concurrent activity that requires synchronization between the component processes: for $P\;|[X]|\;Q$ , any event in the interface set $X\subseteq \Sigma$ can only occur when both P and Q are able to engage in that event.

For example, the process $P\;|[\{a\}]|\;Q$ requires that P and Q must both be able to perform event a before that event can occur. So, the process $(a\to P)\;|[\{a\}]|\;(a\to Q)$ is equivalent to $a\to (P\;|[\{a\}]|\;Q)$ , while $(a\to P)\;|[\{a,b\}]|\;(b\to Q)$ is equivalent to $\mathrm {STOP}$ (i.e. the process deadlocks).

**Hiding**

The hiding operator provides a way to abstract processes by making some events unobservable by the environment. $P\setminus X$ is the process P with the event set X hidden.

A trivial example of hiding is $(a\to P)\setminus \{a\}$ which, assuming that the event a doesn't appear in P , simply reduces to P . Hidden events are internalized as *τ actions*, which are invisible to and uncontrollable by the environment. The existence of hiding introduces an additional behaviour called divergence, where an infinite sequence of τ actions is performed. This is captured by the process $\mathbf {div}$ , whose behaviour is solely to perform τ actions forever. For example, $(\mu P.a\to P)\setminus \{a\}$ is equivalent to $\mathbf {div}$ .

### Examples

One of the archetypal CSP examples is an abstract representation of a chocolate vending machine and its interactions with a person wishing to buy some chocolate. This vending machine might be able to carry out two different events, “coin” and “choc”, which represent the insertion of payment and the delivery of a chocolate, respectively. A machine that demands payment (only in cash) before offering a chocolate can be written as:

$\mathrm {VendingMachine} =\mathrm {coin} \rightarrow \mathrm {choc} \rightarrow \mathrm {STOP}$

A person who might choose to use a coin or card to make payments could be modelled as:

$\mathrm {Person} =(\mathrm {coin} \rightarrow \mathrm {STOP} )\;\Box \;(\mathrm {card} \rightarrow \mathrm {STOP} )$

These two processes can be put in parallel, so that they can interact with each other. The behaviour of the composite process depends on the events that the two component processes must synchronise on. Thus,

$\mathrm {VendingMachine} \left\vert \left[\left\{\mathrm {coin} ,\mathrm {card} \right\}\right]\right\vert \mathrm {Person} \equiv \mathrm {coin} \rightarrow \mathrm {choc} \rightarrow \mathrm {STOP}$

whereas if synchronization were only required on “coin”, we would obtain

$\mathrm {VendingMachine} \left\vert \left[\left\{\mathrm {coin} \right\}\right]\right\vert \mathrm {Person} \equiv \left(\mathrm {coin} \rightarrow \mathrm {choc} \rightarrow \mathrm {STOP} \right)\Box \left(\mathrm {card} \rightarrow \mathrm {STOP} \right)$

If we abstract this latter composite process by hiding the “coin” and “card” events, i.e.,

$\left(\left(\mathrm {coin} \rightarrow \mathrm {choc} \rightarrow \mathrm {STOP} \right)\Box \left(\mathrm {card} \rightarrow \mathrm {STOP} \right)\right)\setminus \left\{\mathrm {coin,card} \right\}$

we obtain the nondeterministic process

$\left(\mathrm {choc} \rightarrow \mathrm {STOP} \right)\sqcap \mathrm {STOP}$

This is a process that either offers a “choc” event and then stops, or just stops. In other words, if we treat the abstraction as an external view of the system (e.g., someone who does not see the decision reached by the person), nondeterminism has been introduced.

## Formal definition

### Syntax

The syntax of CSP defines the “legal” ways in which processes and events may be combined. Let e be an event, b be a boolean, and X be a set of events. Then the basic syntax of CSP can be defined as:

${\begin{array}{lcll}{Proc}&::=&\mathrm {STOP} &\;\\&|&\mathrm {SKIP} &\;\\&|&e\rightarrow {Proc}&({\text{prefixing}})\\&|&{Proc}\;\Box \;{Proc}&({\text{external}}\;{\text{choice}})\\&|&{Proc}\;\sqcap \;{Proc}&({\text{nondeterministic}}\;{\text{choice}})\\&|&{Proc}\;\vert \vert \vert \;{Proc}&({\text{interleaving}})\\&|&{Proc}\;|[\{X\}]|\;{Proc}&({\text{interface}}\;{\text{parallel}})\\&|&{Proc}\setminus X&({\text{hiding}})\\&|&{Proc};{Proc}&({\text{sequential}}\;{\text{composition}})\\&|&\mathrm {if} \;b\;\mathrm {then} \;{Proc}\;\mathrm {else} \;Proc&({\text{boolean}}\;{\text{conditional}})\\&|&{Proc}\;\triangleright \;{Proc}&({\text{timeout}})\\&|&{Proc}\;\triangle \;{Proc}&({\text{interrupt}})\end{array}}$

Note that, in the interests of brevity, the syntax presented above omits the $\mathbf {div}$ process, which represents divergence, as well as various operators such as alphabetized parallel, piping, and indexed choices.

### Formal semantics

CSP has been imbued with several different formal semantics, which define the *meaning* of syntactically correct CSP expressions. The theory of CSP includes mutually consistent denotational semantics, algebraic semantics, and operational semantics.

### Denotational semantics

The three major denotational models of CSP are the *traces* model, the *stable failures* model, and the *failures/divergences* model. Semantic mappings from process expressions to each of these three models provide the denotational semantics for CSP.

Denotational semantics allows several definitions of a partial order of *refinement* on processes, which in turn can be used to elegantly represent several properties on processes. Generally, $P\sqsubseteq Q$ denotes Q *refines* P .

#### Traces model

The *traces model* defines the meaning of a process expression as the set of sequences of events (traces) that the process can be observed to perform. For example,

- $\mathrm {traces} \left(\mathrm {STOP} \right)=\left\{\langle \rangle \right\}$ since $\mathrm {STOP}$ performs no events
- $\mathrm {traces} \left(a\rightarrow b\rightarrow \mathrm {STOP} \right)=\left\{\langle \rangle ,\langle a\rangle ,\langle a,b\rangle \right\}$ since the process $(a\rightarrow b\rightarrow \mathrm {STOP} )$ can be observed to have performed no events, the event a, or the sequence of events a followed by b

More formally, the traces model ${\mathcal {T}}$ is defined as the set of non-empty prefix-closed subsets of $\Sigma ^{\ast }$ . The meaning of a process P in the traces model is defined as $\mathrm {traces} \left(P\right)\subseteq \Sigma ^{\ast }$ such that:

1. $\langle \rangle \in \mathrm {traces} \left(P\right)$ (i.e. $\mathrm {traces} \left(P\right)$ contains the empty sequence)
2. $s_{1}\smallfrown s_{2}\in \mathrm {traces} \left(P\right)\implies s_{1}\in \mathrm {traces} \left(P\right)$ (i.e. $\mathrm {traces} \left(P\right)$ is prefix-closed)

where $\Sigma ^{\ast }$ is the set of all possible finite sequences of events.

A process P is said to *trace-refine* another Q if and only if $\mathrm {traces} (P)\supseteq \mathrm {traces} (Q)$ . P *trace-refines* Q is denoted $Q\sqsubseteq _{\mathrm {T} }P$ .

#### Stable failures model

The *stable failures model* ${\mathcal {F}}$ extends the traces model with refusal sets, which are sets of events $X\subseteq \Sigma$ that a process can refuse to perform. A *failure* is a pair $\left(s,X\right)$ , consisting of a trace s, and a refusal set X which identifies the events that a process may refuse once it has executed the trace s. The observed behavior of a process in the stable failures model is described by the pair $\left(\mathrm {traces} \left(P\right),\mathrm {failures} \left(P\right)\right)$ . For example,

$\mathrm {failures} \left(\left(a\rightarrow \mathrm {STOP} \right)\Box \left(b\rightarrow \mathrm {STOP} \right)\right)=\left\{\left(\langle \rangle ,\emptyset \right),\left(\langle a\rangle ,\left\{a,b\right\}\right),\left(\langle b\rangle ,\left\{a,b\right\}\right)\right\}$ $\mathrm {failures} \left(\left(a\rightarrow \mathrm {STOP} \right)\sqcap \left(b\rightarrow \mathrm {STOP} \right)\right)=\left\{\left(\langle \rangle ,\left\{a\right\}\right),\left(\langle \rangle ,\left\{b\right\}\right),\left(\langle a\rangle ,\left\{a,b\right\}\right),\left(\langle b\rangle ,\left\{a,b\right\}\right)\right\}$

A process P *stable-failures-refines* Q if and only if $\mathrm {traces} (P)\supseteq \mathrm {traces} (Q)\land \mathrm {failures} (P)\supseteq \mathrm {failures} (Q)$ . P *stable-failures-refines* Q is denoted $Q\sqsubseteq _{\mathrm {F} }P$ .

#### Failures/divergences model

The *failures/divergence model* ${\mathcal {N}}$ further extends the failures model to handle divergence. The semantics of a process in the failures/divergences model is a pair $\left(\mathrm {failures} _{\perp }\left(P\right),\mathrm {divergences} \left(P\right)\right)$ where $\mathrm {divergences} \left(P\right)$ is defined as the extension-closure of the set of all traces after which the process can immediately diverge, and $\mathrm {failures} _{\perp }\left(P\right)=\mathrm {failures} \left(P\right)\cup \left\{\left(s,X\right)\mid s\in \mathrm {divergences} \left(P\right),X\subseteq \Sigma ^{*}\right\}$ , which is the extension of $\mathrm {failures} (P)$ with all divergent traces.

A process P *failures-divergences-refines* Q if and only if $\mathrm {failures} _{\bot }(P)\supseteq \mathrm {failures} _{\bot }(Q)\land \mathrm {divergences} (P)\supseteq \mathrm {divergences} (Q)$ . P *failures-divergences refines* Q is denoted $Q\sqsubseteq _{\mathrm {FD} }P$ .

#### Unique fixed points

One of the most important principles in CSP is the *unique fixed points* (UFP) rule. Generally, it states that a process which satisfies certain nice properties has a single semantic interpretation. It can be used to conclude algebraic proofs that two processes are equal in a model of CSP. A version for single recursions in the traces model is outlined here.

Consider processes as their trace sets. The operator $\downarrow$ is defined for all processes P , all $n\in \mathbb {N}$ so that $P\downarrow n=\{s\in P:\#s\leq n\}$ , where $\#s$ denotes the length of string s : the set of traces in P of length at most n . This allows a metric to be defined on ${\mathcal {T}}$ . For each P , Q , let $d(P,Q)=\mathrm {inf} \{2^{-n}:P\downarrow n=Q\downarrow n\}$ . Informally, a process which agrees on traces with another up to some length is ‘more distant’ from it than one which agrees with it up to a greater length. It can be shown that this forms a complete metric space.

A function on trace sets $F:{\mathcal {T}}\rightarrow {\mathcal {T}}$ is called *constructive* if and only if for all processes P , Q , all $n\in \mathbb {N}$ , if $P\downarrow n=Q\downarrow n$ then $F(P)\downarrow (n+1)=F(Q)\downarrow (n+1)$ . This means that a function is constructive if and only if it is a contraction mapping with respect to the metric on trace sets.

By the Banach fixed-point theorem, if F is a constructive function, it has a unique fixed point. This means that if X and Y are processes defined recursively as $X=F(X)$ and $Y=F(Y)$ , then they are equivalent in the traces model. UFP can also be extended to mutual recursions (by using vectors of processes) and other models of CSP (e.g., in ${\mathcal {F}}$ by defining the metric as in ${\mathcal {T}}$ , with respect to the trace parts of a process's trace-failure pair).

It can be derived using UFP (and Tarski's fixed-point theorem), that for monotonic F , a recursive term defined as $X=F(X)$ has the semantic interpretation $\sqcap _{n=0}^{\infty }F^{n}(\bot )$ , where $\bot$ is the least element of the model. In the traces, stable failures and failures/divergences models, $\bot =\mathbf {div}$ (equivalent to $\mathrm {STOP}$ in the traces model).

## Tools

Over the years, a number of tools for analyzing and understanding systems described using CSP have been produced. Early tool implementations used a variety of machine-readable syntaxes for CSP, making input files written for different tools incompatible. However, most CSP tools have now standardized on the machine-readable dialect of CSP devised by Bryan Scattergood, sometimes referred to as CSP*M*. The CSP*M* dialect of CSP possesses a formally defined operational semantics, which includes an embedded functional programming language.

### FDR

The most well-known CSP tool is probably *Failures–Divergences Refinement*, which is a commercial product originally developed by Formal Systems (Europe) Ltd. FDR is often described as a model checker, but is technically a *refinement* checker, in that it converts two CSP process expressions into labelled transition systems (LTSs), and then determines whether one of the processes is a refinement of the other within some specified semantic model (traces, failures, or failures/divergence). FDR applies various state-space compression algorithms to the process LTSs in order to reduce the size of the state-space that must be explored during a refinement check. FDR was succeeded by FDR2, FDR3 and FDR4.

### ARC

The *Adelaide Refinement Checker* (*ARC*) is a CSP refinement checker developed by the Formal Modelling and Verification Group at The University of Adelaide. ARC differs from FDR2 in that it internally represents CSP processes as ordered binary decision diagrams (OBDDs), which alleviates the state explosion problem of explicit LTS representations without requiring the use of state-space compression algorithms such as those used in FDR2.

### ProB

The *ProB* project, which is hosted by the Institut für Informatik, Heinrich-Heine-Universität Düsseldorf, was originally created to support analysis of specifications constructed in the B method. However, it also includes support for analysis of CSP processes both through refinement checking, and LTL model-checking. ProB can also be used to verify properties of combined CSP and B specifications. A ProBE CSP Animator is integrated in FDR3.

### PAT

The *Process Analysis Toolkit* (PAT) is a CSP analysis tool developed in the School of Computing at the National University of Singapore. PAT is able to perform refinement checking, LTL model-checking, and simulation of CSP and Timed CSP processes. The PAT process language extends CSP with support for mutable shared variables, asynchronous message passing, and a variety of fairness and quantitative time-related process constructs such as `deadline` and `waituntil`. The underlying design principle of the PAT process language is to combine a high-level specification language with procedural programs (e.g. an event in PAT may be a sequential program or even an external C# library call) for greater expressiveness. Mutable shared variables and asynchronous channels provide a convenient syntactic sugar for well-known process modelling patterns used in standard CSP. The PAT syntax is similar, but not identical, to CSP*M*. The principal differences between the PAT syntax and standard CSP*M* are the use of semicolons to terminate process expressions, the inclusion of syntactic sugar for variables and assignments, and the use of slightly different syntax for internal choice and parallel composition.

### Others

*VisualNets* produces animated visualisations of CSP systems from specifications, and supports timed CSP.

*CSPsim* is a lazy simulator. It does not model check CSP, but is useful for exploring very large (potentially infinite) systems.

*SyncStitch* is a CSP refinement checker with an interactive modeling and analyzing environment. It has a graphical state-transition diagram editor. The user can model the behavior of processes as not only CSP expressions but also state-transition diagrams. The results of checking are also reported graphically as computation trees and can be analyzed interactively with peripheral inspection tools. In addition to refinement checks, it can perform deadlock checks and livelock checks.

Several other specification languages and formalisms have been derived from, or inspired by, the classic untimed CSP, including:

- Timed CSP, which incorporates timing information for reasoning about real-time systems
- Receptive Process Theory, a specialization of CSP that assumes an asynchronous (i.e., nonblocking) send operation
- CSPP
- HCSP
- TCOZ, an integration of Timed CSP and Object Z
- Circus, an integration of CSP and Z based on the Unifying Theories of Programming
- CML Archived 2020-02-19 at the Wayback Machine (COMPASS Modelling Language), a combination of Circus and VDM developed for the modelling of Systems of Systems (SoS)
- CspCASL, an extension of CASL that integrates CSP
- LOTOS, an international standard that incorporates features of CSP and CCS.
- PALPS, a probabilistic extension with locations for ecological models developed by Anna Philippou and Mauricio Toro Bermúdez

## Comparison with the actor model

Inasmuch as it is concerned with concurrent processes that exchange messages, the actor model is broadly similar to CSP. However, the two models make some fundamentally different choices with regard to the primitives they provide:

- CSP processes are anonymous, while actors have identities.
- CSP uses explicit channels for message passing, whereas actor systems transmit messages to named destination actors. These approaches may be considered duals of each other, in the sense that processes received through a single channel effectively have an identity corresponding to that channel, while the name-based coupling between actors may be broken by constructing actors that behave as channels.
- CSP message-passing fundamentally involves a rendezvous between the processes involved in sending and receiving the message, i.e., the sender cannot transmit a message until the receiver is ready to accept it. In contrast, message-passing in actor systems is fundamentally asynchronous, i.e., message transmission and reception do not have to happen at the same time, and senders may transmit messages before receivers are ready to accept them. These approaches may also be considered duals of each other, in the sense that rendezvous-based systems can be used to construct buffered communications that behave as asynchronous messaging systems, while asynchronous systems can be used to construct rendezvous-style communications by using a message/acknowledgement protocol to synchronize senders and receivers.

Note that the aforementioned properties do not necessarily refer to the original CSP paper by Hoare, but rather the modern incarnation of the idea as seen in implementations such as Go and Clojure's *core.async*. In the original paper, channels were not a central part of the specification, and the sender and receiver processes actually identify each other by name.

## Award

In 1990, “A Queen’s Award for Technological Achievement [was] conferred ... on [Oxford University] Computing Laboratory. The award recognises a successful collaboration between the laboratory and Inmos Ltd. … Inmos’ flagship product is the ‘transputer’, a microprocessor with many of the parts that would normally be needed in addition built into the same single component.” According to Tony Hoare, “The INMOS Transputer was an embodiment of the ideas … of building microprocessors that could communicate with each other along wires that would stretch between their terminals. The founder had the vision that the **CSP** ideas were ripe for industrial exploitation, and he made that the basis of the language for programming Transputers, which was called Occam. … The company estimated it enabled them to deliver the hardware one year earlier than would otherwise have happened. They applied for and won a Queen’s award for technological achievement, in conjunction with Oxford University Computing Laboratory.”
