---
title: "Software development process"
source: https://en.wikipedia.org/wiki/Software_development_process
domain: agile-devops
license: CC-BY-SA-4.0
tags: agile, scrum, kanban, devops, continuous delivery, pair programming
fetched: 2026-07-02
---

# Software development process

A **software development process** prescribes a process for developing software. It typically divides an overall effort into smaller steps or sub-processes that are intended to ensure high-quality results. The process may describe specific deliverables – artifacts to be created and completed.

Although not strictly limited to it, software development process often refers to the high-level process that governs the development of a software system from its beginning to its end of life – known as a methodology, model or framework. The system development life cycle (SDLC) describes the typical phases that a development effort goes through from the beginning to the end of life for a system – including a software system. A methodology prescribes how engineers go about their work in order to move the system through its life cycle. A methodology is a classification of processes or a blueprint for a process that is devised for the SDLC. For example, many processes can be classified as a spiral model.

Software process and software quality are closely interrelated; some unexpected facets and effects have been observed in practice.

## Methodology

The SDLC drives the definition of a methodology in that a methodology must address the phases of the SDLC. Generally, a methodology is designed to result in a high-quality system that meets or exceeds expectations (requirements) and is delivered on time and within budget even though computer systems can be complex and integrate disparate components. Various methodologies have been devised, including waterfall, spiral, agile, rapid prototyping, incremental, and synchronize and stabilize.

A major difference between methodologies is the degree to which the phases are sequential vs. iterative. Agile methodologies, such as XP and scrum, focus on lightweight processes that allow for rapid changes. Iterative methodologies, such as Rational Unified Process and dynamic systems development method, focus on stabilizing project scope and iteratively expanding or improving products. Sequential or big-design-up-front (BDUF) models, such as waterfall, focus on complete and correct planning to guide larger projects and limit risks to successful and predictable results. Anamorphic development is guided by project scope and adaptive iterations. In scrum, for example, one could say a single user story goes through all the phases of the SDLC within a two-week sprint. By contrast the waterfall methodology, where every business requirement is translated into feature/functional descriptions which are then all implemented typically over a period of months or longer.

A project can include both a project life cycle (PLC) and an SDLC, which describe different activities. According to Taylor (2004), "the project life cycle encompasses all the activities of the project, while the systems development life cycle focuses on realizing the product requirements".

### History

The term *SDLC* is often used as an abbreviated version of *SDLC methodology*. Further, some use *SDLC* and *traditional SDLC* to mean the waterfall methodology.

According to Elliott (2004), SDLC "originated in the 1960s, to develop large scale functional business systems in an age of large scale business conglomerates. Information systems activities revolved around heavy data processing and number crunching routines". The structured systems analysis and design method (SSADM) was produced for the UK government Office of Government Commerce in the 1980s. Ever since, according to Elliott (2004), "the traditional life cycle approaches to systems development have been increasingly replaced with alternative approaches and frameworks, which attempted to overcome some of the inherent deficiencies of the traditional SDLC". The main idea of the SDLC has been "to pursue the development of information systems in a very deliberate, structured and methodical way, requiring each stage of the life cycle––from the inception of the idea to delivery of the final system––to be carried out rigidly and sequentially" within the context of the framework being applied.

Other methodologies were devised later:

**1970s**

- Structured programming since 1969
- Cap Gemini SDM, originally from PANDATA, the first English translation was published in 1974. SDM stands for System Development Methodology

**1980s**

- Structured systems analysis and design method (SSADM) from 1980 onwards
- Information Requirement Analysis/Soft systems methodology

**1990s**

- Object-oriented programming (OOP) developed in the early 1960s and became a dominant programming approach during the mid-1990s
- Rapid application development (RAD), since 1991
- Dynamic systems development method (DSDM), since 1994
- Scrum, since 1995
- Team software process, since 1998
- Rational Unified Process (RUP), maintained by IBM since 1998
- Extreme programming, since 1999

**2000s**

- Agile Unified Process (AUP) maintained since 2005 by Scott Ambler
- Disciplined agile delivery (DAD) Supersedes AUP

**2010s**

- Scaled Agile Framework (SAFe)
- Large-Scale Scrum (LeSS)
- DevOps

Since DSDM in 1994, all of the methodologies on the above list except RUP have been agile methodologies - yet many organizations, especially governments, still use pre-agile processes (often waterfall or similar).

### Examples

The following are notable methodologies somewhat ordered by popularity.

**Agile**

Agile software development refers to a group of frameworks based on iterative development, where requirements and solutions evolve via collaboration between self-organizing cross-functional teams. The term was coined in the year 2001 when the Agile Manifesto was formulated.

**Waterfall**

The waterfall model is a sequential development approach, in which development flows one way (like a waterfall) through the SDLC phases.

**Spiral**

