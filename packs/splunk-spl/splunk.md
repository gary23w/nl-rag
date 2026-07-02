---
title: "Splunk"
source: https://en.wikipedia.org/wiki/Splunk
domain: splunk-spl
license: CC-BY-SA-4.0
tags: splunk spl query, machine data indexing, security search query language, log analytics platform, security dashboard visualization
fetched: 2026-07-02
---

# Splunk

**Splunk Inc.** is a subsidiary of Cisco Systems that produces software for indexing, searching, and analyzing machine-generated data, allowing for the creation of dashboards, alerts, graphs, and reports to monitor system health and to detect and respond to issues in real time. With a focus on cyber security and observability, Splunk describes its on-premises software and SaaS products as SIEM, SOAR (Security Orchestration, Automation, and Response), and observability solutions.

Splunk was acquired by Cisco in September 2023 for $28 billion in an all-cash deal. The transaction was completed on March 18, 2024. After the acquisition, Splunk remained headquartered in San Francisco, California, although in a new office.

## History

### Founding & early years

Michael Baum, Rob Das and Erik Swan co-founded Splunk Inc in 2003. Venture firms August Capital, Sevin Rosen, Ignition Partners and JK&B Capital backed the company.

By 2007, Splunk had raised US$40 million. It became profitable in 2009. In 2012, Splunk had its initial public offering, trading under NASDAQ symbol SPLK.

### Company growth

Between 2013 and 2019, Splunk expanded by acquiring a series of companies focused on data analytics, cybersecurity, and observability, including: BugSense, Cloudmeter, Metafor, Caspida, Rocana, Phantom Cyber Corporation, VictorOps, KryptonCloud, SignalFx, Drastin, SignalSense, and Omnition.

During this time the company also formed partnerships, such as a "cybersecurity alliance" with U.S. government security contractor Booz Allen Hamilton Inc. in 2015, pledged to donate $100 million in software licenses, training, support, education, and volunteerism for nonprofits and schools over a 10-year period in 2016, and was recognized among the highest-paying companies for employees in the United States according to Glassdoor in 2017. In 2019, Splunk received FedRAMP authorization from the General Services Administration FedRAMP Program Management Office at the moderate level, sponsored by the International Trade Administration, enabling Splunk to sell to the federal government.

In 2020 Splunk announced the launch of its corporate venture fund, Splunk Ventures—a $100 million Innovation Fund and a $50 million Social Impact Fund to invest in early-stage startups.

On November 15, 2021, Doug Merritt stepped down as president and CEO. Graham Smith, Splunk's chairman since 2019, took over as interim CEO. On March 2, 2022, Splunk named Gary Steele, previously at Proofpoint, as its CEO and the successor to interim chief Graham Smith effective April 2022.

### Cisco acquisition

On September 21, 2023 Cisco announced it would acquire Splunk for $28 billion in an all-cash deal. In November 2023, the company announced layoffs affecting 7% or 500 of its employees, following an earlier reduction of 300 staff in the same year. CEO Gary Steele clarified in a letter to employees, filed with the U.S. Securities and Exchange Commission, that the decision was not related to the Cisco deal.

In April 2024, Splunk won an infringement case against Cribl Inc, a startup competitor, for copying enterprise data analysis software. The jury awarded Splunk $1 in damages.

The acquisition of Splunk was completed in March 2024. It was the largest deal in Cisco's history. At the time, Splunk had 1,100 patents, with clients such as Singapore Airlines, Papa John's, Heineken, and McLaren. Splunk continued under the same management, with pricing projected to stay the same.

In May 2024, former Splunk CEO Gary Steele was promoted to a Cisco executive, although Splunk continued to report to him. He remained Splunk general manager. Cisco's observability product development including its Cisco AppDynamics software was moved into Splunk after the integration.

In 2025, Splunk became a central element of Cisco's enterprise AI and security strategy following its integration into Cisco's software portfolio.

## Products

Splunk's core offering collects and analyzes high volumes of machine-generated data. It uses a lightweight agent to locally collect log messages from files, receives them via TCP or UDP syslog protocol on an open port (not preferred), or calls scripts to collect events from various application programming interfaces (APIs) to connect to applications and devices. It was developed for troubleshooting and monitoring distributed applications based on log messages.

Splunk Enterprise Security (ES) provides security information and event management (SIEM) for machine data generated from security technologies such as network, endpoints, access, malware, vulnerability, and identity information. It is a premium application that is licensed independently.

In 2011, Splunk released Splunk Storm, a cloud-based version of the core Splunk product. Splunk Storm offered a turnkey, managed, and hosted service for machine data. In 2013, Splunk announced that Splunk Storm would become a completely free service and expanded its cloud offering with Splunk Cloud. In 2015, Splunk shut down Splunk Storm.

In 2013, Splunk announced a product called Hunk: Splunk Analytics for Hadoop, which supports accessing, searching, and reporting on external data sets located in Hadoop from a Splunk interface.

