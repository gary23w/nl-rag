---
title: "Failure mode and effects analysis"
source: https://en.wikipedia.org/wiki/Failure_mode_and_effects_analysis
domain: failure-mode-effects-analysis
license: CC-BY-SA-4.0
tags: failure mode and effects analysis, fmea worksheet, risk priority number, criticality analysis
fetched: 2026-07-02
---

# Failure mode and effects analysis

**Failure mode and effects analysis** (**FMEA**; often written with "failure modes" in plural) is the process of reviewing as many components, assemblies, and subsystems as possible to identify potential failure modes in a system and their causes and effects. For each component, the failure modes and their resulting effects on the rest of the system are recorded in a specific FMEA worksheet. There are numerous variations of such worksheets. A FMEA can be a qualitative analysis, but may be put on a semi-quantitative basis with an RPN (Risk Priority Number) model. Related methods combine mathematical failure rate models with statistical failure mode ratio databases. It was one of the first highly structured, systematic techniques for failure analysis. It was developed by reliability engineers in the late 1950s to study problems that might arise from malfunctions of military systems. An FMEA is often the first step of a system reliability study.

A few different types of FMEA analyses exist, such as:

- Functional
- Design
- Process
- Software

Sometimes FMEA is extended to FMECA(failure mode, effects, and criticality analysis) with Risk Priority Numbers (RPN) to indicate criticality.

FMEA is an inductive reasoning (forward logic) single point of failure analysis and is a core task in reliability engineering, safety engineering and quality engineering.

A successful FMEA activity helps identify potential failure modes based on experience with similar products and processes—or based on common physics of failure logic. It is widely used in development and manufacturing industries in various phases of the product life cycle. *Effects analysis* refers to studying the consequences of those failures on different system levels.

Functional analyses are needed as an input to determine correct failure modes, at all system levels, both for functional FMEA or piece-part (hardware) FMEA. An FMEA is used to structure mitigation for risk reduction based on either reducing the severity of the failure mode or effect, or on lowering the probability of failure, or both.

The FMEA is in principle a full inductive (forward logic) analysis; however the failure probability can only be estimated or reduced by understanding the *failure mechanism*. Hence, FMEA may include information on causes of failure (deductive analysis) to reduce the possibility of occurrence by eliminating identified *(root) causes*.

## Introduction

The FME(C)A is a design tool used to systematically analyze postulated component failures and identify the resultant effects on system operations. The analysis is sometimes characterized as consisting of two sub-analyses, the first being the failure modes and effects analysis (FMEA), and the second, the criticality analysis (CA). Successful development of an FMEA requires that the analyst include all significant failure modes for each contributing element or part in the system. FMEAs can be performed at the system, subsystem, assembly, subassembly or part level.

The FMECA should be a living document during development of a hardware design. It should be scheduled and completed concurrently with the design. If completed in a timely manner, the FMECA can help guide design decisions. The usefulness of the FMECA as a design tool and in the decision-making process is dependent on the effectiveness and timeliness with which design problems are identified. Timeliness is probably the most important consideration. In the extreme case, the FMECA would be of little value to the design decision process if the analysis is performed after the hardware is built. While the FMECA identifies all part failure modes, its primary benefit is the early identification of all critical and catastrophic subsystem or system failure modes so they can be eliminated or minimized through design modification at the earliest point in the development effort; therefore, the FMECA should be performed at the system level as soon as preliminary design information is available and extended to the lower levels as the detail design progresses.

Remark: For more complete scenario modelling another type of reliability analysis may be considered, for example fault tree analysis (FTA); a *deductive* (backward logic) failure analysis that may handle multiple failures within the item and/or external to the item including maintenance and logistics. It starts at higher functional / system level. An FTA may use the basic failure mode FMEA records or an effect summary as one of its inputs (the basic events). Interface hazard analysis, human error analysis and others may be added for completion in scenario modelling.

