---
title: "Method of matched asymptotic expansions"
source: https://en.wikipedia.org/wiki/Method_of_matched_asymptotic_expansions
domain: singular-perturbation
license: CC-BY-SA-4.0
tags: singular perturbation, boundary layer, matched asymptotic expansions, relaxation oscillator
fetched: 2026-07-02
---

# Method of matched asymptotic expansions

In mathematics, the **method of matched asymptotic expansions** is a common approach to finding an accurate approximation to the solution to an equation, or system of equations. It is particularly used when solving singularly perturbed differential equations. It involves finding several different approximate solutions, each of which is valid (i.e. accurate) for part of the range of the independent variable, and then combining these different solutions together to give a single approximate solution that is valid for the whole range of values of the independent variable. In the Russian literature, these methods were known under the name of "intermediate asymptotics" and were introduced in the work of Yakov Zeldovich and Grigory Barenblatt.

## Method overview

In a large class of singularly perturbed problems, the domain may be divided into two or more subdomains. In one of these, often the largest, the solution is accurately approximated by an asymptotic series found by treating the problem as a regular perturbation (i.e., by setting a relatively small parameter to zero). The other subdomains consist of one or more small regions in which that approximation is inaccurate, generally because the perturbation terms in the problem are not negligible there. These areas are referred to as *transition layers* in general, and specifically as *boundary layers* or *interior layers* depending on whether they occur at the domain boundary (as is the usual case in applications) or inside the domain, respectively.

An approximation in the form of an asymptotic series is obtained in the transition layer(s) by treating that part of the domain as a separate perturbation problem. This approximation is called the *inner solution*, and the other is the *outer solution*, named for their relationship to the transition layer(s). The outer and inner solutions are then combined through a process called "matching" in such a way that an approximate solution for the whole domain is obtained.

## A simple example

Consider the boundary value problem $\varepsilon y''+(1+\varepsilon )y'+y=0,$ where y is a function of independent time variable t , which ranges from 0 to 1, the boundary conditions are $y(0)=0$ and $y(1)=1$ , and $\varepsilon$ is a small parameter, such that $0<\varepsilon \ll 1$ .

### Outer solution, valid for *t* = *O*(1)

Since $\varepsilon$ is very small, our first approach is to treat the equation as a regular perturbation problem, i.e. make the approximation $\varepsilon =0$ , and hence find the solution to the problem $y'+y=0.$

Alternatively, consider that when y and t are both of size *O*(1), the four terms on the left hand side of the original equation are respectively of sizes $O(\varepsilon )$ , *O*(1), $O(\varepsilon )$ and *O*(1). The leading-order balance on this timescale, valid in the distinguished limit $\varepsilon \to 0$ , is therefore given by the second and fourth terms, i.e., $y'+y=0.$

This has solution $y=Ae^{-t}$ for some constant A . Applying the boundary condition $y(0)=0$ , we would have $A=0$ ; applying the boundary condition $y(1)=1$ , we would have $A=e$ . It is therefore impossible to satisfy both boundary conditions, so $\varepsilon =0$ is not a valid approximation to make across the whole of the domain (i.e. this is a singular perturbation problem). From this we infer that there must be a boundary layer at one of the endpoints of the domain where $\varepsilon$ needs to be included. This region will be where $\varepsilon$ is no longer negligible compared to the independent variable t , i.e. t and $\varepsilon$ are of comparable size, i.e. the boundary layer is adjacent to $t=0$ . Therefore, the other boundary condition $y(1)=1$ applies in this outer region, so $A=e$ , i.e. $y_{\mathrm {O} }=e^{1-t}$ is an accurate approximate solution to the original boundary value problem in this outer region. It is the leading-order solution.

### Inner solution, valid for *t* = *O*(*ε*)

In the inner region, t and $\varepsilon$ are both tiny, but of comparable size, so define the new *O*(1) time variable $\tau =t/\varepsilon$ . Rescale the original boundary value problem by replacing t with $\tau \varepsilon$ , and the problem becomes ${\frac {1}{\varepsilon }}y''(\tau )+\left({1+\varepsilon }\right){\frac {1}{\varepsilon }}y'(\tau )+y(\tau )=0,$ which, after multiplying by $\varepsilon$ and taking $\varepsilon =0$ , is $y''+y'=0.$

Alternatively, consider that when t has reduced to size $O(\varepsilon )$ , then y is still of size *O*(1) (using the expression for $y_{\mathrm {O} }$ ), and so the four terms on the left hand side of the original equation are respectively of sizes $O(\varepsilon ^{-1})$ , $O(\varepsilon ^{-1})$ , $O(1)$ and $O(1)$ . The leading-order balance on this timescale, valid in the distinguished limit $\varepsilon \to 0$ , is therefore given by the first and second terms, i.e. $y''+y'=0.$

