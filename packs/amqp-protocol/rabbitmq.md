---
title: "RabbitMQ"
source: https://en.wikipedia.org/wiki/RabbitMQ
domain: amqp-protocol
license: CC-BY-SA-4.0
tags: amqp protocol, advanced message queuing protocol, message broker protocol, queue-based messaging
fetched: 2026-07-02
---

# RabbitMQ

**RabbitMQ** is an open-source message-broker software (sometimes called message-oriented middleware) that originally implemented the Advanced Message Queuing Protocol (AMQP) and has since been extended with a plug-in architecture to support Streaming Text Oriented Messaging Protocol (STOMP), MQ Telemetry Transport (MQTT), and other protocols.

Written in Erlang, the RabbitMQ server is built on the Open Telecom Platform framework for clustering and failover. Client libraries to interface with the broker are available for all major programming languages. The source code is released under the Mozilla Public License.

Since November 2020, there are commercial offerings available of RabbitMQ, for support and enterprise features: "VMware RabbitMQ OVA", "VMware RabbitMQ" and "VMware RabbitMQ for Kubernetes" (different feature levels) Open-Source RabbitMQ is also packaged by Bitnami and commercially for Broadcom's VMware Tanzu Application Service.

## History

Originally developed by Rabbit Technologies Ltd. which started as a joint venture between LShift and CohesiveFT in 2007, RabbitMQ was acquired in April 2010 by SpringSource, a division of VMware. The project became part of Pivotal Software in May 2013, which then got acquired back by VMware in December 2019.

The project consists of:

- The RabbitMQ exchange server
- Gateways for AMQP, HTTP, STOMP, and MQTT protocols
- AMQP client libraries for Java, .NET Framework and Erlang. (AMQP clients for other languages are available from other vendors.)
- A plug-in platform for extensibility, with a predefined collection of supported plug-ins, including:
  - A "Shovel" plug-in that takes care of moving or copying (replicating) messages from one broker to another.
  - A "Federation" plug-in that enables efficient sharing of messages between brokers (at the exchange level).
  - A "Management" plug-in that enables monitoring and control of brokers and clusters of brokers.

## Examples

This section gives sample programs written in Python (using the *pika* package) for sending and receiving messages using a queue.

### Sending

The following code fragment establishes a connection, makes sure the recipient queue exists, then sends a message and finally closes the connection.

```mw
#!/usr/bin/env python3
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()
channel.queue_declare(queue="hello")
channel.basic_publish(exchange="", routing_key="hello", body="Hello World!")
print(" [x] Sent 'Hello World!'")
connection.close()
```

### Receiving

Similarly, the following program receives messages from the queue and prints them on the screen: (Note: This example does not acknowledge receipt of the message.)

```mw
#!/usr/bin/env python3
import pika

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()
channel.queue_declare(queue="hello")
print(" [*] Waiting for messages. To exit press Ctrl+C")
channel.basic_consume(queue="hello", on_message_callback=callback)
channel.start_consuming()
```
