---
title: "Object copying"
source: https://en.wikipedia.org/wiki/Deep_copy
domain: immer-immutable
license: CC-BY-SA-4.0
tags: immer immutable, immutable update, structural sharing, draft state
fetched: 2026-07-02
---

# Object copying

(Redirected from

Deep copy

)

In object-oriented programming, **object copying** is creating a copy of an existing object, a unit of data in object-oriented programming. The resulting object is called an *object copy* or simply *copy* of the original object. Copying is basic but has subtleties and can have significant overhead. There are several ways to copy an object, most commonly by a copy constructor or cloning. Copying is done mostly so the copy can be modified or moved, or the current value preserved. If either of these is unneeded, a reference to the original data is sufficient and more efficient, as no copying occurs.

Objects in general store composite data. While in simple cases copying can be done by allocating a new, uninitialized object and copying all fields (attributes) from the original object, in more complex cases this does not result in desired behavior.

## Methods of copying

The design goal of most objects is to give the resemblance of being made out of one monolithic block even though most are not. As objects are made up of several different parts, copying becomes nontrivial. Several strategies exist to treat this problem.

Consider an object A, which contains fields xi (more concretely, consider if A is a string and xi is an array of its characters). There are different strategies for making a copy of A, referred to as *shallow copy* and *deep copy*. Many languages allow generic copying by one or either strategy, defining either one *copy* operation or separate *shallow copy* and *deep copy* operations. Note that even shallower is to use a reference to the existing object A, in which case there is no new object, only a new reference.

The terminology of *shallow copy* and *deep copy* dates to Smalltalk-80. The same distinction holds for comparing objects for equality: most basically there is a difference between identity (same object) and equality (same value), corresponding to shallow equality and (1 level) deep equality of two object references, but then further whether equality means comparing only the fields of the object in question or dereferencing some or all fields and comparing their values in turn (e.g., are two linked lists equal if they have the same nodes, or if they have same values?).

### Shallow copy

Variable reference to different memory space

The assignment of variable B to A.

Variables referring to same area of memory.

One method of copying an object is the *shallow copy*. In that case a new object B is created, and the fields values of A are copied over to B. This is also known as a *field-by-field copy*, *field-for-field copy*, or *field copy*. If the field value is a reference to an object (e.g., a memory address) it copies the reference, hence referring to the same object as A does, and if the field value is a primitive type, it copies the value of the primitive type. In languages without primitive types (where everything is an object), all fields of the copy B are references to the same objects as the fields of original A. The referenced objects are thus *shared*, so if one of these objects is modified (from A or B), the change is visible in the other. Shallow copies are simple and typically cheap, as they can usually be implemented by simply copying the bits exactly.

### Deep copy

A deep copy in progress.

A deep copy has been completed.

An alternative is a deep copy, meaning that fields are dereferenced: rather than references to objects being copied, new copy of objects are created for any referenced objects, and references to these are placed in B. Later modifications to the contents remain unique to A or B, as the contents are not shared.

### Combination

In more complex cases, some fields in a copy should have shared values with the original object (as in a shallow copy), corresponding to an "association" relationship; some fields should have copies (as in a deep copy), corresponding to an "aggregation" relationship. In these cases a custom implementation of copying is generally required; this issue and solution dates to Smalltalk-80. Alternatively, fields can be marked as requiring a shallow copy or deep copy, and copy operations automatically generated (likewise for comparison operations). This is not implemented in most object-oriented languages, however, though there is partial support in Eiffel.

## Implementation

Nearly all object-oriented programming languages provide some way to copy objects. As most languages do not provide most objects for programs, a programmer must define how an object should be copied, just as they must define if two objects are identical or even comparable in the first place. Many languages provide some default behavior.

How copying is solved varies from language to language, and what concept of an object it has.

### Lazy copy

A lazy copy is an implementation of a deep copy. When initially copying an object, a (fast) shallow copy is used. A counter is also used to track how many objects share the data. When the program wants to modify an object, it can determine if the data is shared (by examining the counter) and can do a deep copy if needed.

Lazy copy looks to the outside just as a deep copy, but takes advantage of the speed of a shallow copy whenever possible. The downside are rather high but constant base costs because of the counter. Also, in certain situations, circular references can cause problems.

Lazy copy is related to copy-on-write.

In C++, a lazy copy occurs by default when invoking the copy constructor.

### In Java

The following presents examples for one of the most widely used object-oriented languages, Java, which should cover nearly every way that an object-oriented language can treat this problem.

Unlike in C++, objects in Java are always accessed indirectly through references. Objects are never created implicitly but instead are always passed or assigned by a reference variable. (Methods in Java are always *pass by value*, however, it is the value of the reference variable that is being passed.) The Java Virtual Machine manages garbage collection so that objects are cleaned up after they are no longer reachable. There is no automatic way to copy any given object in Java.

