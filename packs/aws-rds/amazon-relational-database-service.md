---
title: "Amazon Relational Database Service"
source: https://en.wikipedia.org/wiki/Amazon_Relational_Database_Service
domain: aws-rds
license: CC-BY-SA-4.0
tags: aws rds, relational database service, managed database, cloud database
fetched: 2026-07-02
---

# Amazon Relational Database Service

**Amazon Relational Database Service** (or **Amazon RDS**) is a distributed relational database service by Amazon Web Services (AWS). It is a web service running "in the cloud" designed to simplify the setup, operation, and scaling of a relational database for use in applications. Administration processes like patching the database software, backing up databases and enabling point-in-time recovery are managed automatically. Scaling storage and compute resources can be performed by a single API call to the AWS control plane on-demand. AWS does not offer an SSH connection to the underlying virtual machine as part of the managed service.

## History

Amazon RDS was first released on 26 October 2009, supporting MySQL databases. This was followed by support for Oracle Database in June 2011, Microsoft SQL Server in May 2012, PostgreSQL in November 2013, and MariaDB (a fork of MySQL) in October 2015, and an additional 80 features during 2017.

In November 2014 AWS announced Amazon Aurora, a MySQL-compatible database offering enhanced high availability and performance, and in October 2017 a PostgreSQL-compatible database offering was launched.

In March 2019 AWS announced support of PostgreSQL 11 in RDS, five months after official release.

## Features

New database instances can be launched from the AWS Management Console or using the Amazon RDS APIs. Amazon RDS offers different features to support different use cases. Some of the major features are:

### Multi-Availability Zone (AZ) deployment

In May 2010 Amazon announced Multi-Availability Zone deployment support. Amazon RDS Multi-Availability Zone (AZ) allows users to automatically provision and maintain a synchronous physical or logical "standby" replica, depending on database engine, in a different Availability Zone (independent infrastructure in a physically separate location). Multi-AZ database instance can be developed at creation time or modified to run as a Multi-AZ deployment later. Multi-AZ deployments aim to provide enhanced availability and data durability for MySQL, MariaDB, Oracle, PostgreSQL and SQL Server instances and are targeted for production environments. In the event of planned database maintenance or unplanned service disruption, Amazon RDS automatically fails over to the up-to-date standby, allowing database operations to resume without administrative intervention.

Multi-AZ RDS instances are optional and have a cost associated with them. When creating a RDS instance, the user is asked if they would like to use a Multi-AZ RDS instance. In Multi-AZ RDS deployments backups are done in the standby instance so I/O activity is not suspended any time but users may experience elevated latencies for a few minutes during backups.

### Read replicas

Read replicas allow different use cases such as to scale in for read-heavy database workloads. There are up to five replicas available for MySQL, MariaDB, and PostgreSQL. Instances use the native, asynchronous replication functionality of their respective database engines. They have no backups configured by default and are accessible and can be used for read scaling. MySQL and MariaDB read replicas can be made writeable again since October 2012; PostgreSQL read replicas do not support it. Replicas are done at database instance level and do not support replication at database or table level.

### Performance metrics and monitoring

Performance metrics for Amazon RDS are available from the AWS Management Console or the Amazon CloudWatch API. In December 2015, Amazon announced an optional enhanced monitoring feature that provides an expanded set of metrics for the MySQL, MariaDB, and Aurora database engines.

### RDS costs

Amazon RDS instances are priced very similarly to Amazon Elastic Compute Cloud (EC2). RDS is charged per hour and comes in two packages: On-Demand DB Instances and Reserved DB Instances. On-Demand Instances are at an ongoing hourly usage rate. Reserved RDS Instances are offered in 1-year and 3-year terms and include no-upfront, partial-upfront, and all-upfront payment options. Currently, AWS does not offer a 3-year reservation with an "no-upfront" payment option.

Apart from the hourly cost of running the RDS instance, users are charged for the amount of storage provisioned, data transfers and input and output operations performed. AWS have introduced Provisioned Input and Output Operations, in which the user can define how many IO per second are required by their application. IOPS can contribute significantly to the total cost of running the RDS instance.

Amazon RDS also has an Aurora Serverless option. The serverless pricing unit is dollars per ACU hour. ACU stands for 'Aurora Capacity Unit'. This option is designed for customers that need to dramatically scale workloads.

As part of the AWS Free Tier, the Amazon RDS Free Tier helps new AWS customers get started with a managed database service in the cloud for free. You can use the Amazon RDS Free Tier to develop new applications, test existing applications, or simply gain hands-on experience with Amazon RDS.

### Automatic backups

Amazon RDS creates and saves automated backups of RDS DB instances. The first snapshot of a DB instance contains the data for the full DB instance and subsequent snapshots are incremental, maximum retention period is 35 days. In Multi-AZ RDS deployments backups are done in the standby instance so I/O activity is not suspended for any amount of time but you may experience elevated latencies for a few minutes during backups.

