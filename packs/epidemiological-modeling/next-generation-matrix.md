---
title: "Next-generation matrix"
source: https://en.wikipedia.org/wiki/Next-generation_matrix
domain: epidemiological-modeling
license: CC-BY-SA-4.0
tags: epidemiological modeling, compartmental models epidemiology, basic reproduction number, next-generation matrix
fetched: 2026-07-02
---

# Next-generation matrix

In epidemiology, the **next-generation matrix** is used to derive the basic reproduction number, for a compartmental model of the spread of infectious diseases. In population dynamics it is used to compute the basic reproduction number for structured population models. It is also used in multi-type branching models for analogous computations.

The method to compute the basic reproduction ratio using the next-generation matrix is given by Diekmann *et al.* (1990) and van den Driessche and Watmough (2002). To calculate the basic reproduction number by using a next-generation matrix, the whole population is divided into n compartments in which there are $m<n$ infected compartments. Let $x_{i},i=1,2,3,\ldots ,m$ be the numbers of infected individuals in the $i^{th}$ infected compartment at time *t*. Now, the epidemic model is

${\frac {\mathrm {d} x_{i}}{\mathrm {d} t}}=F_{i}(x)-V_{i}(x)$

, where

$V_{i}(x)=[V_{i}^{-}(x)-V_{i}^{+}(x)]$

In the above equations, $F_{i}(x)$ represents the rate of appearance of new infections in compartment i . $V_{i}^{+}$ represents the rate of transfer of individuals into compartment i by all other means, and $V_{i}^{-}(x)$ represents the rate of transfer of individuals out of compartment i . The above model can also be written as

${\frac {\mathrm {d} x}{\mathrm {d} t}}=F(x)-V(x)$

where

$F(x)={\begin{pmatrix}F_{1}(x),&F_{2}(x),&\ldots ,&F_{m}(x)\end{pmatrix}}^{T}$

and

$V(x)={\begin{pmatrix}V_{1}(x),&V_{2}(x),&\ldots ,&V_{m}(x)\end{pmatrix}}^{T}.$

Let $x_{0}$ be the disease-free equilibrium. The values of the parts of the Jacobian matrix $F(x)$ and $V(x)$ are:

$DF(x_{0})={\begin{pmatrix}F&0\\0&0\end{pmatrix}}$

and

$DV(x_{0})={\begin{pmatrix}V&0\\J_{3}&J_{4}\end{pmatrix}}$

respectively.

Here, F and V are *m* × *m* matrices, defined as $F={\frac {\partial F_{i}}{\partial x_{j}}}(x_{0})$ and $V={\frac {\partial V_{i}}{\partial x_{j}}}(x_{0})$ .

Now, the matrix $FV^{-1}$ is known as the next-generation matrix. The basic reproduction number of the model is then given by the eigenvalue of $FV^{-1}$ with the largest absolute value (the spectral radius of $FV^{-1}$ ). Next generation matrices can be computationally evaluated from observational data, which is often the most productive approach where there are large numbers of compartments.
