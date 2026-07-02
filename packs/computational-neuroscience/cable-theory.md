---
title: "Cable theory"
source: https://en.wikipedia.org/wiki/Cable_theory
domain: computational-neuroscience
license: CC-BY-SA-4.0
tags: computational neuroscience, hodgkin-huxley model, biological neuron model, cable theory
fetched: 2026-07-02
---

# Cable theory

In neuroscience, classical **cable theory** uses mathematical models to calculate the electric current (and accompanying voltage) along passive neurites, particularly the dendrites that receive synaptic inputs at different sites and times. Estimates are made by modeling dendrites and axons as cylinders composed of segments with capacitances $c_{m}$ and resistances $r_{m}$ combined in parallel (see Fig. 1). The capacitance of a neuronal fiber comes about because electrostatic forces are acting through the very thin lipid bilayer (see Figure 2). The resistance in series along the fiber $r_{l}$ is due to the axoplasm's significant resistance to movement of electric charge.

## History

Cable theory in computational neuroscience has roots leading back to the 1850s, when Professor William Thomson (later known as Lord Kelvin) began developing mathematical models of signal decay in submarine (underwater) telegraphic cables. The models resembled the partial differential equations used by Fourier to describe heat conduction in a wire.

The 1870s saw the first attempts by Hermann to model neuronal electrotonic potentials also by focusing on analogies with heat conduction. However, it was Hoorweg who first discovered the analogies with Kelvin's undersea cables in 1898 and then Hermann and Cremer who independently developed the cable theory for neuronal fibers in the early 20th century. Further mathematical theories of nerve fiber conduction based on cable theory were developed by Cole and Hodgkin (1920s–1930s), Offner et al. (1940), and Rushton (1951).

Experimental evidence for the importance of cable theory in modelling the behavior of axons began surfacing in the 1930s from work done by Cole, Curtis, Hodgkin, Sir Bernard Katz, Rushton, Tasaki and others. Two key papers from this era are those of Davis and Lorente de Nó (1947) and Hodgkin and Rushton (1946).

The 1950s saw improvements in techniques for measuring the electric activity of individual neurons. Thus cable theory became important for analyzing data collected from intracellular microelectrode recordings and for analyzing the electrical properties of neuronal dendrites. Scientists like Coombs, Eccles, Fatt, Frank, Fuortes and others now relied heavily on cable theory to obtain functional insights of neurons and for guiding them in the design of new experiments.

Later, cable theory with its mathematical derivatives allowed ever more sophisticated neuron models to be explored by workers such as Jack, Rall, Redman, Rinzel, Idan Segev, Tuckwell, Bell, and Iannella. More recently, cable theory has been applied to model electrical activity in bundled neurons in the white matter of the brain.

## Deriving the cable equation

Note, various conventions of *r**m* exist. Here *r**m* and *c**m*, as introduced above, are measured per membrane-length unit (per meter (m)). Thus *r**m* is measured in ohm·meters (Ω·m) and *c**m* in farads per meter (F/m). This is in contrast to *R**m* (in Ω·m2) and *C**m* (in F/m2), which represent the specific resistance and capacitance respectively of one unit area of membrane (in m2). Thus, if the radius, *a*, of the axon is known, then its circumference is 2*πa*, and its *r**m*, and its *c**m* values can be calculated as:

| $r_{m}={\frac {R_{m}}{2\pi a\ }}$ |   | 1 |
|---|---|---|

| $c_{m}=C_{m}2\pi a\$ |   | 2 |
|---|---|---|

These relationships make sense intuitively, because the greater the circumference of the axon, the greater the area for charge to escape through its membrane, and therefore the lower the membrane resistance (dividing *R**m* by 2*πa*); and the more membrane available to store charge (multiplying *C**m* by 2*πa*). The specific electrical resistance, *ρ**l*, of the axoplasm allows one to calculate the longitudinal intracellular resistance per unit length, *r**l*, (in Ω·m−1) by the equation:

| $r_{l}={\frac {\rho _{l}}{\pi a^{2}\ }}$ |   | 3 |
|---|---|---|

The greater the cross sectional area of the axon, *πa*2, the greater the number of paths for the charge to flow through its axoplasm, and the lower the axoplasmic resistance.

Several important avenues of extending classical cable theory have recently seen the introduction of endogenous structures in order to analyze the effects of protein polarization within dendrites and different synaptic input distributions over the dendritic surface of a neuron.

To better understand how the cable equation is derived, first consider an idealized neuron with a perfectly sealed membrane (*r**m*=∞) with no loss of current to the outside, and no capacitance (*c**m* = 0). A current injected into the fiber at position *x* = 0 would move along the inside of the fiber unchanged. Moving away from the point of injection and by using Ohm's law (*V* = *IR*) we can calculate the voltage change as:

| $\Delta V=-i_{l}r_{l}\Delta x\$ |   | 4 |
|---|---|---|

where the negative is because current flows down the potential gradient.

Letting Δ*x* go towards zero and having infinitely small increments of *x*, one can write (**4**) as:

| ${\frac {\partial V}{\partial x}}=-i_{l}r_{l}\$ |   | 5 |
|---|---|---|

or

| ${\frac {1}{r_{l}}}{\frac {\partial V}{\partial x}}=-i_{l}\$ |   | 6 |
|---|---|---|

Bringing *r**m* back into the picture is like making holes in a garden hose. The more holes, the faster the water will escape from the hose, and the less water will travel all the way from the beginning of the hose to the end. Similarly, in an axon, some of the current traveling longitudinally through the axoplasm will escape through the membrane.

If *i**m* is the current escaping through the membrane per length unit, m, then the total current escaping along *y* units must be *y·i**m*. Thus, the change of current in the axoplasm, Δ*i**l*, at distance, Δ*x*, from position *x*=0 can be written as:

| $\Delta i_{l}=-i_{m}\Delta x\$ |   | 7 |
|---|---|---|

or, using continuous, infinitesimally small increments:

| ${\frac {\partial i_{l}}{\partial x}}=-i_{m}\$ |   | 8 |
|---|---|---|

$i_{m}$ can be expressed with yet another formula, by including the capacitance. The capacitance will cause a flow of charge (a current) towards the membrane on the side of the cytoplasm. This current is usually referred to as displacement current (here denoted $i_{c}$ .) The flow will only take place as long as the membrane's storage capacity has not been reached. $i_{c}$ can then be expressed as:

| $i_{c}=c_{m}{\frac {\partial V}{\partial t}}\$ |   | 9 |
|---|---|---|

where $c_{m}$ is the membrane's capacitance and ${\partial V}/{\partial t}$ is the change in voltage over time. The current that passes the membrane ( $i_{r}$ ) can be expressed as:

| $i_{r}={\frac {V}{r_{m}}}$ |   | 10 |
|---|---|---|

and because $i_{m}=i_{r}+i_{c}$ the following equation for $i_{m}$ can be derived if no additional current is added from an electrode:

| ${\frac {\partial i_{l}}{\partial x}}=-i_{m}=-({\frac {V}{r_{m}}}+c_{m}{\frac {\partial V}{\partial t}})$ |   | 11 |
|---|---|---|

where ${\partial i_{l}}/{\partial x}$ represents the change per unit length of the longitudinal current.

Combining equations (**6**) and (**11**) gives a first version of a cable equation:

| ${\frac {1}{r_{l}}}{\frac {\partial ^{2}V}{\partial x^{2}}}=c_{m}{\frac {\partial V}{\partial t}}+{\frac {V}{r_{m}}}$ |   | 12 |
|---|---|---|

which is a second-order partial differential equation (PDE).

By a simple rearrangement of equation (**12**) (see later) it is possible to make two important terms appear, namely the length constant (sometimes referred to as the space constant) denoted $\lambda$ and the time constant denoted $\tau$ . The following sections focus on these terms.

## Length constant

The length constant, $\lambda$ (lambda), is a parameter that indicates how far a stationary current will influence the voltage along the cable. The larger the value of $\lambda$ , the farther the charge will flow. The length constant can be expressed as:

| $\lambda ={\sqrt {\frac {r_{m}}{r_{l}}}}$ |   | 13 |
|---|---|---|

The larger the membrane resistance, *r**m*, the greater the value of $\lambda$ , and the more current will remain inside the axoplasm to travel longitudinally through the axon. The higher the axoplasmic resistance, $r_{l}$ , the smaller the value of $\lambda$ , the harder it will be for current to travel through the axoplasm, and the shorter the current will be able to travel. It is possible to solve equation (**12**) and arrive at the following equation (which is valid in steady-state conditions, i.e. when time approaches infinity):

| $V_{x}=V_{0}e^{-{\frac {x}{\lambda }}}$ |   | 14 |
|---|---|---|

Where $V_{0}$ is the depolarization at $x=0$ (point of current injection), *e* is the exponential constant (approximate value 2.71828) and $V_{x}$ is the voltage at a given distance *x* from *x*=0. When $x=\lambda$ then

| ${\frac {x}{\lambda }}=1$ |   | 15 |
|---|---|---|

and

| $V_{x}=V_{0}e^{-1}$ |   | 16 |
|---|---|---|

which means that when we measure V at distance $\lambda$ from $x=0$ we get

| $V_{\lambda }={\frac {V_{0}}{e}}=0.368V_{0}$ |   | 17 |
|---|---|---|

Thus $V_{\lambda }$ is always 36.8 percent of $V_{0}$ .

## Time constant

Neuroscientists are often interested in knowing how fast the membrane potential, $V_{m}$ , of an axon changes in response to changes in the current injected into the axoplasm. The time constant, $\tau$ , is an index that provides information about that value. $\tau$ can be calculated as:

| $\tau =r_{m}c_{m}.\$ |   | 18 |
|---|---|---|

The larger the membrane capacitance, $c_{m}$ , the more current it takes to charge and discharge a patch of membrane and the longer this process will take. The larger the membrane resistance $r_{m}$ , the harder it is for a current to induce a change in membrane potential. So the higher the $\tau$ the slower the nerve impulse can travel. That means, membrane potential (voltage across the membrane) lags more behind current injections. Response times vary from 1–2 milliseconds in neurons that are processing information that needs high temporal precision to 100 milliseconds or longer. A typical response time is around 20 milliseconds.

## Generic form and mathematical structure

If one multiplies equation (**12**) by $r_{m}$ on both sides of the equal sign we get:

| ${\frac {r_{m}}{r_{l}}}{\frac {\partial ^{2}V}{\partial x^{2}}}=c_{m}r_{m}{\frac {\partial V}{\partial t}}+V$ |   | 19 |
|---|---|---|

and recognize $\lambda ^{2}={r_{m}}/{r_{l}}$ on the left side and $\tau =c_{m}r_{m}$ on the right side. The cable equation can now be written in its perhaps best known form:

| $\lambda ^{2}{\frac {\partial ^{2}V}{\partial x^{2}}}=\tau {\frac {\partial V}{\partial t}}+V$ |   | 20 |
|---|---|---|

This is a 1D heat equation or diffusion equation for which many solution methods, such as Green's functions and Fourier methods, have been developed.

It is also a special degenerate case of the Telegrapher's equation, where the inductance L vanishes and the signal propagation speed $1/{\sqrt {LC}}$ is infinite.
