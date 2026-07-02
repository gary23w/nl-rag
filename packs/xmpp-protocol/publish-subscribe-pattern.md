---
title: "Publish–subscribe pattern"
source: https://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern
domain: xmpp-protocol
license: CC-BY-SA-4.0
tags: xmpp protocol, extensible messaging and presence protocol, jabber messaging, xml streaming protocol
fetched: 2026-07-02
---

# Publish–subscribe pattern

In software architecture, the **publish–subscribe pattern** (**pub/sub**) is a messaging pattern in which message senders, called **publishers**, categorize messages into classes (or *topics*), and send them without needing to know which components will receive them. Message recipients, called **subscribers**, express interest in one or more classes and only receive messages in those classes, without needing to know the identity of the publishers.

This pattern decouples the components that produce messages from those that consume them, and supports asynchronous, many-to-many communication. The publish–subscribe model is commonly contrasted with message queue-based and point-to-point messaging models, where producers send messages directly to consumers.

Publish–subscribe is a sibling of the message queue paradigm, and is typically a component of larger message-oriented middleware systems. Many modern messaging frameworks and protocols, such as the Java Message Service (JMS), Apache Kafka, and MQTT, support both the pub/sub and queue-based models.

This pattern provides greater network scalability and supports more dynamic topologies, but can make it harder to modify the publisher’s logic or the structure of the published data. Compared to synchronous patterns like RPC and point-to-point messaging, publish–subscribe provides the highest level of decoupling among architectural components. However, it can also lead to semantic or format coupling between publishers and subscribers, which may cause systems to become entangled or brittle over time.

## Message filtering

In publish–subscribe systems, subscribers typically receive only a subset of messages. The process of selecting relevant messages is called **filtering**, and it can be implemented in several ways:

- **Topic-based filtering**: Messages are published to named *topics* or *channels*. Subscribers register to receive messages on specific topics, and receive all messages published to them.
- **Content-based filtering**: Subscribers define constraints based on message attributes or content. Messages are delivered only if they match the subscriber's criteria.
- **Hybrid systems**: Some implementations combine topic- and content-based filtering. Messages are categorized by topic, and subscribers apply content-based filters to messages within those topics.

## Topologies

In most pub/sub systems, publishers and subscribers communicate through a central intermediary such as a message broker or event bus. The broker receives messages from publishers and forwards them to the appropriate subscribers, optionally performing store and forward, priority queuing, or other routing logic.

Subscriber registration can occur at different times:

- **Build time**: Subscribers are hardcoded to handle specific messages or events (e.g., GUI event handlers).
- **Initialization time**: Subscriptions are defined in XML configuration files or metadata.
- **Runtime**: Subscriptions can be added or removed dynamically (e.g., database triggers, RSS readers).

Some pub/sub systems use **brokerless** architectures, in which publishers and subscribers discover each other and exchange messages directly. For example, the Data Distribution Service (DDS) middleware uses IP multicast and metadata sharing to establish communication paths. Brokerless systems require construction of overlay networks, often using Small-World topologies to enable efficient routing.

It was shown by Jon Kleinberg that efficient decentralized routing requires Navigable Small-World topologies, which are employed in federated or peer-to-peer pub/sub systems. Locality-aware pub/sub networks use low-latency links to reduce message propagation time.

## History

