---
title: "Change management (engineering)"
source: https://en.wikipedia.org/wiki/Change_management_(engineering)
domain: infrastructure-drift
license: CC-BY-SA-4.0
tags: configuration drift, declared versus actual state, drift detection reconcile, state divergence
fetched: 2026-07-02
---

# Change management (engineering)

The **change request management** process in systems engineering is the process of requesting, determining attainability, planning, implementing, and evaluating of changes to a system. Its main goals are to support the processing and traceability of changes to an interconnected set of factors.

## Introduction

There is considerable overlap and confusion between change request management, change control and configuration management. The definition below does not yet integrate these areas.

Change request management has been embraced for its ability to deliver benefits by improving the affected system and thereby satisfying "customer needs," but has also been criticized for its potential to confuse and needlessly complicate change administration. In some cases, notably in the Information Technology domain, more funds and work are put into system maintenance (and change request management) than into the initial creation of a system. Typical investment by organizations during initial implementation of large ERP systems is 15 to 20 percent of overall budget.

In the same vein, Hinley describes two of Lehman's laws of software evolution:

- **The law of continuing change**: Systems that are used must change, or else automatically become less useful.
- **The law of increasing complexity**: Through changes, the structure of a system becomes ever more complex, and more resources are required to simplify it.

Change request management is also of great importance in the field of manufacturing, which is confronted with many changes due to increasing and worldwide competition, technological advances and demanding customers. Because many systems tend to change and evolve as they are used, the problems of these industries are experienced to some degree in many others.

Notes: In the process below, it is arguable that the change committee should be responsible not only for accept/reject decisions, but also prioritization, which influences how change requests are batched for processing.

## The process and its deliverables

For the description of the change request management process, the meta-modeling technique is used. Figure 1 depicts the process-data diagram, which is explained in this section.

(Figure 1: Process-data model for the change management process)

### Activities

There are six main activities, which jointly form the change request management process. They are: Identify potential change, Analyze change request, Evaluate change, Plan change, Implement change and Review and close change. These activities are executed by four different roles, which are discussed in Table 1. The activities (or their sub-activities, if applicable) themselves are described in Table 2.

| Role | Description |
|---|---|
| **Customer** | The customer is the role that requests a change due to problems encountered or new functionality requirements; this can be a person or an organizational entity and can be in- or external to the company that is asked to implement the change. |
| **Project manager** | The project manager is the owner of the project that the CHANGE REQUEST concerns. In some cases there is a distinct change manager, who in that case takes on this role. |
| **Change committee** | The change committee decides whether a CHANGE REQUEST will be implemented or not. Sometimes this task is performed by the project manager as well. |
| **Change builder** | The change builder is the person who plans and implements the change; it could be argued that the planning component is (partially) taken on by the project manager. |

