---
title: "Building performance simulation"
source: https://en.wikipedia.org/wiki/Building_energy_simulation
domain: building-energy-management
license: CC-BY-SA-4.0
tags: building management system, energy management system, energy audit, occupancy sensor
fetched: 2026-07-02
---

# Building performance simulation

(Redirected from

Building energy simulation

)

**Building performance simulation** (BPS) is the replication of aspects of building performance using a computer-based, mathematical model created on the basis of fundamental physical principles and sound engineering practice. The objective of building performance simulation is the quantification of aspects of building performance which are relevant to the design, construction, operation and control of buildings. Building performance simulation has various sub-domains. Most prominent are thermal simulation, lighting simulation, acoustical simulation and air flow simulation. Most building performance simulation is based on the use of bespoke simulation software. Building performance simulation itself is a field within the wider realm of scientific computing.

## Introduction

From a physical point of view, a building is a very complex system, influenced by a wide range of parameters. A simulation model is an abstraction of the real building which allows to consider the influences on high level of detail and to analyze key performance indicators without cost-intensive measurements. BPS is a technology of considerable potential that provides the ability to quantify and compare the relative cost and performance attributes of a proposed design in a realistic manner and at relatively low effort and cost. Energy demand, indoor environmental quality (incl. thermal and visual comfort, indoor air quality and moisture phenomena), HVAC and renewable system performance, urban level modeling, building automation, and operational optimization are important aspects of BPS.

Over the last six decades, numerous BPS computer programs have been developed. The most comprehensive listing of BPS software can be found in the BEST directory. Some of them only cover certain parts of BPS (e.g. climate analysis, thermal comfort, energy calculations, plant modeling, daylight simulation etc.). The core tools in the field of BPS are multi-domain, dynamic, whole-building simulation tools, which provide users with key indicators such as heating and cooling load, energy demand, temperature trends, humidity, thermal and visual comfort indicators, air pollutants, ecological impact and costs.

A typical building simulation model has inputs for local weather such as Typical Meteorological Year (TMY) file; building geometry; building envelope characteristics; internal heat gains from lighting, occupants and equipment loads; heating, ventilation, and cooling (HVAC) system specifications; operation schedules and control strategies. The ease of input and accessibility of output data varies widely between BPS tools. Advanced whole-building simulation tools are able to consider almost all of the following in some way with different approaches.

Necessary input data for a whole-building simulation:

- **Climate:** ambient air temperature, relative humidity, direct and diffuse solar radiation, wind speed and direction
- **Site:** location and orientation of the building, shading by topography and surrounding buildings, ground properties
- **Geometry:** building shape and zone geometry
- **Envelope:** materials and constructions, windows and shading, thermal bridges, infiltration and openings
- **Internal gains:** lights, equipment and occupants including schedules for operation/occupancy
- **Ventilation system:** transport and conditioning (heating, cooling, humidification) of air
- **Room units:** local units for heating, cooling and ventilation
- **Plant:** Central units for transformation, storage and delivery of energy to the building
- **Controls:** for window opening, shading devices, ventilation systems, room units, plant components

Some examples for key performance indicators:

- **Temperature trends:** in zones, on surfaces, in construction layers, for hot or cold water supply or in double glass facades
- **Comfort indicators:** like PMV and PPD, radiant temperature asymmetry, CO2-concentration, relative humidity
- **Heat balances:** for zones, the whole building or single plant components
- **Load profiles:** for heating and cooling demand, electricity profile for equipment and lighting
- **Energy demand:** for heating, cooling, ventilation, light, equipment, auxiliary systems (e.g. pumps, fans, elevators)
- **Daylight availability:** in certain zone areas, at different time points with variable outside conditions

Other use of BPS software

- **System sizing:** for HVAC components like air handling units, heat exchanger, boiler, chiller, water storage tanks, heat pumps and renewable energy systems.
- **Optimizing control strategies:** Controller setup for shading, window opening, heating, cooling and ventilation for increased operation performance.

## History

The history of BPS is approximately as long as that of computers. The very early developments in this direction started in the late 1950s and early 1960s in the United States and Sweden. During this period, several methods had been introduced for analyzing single system components (e.g. gas boiler) using steady state calculations. The very first reported simulation tool for buildings was **BRIS**, introduced in 1963 by the Royal Institute of Technology in Stockholm. Until the late 1960s, several models with hourly resolution had been developed focusing on energy assessments and heating/cooling load calculations. This effort resulted in more powerful simulation engines released in the early 1970s, among which were BLAST, DOE-2, ESP-r, HVACSIM+ and TRNSYS. In the United States, the 1970s energy crisis intensified these efforts, as reducing the energy consumption of buildings became an urgent domestic policy interest. The energy crisis also initiated development of U.S. building energy standards, beginning with ASHRAE 90-75.

