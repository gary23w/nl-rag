---
title: "Smart grid (part 2/2)"
source: https://en.wikipedia.org/wiki/Smart_grid
domain: smart-grid
license: CC-BY-SA-4.0
tags: smart grid, intelligent electrical grid, grid modernization, distributed energy grid
fetched: 2026-07-02
part: 2/2
---

## Oppositions and concerns

Most opposition and concerns have centered on smart meters and the items (such as remote control, remote disconnect, and variable rate pricing) enabled by them. Where opposition to smart meters is encountered, they are often marketed as "smart grid" which connects smart grid to smart meters in the eyes of opponents. Specific points of opposition or concern include:

- consumer concerns over privacy, e.g. use of usage data by law enforcement
- social concerns over "fair" availability of electricity
- concern that complex rate systems (e.g. variable rates) remove clarity and accountability, allowing the supplier to take advantage of the customer
- concern over remotely controllable "kill switch" incorporated into most smart meters
- social concerns over Enron style abuses of information leverage
- concerns over giving the government mechanisms to control the use of all power using activities
- concerns over RF emissions from smart meters

### Security

While modernization of electrical grids into smart grids allows for optimization of everyday processes, a smart grid, being online, can be vulnerable to cyberattacks. Transformers which increase the voltage of electricity created at power plants for long-distance travel, transmission lines themselves, and distribution lines which deliver the electricity to its consumers are particularly susceptible. These systems rely on sensors which gather information from the field and then deliver it to control centers, where algorithms automate analysis and decision-making processes. These decisions are sent back to the field, where existing equipment execute them. Hackers have the potential to disrupt these automated control systems, severing the channels which allow generated electricity to be utilized. This is called a denial of service or DoS attack. They can also launch integrity attacks which corrupt information being transmitted along the system as well as desynchronization attacks which affect when such information is delivered to the appropriate location. Additionally, intruders can gain access via renewable energy generation systems and smart meters connected to the grid, taking advantage of more specialized weaknesses or ones whose security has not been prioritized. Because a smart grid has a large number of access points, like smart meters, defending all of its weak points can prove difficult. Advanced Persistent Threats (APTs) have evolved to target smart grids by reprogramming Programmable Logic Controllers (PLCs) to display false 'normal' operating conditions to operators while causing physical damage. To counter these vulnerabilities, experts recommend shifting from traditional network segmentation to 'micro-segmentation' and adopting 'zero-trust' models that require verification at every layer of the infrastructure.

There is also concern on the security of the infrastructure, primarily that involving communications technology. Concerns chiefly center around the communications technology at the heart of the smart grid. Designed to allow real-time contact between utilities and meters in customers' homes and businesses, there is a risk that these capabilities could be exploited for criminal or even terrorist actions. One of the key capabilities of this connectivity is the ability to remotely switch off power supplies, enabling utilities to quickly and easily cease or modify supplies to customers who default on payment. This is undoubtedly a massive boon for energy providers, but also raises some significant security issues. Cybercriminals have infiltrated the U.S. electric grid before on numerous occasions. Aside from computer infiltration, there are also concerns that computer malware like Stuxnet, which targeted SCADA systems which are widely used in industry, could be used to attack a smart grid network.

Electricity theft is a concern in the U.S. where the smart meters being deployed use RF technology to communicate with the electricity transmission network. People with knowledge of electronics can devise interference devices to cause the smart meter to report lower than actual usage. Similarly, the same technology can be employed to make it appear that the energy the consumer is using is being used by another customer, increasing their bill.

The damage from a well-executed, sizable cyberattack could be extensive and long-lasting. One incapacitated substation could take from nine days to over a year to repair, depending on the nature of the attack. It can also cause an hours-long outage in a small radius. It could have an immediate effect on transportation infrastructure, as traffic lights and other routing mechanisms as well as ventilation equipment for underground roadways is reliant on electricity. Additionally, infrastructure which relies on the electric grid, including wastewater treatment facilities, the information technology sector, and communications systems could be impacted.

