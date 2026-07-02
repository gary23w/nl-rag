---
title: "Watermark (data synchronization)"
source: https://en.wikipedia.org/wiki/Watermark_(data_synchronization)
domain: gcp-dataflow
license: CC-BY-SA-4.0
tags: gcp cloud dataflow, stream batch processing gcp, apache beam runner, data pipeline google
fetched: 2026-07-02
---

# Watermark (data synchronization)

A **Watermark** for data synchronization describes an object of a predefined format which provides a point of reference value for two systems/datasets attempting to establish delta/incremental synchronization; any object in the queried data source which was created, modified, or deleted after the watermark's value will be qualified as "above watermark" and should be returned to the client requesting data.

This approach allows the client to retrieve only the objects which have changed since the latest watermark, and also enables the client to resume its synchronization job from where it left off in the event of some pause or downtime.

## Methodology

**Watermark** term is often used in Directory Synchronization software development projects. For example, products such as Microsoft Exchange Server, Active Directory, Active Directory Application Mode (ADAM), and Microsoft Identity Integration Server 2003/ Microsoft Identity Lifecycle Manager Server 2007, as well as Cisco Unified Communications Manager or Sun Microsystems IPlanet and other LDAP-based directory products are using DirSync and consequently will consume "watermark" object to provide efficient synchronization between directories. Watermark object sometimes can be referred as "cookie". DirSync control implementation can differ from product to product, however concept of watermark will allow any product to read changes in the directory incrementally.

> The DirSync control is a Lightweight Directory Access Protocol (LDAP) server extension that enables a program to search an Active Directory partition for objects that have changed. When a program performs a DirSync search, the program creates a cookie that identifies the directory state at the time of an earlier DirSync query. With the first search, the program creates an empty cookie and Active Directory returns all objects that satisfy the query. Active Directory also returns an updated cookie that can be passed to the next search to obtain changes that are made since the first search. This process is repeated for each search.

— MSDN, from "How to poll for object attribute changes in Active Directory on Windows 2000 and Windows Server 2003" May 23, 2007
