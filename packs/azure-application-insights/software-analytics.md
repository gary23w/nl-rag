---
title: "Software analytics"
source: https://en.wikipedia.org/wiki/Software_analytics
domain: azure-application-insights
license: CC-BY-SA-4.0
tags: azure application insights, apm azure, application telemetry azure, distributed tracing azure
fetched: 2026-07-02
---

# Software analytics

**Software analytics** is the analytics specific to the domain of software systems taking into account source code, static and dynamic characteristics (e.g., software metrics) as well as related processes of their development and evolution. It aims at describing, monitoring, predicting, and improving the efficiency and effectiveness of software engineering throughout the software lifecycle, in particular during software development and software maintenance. The data collection is typically done by mining software repositories, but can also be achieved by collecting user actions or production data.

## Definitions

- "Software analytics aims to obtain insightful and actionable information from software artifacts that help practitioners accomplish tasks related to software development, systems, and users." --- centers on analytics applied to artifacts a software system is composed of.
- "Software analytics is analytics on software data for managers and software engineers with the aim of empowering software development individuals and teams to gain and share insight form their data to make better decisions." --- strengthens the core objectives for methods and techniques of software analytics, focusing on both software artifacts and activities of involved developers and teams.
- "Software analytics (SA) represents a branch of big data analytics. SA is concerned with the analysis of all software artifacts, not only source code. [...] These tiers vary from the higher level of the management board and setting the enterprise vision and portfolio management, going through project management planning and implementation by software developers." --- reflects the broad scope including various stakeholders.

## Aims

Software analytics aims at supporting decisions and generating insights, i.e., findings, conclusions, and evaluations about software systems and their implementation, composition, behavior, quality, evolution as well as about the activities of various stakeholders of these processes.

- Insightful information obtained by software analytics conveys meaningful and useful understanding or knowledge towards performing target tasks. Typically, it cannot be easily obtained by direct examining raw big data without the aid of analytics methods and techniques.
- Actionable information obtained by software analytics steers or prescribes solutions that stakeholders in software engineering processes may take (e.g., software practitioners, development leaders, or C-level management).

## Approach

Methods, techniques, and tools of software analytics typically rely on gathering, measuring, analyzing, and visualizing information found in the manifold data sources stored in software development environments and ecosystems. Software systems are well suited for applying analytics because, on the one hand, mostly formalized and precise data is available and, on the other hand, software systems are extremely difficult to manage ---in a nutshell: "software projects are highly measurable, but often unpredictable."

Core data sources include source code, "check-ins, work items, bug reports and test executions [...] recorded in software repositories such as CVS, Subversion, GIT, and Bugzilla." Telemetry data as well as execution traces or logs can also be taken into account.

Automated analysis, massive data, and systematic reasoning support decision-making at almost all levels. In general, key technologies employed by software analytics include analytical technologies such as machine learning, data mining, statistics, pattern recognition, information visualization as well as large-scale data computing & processing. For example, software analytics tools allow users to map derived analysis results by means of software maps, which support interactively exploring system artifacts and correlated software metrics — such as class hierarchies and package coupling in a large Java application. There are also software analytics tools using analytical technologies on top of software quality models in agile software development companies, which support assessing software qualities (e.g., reliability), and deriving actions for their improvement.

## History

In 2009, the term "software analytics" was used in a paper by Dongmei Zhang, Shi Han, Yingnong Dang, Jian-Guang Lou, and Haidong Zhang in part by the Software Analytics Group (SA) at Microsoft Research Asia (MSRA).

The term has since become well known in the software engineering research community after a series of tutorials and talks on software analytics were given by the Software Analytics Group, in collaboration with Tao Xie from North Carolina State University, at software engineering conferences including a tutorial at the IEEE/ACM International Conference on Automated Software Engineering (ASE 2011), a talk at the International Workshop on Machine Learning Technologies in Software Engineering (MALETS 2011), a tutorial and a keynote talk given by Zhang at the IEEE-CS Conference on Software Engineering Education and Training, a tutorial at the International Conference on Software Engineering - Software Engineering in Practice Track, and a keynote talk given by Zhang at the Working Conference on Mining Software Repositories.

In November 2010, Software Development Analytics (Software Analytics with a focus on Software Development) was proposed by Thomas Zimmermann and his colleagues at the Empirical Software Engineering Group (ESE) at Microsoft Research Redmond in their FoSER 2010 paper. A goldfish bowl panel on software development analytics was organized by Zimmermann and Tim Menzies from West Virginia University at the International Conference on Software Engineering, Software Engineering in Practice Track.
