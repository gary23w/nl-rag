---
title: "Reaction wheel"
source: https://en.wikipedia.org/wiki/Reaction_wheel
domain: satellite-systems
license: CC-BY-SA-4.0
tags: satellite systems, communications satellite, geostationary orbit, cubesat
fetched: 2026-07-02
---

# Reaction wheel

A **reaction wheel** (**RW**) is an electric motor attached to a flywheel, which, when its rotation speed is changed, causes a counter-rotation proportionately through conservation of angular momentum. A reaction wheel can rotate only around its center of mass; it is not capable of moving from one place to another (translational force).

Reaction wheels are used primarily by spacecraft for three-axis fine attitude control, but can also be used for fast detumbling. Reaction wheels do not require rockets or external applicators of torque, which reduces the mass fraction needed for fuel. They provide a high pointing accuracy, and are particularly useful when the spacecraft must be rotated by very small amounts, such as keeping a telescope pointed at a star.

A reaction wheel is sometimes operated at a constant (or near-constant) rotation speed, to provide a satellite with a large amount of stored angular momentum. Doing so alters the spacecraft's rotational dynamics so that disturbance torques perpendicular to one axis of the satellite (the axis parallel to the wheel's spin axis) do not result directly in spacecraft angular motion about the same axis as the disturbance torque; instead, they result in (generally smaller) angular motion (precession) of that spacecraft axis about a perpendicular axis. This has the effect of tending to stabilize that spacecraft axis to point in a nearly-fixed direction, allowing for a less-complicated attitude control system. Satellites using this "momentum-bias" stabilization approach include SCISAT-1; by orienting the momentum wheel's axis to be parallel to the orbit-normal vector, this satellite is in a "pitch momentum bias" configuration. Reaction wheels can also be used during the detumbling phase to stabilize the spacecraft after launcher separation or an unforeseen event.

## Design

For three-axis control, reaction wheels must be mounted along at least three directions, with extra wheels providing redundancy to the attitude control system. A redundant mounting configuration could consist of four wheels along tetrahedral axes, or a spare wheel carried in addition to a three axis configuration. Changes in speed (in either direction) are controlled electronically by computer. The strength of the materials used in a reaction wheel determine the speed at which the wheel would come apart, and therefore how much angular momentum it can store.

Since the reaction wheel is a small fraction of the spacecraft's total mass, easily controlled, temporary changes in its speed result in small changes in angle. The wheels therefore permit very precise changes in a spacecraft's attitude. For this reason, reaction wheels are often used to aim spacecraft carrying cameras or telescopes.

Over time, reaction wheels may build up enough stored momentum to exceed the maximum speed of the wheel, called saturation. However, slowing down the wheels imparts a torque causing undesired rotation. Designers therefore supplement reaction wheel systems with other attitude control mechanisms to cancel out the torque caused by "desaturating" the reaction wheels. Typically designers use "reaction control systems": arrays of small chemical rocket engines that fire as the wheels slow down to counter the torque the wheels are imparting on the spacecraft as they slow down.

More fuel efficient methods for reaction wheel desaturation have been developed over time. By reducing the amount of fuel the spacecraft needs to be launched with, they increase the useful payload that can be delivered to orbit. These methods include magnetorquers (better known as torque rods), which transfer angular momentum to the Earth through its planetary magnetic field requiring only electrical power and no fuel. They are however limited to areas of space with a sufficiently large magnetic field (such as in low Earth orbit). In the absence of a sufficiently strong magnetic field, the next most efficient practice is to use high-efficiency attitude jets such as ion thrusters.

## Examples

Beresheet was launched on a Falcon 9 rocket on 22 February 2019 1:45 UTC, with the goal of landing on the Moon. Beresheet uses the low-energy transfer technique to save fuel. Since its fourth maneuver in its elliptical orbit, to prevent shakes when the amount of liquid fuel ran low, there was a need to use a reaction wheel.

The James Webb Space Telescope has six reaction wheels built by Rockwell Collins Deutschland.

