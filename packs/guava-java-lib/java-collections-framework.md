---
title: "Java collections framework"
source: https://en.wikipedia.org/wiki/Java_collections_framework
domain: guava-java-lib
license: CC-BY-SA-4.0
tags: guava library, java core utilities, guava collections, guava immutable collections
fetched: 2026-07-02
---

# Java collections framework

The **Java collections framework** is a set of classes and interfaces that implement commonly reusable collection data structures (collections).

Although referred to as a framework, it works in a manner of a library. The collections framework provides both interfaces that define various collections and classes that implement them.

## Differences from Arrays

`Collection`s and arrays are similar in that they both hold references to objects and they can be managed as a group. However, unlike arrays, `Collection`s do not need to be assigned a certain capacity when instantiated. `Collection`s can grow and shrink in size automatically when objects are added or removed.

`Collection`s cannot hold primitive data types such as `int`, `long`, or `double`. Instead, `Collection`s can hold wrapper classes such as `java.lang.Integer`, `java.lang.Long`, or `java.lang.Double`.

`Collection`s are generic and hence invariant, but arrays are covariant. This can be considered an advantage of generic objects such as `Collection` when compared to arrays, because under circumstances, using the generic `Collection` instead of an array prevents run time exceptions by instead throwing a compile-time exception to inform the developer to fix the code. For example, if a developer declares an `Object[]` object, and assigns the `Object[]` object to the value returned by a new `Long[]` instance with a certain capacity, no compile-time exception will be thrown. If the developer attempts to add a `String` to this `Long[]` object, the java program will throw an `ArrayStoreException`. On the other hand, if the developer instead declared a new instance of a `Collection<Object>` as `ArrayList<Long>`, the Java compiler will (correctly) throw a compile-time exception to indicate that the code is written with incompatible and incorrect type, thus preventing any potential run-time exceptions.The developer can fix the code by instantianting `Collection<Object>` as an `ArrayList<Object>` object. If the code is using Java SE7 or later versions, the developer can instantiate `Collection<Object>` as an `ArrayList<>` object by using the diamond operator

`Collection`s are generic and hence reified, but arrays are not reified.

## History

Collection implementations in pre-JDK 1.2 versions of the Java platform included few data structure classes, but did not contain a collections framework. The standard methods for grouping Java objects were via the array, the `Vector`, and the `Hashtable` classes, which unfortunately were not easy to extend, and did not implement a standard member interface.

To address the need for reusable collection data structures, several independent frameworks were developed, the most used being Doug Lea's *Collections package*, and ObjectSpace *Generic Collection Library* (JGL), whose main goal was consistency with the C++ Standard Template Library (STL).

The collections framework was designed and developed primarily by Joshua Bloch, and was introduced in JDK 1.2. It reused many ideas and classes from Doug Lea's *Collections package*, which was deprecated as a result. Sun Microsystems chose not to use the ideas of JGL, because they wanted a compact framework, and consistency with C++ was not one of their goals.

Doug Lea later developed a concurrency package, comprising new Collection-related classes. An updated version of these concurrency utilities was included in JDK 5.0 as of JSR 166.

## Architecture

Most collections in Java that are not maps are derived from the **`java.util.Collection`** interface. `Collection` defines the basic parts of all collections.

The interface has the `add(E e)` and `remove(E e)` methods for adding to and removing from a `Collection` respectively. It also has the `toArray()` method, which converts the `Collection` into an array of `Object`s in the `Collection` (with return type of `Object[]`). Finally, the `contains(E e)` method checks if a specified element exists in the `Collection`.

The `Collection` interface is a subinterface of **`java.lang.Iterable`**, so any `Collection` may be the target of a for-each statement. (The `Iterable` interface provides the `iterator()` method used by for-each statements.) All `Collection`s implement **`java.util.Iterator`** to scan all of the elements in the `Collection`.

`Collection` is generic. Any `Collection` can store any `Object`. For example, any implementation of `Collection<String>` contains `String` objects. No casting is required when using the `String` objects from an implementation of `Collection<String>`. Note that the angled brackets `< >` can hold a type argument that specifies which type the `Collection` holds.

