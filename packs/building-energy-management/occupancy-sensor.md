---
title: "Occupancy sensor"
source: https://en.wikipedia.org/wiki/Occupancy_sensor
domain: building-energy-management
license: CC-BY-SA-4.0
tags: building management system, energy management system, energy audit, occupancy sensor
fetched: 2026-07-02
---

# Occupancy sensor

An **occupancy sensor** is an indoor device used to detect the presence of a person. Applications include automatic adjustment of lights or temperature or ventilation systems in response to the quantity of people present. The sensors typically use infrared, ultrasonic, microwave, or other technology. The term encompasses devices as different as PIR sensors, hotel room keycard locks and smart meters. Occupancy sensors are typically used to save energy, provide automatic control, and comply with building codes.

## Vacancy sensor

A vacancy sensor works like an occupancy sensor, however, lights must be manually turned ON, but will automatically turn OFF when motion is no longer detected.

## Sensor types

Occupancy sensor types include:

1. PIR sensors, which work on heat difference detection, measuring infrared radiation. Inside the device is a pyroelectric sensor which can detect the sudden presence of objects (such as humans) who radiate a temperature different from the temperature of the background, such as the room temperature of a wall.
2. Environmental sensors, such as temperature, humidity and CO2 sensors, which detect the change in the environment due to the presence of a human.
3. Ultrasonic sensors, similar to radar. they work on the doppler shift principle. An ultrasonic sensor will send high frequency sound waves in area and will check for their reflected patterns. If the reflected pattern is changing continuously then it assumes that there is occupancy and the lighting load connected is turned on. If the reflected pattern is the same for a preset time then the sensor assumes there is no occupancy and the load is switched off.
4. Microwave sensors. Similar to the ultrasonic sensor, a microwave sensor also works on the doppler shift principle. A microwave sensor will send high frequency microwaves in an area and will check for their reflected patterns. If the reflected pattern is changing continuously then it assumes that there is occupancy and the lighting load connected is turned on. If the reflected pattern is the same for a preset time then the sensor assumes there is no occupancy and the load is switched off. A microwave sensor has high sensitivity as well as detection range compared to other types of sensors.
5. Keycard light slots, used in a hotel energy management system to detect when a hotel room is occupied, by requiring the guest to place their keycard in a slot to activate lights and thermostats.
6. Smart meters, which work by detecting the change in power consumption patterns that exhibit distinct characteristics for occupied and vacant states.
7. Barometric Pressure sensors can be used to monitor door openings, which are associated with foot traffic, in rooms containing positive pressure, including operating rooms.
8. Door operated switch.
9. Audio detection.
10. Human sensing (via people counting) became widespread in 2020 as companies installed AI cameras and occupancy sensors to enforce social distancing and capacity limits during the COVID-19 pandemic.
11. Bluetooth Low Energy (BLE), detect occupancy by linking to nearby devices with a dedicated app, but they miss people without the app or misread presence if a device is left behind.

## Occupancy sensors for lighting control

Motion sensors are often used in indoor spaces to control electric lighting. If no motion is detected, it is assumed that the space is empty, and thus does not need to be lit. Turning off the lights in such circumstances can save substantial amounts of energy. In lighting practice occupancy sensors are sometimes also called "presence sensors" or "vacancy sensors". Some occupancy sensors (e.g. LSG's Pixelview, Philips Lumimotion, Ecoamicatechs Sirius etc.) also classify the number of occupants, their direction of motion, etc., through image processing. Pixelview is a camera-based occupancy sensor, using a camera that is built into each light fixture.

### System design and components

Occupancy sensors for lighting control typically use infrared (IR), ultrasonic, tomographic motion detection, microwave sensors, or camera-based sensors (image processing). The field of view of the sensor must be carefully selected/adjusted so that it responds only to motion in the space served by the controlled lighting. For example, an occupancy sensor controlling lights in an office should not detect motion in the corridor outside the office. Tomographic motion detection systems have the unique benefit of detecting motion through walls and obstructions, yet do not trigger as easily from motion on the outside of the detection area like traditional microwave sensors.

Sensors and their placement are never perfect, therefore most systems incorporate a delay time before switching. This delay time is often user-selectable, but a typical default value is 15 minutes. This means that the sensor must detect no motion for the entire delay time before the lights are switched. Most systems switch lights off at the end of the delay time, but more sophisticated systems with dimming technology reduce lighting slowly to a minimum level (or zero) over several minutes, to minimize the potential disruption in adjacent spaces. If lights are off and an occupant re-enters a space, most current systems switch lights back on when motion is detected. However, systems designed to switch lights off automatically with no occupancy, and that require the occupant to switch lights on when they re-enter are gaining in popularity due to their potential for increased energy savings. These savings accrue because in a spaces with access to daylight the occupant may decide on their return that they no longer require supplemental electric light.

Originally invented by Kevin D. Fraser of San Francisco. The prototype utilized existing ultrasonic intrusion alarm technology coupled to conventional industrial timers, with basic switching elements. First prototype was crafted on a plywood base; the first model required a separate transmitter and receiver processing 20,200 cycles per second of sound energy. Mr. Fraser was employed by and developed the device for the Embarcadero Center high-rise office complex in San Francisco, and as such employee did not profit from the invention. He took the concept to Unisec security devices and had them build a single piece transceiver based on 277VAC - the level of electricity used for commercial lighting in the Embarcadero Center complex. Four hundred of these units were installed under a newly named UNENCO brand, and installed in the bathrooms of the four high-rise towers. This was an immediate success. This application received Congressional Mention for Kevin Fraser's efforts, as well as various Pacific Gas & Electric awards. Noted local columnist Herb Cain made mention that one should not sit too long in the stalls at Embarcadero Center, and the word caught on regarding the technology. While not receiving a patent, Mr. Fraser was acknowledged by the Association of Energy Engineers (AEE) as the inventor.
