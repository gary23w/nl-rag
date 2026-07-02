---
title: "Manufacturing execution system"
source: https://en.wikipedia.org/wiki/Manufacturing_execution_system
domain: manufacturing-execution-systems
license: CC-BY-SA-4.0
tags: manufacturing execution system, isa-95, overall equipment effectiveness, statistical process control
fetched: 2026-07-02
---

# Manufacturing execution system

**Manufacturing execution systems** (**MES**) are computerized systems used in manufacturing to track and document the transformation of raw materials to finished goods. MES provides information that helps manufacturing decision-makers understand how current conditions on the plant floor can be optimized to improve production output. MES works as real-time monitoring system to enable the control of multiple elements of the production process (e.g. inputs, personnel, machines and support services).

MES may operate across multiple function areas, for example management of product definitions across the product life-cycle, resource scheduling, order execution and dispatch, production analysis and downtime management for overall equipment effectiveness (OEE), product quality, or materials track and trace. MES creates the "as-built" record, capturing the data, processes and outcomes of the manufacturing process. This can be especially important in regulated industries, such as food and beverage or pharmaceutical, where documentation and proof of processes, events and actions may be required.

## Modern trends

As of 2025, the manufacturing execution systems are shifting from rigid, monolithic on-premise software to modular, cloud-connected platforms. Key drivers of this evolution include:

- **Cloud and hybrid architectures:** While traditional MES relied entirely on local servers, modern systems often utilize a "hybrid" approach. Critical real-time control functions remain on the "edge" (on-premise) to ensure low latency and security, while heavy data analytics and long-term storage are offloaded to cloud platforms.
- **Low-code/no-code platforms:** New platforms allow manufacturing engineers to create custom applications and dashboards using drag-and-drop interfaces without requiring deep programming knowledge. This "citizen developer" model reduces the cost and time required to customize MES workflows compared to legacy systems.
- **AI and predictive analytics:** Modern MES integrates with AI and machine learning algorithms. Instead of merely reporting past production failures, these systems analyze historical data to predict equipment maintenance needs (predictive maintenance) and optimize production schedules dynamically.

## Benefits

"Manufacturing execution systems [help] create flawless manufacturing processes and provide real-time feedback of requirement changes", and provide information at a single source. Other benefits from a successful MES implementation might include:

- Reduced waste, re-work and scrap, including quicker setup times
- More accurate capture of cost information (e.g. labour, scrap, downtime, and tooling)
- Increased uptime
- Incorporate paperless workflow activities
- Manufacturing operations traceability
- Decreased downtime and easy fault finding
- Reduced inventory, through the eradication of just-in-case inventory

## MES

A wide variety of systems arose using collected data for a dedicated purpose. Further development of these systems during the 1990s introduced overlap in functionality. Then the Manufacturing Enterprise Solutions Association International (MESA) introduced some structure by defining 11 functions that set the scope of MES. In 2000, the ANSI/ISA-95 standard merged this model with the Purdue Reference Model (PRM).

A functional hierarchy was defined in which MES were situated at Level 3 between ERP at Level 4 and process control at Levels 0, 1, 2. With the publication of the third part of the standard in 2005, activities in Level 3 were divided over four main operations: production, quality, logistics and maintenance.

Between 2005 and 2013, additional or revised parts of the ANSI/ISA-95 standard defined the architecture of an MES into more detail, covering how to internally distribute functionality and what information to exchange internally as well as externally.

## Functional areas

Over the years, international standards and models have refined the scope of such systems in terms of activities. These typically include:

