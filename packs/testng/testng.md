---
title: "TestNG"
source: https://en.wikipedia.org/wiki/TestNG
domain: testng
license: CC-BY-SA-4.0
tags: testng java, java testing, test automation, unit testing
fetched: 2026-07-02
---

# TestNG

**TestNG** is a testing framework for the Java programming language created by Cédric Beust and inspired by JUnit and NUnit. The design goal of TestNG is to cover a wider range of test categories: unit, functional, end-to-end, integration, etc., with more powerful and easy-to-use functionalities.

## Features

TestNG's main features include:

1. Annotation support.
2. Support for data-driven/parameterized testing (with `@DataProvider` and/or XML configuration).
3. Support for multiple instances of the same test class (with `@Factory`)
4. Flexible execution model. TestNG can be run either by Ant via build.xml (with or without a test suite defined), or by an IDE plugin with visual results. There isn't a `TestSuite` class, while test suites, groups and tests selected to run are defined and configured by XML files.
5. Concurrent testing: run tests in arbitrarily big thread pools with various policies available (all methods in their own thread, one thread per test class, etc.), and test whether the code is multithread safe.
6. Embeds BeanShell for further flexibility.
7. Default JDK functions for runtime and logging (no dependencies).
8. Dependent methods for application server testing.
9. Distributed testing: allows distribution of tests on slave machines.

### Data provider

A data provider in TestNG is a method in a test class, which provides an array of varied actual values to dependent test methods.

Example:

```mw
	//This method will provide data to any test method that declares that its Data Provider is named "provider1". 
	@DataProvider(name = "provider1")
	public Object[][] createData1() {
		return new Object[][] { 
			{ "Cedric", new Integer(36) },
			{ "Anne", new Integer(37) }
		};
	}

	// This test method declares that its data should be supplied by the Data Provider named "provider1".
	@Test(dataProvider = "provider1")
	public void verifyData1(String n1, Integer n2) {
		System.out.println(n1 + " " + n2);
	}

	// A data provider which returns an iterator of parameter arrays.
	@DataProvider(name = "provider2")
	public Iterator<Object[]> createData() {
		return new MyIterator(...);
	}	

	// A data provider with an argument of the type java.lang.reflect.Method.
	// It is particularly useful when several test methods use the same 
	// provider and you want it to return different values depending on 
	// which test method it is serving. 
	@DataProvider(name = "provider3")
	public Object[][] createData(Method m) {
		System.out.println(m.getName()); 
		return new Object[][] { new Object[] { "Cedric" } };
	}
```

The returned type of a data provider can be one of the following two types:

- An array of array of objects (`Object[][]`) where the first dimension's size is the number of times the test method will be invoked and the second dimension size contains an array of objects that must be compatible with the parameter types of the test method.
- An `Iterator<Object[]>`. The only difference with `Object[][]` is that an Iterator lets you create your test data lazily. TestNG will invoke the iterator and then the test method with the parameters returned by this iterator one by one. This is particularly useful if you have a lot of parameter sets to pass to the method and you don't want to create all of them upfront.

### Tool support

TestNG is supported, out-of-the-box or via plug-ins, by each of the three major Java IDEs - Eclipse, IntelliJ IDEA, and NetBeans. It also comes with a custom task for Apache Ant and is supported by the Maven build system. The Hudson continuous integration server has built-in support for TestNG and is able to track and chart test results over time. Most Java code coverage tools, such as Cobertura, work seamlessly with TestNG.

Note: TestNG support for Eclipse is only embedded in the Eclipse Marketplace for Eclipse versions up to 2018-09 (4.9). For later versions of Eclipse, TestNG must be manually installed as per instructions in the TestNG site.

### Reporting

TestNG generates test reports in HTML and XML formats. The XML output can be transformed by the Ant JUnitReport task to generate reports similar to those obtained when using JUnit. Since version 4.6, TestNG also provides a reporter API that permits third-party report generators, such as ReportNG, PDFngreport and TestNG-XSLT, to be used.

## Comparison with JUnit

TestNG has a longstanding rivalry with the JUnit test automation framework. Each of them has differences and respective advantages. Stack Overflow discussions reflect this controversy.

### Annotations

In JUnit 5, the @BeforeAll and @AfterAll methods have to be declared as static in most circumstances. TestNG does not have this constraint.

TestNG includes four additional setup/teardown annotation pairs for the test suite and groups: @BeforeSuite, @AfterSuite, @BeforeTest, @AfterTest, @BeforeGroup and @AfterGroup, @BeforeMethod and @AfterMethod. TestNG also provides support to automate testing an application using selenium.

### Parameterized testing

Parameterized testing is implemented in both tools, but in quite different ways.

TestNG has two ways for providing varying parameter values to a test method: by setting the *testng.xml*, and by defining a *@DataProvider* method.

In JUnit 5, the *@ParameterizedTest* annotation allows parameterized testing. This annotation is combined with another annotation declaring the source of parameterized arguments, such as *@ValueSource* or *@EnumSource*. Using *@ArgumentsSource* allows the user to implement a more dynamic `ArgumentsProvider`. In JUnit 4, *@RunWith* and *@Parameters* are used to facilitate parameterized tests, where the *@Parameters* method has to return a `List[]` with the parameterized values, which will be fed into the test class constructor.

### Conclusion

Different users often prefer certain features of one framework or another. JUnit is more widely popular and often shipped with mainstream IDEs by default. TestNG is noted for extra configuration options and capability for different kinds of testing. Which one more suitable depends on the use context and requirements.
