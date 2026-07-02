---
title: "Vibrating structure gyroscope"
source: https://en.wikipedia.org/wiki/Vibrating_structure_gyroscope
domain: gyroscope-mems
license: CC-BY-SA-4.0
tags: gyroscope sensor, vibrating structure gyroscope, coriolis force, ring laser gyroscope
fetched: 2026-07-02
---

# Vibrating structure gyroscope

A **vibrating structure gyroscope** (**VSG**), defined by the IEEE as a **Coriolis vibratory gyroscope** (**CVG**), is a gyroscope that uses a vibrating (as opposed to rotating) structure as its orientation reference. A VSG functions much like the halteres of flies (insects in the order Diptera).

The underlying physical principle is that a vibrating object tends to continue vibrating in the same plane even if its support rotates. The Coriolis effect causes the object to exert a force on its support, and by measuring this force the rate of rotation can be determined.

Vibrating structure gyroscopes are simpler and cheaper than conventional rotating gyroscopes of similar accuracy. Inexpensive VSGs manufactured with micro-electromechanical systems (MEMS) technology are widely used in smartphones, gaming devices, cameras and many other applications.

## Theory of operation

Consider two proof masses vibrating in plane (as in a MEMS gyro) at frequency $\omega _{r}$ . The Coriolis effect induces an acceleration on the proof masses equal to $a_{\mathrm {c} }=2(\Omega \times v)$ , where v is the velocity and $\Omega$ is the angular rate of rotation. The in-plane velocity of the proof masses is given by $v=x_{\text{ip}}\omega _{r}\cos(\omega _{r}t)$ , if the in-plane position at time t is given by $x_{\text{ip}}=\sin(\omega _{r}t)$ . The out-of-plane motion $y_{\text{op}}$ , induced by rotation, is given by:

$y_{\text{op}}={\frac {F_{c}}{k_{\text{op}}}}={\frac {1}{k_{\text{op}}}}2m\Omega x_{\text{ip}}\omega _{r}\cos(\omega _{r}t)$

where

$F_{c}$

is the Coriolis force,

$k_{\text{op}}$

is the

spring constant

in the out-of-plane direction,

m

is the mass of a proof mass, and

$\Omega$

is the magnitude of a

rotation vector

in the plane of and perpendicular to the driven proof mass motion.

By measuring $y_{\text{op}}$ , the rate of rotation $\Omega$ can thus be determined.

## Implementations

### Cylindrical resonator gyroscope (CRG)

This type of gyroscope was developed by GEC-Marconi and Ferranti in the 1980s using metal alloys with attached piezoelectric elements and a single-piece piezoceramic design. In the 1990s, CRGs with magneto-electric excitation and readout were produced by American-based Inertial Engineering, Inc. in California, and piezoceramic variants by Watson Industries. A recently-patented variant by Innalabs uses a cylindrical resonator design made from Elinvar alloy with piezoceramic elements for excitation and pickoff at its bottom.

This technology gave a substantially increased product life (MTBF > 500,000 hours); its shock resistance (>300g) should qualify it for *tactical* (mid-accuracy) applications.

The resonator is operated in its second-order resonant mode. The Q factor is usually about 20,000; that predetermines its noise and angular random walks. Standing waves are elliptically-shaped oscillations with four antinodes and four nodes located circumferentially along the rim.

The angle between two adjacent antinode–node pairs is 45 degrees. One of the elliptical resonant modes is excited to a prescribed amplitude. When the device rotates about its sensitive axis (along its inner stem), the resulting Coriolis forces acting on the resonator's vibrating mass elements excite the second resonant mode. The angle between major axes of the two modes is also 45 degrees.

A closed loop drives the second resonant mode to zero, and the force required to null this mode is proportional to the input rotation rate. This control loop is designated the *force-rebalanced mode*.

Piezoelectric elements on the resonator produce forces and sense induced motions. This electromechanical system provides the low output noise and large dynamic range that demanding applications require, but suffers from intense acoustic noises and high overloads.

### Piezoelectric gyroscopes

A piezoelectric material can be induced to vibrate, and lateral motion due to Coriolis force can be measured to produce a signal related to the rate of rotation.

### Tuning fork gyroscope

This type of gyroscope uses a pair of test masses driven to resonance. Their displacement from the plane of oscillation is measured to produce a signal related to the system's rate of rotation.

Frederick William Meredith registered a patent for such a device in 1942 while working at the Royal Aircraft Establishment (RAE). Further development was carried out at the RAE in 1958 by G. H. Hunt and A. E. W. Hobbs, who demonstrated drift of less than one degree per hour, or (2.78×10−4)°/s.

