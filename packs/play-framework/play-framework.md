---
title: "Play Framework"
source: https://en.wikipedia.org/wiki/Play_Framework
domain: play-framework
license: CC-BY-SA-4.0
tags: play framework, scala web, reactive web framework, akka backend
fetched: 2026-07-02
---

# Play Framework

**Play Framework** is an open-source web application framework which follows the model–view–controller (MVC) architectural pattern. It is written in Scala and usable from other programming languages that are compiled to JVM bytecode, e.g. Java. It aims to optimize developer productivity by using convention over configuration, hot code reloading and display of errors in the browser.

Support for the Scala programming language has been available since version 1.1 of the framework. In version 2.0, the framework core was rewritten in Scala. Build and deployment was migrated to SBT, and templates use Scala instead of Apache Groovy.

## History

Play was created by software developer Guillaume Bort, while working at Zengularity SA (formerly Zenexity). Although the early releases are no longer available online, there is evidence of Play existing as far back as May 2007. In 2007, pre-release versions of the project were available to download from Zenexity's website.

| Version | Date | Notes |
|---|---|---|
| Unsupported: 1.0 | May 2008 | The first published code for 1.0 appeared on Launchpad. This was followed by a full 1.0 release in October 2009. |
| Unsupported: 1.1 | November 2010 | Released after a move from Launchpad to GitHub. It included a migration from Apache MINA to JBoss Netty, Scala support, native GlassFish container, an asynchronous web services library, OAuth support, HTTPS support and other features. |
| Unsupported: 1.2 | April 2011 | It included dependency management with Apache Ivy, support for WebSocket, integrated database migration (reversion was not implemented), a switch to the H2 database as the default development database and other features. |
| Unsupported: 1.3 | January 15, 2015 | libraries upgraded (a.o. netty, hibernate, etc.), added multiple databases support and included customisable template name resolving. |
| Unsupported: 1.4 | October 30, 2015 | Compatible to Java 7 and removed support for Java 6. Added ability to define enabled ssl protocols. |
| Unsupported: 1.5 | September 29, 2017 | Upgraded to Hibernate 5.x. Dropped support for java version prior to 1.8. |
| Unsupported: 1.6 | March 15, 2021 | Compatible to Java 14, libraries upgraded |
| Unsupported: 1.7 | April 3, 2022 | Compatible to Java 17, libraries upgraded, dropped support for java version prior to 11, Play scripts upgrade to Python 3 |
| Unsupported: 2.0 | March 13, 2012 | Sadek Drobi joined Guillaume Bort late 2011 to create Play 2.0 in conjunction with Typesafe Stack 2.0. |
| Unsupported: 2.1 | February 6, 2013 | Upgraded to Scala 2.10 and introduced, among other new features, modularization, a new JSON API, filters and RequireJS support. |
| Unsupported: 2.2 | September 20, 2013 | Upgraded support for SBT to 0.13, better support for buffering, built in support for gzip and new `stage` and `dist` tasks with support for native packaging on several platforms such as OS X (DMG), Linux (RPM, DEB), and Windows (MSI) as well as zip files. |
| Unsupported: 2.3 | May 30, 2014 | Introducing the Activator command, better tooling for static assets, support for Java 8 and Scala 2.11, better performance, Web Service enhancement and support to integrate Actors and Web Sockets. |
| Unsupported: 2.4 | May 26, 2015 | With Dependency injection out of the box, the possibility to embed Play inside other applications, improved Java 8 support, HikariCP as the default connection pool and better testing APIs. |
| Unsupported: 2.5 | March 29, 2016 | Switched from Iteratees to Akka Streams for all asynchronous IO and streaming, replaced custom functional types with Java 8 types (such as `CompletionStage` and `Optional`), introduced equivalent Java APIs for features that previously only existing in the Scala API, such as implementing filters and custom body parsers and with a 20% performance increase. |
| Unsupported: 2.6 | June 23, 2017 | Using Akka HTTP as the default server backend, experimental HTTP/2 support, Scala 2.12 support, no more global state under the hood, JSON Web Token format for cookies, improved security and configuration improvements. |
| Unsupported: 2.7 | February 1, 2019 | Scala 2.13 support, support for Caffeine as underlying cache implementation, updated HikariCP and Guice versions, improved form validation and file uploading functions. |
| Unsupported: 2.8 | December 13, 2019 | Java 11 support, Updated Akka, Jackson, support pre-seek sources for range results |
| Latest version: 2.9 | October 25, 2023 | Scala 3, Java 17, and Java 21 support. |
| Latest version: 3.0 | October 25, 2023 | Because Akka is no longer open source, Play switched from Akka to Apache Pekko. |
| **Legend:**UnsupportedSupported**Latest version**Preview versionFuture version |   |   |

## Motivation

Play is heavily inspired by ASP.NET MVC, Ruby on Rails and Django and is similar to this family of frameworks. Play web applications can be written in Scala or Java, in an environment that may be less Java Enterprise Edition-centric. Play uses no Java EE constraints. This can make Play simpler to develop compared to other Java-centric platforms.

Although Play 1.x could also be packaged as WAR files to be distributed to standard Java EE application servers, Play 2.x applications are now designed to be run using the built-in Akka HTTP or Netty web servers exclusively.

## Major differences from Java frameworks

- Stateless: Play 2 is fully RESTful – there is no Java EE session per connection.
- Integrated unit testing: JUnit and Selenium support is included in the core.
- API comes with most required elements built-in.
- Asynchronous I/O: due to using Akka HTTP as its web server, Play can service long requests asynchronously rather than tying up HTTP threads doing business logic like Java EE frameworks that don't use the asynchronous support offered by Servlet 3.0.
- Modular architecture: like Ruby on Rails and Django, Play comes with the concept of modules.
- Native Scala support: Play 2 uses Scala internally but also exposes both a Scala API, and a Java API that is deliberately slightly different to fit in with Java conventions, and Play is completely interoperable with Java.

## Testing framework

Play provides integration with test frameworks for unit testing and functional testing for both Scala and Java applications. For Scala, integrations with Scalatest and Specs2 are provided out-of-the-box and, for Java, there is integration with JUnit 4. For both languages, there is also integration with Selenium (software). SBT is used to run the tests and also to generate reports. It is also possible to use code coverage tools by using sbt plugins such as scoverage or jacoco4sbt.

## Usage

In August 2011, Heroku announced native support for Play applications on its cloud computing platform. This followed module-based support for Play 1.0 on Google App Engine, and documented support on Amazon Web Services.

As of October 2013, the Play Framework was the most popular Scala project on GitHub.

In July 2015, Play was the 3rd most popular Scala library in GitHub, based on 64,562 Libraries. 21.3% of the top Scala projects used Play as their framework of choice.

Corporate users of the Play Framework have included Coursera, HuffPost, Hootsuite, Janrain, LinkedIn, and Connectifier.