Copying is usually performed by a clone() method of a class. This method usually, in turn, calls the clone() method of its parent class to obtain a copy, and then does any custom copying procedures. Eventually this gets to the clone() method of `Object` (the uppermost class), which creates a new instance of the same class as the object and copies all the fields to the new instance (a "shallow copy"). If this method is used, the class must implement the `Cloneable` marker interface, or else it will throw a "Clone Not Supported Exception". After obtaining a copy from the parent class, a class' own clone() method may then provide custom cloning capability, like deep copying (i.e. duplicate some of the structures referred to by the object) or giving the new instance a new unique ID.

The return type of clone() is `Object`, but implementers of a clone method could write the type of the object being cloned instead due to Java's support for covariant return types. One advantage of using clone() is that since it is an overridable method, we can call clone() on any object, and it will use the clone() method of its class, without the calling code needing to know what that class is (which would be needed with a copy constructor).

A disadvantage is that one often cannot access the clone() method on an abstract type. Most interfaces and abstract classes in Java do not specify a public clone() method. Thus, often the only way to use the clone() method is if the class of an object is known, which is contrary to the abstraction principle of using the most generic type possible. For example, if one has a List reference in Java, one cannot invoke clone() on that reference because List specifies no public clone() method. Implementations of List like Array List and Linked List all generally have clone() methods, but it is inconvenient and bad abstraction to carry around the class type of an object.

Another way to copy objects in Java is to serialize them through the `Serializable` interface. This is typically used for persistence and wire protocol purposes, but it does create copies of objects and, unlike clone, a deep copy that gracefully handles cycled graphs of objects is readily available with minimal effort from a programmer.

Both of these methods suffer from a notable problem: the constructor is not used for objects copied with clone or serialization. This can lead to bugs with improperly initialized data, prevents the use of `final` member fields, and makes maintenance challenging. Some utilities attempt to overcome these issues by using reflection to deep copy objects, such as the deep-cloning library.

### In Eiffel

Runtime objects in Eiffel are accessible either indirectly through references or as *expanded* objects which fields are embedded within the objects that use them. That is, fields of an object are stored either externally or internally.

The Eiffel class `ANY` contains features for shallow and deep copying and cloning of objects. All Eiffel classes inherit from `ANY`, so these features are available within all classes, and are applicable both to reference and expanded objects.

The `copy` feature effects a shallow, field-by-field copy from one object to another. In this case no new object is created. If `y` were copied to `x`, then the same objects referenced by `y` before the application of `copy`, will also be referenced by `x` after the `copy` feature completes.

To effect the creation of a new object which is a shallow duplicate of `y`, the feature `twin` is used. In this case, one new object is created with its fields identical to those of the source.

The feature `twin` relies on the feature `copy`, which can be redefined in descendants of `ANY`, if needed. The result of `twin` is of the anchored type `like Current`.

Deep copying and creating deep twins can be done using the features `deep_copy` and `deep_twin`, again inherited from class `ANY`. These features have the potential to create many new objects, because they duplicate all the objects in an entire object structure. Because new duplicate objects are created instead of simply copying references to existing objects, deep operations will become a source of performance issues more readily than shallow operations.

### In other languages

In C#, rather than using the interface `ICloneable`, a generic extension method can be used to create a deep copy using reflection. This has two advantages: First, it provides the flexibility to copy every object without having to specify each property and variable to be copied manually. Second, because the type is generic, the compiler ensures that the destination object and the source object have the same type.

In Objective-C, the methods `copy` and `mutableCopy` are inherited by all objects and intended for performing copies; the latter is for creating a mutable type of the original object. These methods in turn call the `copyWithZone` and `mutableCopyWithZone` methods, respectively, to perform the copying. An object must implement the corresponding `copyWithZone` method to be copyable.

In OCaml, the library function Oo.copy performs shallow copying of an object.

In Python, the library's copy module provides shallow copy and deep copy of objects through the `copy()` and `deepcopy()` functions, respectively. Programmers may define special methods `__copy__()` and `__deepcopy__()` in an object to provide custom copying implementation.

In Ruby, all objects inherit two methods for performing shallow copies, clone and dup. The two methods differ in that `clone` copies an object's tainted state, frozen state, and any singleton methods it may have, whereas `dup` copies only its tainted state. Deep copies may be achieved by dumping and loading an object's byte stream or YAML serialization. Alternatively, you can use the deep_dive gem to do a controlled deep copy of your object graphs.

In Rust, structs can implement the `clone` method using the `Clone` trait.

In Perl, nested structures are stored by the use of references, thus a developer can either loop over the entire structure and re-reference the data or use the `dclone()` function from the module Storable.

In VBA, an assignment of variables of type `Object` is a shallow copy, an assignment for all other types (numeric types, String, user defined types, arrays) is a deep copy. So the keyword `Set` for an assignment signals a shallow copy and the (optional) keyword `Let` signals a deep copy. There is no built-in method for deep copies of Objects in VBA.