The December 2015 Ukraine power grid cyberattack, the first recorded of its kind, disrupted services to nearly a quarter of a million people by bringing substations offline. The Council on Foreign Relations has noted that states are most likely to be the perpetrators of such an attack as they have access to the resources to carry one out despite the high level of difficulty of doing so. Cyber intrusions can be used as portions of a larger offensive, military or otherwise. Some security experts warn that this type of event is easily scalable to grids elsewhere. Insurance company Lloyd's of London has already modeled the outcome of a cyberattack on the Eastern Interconnection, which has the potential to impact 15 states, put 93 million people in the dark, and cost the country's economy anywhere from $243 billion to $1 trillion in various damages.

According to the U.S. House of Representatives Subcommittee on Economic Development, Public Buildings, and Emergency Management, the electric grid has already seen a sizable number of cyber intrusions, with two in every five aiming to incapacitate it. As such, the U.S. Department of Energy has prioritized research and development to decrease the electric grid's vulnerability to cyberattacks, citing them as an "imminent danger" in its 2017 Quadrennial Energy Review. The Department of Energy has also identified both attack resistance and self-healing as major keys to ensuring that today's smart grid is future-proof. While there are regulations already in place, namely the Critical Infrastructure Protection Standards introduced by the North America Electric Reliability Council, a significant number of them are suggestions rather than mandates. Most electricity generation, transmission, and distribution facilities and equipment are owned by private stakeholders, further complicating the task of assessing adherence to such standards. Additionally, even if utilities want to fully comply, they may find that it is too expensive to do so.

Some experts argue that the first step to increasing the cyber defenses of the smart electric grid is completing a comprehensive risk analysis of existing infrastructure, including research of software, hardware, and communication processes. Additionally, as intrusions themselves can provide valuable information, it could be useful to analyze system logs and other records of their nature and timing. Common weaknesses already identified using such methods by the Department of Homeland Security include poor code quality, improper authentication, and weak firewall rules. Once this step is completed, some suggest that it makes sense to then complete an analysis of the potential consequences of the aforementioned failures or shortcomings. This includes both immediate consequences as well as second- and third-order cascading effects on parallel systems. Finally, risk mitigation solutions, which may include simple remediation of infrastructure inadequacies or novel strategies, can be deployed to address the situation. Some such measures include recoding of control system algorithms to make them more able to resist and recover from cyberattacks or preventive techniques that allow more efficient detection of unusual or unauthorized changes to data. Strategies to account for human error which can compromise systems include educating those who work in the field to be wary of strange USB drives, which can introduce malware if inserted, even if just to check their contents.

Other solutions include utilizing transmission substations, constrained SCADA networks, policy based data sharing, and attestation for constrained smart meters.

Transmission substations utilize one-time signature authentication technologies and one-way hash chain constructs. These constraints have since been remedied with the creation of a fast-signing and verification technology and buffering-free data processing.

A similar solution has been constructed for constrained SCADA networks. This involves applying a Hash-Based Message Authentication Code to byte streams, converting the random-error detection available on legacy systems to a mechanism that guarantees data authenticity.

Policy-based data sharing utilizes GPS-clock-synchronized-fine-grain power grid measurements to provide increased grid stability and reliability. It does this through synchro-phasor requirements that are gathered by PMUs.

Attestation for constrained smart meters faces a slightly different challenge, however. One of the biggest issues with attestation for constrained smart meters is that in order to prevent energy theft, and similar attacks, cyber security providers have to make sure that the devices' software is authentic. To combat this problem, an architecture for constrained smart networks has been created and implemented at a low level in the embedded system.

The protection system of a smart grid provides grid reliability analysis, failure protection, and security and privacy protection services. While the additional communication infrastructure of a smart grid provides additional protective and security mechanisms, it also presents a risk of external attack and internal failures. In a report on cyber security of smart grid technology first produced in 2010, and later updated in 2014, the US National Institute of Standards and Technology pointed out that the ability to collect more data about energy use from customer smart meters also raises major privacy concerns, since the information stored at the meter, which is potentially vulnerable to data breaches, can be mined for personal details about customers.


## Other challenges to adoption

Before a utility installs an advanced metering system, or any type of smart system, it must make a business case for the investment. Some components, like the power system stabilizers (PSS) installed on generators are very expensive, require complex integration in the grid's control system, are needed only during emergencies, and are only effective if other suppliers on the network have them. Without any incentive to install them, power suppliers don't. Most utilities find it difficult to justify installing a communications infrastructure for a single application (e.g. meter reading). Because of this, a utility must typically identify several applications that will use the same communications infrastructure – for example, reading a meter, monitoring power quality, remote connection and disconnection of customers, enabling demand response, etc. Ideally, the communications infrastructure will not only support near-term applications, but unanticipated applications that will arise in the future. Regulatory or legislative actions can also drive utilities to implement pieces of a smart grid puzzle. Each utility has a unique set of business, regulatory, and legislative drivers that guide its investments. This means that each utility will take a different path to creating their smart grid and that different utilities will create smart grids at different adoption rates.

