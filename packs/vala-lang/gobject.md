---
title: "GObject"
source: https://en.wikipedia.org/wiki/GObject
domain: vala-lang
license: CC-BY-SA-4.0
tags: vala language, vala lang, gobject vala, gnome vala
fetched: 2026-07-02
---

# GObject

The **GLib Object System**, or **GObject**, is a free software library providing a portable object system and transparent cross-language interoperability. GObject is designed for use both directly in C programs to provide object-oriented C-based APIs and through bindings to other languages to provide transparent cross-language interoperability, e.g. PyGObject.

## History

Depending only on GLib and libc, GObject is a cornerstone of GNOME and is used throughout GTK, Pango, ATK, and most higher-level GNOME libraries like GStreamer and applications. Prior to GTK+ 2.0, code similar to GObject was part of the GTK codebase. (The name "GObject" was not yet in use — the common baseclass was called `GtkObject`.)

At the release of GTK+ 2.0, the object system was extracted into a separate library due to its general utility. In the process, most non-GUI-specific parts of the `GtkObject` class were moved up into `GObject`, the new common baseclass. Having existed as a separate library since March 11, 2002 (the release date of GTK+ 2.0), the GObject library is now used by many non-GUI programs such as command-line and server applications.

## Relation to GLib

Though GObject has its own separate set of documentation and is usually compiled into its own shared library file, the source code for GObject resides in the GLib source tree and is distributed along with GLib. For this reason, GObject uses the GLib version numbers and is typically packaged together with GLib (for example, Debian puts GObject in its `libglib2.0` package family).

## The type system

At the most basic level of the GObject framework lies a generic and dynamic type system called GType. The GType system holds a runtime description of all objects allowing glue code to facilitate multiple language bindings. The type system can handle any singly inherited class structure, in addition to *non-classed* types such as opaque pointers, strings, and variously sized integers and floating point numbers.

The type system knows how to copy, assign, and destroy values belonging to any of the registered types. This is trivial for types like integers, but many complex objects are reference-counted, while some are complex but not reference-counted. When the type system "copies" a reference-counted object, it will typically just increase its reference count, whereas when copying a complex, non-reference-counted object (such as a string), it will typically create an actual copy by allocating memory.

This basic functionality is used for implementing `GValue`, a type of generic container that can hold values of any type known by the type system. Such containers are particularly useful when interacting with dynamically typed language environments in which all native values reside in such type-tagged containers.

### Fundamental types

Types that do not have any associated classes are called *non-classed*. These types, together with all types that correspond to some form of root class, are known as *fundamental types*: the types from which all other types are derived. These make up a relatively closed set, but although the average user is not expected to create their own fundamental types, the possibility does exist and has been exploited to create custom class hierarchies — i.e., class hierarchies not based on the `GObject` class.

As of GLib 2.9.2, the *non-classed* built-in fundamental types are:

- an empty type, corresponding to C's `void` (`G_TYPE_NONE`);
- types corresponding to C's signed and unsigned `char`, `int`, `long`, and 64-bit integers (`G_TYPE_CHAR`, `G_TYPE_UCHAR`, `G_TYPE_INT`, `G_TYPE_UINT`, `G_TYPE_LONG`, `G_TYPE_ULONG`, `G_TYPE_INT64`, and `G_TYPE_UINT64`);
- a Boolean type (`G_TYPE_BOOLEAN`);
- an enumeration type and a "flags" type, both corresponding to C's `enum` type, but differing in that the latter is only used for bit fields (`G_TYPE_ENUM` and `G_TYPE_FLAGS`);
- types for single- and double-precision IEEE floats, corresponding to C's `float` and `double` (`G_TYPE_FLOAT` and `G_TYPE_DOUBLE`);
- a string type, corresponding to C's `char *` (`G_TYPE_STRING`);
- an opaque pointer type, corresponding to C's `void *` (`G_TYPE_POINTER`).

The *classed* built-in fundamental types are:

- a base class type for instances of `GObject`, the root of the standard class inheritance tree (`G_TYPE_OBJECT`)
- a base interface type, analogous to the base class type but representing the root of the standard *interface* inheritance tree (`G_TYPE_INTERFACE`)
- a type for boxed structures, which are used to wrap simple value objects or foreign objects in reference-counted "boxes" (`G_TYPE_BOXED`)
- a type for "parameter specification objects," which are used in GObject to describe metadata for object properties (`G_TYPE_PARAM`).

