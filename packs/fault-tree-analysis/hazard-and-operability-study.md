---
title: "Hazard and operability study"
source: https://en.wikipedia.org/wiki/Hazard_and_operability_study
domain: fault-tree-analysis
license: CC-BY-SA-4.0
tags: fault tree analysis, top event logic, event tree analysis, reliability block diagram
fetched: 2026-07-02
---

# Hazard and operability study

A **hazard and operability study** (HAZOP) is a structured and systematic examination of a complex system, usually a process facility or machinery, in order to identify hazards to personnel, equipment or the environment, as well as operability problems that could affect operations efficiency. It is the foremost hazard identification tool in the domain of process safety. The intention of performing a HAZOP is to review the process or machinery through all phases of the product lifecycle to pick up design and engineering issues that may otherwise not have been found in other hazard identification (risk assessments) or design tools (FMEA’s, FTA’s, etc.)

The technique is based on breaking the overall complex design of the process into a number of simpler sections called *nodes* which are then individually reviewed. It is carried out by a suitably experienced multi-disciplinary team (roles defined in section below) during a series of meetings. The HAZOP technique is qualitative and aims to stimulate the imagination of participants to identify potential hazards and operability problems. Structure and direction are given to the review process by applying standardized guideword prompts to the review of each node. A relevant standard IEC 61882 calls for team members to display 'intuition and good judgement' and for the meetings to be held in "an atmosphere of critical thinking in a frank and open atmosphere [*sic*]."

The HAZOP technique was initially developed for systems involving the treatment of a fluid medium or other material flow in the process industries, where it is now a major element of process safety management. It was later expanded to the analysis of batch reactions and process plant operational procedures. Recently, it has been used to assess domains other than or only loosely related to the process industries, namely: software applications including programmable electronic systems; software and code development; systems involving the movement of people by transport modes such as road, rail, and air; administrative procedures in different industries; medical devices; machinery; etc.

## History

The technique is generally considered to have originated in the Heavy Organic Chemicals Division of Imperial Chemical Industries (ICI), which was then a major British and international chemical company.

Its origins have been described by Trevor Kletz, who was the company's safety advisor from 1968 to 1982. In 1963 a team of three people met for three days a week for four months to study the design of a new phenol plant, starting with a technique called *critical examination* which asked for alternatives but later changed this to ask for *deviations*. The method was further refined within the company, under the name *operability studies*, and became the third stage, detailed design, of its hazard analysis procedure (the first two stages being done during conception and specification).

In 1974 a one-week safety course including this procedure was offered by the Institution of Chemical Engineers (IChemE) at Teesside Polytechnic. Coming shortly after the Flixborough disaster, the course was fully booked, as were ones in the next few years. In the same year as the 1974 course offering, the first paper in open literature was also published. In 1977 the Chemical Industries Association published a guide. Up to this time the term 'HAZOP' had not been used in formal publications. The first to do this was Kletz in 1983, with what were essentially the course notes (revised and updated) from the IChemE courses. By 1983, hazard and operability studies had become an expected part of chemical engineering degree courses in the UK.

Nowadays, government regulators (EPA, OSHA, etc.) and the process industry at large (including operators and contractors) consider HAZOP a strictly necessary step of project development, at the very least during the detailed design phase.

## Method

The method is applied to complex processes, for which sufficient design information is available and not likely to change significantly. This range of data should be explicitly identified and taken as the "design intent" basis for the HAZOP study. For example, a prudent designer will have intended to allow for foreseeable variations within the process, creating a larger design envelope than just the basic requirements, and the HAZOP will be looking at ways in which this might not be sufficient.

A common use of the HAZOP is relatively early through the detailed design of a plant or process. However, it can also be applied at other stages (operational life) of existing plants, in which case it is usefully applied as a revalidation tool to ensure that unduly managed changes have not crept in since first plant start-up. Where design information is not fully available, such as during front-end loading, a *coarse* HAZOP can be conducted; however, where a design is required to have a HAZOP performed to meet legislative or regulatory requirements, such an early rough exercise cannot be considered sufficient and a later, detailed design HAZOP also becomes necessary.

For process plants, identifiable sections (*nodes*) are chosen so that for each a meaningful *design intent* can be specified . They are commonly indicated on piping and instrumentation diagrams (P&IDs) and process flow diagrams (PFDs). P&IDs in particular are the foremost reference document for conducting a HAZOP. The detail of each node should be appropriate to the complexity of the system and the magnitude of the hazards it might pose. However, node documentation will also need to balance between "too large and complex" (fewer nodes, but the team members may not be able to consider issues within the whole node at once) and "too small and simple" (many trivial and repetitive nodes, each of which has to be reviewed independently and documented).

For each node, the HAZOP team uses a list of standardized *guidewords* and process *parameters* listed in the section below to identify potential *deviations* from the design intent. For each deviation, the team identifies feasible *causes* and likely *consequences* then decides (with confirmation by risk analysis where necessary, e.g., by way of an agreed upon risk matrix) whether the existing safeguards are sufficient, or whether an *action* or *recommendation* to install additional safeguards or put in place administrative controls is necessary to reduce the risks to an acceptable level.

The degree of preparation for the HAZOP is critical to the overall success of the review. "Frozen" design information provided to the team members with time for them to familiarize themselves with the process, an adequate schedule allowed for the performance of the HAZOP, provision of the best team members for their role. Those scheduling a HAZOP should take into account the review scope, the number of nodes to be reviewed, the provision of completed design drawings and documentation and the need to maintain team performance over an extended time-frame. The team members may also need to perform some of their normal tasks during this period and the HAZOP team members can tend to lose focus unless adequate time is allowed for them to refresh their mental capabilities.