In 1988, Barry Boehm published a software system development spiral model, which combines key aspects of the waterfall model and rapid prototyping, in an effort to combine advantages of top-down and bottom-up concepts. It emphases a key area many felt had been neglected by other methodologies: deliberate iterative risk analysis, particularly suited to large-scale complex systems.

**Incremental**

Various methods combine linear and iterative methodologies, with the primary objective of reducing inherent project risk by breaking a project into smaller segments and providing more ease-of-change during the development process.

**Prototyping**

Software prototyping is about creating prototypes, i.e. incomplete versions of the software program being developed.

**Rapid**

Rapid application development (RAD) is a methodology which favors iterative development and the rapid construction of prototypes instead of large amounts of up-front planning. The "planning" of software developed using RAD is interleaved with writing the software itself. The lack of extensive pre-planning generally allows software to be written much faster and makes it easier to change requirements.

**Shape Up**

Shape Up is a software development approach introduced by Basecamp in 2018. It is a set of principles and techniques that Basecamp developed internally to overcome the problem of projects dragging on with no clear end. Its primary target audience is remote teams. Shape Up has no estimation and velocity tracking, backlogs, or sprints, unlike waterfall, agile, or scrum. Instead, those concepts are replaced with appetite, betting, and cycles. As of 2022, besides Basecamp, notable organizations that have adopted Shape Up include UserVoice and Block.

**Chaos**

Chaos model has one main rule: always resolve the most important issue first.

**Incremental funding**

Incremental funding methodology - an iterative approach.

**Lightweight**

Lightweight methodology - a general term for methods that only have a few rules and practices.

**Structured systems analysis and design**

Structured systems analysis and design method - a specific version of waterfall.

**Slow programming**

As part of the larger slow movement, emphasizes careful and gradual work without (or minimal) time pressures. Slow programming aims to avoid bugs and overly quick release schedules.

**V-Model**

V-Model (software development) - an extension of the waterfall model.

**Unified Process**

Unified Process (UP) is an iterative software development methodology framework, based on Unified Modeling Language (UML). UP organizes the development of software into four phases, each consisting of one or more executable iterations of the software at that stage of development: inception, elaboration, construction, and guidelines.

### Comparison

The waterfall model describes the SDLC phases such that each builds on the result of the previous one. Not every project requires that the phases be sequential. For relatively simple projects, phases may be combined or overlapping. Alternative methodologies to waterfall are described and compared below.

| MethologyMetric | Water­fall | RAD | Open source | OOP | JAD | Proto­typing | End-user |
|---|---|---|---|---|---|---|---|
| Control | Formal | MIS | Weak | Standards | Joint | User | User |
| Time frame | Long | Short | Medium | Any | Medium | Short | Short – |
| Users | Many | Few | Few | Varies | Few | One or two | One |
| MIS staff | Many | Few | Hundreds | Split | Few | One or two | None |
| Transaction/DSS | Transaction | Both | Both | Both | DSS | DSS | DSS |
| Interface | Minimal | Minimal | Weak | Windows | Crucial | Crucial | Crucial |
| Documentation and training | Vital | Limited | Internal | In Objects | Limited | Weak | None |
| Integrity and security | Vital | Vital | Unknown | In Objects | Limited | Weak | Weak |
| Reusability | Limited | Some | Maybe | Vital | Limited | Weak | None |

## Process meta-models

Some process models are abstract descriptions for evaluating, comparing, and improving the specific process adopted by an organization.

**ISO/IEC 12207**

ISO/IEC 12207 is the international standard describing the method to select, implement, and monitor the life cycle for software.

**Capability Maturity Model Integration**

The Capability Maturity Model Integration (CMMI) is one of the leading models and is based on best practices. Independent assessments grade organizations on how well they follow their defined processes, not on the quality of those processes or the software produced. CMMI has replaced CMM.

**ISO 9000**

ISO 9000 describes standards for a formally organized process to manufacture a product and the methods of managing and monitoring progress. Although the standard was originally created for the manufacturing sector, ISO 9000 standards have been applied to software development as well. Like CMMI, certification with ISO 9000 does not guarantee the quality of the end result, only that formalized business processes have been followed.

**ISO/IEC 15504**

ISO/IEC 15504 *Information technology—Process assessment*, a.k.a. Software Process Improvement Capability Determination (SPICE), is a framework for the assessment of software processes. This standard is aimed at setting out a clear model for process comparison. SPICE is used much like CMMI. It models processes to manage, control, guide, and monitor software development. This model is then used to measure what a development organization or project team actually does during software development. This information is analyzed to identify weaknesses and drive improvement. It also identifies strengths that can be continued or integrated into common practice for that organization or team.

**ISO/IEC 24744**

ISO/IEC 24744 *Software Engineering—Metamodel for Development Methodologies*, is a power type-based metamodel for software development methodologies.

**Soft systems methodology**

Soft systems methodology is a general method for improving management processes.

**Method engineering**

Method engineering is a general method for improving information system processes.
