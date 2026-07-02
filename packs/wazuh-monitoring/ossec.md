---
title: "OSSEC"
source: https://en.wikipedia.org/wiki/OSSEC
domain: wazuh-monitoring
license: CC-BY-SA-4.0
tags: wazuh monitoring, host intrusion detection, file integrity monitoring, security log management, endpoint security agent
fetched: 2026-07-02
---

# OSSEC

**OSSEC (Open Source HIDS SECurity)** is a free, open-source host-based intrusion detection system (HIDS). It performs log analysis, integrity checking, Windows registry monitoring, rootkit detection, time-based alerting, and active response. It provides intrusion detection for most operating systems, including Linux, OpenBSD, FreeBSD, OS X, Solaris and Windows. OSSEC has a centralized, cross-platform architecture allowing multiple systems to be easily monitored and managed. OSSEC has a log analysis engine that is able to correlate and analyze logs from multiple devices and formats.

## History

In June 2008, the OSSEC project and all the copyrights owned by Daniel B. Cid, the project leader, were acquired by Third Brigade, Inc. They promised to continue to contribute to the open source community and to extend commercial support and training to the OSSEC open source community.

In May 2009, Trend Micro acquired Third Brigade and the OSSEC project, with promises to keep it open source and free.

In 2018, Trend released the domain name and source code to the OSSEC Foundation.

The OSSEC project is being developed and maintained by Atomicorp who stewards the free and open source version and also offers a commercial version.

## Characteristics

OSSEC consists of a main application, an agent, and a web interface.

- *Manager* (or server), which is required for distributed network or stand-alone installations.
- *Agent*, a small program installed on the systems to be monitored.
- *Agentless* mode, can be used to monitor firewalls, routers, and even Unix systems.

### Features

- Log based Intrusion Detection (LID): Actively monitors and analyzes data from multiple log data points in real-time.
- Rootkit and Malware Detection: Process and file level analysis to detect malicious applications and rootkits.
- Active Response: Respond to attacks and changes on the system in real time through multiple mechanisms including firewall policies, integration with 3rd parties such as CDN's and support portals, as well as self-healing actions.
- Compliance Auditing: Application and system level auditing for compliance with many common standards such as PCI-DSS, and CIS benchmarks.
- File Integrity Monitoring (FIM): For both files and windows registry settings in real time not only detects changes to the system, it also maintains a forensic copy of the data as it changes over time.
- System Inventory: Collects system information, such as installed software, hardware, utilization, network services, listeners and other information.
