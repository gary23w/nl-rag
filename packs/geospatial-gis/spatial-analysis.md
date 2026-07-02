---
title: "Spatial analysis"
source: https://en.wikipedia.org/wiki/Spatial_analysis
domain: geospatial-gis
license: CC-BY-SA-4.0
tags: geospatial gis, spatial analysis, geographic information, digital cartography
fetched: 2026-07-02
---

# Spatial analysis

**Spatial analysis** is any of the formal techniques which study entities using their topological, geometric, or geographic properties, primarily used in urban design. Spatial analysis includes a variety of techniques using different analytic approaches, especially spatial statistics. It may be applied in fields as diverse as astronomy, with its studies of the placement of galaxies in the cosmos, or to chip fabrication engineering, with its use of "place and route" algorithms to build complex wiring structures. In a more restricted sense, spatial analysis is **geospatial analysis**, the technique applied to structures at the human scale, most notably in the analysis of geographic data. It may also applied to genomics, as in transcriptomics data, but is primarily for spatial data.

Complex issues arise in spatial analysis, many of which are neither clearly defined nor completely resolved, but form the basis for current research. The most fundamental of these is the problem of defining the spatial location of the entities being studied. Classification of the techniques of spatial analysis is difficult because of the large number of different fields of research involved, the different fundamental approaches which can be chosen, and the many forms the data can take.

## History

Spatial analysis began with early attempts at cartography and surveying. Land surveying goes back to at least 1,400 B.C in Egypt: the dimensions of taxable land plots were measured with measuring ropes and plumb bobs. Many fields have contributed to its rise in modern form. Biology contributed through botanical studies of global plant distributions and local plant locations, ethological studies of animal movement, landscape ecological studies of vegetation blocks, ecological studies of spatial population dynamics, and the study of biogeography. Epidemiology contributed with early work on disease mapping, notably John Snow's work of mapping an outbreak of cholera, with research on mapping the spread of disease and with location studies for health care delivery. Statistics has contributed greatly through work in spatial statistics. Economics has contributed notably through spatial econometrics. Geographic information system is currently a major contributor due to the importance of geographic software in the modern analytic toolbox. Remote sensing has contributed extensively in morphometric and clustering analysis. Computer science has contributed extensively through the study of algorithms, notably in computational geometry. Mathematics continues to provide the fundamental tools for analysis and to reveal the complexity of the spatial realm, for example, with recent work on fractals and scale invariance. Scientific modelling provides a useful framework for new approaches.

## Fundamental issues

Spatial analysis confronts many fundamental issues in the definition of its objects of study, in the construction of the analytic operations to be used, in the use of computers for analysis, in the limitations and particularities of the analyses which are known, and in the presentation of analytic results. Many of these issues are active subjects of modern research.

Common errors often arise in spatial analysis, some due to the mathematics of space, some due to the particular ways data are presented spatially, some due to the tools which are available. Census data, because it protects individual privacy by aggregating data into local units, raises a number of statistical issues. The fractal nature of coastline makes precise measurements of its length difficult if not impossible. A computer software fitting straight lines to the curve of a coastline, can easily calculate the lengths of the lines which it defines. However these straight lines may have no inherent meaning in the real world, as was shown for the coastline of Britain.

These problems represent a challenge in spatial analysis because of the power of maps as media of presentation. When results are presented as maps, the presentation combines spatial data which are generally accurate with analytic results which may be inaccurate, leading to an impression that analytic results are more accurate than the data would indicate.

### Formal Problems

#### Boundary problem

A boundary problem in analysis is a phenomenon in which geographical patterns are differentiated by the shape and arrangement of boundaries that are drawn for administrative or measurement purposes. The boundary problem occurs because of the loss of neighbors in analyses that depend on the values of the neighbors. While geographic phenomena are measured and analyzed within a specific unit, identical spatial data can appear either dispersed or clustered depending on the boundary placed around the data. In analysis with point data, dispersion is evaluated as dependent of the boundary. In analysis with areal data, statistics should be interpreted based upon the boundary.

#### Modifiable areal unit problem

The modifiable areal unit problem (MAUP) is a source of statistical bias that can significantly impact the results of statistical hypothesis tests. The MAUP affects results when point-based measures of spatial phenomena are aggregated into spatial partitions or *areal units* (such as regions or districts) as in, for example, population density or illness rates. The resulting summary values (e.g., totals, rates, proportions, densities) are influenced by both the shape and scale of the aggregation unit.

