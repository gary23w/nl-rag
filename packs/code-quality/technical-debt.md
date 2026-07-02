---
title: "Technical debt"
source: https://en.wikipedia.org/wiki/Technical_debt
domain: code-quality
license: CC-BY-SA-4.0
tags: refactoring, code smell, technical debt, cyclomatic complexity, coupling, clean code
fetched: 2026-07-02
---

# Technical debt

**Technical debt** (also known as **design debt** or **code debt**) is a qualitative description of the cost to maintain a system that is attributable to choosing an expedient solution for its development. While an expedited solution can accelerate development in the short term, the resulting low quality may increase future costs if left unresolved. The term is often used in the context of information technology and especially software development.

Technical debt is similar to yet differs significantly from monetary debt. Incurring either generally makes future goals more challenging to attain. But unlike monetary debt, technical debt is often incurred without intention. The choice to minimize development time and cost, an ever-present aspect of business, is the primary factor. Technical debt is generally only assessed retroactively (after a development effort).

Properly managing technical debt is essential for maintaining software quality and long-term sustainability. In some cases, taking on technical debt is a strategic choice to meet immediate goals, such as delivering a proof of concept or a quick release. However, failure to prioritize and address the debt can result in reduced maintainability, increased development costs, and risk to production systems.

Technical debt results from design and implementation decisions that may optimize for the short term, but at the expense of future adaptability and maintainability. System aspects that incur technical debt can be described as a collection of design or implementation constructs that make future changes more costly or impossible, primarily impacting internal system qualities such as maintainability and evolvability.

## Origin

Ward Cunningham coined the term *technical debt* in 1992. After reading *Metaphors We Live By*, Cunningham devised this debt metaphor to explain to his boss the need to refactor the financial product they were working on:

> Shipping first time code is like going into debt. A little debt speeds development so long as it is paid back promptly with a rewrite.... The danger occurs when the debt is not repaid. Every minute spent on not-quite-right code counts as interest on that debt. Entire engineering organizations can be brought to a stand-still under the debt load of an unconsolidated implementation, object-oriented or otherwise.

Similar concepts had existed before this. In 1980, Meir "Manny" Lehman had published a similar law using an "architectural metaphor" for the deteriorating nature of software. Manny's Law states: "As an evolving program is continually changed, its complexity, reflecting deteriorating structure, increases unless work is done to maintain or reduce it."

## Causes

Common causes of technical debt include:

**Pressure to minimize development time**

An ever-present aspect of business.

**Unexpected and ill-defined features and changes**

The implementation of last-minute

specification changes

or changes that are insufficiently documented or tested,

**Gaps in knowledge or skills**

May manifest as a lack of

process

understanding, insufficient knowledge, poor technological leadership, or inadequate mentoring or

knowledge sharing

practices.

**Issues in the development process**

Such as sub-optimal solutions, insufficient

requirements

(from process inefficiencies), conflicting requirements on parallel branches, deferred

refactoring

, or delayed upstream contributions.

**Non-compliance with best practice**

Such as insufficient

software documentation

, poor collaboration practices, lack of ownership,

rewrites

for outsourced software, inadequate attention to code quality,

tightly coupled components

, lack of a

test suite

, or failure to align to standards (including ignoring industry standard

frameworks

).

## Consequences

By increasing the cost of ongoing maintenance, technical debt makes it harder to predict release schedules. "Interest payments" result from incomplete work and escalating integration costs due to changes in the upstream project. Increases in complexity and the amount of uncompleted work make it increasingly difficult to accurately estimate effort, resulting in delays, missed deadlines, and stress on engineering teams, which can result in higher staff turnover, compounding the problem. Carrying technical debt into production increases the risk of outages, financial losses, and potential legal issues due to breached service-level agreements. Future refactoring becomes riskier and costlier, with modifications to production code introducing greater chances of disruption.

Failure to address technical debt can cause productivity to decline and slow down the delivery of features. The cumulative effects of technical debt result in increasingly fragile systems that can make bold improvements difficult. The domination of incremental changes, along with delays to critical refactoring, can result in stressed systems with inconsistent design, causing users to suffer from degraded performance and limited functionality while developers struggle to maintain quality.

## Planning

Kenny Rubin uses the following categories to help manage technical debt:

**Happened-upon**

The development team was unaware it existed until it was exposed during the normal course of performing work on the product. For example, the team is adding a new feature to the product and in doing so it realizes that a work-around had been built into the code years before by someone who has long since departed.

**Known**

Known to the development team and has been made visible using one of many approaches.

**Targeted**

Known and has been targeted for servicing by the development team.

## Limitations

The concept of technical debt presumes that an overly-expedient development effort results in additional future costs and that the costs would be avoided if different decisions were made during the effort. While true, other considerations impact the potential cost of expedient development decisions. For example, if the system does not survive long enough to be modified for a subsequent release, then the savings due to the expedient development choices are true savings since there is no future development cost. Future events may render expedient "long-term" designs obsolete. New tools and techniques might reduce the cost of future rework, challenging current debt assumptions.
