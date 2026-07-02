---
title: "Zero-touch provisioning"
source: https://en.wikipedia.org/wiki/Zero-touch_provisioning
domain: network-automation
license: CC-BY-SA-4.0
tags: network automation, zero touch provisioning, config management, net devops
fetched: 2026-07-02
---

# Zero-touch provisioning

**Zero-touch provisioning** (**ZTP**), or **zero-touch enrollment**, is the process of remotely provisioning large numbers of network devices such as switches, routers and mobile devices without having to manually program each one individually. The feature improves existing provisioning models, solutions and practices in the areas of wireless networks, (complex) network management and operations services, and cloud based infrastructure services provisioning.

ZTP saves configuration time while reducing errors. The process can also be used to update existing systems using scripts. Research has shown that ZTP systems allow for faster provisioning versus manual provisioning. The global market for ZTP services was estimated to be $2.1 Billion in 2021.

In April 2019, the Internet Engineering Task Force published RFC 8572 Secure Zero Touch Provisioning (SZTP) as a Proposed Standard.

The FIDO Alliance published FIDO Device Onboard version 1.0 in December 2020, and followed up with a FIDO Device Onboard version 1.1 in April 2022. Several FDO "app notes" augment this specification. FIDO Device Onboard is also a ZTP type protocol.

## Applications

One application of the technology is to improve delivery of cloud computing services. The concept has been particularly influential for information technology when paired with mobile device management. Repetitive processes that can be automated and streamlined include configuring settings; collecting inventory details; deploying apps; managing licenses; and implementing security policy, including password management and wiping remote devices.

## System architecture

A basic ZTP system requires a network device that supports ZTP, a server that supports Dynamic Host Configuration Protocol (DHCP) or Trivial File Transfer Protocol (TFTP), and a file server. When a ZTP-enabled device is powered on, the device's boot file sets up configuration parameters. A switch then sends a request using DHCP or TFTP to get the device's configuration file from a central location. The file then runs and configures ports, IP addresses and other server parameters for each location.

## Similar concepts

A similar concept is the zero-touch network, which integrates zero-touch provisioning with automation, artificial intelligence and machine learning.

## Standards activity

In December 2017, the European Telecommunications Standards Institute (ETSI) formed the Zero-touch network and Service Management group (ZSM) to accelerate development and standardization of the technology. In the summer of 2019, the group published a series of documents defining ZSM requirements, reference architecture and terminology.

In April 2019, the Internet Engineering Task Force published RFC 8572 Secure Zero Touch Provisioning (SZTP) as a Proposed Standard.
