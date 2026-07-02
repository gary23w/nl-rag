---
title: "Dynamic dispatch"
source: https://en.wikipedia.org/wiki/Fat_pointer
domain: hardware-memory-safety
license: CC-BY-SA-4.0
tags: hardware enforced memory safety, capability based addressing, fat pointer hardware, cheri capability model
fetched: 2026-07-02
---

# Dynamic dispatch

(Redirected from

Fat pointer

)

In computer science, **dynamic dispatch** is the process of selecting which implementation of a polymorphic operation (method or function) to call at run time. It is commonly employed in, and considered a prime characteristic of, object-oriented programming (OOP) languages and systems.

Object-oriented systems model a problem as a set of interacting objects that enact operations referred to by name. Polymorphism is the phenomenon wherein somewhat interchangeable objects each expose an operation of the same name but possibly differing in behavior. As an example, a File object and a Database object both have a StoreRecord method that can be used to write a personnel record to storage. Their implementations differ. A program holds a reference to an object which may be either a File object or a Database object. Which one it is may have been determined by a run-time setting, and at this stage, the program may not know or care which. When the program calls StoreRecord on the object, something needs to choose which behavior gets enacted. If one thinks of OOP as sending messages to objects, then in this example the program sends a StoreRecord message to an object of unknown type, leaving it to the run-time support system to dispatch the message to the right object. The object enacts whichever behavior it implements.

Dynamic dispatch contrasts with *static dispatch*, in which the implementation of a polymorphic operation is selected at compile time. The purpose of dynamic dispatch is to defer the selection of an appropriate implementation until the run time type of a parameter (or multiple parameters) is known.

Dynamic dispatch is different from late binding (also known as dynamic binding). Name binding associates a name with an operation. A polymorphic operation has several implementations, all associated with the same name. Bindings can be made at compile time or (with late binding) at run time. With dynamic dispatch, one particular implementation of an operation is chosen at run time. While dynamic dispatch does not imply late binding, late binding does imply dynamic dispatch, since the implementation of a late-bound operation is not known until run time.

## Mechanisms

### Single and multiple dispatch

The choice of which version of a method to call may be based either on a single object, or on a combination of objects. The former is called *single dispatch* and is directly supported by common object-oriented languages such as Smalltalk, C++, Java, C#, Objective-C, Swift, JavaScript, and Python. In these and similar languages, one may call a method for division with syntax that resembles

```mw
dividend.divide(divisor)  # dividend / divisor
```

where the parameters are optional. This is thought of as sending a message named divide with parameter divisor to dividend. An implementation will be chosen based only on dividend's type (perhaps rational, floating point, matrix), disregarding the type or value of divisor.

By contrast, some languages dispatch methods or functions based on the combination of operands; in the division case, the types of the dividend and divisor together determine which divide operation will be performed. This is known as *multiple dispatch*. Examples of languages that support multiple dispatch are Common Lisp, Dylan, and Julia.

### Dynamic dispatch mechanisms

A language may be implemented with different dynamic dispatch mechanisms. The choices of the dynamic dispatch mechanism offered by a language to a large extent alter the programming paradigms that are available or are most natural to use within a given language.

Normally, in a typed language, the dispatch mechanism will be performed based on the type of the arguments (most commonly based on the type of the receiver of a message). Languages with weak or no typing systems often carry a dispatch table as part of the object data for each object. This allows **instance behaviour** as each instance may map a given message to a separate method.

Some languages offer a hybrid approach.

Dynamic dispatch will always incur an overhead so some languages offer static dispatch for particular methods.

#### C++ implementation

C++ uses early binding and offers both dynamic and static dispatch. The default form of dispatch is static. To get dynamic dispatch the programmer must declare a method as virtual.

C++ compilers typically implement dynamic dispatch with a data structure called a virtual function table (vtable) that defines the name-to-implementation mapping for a given class as a set of member function pointers. This is purely an implementation detail, as the C++ specification does not mention vtables. Instances of that type will then store a pointer to this table as part of their instance data, complicating scenarios when multiple inheritance is used. Since C++ does not support late binding, the virtual table in a C++ object cannot be modified at runtime, which limits the potential set of dispatch targets to a finite set chosen at compile time.

