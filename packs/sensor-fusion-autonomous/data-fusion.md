---
title: "Data fusion"
source: https://en.wikipedia.org/wiki/Data_fusion
domain: sensor-fusion-autonomous
license: CC-BY-SA-4.0
tags: sensor fusion, extended kalman filter, particle filter, dead reckoning
fetched: 2026-07-02
---

# Data fusion

**Data fusion** is the process of integrating multiple data sources to produce more consistent, accurate, and useful information than that provided by any individual data source.

Data fusion processes are often categorized as low, intermediate, or high, depending on the processing stage at which fusion takes place. Low-level data fusion combines several sources of raw data to produce new raw data. The expectation is that fused data is more informative and synthetic than the original inputs.

For example, sensor fusion is also known as (multi-sensor) data fusion and is a subset of information fusion.

The concept of data fusion has origins in the evolved capacity of humans and animals to incorporate information from multiple senses to improve their ability to survive. For example, a combination of sight, touch, smell, and taste may indicate whether a substance is edible.

## The JDL/DFIG model

In the mid-1980s, the Joint Directors of Laboratories formed the Data Fusion Subpanel (which later became known as the Data Fusion Group). With the advent of the World Wide Web, data fusion thus included data, sensor, and information fusion. The JDL/DFIG introduced a model of data fusion that divided the various processes. Currently, the six levels with the Data Fusion Information Group (DFIG) model are:

- Level 0: *Source Preprocessing* (or *Data Assessment*)
- Level 1: *Object Assessment*
- Level 2: *Situation Assessment*
- Level 3: *Impact Assessment* (or *Threat Refinement*)
- Level 4: *Process Refinement* (or *Resource Management*)
- Level 5: *User Refinement* (or *Cognitive Refinement*)
- Level 6: *Mission Refinement* (or *Mission Management*)

Although the JDL Model (Level 1–4) is still in use today, it is often criticized for its implication that the levels necessarily happen in order and also for its lack of adequate representation of the potential for a human-in-the-loop. The DFIG model (Level 0–5) explored the implications of situation awareness, user refinement, and mission management. Despite these shortcomings, the JDL/DFIG models are useful for visualizing the data fusion process, facilitating discussion and common understanding, and important for systems-level information fusion design.

## Geospatial applications

In the geospatial (GIS) domain, data fusion is often synonymous with data integration. In these applications, there is often a need to combine diverse data sets into a unified (fused) data set which includes all of the data points and time steps from the input data sets. The fused data set is different from a simple combined superset in that the points in the fused data set contain attributes and metadata which might not have been included for these points in the original data set.

A simplified example of this process is shown below where data set "α" is fused with data set β to form the fused data set δ. Data points in set "α" have spatial coordinates X and Y and attributes A1 and A2. Data points in set β have spatial coordinates X and Y and attributes B1 and B2. The fused data set contains all points and attributes.

| Input Data Set α | Input Data Set β | Fused Data Set δ |
|---|---|---|
| Point X Y A1 A2 α1 10 10 M N α2 10 30 M N α3 30 10 M N α4 30 30 M N | Point X Y B1 B2 β1 20 20 Q R β2 20 40 Q R β3 40 20 Q R β4 40 40 Q R | Point X Y A1 A2 B1 B2 δ1 10 10 M N *Q?* *R?* δ2 10 30 M N *Q?* *R?* δ3 30 10 M N *Q?* *R?* δ4 30 30 M N *Q?* *R?* δ5 20 20 *M?* *N?* Q R δ6 20 40 *M?* *N?* Q R δ7 40 20 *M?* *N?* Q R δ8 40 40 *M?* *N?* Q R |

In a simple case where all attributes are uniform across the entire analysis domain, the attributes may be simply assigned: *M?, N?, Q?, R?* to M, N, Q, R. In a real application, attributes are not uniform and some type of interpolation is usually required to properly assign attributes to the data points in the fused set.

In a much more complicated application, marine animal researchers use data fusion to combine animal tracking data with bathymetric, meteorological, sea surface temperature (SST) and animal habitat data to examine and understand habitat utilization and animal behavior in reaction to external forces such as weather or water temperature. Each of these data sets exhibit a different spatial grid and sampling rate so a simple combination would likely create erroneous assumptions and taint the results of the analysis. But through the use of data fusion, all data and attributes are brought together into a single view in which a more complete picture of the environment is created. This enables scientists to identify key locations and times and form new insights into the interactions between the environment and animal behaviors.

In the figure at right, rock lobsters are studied off the coast of Tasmania. Hugh Pederson of the University of Tasmania used data fusion software to fuse southern rock lobster tracking data (color-coded for in yellow and black for day and night, respectively) with bathymetry and habitat data to create a unique 4D picture of rock lobster behavior.

## Data integration

In applications outside of the geospatial domain, differences in the usage of the terms Data integration and Data fusion apply. In areas such as business intelligence, for example, data integration is used to describe the combining of data, whereas data fusion is integration followed by reduction or replacement. Data integration might be viewed as set combination wherein the larger set is retained, whereas fusion is a set reduction technique with improved confidence.

### Application areas

- Bioinformatics
- Biometrics
- Business intelligence
- Business performance management
- Cheminformatics
  - Quantitative structure-activity relationship
- Discovery science
- Geospatial information systems
- Intelligence services
- Intelligent transport systems
- Loyalty card
- Oceanography
- Soil mapping
- Wireless sensor networks

## From multiple traffic sensing modalities

The data from the different sensing technologies can be combined in intelligent ways to determine the traffic state accurately. A Data fusion based approach that utilizes the road side collected acoustic, image and sensor data has been shown to combine the advantages of the different individual methods.

## Decision fusion

In many cases, geographically dispersed sensors are severely energy- and bandwidth-limited. Therefore, the raw data concerning a certain phenomenon are often summarized in a few bits from each sensor. When inferring on a binary event (i.e., ${\mathcal {H}}_{0}$ or ${\mathcal {H}}_{1}$ ), in the extreme case only binary decisions are sent from sensors to a Decision Fusion Center (DFC) and combined in order to obtain improved classification performance.

## For enhanced contextual awareness

With a multitude of built-in sensors including motion sensor, environmental sensor, position sensor, a modern mobile device typically gives mobile applications access to a number of sensory data which could be leveraged to enhance the contextual awareness. Using signal processing and data fusion techniques such as feature generation, feasibility study and principal component analysis (PCA) such sensory data will greatly improve the positive rate of classifying the motion and contextual relevant status of the device. Many context-enhanced information techniques are provided by Snidaro, et al.

## Statistical methods

### Bayesian auto-regressive Gaussian processes

Gaussian processes are a popular machine learning model. If an auto-regressive relationship between the data is assumed, and each data source is assumed to be a Gaussian process, this constitutes a non-linear Bayesian regression problem.

### Semiparametric estimation

Many data fusion methods assume common conditional distributions across several data sources. Recently, methods have been developed to enable efficient estimation within the resulting semiparametric model.