For example, census data may be aggregated into county districts, census tracts, postcode areas, police precincts, or any other arbitrary spatial partition. Thus, the results of data aggregation are dependent on the mapmaker's choice of which "modifiable areal unit" to use in their analysis. A census choropleth map calculating population density using state boundaries will yield radically different results from a map that calculates density based on county boundaries. Furthermore, census district boundaries are also subject to change over time, meaning the MAUP must be considered when comparing past to current data.

#### Modifiable temporal unit problem

The Modified Temporal Unit Problem (MTUP) is a source of statistical bias that occurs in time series and spatial analysis when using temporal data that has been aggregated into temporal units. In such cases, choosing a temporal unit (e.g., days, months, years) can affect the analysis results and lead to inconsistencies or errors in statistical hypothesis testing.

#### Neighborhood effect averaging problem

The neighborhood effect averaging problem (NEAP) is a source of statistical bias that can significantly impact the results of statistical hypothesis tests. It is caused by the influence of aggregating neighborhood-level phenomena on individuals when mobility-dependent exposures influence the phenomena. The problem confounds the neighbourhood effect, which suggests that a person's neighborhood impacts their individual characteristics, such as health. It relates to the boundary problem, in that delineated neighborhoods used for analysis may not fully account for an individual's activity space if the borders are permeable, and individual mobility crosses the boundaries. The term was first coined by Mei-Po Kwan in 2018.

#### Travelling salesman problem

In the theory of computational complexity, the travelling salesman problem (TSP) asks the following question: "Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city exactly once and returns to the origin city?" It is an NP-hard problem in combinatorial optimization, important in theoretical computer science and operations research.

The travelling purchaser problem, the vehicle routing problem and the ring star problem are three generalizations of TSP.

The decision version of the TSP (where given a length *L*, the task is to decide whether the graph has a tour whose length is at most *L*) belongs to the class of NP-complete problems. Thus, it is possible that the worst-case running time for any algorithm for the TSP increases superpolynomially (but no more than exponentially) with the number of cities.

The problem was first formulated in 1930 and is one of the most intensively studied problems in optimization. It is used as a benchmark for many optimization methods. Even though the problem is computationally difficult, many heuristics and exact algorithms are known, so that some instances with tens of thousands of cities can be solved completely, and even problems with millions of cities can be approximated within a small fraction of 1%.

#### Uncertain geographic context problem

In geography, public health, and other fields that study spatial relationships, the uncertain geographic context problem (UGCoP) is a methodological problem in which the geographic areas used in research to represent people's environments—such as neighborhoods, census tracts, administrative areas, or activity spaces—may differ from the places and periods that actually shape the phenomena being studied, potentially leading to misleading conclusions.

For example, a study that measures the effect of a person's residential neighborhood on health outcomes may overlook environmental influences encountered while working, traveling, or engaging in activities elsewhere. The term was coined by geographer Mei-Po Kwan in 2012.

#### Weber problem

In geometry, the Weber problem, named after Alfred Weber, is one of the most famous problems in location theory. It requires finding a point in the plane that minimizes the sum of the transportation costs from this point to n destination points, where different destination points are associated with different costs per unit distance.

The Weber problem generalizes the geometric median, which assumes transportation costs per unit distance are the same for all destination points, and the problem of computing the Fermat point, the geometric median of three points. For this reason it is sometimes called the Fermat–Weber problem, although the same name has also been used for the unweighted geometric median problem. The Weber problem is in turn generalized by the attraction–repulsion problem, which allows some of the costs to be negative, so that greater distance from some points is better.

### Spatial characterization

The definition of the spatial presence of an entity constrains the possible analysis which can be applied to that entity and influences the final conclusions that can be reached. While this property is fundamentally true of all analysis, it is particularly important in spatial analysis because the tools to define and study entities favor specific characterizations of the entities being studied. Statistical techniques favor the spatial definition of objects as points because there are very few statistical techniques which operate directly on line, area, or volume elements. Computer tools favor the spatial definition of objects as homogeneous and separate elements because of the limited number of database elements and computational structures available, and the ease with which these primitive structures can be created.

### Spatial dependence

