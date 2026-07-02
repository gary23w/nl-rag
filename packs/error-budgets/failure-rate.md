---
title: "Failure rate"
source: https://en.wikipedia.org/wiki/Failure_rate
domain: error-budgets
license: CC-BY-SA-4.0
tags: error budget, reliability spend policy, budget burn allowance, release velocity tradeoff
fetched: 2026-07-02
---

# Failure rate

**Failure rate** is the frequency with which any system or component fails, expressed in failures per unit of time. It thus depends on the system conditions, time interval, and total number of systems under study. It can describe electronic, mechanical, or biological systems, in fields such as systems and reliability engineering, medicine and biology, or insurance and finance. It is usually denoted by the Greek letter $\lambda$ (lambda).

In real-world applications, the failure probability of a system usually differs over time; failures occur more frequently in early-life ("burning in"), or as a system ages ("wearing out"). This is known as the bathtub curve, where the middle region is called the "useful life period".

## Mean time between failures (MTBF)

The mean time between failures (MTBF, $1/\lambda$ ) is often reported instead of the failure rate, as numbers such as "2,000 hours" are more intuitive than numbers such as "0.0005 per hour".

However, this is only valid if the failure rate $\lambda (t)$ is actually constant over time, such as within the flat region of the bathtub curve. In many cases where MTBF is quoted, it refers only to this region; thus it cannot be used to give an accurate calculation of the average lifetime of a system, as it ignores the "burn-in" and "wear-out" regions.

MTBF appears frequently in engineering design requirements, and governs the frequency of required system maintenance and inspections. A similar ratio used in the transport industries, especially in railways and trucking, is "mean distance between failures" (MDBF) - allowing maintenance to be scheduled based on distance travelled, rather than at regular time intervals.

## Mathematical definition

The simplest definition of failure rate $\lambda$ is simply the number of failures $\Delta n$ per time interval $\Delta t$ :

$\lambda ={\frac {\Delta n}{\Delta t}}$

which would depend on the number of systems under study, and the conditions over the time period.

### Failures over time

To accurately model failures over time, a **cumulative failure distribution**, $F(t)$ must be defined, which can be any cumulative distribution function (CDF) that gradually increases from 0 to 1 . In the case of many identical systems, this may be thought of as the fraction of systems failing over time t , after all starting operation at time $t=0$ ; or in the case of a single system, as the probability of the system having its failure time T before time t :

$F(t)=\Pr(T\leq t).$

As CDFs are defined by integrating a probability density function, the **failure probability density** $f(t)$ is defined such that:

$F(t)=\int _{0}^{t}f(\tau )\,d\tau$

where $\tau$ is a dummy integration variable. Here $f(t)$ can be thought of as the *instantaneous failure rate*, i.e. the probability of failure in the time interval between t and $t{+}\Delta t$ , as $\Delta t$ tends towards 0 :

$f(t)=\lim _{\Delta t\to 0^{+}}{\frac {\Pr(t<T\leq t{+}\Delta t)}{\Delta t}}.$

### Hazard rate

A concept closely related but different to instantaneous failure rate $f(t)$ is the **hazard rate** (or **hazard function**), $h(t)$ . In the many-system case, this is defined as the proportional failure rate of the systems *still functioning* at time t – as opposed to $f(t)$ , which is the expressed as a proportion of the *initial number* of systems.

For convenience we first define the reliability (or survival function) as:

$R(t)=1-F(t)=\Pr(T>t)$

then the hazard rate is simply the instantaneous failure rate, scaled by the fraction of surviving systems at time t :

$h(t)={\frac {f(t)}{R(t)}}$

In the probabilistic sense for a single system, this can be interpreted as the instantaneous failure rate under the conditional probability that the system or component has already survived to time t :

$h(t)=\lim _{\Delta t\to 0^{+}}{\frac {\Pr(t<T\leq t{+}\Delta t\mid T>t)}{\Delta t}}.$

#### Conversion to cumulative failure rate

To convert between $h(t)$ and $F(t)$ , we can solve the differential equation

