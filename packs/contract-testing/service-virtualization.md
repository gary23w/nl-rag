---
title: "Service virtualization"
source: https://en.wikipedia.org/wiki/Service_virtualization
domain: contract-testing
license: CC-BY-SA-4.0
tags: contract testing, consumer-driven contracts, service virtualization, api testing
fetched: 2026-07-02
---

# Service virtualization

In software engineering, **service virtualization** or **service virtualisation** is a method to emulate the behavior of specific components in heterogeneous component-based applications such as API-driven applications, cloud-based applications and service-oriented architectures. It is used to provide software development and QA/testing teams access to dependent system components that are needed to exercise an application under test (AUT), but are unavailable or difficult-to-access for development and testing purposes. With the behavior of the dependent components "virtualized", testing and development can proceed without accessing the actual live components. Service virtualization is recognized by vendors, industry analysts, and industry publications as being different than mocking. See here for a Comparison of API simulation tools.

## Overview

Service virtualization emulates the behavior of software components to remove dependency constraints on development and testing teams. Such constraints occur in complex, interdependent environments when a component connected to the application under test is:

- Not yet completed
- Still evolving
- Controlled by a third-party or partner
- Available for testing only in limited capacity or at inconvenient times
- Difficult to provision or configure in a test environment
- Needed for simultaneous access by different teams with varied test data setup and other requirements
- Restricted or costly to use for load and performance testing

Although the term "service virtualization" reflects the technique's initial focus on virtualizing web services, service virtualization extends across all aspects of composite applications: services, databases, mainframes, ESBs, and other components that communicate using common messaging protocols. Other similar tools are called API simulators, API mocking tools, over the wire test doubles.

Service virtualization emulates only the behavior of the specific dependent components that developers or testers need to exercise in order to complete their end-to-end transactions. Rather than virtualizing entire systems, it virtualizes only specific slices of dependent behavior critical to the execution of development and testing tasks. This provides just enough application logic so that the developers or testers get what they need without having to wait for the actual service to be completed and readily available. For instance, instead of virtualizing an entire database (and performing all associated test data management as well as setting up the database for every test session), you monitor how the application interacts with the database, then you emulate the related database behavior (the SQL queries that are passed to the database, the corresponding result sets that are returned, and so forth).

## Application

Service virtualization involves creating and deploying a "virtual asset" that simulates the behavior of a real component which is required to exercise the application under test, but is difficult or impossible to access for development and testing purposes.

A virtual asset stands in for a dependent component by listening for requests and returning an appropriate response—with the appropriate performance. For a database, this might involve listening for a SQL statement, then returning data source rows. For a web service, this might involve listening for an XML message over HTTP, JMS, or MQ, then returning another XML message. The virtual asset's functionality and performance might reflect the actual functionality/performance of the dependent component, or it might simulate exceptional conditions (such as extreme loads or error conditions) to determine how the application under test responds under those circumstances.

Virtual assets are typically created by:

- Recording live communication among components as the system is exercised from the application under test (AUT)
- Providing logs representing historical communication among components
- Analyzing service interface specifications (such as a WSDL)
- Defining the behavior manually with various interface controls and data source values

They are then further configured to represent specific data, functionality, and response times.

Virtual assets are deployed locally or in the cloud (public or private). With development/test environments configured to use the virtual assets in place of dependent components, developers or testers can then exercise the application they are working on without having to wait for the dependent components to be completed or readily accessible.

Industry analysts report that service virtualization is best suited for "IT shops with significant experience with 'skipping' integration testing due to 'dependent software', and with a reasonably sophisticated test harness.

## Relation to stubbing and mocking

An alternative approach to working around the test environment access constraints outlined in this article's introduction is for team members to develop method stubs or mock objects that substitute for dependent resources. The shortcoming of this approach became apparent in the early 2000s with the rise of Service-oriented architecture. The proliferation of Composite applications that rely on numerous dependent services, plus the rise of Agile software development following the 2001 publication of the Agile Manifesto, made it increasingly difficult for developers or testers to manually develop the number, scope, and complexity of stubs or mocks required to complete development and testing tasks for modern enterprise application development.

The first step in the evolution from stubbing to service virtualization was the technology packaged in SOA testing tools since 2002. The earliest implementations of service virtualization were designed to automate the process of developing simple stub-like emulations so that composite applications could be tested more efficiently. As enterprise systems continued to grow increasingly complex and distributed, software tool vendors shifted focus from stubbing to the more environment-focused service virtualization. While stubbing can still be completed through manual development and management of stubs, what has become known as "service virtualization" is completed by using one of the available commercial off the shelf (COTS) service virtualization technologies as a platform for the development and deployment of their "service virtualization assets".

## Agile and DevOps

The increasing popularity of Agile software development and DevOps has created demand for a new set of tools to deliver service virtualization to communities that work in this way. Practices such as Continuous delivery and moving away from mainframe and monolith development to more distributed microservice-based architectures fit well with the capabilities of service virtualization. Agile and DevOps teams prefer to work with lightweight tools that have less accumulated bloat and no cumbersome licensing restrictions.
