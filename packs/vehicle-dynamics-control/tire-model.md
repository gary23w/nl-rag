---
title: "Tire model"
source: https://en.wikipedia.org/wiki/Tire_model
domain: vehicle-dynamics-control
license: CC-BY-SA-4.0
tags: vehicle dynamics, electronic stability control, anti-lock braking, traction control
fetched: 2026-07-02
---

# Tire model

In vehicle dynamics, a **tire model** is a type of multibody simulation used to simulate the behavior of tires. In current vehicle simulator models, the tire model is the weakest and most difficult part to simulate.

Tire models can be classified on their accuracy and complexity, in a spectrum that goes from more simple empirical models to more complex physical models that are theoretically grounded. Empirical models include Hans B. Pacejka's *Magic Formula*, while physically based models include brush models (although they are still quite simplified), and more complex and detailed physical models include RMOD-K, FTire and Hankook. Theoretically-based models can be in turn classified from more approximative to more complex ones, going for example from the solid model, to the rigid ring model, to the flexural (elastic) ring model (like the Fiala model), and the most complex ones based on finite element methods.

Brush models were very popular in the 1960s and '70s, after which Pacejka's models became widespread for many applications.

## Classification by purpose

### Driving dynamics models

- Brush model (Dugoff, Fancher and Segel, 1970)
- Hohenheim tire model (physical approach [1])
- Pacejka Magic Formula Tire (Bakker, Nyborg and Pacejka, 1987)
- TameTire (semi-physical approach)
- TMeasy (semi-physical approach)
- Stretched string tire model (Fiala 1954)

### Comfort models

- BRIT (Brush and Ring Tire)
- CDTire (Comfort and Durability Tire)
- Ctire (Comfort tire)
- Dtire (Dynamical Nonlinear Spatial Tire Model)
- FTire (Flexible Structure Tire Model)
- RMOD-K (Comfort and Durability Tire)
- SWIFT (Short Wavelength Intermediate Frequency Tire) (Besselink, Pacejka, Schmeitz, & Jansen, 2005)

## Applications

Fully physics-based tire models have been typically too computational expensive to be run in realtime driving simulations. For example, to since CDTire/3D, a physics-based tire model, cannot be run in realtime, for realtime applications typically an equivalent semi-empirical "magic formula" type of model, called CDTire/Realtime, is derived from it through experiments and a regression algorithm.

In 2016, a slightly less accurate version of FTire, a physics-based tire model, was adapted to be run in real time. This realtime version of FTire was shown in 2018 to run on a 2,7 GHz 12 Core Intel Xeon E5 (2014, 22 nm process, about $2000), with 900 contact road/contact patch elements, a sample frequency of 4.0 kHz including thermal and wear simulation.

The typical tire model sampling rate used in automotive simulators is 1 kHz. However, running at higher frequencies, like 2 kHz, might mitigate lowered numerical stability in some scenarios, and might increase the model accuracy in frequency domain above about 250 Hz.