### Functional failure mode and effects analysis

The analysis should always be started by someone listing the functions that the design needs to fulfill. Functions are the starting point of a well done FMEA, and using functions as baseline provides the best yield of an FMEA. After all, a design is only one possible solution to perform functions that need to be fulfilled. This way an FMEA can be done on concept designs as well as detail designs, on hardware as well as software, and no matter how complex the design.

When performing a FMECA, interfacing hardware (or software) is first considered to be operating within specification. After that it can be extended by consequently using one of the 5 possible failure modes of one function of the interfacing hardware as a cause of failure for the design element under review. This gives the opportunity to make the design robust against function failure elsewhere in the system.

In addition, each part failure postulated is considered to be the only failure in the system (i.e., it is a single failure analysis). In addition to the FMEAs done on systems to evaluate the impact lower level failures have on system operation, several other FMEAs are done. Special attention is paid to interfaces between systems and in fact at all functional interfaces. The purpose of these FMEAs is to assure that irreversible physical and/or functional damage is not propagated across the interface as a result of failures in one of the interfacing units. These analyses are done to the piece part level for the circuits that directly interface with the other units. The FMEA can be accomplished without a CA, but a CA requires that the FMEA has previously identified system level critical failures. When both steps are done, the total process is called an FMECA.

### Ground rules

The ground rules of each FMEA include a set of project selected procedures; the assumptions on which the analysis is based; the hardware that has been included and excluded from the analysis; and the rationale for the exclusions. The ground rules also describe the indenture level of the analysis (i.e. the level in the hierarchy of the part to the sub-system, sub-system to the system, etc.), the basic hardware status, and the criteria for system and mission success. Every effort should be made to define all ground rules before the FMEA begins; however, the ground rules may be expanded and clarified as the analysis proceeds. A typical set of ground rules (assumptions) follows:

1. Only one failure mode exists at a time.
2. All inputs (including software commands) to the item being analyzed are present and at nominal values.
3. All consumables are present in sufficient quantities.
4. Nominal power is available.

### Benefits

Major benefits derived from a properly implemented FMECA effort are as follows. It provides:

1. A documented method for selecting a design with a high probability of successful operation and safety.
2. A documented uniform method of assessing potential failure mechanisms, failure modes and their impact on system operation, resulting in a list of failure modes ranked according to the seriousness of their system impact and likelihood of occurrence.
3. Early identification of single failure points (SFPS) and system interface problems, which may be critical to mission success and/or safety. They also provide a method of verifying that switching between redundant elements is not jeopardized by postulated single failures.
4. An effective method for evaluating the effect of proposed changes to the design and/or operational procedures on mission success and safety.
5. A basis for in-flight troubleshooting procedures and for locating performance monitoring and fault-detection devices.
6. Criteria for early planning of tests.

From the above list, early identifications of SFPS, input to the troubleshooting procedure and locating of performance monitoring / fault detection devices are probably the most important benefits of the FMECA. In addition, the FMECA procedures are straightforward and allow orderly evaluation of the design.

## History

Procedures for conducting FMECA were described in 1949 in US Armed Forces Military Procedures document MIL-P-1629, revised in 1980 as MIL-STD-1629A. By the early 1960s, contractors for the U.S. National Aeronautics and Space Administration (NASA) were using variations of FMECA or FMEA under a variety of names. NASA programs using FMEA variants included Apollo, Viking, Voyager, Magellan, Galileo, and Skylab. The civil aviation industry was an early adopter of FMEA, with the Society for Automotive Engineers (SAE, an organization covering aviation and other transportation beyond just automotive, despite its name) publishing ARP926 in 1967. After two revisions, Aerospace Recommended Practice ARP926 has been replaced by ARP4761, which is now broadly used in civil aviation.

