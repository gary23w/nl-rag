---
title: "Data center (part 1/2)"
source: https://en.wikipedia.org/wiki/Data_center
domain: alibaba-cloud
license: CC-BY-SA-4.0
tags: alibaba cloud, aliyun compute, alibaba cloud ecs, chinese cloud provider alibaba
fetched: 2026-07-02
part: 1/2
---

# Data center

A **data center** is a facility used to house computer systems and associated components, such as telecommunications and storage systems. Data centers are critical infrastructure for the storage and processing of information, and they support the global financial system, cloud services, machine learning, and artificial intelligence (AI).

Data centers vary widely in terms of size, power and water requirements, and overall structure. Four common categories are onsite *enterprise* data centers used mainly by a company's employees and clients, *colocation* facilities where many companies rent space in a shared data center, *hyperscale* data centers owned by very large cloud service companies, and smaller *edge* data centers located close to end users. Hyperscale and colocation facilities collectively account for approximately 74% of U.S. server energy consumption as of 2023, a share that has grown significantly over the past decade as workloads have migrated away from enterprise on-premises infrastructure.

Since IT operations are crucial for business continuity, a data center generally includes redundant or backup components. Other important design considerations are power supply, network infrastructure, environmental controls (e.g., cooling, fire suppression), and various measures for physical and data security. Large data centers operate at an industrial scale, requiring significant energy. Estimated global data center electricity consumption in 2024 was around 415 terawatt hours (TWh), or about 1.5% of global electricity demand. The International Energy Agency (IEA) projects that data center electricity consumption could double by 2030. The rapid growth of data center infrastructure has prompted regulatory debates in multiple jurisdictions regarding tax incentives, electricity grid impacts, water consumption, and compatibility with state and national climate commitments.

Rapid growth of the AI industry is leading to strain on electric grids and increased electricity costs for consumers. This in turn has drawn growing opposition to new data centers from local people who would bear the burdens of social and environmental impacts, such as energy and water use, while faraway actors and institutions would receive the projects' benefits. These opposition movements have materialized especially in parts of Europe, the U.S., and South America. Billions of dollars in projects were halted or delayed by data center resistances in the U.S. between May 2024 and June 2025.


## Classification and types

Data centers are usually classified according to their ownership model, scale, and intended use.

| Type | Typical scale | Primary purpose | Key characteristic |
|---|---|---|---|
| Enterprise | 1–10 MW | Internal IT operations | Owned and operated by a single organization |
| Colocation | 10–100 MW | Shared hosting for multiple clients | Customers lease space, power, and cooling |
| Hyperscale | 100 MW+ | Cloud services and AI workloads | Massive scalability; operated by major cloud providers |
| Edge | 1–10 MW | Low-latency local processing | Distributed near end users or data sources |

Distribution of computing workloads across these four categories has shifted dramatically over the past decade, with hyperscale and colocation collectively accounting for approximately 74% of U.S. server energy consumption in 2023, up from less than 40% in 2014; this share is projected to reach 85% by 2028. However, these classifications are not mutually exclusive from each other, and they may overlap depending on the operational structure and service model of the particular data center.

### Enterprise

Enterprise data centers are owned and operated by a single organization for their own internal information technology (IT) needs, rather than for commercial hosting of other companies' data. They used to be essential infrastructures; as in 2014, enterprise data centers accounted for over 60% of the U.S. server energy consumption, but this share fell sharply to about 10% by 2023 as workloads migrated to hyperscale and colocation facilities. Energy efficiency at an enterprise data center tends to be significantly lower than at hyperscale facilities due to its cooling, which can account for over 30% of electricity consumption at enterprise sites, compared to roughly 7% at efficient hyperscale data centers. The shift away from enterprise facilities toward cloud and colocation infrastructure is one of the defining structural trends of the previous decade.

### Colocation

Colocation centers provide shared physical infrastructure, such as power, cooling, space, etc., to multiple tenants who lease space rather than building their own facilities. Colocation data centers reduce expenditure for organizations while enabling operators to achieve economies of scale in power procurement and cooling efficiency. Some of the largest data centers in the world are colocation centers, and this category accounted for about 22% of worldwide data center capacity as of 2024, making them the second-largest category by capacity after hyperscale facilities. Major colocation providers include Equinix, Switch, COPT, and Digital Realty, which operate facilities across multiple continents.

Colocation centers often host private peering connections between their customers, internet transit providers, cloud providers, meet-me rooms for connecting customers, Internet exchange points, and landing points and terminal equipment for fiber optic submarine communication cables, which are critical to connecting the internet.

### Hyperscale

