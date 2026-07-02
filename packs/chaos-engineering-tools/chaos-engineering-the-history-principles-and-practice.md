---
title: "Chaos Engineering: the history, principles, and practice"
source: https://www.gremlin.com/community/tutorials/chaos-engineering-the-history-principles-and-practice
domain: chaos-engineering-tools
license: CC-BY-SA-4.0
tags: chaos engineering, fault injection, resilience testing, failure injection
fetched: 2026-07-02
---

# Chaos Engineering: the history, principles, and practice

Last Updated:

October 12, 2023

Topics:

Chaos Engineering

,

Learn the history behind Chaos Engineering, how to apply it, and how it helps improve reliability.

This is an older tutorial

We strive to keep all tutorials current. However, this tutorial has not been updated recently and may contain out-of-date instructions.

With the rise of microservices and distributed cloud architectures, the web has grown increasingly complex. We all depend on these systems more than ever, yet failures have become much harder to predict.

These failures cause costly outages for companies. The outages hurt customers trying to shop, transact business, and get work done. Even brief outages can impact a company's bottom line, so the cost of downtime is becoming a KPI for many engineering teams. For example, in 2017, 98% of organizations said a single hour of downtime would cost their business over $100,000. One outage can cost a single company millions of dollars. The CEO of British Airways recently explained how one failure that stranded tens of thousands of British Airways (BA) passengers in May 2017 cost the company 80 million pounds ($102.19 million USD).

Companies need a solution to this challenge—waiting for the next costly outage is not an option. To meet the challenge head on, more and more companies are turning to Chaos Engineering.

**Chaos Engineering is Preventive Medicine**

Chaos Engineering is a disciplined approach to identifying failures before they become outages. By proactively testing how a system responds under stress, you can identify and fix failures before they end up in the news.

Chaos Engineering lets you compare what you think will happen to what actually happens in your systems. You literally “break things on purpose” to learn how to build more resilient systems.

(If you’re here to get started with Chaos Engineering, you can get free access to all of Gremlin for 30 days. Run your first Chaos Engineering experiments and identify hidden risks in your systems by signing up.)

## What are the Principles of Chaos Engineering?

Chaos Engineering involves running thoughtful, planned experiments that teach us how our systems behave in the face of failure.

These experiments follow three steps:

You start by forming a hypothesis about how a system should behave when something goes wrong.

Then, you design the smallest possible experiment to test it in your system.

Finally, you measure the impact of the failure at each step, looking for signs of success or failure. When the experiment is over, you have a better understanding of your system's real-world behavior.

## Which companies practice Chaos Engineering?

Many larger tech companies practice Chaos Engineering to better understand their distributed systems and microservice architectures. The list includes Twilio, Netflix, LinkedIn, Facebook, Google, Microsoft, Amazon, and many others. The list is always growing.

But more traditional industries, like banking and finance, have caught on to Chaos Engineering, too. For example, in 2014, the National Australia Bank migrated from physical infrastructure to Amazon Web Services and used Chaos Engineering to dramatically reduce incident counts.

The Chaos Engineering Slack Community has created a diagram that tracks known Chaos Engineering tools and known engineers working on Chaos Engineering.

## Why would you break things on purpose?

Think of a vaccine or a flu shot, where you inject yourself with a small amount of a potentially harmful foreign body in order to build resistance and prevent illness. Chaos Engineering is a tool we use to build such an immunity in our technical systems by injecting harm (like latency, CPU failure, or network black holes) in order to find and mitigate potential weaknesses.

These experiments have the added benefit of helping teams build muscle memory in resolving outages, akin to a fire drill (or changing a flat tire, in the Netflix analogy). By breaking things on purpose we surface unknown issues that could impact our systems and customers.

According to the 2021 State of Chaos Engineering report, the most common outcomes of Chaos Engineering are increased availability, lower mean time to resolution (MTTR), lower mean time to detection (MTTD), fewer bugs shipped to product, and fewer outages. Teams who frequently run Chaos Engineering experiments are more likely to have >99.9% availability.

## What's the role of Chaos Engineering in distributed systems?

Distributed systems are inherently more complex than monolithic systems, so it’s hard to predict all the ways they might fail. The eight fallacies of distributed systems shared by Peter Deutsch and others at Sun Microsystems describe false assumptions that programmers new to distributed applications invariably make.

### Fallacies of Distributed Systems:

- The network is reliable
- Latency is zero
- Bandwidth is infinite
- The network is secure
- Topology doesn't change
- There is one administrator
- Transport cost is zero
- The network is homogeneous

Many of these fallacies drive the design of Chaos Engineering experiments such as “packet-loss attacks” and “latency attacks”. For example, network outages can cause a range of failures for applications that severely impact customers. Applications may stall while they wait endlessly for a packet. Applications may permanently consume memory or other Linux system resources. And even after a network outage has passed, applications may fail to retry stalled operations, or may retry too aggressively. Applications may even require a manual restart. Each of these examples need to be tested and prepared for.

## What are the customer, business, and technical benefits of Chaos Engineering?

