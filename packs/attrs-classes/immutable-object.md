---
title: "Immutable object"
source: https://en.wikipedia.org/wiki/Immutable_object
domain: attrs-classes
license: CC-BY-SA-4.0
tags: python attrs, attrs classes library, boilerplate class python
fetched: 2026-07-02
---

# Immutable object

In object-oriented (OO) and functional programming, an **immutable object** (unchangeable object) is an object whose state cannot be modified after it is created. This is in contrast to a **mutable object** (changeable object), which can be modified after it is created. In some cases, an object is considered immutable even if some internally used attributes change, but the object's state appears unchanging from an external point of view. For example, an object that uses memoization to cache the results of expensive computations could still be considered an immutable object.

Strings and other concrete objects are typically expressed as immutable objects to improve readability and runtime efficiency in object-oriented programming. Immutable objects are also useful because they are inherently thread-safe. Other benefits are that they are simpler to understand and reason about and offer higher security than mutable objects.

## Concepts

### Immutable variables

In imperative programming, values held in program variables whose content never changes are known as *constants* to differentiate them from variables that could be altered during execution. Examples include conversion factors from meters to feet, or the value of pi to several decimal places.

Read-only fields may be calculated when the program runs (unlike constants, which are known beforehand), but never change after they are initialized.

### Weak vs strong immutability

Sometimes, one talks of certain *fields* of an object being immutable. This means that there is no way to change those parts of the object state, even though other parts of the object may be changeable (*weakly immutable*). If all fields are immutable, then the object is immutable. If the whole object cannot be extended by another class, the object is called *strongly immutable*. This might, for example, help to explicitly enforce certain invariants about certain data in the object staying the same through the lifetime of the object. In some languages, this is done with a keyword (e.g. `const` in C++, `final` in Java) that designates the field as immutable. Some languages reverse it: in OCaml, fields of an object or record are by default immutable, and must be explicitly marked with `mutable` to be so.

### References to objects

In most object-oriented languages, objects can be referred to using references. Some examples of such languages are Java, C++, C#, VB.NET, and many scripting languages, such as Perl, Python, and Ruby. In this case, it matters whether the state of an object can vary when objects are shared via references.

### Referencing vs copying objects

If an object is known to be immutable, it is preferred to create a reference of it instead of copying the entire object. This is done to conserve memory by preventing data duplication and avoid calls to constructors and destructors; it also results in a potential boost in execution speed.

The reference copying technique is much more difficult to use for mutable objects, because if any user of a mutable object reference changes it, all other users of that reference see the change. If this is not the intended effect, it can be difficult to notify the other users to have them respond correctly. In these situations, defensive copying of the entire object rather than the reference is usually an easy but costly solution. The observer pattern is an alternative technique for handling changes to mutable objects.

### Copy-on-write

A technique that blends the advantages of **mutable** and **immutable** objects, and is supported directly in almost all modern hardware, is copy-on-write (COW). Using this technique, when a user asks the system to copy an object, it instead merely creates a new reference that still points to the same object. As soon as a user attempts to modify the object through a particular reference, the system makes a real copy, applies the modification to that, and sets the reference to refer to the new copy. The other users are unaffected, because they still refer to the original object. Therefore, under COW, all users appear to have a mutable version of their objects, although in the case that users do not modify their objects, the space-saving and speed advantages of immutable objects are preserved. Copy-on-write is popular in virtual memory systems because it allows them to save memory space while still correctly handling anything an application program might do.

### Interning

The practice of always using references in place of copies of equal objects is known as *interning*. If interning is used, two objects are considered equal if and only if their references, typically represented as pointers or integers, are equal. Some languages do this automatically: for example, Python automatically interns short strings. If the algorithm that implements interning is guaranteed to do so in every case that it is possible, then comparing objects for equality is reduced to comparing their pointers – a substantial gain in speed in most applications. (Even if the algorithm is not guaranteed to be comprehensive, there still exists the possibility of a fast path case improvement when the objects are equal and use the same reference.) Interning is generally only useful for immutable objects.

### Thread safety

