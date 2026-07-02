---
title: "Wind turbine design (part 1/2)"
source: https://en.wikipedia.org/wiki/Wind_turbine_design
domain: wind-turbine-control
license: CC-BY-SA-4.0
tags: wind turbine control, blade pitch, yaw system, wind farm
fetched: 2026-07-02
part: 1/2
---

# Wind turbine design

**Wind turbine design** is the process of defining the form and configuration of a wind turbine to extract energy from the wind. An installation consists of the systems needed to capture the wind's energy, point the turbine into the wind, convert mechanical rotation into electrical power, and other systems to start, stop, and control the turbine.

In 1919, German physicist Albert Betz showed that for a hypothetical ideal wind-energy extraction machine, the fundamental laws of conservation of mass and energy allowed no more than 16/27 (59.3%) of the wind's kinetic energy to be captured. This Betz's law limit can be approached by modern turbine designs which reach 70 to 80% of this theoretical limit.

In addition to the blades, design of a complete wind power system must also address the hub, controls, generator, supporting structure and foundation. Turbines must also be integrated into power grids.


## Aerodynamics

Blade shape and dimension are determined by the aerodynamic performance required to efficiently extract energy, and by the strength required to resist forces on the blade.

The aerodynamics of a horizontal-axis wind turbine are not straightforward. The air flow at the blades is not the same as that away from the turbine. The way that energy is extracted from the air also causes air to be deflected by the turbine. Wind turbine aerodynamics at the rotor surface exhibit phenomena that are rarely seen in other aerodynamic fields.


## Power control

Rotation speed must be controlled for efficient power generation and to keep the turbine components within speed and torque limits. The centrifugal force on the blades increases as the square of the rotation speed, which makes this structure sensitive to overspeed. Because power increases as the cube of the wind speed, turbines must survive much higher wind loads (such as gusts of wind) than those loads from which they generate power.

A wind turbine must produce power over a range of wind speeds. The cut-in speed is around 3–4 m/s for most turbines, and cut-out at 25 m/s. If the rated wind speed is exceeded the power has to be limited.

A control system involves three basic elements: sensors to measure process variables, actuators to manipulate energy capture and component loading, and control algorithms that apply information gathered by the sensors to coordinate the actuators.

Any wind blowing above the survival speed damages the turbine. The survival speed of commercial wind turbines ranges from 40 m/s (144 km/h, 89 MPH) to 72 m/s (259 km/h, 161 MPH), typically around 60 m/s (216 km/h, 134 MPH). Some turbines can survive 80 metres per second (290 km/h; 180 mph).

### Stall

A stall on an airfoil occurs when air passes over it in such a way that the generation of lift rapidly decreases. Usually this is due to a high angle of attack (AOA), but can also result from dynamic effects. The blades of a fixed pitch turbine can be designed to stall in high wind speeds, slowing rotation. This is a simple fail-safe mechanism to help prevent damage. However, other than systems with dynamically controlled pitch, it cannot produce a constant power output over a large range of wind speeds, which makes it less suitable for large scale, power grid applications.

A fixed-speed HAWT (Horizontal Axis Wind Turbine) inherently increases its angle of attack at higher wind speed as the blades speed up. A natural strategy, then, is to allow the blade to stall when the wind speed increases. This technique was successfully used on many early HAWTs. However, the degree of blade pitch tended to increase noise levels.

Vortex generators may be used to control blade lift characteristics. VGs are placed on the airfoil to enhance the lift if they are placed on the lower (flatter) surface or limit the maximum lift if placed on the upper (higher camber) surface.

### Furling

Furling works by decreasing the angle of attack, which reduces drag and blade cross-section. One major problem is getting the blades to stall or furl quickly enough in a wind gust. A fully furled turbine blade, when stopped, faces the edge of the blade into the wind.

Loads can be reduced by making a structural system softer or more flexible. This can be accomplished with downwind rotors or with curved blades that twist naturally to reduce angle of attack at higher wind speeds. These systems are nonlinear and couple the structure to the flow field - requiring design tools to evolve to model these nonlinearities.

Standard turbines all furl in high winds. Since furling requires acting against the torque on the blade, it requires some form of pitch angle control, which is achieved with a slewing drive. This drive precisely angles the blade while withstanding high torque loads. In addition, many turbines use hydraulic systems. These systems are usually spring-loaded, so that if hydraulic power fails, the blades automatically furl. Other turbines use an electric servomotor for every blade. They have a battery-reserve in case of grid failure. Small wind turbines (under 50 kW) with variable-pitching generally use systems operated by centrifugal force, either by flyweights or geometric design, and avoid electric or hydraulic controls.

Fundamental gaps exist in pitch control, limiting the reduction of energy costs, according to a report funded by the Atkinson Center for a Sustainable Future. Load reduction is currently focused on full-span blade pitch control, since individual pitch motors are the actuators on commercial turbines. Significant load mitigation has been demonstrated in simulations for blades, tower, and drive train. However, further research is needed to increase energy capture and mitigate fatigue loads.