**Spatial dependence** is the spatial relationship of variable values (for themes defined over space, such as rainfall) or locations (for themes defined as objects, such as cities). Spatial dependence is measured as the existence of statistical dependence in a collection of random variables, each of which is associated with a different geographical location. Spatial dependence is of importance in applications where it is reasonable to postulate the existence of corresponding set of random variables at locations that have not been included in a sample. Thus rainfall may be measured at a set of rain gauge locations, and such measurements can be considered as outcomes of random variables, but rainfall clearly occurs at other locations and would again be random. Because rainfall exhibits properties of autocorrelation, spatial interpolation techniques can be used to estimate rainfall amounts at locations near measured locations.

As with other types of statistical dependence, the presence of spatial dependence generally leads to estimates of an average value from a sample being less accurate than had the samples been independent, although if negative dependence exists a sample average can be better than in the independent case. A different problem than that of estimating an overall average is that of spatial interpolation: here the problem is to estimate the unobserved random outcomes of variables at locations intermediate to places where measurements are made, on that there is spatial dependence between the observed and unobserved random variables.

Tools for exploring spatial dependence include: spatial correlation, spatial covariance functions and semivariograms. Methods for spatial interpolation include Kriging, which is a type of best linear unbiased prediction. The topic of spatial dependence is of importance to geostatistics and spatial analysis.

#### Spatial auto-correlation

Spatial dependency is the co-variation of properties within geographic space: characteristics at proximal locations appear to be correlated, either positively or negatively. Spatial dependency leads to the **spatial autocorrelation** problem in statistics since, like temporal autocorrelation, this violates standard statistical techniques that assume independence among observations. For example, regression analyses that do not compensate for spatial dependency can have unstable parameter estimates and yield unreliable significance tests. Spatial regression models (see below) capture these relationships and do not suffer from these weaknesses. It is also appropriate to view spatial dependency as a source of information rather than something to be corrected.

Locational effects also manifest as spatial heterogeneity, or the apparent variation in a process with respect to location in geographic space. Unless a space is uniform and boundless, every location will have some degree of uniqueness relative to the other locations. This affects the spatial dependency relations and therefore the spatial process. Spatial heterogeneity means that overall parameters estimated for the entire system may not adequately describe the process at any given location.

### Spatial association

**Spatial association** is the degree to which things are similarly arranged in space. Analysis of the distribution patterns of two phenomena is done by map overlay. If the distributions are similar, then the spatial association is strong, and vice versa. In a Geographic Information System, the analysis can be done quantitatively. For example, a set of observations (as points or extracted from raster cells) at matching locations can be intersected and examined by regression analysis.

Like spatial autocorrelation, this can be a useful tool for spatial prediction. In spatial modeling, the concept of spatial association allows the use of covariates in a regression equation to predict the geographic field and thus produce a map.

#### The second dimension of spatial association

The second dimension of spatial association (SDA) reveals the association between spatial variables through extracting geographical information at locations outside samples. SDA effectively uses the missing geographical information outside sample locations in methods of the first dimension of spatial association (FDA), which explore spatial association using observations at sample locations. In the field of public health surveillance, spatial analysis techniques have investigated topics such as the correlation between literacy rates and health insurance enrollment gaps.

### Scaling

Spatial measurement scale is a persistent issue in spatial analysis; more detail is available at the modifiable areal unit problem (MAUP) topic entry. Landscape ecologists developed a series of scale invariant metrics for aspects of ecology that are fractal in nature. In more general terms, no scale independent method of analysis is widely agreed upon for spatial statistics.

### Sampling

Spatial sampling involves determining a limited number of locations in geographic space for faithfully measuring phenomena that are subject to dependency and heterogeneity. Dependency suggests that since one location can predict the value of another location, we do not need observations in both places. But heterogeneity suggests that this relation can change across space, and therefore we cannot trust an observed degree of dependency beyond a region that may be small. Basic spatial sampling schemes include random, clustered and systematic. These basic schemes can be applied at multiple levels in a designated spatial hierarchy (e.g., urban area, city, neighborhood). It is also possible to exploit ancillary data, for example, using property values as a guide in a spatial sampling scheme to measure educational attainment and income. Spatial models such as autocorrelation statistics, regression and interpolation (see below) can also dictate sample design.

### Common errors in spatial analysis

The fundamental issues in spatial analysis lead to numerous problems in analysis including bias, distortion and outright errors in the conclusions reached. These issues are often interlinked but various attempts have been made to separate out particular issues from each other.

#### Length