The development of building simulation represents a combined effort between academia, governmental institutions, industry, and professional organizations. Over the past decades the building simulation discipline has matured into a field that offers unique expertise, methods and tools for building performance evaluation. Several review papers and state of the art analysis were carried out during that time giving an overview about the development.

In the 1980s, a discussion about future directions for BPS among a group of leading building simulation specialists started. There was a consensus that most of the tools, that had been developed until then, were too rigid in their structure to be able to accommodate the improvements and flexibility that would be called for in the future. Around this time, the very first equation-based building simulation environment **ENET** was developed, which provided the foundation of **SPARK**. In 1989, Sahlin and Sowell presented a **Neutral Model Format** (NMF) for building simulation models, which is used today in the commercial software IDA ICE. Four years later, Klein introduced the **Engineering Equation Solver** (EES) and in 1997, Mattsson and Elmqvist reported on an international effort to design **Modelica**.

BPS still presents challenges relating to problem representation, support for performance appraisal, enabling operational application, and delivering user education, training, and accreditation. Clarke (2015) describes a future vision of BPS with the following, most important tasks which should be addressed by the global BPS community.

- Better concept promotion
- Standardization of input data and accessibility of model libraries
- Standard performance assessment procedures
- Better embedding of BPS in practice
- Operational support and fault diagnosis with BPS
- Education, training, and user accreditation

## Accuracy

In the context of building simulation models, **error** refers to the discrepancy between simulation results and the actual measured performance of the building. There are normally occurring uncertainties in building design and building assessment, which generally stem from approximations in model inputs, such as occupancy behavior. **Calibration** refers to the process of "tuning" or adjusting assumed simulation model inputs to match observed data from the utilities or Building Management System (BMS).

The number of publications dealing with accuracy in building modeling and simulation increased significantly over the past decade. Many papers report large gaps between simulation results and measurements, while other studies show that they can match very well. The reliability of results from BPS depends on many different things, e.g. on the quality of input data, the competence of the simulation engineers and on the applied methods in the simulation engine. An overview about possible causes for the widely discussed performance gap from design stage to operation is given by de Wilde (2014) and a progress report by the Zero Carbon Hub (2013). Both conclude the factors mentioned above as the main uncertainties in BPS.

ASHRAE Standard 140-2017 "Standard Method of Test for the Evaluation of Building Energy Analysis Computer Programs (ANSI Approved)" provides a method to validate the technical capability and range of applicability of computer programs to calculate thermal performance. ASHRAE Guideline 4-2014 provides performance indices criteria for model calibration. The performance indices used are normalized mean bias error (NMBE), coefficient of variation (CV) of the root mean square error (RMSE), and R2 (coefficient of determination). ASHRAE recommends a R2 greater than 0.75 for calibrated models. The criteria for NMBE and CV RMSE depends on if measured data is available at a monthly or hourly timescale.

## Technological aspects

Given the complexity of building energy and mass flows, it is generally not possible to find an analytical solution, so the simulation software employs other techniques, such as response function methods, or numerical methods in finite differences or finite volume, as an approximation. Most of today's whole building simulation programs formulate models using imperative programming languages. These languages assign values to variables, declare the sequence of execution of these assignments and change the state of the program, as is done for example in C/C++, Fortran or MATLAB/Simulink. In such programs, model equations are tightly connected to the solution methods, often by making the solution procedure part of the actual model equations. The use of imperative programming languages limits the applicability and extensibility of models. More flexibility offer simulation engines using symbolic Differential Algebraic Equations (DAEs) with general purpose solvers that increase model reuse, transparency and accuracy. Since some of these engines have been developed for more than 20 years (e.g. IDA ICE) and due to the key advantages of equation-based modeling, these simulation engines can be considered as state of the art technology.

## Applications

Building simulation models may be developed for both new or existing buildings. Major use categories of building performance simulation include:

- **Architectural Design**: quantitatively compare design or retrofit options in order to inform a more energy-efficient building design
- **HVAC Design:** calculate thermal loads for sizing of mechanical equipment and help design and test system control strategies
- **Building Performance Rating:** demonstrate performance-based compliance with energy codes, green certification, and financial incentives
- **Building Stock Analysis:** support development of energy codes and standards and plan large scale energy efficiency programs
- **CFD in buildings:** simulation of boundary conditions like surface heat fluxes and surface temperatures for a following CFD study of the situation

## Software tools

There are hundreds of software tools available for simulating the performance of buildings and building subsystems, which range in capability from whole-building simulations to model input calibration to building auditing. Among whole-building simulation software tools, it is important to draw a distinction between the ***simulation engine***, which dynamically solves equations rooted in thermodynamics and building science, and the ***modeler application (interface)***.

