---
title: "Design by contract"
source: https://en.wikipedia.org/wiki/Design_by_contract
domain: formal-methods
license: CC-BY-SA-4.0
tags: formal verification, model checking, tla+, hoare logic, design by contract, static analysis
fetched: 2026-07-02
---

# Design by contract

**Design by contract** (**DbC**), also known as **contract programming**, **programming by contract** and **design-by-contract programming**, is an approach for designing software.

It prescribes that software designers should define formal, precise and verifiable interface specifications for software components, which extend the ordinary definition of abstract data types with preconditions, postconditions and invariants. These specifications are referred to as "contracts", in accordance with a conceptual metaphor with the conditions and obligations of business contracts.

The DbC approach assumes all *client components* that invoke an operation on a *server component* will meet the preconditions specified as required for that operation.

Where this assumption is considered too risky (as in multi-channel or distributed computing), the inverse approach is taken, meaning that the *server component* tests that all relevant preconditions hold true (before, or while, processing the *client component'*s request) and replies with a suitable error message if not.

## History

The term was coined by Bertrand Meyer in connection with his design of the Eiffel programming language and first described in various articles starting in 1986 and the two successive editions (1988, 1997) of his book *Object-Oriented Software Construction*. Eiffel Software applied for trademark registration for *Design by Contract* in December 2003, and it was granted in December 2004. The current owner of this trademark is Eiffel Software.

Design by contract has its roots in work on formal verification, formal specification and Hoare logic. The original contributions include:

- A clear metaphor to guide the design process
- The application to inheritance, in particular a formalism for redefinition and dynamic binding
- The application to exception handling
- The connection with automatic software documentation

## Description

The central idea of DbC is a metaphor on how elements of a software system collaborate with each other on the basis of mutual *obligations* and *benefits*. The metaphor comes from business life, where a "client" and a "supplier" agree on a "contract" that defines, for example, that:

- The supplier must provide a certain product (obligation) and is entitled to expect that the client has paid its fee (benefit).
- The client must pay the fee (obligation) and is entitled to get the product (benefit).
- Both parties must satisfy certain obligations, such as laws and regulations, applying to all contracts.

Similarly, if the method of a class in object-oriented programming provides a certain functionality, it may:

- Expect a certain condition to be guaranteed on entry by any client module that calls it: the method's precondition—an obligation for the client, and a benefit for the supplier (the method itself), as it frees it from having to handle cases outside of the precondition.
- Guarantee a certain property on exit: the method's postcondition—an obligation for the supplier, and obviously a benefit (the main benefit of calling the method) for the client.
- Maintain a certain property, assumed on entry and guaranteed on exit: the class invariant.

The contract is semantically equivalent to a Hoare triple which formalises the obligations. This can be summarised by the "three questions" that the designer must repeatedly answer in the contract:

- What does the contract expect?
- What does the contract guarantee?
- What does the contract maintain?

Many programming languages have facilities to make assertions like these. However, DbC considers these contracts to be so crucial to software correctness that they should be part of the design process. In effect, DbC advocates writing the assertions first. Contracts can be written by code comments, enforced by a test suite, or both, even if there is no special language support for contracts.

The notion of a contract extends down to the method/procedure level; the contract for each method will normally contain the following pieces of information:

- Acceptable and unacceptable input values or types, and their meanings
- Return values or types, and their meanings
- Error and exception condition values or types that can occur, and their meanings
- Side effects
- Preconditions
- Postconditions
- Invariants
- (more rarely) Performance guarantees, e.g. for time or space used

Subclasses in an inheritance hierarchy are allowed to weaken preconditions (but not strengthen them) and strengthen postconditions and invariants (but not weaken them). These rules approximate behavioural subtyping.

All class relationships are between client classes and supplier classes. A client class is obliged to make calls to supplier features where the resulting state of the supplier is not violated by the client call. Subsequently, the supplier is obliged to provide a return state and data that does not violate the state requirements of the client.

For instance, a supplier data buffer may require that data is present in the buffer when a delete feature is called. Subsequently, the supplier guarantees to the client that when a delete feature finishes its work, the data item will, indeed, be deleted from the buffer. Other design contracts are concepts of class invariant. The class invariant guarantees (for the local class) that the state of the class will be maintained within specified tolerances at the end of each feature execution.

When using contracts, a supplier will verify that the contract conditions are satisfied—a practice known as offensive programming—the general idea being that code should "fail hard", with contract verification being the safety net.

DbC's "fail hard" property simplifies the debugging of contract behavior, as the intended behaviour of each method is clearly specified.

This approach differs substantially from that of defensive programming, where the supplier is responsible for figuring out what to do when a precondition is broken. More often than not, the supplier throws an exception to inform the client that the precondition has been broken, and in both cases—DbC and defensive programming alike—the client must figure out how to respond to that. In such cases, DbC makes the supplier's job easier.

Design by contract also defines criteria for correctness for a software module:

- If the class invariant AND precondition are true before a supplier is called by a client, then the invariant AND the postcondition will be true after the service has been completed.
- When making calls to a supplier, a software module should not violate the supplier's preconditions.

Design by contract can also facilitate code reuse, since the contract for each piece of code is fully documented. The contracts for a module can be regarded as a form of software documentation for the behavior of that module.

Design by contract, in C++ for example, looks like the following:

```mw
int f(const int x)
    pre(x != 1) // a precondition assertion
    post(r : r == x && r != 2) // a postcondition assertion; r names the result object of f
{
    contract_assert(x != 3); // an assertion statement
    return x;
}
```

## Performance implications

Contract conditions should never be violated during execution of a bug-free program. Contracts are therefore typically only checked in debug mode during software development. Later at release, the contract checks are disabled to maximize performance.

In many programming languages, contracts are implemented with assert. Asserts are by default compiled away in release mode in C/C++, and similarly deactivated in C# and Java.

Launching the Python interpreter with "-O" (for "optimize") as an argument will likewise cause the Python code generator to not emit any bytecode for asserts.

This effectively eliminates the run-time costs of asserts in production code—irrespective of the number and computational expense of asserts used in development—as no such instructions will be included in production by the compiler.

## Relationship to software testing

Design by contract does not replace regular testing strategies, such as unit testing, integration testing and system testing. Rather, it complements external testing with internal self-tests that can be activated both for isolated tests and in production code during a test-phase.

The advantage of internal self-tests is that they can detect errors before they manifest themselves as invalid results observed by the client. This leads to earlier and more specific error detection.

The use of assertions can be considered to be a form of test oracle, a way of testing the design by contract implementation.

## Language support

### Languages with native support

Languages that implement most DbC features natively include:

- Ada 2012
  - SPARK (via static analysis of Ada programs)
- Ciao
- Clojure
- Cobra
- C++ (since C++26)
- D
- Dafny
- Eiffel
- Fortress
- Kotlin
- Mercury
- Oxygene (formerly Chrome and Delphi Prism)
- Racket (including higher order contracts, and emphasizing that contract violations must blame the guilty party and must do so with an accurate explanation)
- Sather
- Scala
- Vala
- Vienna Development Method (VDM)

Further, the standard method combination in the Common Lisp Object System has the method qualifiers `:before`, `:after` and `:around` that allow writing contracts as auxiliary methods, among other uses.