The team meetings should be managed by an independent, trained HAZOP *facilitator* (also referred to as HAZOP leader or chairperson), who is responsible for the overall quality of the review, partnered with a dedicated *scribe* to minute the meetings. As the IEC standard puts it:

> The success of the study strongly depends on the alertness and concentration of the team members and it is therefore important that the sessions are not too long and that there are appropriate intervals between sessions. How these requirements are achieved is ultimately the responsibility of the study leader.

For a medium-sized chemical plant, where the total number of items to be considered is around 1200 pieces of equipment and piping, about 40 such meetings would be needed. Various software programs are now available to assist in the management and scribing of the HAZOP activities.

### Guidewords and parameters

Source:

In order to identify deviations, the team applies (systematically i.e. in a given order) a set of **guidewords** to each node in the process. To prompt discussion, or to ensure completeness, appropriate process **parameters** are considered in turn, which apply to the design intent. Typical parameters are flow (or flowrate), temperature, pressure, level, composition, etc. The IEC standard notes guidewords should be chosen that are appropriate to the study, neither too specific (limiting ideas and discussion) nor too general (allowing loss of focus). A fairly standard set of guidewords (given as an example the standard) is as follows:

| Guideword | Meaning |
|---|---|
| No (not, none) | None of the design intent is achieved |
| More (more of, higher) | Quantitative increase in a parameter |
| Less (less of, lower) | Quantitative decrease in a parameter |
| As well as (more than) | An additional activity occurs |
| Part of | Only some of the design intention is achieved |
| Reverse | Logical opposite of the design intent occurs |
| Other than (other) | Complete substitution (another activity takes place or an unusual activity occurs or uncommon condition exists) |

Where a guide word is meaningfully applicable to a parameter (e.g., "no flow", "more temperature"), their combination should be recorded as a credible potential *deviation* from the design intent that requires review.

The following table gives an overview of commonly used guideword-parameter pairs (deviations) and common interpretations of them.

| Parameter / Guide Word | No | More | Less | As well as | Part of | Reverse | Other than |
|---|---|---|---|---|---|---|---|
| Flow | no flow | high flow | low flow | deviating concentration |   | reverse flow |   |
| Pressure | vacuum | high pressure | low pressure |   |   |   |   |
| Temperature |   | high temperature | low temperature |   |   |   |   |
| Level | no level | high level | low level |   |   |   |   |
| Time | sequence step skipped | too long / too late | too short / too soon | extra actions | missing actions | backwards | wrong time |
| Agitation | no mixing | fast mixing | slow mixing |   |   |   |   |
| Reaction | no reaction | fast reaction / runaway | slow reaction |   |   |   |   |
| Start-up / Shut-down |   | too fast | too slow | actions missed |   |   | wrong recipe |
| Draining / Venting | none | too long | too short | deviating pressure | wrong timing |   |   |
| Inerting | none | high pressure | low pressure |   | contamination |   | wrong material |
| Utility failure (e.g., instrument air, power) | failure |   |   |   |   |   |   |
| DCS failure | failure |   |   |   |   |   |   |
| Maintenance | none |   |   |   |   |   |   |

Once the causes and effects of any potential hazards have been established, the system being studied can then be modified to improve its safety. The modified design should then be subject to a formal HAZOP close-out, to ensure that no new problems have been added.

## HAZOP team

A HAZOP study is a team effort. The team should be as small as practicable and having relevant skills and experience. Where a system has been designed by a contractor, the HAZOP team should contain personnel from both the contractor and the client company. A minimum team size of five is recommended. In a large process there will be many HAZOP meetings and the individuals within the team may change, as different specialists and deputies will be required for the various roles. As many as 20 individuals may be involved. Each team member should have a definite role as follows:

| Name | Role |
|---|---|
| Study leader / Chairman / Facilitator | Someone experienced in leading HAZOPs, who is familiar with this type of process but is independent of the design team. Responsible for progressing through the series of nodes, moderating the team discussions, maintaining the accuracy of the record, ensuring the clarity of the recommended actions and identifying appropriate actionees. |
| Recorder / secretary / scribe | To document the causes, consequences, safeguards and actions identified for each deviation, to record the conclusions and recommendations of the team discussions (accurately but comprehensibly). |
| Design engineer | To explain the design and its representation, to explains how a defined deviation can occur and the corresponding system or organizational response. |
| Operator / user | Explains the operational context within which the system will operate, the operational consequences of a deviation and the extent to which deviations might lead to unacceptable consequences. |
| Specialists | Provide expertise relevant to the system, the study, the hazards and their consequences. They could be called upon for limited participation. |
| Maintainer | Someone who will maintain the system going forward. |

In earlier publications it was suggested that the study leader could also be the recorder but separate roles are now generally recommended.

The use of computers and projector screens enhances the recording of meeting minutes (the team can see what is minuted and ensure that it is accurate), the display of P&IDs for the team to review, the provision of supplemental documented information to the team and the logging of non-HAZOP issues that may arise during the review, e.g., drawing/document corrections and clarifications. Specialist software is now available from several suppliers to support the recording of meeting minutes and tracking the completion of recommended actions.

## Machinery

A machinery operability study takes a simpler approach to defining "nodes" by assessing the machine in all lifecycle stages (assembly, operation, maintenance, dismantling) and the corresponding stage operations (SOP. task list, operator movements, etc.) to identify hazards: hot parts, moving parts, and sharp edges.