A control technique applied to the pitch angle is done by comparing the power output with the power value at the rated engine speed (power reference, Ps reference). Pitch control is done with PI controller. In order to adjust pitch rapidly enough, the actuator uses the time constant Tservo, an integrator and limiters. The pitch angle remains from 0° to 30° with a change rate of 10°/second.

As in the figure at the right, the reference pitch angle is compared with the actual pitch angle b and then the difference is corrected by the actuator. The reference pitch angle, which comes from the PI controller, goes through a limiter. Restrictions are important to maintain the pitch angle in real terms. Limiting the change rate is especially important during network faults. The importance is due to the fact that the controller decides how quickly it can reduce the aerodynamic energy to avoid acceleration during errors.


## Other controls

### Generator torque

Modern large wind turbines operate at variable speeds. When wind speed falls below the turbine's rated speed, generator torque is used to control the rotor speed to capture as much power as possible. The most power is captured when the tip speed ratio is held constant at its optimum value (typically between 6 and 7). This means that rotor speed increases proportional to wind speed. The difference between the aerodynamic torque captured by the blades and the applied generator torque controls the rotor speed. If the generator torque is lower, the rotor accelerates, and if the generator torque is higher, the rotor slows. Below rated wind speed, the generator torque control is active while the blade pitch is typically held at the constant angle that captures the most power, fairly flat to the wind. Above rated wind speed, the generator torque is typically held constant while the blade pitch is adjusted accordingly.

One technique to control a permanent magnet synchronous motor is field-oriented control. Field-oriented control is a closed loop strategy composed of two current controllers (an inner loop and cascading outer loop) necessary for controlling the torque, and one speed controller.

### Constant torque angle control

In this control strategy the d axis current is kept at zero, while the vector current aligns with the q axis in order to maintain the torque angle at 90o. This is a common control strategy because only the Iqs current must be controlled. The torque equation of the generator is a linear equation dependent only on the Iqs current.

So, the electromagnetic torque for Ids = 0 (we can achieve that with the d-axis controller) is now:

$Te=3/2p(\lambda pmIqs+(Lds-Lqs)IdsIqs)=3/2p\lambda pmIqs$

Thus, the complete system of the machine side converter and the cascaded PI controller loops is given by the figure. The control inputs are the duty rations mds and mqs, of the PWM-regulated converter. It displays the control scheme for the wind turbine in the machine side and simultaneously how the Ids to zero (the torque equation is linear).

### Yawing

Large turbines are typically actively controlled to face the wind direction measured by a wind vane situated on the back of the nacelle. By minimizing the yaw angle (the misalignment between wind and turbine pointing direction), power output is maximized and non-symmetrical loads minimized. However, since wind direction varies, the turbine does not strictly follow the wind and experiences a small yaw angle on average. The power output losses can be approximated to fall with (cos(yaw angle))3. Particularly at low-to-medium wind speeds, yawing can significantly reduce output, with wind common variations reaching 30°. At high wind speeds, wind direction is less variable.

### Electrical braking

Braking a small turbine can be done by dumping energy from the generator into a resistor bank, converting kinetic energy into heat. This method is useful if the kinetic load on the generator is suddenly reduced or is too small to keep the turbine speed within its allowed limit.

Cyclically braking slows the blades, which increases the stalling effect and reducing efficiency. Rotation can be kept at a safe speed in faster winds while maintaining (nominal) power output. This method is usually not applied on large, grid-connected wind turbines.

### Mechanical braking

A mechanical drum brake or disc brake stops rotation in emergency situations such as extreme gust events. The brake is a secondary means to hold the turbine at rest for maintenance, with a rotor lock system as primary means. Such brakes are usually applied only after blade furling and electromagnetic braking have reduced the turbine speed because mechanical brakes can ignite a fire inside the nacelle if used at full speed. Turbine load increases if the brake is applied at rated RPM.


## Turbine size

Turbines come in size classes. The smallest, with power less than 10 kW are used in homes, farms and remote applications whereas intermediate wind turbines (10-250 kW ) are useful for village power, hybrid systems and distributed power. The world's largest wind turbine as of 2021 was Vestas' V236-15.0 MW turbine. The new design's blades offer the largest swept area in the world with three 115.5 metres (379 ft) blades giving a rotor diameter of 236 metres (774 ft). Ming Yang in China have announced a larger 16 MW design.

For a given wind speed, turbine mass is approximately proportional to the cube of its blade-length. Wind power intercepted is proportional to the square of blade-length. The maximum blade-length of a turbine is limited by strength, stiffness, and transport considerations.

Labor and maintenance costs increase slower than turbine size, so to minimize costs, wind farm turbines are basically limited by the strength of materials, and siting requirements.

### Low temperature