Type overloading does not produce dynamic dispatch in C++ as the language considers the types of the message parameters part of the formal message name. This means that the message name the programmer sees is not the formal name used for binding.

#### Go, Rust and Nim implementation

In Go, Rust and Nim, a more versatile variation of early binding is used. Vtable pointers are carried with object references as 'fat pointers' ('interfaces' in Go, or 'trait objects' in Rust).

This decouples the supported interfaces from the underlying data structures. Each compiled library needn't know the full range of interfaces supported in order to correctly use a type, just the specific vtable layout that they require. Code can pass around different interfaces to the same piece of data to different functions. This versatility comes at the expense of extra data with each object reference, which is problematic if many such references are stored persistently.

The term *fat pointer* simply refers to a pointer with additional associated information. The additional information may be a vtable pointer for dynamic dispatch described above, but is more commonly the associated object's size to describe e.g. a *slice*.

#### Smalltalk implementation

Smalltalk uses a type-based message dispatcher. Each instance has a single type whose definition contains the methods. When an instance receives a message, the dispatcher looks up the corresponding method in the message-to-method map for the type and then invokes the method.

Because a type can have a chain of base types, this look-up can be expensive. A naive implementation of Smalltalk's mechanism would seem to have a significantly higher overhead than that of C++ and this overhead would be incurred for every message that an object receives.

Real Smalltalk implementations often use a technique known as inline caching that makes method dispatch very fast. Inline caching basically stores the previous destination method address and object class of the call site (or multiple pairs for multi-way caching). The cached method is initialized with the most common target method (or just the cache miss handler), based on the method selector. When the method call site is reached during execution, it just calls the address in the cache. (In a dynamic code generator, this call is a direct call as the direct address is back patched by cache miss logic.) Prologue code in the called method then compares the cached class with the actual object class, and if they don't match, execution branches to a cache miss handler to find the correct method in the class. A fast implementation may have multiple cache entries and it often only takes a couple of instructions to get execution to the correct method on an initial cache miss. The common case will be a cached class match, and execution will just continue in the method.

Out-of-line caching can also be used in the method invocation logic, using the object class and method selector. In one design, the class and method selector are hashed, and used as an index into a method dispatch cache table.

As Smalltalk is a reflective language, many implementations allow mutating individual objects into objects with dynamically generated method lookup tables. This allows altering object behavior on a per object basis. A whole category of languages known as prototype-based languages has grown from this, the most famous of which are Self and JavaScript. Careful design of the method dispatch caching allows even prototype-based languages to have high-performance method dispatch.

Many other dynamically typed languages, including Python, Ruby, Objective-C and Groovy use similar approaches.

## Examples

### C

Dynamic dispatch is not built in to C like other languages, but it is still possible by manually managing function pointers.

```mw
#include <stdio.h>
#include <stdlib.h>

typedef struct Pet {
    const char* name;
    void (*speak)(struct Pet*); // holds function pointer
} Pet;

Pet* createPet(const char* name, void (*speakFunc)(Pet*)) {
    Pet* pet = (Pet*)malloc(sizeof(Pet));
    pet->name = name;
    pet->speak = speakFunc;
    return pet;
}

void destroyPet(Pet* pet) {
    free(pet);
}

void dogSpeak(Pet* pet) {
    printf("%s says 'Woof!'\n", pet->name);
}

void catSpeak(Pet* pet) {
    printf("%s says 'Meow!'\n", pet->name);
}

void speak(Pet* pet) {
    pet->speak(pet);
}

int main() {
    Pet* fido = createPet("Fido", dogSpeak);
    Pet* simba = createPet("Simba", catSpeak);

    speak(fido); // calls dogSpeak()
    speak(simba); // speaks catSpeak();

    // cleanup; free resources
    destroyPet(fido);
    destroyPet(simba);
    return 0;
}
```

### C++