In discussing the coastline of Britain, Benoit Mandelbrot showed that certain spatial concepts are inherently nonsensical despite presumption of their validity. Lengths in ecology depend directly on the scale at which they are measured and experienced. So while surveyors commonly measure the length of a river, this length only has meaning in the context of the relevance of the measuring technique to the question under study.

- (Britain measured using a 200 km linear measurement)Britain measured using a 200 km linear measurement
- (Britain measured using a 100 km linear measurement)Britain measured using a 100 km linear measurement
- (Britain measured using a 50 km linear measurement)Britain measured using a 50 km linear measurement

#### Locational fallacy

The locational fallacy refers to error due to the particular spatial characterization chosen for the elements of study, in particular choice of placement for the spatial presence of the element.

Spatial characterizations may be simplistic or even wrong. Studies of humans often reduce the spatial existence of humans to a single point, for instance their home address. This can easily lead to poor analysis, for example, when considering disease transmission which can happen at work or at school and therefore far from the home.

The spatial characterization may implicitly limit the subject of study. For example, the spatial analysis of crime data has recently become popular but these studies can only describe the particular kinds of crime which can be described spatially. This leads to many maps of assault but not to any maps of embezzlement with political consequences in the conceptualization of crime and the design of policies to address the issue.

#### Atomic fallacy

This describes errors due to treating elements as separate 'atoms' outside of their spatial context. The fallacy is about transferring individual conclusions to spatial units.

#### Ecological fallacy

The ecological fallacy describes errors due to performing analyses on aggregate data when trying to reach conclusions on the individual units. Errors occur in part from spatial aggregation. For example, a pixel represents the average surface temperatures within an area. Ecological fallacy would be to assume that all points within the area have the same temperature.

### Solutions to the fundamental issues

#### Geographic space

A mathematical space exists whenever we have a set of observations and quantitative measures of their attributes. For example, we can represent individuals' incomes or years of education within a coordinate system where the location of each individual can be specified with respect to both dimensions. The distance between individuals within this space is a quantitative measure of their differences with respect to income and education. However, in spatial analysis, we are concerned with specific types of mathematical spaces, namely, geographic space. In geographic space, the observations correspond to locations in a spatial measurement framework that capture their proximity in the real world. The locations in a spatial measurement framework often represent locations on the surface of the Earth, but this is not strictly necessary. A spatial measurement framework can also capture proximity with respect to, say, interstellar space or within a biological entity such as a liver. The fundamental tenet is Tobler's First Law of Geography: if the interrelation between entities increases with proximity in the real world, then representation in geographic space and assessment using spatial analysis techniques are appropriate.

The Euclidean distance between locations often represents their proximity, although this is only one possibility. There are an infinite number of distances in addition to Euclidean that can support quantitative analysis. For example, "Manhattan" (or "Taxicab") distances where movement is restricted to paths parallel to the axes can be more meaningful than Euclidean distances in urban settings. In addition to distances, other geographic relationships such as connectivity**(e.g., the existence or degree of shared borders) and direction** can also influence the relationships among entities. It is also possible to compute minimal cost paths across a cost surface; for example, this can represent proximity among locations when travel must occur across rugged terrain.

## Types

> Spatial data comes in many varieties and it is not easy to arrive at a system of classification that is simultaneously exclusive, exhaustive, imaginative, and satisfying. -- G. Upton & B. Fingelton

### Spatial data analysis

Urban and Regional Studies deal with large tables of spatial data obtained from censuses and surveys. It is necessary to simplify the huge amount of detailed information in order to extract the main trends. Multivariable analysis (or Factor analysis, FA) allows a change of variables, transforming the many variables of the census, usually correlated between themselves, into fewer independent "Factors" or "Principal Components" which are, actually, the eigenvectors of the data correlation matrix weighted by the inverse of their eigenvalues. This change of variables has two main advantages:

1. Since information is concentrated on the first new factors, it is possible to keep only a few of them while losing only a small amount of information; mapping them produces fewer and more significant maps
2. The factors, actually the eigenvectors, are orthogonal by construction, i.e. not correlated. In most cases, the dominant factor (with the largest eigenvalue) is the Social Component, separating rich and poor in the city. Since factors are not-correlated, other smaller processes than social status, which would have remained hidden otherwise, appear on the second, third, ... factors.

Factor analysis depends on measuring distances between observations : the choice of a significant metric is crucial. The Euclidean metric (Principal Component Analysis), the Chi-Square distance (Correspondence Analysis) or the Generalized Mahalanobis distance (Discriminant Analysis) are among the more widely used. More complicated models, using communalities or rotations have been proposed.

