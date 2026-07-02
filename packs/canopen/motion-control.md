---
title: "Motion control"
source: https://en.wikipedia.org/wiki/Motion_control
domain: canopen
license: CC-BY-SA-4.0
tags: canopen protocol, canopen fieldbus, can bus higher-layer, embedded device network
fetched: 2026-07-02
---

# Motion control

**Motion control** is a sub-field of automation, encompassing the systems or sub-systems involved in moving parts of machines in a controlled manner. Motion control systems are extensively used in a variety of fields for automation purposes, including precision engineering, micromanufacturing, biotechnology, and nanotechnology. The main components involved typically include a motion controller, an energy amplifier, and one or more prime movers or actuators. Motion control may be open loop or closed loop. In open loop systems, the controller sends a command through the amplifier to the prime mover or actuator, and does not know if the desired motion was actually achieved. Typical systems include stepper motor or fan control. For tighter control with more precision, a measuring device may be added to the system (usually near the end motion). When the measurement is converted to a signal that is sent back to the controller, and the controller compensates for any error, it becomes a Closed loop System.

Typically the position or velocity of machines are controlled using some type of device such as a hydraulic pump, linear actuator, or electric motor, generally a servo. Motion control is an important part of robotics and CNC machine tools, however in these instances it is more complex than when used with specialized machines, where the kinematics are usually simpler. The latter is often called General Motion Control (GMC). Motion control is widely used in the packaging, printing, textile, semiconductor production, and assembly industries. Motion Control encompasses every technology related to the movement of objects. It covers every motion system from micro-sized systems such as silicon-type micro induction actuators to micro-siml systems such as a space platform. But, these days, the focus of motion control is the special control technology of motion systems with electric actuators such as dc/ac servo motors. Control of robotic manipulators is also included in the field of motion control because most of robotic manipulators are driven by electrical servo motors and the key objective is the control of motion.

## Overview

The basic architecture of a motion control system contains:

- A motion controller, which calculates and controls the mechanical trajectories (motion profile) an actuator must follow (*i.e.*, motion planning) and, in closed loop systems, employs feedback to make control corrections and thus implement closed-loop control.
- A drive or amplifier to transform the control signal from the motion controller into energy that is presented to the actuator. Newer "intelligent" drives can close the position and velocity loops internally, resulting in much more accurate control.
- A prime mover or actuator such as a hydraulic pump, pneumatic cylinder, linear actuator, or electric motor for output motion.
- In closed loop systems, one or more feedback sensors such as absolute and incremental encoders, resolvers or Hall effect devices to return the position or velocity of the actuator to the motion controller in order to close the position or velocity control loops.
- Mechanical components to transform the motion of the actuator into the desired motion, including: gears, shafting, ball screw, belts, linkages, and linear and rotational bearings.

The interface between the motion controller and drives it control is very critical when coordinated motion is required, as it must provide tight synchronization. Historically the only open interface was an analog signal, until open interfaces were developed that satisfied the requirements of coordinated motion control, the first being SERCOS in 1991 which is now enhanced to SERCOS III. Later interfaces capable of motion control include Ethernet/IP, Profinet IRT, Ethernet Powerlink, and EtherCAT.

Common control functions include:

- Velocity control.
- Position (point-to-point) control: There are several methods for computing a motion trajectory. These are often based on the velocity profiles of a move such as a triangular profile, trapezoidal profile, or an S-curve profile.
- Pressure or force control.
- Impedance control: This type of control is suitable for environment interaction and object manipulation, such as in robotics.
- Electronic gearing (or cam profiling): The position of a slave axis is mathematically linked to the position of a master axis. A good example of this would be in a system where two rotating drums turn at a given ratio to each other. A more advanced case of electronic gearing is electronic camming. With electronic camming, a slave axis follows a profile that is a function of the master position. This profile need not be salted, but it must be an animated function