Utility-scale wind turbine generators have minimum temperature operating limits that apply in areas with temperatures below −20 °C (−4 °F). Turbines must be protected from ice accumulation that can make anemometer readings inaccurate and which, in certain turbine control designs, can cause high structure loads and damage. Some turbine manufacturers offer low-temperature packages at extra cost, which include internal heaters, different lubricants, and different alloys for structural elements. If low-temperatures are combined with a low-wind condition, the turbine requires an external supply of power, equivalent to a few percent of its rated output, for internal heating. For example, the St. Leon Wind Farm in Manitoba, Canada, has a total rating of 99 MW and is estimated to need up to 3 MW (around 3% of capacity) of station service power a few days a year for temperatures down to −30 °C (−22 °F).


## Nacelle

←

→

↑

↓

▶

-25

80

50

Interior view of a wind turbine nacelle

The nacelle houses the gearbox and generator connecting the tower and rotor. Sensors detect the wind speed and direction, and motors turn the nacelle into the wind to maximize output.

### Gearbox

In conventional wind turbines, the blades spin a shaft that is connected through a gearbox to the generator. The gearbox converts the turning speed of the blades (15 to 20 RPM for a one-megawatt turbine) into the 1,800 (750-3600) RPM that the generator needs to generate electricity. Gearboxes are one of the more expensive components for installing and maintaining wind turbines. Analysts from GlobalData estimate that the gearbox market grew from $3.2bn in 2006 to $6.9bn in 2011. The market leader for Gearbox production was Winergy in 2011. The use of magnetic gearboxes has been explored as a way of reducing maintenance costs.

### Generator

For large horizontal-axis wind turbines (HAWT), the generator is mounted in a nacelle at the top of a tower, behind the rotor hub. Older wind turbines generate electricity through asynchronous machines directly connected to the grid. The gearbox reduces generator cost and weight. Commercial generators have a rotor carrying a winding so that a rotating magnetic field is produced inside a set of windings called the stator. While the rotating winding consumes a fraction of a percent of the generator output, adjustment of the field current allows good control over the output voltage.

The rotor's varying output frequency and voltage can be matched to the fixed values of the grid using multiple technologies such as doubly fed induction generators or full-effect converters, which converts the variable frequency current to DC and then back to AC using inverters. Although such alternatives require costly equipment and cost power, the turbine can capture a significantly larger fraction of the wind energy. Most are low voltage 660 Volt, but some offshore turbines (several MW) are 3.3 kV medium voltage.

In some cases, especially when offshore, a large collector transformer converts the wind farm's medium-voltage AC grid to DC and transmits the energy through a power cable to an onshore HVDC converter station.

### Hydraulic

Hydraulic wind turbines perform the frequency and torque adjustments of gearboxes via a pressurized hydraulic fluid. Typically, the action of the turbine pressurizes the fluid with a hydraulic pump at the nacelle. Meanwhile, components on the ground can transform this pressure into energy, and recirculate the working fluid. Typically, the working fluid used in this kind of hydrostatic transmission is oil, which serves as a lubricant, reducing losses due to friction in the hydraulic units and allowing for a broad range of operating temperatures. However, other concepts are currently under study, which involve using water as the working fluid because it is abundant and eco-friendly.

Hydraulic turbines provide benefits to both operation and capital costs. They can use hydraulic units with variable displacement to have a continuously variable transmission that adapts in real time. This decouples generator speed to rotor speed, avoiding stalling and allowing for operating the turbine at an optimum speed and torque. This built-in transmission is how these hydraulic systems avoid the need for a conventional gearbox. Furthermore, hydraulic instead of mechanical power conversion introduces a damping effect on rotation fluctuations, reducing fatigue of the drivetrain and improving turbine structural integrity. Additionally, using a pressurized fluid instead of mechanical components allows for the electrical conversion to occur on the ground instead of the nacelle: this reduces maintenance difficulty, and reduces weight and center of gravity of the turbine. Studies estimate that these benefits may yield to a 3.9-18.9% reduction in the levelized cost of power for offshore wind turbines.

Some years ago, Mitsubishi, through its branch Artemis, deployed the Sea Angel, a unique hydraulic wind turbine at the utility scale. The Digital Displacement technology underwent trials on the Sea Angel, a wind turbine rated at 7 MW. This design is capable of adjusting the displacement of the central unit in response to erratic wind velocities, thereby maintaining the optimal efficiency of the system. Still, these systems are newer and in earlier stages of commercialization compared to conventional gearboxes.

### Gearless

Gearless wind turbines (also called direct drive) eliminate the gearbox. Instead, the rotor shaft is attached directly to the generator, which spins at the same speed as the blades.

Advantages of permanent magnet direct drive generators (PMDD) over geared generators include increased efficiency, reduced noise, longer lifetime, high torque at low RPM, faster and precise positioning, and drive stiffness. PMDD generators "eliminate the gear-speed increaser, which is susceptible to significant accumulated fatigue torque loading, related reliability issues, and maintenance costs".

