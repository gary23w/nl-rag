---
title: "Gradual typing"
source: https://en.wikipedia.org/wiki/Gradual_typing
domain: gradual-typing
license: CC-BY-SA-4.0
tags: gradual typing, dynamic type checking, type soundness, blame calculus
fetched: 2026-07-02
---

# Gradual typing

**Gradual typing** is a type system that allows for both static typing and dynamic typing *but enforces types at runtime*. Gradual typing allows software developers to choose either type paradigm as appropriate, from within a single language.

In many cases gradual typing is added to an existing dynamic language, creating a derived language *allowing* for, but not *requiring*, static typing to be used. In some cases, a language uses gradual typing from the start. However, there are performance and implementation complexity tradeoffs compared to dynamic or optional typing.

## History

The term was coined by Jeremy Siek, who developed gradual typing in 2006 with Walid Taha.

## Implementation

In gradual typing, a special type named *dynamic* is used to represent statically-unknown types. The notion of type equality is replaced by a new relation called *consistency* that relates the dynamic type to every other type. The consistency relation is reflexive and symmetric but not transitive.

Prior attempts at integrating static and dynamic typing tried to make the dynamic type be both the top and bottom of the subtype hierarchy. However, because subtyping is transitive, that results in every type becoming related to every other type, and so subtyping would no longer rule out any static type errors. The addition of a second phase of plausibility checking to the type system did not completely solve this problem.

Gradual typing can easily be integrated into the type system of an object-oriented language that already uses the subsumption rule to allow implicit upcasts with respect to subtyping. The main idea is that consistency and subtyping are orthogonal ideas that compose nicely. To add subtyping to a gradually-typed language, simply add the subsumption rule and add a subtyping rule that makes the dynamic type a subtype of itself, because subtyping is supposed to be reflexive. (But do not make the top of the subtyping order dynamic!)

## Comparison With Optional Types

Gradual and optional typing are similar in that variables and expressions may be given types and the correctness of the typing is checked at compile time (which is *static typing*). However, in a gradual type system, runtime checks are inserted at the boundaries of typed and untyped code. In an optional type system, all types are erased at compile time and untyped values can propagate through code that had type annotations.

```mw
class Account { 
  credits:int //number of credits in account, statically typed
  new(credits:int) {
    this.credits = credits; 
  }
  
  compare(account:Account){
     //won't throw error in optionally typed as "1" > 1 is a valid comparison
    return this.credits > account.credits;
  }
  
  spendCredit(){
     this.credits = this.credits - 1; //optionally typed throws here
  }
  
}

//assume everything below executes at runtime/after Account has been compiled
let a = new Account(1); //valid in both systems
let b = new Account("2"); //gradually typed throws here, preventing invalid Account instances
b.compare(a); //optionally typed returns false
b.spendCredit(); //optionally typed throws here
```

In a gradually typed language, an exception would be raised anytime a non-integer value is supplied for `credit` and stack traces would stop at invalid calls (`new Account("2")`). In an optionally typed language, an exception would only be raised when the language is forced to perform operations that would be incompatible with its type: `credit` can be set to "1" (a *string*) but this would only throw an error when performing math on it (e.x. when `spendCredit` attempts to subtract the *integer* 1). `compare` functions as normal, illustrating how a program running in production could create and manipulate invalid `Accounts` without triggering an error. This could result in data corruption if the invalid instances are saved to a datastore.

Getting similar results in an optionally typed language requires a programmer to manually perform type checking by inserting guards:

```mw
class Account { 
  private credit:int //private prevents external code setting (invalid) value
  new(credit:int) {
    this.setCredit(credit); //must flow through guarded setter
  }
  
  //setter to ensure only values of the correct type are assigned
  setCredit(credit:int){ 
    if(isInt(credit)){ //manual type check to guard against data corruption
      this.credit = credit; 
    } else {
      throw TypeError;
    }
  }
  
  compare(account:Account){ //types are stripped at compile time
    if(instanceOf(account, Account)){ //manual type checks everywhere!
      return this.credit > account.credit;
    } else {
      throw TypeError;
    }
  }
  
  //since the private `credits` field can only be accessed within the class,
  //methods can rely on compile time type checking.
  spendCredit(){
     this.credits = this.credits - 1; //no need for `isInt(this.credits)`
  }
  
}

//assume everything below executes at runtime/after Account has been compiled
let a = new Account(1); //valid
let b = new Account("2"); //stacktrace wouldn't stop here, but inside `setCredit`
```

Note however, that stack traces won't trace to the offending call but the setter. If the programmer forgets to pass externally provided values through the setter, it's still possible that an invalid instance could be created and saved to disk but discovered during a later execution. This makes data corruption harder to prevent and impedes tracking down offending code paths.

## Implementations

Examples of gradually typed languages derived from existing dynamically typed languages include Closure Compiler, Hack (for PHP), PHP (since 7.0), Typed Racket (for Racket), Typed Clojure (for Clojure), or cperl (a typed Perl 5). ActionScript was a gradually typed language that interoperated with ECMAScript, though it originally arose separately as a sibling, both influenced by Apple's HyperTalk.

A system for the J programming language has been developed, adding coercion, error propagation and filtering to the normal validation properties of the type system as well as applying type functions outside of function definitions, thereby the increasing flexibility of type definitions.

Conversely, C# started as a statically typed language, but as of version 4.0 is gradually typed, allowing variables to be explicitly marked as dynamic by using the `dynamic` type.

Raku (formerly Perl6) has had gradual typing implemented from the start. Type checks occur at all locations where values are assigned or bound. An "untyped" variable or parameter is typed as `Any`, which will match (almost) all values. The compiler flags type-checking conflicts at compile time if it can determine at compile time that they will never succeed.

Objective-C has gradual typing for object pointers with respect to method calls. Static typing is used when a variable is typed as pointer to a certain class of object: when a method call is made to the variable, the compiler statically checks that the class is declared to support such a method, or it generates a warning or error. However, if a variable of the type `id` is used, the compiler will allow any method to be called on it.

The JS++ programming language, released in 2011, is a superset of JavaScript (dynamically typed) with a gradual type system that is sound for ECMAScript and DOM API corner cases.

GDScript, the Godot game engine's primary scripting language, started out dynamically typed and introduced gradual typing with version 3.1 of the engine, allowing users to type variables, function parameters, arrays and dictionaries through type hints. Additionally, when assigning a value to a variable using the `:=` notation, Godot will attempt to infer the type of the variable at build time.
