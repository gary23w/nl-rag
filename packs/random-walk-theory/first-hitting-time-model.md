---
title: "First-hitting-time model"
source: https://en.wikipedia.org/wiki/First-hitting-time_model
domain: random-walk-theory
license: CC-BY-SA-4.0
tags: random walk, self-avoiding walk, markov chain, gambler's ruin
fetched: 2026-07-02
---

# First-hitting-time model

In statistics, **first-hitting-time models** are simplified models that estimate the amount of time that passes before some random or stochastic process crosses a barrier, boundary or reaches a specified state, termed the **first hitting time**, or the **first passage time**. Accurate models give insight into the physical system under observation, and have been the topic of research in very diverse fields, from economics to ecology.

The idea that a first hitting time of a stochastic process might describe the time to occurrence of an event has a long history, starting with an interest in the first passage time of Wiener diffusion processes in economics and then in physics in the early 1900s. Modeling the probability of financial ruin as a first passage time was an early application in the field of insurance. An interest in the mathematical properties of first-hitting-times and statistical models and methods for analysis of survival data appeared steadily between the middle and end of the 20th century.

First-hitting-time models are a sub-class of survival models.

## Examples

A common example of a first-hitting-time model is a ruin problem, such as Gambler's ruin. In this example, an entity (often described as a gambler or an insurance company) has an amount of money which varies randomly with time, possibly with some drift. The model considers the event that the amount of money reaches 0, representing bankruptcy. The model can answer questions such as the probability that this occurs within finite time, or the mean time until which it occurs.

First-hitting-time models can be applied to expected lifetimes, of patients or mechanical devices. When the process reaches an adverse threshold state for the first time, the patient dies, or the device breaks down.

The time for a particle to escape through a narrow opening in a confined space is termed the narrow escape problem, and is commonly studied in biophysics and cellular biology.

## First passage time of a 1D Brownian particle

One of the simplest and omnipresent stochastic systems is that of the Brownian particle in one dimension. This system describes the motion of a particle which moves stochastically in one dimensional space, with equal probability of moving to the left or to the right. Given that Brownian motion is used often as a tool to understand more complex phenomena, it is important to understand the probability of a first passage time of the Brownian particle of reaching some position distant from its start location. This is done through the following means.

The probability density function (PDF) for a particle in one dimension is found by solving the one-dimensional diffusion equation. (This equation states that the position probability density diffuses outward over time. It is analogous to say, cream in a cup of coffee if the cream was all contained within some small location initially. After a long time the cream has diffused throughout the entire drink evenly.) Namely,

${\frac {\partial p(x,t\mid x_{0})}{\partial t}}=D{\frac {\partial ^{2}p(x,t\mid x_{0})}{\partial x^{2}}},$

given the initial condition $p(x,t={0}\mid x_{0})=\delta (x-x_{0})$ ; where $x(t)$ is the position of the particle at some given time, $x_{0}$ is the tagged particle's initial position, and D is the diffusion constant with the S.I. units $m^{2}s^{-1}$ (an indirect measure of the particle's speed). The bar in the argument of the instantaneous probability refers to the conditional probability. The diffusion equation states that the rate of change over time in the probability of finding the particle at $x(t)$ position depends on the deceleration over distance of such probability at that position.

It can be shown that the one-dimensional PDF is

$p(x,t;x_{0})={\frac {1}{\sqrt {4\pi Dt}}}\exp \left(-{\frac {(x-x_{0})^{2}}{4Dt}}\right).$

This states that the probability of finding the particle at $x(t)$ is Gaussian, and the width of the Gaussian is time dependent. More specifically the Full Width at Half Maximum (FWHM) – technically, this is actually the Full *Duration* at Half Maximum as the independent variable is time – scales like

${\rm {FWHM}}\sim {\sqrt {t}}.$

Using the PDF one is able to derive the average of a given function, L , at time t :

$\langle L(t)\rangle \equiv \int _{-\infty }^{\infty }L(x,t)p(x,t)\,dx,$

where the average is taken over all space (or any applicable variable).

The *First Passage Time Density* (FPTD) is the probability that a particle has *first* reached a point $x_{c}$ at exactly time t (not at some time during the interval up to t ). This probability density is calculable from the *Survival probability* (a more common probability measure in statistics). Consider the absorbing boundary condition $p(x_{c},t)=0$ (The subscript c for the absorption point $x_{c}$ is an abbreviation for *cliff* used in many texts as an analogy to an absorption point). The PDF satisfying this boundary condition is given by

$p(x,t;x_{0},x_{c})={\frac {1}{\sqrt {4\pi Dt}}}\left(\exp \left(-{\frac {(x-x_{0})^{2}}{4Dt}}\right)-\exp \left(-{\frac {(x-(2x_{c}-x_{0}))^{2}}{4Dt}}\right)\right),$