Using multivariate methods in spatial analysis began really in the 1950s (although some examples go back to the beginning of the century) and culminated in the 1970s, with the increasing power and accessibility of computers. Already in 1948, in a seminal publication, two sociologists, Wendell Bell and Eshref Shevky, had shown that most city populations in the US and in the world could be represented with three independent factors : 1- the « socio-economic status » opposing rich and poor districts and distributed in sectors running along highways from the city center, 2- the « life cycle », i.e. the age structure of households, distributed in concentric circles, and 3- « race and ethnicity », identifying patches of migrants located within the city. In 1961, in a groundbreaking study, British geographers used FA to classify British towns. Brian J Berry, at the University of Chicago, and his students made a wide use of the method, applying it to most important cities in the world and exhibiting common social structures. The use of Factor Analysis in Geography, made so easy by modern computers, has been very wide but not always very wise.

Since the vectors extracted are determined by the data matrix, it is not possible to compare factors obtained from different censuses. A solution consists in fusing together several census matrices in a unique table which, then, may be analyzed. This, however, assumes that the definition of the variables has not changed over time and produces very large tables, difficult to manage. A better solution, proposed by psychometricians, groups the data in a « cubic matrix », with three entries (for instance, locations, variables, time periods). A Three-Way Factor Analysis produces then three groups of factors related by a small cubic « core matrix ». This method, which exhibits data evolution over time, has not been widely used in geography. In Los Angeles, however, it has exhibited the role, traditionally ignored, of Downtown as an organizing center for the whole city during several decades.

### Spatial autocorrelation

Spatial autocorrelation statistics measure and analyze the degree of dependency among observations in a geographic space. Classic spatial autocorrelation statistics include Moran's I , Geary's C , Getis's G and the standard deviational ellipse. These statistics require measuring a spatial weights matrix that reflects the intensity of the geographic relationship between observations in a neighborhood, e.g., the distances between neighbors, the lengths of shared border, or whether they fall into a specified directional class such as "west". Classic spatial autocorrelation statistics compare the spatial weights to the covariance relationship at pairs of locations. Spatial autocorrelation that is more positive than expected from random indicate the clustering of similar values across geographic space, while significant negative spatial autocorrelation indicates that neighboring values are more dissimilar than expected by chance, suggesting a spatial pattern similar to a chess board.

Spatial autocorrelation statistics such as Moran's I and Geary's C are global in the sense that they estimate the overall degree of spatial autocorrelation for a dataset. The possibility of spatial heterogeneity suggests that the estimated degree of autocorrelation may vary significantly across geographic space. **Local spatial autocorrelation statistics** provide estimates disaggregated to the level of the spatial analysis units, allowing assessment of the dependency relationships across space. G statistics compare neighborhoods to a global average and identify local regions of strong autocorrelation. Local versions of the I and C statistics are also available.

### Spatial heterogeneity

Spatial heterogeneity is a property generally ascribed to a landscape or to a population. It refers to the uneven distribution of various concentrations of each species within an area. A landscape with spatial heterogeneity has a mix of concentrations of multiple species of plants or animals (biological), or of terrain formations (geological), or environmental characteristics (e.g. rainfall, temperature, wind) filling its area. A population showing spatial heterogeneity is one where various concentrations of individuals of this species are unevenly distributed across an area; nearly synonymous with "patchily distributed."

### Spatial interaction

Spatial interaction or "gravity models" estimate the flow of people, material or information between locations in geographic space. Factors can include origin propulsive variables such as the number of commuters in residential areas, destination attractiveness variables such as the amount of office space in employment areas, and proximity relationships between the locations measured in terms such as driving distance or travel time. In addition, the topological, or connective, relationships between areas must be identified, particularly considering the often conflicting relationship between distance and topology; for example, two spatially close neighborhoods may not display any significant interaction if they are separated by a highway. After specifying the functional forms of these relationships, the analyst can estimate model parameters using observed flow data and standard estimation techniques such as ordinary least squares or maximum likelihood. Competing destinations versions of spatial interaction models include the proximity among the destinations (or origins) in addition to the origin-destination proximity; this captures the effects of destination (origin) clustering on flows.

### Spatial interpolation

