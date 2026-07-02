---
title: "Amazon Neptune"
source: https://en.wikipedia.org/wiki/Amazon_Neptune
domain: aws-neptune
license: CC-BY-SA-4.0
tags: aws neptune, amazon neptune, managed graph database, knowledge graph service
fetched: 2026-07-02
---

# Amazon Neptune

**Amazon Neptune** is a managed graph database product published by Amazon.com. It is used as a web service and is part of Amazon Web Services (AWS). It was announced on November 29, 2017. Amazon Neptune supports popular graph models property graph and W3C's RDF, and their respective query languages Apache TinkerPop's Gremlin, openCypher, and SPARQL, including other Amazon Web Services products.

Amazon Neptune general availability (GA) was announced on May 30, 2018 and is currently available in 22 AWS regions. Neptune is HIPAA eligible. On December 12, 2018, it was announced that Amazon Neptune was in-scope for Payment Card Industry Data Security Standard, and ISO compliance programs.

## History

Amazon Neptune is based on Blazegraph. Amazon acquired the Blazegraph developers and the Blazegraph open source development was essentially stopped in April 2018.

| Release | Change | Date |
|---|---|---|
| 1.0.2.2 | Engine version 1.0.2.2 | March 9, 2020 |
| 1.0.2.1 | Engine version 1.0.2.1.R4 | December 20, 2019 |
| 1.0.2.1 | Engine version 1.0.2.1.R3 | December 12, 2019 |
| 1.0.2.1 | Engine version 1.0.2.1.R2 | November 23, 2019 |
| 1.0.2.0 | Engine version 1.0.2.0.R2 | November 8, 2019 |
| 1.0.1.0 | Engine version 1.0.1.0.200502.0 | October 31, 2019 |
| 1.0.1.0 | Engine version 1.0.1.0.200463.0 | October 15, 2019 |
| 1.0.1.0 | Engine version 1.0.1.0.200457.0 | September 19, 2019 |
| 1.0.1.0 | Engine version 1.0.1.0.200369.0 | August 13, 2019 |
| 1.0.1.0 | Engine version 1.0.1.0.200348.0 | July 2, 2019 |
| 1.0.1.0 | Engine version 1.0.1.0.200310.0 | June 12, 2019 |
| 1.0.1.0 | Engine version 1.0.1.0.200296.0 | May 1, 2019 |
| 1.0.1.0 | Engine version 1.0.1.0.200267.0 | January 21, 2019 |
| 1.0.1.0 | Engine version 1.0.1.0.200264.0 | November 19, 2018 |
| 1.0.1.0 | Engine version 1.0.1.0.200258.0 | November 8, 2018 |
| 1.0.1.0 | Engine version 1.0.1.0.200255.0 | October 29, 2018 |
| 1.0.1.0 | Engine version 1.0.1.0.200237.0 | September 6, 2018 |
| 1.0.1.0 | Engine version 1.0.1.0.200236.0 | July 24, 2018 |
| 1.0.1.0 | Engine version 1.0.1.0.200233.0 | June 22, 2018 |
| 1.0.1.0 | Amazon Neptune initial release | May 30, 2018 |

## Features

### External support

Amazon Neptune supports the open source Apache TinkerPop Gremlin graph traversal language, openCypher query language for property graphs, and the W3C standard Resource Description Framework's (RDF) SPARQL query language. All three can be used on the same Neptune instance, and allows the user to build queries to navigate highly connected data sets and provides high performance for both graph models. Neptune also uses other AWS product features such as those of Amazon S3, Amazon EC2 and Amazon CloudWatch.

### Security

All Amazon Neptune database clusters are created and stored in an Amazon Virtual Private Cloud (VPC), which allows the user to isolate their database in their own private network. Using Neptune's VPC configuration, the user can configure firewall settings to their needs in order to control network access to database instances. Amazon Neptune is integrated with AWS Identity and Access Management (IAM), which allows the user to create AWS IAM groups and control the actions that the groups and other AWS IAM users can do. Neptune allows the user to encrypt databases using keys created through AWS Key Management Service (KMS). A database instance running with Neptune Encryption, encrypts all of the stored data, backups, snapshots and replicas in the same cluster. Amazon Neptune allows the user to use HTTPS to encrypt data during its transfer to and from clients or Neptune service endpoints using Transport Layer Security (TLS).

### Storage

The data is stored in a cluster volume, a virtual volume utilizing SSD drives. These sizes of these volumes are dynamic, they increase depending how much data is stored in the database, with a maximum of 64 TB. The Amazon Neptune SLA policy is designed to offer a monthly uptime percentage greater that of 99.9%, increasing database performance and availability by integrating the engine with a virtual storage based on SSD drives, that are specially made for database workloads. Neptune maintains copies of the user's data in multiple Availability Zones. In case of failures, Neptune automatically detects any failed segments in a disk volume and repairs them.

## Availability

Neptune is now generally available in the US East (N. Virginia), US East (Ohio), US West (Oregon), US West (N. California), Canada (Central), AWS GovCloud (US-West), AWS GovCloud (US-East), Europe (Ireland), Europe (London), Europe (Frankfurt), Europe (Stockholm), Europe (Paris), South America (São Paulo), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Asia Pacific (Mumbai), Asia Pacific (Seoul), Asia Pacific (Hong Kong), China (Ningxia), China (Beijing), Operated by NWCD, and Middle-East (Bahrain) AWS regions.

## Pricing

Pricing is determined by AWS regions, with each region having different prices for the available services.

On-Demand Instance Pricing lets the user pay only for what instance they use by the hour instead of a fixed sum. The price also differs depending on the instance class. Similarly, the user only pays for the storage consumed by the database, with no payments in advance. The price is based on the storage rate and I/O rate, which are billed in GB per month and per million request increments respectively. This pricing model is beneficial to short-term and small-scale projects and is available in all AWS regions. The price for backup storage is also billed in per GB-month increments albeit at different rates. Data Transfer is priced in per GB increments, the amount depends on whether the data is transferred in or out of Amazon Neptune and how much data is transferred per month (TB per Month).

## Application

On September 12, 2018, it was announced that Neptune achieved HIPAA eligibility enabling it to process data sets containing protected health information (PHI). On December 12, 2018, it was announced that Amazon Neptune was in-scope for Payment Card Industry Data Security Standard, ISO 9001, ISO 27001, ISO 27017, and ISO 27018 compliance programs. The user can use Amazon Neptune in applications that are subject to PCI compliance or require ISO certification. On May 17, 2019, it was announced that Neptune achieved SSAE 16 eligibility

Neptune powers graph use cases such as recommendation engines, fraud detection, knowledge graphs, drug discovery, network security, and social networking.

## Notable users

Some notable customers of Amazon Neptune include, Samsung Electronics, Pearson, Intuit, Siemens, AstraZeneca, FINRA, LifeOmic, Blackfynn, and Amazon Alexa
