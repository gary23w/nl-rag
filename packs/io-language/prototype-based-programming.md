---
title: "Prototype-based programming"
source: https://en.wikipedia.org/wiki/Prototype-based_programming
domain: io-language
license: CC-BY-SA-4.0
tags: io language, prototype based programming, message passing, actor model, coroutine concurrency
fetched: 2026-07-02
---

# Prototype-based programming

**Prototype-based programming** is a style of object-oriented programming in which behavior reuse (known as inheritance) is performed via a process of reusing existing objects that serve as prototypes. This model can also be known as *prototypal*, *prototype-oriented,* *classless*, or *instance-based* programming.

Prototype-based programming uses the process generalized objects, which can then be cloned and extended. Using fruit as an example, a "fruit" object would represent the properties and functionality of fruit in general. A "banana" object would be cloned from the "fruit" object and general properties specific to bananas would be appended. Each individual "banana" object would be cloned from the generic "banana" object. Compare to the class-based paradigm, where a "fruit" *class* would be extended by a "banana" *class*.

## History

The first prototype-based programming language was Daniel G. Bobrow and Terry Winograd’s KRL. The 1976 Stanford AIM-293 makes it the first language to claim the term object-oriented in the modern sense, the one that formally introduced the term "inheritance" ("of properties"), actually implementing multiple inheritance, and the one that introduced the term "prototype" with the present meaning.

Other early prototype systems include Director a.k.a. Ani (on top of MacLisp) (1976-1979), and contemporaneously and not independently, ThingLab (on top of Smalltalk) (1977-1981), respective PhD projects by Kenneth Michael Kahn at MIT and Alan Hamilton Borning at Stanford (but working with Alan Kay at Xerox PARC). Hewitt's Actors team at MIT added support for Prototype OO to ACT-1 in 1979 based on Kahn's work, calling the underlying mechanism "delegation" to distinguish it from the Class OO support they also added as "inheritance". Borning popularized the word "prototype" in this context in his 1981 paper in *ACM Transactions on Programming Languages and Systems (TOPLAS)*. Meanwhile, Rees and Adams's implemented class-less OO using lexical closures in Yale T Scheme (1981-1989)—they didn't say "prototype", but it was isomorphic. Ken Dickey later published their OO model as portable Scheme code in 1992 as YASOS.

Now, the language that made the name and notion of prototypes popular among academics was Self (1985-1995), developed by David Ungar and Randall Smith. But the language that made prototypes ubiquitous for everyone was Brendan Eich's JavaScript (1995-ongoing).

