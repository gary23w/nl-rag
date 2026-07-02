---
title: "Compartmental models (epidemiology) (part 2/2)"
source: https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology
domain: epidemiological-modeling
license: CC-BY-SA-4.0
tags: epidemiological modeling, compartmental models epidemiology, basic reproduction number, next-generation matrix
fetched: 2026-07-02
part: 2/2
---

## Variations on the basic SIR model

### SIS model

Some infections, for example, those from the common cold and influenza, do not confer any long-lasting immunity. Such infections may give temporary resistance but do not give long-term immunity upon recovery from infection, and individuals become susceptible again.

We have the model:

${\begin{aligned}{\frac {dS}{dt}}&=-{\frac {\beta SI}{N}}+\gamma I\\[6pt]{\frac {dI}{dt}}&={\frac {\beta SI}{N}}-\gamma I\end{aligned}}$

Note that denoting with *N* the total population it holds that:

${\frac {dS}{dt}}+{\frac {dI}{dt}}=0\Rightarrow S(t)+I(t)=N$

.

It follows that:

${\frac {dI}{dt}}=(\beta -\gamma )I-{\frac {\beta }{N}}I^{2}$

,

i.e. the dynamics of infectious is ruled by a logistic function, so that $\forall I(0)>0$ :

${\begin{aligned}&{\frac {\beta }{\gamma }}\leq 1\Rightarrow \lim _{t\to +\infty }I(t)=0,\\[6pt]&{\frac {\beta }{\gamma }}>1\Rightarrow \lim _{t\to +\infty }I(t)=\left(1-{\frac {\gamma }{\beta }}\right)N.\end{aligned}}$

It is possible to find an analytical solution to this model (by making a transformation of variables: $I=y^{-1}$ and substituting this into the mean-field equations), such that the basic reproduction rate is greater than unity. The solution is given as

$I(t)={\frac {I_{\infty }}{1+Ve^{-\chi t}}}$

.

where $I_{\infty }=(1-\gamma /\beta )N$ is the endemic infectious population, $\chi =\beta -\gamma$ , and $V=I_{\infty }/I_{0}-1$ . As the system is assumed to be closed, the susceptible population is then $S(t)=N-I(t)$ .

Whenever the integer nature of the number of agents is evident (populations with fewer than tens of thousands of individuals), inherent fluctuations in the disease spreading process caused by discrete agents result in uncertainties. In this scenario, the evolution of the disease predicted by compartmental equations deviates significantly from the observed results. These uncertainties may even cause the epidemic to end earlier than predicted by the compartmental equations.

As a special case, one obtains the usual logistic function by assuming $\gamma =0$ . This can be also considered in the SIR model with $R=0$ , i.e. no removal will take place. That is the *SI model*. The differential equation system using $S=N-I$ thus reduces to:

${\frac {dI}{dt}}\propto I\cdot (N-I).$

In the long run, in the SI model, all individuals will become infected.

### SIRD model

The *Susceptible-Infectious-Recovered-Deceased model* differentiates between *Recovered* (meaning specifically individuals having survived the disease and now immune) and *Deceased*. The SIRD model has semi analytical solutions based on the four parts method. This model uses the following system of differential equations:

${\begin{aligned}&{\frac {dS}{dt}}=-{\frac {\beta IS}{N}},\\[6pt]&{\frac {dI}{dt}}={\frac {\beta IS}{N}}-\gamma I-\mu I,\\[6pt]&{\frac {dR}{dt}}=\gamma I,\\[6pt]&{\frac {dD}{dt}}=\mu I,\end{aligned}}$

where $\beta ,\gamma ,\mu$ are the rates of infection, recovery, and mortality, respectively.

### SIRV model

The *Susceptible-Infectious-Recovered-Vaccinated model* is an extended SIR model that accounts for vaccination of the susceptible population. This model uses the following system of differential equations:

${\begin{aligned}&{\frac {dS}{dt}}=-{\frac {\beta (t)IS}{N}}-v(t)S,\\[6pt]&{\frac {dI}{dt}}={\frac {\beta (t)IS}{N}}-\gamma (t)I,\\[6pt]&{\frac {dR}{dt}}=\gamma (t)I,\\[6pt]&{\frac {dV}{dt}}=v(t)S,\end{aligned}}$

where $\beta ,\gamma ,v$ are the rates of infection, recovery, and vaccination, respectively. For the semi-time initial conditions $S(0)=(1-\eta )N$ , $I(0)=\eta N$ , $R(0)=V(0)=0$ and constant ratios $k=\gamma (t)/\beta (t)$ and $b=v(t)/\beta (t)$ the model had been solved approximately. The occurrence of a pandemic outburst requires $k+b<1-2\eta$ and there is a critical reduced vaccination rate $b_{c}$ beyond which the steady-state size $S_{\infty }$ of the susceptible compartment remains relatively close to $S(0)$ . Arbitrary initial conditions satisfying $S(0)+I(0)+R(0)+V(0)=N$ can be mapped to the solved special case with $R(0)=V(0)=0$ .

The numerical solution of this model to calculate the real-time reproduction number $R_{t}$ of COVID-19 can be practiced based on information from the different populations in a community. Numerical solution is a commonly used method to analyze complicated kinetic networks when the analytical solution is difficult to obtain or limited by requirements such as boundary conditions or special parameters. It uses recursive equations to calculate the next step by converting the numerical integration into Riemann sum of discrete time steps e.g., use yesterday's principal and interest rate to calculate today's interest which assumes the interest rate is fixed during the day. The calculation contains projected errors if the analytical corrections on the numerical step size are not included, e.g. when the interest rate of annual collection is simplified to 12 times the monthly rate, a projected error is introduced. Thus the calculated results will carry accumulative errors when the time step is far away from the reference point and a convergence test is needed to estimate the error. However, this error is usually acceptable for data fitting. When fitting a set of data with a close time step, the error is relatively small because the reference point is nearby compared to when predicting a long period of time after a reference point. Once the real-time $R_{t}$ is pulled out, one can compare it to the basic reproduction number $R_{0}$ . Before the vaccination, $R_{t}$ gives the policy maker and general public a measure of the efficiency of social mitigation activities such as social distancing and face masking simply by dividing ${\frac {R_{t}}{R_{0}}}$ . Under massive vaccination, the goal of disease control is to reduce the effective reproduction number $R_{e}={\frac {R_{t}S}{N}}<1$ , where S is the number of susceptible population at the time and N is the total population. When $R_{e}<1$ , the spreading decays and daily infected cases go down.