- Management of product definitions. This may include storage, version control and exchange with other systems of master data like product production rules, bill of material, bill of resources, process set points and recipe data all focused on defining how to make a product. Management of product definitions can be part of product lifecycle management.
- Management of resources. This may include registration, exchange and analysis of resource information, aiming to prepare and execute production orders with resources of the right capabilities and availability.
- Scheduling (production processes). These activities determine the production schedule as a collection of work orders to meet the production requirements, typically received from enterprise resource planning (ERP) or specialized advanced planning and scheduling systems, making optimal use of local resources.
- Dispatching production orders. Depending on the type of production processes this may include further distribution of batches, runs and work orders, issuing these to work centers and adjustment to unanticipated conditions.
- Execution of production orders. Although actual execution is done by process control systems, an MES may perform checks on resources and inform other systems about the progress of production processes.
- Collection of production data. This includes collection, storage and exchange of process data, equipment status, material lot information and production logs in either a data historian or relational database.
- Production performance analysis. Create useful information out of the raw collected data about the current status of production, like Work In Progress (WIP) overviews, and the production performance of the past period like the overall equipment effectiveness or any other performance indicator.
- Production track and trace. Registration and retrieval of related information in order to present a complete history of lots, orders or equipment (particularly important in health related productions, e.g. pharmaceuticals).

## Relationship with other systems

MES integrates with ISA-95 (previous Purdue Reference Model, “95”) with multiple relationships.

### Relationship with other Level 3 systems

The collection of systems acting on the ISA-95 Level 3 can be called manufacturing operations management systems (MOMS). Apart from an MES, there are typically laboratory information management system (LIMS), warehouse management system (WMS) and computerized maintenance management system (CMMS). From the MES point of view, possible information flows are:

- To LIMS: quality test requests, sample lots, statistical process data
- From LIMS: quality test results, product certificates, testing progress
- To WMS: material resource requests, material definitions, product deliveries
- From WMS: material availability, staged material lots, product shipments
- To CMMS: equipment running data, equipment assignments, maintenance requests
- From CMMS: maintenance progress, equipment capabilities, maintenance schedule

### Relationship with Level 4 systems

Examples of systems acting on ISA-95 Level 4 are product lifecycle management (PLM), enterprise resource planning (ERP), customer relationship management (CRM), human resource management (HRM), and process development execution system (PDES). From the MES point of view, possible information flows are:

- To PLM: production test results
- From PLM: product definitions, bill of operations (routings), electronic work instructions, equipment settings
- To ERP: production performance results, produced and consumed material
- From ERP: production planning, order requirements
- To CRM: product tracking and tracing information
- From CRM: product complaints
- To HRM: personnel performance
- From HRM: personnel skills, personnel availability
- To PDES: production test and execution results
- From PDES: manufacturing flow definitions, design of experiments (DoE) definitions

In many cases, middleware enterprise application integration (EAI) systems are being used to exchange transaction messages between MES and Level 4 systems. A common data definition, B2MML, has been defined within the ISA-95 standard to link MES systems to these Level 4 systems.

### Relationship with Level 0, 1, 2 systems

Systems acting on ISA-95 Level 2 are supervisory control and data acquisition (SCADA), programmable logic controllers (PLC), distributed control systems (DCS) and building automation systems (BAS). Information flows between MES and these process control systems are roughly similar:

- To PLCs: work instructions, recipes, set points
- From PLCs: process values, alarms, adjusted set points, production results

Most MES systems include connectivity as part of their product offering. Direct communication of plant floor equipment data is established by connecting to the PLC. Often, plant floor data is first collected and diagnosed for real-time control in a DCS or SCADA system. In this case, the MES systems connect to these Level 2 systems for exchanging plant floor data.

The industry standard for plant floor connectivity has evolved from OLE for Process Control (OPC) to OPC Unified Architecture (OPC-UA). Unlike its predecessor, OPC-UA is platform-independent, allowing it to run on Linux and embedded devices while offering robust security models.

In modern Industry 4.0 architectures, MES connectivity often extends beyond the traditional hierarchy. Systems increasingly utilize IIoT protocols like MQTT (often with Sparkplug B) to transmit lightweight data to cloud-based analytics platforms, creating a hybrid architecture where OPC-UA handles complex machine data and MQTT handles rapid telemetry.