**Collection Framework**

*Collection Framework just holds all the collections (general concept) like list etc, which follows collection interface.*

**Types of collection**

There are several kinds of collections: queues, maps, lists and sets.

Queues allow the programmer to insert items in a certain order and retrieve those items in the same order. An example is a waiting list. The base interfaces for queues are called `Queue`.

Dictionaries/Maps store references to objects with a lookup key to access the object's values. One example of a key is an identification card. The base interface for dictionaries/maps is called `Map`.

Lists are finite collections where it can store the same value multiple times.

Sets are unordered collections that can be iterated and contain each element at most once. The base interface for sets is called `Set`.

## List interface

Lists are implemented in the collections framework via the **`java.util.List`**interface. It defines a list as essentially a more flexible version of an array. Elements have a specific order, and duplicate elements are allowed. Elements can be placed in a specific position. They can also be searched for within the list.

### List implementations

There are several concrete classes that implement `List`, including `AbstractList` and all of its corresponding subclasses, as well as `CopyOnWriteArrayList`.

#### AbstractList class

The direct subclasses of `AbstractList` class include `AbstractSequentialList`, `ArrayList` and `Vector`.

`AbstractList` is an example of a *skeletal implementation*, which leverages and combines the advantages of interfaces and abstract classes by making it easy for the developer to develop their own implementation for the given interface.

##### ArrayList class

The **`java.util.ArrayList`** class implements the `List` as an array. Whenever functions specific to a `List` are required, the class moves the elements around within the array in order to do it.

##### LinkedList class

The **`java.util.LinkedList`** class stores the elements in nodes that each have a pointer to the previous and next nodes in the `List`. The `List` can be traversed by following the pointers, and elements can be added or removed simply by changing the pointers around to place the node in its proper place.

##### Vector class

The `Vector` class has `Stack` as its direct subclass. This is an example of a violation of the composition over inheritance principle in the Java platform libraries, since in computer science, a vector is generally not a stack. Composition would have been more appropriate in this scenario.

###### Stack class

The `Stack` class `extends` class **`java.util.Vector`** with five operations that allow a `Vector` to be treated as a `Stack`. Stacks are created using **`java.util.Stack`**. The `Stack` offers methods to put a new object on the `Stack` (method `push(E e)`) and to get objects from the `Stack` (method `pop()`). A `Stack` returns the object according to last-in-first-out (LIFO), e.g. the object which was placed latest on the `Stack` is returned first. `java.util.Stack` is a standard implementation of a stack provided by Java.

The `Stack` class represents a last-in-first-out (LIFO) stack of objects. The Stack class has five additional operations that allow a `Vector` to be treated as a `Stack`. The usual `push(E e)` and `pop()` operations are provided, as well as a method (`peek()`) to peek at the top item on the `Stack`, a method to test for whether the `Stack` is empty (`empty()`), and a method to search the `Stack` for an item and discover how far it is from the top (`search(Object o)`). When a `Stack` is first created, it contains no items.

#### CopyOnWriteArrayList class

The `CopyOnWriteArrayList` extends the `Object` class, and does not extend any other classes. `CopyOnWriteArrayList` allows for thread-safety without performing excessive synchronization.

In some scenarios, synchronization is mandatory. For example, if a method modifies a static field, and the method must be called by multiple threads, then synchronization is mandatory and concurrency utilities such as `CopyOnWriteArrayList` should not be used.

However synchronization can incur a performance overhead. For scenarios where synchronization is not mandatory, then the `CopyOnWriteArrayList` is a viable, thread-safe alternative to synchronization that leverages multi-core processors and results in higher CPU utilization.

## Queue interfaces

The **`java.util.Queue`** interface defines the queue data structure, which stores elements in the order in which they are inserted. New additions go to the end of the line, and elements are removed from the front. It creates a first-in first-out system. This interface is implemented by `java.util.LinkedList`, **`java.util.ArrayDeque`**, and **`java.util.PriorityQueue`**.

### Queue implementations

#### AbstractQueue class