Types that can be instantiated automatically by the type system are called *instantiable*. An important characteristic of these types is that the first bytes of any instance always contain a pointer to the *class structure* (a form of virtual table) associated to the type of the instance. For this reason, any instantiable type must be classed. Contrapositively, any non-classed type (such as *integer* or *string*) must be non-instantiable. On the other hand, most classed types are instantiable, but some, such as interface types, are not.

### Derived types

The types that are derived from the built-in GObject fundamental types fall roughly into four categories:

**Enumerated types and "flags" types**

In general, every enumerated type and every integer-based bit field type (i.e., every

enum

type) that one wishes to use in some way that is related to the object system

—

for example, as the type of an object property

—

should be registered with the type system. Typically, the initialization code that takes care of registering these types is generated by an automated tool called

glib-mkenums

and stored in a separate file.

**Boxed types**

Some data structures that are too simple to be made full-fledged class types (with all the overhead incurred) may still need to be registered with the type system. For example, we might have a class to which we want to add a

background-color

property, whose values should be instances of a structure that looks like

struct

color

{

int

r

,

g

,

b

;

}

. To avoid having to subclass

GObject

, we can create a

boxed type

to represent this structure, and provide functions for copying and freeing. GObject ships with a handful of boxed types wrapping simple GLib data types. Another use for boxed types is as a way to wrap foreign objects in a tagged container that the type system can identify and will know how to copy and free.

**Opaque pointer types**

Sometimes, for objects that need to be neither copied or reference-counted nor freed, even a boxed type would be overkill. While such objects can be used in GObject by simply treating them as opaque pointers (

G_TYPE_POINTER

), it is often a good idea to create a derived pointer type, documenting the fact that the pointers should reference a particular kind of object, even though nothing else is said about it.

**Class and interface types**

Most types in a GObject application will be classes

—

in the normal object-oriented sense of the word

—

derived directly or indirectly from the root class,

GObject

. There are also interfaces, which, unlike classic

Java

-style

interfaces

, can contain implemented methods. GObject interfaces can thus be described as

mixins

.

## Messaging system

The GObject messaging system consists of two complementary parts: *closures* and *signals*.

**Closures**

A GObject closure is a generalized version of a

callback

. Support exists for closures written in C and C++, as well as arbitrary languages (when bindings are provided). This allows code written in (for example) Python and Java to be invoked via a GObject closure.

**Signals**

Signals are the primary mechanism by which closures are invoked. Objects register signal listeners with the type system, specifying a mapping between a given signal and a given closure. Upon emission of a registered signal, that signal's closure is invoked. In GTK, all native GUI events (such as mouse motion and keyboard actions) can generate GObject signals for listeners to potentially act upon.

## Class implementation

Each GObject class is implemented by at least two structures: the *class structure* and the *instance structure*.

**The class structure**

The class structure corresponds to the

vtable

of a C++ class. It must begin with the class structure of the superclass. Following that, it will hold a set of function pointers

—

one for each

virtual method

of the class. Class-specific variables can be used to emulate class members.

**The instance structure**

The instance structure, which will exist in one copy per object instance, must begin with the instance structure of the

superclass

(this ensures that all instances begin with a pointer to the class structure, since all fundamental instantiable types share this property). After the data belonging to the superclass, the structure can hold any instance-specific variables, corresponding to C++ member variables.

Defining a class in the GObject framework is complex, requiring large amounts of boilerplate code, such as manual definitions of type casting macros and obscure type registration incantations. Also, since a C structure cannot have access modifiers like "public", "protected", or "private", workarounds must be used to provide encapsulation. One approach is to include a pointer to the private data — conventionally called `_priv` — in the instance structure. The *private structure* can be declared in the public header file, but defined only in the implementation file, with the effect that the private data is opaque to users, but transparent to the implementor. If the private structure is registered with GType, it will be automatically allocated by the object system. Indeed, it is not even necessary to include the `_priv` pointer, if one is willing to use the incantation `G_TYPE_INSTANCE_GET_PRIVATE` every time the private data is needed.

To address some of these complexities, several higher-level languages exist that source-to-source compiles to GObject in C. The Vala programming language uses a C#-style syntax and is pre-processed into vanilla C code. The GObject Builder, or GOB2, offers a template syntax reminiscent of Java.

