---
title: "Azure DevOps Server"
source: https://en.wikipedia.org/wiki/Azure_DevOps_Server
domain: azure-devops
license: CC-BY-SA-4.0
tags: azure devops, azure pipelines, ci cd, continuous integration
fetched: 2026-07-02
---

# Azure DevOps Server

**Azure DevOps Server**, formerly known as **Team Foundation Server** (**TFS**) and **Visual Studio Team System** (**VSTS**), is a Microsoft product that provides version control (either with Team Foundation Version Control (TFVC) or Git), reporting, requirements management, project management (for both agile software development and waterfall teams), automated builds, testing and release management capabilities. It covers the entire application lifecycle and enables DevOps capabilities. Azure DevOps can be used as a back-end to numerous integrated development environments (IDEs) but is tailored for Microsoft Visual Studio and Eclipse on all platforms.

## On-premises vs. online

Azure DevOps is available in two different forms: on-premises ("Server") and online ("Services"). The latter form is called Azure DevOps Services (formerly Visual Studio Online before it was renamed to Visual Studio Team Services in 2015). The cloud service is backed by the Microsoft Azure cloud platform. It uses the same code as the on-premises version of Azure DevOps, with minor modifications, and implements the most recent features. A user signs in using a Microsoft account to set up an environment, creating projects and adding team members. New features developed in short development cycles are added to the cloud version first. These features migrate to the on-premises version as updates, at approximately three-month intervals.

## Architecture

### Server architecture

Azure DevOps is built on multi-tier scalable architecture. The primary structure consists of an application tier responsible for processing logic and maintaining the web application portal (referred to as Team Web Access or TWA). Azure DevOps is built using Windows Communication Foundation web services. To support scalability, the application tier can be load balanced and the data tier can be clustered.

The primary container is the project collection. A project collection is a database that contains a group of Team Projects. Data from the project collection databases is aggregated into the warehouse database, which denormalizes the data in preparation for loading into an Analysis Services cube. The warehouse and the cube allow complex trend reporting and data analysis.

Azure DevOps can integrate with an existing SharePoint farm. To support teams requiring enterprise project scheduling, Azure DevOps also integrates with Microsoft Project Server.

### Extensibility

Microsoft provides two standalone redistributed APIs for connecting to Azure DevOps: a Java SDK and a .NET Framework SDK. These APIs allow for client connectivity to Azure DevOps. Because Azure DevOps is written on a service-oriented architecture, it can communicate with virtually any tool that can call a web service. Another extensible mechanism is subscribing to system alerts: for example, alerts that a work item was changed, or a build completed. When used in an extensible scenario, these alerts can be sent to a web service, triggering actions to alter or update work items (such as implementing advanced business rules or generating work items programmatically based on a given scenario).

The data warehouse can also be extended through the creation of custom data warehouse adapters.

### Clients

Azure DevOps supports Visual Studio 2010 and later, Microsoft Test Manager (MTM) 2012, and 2013. Eclipse, older versions of Visual Studio, and other environments can be plugged into Azure DevOps using the Microsoft Source Code Control Integration Provider.

Microsoft Excel and Microsoft Project are also supported to help manage work items which allows for bulk update, bulk entry and bulk export of work items. Microsoft Project can be used to schedule work when conforming to a waterfall software development methodology. Both Excel and Project support bi-directional updates of data. This allows, for example, project managers to put a schedule in Project, have that work imported into Azure DevOps where developers update the work and then the schedule can be updated.

With Team Foundation Server 2012, Microsoft PowerPoint was also integrated with Azure DevOps to enable rapid storyboard development to help with the requirements management process. The integration provides extensible storyboard shapes that can be used to build any type of interface mockup that can then be animated with PowerPoint's built-in functions. These storyboards can then be linked to work items.

In an effort to handle the growing geographic dispersion of teams and to involve stakeholders earlier and more often in the process, Microsoft added the Feedback Client. This tool allows users to exercise an application, annotate what they are seeing with audio and video, capture screens and provide contextual feedback to the development team.

## Work items

At the heart of Azure DevOps is the "work item", which can be work that needs to be accomplished, a risk to track, a test case, a bug, etc. Work items are defined through the XML documents and are highly extensible. Work items are combined into a **Process Template** that contains these and other pieces of information to provide a development framework. Azure DevOps includes Process Templates for the Microsoft Solutions Framework for Agile, Scrum and CMMI.

Work items can be linked to each other using different relationships to create a hierarchical tree of work items or a flat relationship between work items. Work items can also be linked to external artifacts such as web pages, documents, source code, build results, test results and specific versions of items in source control.

The flexibility in the work item system allows Azure DevOps to play many roles from requirements management to bug tracking, risk and issue tracking, as well as recording the results of reviews. The extensible linking capabilities ensure that traceability from requirements to source code to test cases and results can be accomplished and reported on for auditing purposes as well as historical understanding of changes.

## Source control

Azure DevOps supports two different types of source control – its original source control engine called Team Foundation Version Control (TFVC) and with the release of TFS 2013, it supports Git as a core source control repository.

### Team Foundation Version Control

