---
title: "User behavior analytics"
source: https://en.wikipedia.org/wiki/User_behavior_analytics
domain: insider-threat
license: CC-BY-SA-4.0
tags: insider threat program, user behavior analytics, least privilege enforcement, separation of duties, data exfiltration monitoring
fetched: 2026-07-02
---

# User behavior analytics

**User behavior analytics** (**UBA**) or **user and entity behavior analytics** (**UEBA**), is the concept of analyzing the behavior of users, subjects, visitors, etc. for a specific purpose. It allows cybersecurity tools to build a profile of each individual's normal activity, by looking at patterns of human behavior, and then highlighting deviations from that profile (or anomalies) that may indicate a potential compromise.

## Purpose of UBA

The reason for using UBA, according to Johna Till Johnson from Nemertes Research, is that "security systems provide so much information that it is tough to uncover information that truly indicates a potential for a real attack. Analytics tools help make sense of the vast amount of data that SIEM, IDS/IPS, system logs, and other tools gather. UBA tools use a specialized type of security analytics that focuses on the behavior of systems and the people using them. UBA technology first evolved in the field of marketing, to help companies understand and predict consumer-buying patterns. But as it turns out, UBA can be extraordinarily useful in the security context too."

## Distinction between UBA and UEBA

The E in UEBA extends the analysis to include entity activities that take place but that are not necessarily directly linked or tied to a user's specific actions but that can still correlate to a vulnerability, reconnaissance, intrusion breach or exploit occurrence.

The term "UEBA" was coined by Gartner in 2015. UEBA tracks the activity of devices, applications, servers and data. UEBA systems produce more data and provide more complex reporting options than UBA systems.

## Difference with EDR

UEBA tools differ from endpoint detection and response (EDR) capabilities in that UEBA is an analytic focus on the user behavior whereas EDR has an analytic focus on the endpoint. Cybersecurity solutions, like EDR and XDR, typically prioritize detection and response to external threats once an incident has occurred. EUBA and IRM solutions are looking for prevent potential risks internally by analyzing employee behavior.

## Continuous Authentication in User Behavior Analytics

Continuous authentication has been proposed as a form of user behavior analytics in which a system verifies identity throughout an active session rather than only at login. By monitoring behavior during use, this approach reduces the risk of system abuse after initial access is granted. Research in this area has examined signals such as mouse movements, keystroke timing, network activity, and application usage patterns. These signals can form computer-usage profiles that remain consistent over long periods and differ across individuals, allowing machine-learning models to flag behavior that deviates from the user's typical patterns. Such systems may also use machine-learning models and anomaly detection to identify suspicious sessions based on deviations from ordinary interaction patterns.

Machine-learning systems for continuous authentication typically rely on long-term data because everyday behavior drifts across hours, days, or weeks. Models must account for changes caused by fatigue, workload, or environmental context. This is why researchers distinguish offline evaluations, where models are tested on pre-collected datasets, from online evaluations, which observe behavior in real time and capture day-to-day variability. Continuous authentication is usually considered in environments where some degree of monitoring is already expected and where the expectation of privacy is lower, such as corporate settings.

The same study also examined the temporal structure of computer-usage behavior. Using surrogate-data analysis, Giovanini et al. found strong 24-hour cycles in most users' activity patterns, indicating that daily routines shape usage profiles in a measurable way and that these profiles contain both time-dependent structure and random variation. This has led researchers to suggest that separating periodic patterns from background system processes may help improve model stability. At the same time, many existing evaluations rely on relatively small samples and only one device per user, and more recent work highlights the need for larger, more diverse datasets to understand long-term behavioral change and to properly assess the robustness of continuous-authentication techniques.

Follow-up work in this space has noted that not all features used in continuous authentication necessarily reflect human behavior directly. In systems that collect data on running processes, contacted domains, keystroke timing, mouse movement, and web activity, many of the strongest predictive features come from network and application usage patterns rather than from human-generated motion. These characteristics often reflect device configuration or network environment and can sometimes cause models to distinguish devices rather than users. This concern has been emphasized in recent studies on device bias, which show that authentication models may unintentionally learn hardware- or sensor-specific characteristics rather than behavioral traits. Because such environmental and device-linked features may appear distinctive only within a specific setting, researchers commonly emphasize the importance of incorporating human-driven behavioral signals, such as keystroke timing or mouse movement, and of using datasets that include multiple devices per user and longer real-world observation periods.
