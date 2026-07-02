---
title: "Data assimilation"
source: https://en.wikipedia.org/wiki/Data_assimilation
domain: weather-forecasting-nwp
license: CC-BY-SA-4.0
tags: numerical weather prediction, data assimilation, ensemble forecasting, primitive equations
fetched: 2026-07-02
---

# Data assimilation

**Data assimilation** refers to a large group of methods that update information from numerical computer models with information from observations. Data assimilation is used to update model states, model trajectories over time, model parameters, and combinations thereof. What distinguishes data assimilation from other estimation methods is that the computer model is a dynamical model, i.e. the model describes how model variables change over time, and its firm mathematical foundation in Bayesian Inference. As such, it generalizes inverse methods and has close connections with machine learning.

Data assimilation initially developed in the field of numerical weather prediction. Numerical weather prediction models are equations describing the evolution of the atmosphere, typically coded into a computer program. When these models are used for forecasting the model output quickly deviates from the real atmosphere. Hence, we use observations of the atmosphere to keep the model on track. Data assimilation provides a very large number of practical ways to bring these observations into the models.

Simply inserting point-wise measurements into the numerical models did not provide a satisfactory solution. Real world measurements contain errors both due to the quality of the instrument and how accurately the position of the measurement is known. These errors can cause instabilities in the models that eliminate any level of skill in a forecast. Thus, more sophisticated methods were needed in order to initialize a model using all available data while making sure to maintain stability in the numerical model. Such data typically includes the measurements as well as a previous forecast valid at the same time the measurements are made. If applied iteratively, this process begins to accumulate information from past observations into all subsequent forecasts.

Because data assimilation developed out of the field of numerical weather prediction, it initially gained popularity amongst the geosciences. In fact, one of the most cited publication in all of the geosciences is an application of data assimilation to reconstruct the observed history of the atmosphere.

## Details of the data assimilation process

Classically, data assimilation has been applied to chaotic dynamical systems that are too difficult to predict using simple extrapolation methods. The cause of this difficulty is that small changes in initial conditions can lead to large changes in prediction accuracy. This is sometimes known as the butterfly effect – the sensitive dependence on initial conditions in which a small change in one state of a deterministic nonlinear system can result in large differences in a later state.

At any update time, data assimilation usually takes a forecast (also known as the first guess, or background information) and applies a correction to the forecast based on a set of observed data and estimated errors that are present in both the observations and the forecast itself. The difference between the forecast and the observations at that time is called the departure or the innovation (as it provides new information to the data assimilation process). A weighting factor is applied to the innovation to determine how much of a correction should be made to the forecast based on the new information from the observations. The best estimate of the state of the system based on the correction to the forecast determined by a weighting factor times the innovation is called the analysis. In one dimension, computing the analysis could be as simple as forming a weighted average of a forecasted and observed value. In multiple dimensions the problem becomes more difficult. Much of the work in data assimilation is focused on adequately estimating the appropriate weighting factor based on intricate knowledge of the errors in the system.

The measurements are usually made of a real-world system, rather than of the model's incomplete representation of that system, and so a special function called the observation operator (usually depicted by *h()* for a nonlinear operator or "H" for its linearization) is needed to map the modeled variable to a form that can be directly compared with the observation.

## Data assimilation as statistical estimation

One of the common mathematical philosophical perspectives is to view data assimilation as a Bayesian estimation problem. From this perspective, the analysis step is an application of Bayes' theorem and the overall assimilation procedure is an example of recursive Bayesian estimation. However, the probabilistic analysis is usually simplified to a computationally feasible form. Advancing the probability distribution in time would be done exactly in the general case by the Fokker–Planck equation, but that is not feasible for high-dimensional systems; so, various approximations operating on simplified representations of the probability distributions are used instead. Often the probability distributions are assumed Gaussian so that they can be represented by their mean and covariance, which gives rise to the Kalman filter.