TFVC is a centralized version control system allowing teams to store any type of artifact within its repository. TFVC supports two different types of workspaces when working with client tools – Server Workspaces and Local Workspaces. Server workspaces allow developers to lock files for check-out and provide notification to other developers that files are being edited. A frequent complaint for this model is that files on the development machine are marked as read-only. It also requires developers to "go offline" when the server can't be contacted. Local workspaces were designed to avoid these problems. In a local workspace scenario files are not read-only and they do not have to be checked out before working on them. As long as the files are on the developer's local machine, it doesn't matter if the server is connected or not. Conflicts are dealt with at check-in time.

To improve performance for remote clients, Azure DevOps includes the ability to install Proxy Servers. Proxy servers allow source control contents to be cached at a site closer to the developers to avoid long network trips and the associated latency. Check-ins are still performed directly against the Azure DevOps application tier so the Proxy Server is most beneficial in read scenarios.

As part of the source control engine, Azure DevOps supports a number of features to help developers ensure the code that is checked in follows configurable rules. Azure DevOps also supports a Code Analysis feature that when used independently is known as FxCop.

### Git

With the release of TFS 2013, Microsoft added native support for Git. This is not a Microsoft specific implementation but a standard implementation based on the libgit2 library. Because Microsoft took the approach of using a standard library, any Git client can now be used natively with Azure DevOps. This allows tools on any platform and any IDE that support Git to connect to Azure DevOps. In addition, if developers do not want to use Microsoft's Team Explorer Everywhere plug-in for Eclipse, they can choose to use eGit to connect to Azure DevOps.

## Reporting

The reporting infrastructure consists of a data warehouse, which is a relational database and a SQL Server Analysis Services data cube. Both of these sources are available for reporting through SQL Server Reporting Services when this option is installed. Since these are standard database and cube structures, any tool which can point to these data sources can report from them. This includes tools such as Cognos, Tableau, Excel and other reporting tools. Included with each out of the box process template is a set of reports for reporting services which cover Build information, Test results and progress, project management, agile reports (Backlog Overview, Release Burndown, Sprint Burndown and Velocity), bug and issue data. New reports can be created using Report Builder for SSRS and any of the existing reports can be modified.

TFS 2013 introduced a new feature called "light-weight reporting" which provides for the ability to create real-time reports based on query results and which do not rely on the warehouse or cube.

## Team Build

Team Build (prior to TFS 2015) is a build server application included with Team Foundation Server. Two components make up Team Build – MSBuild and Windows Workflow Foundation. MSBuild is a declarative XML language similar to Apache Ant.

Windows Workflow controls the overall flow of the build process, and Azure DevOps includes many pre-built workflow activities for managing common tasks that are performed during a build. The build system is extensible with users being able to create their own workflow activities, the ability to inject MSBuild into the process and to execute external processes.

The build process can be configured for various types of builds including scheduled builds, continuous integration, gated check-in and rolling builds.

The build process in Azure DevOps is also part of the traceability mechanism in that Team Build brings together many of the artifacts that are created and stored in Azure DevOps. Assuming developers associate source code with work items on check-in, Team Build has the ability to report on the changes in each build – both source code changes and work item changes as well as test results. As bugs and PBIs are resolved and integrated into builds, the work items which track these artifacts are automatically updated to indicate in which build they were successfully integrated. Combined with the testing tools, testers then get an integrated view of what code was changed in each build, but also which bugs, PBIs and other work changed from build to build.

## Release management

In mid-2013 Microsoft purchased a product called InRelease from InCycle Software. InRelease was fully incorporated into Team Foundation Server 2013. This capability complemented the automated build and testing processes by allowing a true continuous deployment solution. The tools were re-branded "Release Management" for TFS 2013. The Release Management capabilities give teams the ability to perform a controlled, workflow (provided by Windows Workflow Foundation) driven release to development, test and production environments and provides dashboards for monitoring the progress of one or more releases.

## History

This first version of Team Foundation Server was released March 17, 2006.

| Product name | Form | Release year | Version Number |
|---|---|---|---|
| Team Foundation Server 2005 | On-premises | 2006 | 8 |
| Team Foundation Server 2008 | On-premises | 2008 | 9 |
| Team Foundation Server 2010 | On-premises | 2010 | 10 |
| Team Foundation Service Preview | Cloud | 2012 |   |
| Team Foundation Server 2012 | On-premises | 2012 | 11 |
| Visual Studio Online | Cloud | 2013 |   |
| Team Foundation Server 2013 | On-premises | 2013 | 12 |
| Team Foundation Server 2015 | On-premises | 2015 | 14 |
| Visual Studio Team Services | Cloud | 2015 |   |
| Team Foundation Server 2017 | On-premises | 2017 | 15 |
| Team Foundation Server 2018 | On-premises | 2017 | 16 |
| Azure DevOps Services | Cloud | 2018 |   |
| Azure DevOps Server 2019 | On-premises | 2019 | 17 |
| Azure DevOps Server 2020 | On-premises | 2020 | 18 |
| Azure DevOps Server 2022 | On-premises | 2022 |   |