Hyperscale data centers are large-scale facilities, typically exceeding 100 megawatts of power capacity, designed to support massive, scalable computing workloads for cloud services, AI training, and large-scale data processing. By the end of 2024, there were 1,136 operational hyperscale data centers globally, a figure that doubled over the previous five years, with the U.S. accounting for approximately 54% of total hyperscale capacity. In particular, the three largest operators, Amazon Web Services, Microsoft Azure, and Google Cloud, collectively account for approximately 59% of all hyperscale data center capacity globally. As a growing trend, hyperscale data centers represented about 41% of worldwide data center capacity in 2024 and are projected to exceed 60% by 2029 as enterprise on-premises infrastructure continues to decline. Moreover, as artificial intelligence (AI) is becoming widely used, AI data centers are being built more rapidly, and they can consume as much electricity as 100,000 households, more than conventional data centers. Since 2024, there has been widespread grassroots Opposition to AI Data Centers.

### Edge

Edge data centers are smaller facilities, typically ranging from 1 to 10 megawatts. They are positioned closer to end users or data sources to reduce network latency and support real-time applications, such as autonomous vehicles, industrial automation, and content delivery. Unlike hyperscale data centers, edge data centers are intentionally distributed across many locations rather than consolidated, with deployments occurring in urban areas, cell tower sites, as well as industrial locations. The growth of edge computing infrastructure has been tied to the expansion of 5G wireless networks and the increasing use of Internet of Things (IoT) devices, which generate data that is more efficiently processed near its source than transmitted to a centralized data center.

Micro data centers (MDCs) are access-level data centers that are smaller in size than traditional data centers but provide the same features. They are typically located near the data source to reduce communication delays, as their small size allows several MDCs to be spread out over a wide area. MDCs are suited to user-facing, front end applications. They are commonly used in edge computing and other areas where low latency data processing is needed.

#### Modularity and flexibility

Modularity and flexibility are key elements in allowing a data center to grow and change over time. Data center modules are pre-engineered, standardized building blocks that can be configured and moved as needed.

A modular data center may consist of data center equipment contained within shipping containers or similar portable containers. Components of the data center can be prefabricated and standardized, which facilitates moving if needed.

These modular data centers are useful for IT disaster recovery. Mobile data centers are also used to move large quantities of data, by physically transporting the hardware that contains it, and in cryptocurrency mining, where fleets of mobile data centers are transported to take advantage of cheaper sources of energy.


## History

Data centers have their roots in the huge computer rooms of the 1940s, typified by the Electronic Numerical Integrator and Computer (ENIAC), one of the earliest examples of a data center. Early computer systems were complex to operate and maintain, and required a special environment in which to operate. Many cables were necessary to connect all of the components, and methods to accommodate and organize these were devised such as standard racks to mount equipment, raised floors, and cable trays (installed overhead or under the elevated floor). A single mainframe required a great deal of power and had to be cooled to avoid overheating. Security became important – computers were expensive, and were often used for government and military purposes. As such, basic design guidelines for controlling access to the computer room were devised.

During the microcomputer industry boom of the 1980s, computers started to be deployed everywhere, in many cases with little or no care about operating requirements. However, as information technology (IT) operations started to grow in complexity, organizations grew aware of the need to control IT resources. The availability of inexpensive networking equipment, coupled with new standards for the network structured cabling, made it possible to use a hierarchical design that put servers in a specific room inside the company. The use of the term *data center*, as applied to specially designed computer rooms, started to gain popular recognition about this time.

During the dot-com bubble (1997–2000), there was a boom in data center construction because companies needed fast Internet connectivity and non-stop operation to establish their Internet presence. Many companies started building very large facilities, called **internet data centers** (IDCs), which provided enhanced capabilities, such as crossover backup: "If a Bell Atlantic line is cut, we can transfer them to ... to minimize the time of outage."

The global data center market saw steady growth in the 2010s, with a notable acceleration in the latter half of the decade. According to Gartner, worldwide data center infrastructure spending reached $200 billion in 2021, representing a 6% increase from 2020 despite economic challenges posed by the COVID-19 pandemic.

In 2024, global energy consumption from data centers was 620 TWh, with 80% of that consumption concentrated in the U.S., China, and the United Kingdom. Colocation centers were the most common category worldwide, with 4,799 colocation centers in 127 countries. In that year, the largest data center in the world was Citadel, owned by Switch, at the Tahoe Reno Industrial Center in Reno, Nevada, occupying 7.2 million square feet.

