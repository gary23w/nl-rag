---
title: "Policy-based management"
source: https://en.wikipedia.org/wiki/Policy-based_management
domain: admission-controllers
license: CC-BY-SA-4.0
tags: admission controller webhook, validating admission policy, mutating admission webhook, cluster request interception
fetched: 2026-07-02
---

# Policy-based management

**Policy-based management** is a technology that can simplify the complex task of managing networks and distributed systems. Under this paradigm, an administrator can manage different aspects of a network or distributed system in a flexible and simplified manner by deploying a set of policies that govern its behaviour. Policies are technology independent rules aiming to enhance the hard-coded functionality of managed devices by introducing interpreted logic that can be dynamically changed without modifying the underlying implementation. This allows for a certain degree of programmability without the need to interrupt the operation of either the managed system or of the management system itself. Policy-based management can increase significantly the self-managing aspects of any distributed system or network, leading to more autonomic behaviour demonstrated by Autonomic computing systems.

## Frameworks and languages

The most well known policy-based management architecture was specified jointly by the IETF and the DMTF. This consists of four main functional elements: the Policy Management Tool (PMT), Policy Repository, Policy Decision Point (PDP), and Policy Enforcement Point (PEP).

The PMT is used by an administrator to define or update the policies to be enforced in the managed network. Resulting policies are stored in a repository in a form that must correspond to an information model so as to ensure interoperability across products from different vendors. When new policies have been added in the repository, or existing ones have been changed, the PMT issues the relevant PDP with notifications, which in turn interprets the policies and communicates them to the PEP. The latter is a component that runs on a policy-aware node and can execute (enforce) the different policies. The components of the architecture can communicate with each other using a variety of protocols. The preferred choice for communicating policy decisions between a PDP and network devices (PEPs) is the Common Open Policy Service (COPS) or SNMP, and LDAP for the PMT/PDP–repository communication.

The simplest approach for policy specification is through a sequence of rules, in which each rule is the form of a simple condition-action pair. The IETF policy framework adopts this approach and considers policies as rules that specify actions to be performed in response to defined conditions:

```
       if <condition(s)> then <action(s)>
```

The conditional part of the rule can be a simple or compound expression specified in either conjunctive or disjunctive normal form. The action part of the rule can be a set of actions that must be executed when the conditions are true. The IETF does not define a specific language to express network policies but rather a generic object-oriented information model for representing policy information. This model is a generic one, specifying the structure of abstract policy classes by means of association, thus allowing vendors to implement their own set of conditions and actions to be used by the policy rules.

## Policy conflicts

As with any programmable system, a policy-driven one can suffer from inconsistencies incurred by contradicting rules governing its behaviour. These are known as policy conflicts and come about as a result of specification errors, omissions, or contradictory management operations and, in some cases, can have catastrophic effects on the operation of the managed system. They have also been described as being analogous to software bugs that occur when two or more policies are activated simultaneously enforcing contradictory management operations on the system.

### Classification of policy conflicts

Policy conflicts are broadly classified into domain-independent and application-specific, where the former, as the names suggest, are independent of the policy application, and the latter are bound by the constraints of the application domain. Example application domains that have been considered in the literature include quality of service (QoS) in IP networks, distributed systems, firewall security, and call control in telecommunication networks. Policy conflicts can also be classified according to the time-frame at which they can be detected: static conflicts can be detected through off-line analysis at policy specification time, whereas dynamic conflicts can only be detected when policies are enforced as they depend on the current state of the managed system. For example, conflicts can occur between policies for dynamically allocating resources and those setting quotas for users or classes of service. As such, automation should be a key aspect of dynamic analysis mechanisms so that the operational impact of a conflict can be kept to a minimum.

### Detection and resolution of policy conflicts

To effectively use policies and drive the functionality of a managed system in a consistent manner, it is necessary to check that newly created policies do not conflict with each other or with policies already deployed in the system. To achieve this, detection processes utilise information regarding the conditions under which conflicts can arise to search policy spaces and identify policies that meet the conflict criteria. Based on the types of conflicts identified in the literature and the different application domains in which they occur, research has concentrated in the development of mechanisms and techniques for their effective detection. Although simple conflicts (e.g. modality conflicts) can be detected by syntactic analysis, more specialised inconsistencies require a precise definition of the conditions for a conflict, which sometimes include domain-specific knowledge, and processes that utilise such information to signal the occurrence of a conflict. Popular approaches for the detection of conflicts have been based on: meta-policies (detection rules), policy relationships, applicability spaces, and information models.

Resolution is the latter part of policy analysis, which aims at handling detected inconsistencies, preferably in an automated manner, so that consistency among policies can be restored. The process of resolving conflicts may involve retracting, suppressing, prioritising, or amending policies, and in some cases, enforcing a new policy altogether so that consistency among policy rules can be restored. The methodology in doing so depends heavily on the type of policies involved and the domain in which conflicts occur. Although human intervention is unavoidable in some situations, several research efforts focussed on techniques to automate the resolution process where possible. Popular approaches for the resolution of conflicts have been based on: meta-policies (resolution rules), precedence, policy ordering, and conflict prevention.

The time-frame at which conflicts can be detected influences the analysis methodology and requirements for dealing with them. Static conflicts are typically detected through analysis initiated manually by the system administrator; conflicts represent inconsistencies between policies and are typically resolved by amending the policies. In contrast, run-time conflicts must be detected by a process that monitors policy enforcement and detects inconsistent situations in the system’s execution. Resolution must be achieved automatically, for example through enforcing resolution rules. Lack of automation in the handling of run-time conflicts may have catastrophic consequences on the correct system operation, especially when managing QoS for delay sensitive applications.

## Policy refinement

Ideally, a policy-based management system should facilitate the definition of high-level administrative goals, which are easy for humans to express and understand, enable their translation into low-level policies and map them into commands that configure the managed devices accordingly. While the high-level goals reflect the business objectives of the network administrator, the low-level policies are responsible for device-level configurations.

Policy refinement is the process of transforming a high-level goal or abstract policy specification into low-level, concrete policies that can be enforced on the managed system. The main tasks of the refinement process are the following:

- Determine the resources that are needed to satisfy the requirements of the policy
- Translate high-level goals into operational policies that the system can enforce
- Verify that the low-level policies actually meet the requirements specified by the high-level goal

Several policy refinement approaches have been developed. The most notable ones are based on linear temporal logic, event calculus, and utility computing.