LightSail 2 was launched on 25 June 2019, focused around the concept of a solar sail. LightSail 2 uses a reaction wheel system to change orientation by very small amounts, allowing it to receive different amounts of momentum from the light across the sail, resulting in a higher altitude.

## Failures and mission impact

The failure of one or more reaction wheels can cause a spacecraft to lose its ability to maintain attitude (orientation) and thus potentially cause a mission failure. Recent studies conclude that these failures can be correlated with space weather effects. These events probably caused failures by inducing electrostatic discharge in the steel ball bearings of Ithaco wheels, compromising the smoothness of the mechanism. Supporting this hypothesis, newer reaction wheels have non-conducting ceramic bearings, and none have failed in this manner.

Two servicing missions to the Hubble Space Telescope have replaced a reaction wheel. In February 1997, the Second Servicing Mission (STS-82) replaced one after 'electrical anomalies', rather than any mechanical problem. Study of the returned mechanism provided a rare opportunity to study equipment that had undergone long-term service (seven years) in space, particularly for the effects of vacuum on lubricants. The lubricating compound was found to be in 'excellent condition'. In 2002, during Servicing Mission 3B (STS-109), astronauts from the shuttle *Columbia* replaced another reaction wheel. Neither of these wheels had failed and Hubble was designed with four redundant wheels, and maintained pointing ability so long as three were functional.

In 2004, during the mission of the *Hayabusa* spacecraft, an X-axis reaction wheel failed. The Y-axis wheel failed in 2005, causing the craft to rely on chemical thrusters to maintain attitude control.

From July 2012 to May 11, 2013, two out of the four reaction wheels in the Kepler space telescope failed. This loss severely affected Kepler's ability to maintain a sufficiently precise orientation to continue its original mission. On August 15, 2013, engineers concluded that Kepler's reaction wheels cannot be recovered and that planet-searching using the transit method (measuring changes in star brightness caused by orbiting planets) could not continue. Although the failed reaction wheels still function, they are experiencing friction exceeding acceptable levels, and consequently hindering the ability of the telescope to properly orient itself. The Kepler telescope was returned to its "point rest state", a stable configuration that uses small amounts of thruster fuel to compensate for the failed reaction wheels, while the Kepler team considered alternative uses for Kepler that do not require the extreme accuracy in its orientation needed by the original mission. On May 16, 2014, NASA extended the Kepler mission to a new mission named K2, which uses Kepler differently, but allows it to continue searching for exoplanets. On October 30, 2018, NASA announced the end of the Kepler mission after it was determined that the fuel supply had been exhausted.

The NASA space probe *Dawn* had excess friction in one reaction wheel in June 2010. It was originally scheduled to depart Vesta and begin its two-and-a-half-year journey to Ceres on August 26, 2012; however, a problem with another of the spacecraft's reaction wheels forced *Dawn* to briefly delay its departure from Vesta's gravity until September 5, 2012, and it planned to use thruster jets instead of the reaction wheels during the three-year journey to Ceres. The loss of the reaction wheels limited the camera observations on the approach to Ceres.

On the evening of Tuesday, January 18, 2022, a possible failure of one of the Swift Observatory's reaction wheels caused the mission control team to power off the suspected wheel, putting the observatory in safe mode as a precaution. This was the first time a reaction wheel failed on Swift in 17 years. Swift resumed science operations on February 17, 2022.

## Similar devices

A control moment gyroscope (CMG) is a related but different type of attitude actuator, generally consisting of a momentum wheel mounted in a one-axis or two-axis gimbal. When mounted to a rigid spacecraft, applying a constant torque to the wheel using one of the gimbal motors causes the spacecraft to develop a constant angular velocity about a perpendicular axis, thus allowing control of the spacecraft's pointing direction. CMGs are generally able to produce larger sustained torques than RWs with less motor heating, and are preferentially used in larger or more-agile (or both) spacecraft, including Skylab, Mir, and the International Space Station.