To make up for a direct-drive generator's slower rotation rate, the diameter of the generator's rotor is increased so that it can contain more magnets to create the required frequency and power. Gearless wind turbines are often heavier than geared wind turbines. An EU study showed that gearbox reliability is not the main problem in wind turbines. The reliability of direct drive turbines offshore is still not known, given the small sample size.

Experts from Technical University of Denmark estimate that a geared generator with permanent magnets may require 25 kg/MW of the rare-earth element neodymium, while a gearless may use 250 kg/MW.

In December 2011, the US Department of Energy announced a critical shortage of rare-earth elements such as neodymium. China produces more than 95% of rare-earth elements, while Hitachi holds more than 600 patents covering neodymium magnets. Direct-drive turbines require 600 kg of permanent magnet material per megawatt, which translates to several hundred kilograms of rare-earth content per megawatt, as neodymium content is estimated to be 31% of magnet weight. Hybrid drivetrains (intermediate between direct drive and traditional geared) use significantly less rare-earth materials. While permanent magnet wind turbines only account for about 5% of the market outside of China, their market share inside of China is estimated at 25% or higher. In 2011, demand for neodymium in wind turbines was estimated to be 1/5 of that in electric vehicles.


## Blades

### Blade design

The ratio between the blade speed and the wind speed is called tip-speed ratio. High efficiency 3-blade-turbines have tip speed/wind speed ratios of 6 to 7. Wind turbines spin at varying speeds (a consequence of their generator design). Use of aluminum and composite materials has contributed to low rotational inertia, which means that newer wind turbines can accelerate quickly if the winds pick up, keeping the tip speed ratio more nearly constant. Operating closer to their optimal tip speed ratio during energetic gusts of wind allows wind turbines to improve energy capture from sudden gusts.

Noise increases with tip speed. To increase tip speed without increasing noise would reduce torque into the gearbox and generator, reducing structural loads, thereby reducing cost. The noise reduction is linked to the detailed blade aerodynamics, especially factors that reduce abrupt stalling. The inability to predict stall restricts the use of aggressive aerodynamics. Some blades have a winglet to increase performance and reduce noise.

A blade can have a lift-to-drag ratio of 120, compared to 70 for a sailplane and 15 for an airliner. In order to optimize the lift-to-drag ratio of a blade, they are typically designed with varying airfoil cross-sections along their length, customized to the varying wind speeds and angles encountered from root to tip.

An additional design improvement is the incorporation of vortex generators, small fins mounted to the surface of the blade, the help to smooth the airflow, preventing flow separation and reducing turbulence, both of which contribute to reducing energy losses. All of these innovations have the end goal of increasing the efficiency of converting wind energy to electricity.

Study of the hydrodynamics of the knobbly flippers of the humpback whale by the marine biologist Frank E. Fish led to an improved design of wind turbine blades.

### Applications of IMU in Wind Power Generation

#### Blade Dynamic Deformation and Load Monitoring

The role of the Inertial Measurement Unit (IMU) in wind power generation is to measure the three-axis acceleration and angular velocity of wind turbine blades, hubs, and tower tops in real-time. By using inertial navigation algorithms, it calculates the motion states (position, velocity, and attitude) of these components. IMU captures the global dynamic information of wind turbines and, through data fusion with Kalman filters and GNSS data, reduces cumulative errors. This enables high-precision estimation of blade deflection and loads, providing critical support for monitoring the operational loads of wind turbines.

IMUs measure angular velocity and acceleration, which, combined with navigation algorithms, capture the flexural attitude and positional changes of blades during operation in real time. Through the use of Kalman filters (KF) to fuse data from multiple IMUs, and based on rigid body geometric models and rotor angles, the position of each IMU is determined. Precision is further enhanced by compensating for differences between actual positions and the model.

*GNSS Integration*:

GNSS plays two key roles:

1. *Time Synchronization*: It provides a unified time reference for all IMUs, ensuring sensor data alignment.
2. *Absolute Position Reference*: By integrating IMU data, it limits drift errors, ensuring convergence and accuracy in IMU navigation solutions (position and attitude).

#### Structural Health Monitoring and Fault Prediction

IMU can be combined with other sensors (e.g., vibration and stress sensors) to improve fault detection sensitivity through multi-source data fusion. For example, IMUs installed on the turbine main shaft can extract tower acceleration signals through signal processing and use azimuth information to identify specific faults. Multi-sensor fusion technology can detect blade stress changes and crack risks, reducing downtime losses.

In 2021, Chinese researchers proposed an innovative multi-IMU data fusion algorithm for wind turbine blade dynamic deformation sensing. This algorithm uses a relative motion sensing fusion method that employs an improved Kalman filter and a feedback-based distributed structure to achieve multi-node data fusion.