```mw
import std;

using std::string;

// make Pet an abstract virtual base class
class Pet {
protected:
    string name;
public:
    explicit Pet(const string& name):
        name{name} {}

    virtual void speak() = 0;
};

class Dog : public Pet {
public:
    explicit Dog(const string& name):
        Pet(name) {}

    void speak() override {
        std::println("{} says 'Woof!'", name);
    }
};

class Cat : public Pet {
public:
    explicit Cat(const string& name):
        Pet(name) {}

    void speak() override {
        std::println("{} says 'Meow!'", name);
    }
};

// speak() will be able to accept anything deriving from Pet
void speak(Pet& pet) {
    pet.speak();
}

int main() {
    Dog fido("Fido");
    Cat simba("Simba");
    speak(fido);
    speak(simba);
    return 0;
}
```

### C

```mw
namespace Wikipedia.Examples;

using System;

abstract class Pet
{
    protected string name;

    public Pet(string name)
    {
        this.name = name;
    }

    public abstract void Speak();
}

class Dog : Pet
{
    public Dog(string name) : base(name) { }

    public override void Speak()
    {
        Console.WriteLine($"{name} says 'Woof!'");
    }
}

class Cat : Pet
{
    public Cat(string name) : base(name) { }

    public override void Speak()
    {
        Console.WriteLine($"{name} says 'Meow!'");
    }
}

public class Main
{
    public static void Speak(Pet pet)
    {
        pet.Speak();
    }

    public static void Main()
    {
        Dog fido = new("Fido");
        Cat simba = new("Simba");
        Speak(fido);
        Speak(simba);
    }
}
```

### Java

```mw
package org.wikipedia.examples;

abstract class Pet {
    protected String name;

    public Pet(String name) {
        this.name = name;
    }

    public abstract void speak();
}

class Dog extends Pet {
    public Dog(String name) {
        super(name);
    }

    @Override
    public void speak() {
        System.out.printf("%s says 'Woof!'%n", name);
    }
}

class Cat extends Pet {
    public Cat(String name) {
        super(name);
    }

    @Override
    public void speak() {
        System.out.printf("%s says 'Meow!'%n", name);
    }
};

public class Main {
    public static void speak(Pet pet) {
        pet.speak();
    }

    public static void main(String[] args) {
        Dog fido = new Dog("Fido");
        Cat simba = new Cat("Simba");
        speak(fido);
        speak(simba);
    }
}
```

### Python

```mw
from abc import ABC, abstractmethod
from typing import Never

# ABC is a class used to denote that classes directly extending it are abstract
class Pet(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def speak(self) -> Never:
        raise NotImplementedError("Abstract method must be implemented by derived classes")

class Dog(Pet):
    def __init__(self, name: str) -> None:
        super.__init__(name)

    def speak(self) -> None:
        print(f"{self.name} says 'Woof!'")

class Cat(Pet):
    def __init__(self, name: str) -> None:
        super.__init__(name)

    def speak(self) -> None:
        print(f"{self.name} says 'Meow!'")

def speak(pet: Pet) -> None:
    # Dynamically dispatches the speak method
    # pet can either be an instance of Dog or Cat
    pet.speak()

if __name__ == "__main__":
    fido: Dog = Dog("Fido")
    speak(fido)
    simba: Cat = Cat("Simba")
    speak(simba)
```

### Rust

```mw
trait Pet {
    fn speak(&self);
}

struct Dog<'a> {
    name: &'a str
}

struct Cat<'a> {
    name: &'a str
}

impl<'a> Dog<'a> {
    fn new(name: &'a str) -> Self {
        Dog { name }
    }
}

impl<'a> Cat<'a> {
    fn new(name: &'a str) -> Self {
        Cat { name }
    }
}

impl Pet<'a> for Dog<'a> {
    fn speak(&self) {
        println!("{} says 'Woof!'", self.name);
    }
}

impl Pet<'a> for Cat<'a> {
    fn speak(&self) {
        println!("{} says 'Meow!'", self.name);
    }
}

// speak() uses dynamic dispatch and resolves the type at runtime,
// for any type that implements the trait Pet
fn speak(pet: &dyn Pet) {
    pet.speak();
}

fn main() {
    let fido: Dog = Dog::new("Fido");
    let simba: Cat = Cat::new("Simba");
    speak(&fido);
    speak(&simba);
}
```
