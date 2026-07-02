---
title: "Test-driven development"
source: https://en.wikipedia.org/wiki/Test-driven_development
domain: xunit-dotnet-lib
license: CC-BY-SA-4.0
tags: xunit testing, dotnet unit test framework, xunit fact theory, xunit test collection
fetched: 2026-07-02
---

# Test-driven development

**Test-driven development** (**TDD**) is a way of writing code that involves writing an automated unit-level test case that fails, then writing just enough code to make the test pass, then refactoring both the test code and the production code, then repeating with another new test case.

Alternative approaches to writing automated tests is to write all of the production code before starting on the test code or to write all of the test code before starting on the production code. With TDD, both are written together, therefore shortening debugging time necessities.

TDD is related to the test-first programming concepts of extreme programming, begun in 1999, but more recently has created more general interest in its own right.

Programmers also apply the concept to improving and debugging legacy code developed with older techniques.

## History

Software engineer Kent Beck, who is credited with having developed or "rediscovered" the technique, stated in 2003 that TDD encourages simple designs and inspires confidence.

> The original description of TDD was in an ancient book about programming. It said you take the input tape, manually type in the output tape you expect, then program until the actual output tape matches the expected output. After I'd written the first xUnit framework in Smalltalk I remembered reading this and tried it out. That was the origin of TDD for me. When describing TDD to older programmers, I often hear, "Of course. How else could you program?" Therefore I refer to my role as "rediscovering" TDD.

— Kent Beck, "Why does Kent Beck refer to the 'rediscovery' of test-driven development? What's the history of test-driven development before Kent Beck's rediscovery?"

## Coding cycle

The TDD steps vary somewhat by author in count and description, but are generally as follows. These are based on the book *Test-Driven Development by Example*, and Kent Beck's Canon TDD article.

**1. List scenarios for the new feature**

List the expected variants in the new behavior. "There's the basic case & then what-if this service times out & what-if the key isn't in the database yet &…" The developer can discover these specifications by asking about

use cases

and

user stories

. A key benefit of TDD is that it makes the developer focus on requirements

before

writing code. This is in contrast with the usual practice, where unit tests are only written

after

code.

**2. Write a test for an item on the list**

Write an automated test that

would

pass if the variant in the new behavior is met.

**3. Run all tests. The new test should *fail* – for *expected* reasons**

This shows that new code is actually needed for the desired feature. It validates that the

test harness

is working correctly. It rules out the possibility that the new test is flawed and will always pass.

**4. Write the simplest code that passes the new test**

Inelegant code and

hard coding

is acceptable. The code will be honed in Step 6. No code should be added beyond the tested functionality.

**5. All tests should now pass**

If any fail, fix failing tests with minimal changes until all pass.

**6. Refactor as needed while ensuring all tests continue to pass**

Code is

refactored

for

readability

and maintainability. In particular, hard-coded test data should be removed from the production code. Running the test suite after each refactor ensures that no existing functionality is broken. Examples of refactoring:

- moving code to where it most logically belongs
- removing duplicate code
- making names self-documenting
- splitting methods into smaller pieces
- re-arranging inheritance hierarchies

**Repeat**

Repeat the process, starting at step 2, with each test on the list until all tests are implemented and passing.

Each tests should be small and commits made often. If new code fails some tests, the programmer can undo or revert rather than debug excessively.

When using external libraries, it is important not to write tests that are so small as to effectively test merely the library itself, unless there is some reason to believe that the library is buggy or not feature-rich enough to serve all the needs of the software under development.

## Test-driven work

TDD has been adopted outside of software development, in both product and service teams, as **test-driven work**. For testing to be successful, it needs to be practiced at the micro and macro levels. Every method in a class, every input data value, log message, and error code, amongst other data points, need to be tested. Similar to TDD, non-software teams develop quality control (QC) checks (usually manual tests rather than automated tests) for each aspect of the work prior to commencing. These QC checks are then used to inform the design and validate the associated outcomes. The six steps of the TDD sequence are applied with minor semantic changes:

1. "Add a check" replaces "Add a test"
2. "Run all checks" replaces "Run all tests"
3. "Do the work" replaces "Write some code"
4. "Run all checks" replaces "Run tests"
5. "Clean up the work" replaces "Refactor code"
6. "Repeat"

## Development style

There are various aspects to using test-driven development, for example the principles of "keep it simple, stupid" (KISS) and "You aren't gonna need it" (YAGNI). By focusing on writing only the code necessary to pass tests, designs can often be cleaner and clearer than is achieved by other methods. In *Test-Driven Development by Example*, Kent Beck also suggests the principle "Fake it till you make it".

To achieve some advanced design concept such as a design pattern, tests are written that generate that design. The code may remain simpler than the target pattern, but still pass all required tests. This can be unsettling at first but it allows the developer to focus only on what is important.

Writing the tests first: The tests should be written before the functionality that is to be tested. This has been claimed to have many benefits. It helps ensure that the application is written for testability, as the developers must consider how to test the application from the outset rather than adding it later. It also ensures that tests for every feature gets written. Additionally, writing the tests first leads to a deeper and earlier understanding of the product requirements, ensures the effectiveness of the test code, and maintains a continual focus on software quality.

When writing feature-first code, there is a tendency by developers and organizations to push the developer on to the next feature, even neglecting testing entirely. The first TDD test might not even compile at first, because the classes and methods it requires may not yet exist. Nevertheless, that first test functions as the beginning of an executable specification.

Each test case fails initially: This ensures that the test really works and can catch an error. Once this is shown, the underlying functionality can be implemented. This has led to the "test-driven development mantra", which is "red/green/refactor", where red means *fail* and green means *pass*. Test-driven development constantly repeats the steps of adding test cases that fail, passing them, and refactoring. Receiving the expected test results at each stage reinforces the developer's mental model of the code, boosts confidence and increases productivity.

### Code visibility

In test-driven development, writing tests before implementation raises questions about testing private methods versus testing only through public interfaces. This choice affects the design of both test code and production code.

### Test isolation

Test-driven development relies primarily on unit tests for its rapid red-green-refactor cycle. These tests execute quickly by avoiding process boundaries, network connections, or external dependencies. While TDD practitioners also write integration tests to verify component interactions, these slower tests are kept separate from the more frequent unit test runs. Testing multiple integrated modules together also makes it more difficult to identify the source of failures.

When code under development relies on external dependencies, TDD encourages the use of test doubles to maintain fast, isolated unit tests. The typical approach involves using interfaces to separate external dependencies and implementing test doubles for testing purposes.

Since test doubles don't prove the connection to real external components, TDD practitioners supplement unit tests with integration testing at appropriate levels. To keep execution faster and more reliable, testing is maximized at the unit level while minimizing slower tests at higher levels.

### Keep the unit small

For TDD, a unit is most commonly defined as a class, or a group of related functions often called a module. Keeping units relatively small is claimed to provide critical benefits, including:

- Reduced debugging effort – When test failures are detected, having smaller units aids in tracking down errors.
- Self-documenting tests – Small test cases are easier to read and to understand.

Advanced practices of test-driven development can lead to acceptance test–driven development (ATDD) and specification by example where the criteria specified by the customer are automated into acceptance tests, which then drive the traditional unit test-driven development (UTDD) process. This process ensures the customer has an automated mechanism to decide whether the software meets their requirements. With ATDD, the development team now has a specific target to satisfy – the acceptance tests – which keeps them continuously focused on what the customer really wants from each user story.

## Best practices

### Test structure

Effective layout of a test case ensures all required actions are completed, improves the readability of the test case, and smooths the flow of execution. Consistent structure helps in building a self-documenting test case. A commonly applied structure for test cases has (1) setup, (2) execution, (3) validation, and (4) cleanup.