### Operation

Database instances can be managed from the AWS Management Console, using the Amazon RDS APIs and using AWS CLI. Since 1 June 2017, you can stop AWS RDS instances from AWS Management Console or AWS CLI for 7 days at a time. After 7 days, it will be automatically started, and since September 2018 RDS instances can be protected from accidental deletion. Increase DB space is supported, but not decrease allocated space. Additionally there is at least a six-hour period where new allocation cannot be done.

## Database instance types

As of August 2020, Amazon RDS supports 82 DB instance types - to support different types of workloads:

- General Purpose: 31 instances
- Memory Optimized: 33 instances
- Previous Generation: 18 instances

### General purpose

| Instance type | Memory | EBS optimized / throughput | Cores | Network performance |
|---|---|---|---|---|
| db.t2.micro | 1 GB | —N/a | 1 cores | Low to moderate |
| db.t2.small | 2 GB | —N/a | 1 cores | Low to moderate |
| db.t2.medium | 4 GB | —N/a | 2 cores | Low to moderate |
| db.t2.large | 8 GB | —N/a | 2 cores | Low to moderate |
| db.t2.xlarge | 16 GB | —N/a | 4 cores | Moderate |
| db.t2.2xlarge | 32 GB | —N/a | 8 cores | Moderate |
| db.t3.micro | 1 GB | —N/a | 2 cores | Up to 5 Gbps |
| db.t3.small | 2 GB | —N/a | 2 cores | Up to 5 Gbps |
| db.t3.medium | 4 GB | —N/a | 2 cores | Up to 5 Gbps |
| db.t3.large | 8 GB | —N/a | 2 cores | Up to 5 Gbps |
| db.t3.xlarge | 16 GB | —N/a | 4 cores | Up to 5 Gbps |
| db.t3.2xlarge | 32 GB | —N/a | 8 cores | Up to 5 Gbps |
| db.m4.large | 8 GB | 450 Mbit/s | 2 cores | Moderate |
| db.m4.xlarge | 16 GB | 750 Mbit/s | 4 cores | High |
| db.m4.2xlarge | 32 GB | 1000 Mbit/s | 8 cores | High |
| db.m4.4xlarge | 64 GB | 2000 Mbit/s | 16 cores | High |
| db.m4.10xlarge | 160 GB | 4000 Mbit/s | 40 cores | 10 Gigabit |
| db.m4.16xlarge | 256 GB | 10000 Mbit/s | 64 cores | 25 Gigabit |
| db.m5.large | 8 GB | up to 3500 Mbit/s | 2 cores | Up to 10 Gbps |
| db.m5.xlarge | 16 GB | up to 3500 Mbit/s | 4 cores | Up to 10 Gbps |
| db.m5.2xlarge | 32 GB | up to 3500 Mbit/s | 8 cores | Up to 10 Gbps |
| db.m5.4xlarge | 64 GB | 3500 Mbit/s | 16 cores | Up to 10 Gbps |
| db.m5.12xlarge | 192 GB | 7000 Mbit/s | 48 cores | 10 Gigabit |
| db.m5.24xlarge | 384 GB | 14000 Mbit/s | 96 cores | 25 Gigabit |
| db.m6g.large | 8 GB | Up to 4750 Mbit/s | 2 cores | Up to 10 Gbps |
| db.m6g.xlarge | 16 GB | Up to 4750 Mbit/s | 4 cores | Up to 10 Gbps |
| db.m6g.2xlarge | 32 GB | Up to 4750 Mbit/s | 8 cores | Up to 10 Gbps |
| db.m6g.4xlarge | 64 GB | 4750 Mbit/s | 16 cores | Up to 10 Gbps |
| db.m6g.8xlarge | 128 GB | 9000 Mbit/s | 32 cores | 12 Gbps |
| db.m6g.12xlarge | 192 GB | 13500 Mbit/s | 48 cores | 20 Gbps |
| db.m6g.16xlarge | 256 GB | 19000 Mbit/s | 64 cores | 25 Gbps |

### Memory optimized