Modern variants of tactical gyroscopes use doubled tuning forks such as those produced by American manufacturer Systron Donner in California and French manufacturer Safran.

### Wine-glass resonator

Also called a hemispherical resonator gyroscope or HRG, a wine-glass resonator uses a thin solid-state hemisphere anchored by a thick stem. The hemisphere with its stem is driven to flexural resonance and the nodal points are measured to detect rotation. There are two basic variants of such a system: one based on a rate regime of operation (*force-to-rebalance mode*) and another variant based on an integrating regime of operation (*whole-angle mode*). Usually, the latter one is used in combination with a controlled parametric excitation. It is possible to use both regimes with the same hardware, which is a feature unique to these gyroscopes.

For a single-piece design (i.e., the hemispherical cup and stem(s) form a monolithic part) made from high-purity quartz glass, it is possible to reach a Q factor greater than 30–50 million in vacuum, so the corresponding random walks are extremely low. The Q is limited by the coating, an extremely thin film of gold or platinum, and by fixture losses. Such resonators have to be fine-tuned by ion-beam micro-erosion of the glass or by laser ablation. Engineers and researchers in several countries have been working on further improvements of these sophisticated state-of-art technologies.

Safran and Northrop Grumman are major manufacturers of HRGs.

### Vibrating wheel gyroscope

A wheel is driven to rotate a fraction of a full turn about its axis. The tilt of the wheel is measured to produce a signal related to the rate of rotation.

## MEMS gyroscopes

Inexpensive vibrating structure microelectromechanical systems (MEMS) gyroscopes have become widely available. These are packaged similarly to other integrated circuits and may provide either analogue or digital outputs. In many cases, a single part includes gyroscopic sensors for multiple axes. Some parts incorporate multiple gyroscopes and accelerometers (or multiple-axis gyroscopes and accelerometers), to achieve output that has six full degrees of freedom. These units are called inertial measurement units, or IMUs. Panasonic, Bosch, InvenSense, Seiko Epson, Sensonor, Hanking Electronics, STMicroelectronics, Freescale Semiconductor, and Analog Devices are major manufacturers.

Internally, MEMS gyroscopes use micro-lithographically constructed versions of one or more of the mechanisms outlined above (tuning forks, vibrating wheels, or various designs, similar to TFGs, CRGs, or HRGs).

MEMS gyroscopes are used in automotive roll-over prevention and airbag systems, image stabilization, and many other potential applications.

## Applications

### Automotive

Automotive yaw sensors can be built around vibrating structure gyroscopes. These are used to detect error states in yaw compared to a predicted response when connected as an input to electronic stability control systems in conjunction with a steering wheel sensor. Advanced systems could conceivably offer rollover detection based on a second VSG, but it is cheaper to add longitudinal and vertical accelerometers to the existing lateral one to this end.

### Entertainment

The Nintendo Game Boy Advance game WarioWare: Twisted! uses a piezoelectric gyroscope to detect rotational movement. The Sony Sixaxis PS3 controller uses a single MEMS gyroscope to measure the sixth axis (yaw). The Nintendo Wii MotionPlus accessory uses multi-axis MEMS gyroscopes provided by InvenSense to augment the motion sensing capabilities of the Wii Remote. Most modern smartphones and gaming devices also feature MEMS gyroscopes.

### Hobbies

Vibrating structure gyroscopes are commonly used in radio-controlled helicopters to help control the helicopter's tail rotor and in radio-controlled airplanes to help keep the attitude steady during flight. They are also used in multirotor flight controllers, since multirotors are inherently aerodynamically unstable and cannot stay airborne without electronic stabilization.

### Industrial robotics

Epson Robots uses a quartz MEMS gyroscope, called QMEMS, to detect and control vibrations on their robots. This helps the robots position the robot end effector with high precision in high speed and fast-deceleration motion.

### Photography

Many image stabilization systems on video and still cameras employ vibrating structure gyroscopes.

### Spacecraft orientation

Oscillation can also be induced and controlled in vibrating structure gyroscopes for the positioning of spacecraft such as *Cassini–Huygens*. These small hemispherical resonator gyroscopes made of quartz glass operate in vacuum. There are also prototypes of elastically-decoupled cylindrical resonator gyroscopes (CRGs) made from high-purity single-crystalline sapphire. The high-purity leuko-sapphire has a Q factor an order of value greater than quartz glass used for HRG, but this material is hard and has anisotropy. They provide accurate three-axis positioning of the spacecraft and are highly reliable over the years, as they have no moving parts.

### Other

The Segway uses a vibrating structure gyroscope made by Silicon Sensing Systems to stabilize the operator platform.
