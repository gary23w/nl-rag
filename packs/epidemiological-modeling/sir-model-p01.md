---
title: "Compartmental models (epidemiology) (part 1/2)"
source: https://en.wikipedia.org/wiki/SIR_model
domain: epidemiological-modeling
license: CC-BY-SA-4.0
tags: epidemiological modeling, compartmental models epidemiology, basic reproduction number, next-generation matrix
fetched: 2026-07-02
part: 1/2
---

# Compartmental models (epidemiology)

(Redirected from

SIR model

)

**Compartmental models** are a mathematical framework used to simulate how populations move between different states or "compartments". While widely applied in various fields, they have become particularly fundamental to the mathematical modelling of infectious diseases. In these models, the population is divided into compartments labeled with shorthand notation – most commonly **S**, **I**, and **R**, representing **S**usceptible, **I**nfectious, and **R**ecovered individuals. The sequence of letters typically indicates the flow patterns between compartments; for example, an SEIS model represents progression from susceptible to exposed to infectious and then back to susceptible again.

These models originated in the early 20th century through pioneering epidemiological work by several mathematicians. Key developments include Hamer's work in 1906, Ross's contributions in 1916, collaborative work by Ross and Hudson in 1917, the seminal Kermack and McKendrick model in 1927, and Kendall's work in 1956. The historically significant Reed–Frost model, though often overlooked, also substantially influenced modern epidemiological modeling approaches.

Most implementations of compartmental models use ordinary differential equations (ODEs), providing deterministic results that are mathematically tractable. However, they can also be formulated within stochastic frameworks that incorporate randomness, offering more realistic representations of population dynamics at the cost of greater analytical complexity.

Epidemiologists and public health officials use these models for several critical purposes: analyzing disease transmission dynamics, projecting the total number of infections and recoveries over time, estimating key epidemiological parameters such as the basic reproduction number (R0) or effective reproduction number (Rt), evaluating potential impacts of different public health interventions before implementation, and informing evidence-based policy decisions during disease outbreaks. Beyond infectious disease modeling, the approach has been adapted for applications in population ecology, pharmacokinetics, chemical kinetics, and other fields requiring the study of transitions between defined states. For such investigations and to consult decision makers, often more complex models are used.


## SIR model

The **SIR model** is one of the simplest compartmental models, and many models are derivatives of this basic form. The model consists of three compartments:

S

: The number of

s

usceptible individuals. When a susceptible and an infectious individual come into "infectious contact", the susceptible individual contracts the disease and transitions to the infectious compartment.

I

: The number of

i

nfectious individuals. These are individuals who have been infected and are capable of infecting susceptible individuals.

R

for the number of

r

emoved (and immune) or deceased individuals. These are individuals who have been infected and have either recovered from the disease and entered the removed compartment, or died. It is assumed that the number of deaths is negligible with respect to the total population. This compartment may also be called "

r

ecovered" or "

r

esistant".

This model is reasonably predictive for infectious diseases that are transmitted from human to human, and where recovery confers lasting resistance, such as measles, mumps, and rubella.

These variables (**S**, **I**, and **R**) represent the number of people in each compartment at a particular time. To represent that the number of susceptible, infectious, and removed individuals may vary over time (even if the total population size remains constant), we make the precise numbers a function of *t* (time): **S**(*t*), **I**(*t*), and **R**(*t*). For a specific disease in a specific population, these functions may be worked out in order to predict possible outbreaks and bring them under control. Note that in the SIR model, $R(0)$ and $R_{0}$ are different quantities – the former describes the number of recovered at *t* = 0 whereas the latter describes the ratio between the frequency of contacts to the frequency of recovery.

As implied by the variable function of *t*, the model is dynamic in that the numbers in each compartment may fluctuate over time. The importance of this dynamic aspect is most obvious in an endemic disease with a short infectious period, such as measles in the UK prior to the introduction of a vaccine in 1968. Such diseases tend to occur in cycles of outbreaks due to the variation in number of susceptibles (S(*t*)) over time. During an epidemic, the number of susceptible individuals falls rapidly as more of them are infected and thus enter the infectious and removed compartments. The disease cannot break out again until the number of susceptibles has built back up, e.g. as a result of offspring being born into the susceptible compartment.