This has solution $y=B-Ce^{-\tau }$ for some constants B and C . Since $y(0)=0$ applies in this inner region, this gives $B=C$ , so an accurate approximate solution to the original boundary value problem in this inner region (it is the leading-order solution) is $y_{\mathrm {I} }=B\left({1-e^{-\tau }}\right)=B\left({1-e^{-t/\varepsilon }}\right).$

### Matching

We use matching to find the value of the constant B . The idea of matching is that the inner and outer solutions should agree for values of t in an intermediate (or overlap) region, i.e. where $\varepsilon \ll t\ll 1$ . We need the outer limit of the inner solution to match the inner limit of the outer solution, i.e., $\lim _{\tau \to \infty }y_{\mathrm {I} }=\lim _{t\to 0}y_{\mathrm {O} },$ which gives $B=e$ .

The above problem is the simplest of the simple problems dealing with matched asymptotic expansions. One can immediately calculate that $e^{1-t}$ is the entire asymptotic series for the outer region whereas the ${\mathcal {O}}(\varepsilon )$ correction to the inner solution $y_{\mathrm {I} }$ is ${\textstyle B(1-e^{-t/\varepsilon })}$ and the constant of integration B must be obtained from inner-outer matching.

Notice, the intuitive idea for matching of taking the limits i.e. ${\textstyle \lim _{\tau \to \infty }y_{\mathrm {I} }=\lim _{t\to 0}y_{\mathrm {O} },}$ does not apply at this level. This is simply because the underlined term does not converge to a limit. The methods to follow in these types of cases are either to go for a) method of an intermediate variable or using b) the Van-Dyke matching rule. The former method is cumbersome and works always whereas the Van-Dyke matching rule is easy to implement but with limited applicability. A concrete boundary value problem having all the essential ingredients is the following.

Consider the boundary value problem $\varepsilon y''-x^{2}y'-y=1,\quad y(0)=y(1)=1$

The conventional outer expansion $y_{\mathrm {O} }=y_{0}+\varepsilon y_{1}+\cdots$ gives $y_{0}=\alpha e^{1/x}-1$ , where $\alpha$ must be obtained from matching.

The problem has boundary layers both on the left and on the right. The left boundary layer near 0 has a thickness $\varepsilon ^{1/2}$ whereas the right boundary layer near 1 has thickness $\varepsilon$ . Let us first calculate the solution on the left boundary layer by rescaling $X=x/\varepsilon ^{1/2},\;Y=y$ , then the differential equation to satisfy on the left is $Y''-\varepsilon ^{1/2}X^{2}Y'-Y=1,\quad Y(0)=1$ and accordingly, we assume an expansion $Y^{l}=Y_{0}^{l}+\varepsilon ^{1/2}Y_{1/2}^{l}+\cdots$ .

The ${\mathcal {O}}(1)$ inhomogeneous condition on the left provides us the reason to start the expansion at ${\mathcal {O}}(1)$ . The leading order solution is $Y_{0}^{l}=2e^{-X}-1$ .

This with $1-1$ van-Dyke matching gives $\alpha =0$ .

Let us now calculate the solution on the right rescaling $X=(1-x)/\varepsilon ,\;Y=y$ , then the differential equation to satisfy on the right is $Y''+\left(1-2\varepsilon X+\varepsilon ^{2}X^{2}\right)Y'-\varepsilon Y=\varepsilon ,\quad Y(1)=1,$ and accordingly, we assume an expansion $Y^{r}=Y_{0}^{r}+\varepsilon Y_{1}^{r}+\cdots .$

The ${\mathcal {O}}(1)$ inhomogeneous condition on the right provides us the reason to start the expansion at ${\mathcal {O}}(1)$ . The leading order solution is $Y_{0}^{r}=(1-B)+Be^{-X}$ . This with $1-1$ van-Dyke matching gives $B=2$ . Proceeding in a similar fashion if we calculate the higher order-corrections we get the solutions as $Y^{l}=2e^{-X}-1+\varepsilon ^{1/2}e^{-X}\left({\frac {X^{3}}{3}}+{\frac {X^{2}}{2}}+{\frac {X}{2}}\right)+{\mathcal {O}}(\varepsilon ),\quad X={\frac {x}{\varepsilon ^{1/2}}}.$ $y\equiv -1.$ $Y^{r}=2e^{-X}-1+2\varepsilon e^{-X}\left(X+X^{2}\right)+{\mathcal {O}}(\varepsilon ^{2}),\quad X={\frac {1-x}{\varepsilon }}.$

