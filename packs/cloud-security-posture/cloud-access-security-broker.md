---
title: "Cloud access security broker"
source: https://en.wikipedia.org/wiki/Cloud_access_security_broker
domain: cloud-security-posture
license: CC-BY-SA-4.0
tags: cloud computing security, cloud access security broker, infrastructure as code, cloud workload protection, shared responsibility model
fetched: 2026-07-02
---

# Cloud access security broker

A **cloud access security broker** (**CASB**) (sometimes pronounced cas-bee) is on-premises or cloud based software that sits between cloud service users and cloud applications, and monitors all activity and enforces security policies. A CASB can offer services such as monitoring user activity, warning administrators about potentially hazardous actions, enforcing security policy compliance, and automatically preventing malware.

## Definition

First defined in 2012 by Gartner, a cloud access security broker (CASB) is defined as:

> [An] on-premises, or cloud-based security policy enforcement points, placed between cloud service consumers and cloud service providers to combine and interject enterprise security policies as the cloud-based resources are accessed. CASBs consolidate multiple types of security policy enforcement. Example security policies include authentication, single sign-on, authorization, credential mapping, device profiling, encryption, tokenization, logging, alerting, malware detection/prevention and so on.

## Types

CASBs deliver security and management features. Broadly speaking, "security" is the prevention of high-risk events, whilst "management" is the monitoring and mitigation of high-risk events.

CASBs that deliver security must be in the path of data access, between the user and the cloud provider. Architecturally, this might be achieved with proxy agents on each end-point device, or in agentless fashion without configuration on each device. Agentless CASBs allow for rapid deployment and deliver security on both company-managed and unmanaged BYOD devices. Agentless CASB also respect user privacy, inspecting only corporate data. Agent-based CASBs are difficult to deploy and effective only on devices that are managed by the corporation. Agent-based CASBs typically inspect both corporate and personal data.
