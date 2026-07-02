---
title: "Computer security incident management"
source: https://en.wikipedia.org/wiki/Computer_security_incident_management
domain: incident-response
license: CC-BY-SA-4.0
tags: incident response, computer security incident, computer emergency response team, business continuity planning, root cause analysis
fetched: 2026-07-02
---

# Computer security incident management

In the fields of computer security and information technology, **computer security incident management** involves the monitoring and detection of security events on a computer or computer network, and the execution of proper responses to those events. Computer security incident management is a specialized form of incident management, the primary purpose of which is the development of a well understood and predictable response to damaging events and computer intrusions.

Incident management requires a process and a response team which follows this process. In the United States, This definition of computer security incident management follows the standards and definitions described in the National Incident Management System (NIMS). The incident coordinator manages the response to an emergency security incident. In a Natural Disaster or other event requiring response from Emergency services, the incident coordinator would act as a liaison to the emergency services incident manager.

## Incident response plans

An incident response plan (IRP) is a group of policies that dictate an organizations reaction to a cyber attack. Once a security breach has been identified, for example by network intrusion detection system (NIDS) or host-based intrusion detection system (HIDS) (if configured to do so), the plan is initiated. It is important to note that there can be legal implications to a data breach. Knowing local and federal laws is critical. Every plan is unique to the needs of the organization, and it can involve skill sets that are not part of an IT team. For example, a lawyer may be included in the response plan to help navigate legal implications to a data breach.

As mentioned above every plan is unique but most plans will include the following:

### Preparation

Good preparation includes the development of an incident response team (IRT). Skills need to be used by the IRT would be, penetration testing, computer forensics, network security, etc. The IRT should also keep track of trends in cybersecurity and modern attack strategies. A training program for end users is important as well as most modern attack strategies target users on the network.

As part of the preparation phase in incident response a plan should be developed and address the following:

- Roles and Responsibilities
- Lists the IRT members and their duties
- Communication protocols
- Training and awareness
- Logging policies and configurations
- Event status definitions and thresholds
- Playbooks and runbooks for common incident types
- Legal and compliance considerations

### Identification

This part of the incident response plan identifies if there was a security event. When an end user reports information or an admin notices irregularities, an investigation is launched. An incident log is a crucial part of this step. All of the members of the team should be updating this log to ensure that information flows as fast as possible. If it has been identified that a security breach has occurred the next step should be activated.

### Containment

In this phase, the IRT works to isolate the areas that the breach took place to limit the scope of the security event. During this phase it is important to preserve information forensically so it can be analyzed later in the process. Containment could be as simple as physically containing a server room or as complex as segmenting a network to not allow the spread of a virus.

### Eradication

This is where the threat that was identified is removed from the affected systems. This could include deleting malicious files, terminating compromised accounts, or deleting other components. Some events do not require this step, however it is important to fully understand the event before moving to this step. This will help to ensure that the threat is completely removed.

### Recovery

This stage is where the systems are restored back to original operation. In complex incidents such as ransomware attacks, recovery efforts may involve not only restoring data but also reconstructing compromised systems and performing forensic analysis to ensure the integrity of recovered information. This stage could include the recovery of data, changing user access information, or updating firewall rules or policies to prevent a breach in the future. Without executing this step, the system could still be vulnerable to future security threats.

### Lessons learned

In this step information that has been gathered during this process is used to make future decisions on security. This step is crucial to the ensure that future events are prevented. Using this information to further train admins is critical to the process. This step can also be used to process information that is distributed from other entities who have experienced a security event.

## Sector-specific requirements

Incident response requirements vary by industry. In the United States healthcare sector, the Health Insurance Portability and Accountability Act (HIPAA) Security Rule requires covered entities to implement security incident procedures, including mechanisms to identify and respond to suspected or known security incidents and to mitigate harmful effects. A December 2024 Notice of Proposed Rulemaking would strengthen these requirements by mandating written incident response plans, requiring restoration of critical systems within 72 hours of an incident, and requiring regular testing and revision of contingency plans. The 2024 Change Healthcare cyberattack, which disrupted claims processing for healthcare providers across the United States for several weeks, highlighted the importance of robust incident response planning in the healthcare sector.