Immutable objects can be useful in multi-threaded applications. Multiple threads can act on data represented by immutable objects without concern of the data being changed by other threads. Immutable objects are therefore considered more *thread-safe* than mutable objects.

### Violating immutability

Immutability does not imply that the object as stored in the computer's memory is unwriteable. Rather, immutability is a compile-time construct that indicates what a programmer can do through the normal interface of the object, not necessarily what they can absolutely do (for instance, by circumventing the type system or violating const correctness in C or C++).

## Language-specific details

In Python, Java and the .NET Framework, strings are immutable objects. Both Java and the .NET Framework have mutable versions of string. In Java these are `StringBuffer` and `StringBuilder` (mutable versions of Java `String`) and in .NET this is `StringBuilder` (mutable version of .Net `String`). Python 3 has a mutable string (bytes) variant, named `bytearray`.

Additionally, all of the primitive wrapper classes in Java are immutable.

Similar patterns are the Immutable Interface and Immutable Wrapper.

In pure functional programming languages it is not possible to create mutable objects without extending the language (e.g. via a mutable references library or a foreign function interface), so all objects are immutable.

### Ada

In Ada, any object is declared either *variable* (i.e. mutable; typically the implicit default), or `constant` (i.e. immutable) via the `constant` keyword.

```mw
  type Some_type is new Integer; -- could be anything more complicated
  x: constant Some_type:= 1; -- immutable
  y: Some_type; -- mutable
```

Subprogram parameters are immutable in the *in* mode, and mutable in the *in out* and *out* modes.

```mw
  procedure Do_it(a: in Integer; b: in out Integer; c: out Integer) is
  begin
    -- a is immutable
    b:= b + a;
    c:= a;
  end Do_it;
```

### C

In C# one can enforce immutability of the fields of a class with the `readonly` statement. By enforcing all the fields as immutable, the type becomes an immutable type.

```mw
class ImmutableType
{
    public readonly double Value { get; }

    public ImmutableType(double x) 
    { 
        Value = x; 
    }

    public ImmutableType Square() 
    { 
        return new ImmutableType(Value * Value); 
    }
}
```

C# has records which are immutable.

```mw
record Person(string FirstName, string LastName);
```

### C++

In C++, a const-correct implementation of `ShoppingCart` would allow the user to create instances of the class and then use them as either `const` (immutable) or mutable, as desired, by providing two different versions of the `items()` method. (Notice that in C++ it is not necessary — and in fact impossible — to provide a specialized constructor for `const` instances.)

```mw
import std;

using std::vector;
using std::views::transform;

class ShoppingCart {
private:
    vector<Merchandise> items;
public:
    explicit Cart(const vector<Merchandise>& items): 
        items{items} {}

    vector<Merchandise>& items() { 
        return items; 
    }

    const vector<Merchandise>& items() const { 
        return items;
    }

    double computeTotalCost() const { 
        return std::ranges::accumulate(
            items | transform([](const Merchandise& m) -> double { return m.getPrice(); }), 
            0.0
        );
    }
};
```

Note that, when there is a data member that is a pointer or reference to another object, then it is possible to mutate the object pointed to or referenced only within a non-const method.

C++ also provides abstract (as opposed to bitwise) immutability via the `mutable` keyword, which lets a member variable be changed from within a `const` method.

```mw
import std;

using std::optional;
using std::vector;
using std::views::transform;

class ShoppingCart {
private:
    vector<Merchandise> items;
    mutable optional<int> totalCost;
public:
    explicit Cart(const vector<Merchandise>& items): 
        items{items} {}

    const vector<Merchandise>& items() const { 
        return items; 
    }

    int computeTotalCost() const {
        if (!totalCost) {
            totalCost = std::ranges::accumulate(
                items | transform([](const Merchandise& m) -> double { return m.getPrice(); }), 
                0.0
            );
        }
        return *totalCost;
    }
};
```

### D