- Setup: Put the unit under test (UUT) or the overall test system in the state needed to run the test.
- Execution: Trigger/drive the UUT to perform the target behavior and capture all output, such as return values and output parameters. This step is usually very simple.
- Validation: Ensure the results of the test are correct. These results may include explicit outputs captured during execution or state changes in the UUT.
- Cleanup: Restore the UUT or the overall test system to the pre-test state. This restoration permits another test to execute immediately after this one. In some cases, in order to preserve the information for possible test failure analysis, the cleanup should be starting the test just before the test's setup run.

### Individual best practices

Some best practices that an individual could follow would be to separate common set-up and tear-down logic into test support services utilized by the appropriate test cases, to keep each test oracle focused on only the results necessary to validate its test, and to design time-related tests to allow tolerance for execution in non-real time operating systems. The common practice of allowing a 5-10 percent margin for late execution reduces the potential number of false negatives in test execution. It is also suggested to treat test code with the same respect as production code. Test code must work correctly for both positive and negative cases, last a long time, and be readable and maintainable. Teams can get together and review tests and test practices to share effective techniques and catch bad habits.

### Practices to avoid, or "anti-patterns"

- Having test cases depend on system state manipulated from previously executed test cases (i.e., you should always start a unit test from a known and pre-configured state).
- Dependencies between test cases. A test suite where test cases are dependent upon each other is brittle and complex. Execution order should not be presumed. Basic refactoring of the initial test cases or structure of the UUT causes a spiral of increasingly pervasive impacts in associated tests.
- Interdependent tests. Interdependent tests can cause cascading false negatives. A failure in an early test case breaks a later test case even if no actual fault exists in the UUT, increasing defect analysis and debug efforts.
- Testing precise execution, timing or performance.
- Building "all-knowing oracles". An oracle that inspects more than necessary is more expensive and brittle over time. This very common error is dangerous because it causes a subtle but pervasive time sink across the complex project.
- Testing implementation details.
- Slow running tests.

## Comparison and demarcation

### TDD and ATDD

Test-driven development is related to, but different from acceptance test–driven development (ATDD). TDD is primarily a developer's tool to help create well-written unit of code (function, class, or module) that correctly performs a set of operations. ATDD is a communication tool between the customer, developer, and tester to ensure that the requirements are well-defined. TDD requires test automation. ATDD does not, although automation helps with regression testing. Tests used in TDD can often be derived from ATDD tests, since the code units implement some portion of a requirement. ATDD tests should be readable by the customer. TDD tests do not need to be.

### TDD and BDD

BDD (behavior-driven development) combines practices from TDD and from ATDD. It includes the practice of writing tests first, but focuses on tests which describe behavior, rather than tests which test a unit of implementation. Tools such as JBehave, Cucumber, Mspec and Specflow provide syntaxes which allow product owners, developers and test engineers to define together the behaviors which can then be translated into automated tests.

## Software for TDD

There are many testing frameworks and tools that are useful in TDD.

### xUnit frameworks

Developers may use computer-assisted testing frameworks, commonly collectively named xUnit (which are derived from SUnit, created in 1998), to create and automatically run the test cases. xUnit frameworks provide assertion-style test validation capabilities and result reporting. These capabilities are critical for automation as they move the burden of execution validation from an independent post-processing activity to one that is included in the test execution. The execution framework provided by these test frameworks allows for the automatic execution of all system test cases or various subsets along with other features.

### TAP results

Testing frameworks may accept unit test output in the language-agnostic Test Anything Protocol created in 1987.

## TDD for complex systems

Exercising TDD on large systems requires a modular architecture, defined components with published interfaces, and disciplined system layering with maximization of platform independence. These proven practices yield increased testability and facilitate the application of build and test automation.

### Designing for testability

Complex systems require an architecture that meets a range of requirements. A key subset of these requirements includes support for the complete and effective testing of the system. Effective modular design yields components that share traits essential for effective TDD.