for $x<x_{c}$ . The survival probability, the probability that the particle has remained at a position $x<x_{c}$ for all times up to t , is given by

$S(t)\equiv \int _{-\infty }^{x_{c}}p(x,t;x_{0},x_{c})\,dx=\operatorname {erf} \left({\frac {x_{c}-x_{0}}{2{\sqrt {Dt}}}}\right),$

where $\operatorname {erf}$ is the error function. The relation between the Survival probability and the FPTD is as follows: the probability that a particle has reached the absorption point between times t and $t+dt$ is $f(t)\,dt=S(t)-S(t+dt)$ . If one uses the first-order Taylor approximation, the definition of the FPTD follows):

$f(t)=-{\frac {\partial S(t)}{\partial t}}.$

By using the diffusion equation and integrating, the explicit FPTD is

$f(t)\equiv {\frac {|x_{c}-x_{0}|}{\sqrt {4\pi Dt^{3}}}}\exp \left(-{\frac {(x_{c}-x_{0})^{2}}{4Dt}}\right).$

The first-passage time for a Brownian particle therefore follows a Lévy distribution.

For $t\gg {\frac {(x_{c}-x_{0})^{2}}{4D}}$ , it follows from above that

$f(t)={\frac {\Delta x}{\sqrt {4\pi Dt^{3}}}}\sim t^{-3/2},$

where $\Delta x\equiv |x_{c}-x_{0}|$ . This equation states that the probability for a Brownian particle achieving a first passage at some long time (defined in the paragraph above) becomes increasingly small, but is always *finite*.

The first moment of the FPTD diverges (as it is a so-called *heavy-tailed* distribution), therefore one cannot calculate the average FPT, so instead, one can calculate the *typical* time, the time when the FPTD is at a maximum ( $\partial f/\partial t=0$ ), i.e.,

$\tau _{\rm {ty}}={\frac {\Delta x^{2}}{6D}}.$

## First-hitting-time applications in many families of stochastic processes

First hitting times are central features of many families of stochastic processes, including Poisson processes, Wiener processes, gamma processes, and Markov chains, to name but a few. The state of the stochastic process may represent, for example, the strength of a physical system, the health of an individual, or the financial condition of a business firm. The system, individual or firm fails or experiences some other critical endpoint when the process reaches a threshold state for the first time. The critical event may be an adverse event (such as equipment failure, congested heart failure, or lung cancer) or a positive event (such as recovery from illness, discharge from hospital stay, child birth, or return to work after traumatic injury). The lapse of time until that critical event occurs is usually interpreted generically as a ‘survival time’. In some applications, the threshold is a set of multiple states so one considers competing first hitting times for reaching the first threshold in the set, as is the case when considering competing causes of failure in equipment or death for a patient.

## Threshold regression: first-hitting-time regression

Practical applications of theoretical models for first hitting times often involve regression structures. When first hitting time models are equipped with regression structures, accommodating covariate data, we call such regression structure *threshold regression*. The threshold state, parameters of the process, and even time scale may depend on corresponding covariates. Threshold regression as applied to time-to-event data has emerged since the start of this century and has grown rapidly, as described in a 2006 survey article and its references. Connections between threshold regression models derived from first hitting times and the ubiquitous Cox proportional hazards regression model was investigated in. Applications of threshold regression range over many fields, including the physical and natural sciences, engineering, social sciences, economics and business, agriculture, health and medicine.

## Latent vs observable

In many real world applications, a first-hitting-time (FHT) model has three underlying components: (1) a *parent stochastic process* $\{X(t)\}\,\,$ , which might be latent, (2) a *threshold* (or the barrier) and (3) a *time scale*. The first hitting time is defined as the time when the stochastic process first reaches the threshold. It is very important to distinguish whether the sample path of the parent process is latent (i.e., unobservable) or observable, and such distinction is a characteristic of the FHT model. By far, latent processes are most common. To give an example, we can use a Wiener process $\{X(t),t\geq 0\,\}\,$ as the parent stochastic process. Such Wiener process can be defined with the mean parameter ${\mu }\,\,$ , the variance parameter ${\sigma ^{2}}\,\,$ , and the initial value $X(0)=x_{0}>0\,$ .

## Operational or analytical time scale

The time scale of the stochastic process may be calendar or clock time or some more operational measure of time progression, such as mileage of a car, accumulated wear and tear on a machine component or accumulated exposure to toxic fumes. In many applications, the stochastic process describing the system state is latent or unobservable and its properties must be inferred indirectly from censored time-to-event data and/or readings taken over time on correlated processes, such as marker processes. The word ‘regression’ in threshold regression refers to first-hitting-time models in which one or more regression structures are inserted into the model in order to connect model parameters to explanatory variables or covariates. The parameters given regression structures may be parameters of the stochastic process, the threshold state and/or the time scale itself.
