---
title: "Hazard analysis"
source: https://en.wikipedia.org/wiki/Hazard_analysis
domain: functional-safety-concepts
license: CC-BY-SA-4.0
tags: functional safety, hazard analysis, fail-safe design, redundancy engineering
fetched: 2026-07-02
---

# Hazard analysis

A **hazard analysis** is one of many methods that may be used to assess risk. At its core, the process entails describing a system object (such as a person or machine) that intends to conduct some activity. During the performance of that activity, an adverse event (referred to as a “factor”) may be encountered that could cause or contribute to an occurrence (mishap, incident, accident). Finally, that occurrence will result in some outcome that may be measured in terms of the degree of loss or harm. This outcome may be measured on a continuous scale, such as an amount of monetary loss, or the outcomes may be categorized into various levels of severity e.g. environmental damage, personal injury, or reputational damage etc.

## A Simple Hazard Analysis

The first step in hazard analysis is to identify the hazards. If an automobile is an object performing an activity such as driving over a bridge, and that bridge may become icy, then an icy bridge might be identified as a hazard. If this hazard is encountered, it could cause or contribute to the occurrence of an automobile accident, and the outcome of that occurrence could range in severity from a minor fender-bender to a fatal accident.

## Managing Risk through Hazard Analysis

A hazard analysis may be used to inform decisions regarding the mitigation of risk. For instance, the probability of encountering an icy bridge may be reduced by adding salt such that the ice will melt. Or, risk mitigation strategies may target the occurrence. For instance, putting tire chains on a vehicle does nothing to change the probability of a bridge becoming icy, but if an icy bridge is encountered, it does improve traction, reducing the chance of a sliding into another vehicle. Finally, risk may be managed by influencing the severity of outcomes. For instance, seatbelts and airbags do nothing to prevent bridges from becoming icy, nor do they prevent accidents caused by that ice. However, in the event of an accident, these devices lower the probability of the accident resulting in fatal or serious injuries.

## Software Hazard Analysis

IEEE STD-1228-1994 Software Safety Plans prescribes industry best practices for conducting software safety hazard analyses to help ensure safety requirements and attributes are defined and specified for inclusion in software that commands, controls or monitors critical functions. When software is involved in a system, the development and design assurance of that software is often governed by DO-178C. The severity of consequence identified by the hazard analysis establishes the criticality level of the software. Software criticality levels range from A to E, corresponding to the severity of Catastrophic to No Safety Effect. Higher levels of rigor are required for level A and B software and corresponding functional tasks and work products is the system safety domain are used as objective evidence of meeting safety criteria and requirements.

In 2009 a leading edge commercial standard was promulgated based on decades of proven system safety processes in DoD and NASA. ANSI/GEIA-STD-0010-2009 (Standard Best Practices for System Safety Program Development and Execution) is a demilitarized commercial best practice that uses proven holistic, comprehensive and tailored approaches for hazard prevention, elimination and control. It is centered around the hazard analysis and functional based safety process.

## Severity category examples

When used as part of an aviation hazard analysis, "Severity" describes the outcome (the degree of loss or harm) that results from an occurrence (an aircraft accident or incident). When categorized, severity categories must be mutually exclusive such that every occurrence has one, and only one, severity category associated with it. The definitions must also be collectively exhaustive such that all occurrences fall into one of the categories. In the US, the FAA includes five severity categories as part of its safety risk management policy.

| Severity | Definition |
|---|---|
| Severity 1 - Catastrophic | An expected unintentional effect that includes any of the following: 3 or more fatalities Crewed aircraft hull loss with at least 1 fatality |
| Severity 2 - Hazardous | An expected unintentional effect that includes any of the following: 1-2 fatalities without crewed aircraft hull loss Crewed aircraft hull loss without fatalities 3 or more serious injuries |
| Severity 3 - Major | An expected unintentional effect that includes any of the following: 1-2 serious injuries 3 or more minor injuries Substantial damage to crewed aircraft Hull loss to uncrewed aircraft > 55 lbs |
| Severity 4 - Minor | An expected unintentional effect that includes any of the following: 1-2 minor injuries Minor damage to crewed aircraft Substantial damage to uncrewed aircraft > 55 lbs |
| Severity 5 - Minimal | Negligible safety effect |

(medical devices)

| Severity | Definition |
|---|---|
| Catastrophic | Results in death |
| Critical | Results in permanent impairment or life-threatening injury |
| Serious | Results in injury or impairment requiring professional medical intervention |
| Minor | Results in temporary injury or impairment not requiring professional medical intervention |
| Negligible | Results in temporary discomfort or inconvenience |

## Likelihood category examples

When used as part of an aviation hazard analysis, a "Likelihood" is a specific probability. It is the joint probability of a hazard occurring, that hazard causing or contributing to an aircraft accident or incident, and the resulting degree of loss or harm falling within one of the defined severity categories. Thus, if there are five severity categories, each hazard will have five likelihoods. In the US, the FAA provides a continuous probability scale for measuring likelihood, but also includes seven likelihood categories as part of its safety risk management policy.

| Likelihood | Definition |
|---|---|
| Likelihood A - Frequent | Probability < 1 but >= $1\times 10^{-5}$ |
| Likelihood B - Infrequent | Probability < $1\times 10^{-5}$ but >= $1\times 10^{-6}$ |
| Likelihood C - Extremely Infrequent | Probability < $1\times 10^{-6}$ but >= $1\times 10^{-7}$ |
| Likelihood D - Remote | Probability < $1\times 10^{-7}$ but >= $1\times 10^{-8}$ |
| Likelihood E - Extremely Remote | Probability < $1\times 10^{-8}$ but >= $1\times 10^{-9}$ |
| Likelihood F - Improbable | Probability < $1\times 10^{-9}$ but >= $1\times 10^{-10}$ |
| Likelihood G - Extremely Improbable | Probability < $1\times 10^{-10}$ but > 0 |

(medical devices)

| Likelihood | Definition |
|---|---|
| Frequent | ≥ 10−3 |
| Probable | < 10−3 and ≥ 10−4 |
| Occasional | < 10−4 and ≥ 10−5 |
| Remote | < 10−5 and ≥ 10−6 |
| Improbable | < 10−6 |