- High Cohesion ensures each unit provides a set of related capabilities and makes the tests of those capabilities easier to maintain.
- Low Coupling allows each unit to be effectively tested in isolation.
- Published Interfaces restrict Component access and serve as contact points for tests, facilitating test creation and ensuring the highest fidelity between test and production unit configuration.

A key technique for building effective modular architecture is Scenario Modeling where a set of sequence charts is constructed, each one focusing on a single system-level execution scenario. The Scenario Model provides an excellent vehicle for creating the strategy of interactions between components in response to a specific stimulus. Each of these Scenario Models serves as a rich set of requirements for the services or functions that a component must provide, and it also dictates the order in which these components and services interact together. Scenario modeling can greatly facilitate the construction of TDD tests for a complex system.

### Managing tests for large teams

In a larger system, the impact of poor component quality is magnified by the complexity of interactions. This magnification makes the benefits of TDD accrue even faster in the context of larger projects. However, the complexity of the total population of tests can become a problem in itself, eroding potential gains. It sounds simple, but a key initial step is to recognize that test code is also important software and should be produced and maintained with the same rigor as the production code.

Creating and managing the architecture of test software within a complex system is just as important as the core product architecture. Test drivers interact with the UUT, test doubles and the unit test framework.

## Advantages and disadvantages

Empirical studies of test-driven development (TDD) have reported mixed results. Reviews generally find evidence that TDD can improve some measures of software quality, but its effect on productivity is less consistent. A 2013 meta-analysis of 27 studies found a small positive effect on external quality and little or no overall effect on productivity, with larger quality gains but also larger productivity reductions in industrial studies. A 2016 systematic review of studies published between 1999 and 2014 found that most studies reported improvements in internal and external software quality, but that productivity results varied between academic and industrial settings.

A comparative analysis of empirical studies concluded that TDD may reduce introduced defects and lead to more maintainable code, while some implemented code may be smaller or less complex. However, an industry experiment with professional developers found that the effect of TDD depended strongly on task characteristics, and concluded that further evidence was needed before determining whether TDD was better or worse than incremental test-last development in industrial settings. A later study of TDD process characteristics found that quality and productivity improvements were associated more with small, uniform development steps than with the test-first ordering itself.

### Potential benefits

TDD can provide rapid feedback during development because the developer repeatedly runs a growing set of automated tests. This can make regressions easier to detect soon after they are introduced, and can support refactoring by providing a safety net for behavioral changes. Because tests are written before the corresponding production code, the developer must consider the desired behavior and interface of the code before implementation. This can encourage smaller units of code, looser coupling, and clearer interfaces, especially when tests are written against public behavior rather than implementation details.

TDD also tends to produce a suite of automated tests as a by-product of development. Such tests can be useful in continuous integration workflows, where changes are tested frequently before being merged or released. In this sense, TDD may improve confidence in later changes, although passing unit tests do not by themselves prove that the software is correct.

### Limitations

TDD is not a substitute for other forms of software testing. Since TDD is commonly practiced through unit testing, it may not adequately test behavior that depends on user interfaces, databases, distributed systems, hardware, timing, security properties, or interactions between components. These areas often require additional integration testing, system testing, acceptance testing, usability testing, or other specialized testing methods.

Tests written during TDD may share the same misunderstandings as the production code. If a developer misinterprets a requirement, both the test and the implementation can encode the same incorrect assumption, causing the test to pass while the software remains wrong. A large number of passing tests can therefore create a false sense of security if the tests are incomplete, overly narrow, or focused on implementation details rather than externally visible behavior.

Automated tests also create maintenance costs. Tests that are tightly coupled to internal implementation details, use excessive mocking, rely on fragile timing assumptions, or contain duplicated setup code can become difficult to maintain. In some contexts, especially complex brownfield tasks or projects with limited automated-testing experience, the time required to write and maintain tests may reduce short-term productivity.

## Conference

First TDD Conference was held during July 2021. Conferences were recorded on YouTube