In D, there exist two type qualifiers, `const` and `immutable`, for variables that cannot be changed. Unlike C++'s `const`, Java's `final`, and C#'s `readonly`, they are transitive and recursively apply to anything reachable through references of such a variable. The difference between `const` and `immutable` is what they apply to: `const` is a property of the variable: there might legally exist mutable references to referred value, i.e. the value can actually change. In contrast, `immutable` is a property of the referred value: the value and anything transitively reachable from it cannot change (without breaking the type system, leading to undefined behavior). Any reference of that value must be marked `const` or `immutable`. Basically for any unqualified type `T`, `const(T)` is the disjoint union of `T` (mutable) and `immutable(T)`.

```mw
class Example {
    Object mutableField; // mutable
    const Object constField;
    immutable Object immutableField;
}
```

For a mutable `Example` object, its `mutableField` can be written to. For a `const(Example)` object, `mutableField` cannot be modified, it inherits `const`; `immutableField` is still immutable as it is the stronger guarantee. For an `immutable(Example)`, all fields are immutable.

In a function like this:

```mw
void fn(Example m, const Example c, immutable Example i) { 
    // inside the braces
}
```

Inside the braces, `c` might refer to the same object as `m`, so mutations to `m` could indirectly change `c` as well. Also, `c` might refer to the same object as `i`, but since the value then is immutable, there are no changes. However, `m` and `i` cannot legally refer to the same object.

In the language of guarantees, mutable has no guarantees (the function might change the object), `const` is an outward-only guarantee that the function will not change anything, and `immutable` is a bidirectional guarantee (the function will not change the value and the caller must not change it).

Values that are `const` or `immutable` must be initialized by direct assignment at the point of declaration or by a constructor.

Because `const` parameters forget if the value was mutable or not, a similar construct, `inout`, acts, in a sense, as a variable for mutability information. A function of type `const(S) function(const(T))` returns `const(S)` typed values for mutable, const and immutable arguments. In contrast, a function of type `inout(S) function(inout(T))` returns `S` for mutable `T` arguments, `const(S)` for `const(T)` values, and `immutable(S)` for `immutable(T)` values.

Casting immutable values to mutable inflicts undefined behavior upon change, even if the original value comes from a mutable origin. Casting mutable values to immutable can be legal when there remain no mutable references afterward. "An expression may be converted from mutable (...) to immutable if the expression is unique and all expressions it transitively refers to are either unique or immutable." If the compiler cannot prove uniqueness, the casting can be done explicitly and it is up to the programmer to ensure that no mutable references exist.

The type `string` is an alias for `immutable(char)[]`, i.e. a typed slice of memory of immutable characters. Making substrings is cheap, as it just copies and modifies a pointer and a length filed, and safe, as the underlying data cannot be changed. Objects of type `const(char)[]` can refer to strings, but also to mutable buffers.

Making a shallow copy of a const or immutable value removes the outer layer of immutability: Copying an immutable string (`immutable(char[])`) returns a string (`immutable(char)[]`). The immutable pointer and length are being copied and the copies are mutable. The referred data has not been copied and keeps its qualifier, in the example `immutable`. It can be stripped by making a depper copy, e.g. using the `dup` function.

### Java

A classic example of an immutable object is an instance of the Java `String` class

```mw
String s = "ABC";
s.toLowerCase(); // This accomplishes nothing!
```

The method `toLowerCase()` does not change the data "ABC" that `s` contains. Instead, a new String object is instantiated and given the data "abc" during its construction. A reference to this String object is returned by the `toLowerCase()` method. To make the String `s` contain the data "abc", a different approach is needed:

```mw
s = s.toLowerCase();
```

Now the String `s` references a new String object that contains "abc". There is nothing in the syntax of the *declaration* of the class String that enforces it as immutable; rather, none of the String class's methods ever affect the data that a String object contains, thus making it immutable.

The keyword `final` (detailed article) is used in implementing immutable primitive types and object references, but it cannot, by itself, make *the objects themselves* immutable. See below examples:

Primitive type variables (`int`, `long`, `short`, etc.) can be reassigned after being defined. This can be prevented by using `final`.

```mw
int i = 42; //int is a primitive type
i = 43; // OK

final int j = 42;
j = 43; // does not compile. j is final so can't be reassigned
```

Reference types cannot be made immutable just by using the `final` keyword. `final` only prevents reassignment.

