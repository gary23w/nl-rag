---
title: "Time-of-flight camera"
source: https://en.wikipedia.org/wiki/Time-of-flight_camera
domain: proximity-sensors
license: CC-BY-SA-4.0
tags: proximity sensor, photoelectric sensor, passive infrared sensor, capacitive displacement sensor
fetched: 2026-07-02
---

# Time-of-flight camera

A **time-of-flight camera** (**ToF camera**), also known as **time-of-flight sensor** (**ToF sensor**), is a range imaging camera system for measuring distances between the camera and the subject for each point of the image based on time-of-flight, the round trip time of an artificial light signal, as provided by a laser or an LED. Laser-based time-of-flight cameras are part of a broader class of scannerless LIDAR, in which the entire scene is captured with each laser pulse, as opposed to point-by-point with a laser beam such as in scanning LIDAR systems. Time-of-flight camera products for civil applications began to emerge around 2000, as the semiconductor processes allowed the production of components fast enough for such devices. The systems cover ranges of a few centimeters up to several kilometers.

## Types of devices

Several different technologies for time-of-flight cameras have been developed.

### RF-modulated light sources with phase detectors

Photonic Mixer Devices (PMD), the Swiss Ranger, and CanestaVision work by modulating the outgoing beam with an RF carrier, then measuring the phase shift of that carrier on the receiver side. This approach has a modular error challenge: measured ranges are modulo the RF carrier wavelength. The Swiss Ranger is a compact, short-range device, with ranges of 5 or 10 meters and a resolution of 176 x 144 pixels. With phase unwrapping algorithms, the maximum uniqueness range can be increased. The PMD can provide ranges up to 60 m. Illumination is pulsed LEDs rather than a laser. More recent CW-ToF camera systems illuminate the scene with high-frequency modulated LED light and analyze the phase shift of the returning signal at each pixel to compute depth. For example, in traffic enforcement applications, retroreflective surfaces such as license plates and vehicle reflectors generate strong return signals that are used to construct depth images over time. These images allow tracking of vehicle positions in 3D space and calculation of speed by applying regression analysis to the position-time data. Unlike conventional RADAR, this method measures speed along the vehicle's true direction of travel and is independent of the vehicle’s distance and angle relative to the camera. In some continuous-wave ToF systems, depth images captured over successive time intervals are used to estimate the 3D positions of moving objects, such as vehicles. The system tracks multiple retroreflective points across consecutive frames and reconstructs the object’s trajectory through 3D space. By applying regression analysis to the change in position over time, the system accurately determines the object's speed along its path of travel. Unlike conventional RADAR, this approach minimizes errors associated with distance and angle to the target. CanestaVision developer Canesta was purchased by Microsoft in 2010. The Kinect2 for Xbox One was based on ToF technology from Canesta.

### Range gated imagers

These devices have a built-in shutter in the image sensor that opens and closes at the same rate as the light pulses are sent out. Most time-of-flight 3D sensors are based on this principle invented by Medina. Because part of every returning pulse is blocked by the shutter according to its time of arrival, the amount of light received relates to the distance the pulse has traveled. The distance can be calculated using the equation, *z* = *R* (*S2* − *S1*) / 2(*S1* + *S2*) + *R* / 2 for an ideal camera. *R* is the camera range, determined by the round trip of the light pulse, *S1* the amount of the light pulse that is received, and *S2* the amount of the light pulse that is blocked.

The ZCam by 3DV Systems is a range-gated system. Microsoft purchased 3DV in 2009. Microsoft's second-generation Kinect sensor was developed using knowledge gained from Canesta and 3DV Systems.

Similar principles are used in the ToF camera line developed by the Fraunhofer Institute of Microelectronic Circuits and Systems and TriDiCam. These cameras employ photodetectors with a fast electronic shutter.

The depth resolution of ToF cameras can be improved with ultra-fast gating intensified CCD cameras. These cameras provide gating times down to 200ps and enable ToF setup with sub-millimeter depth resolution.