In 2015, Splunk announced a Light version of the core Splunk product aimed at smaller IT environments and mid-sized enterprises. Splunk debuted Splunk IT Service Intelligence (ITSI) in September 2015. ITSI leverages Splunk data to provide visibility into IT performance. Software analytics can detect anomalies and determine their causes and the areas it affects.

Splunk *Security Orchestration, Automation and Response* (SOAR) free community edition, is free for as long as you want, up to 100 actions/day to automate tasks, orchestrate workflows, and reduce incident response times for cloud, on-premises or hybrid deployments.

### Cloud transformation

In 2016, Google announced its cloud platform would integrate with Splunk to expand in areas like IT ops, security, and compliance. The company also announced additional machine learning capabilities for several of its major product offerings, which are installed on top of the platform. Splunk Cloud received FedRAMP authorization from the General Services Administration FedRAMP Program Management Office at the moderate level in 2019, enabling Splunk to sell to the federal government. This allows customers to access Google's AI and ML services and power them with data from Splunk. Also, by integrating with Google Anthos and Google Cloud Security Command Center, Splunk data can be shared among different cloud-based applications. To help companies manage the shift to a multi cloud environment, Splunk launched its Observability Cloud, which combines infrastructure monitoring, application performance monitoring, digital experience monitoring, log investigation, and incident response capabilities. In 2020, the company announced that Splunk Cloud is available on the Google Cloud Platform and launched an initiative with Amazon Web Services to help customers migrate on-premises Splunk workloads to Splunk Cloud on the AWS cloud.

In 2017, Splunk introduced Splunk Insights for ransomware, an analytics tool for assessing and investigating potential threats by ingesting event logs from multiple sources. The software is targeted toward smaller organizations like universities. The company also launched Splunk Insights for AWS Cloud Monitoring, a service to facilitate enterprises' migration to Amazon Web Services' cloud.

In 2018, Splunk introduced Splunk Industrial Asset Intelligence, which extracts information from IIoT (Industrial Internet of Things) data from various resources and presents its users with critical alerts.

In 2019, Splunk announced new capabilities to its platform, including the general availability of Data Fabric Search and Data Stream Processor. Data Fabric Search uses datasets across different data stores, including those that are not Splunk-based, into a single view. The required data structure is only created when a query is run.

Data Stream Processor is a real-time processing product that collects data from various sources and then distributes results to Splunk or other destinations. It allows role-based access to create alerts and reports based on data that is relevant for each individual. In 2020, it was updated to allow it to access, process, and route real-time data from multiple cloud services. Also, in 2019, Splunk rolled out Splunk Connected Experiences, which extends its data processing and analytics capabilities to augmented reality (AR), mobile devices, and mobile applications.

In 2020, Splunk announced Splunk Enterprise 8.1 and the Splunk Cloud edition. They include stream processing, machine learning, and multi-cloud capabilities.

In October 2019, Splunk announced the integration of its security tools - including security information and event management (SIEM), user behavior analytics (UBA), and security orchestration, automation, and response (Splunk Phantom) — into the new Splunk Mission Control.

In 2019, Splunk introduced an application performance monitoring (APM) platform, SignalFx Microservices APM, that pairs “no-sample’ monitoring and analysis features with Omnition's full-fidelity tracing capabilities. Splunk also announced that a capability called Kubernetes Navigator would be available through its product, SignalFx Infrastructure Monitoring.

## Splunkbase

Splunkbase is a community hosted by Splunk where users can go to find apps and add-ons for Splunk, which can improve the functionality and usefulness of Splunk, as well as provide a quick and easy interface for specific use cases and/or vendor products. As of October 2019, more than 2,000 apps were available on the site.

Integrations on Splunkbase include the Splunk App for New Relic, the ForeScout Extended Module for Splunk, and Splunk App for AWS.

## Sponsorships

### McLaren

Starting in 2020, Splunk announced a partnership with the McLaren Formula One team, sponsoring the team and working with them to provide data analysis and insight on racing performance.

Splunk worked with McLaren Racing for several years, evaluating the performance data pulled from the nearly 300 sensors on every racecar, before becoming McLaren's official technology partner in February 2020. The partnership resulted in Splunk deployed across the McLaren Group. This included using Splunk to interpret data from McLaren's e-sports team. As part of the partnership, Splunk's logo was added to the sidepod and cockpit surrounds of the MCL35 racecar.

### Trek-Segafredo

In November 2018, Splunk signed a sponsorship deal with the Trek-Segafredo professional road cycling team; the partnership started in 2019. Splunk replaced CA Industries as the company's technology partner. Splunk provides data analysis for the company, including analysis on riders, coaches, and mechanics. Team jerseys, bikes, and vehicles carry Splunk branding. Splunk also participates in Trek's race hospitality program.
