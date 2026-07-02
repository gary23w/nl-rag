---
title: "Service-level objective"
source: https://en.wikipedia.org/wiki/Service-level_objective
domain: slo-burn-rate
license: CC-BY-SA-4.0
tags: burn rate alerting, error budget consumption, multiwindow burn alert, fast slow burn
fetched: 2026-07-02
---

# Service-level objective

A **service-level objective** (**SLO**) is a target value or range of values for a service level that is measured by an SLI. An SLO is a key element of a service-level agreement (SLA) between a service provider and a customer. SLOs are agreed upon as a means of measuring the performance of the service provider and are outlined as a way of avoiding disputes between the two parties based on misunderstanding.

## Overview

There is often confusion in the use of SLAs and SLOs. The SLA is the entire agreement that specifies what service is to be provided, how it is supported, times, locations, costs, performance, and responsibilities of the parties involved. SLOs are specific measurable characteristics of the SLA such as availability, throughput, frequency, response time, or quality. These SLOs together are meant to define the expected service between the provider and the customer and vary depending on the service's urgency, resources, and budget. SLOs provide a quantitative means to define the level of service a customer can expect from a provider.

The SLO are formed by setting goals for metrics (commonly called service level indicators, SLIs). As an example, an availability SLO may be defined as the expected measured value of an availability SLI over a prescribed duration (e.g. four weeks). The availability SLI used will vary based on the nature and architecture of the service. For example, a simple web service might use the ratio of successful responses served vs the total number of valid requests received. (total_success / total_valid)

## Examples

Sturm and Morris argue that SLOs must be:

- Attainable
- Repeatable
- Measurable
- Understandable
- Meaningful
- Controllable
- Affordable
- Mutually acceptable

While Andrieux et al. define the SLO as "the quality of service aspect of the agreement. Syntactically, it is an assertion over the terms of the agreement as well as such qualities as date and time". Keller and Ludwig more concisely define an SLO as "commitment to maintain a particular state of the service in a given period" with respect to the state of the SLA parameters. Keller and Ludwig go on to state that while service providers will most often be the lead entity in taking on SLOs there is no firm definition as such and any entity can be responsible for an SLO. Along with this an SLO can be broken down into a number of different components:

- Obliged – The entity that is required to deliver the SLO.
- Validity period – The time in which the SLO will be delivered.
- Expression – This is the actual language that defines what the SLO will be.

Optionally an EvaluationEvent maybe assigned to the SLO, an EvaluationEvent is defined as the measure by which the SLO will be checked to see whether it's meeting the expression.

SLOs should generally be specified in terms of an achievement value or service level, a target measurement, a measurement period, and where and how they are measured. As an example, "90% of calls to the helpdesk should be answered in less than 20 seconds measured over a one-month period as reported by the ACD system". Results can be reported as a percent of time that the target answer time was achieved and then compared to the desired service level (90%).

| Type of measure | Example SLO requirement | Measurement period |
|---|---|---|
| Availability | The application will be available 99.95% of the time | Over a year |
| Service-desk response | 75% of help desk calls will be answered in less than a minute 85% of help desk calls will be answered within two minutes 100% of help desk calls will be answered within three minutes | Over a month |
| Incident response time | 99% of severity 1 tickets will be resolved within three hours 98% of severity 2 tickets will be resolved within eight hours 98% of severity 3 tickets will be resolved within three business days 98% of severity 4 tickets will be resolved within five business days | Over a quarter |
| Response time | 85% of TCP replies within 1.5 seconds of receiving a request 99.5% of TCP replies within 4 seconds of receiving a request | Over a month |

## Term usage

The SLO term is found in various scientific papers, for instance in the reference architecture of the SLA@SOI project, and it is used in the Open Grid Forum document on WS-Agreement.