Since the late 1990s, the classless paradigm has grown increasingly popular. Some current prototype-oriented languages are JavaScript (and other ECMAScript implementations such as JScript and Flash's ActionScript 1.0), Lua, Cecil, NewtonScript, Io, Ioke, MOO, REBOL and AHK.

Since the 2010s, a new generation of languages with pure functional prototypes has appeared, that reduce OOP to its very core: Jsonnet is a dynamic lazy pure functional language with a builtin prototype object system using mixin inheritance; Nix is a dynamic lazy pure functional language that builds an equivalent object system (Nix "extensions") in just two short function definitions (plus many other convenience functions). Both languages are used to define large distributed software configurations (Jsonnet being directly inspired by GCL, the Google Configuration Language, with which Google defines all its deployments, and has similar semantics though with dynamic binding of variables). Since then, other languages like Gerbil Scheme have implemented pure functional lazy prototype systems based on similar principles.

## Design and implementation

Etymologically, a "prototype" means "first cast" ("cast" in the sense of being manufactured). A prototype is a concrete thing, from which other objects can be created by copying and modifying. For example, the International Prototype of the Kilogram is an actual object that really exists, from which new kilogram-objects can be created by copying. In comparison, a "class" is an abstract thing, in which objects can belong. For example, all kilogram-objects are in the class of KilogramObject, which might be a subclass of MetricObject, and so on.

Prototypal inheritance in JavaScript is described by Douglas Crockford as

> You make prototype objects, and then … make new instances. Objects are mutable in JavaScript, so we can augment the new instances, giving them new fields and methods. These can then act as prototypes for even newer objects. We don't need classes to make lots of similar objects… Objects inherit from objects. What could be more object oriented than that?

Advocates of prototype-based programming argue that it encourages the programmer to focus on the behavior of some set of examples and only later worry about classifying these objects into archetypal objects that are later used in a fashion similar to classes. Many prototype-based systems encourage the alteration of prototypes during run-time, whereas only very few class-based object-oriented systems (such as the dynamic object-oriented system, Common Lisp, Dylan, Objective-C, Perl, Python, Ruby, or Smalltalk) allow classes to be altered during the execution of a program.

Almost all prototype-based systems are based on interpreted and dynamically typed languages. Systems based on statically typed languages are technically feasible, however. The Omega language discussed in *Prototype-Based Programming* is an example of such a system, though according to Omega's website even Omega is not exclusively static, but rather its "compiler may choose to use static binding where this is possible and may improve the efficiency of a program."

## Object construction

In prototype-based languages there are no explicit classes. Objects inherit directly from other objects through a prototype property. The prototype property is called `prototype` in Self and JavaScript, or `proto` in Io. There are two methods of constructing new objects: *ex nihilo* ("from nothing") object creation or through *cloning* an existing object. The former is supported through some form of object literal, declarations where objects can be defined at runtime through special syntax such as `{...}` and passed directly to a variable. While most systems support a variety of cloning, *ex nihilo* object creation is not as prominent.

In class-based languages, a new instance is constructed through a class's constructor function, a special function that reserves a block of memory for the object's members (properties and methods) and returns a reference to that block. An optional set of constructor arguments can be passed to the function and are usually held in properties. The resulting instance will inherit all the methods and properties that were defined in the class, which acts as a kind of template from which similarly typed objects can be constructed.

Systems that support *ex nihilo* object creation allow new objects to be created from scratch without cloning from an existing prototype. Such systems provide a special syntax for specifying the properties and behaviors of new objects without referencing existing objects. In many prototype languages there exists a root object, often called *Object*, which is set as the default prototype for all other objects created in run-time and which carries commonly needed methods such as a `toString()` function to return a description of the object as a string. One useful aspect of *ex nihilo* object creation is to ensure that a new object's slot (properties and methods) names do not have namespace conflicts with the top-level *Object* object. (In the JavaScript language, one can do this by using a null prototype, i.e. `Object.create(null)`.)

*Cloning* refers to a process whereby a new object is constructed by copying the behavior of an existing object (its prototype). The new object then carries all the qualities of the original. From this point on, the new object can be modified. In some systems the resulting child object maintains an explicit link (via *delegation* or *resemblance*) to its prototype, and changes in the prototype cause corresponding changes to be apparent in its clone. Other systems, such as the Forth-like programming language Kevo, do not propagate change from the prototype in this fashion and instead follow a more *concatenative* model where changes in cloned objects do not automatically propagate across descendants.

```mw
// Example of true prototypal inheritance style in JavaScript.

// Object creation using the literal object notation {}.
const foo = { name: "foo", one: 1, two: 2 };

// Another object.
const bar = { two: "two", three: 3 };

// Object.setPrototypeOf() is a method introduced in ECMAScript 2015.
// For the sake of simplicity, let us pretend that the following
// line works regardless of the engine used:
Object.setPrototypeOf(bar, foo); // foo is now the prototype of bar.

// If we try to access foo's properties from bar from now on, 
// we'll succeed. 
bar.one; // Resolves to 1.

// The child object's properties are also accessible.
bar.three; // Resolves to 3.

// Own properties shadow prototype properties.
bar.two; // Resolves to "two".
bar.name; // Unaffected, resolves to "foo".
foo.name; // Resolves to "foo".
```

For another example:

```mw
const foo = { one: 1, two: 2 };

// bar.[[prototype]] = foo
const bar = Object.create(foo);

bar.three = 3;

bar.one; // 1
bar.two; // 2
bar.three; // 3
```

## Delegation

In prototype-based languages that use *delegation*, the language runtime is capable of dispatching the correct method or finding the right piece of data simply by following a series of delegation pointers (from object to its prototype) until a match is found. All that is required to establish this behavior-sharing between objects is the delegation pointer. Unlike the relationship between class and instance in class-based object-oriented languages, the relationship between the prototype and its offshoots does not require that the child object have a memory or structural similarity to the prototype beyond this link. As such, the child object can continue to be modified and amended over time without rearranging the structure of its associated prototype as in class-based systems. It is also important to note that not only data, but also methods can be added or changed. For this reason, some prototype-based languages refer to both data and methods as "slots" or "members".

## Concatenation

In *concatenative* prototyping - the approach implemented by the Kevo programming language - there are no visible pointers or links to the original prototype from which an object is cloned. The prototype (parent) object is copied rather than linked to and there is no delegation. As a result, changes to the prototype will not be reflected in cloned objects. Incidentally, the Cosmos programming language achieves the same through the use of persistent data structures.

The main conceptual difference under this arrangement is that changes made to a prototype object are not automatically propagated to clones. This may be seen as an advantage or disadvantage. (However, Kevo does provide additional primitives for publishing changes across sets of objects based on their similarity — so-called *family resemblances* or *clone family* mechanism — rather than through taxonomic origin, as is typical in the delegation model.) It is also sometimes claimed that delegation-based prototyping has an additional disadvantage in that changes to a child object may affect the later operation of the parent. However, this problem is not inherent to the delegation-based model and does not exist in delegation-based languages such as JavaScript, which ensure that changes to a child object are always recorded in the child object itself and never in parents (i.e. the child's value shadows the parent's value rather than changing the parent's value).

In simplistic implementations, concatenative prototyping will have faster member lookup than delegation-based prototyping (because there is no need to follow the chain of parent objects), but will conversely use more memory (because all slots are copied, rather than there being a single slot pointing to the parent object). More sophisticated implementations can avoid this problem, however, although trade-offs between speed and memory are required. For example, systems with concatenative prototyping can use a copy-on-write implementation to allow for behind-the-scenes data sharing — and such an approach is indeed followed by Kevo. Conversely, systems with delegation-based prototyping can use caching to speed up data lookup.

## Criticism

Advocates of class-based object models who criticize prototype-based systems often have concerns similar to the concerns that proponents of static type systems for programming languages have of dynamic type systems (see datatype). Usually, such concerns involve correctness, safety, predictability, efficiency and programmer unfamiliarity.

On the first three points, classes are often seen as analogous to types (in most statically typed object-oriented languages they serve that role) and are proposed to provide contractual guarantees to their instances, and to users of their instances, that they will behave in some given fashion.

Regarding efficiency, declaring classes simplifies many compiler optimizations that allow developing efficient method and instance-variable lookup. For the Self language, much development time was spent on developing, compiling, and interpreting techniques to improve the performance of prototype-based systems versus class-based systems.

A common criticism made against prototype-based languages is that the community of software developers is unfamiliar with them, despite the popularity and market permeation of JavaScript. However, knowledge about prototype-based systems is increasing with the proliferation of JavaScript frameworks and the complex use of JavaScript as the World Wide Web (Web) matures. ECMAScript 6 introduced classes as syntactic sugar over JavaScript's existing prototype-based inheritance, providing an alternative way to create objects and manage inheritance.

## Languages supporting prototype-based programming

- Actor-Based Concurrent Language (ABCL): ABCL/1, ABCL/R, ABCL/R2, ABCL/c+
- Agora
- AutoHotkey
- Cecil and Diesel of Craig Chambers
- ColdC
- COLA
- Common Lisp, with Sheeple, CommonORBIT, or other libraries.
- Cyan
- ECMAScript
  - ActionScript 1.0, used by Adobe Flash and Adobe Flex
  - ECMAScript for XML (E4X)
  - JavaScript
  - JScript
  - TypeScript
- Haskell, with Kiselyov and Lämmel's OOHaskell, or Gale's Hoop.
- Io
- Ioke
- Jsonnet
- Logtalk
- LPC
- Lua
- M2000
- Maple
- MOO
- Neko
- NewtonScript
- Nim
- Nix (where prototypes are called "extensions" or "customizations")
- Object Lisp
- Obliq
- Omega
- OpenLaszlo
- Perl, with the Class::Prototyped module
- R, with the proto package
- REBOL
- Red
- Ruby
- Scheme, with YASOS, Gerbil-POO, or other libraries.
- Self
- Seph
- Slate
- SmartFrog
- Snap!
- Etoys
- TADS
- Tcl with snit extension
- Umajin
