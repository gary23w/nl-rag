---
title: "Spacecraft attitude determination and control"
source: https://en.wikipedia.org/wiki/Spacecraft_attitude_control
domain: spacecraft-guidance
license: CC-BY-SA-4.0
tags: spacecraft guidance, star tracker, attitude control, reaction control system
fetched: 2026-07-02
---

# Spacecraft attitude determination and control

(Redirected from

Spacecraft attitude control

)

**Spacecraft attitude control** is the process of controlling the orientation of a spacecraft (vehicle or satellite) with respect to an inertial frame of reference or another entity such as the celestial sphere, certain fields, and nearby objects, etc.

Controlling vehicle attitude requires actuators to apply the torques needed to orient the vehicle to a desired attitude, and algorithms to command the actuators based on the current attitude and specification of a desired attitude.

Before and during attitude control can be performed, **spacecraft attitude determination** must be performed, which requires sensors for absolute or relative measurement.

The broader integrated field that studies the combination of sensors, actuators and algorithms is called *guidance, navigation and control*, which also involves non-attitude concepts, such as position determination and navigation.

Spacecraft generally have an attitude determination and control system (ADCS), which includes both sensors and actuators. However, budget satellites (such as some cubesats), may elect for simpler attitude control systems (ACS) which use passive techniques, including the yo-yo de-spin technique and permanent magnets to control the attitude of the satellite.

## Motivation

A spacecraft's attitude must typically be stabilized and controlled for a variety of reasons. It is often needed so that the spacecraft high-gain antenna may be accurately pointed to Earth for communications, so that onboard experiments may accomplish precise pointing for accurate collection and subsequent interpretation of data, so that the heating and cooling effects of sunlight and shadow may be used intelligently for thermal control, and also for guidance: short propulsive maneuvers must be executed in the right direction.

Many spacecraft have components that require articulation or pointing. Voyager and *Galileo*, for example, were designed with scan platforms for pointing optical instruments at their targets largely independently of spacecraft orientation. Many spacecraft, such as Mars orbiters, have solar panels that must track the Sun so they can provide electrical power to the spacecraft. *Cassini*'s main engine nozzles were steerable. Knowing where to point a solar panel, or scan platform, or a nozzle — that is, how to articulate it — requires knowledge of the spacecraft's attitude. Because a single subsystem keeps track of the spacecraft's attitude, the Sun's location, and Earth's location, it can compute the proper direction to point the appendages. It logically falls to the same subsystem – the Attitude and Articulation Control Subsystem (AACS), then, to manage both attitude and articulation. The name AACS may even be carried over to a spacecraft even if it has no appendages to articulate.

## Background

Attitude is part of the description of how an object is placed in the space it occupies. Attitude and position fully describe how an object is placed in space. For some applications (e.g., robotics, computer vision), it is customary to combine position and attitude together into a single description known as Pose.

Attitude can be described using a variety of methods; however, the most common are Rotation matrices, Quaternions, and Euler angles. While Euler angles are oftentimes the most straightforward representation to visualize, they can cause problems for highly-maneuverable systems because of a phenomenon known as Gimbal lock. A rotation matrix, on the other hand, provides a full description of the attitude at the expense of requiring nine values instead of three. The use of a rotation matrix can lead to increased computational expense and they can be more difficult to work with. Quaternions offer a decent compromise in that they do not suffer from gimbal lock and only require four values to fully describe the attitude.

## Control

### Types of stabilization

Attitude control of spacecraft is maintained using one of two principal approaches: spin stabilization and three-axis stabilization.

#### Spin stabilization

Spin stabilization is accomplished by setting the spacecraft spinning, using the gyroscopic action of the rotating spacecraft mass as the stabilizing mechanism. Propulsion system thrusters are fired only occasionally to make desired changes in spin rate, or in the spin-stabilized attitude. If desired, the spinning may be stopped through the use of thrusters or by yo-yo de-spin. The *Pioneer 10* and *Pioneer 11* probes in the outer Solar System are examples of spin-stabilized spacecraft.

#### Three-axis stabilization

Three-axis stabilization is an alternative method of spacecraft attitude control in which the spacecraft is held fixed in the desired orientation without any rotation.

