---
title: "Motivation"
source: https://dramatiq.io/motivation.html
domain: dramatiq
license: CC-BY-SA-4.0
tags: python dramatiq, dramatiq task queue, background task python
fetched: 2026-07-02
---

# Motivation

Dramatiq’s primary reason for being is the fact that I wanted a distributed task queueing library that is simple and has sane defaults for most SaaS workloads. In that sense, it draws a lot of inspiration from GAE Push Queues and Sidekiq.

Dramatiq’s driving principles are as follows:

- high reliability and performance
- simple and easy to understand core
- convention over configuration

If you’ve ever had to use Celery in anger, Dramatiq could be the tool for you.

## Compared to *

Note

This section was last updated in 2019. It’s possible that various bits of the table below are now outdated. Clarifications in PR form are always welcome!

I’ve used Celery professionally for years and my growing frustration with it is one of the reasons why I developed dramatiq. Here are some of the main differences between Dramatiq, Celery, Huey and RQ:

|   | Dramatiq | Celery | Huey | RQ |
|---|---|---|---|---|
| Python 2 support | No | Yes | Yes | Yes |
| Windows support | Yes | No | Yes | No |
| Simple implementation | Yes | No [3] | Yes | Yes |
| Automatic retries | Yes | No | Yes | No |
| Reliable delivery | Yes | Optional [1] | No | No |
| Locks and rate limiting | Yes | No | Yes | No |
| Task prioritization | Yes [4] | No [4] | Yes | Yes |
| Delayed tasks | Yes | Yes [2] | Yes | No |
| Cronlike scheduling | No [5] | Yes | Yes | No |
| Chaining / Pipelining | Yes | Yes | Yes | No |
| Result storage | Yes | Yes | Yes | Yes |
| Code auto-reload | Yes | No | No | No |
| RabbitMQ support | Yes | Yes | Yes | No |
| Redis support | Yes | Yes | Yes | Yes |
| In-memory broker support | Yes | No | Yes | No |
| Greenlet support | Yes | Yes | Yes | No |
