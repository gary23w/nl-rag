---
title: "Data reduction"
source: https://en.wikipedia.org/wiki/Data_reduction
domain: kernelization
license: CC-BY-SA-4.0
tags: kernelization technique, problem kernel, data reduction rule, vertex cover kernel
fetched: 2026-07-02
---

# Data reduction

**Data reduction** is the transformation of numerical or alphabetical digital information derived empirically or experimentally into a corrected, ordered, and simplified form. The purpose of data reduction can be two-fold: reduce the number of data records by eliminating invalid data or produce summary data and statistics at different aggregation levels for various applications. Data reduction does not necessarily mean loss of information.

When information is derived from instrument readings there may also be a transformation from analog to digital form. When the data are already in digital form the 'reduction' of the data typically involves some editing, scaling, encoding, sorting, collating, and producing tabular summaries. When the observations are discrete but the underlying phenomenon is continuous then smoothing and interpolation are often needed. The data reduction is often undertaken in the presence of reading or measurement errors. Some idea of the nature of these errors is needed before the most likely value may be determined.

An example in astronomy is the data reduction in the *Kepler* satellite. This satellite records 95-megapixel images once every six seconds, generating dozens of megabytes of data per second, which is orders-of-magnitudes more than the downlink bandwidth of 550 kB/s. The on-board data reduction encompasses co-adding the raw frames for thirty minutes, reducing the bandwidth by a factor of 300. Furthermore, interesting targets are pre-selected and only the relevant pixels are processed, which is 6% of the total. This reduced data is then sent to Earth where it is processed further.

Research has also been carried out on the use of data reduction in wearable (wireless) devices for health monitoring and diagnosis applications. For example, in the context of epilepsy diagnosis, data reduction has been used to increase the battery lifetime of a wearable EEG device by selecting and only transmitting EEG data that is relevant for diagnosis and discarding background activity.

## Types of Data Reduction

### Dimensionality Reduction

When dimensionality increases, data becomes increasingly sparse while density and distance between points, critical to clustering and outlier analysis, becomes less meaningful. Dimensionality reduction helps reduce noise in the data and allows for easier visualization, such as the example below where 3-dimensional data is transformed into 2 dimensions to show hidden parts. One method of dimensionality reduction is wavelet transform, in which data is transformed to preserve relative distance between objects at different levels of resolution, and is often used for image compression.

### Numerosity Reduction

This method of data reduction reduces the data volume by choosing alternate, smaller forms of data representation. Numerosity reduction can be split into 2 groups: parametric and non-parametric methods. Parametric methods (regression, for example) assume the data fits some model, estimate model parameters, store only the parameters, and discard the data. One example of this is in the image below, where the volume of data to be processed is reduced based on more specific criteria. Another example would be a log-linear model, obtaining a value at a point in m-D space as the product on appropriate marginal subspaces. Non-parametric methods do not assume models, some examples being histograms, clustering, sampling, etc.

### Statistical modelling

Data reduction can be obtained by assuming a statistical model for the data. Classical principles of data reduction include sufficiency, likelihood, conditionality and equivariance.
