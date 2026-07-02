---
title: "Test double"
source: https://en.wikipedia.org/wiki/Test_double
domain: pytest-fixtures-lib
license: CC-BY-SA-4.0
tags: python pytest fixtures, pytest fixture setup, test fixture python
fetched: 2026-07-02
---

# Test double

A **test double** is software used in software test automation that satisfies a dependency so that the test need not depend on production code. A test double provides functionality via an interface that the software under test cannot distinguish from production code.

A programmer generally uses a test double to isolate the behavior of the consuming code from the rest of the codebase.

A test double is usually a simplified version of the production code and may include capabilities specific to testing.

Test doubles are used to build test harnesses.

## Uses

A test double may be used to simplify tests, increase speed of execution or allow for deterministic results of an action.

For example, a program that uses a database server is relatively slow and consumes significant system resources, which impedes testing productivity. A test might require data from the database that under normal system activity is regularly changing, so provides non-deterministic outputs for any given query. A test double can provide a static value instead of accessing a real database, thereby both avoiding network or system calls, and changing data.

A test double may also be used to test part of the system that is ready for testing even if its dependencies are not.

For example, in a system with modules Login, Home and User, suppose Login is ready for test, but the other two are not. The consumed functions of Home and User can be implemented as test doubles so that Login can be tested.

## Caveats

While test doubles are often used to facilitate unit testing there are limitation of using test doubles, the key one being that actual database connectivity or other external-access is not proven to work by those tests. To avoid errors that may be missed by this, other tests are needed that instantiate the code with the "real" implementations of the interfaces discussed above. These integration risks are typically covered by integration tests, system tests or system integration tests.

## Implementation approaches

When implementing test doubles, the typical approach involves two key steps:

1. Whenever external access is needed in production, an interface should be defined that describes the access available. See the dependency inversion principle for a discussion of the benefits of doing this regardless of TDD.
2. The interface should be implemented in two ways, one of which really accesses the external process for use in production, and the other of which is a test double typically a mock or a fake.

This approach enforces a unit-testable separation and drives more modular, testable and reusable code design.

## Types

Test doubles are categorization many ways.

### General

Although not universally accepted, Gerard Meszaros categorizes test doubles as:

- Stub — provides static input
- Mock — verifies output via expectations defined before the test runs
- Spy — supports setting the output of a call before a test runs and verifying input parameters after the test runs
- Fake — a relatively full-function implementation that is better suited to testing than the production version (e.g., an in-memory database instead of a database server)
- Dummy value — a value that is required for the tested interface but for which the test case does not depend

While there is no open standard for categories, Martin Fowler used these terms in his article, *Mocks Aren't Stubs* referring to Meszaros' book. Microsoft also used the same terms and definitions in an article titled, *Exploring The Continuum Of Test Doubles*.

### Service

For service-oriented architecture (SOA) systems and microservices, testers use test doubles that communicate with the system under test over a network protocol. These test doubles are called by different names by the tool vendors. A commonly used term is service virtualization. Other names used include API simulation, API mock, HTTP stub, HTTP mock, over the wire test double.

### Verified fake

A *verified fake* is a fake object whose behavior has been verified to match that of the real object using a set of tests that run against both the verified fake and the real implementation.
