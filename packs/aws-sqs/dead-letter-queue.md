---
title: "Dead letter queue"
source: https://en.wikipedia.org/wiki/Dead_letter_queue
domain: aws-sqs
license: CC-BY-SA-4.0
tags: aws sqs, simple queue service, message queue, event-driven
fetched: 2026-07-02
---

# Dead letter queue

In message queueing a **dead letter queue** (DLQ), or **dead letter topic** (DLT) in some messaging systems, is a service implementation to store messages that the messaging system cannot or should not deliver. Although implementation-specific, messages can be routed to the DLQ for the following reasons:

1. The message is sent to a queue that does not exist.
2. The maximum queue length is exceeded.
3. The message exceeds the size limit.
4. The message expires because it reached the TTL (time to live)
5. The message is rejected by another queue exchange.
6. The message has been read and rejected too many times.

Routing these messages to a dead letter queue enables analysis of common fault patterns and potential software problems. If a message consumer receives a message that it considers invalid, it can instead forward it an Invalid Message Channel, allowing a separation between application-level faults and delivery failures.

Management of dead letter queues typically involves monitoring and alert systems. Organizations may implement specialized handlers for automated remediation or manual processing of DLQ messages.

Queueing systems that incorporate dead letter queues include Amazon EventBridge, Amazon Simple Queue Service, Apache ActiveMQ, Google Cloud Pub/Sub, HornetQ, Microsoft Message Queuing, Microsoft Azure Event Grid and Azure Service Bus, WebSphere MQ, Solace Platform, Rabbit MQ, Confluent Cloud and Apache Pulsar.
