---
title: "Workflow"
source: https://en.wikipedia.org/wiki/Workflow
domain: prefect
license: CC-BY-SA-4.0
tags: prefect orchestration, dataflow automation, workflow engine, task retries, pipeline scheduling
fetched: 2026-07-02
---

# Workflow

**Workflow** is a generic term for orchestrated and repeatable patterns of activity, enabled by the systematic organization of resources into processes that transform materials, provide services, or process information. It can be depicted as a sequence of operations, the work of a person or group, the work of an organization of staff, or one or more simple or complex mechanisms.

From a more abstract perspective, workflow may be considered a view or representation of real work. The flow being described may refer to a document, service, or product that is being transferred from one step to another.

Workflows may be viewed as fundamental building blocks to be combined with other parts of an organization's structure, such as information technology, teams, projects, and hierarchies.

## Historical development

The development of the workflow concept occurred across several loosely defined, overlapping eras.

### Beginnings in manufacturing

The modern history of workflows can be traced to Frederick Taylor and Henry Gantt, although the term "workflow" was not used in this context during their lifetimes. One of the earliest instances of the term "work flow" was in a railway engineering journal from 1921.

Taylor and Gantt launched the study of the deliberate, rational organization of work, primarily in the context of manufacturing. This gave rise to time and motion studies. Related concepts include job shops and queuing systems (Markov chains).

The 1948 book *Cheaper by the Dozen* introduced the emerging workflow concept to the context of family life.

### Maturation and growth

The invention of the typewriter and the copier helped spread the study of the rational organization of labor from the manufacturing shop floor to the office. Filing and other sophisticated systems for managing physical information flows evolved. Several events likely contributed to the development of formalized information workflows. First, the field of optimization theory matured and developed mathematical optimization techniques. For example, Soviet mathematician and economist Leonid Kantorovich developed the seeds of linear programming in 1939 through efforts to solve a plywood manufacturer's production optimization issues. Second, World War II and the Apollo program drove process improvement forward with their demands for the rational organization of work.

### Quality era

In the postwar era, the work of W. Edwards Deming and Joseph M. Juran led to a focus on quality, first in Japanese companies, and more globally from the 1980s. There were various movements ranging from total quality management to Six Sigma, and then more qualitative notions of business process re-engineering. This led to more efforts to improve workflows in both knowledge economy sectors and manufacturing. Thought leaders recognized variable demands on workflows when they considered the theory of critical paths and moving bottlenecks.

## Workflow management

Basu and Kumar noted that the term "workflow management" referred to tasks associated with the flow of information through the value chain rather than the flow of material goods: they characterise the definition, analysis and management of information as "workflow management". They note that workflow can be managed within a single organisation, where distinct roles are allocated to individual resources, and also across multiple organisations or distributed locations, where attention needs to be paid to the interactions between activities which are located at the organizational or locational boundaries. The transmission of information from one organization to another is a critical issue in this inter-organizational context and raises the importance of tasks they describe as "validation", "verification" and "data usage analysis".

## Workflow management systems

A workflow management system (WfMS) is a software system for creating, executing, and monitoring a defined sequence of processes and tasks, with the broad goals of increasing productivity, reducing costs, becoming more agile, and improving information exchange within an organization. These systems may be process-centric or data-centric, and they may also represent the workflow as graphical maps. A workflow management system may also include an extensible interface so that external software applications can be integrated, providing support for wide area workflows that provide both faster response times and improved productivity.

The workflow concept is closely related to several fields in operations research and other areas that study the nature of work either quantitatively or qualitatively, such as artificial intelligence (in particular, the sub-discipline of AI planning) and ethnography. The term "workflow" is more commonly used in particular industries like printing, as well as professional domains such as clinical laboratories. It may have particular specialized meanings in these areas.

1. **Processes**: A process is a more general notion than workflow and can apply to, for example, physical or biological processes, whereas a workflow is typically a process or collection of processes described in the context of work, such as all processes occurring in a machine shop.
2. **Planning and scheduling**: A plan is a description of the logically necessary, partially ordered set of activities required to accomplish a specific goal given certain starting conditions. A plan, when augmented with a schedule and resource allocation calculations, completely defines a particular *instance* of systematic processing in pursuit of a goal. A workflow may be viewed as an often optimal or near-optimal realization of the mechanisms required to execute the same plan repeatedly.
3. **Flow control**: This is a control concept applied to workflows, to distinguish from static control of buffers of material or orders, to mean a more dynamic control of flow speed and flow volumes in motion and in process. Such orientation to dynamic aspects is the basic foundation to prepare for more advanced job shop controls, such as just-in-time or just-in-sequence.
4. **In-transit visibility**: This monitoring concept applies to transported material as well as to work in process or work in progress, i.e., workflows.

