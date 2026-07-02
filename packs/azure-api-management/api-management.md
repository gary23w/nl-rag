---
title: "API management"
source: https://en.wikipedia.org/wiki/API_management
domain: azure-api-management
license: CC-BY-SA-4.0
tags: azure api management, api gateway azure, api governance azure, developer portal azure
fetched: 2026-07-02
---

# API management

**API management** is the process of creating and publishing web application programming interfaces (APIs), enforcing their usage policies, controlling access, nurturing the subscriber community, collecting and analyzing usage statistics, and reporting on performance. API management components provide mechanisms and tools to support developer and subscriber communities.

## Components

While solutions vary, components that provide the following functions are typically found in API management products:

### Gateway

A server that acts as an API front-end receives API requests, enforces throttling and security policies, passes requests to the back-end service and then passes the response back to the requester. A gateway often includes a transformation engine to orchestrate and modify the requests and responses on the fly. A gateway can also provide functions such as collecting analytics data and providing caching. The gateway can provide the functionality to support authentication, authorization, security, audit and regulatory compliance. Gateways can be implemented using technologies like Nginx or HAProxy.Leading API management platforms such as Google, Kong, MuleSoft, and Boomi have shifted toward multi-vendor API governance, with Boomi now able to discover and govern external gateways, highlighting a move toward unified multi-vendor control.

### Publishing tools

A collection of tools that API providers use to define APIs, for instance using the OpenAPI or RAML specifications, generate API documentation, govern API usage through access and usage policies for APIs, test and debug the execution of API, including security testing and automated generation of tests and test suites, deploy APIs into production, staging, and quality assurance environments, and coordinate the overall API lifecycle.

### Developer portal/API store

A community site, typically branded by an API provider, that can encapsulate for API users in a single convenient source information and functionality including documentation, tutorials, sample code, software development kits, an interactive API console and sandbox to trial APIs, the ability to subscribe to the APIs and manage subscription keys such as OAuth2 Client ID and Client Secret, and obtain support from the API provider and user and community.

### Reporting and analytics

Functionality to monitor API usage and load (overall hits, completed transactions, number of data objects returned, amount of compute time and other internal resources consumed, the volume of data transferred). This can include real-time API monitoring with alerts being raised directly or via a higher-level network management system, for instance, if the load on an API has become too great, as well as functionality to analyze historical data, such as transaction logs, to detect usage trends. Functionality can also be provided to create synthetic transactions that can be used to test the performance and behavior of API endpoints. The API provider can use the information gathered by the reporting and analytics functionality to optimize the API offering within an organization's overall continuous improvement process and define software Service-Level Agreements for APIs.

### Monetization

Functionality to support charging for access to commercial APIs. This functionality can include support for setting up pricing rules based on usage, load and functionality, issuing invoices, and collecting payments, including multiple types of credit card payments.

## Market size

Several industry analysts have observed that the market size for API management solutions has been growing rapidly since the early 2010s. Gartner estimated the market size for API management to be $70 million in 2013, growing at 40% a year. According to Forrester Research, in the US alone, annual spend on API management was $140 million in 2014, expected to grow to $660 million by 2020, with total global sales predicted to exceed a billion dollars by that year. The most recent market analysis, conducted by KBV Research in 2019, predicted a continuing CAGR of 28.4% taking the total market value to $6.2billion by 2024
