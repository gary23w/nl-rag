---
title: "Enterprise Integration Patterns"
source: https://en.wikipedia.org/wiki/Enterprise_Integration_Patterns
domain: apache-camel
license: CC-BY-SA-4.0
tags: apache camel, enterprise integration patterns, integration framework, message routing
fetched: 2026-07-02
---

# *Enterprise Integration Patterns*

***Enterprise Integration Patterns*** is a book by Gregor Hohpe and Bobby Woolf which describes 65 patterns for the use of enterprise application integration and message-oriented middleware in the form of a pattern language.

## The integration (messaging) pattern language

The pattern language presented in the book consists of 65 patterns structured into 9 categories, which largely follow the flow of a message from one system to the next through channels, routing, and transformations. The book includes an icon-based pattern language, sometimes nicknamed "GregorGrams" after one of the authors. Excerpts from the book (short pattern descriptions) are available on the supporting website (see External links).

### Integration styles and types

The book distinguishes four top-level alternatives for integration:

1. File Transfer
2. Shared Database
3. Remote Procedure Invocation
4. Messaging

The following integration types are introduced:

- Information Portal
- Data Replication
- Shared Business Function
- Service Oriented Architecture
- Distributed Business Process
- Business-to-Business Integration
- Tightly Coupled Interaction vs. Loosely Coupled Interaction

### Messaging

- Message Channel
- Message
- Pipes and Filters
- Message Router
- Message Translator
- Message Endpoint

### Message Channel

- Point-to-Point Channel
- Publish-Subscribe Channel
- Datatype Channel
- Invalid Message Channel
- Dead Letter Channel
- Guaranteed Delivery
- Channel Adapter
- Messaging Bridge
- Message Bus

### Message Construction

- Command Message
- Document Message
- Event Message
- Request-Reply
- Return Address
- Correlation Identifier
- Message Sequence
- Message Expiration
- Format Indicator

### Message Router

- Content-Based Router
- Message Filter
- Dynamic Router
- Recipient List
- Splitter
- Aggregator
- Resequencer
- Composed Message Processor
- Scatter-Gather
- Routing Slip
- Process Manager
- Message Broker

### Message Transformation

- Envelope Wrapper
- Content Enricher
- Content Filter
- Claim Check
- Normalizer
- Canonical Data Model

### Message Endpoint

- Messaging Gateway
- Messaging Mapper
- Transactional Client
- Polling Consumer
- Event-Driven Consumer
- Competing Consumers
- Message Dispatcher
- Selective Consumer
- Durable Subscriber
- Idempotent Receiver
- Service Activator

### System Management

- Control Bus
- Detour
- Wire Tap
- Message History
- Message Store
- Smart Proxy
- Test Message
- Channel Purger

The pattern language continues to be relevant as of today, for instance in cloud application development and integration, and in the internet of things. In 2015, the two book authors reunited—for the first time since the publication of the book—for a retrospective and interview in *IEEE Software*.

## Implementation

Enterprise Integration Patterns are implemented in many open source integration solutions. Notable implementations include Spring Integration, Apache Camel, Red Hat Fuse, Mule ESB and Guaraná DSL.
