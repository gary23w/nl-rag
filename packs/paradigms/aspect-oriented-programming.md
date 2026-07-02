---
title: "Aspect-oriented programming"
source: https://en.wikipedia.org/wiki/Aspect-oriented_programming
domain: paradigms
license: CC-BY-SA-4.0
tags: programming paradigm, object-oriented, functional programming, declarative, imperative programming
fetched: 2026-07-02
---

# Aspect-oriented programming

In computing, **aspect-oriented programming** (**AOP**) is a programming paradigm that aims to increase modularity by allowing the separation of *cross-cutting concerns*. It does so by adding behavior to existing code (an advice) *without* modifying the code, instead separately specifying which code is modified via a "pointcut" specification, such as "log all function calls when the function's name begins with 'set'". This allows behaviors that are not central to the business logic (such as logging) to be added to a program without cluttering the code of core functions.

AOP includes programming methods and tools that support the modularization of concerns at the level of the source code, while **aspect-oriented software development** refers to a whole engineering discipline.

Aspect-oriented programming entails breaking down program logic into cohesive areas of functionality (so-called *concerns*). Nearly all programming paradigms support some level of grouping and encapsulation of concerns into separate, independent entities by providing abstractions (e.g., functions, procedures, modules, classes, methods) that can be used for implementing, abstracting, and composing these concerns. Some concerns "cut across" multiple abstractions in a program, and defy these forms of implementation. These concerns are called *cross-cutting concerns* or horizontal concerns.

Logging exemplifies a cross-cutting concern because a logging strategy must affect every logged part of the system. Logging thereby *crosscuts* all logged classes and methods.

All AOP implementations have some cross-cutting expressions that encapsulate each concern in one place. The difference between implementations lies in the power, safety, and usability of the constructs provided. For example, interceptors that specify the methods to express a limited form of cross-cutting, without much support for type-safety or debugging. AspectJ has a number of such expressions and encapsulates them in a special class, called an aspect. For example, an aspect can alter the behavior of the base code (the non-aspect part of a program) by applying advice (additional behavior) at various join points (points in a program) specified in a quantification or query called a pointcut (that detects whether a given join point matches). An aspect can also make binary-compatible structural changes to other classes, such as adding members or parents.

## History

AOP has several direct antecedents: reflection and metaobject protocols, subject-oriented programming, Composition Filters, and Adaptive Programming.

Gregor Kiczales and colleagues at Xerox PARC developed the explicit concept of AOP and followed this with the AspectJ AOP extension to Java. IBM's research team pursued a tool approach over a language design approach and in 2001 proposed Hyper/J and the Concern Manipulation Environment, which have not seen wide use.

The examples in this article use AspectJ.

The Microsoft Transaction Server is considered to be the first major application of AOP followed by Enterprise JavaBeans.

## Motivation and basic concepts

Typically, an aspect is *scattered* or *tangled* as code, making it harder to understand and maintain. It is scattered by the function (such as logging) being spread over a number of unrelated functions that might use *its* function, possibly in entirely unrelated systems or written in different languages. Thus, changing logging can require modifying all affected modules. Aspects become tangled not only with the mainline function of the systems in which they are expressed but also with each other. Changing one concern thus entails understanding all the tangled concerns or having some means by which the effect of changes can be inferred.

For example, consider a banking application with a conceptually very simple method for transferring an amount from one account to another. Such an example in Java looks like:

```mw
sealed class BankingException 
    extends Exception 
    permits InsufficientFundsException, UnauthorisedUserException {
    // ...
}

public class Bank {
    public void transfer(Account fromAcc, Account toAcc, int amount) throws BankingException {
        if (fromAcc.getBalance() < amount) {
            throw new InsufficientFundsException();
        }

        fromAcc.withdraw(amount);
        toAcc.deposit(amount);
    }
}
```

However, this transfer method overlooks certain considerations that a deployed application would require, such as verifying that the current user is authorized to perform this operation, encapsulating database transactions to prevent accidental data loss, and logging the operation for diagnostic purposes.

A version with all those new concerns might look like this:

