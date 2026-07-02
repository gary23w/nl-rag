---
title: "Suricata (software)"
source: https://en.wikipedia.org/wiki/Suricata_(software)
domain: suricata-ids
license: CC-BY-SA-4.0
tags: suricata ids, network intrusion detection, deep packet inspection, intrusion prevention system, packet capture analysis
fetched: 2026-07-02
---

# Suricata (software)

**Suricata** is an open-source network analysis and threat detection software. The features include intrusion detection system (IDS) and intrusion prevention system (IPS) as well as network transaction logging and file extraction. It was developed by the Open Information Security Foundation (OISF). The first standard release was in July 2010.

## Features

### IDS and IPS

Suricata provides threat detection capabilities. In IDS mode, it is going to analyse the traffic and generate an alert when a signature matches.

In IPS mode, it acts like a firewall. It provides traffic filtering and monitoring and allows network administrators to write and enforce detection rules.

Suricata is able to detect common attack vectors such as port scanning, denial-of-service, pass-the-hash, and brute-force attacks.

### Network monitoring

Suricata can be used to monitor network traffic in real time. It can log various types of network transactions, including HTTP, DNS, SMB and TLS sessions.

### File extraction

Suricata can extract files from network traffic to disk for further analysis. It supports extraction over protocols such as FTP, HTTP, SMTP and SMB. It can also perform file type identification or hash computation of the files seen on the network without extracting them to disk.

### PCAP logging

Suricata can log network traffic in PCAP format for later analysis with tools such as Wireshark. It also supports conditional pcap logging where only the traffic of flow where a rule matched is logged.

### Event Format

Suricata logs events in the JSON format, which can be easily parsed and analyzed by other tools.

## Release cycle

Typically, a major update of Suricata is released every 2 years.

## Ruleset

Suricata uses a ruleset to perform detection and threat analysis. This ruleset is composed of signatures that define which behaviors on the network should trigger an alert event. The ruleset is usually constituted of signatures of various severity. Some are designed to alert on Common Vulnerabilities and Exposures exploitation and some are just there to select interesting events (like a software update) that could be meaningful during an investigation.
