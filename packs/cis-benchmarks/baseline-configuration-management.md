---
title: "Baseline (configuration management)"
source: https://en.wikipedia.org/wiki/Baseline_(configuration_management)
domain: cis-benchmarks
license: CC-BY-SA-4.0
tags: cis benchmarks, cis critical security controls, security configuration baseline, center for internet security, system hardening guide
fetched: 2026-07-02
---

# Baseline (configuration management)

In configuration management, a **baseline** is an agreed description of the attributes of a product, at a point in time, which serves as a basis for defining change. A change is a movement from this baseline state to a next state. The identification of significant changes from the baseline state is the central purpose of baseline identification.

Typically, significant states are those that receive a formal approval status, either explicitly or implicitly. An approval status may be attributed to individual items, when a prior definition for that status has been established by project leaders, or signified by mere association to a particular established baseline. Nevertheless, this approval status is usually recognized publicly. A baseline may be established for the singular purpose of marking an approved configuration item, e.g. a project plan that has been signed off for execution. Associating multiple configuration items to such a baseline indicates those items as also being approved. Baselines may also be used to mark milestones. A baseline may refer to a single work product, or a set of work products that can be used as a logical basis for comparison.

Most baselines are established at a fixed point in time and serve to continue to reference that point (identification of state). However, some baselines, dynamic baselines, are established to carry forward as a reference to the item itself regardless of any changes to the item. These latter baselines evolve with the progression of the work effort but continue to identify notable work products in the project. Retrieving such a dynamic baseline obtains the current revision of only these notable items in the project.

While marking approval status covers the majority of uses for a baseline, multiple fixed baselines may also be established to monitor the progress of work through the passage of time. In this case, each baseline is a visible measure through an endured team effort, e.g. a series of developmental baselines. This progression is revealed when the baselines are compared with each other. A baseline may also be established as the basis for subsequent exclusive activities when the baselined products have met certain criteria. For example, certain activities reserved for items with a prior formal approval, such as formal change control procedures.

Baselines themselves are valued not only to identify the notable state of work product(s) but also provide historical views of how work product elements have progressed together over time. When a fixed baseline is retrieved, the state of the work product(s) in that subset share the same significance in their history of changes; this allows project leaders to compare the relative progress of single parts of a project to the project as a whole, which allows project leaders to identify individual items that lag or lead in progress toward better functionality or performance. For this reason, baseline identification, monitoring, and retrieval are critical to the success of configuration management, and ultimately, project quality.

Conversely, the configuration of a project includes all of its baselines, the status of the configuration, all audits, and all metrics collected. The current configuration refers to the current status, current audit, and current metrics. Similarly, but less common, a baseline may refer to all items in a project. This may include the latest revision of all items or only specific revisions of all items in the project, depending on the nature of the baseline, dynamic or fixed respectively. Once retrieved, the baseline may be compared to a particular configuration or another baseline. In configuration management, the configuration of a project is not the same as a baseline in the project but the two could coincide.

Fixed baselines often coincide with or signify project milestones, such as the set of items at a particular certifying review. Some examples include:

- Functional baseline: initial specifications established; contract, et cetera
- Allocated baseline: state of work products after requirements are approved
- Developmental baseline: state of work products amid development
- Product baseline: contains the releasable contents of the project
- Others, based upon proprietary business practices

## Application

Though common in software revision control systems as labels' or tags, the existence of baselines is found in several other technology-related domains. Baselines can be found in UML modeling systems and business rule management systems, among others.

In addition to the field of hardware and software engineering, baselines can be found in medicine (e.g. monitoring health progress), politics (e.g. statistics), physics and chemistry (e.g. observations and changes), finance (e.g. budgeting), and others.

## Baselining configuration items

In the process of performing configuration management, configuration items (or work products) may be assigned a baseline so as to establish them as having a certain status. In this sense, to baseline a work product may require certain change(s) to the work product to ensure it conforms to the characteristics associated with the baseline referenced. This varies upon context, but in many cases this requires that the work product is "reset" to an initial (possibly inherently approved) state from which work may proceed.

## Baseline control

In many environments, baselines are controlled such that certain subsequent activities against work products in that baseline are either prohibited or permitted. These activities are selected and controlled, and again, depending upon the configuration management system, are also monitored. Consequently, baselines are ordinarily subjected to configuration management audits. Configuration audits may include an examination of specific actions performed against the baseline, identification of individuals involved in any action, an evaluation of change within the baseline, (re-)certification for approval, accounting, metric collection, comparison to another baseline, or all of these.
