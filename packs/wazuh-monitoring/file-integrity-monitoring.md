---
title: "File integrity monitoring"
source: https://en.wikipedia.org/wiki/File_integrity_monitoring
domain: wazuh-monitoring
license: CC-BY-SA-4.0
tags: wazuh monitoring, host intrusion detection, file integrity monitoring, security log management, endpoint security agent
fetched: 2026-07-02
---

# File integrity monitoring

**File integrity monitoring (FIM)** is an internal control or process that performs the act of validating the integrity of operating system and application software files using a verification method between the current file state and a known, good baseline. This comparison method often involves calculating a known cryptographic checksum of the file's original baseline and comparing with the calculated checksum of the current state of the file. Other file attributes can also be used to monitor integrity.

Generally, the act of performing file integrity monitoring is automated using internal controls such as an application or process. Such monitoring can be performed randomly, at a defined polling interval, or in real-time.

## Security objectives

Changes to configurations, files and file attributes across the IT infrastructure are common, but hidden within a large volume of daily changes can be the few that impact file or configuration integrity. These changes can also reduce security posture and in some cases may be leading indicators of a breach in progress. Values monitored for unexpected changes to files or configuration items include:

- Credentials
- Privileges and security settings
- Content
- Core attributes and size
- Hash values
- Configuration values

## Compliance objectives

Multiple compliance objectives indicate file integrity monitoring as a requirement. Several examples of compliance objectives with the requirement for file integrity monitoring include:

- PCI DSS - Payment Card Industry Data Security Standard (Requirement 11.5)
- SOX - Sarbanes-Oxley Act (Section 404)
- NERC CIP - NERC CIP Standard (CIP-010-2)
- FISMA - Federal Information Security Management Act (NIST SP800-53 Rev3)
- HIPAA - Health Insurance Portability and Accountability Act of 1996 (NIST Publication 800-66)
- SANS Critical Security Controls (Control 3)
