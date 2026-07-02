---
title: "Test automation"
source: https://en.wikipedia.org/wiki/Test_automation
domain: junit5-java-lib
license: CC-BY-SA-4.0
tags: junit5 testing, java unit test framework, junit jupiter, junit jupiter api
fetched: 2026-07-02
---

# Test automation

**Test automation** is the use of software (separate from the software being tested) for controlling the execution of tests and comparing actual outcome with predicted. Test automation supports testing the system under test (SUT) without manual interaction which can lead to faster test execution and testing more often. Test automation is a key aspect of continuous testing and often for continuous integration and continuous delivery (CI/CD).

## Compared to manual testing

Automation provides many benefits over manual testing.

### API testing

For API testing, tests drive the SUT via its application programming interface (API). Compared to manual testing, automated API testing often can execute a relatively large number of cases in a relatively short time.

### GUI testing

For GUI testing, tests drive the SUT via its graphical user interface (GUI) by generating events such as keystrokes and mouse clicks. Automated GUI testing can be challenging to develop, but can run much faster than a human could perform the same testing. Specializations include:

- Record & playback testing – Some GUI testing tools provide a feature that allows for interactively recording user actions and replaying them later as a test, comparing actual results to expected. An advantage of this approach is that it requires little or no coding. However, some claim that such tests suffer from reliability, maintainability and accuracy issues. For example, changing the label of a button or moving it to another part of the view may require tests to be re-recorded, and such tests often are inefficient and incorrectly record unimportant activities.

- For testing a web site, the GUI is the browser and interaction is via DOM events and HTML. A headless browser or solutions based on Selenium Web Driver are normally used for this purpose.

### Regression testing

When automated testing is in place, regression testing can be a relatively quick and easy operation. Instead of a significant outlay of human time and effort, a regression test run could require nothing more than a push of a button and even starting the run can be automated.

## Automated techniques

The following are notable testing techniques categorized as test automation.

### Continuous testing

Continuous testing is the process of executing automated tests as part of the software delivery pipeline to assess the business risk of releasing the SUT. The scope of testing extends from validating bottom-up requirements or user stories to assessing the system requirements associated with overarching business goals.

### Model-based testing

For model-based testing, the SUT is modeled and test cases can be generated from it to support no code test development. Some tools support the encoding of test cases as plain English that can be used on multiple operating systems, browsers, and smart devices.

### Test-driven development

Test-driven development (TDD) inherently includes the generation of automation test code. Unit test code is written while the SUT code is written. When the code is complete, the tests are complete as well.

### Other

Other test automation techniques include:

- Data-driven testing
- Modularity-driven testing
- Keyword-driven testing
- Behavior driven development

## Considerations

A review of 52 practitioner and 26 academic sources found that five main factors to consider in test automation decision are: system under test (SUT), scope of testing, test toolset, human and organizational topics, cross-cutting factors. The factors most frequently identified were: need for regression testing, economic factors, and maturity of SUT.

While the reusability of automated tests is valued by software development companies, this property can also be viewed as a disadvantage as it leads to a plateau effect, where repeatedly executing the same tests stops detecting errors.

Testing tools can help automate tasks such as product installation, test data creation, GUI interaction, problem detection (consider parsing or polling agents equipped with test oracles), defect logging, etc., without necessarily automating tests in an end-to-end fashion.

Considerations when developing automated tests include:

- Platform and operating system independence
- Data-driven testing
- Reporting (database, Crystal Reports)
- Ease of debugging
- Logging
- Version control
- Extension and customization (e.g., APIs for integrating with other tools)
- Integration with developer tools (e.g., using Ant or Maven for Java development)
- Unattended test runs for integration with build processes and batch runs
- Email notifications (i.e., bounce messages)
- Distributed test execution

## Roles

To support coded automated testing, the test engineer or software quality assurance person must have software coding ability. Some testing techniques such as table-driven and no-code can lessen or alleviate the need for programming skill.

## Framework

A test automation framework provides a programming environment that integrates test logic, test data, and other resources. The framework provides the basis of test automation and simplifies the automation effort. Using a framework can lower the cost of test development and maintenance. If there is change to any test case then only the test case file needs to be updated and the driver script and startup script will remain the same.

A framework is responsible for defining the format in which to express expectations, providing a mechanism to hook into or drive the SUT, executing the tests, and reporting results.

Various types of frameworks are available:

- Linear – procedural code, possibly generated by tools like those that use record and playback
- Structured – uses control structures - typically ‘if-else’, ‘switch’, ‘for’, ‘while’ conditions/ statements
- Data-driven – data is persisted outside of tests in a database, spreadsheet, or other mechanism
- Keyword-driven
- Hybrid – multiple types are used
- Agile automation framework
- Unit testing – some frameworks are intended primarily for unit testing such as xUnit, JUnit and NUnit

## Test automation interface

A test automation interface is a platform that provides a workspace for incorporating multiple testing tools and frameworks for system/integration testing. A test automation interface may simplify the process of mapping tests to business criteria without coding. A test automation interface may improve the efficiency and flexibility of maintaining tests.

A test automation interface consists of the following aspects:

**Interface engine**

Consists of a

parser

and a test runner. The parser is present to parse the object files coming from the object repository into the test specific scripting language. The test runner executes the test scripts using a

test harness

.

**Object repository**

Collection of UI/Application object data recorded by the testing tool while exploring the SUT.
