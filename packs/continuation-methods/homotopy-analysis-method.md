---
title: "Homotopy analysis method"
source: https://en.wikipedia.org/wiki/Homotopy_analysis_method
domain: continuation-methods
license: CC-BY-SA-4.0
tags: numerical continuation, homotopy continuation, bifurcation theory, predictor-corrector method
fetched: 2026-07-02
---

# Homotopy analysis method

The **homotopy analysis method** (**HAM**) is a semi-analytical technique to solve nonlinear ordinary/partial differential equations. The homotopy analysis method employs the concept of the homotopy from topology to generate a convergent series solution for nonlinear systems. This is enabled by utilizing a homotopy-Maclaurin series to deal with the nonlinearities in the system.

The HAM was first applied to calculate the ballistic transport of hot electrons in inhomogeneous sub-micron structures by solving a system of nonlinear differential equations in 1988 by Claus Hillebrand, RWTH Aachen. This was published in his thesis in 1989, see reference [4]. The HAM was first devised in 1992 by Liao Shijun of Shanghai Jiaotong University in his PhD dissertation and further modified in 1997 to introduce a non-zero auxiliary parameter, referred to as the **convergence-control parameter**, ***c*****0**, to construct a homotopy on a differential system in general form. The convergence-control parameter is a non-physical variable that provides a simple way to verify and enforce convergence of a solution series. The capability of the HAM to naturally show convergence of the series solution is unusual in analytical and semi-analytic approaches to nonlinear partial differential equations.

## Characteristics

The HAM distinguishes itself from various other analytical methods in four important aspects. First, it is a series expansion method that is not directly dependent on small or large physical parameters. Thus, it is applicable for not only weakly but also strongly nonlinear problems, going beyond some of the inherent limitations of the standard perturbation methods. Second, the HAM is a unified method for the Lyapunov artificial small parameter method, the delta expansion method, the Adomian decomposition method, and the homotopy perturbation method. The greater generality of the method often allows for strong convergence of the solution over larger spatial and parameter domains. Third, the HAM gives excellent flexibility in the expression of the solution and how the solution is explicitly obtained. It provides great freedom to choose the basis functions of the desired solution and the corresponding auxiliary linear operator of the homotopy. Finally, unlike the other analytic approximation techniques, the HAM provides a simple way to ensure the convergence of the solution series.

The homotopy analysis method is also able to combine with other techniques employed in nonlinear differential equations such as spectral methods and Padé approximants. It may further be combined with computational methods, such as the boundary element method to allow the linear method to solve nonlinear systems. Different from the numerical technique of homotopy continuation, the homotopy analysis method is an analytic approximation method as opposed to a discrete computational method. Further, the HAM uses the homotopy parameter only on a theoretical level to demonstrate that a nonlinear system may be split into an infinite set of linear systems which are solved analytically, while the continuation methods require solving a discrete linear system as the homotopy parameter is varied to solve the nonlinear system.

## Applications

In the last twenty years, the HAM has been applied to solve a growing number of nonlinear ordinary/partial differential equations in science, finance, and engineering. For example, multiple steady-state resonant waves in deep and finite water depth were found with the wave resonance criterion of arbitrary number of traveling gravity waves; this agreed with Phillips' criterion for four waves with small amplitude. Further, a unified wave model applied with the HAM, admits not only the traditional smooth progressive periodic/solitary waves, but also the progressive solitary waves with peaked crest in finite water depth. This model shows peaked solitary waves are consistent solutions along with the known smooth ones. Additionally, the HAM has been applied to many other nonlinear problems such as nonlinear heat transfer, the limit cycle of nonlinear dynamic systems, the American put option, the exact Navier–Stokes equation, the option pricing under stochastic volatility, the electrohydrodynamic flows, the Poisson–Boltzmann equation for semiconductor devices, and others.

## Brief mathematical description

Consider a general nonlinear differential equation

${\mathcal {N}}[u(x)]=0$

,

where ${\mathcal {N}}$ is a nonlinear operator. Let ${\mathcal {L}}$ denote an auxiliary linear operator, *u*0(*x*) an initial guess of *u*(*x*), and *c*0 a constant (called the convergence-control parameter), respectively. Using the embedding parameter *q* ∈ [0,1] from homotopy theory, one may construct a family of equations,

