---
title: "Enterprise messaging system"
source: https://en.wikipedia.org/wiki/Enterprise_messaging_system
domain: rabbitmq
license: CC-BY-SA-4.0
tags: rabbitmq broker, advanced message queuing protocol, message broker, work queues, enterprise messaging system
fetched: 2026-07-02
---

# Enterprise messaging system

An **enterprise messaging system** (**EMS**) or messaging system in brief is a set of published enterprise-wide standards that allows organizations to send semantically precise messages between computer systems. EMS systems promote loosely coupled architectures that allow changes in the formats of messages to have minimum impact on message subscribers. EMS systems are facilitated by the use of structured messages (such as using XML or JSON), and appropriate protocols, such as DDS, MSMQ, AMQP or SOAP with web services.

EMS usually takes into account the following considerations:

1. *Security*: Messages must be encrypted if they travel over public interfaces. Messages must be authenticated or digitally signed if the receiver is to have confidence that the messages have not been tampered with in transit.
2. *Routing*: Messages need to be routed efficiently from the sender to the receiver. Intermediate nodes may need to route the messages if the body of the message is encrypted.
3. *Metadata*: The body of the document contains information that must be unambiguously interpreted. Metadata registries should be used to create precise definitions for each data element.
4. *Subscription*: Systems should be able to subscribe to all messages that match a specific pattern. Messages with a specific content may be routed differently. For example, some messages may have different priority or security policies.
5. *Policy*: Enterprise messaging systems should provide some consideration for a centralized policy of messages such as what classes or roles of users can access different fields of any message.

EMS are also known as Message-Oriented Middleware (MOM)

## Separation of message header and message body

The design of an EMS is usually broken down into two sections:

1. *Message header design* – Message headers contain the information necessary to route messages. Message headers are usually coded in clear text so that intermediate nodes receive all the necessary information they need to route and prioritize the message. Message headers are analogous to the information printed on the outside of a letter (to, from, priority of message etc.)
2. *Message body semantics* – Message body semantics include the precise definition of all of the data elements in the body of the message. Message semantics can be aided by the use of a precise data dictionary that documents metadata.

## Comparisons

The commonalities between messaging systems (in terms of capabilities and architecture) have been captured in a platform-independent fashion as enterprise integration patterns (a.k.a. messaging patterns).

Although similar in concept to an enterprise service bus (ESB), an EMS places emphasis on design of messaging protocols (for instance, using DDS, MSMQ or AMQP), not the implementation of the services using a specific technology such as web services, DDS APIs for C/C++ and Java, .NET or Java Message Service (JMS).

Note that an Enterprise Messaging System should not be confused with an electronic mail system used for delivering human readable text messages to individual people.

An example of a specific application programming interface (API) that implements an enterprise messaging system is the Java Message Service. Although this is an API it embodies many of the same issues involved in setting up a full EMS.

Policy statements may also be extracted from a centralized policy server. These policy statements can be expressed in the XML Access Control Markup Language (XACML).
