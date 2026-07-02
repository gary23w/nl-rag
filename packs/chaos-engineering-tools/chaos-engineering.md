---
title: "Chaos engineering"
source: https://en.wikipedia.org/wiki/Chaos_engineering
domain: chaos-engineering-tools
license: CC-BY-SA-4.0
tags: chaos engineering, fault injection, resilience testing, failure injection
fetched: 2026-07-02
---

# Chaos engineering

**Chaos engineering** is the discipline of experimenting on a system in order to build confidence in the system's capability to withstand turbulent conditions in production.

## Concept

In software development, the ability of a given software to tolerate failures while still ensuring adequate quality of service—often termed *resilience*—is typically specified as a requirement. However, development teams may fail to meet this requirement due to factors such as short deadlines or lack of domain knowledge. Chaos engineering encompasses techniques aimed at meeting resilience requirements.

Chaos engineering can be used to achieve resilience against infrastructure failures, network failures, and application failures; the latter includes resilience to unhandled exceptions.

## Operational readiness using chaos engineering

Calculating how much confidence we have in the interconnected complex systems that are put into production environments requires operational readiness metrics. Operational readiness can be evaluated using chaos engineering simulations. Solutions for increasing the resilience and operational readiness of a platform include strengthening the backup, restore, network file transfer, failover capabilities and overall security of the environment.

An evaluation to induce chaos in a Kubernetes environment terminated random pods receiving data from edge devices in data centers while processing analytics on a big data network. The pods' recovery time was a resiliency metric that estimated the response time.

## History

**1983 – Apple**

While MacWrite and MacPaint were being developed for the first Apple Macintosh computer, Steve Capps created "Monkey", a desk accessory which randomly generated user interface events at high speed, simulating a monkey frantically banging the keyboard and moving and clicking the mouse. It was promptly put to use for debugging by generating errors for programmers to fix, because automated testing was not possible; the first Macintosh had too little free memory space for anything more sophisticated.

**1992 – Prologue** While ABAL2 and SING were being developed for the first graphical versions of the PROLOGUE operating system, Iain James Marshall created "La Matraque", a desk accessory which randomly generated random sequences of both legal and invalid graphical interface events, at high speed, thus testing the critical edge behaviour of the underlying graphics libraries. This program would be launched prior to production delivery, for days on end, thus ensuring the required degree of total resilience. This tool was subsequently extended to include the Database and other File Access instructions of the ABAL language to check and ensure their subsequent resiliance. A variation of this tool is currently employed for the qualification of the modern day version known as OPENABAL.

**2003 – Amazon**

While working to improve website reliability at Amazon, Jesse Robbins created "Game day", an initiative that increases reliability by purposefully creating major failures on a regular basis. Robbins has said it was inspired by firefighter training and research in other fields lessons in complex systems, reliability engineering.

**2006 – Google**

While at Google, Kripa Krishnan created a similar program to Amazon's Game day (see above) called "DiRT" (Disaster Recovery Testing). Jason Cahoon, a Site Reliability Engineer at Google, contributed a chapter on Google DiRT in the "Chaos Engineering" book and described the system at the GOTOpia 2021 conference.

**2011 – Netflix**

While overseeing Netflix's migration to the cloud in 2011 Nora Jones, Casey Rosenthal, and Greg Orzell expanded the discipline while working together at Netflix by setting up a tool that would cause breakdowns in their production environment, the environment used by Netflix customers. The intent was to move from a development model that assumed no breakdowns to a model where breakdowns were considered to be inevitable, driving developers to consider built-in resilience to be an obligation rather than an option:

> "At Netflix, our culture of freedom and responsibility led us not to force engineers to design their code in a specific way. Instead, we discovered that we could align our teams around the notion of infrastructure resilience by isolating the problems created by server neutralization and pushing them to the extreme. We have created Chaos Monkey, a program that randomly chooses a server and disables it during its usual hours of activity. Some will find that crazy, but we could not depend on the random occurrence of an event to test our behavior in the face of the very consequences of this event. Knowing that this would happen frequently has created a strong alignment among engineers to build redundancy and process automation to survive such incidents, without impacting the millions of Netflix users. Chaos Monkey is one of our most effective tools to improve the quality of our services."

By regularly "killing" random instances of a software service, it was possible to test a redundant architecture to verify that a server failure did not noticeably impact customers.

The concept of chaos engineering is close to the one of Phoenix Servers, first introduced by Martin Fowler in 2012.

## Chaos engineering tools

### Chaos Monkey

**Chaos Monkey** is a tool invented in 2011 by Netflix to test the resilience of its IT infrastructure. It works by intentionally disabling computers in Netflix's production network to test how the remaining systems respond to the outage. Chaos Monkey is now part of a larger suite of tools called the Simian Army designed to simulate and test responses to various system failures and edge cases.

The code behind Chaos Monkey was released by Netflix in 2012 under an Apache 2.0 license.

The name "Chaos Monkey" is explained in the book *Chaos Monkeys* by Antonio Garcia Martinez:

> Imagine a monkey entering a 'data center', these 'farms' of servers that host all the critical functions of our online activities. The monkey randomly rips cables, destroys devices and returns everything that passes by the hand [i.e. flings excrement]. The challenge for IT managers is to design the information system they are responsible for so that it can work despite these monkeys, which no one ever knows when they arrive and what they will destroy.

#### Simian Army

The Simian Army is a suite of tools developed by Netflix to test the reliability, security, or resilience of its Amazon Web Services infrastructure and includes the following tools:

- At the very top of the Simian Army hierarchy, Chaos Kong drops a full AWS "Region". Though rare, loss of an entire region does happen and Chaos Kong simulates a systems response and recovery to this type of event.
- Chaos Gorilla drops a full Amazon "Availability Zone" (one or more entire data centers serving a geographical region).

### Other

Voyages-sncf.com's 2017 "Day of Chaos" gamified simulating pre-production failures to present at the 2017 DevOps REX conference. Founded in 2019, Steadybit popularized pre-production chaos and reliability engineering. Its open-source Reliability Hub extends Steadybit.

Proofdock can inject infrastructure, platform, and application failures on Microsoft Azure DevOps. Gremlin is a "failure-as-a-service" platform. Facebook's Project Storm simulates datacenter failures for natural disaster resistance.