```mw
import java.util.logging.*;

sealed class BankingException 
    extends Exception 
    permits InsufficientFundsException, UnauthorisedUserException {
    // ...
}

public class Bank {
    private static final Logger logger;
    private final Database database;
    
    public void transfer(Account fromAcc, Account toAcc, int amount, User user) throws BankingException {
        logger.info("Transferring money...");
  
        if (!isUserAuthorised(user, fromAcc)) {
            logger.log(Level.WARNING, "User has no permission.");
            throw new UnauthorisedUserException();
        }
  
        if (fromAcc.getBalance() < amount) {
            logger.log(Level.WARNING, "Insufficient funds.");
            throw new InsufficientFundsException();
        }

        fromAcc.withdraw(amount);
        toAcc.deposit(amount);

        database.commitChanges(); // Atomic operation.

        logger.log(Level.INFO, "Transaction successful.");
    }
}
```

In this example, other interests have become *tangled* with the basic functionality (sometimes called the *business logic concern*). Transactions, security, and logging all exemplify *cross-cutting concerns*.

Now consider what would happen if we suddenly need to change the security considerations for the application. In the program's current version, security-related operations appear *scattered* across numerous methods, and such a change would require major effort.

AOP tries to solve this problem by allowing the programmer to express cross-cutting concerns in stand-alone modules called *aspects*. Aspects can contain *advice* (code joined to specified points in the program) and *inter-type declarations* (structural members added to other classes). For example, a security module can include advice that performs a security check before accessing a bank account. The pointcut defines the times (join points) when one can access a bank account, and the code in the advice body defines how the security check is implemented. That way, both the check and the places can be maintained in one place. Further, a good pointcut can anticipate later program changes, so if another developer creates a new method to access the bank account, the advice will apply to the new method when it executes.

So for the example above implementing logging in an aspect:

```mw
aspect Logger {
    Logger logger;

    void Bank.transfer(Account fromAcc, Account toAcc, int amount, User user)  {
        logger.info("Transferring money...");
    }

    void Bank.getMoneyBack(User user, int transactionId)  {
        logger.info("User requested money back.");
    }

    // Other crosscutting code.
}
```

One can think of AOP as a debugging tool or a user-level tool. Advice should be reserved for cases in which one cannot get the function changed (user level) or do not want to change the function in production code (debugging).

## Join point models

The advice-related component of an aspect-oriented language defines a join point model (JPM). A JPM defines three things:

1. When the advice can run. These are called *join points* because they are points in a running program where additional behavior can be usefully joined. A join point needs to be addressable and understandable by an ordinary programmer to be useful. It should also be stable across inconsequential program changes to maintain aspect stability. Many AOP implementations support method executions and field references as join points.
2. A way to specify (or *quantify*) join points, called *pointcuts*. Pointcuts determine whether a given join point matches. Most useful pointcut languages use a syntax like the base language (for example, AspectJ uses Java signatures) and allow reuse through naming and combination.
3. A means of specifying code to run at a join point. AspectJ calls this *advice*, and can run it before, after, and around join points. Some implementations also support defining a method in an aspect on another class.

Join-point models can be compared based on the join points exposed, how join points are specified, the operations permitted at the join points, and the structural enhancements that can be expressed.

### AspectJ's join-point model

- The join points in AspectJ include method or constructor call or execution, the initialization of a class or object, field read and write access, and exception handlers. They do not include loops, super calls, throws clauses, or multiple statements.
- Pointcuts are specified by combinations of *primitive pointcut designators* (PCDs). "Kinded" PCDs match a particular kind of join point (e.g., method execution) and often take a Java-like signature as input. One such pointcut looks like this: execution(* set*(*)) This pointcut matches a method-execution join point, if the method name starts with "`set`" and there is exactly one argument of any type. "Dynamic" PCDs check runtime types and bind variables. For example, this(Point) This pointcut matches when the currently executing object is an instance of class `Point`. Note that the unqualified name of a class can be used via Java's normal type lookup. "Scope" PCDs limit the lexical scope of the join point. For example: within(com.company.*) This pointcut matches any join point in any type in the `com.company` package. The *`*`* is one form of the wildcards that can be used to match many things with one signature. Pointcuts can be composed and named for reuse. For example: pointcut set() : execution(* set*(*) ) && this(Point) && within(com.company.*); This pointcut matches a method-execution join point, if the method name starts with "`set`" and `this` is an instance of type `Point` in the `com.company` package. It can be referred to using the name "`set()`".
- Advice specifies to run at (before, after, or around) a join point (specified with a pointcut) certain code (specified like code in a method). The AOP runtime invokes Advice automatically when the pointcut matches the join point. For example: after() : set() { Display.update(); } This effectively specifies: "if the *`set()`* pointcut matches the join point, run the code `Display.update()` after the join point completes."

