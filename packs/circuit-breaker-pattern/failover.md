---
title: "Failover"
source: https://en.wikipedia.org/wiki/Failover
domain: circuit-breaker-pattern
license: CC-BY-SA-4.0
tags: circuit breaker pattern, fault tolerance resilience, cascading failure prevention, bulkhead isolation pattern
fetched: 2026-07-02
---

# Failover

**Failover** is switching to a redundant or standby computer server, system, hardware component or network upon the failure or abnormal termination of the previously active application, server, system, hardware component, or network in a computer network. Failover and switchover are essentially the same operation, except that failover is automatic and usually operates without warning, while switchover requires human intervention.

## History

The term "failover", although probably in use by engineers much earlier, can be found in a 1962 declassified NASA report. The term "switchover" can be found in the 1950s when describing '"Hot" and "Cold" Standby Systems', with the current meaning of immediate switchover to a running system (hot) and delayed switchover to a system that needs starting (cold). A conference proceedings from 1957 describes computer systems with both Emergency Switchover (i.e., failover) and Scheduled Failover (for maintenance).

## Failover

Systems designers usually provide failover capability in servers, systems or networks requiring high availability and a high degree of reliability.

At the server level, failover automation usually sends a heartbeat between two servers, either through the network or through a separate connection (for example, RS-232). In the most common design, as long as a regular "pulse" or heartbeat continues between the main server and the second server, the second server will not bring its systems online; however, a few systems actively use all servers and can failover their work to remaining servers after a failure. There may also be a third "spare parts" server that has running spare components for "hot" switching to prevent downtime. The second server takes over the work of the first as soon as it detects an alteration in the heartbeat of the first machine. Some systems have the ability to send a notification of failover.

Certain systems, intentionally, do not fail over entirely automatically, but require human intervention. This "automated with manual approval" configuration runs automatically once a human has approved the failover.

## Failback

**Failback** is the process of restoring a system, component, or service previously in a state of failure back to its original, working state, and having the standby system go from functioning back to standby.

## Usage

The use of virtualization software has allowed failover practices to become less reliant on physical hardware through the process referred to as migration in which a running virtual machine is moved from one physical host to another, with little or no disruption in service.

Failover and failback technology are also regularly used in the Microsoft SQL Server database, in which SQL Server Failover Cluster Instance (FCI) is installed and configured on top of the Windows Server Failover Cluster (WSFC). The SQL Server groups and resources running on WSFC can be manually failed over to the second node for any planned maintenance on the first node or automatically fail over to the second node in case of any issues on the first node. In the same way, a failback operation can be performed to the first node once the issue is resolved or maintenance is done on it.
