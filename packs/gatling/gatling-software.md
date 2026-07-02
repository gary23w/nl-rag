---
title: "Gatling (software)"
source: https://en.wikipedia.org/wiki/Gatling_(software)
domain: gatling
license: CC-BY-SA-4.0
tags: gatling scala, load testing, performance testing, simulation scripts
fetched: 2026-07-02
---

# Gatling (software)

**Gatling** is a load and performance testing framework based on Scala and Netty. The first stable release was published on January 13, 2012. In 2015, Gatling's founder, Stéphane Landelle, created a company (named "Gatling Corp"), dedicated to the development of the open-source project. According to Gatling Corp's official website, Gatling was downloaded more than 20,000,000 times (2024). In June 2016, Gatling officially presented Gatling Enterprise the commercial version which included test orchestration and team collaboration features.

The software is designed to be used as a load testing tool for analyzing and measuring the performance of a variety of services, with a focus on web applications, application programming interfaces (APIs), and microservices.

Gatling was mentioned twice in ThoughtWorks Technology Radar, in 2013 and 2014, "as a tool worth trying", with an emphasis on "the interesting premise of *treating your performance tests as production code*".

The latest minor release is Gatling 3.14, published on May 12, 2025.

## Company History

Gatling started as an open-source project in 2012 by Stéphane Landelle, while he was the chief technology officer (CTO) of a French IT consulting firm, eBusiness Information. In 2015 a dedicated company named "Gatling Corp" to develop a commercial product for load test orchestration and collaboration. The first version of Gatling Enterprise (originally named FrontLine) was released in 2016.

The company is based in Bagneux, France, near Paris.

Gatling Corp is a member of Systematic Paris-Region, an Île-de-France business cluster created in 2005, devoted to complex systems and ICT. Systematic Paris-Region gathers large groups, SMEs, universities and research labs to promote digital innovation. Gatling is a member of Systematic's Open Source Working Group and was elected member of Systematic's board of directors, as a representative of SMEs, in November 2016.

The company took part in some events, like the Paris Open Source Summit (POSS, 2015, 2016 and 2017 editions), Liferay's 2016 Symposium, Java User Group (JUG)'s meetings, the Paris Gatling User Group and the New York Gatling User Group.

## Overview of the Project

Gatling consists of an open-source core and an enterprise orchestration and collaboration platform. The open-source performance testing tool includes:

- The high-performance load generator engine
- SDKs in multiple programming languages for Java, Scala, Kotlin, JavaScript, and TypeScript.
- Static HTML reports

Gatling Enterprise includes all of the open-source features and additionally:

- Real-time and interactive reporting
- Customized reports and sharing options
- Multiple load generator options, from fully managed to self-hosted
- Full CI/CD integration
- RBAC and SSO
- AI features and tooling

## Terminology

- **Simulation:** The simulation file includes the different *scenarios* of a test, its parametrization and the *injection profiles*. Technically speaking, a simulation is a Scala class. Here are examples of simulations in Java and JavaScript:

```mw
//Java

public class BasicSimulation extends Simulation {

  HttpProtocolBuilder httpProtocol =
    http.baseUrl("https://e-comm.gatling.io")
      .acceptHeader("application/json")
      .contentTypeHeader("application/json");

  ScenarioBuilder myFirstScenario = scenario("My First Scenario")
    .exec(http("Request 1")
      .get("/session/"));

  {
    setUp(
      myFirstScenario.injectOpen(constantUsersPerSec(2).during(60))
    ).protocols(httpProtocol);
  }
}
```

```mw
//JavaScript

export default simulation((setUp) => {

  const httpProtocol =
    http.baseUrl("https://e-comm.gatling.io")
      .acceptHeader("application/json")
      .contentTypeHeader("application/json");

  const myScenario = scenario("My Scenario")
    .exec(http("Request 1")
      .get("/session/"));

  setUp(
    myScenario.injectOpen(constantUsersPerSec(2).during(60))
  ).protocols(httpProtocol);
});
```

- **Scenario:** A scenario consists of a series of *requests*. Each scenario within a *simulation* can have its own *injection profile*. Here is an example of a scenario:

```mw
//Java

ScenarioBuilder myFirstScenario = scenario("My First Scenario")
    .exec(http("Request 1")
      .get("/session/"));

  {
    setUp(
      myFirstScenario.injectOpen(constantUsersPerSec(2).during(60))
    ).protocols(httpProtocol);
  }
```

```mw
//JavaScript

const myScenario = scenario("My Scenario")
    .exec(http("Request 1")
      .get("/session/"));

  setUp(
    myScenario.injectOpen(constantUsersPerSec(2).during(60))
  ).protocols(httpProtocol);
});
```

- **Group:** Groups can be used as a subdivision of a *scenario*. It is also a series of *requests*, that has a functional purpose (for instance, the login process).
- **Request:** Gatling is able to simulate complex users' behaviors. For this purpose, it generates the appropriate requests in the system under test. Here is an example of a request in Gatling:

```mw
//Java

.exec(http("Request 1")
    .get("/session/"));
```