### SIRVD model

The *susceptible-infected-recovered-vaccinated-deceased* (SIRVD) epidemic compartment model extends the SIR model to include the effects of vaccination campaigns and time-dependent fatality rates on epidemic outbreaks. It encompasses the SIR, SIRV, SIRD, and SI models as special cases, with individual time-dependent rates governing transitions between different fractions. This model uses the following system of differential equations for the population fractions $S,I,R,V,D$ :

${\begin{aligned}&{\frac {dS}{dt}}=-a(t)SI-v(t)S,\\[6pt]&{\frac {dI}{dt}}=a(t)SI-\mu (t)I-\psi (t)I,\\[6pt]&{\frac {dR}{dt}}=\mu (t)I,\\[6pt]&{\frac {dV}{dt}}=v(t)S,\\[6pt]&{\frac {dD}{dt}}=\psi (t)I\end{aligned}}$

where $a(t),v(t),\mu (t),\psi (t)$ are the infection, vaccination, recovery, and fatality rates, respectively. For the semi-time initial conditions $S(0)=1-\eta$ , $I(0)=\eta$ , $R(0)=V(0)=D(0)=0$ and constant ratios $k=\mu (t)/a(t)$ , $b=v(t)/a(t)$ , and $q=\psi (t)/a(t)$ the model had been solved approximately, and exactly for some special cases, irrespective of the functional form of $a(t)$ . This is achieved upon rewriting the above SIRVD model equations in equivalent, but reduced form

${\begin{aligned}&{\frac {dS}{d\tau }}=-SI-b(\tau )S,\\[6pt]&{\frac {dI}{d\tau }}=SI-[k(\tau )+q(\tau )]I,\\[6pt]&{\frac {dR}{d\tau }}=k(\tau )I,\\[6pt]&{\frac {dV}{d\tau }}=b(\tau )S,\\[6pt]&{\frac {dD}{d\tau }}=q(\tau )S\end{aligned}}$

where

$\tau (t)=\int _{0}^{t}a(\xi )d\xi$

is a reduced, dimensionless time. The temporal dependence of the infected fraction $I(\tau )$ and the rate of new infections $j(\tau )=S(\tau )I(\tau )$ differs when considering the effects of vaccinations and when the real-time dependence of fatality and recovery rates diverge. These differences have been highlighted for stationary ratios and gradually decreasing fatality rates. The case of stationary ratios allows one to construct a diagnostics method to extract analytically all SIRVD model parameters from measured COVID-19 data of a completed pandemic wave.

### SIRVB model

The SIRVB model adds a breakthrough pathway in the SIRV model.

The kinetic equations become:

${\begin{aligned}&{\frac {dS}{dt}}=-a(t)SI-v(t)S+b(t)[\mu (t)I+v(t)S],\\[6pt]&{\frac {dI}{dt}}=a(t)SI-\mu (t)I,\\[6pt]&{\frac {dR}{dt}}=[1-b(t)]\mu (t)I,\\[6pt]&{\frac {dV}{dt}}=[1-b(t)]v(t)S,\\[6pt]\end{aligned}}$

where infection rate $a(t)$ can be write as $\beta (t)/N$ , recovery rate $\mu (t)$ can be simplified to a constant $\gamma$ , $v(t)$ is the vaccination rate, $b(t)$ is the break through ratio or fraction of immuned people susceptible to reinfection (<1).

### MSIR model

For many infections, including measles, babies are not born into the susceptible compartment but are immune to the disease for the first few months of life due to protection from maternal antibodies (passed across the placenta and additionally through colostrum). This is called passive immunity. This added detail can be shown by including an M class (for maternally derived immunity) at the beginning of the model.

To indicate this mathematically, an additional compartment is added, *M*(*t*)*.* This results in the following differential equations:

${\begin{aligned}{\frac {dM}{dt}}&=\Lambda -\delta M-\mu M\\[8pt]{\frac {dS}{dt}}&=\delta M-{\frac {\beta SI}{N}}-\mu S\\[8pt]{\frac {dI}{dt}}&={\frac {\beta SI}{N}}-\gamma I-\mu I\\[8pt]{\frac {dR}{dt}}&=\gamma I-\mu R\end{aligned}}$

### Carrier state

Some people who have had an infectious disease such as tuberculosis never completely recover and continue to carry the infection, whilst not suffering the disease themselves. They may then move back into the infectious compartment and suffer symptoms (as in tuberculosis) or they may continue to infect others in their carrier state, while not suffering symptoms. The most famous example of this is probably Mary Mallon, who infected 22 people with typhoid fever. The carrier compartment is labelled C.

(A simple modification of previous image by Viki Male to make the word "Carrier" plainly visible.)

### SEIR model

For many important infections, there is a significant latency period during which individuals have been infected but are not yet infectious themselves. During this period the individual is in compartment *E* (for exposed).

Assuming that the latency period is a random variable with exponential distribution with parameter a (i.e. the average latency period is $a^{-1}$ ), and also assuming the presence of vital dynamics with birth rate $\Lambda$ equal to death rate $N\mu$ (so that the total number N is constant), we have the model:

${\begin{aligned}{\frac {dS}{dt}}&=\mu N-\mu S-{\frac {\beta IS}{N}}\\[8pt]{\frac {dE}{dt}}&={\frac {\beta IS}{N}}-(\mu +a)E\\[8pt]{\frac {dI}{dt}}&=aE-(\gamma +\mu )I\\[8pt]{\frac {dR}{dt}}&=\gamma I-\mu R.\end{aligned}}$

We have $S+E+I+R=N,$ but this is only constant because of the simplifying assumption that birth and death rates are equal; in general N is a variable.

For this model, the basic reproduction number is:

$R_{0}={\frac {a}{\mu +a}}{\frac {\beta }{\mu +\gamma }}.$

Similarly to the SIR model, also, in this case, we have a Disease-Free-Equilibrium (*N*,0,0,0) and an Endemic Equilibrium EE, and one can show that, independently from biologically meaningful initial conditions

$\left(S(0),E(0),I(0),R(0)\right)\in \left\{(S,E,I,R)\in [0,N]^{4}:S\geq 0,E\geq 0,I\geq 0,R\geq 0,S+E+I+R=N\right\}$

it holds that:

$R_{0}\leq 1\Rightarrow \lim _{t\to +\infty }\left(S(t),E(t),I(t),R(t)\right)=DFE=(N,0,0,0),$

$R_{0}>1,I(0)>0\Rightarrow \lim _{t\to +\infty }\left(S(t),E(t),I(t),R(t)\right)=EE.$

In case of periodically varying contact rate $\beta (t)$ the condition for the global attractiveness of DFE is that the following linear system with periodic coefficients:

${\begin{aligned}{\frac {dE_{1}}{dt}}&=\beta (t)I_{1}-(\gamma +a)E_{1}\\[8pt]{\frac {dI_{1}}{dt}}&=aE_{1}-(\gamma +\mu )I_{1}\end{aligned}}$

