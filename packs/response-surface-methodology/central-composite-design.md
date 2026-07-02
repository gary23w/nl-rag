---
title: "Central composite design"
source: https://en.wikipedia.org/wiki/Central_composite_design
domain: response-surface-methodology
license: CC-BY-SA-4.0
tags: response surface methodology, central composite design, Box Behnken, optimal design
fetched: 2026-07-02
---

# Central composite design

In statistics, a **central composite design** is an experimental design, useful in response surface methodology, for building a second order (quadratic) model for the response variable without needing to use a complete three-level factorial experiment.

After the designed experiment is performed, linear regression is used, sometimes iteratively, to obtain results. Coded variables are often used when constructing this design.

## Implementation

The design consists of three distinct sets of experimental runs:

1. A factorial (perhaps fractional) design in the factors studied, each having two levels;
2. A set of *center points*, experimental runs whose values of each factor are the medians of the values used in the factorial portion. This point is often replicated in order to improve the precision of the experiment;
3. A set of *axial points*, experimental runs identical to the centre points except for one factor, which will take on values both below and above the median of the two factorial levels, and typically both outside their range. All factors are varied in this way.

## Design matrix

The design matrix for a central composite design experiment involving *k* factors is derived from a matrix, **d**, containing the following three different parts corresponding to the three types of experimental runs:

1. The matrix **F** obtained from the factorial experiment. The factor levels are scaled so that its entries are coded as +1 and −1.
2. The matrix **C** from the center points, denoted in coded variables as (0,0,0,...,0), where there are *k* zeros.
3. A matrix **E** from the axial points, with 2*k* rows. Each factor is sequentially placed at ±α and all other factors are at zero. The value of α is determined by the designer; while arbitrary, some values may give the design desirable properties. This part would look like:

$\mathbf {E} ={\begin{bmatrix}\alpha &0&0&\cdots &\cdots &\cdots &0\\{-\alpha }&0&0&\cdots &\cdots &\cdots &0\\0&\alpha &0&\cdots &\cdots &\cdots &0\\0&{-\alpha }&0&\cdots &\cdots &\cdots &0\\\vdots &{}&{}&{}&{}&{}&\vdots \\0&0&0&0&\cdots &\cdots &\alpha \\0&0&0&0&\cdots &\cdots &{-\alpha }\\\end{bmatrix}}.$

Then **d** is the vertical concatenation:

$\mathbf {d} ={\begin{bmatrix}\mathbf {F} \\\mathbf {C} \\\mathbf {E} \end{bmatrix}}.$

The design matrix **X** used in linear regression is the horizontal concatenation of a column of 1s (intercept), **d**, and all elementwise products of a pair of columns of **d**:

$\mathbf {X} ={\begin{bmatrix}\mathbf {1} &\mathbf {d} &\mathbf {d} (1)\times \mathbf {d} (2)&\mathbf {d} (1)\times \mathbf {d} (3)&\cdots &\mathbf {d} (k-1)\times \mathbf {d} (k)&\mathbf {d} (1)^{2}&\mathbf {d} (2)^{2}&\cdots &\mathbf {d} (k)^{2}\end{bmatrix}},$

where **d**(*i*) represents the *i*th column in **d**.

### Choosing α

There are many different methods to select a useful value of α. Let *F* be the number of points due to the factorial design and *T* = 2*k* + *n*, the number of additional points, where *n* is the number of central points in the design. Common values are as follows (Myers, 1971):

1. **Orthogonal design:**: $\alpha =(Q\times F/4)^{1/4}\,\!$ , where $Q=({\sqrt {F+T}}-{\sqrt {F}})^{2}$ ;
2. **Rotatable design**: α = *F*1/4 (the design implemented by MATLAB’s *ccdesign* function).

### Application of central composite designs for optimization

Statistical approaches such as Response Surface Methodology can be employed to maximize the production of a special substance by optimization of operational factors. In contrast to conventional methods, the interaction among process variables can be determined by statistical techniques. For instance, in a study, a central composite design was employed to investigate the effect of critical parameters of organosolv pretreatment of rice straw including temperature, time, and ethanol concentration. The residual solid, lignin recovery, and hydrogen yield were selected as the response variables.