Some features of smart grids draw opposition from industries that currently are, or hope to provide similar services. An example is competition with cable and DSL Internet providers from broadband over powerline internet access. Providers of SCADA control systems for grids have intentionally designed proprietary hardware, protocols and software so that they cannot inter-operate with other systems in order to tie its customers to the vendor.

The incorporation of digital communications and computer infrastructure with the grid's existing physical infrastructure poses challenges and inherent vulnerabilities. According to *IEEE Security & Privacy*, the smart grid will require that people develop and use large computer and communication infrastructure that supports a greater degree of situational awareness and that allows for more specific command and control operations. This process is necessary to support major systems such as demand-response wide-area measurement and control, storage and transportation of electricity, and the automation of electric distribution.

### Power Theft / Power Loss

Various "smart grid" systems have dual functions. This includes Advanced Metering Infrastructure systems which, when used with various software can be used to detect power theft and by process of elimination, detect where equipment failures have taken place. These are in addition to their primary functions of eliminating the need for human meter reading and measuring the time-of-use of electricity.

The worldwide power loss including theft is estimated at two-hundred billion dollars annually.

Electricity theft also represents a major challenge when providing reliable electrical service in developing countries.


## Deployments and attempted deployments

### Enel

The earliest, and one of the largest, example of a smart grid is the Italian system installed by Enel S.p.A. of Italy. Completed in 2005, the Telegestore project was highly unusual in the utility world because the company designed and manufactured their own meters, acted as their own system integrator, and developed their own system software. The Telegestore project is widely regarded as the first commercial scale use of smart grid technology to the home, and delivers annual savings of 500 million euro at a project cost of 2.1 billion euro.

### US Dept. of Energy - ARRA Smart Grid Project

One of the largest deployment programs in the world to-date is the U.S. Dept. of Energy's Smart Grid Program funded by the American Recovery and Reinvestment Act of 2009. This program required matching funding from individual utilities. A total of over $9 billion in Public/Private funds were invested as part of this program. Technologies included Advanced Metering Infrastructure, including over 65 million Advanced "Smart" Meters, Customer Interface Systems, Distribution & Substation Automation, Volt/VAR Optimization Systems, over 1,000 Synchrophasors, Dynamic Line Rating, Cyber Security Projects, Advanced Distribution Management Systems, Energy Storage Systems, and Renewable Energy Integration Projects. This program consisted of Investment Grants (matching), Demonstration Projects, Consumer Acceptance Studies, and Workforce Education Programs. Reports from all individual utility programs as well as overall impact reports will be completed by the second quarter of 2015.

In the U.S., the Energy Policy Act of 2005 and Title XIII of the Energy Independence and Security Act of 2007 are providing funding to encourage smart grid development. The objective is to enable utilities to better predict their needs, and in some cases involve consumers in a time-of-use tariff. Funds have also been allocated to develop more robust energy control technologies.

### Austin, Texas

In the US, the city of Austin, Texas, has been working on building its smart grid since 2003, when its utility first replaced 1/3 of its manual meters with smart meters that communicate via a wireless mesh network. It currently manages 200,000 devices real-time (smart meters, smart thermostats, and sensors across its service area), and expects to be supporting 500,000 devices real-time in 2009 servicing 1 million consumers and 43,000 businesses.

### Boulder, Colorado

Boulder, Colorado, completed the first phase of its smart grid project in August 2008. Both systems use the smart meter as a gateway to the home automation network (HAN) that controls smart sockets and devices. Some HAN designers favor decoupling control functions from the meter, out of concern of future mismatches with new standards and technologies available from the fast moving business segment of home electronic devices.

### Hydro One

Hydro One, in Ontario, Canada is in the midst of a large-scale Smart Grid initiative, deploying a standards-compliant communications infrastructure from Trilliant. By the end of 2010, the system will serve 1.3 million customers in the province of Ontario. The initiative won the "Best AMR Initiative in North America" award from the Utility Planning Network.