Range gated imagers can also be used in 2D imaging to suppress anything outside a specified distance range, such as to see through fog. A pulsed laser provides illumination, and an optical gate allows light to reach the imager only during the desired time period.

### Direct Time-of-Flight imagers

These devices measure the direct time-of-flight required for a single laser pulse to leave the camera and reflect back onto the focal plane array. Also known as "trigger mode", the 3D images captured using this methodology image complete spatial and temporal data, recording full 3D scenes with single laser pulse. This allows rapid acquisition and rapid real-time processing of scene information. For time-sensitive autonomous operations, this approach has been demonstrated for autonomous space testing and operation such as used on the OSIRIS-REx Bennu asteroid sample and return mission and autonomous helicopter landing.

Advanced Scientific Concepts, Inc. provides application specific (e.g. aerial, automotive, space) Direct TOF vision systems known as 3D Flash LIDAR cameras. Their approach utilizes InGaAs Avalanche Photo Diode (APD) or PIN photodetector arrays capable of imaging laser pulse in the 980 nm to 1600 nm wavelengths.

## Components

A time-of-flight camera consists of the following components:

- **Illumination unit:** It illuminates the scene. For RF-modulated light sources with phase detector imagers, the light has to be modulated with high speeds up to 100 MHz, only LEDs or laser diodes are feasible. For Direct TOF imagers, a single pulse per frame (e.g. 30 Hz) is used. The illumination normally uses infrared light to make the illumination unobtrusive.
- **Optics:** A lens gathers the reflected light and images the environment onto the image sensor (focal plane array). An optical band-pass filter only passes the light with the same wavelength as the illumination unit. This helps suppress non-pertinent light and reduce noise.
- **Image sensor:** This is the heart of the TOF camera. Each pixel measures the time the light has taken to travel from the illumination unit (laser or LED) to the object and back to the focal plane array. Several different approaches are used for timing; see *Types of devices* above.
- **Driver electronics:** Both the illumination unit and the image sensor have to be controlled by high speed signals and synchronized. These signals have to be very accurate to obtain a high resolution. For example, if the signals between the illumination unit and the sensor shift by only 10 picoseconds, the distance changes by 1.5 mm. For comparison: current CPUs reach frequencies of up to 3 GHz, corresponding to clock cycles of about 300 ps - the corresponding 'resolution' is only 45 mm.
- **Computation/Interface:** The distance is calculated directly in the camera. To obtain good performance, some calibration data is also used. The camera then provides a distance image over some interface, for example USB or Ethernet.

## Principle

The simplest version of a time-of-flight camera uses *light pulses* or a single light pulse. The illumination is switched on for a very short time, the resulting light pulse illuminates the scene and is reflected by the objects in the field of view. The camera lens gathers the reflected light and images it onto the sensor or focal plane array. Depending upon the distance, the incoming light experiences a delay. As light has a speed of approximately c = 300,000,000 meters per second, this delay is very short: an object 2.5 m away will delay the light by:

$t_{D}=2\cdot {\frac {D}{c}}=2\cdot {\frac {2.5\;\mathrm {m} }{300\;000\;000\;{\frac {\mathrm {m} }{\mathrm {s} }}}}=0.000\;000\;016\;66\;\mathrm {s} =16.66\;\mathrm {ns}$

For amplitude modulated arrays, the pulse width of the illumination determines the maximum range the camera can handle. With a pulse width of e.g. 50 ns, the range is limited to

$D_{\mathrm {max} }={\frac {1}{2}}\cdot c\cdot t_{0}={\frac {1}{2}}\cdot 300\;000\;000\;{\frac {\mathrm {m} }{\mathrm {s} }}\cdot 0.000\;000\;05\;\mathrm {s} =\!\ 7.5\;\mathrm {m}$

These short times show that the illumination unit is a critical part of the system. Only with special LEDs or lasers is it possible to generate such short pulses.