```mw
final MyObject m = new MyObject(); //m is of reference type
m.data = 100; // OK. We can change state of object m (m is mutable and final doesn't change this fact)
m = new MyObject(); // does not compile. m is final so can't be reassigned
```

Primitive wrappers (`Integer`, `Long`, `Short`, `Double`, `Float`, `Character`, `Byte`, `Boolean`) are also all immutable. Immutable classes can be implemented by following a few simple guidelines.

### JavaScript

In JavaScript, all primitive types (Undefined, Null, Boolean, Number, BigInt, String, Symbol) are immutable, but custom objects are generally mutable.

```mw
function doSomething(x) { /* does changing x here change the original? */ };
var str = 'a string';
var obj = { an: 'object' };
doSomething(str);         // strings, numbers and bool types are immutable, function gets a copy
doSomething(obj);         // objects are passed in by reference and are mutable inside function
doAnotherThing(str, obj); // `str` has not changed, but `obj` may have.
```

To simulate immutability in an object, one may define properties as read-only (writable: false).

```mw
var obj = {};
Object.defineProperty(obj, 'foo', { value: 'bar', writable: false });
obj.foo = 'bar2'; // silently ignored
```

However, the approach above still lets new properties be added. Alternatively, one may use Object.freeze to make existing objects immutable.

```mw
var obj = { foo: 'bar' };
Object.freeze(obj);
obj.foo = 'bars'; // cannot edit property, silently ignored
obj.foo2 = 'bar2'; // cannot add property, silently ignored
```

With the implementation of ECMA262, JavaScript has the ability to create immutable references that cannot be reassigned. However, using a `const` declaration doesn't mean that value of the read-only reference is immutable, just that the name cannot be assigned to a new value.

```mw
const ALWAYS_IMMUTABLE = true;

try {
  ALWAYS_IMMUTABLE = false;
} catch (err) {
  console.log("Can't reassign an immutable reference.");
}

const arr = [1, 2, 3];
arr.push(4);
console.log(arr); // [1, 2, 3, 4]
```

The use of immutable state has become a rising trend in JavaScript since the introduction of React, which favours Flux-like state management patterns such as Redux.

### Perl

In Perl, one can create an immutable class with the Moo library by simply declaring all the attributes read only:

```mw
package Immutable;
use Moo;

has value => (
    is      => 'ro',   # read only
    default => 'data', # can be overridden by supplying the constructor with
                       # a value: Immutable->new(value => 'something else');
);

1;
```

