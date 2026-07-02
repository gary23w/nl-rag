---
title: "Single point of failure"
source: https://en.wikipedia.org/wiki/Single_point_of_failure
domain: fault-tree-analysis
license: CC-BY-SA-4.0
tags: fault tree analysis, top event logic, event tree analysis, reliability block diagram
fetched: 2026-07-02
---

# Single point of failure

A **single point of failure** (**SPOF**) is a part of a system that would stop the entire system from working if it were to fail. The term single point of failure implies that there is no backup or redundant option that would enable the system to continue to function without it. SPOFs are undesirable in any system with a goal of high availability or reliability, be it a business practice, software application, or other industrial system. If there is a SPOF present in a system, it produces a potential interruption to the system that is substantially more disruptive than an error would be elsewhere in the system.

## Overview

Systems can be made robust by adding redundancy in all potential SPOFs. Redundancy can be achieved at various levels.

The assessment of a potential SPOF involves identifying the critical components of a complex system that would provoke a total systems failure in case of malfunction. Highly reliable systems should not rely on any such individual component.

For instance, the owner of a small tree care company may own only one woodchipper. If the chipper breaks, they may be unable to complete their current job and may have to cancel future jobs until they can obtain a replacement. The owner could prepare for this in multiple ways. The owner of the tree care company may have spare parts ready for the repair of the wood chipper, in case it fails. At a higher level, they may have a second wood chipper that they can bring to the job site. Finally, at the highest level, they may have enough equipment available to completely replace everything at the work site in the case of multiple failures.

- (Possible SPOFs in a simple setup) Possible SPOFs in a simple setup
- (Using redundancy to avoid some SPOFs) Using redundancy to avoid some SPOFs
- (Completely redundant system without SPOFs (note: assumes generator and grid sources are each rated at N, each UPS is rated at N, and "A/C" and "Electrical" are in and of themselves completely fault tolerant systems)) Completely redundant system without SPOFs (note: assumes generator and grid sources are each rated at N, each UPS is rated at N, and "A/C" and "Electrical" are in and of themselves completely fault tolerant systems)

## Computing

A fault-tolerant computer system can be achieved at the internal component level, at the system level (multiple machines), or site level (replication).

One would normally deploy a load balancer to ensure high availability for a server cluster at the system level. In a high-availability server cluster, each individual server may attain internal component redundancy by having multiple power supplies, hard drives, and other components. System-level redundancy could be obtained by having spare servers waiting to take on the work of another server if it fails.

Since a data center is often a support center for other operations, such as business logic, it represents a potential SPOF in itself. Thus, at the site level, the entire cluster may be replicated at another location, where it can be accessed in case the primary location becomes unavailable. This is typically addressed as part of an IT disaster recovery program. While previously the solution to this SPOF was physical duplication of clusters, the high demand for this duplication led multiple businesses to outsource duplication to 3rd parties using cloud computing. It has been argued by scholars, however, that doing so simply moves the SPOF and may even increase the likelihood of a failure or cyberattack.

Paul Baran and Donald Davies developed packet switching, a key part of "survivable communications networks". Such networks – including ARPANET and the Internet – are designed to have no single point of failure. Multiple paths between any two points on the network allow those points to continue communicating with each other, the packets "routing around" damage, even after any single failure of any one particular path or any one intermediate node.

### Software engineering

In software engineering, a **bottleneck** occurs when the capacity of an application or a computer system is limited by a single component. The bottleneck has the lowest throughput of all parts of the transaction path. A common example is when a used programming language is capable of parallel processing, but a given snippet of code has several independent processes run sequentially rather than simultaneously.

### Performance engineering

Tracking down bottlenecks (sometimes known as *hot spots* – sections of the code that execute most frequently – i.e., have the highest execution count) is called performance analysis. Reduction is usually achieved with the help of specialized tools, known as performance analyzers or profilers. The objective is to make those particular sections of code perform as fast as possible to improve overall algorithmic efficiency.

### Computer security

A vulnerability or security exploit in just one component can compromise an entire system. One of the largest concerns in computer security is attempting to eliminate SPOFs without sacrificing too much convenience to the user. With the invention and popularization of the Internet, several systems became connected to the broader world through many difficult-to-secure connections. While companies have developed a number of solutions to this, the most consistent form of SPOFs in complex systems tends to remain user error, either by accidental mishandling by an operator or outside interference through phishing attacks.

## Other fields

The concept of a single point of failure has also been applied to fields outside of engineering, computers, and networking, such as corporate supply chain management and transportation management.

Design structures that create single points of failure include bottlenecks and series circuits (in contrast to parallel circuits).

In transportation, some noted recent examples of the concept's application have included the Nipigon River Bridge in Canada, where a partial bridge failure in January 2016 entirely severed road traffic between Eastern Canada and Western Canada for several days because it is located along a portion of the Trans-Canada Highway where there is no alternate detour route for vehicles to take; and the Norwalk River Railroad Bridge in Norwalk, Connecticut, an aging swing bridge that sometimes gets stuck when opening or closing, disrupting rail traffic on the Northeast Corridor line.

The concept of a single point of failure has also been applied to the intelligence field, and the processes of intelligence. Edward Snowden talked of the dangers of being what he described as "the single point of failure" – the sole repository of information.

## Life-support systems

A component of a life-support system that would constitute a single point of failure would be required to be extremely reliable.