Growth of the data center industry has prompted local resistance. A 2023 survey found social mobilizations against the industry in Europe, the U.S., and South America. These movements expressed concern about the centers' energy and water use, pollution, and impact on agriculture or the landscape. A 2026 poll by *Politico* suggested that resistance to growth of the industry would make candidates' stance on data centers a significant issue for voters in the U.S.

### In the United States

The U.S. hosted 5,381 data centers in March 2024, the highest number of any country worldwide, accounting for 40% of the global market in 2023. As of 2023, about 80% of U.S. data center load was concentrated in 15 states, led by Virginia and Texas. As of 2025, roughly one third of America's data centers were in three states: Virginia (643), Texas (395), and California (319).

The largest concentration of data centers in the world is in Northern Virginia, with over 250 facilities in the region. In 2025, Georgia was the fastest growing data center hub in the U.S., having enacted several state tax exemptions for the industry and hosting between 100 and 150 centers in the state. Local governments have responded to the growing industry in Georgia with a variety of local ordinances to guide permitting of these facilities.

The consultancy firm McKinsey & Co., projected U.S. demand to double to 35 gigawatts (GW) by 2030, up from 17 GW in 2022. A study published by the Electric Power Research Institute (EPRI) in May 2024 estimated that data centers could consume between 4.6% and 9.1% of the country's electricity generation by 2030. In 2025, it was estimated that the U.S. GDP growth was only 0.1% without the investments in data centers for artificial intelligence.


## Design

Data centers house critical computing resources in a controlled environment and must generally operate with very high availability. Key design elements include providing power for the equipment, temperature and humidity control, cabling, fire safety, and security.

Information security is also a concern. For this reason, a data center has to offer a secure environment that minimizes the chances of a security breach.

### Obsolescence and modernization

Industry research company International Data Corporation (IDC) puts the average age of a data center at nine years old. Gartner, another research company, says data centers older than seven years are obsolete. The growth in data (163 zettabytes by 2025) is one factor driving the need for data centers to modernize.

Focus on modernization is not new. Rapid obsolescence of data center equipment was a concern by at least 2007, and in 2011, Uptime Institute was concerned about aging equipment.

### Industry standards

The Telecommunications Industry Association (TIA)'s Telecommunications Infrastructure Standard for Data Centers specifies the minimum requirements for telecommunications infrastructure of data centers and computer rooms, including single tenant enterprise data centers and multi-tenant Internet hosting data centers. The topology proposed in this document is intended to be applicable to any size data center.

Telcordia GR-3160, *NEBS Requirements for Telecommunications Data Center Equipment and Spaces*, provides guidelines for data center spaces within telecommunications networks, and environmental requirements for the equipment intended for installation in those spaces. These criteria were developed jointly by Telcordia and industry representatives. They may be applied to data center spaces housing data processing or IT equipment. The equipment may be used to:

- Operate and manage a carrier's telecommunication network
- Provide data center-based applications directly to the carrier's customers
- Provide hosted applications for a third party to provide services to their customers
- Provide a combination of these and similar data center applications

### Reliability of electrical power supply

Power supplies, either back up or continuous onsite power, consist of one or more uninterruptible power supplies, battery banks, diesel, gas turbine, and/or gas engine generating sets. Greater primary fuel energy efficiency can be achieved with the use of cogeneration technology, generating electricity, heating, and cooling onsite.

To prevent single points of failure, all elements of the electrical systems, including backup systems, are typically given redundant copies, and critical servers are connected to both the *A-side* and *B-side* power feeds. This arrangement is often made to achieve N+1 redundancy in the systems. Static transfer switches are sometimes used to ensure instantaneous switchover from one supply to the other in the event of a power failure.

### Low-voltage cable routing

Options for low-voltage cable routing might include data cabling that is routed through overhead cable trays; raised floor cabling, both for security reasons and to avoid the extra cost of cooling systems over the racks; and anti-static tiles for flooring, especially in low-cost data centers.

### Environmental control

Maintaining suitable temperature and humidity levels is critical to preventing equipment damage caused by overheating. Overheating can cause components (usually the silicon or copper of the wires or circuits) to melt, causing loose connections and fire hazards. Typical temperature control methods include air conditioning and indirect cooling, such as the use of outside air, indirect evaporative cooling units, and seawater cooling.

Airflow management is the practice of achieving data center cooling efficiency by preventing the recirculation of hot exhaust air and by reducing bypass airflow. Common approaches include hot-aisle/cold-aisle containment and the deployment of in-row cooling units, which position cooling directly between server racks to intercept exhaust heat before it mixes with room air.

Humidity control prevents moisture and related issues. For example, excess humidity can cause dust to adhere more readily to fan blades and heat sinks, impeding air cooling and leading to higher temperatures.

#### Aisle containment

