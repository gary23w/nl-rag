---
title: "OpenAPI Specification"
source: https://en.wikipedia.org/wiki/OpenAPI_Specification
domain: loopback-node
license: CC-BY-SA-4.0
tags: loopback node framework, ibm loopback api, node.js api framework, loopback model driven
fetched: 2026-07-02
---

# OpenAPI Specification

The **OpenAPI Specification** (**OAS**), previously known as the **Swagger Specification**, is a specification for a machine-readable interface definition language for describing, producing, consuming and visualizing web services. Originally developed to support the Swagger framework, it became a separate project in 2015, overseen by the OpenAPI Initiative, an open-source collaboration project of the Linux Foundation.

An OpenAPI Description (OAD) represents a formal description of an API that tools can use to generate code, documentation, test cases, and more.

## History

Swagger development began in early 2010 by Tony Tam, who was working at online dictionary company Wordnik.

In March 2015, SmartBear Software acquired the open-source Swagger API specification from Reverb Technologies, Wordnik's parent company.

In November 2015, SmartBear announced that it was donating the Swagger specification to a new organization called the OpenAPI Initiative, under the sponsorship of the Linux Foundation. Other founding member companies included 3scale, Apigee, Capital One, Google, IBM, Intuit, Microsoft, PayPal, and Restlet.

On 1 January 2016, the Swagger specification was renamed the OpenAPI Specification (OAS) and was moved to a new GitHub repository.

### Consolidation of Formats

Two somewhat similar technologies, MuleSoft's RESTful API Modeling Language (RAML) and Apiary's API Blueprint, had been developed around the same time as what was then still called the Swagger Specification.

The producers of both formats later joined the OpenAPI Initiative: Apiary in 2016 and MuleSoft in 2017. Both have added support for the OAS.

### Version History

In July 2017, the OpenAPI Initiative released version 3.0.0 of its specification.

In February 2021, the OpenAPI Initiative released version 3.1.0. Major changes in OpenAPI Specification 3.1.0 include JSON schema vocabularies alignment, new top-level elements for describing webhooks that are registered and managed out of band, support for identifying API licenses using the standard SPDX identifier, allowance of descriptions alongside the use of schema references and a change to make the PathItems object optional to simplify creation of reusable libraries of components.

In September 2025, the OpenAPI Initiative released version 3.2.0 of the OAS. Notable features include structured tags, first-class streaming media type support, support for arbitrary HTTP methods, clearer example semantics for serializations, OAuth2 device flow and metadata enhancements, and clarified path templating and routing semantics.

#### Release dates

| Version | Date | Notes |
|---|---|---|
| 3.2.0 | 2025-09-19 | Release of the OpenAPI Specification 3.2.0 |
| 3.1.2 | 2025-09-19 | Patch release of the OpenAPI Specification 3.1.2 |
| 3.1.1 | 2024-10-24 | Patch release of the OpenAPI Specification 3.1.1 |
| 3.1.0 | 2021-02-15 | Release of the OpenAPI Specification 3.1.0 |
| 3.0.4 | 2024-10-24 | Patch release of the OpenAPI Specification 3.0.4 |
| 3.0.3 | 2020-02-20 | Patch release of the OpenAPI Specification 3.0.3 |
| 3.0.2 | 2018-10-08 | Patch release of the OpenAPI Specification 3.0.2 |
| 3.0.1 | 2017-12-06 | Patch release of the OpenAPI Specification 3.0.1 |
| 3.0.0 | 2017-07-26 | Release of the OpenAPI Specification 3.0.0 |
| 2.0 | 2014-09-08 | Release of Swagger 2.0 |
| 1.2 | 2014-03-14 | Initial release of the formal document |
| 1.1 | 2012-08-22 | Release of Swagger 1.1 |
| 1.0 | 2011-08-10 | First release of the Swagger Specification |

## Usage

The OAS describes the format for OpenAPI Descriptions (OADs), which can be used by a variety of applications, libraries, and tools.

Applications can use OADs to automatically generate documentation of methods, parameters and data models. This helps keep the documentation, client libraries and source code in sync.

When an OAD is used to generate source code stubs for servers, the process is called scaffolding.

### Relationships to software engineering practices

The paradigm of agreeing on an API contract first and then programming business logic afterwards, in contrast to coding the program first and then writing a retrospective description of its behavior as the contract, is called contract-first development. Since the interface is determined before any code is written, downstream developers can mock the server behavior and start testing right away. In this sense, contract-first development is also a practice of shift-left testing.

## Features

The OpenAPI Specification is language-agnostic. With OpenAPI's declarative resource specification, clients can understand and consume services without knowledge of server implementation or access to the server code.

## Conferences and conference tracks

The OpenAPI Initiative sponsored APIStrat from 2017 to 2019, converting it into the API Specifications Confererence (ASC) from 2020 to 2022. Starting in 2023, the initiative has instead sponsored OpenAPI tracks at multiple conferences throughout the year.
