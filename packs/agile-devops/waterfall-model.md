---
title: "Waterfall model"
source: https://en.wikipedia.org/wiki/Waterfall_model
domain: agile-devops
license: CC-BY-SA-4.0
tags: agile, scrum, kanban, devops, continuous delivery, pair programming
fetched: 2026-07-02
---

# Waterfall model

The **waterfall model** is the process of performing the typical software development life cycle (SDLC) phases in sequential order. Each phase is completed before the next is started, and the result of each phase drives subsequent phases. Compared to alternative SDLC methodologies such as Agile, it is among the least iterative and flexible, as progress flows largely in one direction (like a waterfall) through the phases of conception, requirements analysis, design, construction, testing, deployment, and maintenance. The waterfall model is the earliest SDLC methodology. When first adopted, there were no recognized alternatives for knowledge-based creative work.

## History

The first known presentation describing the use of such phases in software engineering was held by Herbert D. Benington at the Symposium on Advanced Programming Methods for Digital Computers on 29 June 1956. This presentation was about the development of software for SAGE. In 1983, Benington republished his paper with a foreword explaining that the phases were on purpose organized according to the specialization of tasks, and pointing out that the process was not in fact performed in a strict top-down fashion, but depended on a prototype.

Although the term "waterfall" is not used in the paper, the first formal, detailed diagram of the process is often cited as coming from a 1970 article by Winston W. Royce. However, he commented that it had major flaws stemming from how testing only happened at the end of the process, which he described as being "risky and [inviting] failure". The rest of his paper introduced five steps which he felt were necessary to "eliminate most of the development risks" associated with the unaltered waterfall approach. Royce's five additional steps (which included writing complete documentation at various stages of development) never took mainstream hold, but his diagram of what he considered a flawed process became the starting point when describing a "waterfall" approach.

The earliest use of the term "waterfall" may have been in a 1976 paper by Bell and Thayer.

In 1985, the United States Department of Defense adopted the waterfall model in the DOD-STD-2167 standard for working with software development contractors. This standard referred for iterations of a software development to "the sequential phases of a software development cycle" and stated that "the contractor shall implement a software development cycle that includes the following six phases: Software Requirement Analysis, Preliminary Design, Detailed Design, Coding and Unit Testing, Integration, and Testing".

## Phases

The model describes a linear sequence of steps. Although various different versions can be found, the following describes the essence.

### Preliminary analysis

Conduct a preliminary analysis, consider alternative solutions, estimate costs and benefits, and submit a preliminary plan with recommendations.

- Conduct preliminary analysis: Identify the organization's objectives and define the nature and scope of the project. Ensure that the project fits with the objectives.
- Consider alternative solutions: Alternatives may come from interviewing employees, clients, suppliers, and consultants, as well as competitive analysis.
- Cost-benefit analysis: Analyze the costs and benefits of the project.

### Systems analysis, requirements definition

Decompose project goals into defined functions and operations. This involves gathering and interpreting facts, diagnosing problems, and recommending changes. Analyze end-user information needs and resolve inconsistencies and incompleteness:

- Collect facts: Obtain end-user requirements by document review, client interviews, observation, and questionnaires.
- Scrutinize existing system(s): Identify pros and cons.
- Analyze the proposed system: Find solutions to issues and prepare specifications, incorporating appropriate user proposals.

### Systems design

At this step, desired features and operations are detailed, including screen layouts, business rules, process diagrams, pseudocode, and other deliverables.

### Development

Write the code.

### Integration and testing

Assemble the modules in a testing environment. Check for errors, bugs, and interoperability.

### Acceptance, installation, deployment

Put the system into production. This may involve training users, deploying hardware, and loading information from the prior system.

### Maintenance

Monitor the system to assess its ongoing fitness. Make modest changes and fixes as needed. This helps maintain the quality of the system. Continual monitoring and updates ensure the system remains effective and high-quality.

### Evaluation

The system and the process are reviewed. Relevant questions include whether the newly implemented system meets requirements and achieves project goals, whether the system is usable, reliable/available, properly scaled and fault-tolerant. Process checks include review of timelines and expenses, as well as user acceptance.

### Disposal

At end of life, plans are developed for discontinuing the system and transitioning to its replacement. Related information and infrastructure must be repurposed, archived, discarded, or destroyed, while appropriately protecting security.

## Supporting arguments

Time spent early in the software production cycle can reduce costs at later stages. For example, a problem found in the early stages (such as requirements specification) is cheaper to fix than the same bug found later on in the process (by a factor of 50 to 200).

In common practice, waterfall methodologies result in a project schedule with 20–40% of the time invested for the first two phases, 30–40% of the time to coding, and the rest dedicated to testing and implementation. With the project organization needing to be highly structured, most medium and large projects will include a detailed set of procedures and controls, which regulate every process on the project.

A further argument supporting the waterfall model is that it places emphasis on documentation (such as requirements documents and design documents) as well as source code. In less thoroughly designed and documented methodologies, knowledge is lost if team members leave before the project is completed, and it may be difficult for a project to recover from the loss. If a fully working design document is present (as is the intent of big design up front and the waterfall model), new team members and new teams should be able to familiarise themselves to the project by reading the documents.

The waterfall model provides a structured approach; the model itself progresses linearly through discrete, easily understandable and explainable phases and thus is easy to understand. It also provides easily identifiable milestones in the development process, often being used as a beginning example of a development model in many software engineering texts and courses.

## Criticism

Clients may not know the exact requirements before they see working software and thus change their requirements further on, leading to redesign, redevelopment, and retesting, and increased costs.

Designers may not be aware of future difficulties when designing a new software product or feature, in which case revising the design initially can increase efficiency in comparison to a design not built to account for newly discovered constraints, requirements, or problems.

Organisations may attempt to deal with a lack of concrete requirements from clients by employing systems analysts to examine existing manual systems and analyse what they do and how they might be replaced. However, in practice, it is difficult to sustain a strict separation between systems analysis and programming, as implementing any non-trivial system will often expose issues and edge cases that the systems analyst did not consider.

Some organisations, such as the United States Department of Defense, now have a stated preference against waterfall-type methodologies, starting with MIL-STD-498 released in 1994, which encourages *evolutionary acquisition* and *iterative and incremental development*.

## Modified waterfall models

In response to perceived problems with the original, pure waterfall model, many modified versions have been devised to address the problems. These include the rapid development models that Steve McConnell calls "modified waterfalls": Peter DeGrace's "sashimi model" (waterfall with overlapping phases), waterfall with subprojects, and waterfall with risk reduction. Other software development model combinations such as "incremental waterfall model" also exist.

Royce's final model illustrated that feedback could (should, and often would) lead from code testing to design (as testing of code uncovered flaws in the design) and from design back to requirements specification (as design problems may necessitate the removal of conflicting or otherwise unsatisfiable/undesignable requirements). In the same paper Royce also advocated large quantities of documentation, doing the job "twice if possible" (a sentiment similar to that of Fred Brooks, famous for writing the Mythical Man Month — an influential book in software project management — who advocated planning to "throw one away"), and involving the customer as much as possible (a sentiment similar to that of extreme programming).

Royce notes on the final model are:

1. Complete program design before analysis and coding begins
2. Documentation must be current and complete
3. Do the job twice if possible
4. Testing must be planned, controlled, and monitored
5. Involve the customer