Cold aisle containment is done by exposing the rear of equipment racks, while the fronts of the servers are enclosed with doors and covers. This is similar to how large-scale food companies refrigerate and store products.

Computer cabinets/server farms are often organized for containment of hot/cold aisles. Proper air duct placement prevents cold and hot air from mixing. Rows of cabinets are paired to face each other so the cool and hot air intakes and exhausts do not mix air, which would severely reduce cooling efficiency.

Alternatively, a range of underfloor panels can create efficient cold air pathways directed to the raised-floor vented tiles. Either the cold aisle or the hot aisle can be contained.

Another option is fitting cabinets with vertical exhaust duct chimneys. Hot exhaust pipes/vents/ducts can direct the air into a plenum space above a dropped ceiling and back to the cooling units or to outside vents. With this configuration, traditional hot/cold aisle configuration is not required.

### Fire protection

Data centers feature fire protection systems, including passive and active design elements, as well as implementation of fire prevention programs in operations. Smoke detectors are usually installed to provide early warning of a fire.

Although the main room usually does not allow wet pipe-based systems due to the fragile nature of circuit boards, there are systems that can be used in the rest of the facility or in cold/hot aisle air circulation systems that are closed systems. These include sprinkler systems and misting, the latter of which uses high pressure to create extremely small water droplets and can be used in sensitive rooms due to the nature of the droplets.

However, there are other means to put out fires, especially in Sensitive areas, usually using gaseous fire suppression, of which Halon gas was the most popular, until the negative effects of producing and using it were discovered.

### Security

Physical access to data centers is usually restricted. Layered security often starts with fencing, bollards, and mantraps. Video camera surveillance and permanent security guards are almost always present if the data center is large or contains sensitive information. Fingerprint recognition is starting to become commonplace.

Logging access is required by some data protection regulations; some organizations tightly link this to access control systems. Multiple log entries can occur at the main entrance, entrances to internal rooms, and at equipment cabinets. Access control at cabinets can be integrated with intelligent power distribution units, so locks are networked through the same appliance.

### Transformation

Data center transformation takes a step-by-step approach through integrated projects carried out over time. This differs from a traditional method of data center upgrades, which takes a serial and siloed approach. Typical projects within a data center transformation initiative include standardization/consolidation, virtualization, automation, and security.

Data center consolidation consists of reducing the number of data centers and avoiding *server sprawl* (both physical and virtual), which often includes replacing aging data center equipment. This process is aided by standardization, which makes these systems follow a uniform set of configurations to simplify and improve efficiency. Automating tasks such as provisioning, configuration, patching, release management, and compliance are other ways in which data centers can be upgraded. These changes are needed not just when facing fewer skilled IT workers. Lastly, security initiatives integrate the protection of virtual systems with existing security for physical infrastructures.

### Raised floor

The first raised floor computer room was made by IBM in 1956 to allow access for wiring. During the 1970s, raised floors became more common because they allow cool air to circulate more efficiently. A raised floor standards guide (GR-2930) was developed by Telcordia Technologies, a subsidiary of Ericsson.

### Lights out

The "lights-out" data center, also known as a darkened or dark data center, is a data center that has largely eliminated the need for direct access by personnel, except under extraordinary circumstances. Due to the lack of need for staff to enter the data center, it can be operated without lighting. All of the devices are accessed and managed by remote systems, with automation programs used to perform unattended operations. In addition to the energy savings, reduction in staffing costs, and the ability to locate the site further from population centers, implementing a lights-out data center also reduces the threat of malicious attacks upon the infrastructure.

### Noise levels

Generally, local authorities prefer noise levels at data centers to be "10 dB below the existing night-time background noise level at the nearest residence."

Occupational Safety and Health Administration (OSHA) regulations require monitoring of noise levels inside data centers if noise exceeds 85 decibels. The average noise level in server areas of a data center may reach as high as 92–96 dB(A).

Residents living near data centers have described the sound as "a high-pitched whirring noise 24/7", saying "It's like being on a tarmac with an airplane engine running constantly ... Except that the airplane keeps idling and never leaves."

External sources of noise include HVAC (heating, ventilation, and air conditioning) equipment and energy generators.

### Site selection

Location factors include proximity to power grids, telecommunications infrastructure, networking services, transportation lines, and emergency services. Other considerations should include flight paths, neighboring power drains, geological risks, and climate (associated with cooling costs).

Local political considerations, such as availability of subsidies and lack of opposition, are also important factors in locating data centers.

### High availability

Various metrics exist to measure the data-availability that results from data-center availability beyond 95% uptime, with the top of the scale counting how many *nines* can be placed after *99%*. The costs of avoiding downtime should not exceed the cost of the downtime itself.

