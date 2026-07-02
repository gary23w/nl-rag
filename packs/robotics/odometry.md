---
title: "Odometry"
source: https://en.wikipedia.org/wiki/Odometry
domain: robotics
license: CC-BY-SA-4.0
tags: robotics, robot, ros, slam, kinematics, path planning, odometry
fetched: 2026-07-02
---

# Odometry

**Odometry** is the use of data from motion sensors to estimate change in position over time. It is used in robotics by some legged or wheeled robots to estimate their position relative to a starting location. This method is sensitive to errors due to the integration of velocity measurements over time to give position estimates. Rapid and accurate data collection, instrument calibration, and processing are required in most cases for odometry to be used effectively.

The word *odometry* is composed of the Greek words *odos* (meaning "route") and *metron* (meaning "measure").

## Example

Suppose a robot has rotary encoders on its wheels or on its legged joints. It drives forward for some time and then would like to know how far it has traveled. It can measure how far the wheels have rotated, and if it knows the circumference of its wheels, compute the distance.

Train operations are also frequent users of odometrics. Typically, a train gets an absolute position by passing over stationary sensors in the tracks, while odometry is used to calculate relative position while the train is between the sensors.

## More sophisticated example

Suppose a simple robot has two wheels, both capable of moving forward or in reverse, positioned parallel to each other and equidistant from the robot's center. Additionally, each motor has a rotary encoder, allowing determination of whether either wheel has traveled one "unit" forward or reverse along the floor. This unit is defined as the ratio of the wheel's circumference to the encoder's resolution.

If the left wheel were to move forward one unit while the right wheel remained stationary, then the right wheel acts as a pivot, and the left wheel traces a circular arc in the clockwise direction. Since one's unit of distance is usually tiny, one can approximate by assuming that this arc is a line. Thus, the original position of the left wheel, the final position of the left wheel, and the position of the right wheel form a triangle, which one can call *A*.

Also, the original position of the center, the final position of the center, and the position of the right wheel form a triangle which one can call *B*. Since the center of the robot is equidistant to either wheel, and as they share the angle formed at the right wheel, triangles *A* and *B* are similar triangles. In this situation, the magnitude of the change of position of the center of the robot is one half of a unit. The angle of this change can be determined using the law of sines.
