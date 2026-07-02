---
title: "Data-flow diagram"
source: https://en.wikipedia.org/wiki/Data_flow_diagram
domain: threat-modeling
license: CC-BY-SA-4.0
tags: threat modeling, attack surface analysis, attack tree, data flow diagram, stride threat model
fetched: 2026-07-02
---

# Data-flow diagram

(Redirected from

Data flow diagram

)

A **data-flow diagram** is a way of representing a flow of data through a process or a system (usually an information system). The DFD also provides information about the outputs and inputs of each entity and the process itself. A data-flow diagram has no control flow — there are no decision rules and no loops. Specific operations based on the data can be represented by a flowchart.

There are several notations for displaying data-flow diagrams. The notation presented above was described in 1979 by Tom DeMarco as part of structured analysis.

For each data flow, at least one of the endpoints (source and / or destination) must exist in a process. The refined representation of a process can be done in another data-flow diagram, which subdivides this process into sub-processes.

The data-flow diagram is a tool that is part of structured analysis, data modeling and threat modeling. When using UML, the activity diagram typically takes over the role of the data-flow diagram. A special form of data-flow plan is a site-oriented data-flow plan.

Data-flow diagrams can be regarded as inverted Petri nets, because places in such networks correspond to the semantics of data memories. Analogously, the semantics of transitions from Petri nets and data flows and functions from data-flow diagrams should be considered equivalent.

## History

The DFD notation draws on graph theory, originally used in operational research to model workflow in organizations, and in computer science to model the flow of inputs and outputs across computations. DFD originated from the structured analysis and design technique methodology in the middle of the 1970s. It was first proposed by Larry Constantine, and popularized by Edward Yourdon, Tom DeMarco, Chris Gane and Trish Sarson, who enriched the diagramming technique with different notations, data dictionary practices and guidance for the hierarchical decomposition of processes.

The primary aim of data-flow diagrams in the context of structured design was to build complex modular systems, rationalizing the interdependencies across different modules. Data-flow diagrams (DFD) quickly became a popular way to visualize the major steps and data involved in software-system processes. DFDs were usually used to show data flow in a computer system, although they could in theory as well be applied to business process modeling. DFDs were useful to document the major data flows or to explore a new high-level design in terms of data flow.

## DFD components

DFD consists of processes, flows, warehouses, and terminators. There are several ways to view these DFD components.

**Process**

The process (function, transformation) is part of a system that transforms inputs to outputs. The symbol of a process is a circle, an oval, a rectangle or a rectangle with rounded corners (according to the type of notation). The process is named in one word, a short sentence, or a phrase that is clearly to express its essence.

**Data flow**

Data flow (flow, dataflow) shows the transfer of information (sometimes also material) from one part of the system to another. The symbol of the flow is the arrow. The flow should have a name that determines what information (or what material) is being moved. Exceptions are flows where it is clear what information is transferred through the entities that are linked to these flows. Material shifts are modeled in systems that are not merely informative. Flow should only transmit one type of information (material). The arrow shows the flow direction (it can also be bi-directional if the information to/from the entity is logically dependent—e.g. question and answer). Flows link processes, warehouses and terminators.

**Warehouse**

The warehouse (datastore, data store, file, database) is used to store data for later use. The symbol of the store is two horizontal lines, the other way of view is shown in the DFD Notation. The name of the warehouse is a plural noun (e.g. orders)—it derives from the input and output streams of the warehouse. The warehouse does not have to be just a data file but can also be, for example, a folder with documents, a filing cabinet, or a set of optical discs. Therefore, viewing the warehouse in a DFD is independent of implementation. The flow from the warehouse usually represents reading of the data stored in the warehouse, and the flow to the warehouse usually expresses data entry or updating (sometimes also deleting data). The warehouse is represented by two parallel lines between which the memory name is located (it can be modeled as a UML buffer node).

**Terminator**

The terminator is an external entity that communicates with the system and stands outside of the system. It can be, for example, various organizations (e.g. a bank), groups of people (e.g. customers), authorities (e.g. a tax office) or a department (e.g. a human-resources department) of the same organization, which does not belong to the model system. The terminator may be another system with which the modeled system communicates.

## Rules for creating DFD

Entity names should be comprehensible without further comments. A DFD is a graphical modeling method created by analysts often based on interviews with system users. It is useful for system developers, on one hand, and project contractors on the other, so the entity names should be comprehensible by modelers, users, and system analysts. Entity names should be general (independent, e.g. specific individuals carrying out the activity), but should clearly specify the entity. Processes should be numbered for easier mapping and referral to specific processes. The numbering is random, however, it is necessary to maintain consistency across all DFD levels (see DFD Hierarchy). DFD should be clear, as the maximum number of processes in one DFD is recommended to be from 6 to 9, minimum is 3 processes in one DFD. The exception is the so-called contextual diagram where the only process symbolizes the model system and all terminators with which the system communicates.

## DFD consistency

DFD must be consistent with other models of the system—entity relationship diagram, state-transition diagram, data dictionary, and process specification models. Each process must have its name, inputs and outputs. Each flow should have its name (exception see Flow). Each Data store must have input and output flow. Input and output flows do not have to be displayed in one DFD—but they must exist in another DFD describing the same system. An exception is warehouse standing outside the system (external storage) with which the system communicates.

## DFD hierarchy

To make the DFD more transparent (i.e. not too many processes), multi-level DFDs can be created. DFDs that are at a higher level are less detailed (aggregate more detailed DFD at lower levels). The contextual DFD is the highest in the hierarchy (see DFD Creation Rules). The so-called zero level is followed by DFD 0, starting with process numbering (e.g. process 1, process 2). In the next, the so-called first level—DFD 1—the numbering continues. For example, process 1 is divided into the first three levels of the DFD, which are numbered 1.1, 1.2, and 1.3. Similarly, processes in the second level (DFD 2) are numbered 2.1.1, 2.1.2, 2.1.3, and 2.1.4. The number of levels depends on the size of the model system. DFD 0 processes may not have the same number of decomposition levels. DFD 0 contains the most important (aggregated) system functions. The lowest level should include processes that make it possible to create a process specification for roughly one A4 page. If the mini-specification should be longer, it is appropriate to create an additional level for the process where it will be decomposed into multiple processes. For a clear overview of the entire DFD hierarchy, a vertical (cross-sectional) diagram can be created. The warehouse is displayed at the highest level where it is first used and at every lower level as well.