$h(t)={\frac {f(t)}{R(t)}}=-{\frac {R'(t)}{R(t)}}$

with initial condition $R(0)=1$ , which yields

$F(t)=1-\exp {\left(-\int _{0}^{t}h(\tau )d\tau \right)}.$

Thus for a collection of identical systems, only one of hazard rate $h(t)$ , failure probability density $f(t)$ , or cumulative failure distribution $F(t)$ need be defined.

Confusion can occur as the notation $\lambda (t)$ for "failure rate" often refers to the function $h(t)$ rather than $f(t).$

### Constant hazard rate model

There are many possible functions that could be chosen to represent failure probability density $f(t)$ or hazard rate $h(t)$ , based on empirical or theoretical evidence, but the most common and easily-understandable choice is to set

$f(t)=\lambda e^{-\lambda t},$

an exponential function with scaling constant $\lambda$ . As seen in the figures above, this represents a gradually decreasing failure probability density.

The CDF $F(t)$ is then calculated as:

$F(t)=\int _{0}^{t}\lambda e^{-\lambda \tau }\,d\tau =1-e^{-\lambda t},$

which can be seen to gradually approach 1 as $t\to \infty ,$ representing the fact that eventually all systems under study will fail.

The hazard rate function is then:

$h(t)={\frac {f(t)}{R(t)}}={\frac {\lambda e^{-\lambda t}}{e^{-\lambda t}}}=\lambda .$

In other words, in this particular case *only*, the hazard rate is constant over time.

This illustrates the difference in hazard rate and failure probability density - as the number of systems surviving at time $t>0$ gradually reduces, the total failure rate also reduces, but the hazard rate **remains constant**. In other words, the probabilities of each individual system failing do not change over time as the systems age - they are "memory-less".

### Other models

For many systems, a constant hazard function may not be a realistic approximation; the chance of failure of an individual component may depend on its age. Therefore, other distributions are often used.

For example, the deterministic distribution increases hazard rate over time (for systems where wear-out is the most important factor), while the Pareto distribution decreases it (for systems where early-life failures are more common). The commonly used Weibull distribution combines both of these effects, as do the log-normal and hypertabastic distributions.

After modelling a given distribution and parameters for $h(t)$ , the failure probability density $f(t)$ and cumulative failure distribution $F(t)$ can be predicted using the given equations.

## Measuring failure rate

Failure rate data can be obtained in several ways. The most common means are:

**Estimation**

From field failure rate reports, statistical analysis techniques can be used to estimate failure rates. For accurate failure rates the analyst must have a good understanding of equipment operation, procedures for data collection, the key environmental variables impacting failure rates, how the equipment is used at the system level, and how the failure data will be used by system designers.

**Historical data about the device or system under consideration**

Many organizations maintain internal databases of failure information on the devices or systems that they produce, which can be used to calculate failure rates for those devices or systems. For new devices or systems, the historical data for similar devices or systems can serve as a useful estimate.

**Government and commercial failure rate data**

Handbooks of failure rate data for various components are available from government and commercial sources. MIL-HDBK-217F,

Reliability Prediction of Electronic Equipment

, is a

military standard

that provides failure rate data for many military electronic components. Several failure rate data sources are available commercially that focus on commercial components, including some non-electronic components.

**Prediction**

Time lag is one of the serious drawbacks of all failure rate estimations. Often by the time the failure rate data are available, the devices under study have become obsolete. Due to this drawback, failure-rate prediction methods have been developed. These methods may be used on newly designed devices to predict the device's failure rates and failure modes. Two approaches have become well known, Cycle Testing and FMEDA.

**Life Testing**

The most accurate source of data is to test samples of the actual devices or systems in order to generate failure data. This is often prohibitively expensive or impractical, so that the previous data sources are often used instead.

**Cycle Testing**

Mechanical movement is the predominant failure mechanism causing mechanical and electromechanical devices to wear out. For many devices, the wear-out failure point is measured by the number of cycles performed before the device fails, and can be discovered by cycle testing. In cycle testing, a device is cycled as rapidly as practical until it fails. When a collection of these devices are tested, the test will run until 10% of the units fail dangerously.

**FMEDA**

Failure modes, effects, and diagnostic analysis

(FMEDA) is a systematic analysis technique to obtain subsystem / product level failure rates, failure modes and design strength. The FMEDA technique considers:

- All components of a design,
- The functionality of each component,
- The failure modes of each component,
- The effect of each component failure mode on the product functionality,
- The ability of any automatic diagnostics to detect the failure,
- The design strength (de-rating, safety factors) and
- The operational profile (environmental stress factors).

Given a component database calibrated with field failure data that is reasonably accurate, the method can predict product level failure rate and failure mode data for a given application. The predictions have been shown to be more accurate than field warranty return analysis or even typical field failure analysis given that these methods depend on reports that typically do not have sufficient detail information in failure records.

## Examples

### Decreasing failure rates

A decreasing failure rate describes cases where early-life failures are common and corresponds to the situation where $h(t)$ is a decreasing function.

This can describe, for example, the period of infant mortality in humans, or the early failure of transistors due to manufacturing defects.

Decreasing failure rates have been found in the lifetimes of spacecraft - Baker and Baker commenting that "those spacecraft that last, last on and on."

The hazard rate of aircraft air conditioning systems was found to have an exponentially decreasing distribution.

### Renewal processes

In special processes called renewal processes, where the time to recover from failure can be neglected, the likelihood of failure remains constant with respect to time.

For a renewal process with DFR renewal function, inter-renewal times are concave. Brown conjectured the converse, that DFR is also necessary for the inter-renewal times to be concave, however it has been shown that this conjecture holds neither in the discrete case nor in the continuous case.

### Coefficient of variation

When the failure rate is decreasing the coefficient of variation is ⩾ 1, and when the failure rate is increasing the coefficient of variation is ⩽ 1. Note that this result only holds when the failure rate is defined for all t ⩾ 0 and that the converse result (coefficient of variation determining nature of failure rate) does not hold.

### Units

Failure rates can be expressed using any measure of time, but **hours** is the most common unit in practice. Other units, such as miles, revolutions, etc., can also be used in place of "time" units.

Failure rates are often expressed in engineering notation as failures per million, or 10−6, especially for individual components, since their failure rates are often very low.

The **Failures In Time** (**FIT**) rate of a device is the number of failures that can be expected in one billion (109) device-hours of operation (e.g. 1,000 devices for 1,000,000 hours, or 1,000,000 devices for 1,000 hours each, or some other combination). This term is used particularly by the semiconductor industry.

### Combinations of failure types

If a complex system consists of many parts, and the failure of any single part means the failure of the entire system, and the chance of failure for each part is conditionally independent of the failure of any other part, then the total failure rate is simply the sum of the individual failure rates of its parts

$\lambda _{S}=\lambda _{P1}+\lambda _{P2}+\ldots$

however, this assumes that the failure rate $\lambda (t)$ is constant, and that the units are consistent (e.g. failures per million hours), and not expressed as a ratio or as probability densities. This is useful to estimate the failure rate of a system when individual components or subsystems have already been tested.

When adding "redundant" components to eliminate a single point of failure, the quantity of interest is not the sum of individual failure rates but rather the "mission failure" rate, or the "mean time between critical failures" (MTBCF).

Combining failure or hazard rates that are time-dependent is more complicated. For example, mixtures of Decreasing Failure Rate (DFR) variables are also DFR. Mixtures of exponentially distributed failure rates are hyperexponentially distributed.

### Simple example

Suppose it is desired to estimate the failure rate of a certain component. Ten identical components are each tested until they either fail or reach 1,000 hours, at which time the test is terminated. A total of 7,502 component-hours of testing is performed, and 6 failures are recorded.

The *estimated* failure rate is:

${\frac {6{\text{ failures}}}{7502{\text{ hours}}}}=0.0007998\,{\frac {\text{failures}}{\text{hour}}}$

which could also be expressed as a MTBF of 1,250 hours, or approximately 800 failures for every million hours of operation.