*High-Precision and Low-Precision IMU Collaboration:*

1. High-precision IMUs (main nodes) are placed at the blade root base, serving as a global reference point to provide information on the overall torsional attitude and positional changes of the blade.
2. Low-precision IMUs (sub-nodes) are distributed at different positions along the blade, sensing local dynamic deformations.
3. Data from the high-precision IMU is filtered and fused to correct the measurement errors of low-precision IMUs, significantly improving the system's overall measurement accuracy and fault tolerance. Each sub-node independently processes local data, and redundant information is integrated through a global fusion layer to enhance fault tolerance. Even if a single IMU fails, the system can maintain high accuracy.

*Application in Blade Dynamic Testing*

During wind turbine blade dynamic testing, blades undergo continuous motion under external forces. By combining global reference data from high-precision IMUs with local measurements from low-precision IMUs, multi-node data fusion is achieved through a federated Kalman filter. This enables precise perception of the blade's flexural attitude and position in three-dimensional space.

Simulation results show that the fusion algorithm effectively reduces the measurement errors of low-precision IMUs, significantly decreasing the relative position and attitude errors of local blade nodes while maintaining the accuracy of high-precision IMU nodes. Particularly for complex motions at the blade's middle and tip, the fusion algorithm demonstrates strong robustness and accuracy.

### Hub design

In simple designs, the blades are directly bolted to the hub and are unable to pitch, which leads to aerodynamic stall above certain windspeeds. In more sophisticated designs, they are bolted to the pitch bearing, which adjusts their angle of attack with the help of a pitch system according to the wind speed. Pitch control is performed by hydraulic or electric systems (battery or ultracapacitor). The pitch bearing is bolted to the hub. The hub is fixed to the rotor shaft, which drives the generator directly or through a gearbox.

### Blade count

The number of blades is selected for aerodynamic efficiency, component costs, and system reliability. Noise emissions are affected by the location of the blades upwind or downwind of the tower and the rotor speed. Given that the noise emissions from the blades' trailing edges and tips vary by the 5th power of blade speed, a small increase in tip speed dramatically increases noise.

Wind turbines almost universally use either two or three blades. However, patents present designs with additional blades, such as Chan Shin's multi-unit rotor blade system. Aerodynamic efficiency increases with number of blades but with diminishing return. Increasing from one to two yields a six percent increase, while going from two to three yields an additional three percent. Further increasing the blade count yields minimal improvements and sacrifices too much in blade stiffness as the blades become thinner.

Theoretically, an infinite number of blades of zero width is the most efficient, operating at a high value of the tip speed ratio, but this is not practical.

Component costs affected by blade count are primarily for materials and manufacturing of the turbine rotor and drive train. Generally, the lower the number of blades, the lower the material and manufacturing costs. In addition, fewer blades allow higher rotational speed. Blade stiffness requirements to avoid tower interference limit blade thickness, but only when the blades are upwind of the tower; deflection in a downwind machine increases tower clearance. Fewer blades with higher rotational speeds reduce peak torque in the drive train, resulting in lower gearbox and generator costs.

System reliability is affected by blade count primarily through the dynamic loading of the rotor into the drive train and tower systems. While aligning the wind turbine to changes in wind direction (yawing), each blade experiences a cyclic load at its root end depending on blade position. However, these cyclic loads when combined at the drive train shaft are symmetrically balanced for three blades, yielding smoother operation during yaw. One or two blade turbines can use a pivoting teetered hub to nearly eliminate the cyclic loads into the drive shaft and system during yawing. In 2012, a Chinese 3.6 MW two-blade turbine was tested in Denmark.

### Blade size

Increasing blade length pushed power generation from the single megawatt range to upwards of 10 megawatts. A larger area effectively increases tip-speed ratio at a given wind speed, thus increasing its energy extraction. Software such as HyperSizer (originally developed for spacecraft design) can be used to improve blade design.

As of 2015 the rotor diameters of onshore wind turbine blades reached 130 meters, while the diameter of offshore turbines reached 170 meters. In 2001, an estimated 50 million kilograms of fiberglass laminate were used in wind turbine blades.

### Blade weight

An important goal is to control blade weight. Since blade mass scales as the cube of the turbine radius, gravity loading constrains systems with larger blades. Gravitational loads include axial and tensile/ compressive loads (top/bottom of rotation) as well as bending (lateral positions). The magnitude of these loads fluctuates cyclically and the edgewise moments (see below) are reversed every 180° of rotation. Typical rotor speeds and design life are ~10 and 20 years, respectively, with the number of lifetime revolutions on the order of 10^8. Considering wind, it is expected that turbine blades go through ~10^9 loading cycles.

Wind is another source of rotor blade loading. Lift causes bending in the flatwise direction (out of rotor plane) while airflow around the blade cause edgewise bending (in the rotor plane). Flaps bending involves tension on the pressure (upwind) side and compression on the suction (downwind) side. Edgewise bending involves tension on the leading edge and compression on the trailing edge.

