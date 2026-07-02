---
title: "Structural health monitoring"
source: https://en.wikipedia.org/wiki/Structural_health_monitoring
domain: structural-health-monitoring
license: CC-BY-SA-4.0
tags: structural health monitoring, non-destructive testing, strain gauge, modal analysis
fetched: 2026-07-02
---

# Structural health monitoring

**Structural health monitoring** (**SHM**) involves the observation and analysis of a system over time using periodically sampled response measurements to monitor changes to the material and geometric properties of engineering structures such as bridges and buildings.

In an operational environment, structures degrade with age and use. Long term SHM outputs periodically updated information regarding the ability of the structure to continue performing its intended function. After extreme events, such as earthquakes or blast loading, SHM is used for rapid condition screening. SHM is intended to provide reliable information regarding the integrity of the structure in near real time.

The SHM process involves selecting the excitation methods, the sensor types, number and locations, and the data acquisition/storage/transmittal hardware commonly called health and usage monitoring systems. Measurements may be taken to either directly detect any degradation or damage that may occur to a system or indirectly by measuring the size and frequency of loads experienced to allow the state of the system to be predicted.

To directly monitor the state of a system it is necessary to identify features in the acquired data that allows one to distinguish between the undamaged and damaged structure. One of the most common feature extraction methods is based on correlating measured system response quantities, such a vibration amplitude or frequency, with observations of the degraded system. Damage accumulation testing, during which significant structural components of the system under study are degraded by subjecting them to realistic loading conditions, can also be used to identify appropriate features. This process may involve induced-damage testing, fatigue testing, corrosion growth, or temperature cycling to accumulate certain types of damage in an accelerated fashion.

## Introduction

Qualitative and non-continuous methods have long been used to evaluate structures for their capacity to serve their intended purpose. Since the beginning of the 19th century, railroad wheel-tappers have used the sound of a hammer striking the train wheel to evaluate if damage was present. In rotating machinery, vibration monitoring has been used for decades as a performance evaluation technique. Two techniques in the field of SHM are wave propagation based techniques and vibration based techniques. Broadly the literature for vibration based SHM can be divided into two aspects, the first wherein models are proposed for the damage to determine the dynamic characteristics, also known as the direct problem, and the second, wherein the dynamic characteristics are used to determine damage characteristics, also known as the inverse problem.

Several fundamental axioms, or general principles, have emerged:

- Axiom I: All materials have inherent flaws or defects;
- Axiom II: The assessment of damage requires a comparison between two system states;
- Axiom III: Identifying the existence and location of damage can be done in an unsupervised learning mode, but identifying the type of damage present and the damage severity can generally only be done in a supervised learning mode;
- Axiom IVa: Sensors cannot measure damage. Feature extraction through signal processing and statistical classification is necessary to convert sensor data into damage information;
- Axiom IVb: Without intelligent feature extraction, the more sensitive a measurement is to damage, the more sensitive it is to changing operational and environmental conditions;
- Axiom V: The length- and time-scales associated with damage initiation and evolution dictate the required properties of the SHM sensing system;
- Axiom VI: There is a trade-off between the sensitivity to damage of an algorithm and its noise rejection capability;
- Axiom VII: The size of damage that can be detected from changes in system dynamics is inversely proportional to the frequency range of excitation.

These Axioms were challenged in another paper: to give a concise set of three Axioms:

- Axiom AD1: A perfect material is a theoretical construct; real materials require significantly less energy to initiate damage than their ideal counterpart.
- Axiom AD2: The assessment of damage is dependent on the definition of system performance parameters. The clarity of this assessment depends on the precision of parameter definitions.
- Axiom AD3: The more sensitive a measurement is to damage, the more sensitive it is to changing operational and environmental conditions affecting the sensing parameter, and the more vulnerable it is to corruption by noise.

SHM System's elements typically include:

- Structure
- Sensors
- Data acquisition systems
- Data transfer and storage mechanism
- Data management
- Data interpretation and diagnosis:

1. System Identification
2. Structural model update
3. Structural condition assessment
4. Prediction of remaining service life

An example of this technology is embedding sensors in structures like bridges and aircraft. These sensors provide real time monitoring of various structural changes like stress and strain. In the case of civil engineering structures, the data provided by the sensors is usually transmitted to a remote data acquisition centres. With the aid of modern technology, real time control of structures (Active Structural Control) based on the information of sensors is possible

