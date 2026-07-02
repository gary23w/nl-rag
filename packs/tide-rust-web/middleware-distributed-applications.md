---
title: "Middleware (distributed applications)"
source: https://en.wikipedia.org/wiki/Middleware_(distributed_applications)
domain: tide-rust-web
license: CC-BY-SA-4.0
tags: tide rust framework, async-std web framework, rust minimal framework, tide middleware endpoint
fetched: 2026-07-02
---

# Middleware (distributed applications)

**Middleware** in the context of distributed applications is software that constraint services beyond those provided by the operating system to enable the various components of a distributed system to communicate and manage data. Middleware supports and simplifies complex distributed applications. It includes web servers, application servers, messaging and similar tools that support application development and delivery. Middleware is especially integral to modern information technology based on XML, SOAP, Web services, and service-oriented architecture.

Middleware often enables interoperability between applications that run on different operating systems, by supplying services so the application can exchange data in a standards-based way. Middleware sits "in the middle" between application software that may be working on different operating systems. It is similar to the middle layer of a three-tier single system architecture, except that it is stretched across multiple systems or applications. Examples include EAI software, telecommunications software, transaction monitors, and messaging-and-queueing software.

The distinction between operating system and middleware functionality is, to some extent, arbitrary. While core kernel functionality can only be provided by the operating system itself, some functionality previously provided by separately sold middleware is now integrated in operating systems. A typical example is the TCP/IP stack for telecommunications, nowadays included virtually in every operating system.

## Definitions

Middleware is defined as software that provides a link between separate software applications. It is sometimes referred to as plumbing because it connects two applications and passes data between them. Middleware allows data contained in one database to be accessed through another. This makes it particularly useful for enterprise application integration and data integration tasks.

In more abstract terms, middleware is "The software layer that lies between the operating system and applications on each side of a distributed computing system in a network."

## Origins

Middleware gained popularity in the 1980s as a solution to the problem of how to link newer applications to older legacy systems, although the term had been in use since 1968. It also facilitated distributed processing, the connection of multiple applications to create a larger application, usually over a network.

## Use

Middleware services provide a more functional set of application programming interfaces to allow an application to:

- Locate transparently across the network, thus providing interaction with another service or application
- Filter data to make them friendly usable or public via anonymization process for privacy protection (for example)
- Be independent from network services
- Be reliable and always available
- Add complementary attributes like semantics

when compared to the operating system and network services.

Middleware offers some unique technological advantages for business and industry. For example, traditional database systems are usually deployed in closed environments where users access the system only via a restricted network or intranet (e.g., an enterprise’s internal network). With the phenomenal growth of the World Wide Web, users can access virtually any database for which they have proper access rights from anywhere in the world. Middleware addresses the problem of varying levels of interoperability among different database structures. Middleware facilitates transparent access to legacy database management systems (DBMSs) or applications via a web server without regard to database-specific characteristics.

Businesses frequently use middleware applications to link information from departmental databases, such as payroll, sales, and accounting, or databases housed in multiple geographic locations. In the highly competitive healthcare community, laboratories make extensive use of middleware applications for data mining, laboratory information system (LIS) backup, and to combine systems during hospital mergers. Middleware helps bridge the gap between separate LISs in a newly formed healthcare network following a hospital buyout.

Middleware can help software developers avoid having to write application programming interfaces (API) for every control program, by serving as an independent programming interface for their applications. For Future Internet network operation through traffic monitoring in multi-domain scenarios, using mediator tools (middleware) is a powerful help since they allow operators, searchers and service providers to supervise Quality of service and analyse eventual failures in telecommunication services.

Finally, e-commerce uses middleware to assist in handling rapid and secure transactions over many different types of computer environments. In short, middleware has become a critical element across a broad range of industries, thanks to its ability to bring together resources across dissimilar networks or computing platforms.

In 2004 members of the European Broadcasting Union (EBU) carried out a study of Middleware with respect to system integration in broadcast environments. This involved system design engineering experts from 10 major European broadcasters working over a 12-month period to understand the effect of predominantly software-based products to media production and broadcasting system design techniques. The resulting reports Tech 3300 and Tech 3300s were published and are freely available from the EBU web site.

## Types

### Message-oriented middleware

Message-oriented middleware (MOM) is middleware where transactions or event notifications are delivered between disparate systems or components by way of messages, often via an enterprise messaging system. With MOM, messages sent to the client are collected and stored until they are acted upon, while the client continues with other processing.