During the 1970s, use of FMEA and related techniques spread to other industries. In 1971 NASA prepared a report for the U.S. Geological Survey recommending the use of FMEA in assessment of offshore petroleum exploration. A 1973 U.S. Environmental Protection Agency report described the application of FMEA to wastewater treatment plants. FMEA as application for HACCP on the Apollo Space Program moved into the food industry in general.

The automotive industry began to use FMEA by the mid 1970s. The Ford Motor Company introduced FMEA to the automotive industry for safety and regulatory consideration after the Pinto affair. Ford applied the same approach to processes (PFMEA) to consider potential process induced failures prior to launching production. In 1993 the Automotive Industry Action Group (AIAG) first published an FMEA standard for the automotive industry. It is now in its fourth edition. The SAE first published related standard J1739 in 1994. This standard is also now in its fourth edition. In 2019 both method descriptions were replaced by the new AIAG / VDA FMEA handbook. It is a harmonization of the former FMEA standards of AIAG, VDA, SAE and other method descriptions. As of 2024, the AIAG / VDA FMEA Handbook is accepted by GM, Ford, Stellantis, Honda NA, BMW, Volkswagen Group, Mercedes-Benz Group AG (formerly Daimler AG), and Daimler Truck.

Although initially developed by the military, FMEA methodology is now extensively used in a variety of industries including semiconductor processing, food service, plastics, software, and healthcare. Toyota has taken this one step further with its design review based on failure mode (DRBFM) approach. The method is now supported by the American Society for Quality which provides detailed guides on applying the method. The standard failure modes and effects analysis (FMEA) and failure modes, effects and criticality analysis (FMECA) procedures identify the product failure mechanisms, but may not model them without specialized software. This limits their applicability to provide a meaningful input to critical procedures such as virtual qualification, root cause analysis, accelerated test programs, and to remaining life assessment. To overcome the shortcomings of FMEA and FMECA a failure modes, mechanisms and effect analysis (FMMEA) has often been used.

A variation of FMEA developed for functional safety applications is called Design Deviation and Mitigation Analysis (DDMA).[5] The DDMA variation adds information not normally included in a FMEA such as the automatic diagnostic mitigations, latent fault tests, and useful life. DDMA deletes RPN numbers as they are replaced by FMEDA results.

Following the release of IATF 16949:2016, an international quality standard that requires companies to have an organization-specific documented FMEA process, many original equipment manufacturers (OEMs) like Ford are updating their Customer Specific Requirements (CSR) to include the usage of specific FMEA software. For Ford specifically, these requirements had multiple-stage compliance deadlines of July and December of 2022.

## Basic terms

The following covers some basic FMEA terminology.

**Action priority (AP)**

The AP replaces the former risk matrix and RPN in the AIAG / VDA FMEA handbook 2019. It makes a statement about the need for additional improvement measures.

**Failure**

The loss of a function under stated conditions.

**Failure mode**

The specific manner or way by which a failure occurs in terms of failure of the part, component, function, equipment, subsystem, or system under investigation. Depending on the type of FMEA performed, failure mode may be described at various levels of detail. A piece part FMEA will focus on detailed part or component failure modes (such as fully fractured axle or deformed axle, or electrical contact stuck open, stuck short, or intermittent). A functional FMEA will focus on functional failure modes. These may be general (such as no function, over function, under function, intermittent function, or unintended function) or more detailed and specific to the equipment being analyzed. A PFMEA will focus on process failure modes (such as inserting the wrong drill bit).

**Failure cause and/or mechanism**

Defects in requirements, design, process, quality control, handling or part application, which are the underlying cause or sequence of causes that initiate a process (mechanism) that leads to a failure mode over a certain time. A failure mode may have more causes.

For example; "fatigue or corrosion of a structural beam" or "fretting corrosion in an electrical contact" is a failure mechanism and in itself (likely) not a failure mode. The related failure mode (end state) is a "full fracture of structural beam" or "an open electrical contact". The initial cause might have been "Improper application of corrosion protection layer (paint)" and /or "(abnormal) vibration input from another (possibly failed) system".