The direct subclasses of `AbstractQueue` class include `ArrayBlockingQueue`, `ConcurrentLinkedQueue`, `DelayeQueue`, `LinkedBlockingDeque`, `LinkedBlockingQueue`. `LinkedTransferQueue` and `PriorityBlockingQueue`.

Note that `ArrayDeque` and `ConcurrentLinkedDeque` both extend `AbstractCollection` but do not extend any other abstract classes such as `AbstractQueue`.

`AbstractQueue` is an example of a *skeletal implementation*.

##### PriorityQueue class

The `java.util.PriorityQueue` class implements `java.util.Queue`, but also alters it. `PriorityQueue` has an additional `comparator()` method. Instead of elements being ordered in the order in which they are inserted, they are ordered by priority. The method used to determine priority is either the `java.lang.Comparable#compareTo(T)` method in the elements, or a method given in the constructor. The class creates this by using a heap to keep the items sorted.

##### ConcurrentLinkedQueue class

The `java.util.concurrent.ConcurrentLinkedQueue` class extends `java.util.AbstractQueue`. `ConcurrentLinkedQueue` implements the `java.util.Queue` interface.

The `ConcurrentLinkedQueue` class is a thread-safe collection, since for any an element placed inside a `ConcurrentLinkedQueue`, the Java Collection Library guarantees that the element is *safely published* by allowing any thread to get the element from the collection. An object is said to be *safely published* if the object's state is made visible to all other thread at the same point in time. Safe publication usually requires synchronization of the publishing and consuming threads.

### BlockingQueue interface

The **`java.util.concurrent.BlockingQueue`** interface extends `Queue`.

The `BlockingQueue` interface has the following direct sub-interfaces: `BlockingDeque` and `TransferQueue`. `BlockingQueue` works like a regular `Queue`, but additions to and removals from the `BlockingQueue` are blocking. If `remove(Object o)` is called on an empty `BlockingQueue`, it can be set to wait either a specified time or indefinitely for an item to appear in the `BlockingQueue`. Similarly, adding an item using the method `add(Object o)` is subject to an optional capacity restriction on the `BlockingQueue`, and the method can wait for space to become available in the `BlockingQueue` before returning. `BlockingQueue` interface introduces a method `take()` which removes and gets the head of the `BlockingQueue`, and waits until the `BlockingQueue` is no longer empty if required.

### Double-ended queue (Deque) interfaces

The `Deque` interface extends the `Queue` interface. `Deque` creates a double-ended queue. While a regular `Queue` only allows insertions at the rear and removals at the front, the `Deque` allows insertions or removals to take place both at the front and the back. A `Deque` is like a `Queue` that can be used forwards or backwards, or both at once. Additionally, both a forwards and a backwards iterator can be generated. The `Deque` interface is implemented by `java.util.ArrayDeque` and `java.util.LinkedList`.

#### Deque implementations

##### LinkedList class

`LinkedList`, of course, also implements the `List` interface and can also be used as one. But it also has the `Queue` methods. `LinkedList` implements the **`java.util.Deque`** interface, giving it more flexibility.

##### ArrayDeque class

`ArrayDeque` implements the `Queue` as an array. Similar to `LinkedList`, `ArrayDeque` also implements the **`java.util.Deque`** interface.

#### BlockingDeque interface

The **`java.util.concurrent.BlockingDeque`** interface extends `java.util.concurrent.BlockingQueue`. `BlockingDeque` is similar to `BlockingQueue`. It provides the same methods for insertion and removal with time limits for waiting for the insertion or removal to become possible. However, the interface also provides the flexibility of a `Deque`. Insertions and removals can take place at both ends. The blocking function is combined with the `Deque` function.

## Set interfaces

Java's **`java.util.Set`**interface defines the `Set`. A `Set` can't have any duplicate elements in it. Additionally, the `Set` has no set order. As such, elements can't be found by index. `Set` is implemented by **`java.util.HashSet`**, **`java.util.LinkedHashSet`**, and **`java.util.TreeSet`**.

### Set interface implementations

There are several implementations of the Set interface, including `AbstractSet` and its subclasses, and the final static inner class `ConcurrentHashMap.KeySetView<K, V>` (where `K` and `V` are formal type parameters).

#### AbstractSet

