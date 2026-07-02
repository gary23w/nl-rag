---
title: "Exception handling"
source: https://en.wikipedia.org/wiki/Exception_handling
domain: anyhow-error-rust
license: CC-BY-SA-4.0
tags: anyhow error handling, rust error library, anyhow context, rust error propagation
fetched: 2026-07-02
---

# Exception handling

In computing and computer programming, **exception handling** is the process of responding to the occurrence of *exceptions* – anomalous or exceptional conditions requiring special processing – during the execution of a program. In general, an exception breaks the normal flow of execution and executes a pre-registered *exception handler*; the details of how this is done depend on whether it is a hardware or software exception and how the software exception is implemented.

Exceptions are defined by different layers of a computer system, and the typical layers are CPU-defined interrupts, operating system (OS)-defined signals, and programming language-defined exceptions. Each layer requires different ways of exception handling although they may be interrelated, e.g. a CPU interrupt could be turned into an OS signal. Some exceptions, especially hardware ones, may be handled so gracefully that execution can resume where it was interrupted.

## Definition

The definition of an exception is based on the observation that each procedure has a precondition, a set of circumstances for which it will terminate "normally". An exception handling mechanism allows the procedure to *raise an exception* if this precondition is violated, for example if the procedure has been called on an abnormal set of arguments. The exception handling mechanism then *handles* the exception.

The precondition, and the definition of exception, is subjective. The set of "normal" circumstances is defined entirely by the programmer, e.g. the programmer may deem division by zero to be undefined, hence an exception, or devise some behavior such as returning zero or a special "ZERO DIVIDE" value (circumventing the need for exceptions). Common exceptions include an invalid argument (e.g. value is outside of the domain of a function), an unavailable resource (like a missing file, a network drive error, or out-of-memory errors), or that the routine has detected a normal condition that requires special handling, e.g., attention, end of file. Social pressure is a major influence on the scope of exceptions and use of exception-handling mechanisms, i.e. "examples of use, typically found in core libraries, and code examples in technical books, magazine articles, and online discussion forums, and in an organization’s code standards".

Exception handling solves the semipredicate problem, in that the mechanism distinguishes normal return values from erroneous ones. In languages without built-in exception handling such as C, routines would need to signal the error in some other way, such as the common return code and errno pattern. Taking a broad view, errors can be considered to be a proper subset of exceptions, and explicit error mechanisms such as errno can be considered (verbose) forms of exception handling. The term "exception" is preferred to "error" because it does not imply that anything is wrong - a condition viewed as an error by one procedure or programmer may not be viewed that way by another.

The term "exception" may be misleading because its connotation of "anomaly" indicates that raising an exception is abnormal or unusual, when in fact raising the exception may be a normal and usual situation in the program. For example, suppose a lookup function for an associative array throws an exception if the key has no value associated. Depending on context, this "key absent" exception may occur much more often than a successful lookup.

## History

The first hardware exception handling was found in the UNIVAC I from 1951. Arithmetic overflow executed two instructions at address 0 which could transfer control or fix up the result. Software exception handling developed in the 1960s and 1970s. Exception handling was subsequently widely adopted by many programming languages from the 1980s onward.

## Hardware exceptions

There is no clear consensus as to the exact meaning of an exception with respect to hardware. From the implementation point of view, it is handled identically to an interrupt: the processor halts execution of the current program, looks up the interrupt handler in the interrupt vector table for that exception or interrupt condition, saves state, and switches control.

## IEEE 754 floating-point exceptions

Exception handling in the IEEE 754 floating-point standard refers in general to exceptional conditions and defines an exception as "an event that occurs when an operation on some particular operands has no outcome suitable for every reasonable application. That operation might signal one or more exceptions by invoking the default or, if explicitly requested, a language-defined alternate handling."

By default, an IEEE 754 exception is resumable and is handled by substituting a predefined value for different exceptions, e.g. infinity for a divide by zero exception, and providing status flags for later checking of whether the exception occurred (see C language revision C99 for a typical example of handling of IEEE 754 exceptions). An exception-handling style enabled by the use of status flags involves: first computing an expression using a fast, direct implementation; checking whether it failed by testing status flags; and then, if necessary, calling a slower, more numerically robust, implementation.

The IEEE 754 standard uses the term "trapping" to refer to the calling of a user-supplied exception-handling routine on exceptional conditions, and is an optional feature of the standard. The standard recommends several usage scenarios for this, including the implementation of non-default pre-substitution of a value followed by resumption, to concisely handle removable singularities.

The default IEEE 754 exception handling behaviour of resumption following pre-substitution of a default value avoids the risks inherent in changing flow of program control on numerical exceptions. For example, the 1996 Cluster spacecraft launch ended in a catastrophic explosion due in part to the Ada exception handling policy of aborting computation on arithmetic error. William Kahan claims the default IEEE 754 exception handling behavior would have prevented this.

## In programming languages

In computer programming, several programming language mechanisms exist for exception handling. The term *exception* is typically used to denote a data structure storing information about an exceptional condition. One mechanism to transfer control, or *raise* an exception, is known as a *throw*; the exception is said to be *thrown*. Execution is transferred to a *catch*.

## In user interfaces

Front-end web development frameworks, such as React and Vue, have introduced error handling mechanisms where errors propagate up the user interface (UI) component hierarchy, in a way that is analogous to how errors propagate up the call stack in executing code. Here the error boundary mechanism serves as an analogue to the typical try-catch mechanism. Thus a component can ensure that errors from its child components are caught and handled, and not propagated up to parent components.

For example, in Vue.js, a component would catch errors by implementing `errorCaptured`

```mw
Vue.component('parent', {
    template: '<div><slot></slot></div>',
    errorCaptured: (err, vm, info) => alert('An error occurred');
})
Vue.component('child', {
    template: '<div>{{ cause_error() }}</div>'
})
```

When used like this in markup:

```mw
<parent>
    <child></child>
</parent>
```

The error produced by the child component is caught and handled by the parent component.