| Activity | Sub-activity | Description |
|---|---|---|
| **Identify potential change** | Require new functionality | A customer desires new functionality and formulates a REQUIREMENT. |
|   | Encounter problem | A customer encounters a problem (e.g. a bug) in the system and this leads to a PROBLEM REPORT. |
|   | Request change | A customer proposes a change through creation of a CHANGE REQUEST. |
| **Analyze change request** | Determine technical feasibility | The project manager determines the technical feasibility of the proposed CHANGE REQUEST, leading to a CHANGE TECHNICAL FEASIBILITY. |
|   | Determine costs and benefits | The project manager determines the costs and benefits of the proposed CHANGE REQUEST, resulting in CHANGE COSTS AND BENEFITS. This and the above sub-activity can be done in any order and they are independent of each other, hence the modeling as unordered activities. |
| **Evaluate change** |   | Based on the CHANGE REQUEST, its CHANGE TECHNICAL FEASIBILITY and CHANGE COSTS AND BENEFITS, the change committee makes the go/no-go decision. This is modeled as a separate activity because it is an important process step and has another role performing it. It is modeled as a sub-activity (without any activity containing it) as recommended by Remko Helms (personal communication). |
| **Plan change** | Analyze change impact | The extent of the change (i.e. what other items the change effects) is determined in a CHANGE IMPACT ANALYSIS. It could be argued that this activity leads to another go/no-go decision, or that it even forms a part of the Analyze change request activity. It is modeled here as a planning task for the change builder because of its relationship with the activity Propagate change. |
|   | Create planning | A CHANGE PLANNING is created for the implementation of the change. Some process descriptions (e.g. Mäkäräinen, 2000) illustrate that is also possible to ‘save’ changes and process them later in a batch. This activity could be viewed as a good point to do this. |
| **Implement change** | Execute change | The change is ‘programmed’; this activity has a strong relationship with Propagate change, because sometimes the change has to be adapted to other parts of the system (or even other systems) as well. |
|   | Propagate change | The changes resulting from Execute change have to be propagated to other system parts that are influenced by it. Because this and the above sub-activity are highly dependent on each other, they have been modeled as concurrent activities. |
|   | Test change | The change builder tests whether what (s)he has built actually works and satisfies the CHANGE REQUEST. As depicted in the diagram, this can result in an iterative process together with the above two sub-activities. |
|   | Update documentation | The DOCUMENTATION is updated to reflect the applied changes. |
|   | Release change | A new SYSTEM RELEASE, which reflects the applied change, is made public. |
| **Review and close change** | Verify change | The implementation of the change in the new SYSTEM RELEASE is verified for the last time, now by the project manager. Maybe this has to happen before the release, but due to conflicting literature sources and diagram complexity considerations it was chosen to model it this way and include this issue. |
|   | Close change | This change cycle is completed, i.e. the CHANGE LOG ENTRY is wrapped up. |

### Deliverables

Besides activities, the process-data diagram (Figure 1) also shows the deliverables of each activity, i.e. the data. These deliverables or concepts are described in Table 3; in this context, the most important concepts are: CHANGE REQUEST and CHANGE LOG ENTRY.

A few concepts are defined by the author (i.e. lack a reference), because either no (good) definitions could be found, or they are the obvious result of an activity. These concepts are marked with an asterisk (‘*’). Properties of concepts have been left out of the model, because most of them are trivial and the diagram could otherwise quickly become too complex. Furthermore, some concepts (e.g. CHANGE REQUEST, SYSTEM RELEASE) lend themselves for the versioning approach as proposed by Weerd, but this has also been left out due to diagram complexity constraints.

