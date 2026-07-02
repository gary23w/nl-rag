---
title: "What is platform engineering?"
source: https://platformengineering.org/blog/what-is-platform-engineering
domain: platform-engineering
license: CC-BY-SA-4.0
tags: platform engineering, cognitive load reduction, product mindset infrastructure, platform team
fetched: 2026-07-02
---

# What is platform engineering?

‍

Platform engineering is the discipline of designing and building toolchains and workflows that enable self-service capabilities for software engineering organizations in the cloud-native era. Platform engineers provide an integrated product most often referred to as an “Internal Developer Platform” covering the operational necessities of the entire lifecycle of an application. An Internal Developer Platform (IDP) encompasses a variety of technologies and tools, integrated in a manner that reduces cognitive load on developers while retaining essential context and underlying technologies. It helps operations structure their setup and enable developer self-service. Platform engineering done right means providing golden paths and paved roads that match the preferred abstraction level of the individual developer, who interacts with the IDP.

In this article we are going to explore the origins of this discipline and discuss the main focus areas of platform engineers. We will also explain how this fits into the setup of a modern engineering organization and is actually a key component in most advanced development teams.

## From the ashes of DevOps: the rise of Internal Developer Platforms

Let’s turn the clock back a couple of decades. The late 90s and early 2000s, the time most setups had a single gatekeeper (and point of failure), the SysAdmin. If developers wanted to get anything done to run their applications, they had to go through them. In practice, this translated to the well-known “throw over the fence” workflow, which led to poor experiences on both sides of the fence. As an industry, we all agreed this was not the ideal we should aspire to.

At the same time that cloud started becoming a thing, with AWS launching in 2006, the concept of DevOps gained ground and established itself as the new golden standard for engineering teams. While cloud native drove huge improvements in areas like scalability, availability and operability, it also meant setups became a lot more complex. Gone were the days of running a single script to deploy a monolithic application consuming one relational database.

Suddenly, engineers had to master 10 different tools, Helm charts, Terraform modules, etc. just to deploy and test a simple code change to one of multiple environments in your multi-cluster microservice setup. The problem is that throughout this toolchain evolution, the industry seemingly decided that division of labor (Ops and Devs), which proved successful in virtually every other sector of the global economy, was not a good idea. Instead, the DevOps paradigm was championed as the way to achieve a high performing setup.

**Developers should be able to deploy and run their apps and services end to end. “You build it, you run it”. True DevOps.**

The issue with this approach is that for most companies, this is actually rather unrealistic. While the above works for very advanced organizations like Google, Amazon or Airbnb, it is very far from trivial to replicate true DevOps in practice for most other teams. The main reason being it is unlikely most companies have access to the same talent pool and the same level of resources they can invest into just optimizing their developer workflows and experience.

Instead, what tends to happen when a regular engineering organization tries to implement true DevOps, is that a series of antipatterns emerge. This is well documented by the Team Topologies team (Matthew Skelton and Manuel Pais, speaker at one of our Platform Engineers meetups) in their analysis of DevOps anti-types, a highly recommended read for anyone who wants to better understand these dynamics. Below, an example of what emerges in many development teams when the organization decides to implement DevOps and remove a formal Ops role or team. Developers (usually the more senior ones) end up taking responsibility for managing environments, infrastructure, etc. This leads to a setup where “shadow operations” are performed by the same engineers whose input in terms of coding and product development is most valuable. Everyone loses. The senior engineer who now becomes responsible for the setup and needs to solve requests from more junior colleagues. The wider organization, which is now misusing some of its most expensive and talented resources and cannot ship features with the same speed and reliability.

This type of antipatterns has been shown by a number of studies, such as the State of DevOps by Puppet or, most recently, by Humanitec’s Benchmarking study. In the latter, top and low performing organizations were clustered, based on standard DevOps metrics (lead time, deployment frequency, MTTR, etc.). As shown below, a stunning 44% of low performing organizations experience the above antipattern, with some developers doing DevOps tasks on their own and helping less experienced colleagues. This is compared to top performers, where 100% of the organizations have successfully implemented a true “you build it, you run it” approach.

So what is the key difference between low and top performing organizations? How do the best teams ensure their developers can run their apps and services, without the constant need for help by senior colleagues? You guessed it, they have a platform team building an Internal Developer Platform. The State of DevOps Report 2020 by Puppet clearly shows the correlation between the use of internal platforms and the degree of DevOps evolution of organizations.

That is what the best engineering organizations do. They set up internal platform teams who build IDPs. When using these IDPs, developers can pick the right level of abstraction to run their apps and services, depending on their preference, i.e. do they like messing around with Helm charts, YAML files and Terraform modules? Great, they can do so. Are they a junior frontend who doesn’t care if the app is running on EKS? Fantastic, they can just self-serve an environment that comes fully provisioned with everything they need to deploy and test their code, without worrying where it runs.

## Golden paths and paved roads

What do we mean by golden paths and paved roads? Let’s be more specific. Today, most CI/CD setups are focused on simply updating images. CI builds them, updates the image path in configs, done. That covers most of the deployment use cases. But things start getting more complex and time consuming, whenever we need to do anything beyond this basic workflow, such as:

- Adding environment variables and changing configurations
- Adding services and dependencies
- Rolling back and debugging
- Spinning up a new environment
- Refactoring
- Adding/changing resources
- Enforcing RBAC

The list goes on. Platform engineering is about binding all of this into a paved road. Rather than letting everybody operate everything and having to understand the entire toolchain to do so, platform engineers provide the glue to bind everything into a consistent self-service experience.

This glue is the internal platform. In the words of Evan Bottcher (Thoughtworks), platforms are “a foundation of self-service APIs, tools, services, knowledge and support, which are arranged as a compelling internal product. Autonomous delivery teams can make use of the platform to deliver product features at a higher pace, with reduced coordination.”

Building on top of this definition, Humanitec’s Kaspar von Gruenberg defines an Internal Developer Platform as a “the sum of all the tech and tools that a platform engineering team binds together to pave golden paths for developers.”

## Principles of platform engineering

Many organizations are waking up to the benefits of Internal Developer Platforms and developer self-service. To cite Puppet’s State of DevOps Report 2021, “The existence of a platform team does not inherently unlock higher evolution DevOps; however, great platform teams scale out the benefits of DevOps initiatives.”

Hiring the right talent to build such platforms and workflows though can be tricky. And even trickier is to ensure they consistently deliver a reliable product to the rest of the engineering organization, incorporating their feedback into the IDP.

Below are some helpful principles that I see are a common thread among successful platform teams and self-service driven organizations:

### Clear mission and role

The platform team needs a clear mission. An example: “Build reliable workflows that allow engineers to independently interact with our setup and self-serve the infrastructure they need to run their apps and services”. Whatever makes the most sense for your team, make sure this is defined from the get go. It is also extremely important to establish a clear role for the platform team, which shouldn’t be seen as yet another help desk that spins up environments on demand, but rather as a dedicated product team serving internal customers.

### Treat your platform as a product

Expanding on the product focus, the platform team needs to be driven by a product mindset. They need to focus on what provides real value to their internal customers, the app developers, based on the feedback they gave them. Make sure they ship features based on this feedback loop and don’t get distracted by playing around with a shiny new technology that just came out.

### Focus on common problems

Platform teams prevent other teams within from reinventing the wheel by tackling shared problems over and over. It’s key to figure out what these common issues are: start by understanding developer pain points and friction areas that cause slowdowns in development. This information can be gathered both qualitatively through developers’ feedback and quantitatively, looking at engineering KPIs.

### Glue is valuable

Often platform teams are seen as a pure cost center, because they don’t ship any actual product features for the end user. They are only glueing together our systems after all. This is a very dangerous perspective and, of course, that glue is extremely valuable. Platform engineers need to embrace and advertise themselves and their value proposition internally. Once you have designed the golden paths and paved roads for your teams, the main value you create as a platform team is to be the sticky glue that brings the toolchain together and ensures a smooth self-service workflow for your engineers.

### Don’t reinvent the wheel

The same way platform teams should prevent other teams within the organization from reinventing the wheel and finding new creative solutions to the same problems, they should avoid falling into the same fallacy. It doesn’t matter if your homegrown CI/CD solution is superior today, commercial vendors will catch up eventually. Platform teams should always ask what is their differentiator. Instead of building in-house alternatives to a CI system or a metrics dashboard and compete against businesses that have 20 or 50 times their capacity, they should focus on the specific needs of their organization and tailor off-the-shelf solutions to their requirements. Commercial competitors are more likely to optimize for more generic needs of the industry anyway.

## The modern engineering organisation

According to Puppet’s State of DevOps Report 2021, “highly evolved organizations tend to follow the Team Topologies model”.

Published in 2019, the book Team Topologies by Matthew Skelton and Manuel Pais became one of the most influential blueprints for modern team setups in successful engineering organisations. According to their blueprint, there are four fundamental topologies teams should structure themselves around.

- Stream-aligned team: aligned to a flow of work from a segment of the business domain, they work on core business logic.
- Enabling team: helps stream-aligned teams to overcome obstacles and detects missing capabilities.
- Complicated subsystem team: forms whenever significant mathematical/technical expertise is needed.
- Platform team: provides a compelling internal platform to accelerate delivery by stream-aligned teams

As painted in the graphic above, the platform team is transversal to all others, ensuring a smooth self-service workflow, from code to production.

## When should you look at this?

A common misconception is that platform engineering is something that only makes sense in large teams. And while if your team is composed of 5 developers, a platform team and IDP are surely an overkill, as soon as your organization grows past the 20-30 developers mark, an Internal Developer Platform is probably something you should look at, sooner rather than later. I have heard countless stories of teams who delayed building an IDP for way too long and had to suffer unnecessary hardships, e.g. your only DevOps hire leaves and your whole organization can’t deploy for weeks. IDPs and hiring platform engineers are investments you might want to consider today.

## How to get started

If you are reading this, you are already halfway there. Attend our events, join the Slack channel, engage with other platform engineers and platform nerds. Follow the journey of other teams, such as Adevinta, Flywire and others. Share with the community what your team struggles with and understand when and where self-service might make sense. Check out existing offerings around Internal Developer Platforms to jumpstart your journey. Start lightweight and keep iterating on use-cases.
