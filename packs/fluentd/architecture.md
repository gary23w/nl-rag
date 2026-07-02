---
title: "What is Fluentd?"
source: https://www.fluentd.org/architecture
domain: fluentd
license: CC-BY-SA-4.0
tags: fluentd logging, log collection, log management, unified logging layer
fetched: 2026-07-02
---

# What is Fluentd?

- (feedback) **Feedback**
- (slack)

### Before Fluentd

### After Fluentd

### Fluentd is an open source data collector, which lets you unify the data collection and consumption for a better use and understanding of data.

Here're the key features.

## Unified Logging with JSON

Fluentd tries to structure data as JSON as much as possible: this allows Fluentd to **unify** all facets of processing log data: collecting, filtering, buffering, and outputting logs across **multiple sources and destinations** (Unified Logging Layer). The downstream data processing is much easier with JSON, since it has enough structure to be accessible while retaining flexible schemas.

## Pluggable Architecture

Fluentd has a flexible plugin system that allows the community to extend its functionality. Our 500+ community-contributed plugins connect dozens of data sources and data outputs. By leveraging the plugins, you can start making better use of your logs right away.

## Minimum Resources Required

Fluentd is written in a combination of C language and Ruby, and requires very little system resource. The vanilla instance runs on 30-40MB of memory and can process 13,000 events/second/core. If you have tighter memory requirements (-450kb), check out Fluent Bit, the lightweight forwarder for Fluentd.

## Built-in Reliability

Fluentd supports memory- and file-based buffering to prevent inter-node data loss. Fluentd also supports robust failover and can be set up for high availability. 2,000+ data-driven companies rely on Fluentd to differentiate their products and services through a better use and understanding of their log data.

### Fluentd History

Fluentd was conceived by Sadayuki "Sada" Furuhashi in 2011. Sada is a co-founder of Treasure Data, Inc., a primary sponsor of the Fluentd project. Since being open-sourced in October 2011, the Fluentd project has grown dramatically: dozens of contributors, hundreds of community-contributed plugins, thousands of users, and trillions of events collected, filtered and stored. Fluentd was accepted to Cloud Native Computing Foundation on November 8, 2016 and is at the Graduated project maturity level on 2019. And its development is maintained with the community.

Learn why Fluentd is for you

## Learn

Want to learn the basics of Fluentd? Check out these pages.

- What is Fluentd?
- Why use Fluentd?
- Who is using Fluentd?
- What is Unified Logging Layer?
- FAQs

## Ask the Community

Couldn't find enough information? Let's ask the community!

- Forum
- Google Group
- News Letter
- Stack Overflow
- Issue Tracker
- Twitter
- Facebook
- Source Code

## Ask the Experts

You need commercial-grade support from Fluentd committers and experts?

- Enterprise Services
- Ecosystem Survey/Interview

©2010-2026 Fluentd Project. ALL Rights Reserved. Fluentd is a hosted project under the Cloud Native Computing Foundation (CNCF). All components are available under the Apache 2 License.

The Linux Foundation has registered trademarks and uses trademarks. For a list of trademarks of The Linux Foundation, please see our Trademark Usage page.
