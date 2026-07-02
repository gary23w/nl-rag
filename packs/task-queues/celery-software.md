---
title: "Celery (software)"
source: https://en.wikipedia.org/wiki/Celery_(software)
domain: task-queues
license: CC-BY-SA-4.0
tags: task queue, message queue, distributed task, worker queue
fetched: 2026-07-02
---

# Celery (software)

**Celery** is an open source asynchronous task queue or job queue which is based on distributed message passing. While it supports scheduling, its focus is on operations in real time.

## Overview

The execution units, called *tasks*, are executed concurrently on one or more worker nodes using multiprocessing, eventlet or gevent. Tasks can execute asynchronously (in the background) or synchronously (wait until ready). Celery is used in production systems, for services such as Instagram, to process millions of tasks every day.

## Technology

Celery is written in Python, but the protocol can be implemented in any language. It can also operate with other languages using webhooks. There is also a Ruby-Client called RCelery, a PHP client, a Go client, a Rust client, and a Node.js client.

Celery requires a message broker to run. As of October 2024, Redis and RabbitMQ are supported and actively maintained and monitored. Amazon SQS is supported and maintained but does not support worker inspection and management at runtime, while Zookeeper and Kafka are currently in experimental development.
