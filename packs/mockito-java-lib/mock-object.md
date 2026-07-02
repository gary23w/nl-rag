---
title: "Mock object"
source: https://en.wikipedia.org/wiki/Mock_object
domain: mockito-java-lib
license: CC-BY-SA-4.0
tags: mockito mocking, java mock framework, mockito stub, mockito verify java
fetched: 2026-07-02
---

# Mock object

In computer programming, a **mock object** is an object that imitates a production object in limited ways. A programmer might use a mock object as a test double for software testing. A mock object can also be used in generic programming.

## Analogy

A mock object can be useful to the software tester like a car designer uses a crash test dummy to simulate a human in a vehicle impact.

## Motivation

In a unit test, mock objects can simulate the behavior of complex, real objects and are therefore useful when a real object is impractical or impossible to incorporate into a unit test. If an object has any of the following characteristics, it may be useful to use a mock object in its place:

- it supplies non-deterministic results (e.g. the current time or the current temperature)
- it has states that are difficult to create or reproduce (e.g. a network error)
- it is slow (e.g. a complete database, which would have to be prepared before the test)
- it does not yet exist or may change behavior
- it would have to include information and methods exclusively for testing purposes (and not for its actual task)

For example, an alarm clock program which causes a bell to ring at a certain time might get the current time from a time service. To test this, the test must wait until the alarm time to know whether it has rung the bell correctly. If a mock time service is used in place of the real time service, it can be programmed to provide the bell-ringing time (or any other time) regardless of the real time, so that the alarm clock program can be tested in isolation.

## Technical details

Mock objects have the same interface as the real objects they mimic, allowing a client object to remain unaware of whether it is using a real object or a mock object. Many available mock object frameworks allow the programmer to specify which methods will be invoked on a mock object, in what order, what parameters will be passed to them, and what values will be returned. Thus, the behavior of a complex object such as a network socket can be mimicked by a mock object, allowing the programmer to discover whether the object being tested responds appropriately to the wide variety of states such mock objects may be in.

### Mocks, fakes or stubs

The definitions of mock, fake and stub are not consistent across the literature. Nonetheless, all represent a production object in a testing environment by exposing the same interface.

Regardless of name, the simplest form returns pre-arranged responses (as in a method stub) and the most complex form imitates a production object's complete logic.

Such a test object might contain assertions to examine the context of each call. For example, a mock object might assert the order in which its methods are called, or assert consistency of data across method calls.

In the book *The Art of Unit Testing* mocks are described as a fake object that helps decide whether a test failed or passed by verifying whether an interaction with an object occurred. Everything else is defined as a stub. In that book, *fakes* are anything that is not real, which, based on their usage, can be either *stubs* or *mocks*.

### Setting expectations

Consider an example where an authorization subsystem has been mocked. The mock object implements an `isUserAllowed(task : Task) : boolean` method to match that in the real authorization class. Many advantages follow if it also exposes an `isAllowed : boolean` property, which is not present in the real class. This allows test code to easily set the expectation that a user will, or will not, be granted permission in the next call and therefore to readily test the behavior of the rest of the system in either case.

Similarly, mock-only settings could ensure that subsequent calls to the sub-system will cause it to throw an exception, hang without responding, or return `null` etc. Thus, it is possible to develop and test client behaviors for realistic fault conditions in back-end sub-systems, as well as for their expected responses. Without such a simple and flexible mock system, testing each of these situations may be too laborious for them to be given proper consideration.

### Writing log strings

A mock database object's `save(person : Person)` method may not contain much (if any) implementation code. It might check the existence and perhaps the validity of the Person object passed in for saving (see fake vs. mock discussion above), but beyond that there might be no other implementation.

This is a missed opportunity. The mock method could add an entry to a public log string. The entry need be no more than "Person saved", or it may include some details from the person object instance, such as a name or ID. If the test code also checks the final contents of the log string after various series of operations involving the mock database, then it is possible to verify that in each case exactly the expected number of database saves have been performed. This can find otherwise invisible performance-sapping bugs, for example, where a developer, nervous of losing data, has coded repeated calls to `save()` where just one would have sufficed.

## Use in test-driven development

Programmers working with the test-driven development (TDD) method make use of mock objects when writing software. Mock objects meet the interface requirements of, and stand in for, more complex real ones; thus they allow programmers to write and unit-test functionality in one area without calling complex underlying or collaborating classes. Using mock objects allows developers to focus their tests on the behavior of the system under test without worrying about its dependencies. For example, testing a complex algorithm based on multiple objects being in particular states can be clearly expressed using mock objects in place of real objects.

Apart from complexity issues and the benefits gained from this separation of concerns, there are practical speed issues involved. Developing a realistic piece of software using TDD may easily involve several hundred unit tests. If many of these induce communication with databases, web services and other out-of-process or networked systems, then the suite of unit tests will quickly become too slow to be run regularly. This in turn leads to bad habits and a reluctance by the developer to maintain the basic tenets of TDD.

When mock objects are replaced by real ones, the end-to-end functionality will need further testing. These will be integration tests rather than unit tests.

## Limitations

The use of mock objects can closely couple the unit tests to the implementation of the code that is being tested. For example, many mock object frameworks allow the developer to check the order of and number of times that mock object methods were invoked by the real object being tested; subsequent refactoring of the code that is being tested could therefore cause the test to fail even though all mocked object methods still obey the contract of the previous implementation. This illustrates that unit tests should test a method's external behavior rather than its internal implementation. Over-use of mock objects as part of a suite of unit tests can result in a dramatic increase in the amount of maintenance that needs to be performed on the tests themselves during system evolution as refactoring takes place. The improper maintenance of such tests during evolution could allow bugs to be missed that would otherwise be caught by unit tests that use instances of real classes. Conversely, simply mocking one method might require far less configuration than setting up an entire real class and therefore reduce maintenance needs.

Mock objects have to accurately model the behavior of the object they are mocking, which can be difficult to achieve if the object being mocked comes from another developer or project or if it has not even been written yet. If the behavior is not modelled correctly, then the unit tests may register a pass even though a failure would occur at run time under the same conditions that the unit test is exercising, thus rendering the unit test inaccurate.
