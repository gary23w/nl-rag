---
title: "Precondition"
source: https://en.wikipedia.org/wiki/Precondition
domain: hoare-logic-deep
license: CC-BY-SA-4.0
tags: Hoare logic, Hoare triple, partial correctness, total correctness
fetched: 2026-07-02
---

# Precondition

In computer programming, a **precondition** is a condition or predicate that must always be true just prior to the execution of some section of code or before an operation in a formal specification.

If a precondition is violated, the effect of the section of code becomes undefined and thus may or may not carry out its intended work. Preconditions that are missing, insufficient, or not formally proved (or have an incorrect attempted proof), or are not checked statically or dynamically, can give rise to Security problems, particularly in unsafe languages that are not strongly typed.

Often, preconditions are simply included in the documentation of the affected section of code. Preconditions are sometimes tested using guards or assertions within the code itself, and some languages have specific syntactic constructions for doing so.

## Example

The factorial function is only defined where its parameter is an integer greater than or equal to zero. So an implementation of the factorial function would have a precondition that its parameter be an integer *and* that the parameter be greater than or equal to zero. Alternatively the type system of the language may be used to specify that the parameter of the factorial function is a natural number (unsigned integer), which can be formally verified automatically by a compiler's type checker.

In addition where numeric types have a limited range (as they do in most programming languages) the precondition must also specify the maximum value that the parameter may have if overflow is not to occur. (e.g. if an implementation of factorial returns the result in a 64-bit unsigned integer then the parameter must be less than 21 because factorial(21) is larger than the maximum unsigned integer that can be stored in 64 bits). Where the language supports range sub-types (e.g. Ada) such constraints can be automatically verified by the type system. More complex constraints can be formally verified interactively with a proof assistant.

## In object-oriented programming

Preconditions in object-oriented software development are an essential part of design by contract. Design by contract also includes notions of postcondition and class invariant.

The precondition for any routine defines any constraints on object state which are necessary for successful execution. From the program developer's viewpoint, this constitutes the routine caller's portion of the contract. The caller then is obliged to ensure that the precondition holds prior to calling the routine. The reward for the caller's effort is expressed in the called routine's postcondition.

### Eiffel example

The routine in the following example written in Eiffel takes as an argument an integer which must be a valid value for an hour of the day, i. e., 0 through 23, inclusively. The precondition follows the keyword `require`. It specifies that the argument must be greater than or equal to zero and less than 24. The tag `valid_argument` describes this precondition clause and serves to identify it in case of a runtime precondition violation.

```mw
    set_hour (a_hour: INTEGER)
            -- Set `hour' to `a_hour'
        require
            valid_argument: 0 <= a_hour and a_hour < 24
        do
            hour := a_hour
        ensure
            hour_set: hour = a_hour
        end
```

### Preconditions and inheritance

In the presence of inheritance, the routines inherited by descendant classes (subclasses) do so with their preconditions in force. This means that any implementations or redefinitions of inherited routines also have to be written to comply with their inherited contract. Preconditions can be modified in redefined routines, but they may only be weakened. That is, the redefined routine may lessen the obligation of the client, but not increase it.
