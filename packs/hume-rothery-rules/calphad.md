---
title: "CALPHAD"
source: https://en.wikipedia.org/wiki/CALPHAD
domain: hume-rothery-rules
license: CC-BY-SA-4.0
tags: hume-rothery rules
fetched: 2026-07-04
---

# CALPHAD

**CALPHAD** stands for *CALculation of PHAse Diagrams*, a methodology introduced in 1970 by Larry Kaufman. An equilibrium phase diagram is usually a diagram with axes for temperature and composition of a chemical system. It shows the regions where substances or solutions (i.e. phases) are stable and regions where two or more of them coexist. Phase diagrams are a very powerful tool for predicting the state of a system under different conditions and were initially a graphical method to rationalize experimental information on states of equilibrium. In complex systems, computational methods such as CALPHAD are employed to model thermodynamic properties for each phase and simulate multicomponent phase behavior. The CALPHAD approach is based on the fact that a phase diagram is a manifestation of the equilibrium thermodynamic properties of the system, which are the sum of the properties of the individual phases. It is thus possible to calculate a phase diagram by first assessing the thermodynamic properties of all the phases in a system.

## Methodology

With the CALPHAD method one collects all experimental information on phase equilibria in a system and all thermodynamic information obtained from thermochemical and thermophysical studies. The thermodynamic properties of each phase are then described with a mathematical model containing adjustable parameters. The parameters are evaluated by optimizing the fit of the model to all the information, also involving coexisting phases. It is then possible to recalculate the phase diagram as well as the thermodynamic properties of all the phases. The philosophy of the CALPHAD method is to obtain a consistent description of the phase diagram and the thermodynamic properties so to reliably predict the set of stable phases and their thermodynamic properties in regions without experimental information and for metastable states during simulations of phase transformations.

### Thermodynamic modeling of a phase

There are two crucial factors for the success of the CALPHAD method. The first factor is to find realistic as well as convenient mathematical models for the Gibbs energy for each phase. The Gibbs energy is used because most experimental data have been determined at known temperature and pressure and any other thermodynamic quantities can be calculated from it. It is not possible to obtain an exact description of the behavior of the Gibbs energy of a multi-component system with analytical expressions. It is thus necessary to identify the main features and base the mathematical models on them. The discrepancy between model and reality is finally represented by a power series expansion in temperature, pressure and constitution of the phase. The adjustable parameters of these model descriptions are refined to reproduce the experimental data. The strength of the CALPHAD method is that the descriptions of the constituent sub-systems can be combined to describe a multi-component system.

### Equilibrium calculations

The second crucial factor is the availability of computer software for calculating equilibria and various kinds of diagrams and databases with the stored assessed information. As there are at present many different kinds of models used for different kinds of phases there are several thermodynamic databases available, either free or commercially, for different materials like steels, super-alloys, semiconductor materials, aqueous solutions, slags, etc. There are also several different kinds of software available using different kinds of algorithms for computing the equilibrium. It is an advantage if the software allows the equilibrium to be calculated using many different types of conditions for the system, not only the temperature, pressure and overall composition because in many cases the equilibrium may be determined at constant volume or at a given chemical potential of an element or a given composition of a particular phase.

## Applications

CALPHAD had a slow start in the 60s but sophisticated thermodynamic data bank systems started to appear in the 80s and today there are several commercial products on the market, e.g. FactSage, MTDATA, PANDAT, MatCalc, JMatPro, and Thermo-Calc as well as open-sources codes such as OpenCalphad, PyCalphad, and ESPEI. They are used in research and industrial development (e.g., PrecipiCalc software and *Materials by Design* Technology), where they save large amounts of time and resources by reducing the experimental work and by making thermodynamic predictions available for multi-component systems that would be practically unattainable without this approach. There is a journal with this name where recent scientific achievements are published but scientific papers describing the use of the CALPHAD methods are published also in many other journals.
