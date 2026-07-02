---
title: "Vehicle dynamics"
source: https://en.wikipedia.org/wiki/Vehicle_dynamics
domain: vehicle-dynamics-control
license: CC-BY-SA-4.0
tags: vehicle dynamics, electronic stability control, anti-lock braking, traction control
fetched: 2026-07-02
---

# Vehicle dynamics

**Vehicle dynamics** is the study of vehicle motion, e.g., how a vehicle's forward movement changes in response to driver inputs, propulsion system outputs, ambient conditions, air/surface/water conditions, etc. Vehicle dynamics is a part of engineering primarily based on classical mechanics. It may be applied for motorized vehicles (such as automobiles), bicycles and motorcycles, aircraft, and watercraft.

## Factors affecting vehicle dynamics

The aspects of a vehicle's design which affect the dynamics can be grouped into drivetrain and braking, suspension and steering, distribution of mass, aerodynamics and tires.

### Drivetrain and braking

- Automobile layout (i.e. location of engine and driven wheels)
- Powertrain
- Braking system

### Suspension and steering

Some attributes relate to the geometry of the suspension, steering and chassis. These include:

- Ackermann steering geometry
- Axle track
- Camber angle
- Caster angle
- Ride height
- Roll center
- Scrub radius
- Steering ratio
- Toe
- Wheel alignment
- Wheelbase

### Distribution of mass

Some attributes or aspects of vehicle dynamics are purely due to mass and its distribution. These include:

- Center of mass
- Moment of inertia
- Roll moment
- Sprung mass
- Unsprung mass
- Weight distribution

### Aerodynamics

Some attributes or aspects of vehicle dynamics are purely aerodynamic. These include:

- Automobile drag coefficient
- Automotive aerodynamics
- Center of pressure
- Downforce
- Ground effect in cars

### Tires

Some attributes or aspects of vehicle dynamics can be attributed directly to the tires. These include:

- Camber thrust
- Circle of forces
- Contact patch
- Cornering force
- Ground pressure
- Pacejka's Magic Formula
- Pneumatic trail
- Radial Force Variation
- Relaxation length
- Rolling resistance
- Self aligning torque
- Skid
- Slip angle
- Slip (vehicle dynamics)
- Spinout
- Steering ratio
- Tire load sensitivity

## Vehicle behaviours

Some attributes or aspects of vehicle dynamics are purely dynamic. These include:

- Body flex
- Body roll
- Bump steer
- Bundorf analysis
- Directional stability
- Critical speed
- Noise, vibration, and harshness
- Pitch
- Ride quality
- Roll
- Speed wobble
- Understeer, oversteer, lift-off oversteer, and fishtailing
- Weight transfer and load transfer
- Yaw

## Analysis and simulation

The dynamic behavior of vehicles can be analysed in several different ways. This can be as straightforward as a simple spring mass system, through a three-degree of freedom (DoF) bicycle model, to a large degree of complexity using a multibody system simulation package such as MSC ADAMS or Modelica. As computers have gotten faster, and software user interfaces have improved, commercial packages such as CarSim have become widely used in industry for rapidly evaluating hundreds of test conditions much faster than real time. Vehicle models are often simulated with advanced controller designs provided as software in the loop (SIL) with controller design software such as Simulink, or with physical hardware in the loop (HIL).

Vehicle motions are largely due to the shear forces generated between the tires and road, and therefore the tire model is an essential part of the math model. In current vehicle simulator models, the tire model is the weakest and most difficult part to simulate. The tire model must produce realistic shear forces during braking, acceleration, cornering, and combinations, on a range of surface conditions. Many models are in use. Most are semi-empirical, such as the Pacejka Magic Formula model.

Racing car games or simulators are also a form of vehicle dynamics simulation. In early versions many simplifications were necessary in order to get real-time performance with reasonable graphics. However, improvements in computer speed have combined with interest in realistic physics, leading to driving simulators that are used for vehicle engineering using detailed models such as CarSim.

It is important that the models should agree with real world test results, hence many of the following tests are correlated against results from instrumented test vehicles.

Techniques include:

- Linear range constant radius understeer
- Fishhook
- Frequency response
- Lane change
- Moose test
- Sinusoidal steering
- Skidpad
- Swept path analysis
