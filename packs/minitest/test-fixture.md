---
title: "Test fixture"
source: https://en.wikipedia.org/wiki/Test_fixture
domain: minitest
license: CC-BY-SA-4.0
tags: minitest ruby, ruby testing, unit testing, test framework
fetched: 2026-07-02
---

# Test fixture

A **test fixture** is a device used to consistently test some item, device, or piece of software. Test fixtures are used in the testing of electronics, software and physical devices.

## Electronics

In testing electronic equipment such as circuit boards, electronic components, and chips, a test fixture is a device or setup designed to hold the device under test in place and allow it to be tested by being subjected to controlled electronic test signals. Examples are a bed of nails tester or smart fixture.

Test fixtures can come in different shapes, sizes, and functions. There are several different types of test fixtures, including In-Circuit Test Fixtures, Functional Test Fixtures, and Wireless Test Fixtures. In Circuit Test (ICT) fixtures individually test each component on a PCB, while functional test fixtures assess the entire board's functionality. Functional test fixtures simulate real-world conditions, whereas ICT is more focused on detecting assembly defects like short circuits or missing components. An In-Circuit Test fixture can come in both Inline and Standard variations. An Inline Test Fixture is designed for fast, automated testing directly within a production line, ideal for high-volume manufacturing where continuous testing maximises efficiency. A Standard Test Fixture, on the other hand, usually requires manual loading, making it well-suited to smaller-scale or specialised testing.

- (Side connectors, centering pins, test needles, pre-centering parts.) Side connectors, centering pins, test needles, pre-centering parts.
- (A functional test fixture is a complex device to interface the device under test (DUT) to the automatic test equipment (ATE).) A functional test fixture is a complex device to interface the device under test (DUT) to the automatic test equipment (ATE).

## Software

In the context of software, a test fixture (also called "test context") is used to set up the system state and input data needed for test execution. For example, the Ruby on Rails web framework uses YAML to initialize a database with known parameters before running a test. This allows for tests to be repeatable, which is one of the key features of an effective test framework. In most cases, a custom test fixture will normally require custom test software. This software is created in order to ensure optimal testing performance and seamless integration. The custom software can be configured to carry out a number of different tests from BIST (Built-In Self Test) to advanced JTAG Implementation.

### Setup

Test fixtures can be set up three different ways: in-line, delegate, and implicit.

1. In-line setup creates the test fixture in the same method as the rest of the test. While in-line setup is the simplest test fixture to create, it leads to duplication when multiple tests require the same initial data.
2. Delegate setup places the test fixture in a separate standalone helper method that is accessed by multiple test methods.
3. Implicit setup places the test fixture in a setup method which is used to set up multiple test methods. This differs from delegate setup in that the overall setup of multiple tests is in a single setup method where the test fixture gets created rather than each test method having its own setup procedures and linking to an external test fixture.

### Advantages and disadvantages

The main advantage of a test fixture is that it allows for tests to be repeatable since each test is always starting with the same setup. Test fixtures also ease test code design by allowing the developer to separate methods into different functions and reuse each function for other tests. Further, test fixtures preconfigure tests into a known initial state instead of working with whatever was left from a previous test run.

A disadvantage is that it could lead to duplication of test fixtures if using in-line setup.

### Practices to avoid

It is considered bad practice when implicit test fixtures are too general, or when a test method sets up a test fixture and does not use it during the test. A more subtle issue is if the test methods ignore certain fields within the test fixture. Another bad practice is a test setup that contains more steps than needed for the test; this is a problem seen in in-line setup.

A test case is considered "unsafe" when it modifies its fixture(s). An unsafe test case can render subsequent tests useless by leaving the fixture in an unexpected state. It also causes the order of tests to be important: a modified fixture must be reset if more tests are to be run after an unsafe test.

### Examples

Examples of fixtures include loading a database with a specific known set of data, erasing a hard disk and installing a known clean operating system installation, copying a specific known set of files, or the preparation of input data as well as set-up and creation of mock objects.

Software which is used to run reproducible tests systematically on a piece of software under test is known as a test harness; part of its job is to set up suitable test fixtures.

In generic xUnit, a *test fixture* is all the things that must be in place in order to run a test and expect a particular outcome.

Frequently fixtures are created by handling *setUp()* and *tearDown()* events of the unit testing framework. In *setUp()* one would create the expected state for the test and in *tearDown()* it would clean up what had been set up.

Four phases of a test:

1. Set-up
2. Exercise, interacting with the system under test
3. Verify, determining whether the expected outcome has been obtained
4. Tear down, to return to the original state

## Physical testing

In physical testing, a fixture is a device or apparatus to hold or support the test specimen during the test. The influence of test fixtures on test results is important and is an ongoing subject of research.

Many test methods detail the requirements of test fixtures in the text of the document.

- (Test fixture on universal testing machine for three-point flex test) Test fixture on universal testing machine for three-point flex test
- (Hydraulic system testing on fixture) Hydraulic system testing on fixture
- (jet engine fixtures for operational testing) jet engine fixtures for operational testing

Some fixtures employ clamps, wedge grips and pincer grips.

- (pincer clamps max. 50 kN spring-biased) pincer clamps max. 50 kN spring-biased
- (offset compensated wedge grip max.50 kN) offset compensated wedge grip max.50 kN
- (different vice and screw grips of a German manufacturer) different vice and screw grips of a German manufacturer
- (ASTM-D5034 Textile vice grip of a specialized manufacturer) ASTM-D5034 Textile vice grip of a specialized manufacturer

Further types of construction include eccentric roller fixtures, thread grips and button head grips and rope grips.

- (symmetric roller grip, self-closing and self-adjusting) symmetric roller grip, self-closing and self-adjusting
- (multiple button head grip for speedy tests on series) multiple button head grip for speedy tests on series
- (small rope grip 200N to test fine wires) small rope grip 200N to test fine wires
- (very compact wedge grip for temperature chambers providing extreme temperatures) very compact wedge grip for temperature chambers providing extreme temperatures

Mechanical holding apparatuses provide the clamping force via arms, wedges or eccentric wheel to the jaws. Additionally there are pneumatic and hydraulic fixtures for tensile testing that allow very fast clamping procedures and very high clamping forces.

- (pneumatic grip, symmetrical, clamping force 2.4 kN) pneumatic grip, symmetrical, clamping force 2.4 kN
- (heavy duty hydraulic clamps, clamping force 700 kN) heavy duty hydraulic clamps, clamping force 700 kN
- (Bending device for tensile testing machines) Bending device for tensile testing machines
- (Equipment to test peeling forces up to 10 kN) Equipment to test peeling forces up to 10 kN