`AbstractSet` is a *skeletal implementation* for the `Set` interface.

Direct subclasses of `AbstractSet` include `ConcurrentSkipListSet`, `CopyOnWriteArraySet`, `EnumSet`, `HashSet` and `TreeSet`.

##### EnumSet class

The `EnumSet` class extends `AbstractSet`. The `EnumSet` class has no public constructors, and only contain static factory methods.

`EnumSet` contains the static factory method `EnumSet.of()`. This method is an aggregation method. It takes in several parameters, takes into account of the type of the parameters, then returns an instance with the appropriate type. As of 2018, In Java SE8 OpenJDK implementation uses two implementations of `EnumSet` which are invisible to the client, which are `RegularEnumSet` and `JumboEnumSet`. If the `RegularEnumSet` no longer provided any performance benefits for small enum types, it could be removed from the library without negatively impacting the Java Collection Library.

`EnumSet` is a good replacement for the *bit fields*, which is a type of set, as described below.

Traditionally, whenever developers encountered elements of an enumerated type that needs to be placed in a set, the developer would use the *int enum pattern* in which every constant is assigned a different power of 2. This bit representation enables the developer to use the bitwise OR operation, so that the constants can be combined into a set, also known as a *bit field*. This *bit field representation* enables the developer to make efficient set-based operations and bitwise arithmetic such as intersection and unions.

However, there are many problems with *bit field representation* approach. A bit field is less readable than an int enum constant. Also, if the elements are represented by bit fields, it is impossible to iterate through all of these elements.

A recommended alternative approach is to use an `EnumSet`, where an int enum is used instead of a *bit field*. This approach uses an `EnumSet` to represent the set of values that belong to the same `Enum` type. Since the `EnumSet` implements the `Set` interface and no longer requires the use of bit-wise operations, this approach is more type-safe. Furthermore, there are many static factories that allow for object instantiation, such as the method `EnumSet.of()` method.

After the introduction of the `EnumSet`, the *bit field representation* approach is considered to be obsolete.

##### HashSet class

`HashSet` uses a hash table. More specifically, it uses a **`java.util.LinkedHashMap`** to store the hashes and elements and to prevent duplicates.

###### LinkedHashSet class

The `java.util.LinkedHashSet` class extends `HashSet` by creating a doubly linked list that links all of the elements by their insertion order. This ensures that the iteration order over the `Set` is predictable.

##### CopyOnWriteArraySet class

`CopyOnWriteArraySet` is a concurrent replacement for a synchronized `Set`. It provides improved concurrency in many situations by removing the need to perform synchronization or making a copy of the object during iteration, similar to how `CopyOnWriteArrayList` acts as the concurrent replacement for a synchronized `List`. On the other hand, similar to `CopyOnWriteArrayList`, `CopyOnWriteArraySet` should not be used when synchronization is mandatory.

### SortedSet interface

The `java.util.SortedSet` interface extends the `java.util.Set` interface. Unlike a regular `Set`, the elements in a `SortedSet` are sorted, either by the element's `compareTo(T o)` method, or a method provided to the constructor of the `SortedSet`. The first and last elements of the `SortedSet` can be retrieved using the `first()` and `last()` methods respectively, and subsets can be created via minimum and maximum values, as well as beginning or ending at the beginning or ending of the `SortedSet`. The `java.util.TreeSet` class implements the `SortedSet` interface.

#### NavigableSet interface

The **`java.util.NavigableSet`** interface extends the `java.util.SortedSet` interface and has a few additional methods. The `floor(E e)`, `ceiling(E e)`, `lower(E e)`, and `higher(E e)` methods find an element in the set that's close to the parameter. Additionally, a descending iterator over the items in the `Set` is provided. As with `SortedSet`, `java.util.TreeSet` implements `NavigableSet`.

##### TreeSet class

`java.util.TreeSet` uses a red–black tree implemented by a **`java.util.TreeMap`**. The red–black tree ensures that there are no duplicates. Additionally, it allows `TreeSet` to implement **`java.util.SortedSet`**.

##### ConcurrentSkipListSet class