### Other potential join point models

There are other kinds of JPMs. All advice languages can be defined in terms of their JPM. For example, a hypothetical aspect language for UML may have the following JPM:

- Join points are all model elements.
- Pointcuts are some Boolean expression combining the model elements.
- The means of affect at these points are a visualization of all the matched join points.

### Inter-type declarations

*Inter-type declarations* provide a way to express cross-cutting concerns affecting the structure of modules. Also known as *open classes* and *extension methods*, this enables programmers to declare in one place members or parents of another class, typically to combine all the code related to a concern in one aspect. For example, if a programmer implemented the cross-cutting display-update concern using visitors, an inter-type declaration using the visitor pattern might look like this in AspectJ:

```mw
aspect DisplayUpdate {
    void Point.acceptVisitor(Visitor v) {
        v.visit(this);
    }
    // other crosscutting code...
}
```

This code snippet adds the `acceptVisitor` method to the `Point` class.

Any structural additions are required to be compatible with the original class, so that clients of the existing class continue to operate, unless the AOP implementation can expect to control all clients at all times.

## Implementation

AOP programs can affect other programs in two different ways, depending on the underlying languages and environments:

1. a combined program is produced, valid in the original language and indistinguishable from an ordinary program to the ultimate interpreter
2. the ultimate interpreter or environment is updated to understand and implement AOP features.

The difficulty of changing environments means most implementations produce compatible combination programs through a type of program transformation known as *weaving*. An aspect weaver reads the aspect-oriented code and generates appropriate object-oriented code with the aspects integrated. The same AOP language can be implemented through a variety of weaving methods, so the semantics of a language should never be understood in terms of the weaving implementation. Only the speed of an implementation and its ease of deployment are affected by the method of combination used.

Systems can implement source-level weaving using preprocessors (as C++ was implemented originally in CFront) that require access to program source files. However, Java's well-defined binary form enables bytecode weavers to work with any Java program in .class-file form. Bytecode weavers can be deployed during the build process or, if the weave model is per-class, during class loading. AspectJ started with source-level weaving in 2001, delivered a per-class bytecode weaver in 2002, and offered advanced load-time support after the integration of AspectWerkz in 2005.

Any solution that combines programs at runtime must provide views that segregate them properly to maintain the programmer's segregated model. Java's bytecode support for multiple source files enables any debugger to step through a properly woven .class file in a source editor. However, some third-party decompilers cannot process woven code because they expect code produced by Javac rather than all supported bytecode forms (see also § Criticism, below).

Deploy-time weaving offers another approach. This basically implies post-processing, but rather than patching the generated code, this weaving approach *subclasses* existing classes so that the modifications are introduced by method-overriding. The existing classes remain untouched, even at runtime, and all existing tools, such as debuggers and profilers, can be used during development. A similar approach has already proven itself in the implementation of many Java EE application servers, such as IBM's WebSphere.

### Terminology

Standard terminology used in Aspect-oriented programming may include:

**Cross-cutting concerns**

Even though most classes in an object-oriented model will perform a single, specific function, they often share common, secondary requirements with other classes. For example, we may want to add logging to classes within the data-access layer and also to classes in the UI layer whenever a thread enters or exits a method. Further concerns can be related to security such as

access control

or

information flow control

.

Even though each class has a very different primary functionality, the code needed to perform the secondary functionality is often identical.

**Advice**

This is the additional code that you want to apply to your existing model. In our example, this is the logging code that we want to apply whenever the thread enters or exits a method.:

**Pointcut**

This refers to the point of execution in the application at which cross-cutting concern needs to be applied. In our example, a pointcut is reached when the thread enters a method, and another pointcut is reached when the thread exits the method.

**Aspect**

The combination of the pointcut and the advice is termed an aspect. In the example above, we add a logging aspect to our application by defining a pointcut and giving the correct advice.

## Comparison to other programming paradigms

Aspects emerged from object-oriented programming and reflective programming. AOP languages have functionality similar to, but more restricted than, metaobject protocols. Aspects relate closely to programming concepts like subjects, mixins, and delegation. Other ways to use aspect-oriented programming paradigms include Composition Filters and the hyperslices approach. Since at least the 1970s, developers have been using forms of interception and dispatch-patching that resemble some of the implementation methods for AOP, but these never had the semantics that the cross-cutting specifications provide in one place.