$(1-q){\mathcal {L}}[U(x;q)-u_{0}(x)]=c_{0}\,q\,{\mathcal {N}}[U(x;q)],$

called the zeroth-order deformation equation, whose solution varies continuously with respect to the embedding parameter *q* ∈ [0,1]. This is the linear equation

${\mathcal {L}}[U(x;q)-u_{0}(x)]=0,$

with known initial guess *U*(*x*; 0) = *u*0(*x*) when *q* = 0, but is equivalent to the original nonlinear equation ${\mathcal {N}}[u(x)]=0$ , when *q* = 1, i.e. *U*(*x*; 1) = *u*(*x*)). Therefore, as *q* increases from 0 to 1, the solution *U*(*x*; *q*) of the zeroth-order deformation equation varies (or deforms) from the chosen initial guess *u*0(*x*) to the solution *u*(*x*) of the considered nonlinear equation.

Expanding *U*(*x*; *q*) in a Taylor series about *q* = 0, we have the homotopy-Maclaurin series

$U(x;q)=u_{0}(x)+\sum _{m=1}^{\infty }u_{m}(x)\,q^{m}.$

Assuming that the so-called convergence-control parameter *c*0 of the zeroth-order deformation equation is properly chosen that the above series is convergent at *q* = 1, we have the homotopy-series solution

$u(x)=u_{0}(x)+\sum _{m=1}^{\infty }u_{m}(x).$

From the zeroth-order deformation equation, one can directly derive the governing equation of *u*m(*x*)

${\mathcal {L}}[u_{m}(x)-\chi _{m}u_{m-1}(x)]=c_{0}\,R_{m}[u_{0},u_{1},\ldots ,u_{m-1}],$

called the *m*th-order deformation equation, where $\chi _{1}=0$ and $\chi _{k}=1$ for *k* > 1, and the right-hand side *R**m* is dependent only upon the known results *u*0, *u*1, ..., *u**m* − 1 and can be obtained easily using computer algebra software. In this way, the original nonlinear equation is transferred into an infinite number of linear ones, but without the assumption of any small/large physical parameters.

Since the HAM is based on a homotopy, one has great freedom to choose the initial guess *u*0(*x*), the auxiliary linear operator ${\mathcal {L}}$ , and the convergence-control parameter *c*0 in the zeroth-order deformation equation. Thus, the HAM provides the mathematician freedom to choose the equation-type of the high-order deformation equation and the base functions of its solution. The optimal value of the convergence-control parameter *c*0 is determined by the minimum of the squared residual error of governing equations and/or boundary conditions after the general form has been solved for the chosen initial guess and linear operator. Thus, the convergence-control parameter *c*0 is a simple way to guarantee the convergence of the homotopy series solution and differentiates the HAM from other analytic approximation methods. The method overall gives a useful generalization of the concept of homotopy.

## The HAM and computer algebra

The HAM is an analytic approximation method designed for the computer era with the goal of "computing with functions instead of numbers." In conjunction with a computer algebra system such as Mathematica or Maple, one can gain analytic approximations of a highly nonlinear problem to arbitrarily high order by means of the HAM in only a few seconds. Inspired by the recent successful applications of the HAM in different fields, a Mathematica package based on the HAM, called BVPh, has been made available online for solving nonlinear boundary-value problems [5]. BVPh is a solver package for highly nonlinear ODEs with singularities, multiple solutions, and multipoint boundary conditions in either a finite or an infinite interval, and includes support for certain types of nonlinear PDEs. Another HAM-based Mathematica code, APOh, has been produced to solve for an explicit analytic approximation of the optimal exercise boundary of American put option, which is also available online [6].

## Frequency response analysis for nonlinear oscillators

The HAM has recently been reported to be useful for obtaining analytical solutions for nonlinear frequency response equations. Such solutions are able to capture various nonlinear behaviors such as hardening-type, softening-type or mixed behaviors of the oscillator. These analytical equations are also useful in prediction of chaos in nonlinear systems.