Wind loads are cyclical because of natural variability in wind speed and wind shear (higher speeds at top of rotation).

Failure in ultimate loading of wind-turbine rotor blades exposed to wind and gravity loading is a failure mode that needs to be considered when the rotor blades are designed. The wind speed that causes bending of the rotor blades exhibits a natural variability, and so does the stress response in the rotor blades. Also, the resistance of the rotor blades, in terms of their tensile strengths, exhibits a natural variability. Given the increasing size of production wind turbines, blade failures are increasingly relevant when assessing public safety risks from wind turbines. The most common failure is the loss of a blade or part thereof. This has to be considered in the design.

In light of these failure modes and increasingly larger blade systems, researchers seek cost-effective materials with higher strength-to-mass ratios.

### Blade materials

In general, materials should meet the following criteria:

- wide availability and easy processing to reduce cost and maintenance
- low weight or density to reduce gravitational forces
- high strength to withstand wind and gravitational loading
- high fatigue resistance to withstand cyclic loading
- high stiffness to ensure stability of the optimal shape and orientation of the blade and clearance with the tower
- high fracture toughness
- the ability to withstand environmental impacts such as lightning strikes, humidity, and temperature

#### History

Wood and canvas sails were used on early windmills due to their low price, availability, and ease of manufacture. These materials, however, require frequent maintenance. Wood and canvas construction limits the airfoil shape to a flat plate, which has a relatively high ratio of drag to force captured (low aerodynamic efficiency) compared to solid airfoils. Construction of solid airfoil designs requires inflexible materials such as metals or composites.

Advances in turbine blade materials mirrored the progression of materials science as a broader subject. The first large turbine blades were predominantly made from metals like steel and aluminum due to their availability and robustness. However, their heavy weight and low flexibility restricted turbine size and decreased efficiency, requiring more energy to maintain blade rotation.

The wind energy sector eventually moved onto lighter materials, namely fiberglass, a marked improvement over the excessive weight of metals. However, fiberglass possessed its own set of disadvantages, notably durability and sustainability issues. They were susceptible to environmental damages including UV radiation and moisture, leading to delamination and loss of structural integrity. Additionally, fiberglass is difficult to recycle, making the end-of-life impact of fiberglass blades quite high.

As a response to these challenges, the wind energy industry looked to carbon fiber as a blade material, the specific stiffness and durability of which are greater than both metal and carbon fiber. The superior stiffness-to-weight ratio allows for the use of larger blades, increasing efficiency (see **size** section). In recent research, bio-based composites and nanostructure enhancements have been utilized to further reduce weight and increase strength and stiffness.

#### Polymer

The majority of commercialized wind turbine blades are made from fiber-reinforced polymers (FRPs), which are composites consisting of a polymer matrix and fibers. The long fibers provide longitudinal stiffness and strength, and the matrix provides fracture toughness, delamination strength, out-of-plane strength, and stiffness. Material indices based on maximizing power efficiency, high fracture toughness, fatigue resistance, and thermal stability are highest for glass and carbon fiber reinforced plastics (GFRPs and CFRPs).

In turbine blades, matrices such as thermosets or thermoplastics are used; as of 2017, thermosets are more common. These allow for the fibers to be bound together and add toughness. Thermosets make up 80% of the market, as they have lower viscosity, and also allow for low-temperature cure, both features contributing to ease of processing during manufacture. Thermoplastics offer recyclability that the thermosets do not, however their processing temperature and viscosity are much higher, limiting the product size and consistency, which are both important for large blades. Fracture toughness is higher for thermoplastics, but the fatigue behavior is worse.

Fiberglass

-reinforced

epoxy

blades of Siemens SWT-2.3-101 wind turbines. The blade size of 49 meters

is in comparison to a

substation

behind them at

Wolfe Island Wind Farm

.

Manufacturing blades in the 40 to 50-metre range involves proven fiberglass composite fabrication techniques. Manufacturers such as Nordex and GE Wind use an infusion process. Other manufacturers vary this technique, some including carbon and wood with fiberglass in an epoxy matrix. Other options include pre-impregnated ("prepreg") fiberglass and vacuum-assisted resin transfer moulding. Each of these options uses a glass-fiber reinforced polymer composite constructed with differing complexity. Perhaps the largest issue with open-mould, wet systems is the emissions associated with the volatile organic compounds ("VOCs") released. Preimpregnated materials and resin infusion techniques contain all VOCs, however these contained processes have their challenges, because the production of thick laminates necessary for structural components becomes more difficult. In particular, the preform resin permeability dictates the maximum laminate thickness; also, bleeding is required to eliminate voids and ensure proper resin distribution. One solution to resin distribution is to use partially impregnated fiberglass. During evacuation, the dry fabric provides a path for airflow and, once heat and pressure are applied, the resin may flow into the dry region, resulting in an evenly impregnated laminate structure.