### Île d'Yeu

Île d'Yeu began a 2-year pilot program in Spring of 2020. Twenty-three houses in the Ker Pissot neighborhood and surrounding areas were interconnected with a microgrid that was automated as a smart grid with software from Engie. Sixty-four solar panels with a peak capacity of 23.7 kW were installed on five houses and a battery with a storage capacity of 15 kWh was installed on one house. Six houses store excess solar energy in their hot water heaters. A dynamic system apportions the energy provided by the solar panels and stored in the battery and hot water heaters to the system of 23 houses. The smart grid software dynamically updates energy supply and demand in 5 minute intervals, deciding whether to pull energy from the battery or from the panels and when to store it in the hot water heaters. This pilot program was the first such project in France.

### Mannheim

The City of Mannheim in Germany is using realtime Broadband Powerline (BPL) communications in its Model City Mannheim "MoMa" project.

### Sydney

Sydney also in Australia, in partnership with the Australian Government implemented the Smart Grid, Smart City program.

### Évora

InovGrid is a project in Évora, Portugal that aims to equip the electricity grid with information and devices to automate grid management, improve service quality, reduce operating costs, promote energy efficiency and environmental sustainability, and increase the penetration of renewable energies and electric vehicles. It will be possible to control and manage the state of the entire electricity distribution grid at any given instant, allowing suppliers and energy services companies to use this technological platform to offer consumers information and added-value energy products and services. This project to install an intelligent energy grid places Portugal and EDP at the cutting edge of technological innovation and service provision in Europe.

### E-Energy

In the so-called *E-Energy* projects several German utilities are creating first nucleolus in six independent model regions. A technology competition identified this model regions to carry out research and development activities with the main objective to create an "Internet of Energy".

### Massachusetts

One of the first attempted deployments of "smart grid" technologies in the United States was rejected in 2009 by electricity regulators in the Commonwealth of Massachusetts, a US state. According to an article in the Boston Globe, Northeast Utilities' Western Massachusetts Electric Co. subsidiary actually attempted to create a "smart grid" program using public subsidies that would switch low income customers from post-pay to pre-pay billing (using "smart cards") in addition to special hiked "premium" rates for electricity used above a predetermined amount. This plan was rejected by regulators as it "eroded important protections for low-income customers against shutoffs". According to the Boston Globe, the plan "unfairly targeted low-income customers and circumvented Massachusetts laws meant to help struggling consumers keep the lights on". A spokesman for an environmental group supportive of smart grid plans and Western Massachusetts' Electric's aforementioned "smart grid" plan, in particular, stated "If used properly, smart grid technology has a lot of potential for reducing peak demand, which would allow us to shut down some of the oldest, dirtiest power plants... It's a tool."

### eEnergy Vermont consortium

The eEnergy Vermont consortium is a US statewide initiative in Vermont, funded in part through the American Recovery and Reinvestment Act of 2009, in which all of the electric utilities in the state have rapidly adopted a variety of Smart Grid technologies, including about 90% Advanced Metering Infrastructure deployment, and are presently evaluating a variety of dynamic rate structures.

### Netherlands

In the Netherlands a large-scale project (>5000 connections, >20 partners) was initiated to demonstrate integrated smart grids technologies, services and business cases.

### Chattanooga

EPB in Chattanooga, TN is a municipally owned electric utility that started construction of a smart grid in 2008, receiving a $111,567,606 grant from the US DOE in 2009 to expedite construction and implementation (for a total budget of $232,219,350). Deployment of power-line interrupters (1170 units) was completed in April 2012, and deployment of smart meters (172,079 units) was completed in 2013. The smart grid's backbone fiber-optic system was also used to provide the first gigabit-speed internet connection to residential customers in the US through the Fiber to the Home initiative, and now speeds of up to 10 gigabits per second are available to residents. The smart grid is estimated to have reduced power outages by an average of 60%, saving the city about 60 million dollars annually. It has also reduced the need for "truck rolls" to scout and troubleshoot faults, resulting in an estimated reduction of 630,000 truck driving miles, and 4.7 million pounds of carbon emissions. In January 2016, EPB became the first major power distribution system to earn Performance Excellence in Electricity Renewal (PEER) certification.

### OpenADR Implementations