- One method is to use small thrusters to continually nudge the spacecraft back and forth within a deadband of allowed attitude error. Thrusters may also be referred to as mass-expulsion control (MEC) systems, or reaction control systems (RCS). The space probes *Voyager 1* and *Voyager 2* employ this method, and have used up about three quarters of their 100 kg of propellant as of July 2015.
- Another method for achieving three-axis stabilization is to use electrically powered reaction wheels, also called momentum wheels, which are mounted on three orthogonal axes aboard the spacecraft. They provide a means to trade angular momentum back and forth between spacecraft and wheels. To rotate the vehicle on a given axis, the reaction wheel on that axis is accelerated in the opposite direction. To rotate the vehicle back, the wheel is slowed. Excess momentum that builds up in the system due to external torques from, for example, solar photon pressure or gravity gradients, must be occasionally removed from the system by applying controlled torque to the spacecraft to allowing the wheels to return to a desired speed under computer control. This is done during maneuvers called momentum desaturation or momentum unload maneuvers. Most spacecraft use a system of thrusters to apply the torque for desaturation maneuvers. A different approach was used by the Hubble Space Telescope, which had sensitive optics that could be contaminated by thruster exhaust, and instead used magnetic torquers for desaturation maneuvers.

There are advantages and disadvantages to both spin stabilization and three-axis stabilization. Spin-stabilized craft provide a continuous sweeping motion that is desirable for fields and particles instruments, as well as some optical scanning instruments, but they may require complicated systems to de-spin antennas or optical instruments that must be pointed at targets for science observations or communications with Earth. Three-axis controlled craft can point optical instruments and antennas without having to de-spin them, but they may have to carry out special rotating maneuvers to best utilize their fields and particle instruments. If thrusters are used for routine stabilization, optical observations such as imaging must be designed knowing that the spacecraft is always slowly rocking back and forth, and not always exactly predictably. Reaction wheels provide a much steadier spacecraft from which to make observations, but they add mass to the spacecraft, they have a limited mechanical lifetime, and they require frequent momentum desaturation maneuvers, which can perturb navigation solutions because of accelerations imparted by the use of thrusters.

### Actuators

Attitude control can be obtained by several mechanisms, including:

#### Thrusters

Vernier thrusters are the most common actuators, as they may be used for station keeping as well. Thrusters must be organized as a system to provide stabilization about all three axes, and at least two thrusters are generally used in each axis to provide torque as a couple in order to prevent imparting a translation to the vehicle. Their limitations are fuel usage, engine wear, and cycles of the control valves. The fuel efficiency of an attitude control system is determined by its specific impulse (proportional to exhaust velocity) and the smallest torque impulse it can provide (which determines how often the thrusters must fire to provide precise control). Thrusters must be fired in one direction to start rotation, and again in the opposing direction if a new orientation is to be held. Thruster systems have been used on most crewed space vehicles, including Vostok, Mercury, Gemini, Apollo, Soyuz, and the Space Shuttle.

To minimize the fuel limitation on mission duration, auxiliary attitude control systems may be used to reduce vehicle rotation to lower levels, such as small ion thrusters that accelerate ionized gases electrically to extreme velocities, using power from solar cells.

#### Reaction/momentum wheels

Momentum wheels are electric motor driven rotors made to spin in the direction opposite to that required to re-orient the vehicle. Because momentum wheels make up a small fraction of the spacecraft's mass and are computer controlled, they give precise control. Momentum wheels are generally suspended on magnetic bearings to avoid bearing friction and breakdown problems. Spacecraft Reaction wheels often use mechanical ball bearings.

To maintain orientation in three dimensional space a minimum of three reaction wheels must be used, with additional units providing single failure protection. See Euler angles.

#### Control moment gyros

These are rotors spun at constant speed, mounted on gimbals to provide attitude control. Although a CMG provides control about the two axes orthogonal to the gyro spin axis, triaxial control still requires two units. A CMG is a bit more expensive in terms of cost and mass, because gimbals and their drive motors must be provided. The maximum torque (but not the maximum angular momentum change) exerted by a CMG is greater than for a momentum wheel, making it better suited to large spacecraft. A major drawback is the additional complexity, which increases the number of failure points. For this reason, the International Space Station uses a set of four CMGs to provide dual failure tolerance.

#### Solar sails

Small solar sails (devices that produce thrust as a reaction force induced by reflecting incident light) may be used to make small attitude control and velocity adjustments. This application can save large amounts of fuel on a long-duration mission by producing control moments without fuel expenditure. For example, *Mariner 10* adjusted its attitude using its solar cells and antennas as small solar sails.

