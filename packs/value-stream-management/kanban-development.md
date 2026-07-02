---
title: "Kanban (development)"
source: https://en.wikipedia.org/wiki/Kanban_(development)
domain: value-stream-management
license: CC-BY-SA-4.0
tags: value stream mapping, flow efficiency waste, end to end delivery flow, value stream metrics
fetched: 2026-07-02
---

# Kanban (development)

**Kanban** (Japanese: 看板, meaning *signboard* or *billboard*) is a lean method to manage and improve work across human systems. This approach aims to manage work by balancing demands with available capacity, and by improving the handling of system-level bottlenecks.

Work items are visualized to give participants a view of progress and process, from start to finish—usually via a kanban board. Work is pulled as capacity permits, rather than work being pushed into the process when requested.

In knowledge work and in software development, the aim is to provide a visual process management system which aids decision-making about what, when, and how much to produce. The underlying kanban method originated in lean manufacturing, which was inspired by the Toyota Production System. It has its origin in the late 1940s when the Toyota automotive company implemented a production system called just-in-time, which had the objective of producing according to customer demand and identifying possible material shortages within the production line. But it was a team at Corbis that realized how this method devised by Toyota could become a process applicable to any type of organizational process. Kanban is commonly used in software development in combination with methods and frameworks such as Scrum.

## Kanban boards

The diagram here shows a software development workflow on a kanban board.

Kanban boards, designed for the context in which they are used, vary considerably and may show work item types ("features" and "user stories" here), columns delineating workflow activities, explicit policies, and swimlanes (rows crossing several columns, used for grouping user stories by feature here). The aim is to make the general workflow and the progress of individual items clear to participants and stakeholders.

A Kanban Board represents the system's Definition of Workflow and requires the following minimum elements:

- A definition of the individual units of value that are moving through the workflow. These units of value are referred to as *work items* *(or items*).
- A definition for when work items are *started* and *finished* within the workflow. Your workflow may have more than one started or finished point depending on the work item.
- One or more defined states that the work items flow through from started to finished. Any work items between a started point and a finished point are considered *work in progress* (WIP).
- A definition of how WIP will be controlled from started to finished.
- Explicit policies about how work items can flow through each state from started to finished.
- A *service level expectation* (SLE), which is a forecast of how long it should take a work item to flow from started to finished.

## Kanban practices

The Practices of Kanban as described in the Kanban Guide are

- Defining and visualizing a workflow
- Actively managing items in a workflow
- Improving a workflow

Kanban is a strategy that aims to follow these in order to create systems that are efficient, effective, and predictable.

The Kanban Method is a specialized and detailed extrapolation of Kanban. As described in books on The Kanban Method for software development, the two primary practices of The Kanban Method are to visualize work and to limit work in progress (WIP). Four additional general practices of The Kanban Method listed in *Essential Kanban Condensed* are to make policies explicit, manage flow, implement feedback loops, and improve collaboratively.

The kanban board in the diagram above highlights the first three general practices of The Kanban Method.

- It visualizes the work of the development team (the features and user stories).
- It captures WIP limits for development steps: the circled values below the column headings that limit the number of work items under that step.
- It documents policies, also known as done rules, inside blue rectangles under some of the development steps.
- It also shows some kanban flow management for the "user story preparation", "user story development", and "feature acceptance" steps, which have "in progress" and "ready" sub-columns. Each step's WIP limit applies to both sub-columns, preventing work items from overwhelming the flow into or out of those steps.

## Managing workflow

Kanban manages workflow directly on the kanban board. The WIP limits for development steps provide development teams immediate feedback on common workflow issues.

For example, on the kanban board shown above, the "deployment" step has a WIP limit of five and there are currently five epics shown in that step. No more work items can move into deployment until one or more epics complete that step (moving to "delivered"). This prevents the "deployment" step from being overwhelmed. Team members working on "feature acceptance" (the previous step) might get stuck because they can't deploy new epics. They can see why immediately on the board and help with the current epic deployments.

Once the five epics in the "deployment" step are delivered, the two epics from the "ready" sub-column of "feature acceptance" (the previous step) can be moved to the "deployment" column. When those two epics are delivered, no other epics can be deployed (assuming no new epics are ready). Now, team members working on deployment are stuck. They can see why immediately and help with feature acceptance.

In a Kanban board setup, swimlanes are used to visually organize work into different stages of a process, ensuring clarity and focus. For efficient workflow management, it is crucial to maintain distinct swimlanes for key phases such as requirements, development, testing, and closed/completed tasks. Specifically, testing stories should always be placed within the designated "Testing" swimlane. This separation ensures that testing activities are easily trackable and not intermingled with other stories in development or other stages. By keeping testing tasks within their own swimlane, teams can quickly identify bottlenecks, prioritize issues, and maintain the integrity of the testing process without cross-contamination from development or requirement phases. This structure leads to clearer workflows and enhances team collaboration.

This workflow control works similarly for every step. Problems are visual and evident immediately, and re-planning can be done continuously. The work management is made possible by limiting work in progress in a way team members can see and track at all times.

## Evolution and documentation of method

David Anderson's 2010 book, *Kanban*, describes an evolution of the approach from a 2004 project at Microsoft using a theory-of-constraints approach and incorporating a drum-buffer-rope (comparable to the kanban pull system), to a 2006–2007 project at Corbis (a separate company, also founded by Bill Gates) in which the kanban method was identified. In 2009, Don Reinertsen published a book on second-generation lean product-development which describes the adoption of the kanban system and the use of data collection and an economic model for management decision-making. Another early contribution came from Corey Ladas, whose 2008 book *Scrumban* suggested that kanban could improve scrum for software development. Ladas saw scrumban as the transition from scrum to kanban. Jim Benson and Tonianne DeMaria Barry published *Personal Kanban*, applying kanban to individuals and small teams, in 2011. In *Kanban from the Inside* (2014), Mike Burrows explained kanban's principles, practices and underlying values and related them to earlier theories and models. In *Agile Project Management with Kanban* (2015), Eric Brechner provides an overview of kanban in practice at Microsoft and Xbox. *Kanban Change Leadership* (2015), by Klaus Leopold and Siegfried Kaltenecker, explained the method from the perspective of change management and provided guidance to change-initiatives. In 2016 Lean Kanban University Press published a condensed guide to the method, incorporating improvements and extensions from the early kanban projects.

In 2020 John Coleman and Daniel Vacanti published *The Kanban Guide* to describe the minimal conditions needed to operate a Kanban system. Colleen Johnson, Daniel Vacanti, and Prateek Singh published The Kanban Pocket Guide in 2022, which helps practitioners navigate the Kanban practices. Will Seele and Daniel Vacanti also published the Flow Metrics for Scrum Teams book in 2022 to bring the benefits of metrics commonly used in Kanban to Scrum teams.