Spatial interpolation methods estimate the variables at unobserved locations in geographic space based on the values at observed locations. Basic methods include inverse distance weighting: this attenuates the variable with decreasing proximity from the observed location. Kriging is a more sophisticated method that interpolates across space according to a spatial lag relationship that has both systematic and random components. This can accommodate a wide range of spatial relationships for the hidden values between observed locations. Kriging provides optimal estimates given the hypothesized lag relationship, and error estimates can be mapped to determine if spatial patterns exist.

### Spatial regression

Spatial regression methods capture spatial dependency in regression analysis, avoiding statistical problems such as unstable parameters and unreliable significance tests, as well as providing information on spatial relationships among the variables involved. Depending on the specific technique, spatial dependency can enter the regression model as relationships between the independent variables and the dependent, between the dependent variables and a spatial lag of itself, or in the error terms. **Geographically weighted regression** (GWR) is a local version of spatial regression that generates parameters disaggregated by the spatial units of analysis. This allows assessment of the spatial heterogeneity in the estimated relationships between the independent and dependent variables. The use of Bayesian hierarchical modeling in conjunction with Markov chain Monte Carlo (MCMC) methods have recently shown to be effective in modeling complex relationships using Poisson-Gamma-CAR, Poisson-lognormal-SAR, or Overdispersed logit models. Statistical packages for implementing such Bayesian models using MCMC include WinBugs, CrimeStat and many packages available via R programming language.

Spatial stochastic processes, such as Gaussian processes are also increasingly being deployed in spatial regression analysis. Model-based versions of GWR, known as spatially varying coefficient models have been applied to conduct Bayesian inference. Spatial stochastic processes can become computationally effective using scalable Gaussian process models, such as Gaussian Predictive Processes and Nearest Neighbor Gaussian Processes (NNGP).

### Spatial neural networks

Spatial neural networks (SNNs) constitute a supercategory of tailored

neural networks (NNs)

for representing and predicting geographic phenomena. They generally improve both the statistical

accuracy

and

reliability

of the a-spatial/classic NNs whenever they handle

geo-spatial datasets

, and also of the other spatial

(statistical) models

(e.g. spatial regression models) whenever the geo-spatial

datasets

' variables depict

non-linear relations

.

Examples of SNNs are the OSFA spatial neural networks, SVANNs and GWNNs.

### Spatial volatility

Spatial volatility models describe spatial or spatiotemporal dependence in the conditional variance of a process, extending the concept of Autoregressive conditional heteroskedasticity (ARCH) from time series to spatial settings. Such models account for the fact that variability at one location may be related to variability at neighbouring locations, as defined by a spatial weights matrix. This is in keeping with one formulation of Arbia's law of geography which states that "everything is related to everything else, but things observed at a coarse spatial resolution are more related than things observed at a finer resolution."

A generalised spatial and spatiotemporal ARCH/GARCH framework was introduced by Otto, Schmid, and Garthoff (2018), allowing the conditional variance at a location to depend on weighted past squared residuals from neighbouring locations and, in the spatiotemporal case, on its own past conditional variances. Sato and Matsuda (2017) proposed a spatial log-ARCH model as an alternative formulation.

Spatial volatility models find applications in disciplines where risk or uncertainty propagate over space, including regional economics, environmental risk assessment, and financial networks. A recent review summarises methodological developments, estimation strategies, and applications of spatial and spatiotemporal volatility models across disciplines.

### Simulation and modeling

Spatial interaction models are aggregate and top-down: they specify an overall governing relationship for flow between locations. This characteristic is also shared by urban models such as those based on mathematical programming, flows among economic sectors, or bid-rent theory. An alternative modeling perspective is to represent the system at the highest possible level of disaggregation and study the bottom-up emergence of complex patterns and relationships from behavior and interactions at the individual level.

Complex adaptive systems theory as applied to spatial analysis suggests that simple interactions among proximal entities can lead to intricate, persistent and functional spatial entities at aggregate levels. Two fundamentally spatial simulation methods are cellular automata and agent-based modeling. Cellular automata modeling imposes a fixed spatial framework such as grid cells and specifies rules that dictate the state of a cell based on the states of its neighboring cells. As time progresses, spatial patterns emerge as cells change states based on their neighbors; this alters the conditions for future time periods. For example, cells can represent locations in an urban area and their states can be different types of land use. Patterns that can emerge from the simple interactions of local land uses include office districts and urban sprawl. Agent-based modeling uses software entities (agents) that have purposeful behavior (goals) and can react, interact and modify their environment while seeking their objectives. Unlike the cells in cellular automata, simulysts can allow agents to be mobile with respect to space. For example, one could model traffic flow and dynamics using agents representing individual vehicles that try to minimize travel time between specified origins and destinations. While pursuing minimal travel times, the agents must avoid collisions with other vehicles also seeking to minimize their travel times. Cellular automata and agent-based modeling are complementary modeling strategies. They can be integrated into a common geographic automata system where some agents are fixed while others are mobile.