#### Gravity-gradient stabilization

In orbit, a spacecraft with one axis much longer than the other two will spontaneously orient so that its long axis points at the planet's center of mass. This system has the virtue of needing no active control system or expenditure of fuel. The effect is caused by a tidal force. The upper end of the vehicle feels less gravitational pull than the lower end. This provides a restoring torque whenever the long axis is not co-linear with the direction of gravity. Unless some means of damping is provided, the spacecraft will oscillate about the local vertical. Sometimes tethers are used to connect two parts of a satellite, to increase the stabilizing torque. A problem with such tethers is that meteoroids as small as a grain of sand can part them.

#### Magnetic torquers

Coils or (on very small satellites) permanent magnets exert a moment against the local magnetic field. This method works only where there is a magnetic field against which to react. One classic field "coil" is actually in the form of a conductive tether in a planetary magnetic field. Such a conductive tether can also generate electrical power, at the expense of orbital decay. Conversely, by inducing a counter-current, using solar cell power, the orbit may be raised. Due to massive variability in Earth's magnetic field from an ideal radial field, control laws based on torques coupling to this field will be highly non-linear. Moreover, only two-axis control is available at any given time meaning that a vehicle reorient may be necessary to null all rates.

#### Passive attitude control

Three main types of passive attitude control exist for satellites. The first one uses gravity gradient, and it leads to four stable states with the long axis (axis with smallest moment of inertia) pointing towards Earth. As this system has four stable states, if the satellite has a preferred orientation, e.g. a camera pointed at the planet, some way to flip the satellite and its tether end-for-end is needed.

The second passive system orients the satellite along Earth's magnetic field thanks to a magnet. These purely passive attitude control systems have limited pointing accuracy, because the spacecraft will oscillate around energy minima. This drawback is overcome by adding damper, which can be hysteretic materials or a viscous damper. The viscous damper is a small can or tank of fluid mounted in the spacecraft, possibly with internal baffles to increase internal friction. Friction within the damper will gradually convert oscillation energy into heat dissipated within the viscous damper.

A third form of passive attitude control is aerodynamic stabilization. This is achieved using a drag gradient, as demonstrated on the Get Away Special Passive Attitude Control Satellite (GASPACS) technology demonstration. In low Earth orbit, the force due to drag is many orders of magnitude more dominant than the force imparted due to gravity gradients. When a satellite is utilizing aerodynamic passive attitude control, air molecules from the Earth's upper atmosphere strike the satellite in such a way that the center of pressure remains behind the center of mass, similar to how the feathers on an arrow stabilize the arrow. GASPACS utilized a 1 m inflatable 'AeroBoom', which extended behind the satellite, creating a stabilizing torque along the satellite's velocity vector.

Another form of passive attitude control is yo-yo de-spin. Yo-yo de-spin devices are controversial as they generate space debris, and are primarily used for deep-space spacecraft.

### Control algorithms

Control algorithms are computer programs that receive data from vehicle sensors and derive the appropriate commands to the actuators to rotate the vehicle to the desired attitude. The algorithms range from very simple, e.g. proportional control, to complex nonlinear estimators or many in-between types, depending on mission requirements. Typically, the attitude control algorithms are part of the software running on the computer hardware, which receives commands from the ground and formats vehicle data telemetry for transmission to a ground station.

The attitude control algorithms are written and implemented based on requirement for a particular attitude maneuver. Asides the implementation of passive attitude control such as the gravity-gradient stabilization, most spacecraft make use of active control which exhibits a typical attitude control loop. The design of the control algorithm depends on the actuator to be used for the specific attitude maneuver although using a simple *proportional–integral–derivative controller* (*PID controller*) satisfies most control needs.

The appropriate commands to the actuators are obtained based on error signals described as the difference between the measured and desired attitude. The error signals are commonly measured as euler angles (Φ, θ, Ψ), however an alternative to this could be described in terms of direction cosine matrix or error quaternions. The PID controller which is most common reacts to an error signal (deviation) based on attitude as follows

$T_{c}(t)=K_{\text{p}}e(t)+K_{\text{i}}\int _{0}^{t}e(\tau )\,d\tau +K_{\text{d}}{\dot {e}}(t),$