Creating an immutable class used to require two steps: first, creating accessors (either automatically or manually) that prevent modification of object attributes, and secondly, preventing direct modification of the instance data of instances of that class (this was usually stored in a hash reference, and could be locked with Hash::Util's lock_hash function):

```mw
package Immutable;
use strict;
use warnings;
use base qw(Class::Accessor);
# create read-only accessors
__PACKAGE__->mk_ro_accessors(qw(value));
use Hash::Util 'lock_hash';

sub new {
    my $class = shift;
    return $class if ref($class);
    die "Arguments to new must be key => value pairs\n"
        unless (@_ % 2 == 0);
    my %defaults = (
        value => 'data',
    );
    my $obj = {
        %defaults,
        @_,
    };
    bless $obj, $class;
    # prevent modification of the object data
    lock_hash %$obj;
}
1;
```

Or, with a manually written accessor:

```mw
package Immutable;
use strict;
use warnings;
use Hash::Util 'lock_hash';

sub new {
    my $class = shift;
    return $class if ref($class);
    die "Arguments to new must be key => value pairs\n"
        unless (@_ % 2 == 0);
    my %defaults = (
        value => 'data',
    );
    my $obj = {
        %defaults,
        @_,
    };
    bless $obj, $class;
    # prevent modification of the object data
    lock_hash %$obj;
}

# read-only accessor
sub value {
    my $self = shift;
    if (my $new_value = shift) {
        # trying to set a new value
        die "This object cannot be modified\n";
    } else {
        return $self->{value}
    }
}
1;
```

### PHP

In PHP have readonly properties since version 8.1 and readonly classes since version 8.2.

```mw
readonly class BlogData
{
    public string $title;

    public Status $status;

    public function __construct(string $title, Status $status)
    {
        $this->title = $title;
        $this->status = $status;
    }
}
```

### Python

In Python, some built-in types (numbers, Booleans, strings, tuples, frozensets) are immutable, but custom classes are generally mutable. To simulate immutability in a class, one could override attribute setting and deletion to raise exceptions:

```mw
from typing import Any, NoReturn

class ImmutablePoint:
    """An immutable class with two attributes 'x' and 'y'."""

    __slots__: list[str] = ["x", "y"]

    def __setattr__(self, *args: tuple[Any, ...]) -> NoReturn:
        raise TypeError("Can not modify immutable instance.")

    __delattr__: Callable[[Tuple[Any, ...]], NoReturn] = __setattr__

    def __init__(self, x: int, y: int) -> None:
        # We can no longer use self.value = value to store the instance data
        # so we must explicitly call the superclass
        super().__setattr__("x", x)
        super().__setattr__("y", y)
```

The standard library helpers `collections.namedtuple` and `typing.NamedTuple`, available from Python 3.6 onward, create simple immutable classes. The following example is roughly equivalent to the above, plus some tuple-like features:

```mw
from typing import NamedTuple
import collections

Point: NamedTuple = collections.namedtuple("Point", ["x", "y"])

# the following creates a similar namedtuple to the above
class Point(NamedTuple):
    x: int
    y: int
```

Introduced in Python 3.7, `dataclasses` allow developers to emulate immutability with frozen instances. If a frozen dataclass is built, `dataclasses` will override `__setattr__()` and `__delattr__()` to raise `FrozenInstanceError` if invoked.

```mw
from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: int
    y: int
```

### Racket

Racket substantially diverges from other Scheme implementations by making its core pair type ("cons cells") immutable. Instead, it provides a parallel mutable pair type, via `mcons`, `mcar`, `set-mcar!` etc. In addition, many immutable types are supported, for example, immutable strings and vectors, and these are used extensively. New structs are immutable by default, unless a field is specifically declared mutable, or the whole struct:

```mw
(struct foo1 (x y))             ; all fields immutable
(struct foo2 (x [y #:mutable])) ; one mutable field
(struct foo3 (x y) #:mutable)   ; all fields mutable
```

The language also supports immutable hash tables, implemented functionally, and immutable dictionaries.

### Rust

Rust's ownership system allows developers to declare immutable variables, and pass immutable references. By default, all variables and references are immutable. Mutable variables and references are explicitly created with the `mut` keyword.

Constant items in Rust are always immutable.

```mw
// constant items are always immutable
const ALWAYS_IMMUTABLE: bool = true;

struct MyPair {
    x: usize,
    y: usize,
}

fn main() {
    // explicitly declare a mutable variable
    let mut mutable_obj = MyPair { x: 1, y: 2 };
    mutable_obj.x = 3; // okay

    let mutable_ref = &mut mutable_obj;
    mutable_ref.x = 1; // okay

    let immutable_ref = &mutable_obj;
    immutable_ref.x = 3; // error E0594

    // by default, variables are immutable
    let immutable_obj = MyPair { x: 4, y: 5 };
    immutable_obj.x = 6; // error E0596

    let mutable_ref2 = &mut immutable_obj; // error E0596

    let immutable_ref2 = &immutable_obj;
    immutable_ref2.x = 6; // error E0594
    
}
```

### Scala

In Scala, any entity (narrowly, a binding) can be defined as mutable or immutable: in the declaration, one can use `val` (value) for immutable entities and `var` (variable) for mutable ones. Note that even though an immutable binding can not be reassigned, it may still refer to a mutable object and it is still possible to call mutating methods on that object: the *binding* is immutable, but the underlying *object* may be mutable.

For example, the following code snippet:

```mw
val maxValue = 100
var currentValue = 1
```

defines an immutable entity `maxValue` (the integer type is inferred at compile-time) and a mutable entity named `currentValue`.

By default, collection classes such as `List` and `Map` are immutable, so update-methods return a new instance rather than mutating an existing one. While this may sound inefficient, the implementation of these classes and their guarantees of immutability mean that the new instance can re-use existing nodes, which, especially in the case of creating copies, is very efficient.
