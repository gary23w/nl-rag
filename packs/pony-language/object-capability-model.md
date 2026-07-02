---
title: "Object-capability model"
source: https://en.wikipedia.org/wiki/Object-capability_model
domain: pony-language
license: CC-BY-SA-4.0
tags: pony language, actor model, capability based security, reference capability, object capability model
fetched: 2026-07-02
---

# Object-capability model

The **object-capability model** is a computer security model. A capability describes a transferable right to perform one (or more) operations on a given object. It can be obtained by the following combination:

- An unforgeable reference (in the sense of object references or protected pointers) that can be sent in messages.
- A message that specifies the operation to be performed.

The security model relies on not being able to forge references.

- Objects can interact only by sending messages on references.
- A reference can be obtained by:

1. Initial conditions: In the initial state of the computational world being described, object A may already have a reference to object B.
2. Parenthood: If A creates B, at that moment A obtains the only reference to the newly created B.
3. Endowment: If A creates B, B is born with that subset of A's references with which A chose to endow it.
4. Introduction: If A has references to both B and C, A can send to B a message containing a reference to C. B can retain that reference for subsequent use.

In the object-capability model, *all* computation is performed following the above rules.

Advantages that motivate object-oriented programming, such as encapsulation or information hiding, modular programming (modularity), and separation of concerns, correspond to security goals such as least privilege and privilege separation in capability-based programming.

The object-capability model was first proposed by Jack Dennis and Earl C. Van Horn in 1966.

## Loopholes in object-oriented programming languages

Some object-based programming languages (e.g., JavaScript (criticism), Java, and C#) provide ways to access resources in ways other than according to the rules above, including the following:

- Direct assignment to the instance variables of an object in Java and C#.
- Direct reflective programming (reflection) inspection of the meta-data of an object in Java and C#.
- The pervasive ability to import primitive modules, e.g., java.io.File that enable external effects.

Such use of *undeniable authority* violates the conditions of the object-capability model. Caja and Joe-E are variants of JavaScript and Java, respectively, that impose restrictions to eliminate these loopholes.

## Advantages of object capabilities

Computer scientist E. Dean Tribble stated that in smart contracts, identity-based access control did not support well dynamically changing permissions, compared to the object-capability model. He analogized the ocap model with giving a valet the key to a car, without giving the right to car ownership.

The structural properties of object capability systems favor modularity in code design and ensure reliable encapsulation in code implementation.

These structural properties facilitate the analysis of some security properties of an object-capability program or operating system. Some of these, specifically information flow properties, can be analyzed at the level of object references and connectivity, independent of any knowledge or analysis of the code that determines the behavior of the objects. As a consequence, these security properties can be established and maintained in the presence of new objects that contain unknown and possibly malicious code.

These structural properties stem from the two rules governing access to existing objects:

1) An object

A

can send a message to

B

only if object

A

holds a reference to

B

.

2) An object

A

can obtain a reference to

C

only if object

A

receives a message containing a reference to

C

.

As a consequence of these two rules, an object can obtain a reference to another object only through a preexisting chain of references. In short, "Only connectivity begets connectivity."

**object-capability system**

A computational system that implements principles described in this article.

**object**

An object has local state and behavior. An object in this sense is both a

subject

and an

object

in the sense used in the access control literature.

**reference**

An unforgeable communications channel (protected pointer, opaque address) that unambiguously designates one object, and provides permission to send messages to that object.

**message**

What is sent on a reference. Depending on the system, messages may or may not be first-class objects.

**request**

An operation in which a message is sent on a reference. When the message is received, the receiver will have access to any references included in the message.

**attenuation**

A common

design pattern

in object-capability systems: given one reference of an object, create another reference for a proxy object with certain security restrictions, such as only permitting read-only access or allowing revocation. The proxy object performs security checks on messages that it receives and passes on any that are allowed.

Deep attenuation

refers to the case where the same attenuation is applied transitively to any objects obtained via the original attenuated object, typically by use of a

membrane

.

## Implementations

Almost all historical systems that have been described as *capability systems* can be modeled as object-capability systems. However, some uses of the term *capability* are inconsistent with the model, such as POSIX *capabilities*.

KeyKOS, EROS, Integrity (operating system), CapROS, Coyotos, seL4, OKL4 and Fiasco.OC are secure operating systems that implement the object-capability model.

## Languages that implement object capabilities

- Act 1 (1981)
- Eden (1985)
- Emerald (1987)
- Trusty Scheme (1992)
- W7 (1995)
- Joule (1996)
- Original-E (1997)
- Oz-E (2005)
- Joe-E (2005)
- CaPerl (2006)
- Emily (2006)
- Caja (2007–2021)
- Monte (2008–present)
- Pony (2014–present)
- Wyvern (2012–present)
- Newspeak (2007–present)
- Hack (2021-present)
- Rholang (2018-present)