Commonly known as Structural Health Assessment (SHA) or SHM, this concept is widely applied to various forms of infrastructures, especially as countries all over the world enter into an even greater period of construction of various infrastructures ranging from bridges to skyscrapers. Especially so when damages to structures are concerned, it is important to note that there are stages of increasing difficulty that require the knowledge of previous stages, namely:

1. Detecting the existence of the damage on the structure
2. Locating the damage
3. Identifying the types of damage
4. Quantifying the severity of the damage

It is necessary to employ signal processing and statistical classification to convert sensor data on the infrastructural health status into damage info for assessment.

### Operational evaluation

Operational evaluation attempts to answer four questions regarding the implementation of a damage identification capability:

i) What are the life-safety and/or economic justification for performing the SHM?

ii) How is damage defined for the system being investigated and, for multiple damage possibilities, which cases are of the most concern?

iii) What are the conditions, both operational and environmental, under which the system to be monitored functions?

iv) What are the limitations on acquiring data in the operational environment?

Operational evaluation begins to set the limitations on what will be monitored and how the monitoring will be accomplished. This evaluation starts to tailor the damage identification process to features that are unique to the system being monitored and tries to take advantage of unique features of the damage that is to be detected.

### Data acquisition, normalization and cleansing

The data acquisition portion of the SHM process involves selecting the excitation methods, the sensor types, number and locations, and the data acquisition/storage/transmittal hardware. Again, this process will be application specific. Economic considerations will play a major role in making these decisions. The intervals at which data should be collected is another consideration that must be addressed.

Because data can be measured under varying conditions, the ability to normalize the data becomes very important to the damage identification process. As it applies to SHM, data normalization is the process of separating changes in sensor reading caused by damage from those caused by varying operational and environmental conditions. One of the most common procedures is to normalize the measured responses by the measured inputs. When environmental or operational variability is an issue, the need can arise to normalize the data in some temporal fashion to facilitate the comparison of data measured at similar times of an environmental or operational cycle. Sources of variability in the data acquisition process and with the system being monitored need to be identified and minimized to the extent possible. In general, not all sources of variability can be eliminated. Therefore, it is necessary to make the appropriate measurements such that these sources can be statistically quantified. Variability can arise from changing environmental and test conditions, changes in the data reduction process, and unit-to-unit inconsistencies.

Data cleansing is the process of selectively choosing data to pass on to or reject from the feature selection process. The data cleansing process is usually based on knowledge gained by individuals directly involved with the data acquisition. As an example, an inspection of the test setup may reveal that a sensor was loosely mounted and, hence, based on the judgment of the individuals performing the measurement, this set of data or the data from that particular sensor may be selectively deleted from the feature selection process. Signal processing techniques such as filtering and re-sampling can also be thought of as data cleansing procedures.

Finally, the data acquisition, normalization, and cleansing portion of SHM process should not be static. Insight gained from the feature selection process and the statistical model development process will provide information regarding changes that can improve the data acquisition process.

### Feature extraction and data compression

The area of the SHM process that receives the most attention in the technical literature is the identification of data features that allows one to distinguish between the undamaged and damaged structure. Inherent in this feature selection process is the condensation of the data. The best features for damage identification are, again, application specific.

One of the most common feature extraction methods is based on correlating measured system response quantities, such a vibration amplitude or frequency, with the first-hand observations of the degrading system. Another method of developing features for damage identification is to apply engineered flaws, similar to ones expected in actual operating conditions, to systems and develop an initial understanding of the parameters that are sensitive to the expected damage. The flawed system can also be used to validate that the diagnostic measurements are sensitive enough to distinguish between features identified from the undamaged and damaged system. The use of analytical tools such as experimentally-validated finite element models can be a great asset in this process. In multiple cases the analytical tools are used to perform numerical experiments where the flaws are introduced through computer simulation. Damage accumulation testing, during which significant structural components of the system under study are degraded by subjecting them to realistic loading conditions, can also be used to identify appropriate features. This process may involve induced-damage testing, fatigue testing, corrosion growth, or temperature cycling to accumulate certain types of damage in an accelerated fashion. Insight into the appropriate features can be gained from several types of analytical and experimental studies as described above and is usually the result of information obtained from some combination of these studies.

The operational implementation and diagnostic measurement technologies needed to perform SHM produce more data than traditional uses of structural dynamics information. A condensation of the data is advantageous and necessary when comparisons of multiple feature sets obtained over the lifetime of the structure are envisioned. Also, because data will be acquired from a structure over an extended period of time and in an operational environment, robust data reduction techniques must be developed to retain feature sensitivity to the structural changes of interest in the presence of environmental and operational variability. To further aid in the extraction and recording of quality data needed to perform SHM, the statistical significance of the features should be characterized and used in the condensation process.

