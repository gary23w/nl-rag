---
title: "Event-driven messaging"
source: https://en.wikipedia.org/wiki/Event-driven_messaging
domain: asyncapi-spec
license: CC-BY-SA-4.0
tags: asyncapi specification, event-driven api spec, message-driven api, async api contract
fetched: 2026-07-02
---

# Event-driven messaging

The **event-driven messaging** is a design pattern to enable the service consumers, which are interested in events that occur within the periphery of a service provider, to get notifications about these events as and when they occur without resorting to the traditional inefficient polling based mechanism.

It's important to differentiate between event-driven and message-driven (a.k.a. queue driven) services: Event-driven services (e.g. AWS SNS) are decoupled from their consumers. Whereas queue / message driven services (e.g. AWS SQS) are coupled with their consumers.

## Rationale

The interaction between a service consumer and a service provider is normally initiated by the service consumer as it needs to respond to an event that occurs within the boundary of the service consumer itself, e.g. requiring some data from an external resource (i.e. the service provider) in order to perform a calculation whose results need to be relayed back to a user interface in response to an action performed by the user. However, there are situations where the service consumer needs to wait for the occurrence of an event within the boundary of the service provider itself. Under these circumstances, the service consumer somehow needs to be informed of the event as and when it happens. One way is to program the service consumer to poll the service provider with regular intervals so that it can check if the event happened or not. This approach not only manifests inefficiency but also behavioral unpredictability. Inefficiency because the service consumer and the service provider are engaged in unproductive interactions and unreliable because it might be that the event actually happened more than once before the service consumer could poll the service provider, thereby missing the previous events and their related data. Apart from these problems, such a technique also introduces latency as the interval with which the service consumer performs the polling is fixed and, therefore, it would only fetch the event data at that time and not when the event actually occurred. This whole scenario deteriorates even further if multiple service consumers are dependent on a particular service provider.

In order to tackle this problem, the event-driven messaging design pattern suggests a publisher-subscriber communication mechanism that ensures timely notification of event related data to the service consumer, thereby eliminating the inefficiencies linked with the traditional polling based communication mechanism.

## Usage

The application of the event-driven messaging design pattern requires an event manager with whom the service provider registers its events. The service consumers then register their interest in some or all of the advertised events. Upon the occurrence of an event, the service provider informs the event manager that then notifies all the registered service consumers instantly. This communication mechanism shares its roots with the Observer pattern applied traditionally within the object-oriented world. This design pattern also borrows some concepts from the Event-Driven Architecture as the fundamental rationale behind this design pattern is responding to events.

The actual implementation of such a publisher–subscriber-based communication mechanism requires architectural extensions in order to provide such a complex message tracking and forwarding mechanism. A mature ESB product should normally be able to provide such functionality. The application of this pattern helps to further decouple the service consumers from the service providers and increases the overall reliability of a service composition.