- Customer: the increased availability and durability of service means no outages disrupt their day-to-day lives.
- Business: Chaos Engineering can help prevent extremely large losses in revenue and maintenance costs, create happier and more engaged engineers, improve in on-call training for engineering teams, and improve the SEV (incident) Management Program for the entire company.
- Technical: the insights from chaos experiments can mean a reduction in incidents, reduction in on-call burden, increased understanding of system failure modes, improved system design, faster mean time to detection for SEVs, and reduction in repeated SEVs.

## Chaos Engineering for service teams

Many engineering organizations, including Netflix and Stitch Fix, have dedicated Chaos Engineering teams. These teams are often small in size, with 2—5 engineers. The Chaos Engineering team owns and advocates for Chaos Engineering across the organization. However, they are not the only engineers doing Chaos Engineering day-to-day—they empower teams across their engineering organization to use Chaos Engineering.

These service teams are often the first to practice and evangelize Chaos Engineering within a company:

- Traffic Team (e.g. Nginx, Apache, DNS)
- Streaming Team (e.g. Kafka)
- Storage Team (e.g. S3)
- Data Team (e.g. Hadoop/HDFS)
- Database Team (e.g. MySQL, Amazon RDS, PostgreSQL)

Some companies, such as Remind, are integrating Chaos Engineering into their normal release cycle like other best practice testing as a way to ensure reliability is baked into every feature.

## Which Chaos Engineering experiments do you perform first?

We argue that you should perform your experiments in the following order:

1. Known Knowns - Things you are aware of and understand
2. Known Unknowns - Things you are aware of but don’t fully understand
3. Unknown Knowns - Things you understand but are not aware of
4. Unknown Unknowns - Things you are neither aware of nor fully understand

The diagram below illustrates this concept:

To illustrate this in practice with examples, we will demonstrate how to select experiments based on a sharded MySQL Database. In this example, we have a cluster of 100 MySQL hosts with multiple shards per host.

In one region, we have a primary database host with two replicas and we use semi-sync replication. We also have a pseudo primary and two pseudo replicas in a different region.

**Known-Knowns**

- We know that when a replica shuts down it will be removed from the cluster. We know that a new replica will then be cloned from the primary and added back to the cluster.

**Known-Unknowns**

- We know that the clone will occur, as we have logs that confirm if it succeeds or fails, but we don’t know the weekly average of the mean time it takes from experiencing a failure to adding a clone back to the cluster effectively.
- We know we will get an alert that the cluster has only one replica after 5 minutes but we don’t know if our alerting threshold should be adjusted to more effectively prevent incidents.

**Unknown-Knowns**

- If we shutdown the two replicas for a cluster at the same time, we don’t know exactly the mean time during a Monday morning it would take us to clone two new replicas off the existing primary. But we do know we have a pseudo primary and two replicas which will also have the transactions.

**Unknown-Unknowns**

- We don’t know exactly what would happen if we shutdown an entire cluster in our main region, and we don’t know if the pseudo region would be able to failover effectively because we have not yet run this scenario.

We would create the following chaos experiments, working through them in order:

1. **Known-Knowns:** shut down one replica and measure the time it takes for the shutdown to be detected, the replica to be removed, the clone to kick-off, the clone to be completed, and the clone to be added back to the cluster. Before you kick off this experiment increase replicas from two to three. Run the shutdown experiment at a regular frequency but aim to avoid the experiment resulting in 0 replicas at any time. Report on the mean total time to recovery for a replica shutdown failure and break this down by day and time to account for peak hours.
2. **Known-Unknowns:** Use the results and data of the known-known experiment to answer questions which would currently be “known-unknowns”. You will now be able to know the impact the weekly average of the mean time it takes from experiencing a failure to adding a clone back to the cluster effectively. You will also know if 5 minutes is an appropriate alerting threshold to prevent SEVs.
3. **Unknown-Knowns:** Increase the number of replicas to four before conducting this experiment. Shutdown two replicas for a cluster at the same time, collect the mean time during a Monday morning over several months to determine how long it would take us to clone two new replicas off the existing primary. This experiment may identify unknown issues, for example, the primary cannot handle the load from cloning and backups at the same time and you need to make better use of the replicas.
4. **Unknown-Unknowns:** Shut down of an entire cluster (primary and two replicas) would require engineering work to make this possible. This failure may occur unexpectedly in the wild, but you are not yet ready to handle it. Prioritize the engineering work to handle this failure scenario before you perform chaos experiments.

## How do you plan for your first chaos experiments?

### Planning your First Experiment

One of the most powerful questions in Chaos Engineering is “What could go wrong?”. By asking this question about our services and environments, we can review potential weaknesses and discuss expected outcomes. Similar to a risk assessment, this informs priorities about which scenarios are more likely (or more frightening) and should be tested first. By sitting down as a team and whiteboarding your service(s), dependencies (both internal and external), and data stores, you can formulate a picture of “What could go wrong?”. When in doubt, injecting a failure or a delay into each of your dependencies is a great place to start.

### Creating a Hypothesis