**Failure effect**

Immediate consequences of a failure on operation, or more generally on the needs for the customer / user that should be fulfilled by the function but now is not, or not fully, fulfilled.

**Indenture levels (bill of material or functional breakdown)**

An identifier for system level and thereby item complexity. Complexity increases as levels are closer to one.

**Local effect**

The failure effect as it applies to the item under analysis.

**Next higher level effect**

The failure effect as it applies at the next higher indenture level.

**End effect**

The failure effect at the highest indenture level or total system.

**Detection**

The means of detection of the failure mode by maintainer, operator or built in detection system, including estimated dormancy period (if applicable).

**Probability**

The likelihood of the failure occurring.

**Risk priority number (RPN)**

Severity (of the event) × probability (of the event occurring) × detection (probability that the event would not be detected before the user was aware of it).

**Severity**

The consequences of a failure mode. Severity considers the worst potential consequence of a failure, determined by the degree of injury, property damage, system damage and/or time lost to repair the failure.

**Remarks / mitigation / actions**

Additional info, including the proposed mitigation or actions used to lower a risk or justify a risk level or scenario.

## Example of FMEA worksheet

Example FMEA worksheet

FMEA Ref.

Item

Potential failure mode

Potential cause(s) / mechanism

Mission phase

Local effects of failure

Next higher level effect

System-level end effect

(P) Probability (estimate)

(S) Severity

(D) Detection (indications to operator, maintainer)

Detection dormancy period

Risk level P*S (+D)

Actions for further investigation / evidence

Mitigation / requirements

1.1.1.1

Brake manifold ref. designator 2b, channel A, o-ring

Internal leakage from channel A to B

a) O-ring compression set (creep) failure

b) surface damage during assembly

Landing

Decreased pressure to main brake hose

No left wheel braking

Severely reduced aircraft deceleration on ground and side drift. Partial loss of runway position control. Risk of collision

(C) Occasional

(V) Catastrophic (this is the worst case)

(1) Flight computer and maintenance computer will indicate "Left main brake, pressure low"

Built-in test interval is 1 minute

Unacceptable

Check dormancy period and probability of failure

Require redundant independent brake hydraulic channels and/or require redundant sealing and classify o-ring as

critical part class 1

### Probability (P)

Source:

It is necessary to look at the cause of a failure mode and the likelihood of occurrence. This can be done by analysis, calculations / FEM, looking at similar items or processes and the failure modes that have been documented for them in the past. A failure cause is looked upon as a design weakness. All the potential causes for a failure mode should be identified and documented. This should be in technical terms. Examples of causes are: Human errors in handling, manufacturing induced faults, fatigue, creep, abrasive wear, erroneous algorithms, excessive voltage or improper operating conditions or use (depending on the used ground rules). A failure mode may be given a *Probability Ranking* with a defined number of levels. This field is also often referred to as an *Occurrence Rating*.

| Rating | Meaning |
|---|---|
| 1 | Extremely unlikely (virtually impossible or no known occurrences on similar products or processes, with many running hours) |
| 2 | Remote (relatively few failures) |
| 3 | Occasional (occasional failures) |
| 4 | Reasonably possible (repeated failures) |
| 5 | Frequent (failure is almost inevitable) |

For a piece part FMEA, quantitative probability may be calculated from the results of a reliability prediction analysis and the failure mode ratios from a failure mode distribution catalog, such as RAC FMD-97. This method allows a quantitative FTA to use the FMEA results to verify that undesired events meet acceptable levels of risk.

### Severity (S)

Source:

Determine the Severity for the worst-case scenario adverse end effect (state). It is convenient to write these effects down in terms of what the user might see or experience in terms of functional failures. Examples of these end effects are: full loss of function x, degraded performance, functions in reversed mode, too late functioning, erratic functioning, etc. Each end effect is given a Severity number (S) from, say, I (no effect) to V (catastrophic), based on cost and/or loss of life or quality of life. These numbers prioritize the failure modes (together with probability and detectability). Below a typical classification is given. Other classifications are possible. See also hazard analysis.