The single pixel consists of a photo sensitive element (e.g. a photo diode). It converts the incoming light into a current. In analog timing imagers, connected to the photo diode are fast switches, which direct the current to one of two (or several) memory elements (e.g. a capacitor) that act as summation elements. In digital timing imagers, a time counter, that can be running at several gigahertz, is connected to each photodetector pixel and stops counting when light is sensed.

In the diagram of an amplitude modulated array analog timer, the pixel uses two switches (G1 and G2) and two memory elements (S1 and S2). The switches are controlled by a pulse with the same length as the light pulse, where the control signal of switch G2 is delayed by exactly the pulse width. Depending on the delay, only part of the light pulse is sampled through G1 in S1, the other part is stored in S2. Depending on the distance, the ratio between S1 and S2 changes as depicted in the drawing. Because only small amounts of light hit the sensor within 50 ns, not only one but several thousand pulses are sent out (repetition rate tR) and gathered, thus increasing the signal-to-noise ratio.

After the exposure, the pixel is read out and the following stages measure the signals S1 and S2. As the length of the light pulse is defined, the distance can be calculated with the formula:

$D={\frac {1}{2}}\cdot c\cdot t_{0}\cdot {\frac {S2}{S1+S2}}$

In the example, the signals have the following values: S1 = 0.66 and S2 = 0.33. The distance is therefore:

$D=7.5\;\mathrm {m} \cdot {\frac {0.33}{0.33+0.66}}=2.5\;\mathrm {m}$

In the presence of background light the memory elements receive an additional part of the signal. This would disturb the distance measurement. To eliminate the background part of the signal, the whole measurement can be performed a second time with the illumination switched off. If the objects are further away than the distance range, the result is also wrong. Here, a second measurement with the control signals delayed by an additional pulse width helps to suppress such objects. Other systems work with a sinusoidally modulated light source instead of the pulse source.

For direct TOF imagers, such as 3D Flash LIDAR, a single short pulse from 5 to 10 ns is emitted by the laser. The T-zero event (the time the pulse leaves the camera) is established by capturing the pulse directly and routing this timing onto the focal plane array. T-zero is used to compare the return time of the returning reflected pulse on the various pixels of the focal plane array. By comparing T-zero and the captured returned pulse and comparing the time difference, each pixel accurately outputs a direct time-of-flight measurement. The round trip of a single pulse for 100 meters is 660 ns. With a 10 ns pulse, the scene is illuminated and the range and intensity captured in less than 1 microsecond.

## Advantages

### Simplicity

In contrast to stereo vision or triangulation systems, the whole system is very compact: the illumination is placed just next to the lens, whereas the other systems need a certain minimum base line. In contrast to laser scanning systems, no mechanical moving parts are needed.

### Efficient distance algorithm

It is a direct process to extract the distance information out of the output signals of the TOF sensor. As a result, this task uses only a small amount of processing power, again in contrast to stereo vision, where complex correlation algorithms are implemented. After the distance data has been extracted, object detection, for example, is also a straightforward process to carry out because the algorithms are not disturbed by patterns on the object. The accuracy is usually estimated at 1% of the measured distance.

### Speed

Time-of-flight cameras are able to measure the distances within a complete scene with a single shot. As the cameras reach up to 160 frames per second, they are ideally suited to be used in real-time applications.

## Disadvantages

### Background light

When using CMOS or other integrating detectors or sensors that use visible or near infra-red light (400 nm - 700 nm), although most of the background light coming from artificial lighting or the sun is suppressed, the pixel still has to provide a high dynamic range. The background light also generates electrons, which have to be stored. For example, the illumination units in many of today's TOF cameras can provide an illumination level of about 1 watt. The Sun has an illumination power of about 1050 watts per square meter, and 50 watts after the optical band-pass filter. Therefore, if the illuminated scene has a size of 1 square meter, the light from the sun is 50 times stronger than the modulated signal. For non-integrating TOF sensors that do not integrate light over time and are using near-infrared detectors (InGaAs) to capture the short laser pulse, direct viewing of the sun is a non-issue because the image is not integrated over time, rather captured within a short acquisition cycle typically less than 1 microsecond. Such TOF sensors are used in space applications and in consideration for automotive applications.