You have an idea of what can go wrong. You have chosen the exact failure to inject. What happens next? This is an excellent thought exercise to work through as a team. By discussing the scenario, you can hypothesize on the expected outcome before running it live. What will be the impact to customers, to your service, or to your dependencies?

### Measuring the Impact

To understand how your system behaves under stress, you need to measure your system’s availability and durability. It is good to have a key performance metric that correlates to customer success (such as orders per minute, or stream starts per second). As a rule of thumb, if you ever see an impact to these metrics, you want to halt the experiment immediately. Next is measuring the failure itself where you want to verify (or disprove) your hypothesis. This could be the impact on latency, requests per second, or system resources. Lastly, you want to survey your dashboards and alarms for unintended side effects.

### Have a Rollback Plan

Always have a backup plan in case things go wrong, but accept that sometimes even the backup plan can fail. Talk through how you’re going to revert the impact. If you’re running commands by hand, be thoughtful not to break ssh or control plane access to your instances. One of the core aspects of Gremlin is safety. All of our attacks can be reverted immediately, allowing you to safely abort and return to steady state if things go wrong.

### Go fix it!

After running your first experiment, hopefully, there is one of two outcomes: either you’ve verified that your system is resilient to the failure you introduced, or you’ve found a problem you need to fix. Both of these are good outcomes. On one hand, you’ve increased your confidence in the system and its behavior, and on the other you’ve found a problem before it caused an outage.

### Have Fun

Chaos Engineering is a tool to make your job easier. By proactively testing and validating your system’s failure modes you will reduce your operational burden, increase your availability, and sleep better at night. Gremlin makes it safe and simple to get started—email us to get started today!

## What are some other Chaos Engineering resources?

We've consolidated a ton of useful information here on the Gremlin website. We provide dozens of hands-on tutorials showing you how to use Chaos Engineering with different cloud platforms, services, and technologies, and even as a tool for training incident response teams. Our blog covers use cases and practices using Chaos Engineering, such as preparing for cloud migrations and running GameDays. These posts can help you get started with Chaos Engineering:

- Getting Started with Chaos Engineering
- 4 Chaos Experiments to Start With
- How to Run a Gameday
- Gremlin's Gameday: Breaking DynamoDB (We take our own medicine!)
- What is Chaos Engineering? SREs and Leaders Define the Practice & Where It's Going

Pavlos Ratis has created a GitHub repo called “Awesome Chaos Engineering,” which is a curated list of Chaos Engineering resources. You can find Books, Tools, Papers, Blogs, Newsletters, Conferences, MeetUps, Forums and engineers to follow on Twitter.

Lastly, if you want to learn how Chaos Engineering helps improve the overall reliability of your systems, teams, and organization, check out our guide to reliability in distributed systems.

## Get started with Chaos Engineering

If you’re ready to get started with Chaos Engineering, sign up for a Gremlin trial – our guide to getting started with Chaos Engineering takes you through the process step by step.

## What are some good Chaos Engineering conference presentations?

You can watch presentations from Chaos Conf, the world's largest Chaos Engineering event. You can also watch speakers from Failover Conf, which is themed more around reliability and adapting to changing technology trends. If you're not sure where to start, check out the following presentations:

- QCon 2015 - Kolton Andrus (Gremlin) on Breaking Things at Netflix
- AWS re:Invent 2017 - Nora Jones (Netflix) Describes Why We Need More Chaos - Chaos Engineering, That Is
- Velocity 2017 - Kolton Andrus (Gremlin) shares the Evolution of Chaos
- Australian Government - Tammy Butow (Gremlin) gives an Introduction to Chaos Engineering
- SRECon 2017 - Kolton Andrus (Gremlin) on Breaking Things
- KubeCon North America 2019 - Ana Medina (Gremlin) and Lenny Sharpe (Target) present Finding the Joy in Chaos Engineering
- Failover Conf 2020 - Tammy Butow (Gremlin) explains why Reliability Matters More Than Ever
- Chaos Conf 2020 - Kolton Andrus (Gremlin) presents Chaos Engineering: The Path to Reliability

## Where can you find the Chaos Engineering community?

The Chaos Engineering community is a global community of engineers. Join over 7,000 engineers in the Chaos Engineering Slack community at gremlin.com/slack. You can also follow Gremlin on Twitter @gremlininc and on Instagram @thegremlininc.

## Conclusion

As web systems have grown much more complex with the rise of distributed systems and microservices, system failures have become difficult to predict. So in order to prevent failures from happening, we all need to be proactive in our efforts to learn from failure.

In this guide, we shared a brief history of Chaos Engineering and demonstrated how Chaos Engineering offers you new insights into your systems. We look forward to hearing about your Chaos Engineering journey and encourage you to share your progress with the Chaos Engineering community.

No items found.

Gremlin's automated reliability platform empowers you to find and fix availability risks before they impact your users. Start finding hidden risks in your systems with a free 30 day trial.

start your trial

## Avoid downtime. Use Gremlin to turn failure into resilience.

Gremlin empowers you to proactively root out failure before it causes downtime. See how you can harness chaos to build resilient systems by requesting a demo of Gremlin.

get started
