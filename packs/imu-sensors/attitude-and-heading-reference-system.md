---
title: "Attitude and heading reference system"
source: https://en.wikipedia.org/wiki/Attitude_and_heading_reference_system
domain: imu-sensors
license: CC-BY-SA-4.0
tags: inertial measurement unit, sensor fusion, attitude heading reference, dead reckoning
fetched: 2026-07-02
---

# Attitude and heading reference system

An **attitude and heading reference system** (**AHRS**) consists of sensors on three axes that provide attitude information for aircraft, including roll, pitch, and yaw. These are sometimes referred to as **MARG** (Magnetic, Angular Rate, and Gravity) sensors and consist of either solid-state or microelectromechanical systems (MEMS) gyroscopes, accelerometers and magnetometers. They are designed to replace traditional mechanical gyroscopic flight instruments.

The main difference between an Inertial measurement unit (IMU) and an AHRS is the addition of an on-board processing system in an AHRS, which provides attitude and heading information. This is in contrast to an IMU, which delivers sensor data to an additional device that computes attitude and heading. With sensor fusion, drift from the gyroscopes integration is compensated for by reference vectors, namely gravity, and the Earth's magnetic field. This results in a drift-free orientation, making an AHRS a more cost effective solution than conventional high-grade IMUs that only integrate gyroscopes and rely on a high bias stability of the gyroscopes. In addition to attitude determination an AHRS may also form part of an inertial navigation system.

A form of non-linear estimation such as an Extended Kalman filter is typically used to compute the solution from these multiple sources.

AHRS is reliable and is common in commercial and business aircraft. AHRS is typically integrated with electronic flight instrument systems (EFIS) which are the central part of glass cockpits, to form the primary flight display. AHRS can be combined with air data computers to form an Air data, attitude and heading reference system (ADAHRS), which provide additional information such as airspeed, altitude and outside air temperature.