### Dynamic infrastructure

Dynamic infrastructure provides the ability to intelligently, automatically, and securely move workloads within a data center anytime, anywhere, for migrations, provisioning, to enhance performance, or build co-location facilities. It also facilitates performing routine maintenance on either physical or virtual systems, all while minimizing interruption. A related concept is Composable Infrastructure, which allows for the dynamic reconfiguration of the available resources to suit needs, only when needed.

Side benefits include:

- reducing cost
- facilitating business continuity and high availability
- enabling cloud and grid computing.

### Network infrastructure

Communications in modern data centers are most often based on networks running the Internet protocol suite. Data centers contain a set of routers and switches that transport traffic between the servers and to the outside world, which are connected according to the data center network architecture. Redundancy of the internet connection is often provided by using two or more upstream service providers (see Multihoming).

Some of the servers at a data center are used for running the basic internet and intranet services needed by internal users in the organization, e.g., e-mail servers, proxy servers, and DNS servers.

Network security elements are also usually deployed: firewalls, VPN gateways, intrusion detection systems, and so on. Also common are monitoring systems for the network and some of the applications. Additional off-site monitoring systems are also typical, in case of a failure of communications inside the data center.


## Energy use

Energy consumption and the environmental impacts it creates are a central issue for data centers. Power draw ranges from a few kilowatts (kW) for small server racks to several tens of megawatts (MW) for large facilities. Modern hyperscale data centers can exhibit power densities exceeding 100 times those of conventional office buildings, primarily due to the high concentration of servers and cooling systems required to manage continuous digital workloads. For higher power density facilities, electricity costs are a dominant operating expense and account for over 10% of the total cost of ownership (TCO) of a data center.

As of 2024, data centers in the U.S. are primarily powered by natural gas, which supplies 40% of their electricity (with renewable energy at 24%, nuclear at about 20%, and coal at about 15%). The *Associated Press* reported that electricity for AI data centers in the U.S. would likely come from natural gas or oil, as companies prefer using currently available power plants, which primarily use fossil fuels. Fossil energy is also often cheaper in locations where data centers are developed, and experts believe that energy demands from generative AI and data centers would be difficult to fulfill with renewable energy alone. Some companies such as Google, Amazon, and Meta have expressed interest in nuclear power for their data centers. As of 2020, according to the IEA, solar photovoltaic-generated electricity is at its lowest cost in history. Other data centers, including xAI's Colossus, OpenAI's Stargate, and Meta's Prometheus use their own off-grid natural gas plants. Electric vehicle and lithium-ion batteries have also been used for powering data centers, including for Colossus.

Power utility companies make upgrades to their infrastructure to handle demands of new data centers, and the price for these changes typically falls on residential or smaller commercial consumers. In 2025, the Mountain Valley Pipeline announced plans to expand its capacity by 25% to meet energy needs for data centers.

In December 2025, the Federal Energy Regulatory Commission (FERC) published a unanimous order allowing data centers in the U.S. to have a direct connection with power plants. United States Secretary of Energy Chris Wright expressed support for un-retiring coal plants to power AI data centers. Electricity demands from AI data centers have slowed or reversed the retirement of peaking power plants in the U.S. For example, in 2025, Southern Company announced that energy use from data centers would prevent the company from retiring coal-fired power plants as it had earlier promised. In Nevada, the Desert Research Institute (DRI) calculated that 35% of the state's energy production could go to data centers by the year 2030 if all projects planned in the state as of 2026 are completed. DRI also stated, in areas where there are clusters of data centers, local consumers may end up paying the extra cost of expanding infrastructure.

### Greenhouse gas emissions

In 2024, data centers were estimated to account for about 1.5% of global electricity consumption (approximately 415 TWh) and around 1% of greenhouse gas emissions according to U.S. Environmental Protection Agency (EPA). However, the rapid expansion is causing projections to rise sharply. Due to accelerated demand from AI, data center's global electricity consumption is projected to more than double to around 945 TWh by 2030 in the IEA's base-case scenario, which represents just under 3% of 2030 total global electricity consumption. This growing electricity demand, much of which is still generated by fossil fuels, increases the potential environmental impacts. In addition to operational energy demand, embodied life cycle emissions should be considered, which include the extraction, manufacturing, transportation, and recycling or disposal of materials used in the construction of facilities and hardware.