### Statistical model development

The portion of the SHM process that has received the least attention in the technical literature is the development of statistical models for discrimination between features from the undamaged and damaged structures. Statistical model development is concerned with the implementation of the algorithms that operate on the extracted features to quantify the damage state of the structure. The algorithms used in statistical model development usually fall into three categories. When data are available from both the undamaged and damaged structure, the statistical pattern recognition algorithms fall into the general classification category, commonly referred to as supervised learning. Group classification and regression analysis are categories of supervised learning algorithms. Unsupervised learning refers to algorithms that are applied to data not containing examples from the damaged structure. Outlier or novelty detection is the primary class of algorithms applied in unsupervised learning applications. All of the algorithms analyze statistical distributions of the measured or derived features to enhance the damage identification process.

## Specific structures

### Bridges

Health monitoring of large bridges can be performed by simultaneous measurement of loads on the bridge and effects of these loads. It typically includes monitoring of:

- Wind and weather
- Traffic
- Prestressing and stay cables
- Deck
- Pylons
- Ground

Provided with this knowledge, the engineer can:

- Estimate the loads and their effects
- Estimate the state of fatigue or other limit state
- Forecast the probable evolution of the bridge's health

The state of Oregon in the United States, Department of Transportation Bridge Engineering Department has developed and implemented a Structural Health Monitoring (SHM) program as referenced in this technical paper by Steven Lovejoy, Senior Engineer.

References are available that provide an introduction to the application of fiber optic sensors to Structural Health Monitoring on bridges.

## Examples

The following projects are currently known as some of the biggest on-going bridge monitoring

- The California Department of Transportation is supporting development of the Bridge rapid assessment center for extreme events (BRACE2) to facilitate real-time structural health monitoring across the California highway network.
- Bridges in Hong Kong. The *Wind and Structural Health Monitoring System* is a sophisticated bridge monitoring system, costing US$1.3 million, used by the Hong Kong Highways Department to ensure road user comfort and safety of the Tsing Ma, Ting Kau, Kap Shui Mun and Stonecutters bridges. The sensory system consists of approximately 900 sensors and their relevant interfacing units. With more than 350 sensors on the Tsing Ma bridge, 350 on Ting Kau and 200 on Kap Shui Mun, the structural behaviour of the bridges is measured 24 hours a day, seven days a week. The sensors include accelerometers, strain gauges, displacement transducers, level sensing stations, anemometers, temperature sensors, dynamic weight-in-motion sensors and GPS receivers. They measure everything from tarmac temperature and strains in structural members to wind speed and the deflection and rotation of the kilometres of cables and any movement of the bridge decks and towers.
- The Rio–Antirrio bridge, Greece: has more than 100 sensors monitoring the structure and the traffic in real time.
- Millau Viaduc, France: has one of the largest systems with fiber optics in the world which is considered state of the art.
- The Huey P Long bridge, USA: has over 800 static and dynamic strain gauges designed to measure axial and bending load effects.
- The Fatih Sultan Mehmet Bridge, Turkey: also known as the Second Bosphorus Bridge. It has been monitored using an innovative wireless sensor network with normal traffic condition.
- Masjid al-Haram#Third Saudi expansion, Mecca, Saudi Arabia : has more than 600 sensors ( Concrete pressure cell, Embedment type strain gauge, Sister bar strain gauge, etc.) installed at foundation and concrete columns. This project is under construction.
- The Sydney Harbour Bridge in Australia is currently implementing a monitoring system involving over 2,400 sensors. Asset managers and bridge inspectors have mobile and web browser decision support tools based on analysis of sensor data.
- The Queensferry Crossing, currently under construction across the Firth of Forth, will have a monitoring system including more than 2,000 sensors upon its completion. Asset managers will have access to data for all sensors from a web-based data management interface, including automated data analysis.
- The Penang Second Bridge in Penang, Malaysia has completed the implementation and it's monitoring the bridge element with 3,000 sensors. For the safety of bridge users and as protection of such an investment, the firm responsible for the bridge wanted a structural health monitoring system. The system is used for disaster control, structural health management and data analysis. There were a number of considerations before implementation which included: force (wind, earthquake, temperature, vehicles); weather (air temperature, wind, humidity and precipitation); and response (strain, acceleration, cable tension, displacement and tilt).
- The Lakhta Center, Russia: has more than 3000 sensors and more than 8000 parameters monitoring the structure in real time.