where $T_{c}$ is the control torque, e is the attitude deviation signal, and $K_{\text{p}},K_{\text{i}},K_{\text{d}}$ are the PID controller parameters.

A simple implementation of this can be the application of the proportional control for nadir pointing making use of either momentum or reaction wheels as actuators. Based on the change in momentum of the wheels, the control law can be defined in 3-axes x, y, z as

$T_{c}x=-K_{\text{q1}}q_{1}+K_{\text{w1}}{w_{x}},$

$T_{c}y=-K_{\text{q2}}q_{2}+K_{\text{w2}}{w_{y}},$

$T_{c}z=-K_{\text{q3}}q_{3}+K_{\text{w3}}{w_{z}},$

This control algorithm also affects momentum dumping.

Another important and common control algorithm involves the concept of detumbling, which is attenuating the angular momentum of the spacecraft. The need to detumble the spacecraft arises from the uncontrollable state after release from the launch vehicle. Most spacecraft in low Earth orbit (LEO) makes use of magnetic detumbling concept which utilizes the effect of the Earth's magnetic field. The control algorithm is called the B-Dot controller and relies on magnetic coils or torque rods as control actuators. The control law is based on the measurement of the rate of change of body-fixed magnetometer signals.

$m=-K{\dot {B}}$

where m is the commanded magnetic dipole moment of the magnetic torquer and K is the proportional gain and ${\dot {B}}$ is the rate of change of the Earth's magnetic field.

### Control modes

A spacecraft's ADCS system generally begins detumbling at the start of the mission, either autonomously or when commanded.

Following detumbling, ADCS systems often have several control modes, including:

- **Safe mode:** A low-power, fault-tolerant state entered during anomalies.
- **Sun pointing/sun tracking mode:** Orients the spacecraft so solar panels face the sun.
- **Nadir pointing mode:** Points a specific face toward Earth (nadir). Useful for Earth observation, downlink antennas, and Earth-facing instruments.
- **Inertial target pointing mode:** Holds a fixed inertial direction. Useful for pointing at a star or deep-space object.
- **Ground target tracking mode:** Points at a fixed or moving ground target, slewing the satellite as its position relative to the ground target changes. Useful for highly targeted Earth observation and optical data transfer systems.
- **Slew/transition modes:** Spacecraft slew slowly between modes/targets.

Nadir pointing mode and sun pointing mode, among others, are implemented by using actuators to put the spacecraft into a Y-Thomson spin, named after William T. Thomson, whereby the spacecraft completes one full rotation about its orbit normal axis as it completes one full revolution about the primary body. In a geocentric satellite, a Y-Thomson spin is often used to point one face of the spacecraft to face the center of gravity of the Earth. This spin aligns the spacecraft body frame with the orbit's tangent-normal-radial reference frame. When combined with a nadir-pointing deployable boom, gravity-gradient forces passively stabilize the spacecraft's attitude.

## Determination

*Spacecraft attitude determination* is the process of determining the orientation of a spacecraft (vehicle or satellite). It is a pre-requisite for spacecraft attitude control. A variety of sensors are utilized for relative and absolute attitude determination.

### Sensors

#### Relative attitude sensors

Many sensors generate outputs that reflect the rate of change in attitude. These require a known initial attitude, or external information to use them to determine attitude. Many of this class of sensor have some noise, leading to inaccuracies if not corrected by absolute attitude sensors.

##### Gyroscopes

Gyroscopes are devices that sense rotation in three-dimensional space without reliance on the observation of external objects. Classically, a gyroscope consists of a spinning mass, but there are also "ring laser gyros" utilizing coherent light reflected around a closed path. Another type of "gyro" is a hemispherical resonator gyro where a crystal cup shaped like a wine glass can be driven into oscillation just as a wine glass "sings" as a finger is rubbed around its rim. The orientation of the oscillation is fixed in inertial space, so measuring the orientation of the oscillation relative to the spacecraft can be used to sense the motion of the spacecraft with respect to inertial space.

##### Motion reference units

Motion reference units are a kind of inertial measurement unit with single- or multi-axis motion sensors. They utilize MEMS gyroscopes. Some multi-axis MRUs are capable of measuring roll, pitch, yaw and heave. They have applications outside the aeronautical field, such as:

- Antenna motion compensation and stabilization
- Dynamic positioning
- Heave compensation of offshore cranes
- High speed craft motion control and damping systems
- Hydro acoustic positioning
- Motion compensation of single and multibeam echosounders
- Ocean wave measurements
- Offshore structure motion monitoring
- Orientation and attitude measurements on Autonomous underwater vehicles and Remotely operated underwater vehicles
- Ship motion monitoring

#### Absolute attitude sensors

This class of sensors sense the position or orientation of fields, objects or other phenomena outside the spacecraft.

##### Horizon sensor

A *horizon sensor* is an optical instrument that detects light from the 'limb' of Earth's atmosphere, i.e., at the horizon. Thermal infrared sensing is often used, which senses the comparative warmth of the atmosphere, compared to the much colder cosmic background. This sensor provides orientation with respect to Earth about two orthogonal axes. It tends to be less precise than sensors based on stellar observation. Sometimes referred to as an Earth sensor.

##### Orbital gyrocompass

Similar to the way that a terrestrial gyrocompass uses a pendulum to sense local gravity and force its gyro into alignment with Earth's spin vector, and therefore point north, an *orbital gyrocompass* uses a horizon sensor to sense the direction to Earth's center, and a gyro to sense rotation about an axis normal to the orbit plane. Thus, the horizon sensor provides pitch and roll measurements, and the gyro provides yaw. See Tait-Bryan angles.

##### Sun sensor

A *Sun sensor* is a device that senses the direction to the Sun. This can be as simple as some solar cells and shades, or as complex as a steerable telescope, depending on mission requirements.

##### Earth sensor

An *Earth sensor* is a device that senses the direction to Earth. It is usually an infrared camera; nowadays the main method to detect attitude is the star tracker, but Earth sensors are still integrated in satellites for their low cost and reliability.

##### Star tracker

A *star tracker* is an optical device that measures the position(s) of star(s) using photocell(s) or a camera. It uses magnitude of brightness and spectral type to identify and then calculate the relative position of stars around it.

##### Magnetometer

A *magnetometer* is a device that senses magnetic field strength and, when used in a three-axis triad, magnetic field direction. As a spacecraft navigational aid, sensed field strength and direction is compared to a map of Earth's magnetic field stored in the memory of an on-board or ground-based guidance computer. If spacecraft position is known then attitude can be inferred.

### Attitude estimation

Attitude cannot be measured directly by any single measurement, and so must be calculated (or estimated) from a set of measurements (often using different sensors). This can be done either statically (calculating the attitude using only the measurements currently available), or through the use of a statistical filter (most commonly, the Kalman filter) that statistically combine previous attitude estimates with current sensor measurements to obtain an optimal estimate of the current attitude.

#### Static attitude estimation methods

Static attitude estimation methods are solutions to Wahba's problem. Many solutions have been proposed, notably Davenport's q-method, QUEST, TRIAD, and singular value decomposition.

Crassidis, John L., and John L. Junkins.. Chapman and Hall/CRC, 2004.

#### Sequential estimation methods

Kalman filtering can be used to sequentially estimate the attitude, as well as the angular rate. Because attitude dynamics (combination of rigid body dynamics and attitude kinematics) are non-linear, a linear Kalman filter is not sufficient. Because attitude dynamics is not very non-linear, the Extended Kalman filter is usually sufficient (however Crassidis and Markely demonstrated that the Unscented Kalman filter could be used, and can provide benefits in cases where the initial estimate is poor). Multiple methods have been proposed, however the Multiplicative Extended Kalman Filter (MEKF) is by far the most common approach. This approach utilizes the multiplicative formulation of the error quaternion, which allows for the unity constraint on the quaternion to be better handled. It is also common to use a technique known as dynamic model replacement, where the angular rate is not estimated directly, but rather the measured angular rate from the gyro is used directly to propagate the rotational dynamics forward in time. This is valid for most applications as gyros are typically far more precise than one's knowledge of disturbance torques acting on the system (which is required for precise estimation of the angular rate).

### Position/location determination

For some sensors and applications (such as spacecraft using magnetometers) the precise location must also be known. While pose estimation can be employed, for spacecraft it is usually sufficient to estimate the position (via Orbit determination) separate from the attitude estimation. For terrestrial vehicles and spacecraft operating near the Earth, the advent of Satellite navigation systems allows for precise position knowledge to be obtained easily. This problem becomes more complicated for deep space vehicles, or terrestrial vehicles operating in Global Navigation Satellite System (GNSS) denied environments (see Navigation).