Global data center carbon dioxide emissions are projected to rise from an estimated 220 million tonnes in 2024 to 300–320 million tonnes by 2035. In 2024, Google and Microsoft each consumed more power than over 100 countries. As a result, there is increasing industry pressure for decarbonization. Companies are pursuing direct clean energy agreements, such as Tencent who has pledged to be carbon neutral by 2030, and Microsoft's 2024 agreement to re-open the Three Mile Island nuclear power plant to provide 100% of the electric power for its AI data centers for 20 years.

### Economic analysis of energy use

#### Energy efficiency and overhead

The most commonly used energy efficiency metric for data centers is power usage effectiveness (PUE), calculated as the ratio of total power entering the data center divided by the power used by IT equipment.

PUE =

⁠

Total Facility Power

/

IT Equipment Power

⁠

= 1 +

⁠

Non IT Facility Energy

/

IT Equipment Energy

⁠

PUE measures the percentage of power used by overhead devices (cooling, lighting, etc.). The average U.S. data center has a PUE of 2.0, meaning two watts of total power (overhead + IT equipment) for every watt delivered to IT equipment. State-of-the-art data centers are estimated to have a PUE of roughly 1.2. Google publishes quarterly efficiency metrics from its data centers in operation. PUEs of as low as 1.01 have been achieved with two-phase immersion cooling.

The EPA has an Energy Star rating for standalone or large data centers. To qualify for the ecolabel, a data center must be within the top quartile in energy efficiency of all reported facilities. The Energy Efficiency Improvement Act of 2015 (U.S.) requires federal facilities—including data centers—to operate more efficiently. California's Title 24 (2014) of the California Code of Regulations mandates that every newly constructed data center must have some form of airflow containment in place to optimize energy efficiency.

The European Union (EU) also has a similar initiative: EU Code of Conduct for Data Centres.

Efficiency improvements and renewable energy integration are helping offset some emissions, but fossil fuels remain a major electricity source for data center operations worldwide.

In 2011, server racks in data centers were designed for more than 25 kW, and the typical server was estimated to waste about 30% of the electricity it consumed. The energy demand for information storage systems is also rising. A high-availability data center is estimated to have a 1 MW demand and consume $20 million in electricity over its lifetime, with cooling representing 35% to 45% of the data center's total cost of ownership. Calculations show that in two years, the cost of powering and cooling a server could be equal to the cost of purchasing the server hardware. Research in 2018 showed that a substantial amount of energy could still be conserved by optimizing IT refresh rates and increasing server use. Research for optimizing task scheduling is also underway, with researchers looking to implement energy-efficient scheduling algorithms that could reduce energy consumption by anywhere between 6% and 44%.

In 2011, Facebook, Rackspace, and others founded the Open Compute Project (OCP) to develop and publish open standards for greener data center computing technologies. As part of the project, Facebook published the designs of its server, which it had built for its first dedicated data center in Prineville. Making servers taller left space for more effective heat sinks and enabled the use of fans that moved more air with less energy. By not buying commercial off-the-shelf servers, energy consumption due to unnecessary expansion slots on the motherboard and unneeded components, such as a graphics card, was also saved. In 2016, Google joined the project and published the designs of its 48V DC shallow data center rack. This design had long been part of Google data centers. By eliminating the multiple transformers usually deployed in data centers, Google had achieved a 30% increase in energy efficiency. In 2017, sales for data center hardware built to OCP designs topped $1.2 billion and are expected to reach $6 billion by 2021.

#### Power and cooling analysis

Power is the largest recurring cost to the user of a data center. In 2008, the ASHRAE recommended a temperature range of 64.4 °F (18.0 °C) to 80.6 °F (27.0 °C), though some data centers could operate at higher temperatures. However, cooling at or below 70 °F (21 °C) wastes money and energy. Furthermore, overcooling equipment in environments with a high relative humidity can expose equipment to a high amount of moisture that facilitates the growth of salt deposits on conductive filaments in the circuitry.

A **power and cooling analysis**, also referred to as a thermal assessment, measures the relative temperatures in specific areas as well as the capacity of the cooling systems to handle specific ambient temperatures. A power and cooling analysis can help identify hot spots, over-cooled areas that can handle greater power use density, the breakpoint of equipment loading, the effectiveness of a raised-floor strategy, and optimal equipment positioning (such as AC units) to balance temperatures across the data center. Power cooling density is a measure of how much square footage the center can cool at maximum capacity. The cooling of data centers is the second largest power consumer after servers, with cooling taking about 7% to 30% of energy usage (depending on efficiency), compared to an average of 60% of energy used by servers.

#### Energy efficiency analysis

