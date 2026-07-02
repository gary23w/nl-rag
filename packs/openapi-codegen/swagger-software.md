---
title: "Swagger (software)"
source: https://en.wikipedia.org/wiki/Swagger_(software)
domain: openapi-codegen
license: CC-BY-SA-4.0
tags: openapi codegen, openapi specification, api client generation, swagger code generation
fetched: 2026-07-02
---

# Swagger (software)

**Swagger** is a suite of tools for API developers from SmartBear Software and a former specification upon which the OpenAPI Specification is based.

## History

The Swagger API project was created in 2011 by Tony Tam, technical co-founder of the dictionary site Wordnik. During the development of Wordnik's products, the need for automation of API documentation and client SDK generation became a major source of frustration. Tam designed a simple JSON representation of the API, building upon the flexibility of the HTTP protocol and using many features of tooling built for the SOAP protocol. The concept for the user interface was proposed by Ayush Gupta, who suggested that an interactive user interface would benefit end users who wished to "try out" and develop against the API. Ramesh Pidikiti led implementation of the initial code generator and designer/developer Zeke Sikelianos coined the name Swagger. The Swagger API project was made open source in September 2011. Soon after release, a number of new components were added to the project, including a stand-alone validator and support for Node.js and Ruby on Rails.

In Swagger's early years, modest traction came from small companies and independent developers. HTTP APIs typically did not have a machine-readable description mechanism, and Swagger provided a simple and discoverable way to do so. Tony was invited to a meeting with some of the API industry's thought leaders including John Musser (ProgrammableWeb), Marsh Gardiner (Apigee, now a Google product), Marco Palladino (Kong), and Kin Lane (API Evangelist) to discuss a standardization effort around API descriptions. While the meeting did not yield a concrete plan to do so, it put Swagger on the map as a critical innovation in the API space.

Helped by the use of the Apache 2.0 open-source license, a number of products and online services began including Swagger in their offerings, which accelerated quickly after adoption by Apigee, Intuit, Microsoft, IBM and others who began to publicly endorse the Swagger project.

Shortly after Swagger was created, alternative structures for describing HTTP APIs were introduced, the most popular being API Blueprint in April 2013 and RESTful API Modeling Language (RAML) in September 2013. While these competing products had stronger financial backing than Swagger, they initially focused on different use cases from Swagger, and as of mid-2014, Swagger interest was growing more quickly than the combination of the two others [source: Google Trends].

In November 2015, SmartBear Software, the company that maintained Swagger, announced that it was helping create a new organization, under the sponsorship of the Linux Foundation, called the OpenAPI Initiative. A variety of companies, including Google, IBM, and Microsoft are founding members.

On 1 January 2016, the Swagger specification was renamed to OpenAPI Specification, and was moved to a new software repository on GitHub. While the specification itself was not changed, this renaming signified the split between the API description format and the open-source tooling.

As of July 2017, Swagger tools were downloaded over 100,000 times per day, according to hosting repositories Sonatype and npm.

## Usage

Swagger's open-source tooling usage can be broken up into different use cases: development, interaction with APIs, and documentation.

### Developing APIs

When creating APIs, Swagger tooling may be used to automatically generate an Open API document based on the code itself. This embeds the API description in the source code of a project and is informally called code-first or bottom-up API development.

Alternatively, using Swagger Codegen, developers can decouple the source code from the Open API document, and generate client and server code directly from the design. This makes it possible to defer the coding aspect.

### Interacting with APIs

Using the Swagger Codegen project, end users generate client SDKs directly from the OpenAPI document, reducing the need for human-generated client code. As of August 2017, the Swagger Codegen project supported over 50 different languages and formats for client SDK generation.

### Documenting APIs

When described by an OpenAPI document, Swagger open-source tooling may be used to interact directly with the API through the Swagger UI. This project allows connections directly to live APIs through an interactive, HTML-based user interface. Requests can be made directly from the UI and the options explored by the user of the interface.
