---
title: "Encapsulation (computer programming)"
source: https://en.wikipedia.org/wiki/Encapsulation_(computer_programming)
domain: shadow-dom-deep
license: CC-BY-SA-4.0
tags: shadow dom internals, shadow root attachment, style encapsulation boundary, slot content projection
fetched: 2026-07-02
---

# Encapsulation (computer programming)

In software systems, **encapsulation** refers to the bundling of data with the mechanisms or methods that operate on the data. It may also refer to the limiting of direct access to some of that data, such as an object's components. Essentially, encapsulation prevents external code from being concerned with the internal workings of an object.

Encapsulation allows developers to present a consistent interface that is independent of its internal implementation. As one example, encapsulation can be used to hide the values or state of a structured data object inside a class. This prevents clients from directly accessing this information in a way that could expose hidden implementation details or violate state invariance maintained by the methods.

Encapsulation also encourages programmers to put all the code that is concerned with a certain set of data in the same class, which organizes it for easy comprehension by other programmers. Encapsulation is a technique that encourages decoupling.

All object-oriented programming (OOP) systems support encapsulation, but encapsulation is not unique to OOP. Implementations of abstract data types, modules, and libraries also offer encapsulation. The similarity has been explained by programming language theorists in terms of existential types.

## Meaning

In object-oriented programming languages, and other related fields, encapsulation refers to one of two related but distinct notions, and sometimes to the combination thereof:

- A language mechanism for restricting direct access to some of the object's components.
- A language construct that facilitates the bundling of data with the methods (or other functions) operating on those data.

Some programming language researchers and academics use the first meaning alone or in combination with the second as a distinguishing feature of object-oriented programming, while some programming languages that provide lexical closures view encapsulation as a feature of the language orthogonal to object orientation.

The second definition reflects that in many object-oriented languages, and other related fields, the components are not hidden automatically and this can be overridden. Thus, information hiding is defined as a separate notion by those who prefer the second definition.

The features of encapsulation are supported using classes in most object-oriented languages, although other alternatives also exist.

Encapsulation may also refer to containing a repetitive or complex process in a single unit to be invoked. Object-oriented programming facilitates this at both the method and class levels. This definition is also applicable to procedural programming.

### Encapsulation and inheritance

The authors of *Design Patterns* discuss the tension between inheritance and encapsulation at length and state that in their experience, designers overuse inheritance. They claim that inheritance often breaks encapsulation, given that inheritance exposes a subclass to the details of its parent's implementation. As described by the yo-yo problem, overuse of inheritance and therefore encapsulation, can become too complicated and hard to debug.

## Information hiding

Under the definition that encapsulation "can be used to hide data members and member functions", the internal representation of an object is generally hidden outside of the object's definition. Typically, only the object's own methods can directly inspect or manipulate its fields. Hiding the internals of the object protects its integrity by preventing users from setting the internal data of the component into an invalid or inconsistent state. A supposed benefit of encapsulation is that it can reduce system complexity, and thus increase robustness, by allowing the developer to limit the interdependencies between software components.

Some languages like Smalltalk and Ruby only allow access via object methods, but most others (e.g., C++, C#, Delphi or Java) offer the programmer some control over what is hidden, typically via keywords like `public` and `private`. ISO C++ standard refers to `protected`, `private` and `public` as "access specifiers" and that they do not "hide any information". Information hiding is accomplished by furnishing a compiled version of the source code that is interfaced via a header file.

Almost always, there is a way to override such protection – usually via reflection API (Ruby, Java, C#, etc.), sometimes by mechanism like name mangling (Python), or special keyword usage like `friend` in C++. Systems that provide object-level capability-based security (adhering to the object-capability model) are an exception, and guarantee strong encapsulation.

### Examples

#### Restricting data fields

Languages like C++, C#, Java, PHP, Swift, and Delphi offer ways to restrict access to data fields.

Below is an example in C# that shows how access to a data field can be restricted through the use of a `private` keyword:

```mw
class Program
{
    public class Account
    {
        private decimal _accountBalance = 500.00m;

        public decimal CheckBalance()
        {
            return _accountBalance;
        }
    }

    static void Main()
    {
        Account myAccount = new();
        decimal myBalance = myAccount.CheckBalance();

        /* This Main method can check the balance via the public
         * "CheckBalance" method provided by the "Account" class 
         * but it cannot manipulate the value of "accountBalance" */
    }
}
```

Below is an example in Java:

```mw
public class Employee {
    private BigDecimal salary = new BigDecimal(50000.00);
    
    public BigDecimal getSalary() {
        return this.salary;
    }

    public static void main() {
        Employee e = new Employee();
        BigDecimal sal = e.getSalary();
    }
}
```

Encapsulation is also possible in non-object-oriented languages. In C, for example, a structure can be declared in the public API via the header file for a set of functions that operate on an item of data containing data members that are not accessible to clients of the API with the `extern` keyword.

```mw
// Header file "api.h"
#pragma once

typedef struct Entity Entity; // Opaque structure with hidden members

// API functions that operate on 'Entity' objects
Entity* openEntity(int id);
int processEntity(Entity* e);
void closeEntity(Entity* e);
```

Clients call the API functions to allocate, operate on, and deallocate objects of an opaque data type. The contents of this type are known and accessible only to the implementation of the API functions; clients cannot directly access its contents. The source code for these functions defines the actual contents of the structure:

```mw
// Implementation file "api.c"

#include "api.h"

typedef struct Entity {
    int ent_id; // ID number
    char ent_name[20]; // Name
    ... and other members ...
} Entity;

// API function implementations
Entity* openEntity(int id) { 
    // ... 
}

int processEntity(Entity* e) {
    // ... 
}

void closeEntity(Entity* e) {
    // ... 
}
```

#### Name mangling

Below is an example of Python, which does not support variable access restrictions. However, the convention is that a variable whose name is prefixed by an underscore should be considered private.

```mw
class Car: 
    def __init__(self) -> None:
        self._maxspeed = 200
 
    def drive(self) -> None:
        print(f"Maximum speed is {self._maxspeed}.")
 
redcar: Car = Car()
redcar.drive()  # This will print 'Maximum speed is 200.'

redcar._maxspeed = 10
redcar.drive()  # This will print 'Maximum speed is 10.'
```