An energy efficiency analysis measures the energy use of data center IT and facilities equipment. A typical energy efficiency analysis measures factors such as a data center's Power Use Effectiveness (PUE) against industry standards, identifies mechanical and electrical sources of inefficiency, and identifies air-management metrics. However, the limitation of most current metrics and approaches is they do not include IT in the analysis. Case studies have shown that by addressing energy efficiency holistically in a data center, major efficiencies can be achieved that are not possible otherwise.

#### Computational fluid dynamics (CFD) analysis

Computational fluid dynamics (CFD) analysis uses sophisticated tools and techniques to understand the unique thermal conditions present in each data center—predicting the temperature, airflow, and pressure behavior of a data center to assess performance and energy consumption using numerical modeling. By predicting the effects of these environmental conditions, CFD analysis can be used to predict the impact of high-density racks mixed with low-density racks and the onward impact on cooling resources, poor infrastructure management practices, and AC failure or AC shutdown for scheduled maintenance.

#### Thermal zone mapping

Thermal zone mapping uses sensors and computer modeling to create a three-dimensional image of the hot and cool zones in a data center. This information can help identify optimal positioning of data center equipment. For example, critical servers might be placed in a cool zone that is serviced by redundant AC units.

#### Green data centers

Data centers use a lot of power, consumed via two main usages: the power required to run the equipment and the power required to cool the equipment. Power efficiency reduces the first category.

Cooling cost reduction through natural means includes location decisions. When the focus is avoiding good fiber connectivity, power grid connections, and people concentrations to manage the equipment, a data center can be miles away from users. Mass data centers like Google or Facebook do not need to be near population centers. Arctic locations that can use outside air, which provides cooling, are becoming more popular. Countries with favorable conditions, such as Canada, Finland, Sweden, Norway, and Switzerland are trying to attract cloud computing data centers.

Singapore lifted a three-year ban on new data centers in April 2022. A major data center hub for the Asia-Pacific region, Singapore lifted its moratorium on new data center projects in 2022, granting four new projects, but rejecting more than 16 data center applications from over 20 received. Singapore's new data centers will meet very strict green technology criteria, including "Water Usage Effectiveness (WUE) of 2.0/MWh, Power Usage Effectiveness (PUE) of less than 1.3, and have a "Platinum certification under Singapore's BCA-IMDA Green Mark for New Data Centre" criteria that clearly addressed decarbonization and use of hydrogen cells or solar panels.

#### Energy reuse

It is very difficult to reuse the heat that comes from air-cooled data centers. For this reason, data center infrastructures are more often equipped with heat pumps.


## Power infrastructure

The rapid growth of artificial intelligence (AI) and high-performance computing workloads has increased attention on data center power infrastructure, particularly the relationship between electrical reliability, deployment timelines, energy costs, and decarbonization objectives. Industry publications have described phased approaches to infrastructure development that enable operators to deploy power capacity rapidly while maintaining pathways toward lower-carbon energy systems as technologies, fuel availability, grid capacity, and economics evolve.

Recent industry discussion has also emphasized "speed-to-power" as a significant consideration in data center development, reflecting the growing importance of securing electrical capacity and resilient power systems within increasingly compressed project timelines.


## Regulation and policy responses

In the 2020s, the rapid growth of data center construction gave rise to policy debates over tax incentives, electricity grid, water resources, and climate commitments.

### Tax incentives

By 2024, at least 36 U.S. states had introduced specific tax incentives aimed at attracting data center investment, most often in the form of sales tax exemptions on servers, networking equipment, and electricity. Virginia hosts the largest concentration of data centers in the U.S., and a December 2024 audit by its Joint Legislative Audit and Review Commission (JLARC) put the industry's annual contribution at roughly 74,000 jobs and $9.1 billion in gross state product. The audit reported that the state's sales and use tax exemption was claimed by about 90% of operators and that reduced state revenue by an estimated $928 million in fiscal year 2023. Thus, JLARC concluded that ending the exemption would likely shrink Virginia's share of new data center investment.

Economists have debated the effectiveness of such incentives more broadly. A review published in the *Journal of Economic Perspectives* (JEP) found that state and local business tax incentives in the U.S. had roughly tripled since the 1990s to about $30 billion per year, and reported no strong evidence that firm-specific incentives increase broader economic growth at the state or local level. Further, research by Timothy Bartik of the Upjohn Institute estimated that economic development incentives change firm location decisions in only 2% to 25% of cases.

In response to tax exemption policies, several jurisdictions have started to reevaluate incentives for data centers. In 2024, the Georgia General Assembly passed legislation to terminate the state's data center sales tax exemption. However, the bill was ultimately vetoed by Governor Brian Kemp. In another case in 2026, the Virginia Senate voted 28 to 12 to phase out the state's data center sales tax exemption as part of broader budget negotiations.

