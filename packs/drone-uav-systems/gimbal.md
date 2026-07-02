---
title: "Gimbal"
source: https://en.wikipedia.org/wiki/Gimbal
domain: drone-uav-systems
license: CC-BY-SA-4.0
tags: unmanned aerial vehicle, quadcopter, first-person view, ground control station
fetched: 2026-07-02
---

# Gimbal

A **gimbal** is a pivoted support that permits rotation of an object about an axis. A set of three gimbals, one mounted on the other with orthogonal pivot axes, may be used to allow an object mounted on the innermost gimbal to remain independent of the rotation of its support (e.g. vertical in the first animation). For example, on a ship, the gyroscopes, shipboard compasses, stoves, and even drink holders typically use gimbals to keep them upright with respect to the horizon despite the ship's pitching and rolling.

The gimbal suspension used for mounting compasses and the like is sometimes called a **Cardan suspension** after Italian mathematician and physicist Gerolamo Cardano (1501–1576) who described it in detail. However, Cardano did not invent the gimbal, nor did he claim to. The device has been known since antiquity, first described in the 3rd c. BC by Philo of Byzantium, although some modern authors support the view that it may not have a single identifiable inventor.

## History

The gimbal was first described by the Greek inventor Philo of Byzantium (280–220 BC). Philo described an eight-sided ink pot with an opening on each side, which can be turned so that while any face is on top, a pen can be dipped and inked — yet the ink never runs out through the holes of the other sides. This was done by the suspension of the inkwell at the center, which was mounted on a series of concentric metal rings so that it remained stationary no matter which way the pot is turned.

In Ancient China, the Han dynasty (202 BC – 220 AD) inventor and mechanical engineer Ding Huan created a gimbal incense burner around 180 AD. There is a hint in the writing of the earlier Sima Xiangru (179–117 BC) that the gimbal existed in China since the 2nd century BC. There is mention during the Liang dynasty (502–557) that gimbals were used for hinges of doors and windows, while an artisan once presented a portable warming stove to Empress Wu Zetian (r. 690–705) which employed gimbals. Extant specimens of Chinese gimbals used for incense burners date to the early Tang dynasty (618–907), and were part of the silver-smithing tradition in China.

The authenticity of Philo's description of a cardan suspension has been doubted by some authors on the ground that the part of Philo's *Pneumatica* which describes the use of the gimbal survived only in an Arabic translation of the early 9th century. Thus, as late as 1965, the sinologist Joseph Needham suspected Arab interpolation. However, Carra de Vaux, author of the French translation which still provides the basis for modern scholars, regards the *Pneumatics* as essentially genuine. The historian of technology George Sarton (1959) also asserts that it is safe to assume the Arabic version is a faithful copying of Philo's original, and credits Philo explicitly with the invention. So does his colleague Michael Lewis (2001). In fact, research by the latter scholar (1997) demonstrates that the Arab copy contains sequences of Greek letters which fell out of use after the 1st century, thereby strengthening the case that it is a faithful copy of the Hellenistic original, a view recently also shared by the classicist Andrew Wilson (2002).

The ancient Roman author Athenaeus Mechanicus, writing during the reign of Augustus (30 BC–14 AD), described the military use of a gimbal-like mechanism, calling it "little ape" (*pithêkion*). When preparing to attack coastal towns from the sea-side, military engineers used to yoke merchant-ships together to take the siege machines up to the walls. But to prevent the shipborne machinery from rolling around the deck in heavy seas, Athenaeus advises that "you must fix the *pithêkion* on the platform attached to the merchant-ships in the middle, so that the machine stays upright in any angle".

After antiquity, gimbals remained widely known in the Near East. In the Latin West, reference to the device appeared again in the 9th century recipe book called the *Little Key of Painting'* (*mappae clavicula*). The French inventor Villard de Honnecourt depicts a set of gimbals in his sketchbook (see right). In the early modern period, dry compasses were suspended in gimbals.

## Applications

### Inertial navigation

In inertial navigation, as applied to ships and submarines, a minimum of three gimbals are needed to allow an inertial navigation system (stable table) to remain fixed in inertial space, compensating for changes in the ship's yaw, pitch, and roll. In this application, the inertial measurement unit (IMU) is equipped with three orthogonally mounted gyros to sense rotation about all axes in three-dimensional space. The gyro outputs are kept to a null through drive motors on each gimbal axis, to maintain the orientation of the IMU. To accomplish this, the gyro error signals are passed through "resolvers" mounted on the three gimbals, roll, pitch and yaw. These resolvers perform an automatic matrix transformation according to each gimbal angle, so that the required torques are delivered to the appropriate gimbal axis. The yaw torques must be resolved by roll and pitch transformations. The gimbal angle is never measured. Similar sensing platforms are used on aircraft.

