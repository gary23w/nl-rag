---
title: "Guidance, navigation, and control"
source: https://en.wikipedia.org/wiki/Guidance,_navigation,_and_control
domain: spacecraft-guidance
license: CC-BY-SA-4.0
tags: spacecraft guidance, star tracker, attitude control, reaction control system
fetched: 2026-07-02
---

# Guidance, navigation, and control

**Guidance, navigation and control** (abbreviated **GNC**, **GN&C**, or **G&C**) is a branch of engineering dealing with the design of systems to control the movement of vehicles, especially, automobiles, ships, aircraft, and spacecraft. In many cases these functions can be performed by trained humans. However, because of the speed of, for example, a rocket's dynamics, human reaction time is too slow to control this movement. Therefore, systems—now almost exclusively digital electronic—are used for such control. Even in cases where humans can perform these functions, it is often the case that GNC systems provide benefits such as alleviating operator work load, smoothing turbulence, fuel savings, etc. In addition, sophisticated applications of GNC enable automatic or remote control.

- *Guidance* refers to the determination of the desired path of travel (the "trajectory") from the vehicle's current location to a designated target, as well as desired changes in velocity, rotation and acceleration for following that path.

- *Navigation* refers to the determination, at a given time, of the vehicle's location and velocity (the "state vector") as well as its attitude.
- *Control* refers to the manipulation of the forces, by way of steering controls, thrusters, etc., needed to execute guidance commands while maintaining vehicle stability.

## Parts

Guidance, navigation, and control systems consist of 3 essential parts: *navigation* which tracks current location, *guidance* which leverages navigation data and target information to direct flight control "where to go", and *control* which accepts guidance commands to affect change in aerodynamic and/or engine controls.

**Navigation**

is the art of determining where you are, a science that has seen tremendous focus in 1711 with the

Longitude prize

. Navigation aids either measure position from a

fixed

point of reference (ex. landmark, north star, LORAN Beacon),

relative

position to a target (ex. radar, infra-red, ...) or track

movement

from a known position/starting point (e.g. IMU). Today's complex systems use multiple approaches to determine current position. For example, today's most advanced navigation systems are embodied within the

Anti-ballistic missile

, the

RIM-161 Standard Missile 3

leverages GPS, IMU and

ground segment

data in the boost phase and relative position data for intercept targeting. Complex systems typically have multiple redundancy to address drift, improve accuracy (ex. relative to a target) and address isolated system failure. Navigation systems therefore take multiple inputs from many different sensors, both internal to the system and/or external (ex. ground based update).

Kalman filter

provides the most common approach to combining navigation data (from multiple sensors) to resolve current position.

**Guidance**

is the "driver" of a vehicle. It takes input from the navigation system (where am I) and uses targeting information (where do I want to go) to send signals to the flight control system that will allow the vehicle to reach its destination (within the operating constraints of the vehicle). The "targets" for guidance systems are one or more state vectors (position and velocity) and can be inertial or relative. During powered flight, guidance is continually calculating steering directions for flight control. For example, the

Space Shuttle

targets an altitude, velocity vector, and gamma to drive main engine cut off. Similarly, an

Intercontinental ballistic missile

also targets a vector. The target vectors are developed to fulfill the mission and can be preplanned or dynamically created.

**Control**

Flight control is accomplished either aerodynamically or through powered controls such as engines. Guidance sends signals to flight control. A Digital Autopilot (DAP) is the interface between guidance and control. Guidance and the DAP are responsible for calculating the precise instruction for each flight control. The DAP provides feedback to guidance on the state of flight controls.

## Examples

GNC systems are found in essentially all autonomous or semi-autonomous systems. These include:

- Autopilots
- Driverless cars, like Mars rovers or those participating in the DARPA Grand Challenge
- Guided missiles
- Precision-guided airdrop systems
- Reaction control systems for spacecraft
- Spacecraft launch vehicles
- Unmanned aerial vehicles
- Auto-steering tractors
- Autonomous underwater vehicle

Related examples are:

- Celestial navigation is a position fixing technique that was devised to help sailors cross the featureless oceans without having to rely on dead reckoning to enable them to strike land. Celestial navigation uses angular measurements (sights) between the horizon and a common celestial object. The Sun is most often measured. Skilled navigators can use the Moon, planets or one of 57 navigational stars whose coordinates are tabulated in nautical almanacs. Historical tools include a sextant, watch and ephemeris data. Most interplanetary spacecraft nowadays use optical systems to calibrate inertial navigation systems: Crewman Optical Alignment Sight (COAS), Star Tracker.
- Inertial Measurement Units (IMUs) are the primary inertial system for maintaining current position (navigation) and orientation in missiles and aircraft. They are complex machines with one or more rotating Gyroscopes that can rotate freely in 3 degrees of motion within a complex gimbal system. IMUs are "spun up" and calibrated prior to launch. A minimum of 3 separate IMUs are in place within most complex systems. In addition to relative position, the IMUs contain accelerometers which can measure acceleration in all axes. The position data, combined with acceleration data provide the necessary inputs to "track" motion of a vehicle. IMUs have a tendency to "drift", due to friction and accuracy. Error correction to address this drift can be provided via ground link telemetry, GPS, radar, optical celestial navigation and other navigation aids. When targeting another (moving) vehicle, relative vectors become paramount. In this situation, navigation aids which provide updates of position *relative to the target* are more important. In addition to the current position, inertial navigation systems also typically estimate a predicted position for future computing cycles. See also Inertial navigation system.
- Astro-inertial guidance is a sensor fusion/information fusion of the Inertial guidance and Celestial navigation.
- Long-range Navigation (LORAN) : This was the predecessor of GPS and was (and to an extent still is) used primarily in commercial sea transportation. The system works by triangulating the ship's position based on directional reference to known transmitters.
- Global Positioning System (GPS) : GPS was designed by the US military with the primary purpose of addressing "drift" within the inertial navigation of Submarine-launched ballistic missile(SLBMs) prior to launch. GPS transmits 2 signal types: military and a commercial. The accuracy of the military signal is classified but can be assumed to be well under 0.5 meters. The GPS system space segment is composed of 24 to 32 satellites in medium Earth orbit at an altitude of approximately 20,200 km (12,600 mi). The satellites are in six specific orbits and transmit highly accurate time and satellite location information which can be used to derive distances and calculate position.

- Radar/Infrared/Laser : This form of navigation provides information to guidance *relative to a known target*, it has both civilian (ex rendezvous) and military applications.
  - active (employs own radar to illuminate the target),
  - passive (detects target's radar emissions),
  - semiactive radar homing,
  - Infrared homing : This form of guidance is used exclusively for military munitions, specifically air-to-air and surface-to-air missiles. The missile's seeker head homes in on the infrared (heat) signature from the target's engines (hence the term "heat-seeking missile"),
  - Ultraviolet homing, used in FIM-92 Stinger - more resistive to countermeasures, than IR homing system
  - Laser guidance : A laser designator device calculates relative position to a highlighted target. Most are familiar with the military uses of the technology on Laser-guided bomb. The space shuttle crew leverages a hand held device to feed information into rendezvous planning. The primary limitation on this device is that it requires a line of sight between the target and the designator.
  - Terrain contour matching (TERCOM). Uses a ground scanning radar to "match" topography against digital map data to fix current position. Used by cruise missiles such as the Tomahawk (missile family).