## Examples

The following examples illustrate the variety of workflows seen in various contexts:

1. In machine shops, particularly job shops and flow shops, the flow of a part through the various processing stations is a workflow.
2. Insurance claims processing is an example of an information-intensive, document-driven workflow.
3. Wikipedia editing can be modeled as a stochastic workflow.
4. The Getting Things Done system is a model of personal workflow management for information workers.
5. In software development, support and other industries, the concept of *follow-the-sun* describes a process of passing unfinished work across time zones.
6. In traditional offset and digital printing, the concept of workflow represents the process, people, and usually software technology (RIPs raster image processors or DFE digital front end) controllers that play a part in pre/post processing of print-related files, e.g., PDF pre-flight checking to make certain that fonts are embedded or that the imaging output to plate or digital press will be able to render the document intent properly for the image-output capabilities of the press that will print the final image.
7. In scientific experiments, the overall process (tasks and data flow) can be described as a directed acyclic graph (DAG). This DAG is referred to as a workflow, e.g., Brain Imaging workflows.
8. In healthcare data analysis, a workflow can be identified or used to represent a sequence of steps that comprise a complex data analysis.
9. In service-oriented architectures, an application can be represented through an executable workflow, where different, possibly geographically distributed, service components interact to provide the corresponding functionality under the control of a workflow management system.
10. In shared services, an application can be in the practice of developing robotic process automation (called RPA or RPAAI for self-guided RPA 2.0 based on artificial intelligence) which results in the deployment of attended or unattended software agents to an organization's environment. These software agents, or robots, are deployed to perform pre-defined structured and repetitive sets of business tasks or processes. Artificial intelligence software robots are deployed to handle unstructured data sets and are deployed after performing and deploying robotic process automation.

## Features and phenomenology

1. Modeling: Workflow problems can be modeled and analyzed using graph-based formalisms like Petri nets.
2. Measurement: Many of the concepts used to measure scheduling systems in operations research are useful for measuring general workflows. These include throughput, processing time, and other regular metrics.
3. Specialized connotations: The term "workflow" has specialized connotations in information technology, document management, and imaging. Since 1993, one trade consortium specifically focused on workflow management and the interoperability of workflow management systems, the Workflow Management Coalition.
4. Scientific workflow systems: These found wide acceptance in the fields of bioinformatics and cheminformatics in the early 2000s, when they met the need for multiple interconnected tools that handle multiple data formats and large data quantities. Also, the paradigm of scientific workflows resembles the well-established practice of Perl programming in life science research organizations, making this adoption a natural step towards more structured infrastructure setup.
5. Human-machine interaction: Several conceptualizations of mixed-initiative workflows have been studied, particularly in the military, where automated agents play roles just as humans do. For innovative, adaptive, and collaborative human work, the techniques of human interaction management are required.
6. Workflow analysis: Workflow systems allow users to develop executable processes with no familiarity with formal programming concepts. Automated workflow analysis techniques can help users analyze the properties of user workflows to conduct verification of certain properties before executing them, e.g., analyzing flow control or data flow. Examples of tools based on formal analysis frameworks have been developed and used for the analysis of scientific workflows and can be extended to the analysis of other types of workflows.

## Workflow improvement theories

Several workflow improvement theories have been proposed and implemented in the modern workplace. These include:

1. Six Sigma
2. Total Quality Management
3. Business Process Reengineering
4. Lean systems
5. Theory of constraints

Resource evaluation (both physical and human) is essential to evaluating hand-off points and creating smoother transitions between tasks.

## Components

A workflow can usually be described using formal or informal flow diagramming techniques and displays directed flows between processing steps. Single processing steps or components of a workflow can basically be defined by three parameters:

1. input description: the information, material and energy required to complete the step
2. transformation rules: algorithms which may be carried out by people or machines, or both
3. output description: the information, material, and energy produced by the step and provided as input to downstream steps

Components can only be plugged together if the output of one previous (set of) component(s) is equal to the mandatory input requirements of the following component(s). Thus, the essential description of a component actually comprises only input and output that are described fully in terms of data types and their meaning (semantics). The algorithms' or rules' descriptions need only be included when there are several alternative ways to transform one type of input into one type of output – possibly with different accuracy, speed, etc.

When the components are non-local services that are invoked remotely via a computer network, such as Web services, developers must consider additional descriptors (such as QoS and availability).

## Applications

A workflow application is a software application that automates a process or processes to some degree. These processes are usually business-related but can be any process that requires a series of steps to be automated via software. Some process steps may require human intervention, such as development and approval of custom text, but functions that can be automated should be handled by the application. Advanced applications allow users to introduce new components into the operation.