### Interference

In certain types of TOF devices (but not all of them), if several time-of-flight cameras are running at the same time, the TOF cameras may disturb each other's measurements. There exist several possibilities for dealing with this problem:

- **Time multiplexing:** A control system starts the measurement of the individual cameras consecutively, so that only one illumination unit is active at a time.
- **Different modulation frequencies:** If the cameras modulate their light with different modulation frequencies, their light is collected in the other systems only as background illumination but does not disturb the distance measurement.

For Direct TOF type cameras that use a single laser pulse for illumination, because the single laser pulse is short (e.g. 10 nanoseconds), the round trip TOF to and from the objects in the field of view is correspondingly short (e.g. 100 meters = 660 ns TOF round trip). For an imager capturing at 30 Hz, the probability of an interfering interaction is the time that the camera acquisition gate is open divided by the time between laser pulses or approximately 1 in 50,000 (0.66 μs divided by 33 ms).

### Multiple reflections

In contrast to laser scanning systems where a single point is illuminated, the time-of-flight cameras illuminate a whole scene. For a phase difference device (amplitude modulated array), due to multiple reflections, the light may reach the objects along several paths. Therefore, the measured distance may be greater than the true distance. Direct TOF imagers are vulnerable if the light is reflecting from a specular surface. There are published papers available that outline the strengths and weaknesses of the various TOF devices and approaches.

## Applications

Time-of-flight cameras are used for a wide variety of applications. Examples include robotics and touchless user interfaces.

### In traffic enforcement

Continuous-wave ToF systems are used to detect retroreflective surfaces such as license plates and vehicle reflectors. These systems capture a sequence of depth images to track vehicle positions in 3D space over time. By analyzing the trajectory of these points, they can accurately calculate the speed of vehicles, independently of the distance and angle between the vehicle and the camera.

### Automotive applications

Time-of-flight cameras are used in assistance and safety functions for advanced automotive applications such as active pedestrian safety, precrash detection and indoor applications like out-of-position (OOP) detection.

### Human-machine interfaces and gaming

As time-of-flight cameras provide distance images in real time, it is easy to track movements of humans. This allows new interactions with consumer devices such as televisions. Another topic is to use this type of cameras to interact with games on video game consoles. The second-generation Kinect sensor originally included with the Xbox One console used a time-of-flight camera for its range imaging, enabling natural user interfaces and gaming applications using computer vision and gesture recognition techniques. Creative and Intel also provide a similar type of interactive gesture time-of-flight camera for gaming, the Senz3D based on the DepthSense 325 camera of Softkinetic. Infineon and PMD Technologies enable tiny integrated 3D depth cameras for close-range gesture control of consumer devices like all-in-one PCs and laptops (Picco flexx and Picco monstar cameras).

### Smartphone cameras

Several smartphones include time-of-flight cameras. These are mainly used to improve the quality of photos by providing the camera software with information about foreground and background.

The first mobile phone released with such technology was the LG G3, from early 2014. The BlackBerry Passport and the LG G Flex 2 were also launched with a ToF sensor.

### Measurement and machine vision

Other applications are measurement tasks, e.g. for the fill height in silos. In industrial machine vision, the time-of-flight camera helps to classify and locate objects for use by robots, such as items passing by on a conveyor. Door controls can distinguish easily between animals and humans reaching the door.

### Robotics

Another use of these cameras is the field of robotics: Mobile robots can build up a map of their surroundings very quickly, enabling them to avoid obstacles or follow a leading person. As the distance calculation is simple, only little computational power is used. Since these cameras can also be used to measure distance, teams for FIRST Robotics Competition have been known to use the devices for autonomous routines.