### Water usage

Most large data centers use water for evaporative cooling of their servers, and the volumes involved have drawn growing scrutiny. A 2021 study in *npj Clean Water* estimated that U.S. data centers directly consume about 1.7 billion liters of water per day, with up to 57% of that drawn from potable supplies, and noted that fewer than one-third of operators measured their water use at the time. A separate study published in *Environmental Research Letters* found that about one-fifth of direct water use by U.S. data centers came from moderately or highly water-stressed watersheds, and that nearly half of the country's servers ran on electricity drawn from water-stressed regions. According to a 2024 Berkeley Lab report, data centers in the U.S. had used approximately 17 billion gallons of water. The same report expected hyperscale data centers specifically to use 16 to 33 billion gallons of water per year by 2028.

In Virginia, the December 2024 JLARC audit reported that data centers in the state consumed about 2.1 billion gallons of water in 2023, an 86% increase since 2019, and that roughly one-third of that came from reclaimed water rather than potable supplies. The audit recommended that local governments be authorized to require water-use estimates as part of the data center permitting process.

There is no federal U.S. standard requiring data center operators to disclose water consumption, and access to facility-level data has often been limited by non-disclosure agreements (NDAs) with host municipalities. In 2022, the city of The Dalles, Oregon, settled a public records lawsuit brought by *The Oregonian*, after which Google ended its nationwide practice of treating site-level water use as a trade secret. In 2025, several states considered legislation to require data centers to disclose water use, including bills in Virginia, California, and New Jersey, although each was vetoed by the state's governor that year.

### Electricity and grid policy

The growth of data center electricity demand in the 2020s has prompted regulatory debates over grid capacity, transmission planning, and how the costs of new infrastructure should be allocated among customers. The 2024 Lawrence Berkeley National Laboratory (LBNL) report on U.S. data center energy use, prepared at the request of the U.S. Congress, estimated that data centers accounted for about 4.4% of national electricity consumption in 2023 and projected a rise to between 6.7% and 12% by 2028, depending on growth scenarios. In 2025, the IEA projected that data centers would account for nearly half of new U.S. electricity demand growth through 2030.

The North American Electric Reliability Corporation (NERC), the federally designated electric reliability organization for the U.S., identified data centers as the single largest driver of projected demand growth in its 2024 long-term reliability assessment. Additionally, NERC documented a voltage event in the PJM Interconnection region in July 2024, in which roughly 1,500 megawatts of data center load disconnected simultaneously across about 60 facilities.

How the costs of meeting this demand are shared has also become a central policy question. The JLARC audit in 2024 estimated that, without any changes to how rates are designed, typical residential customers of Dominion Energy Virginia could see their bills rise by $14 to $37 per month by 2040 because of data center-driven grid investment. As such, the report recommended creating a separate customer rate class for large data centers. Some researchers have urged caution in interpreting demand projections. Furthermore, a 2024 commentary in the journal *Joule* argued that public estimates of future data center electricity use vary widely and that utilities have historically over-forecasted load growth, and called for more transparent data on actual facility-level consumption.

### Climate policy alignment

The growth of data centers has raised questions about whether the renewable energy commitments made by their operators are consistent with broader climate goals. Many large operators report meeting electricity-related emissions targets through annual purchases of renewable energy certificates (RECs) or matching their total annual consumption with renewable generation. In 2022, a study by *Nature Climate Change* analyzed 115 companies with Science Based Targets. It found that about 42% of their reported Scope 2 emissions reductions disappeared once REC-based claims were excluded. This directly suggests that some corporate climate progress reflected accounting choices rather than actual reductions in grid emissions.

In response, some operators and researchers have proposed 24/7 carbon-free energy matching. Under this approach, every hour of a facility's electricity use must be matched with carbon-free generation on the same regional grid. A 2024 *Joule* study modeled the idea. The authors found that annual or volumetric matching did little to cut grid emissions under current U.S. policy. Hourly 24/7 matching cut more, but it cost about $13 to $30 more per megawatt-hour.

The tension between data center expansion and corporate climate goals has also become apparent in the operators' own disclosures of information. In 2024, Google reported its greenhouse gas emissions had risen by about 48% since 2019, attributing the increase in large part to data center electricity use associated with AI workloads. Similarly, Microsoft reported in 2024 that its emissions had risen by about 29% since 2020, citing the construction and operation of new data centers. Moreover, the IEA projected in 2025 that global data center carbon dioxide emissions could peak at around 320 million tonnes by 2030 before declining slightly through 2035, with the trajectory depending heavily on the carbon intensity of the electricity supplied to new facilities.