#### Epoxy

Epoxy-based composites have environmental, production, and cost advantages over other resin systems. Epoxies also allow shorter cure cycles, increased durability, and improved surface finish. Prepreg operations further reduce processing time over wet lay-up systems. As turbine blades passed 60 metres, infusion techniques became more prevalent, because traditional resin transfer moulding injection times are too long compared to resin set-up time, limiting laminate thickness. Injection forces resin through a thicker ply stack, thus depositing the resin in the laminate structure before gelation occurs. Specialized epoxy resins have been developed to customize lifetimes and viscosity.

Carbon fiber-reinforced load-bearing spars can reduce weight and increase stiffness. Using carbon fibers in 60-metre turbine blades is estimated to reduce total blade mass by 38% and decrease cost by 14% compared to 100% fiberglass. Carbon fibers have the added benefit of reducing the thickness of fiberglass laminate sections, further addressing the problems associated with resin wetting of thick lay-up sections. Wind turbines benefit from the trend of decreasing carbon fiber costs.

Although glass and carbon fibers have many optimal qualities, their downsides include the fact that high filler fraction (10-70 wt%) causes increased density as well as microscopic defects and voids that can lead to premature failure.

#### Carbon nanotubes

Carbon nanotubes (CNTs) can reinforce polymer-based nanocomposites. CNTs can be grown or deposited on the fibers or added into polymer resins as a matrix for FRP structures. Using nanoscale CNTs as filler instead of traditional microscale filler (such as glass or carbon fibers) results in CNT/polymer nanocomposites, for which the properties can be changed significantly at low filler contents (typically < 5 wt%). They have low density and improve the elastic modulus, strength, and fracture toughness of the polymer matrix. The addition of CNTs to the matrix also reduces the propagation of interlaminar cracks.

Research on a low-cost carbon fiber (LCCF) at Oak Ridge National Laboratory gained attention in 2020, because it can mitigate the structural damage from lightning strikes. On glass fiber wind turbines, lightning strike protection (LSP) is usually added on top, but this is effectively deadweight in terms of structural contribution. Using conductive carbon fiber can avoid adding this extra weight.

**Bio-composites**

A significant concern in materials criteria for a turbine blade is its manufacturing and end-of-life environmental impact, as well its recyclability. While there are methods for manufacturing of fiberglass and carbon fiber composites into turbine blades have a lower carbon footprint than aluminum, for example, they still have a noticeable impact (30–100 kg CO2 equivalent per kg). Additionally, fiberglass is incredibly difficult to recycle and carbon fiber composites, while possible to recycle, require additional research to yield fibers that are suitable for reusing as turbine materials (as opposed to the fibers being so degraded that they are only suitable for downcycling). The development of bio-composite materials with sufficient mechanical properties aims to address these issues.

Bio-composite materials use natural fibers and fillers as reinforcement instead of synthetic glass or carbon fibers. Approaches vary from partial to complete replacement of synthetics, with varying levels of success. Unfortunately, plant-based natural fibers, while having extremely low environmental impact, possess issues in their structural properties. Namely, they have high cellulosic content and large oxygen reaction sites, both of which contribute to issues in mechanical and thermal performance. As such, other natural fibers, such as non-moisture attractive basalt, have become the focus of bio-composite research.

#### Research

Some polymer composites feature self-healing properties. Since the blades of the turbine form cracks from fatigue due to repetitive cyclic stresses, self-healing polymers are attractive for this application, because they can improve reliability and buffer various defects such as delamination. Embedding paraffin wax-coated copper wires in a fiber reinforced polymer creates a network of tubes. Using a catalyst, these tubes and dicyclopentadiene (DCPD) then react to form a thermosetting polymer, which repairs the cracks as they form in the material. As of 2019, this approach is not yet commercial.

Further improvement is possible through the use of carbon nanofibers (CNFs) in the blade coatings. A major problem in desert environments is erosion of the leading edges of blades by sand-laden wind, which increases roughness and decreases aerodynamic performance. The particle erosion resistance of fiber-reinforced polymers is poor when compared to metallic materials and elastomers. Replacing glass fiber with CNF on the composite surface greatly improves erosion resistance. CNFs provide good electrical conductivity (important for lightning strikes), high damping ratio, and good impact-friction resistance.

For wind turbines, especially those offshore, or in wet environments, base surface erosion also occurs. For example, in cold climates, ice can build up on the blades and increase roughness. At high speeds, this same erosion impact can occur from rainwater. A useful coating must have good adhesion, temperature tolerance, weather tolerance (to resist erosion from salt, rain, sand, etc.), mechanical strength, ultraviolet light tolerance, and have anti-icing and flame retardant properties. Along with this, the coating should be cheap and environmentally friendly.