| Rating | Meaning |
|---|---|
| 1 | No relevant effect on reliability or safety |
| 2 | Very minor, no damage, no injuries, only results in a maintenance action (only noticed by discriminating customers) |
| 3 | Minor, low damage, light injuries (affects very little of the system, noticed by average customer) |
| 4 | Critical (causes a loss of primary function; loss of all safety margins, 1 failure away from a catastrophe, severe damage, severe injuries, max 1 possible death) |
| 5 | Catastrophic (product becomes inoperative; the failure may result in complete unsafe operation and possible multiple deaths) |

### Detection (D)

Source:

The means or method by which a failure is detected, isolated by operator and/or maintainer and the time it may take. This is important for maintainability control (availability of the system) and it is especially important for multiple failure scenarios. This may involve dormant failure *modes* (e.g. no direct system effect, while a redundant system / item automatically takes over or when the failure only is problematic during specific mission or system states) or latent failures (e.g. deterioration failure *mechanisms*, like metal growing a crack, but not of critical length). It should be made clear how the failure mode or cause can be discovered by an operator under normal system operation or if it can be discovered by the maintenance crew by some diagnostic action or automatic built in system test. A dormancy and/or latency period may be entered.

| Rating | Meaning |
|---|---|
| 1 | Certain – fault will be caught on test |
| 2 | Almost certain |
| 3 | High |
| 4 | Moderate |
| 5 | Low |
| 6 | Fault is undetected by operators or maintainers |

### Dormancy or latency period

The average time that a failure mode may be undetected may be entered if known. For example:

- Seconds, auto detected by maintenance computer
- 8 hours, detected by turn-around inspection
- 2 months, detected by scheduled maintenance block X
- 2 years, detected by overhaul task x

### Indication

If the undetected failure allows the system to remain in a *safe* / working state, a second failure situation should be explored to determine whether or not an indication will be evident to all *operators* and what corrective action they may or should take.

Indications to the operator should be described as follows:

- Normal. An indication that is evident to an operator when the system or equipment is operating normally.
- Abnormal. An indication that is evident to an operator when the system has malfunctioned or failed.
- Incorrect. An erroneous indication to an operator due to the malfunction or failure of an indicator (i.e., instruments, sensing devices, visual or audible warning devices, etc.).

PERFORM DETECTION COVERAGE ANALYSIS FOR TEST PROCESSES AND MONITORING (From ARP4761 Standard):

This type of analysis is useful to determine how effective various test processes are at the detection of latent and dormant faults. The method used to accomplish this involves an examination of the applicable failure modes to determine whether or not their effects are detected, and to determine the percentage of failure rate applicable to the failure modes which are detected. The possibility that the detection means may itself fail latently should be accounted for in the coverage analysis as a limiting factor (i.e., coverage cannot be more reliable than the detection means availability). Inclusion of the detection coverage in the FMEA can lead to each individual failure that would have been one effect category now being a separate effect category due to the detection coverage possibilities. Another way to include detection coverage is for the FTA to conservatively assume that no holes in coverage due to latent failure in the detection method affect detection of all failures assigned to the failure effect category of concern. The FMEA can be revised if necessary for those cases where this conservative assumption does not allow the top event probability requirements to be met.

After these three basic steps the Risk level may be provided.

### Risk level (P×S) and (D)

Source:

**Risk is the combination of end effect probability and severity** where probability and severity includes the effect on non-detectability (**dormancy time**). This may influence the end effect probability of failure or the worst case effect severity. The exact calculation may not be easy in all cases, such as those where multiple scenarios (with multiple events) are possible and detectability / dormancy plays a crucial role (as for redundant systems). In that case fault tree analysis and/or event trees may be needed to determine exact probability and risk levels.