Certain deployments utilize the OpenADR standard for load shedding and demand reduction during higher demand periods.

#### China

The smart grid market in China is estimated to be $22.3 billion with a projected growth to $61.4 billion by 2015. Honeywell is developing a demand response pilot and feasibility study for China with the State Grid Corp. of China using the OpenADR demand response standard. The State Grid Corp., the Chinese Academy of Sciences, and General Electric intend to work together to develop standards for China's smart grid rollout.

#### United States

In 2009, the US Department of Energy awarded an $11 million grant to Southern California Edison and Honeywell for a demand response program that automatically turns down energy use during peak hours for participating industrial customers. The Department of Energy awarded an $11.4 million grant to Honeywell to implement the program using the OpenADR standard.

Hawaiian Electric Co. (HECO) is implementing a two-year pilot project to test the ability of an ADR program to respond to the intermittence of wind power. Hawaii has a goal to obtain 70 percent of its power from renewable sources by 2030. HECO will give customers incentives for reducing power consumption within 10 minutes of a notice.


## Guidelines, standards and user groups

Part of the IEEE Smart Grid Initiative, IEEE 2030.2 represents an extension of the work aimed at utility storage systems for transmission and distribution networks. The IEEE P2030 group expects to deliver early 2011 an overarching set of guidelines on smart grid interfaces. The new guidelines will cover areas including batteries and supercapacitors as well as flywheels. The group has also spun out a 2030.1 effort drafting guidelines for integrating electric vehicles into the smart grid.

IEC TC 57 has created a family of international standards that can be used as part of the smart grid. These standards include IEC 61850 which is an architecture for substation automation, and IEC 61970/61968 – the Common Information Model (CIM). The CIM provides for common semantics to be used for turning data into information.

OpenADR is an open-source smart grid communications standard used for demand response applications. It is typically used to send information and signals to cause electrical power-using devices to be turned off during periods of higher demand.

MultiSpeak has created a specification that supports distribution functionality of the smart grid. MultiSpeak has a robust set of integration definitions that supports nearly all of the software interfaces necessary for a distribution utility or for the distribution portion of a vertically integrated utility. MultiSpeak integration is defined using extensible markup language (XML) and web services.

The IEEE has created a standard to support synchrophasors – C37.118.

The UCA International User Group discusses and supports real world experience of the standards used in smart grids.

A utility task group within LonMark International deals with smart grid related issues.

There is a growing trend towards the use of TCP/IP technology as a common communication platform for smart meter applications, so that utilities can deploy multiple communication systems, while using IP technology as a common management platform.

IEEE P2030 is an IEEE project developing a "Draft Guide for Smart Grid Interoperability of Energy Technology and Information Technology Operation with the Electric Power System (EPS), and End-Use Applications and Loads".

NIST has included ITU-T G.hn as one of the "Standards Identified for Implementation" for the Smart Grid "for which it believed there was strong stakeholder consensus". G.hn is standard for high-speed communications over power lines, phone lines and coaxial cables.

OASIS EnergyInterop' – An OASIS technical committee developing XML standards for energy interoperation. Its starting point is the California OpenADR standard.

Under the Energy Independence and Security Act of 2007 (EISA), NIST is charged with overseeing the identification and selection of hundreds of standards that will be required to implement the Smart Grid in the U.S. These standards will be referred by NIST to the Federal Energy Regulatory Commission (FERC). This work has begun, and the first standards have already been selected for inclusion in NIST's Smart Grid catalog. However, some commentators have suggested that the benefits that could be realized from Smart Grid standardization could be threatened by a growing number of patents that cover Smart Grid architecture and technologies. If patents that cover standardized Smart Grid elements are not revealed until technology is broadly distributed throughout the network ("locked-in"), significant disruption could occur when patent holders seek to collect unanticipated rents from large segments of the market.


## GridWise Alliance rankings

In November 2017 the non-profit GridWise Alliance along with Clean Edge Inc., a clean energy group, released rankings for all 50 states in their efforts to modernize the electric grid. California was ranked number one. The other top states were Illinois, Texas, Maryland, Oregon, Arizona, the District of Columbia, New York, Nevada and Delaware. "The 30-plus page report from the GridWise Alliance, which represents stakeholders that design, build and operate the electric grid, takes a deep dive into grid modernization efforts across the country and ranks them by state."