is stable (i.e. it has its Floquet's eigenvalues inside the unit circle in the complex plane).

### SEIS model

The SEIS model is like the SEIR model (above) except that no immunity is acquired at the end.

${\color {blue}{{\mathcal {S}}\to {\mathcal {E}}\to {\mathcal {I}}\to {\mathcal {S}}}}$

In this model an infection does not leave any immunity thus individuals that have recovered return to being susceptible, moving back into the *S*(*t*) compartment. The following differential equations describe this model:

${\begin{aligned}{\frac {dS}{dt}}&=\Lambda -{\frac {\beta SI}{N}}-\mu S+\gamma I\\[6pt]{\frac {dE}{dt}}&={\frac {\beta SI}{N}}-(\epsilon +\mu )E\\[6pt]{\frac {dI}{dt}}&=\varepsilon E-(\gamma +\mu )I\end{aligned}}$

### MSEIR model

For the case of a disease, with the factors of passive immunity, and a latency period there is the MSEIR model.

$\color {blue}{{\mathcal {M}}\to {\mathcal {S}}\to {\mathcal {E}}\to {\mathcal {I}}\to {\mathcal {R}}}$

${\begin{aligned}{\frac {dM}{dt}}&=\Lambda -\delta M-\mu M\\[6pt]{\frac {dS}{dt}}&=\delta M-{\frac {\beta SI}{N}}-\mu S\\[6pt]{\frac {dE}{dt}}&={\frac {\beta SI}{N}}-(\varepsilon +\mu )E\\[6pt]{\frac {dI}{dt}}&=\varepsilon E-(\gamma +\mu )I\\[6pt]{\frac {dR}{dt}}&=\gamma I-\mu R\end{aligned}}$

### MSEIRS model

An MSEIRS model is similar to the MSEIR, but the immunity in the R class would be temporary, so that individuals would regain their susceptibility when the temporary immunity ended.

${\color {blue}{{\mathcal {M}}\to {\mathcal {S}}\to {\mathcal {E}}\to {\mathcal {I}}\to {\mathcal {R}}\to {\mathcal {S}}}}$

### More complex general models

When developing more detailed models for in-depth analysis, models are mostly generated for specific outbreak scenarios of specific diseases, including compartments for targeted research questions like hospitalization compartments or detection dynamics. Even though those models are often tailored for specific situations, there are complex models, still usable for a broad variety of different diseases. One of those attempts to create a general model includes twelve compartments, extending the well-known SEIR model by a second stage of infection, detection compartments, and two doses of vaccination. Additionally smear infections are incorporated via an external Pathogen P and a simplistic vector population is included by $S_{V}$ and $I_{V}$ . Moreover population dynamics like birth and death processes can be included. Such complex models enable a deeper understanding of infection dynamics and the introduction of different pharmaceutical and non-pharmaceutical interventions.

### Variable contact rates

It is well known that the probability of getting a disease is not constant in time. As a pandemic progresses, reactions to the pandemic may change the contact rates which are assumed constant in the simpler models. Counter-measures such as masks, social distancing, and lockdown will alter the contact rate in a way to reduce the speed of the pandemic.

In addition, Some diseases are seasonal, such as the common cold viruses, which are more prevalent during winter. With childhood diseases, such as measles, mumps, and rubella, there is a strong correlation with the school calendar, so that during the school holidays the probability of getting such a disease dramatically decreases. As a consequence, for many classes of diseases, one should consider a force of infection with periodically ('seasonal') varying contact rate

$F=\beta (t){\frac {I}{N}},\quad \beta (t+T)=\beta (t)$

with period T equal to one year.

Thus, our model becomes

${\begin{aligned}{\frac {dS}{dt}}&=\mu N-\mu S-\beta (t){\frac {I}{N}}S\\[8pt]{\frac {dI}{dt}}&=\beta (t){\frac {I}{N}}S-(\gamma +\mu )I\end{aligned}}$

(the dynamics of recovered easily follows from $R=N-S-I$ ), i.e. a nonlinear set of differential equations with periodically varying parameters. It is well known that this class of dynamical systems may undergo very interesting and complex phenomena of nonlinear parametric resonance. It is easy to see that if:

${\frac {1}{T}}\int _{0}^{T}{\frac {\beta (t)}{\mu +\gamma }}\,dt<1\Rightarrow \lim _{t\to +\infty }(S(t),I(t))=DFE=(N,0),$

whereas if the integral is greater than one the disease will not die out and there may be such resonances. For example, considering the periodically varying contact rate as the 'input' of the system one has that the output is a periodic function whose period is a multiple of the period of the input. This allowed to give a contribution to explain the poly-annual (typically biennial) epidemic outbreaks of some infectious diseases as interplay between the period of the contact rate oscillations and the pseudo-period of the damped oscillations near the endemic equilibrium. Remarkably, in some cases, the behavior may also be quasi-periodic or even chaotic.

### SIR model with diffusion

Spatiotemporal compartmental models describe not the total number, but the density of susceptible/infective/recovered persons. Consequently, they also allow to model the distribution of infected persons in space. In most cases, this is done by combining the SIR model with a diffusion equation

${\begin{aligned}&\partial _{t}S=D_{S}\nabla ^{2}S-{\frac {\beta IS}{N}},\\[6pt]&\partial _{t}I=D_{I}\nabla ^{2}I+{\frac {\beta IS}{N}}-\gamma I,\\[6pt]&\partial _{t}R=D_{R}\nabla ^{2}R+\gamma I,\end{aligned}}$

where $D_{S}$ , $D_{I}$ and $D_{R}$ are diffusion constants. Thereby, one obtains a reaction-diffusion equation. (Note that, for dimensional reasons, the parameter $\beta$ has to be changed compared to the simple SIR model.) Early models of this type have been used to model the spread of the black death in Europe. Extensions of this model have been used to incorporate, e.g., effects of nonpharmaceutical interventions such as social distancing.

### Interacting Subpopulation SEIR Model

As social contacts, disease severity and lethality, as well as the efficacy of prophylactic measures may differ substantially between interacting subpopulations, e.g., the elderly versus the young, separate SEIR models for each subgroup may be used that are mutually connected through interaction links. Such Interacting Subpopulation SEIR models have been used for modeling the COVID-19 pandemic at continent scale to develop personalized, accelerated, subpopulation-targeted vaccination strategies that promise a shortening of the pandemic and a reduction of case and death counts in the setting of limited access to vaccines during a wave of virus Variants of Concern.

### SIR Model on Networks

The SIR model has been studied on networks of various kinds in order to model a more realistic form of connection than the homogeneous mixing condition which is usually required. A simple model for epidemics on networks in which an individual has a probability p of being infected by each of his infected neighbors in a given time step leads to results similar to giant component formation on Erdos Renyi random graphs. A stochastic compartment model with a transmission pathway via vectors has been developed recently in which a multiple random walkers approach is implemented to investigate the spreading dynamics in random graphs of the Watts-Strogatz and the Barabási-Albert type to mimic human mobility patterns in complex real world environments such as cities, streets, and transportation networks. This model captures the class of vector transmitted infectious diseases such as Dengue, Malaria (transmission by mosquitoes), pestilence (transmission by fleas), and others.

Dynamics of epidemics depend on how people's behavior changes in time. For example, at the beginning of the epidemic, people are ignorant and careless, then, after the outbreak of epidemics and alarm, they begin to comply with the various restrictions and the spreading of epidemics may decline. Over time, some people get tired/frustrated by the restrictions and stop following them (exhaustion), especially if the number of new cases drops down. After resting for some time, they can follow the restrictions again. But during this pause the second wave can come and become even stronger than the first one. Social dynamics should be considered. The social physics models of social stress complement the classical epidemics models.

The simplest SIR-social stress (SIRSS) model is organised as follows. The susceptible individuals (S) can be split in three subgroups by the types of behavior: ignorant or unaware of the epidemic (Sign), rationally resistant (Sres), and exhausted (Sexh) that do not react on the external stimuli (this is a sort of refractory period). In other words: S(t) = Sign(t) + Sres(t) + Sexh(t). Symbolically, the social stress model can be presented by the "reaction scheme" (where I denotes the infected individuals):

- ${\color {blue}{{\mathcal {S_{ign}}}+2{\mathcal {I}}\to {\mathcal {S_{res}}}+2{\mathcal {I}}}}$ – *mobilization reaction* (the autocatalytic form here means that the transition rate is proportional to the square of the infected fraction I);
- ${\color {blue}{{\mathcal {S_{res}}}\to {\mathcal {S_{exh}}}}}$ – *exhaustion process* due to fatigue from anti-epidemic restrictions;
- ${\color {blue}{{\mathcal {S_{exh}}}\to {\mathcal {S_{ign}}}}}$ – *slow relaxation to the initial state* (end of the refractory period).

The main *SIR epidemic reaction*

- ${\color {blue}{{\mathcal {S_{...}}}+{\mathcal {I}}\to {\mathcal {2I}}}}$

has different reaction rate constants $\beta$ for Sign, Sres, and Sexh. Presumably, for Sres, $\beta$ is lower than for Sign and Sign.

The differences between countries are concentrated in two kinetic constants: the rate of mobilization and the rate of exhaustion calculated for COVID-19 epidemic in 13 countries. These constants for this epidemic in all countries can be extracted by the fitting of the SIRSS model to publicly available data

### KdV-SIR equation

Based on the classical SIR model, a Korteweg-de Vries (KdV)–SIR equation and its analytical solution have been proposed to illustrate the fundamental dynamics of an epidemic wave, the dependence of solutions on parameters, and the dependence of predictability horizons on various types of solutions. The KdV-SIR equation is written as follows:

${\frac {d^{2}I}{dt}}-\sigma _{o}^{2}I+{\frac {3}{2}}{\frac {\sigma _{o}^{2}}{I_{max}}}I^{2}=0$ .

Here,

$\sigma _{o}=\gamma (R_{o}-1)$ ,

$R_{o}={\frac {\beta }{\gamma }}{\frac {S_{o}}{N}}$ ,

and

$I_{max}={\frac {S_{o}}{2}}{\frac {(R_{o}-1)^{2}}{R_{o}^{2}}}$ .

$S_{o}$ indicates the initial value of the state variable S . Parameters $\sigma _{o}$ (σ-naught) and $R_{o}$ (R-naught) are the time-independent relative growth rate and basic reproduction number, respectively. $I_{max}$ presents the maximum of the state variables I (for the number of infected persons). The KdV-SIR equation shares the same form as the Korteweg–De Vries equation in the traveling wave coordinate. An analytical solution to the KdV-SIR equation is written as follows:

$I=I_{max}sech^{2}\left({\frac {\sigma _{o}}{2}}t\right)$ ,

which represents a solitary wave solution.


## Heterogeneous (structured, Bayesian) model

Modeling a full population of possibly millions people using two constants $\beta$ and $\gamma$ seem far fetched; each individual has personal characteristics that influence the propagation : immunity status, contact habits and so on. So it is interesting to know what happens if, for instance, $\beta$ and $\gamma$ are not two constants but some random variables (a pair for each individual). This procedure has several names : "heterogeneous model", "structuration" (see also below for age structured models) or "Bayesian" view. Surprising results emerge, for instance it was proved in that the number of infected at the peak of a heterogeneous epidemic is smaller than the deterministic epidemic having same average $\beta$ ; the same holds true for the total epidemic size $S(0)-S(\infty )$ and other models, e.g. SEIR.


## Modelling vaccination

The SIR model can be modified to model vaccination. Typically these introduce an additional compartment to the SIR model, V , for vaccinated individuals. Below are some examples.

### Vaccinating newborns

In presence of a communicable diseases, one of the main tasks is that of eradicating it via prevention measures and, if possible, via the establishment of a mass vaccination program. Consider a disease for which the newborn are vaccinated (with a vaccine giving lifelong immunity) at a rate $P\in (0,1)$ :

${\begin{aligned}{\frac {dS}{dt}}&=\nu N(1-P)-\mu S-\beta {\frac {I}{N}}S\\[8pt]{\frac {dI}{dt}}&=\beta {\frac {I}{N}}S-(\mu +\gamma )I\\[8pt]{\frac {dV}{dt}}&=\nu NP-\mu V\end{aligned}}$

where V is the class of vaccinated subjects. It is immediate to show that:

$\lim _{t\to +\infty }V(t)=NP,$

thus we shall deal with the long term behavior of S and I , for which it holds that:

$R_{0}(1-P)\leq 1\Rightarrow \lim _{t\to +\infty }\left(S(t),I(t)\right)=DFE=\left(N\left(1-P\right),0\right)$

$R_{0}(1-P)>1,\quad I(0)>0\Rightarrow \lim _{t\to +\infty }\left(S(t),I(t)\right)=EE=\left({\frac {N}{R_{0}(1-P)}},N\left(R_{0}(1-P)-1\right)\right).$

In other words, if

$P<P^{*}=1-{\frac {1}{R_{0}}}$

the vaccination program is not successful in eradicating the disease, on the contrary, it will remain endemic, although at lower levels than the case of absence of vaccinations. This means that the mathematical model suggests that for a disease whose basic reproduction number may be as high as 18 one should vaccinate at least 94.4% of newborns in order to eradicate the disease.

### Vaccination and information

Modern societies are facing the challenge of "rational" exemption, i.e. the family's decision to not vaccinate children as a consequence of a "rational" comparison between the perceived risk from infection and that from getting damages from the vaccine. In order to assess whether this behavior is really rational, i.e. if it can equally lead to the eradication of the disease, one may simply assume that the vaccination rate is an increasing function of the number of infectious subjects:

$P=P(I),\quad P'(I)>0.$

In such a case the eradication condition becomes:

$P(0)\geq P^{*},$

i.e. the baseline vaccination rate should be greater than the "mandatory vaccination" threshold, which, in case of exemption, cannot hold. Thus, "rational" exemption might be myopic since it is based only on the current low incidence due to high vaccine coverage, instead taking into account future resurgence of infection due to coverage decline.

### Vaccination of non-newborns

In case there also are vaccinations of non newborns at a rate ρ the equation for the susceptible and vaccinated subject has to be modified as follows:

${\begin{aligned}{\frac {dS}{dt}}&=\mu N(1-P)-\mu S-\rho S-\beta {\frac {I}{N}}S\\[8pt]{\frac {dV}{dt}}&=\mu NP+\rho S-\mu V\end{aligned}}$

leading to the following eradication condition:

$P\geq 1-\left(1+{\frac {\rho }{\mu }}\right){\frac {1}{R_{0}}}$

### Pulse vaccination strategy

This strategy repeatedly vaccinates a defined age-cohort (such as young children or the elderly) in a susceptible population over time. Using this strategy, the block of susceptible individuals is then immediately removed, making it possible to eliminate an infectious disease, (such as measles), from the entire population. Every T time units a constant fraction p of susceptible subjects is vaccinated in a relatively short (with respect to the dynamics of the disease) time. This leads to the following impulsive differential equations for the susceptible and vaccinated subjects:

${\begin{aligned}{\frac {dS}{dt}}&=\mu N-\mu S-\beta {\frac {I}{N}}S,\quad S(nT^{+})=(1-p)S(nT^{-}),&&n=0,1,2,\ldots \\[8pt]{\frac {dV}{dt}}&=-\mu V,\quad V(nT^{+})=V(nT^{-})+pS(nT^{-}),&&n=0,1,2,\ldots \end{aligned}}$

It is easy to see that by setting *I* = 0 one obtains that the dynamics of the susceptible subjects is given by:

$S^{*}(t)=1-{\frac {p}{1-(1-p)E^{-\mu T}}}E^{-\mu MOD(t,T)}$

and that the eradication condition is:

$R_{0}\int _{0}^{T}S^{*}(t)\,dt<1$

### Vaccination games

A huge literature recognizes that the vaccination can be seen as a game: in a population where everybody is vaccinated any epidemic will die off immediately so an additional person will have no interest to vaccinate at all. On the contrary, a person arriving in a population where nobody is vaccinated will have all incentives to vaccinate (the epidemic will break loose in such a population). So, it seems that the individual has interest to do the opposite of the population as a whole. But the population is the sum of all individuals, and the previous affirmation should be false. So, in fact, a Nash equilibrium is reached. Technical tools to treat such situations involve game theory or modern tools such as Mean-field game theory.


## The influence of age: age-structured models

Age has a deep influence on the disease spread rate in a population, especially the contact rate. This rate summarizes the effectiveness of contacts between susceptible and infectious subjects. Taking into account the ages of the epidemic classes $s(t,a),i(t,a),r(t,a)$ (to limit ourselves to the susceptible-infectious-removed scheme) such that:

$S(t)=\int _{0}^{a_{M}}s(t,a)\,da$

$I(t)=\int _{0}^{a_{M}}i(t,a)\,da$

$R(t)=\int _{0}^{a_{M}}r(t,a)\,da$

(where $a_{M}\leq +\infty$ is the maximum admissible age) and their dynamics is not described, as one might think, by "simple" partial differential equations, but by integro-differential equations:

$\partial _{t}s(t,a)+\partial _{a}s(t,a)=-\mu (a)s(a,t)-s(a,t)\int _{0}^{a_{M}}k(a,a_{1};t)i(a_{1},t)\,da_{1}$

$\partial _{t}i(t,a)+\partial _{a}i(t,a)=s(a,t)\int _{0}^{a_{M}}{k(a,a_{1};t)i(a_{1},t)da_{1}}-\mu (a)i(a,t)-\gamma (a)i(a,t)$

$\partial _{t}r(t,a)+\partial _{a}r(t,a)=-\mu (a)r(a,t)+\gamma (a)i(a,t)$

where:

$F(a,t,i(\cdot ,\cdot ))=\int _{0}^{a_{M}}k(a,a_{1};t)i(a_{1},t)\,da_{1}$

is the force of infection, which, of course, will depend, though the contact kernel $k(a,a_{1};t)$ on the interactions between the ages.

Complexity is added by the initial conditions for newborns (i.e. for a=0), that are straightforward for infectious and removed:

$i(t,0)=r(t,0)=0$

but that are nonlocal for the density of susceptible newborns:

$s(t,0)=\int _{0}^{a_{M}}\left(\varphi _{s}(a)s(a,t)+\varphi _{i}(a)i(a,t)+\varphi _{r}(a)r(a,t)\right)\,da$

where $\varphi _{j}(a),j=s,i,r$ are the fertilities of the adults.

Moreover, defining now the density of the total population $n(t,a)=s(t,a)+i(t,a)+r(t,a)$ one obtains:

$\partial _{t}n(t,a)+\partial _{a}n(t,a)=-\mu (a)n(a,t)$

In the simplest case of equal fertilities in the three epidemic classes, we have that in order to have demographic equilibrium the following necessary and sufficient condition linking the fertility $\varphi (.)$ with the mortality $\mu (a)$ must hold:

$1=\int _{0}^{a_{M}}\varphi (a)\exp \left(-\int _{0}^{a}{\mu (q)dq}\right)\,da$

and the demographic equilibrium is

$n^{*}(a)=C\exp \left(-\int _{0}^{a}\mu (q)\,dq\right),$

automatically ensuring the existence of the disease-free solution:

$DFS(a)=(n^{*}(a),0,0).$

A basic reproduction number can be calculated as the spectral radius of an appropriate functional operator.

### Next-generation method

One way to calculate $R_{0}$ is to average the expected number of new infections over all possible infected types. The next-generation method is a general method of deriving $R_{0}$ when more than one class of infectives is involved. This method, originally introduced by Diekmann *et al*. (1990), can be used for models with underlying age structure or spatial structure, among other possibilities. In this picture, the spectral radius of the next-generation matrix G gives the basic reproduction number, $R_{0}=\rho (G).$

Consider a sexually transmitted disease. In a naive population where almost everyone is susceptible, but the infection seed, if the expected number of gender 1 is f and the expected number of infected gender 2 is m , we can know how many would be infected in the next-generation. Such that the *next-generation matrix* G can be written as: $G={\begin{pmatrix}0&f\\m&0\end{pmatrix}},$ where each element $g_{ij}$ is the expected number of secondary infections of gender i caused by a single infected individual of gender j , assuming that the population of gender i is entirely susceptible. Diagonal elements are zero because people of the same gender cannot transmit the disease to each other but, for example, each f can transmit the disease to m , on average. Meaning that each element $g_{ij}$ is a reproduction number, but one where who infects whom is accounted for. If generation a is represented with $\phi _{a}$ then the next generation $\phi _{a+1}$ would be $G\phi _{a}$ .

The spectral radius of the next-generation matrix is the basic reproduction number, $R_{0}=\rho (G)={\sqrt {mf}}$ , that is here, the geometric mean of the expected number of each gender in the next-generation. Note that multiplication factors f and m alternate because, the infectious person has to 'pass through' a second gender before it can enter a new host of the first gender. In other words, it takes two generations to get back to the same type, and every two generations numbers are multiplied by m × f . The average per generation multiplication factor is therefore ${\sqrt {mf}}$ . Note that G is a non-negative matrix so it has single, unique, positive, real eigenvalue which is strictly greater than all the others.

### Next-generation matrix for compartmental models

In mathematical modelling of infectious disease, the dynamics of spreading is usually described through a set of non-linear ordinary differential equations (ODE). So there is always n coupled equations of form ${\dot {C_{i}}}={\operatorname {d} \!C_{i} \over \operatorname {d} \!t}=f(C_{1},C_{2},...,C_{n})$ which shows how the number of people in compartment $C_{i}$ changes over time. For example, in a SIR model, $C_{1}=S$ , $C_{2}=I$ , and $C_{3}=R$ . Compartmental models have a disease-free equilibrium (DFE) meaning that it is possible to find an equilibrium while setting the number of infected people to zero, $I=0$ . In other words, as a rule, there is an infection-free steady state. This solution, also usually ensures that the disease-free equilibrium is also an equilibrium of the system. There is another fixed point known as an Endemic Equilibrium (EE) where the disease is not totally eradicated and remains in the population. Mathematically, $R_{0}$ is a threshold for stability of a disease-free equilibrium such that:

$R_{0}\leq 1\Rightarrow \lim _{t\to \infty }(C_{1}(t),C_{2}(t),\cdots ,C_{n}(t))={\textrm {DFE}}$

$R_{0}>1,I(0)>0\Rightarrow \lim _{t\to \infty }(C_{1}(t),C_{2}(t),\cdots ,C_{n}(t))={\textrm {EE}}.$

To calculate $R_{0}$ , the first step is to linearise around the disease-free equilibrium (DFE), but for the infected subsystem of non-linear ODEs which describe the production of new infections and changes in state among infected individuals. Epidemiologically, the linearisation reflects that $R_{0}$ characterizes the potential for initial spread of an infectious person in a naive population, assuming the change in the susceptible population is negligible during the initial spread. A linear system of ODEs can always be described by a matrix. So, the next step is to construct a linear positive operator that provides the next generation of infected people when applied to the present generation. Note that this operator (matrix) is responsible for the number of infected people, not all the compartments. Iteration of this operator describes the initial progression of infection within the heterogeneous population. So comparing the spectral radius of this operator to unity determines whether the generations of infected people grow or not. $R_{0}$ can be written as a product of the infection rate near the disease-free equilibrium and average duration of infectiousness. It is used to find the peak and final size of an epidemic.

#### The SEIR model with vital dynamics and constant population

As described in the example above, so many epidemic processes can be described with a SIR‌ model. However, for many important infections, such as COVID-19, there is a significant latency period during which individuals have been infected but are not yet infectious themselves. During this period the individual is in compartment *E* (for exposed). Here, the formation of the next-generation matrix from the SEIR‌ model involves determining two compartments, infected and non-infected, since they are the populations that spread the infection. So we only need to model the exposed, ***E***, and infected, ***I***, compartments. Consider a population characterized by a death rate $\mu$ and birth rate $\lambda$ where a communicable disease is spreading. As in the previous example, we can use the transition rates between the compartments per capita such that $\beta$ be the infection rate, $\gamma$ be the recovery rate, and $\kappa$ be the rate at which a latent individual becomes infectious. Then, we can define the model dynamics using the following equations:

${\begin{cases}{\dot {S}}=\lambda -\mu S-\beta SI,\\\\{\dot {E}}=\beta SI-(\mu +\kappa )E,\\\\{\dot {I}}=\kappa E-(\mu +\gamma )I,\\\\{\dot {R}}=\gamma I-\mu R.\end{cases}}$ Here we have 4 compartments and we can define vector $\mathrm {x} =(S,E,I,R)$ where $\mathrm {x} _{i}$ denotes the number or proportion of individuals in the *i*-th compartment. Let $F_{i}(\mathrm {x} )$ be the rate of appearance of new infections in compartment *i* such that it includes only infections that are newly arising, but does not include terms which describe the transfer of infectious individuals from one infected compartment to another. Then if $V_{i}^{+}$ is the rate of transfer of individuals into compartment *i* by all other means and $V_{i}^{-}$ is the rate of transfer of individuals out of the *i*-th compartment, then the difference $F_{i}(\mathrm {x} )-V_{i}(\mathrm {x} )$ gives the rate of change of such that $V_{i}(\mathrm {x} )=V_{i}^{-}(\mathrm {x} )-V_{i}^{+}(\mathrm {x} )$ .

We can now make matrices of partial derivatives of *F* and *V* such that

$F_{ij}={\partial \!\ F_{i}(\mathrm {x} ^{*}) \over \partial \!\ \mathrm {x} _{j}}$ and $V_{ij}={\partial \!\ V_{i}(\mathrm {x} ^{*}) \over \partial \!\ \mathrm {x} _{j}}$ , where $\mathrm {x} ^{*}=(S^{*},E^{*},I^{*},R^{*})=(\lambda /\mu ,0,0,0)$ is the disease-free equilibrium.

We now can form the next-generation matrix (operator) $G=FV^{-1}$ . Basically, F is a non-negative matrix which represents the infection rates near the equilibrium, and V is an M-matrix for linear transition terms making $V^{-1}$ a matrix which represents the average duration of infectiousness. Therefore, $G_{ij}$ gives the rate at which infected individuals in *$\mathrm {x} _{j}$* produce new infections in *$\mathrm {x} _{i}$*, times the average length of time an individual spends in a single visit to compartment *$j.$*

Finally, for this SEIR process we can have:

$F={\begin{pmatrix}0&\beta S^{*}\\0&0\end{pmatrix}}$ and $V={\begin{pmatrix}\mu +\kappa &0\\-\kappa &\gamma +\mu \end{pmatrix}}$ and so $R_{0}=\rho (FV^{-1})={\frac {\kappa \beta S^{*}}{(\mu +\kappa )(\mu +\gamma )}}.$


## Estimation methods

The basic reproduction number can be estimated through examining detailed transmission chains or through genomic sequencing. However, it is most frequently calculated using epidemiological models. During an epidemic, typically the number of diagnosed infections $N(t)$ over time t is known. In the early stages of an epidemic, growth is exponential, with a logarithmic growth rate $K:={\frac {d\ln(N)}{dt}}.$ For exponential growth, N can be interpreted as the cumulative number of diagnoses (including individuals who have recovered) or the present number of infection cases; the logarithmic growth rate is the same for either definition. In order to estimate $R_{0}$ , assumptions are necessary about the time delay between infection and diagnosis and the time between infection and starting to be infectious.

In exponential growth, K is related to the doubling time $T_{d}$ as $K={\frac {\ln(2)}{T_{d}}}.$

### Simple model

If an individual, after getting infected, infects exactly $R_{0}$ new individuals only after exactly a time $\tau$ (the serial interval) has passed, then the number of infectious individuals over time grows as $n_{E}(t)=n_{E}(0)\,R_{0}^{t/\tau }=n_{E}(0)\,e^{Kt}$ or $\ln(n_{E}(t))=\ln(n_{E}(0))+\ln(R_{0})t/\tau .$ The underlying matching differential equation is ${\frac {dn_{E}(t)}{dt}}=n_{E}(t){\frac {\ln(R_{0})}{\tau }}.$ or ${\frac {d\ln(n_{E}(t))}{dt}}={\frac {\ln(R_{0})}{\tau }}.$ In this case, $R_{0}=e^{K\tau }$ or $K={\frac {\ln R_{0}}{\tau }}$ .

For example, with $\tau =5~\mathrm {d}$ and $K=0.183~\mathrm {d} ^{-1}$ , we would find $R_{0}=2.5$ .

If $R_{0}$ is time dependent $\ln(n_{E}(t))=\ln(n_{E}(0))+{\frac {1}{\tau }}\int \limits _{0}^{t}\ln(R_{0}(t))dt$ showing that it may be important to keep $\ln(R_{0})$ below 0, time-averaged, to avoid exponential growth.

### Latent infectious period, isolation after diagnosis

In this model, an individual infection has the following stages:

1. Exposed: an individual is infected, but has no symptoms and does not yet infect others. The average duration of the exposed state is $\tau _{E}$ .
2. Latent infectious: an individual is infected, has no symptoms, but does infect others. The average duration of the latent infectious state is $\tau _{I}$ . The individual infects $R_{0}$ other individuals during this period.
3. Isolation after diagnosis: measures are taken to prevent further infections, for example by isolating the infected person.

This is a SEIR model and $R_{0}$ may be written in the following form $R_{0}=1+K(\tau _{E}+\tau _{I})+K^{2}\tau _{E}\tau _{I}.$ This estimation method has been applied to COVID-19 and SARS. It follows from the differential equation for the number of exposed individuals $n_{E}$ and the number of latent infectious individuals $n_{I}$ , ${\frac {d}{dt}}{\begin{pmatrix}n_{E}\\n_{I}\end{pmatrix}}={\begin{pmatrix}-1/\tau _{E}&R_{0}/\tau _{I}\\1/\tau _{E}&-1/\tau _{I}\end{pmatrix}}{\begin{pmatrix}n_{E}\\n_{I}\end{pmatrix}}.$ The largest eigenvalue of the matrix is the logarithmic growth rate K , which can be solved for $R_{0}$ .

In the special case $\tau _{I}=0$ , this model results in $R_{0}=1+K\tau _{E}$ , which is different from the simple model above ( $R_{0}=\exp(K\tau _{E})$ ). For example, with the same values $\tau =5~\mathrm {d}$ and $K=0.183~\mathrm {d} ^{-1}$ , we would find $R_{0}=1.9$ , rather than the true value of $2.5$ . The difference is due to a subtle difference in the underlying growth model; the matrix equation above assumes that newly infected patients are currently already contributing to infections, while in fact infections only occur due to the number infected at $\tau _{E}$ ago. A more correct treatment would require the use of delay differential equations.

Latent period is the transition time between contagion event and disease manifestation. In cases of diseases with varying latent periods, the basic reproduction number can be calculated as the sum of the reproduction numbers for each transition time into the disease. An example of this is tuberculosis (TB). Blower and coauthors calculated from a simple model of TB the following reproduction number: $R_{0}=R_{0}^{\text{FAST}}+R_{0}^{\text{SLOW}}$ In their model, it is assumed that the infected individuals can develop active TB by either direct progression (the disease develops immediately after infection) considered above as FAST tuberculosis or endogenous reactivation (the disease develops years after the infection) considered above as SLOW tuberculosis.


## Other considerations within compartmental epidemic models

### Vertical transmission

In the case of some diseases such as AIDS and hepatitis B, it is possible for the offspring of infected parents to be born infected. This transmission of the disease down from the mother is referred to as vertical transmission. The influx of additional members into the infected category can be considered within the model by including a fraction of the newborn members in the infected compartment.

### Vector transmission

Diseases transmitted from human to human indirectly, i.e. malaria spread by way of mosquitoes, are transmitted through a vector. In these cases, the infection transfers from human to insect and an epidemic model must include both species, generally requiring many more compartments than a model for direct transmission.

### Others

Other occurrences which may need to be considered when modeling an epidemic include things such as the following:

- Non-homogeneous mixing
- Variable infectivity
- Distributions that are spatially non-uniform
- Diseases caused by macroparasites


## Deterministic versus stochastic epidemic models

The deterministic models presented here are valid only in case of sufficiently large populations, and as such should be used cautiously. These models are only valid in the thermodynamic limit, where the population is effectively infinite. In stochastic models, the long-time endemic equilibrium derived above, does not hold, as there is a finite probability that the number of infected individuals drops below one in a system. In a true system then, the pathogen may not propagate, as no host will be infected. But, in deterministic mean-field models, the number of infected can take on real, namely, non-integer values of infected hosts, and the number of hosts in the model can be less than one, but more than zero, thereby allowing the pathogen in the model to propagate. The reliability of compartmental models is limited to compartmental applications.

One of the possible extensions of mean-field models considers the spreading of epidemics on a network based on percolation theory concepts. Stochastic epidemic models have been studied on different networks and more recently applied to the COVID-19 pandemic.