Preliminary risk levels can be selected based on a risk matrix like that shown below, based on Mil. Std. 882. The higher the risk level, the more justification and mitigation is needed to provide evidence and lower the risk to an acceptable level. High risk should be indicated to higher level management, who are responsible for final decision-making.

| SeverityProbability | I | II | III | IV | V | VI |
|---|---|---|---|---|---|---|
| I | Low | Low | Low | Low | Moderate | High |
| II | Low | Low | Low | Moderate | High | Unacceptable |
| III | Low | Low | Moderate | Moderate | High | Unacceptable |
| IV | Low | Moderate | Moderate | High | Unacceptable | Unacceptable |
| V | Moderate | Moderate | High | Unacceptable | Unacceptable | Unacceptable |

- After this step the FMEA has become like a FMECA.

## Enhanced Design FMEA Technique (DDMA)

A new FMEA variation, **Design Deviation and Mitigation Analysis (DDMA)**, has been introduced. This method adapts Functional Safety requirements to the Design FMEA process. This technique allows for the simultaneous collection of FMEDA information, leveraging functional safety engineering insights to streamline the FMEA.

The functional safety process largely replaces the need for traditional Risk Priority Numbers (RPN). Severity is superseded by a more precise classification of end-level failure modes (safe, dangerous, annunciation, or no effect), while likelihood and detection are replaced by quantitative metrics from the FMEDA, which provides a far more precise analysis of hardware component failures and their impact. To facilitate FMEDA setup, the DDMA process also incorporates descriptions of automatic diagnostics (action taken, coverage) and evaluates the effectiveness of latent fault testing.

## Timing

FMEA should be used:

- When a product or process is being designed (or redesigned)
- When an existing product or process is applied in a novel way
- Before developing control plans or procedures for a new or redesigned process
- When trying to improve an existing product, process, or service
- When analyzing failures for an existing product, process, or service
- Periodically and regularly throughout the lifetime of the product, process, or service

The FMEA should be updated whenever:

- A new cycle begins (new product/process)
- Changes are made to the operating conditions
- A change is made in the design
- New regulations are instituted
- Customer feedback indicates a problem

## Uses

- Development of system requirements that minimize the likelihood of failures
- Development of designs and test systems to ensure that the failures have been eliminated or the risk is reduced to acceptable level
- Development and evaluation of diagnostic systems
- To help with design choices (trade-off analysis)

## Advantages

- Catalyst for teamwork and idea exchange between functions
- Collect information to reduce future failures, capture engineering knowledge
- Early identification and elimination of potential failure modes
- Emphasize problem prevention
- Fulfill legal requirements (product liability)
- Improve company image and competitiveness
- Improve production yield
- Improve the quality, reliability, and safety of a product/process
- Increase user satisfaction
- Maximize profit
- Minimize late changes and associated cost
- Reduce impact on company profit margin
- Reduce system development time and cost
- Reduce the possibility of same kind of failure in future
- Reduce the potential for warranty concerns

## Limitations

While FMEA identifies important hazards in a system, its results may not be comprehensive and the approach has limitations. In the healthcare context, FMEA and other risk assessment methods, including SWIFT (Structured What If Technique) and retrospective approaches, have been found to have limited validity when used in isolation. Challenges around scoping and organisational boundaries appear to be a major factor in this lack of validity.

If used as a top-down tool, FMEA may only identify major failure modes in a system. Fault tree analysis (FTA) is better suited for "top-down" analysis. When used as a bottom-up tool FMEA can augment or complement FTA and identify many more causes and failure modes resulting in top-level symptoms. It is not able to discover complex failure modes involving multiple failures within a subsystem, or to report expected failure intervals of particular failure modes up to the upper level subsystem or system.