Designers have considered alternative ways to achieve separation of code, such as C#'s partial types, but such approaches lack a quantification mechanism that allows reaching several join points of the code with one declarative statement.

Though it may seem unrelated, in testing, the use of mocks or stubs requires the use of AOP techniques, such as around advice. Here the collaborating objects are for the purpose of the test, a cross-cutting concern. Thus, the various Mock Object frameworks provide these features. For example, a process invokes a service to get a balance amount. In the test of the process, it is unimportant where the amount comes from, but only that the process uses the balance according to the requirements.

## Adoption issues

Programmers need to be able to read and understand code to prevent errors. Even with proper education, understanding cross-cutting concerns can be difficult without proper support for visualizing both static structure and the dynamic flow of a program. Starting in 2002, AspectJ began to provide IDE plug-ins to support the visualizing of cross-cutting concerns. Those features, as well as aspect code assist and refactoring, are now common.

Given the power of AOP, making a logical mistake in expressing cross-cutting can lead to widespread program failure. Conversely, another programmer may change the join points in a program, such as by renaming or moving methods, in ways that the aspect writer did not anticipate and with unforeseen consequences. One advantage of modularizing cross-cutting concerns is enabling one programmer to easily affect the entire system. As a result, such problems manifest as a conflict over responsibility between two or more developers for a given failure. AOP can expedite solving these problems, as only the aspect must be changed. Without AOP, the corresponding problems can be much more spread out.

## Criticism

The most basic criticism of the effect of AOP is that control flow is obscured, and that it is not only worse than the much-maligned GOTO statement, but is closely analogous to the joke COME FROM statement. The *obliviousness of application*, which is fundamental to many definitions of AOP (the code in question has no indication that an advice will be applied, which is specified instead in the pointcut), means that the advice is not visible, in contrast to an explicit method call. For example, compare the COME FROM program:

```mw
 5 INPUT X
10 PRINT 'Result is :'
15 PRINT X
20 COME FROM 10
25      X = X * X
30 RETURN
```

with an AOP fragment with analogous semantics:

```mw
main() {
    input x
    print(result(x))
}

input result(int x) { 
    return x 
}

around(int x): call(result(int)) && args(x) {
    int temp = proceed(x)
    return temp * temp
}
```

Indeed, the pointcut may depend on runtime condition and thus not be statically deterministic. This can be mitigated but not solved by static analysis and IDE support showing which advices *potentially* match.

General criticisms are that AOP purports to improve "both modularity and the structure of code", but some counter that it instead undermines these goals and impedes "independent development and understandability of programs". Specifically, quantification by pointcuts breaks modularity: "one must, in general, have whole-program knowledge to reason about the dynamic execution of an aspect-oriented program." Further, while its goals (modularizing cross-cutting concerns) are well understood, its actual definition is unclear and not clearly distinguished from other well-established techniques. Cross-cutting concerns potentially cross-cut each other, requiring some resolution mechanism, such as ordering. Indeed, aspects can apply to themselves, leading to problems such as the liar paradox.

Technical criticisms include that the quantification of pointcuts (defining where advices are executed) is "extremely sensitive to changes in the program", which is known as the *fragile pointcut problem*. The problems with pointcuts are deemed intractable. If one replaces the quantification of pointcuts with explicit annotations, one obtains attribute-oriented programming instead, which is simply an explicit subroutine call and suffers the identical problem of scattering, which AOP was designed to solve.

## Implementations

Many programming languages have implemented AOP, within the language, or as an external library, including:

- .NET framework languages (C#, Visual Basic (.NET) (VB.NET))
  - PostSharp is a commercial AOP implementation with a free but limited edition.
  - Unity provides an API to facilitate proven practices in core areas of programming including data access, security, logging, exception handling and others.
  - AspectDN is an AOP implementation allowing to weave the aspects directly on the .NET executable files.
- ActionScript
- Ada
- AutoHotkey
- C, C++
- COBOL
- The Cocoa Objective-C frameworks
- ColdFusion
- Common Lisp
- Delphi
- Delphi Prism
- e (IEEE 1647)
- Emacs Lisp
- Groovy
- Haskell
- Java
  - AspectJ
- JavaScript
- Logtalk
- Lua
- make
- Matlab
- ML
- Nemerle
- Perl
- PHP
- Prolog
- Python
- Racket
- Ruby
- Squeak Smalltalk
- UML 2.0
- XML
