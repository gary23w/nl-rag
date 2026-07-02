---
title: "Intent-based network"
source: https://en.wikipedia.org/wiki/Intent-Based_Networking
domain: intent-based-networking
license: CC-BY-SA-4.0
tags: intent-based networking, autonomic networking, closed-loop automation, policy abstraction
fetched: 2026-07-02
---

# Intent-based network

(Redirected from

Intent-Based Networking

)

**Intent-Based Networking (IBN)** is an approach to network management that shifts the focus from manually configuring individual devices to specifying desired outcomes or business objectives, referred to as "intents".

## Description

Rather than relying on low-level commands to configure the network, administrators define these high-level intents, and the network dynamically adjusts itself to meet these requirements. IBN simplifies the management of complex networks by ensuring that the network infrastructure aligns with the desired operational goals. For example, an implementer can explicitly state a network purpose with a policy such as "Allow hosts A and B to communicate with X bandwidth capacity" without the need to understand the detailed mechanisms of the underlying devices (e.g. switches), topology or routing configurations.

## Architecture

Advances in Natural Language Understanding (NLU) systems, along with neural network-based algorithms like BERT, RoBERTa, GLUE, and ERNIE, have enabled the conversion of user queries into structured representations that can be processed by automated services. This capability is crucial for managing the increasing complexity of network services. Intent-Based Networking (IBN) leverages these advancements to simplify network management by abstracting network services, reducing operational complexity, and lowering costs.

A proposed three-layered architecture integrates intent-based automation into network management systems. In the **business layer**, intents are based on Key Performance Indicators (KPIs) and Service Level Agreements (SLAs), reflecting business objectives. The **intent layer** evaluates and re-plans actions dynamically, where a **Knowledge** module abstracts and reasons about intents, while an **Agent** interfaces with network objects to execute actions. The **data layer** observes network objects, updates topology information, and interacts with the Knowledge and Agent modules to ensure accurate and timely responses to network changes. At the bottom, the **network layer** contains the physical infrastructure, transforming network data into a usable format for the intent layer to act upon.