In inertial navigation systems, gimbal lock may occur when vehicle rotation causes two of the three gimbal rings to align with their pivot axes in a single plane. When this occurs, it is no longer possible to maintain the sensing platform's orientation.

### Rocket engines

In spacecraft propulsion, rocket engines are generally mounted on a pair of gimbals to allow a single engine to vector thrust about both the pitch and yaw axes; or sometimes just one axis is provided per engine. To control roll, twin engines with differential pitch or yaw control signals are used to provide torque about the vehicle's roll axis.

### Photography and imaging

Gimbals are also used to mount everything from small camera lenses to large photographic telescopes.

In portable photography equipment, single-axis gimbal heads are used in order to allow a balanced movement for camera and lenses. This proves useful in wildlife photography as well as in any other case where very long and heavy telephoto lenses are adopted: a gimbal head rotates a lens around its center of gravity, thus allowing for easy and smooth manipulation while tracking moving subjects.

Very large gimbal mounts in the form 2 or 3 axis altitude-altitude mounts are used in satellite photography for tracking purposes.

Gyrostabilized gimbals which house multiple sensors are also used for airborne surveillance applications including airborne law enforcement, pipe and power line inspection, mapping, and ISR (intelligence, surveillance, and reconnaissance). Sensors include thermal imaging, daylight, low light cameras as well as laser range finder, and illuminators.

Gimbal systems are also used in scientific optics equipment. For example, they are used to rotate a material sample along an axis to study their angular dependence of optical properties.

### Film and video

Handheld 3-axis gimbals are used in stabilization systems designed to give the camera operator the independence of handheld shooting without camera vibration or shake. There are two versions of such stabilization systems: mechanical and motorized.

Mechanical gimbals have the sled, which includes the top *stage* where the camera is attached, the *post* which in most models can be extended, with the monitor and batteries at the bottom to counterbalance the camera weight. This is how the Steadicam stays upright, by simply making the bottom slightly heavier than the top, pivoting at the gimbal. This leaves the center of gravity of the whole rig, however heavy it may be, exactly at the operator's fingertip, allowing deft and finite control of the whole system with the lightest of touches on the gimbal.

Powered by three brushless motors, motorized gimbals have the ability to keep the camera level on all axes as the camera operator moves the camera. An inertial measurement unit (IMU) responds to movement and utilizes its three separate motors to stabilize the camera. With the guidance of algorithms, the stabilizer is able to notice the difference between deliberate movement such as pans and tracking shots from unwanted shake. This allows the camera to seem as if it is floating through the air, an effect achieved by a Steadicam in the past. Gimbals can be mounted to cars and other vehicles such as drones, where vibrations or other unexpected movements would make tripods or other camera mounts unacceptable.

### Marine chronometers

The rate of a mechanical marine chronometer is sensitive to its orientation. Because of this, chronometers were normally mounted on gimbals, in order to isolate them from the rocking motions of a ship at sea.

### Drones

A drone gimbal system is a stabilization mechanism that uses electric motors (usually using brushless servo motors) in the yaw, pitch, and roll axes to isolate the camera or sensor payload from the motion and vibration of the drone.  The system ensures the camera remains stable at a set level, resulting in smooth, high-quality footage even during fast maneuvers or windy conditions.  The system relies on an inertial measurement unit (IMU) to accurately estimate the motion and orientation of the drone and a gimbal control unit (GCU), which use IMU data and PID control algorithms to dynamically adjust the motors in real time, canceling out disturbances.

## Gimbal lock

Gimbal lock is the loss of one degree of freedom in a three-dimensional, three-gimbal mechanism that occurs when the axes of two of the three gimbals are driven into a parallel configuration, "locking" the system into rotation in a degenerate two-dimensional space.

The word "lock" is misleading: no gimbal is restrained; all three gimbals can still rotate freely about their respective axes of suspension. Nevertheless, because of the parallel orientation of two of the gimbals' axes, there is no gimbal available to accommodate rotation about one axis.