In general, BPS software can be classified into

- Applications with integrated simulation engine (e.g. EnergyPlus, ESP-r, TAS, IES-VE, IDA ICE)
- Software that docks to a certain engine (e.g. Designbuilder, eQuest, RIUSKA, Sefaira)
- Plugins for other software enabling certain performance analysis (e.g. DIVA for Rhino, Honeybee, Autodesk Green Building Studio)

Contrary to this presentation, there are some tools that in fact do not meet these sharp classification criteria, such as ESP-r which can also be used as a modeler application for EnergyPlus and there are also other applications using the IDA simulation environment, which makes "IDA" the engine and "ICE" the modeler. Most modeler applications support the user with a graphical user interface to make data input easier. The modeler creates an input file for the simulation engine to solve. The engine returns output data to the modeler application or another visualization tool which in turn presents the results to the user. For some software packages, the calculation engine and the interface may be the same product. The table below gives an overview about commonly used simulation engines and modeler applications for BPS.

| Simulation engine | Developer | first Release | Technology | Modeling Language | License | latest Version | Modeler applications and GUI |
|---|---|---|---|---|---|---|---|
| ApacheSim | Integrated Environmental Solutions Ltd., UK |   |   |   | Commercial | 6.0 | VE 2018 |
| Carrier HAP | United Technologies, US |   |   |   | Commercial | 5.11 | Carrier HAP |
| COMFIE | Mines ParisTech, then IZUBA énergies, FR | 1994 |   |   | Commercial | 5.21.3.0 | Pleiades |
| DOE-2 | James J. Hirsch & Associates, US | 1978 |   |   | Freeware | 2.2 | eQuest, RIUSKA, EnergyPro, GBS |
| EnergyPlus | Lawrence Berkeley National Laboratory, US | 2001 |   |   | Freeware | 9.4.0 | DesignBuilder, OpenStudio, cove.tool, Many other |
| ESP-r | University of Strathclyde, UK | 1974 |   |   | Freeware | 11.11 | ESP-r |
| IDA | EQUA Simulation AB, SE | 1998 | DAE | NMF, Modelica | Commercial | 4.8 | ICE, ESBO |
| SPARK | Lawrence Berkeley National Laboratory, US | 1986 | DAE |   | Freeware | 2.01 | VisualSPARK |
| TAS | Environmental Design Solutions Limited, UK |   |   |   | Commercial | 9.5.0 | TAS 3D Modeler |
| TRNSYS | University of Wisconsin-Madison, US | 1975 |   | FORTRAN, C/C++ | Commercial | 18.0 | Simulation Studio, TRNBuild |

## BPS in practice

Since the 1990s, building performance simulation has undergone the transition from a method used mainly for research to a design tool for mainstream industrial projects. However, the use in different countries still varies greatly. Building certification programs like LEED (USA), BREEAM (UK) or DGNB (Germany) have shown to be a good driving force for BPS to find broader application. Also, national building standards that allow BPS based analysis are of good help for an increasing industrial adoption, such as in the United States (ASHRAE 90.1), Sweden (BBR), Switzerland (SIA) and the United Kingdom (NCM).

The Swedish building regulations are unique in that computed energy use has to be verified by measurements within the first two years of building operation. Since the introduction in 2007, experience shows that highly detailed simulation models are preferred by modelers to reliably achieve the required level of accuracy. Furthermore, this has fostered a simulation culture where the design predictions are close to the actual performance. This in turn has led to offers of formal energy guarantees based on simulated predictions, highlighting the general business potential of BPS.

## Performance-based compliance

In a performance-based approach, compliance with building codes or standards is based on the predicted energy use from a building simulation, rather than a prescriptive approach, which requires adherence to stipulated technologies or design features. Performance-based compliance provides greater flexibility in the building design as it allows designers to miss some prescriptive requirements if the impact on building performance can be offset by exceeding other prescriptive requirements. The certifying agency provides details on model inputs, software specifications, and performance requirements.

The following is a list of U.S. based energy codes and standards that reference building simulations to demonstrate compliance:

- ASHRAE 90.1
- International Energy Conservation Code (IECC)
- Leadership in Energy and Environmental Design (LEED)
- Green Globes
- California Title 24
- EnergyStar Multifamily High rise Program
- Passive House Institute US (PHIUS)
- Living Building Challenge

## Professional associations and certifications

**Professional associations**

- International Building Performance Simulation Association (IBPSA)
- American Society of Heating, Refrigerating, and Air-conditioning Engineers (ASHRAE)

**Certifications**

- BEMP - Building Energy Modeling Professional, administered by ASHRAE
- BESA - Certified Building Energy Simulation Analyst, administered by AEE