Calibration plays a pivotal role in both CA and ABM simulation and modelling approaches. Initial approaches to CA proposed robust calibration approaches based on stochastic, Monte Carlo methods. ABM approaches rely on agents' decision rules (in many cases extracted from qualitative research base methods such as questionnaires). Recent Machine Learning Algorithms calibrate using training sets, for instance in order to understand the qualities of the built environment.

### Multiple-point geostatistics (MPS)

Spatial analysis of a conceptual geological model is the main purpose of any MPS algorithm. The method analyzes the spatial statistics of the geological model, called the training image, and generates realizations of the phenomena that honor those input multiple-point statistics.

A recent MPS algorithm used to accomplish this task is the pattern-based method by Honarkhah. In this method, a distance-based approach is employed to analyze the patterns in the training image. This allows the reproduction of the multiple-point statistics, and the complex geometrical features of the training image. Each output of the MPS algorithm is a realization that represents a random field. Together, several realizations may be used to quantify spatial uncertainty.

One of the recent methods is presented by Tahmasebi et al. uses a cross-correlation function to improve the spatial pattern reproduction. They call their MPS simulation method as the CCSIM algorithm. This method is able to quantify the spatial connectivity, variability and uncertainty. Furthermore, the method is not sensitive to any type of data and is able to simulate both categorical and continuous scenarios. CCSIM algorithm is able to be used for any stationary, non-stationary and multivariate systems and it can provide high quality visual appeal model.,

## Geospatial and hydrospatial analysis

**Geospatial and hydrospatial analysis**, or just **spatial analysis**, is an approach to applying statistical analysis and other analytic techniques to data which has a geographical or spatial aspect. Such analysis would typically employ software capable of rendering maps processing spatial data, and applying analytical methods to terrestrial or geographic datasets, including the use of geographic information systems and geomatics.

### Geographical information system usage

Geographic information systems (GIS) — a large domain that provides a variety of capabilities designed to capture, store, manipulate, analyze, manage, and present all types of geographical data — utilizes geospatial and hydrospatial analysis in a variety of contexts, operations and applications.

#### Basic applications

Geospatial and Hydrospatial analysis, using GIS, was developed for problems in the environmental and life sciences, in particular ecology, geology and epidemiology. It has extended to almost all industries including defense, intelligence, utilities, Natural Resources (i.e. Oil and Gas, Forestry ... etc.), social sciences, medicine and Public Safety (i.e. emergency management and criminology), disaster risk reduction and management (DRRM), and climate change adaptation (CCA). Spatial statistics typically result primarily from observation rather than experimentation. Hydrospatial is particularly used for the aquatic side and the members related to the water surface, column, bottom, sub-bottom and the coastal zones.

#### Basic operations

Vector-based GIS is typically related to operations such as map overlay (combining two or more maps or map layers according to predefined rules), simple buffering (identifying regions of a map within a specified distance of one or more features, such as towns, roads or rivers) and similar basic operations. This reflects (and is reflected in) the use of the term spatial analysis within the Open Geospatial Consortium (OGC) "simple feature specifications". For raster-based GIS, widely used in the environmental sciences and remote sensing, this typically means a range of actions applied to the grid cells of one or more maps (or images) often involving filtering and/or algebraic operations (map algebra). These techniques involve processing one or more raster layers according to simple rules resulting in a new map layer, for example replacing each cell value with some combination of its neighbours' values, or computing the sum or difference of specific attribute values for each grid cell in two matching raster datasets. Descriptive statistics, such as cell counts, means, variances, maxima, minima, cumulative values, frequencies and a number of other measures and distance computations are also often included in this generic term spatial analysis. Spatial analysis includes a large variety of statistical techniques (descriptive, exploratory, and explanatory statistics) that apply to data that vary spatially and which can vary over time. Some more advanced statistical techniques include Getis-ord Gi* or Anselin Local Moran's I which are used to determine clustering patterns of spatially referenced data.