```mw
//JavaScript
.exec(http("Request 1")
      .get("/session/"));
```

- **Injection profile:** An injection profile is the number of virtual users injected during the test in the system under test and how they are injected. Here is an example of an injection profile:

```mw
//Java

    setUp(
      myFirstScenario.injectOpen(constantUsersPerSec(2).during(60))
    ).protocols(httpProtocol);
```

```mw
//JavaScript
setUp(
    myScenario.injectOpen(constantUsersPerSec(2).during(60))
  ).protocols(httpProtocol);
```

## Architecture

Gatling implemented a fully new architecture for a performance testing tool, in order to be more resource efficient. It makes it possible to simulate a high number of requests per second with a single machine.

## Components

### Recorder

Gatling comes with an HTTP web recorder to bootstrap a simulation. The HTTP recorder can be used to directly capture browser actions or convert .har files to load test scenarios.

### Gatling Studio

Gatling Studio is a desktop tool that records browser sessions and converts them into Gatling load test scripts. It captures HTTP interactions — including headers, payloads, and timing — from a live browser session or an imported HAR file, filters out static and third-party requests, and generates Java (Maven) code representing the recorded user flow. The exported project can be run locally with Gatling Community Edition or deployed through Gatling Enterprise Edition.

### Domain-specific language

Gatling is provided with a simple and lightweight Domain-specific language, in which simulations and scenarios are coded. This allows users to add custom behavior through many hooks. This makes simulation scripts readable and easy to maintain.

In 2024 Gatling introduced a new DSL (SDK) for JavaScript and TypeScript. The JavaScript and TypeScript SDK uses GraalVM to translate JavaScript code to Java and execute load tests on a Java virtual machine (JVM). Adding JavaScript and TypeScript support made Gatling the first polyglot load testing tool in the market.

This is an example of what Gatling's domain-specific language looks like (see also § Terminology):

```mw
val scn = scenario("BasicSimulation")
  .exec(http("request_1")
  .get("/"))
  .pause(5)
```

### Reports

At the end of each test, Gatling generates a static HTML report. Reports include:

- Active users over time
- Response time distribution
- Response time percentiles over time
- Requests per second over time
- Responses per second over time

Gatling Enterprise additionally includes:

- Real-time results
- Advanced response metrics
- Load generator health metrics
- Run trends and comparison tools

### AI Insights

Gatling incorporates several AI-assisted features. An IDE plugin can generate test simulations from natural language prompts and convert scripts from tools such as JMeter and LoadRunner. The platform can produce plain-language summaries of completed test runs, highlighting anomalies and regressions. A Model Context Protocol (MCP) server allows compatible AI coding agents to configure and launch tests from within a development environment. The platform also supports protocols associated with large language model (LLM) workloads, including Server-Sent Events (SSE) and WebSockets.

## Protocols support and plugins

It officially supports the following protocols:

- HTTP
- WebSockets
- Server-sent events
- JMS
- MQTT
- gRPC

Gatling documentation states that it is protocol agnostic, which makes it possible to implement other protocols' support.

## Plugins

Gatling comes out with official and community plugins. It integrates with:

- Integrated development environments (IDE), like Eclipse and IntelliJ IDEA
- Build automation software, or Build tools, like Apache Maven, Gradle, Npm and sbt
- Continuous Integration solutions like Jenkins, GitHub Actions, GitLab, TeamCity, and Bamboo

### Community plugins

Here is a non-exhaustive list of plugins created by community members:

- Apache Kafka
- Java Database Connectivity (JDBC)
- Apache Cassandra
- RabbitMQ
- SQL
- Advanced Message Queuing Protocol (AMQP)
- ZeroMQ

## Continuous integration

Automation with Gatling is related to its simulations' maintainability. The integration with other developer tools, especially in the DevOps lifecycle, makes it possible to create performance tests at scale, that is to say to fully automate the execution of performance testing campaigns in the software development process.

## Major and minor releases

| Version | Release date |
|---|---|
| 3.15 | 27 February 2026 |
| 3.14 | 12 May 2025 |
| 3.13 | 13 November 2024 |
| 3.12 | 9 September 2024 |
| 3.11.1 | 25 April 2024 |
| 3.10.3 | 21 December 2023 |
| 3.9.5 | 10 May 2023 |
| 3.0.0 | 23 October 2018 |
| 2.3.0 | 30 August 2017 |
| 2.2.0 | 15 April 2016 |
| 2.1.0 | 15 December 2014 |
| 2.0.0 | 6 October 2014 |
| 1.5.0 | 6 May 2013 |
| 1.4.0 | 20 December 2012 |
| 1.3.0 | 19 September 2012 |
| 1.2.0 | 31 May 2012 |
| 1.1.0 | 26 March 2012 |
| 1.0.0 | 13 January 2012 |

## Licensing

Gatling is published under Apache License 2.0, a permissive free software license written by the Apache Software Foundation (ASF).

The source code is accessible on GitHub.

## Gatling Enterprise

Gatling Enterprise is the commercial version of Gatling. It is proprietary software, distributed by Gatling Corp.
