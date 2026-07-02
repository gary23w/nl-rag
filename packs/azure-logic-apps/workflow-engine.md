---
title: "Workflow engine"
source: https://en.wikipedia.org/wiki/Workflow_engine
domain: azure-logic-apps
license: CC-BY-SA-4.0
tags: azure logic apps, workflow automation azure, integration workflow azure, low code integration
fetched: 2026-07-02
---

# Workflow engine

A **workflow engine** is a software application that manages business processes. It is a key component in workflow technology and typically makes use of a database server.

A workflow engine manages and monitors the state of activities in a workflow, such as the processing and approval of a loan application form, and determines which new activity to transition to according to defined processes (workflows). The actions may be anything from saving an application form in a document management system to sending a reminder e-mail to users or escalating overdue items to management. A workflow engine facilitates the flow of information, tasks, and events. Workflow engines may also be referred to as Workflow Orchestration Engines.

Workflow engines mainly have three functions:

- Verification of the current process status: Check whether it is valid executing a task, given current status.
- Determine the authority of users: Check if the current user is permitted to execute the task.
- Executing condition script: After passing the previous two steps, the workflow engine executes the task, and if the execution successfully completes, it returns the success, if not, it reports the error to trigger and roll back the change.

A workflow engine is a core technique for task allocation software, such as business process management, in which the workflow engine allocates tasks to different executors while communicating data among participants. A workflow engine can execute any arbitrary sequence of steps, for example, a healthcare data analysis.
