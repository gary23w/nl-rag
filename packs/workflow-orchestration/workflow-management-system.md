---
title: "Workflow management system"
source: https://en.wikipedia.org/wiki/Workflow_management_system
domain: workflow-orchestration
license: CC-BY-SA-4.0
tags: workflow orchestration, directed acyclic graph, task scheduling, pipeline automation, data orchestration
fetched: 2026-07-02
---

# Workflow management system

A **workflow management system** (**WfMS** or **WFMS**) provides an infrastructure for the set-up, performance, and monitoring of a defined sequence of tasks arranged as a workflow application.

## International standards

There are several international standards-setting bodies in the field of workflow management:

- Workflow Management Coalition
- World Wide Web Consortium
- Organization for the Advancement of Structured Information Standards
- WS-BPEL 2.0 (integration-centric) and WS-BPEL4People (human task-centric), published by the OASIS Standards Body.

The underlying theoretical basis of workflow management is the mathematical concept of a Petri net.

Each of the workflow models has tasks (nodes) and dependencies between the nodes. Tasks are activated when the dependency conditions are fulfilled.

## Workflows for people

WfMS allows the user to define different workflows for different types of jobs or processes. For example, in a manufacturing setting, a design document might be automatically routed from a designer to a technical director to the production engineer. At each stage in the workflow, one individual or group is responsible for a specific task. Once the task is complete, WfMS ensures that the individuals responsible for the next task are notified and receive the data they need to execute their stage of the process.

Workflows can also have more complex dependencies; for example, if a document is to be translated into several languages, a translation manager could select the languages and each selection would then be activated as a work order form for a different translator. Only when all the translators have completed their respective tasks would the next task in the process be activated. It is process management from the top level to the lower level.

WfMS also automates redundant tasks and ensures that uncompleted tasks are followed up. A key standard that deals with human tasks in workflows is the WS-BPEL4People Standard by the OASIS Standards Body.

## Automated workflows

WfMS may control automated processes in addition to replacing paperwork order transfers.

For example, if the above design documents are now available as AutoCAD but the workflow requires them as Catia, then an automated process would implement the conversion prior to notifying the individual responsible for the next task. This is the concept of enterprise application integration.

WfMS also appears in distributed IT environments such as grid computing or cloud computing. Such systems aim to manage the execution of various processes that may belong to the same application while in many cases they are used as a means to guarantee the offered quality of service (QoS).

WfMS may also be enhanced by using existing enterprise infrastructure such as Microsoft Outlook or Office 365.

## Categories

Components or subsystems of WfMS can be categorized into the following categories:

- Routing system (traffic policemen)

This is the basic function of a WfMS. It conduces to the

routing

of the flow of information or document flow, it transmits the information from one work item to the next one. This feature will not respond to exceptional circumstances.

- Distribution system (cox)

This function is an expansion. It detects exceptional circumstances and transmits the information to designated work positions. With a dynamic assignment, it can assign new tasks to underworked positions, to achieve a continuation or a balance of workload within the workflow.

- Coordination system (foreman)

This function coordinates concurrent activities to prevent resource conflicts or priority conflicts.

- Agent system (labourer)

This function performs automated legwork, relieving the executing instance of operations that require no decision-making.

- Assistant system (expert)

This feature extends the previous features to a process adjustment instance and for proposals for further actions. The basics involve methods of

artificial intelligence

.

## Functional categorization

Workflow systems can be categorized in the following categories based on their functionalities:

- Integration-centric workflow systems
- Human task-centric workflow systems
- XCFG

## List of notable WfMS

- Activiti
- Apache ODE
- Apache Taverna
- Apache Airflow
- Appian
- Bizagi
- Bonita BPM
- Camunda
- CEITON
- Collective Knowledge
- Cuneiform
- IBM BPM
- Imixs-Workflow
- QuickBase
- PRPC
- ProActive
- Pyrus
- Qntrl
- Salesforce.com Process Workflow
- ServiceNow Platform
- SAP Business Workflow
- Windows Workflow Foundation
- YAWL

### ActivityBuilt-in WfMS as part of the function