### Composite solution

To obtain our final, matched, composite solution, valid on the whole domain, one popular method is the uniform method. In this method, we add the inner and outer approximations and subtract their overlapping value, $\,y_{\mathrm {overlap} }$ , which would otherwise be counted twice. The overlapping value is the outer limit of the inner boundary layer solution, and the inner limit of the outer solution; these limits were above found to equal e . Therefore, the final approximate solution to this boundary value problem is, $y(t)=y_{\mathrm {I} }+y_{\mathrm {O} }-y_{\mathrm {overlap} }=e\left({1-e^{-t/\varepsilon }}\right)+e^{1-t}-e=e\left({e^{-t}-e^{-t/\varepsilon }}\right).$

Note that this expression correctly reduces to the expressions for $y_{\mathrm {I} }$ and $y_{\mathrm {O} }$ when t is $O(\varepsilon )$ and *O*(1), respectively.

### Accuracy

This final solution satisfies the problem's original differential equation (shown by substituting it and its derivatives into the original equation). Also, the boundary conditions produced by this final solution match the values given in the problem, up to a constant multiple. This implies, due to the uniqueness of the solution, that the matched asymptotic solution is identical to the exact solution up to a constant multiple. This is not necessarily always the case, any remaining terms should go to zero uniformly as $\varepsilon \rightarrow 0$ .

Not only does our solution successfully approximately solve the problem at hand, it closely approximates the problem's exact solution. It happens that this particular problem is easily found to have exact solution $y(t)={\frac {e^{-t}-e^{-t/\varepsilon }}{e^{-1}-e^{-1/\varepsilon }}},$ which has the same form as the approximate solution, by the multiplying constant. The approximate solution is the first term in a binomial expansion of the exact solution in powers of $e^{1-1/\varepsilon }$ .

### Location of boundary layer

Conveniently, we can see that the boundary layer, where $y'$ and $y''$ are large, is near $t=0$ , as we supposed earlier. If we had supposed it to be at the other endpoint and proceeded by making the rescaling $\tau =(1-t)/\varepsilon$ , we would have found it impossible to satisfy the resulting matching condition. For many problems, this kind of trial and error is the only way to determine the true location of the boundary layer.

## Harder problems

The problem above is a simple example because it is a single equation with only one dependent variable, and there is one boundary layer in the solution. Harder problems may contain several co-dependent variables in a system of several equations, and/or with several boundary and/or interior layers in the solution.

It is often desirable to find more terms in the asymptotic expansions of both the outer and the inner solutions. The appropriate form of these expansions is not always clear: while a power-series expansion in $\varepsilon$ may work, sometimes the appropriate form involves fractional powers of $\varepsilon$ , functions such as $\varepsilon \log \varepsilon$ , et cetera. As in the above example, we will obtain outer and inner expansions with some coefficients which must be determined by matching.

## Second-order differential equations

### Schrödinger-like second-order differential equations

A method of matched asymptotic expansions - with matching of solutions in the common domain of validity - has been developed and used extensively by Dingle and Müller-Kirsten for the derivation of asymptotic expansions of the solutions and characteristic numbers (band boundaries) of Schrödinger-like second-order differential equations with periodic potentials - in particular for the Mathieu equation (best example), Lamé and ellipsoidal wave equations, oblate and prolate spheroidal wave equations, and equations with anharmonic potentials.

### Convection–diffusion equations

Methods of matched asymptotic expansions have been developed to find approximate solutions to the Smoluchowski convection–diffusion equation, which is a singularly perturbed second-order differential equation. The problem has been studied particularly in the context of colloid particles in linear flow fields, where the variable is given by the pair distribution function around a test particle. In the limit of low Péclet number, the convection–diffusion equation also presents a singularity at infinite distance (where normally the far-field boundary condition should be placed) due to the flow field being linear in the interparticle separation. This problem can be circumvented with a spatial Fourier transform as shown by Jan Dhont. A different approach to solving this problem was developed by Alessio Zaccone and coworkers and consists in placing the boundary condition right at the boundary layer distance, upon assuming (in a first-order approximation) a constant value of the pair distribution function in the outer layer due to convection being dominant there. This leads to an approximate theory for the encounter rate of two interacting colloid particles in a linear flow field in good agreement with the full numerical solution. When the Péclet number is significantly larger than one, the singularity at infinite separation no longer occurs and the method of matched asymptotics can be applied to construct the full solution for the pair distribution function across the entire domain.