| Instance type | Memory | EBS optimized / throughput | Cores | Network performance |
|---|---|---|---|---|
| db.r4.large | 15.25 GB | 437 Mbit/s | 2 cores | Up to 10 Gbps |
| db.r4.xlarge | 30.5 GB | 875 Mbit/s | 4 cores | Up to 10 Gbps |
| db.r4.2xlarge | 61 GB | 1750 Mbit/s | 8 cores | Up to 10 Gbps |
| db.r4.4xlarge | 122 GB | 3500 Mbit/s | 16 cores | Up to 10 Gbps |
| db.r4.8xlarge | 244 GB | 7000 Mbit/s | 32 cores | 10 Gbps |
| db.r4.16xlarge | 488 GB | 14000 Mbit/s | 64 cores | 25 Gbps |
| db.r5.large | 16 GB | up to 3500 Mbit/s | 2 cores | Up to 10 Gbps |
| db.r5.xlarge | 32 GB | up to 3500 Mbit/s | 4 cores | Up to 10 Gbps |
| db.r5.2xlarge | 64 GB | up to 3500 Mbit/s | 8 cores | Up to 10 Gbps |
| db.r5.4xlarge | 128 GB | 3500 Mbit/s | 16 cores | Up to 10 Gbps |
| db.r5.12xlarge | 384 GB | 7000 Mbit/s | 48 cores | 10 Gbps |
| db.r5.24xlarge | 768 GB | 14000 Mbit/s | 96 cores | 25 Gbps |
| db.r6g.large | 16 GB | up to 4750 Mbit/s | 2 cores | Up to 10 Gbps |
| db.r6g.xlarge | 32 GB | up to 4750 Mbit/s | 4 cores | Up to 10 Gbps |
| db.r6g.2xlarge | 64 GB | up to 4750 Mbit/s | 8 cores | Up to 10 Gbps |
| db.r6g.4xlarge | 128 GB | 4750 Mbit/s | 16 cores | Up to 10 Gbps |
| db.r6g.8xlarge | 256 GB | 9000 Mbit/s | 32 cores | 12 Gbps |
| db.r6g.12xlarge | 384 GB | 13500 Mbit/s | 48 cores | 20 Gbps |
| db.r6g.16xlarge | 512 GB | 19000 Mbit/s | 64 cores | 25 Gbps |
| db.x1e.xlarge | 122 GB | 500 Mbit/s | 4 cores | Up to 10 Gbps |
| db.x1e.2xlarge | 244 GB | 1000 Mbit/s | 8 cores | Up to 10 Gbps |
| db.x1e.4xlarge | 488 GB | 1750 Mbit/s | 16 cores | Up to 10 Gbps |
| db.x1e.8xlarge | 976 GB | 3500 Mbit/s | 32 cores | Up to 10 Gbps |
| db.x1e.16xlarge | 1952 GB | 7000 Mbit/s | 64 cores | 10 Gbps |
| db.x1e.32xlarge | 3904 GB | 14000 Mbit/s | 128 cores | 25 Gbps |
| db.x1.16xlarge | 976 GB | 7000 Mbit/s | 64 cores | 10 Gbps |
| db.x1.32xlarge | 1952 GB | 14000 Mbit/s | 128 cores | 25 Gbps |
| db.z1d.large | 16 GB | —N/a | 1 cores | Up to 10 Gbps |
| db.z1d.xlarge | 32 GB | —N/a | 2 cores | Up to 10 Gbps |
| db.z1d.2xlarge | 64 GB | —N/a | 4 cores | Up to 10 Gbps |
| db.z1d.3xlarge | 96 GB | —N/a | 6 cores | Up to 10 Gbps |
| db.z1d.6xlarge | 192 GB | —N/a | 12 cores | 10 Gbps |
| db.z1d.12xlarge | 384 GB | —N/a | 48 cores | 25 Gbps |

### Previous generation

| Instance Type | Memory | EBS optimized / throughput | Cores | Network performance |
|---|---|---|---|---|
| db.t1.micro | 0.613 GB | —N/a | 1 cores | Very low |
| db.m1.small | 1.7 GB | —N/a | 1 cores | Low |
| db.m1.medium | 3.75 GB | —N/a | 1 cores | Moderate |
| db.m1.large | 7.5 GB | —N/a | 2 cores | Moderate |
| db.m1.xlarge | 15 GB | —N/a | 4 cores | High |
| db.m2.xlarge | 17.1 GB | —N/a | 2 cores | Moderate |
| db.m2.2xlarge | 34.2 GB | —N/a | 4 cores | Moderate |
| db.m2.4xlarge | 68.4 GB | —N/a | 8 cores | High |
| db.m3.medium | 3.75 GB | —N/a | 1 cores | Moderate |
| db.m3.large | 7.5 GB | —N/a | 2 cores | Moderate |
| db.m3.xlarge | 15 GB | 500 Mbit/s | 4 cores | High |
| db.m3.2xlarge | 30 GB | 10000 Mbit/s | 8 cores | High |
| db.cr1.8xl | 244 GB | —N/a | 32 cores | 10 Gigabit |
| db.r3.large | 15.25 GB | —N/a | 2 cores | Moderate |
| db.r3.xlarge | 30.5 GB | —N/a | 4 cores | Moderate |
| db.r3.2xlarge | 61 GB | —N/a | 8 cores | High |
| db.r3.4xlarge | 122 GB | —N/a | 16 cores | High |
| db.r3.8xlarge | 244 GB | —N/a | 32 cores | 10 Gigabit |