Additionally, the multiplication of the severity, occurrence and detection rankings may result in rank reversals, where a less serious failure mode receives a higher RPN than a more serious failure mode. The reason for this is that the rankings are ordinal scale numbers, and multiplication is not defined for ordinal numbers. The ordinal rankings only say that one ranking is better or worse than another, but not by how much. For instance, a ranking of "2" may not be twice as severe as a ranking of "1", or an "8" may not be twice as severe as a "4", but multiplication treats them as though they are. See Level of measurement for further discussion. Various solutions to this problems have been proposed, e.g., the use of fuzzy logic as an alternative to classic RPN model. In the new AIAG / VDA FMEA handbook (2019) the RPN approach was replaced by the AP (action priority) in the Supplemental FMEA for Monitoring and System Response (FMEA-MSR) method.

The FMEA worksheet is hard to produce, hard to understand and read, as well as hard to maintain. The use of neural network techniques to cluster and visualise failure modes were suggested starting from 2010. An alternative approach is to combine the traditional FMEA table with a set of bow-tie diagrams. The diagrams provide a visualisation of the chains of cause and effect, while the FMEA table provides the detailed information about specific events.

## Types

- **Functional**: before design solutions are provided (or only on high level) functions can be evaluated on potential functional failure effects. General Mitigations ("design to" requirements) can be proposed to limit consequence of functional failures or limit the probability of occurrence in this early development. It is based on a functional breakdown of a system. This type may also be used for software evaluation.
- **Concept design / hardware**: analysis of systems or subsystems in the early design concept stages to analyse the failure mechanisms and lower level functional failures, especially to different concept solutions in more detail. It may be used in trade-off studies.
- **Detailed design / hardware**: analysis of products prior to production. These are the most detailed (in MIL 1629 called Piece-Part or Hardware FMEA) FMEAs and used to identify any possible hardware (or other) failure mode up to the lowest part level. It should be based on hardware breakdown (e.g. the BoM = bill of materials). Any failure effect severity, failure prevention (mitigation), failure detection and diagnostics may be fully analyzed in this FMEA.
- **Process**: analysis of manufacturing and assembly processes. Both quality and reliability may be affected from process faults. The input for this FMEA is amongst others a work process / task breakdown.

### Software FMEA

Source:

The software FMEA focuses on failure modes that originate in the software requirements, design, code or interfaces. The software should not be treated as a "black box" in this analysis. Instead a listing of root causes that historically lead to software failures should be considered instead. The Common Defect Enumeration (CDE) is the preferred method for software FMEA as it has a listing of root causes for software failures that include faulty functionality, faulty error handling, faulty state management, faulty timing, faulty sequencing, faulty processing, faulty usability, faulty machine learning, etc. The software FMEA is a design FMEA in that the goal is to identify missing, insufficient or incorrect design specifications before the code is written.

The probability of a software failure is assessed as follows:

- **Existence:** Are the specifications/design/code clearly insufficient or incorrect?

- **Manifestation:** Is the event a single or multiple point failure? How many installed sites will have the feature with the failure mode?

- **Controls:** How many independent controls for this failure mode currently exist in the design?

- **Detectability:** Is there an explicit test procedure for this failure mode?

Probability is NOT computed from software failure rates for the simple reason that software failure rates measure the time between software failures of EVERY root cause as opposed to the time between a failure due to a single root cause. Additionally, with software failures, the root causes will either be corrected or avoided when the failure occurs. So, time between a specific root cause has minimal value.

Severity must consider the fact that software can fail differently than hardware:

1. Software failures from the same root cause can occur repeated in a short period of time. This doesn't happen with hardware.
2. Medium severity failures that occur repeatedly can result in a very serious system failure. So the analyst must consider this when assessing severity.
3. Software failures aren't limited to a total loss of function. As per the IEEE 1633, if the software performs a function that is not correct as per the requirements, it is counted as a failure.
4. Compensating provisions don't necessarily mitigate the severity of a software failure. That's because many software failures occur without warning and many cause damage before an operator can intervene.