Each member of the population typically progresses from susceptible to infectious to recovered. This can be shown as a flow diagram in which the boxes represent the different compartments and the arrows the transition between compartments (see diagram).

### Transition rates

For the full specification of the model, the arrows should be labeled with the transition rates between compartments. Between *S* and *I*, the transition rate is assumed to be $d(S/N)/dt=-\beta SI/N^{2}$ , where N is the total population, $\beta$ is the average number of contacts per person per time, multiplied by the probability of disease transmission in a contact between a susceptible and an infectious subject, and $SI/N^{2}$ is the fraction of all possible contacts that involves an infectious and susceptible individual. (This is mathematically similar to the law of mass action in chemistry in which random collisions between molecules result in a chemical reaction and the fractional rate is proportional to the concentration of the two reactants.)

Between *I* and *R*, the transition rate is assumed to be proportional to the number of infectious individuals which is $\gamma I$ . If an individual is infectious for an average time period D , then $\gamma =1/D$ . This is also equivalent to the assumption that the length of time spent by an individual in the infectious state is a random variable with an exponential distribution. The "classical" SIR model may be modified by using more complex and realistic distributions for the I-R transition rate (e.g. the Erlang distribution).

For the special case in which there is no removal from the infectious compartment ( $\gamma =0$ ), the SIR model reduces to a very simple SI model, which has a logistic solution, in which every individual eventually becomes infected.

### The SIR model without birth and death

The dynamics of an epidemic, for example, the flu, are often much faster than the dynamics of birth and death, therefore, birth and death are often omitted in simple compartmental models. The SIR system without so-called vital dynamics (birth and death, sometimes called demography) described above can be expressed by the following system of ordinary differential equations:

$\left\{{\begin{aligned}&{\frac {dS}{dt}}=-{\frac {\beta }{N}}IS,\\[6pt]&{\frac {dI}{dt}}={\frac {\beta }{N}}IS-\gamma I,\\[6pt]&{\frac {dR}{dt}}=\gamma I,\end{aligned}}\right.$

where S is the stock of susceptible population in unit number of people, I is the stock of infected in unit number of people, R is the stock of removed population (either by death or recovery) in unit number of people, and N is the sum of these three in unit number of people. $\beta$ is the infection rate constant in the unit number of people infected per day per infected person, and $\gamma$ is the recovery rate constant in the unit fraction of a person recovered per day per infected person, when time is in unit day.

This model was for the first time proposed by William Ogilvy Kermack and Anderson Gray McKendrick as a special case of what we now call Kermack–McKendrick theory, and followed work McKendrick had done with Ronald Ross.

This system is non-linear, however it is possible to derive its analytic solution in implicit form. Firstly note that from:

${\frac {dS}{dt}}+{\frac {dI}{dt}}+{\frac {dR}{dt}}=0,$

it follows that:

$S(t)+I(t)+R(t)={\text{constant}}=N,$

expressing in mathematical terms the constancy of population N . Note that the above relationship implies that one need only study the equation for two of the three variables.

Secondly, we note that the dynamics of the infectious class depends on the following ratio:

$R_{0}={\frac {\beta }{\gamma }},$

the so-called basic reproduction number (also called basic reproduction ratio). This ratio is derived as the expected number of new infections (these new infections are sometimes called secondary infections) from a single infection in a population where all subjects are susceptible. This idea can probably be more readily seen if we say that the typical time between contacts is $T_{c}=\beta ^{-1}$ , and the typical time until removal is $T_{r}=\gamma ^{-1}$ . From here it follows that, on average, the number of contacts by an infectious individual with others *before* the infectious has been removed is: $T_{r}/T_{c}.$

By dividing the first differential equation by the third, separating the variables and integrating we get

$S(t)=S(0)e^{-R_{0}(R(t)-R(0))/N},$

where $S(0)$ and $R(0)$ are the initial numbers of, respectively, susceptible and removed subjects. Writing $s_{0}=S(0)/N$ for the initial proportion of susceptible individuals, and $s_{\infty }=S(\infty )/N$ and $r_{\infty }=R(\infty )/N$ for the proportion of susceptible and removed individuals respectively in the limit $t\to \infty ,$ one has

$s_{\infty }=1-r_{\infty }=s_{0}e^{-R_{0}(r_{\infty }-r_{0})}$

(note that the infectious compartment empties in this limit). This transcendental equation has a solution in terms of the Lambert W function, namely

$s_{\infty }=1-r_{\infty }=-R_{0}^{-1}\,W(-s_{0}R_{0}e^{-R_{0}(1-r_{0})}).$

This shows that at the end of an epidemic that conforms to the simple assumptions of the SIR model, unless $s_{0}=0$ , not all individuals of the population have been removed, so some must remain susceptible. A driving force leading to the end of an epidemic is a decline in the number of infectious individuals. The epidemic does not typically end because of a complete lack of susceptible individuals.

The role of both the basic reproduction number and the initial susceptibility are extremely important. In fact, upon rewriting the equation for infectious individuals as follows:

${\frac {dI}{dt}}=\left(R_{0}{\frac {S}{N}}-1\right)\gamma I,$

it yields that if:

$R_{0}\cdot S(0)>N,$

then:

${\frac {dI}{dt}}(0)>0,$

i.e., there will be a proper epidemic outbreak with an increase of the number of the infectious (which can reach a considerable fraction of the population). On the contrary, if

$R_{0}\cdot S(0)<N,$

then

${\frac {dI}{dt}}(0)<0,$

i.e., independently from the initial size of the susceptible population the disease can never cause a proper epidemic outbreak. As a consequence, it is clear that both the basic reproduction number and the initial susceptibility are extremely important.

#### The force of infection

Note that in the above model the function:

$F=\beta I,$

models the transition rate from the compartment of susceptible individuals to the compartment of infectious individuals, so that it is called the force of infection. However, for large classes of communicable diseases it is more realistic to consider a force of infection that does not depend on the absolute number of infectious subjects, but on their fraction (with respect to the total constant population N ):

$F=\beta {\frac {I}{N}}.$

Capasso and, afterwards, other authors have proposed nonlinear forces of infection to model more realistically the contagion process.

#### Exact analytical solutions to the SIR model

In 2014, Harko and coauthors derived an exact so-called analytical solution (involving an integral that can only be calculated numerically) to the SIR model. In the case without vital dynamics setup, for ${\mathcal {S}}(u)=S(t)$ , etc., it corresponds to the following time parametrization

${\mathcal {S}}(u)=S(0)u$

${\mathcal {I}}(u)=N-{\mathcal {R}}(u)-{\mathcal {S}}(u)$

${\mathcal {R}}(u)=R(0)-\rho \ln(u)$

for

$t={\frac {N}{\beta }}\int _{u}^{1}{\frac {du^{*}}{u^{*}{\mathcal {I}}(u^{*})}},\quad \rho ={\frac {\gamma N}{\beta }},$

with initial conditions

$({\mathcal {S}}(1),{\mathcal {I}}(1),{\mathcal {R}}(1))=(S(0),N-R(0)-S(0),R(0)),\quad u_{T}<u<1,$

where $u_{T}$ satisfies ${\mathcal {I}}(u_{T})=0$ . By the transcendental equation for $R_{\infty }$ above, it follows that $u_{T}=e^{-(R_{\infty }-R(0))/\rho }(=S_{\infty }/S(0)$ , if $S(0)\neq 0)$ and $I_{\infty }=0$ .

An equivalent so-called analytical solution (involving an integral that can only be calculated numerically) found by Miller yields

${\begin{aligned}S(t)&=S(0)e^{-\xi (t)}\\[8pt]I(t)&=N-S(t)-R(t)\\[8pt]R(t)&=R(0)+\rho \xi (t)\\[8pt]\xi (t)&={\frac {\beta }{N}}\int _{0}^{t}I(t^{*})\,dt^{*}\end{aligned}}$

Here $\xi (t)$ can be interpreted as the expected number of transmissions an individual has received by time t . The two solutions are related by $e^{-\xi (t)}=u$ .

Effectively the same result can be found in the original work by Kermack and McKendrick.

These solutions may be easily understood by noting that all of the terms on the right-hand sides of the original differential equations are proportional to I . The equations may thus be divided through by I , and the time rescaled so that the differential operator on the left-hand side becomes simply $d/d\tau$ , where $d\tau =Idt$ , i.e. $\tau =\int Idt$ . The differential equations are now all linear, and the third equation, of the form $dR/d\tau =$ const., shows that $\tau$ and R (and $\xi$ above) are simply linearly related.

A highly accurate analytic approximant of the SIR model as well as exact analytic expressions for the final values $S_{\infty }$ , $I_{\infty }$ , and $R_{\infty }$ were provided by Kröger and Schlickeiser, so that there is no need to perform a numerical integration to solve the SIR model (a simplified example practice on COVID-19 numerical simulation using Microsoft Excel can be found here ), to obtain its parameters from existing data, or to predict the future dynamics of an epidemics modeled by the SIR model. The approximant involves the Lambert W function which is part of all basic data visualization software such as Microsoft Excel, MATLAB, and Mathematica.

While Kendall considered the so-called all-time SIR model where the initial conditions $S(0)$ , $I(0)$ , and $R(0)$ are coupled through the above relations, Kermack and McKendrick proposed to study the more general semi-time case, for which $S(0)$ and $I(0)$ are both arbitrary. This latter version, denoted as semi-time SIR model, makes predictions only for future times $t>0$ . An analytic approximant and exact expressions for the final values are available for the semi-time SIR model as well.

#### Numerical solutions to the SIR model with approximations

Numerical solutions to the SIR model can be found in the literature. An example is using the model to analyze COVID-19 spreading data. Three reproduction numbers can be pulled out from the data analyzed with numerical approximation,

the

basic reproduction number

:

$R_{0}={\frac {\beta _{0}}{\gamma _{0}}}$

the real-time reproduction number:

$R_{t}={\frac {\beta _{t}}{\gamma _{t}}}$

and the real-time effective reproduction number:

$R_{e}={\frac {\beta _{t}S}{\gamma _{t}N}}$

$R_{0}$ represents the speed of reproduction rate at the beginning of the spreading when all populations are assumed susceptible, e.g. if $\beta _{0}=0.4day^{-1}$ and $\gamma _{0}=0.2day^{-1}$ meaning one infectious person on average infects 0.4 susceptible people per day and recovers in 1/0.2=5 days. Thus when this person recovered, there are two people still infectious directly got from this person and $R_{0}=2$ , i.e. the number of infectious people doubled in one cycle of 5 days. The data simulated by the model with $R_{0}=2$ or real data fitted will yield a doubling of the number of infectious people faster than 5 days because the two infected people are infecting people. From the SIR model, we can tell that $\beta$ is determined by the nature of the disease and also a function of the interactive frequency between the infectious person I with the susceptible people S and also the intensity/duration of the interaction like how close they interact for how long and whether or not they both wear masks, thus, it changes over time when the average behavior of the carriers and susceptible people changes. The model use $SI$ to represent these factors but it indeed is referenced to the initial stage when no action is taken to prevent the spread and all population is susceptible, thus all changes are absorbed by the change of $\beta$ .

$\gamma$ is usually more stable over time assuming when the infectious person shows symptoms, she/he will seek medical attention or be self-isolated. So if we find $R_{t}$ changes, most probably the behaviors of people in the community have changed from their normal patterns before the outbreak, or the disease has mutated to a new form. Costive massive detection and isolation of susceptible close contacts have effects on reducing $1/\gamma$ but whose efficiencies are under debate. This debate is largely on the uncertainty of the number of days reduced from after infectious or detectable whichever comes first to before a symptom shows up for an infected susceptible person. If the person is infectious after symptoms show up, or detection only works for a person with symptoms, then these prevention methods are not necessary, and self-isolation and/or medical attention is the best way to cut the $1/\gamma$ values. The typical onset of the COVID-19 infectious period is in the order of one day from the symptoms showing up, making massive detection with typical frequency in a few days useless.

$R_{t}$ does not tell us whether or not the spreading will speed up or slow down in the latter stages when the fraction of susceptible people in the community has dropped significantly after recovery or vaccination. $R_{e}$ corrects this dilution effect by multiplying the fraction of the susceptible population over the total population. It corrects the effective/transmissible interaction between an infectious person and the rest of the community when many of the interaction is immune in the middle to late stages of the disease spreading. Thus, when $R_{e}>1$ , we will see an exponential-like outbreak; when $R_{e}=1$ , a steady state reached and no number of infectious people changes over time; and when $R_{e}<1$ , the disease decays and fades away over time.

Using the differential equations of the SIR model and converting them to numerical discrete forms, one can set up the recursive equations and calculate the S, I, and R populations with any given initial conditions but accumulate errors over a long calculation time from the reference point. Sometimes a convergence test is needed to estimate the errors. Given a set of initial conditions and the disease-spreading data, one can also fit the data with the SIR model and pull out the three reproduction numbers when the errors are usually negligible due to the short time step from the reference point. Any point of the time can be used as the initial condition to predict the future after it using this numerical model with assumption of time-evolved parameters such as population, $R_{t}$ , and $\gamma$ . However, away from this reference point, errors will accumulate over time thus convergence test is needed to find an optimal time step for more accurate results.

Among these three reproduction numbers, $R_{0}$ is very useful to judge the control pressure, e.g., a large value meaning the disease will spread very fast and is very difficult to control. $R_{t}$ is most useful in predicting future trends, for example, if we know the social interactions have reduced 50% frequently from that before the outbreak and the interaction intensities among people are the same, then we can set $R_{t}=0.5R_{0}$ . If social distancing and masks add another 50% cut in infection efficiency, we can set $R_{t}=0.25R_{0}$ . $R_{e}$ will perfectly correlate with the waves of the spreading and whenever $R_{e}>1$ , the spreading accelerates, and when $R_{e}<1$ , the spreading slows down thus useful to set a prediction on the short-term trends. Also, it can be used to directly calculate the threshold population of vaccination/immunization for the herd immunity stage by setting $R_{t}=R_{0}$ , and $R_{E}=1$ , i.e. $S=N/R_{0}$ .

### The SIR model with vital dynamics and constant population

Consider a population characterized by a death rate $\mu$ and birth rate $\Lambda$ , and where a communicable disease is spreading. The model with mass-action transmission is:

${\begin{aligned}{\frac {dS}{dt}}&=\Lambda -\mu S-{\frac {\beta IS}{N}}\\[8pt]{\frac {dI}{dt}}&={\frac {\beta IS}{N}}-\gamma I-\mu I\\[8pt]{\frac {dR}{dt}}&=\gamma I-\mu R\end{aligned}}$

for which the disease-free equilibrium (DFE) is:

$\left(S(t),I(t),R(t)\right)=\left({\frac {\Lambda }{\mu }},0,0\right).$

In this case, we can derive a basic reproduction number:

$R_{0}={\frac {\beta }{\mu +\gamma }},$

which has threshold properties. In fact, independently from biologically meaningful initial values, one can show that:

$R_{0}\leq 1\Rightarrow \lim _{t\to \infty }(S(t),I(t),R(t))={\textrm {DFE}}=\left({\frac {\Lambda }{\mu }},0,0\right)$

$R_{0}>1,I(0)>0\Rightarrow \lim _{t\to \infty }(S(t),I(t),R(t))={\textrm {EE}}=\left({\frac {\gamma +\mu }{\beta }},{\frac {\mu }{\beta }}\left(R_{0}-1\right),{\frac {\gamma }{\beta }}\left(R_{0}-1\right)\right).$

The point EE is called the Endemic Equilibrium (the disease is not totally eradicated and remains in the population). With heuristic arguments, one may show that $R_{0}$ may be read as the average number of infections caused by a single infectious subject in a wholly susceptible population, the above relationship biologically means that if this number is less than or equal to one the disease goes extinct, whereas if this number is greater than one the disease will remain permanently endemic in the population.

### The SIR model

In 1927, W. O. Kermack and A. G. McKendrick created a model in which they considered a fixed population with only three compartments: susceptible, $S(t)$ ; infected, $I(t)$ ; and recovered, $R(t)$ . The compartments used for this model consist of three classes:

- $S(t)$ is used to represent the individuals not yet infected with the disease at time t, or those susceptible to the disease of the population.
- $I(t)$ denotes the individuals of the population who have been infected with the disease and are capable of spreading the disease to those in the susceptible category.
- $R(t)$ is the compartment used for the individuals of the population who have been infected and then removed from the disease, either due to immunization or due to death. Those in this category are not able to be infected again or to transmit the infection to others.

The flow of this model may be considered as follows:

${\color {blue}{{\mathcal {S}}\rightarrow {\mathcal {I}}\rightarrow {\mathcal {R}}}}$

Using a fixed population, $N=S(t)+I(t)+R(t)$ in the three functions resolves that the value N should remain constant within the simulation, if a simulation is used to solve the SIR model. Alternatively, the analytic approximant can be used without performing a simulation. The model is started with values of $S(t=0)$ , $I(t=0)$ and $R(t=0)$ . These are the number of people in the susceptible, infected and removed categories at time equals zero. If the SIR model is assumed to hold at all times, these initial conditions are not independent. Subsequently, the flow model updates the three variables for every time point with set values for $\beta$ and $\gamma$ . The simulation first updates the infected from the susceptible and then the removed category is updated from the infected category for the next time point (t=1). This describes the flow persons between the three categories. During an epidemic the susceptible category is not shifted with this model, $\beta$ changes over the course of the epidemic and so does $\gamma$ . These variables determine the length of the epidemic and would have to be updated with each cycle.

${\frac {dS}{dt}}=-\beta SI$

${\frac {dI}{dt}}=\beta SI-\gamma I$

${\frac {dR}{dt}}=\gamma I$

Several assumptions were made in the formulation of these equations: First, an individual in the population must be considered as having an equal probability as every other individual of contracting the disease with a rate of a and an equal fraction b of people that an individual makes contact with per unit time. Then, let $\beta$ be the multiplication of a and b . This is the transmission probability times the contact rate. Besides, an infected individual makes contact with b persons per unit time whereas only a fraction, $S/N$ of them are susceptible. Thus, we have every infective can infect $abS=\beta S$ susceptible persons, and therefore, the whole number of susceptibles infected by infectives per unit time is $\beta SI$ . For the second and third equations, consider the population leaving the susceptible class as equal to the number entering the infected class. However, a number equal to the fraction $\gamma$ (which represents the mean recovery/death rate, or $1/\gamma$ the mean infective period) of infectives are leaving this class per unit time to enter the removed class. These processes which occur simultaneously are referred to as the Law of Mass Action, a widely accepted idea that the rate of contact between two groups in a population is proportional to the size of each of the groups concerned. Finally, it is assumed that the rate of infection and recovery is much faster than the time scale of births and deaths and therefore, these factors are ignored in this model.

### Steady-state solutions

The only steady state solution to the classic SIR model as defined by the differential equations above is I=0, S and R can then take any values. The model can be changed while retaining three compartments to give a steady-state endemic solution by adding some input to the S compartment.

For example, one may postulate that the expected duration of susceptibility will be $\operatorname {E} [\min(T_{L}\mid T_{S})]$ where $T_{L}$ reflects the time alive (life expectancy) and $T_{S}$ reflects the time in the susceptible state before becoming infected, which can be simplified to:

$\operatorname {E} [\min(T_{L}\mid T_{S})]=\int _{0}^{\infty }e^{-(\mu +\delta )x}\,dx={\frac {1}{\mu +\delta }},$

such that the number of susceptible persons is the number entering the susceptible compartment $\mu N$ times the duration of susceptibility:

$S={\frac {\mu N}{\mu +\lambda }}.$

Analogously, the steady-state number of infected persons is the number entering the infected state from the susceptible state (number susceptible, times rate of infection) $\lambda ={\tfrac {\beta I}{N}},$ times the duration of infectiousness ${\tfrac {1}{\mu +v}}$ :

$I={\frac {\mu N}{\mu +\lambda }}\lambda {\frac {1}{\mu +v}}.$

### Other compartmental models

There are many modifications of the SIR model, including those that include births and deaths, where upon recovery there is no immunity (SIS model), where immunity lasts only for a short period of time (SIRS), where there is a latent period of the disease where the person is not infectious (SEIS and SEIR), and where infants can be born with immunity (MSIR). Also, compartments for vaccination, detection, or infected vectors like fleas, ticks, or mosquitoes can be added. Compartmental models can also be used to model multiple risk groups, and even the interaction of multiple pathogens.
