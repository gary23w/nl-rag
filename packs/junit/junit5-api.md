---
title: "Overview (JUnit 6.1.1 API)"
source: https://junit.org/junit5/docs/current/api/
domain: junit
license: CC-BY-SA-4.0
tags: junit java, java testing, unit testing, xunit family
fetched: 2026-07-02
---

# JUnit 6.1.1 API

This document consists of four sections:

**Platform**

The JUnit Platform serves as a foundation for launching testing frameworks on the JVM. It also defines the TestEngine API for developing a testing framework that runs on the platform. Furthermore, the platform provides a Console Launcher to launch the platform from the command line and the Suite Engine for running a custom test suite using one or more test engines on the platform

**Jupiter**

JUnit Jupiter is the combination of the programming model and extension model for writing JUnit tests and extensions. The Jupiter subproject provides a TestEngine for running Jupiter based tests on the platform.

**Vintage**

JUnit Vintage provides a TestEngine for running JUnit 3 and JUnit 4 based tests on the platform.

**Other Modules**

This section lists all modules that are not part of a dedicated section.

Already consulted the JUnit User Guide?

Module

Description

org.junit.jupiter

Aggregates all JUnit Jupiter modules.

org.junit.jupiter.api

Defines the JUnit Jupiter API for writing tests.

org.junit.jupiter.engine

Provides the JUnit Jupiter

TestEngine

implementation.

org.junit.jupiter.migrationsupport

Support for migrating from JUnit 4 to JUnit Jupiter.

org.junit.jupiter.params

JUnit Jupiter extension for parameterized tests.

org.junit.platform.commons

Common APIs and support utilities for the JUnit Platform.

org.junit.platform.console

Support for launching the JUnit Platform from the console.

org.junit.platform.engine

Public API for test engines.

org.junit.platform.launcher

Public API for configuring and launching test plans.

org.junit.platform.reporting

Defines the JUnit Platform Reporting API.

org.junit.platform.suite

Aggregates all JUnit Platform Suite modules.

org.junit.platform.suite.api

Annotations for configuring a test suite on the JUnit Platform.

org.junit.platform.suite.engine

Provides a

TestEngine

for running declarative test suites.

org.junit.platform.testkit

Defines the Test Kit API for the JUnit Platform.

org.junit.start

Defines the API of the JUnit Start module for writing and running tests.

org.junit.vintage.engine

Provides a

TestEngine

for running JUnit 3 and 4 based tests on the platform.