One of the earliest publicly described pub/sub systems was the "news" subsystem of the Isis Toolkit, presented at the 1987 ACM Symposium on Operating Systems Principles (SOSP '87).

Although the publish–subscribe pattern is now typically distinguished from the observer pattern due to its emphasis on decoupling and distributed communication, early usage in literature and systems sometimes used the terms interchangeably, especially in the context of in-process event handling or GUI frameworks. As distributed systems became more common, the publish–subscribe model evolved to emphasize asynchronous messaging and broker-mediated communication, setting it apart from the more tightly coupled observer pattern.

## Advantages

### Loose coupling

Publishers are loosely coupled to subscribers, and need not even know of their existence. With the topic being the focus, publishers and subscribers are allowed to remain ignorant of system topology. Each can continue to operate as per normal independently of the other. In the traditional tightly coupled client–server paradigm, the client cannot post messages to the server while the server process is not running, nor can the server receive messages unless the client is running. Many pub/sub systems decouple not only the locations of the publishers and subscribers but also decouple them temporally. A common strategy used by middleware analysts with such pub/sub systems is to take down a publisher to allow the subscriber to work through the backlog (a form of bandwidth throttling).

### Scalability

Pub/sub provides the opportunity for better scalability than traditional client-server, through parallel operation, message caching, tree-based or network-based routing, etc. However, in certain types of tightly coupled, high-volume enterprise environments, as systems scale up to become data centers with thousands of servers sharing the pub/sub infrastructure, current vendor systems often lose this benefit; scalability for pub/sub products under high load in these contexts is a research challenge.

Outside of the enterprise environment, on the other hand, the pub/sub paradigm has proven its scalability to volumes far beyond those of a single data center, providing Internet-wide distributed messaging through web syndication protocols such as RSS and Atom. These syndication protocols accept higher latency and lack of delivery guarantees in exchange for the ability for even a low-end web server to syndicate messages to (potentially) millions of separate subscriber nodes.

### Message delivery issues

Redundant subscribers in a pub/sub system can help assure message delivery with minimal additional complexity. For example, a factory may utilize a pub/sub system where equipment can publish problems or failures to a subscriber that displays and logs those problems. If the logger fails (crashes), equipment problem publishers won't necessarily receive notice of the logger failure, and error messages will not be displayed or recorded by any equipment on the pub/sub system. In a client/server system, when an error logger fails, the system will receive an indication of the error logger (server) failure. However, the client/server system will have to deal with that failure by having redundant logging servers online, or by dynamically spawning fallback logging servers. This adds complexity to the client and server designs, as well as to the client/server architecture as a whole. In a pub/sub system, redundant logging subscribers that are exact duplicates of the existing logger can be added to the system to increase logging reliability without any impact to any other equipment on the system. The feature of assured error message logging can also be added incrementally, subsequent to implementing the basic functionality of equipment problem message logging.

## Disadvantages

The most serious problems with pub/sub systems are a side-effect of their main advantage: the decoupling of publisher from subscriber.

### Message delivery issues

A pub/sub system must be designed carefully to be able to provide stronger system properties that a particular application might require, such as assured delivery.

- The broker in a pub/sub system may be designed to deliver messages for a specified time, but then stop attempting delivery, whether or not it has received confirmation of successful receipt of the message by all subscribers. A pub/sub system designed in this way cannot guarantee delivery of messages to any applications that might require such assured delivery. Tighter coupling of the designs of such a publisher and subscriber pair must be enforced outside of the pub/sub architecture to accomplish such assured delivery (e.g. by requiring the subscriber to publish receipt messages).
- A publisher in a pub/sub system may assume that a subscriber is listening, when in fact it is not.

The pub/sub pattern scales well for small networks with a small number of publisher and subscriber nodes and low message volume. However, as the number of nodes and messages grows, the likelihood of instabilities increases, limiting the maximum scalability of a pub/sub network. Example throughput instabilities at large scales include:

- Load surges—periods when subscriber requests saturate network throughput followed by periods of low message volume (underutilized network bandwidth)
- Slowdowns—as more and more applications use the system (even if they are communicating on separate pub/sub channels) the message volume flow to an individual subscriber will slow

For pub/sub systems that use brokers (servers), the argument for a broker to send messages to a subscriber is in-band, and can be subject to security problems. Brokers might be fooled into sending notifications to the wrong client, amplifying denial of service requests against the client. Brokers themselves could be overloaded as they allocate resources to track created subscriptions.

Even with systems that do not rely on brokers, a subscriber might be able to receive data that it is not authorized to receive. An unauthorized publisher may be able to introduce incorrect or damaging messages into the pub/sub system. This is especially true with systems that broadcast or multicast their messages. Encryption (e.g. Transport Layer Security (SSL/TLS)) can prevent unauthorized access, but cannot prevent damaging messages from being introduced by authorized publishers. Architectures other than pub/sub, such as client/server systems, are also vulnerable to authorized message senders that behave maliciously.