| Concept | Description |
|---|---|
| **REQUIREMENT** | A required functionality of a component (or item; NASA, 2005). |
| **PROBLEM REPORT** | Document describing a problem that cannot be solved by a level 1 help desk employee; contains items like date, contact info of person reporting the problem, what is causing the problem, location and description of the problem, action taken and disposition, but this is not depicted in the diagram (Dennis, et al., 2002). |
| **CHANGE REQUEST** | Document that describes the requested change and why it is important; can originate from PROBLEM REPORTS, system enhancements, other projects, changes in underlying systems and senior management, here summarized as REQUIREMENTS (Dennis, et al., 2002). Important attribute: ‘go/no-go decision’, i.e. is the change going to be executed or not? |
| **CHANGE LOG ENTRY*** | Distinct entry in the collection of all changes (e.g. for a project); consists of a CHANGE REQUEST, CHANGE TECHNICAL FEASIBILITY, CHANGE COSTS AND BENEFITS, CHANGE IMPACT ANALYSIS, CHANGE PLANNING, TEST REPORT and CHANGE VERIFICATION. Not all these have to be included if the process is terminated earlier (i.e. if the change is not implemented). |
| **CHANGE TECHNICAL FEASIBILITY** | Concept that indicates whether or not “reliable hardware and software, technical resources capable of meeting the needs of a proposed system [i.e. change request] can be acquired or developed by an organization in the required time” (Vogl, 2004). |
| **CHANGE COSTS AND BENEFITS** | The expected effort required to implement and the advantages (e.g. cost savings, increased revenue) gained by implementing the change. Also named economic feasibility (Vogl, 2004). |
| **CHANGE IMPACT ANALYSIS** | An assessment of the extent of the change. |
| **CHANGE PLANNING** | “A scheme, method or design for the attainment of some objective or to achieve something [i.e. the change]” (Georgetown University, n.d.), in this case the change. |
| **ITEM** | “A non-specific term used to denote any product, including systems, subsystems, assemblies, subassemblies, units, sets, accessories, computer programs, computer software or parts” (Rigby, 2003); has (overlapping) subtypes ADDED ITEM and CHANGED ITEM. |
| **ADDED ITEM*** | Self-explanatory: a newly created ITEM; subtype of ITEM. |
| **CHANGED ITEM*** | Self-explanatory: an ITEM that already existed, but has been altered; subtype of ITEM. |
| **TEST REPORT** | “A document that describes the conduct and results of the testing carried out for a system or component [affected by the change]” (IEEE, 1991). |
| **DOCUMENTATION** | According to the Pennsylvania State University Libraries (2004) definition, DOCUMENTATION is “[p]rinted material which accompanies other materials (usually non-book), and which explains, gives instructions for use, or otherwise functions as a guide to the major materials.” In this context, it can also be digital materials or even training, as long as it relates to (pieces of) the system. |
| **SYSTEM RELEASE** | “[M]erchandise issued for sale or public showing” (Princeton University, 2003). Consists of one or more ITEMS and the accompanying DOCUMENTATION. |
| **CHANGE VERIFICATION** | A determination of whether or not the result of the change implementation fulfills the requirements established earlier (Rigby, 2003). |

Besides just ‘changes’, one can also distinguish deviations and waivers. A deviation is an authorization (or a request for it) to depart from a requirement of an item, prior to the creation of it. A waiver is essentially the same, but than during or after creation of the item. These two approaches can be viewed as minimalistic change request management (i.e. no real solution to the problem at hand).

### Examples

A good example of the change request management process in action can be found in software development. Often users report bugs or desire new functionality from their software programs, which leads to a change request. The product software company then looks into the technical and economical feasibility of implementing this change and consequently it decides whether the change will actually be realized. If that indeed is the case, the change has to be planned, for example through the usage of function points. The actual execution of the change leads to the creation and/or alteration of software code and when this change is propagated it probably causes other code fragments to change as well. After the initial test results seem satisfactory, the documentation can be brought up to date and be released, together with the software. Finally, the project manager verifies the change and closes this entry in the change log.

Another typical area for change request management in the way it is treated here, is the manufacturing domain. Take for instance the design and production of a car. If for example the vehicle's air bags are found to automatically fill with air after driving long distances, this will without a doubt lead to customer complaints (or hopefully problem reports during the testing phase). In turn, these produce a change request (see Figure 2 on the right), which will probably justify a change. Nevertheless, a – most likely simplistic – cost and benefit analysis has to be done, after which the change request can be approved. Following an analysis of the impact on the car design and production schedules, the planning for the implementation of the change can be created. According to this planning, the change can actually be realized, after which the new version of the car is hopefully thoroughly tested before it is released to the public.

## In process plants

Since complex processes can be very sensitive to even small changes, proper management of change to industrial process plants is recognized as critical to safety. Undocumented, not properly risk assessed changes are a recipe for disaster. An eminent example of this is the Flixborough explosion, where improvised changes involving the bypassing of a stage in a reactor train was at the origin of the accident. The change had not been properly thought out, documented and risk-assessed, so that the event of breach of containment had not been identified. In the US, OSHA has regulations that govern how changes are to be made and documented. The main requirement is that a thorough review of a proposed change be performed by a multi-disciplinary team to ensure that as many possible viewpoints are used to minimize the chances of missing a hazard. In this context, change request management is known as Management of Change, or MOC. It is just one of many components of Process Safety Management, section 1910.119(l).1.