#### Advanced operations

Geospatial and Hydrospatial analysis goes beyond 2D and 3D mapping operations and spatial statistics. It is multi-dimensional and also temporal and includes:

- Surface analysis — in particular analysing the properties of physical surfaces, such as gradient, aspect and visibility, and analysing surface-like data "fields";
- Network analysis — examining the properties of natural and man-made networks in order to understand the behaviour of flows within and around such networks; and locational analysis. GIS-based network analysis may be used to address a wide range of practical problems such as route selection and facility location (core topics in the field of operations research), and problems involving flows such as those found in Hydrospatial and hydrology and transportation research. In many instances location problems relate to networks and as such are addressed with tools designed for this purpose, but in others existing networks may have little or no relevance or may be impractical to incorporate within the modeling process. Problems that are not specifically network constrained, such as new road or pipeline routing, regional warehouse location, mobile phone mast positioning or the selection of rural community health care sites, may be effectively analysed (at least initially) without reference to existing physical networks. Locational analysis "in the plane" is also applicable where suitable network datasets are not available, or are too large or expensive to be utilised, or where the location algorithm is very complex or involves the examination or simulation of a very large number of alternative configurations.
- Geovisualization — the creation and manipulation of images, maps, diagrams, charts, 3D views and their associated tabular datasets. GIS packages increasingly provide a range of such tools, providing static or rotating views, draping images over 2.5D surface representations, providing animations and fly-throughs, dynamic linking and brushing and spatio-temporal visualisations. This latter class of tools is the least developed, reflecting in part the limited range of suitable compatible datasets and the limited set of analytical methods available, although this picture is changing rapidly. All these facilities augment the core tools utilised in spatial analysis throughout the analytical process (exploration of data, identification of patterns and relationships, construction of models, and communication of results)

#### Mobile geospatial and hydrospatial Computing

Traditionally geospatial and hydrospatial computing has been performed primarily on personal computers (PCs) or servers. Due to the increasing capabilities of mobile devices, however, geospatial computing in mobile devices is a fast-growing trend. The portable nature of these devices, as well as the presence of useful sensors, such as Global Navigation Satellite System (GNSS) receivers and barometric pressure sensors, make them useful for capturing and processing geospatial and hydrospatial information in the field. In addition to the local processing of geospatial information on mobile devices, another growing trend is cloud-based geospatial computing. In this architecture, data can be collected in the field using mobile devices and then transmitted to cloud-based servers for further processing and ultimate storage. In a similar manner, geospatial and hydrospatial information can be made available to connected mobile devices via the cloud, allowing access to vast databases of geospatial and hydrospatial information anywhere where a wireless data connection is available.

### Geographic information science and spatial analysis

Geographic information systems (GIS) and the underlying geographic information science that advances these technologies have a strong influence on spatial analysis. The increasing ability to capture and handle geographic data means that spatial analysis is occurring within increasingly data-rich environments. Geographic data capture systems include remotely sensed imagery, environmental monitoring systems such as intelligent transportation systems, and location-aware technologies such as mobile devices that can report location in near-real time. GIS provide platforms for managing these data, computing spatial relationships such as distance, connectivity and directional relationships between spatial units, and visualizing both the raw data and spatial analytic results within a cartographic context. Subtypes include:

- Geovisualization (GVis) combines scientific visualization with digital cartography to support the exploration and analysis of geographic data and information, including the results of spatial analysis or simulation. GVis leverages the human orientation towards visual information processing in the exploration, analysis and communication of geographic data and information. In contrast with traditional cartography, GVis is typically three- or four-dimensional (the latter including time) and user-interactive.
- Geographic knowledge discovery (GKD) is the human-centered process of applying efficient computational tools for exploring massive spatial databases. GKD includes geographic data mining, but also encompasses related activities such as data selection, data cleaning and pre-processing, and interpretation of results. GVis can also serve a central role in the GKD process. GKD is based on the premise that massive databases contain interesting (valid, novel, useful and understandable) patterns that standard analytical techniques cannot find. GKD can serve as a hypothesis-generating process for spatial analysis, producing tentative patterns and relationships that should be confirmed using spatial analytical techniques.
- Spatial decision support systems (SDSS) take existing spatial data and use a variety of mathematical models to make projections into the future. This allows urban and regional planners to test intervention decisions prior to implementation.