**Enterprise messaging**

An

enterprise messaging system

is a type of middleware that facilitates message passing between disparate systems or components in standard formats, often using

XML

,

SOAP

or

web services

. As part of an enterprise messaging system,

message broker

software may queue, duplicate, translate and deliver messages to disparate systems or components in a messaging system.

**Enterprise service bus**

Enterprise service bus

(ESB) is defined by the

Burton Group

as "some type of integration middleware product that supports both

message-oriented middleware

and

Web services

".

### Intelligent middleware

Intelligent Middleware (IMW) provides real-time intelligence and event management through intelligent agents. The IMW manages the real-time processing of high volume sensor signals and turns these signals into intelligent and actionable business information. The actionable information is then delivered in end-user power dashboards to individual users or is pushed to systems within or outside the enterprise. It is able to support various heterogeneous types of hardware and software and provides an API for interfacing with external systems. It should have a highly scalable, distributed architecture which embeds intelligence throughout the network to transform raw data systematically into actionable and relevant knowledge. It can also be packaged with tools to view and manage operations and build advanced network applications most effectively.

### Content-centric middleware

Content-centric middleware offers a simple *provider-consumer* abstraction through which applications can issue requests for uniquely identified content, without worrying about where or how it is obtained. Juno is one example, which allows applications to generate content requests associated with high-level delivery requirements. The middleware then adapts the underlying delivery to access the content from sources that are best suited to matching the requirements. This is therefore similar to Publish/subscribe middleware, as well as the Content-centric networking paradigm.

**Remote procedure call**

Remote procedure call

middleware enables a client to use services running on remote systems. The process can be

synchronous

or

asynchronous

.

**Object request broker**

With

object request broker

middleware, it is possible for applications to send objects and request services in an object-oriented system.

**SQL-oriented data access**

SQL-oriented Data Access

is middleware between applications and database servers.

**Embedded middleware**

Embedded middleware provides communication services and software/

firmware

integration interface that operates between embedded applications, the embedded operating system, and external applications.

### Policy Appliances

Policy appliance is a generic term referring to any form of middleware that manages policy rules. They can mediate between data owners or producers, data aggregators, and data users. Among heterogeneous institutional systems or networks they may be used to enforce, reconcile, and monitor agreed information management policies and laws across systems (or between jurisdictions) with divergent information policies or needs. Policy appliances can interact with smart data (data that carries with it contextual relevant terms for its own use), intelligent agents (queries that are self-credentialed, authenticating, or contextually adaptive), or context-aware applications to control information flows, protect security and confidentiality, and maintain privacy. Policy appliances support policy-based information management processes by enabling rules-based processing, selective disclosure, and accountability and oversight.

Examples of policy appliance technologies for rules-based processing include analytic filters, contextual search, semantic programs, labeling and wrapper tools, and DRM, among others; policy appliance technologies for selective disclosure include anonymization, content personalization, subscription and publishing tools, among others; and, policy appliance technologies for accountability and oversight include authentication, authorization, immutable and non-repudiable logging, and audit tools, among others.

### Other

Other sources include these additional classifications:

- Transaction processing monitors – provides tools and an environment to develop and deploy distributed applications.
- Application servers – software installed on a computer to facilitate the serving (running) of other applications.

## Integration Levels

### Data Integration

- Integration of data resources like files and databases

### Cloud Integration

- Integration between various cloud services

### B2B Integration

- Integration of data resources and partner interfaces

### Application Integration

- Integration of applications managed by a company

## Vendors

IBM, Red Hat, Oracle Corporation and Microsoft are some of the vendors that provide middleware software. Vendors such as Axway, SAP, TIBCO, Informatica, Objective Interface Systems, Pervasive, ScaleOut Software and webMethods were specifically founded to provide more niche middleware solutions. Groups such as the Apache Software Foundation, OpenSAF, the ObjectWeb Consortium (now OW2) and OASIS' AMQP encourage the development of open source middleware. Microsoft .NET "Framework" architecture is essentially "Middleware" with typical middleware functions distributed between the various products, with most inter-computer interaction by industry standards, open APIs or RAND software licence. Solace provides middleware in purpose-built hardware for implementations that may experience scale. StormMQ provides Message Oriented Middleware as a service.