### Earth topography

ToF cameras have been used to obtain digital elevation models of the Earth's surface topography, for studies in geomorphology.

## Brands

### Active brands (as of 2011)

- Orbbec - high-performance Femto series iTOF RGB-Depth Camera based on Microsoft's iTOF technology with a global application in logistics, robotics, healthcare, retail, fitness, and 3D content creation and animation
- ESPROS - 3D TOF imager chips, TOF camera and module for automotive, robotics, industrial and IoT applications
- 3D Flash LIDAR Cameras and Vision Systems by Advanced Scientific Concepts, Inc. for aerial, automotive and space applications
- DepthSense - TOF cameras and modules, including RGB sensor and microphones by SoftKinetic
- IRMA MATRIX - TOF camera, used for automatic passenger counting on mobile and stationary applications by iris-GmbH
- Kinect - hands-free user interface platform by Microsoft for video game consoles and PCs, using time-of-flight cameras in its second generation of sensor devices.
- Azure Kinect DK Depth Camera - The Azure Kinect DK depth camera implements the Amplitude Modulated Continuous Wave (AMCW) Time-of-Flight (ToF) principle.Azure Kineck DK
- pmd - camera reference designs and software (pmd[vision], including TOF modules [CamBoard]) and TOF imagers (PhotonICs) by PMD Technologies
- real.IZ 2+3D - High-resolution SXGA (1280×1024) TOF camera developed by startup company odos imaging, integrating conventional image capture with TOF ranging in the same sensor. Based on technology developed at Siemens.
- Senz3D - TOF camera by Creative and Intel based on DepthSense 325 camera of Softkinetic, used for gaming.
- SICK - 3D industrial TOF cameras (Visionary-T) for industrial applications and software
- 3D MLI Sensor - TOF imager, modules, cameras, and software by IEE (International Electronics & Engineering), based on modulated light intensity (MLI)
- TOFCam Stanley - TOF camera by Stanley Electric
- TriDiCam - TOF modules and software, the TOF imager originally developed by Fraunhofer Institute of Microelectronic Circuits and Systems, now developed by the spin out company TriDiCam
- Hakvision - TOF stereo camera
- Cube eye - ToF Camera and Modules, VGA Resolution, website : www.cube-eye.co.kr
- Basler AG - 3D imaging for industrial applications [1]
- LILIN - ToF Surveillance Camera [2]

### Defunct brands

- CanestaVision - TOF modules and software by Canesta (company acquired by Microsoft in 2010)
- D-IMager - TOF camera by Panasonic Electric Works
- OptriCam - TOF cameras and modules by Optrima (rebranded DepthSense prior to SoftKinetic merger in 2011)
- ZCam - TOF camera products by 3DV Systems, integrating full-color video with depth information (assets sold to Microsoft in 2009)
- SwissRanger - an industrial TOF-only camera line originally by the Centre Suisse d'Electronique et Microtechnique, S.A. (CSEM), now developed by Mesa Imaging (Mesa Imaging acquired by Heptagon in 2014)
- Fotonic - TOF cameras and software powered by Panasonic CMOS chip (Fotonic acquired by Autoliv in 2018)
- S.Cube - ToF Camera and Modules by Cube eye

- (D-IMager by Panasonic) D-IMager by Panasonic
- (pmd[vision] CamCube by PMD Technologies) pmd[vision] CamCube by PMD Technologies
- (SwissRanger 4000 by MESA Imaging) SwissRanger 4000 by MESA Imaging
- (FOTONIC-B70 by Fotonic) FOTONIC-B70 by Fotonic
- (3D MLI Sensor by IEE S.A.) 3D MLI Sensor by IEE S.A.
- (ARTTS camera prototype) ARTTS camera prototype
- (pmd[vision] CamBoard by PMD Technologies) pmd[vision] CamBoard by PMD Technologies
- (Kinect for Xbox One by Microsoft) Kinect for Xbox One by Microsoft