## GObject Introspection

- GObject introspection (abbreviated GIR) is a foreign function interface middleware layer between C libraries (using GObject) and language bindings, cf. List of language bindings for GTK.

## Usage

The combination of C and GObject is used in many successful free software projects, such as the GNOME desktop, the GTK toolkit and the GIMP image manipulation program.

Though many GObject applications are written entirely in C, the GObject system maps well into the native object systems of many other languages, like C++, Java, Ruby, Python, Common Lisp, and .NET/Mono. As a result, it is usually relatively painless to create language bindings for well-written libraries that use the GObject framework.

For example, many Python programs use libraries written in C that use the GObject framework by using the PyGObject language binding. (A few of them are listed at Category:Software that uses PyGObject).

Writing GObject code in C in the first place, however, is relatively verbose. The library takes a good deal of time to learn, and programmers with experience in high-level object-oriented languages often find it somewhat tedious to work with GObject in C. For example, creating a subclass (even just a subclass of `GObject`) can require writing and/or copying large amounts of boilerplate code. However, using Vala, a language that is designed primarily to work with GObject and which converts to C, is likely to make working with GObject or writing GObject based libraries nicer.

Although they are not really first-class objects (there are no actual metatypes in GType), metaobjects like classes and interfaces are created by GObject applications at runtime, and provide good support for introspection. The introspective capabilities are used by language bindings and user interface design applications like Glade to allow doing things like loading a shared library that provides a GObject class—usually some kind of widget, in the case of Glade—and then obtain a list of all properties of the class, complete with type information and documentation strings.

## Comparisons to other object systems

Since GObject provides a mostly complete object system for C, it can be seen as an alternative to C-derived languages such as C++ and Objective-C, though both also offer many other features beyond just their respective object systems. An easily observed difference between C++ and GObject is that GObject (like Java) does not support multiple inheritance.

GObject's use of GLib's g_malloc() memory allocation function will cause the program to exit unconditionally upon memory exhaustion, unlike the C library's malloc(), C++'s new, and other common memory allocators which allow a program to cope with or even fully recover from out-of-memory situations without simply crashing. This tends to work against including GObject in software where resilience in the face of limited memory is important, or where very many or very large objects are commonly handled. The g_try_new() can be used when a memory allocation is more likely to fail (for a large object for example), but this cannot grant that the allocation will not fail elsewhere in the code.

Another important difference is that while C++ and Objective-C are separate languages, GObject is strictly a library and as such does not introduce any new syntax or compiler intelligence. For example, when writing GObject-based C code, it is frequently necessary to perform explicit upcasting. Hence, "C with GObject", also called "glib-flavored C", considered as a language separate from plain C, is a strict superset of plain C — like Objective C, but unlike C++.

On platforms where there is no standard ABI that works across all C++ compilers (which is not usually the case, since either the Itanium ABI or the Microsoft ABI are usually followed), a library compiled with one C++ compiler is not always able to call a library compiled with a different one. If such compatibility is required, the C++ methods must be exported as plain C functions, partly defeating the purpose of the C++ object system. The problem occurs in part because different C++ compilers use different kinds of name mangling to ensure the uniqueness of all exported symbols. (This is necessary because, for example, two different classes may have identically named member functions, one function name may be overloaded multiple times, or identically named functions may appear in different namespaces, but in object code these overlaps are not allowed.) In contrast, since C does not support any form of overloading or namespacing, authors of C libraries will typically use explicit prefixes to ensure the global uniqueness of their exported names. Hence, despite being object-oriented, a GObject-based library written in C will always use the same external symbol names regardless of which compiler is used.

Perhaps the most profound difference is GObject's emphasis on signals (called events in other languages). This emphasis derives from the fact that GObject was specifically designed to meet the needs of a GUI toolkit. Whilst there are signal libraries for most object-oriented languages out there, in the case of GObject it is built into the object system. Because of this, a typical GObject application will tend to use signals to a much larger extent than a non-GObject application would, making GObject components much more encapsulated and reusable than the ones using plain C++ or Java. If using glibmm/gtkmm, the official C++ wrappers to Glib/GTK respectively, the sibling project libsigc++ allows easy use of underlying GObject signals using standard C++. Of course, other implementations of signals are available on almost all platforms, although sometimes an extra library is needed, such as Boost.Signals2 for C++.
