---
title: "Restricted maximum likelihood"
source: https://en.wikipedia.org/wiki/Restricted_maximum_likelihood
domain: mixed-effects-models
license: CC-BY-SA-4.0
tags: mixed model, random effects, fixed effects, intraclass correlation
fetched: 2026-07-02
---

# Restricted maximum likelihood

In statistics, the **restricted** (or **residual**, or **reduced**) **maximum likelihood** (**REML**) approach is a particular form of maximum likelihood estimation that does not base estimates on a maximum likelihood fit of all the information, but instead uses a likelihood function calculated from a transformed set of data, so that nuisance parameters have no effect.

In the case of variance component estimation, the original data set is replaced by a set of contrasts calculated from the data, and the likelihood function is calculated from the probability distribution of these contrasts, according to the model for the complete data set. In particular, REML is used as a method for fitting linear mixed models. In contrast to the earlier maximum likelihood estimation, REML can produce unbiased estimates of variance and covariance parameters.

The idea underlying REML estimation was put forward by M. S. Bartlett in 1937. The first description of the approach applied to estimating components of variance in unbalanced data was by Desmond Patterson and Robin Thompson of the University of Edinburgh in 1971, although they did not use the term REML. A review of the early literature was given by Harville.

REML estimation is available in a number of general-purpose statistical software packages, including Genstat (the REML directive), SAS (the MIXED procedure), SPSS (the MIXED command), Stata (the mixed command), JMP (statistical software), and R (especially the lme4 and older nlme packages), as well as in more specialist packages such as MLwiN, HLM, ASReml, BLUPF90, wombat, Statistical Parametric Mapping and CropStat.

REML estimation is implemented in Surfstat, a Matlab toolbox for the statistical analysis of univariate and multivariate surface and volumetric neuroimaging data using linear mixed effects models and random field theory, but more generally in the fitlme package for modeling linear mixed effects models in a domain-general way.