Many methods represent the probability distributions only by the mean and input some pre-calculated covariance. An example of a direct (or sequential) method to compute this is called optimal statistical interpolation, or simply optimal interpolation (OI). An alternative approach is to iteratively solve a cost function that solves an identical problem. These are called "variational methods", such as 3D-Var and 4D-Var. Typical minimization algorithms are the conjugate gradient method or the generalized minimal residual method. The ensemble Kalman filter is sequential method that uses a Monte Carlo approach to estimate both the mean and the covariance of a Gaussian probability distribution by an ensemble of simulations. More recently, hybrid combinations of ensemble approaches and variational methods have become more popular (e.g. they are used for operational forecasts both at the European Centre for Medium-Range Weather Forecasts (ECMWF) and at the NOAA National Centers for Environmental Prediction (NCEP).

## Data assimilation as a model update

Data assimilation can also be achieved within a model update loop, where we will iterate an initial model (or initial guess) in an optimisation loop to constrain the model to the observed data. Many optimisation approaches exist and all of them can be set up to update the model, for instance, evolutionary algorithm have proven to be efficient as free of hypothesis, but computationally expensive.

## Weather forecasting applications

In numerical weather prediction applications, data assimilation is most widely known as a method for combining observations of meteorological variables such as temperature and atmospheric pressure with prior forecasts in order to initialize numerical forecast models.

### Necessity

The atmosphere is a fluid. The idea of numerical weather prediction is to sample the state of the fluid at a given time and use the equations of fluid dynamics and thermodynamics to estimate the state of the fluid at some time in the future. The process of entering observation data into the model to generate initial conditions is called *initialization*. On land, terrain maps available at resolutions down to 1 kilometer (0.6 mi) globally are used to help model atmospheric circulations within regions of rugged topography, in order to better depict features such as downslope winds, mountain waves and related cloudiness that affects incoming solar radiation. The main inputs from country-based weather services are observations from devices (called radiosondes) in weather balloons that measure various atmospheric parameters and transmits them to a fixed receiver, as well as from weather satellites. The World Meteorological Organization acts to standardize the instrumentation, observing practices and timing of these observations worldwide. Stations either report hourly in METAR reports, or every six hours in SYNOP reports. These observations are irregularly spaced, so they are processed by data assimilation and objective analysis methods, which perform quality control and obtain values at locations usable by the model's mathematical algorithms. Some global models use finite differences, in which the world is represented as discrete points on a regularly spaced grid of latitude and longitude; other models use spectral methods that solve for a range of wavelengths. The data are then used in the model as the starting point for a forecast.

A variety of methods are used to gather observational data for use in numerical models. Sites launch radiosondes in weather balloons which rise through the troposphere and well into the stratosphere. Information from weather satellites is used where traditional data sources are not available. Commerce provides pilot reports along aircraft routes and ship reports along shipping routes. Research projects use reconnaissance aircraft to fly in and around weather systems of interest, such as tropical cyclones. Reconnaissance aircraft are also flown over the open oceans during the cold season into systems which cause significant uncertainty in forecast guidance, or are expected to be of high impact from three to seven days into the future over the downstream continent. Sea ice began to be initialized in forecast models in 1971. Efforts to involve sea surface temperature in model initialization began in 1972 due to its role in modulating weather in higher latitudes of the Pacific.

### History

In 1922, Lewis Fry Richardson published the first attempt at forecasting the weather numerically. Using a hydrostatic variation of Bjerknes's primitive equations, Richardson produced by hand a 6-hour forecast for the state of the atmosphere over two points in central Europe, taking at least six weeks to do so. His forecast calculated that the change in surface pressure would be 145 millibars (4.3 inHg), an unrealistic value incorrect by two orders of magnitude. The large error was caused by an imbalance in the pressure and wind velocity fields used as the initial conditions in his analysis, indicating the need for a data assimilation scheme.

Originally "subjective analysis" had been used in which numerical weather prediction (NWP) forecasts had been adjusted by meteorologists using their operational expertise. Then "objective analysis" (e.g. Cressman algorithm) was introduced for automated data assimilation. These objective methods used simple interpolation approaches, and thus were 3DDA (three-dimensional data assimilation) methods.

Later, 4DDA (four-dimensional data assimilation) methods, called "nudging", were developed, such as in the MM5 model. They are based on the simple idea of Newtonian relaxation (the 2nd axiom of Newton). They introduce into the right part of dynamical equations of the model a term that is proportional to the difference of the calculated meteorological variable and the observed value. This term that has a negative sign keeps the calculated state vector closer to the observations. Nudging can be interpreted as a variant of the Kalman-Bucy filter (a continuous time version of the Kalman filter) with the gain matrix prescribed rather than obtained from covariances.

A major development was achieved by L. Gandin (1963) who introduced the "statistical interpolation" (or "optimal interpolation") method, which developed earlier ideas of Kolmogorov. This is a 3DDA method and is a type of regression analysis which utilizes information about the spatial distributions of covariance functions of the errors of the "first guess" field (previous forecast) and "true field". These functions are never known. However, the different approximations were assumed.

The optimal interpolation algorithm is the reduced version of the Kalman filtering (KF) algorithm and in which the covariance matrices are not calculated from the dynamical equations but are pre-determined in advance.

Attempts to introduce the KF algorithms as a 4DDA tool for NWP models came later. However, this was (and remains) a difficult task because the full version requires solution of the enormous number of additional equations (~N*N~10**12, where N=Nx*Ny*Nz is the size of the state vector, Nx~100, Ny~100, Nz~100 – the dimensions of the computational grid). To overcome this difficulty, approximate or suboptimal Kalman filters were developed. These include the Ensemble Kalman filter and the Reduced-Rank Kalman filters (RRSQRT).

Another significant advance in the development of the 4DDA methods was utilizing the optimal control theory (variational approach) in the works of Le Dimet and Talagrand (1986), based on the previous works of J.-L. Lions and G. Marchuk, the latter being the first to apply that theory in the environmental modeling. The significant advantage of the variational approaches is that the meteorological fields satisfy the dynamical equations of the NWP model and at the same time they minimize the functional, characterizing their difference from observations. Thus, the problem of constrained minimization is solved. The 3DDA variational methods were developed for the first time by Sasaki (1958).

As was shown by Lorenc (1986), all the above-mentioned 4DDA methods are in some limit equivalent, i.e. under some assumptions they minimize the same cost function. However, in practical applications these assumptions are never fulfilled, the different methods perform differently and generally it is not clear what approach (Kalman filtering or variational) is better. The fundamental questions also arise in application of the advanced DA techniques such as convergence of the computational method to the global minimum of the functional to be minimised. For instance, cost function or the set in which the solution is sought can be not convex. The 4DDA method which is currently most successful is hybrid incremental 4D-Var, where an ensemble is used to augment the climatological background error covariances at the start of the data assimilation time window, but the background error covariances are evolved during the time window by a simplified version of the NWP forecast model. This data assimilation method is used operationally at forecast centres such as the Met Office.

### Cost function

The process of creating the analysis in data assimilation often involves minimization of a cost function. A typical cost function would be the sum of the squared deviations of the analysis values from the observations weighted by the accuracy of the observations, plus the sum of the squared deviations of the forecast fields and the analyzed fields weighted by the accuracy of the forecast. This has the effect of making sure that the analysis does not drift too far away from observations and forecasts that are known to usually be reliable.

#### 3D-Var

$J(\mathbf {x} )=(\mathbf {x} -\mathbf {x} _{b})^{\mathrm {T} }\mathbf {B} ^{-1}(\mathbf {x} -\mathbf {x} _{b})+(\mathbf {y} -{\mathit {H}}[\mathbf {x} ])^{\mathrm {T} }\mathbf {R} ^{-1}(\mathbf {y} -{\mathit {H}}[\mathbf {x} ]),$

where $\mathbf {B}$ denotes the background error covariance, $\mathbf {R}$ the observational error covariance.

$\nabla J(\mathbf {x} )=2\mathbf {B} ^{-1}(\mathbf {x} -\mathbf {x} _{b})-2{\mathit {H}}^{T}\mathbf {R} ^{-1}(\mathbf {y} -{\mathit {H}}[\mathbf {x} ])$

#### 4D-Var

$J(\mathbf {x} )=(\mathbf {x} -\mathbf {x} _{b})^{\mathrm {T} }\mathbf {B} ^{-1}(\mathbf {x} -\mathbf {x} _{b})+\sum _{i=0}^{n}(\mathbf {y} _{i}-{\mathit {H}}_{i}[\mathbf {x} _{i}])^{\mathrm {T} }\mathbf {R} _{i}^{-1}(\mathbf {y} _{i}-{\mathit {H}}_{i}[\mathbf {x} _{i}])$

provided that ${\mathit {H}}$ is a linear operator (matrix).

### Future development

Factors driving the rapid development of data assimilation methods for NWP models include:

- Utilizing the observations currently offers promising improvement in forecast skill at a variety of spatial scales (from global to highly local) and time scales.
- The number of different kinds of available observations (sodars, radars, satellite) is rapidly growing.

## Other applications

### Monitoring water and energy transfers

Data assimilation has been used, in the 1980s and 1990s, in several HAPEX (Hydrologic and Atmospheric Pilot Experiment) projects for monitoring energy transfers between the soil, vegetation and atmosphere. For instance:

- HAPEX-MobilHy, HAPEX-Sahel,

- the "Alpilles-ReSeDA" (Remote Sensing Data Assimilation) experiment, a European project in the FP4-ENV program which took place in the Alpilles region, South-East of France (1996–97). The Flow-chart diagram (right), excerpted from the final report of that project, shows how to infer variables of interest such as canopy state, radiative fluxes, environmental budget, production in quantity and quality, from remote sensing data and ancillary information. In that diagram, the small blue-green arrows indicate the direct way the models actually run.

### Other forecasting applications

Data assimilation methods are currently also used in other environmental forecasting problems, e.g. in hydrological and hydrogeological forecasting. Bayesian networks may also be used in a data assimilation approach to assess natural hazards such as landslides.

Given the abundance of spacecraft data for other planets in the Solar System, data assimilation is now also applied beyond the Earth to obtain re-analyses of the atmospheric state of extraterrestrial planets. Mars is the only extraterrestrial planet to which data assimilation has been applied so far. Available spacecraft data include, in particular, retrievals of temperature and dust/water/ice optical thicknesses from the Thermal Emission Spectrometer onboard NASA's Mars Global Surveyor and the Mars Climate Sounder onboard NASA's Mars Reconnaissance Orbiter. Two methods of data assimilation have been applied to these datasets: an Analysis Correction scheme and two Ensemble Kalman Filter schemes, both using a global circulation model of the martian atmosphere as forward model. The Mars Analysis Correction Data Assimilation (MACDA) dataset is publicly available from the British Atmospheric Data Centre.

Data assimilation is a part of the challenge for every forecasting problem.

Dealing with biased data is a serious challenge in data assimilation. Further development of methods to deal with biases will be of particular use. If there are several instruments observing the same variable then intercomparing them using probability distribution functions can be instructive.

The numerical forecast models are becoming of higher resolution due to the increase of computational power, with operational atmospheric models now running with horizontal resolutions of order of 1 km (e.g. at the German National Meteorological Service, the Deutscher Wetterdienst (DWD) and Met Office in the UK). This increase in horizontal resolutions is starting to allow to resolve more chaotic features of the non-linear models, e.g. to resolve convection on the grid scale, or clouds, in the atmospheric models. This increasing non-linearity in the models and observation operators poses a new problem in the data assimilation. The existing data assimilation methods such as many variants of ensemble Kalman filters and variational methods, well established with linear or near-linear models, are being assessed on non-linear models.

Many new methods are being developed, e.g. particle filters for high-dimensional problems, and hybrid data assimilation methods.

Other uses include trajectory estimation for the Apollo program, GPS, and atmospheric chemistry.