`ConcurrentSkipListSet` acts as a concurrent replacement for implementations of a synchronized `SortedSet`. For example it replaces a `TreeSet` that has been wrapped by the `synchronizedMap` method.

## Map interfaces

Maps are defined by the **`java.util.Map`** interface in Java.

### Map interface implementations

`Map`s are data structures that associate a key with an element. This lets the map be very flexible. If the key is the hash code of the element, the `Map` is essentially a `Set`. If it's just an increasing number, it becomes a list.

Examples of `Map` implementations include **`java.util.HashMap`**, **`java.util.LinkedHashMap`**, and **`java.util.TreeMap`**.

#### AbstractMap class

`AbstractMap` is an example of a *skeletal implementation*.

The direct subclasses of `AbstractMap` class include `ConcurrentSkipListMap`, `EnumMap`, `HashMap`, `IdentityHashMap`, `TreeMap` and `WeakHashMap`.

##### EnumMap

`EnumMap` extends `AbstractMap`. `EnumMap` has comparable speed with an ordinal-indexed array. This is because `EnumMap` internally uses an array, with implementation details completely hidden from the developer. Hence, the EnumMap gets the type safety of a `Map` while the performance advantages of an array.

##### HashMap

`HashMap` uses a hash table. The hashes of the keys are used to find the elements in various buckets. The `HashMap` is a hash-based collection.

###### LinkedHashMap

`LinkedHashMap` extends `HashMap` by creating a doubly linked list between the elements, allowing them to be accessed in the order in which they were inserted into the map. `LinkedHashMap` contains a `protected` `removeEldestEntry` method which is called by the `put` method whenever a new key is added to the `Map`. The `Map` removes its eldest entry whenever `removeEldestEntry` returns true. The `removeEldestEntry` method can be overridden.

##### TreeMap

`TreeMap`, in contrast to `HashMap` and `LinkedHashMap`, uses a red–black tree. The keys are used as the values for the nodes in the tree, and the nodes point to the elements in the `Map`.

##### ConcurrentHashMap

`ConcurrentHashMap` is similar to `HashMap` and is also a hash-based collection. However, there are a number of differences, such as the differences in the locking strategy they use.

The `ConcurrentHashMap` uses a completely different locking strategy to provide improved scalability and concurrency. `ConcurrentHashMap` does not synchronize every method using the same lock. Instead, `ConcurrentHashMap` use a mechanism known as *lock striping*. This mechanism provides a finer-grained locking mechanism. It also permits a higher degree of shared access.

##### ConcurrentSkipListMap class

`ConcurrentSkipListMap` acts as a concurrent replacement for implementations of a synchronized `SortedMap`. `ConcurrentSkipListMap` is very similar to `ConcurrentSkipListSet`, since `ConcurrentSkipListMap` replaces a `TreeMap` that has been wrapped by the `synchronizedMap` method.

### Map subinterfaces

#### SortedMap interface

The **`java.util.SortedMap`** interface extends the `java.util.Map` interface. This interface defines a `Map` that's sorted by the keys provided. Using, once again, the `compareTo()` method or a method provided in the constructor to the `SortedMap`, the key-element pairs are sorted by the keys. The first and last keys in the `Map` can be called by using the `firstKey()` and `lastKey()` methods respectively. Additionally, submaps can be created from minimum and maximum keys by using the `K) subMap(K fromKey, K toKey)` method. `SortedMap` is implemented by `java.util.TreeMap`.

##### NavigableMap interface

The **`java.util.NavigableMap`** interface extends `java.util.SortedMap` in various ways. Methods can be called that find the key or map entry that's closest to the given key in either direction. The map can also be reversed, and an iterator in reverse order can be generated from it. It's implemented by `java.util.TreeMap`.

#### ConcurrentMap interface

The **`java.util.concurrent.ConcurrentMap`** interface extends the `java.util.Map` interface. This interface a thread Safe `Map` interface, introduced as of Java programming language's Java Collections Framework version 1.5.

## Extensions to the Java collections framework

Java collections framework is extended by the Apache Commons Collections library, which adds collection types such as a bag and bidirectional map, as well as utilities for creating unions and intersections.

Google has released its own collections libraries as part of the guava libraries.