Super hydrophobic surfaces (SHS) cause water droplets to bead, and roll off the blades. SHS prevents ice formation, up to -25 C, as it changes the ice formation process.; specifically, small ice islands form on SHS, as opposed to a large ice front. Further, due to the lowered surface area from the hydrophobic surface, aerodynamic forces on the blade allow these islands to glide off the blade, maintaining proper aerodynamics. SHS can be combined with heating elements to further prevent ice formation.

#### Lightning

Lightning damage over the course of a 25-year lifetime goes from surface level scorching and cracking of the laminate material, to ruptures in the blade or full separation in the adhesives that hold the blade together. It is most common to observe lightning strikes on the tips of the blades, especially in rainy weather due to embedded copper wiring. The most common method countermeasure, especially in non-conducting blade materials like GFRPs and CFRPs, is to add lightning "arresters", which are metallic wires that ground the blade, skipping the blades and gearbox entirely.

### Blade repair

Wind turbine blades typically require repair after 2–5 years. Notable causes of blade damage comes from manufacturing defects, transportation, assembly, installation, lightning strikes, environmental wear, thermal cycling, leading edge erosion, or fatigue. Due to composite blade material and function, repair techniques found in aerospace applications often apply or provide a basis for basic repairs.

Depending on the nature of the damage, the approach of blade repairs can vary. Erosion repair and protection includes coatings, tapes, or shields. Structural repairs require bonding or fastening new material to the damaged area. Nonstructural matrix cracks and delaminations require fills and seals or resin injections. If ignored, minor cracks or delaminations can propagate and create structural damage.

Four zones have been identified with their respective repair needs:

- Zone 1- the blade's leading edge. Requires erosion or crack repair.
- Zone 2- close to the tip but behind the leading edge. Requires aeroelastic semi-structural repair.
- Zone 3- Middle area behind the leading edge. Requires erosion repair.
- Zone 4- Root and near root of the blade. Requires semi-structural or structural repairs

After the past few decades of rapid wind expansion across the globe, wind turbines are aging. This aging brings operation and maintenance(O&M) costs along with it, increasing as turbines approach their end of life. If damages to blades are not caught in time, power production and blade lifespan are decreased. Estimates project that 20-25% of the total levelized cost per kWh produced stems from blade O&M alone.

### Blade recycling

The Global Wind Energy Council (GWEC) predicted that wind energy will supply 28.5% of global energy by 2030. This requires a newer and larger fleet of more efficient turbines and the corresponding decommissioning of older ones. Based on a European Wind Energy Association study, in 2010 between 110 and 140 kilotonnes of composites were consumed to manufacture blades. The majority of the blade material ends up as waste and requires recycling or downcycling. As of 2020, most end-of-use blades are stored or sent to landfills rather than recycled. It is also important to note that recent studies predict that nearly 52,000 tons of turbine blades are to be decommissioned every year until 2030. Typically, glass-fiber-reinforced polymers (GFRPs) comprise around 70% of the laminate material in the blade. GFRPs are not combustible and so hinder the incineration of combustible materials. The following methods are the major EOL paths for turbine blades, with methods varying depending on whether individual fibers are to be recovered and the requisite temperature/catalysts.

- **Mechanical recycling**: This method doesn't recover individual fibers. Initial processes involve shredding, crushing, or milling. The crushed pieces are then separated into fiber-rich and resin-rich fractions. These fractions are ultimately incorporated into new composites either as fillers or reinforcements.
- **Pyrolysis**: Thermal decomposition of the composites recovers individual fibers. For pyrolysis, the material is heated up to 500 °C in an environment without oxygen, causing it to break down into lower-weight organic substances and gaseous products. The glass fibers generally lose 50% of their strength and can be downcycled for fiber reinforcement applications in paints or concrete. This can recover up to approximately 19 MJ/kg at relatively high cost. It requires mechanical pre-processing, similar to that involved in purely mechanical recycling.
- **Solvolysis**: This method involves the polymer matrix undergoing chemical decomposition via solvents including but not limited to acetone, nitric acid, ammonia, and alcohols. Advantages of solvolysis include a lower operation compared to pyrolysis and its ability to yield fibers with favorable surface and mechanical properties. Solvolysis has a significant number of operational considerations, including solvent flow, solvent diffusion, phase transitions, etc., that depend heavily on the polymer structure of the blades, which are notably heterogeneous and contain relatively high numbers of defects and voids. As such, current research focuses on computational modeling of solvolysis to allow for more complete and efficient recycling.
- **Direct structural recycling of composites**: The general idea is to reuse the composite as is, without altering its chemical properties, which can be achieved especially for larger composite material parts by partitioning them into pieces that can be used directly in other applications.

Start-up company Global Fiberglass Solutions claimed in 2020 that it had a method to process blades into pellets and fiber boards for use in flooring and walls. The company started producing samples at a plant in Sweetwater, Texas.
