---
title: "Adaptive cruise control"
source: https://en.wikipedia.org/wiki/Adaptive_cruise_control
domain: adas-systems
license: CC-BY-SA-4.0
tags: advanced driver assistance, adaptive cruise control, lane departure warning, sensor fusion adas
fetched: 2026-07-02
---

# Adaptive cruise control

**Adaptive cruise control** (**ACC**) is a type of advanced driver-assistance system for road vehicles that automatically adjusts the vehicle speed to maintain a safe distance from vehicles ahead. Using sensors such as radar, lidar, or cameras, ACC can slow the vehicle when traffic ahead reduces speed and accelerate back to a preset speed when the road is clear.

First introduced in the 1990s, ACC has evolved from early laser based systems to more advanced radar and camera-based technologies capable of operating at a full speed ranges, including stop-and-go traffic.

ACC is considered a key component of partially automated driving. Under SAE International's classification, most ACC systems are categorized as Level 1 automation, as they control longitudinal vehicle motion but require continuous driver supervision and do not provide full vehicle autonomy. When combined with steering assistance features such as lane centering, the system may qualify as Level 2 automation.

## Consumer use

Adaptive cruise control (ACC) is an advanced driver-assistance feature that supplements, but does not replace, the role of the driver. The system automates longitudinal vehicle control by adjusting throttle and, in many systems, applying braking to maintain a preset following distance, but it requires continuous driver supervision and does not replace the driver's responsibility for vehicle operation.

During operation, the driver selects a desired cruising speed and following distance. If the vehicle approaches slower-moving traffic, ACC automatically reduces engine power and may apply braking to maintain the selected gap. When traffic conditions permit, the vehicle accelerates back to the preset speed. Some full speed range systems are capable of functioning in stop-and-go traffic, though driver attention remains required.

### Pricing

Adaptive cruise control is commonly offered as standard equipment on higher trim levels, or as part of optional safety or technology packages. The inclusion of ACC may increase a vehicle's price by several hundred to several thousand U.S. dollars depending on the manufacturer and the features bundled with the system.

Because ACC is frequently packaged with other ADAS technologies, such as lane-keeping assist or automatic emergency braking, buyers may pay for a broader safety suite rather than the feature as a standalone option.

## Types

ACC systems are commonly distinguished by the sensing technologies used to detect and track vehicles ahead, most often radar, lidar, cameras, or combinations of these sensors.

### Radar-based systems

Radar-based sensors work by emitting a radio wave at a frequency of either 24 GHz or 77 GHz. As these signals are emitted, the car computes how long it takes for the signal to return, thus finding out how far away a vehicle may be in front of it. Due to the widely distributed beam, radar ACC systems allow for a much wider field of view while still being able to provide accurate measurements of 160+ meters (Roughly 525 feet). These radar systems can be hidden behind plastic fascias; however, the fascias may look different from a vehicle without the feature. For example, Mercedes-Benz packages the radar behind the upper grille in the center and behind a solid plastic panel that has painted slats to simulate the look of the rest of the grille.

Single radar systems are the most common. Systems involving multiple sensors use either two similar hardware sensors like the 2010 Audi A8 or the 2010 Volkswagen Touareg, or one central long range radar coupled with two short radar sensors placed on the corners of the vehicle like the BMW 5 and 6 series.

### Lidar-based systems

Laser-based systems work using LIDAR (Light detection and ranging), allowing laser-based ACC to provide the largest detection distance as well as the best accuracy of all ACC systems. However, laser-based systems do not detect and track vehicles as reliably in adverse weather conditions due to the fact that fog, or water particles in the air may absorb and or redirect the light emitted from the laser, through absorption, scattering, and reflection. Laser based ACC systems also have a more difficult time tracking dirty (and therefore non-reflective) vehicles. Laser-based sensors must be exposed, the sensor (a fairly large black box) is typically found in the lower grille, offset to one side.

### Camera-based systems

Camera-based adaptive cruise control (ACC) uses one or more forward-facing cameras to detect and track vehicles ahead using computer vision. Instead of directly measuring range with reflected radio waves (radar) or laser pulses (lidar), camera-based systems infer distance and closing speed from image cues such as object size and motion across frames, and when stereo cameras are used, by estimating depth from parallax between two views.

Some camera-based ACC implementations use **stereo (binocular)** camera arrangements mounted near the windshield, enabling depth perception without radar. Subaru's EyeSight is a well-known example of this approach; Subaru describes EyeSight as using camera-based sensing to support adaptive cruise control and related driver-assistance functions.

Other systems use **multiple cameras** with machine-learning-based perception. Tesla’s “Tesla Vision” is a camera-dominant approach in which vehicles rely primarily on onboard cameras and neural-network processing for adaptive cruise control and other driver-assistance features.

### Multi-sensor systems

Some ACC systems combine multiple sensor types, most commonly radar and cameras, to improve vehicle detection and tracking across varying conditions. In such systems, radar provides robust range and relative-speed measurements, while cameras provide additional visual context for object classification and scene interpretation.

## Predictive systems

Predictive adaptive cruise control (PACC) builds on conventional ACC by incorporating forward-looking data and behavioral estimation to modify vehicle speed in anticipation of upcoming conditions. Rather than reacting only to the distance and relative speed of a preceding vehicle, predictive systems use additional information to adjust speed proactively.

In production vehicles, PACC uses navigation and map data to anticipate roadway features. Some systems incorporate GPS location data, digital maps, and traffic sign recognition to automatically adjust vehicle speed in response to upcoming curves, changes in speed limits, or highway exits. By combining sensor input with navigation information, the system can reduce speed before reaching a lower speed zone or approaching a bend, rather than responding after the change occurs.

These predictive functions are typically implemented as part of a broader driver-assistance package, such as Ford Blue Cruise, GM Super Cruise, or Tesla Autopilot. These systems integrate adaptive cruise control with lane centering, high-precision maps, and driver-monitoring to enable wider autonomy features on compatible roads, distinguishing them from basic ACC implementations. Guidance from U.S. and insurance-industry safety organizations emphasize that these systems remain assistance features and still require active driver supervision.

## Regulations

Adaptive cruise control (ACC) is regulated primarily by **ISO 15622:2018** — Intelligent transport systems — Adaptive cruise control systems — Performance requirements and test procedures, which establishes minimum functional requirements, control behavior, driver interface elements, diagnostics, and performance test procedures for ACC systems. The standard defines ACC as a partial automation of longitudinal vehicle control and distinguishes between **Full Speed Range Adaptive Cruise Control (FSRA)** and **Limited Speed Range Adaptive Cruise Control (LSRA)** systems.

Because ACC systems may automatically apply braking, they must also comply with applicable vehicle braking regulations. In countries applying the UNECE framework, braking performance and electronic braking control requirements are governed by **UN Regulation No. 13-H**, which sets safety and performance standards for passenger car braking systems. ACC systems that provide active brake control must operate within the limits prescribed by these braking regulations.

## History

Adaptive cruise control developed during the 1990s as an extension of conventional cruise control, initially focusing on forward distance detection rather than full longitudinal automation. Early systems relied on lidar sensors and were limited to warning functions or throttle control without automatic braking. By the late 1990s and early 2000s, radar-based systems capable of modulating both throttle and braking began to appear in production vehicles. Over time, manufacturers expanded ACC functionality to include full-speed-range stop-and-go operation, integration with collision mitigation systems, and, later, coordination with lane-centering features. By the mid-2010s, adaptive cruise control had become a core component of Level 2 driver-assistance systems and was increasingly offered as standard equipment across vehicle segments.

- 1992: Mitsubishi Motors was the first to offer a lidar-based distance detection system on the Japanese market Debonair. Marketed as "distance warning", this system warns the driver, without influencing throttle, brakes, or gearshifting.
- 1995: Mitsubishi Diamante introduced laser "Preview Distance Control". This system controlled speed through throttle control and downshifting, but could not apply the brakes.
- 1997: Toyota offered a "laser adaptive cruise control" (lidar) system on the Japanese market Celsior. It controlled speed through throttle control and downshifting, but could not apply the brakes.
- 1999: Mercedes introduced "Distronic", the first radar-assisted ACC, on the Mercedes-Benz S-Class (W220) and the CL-Class.
- 1999: Jaguar began offering a radar-based ACC system on the Jaguar XK (X100).
- 1999: Nissan introduced laser ACC on the Japanese market Nissan Cima.
- 1999: Subaru introduced world's first camera-based ACC on the Japanese-market Subaru Legacy Lancaster.
- 2000: BMW introduced radar "Active Cruise Control" in Europe on the BMW 7 Series - E38.
- 2000: Toyota was the first to bring laser ACC to the US market in late 2000, with the LS 430 Dynamic Laser Cruise Control system.
- 2000: Toyota's laser ACC system added "brake control", that also applies brakes.
- 2001: Infiniti introduced laser "Intelligent Cruise Control" on the 2002 Infiniti Q45 Third generation F50 and 2002 Infiniti QX4.
- 2001: Renault introduced ACC on the Renault Vel Satis (supplied by Bosch)
- 2002: Lancia introduced radar ACC (by Bosch) on the Lancia Thesis
- 2002: Volkswagen introduced radar ACC, manufactured by Autocruise (now TRW), on the Volkswagen Phaeton.
- 2002: Audi introduced radar ACC (Autocruise) on the Audi A8 in late 2002
- 2003: Cadillac introduced radar ACC on the Cadillac XLR.
- 2003: Toyota shifted from laser to radar ACC on the Celsior. The first Lexus Dynamic Radar Cruise Control and a radar-guided pre-collision system appeared on the Lexus LS (XF30) US market facelift.
- 2004: Toyota added "low-speed tracking mode" to the radar ACC on the Crown Majesta. The low-speed tracking mode was a second mode that would warn the driver and provide braking if the car ahead stopped; it could stop the car, but would then deactivate.
- 2005: In the United States, Acura introduced radar ACC integrated with a Collision avoidance system (Collision Mitigation Braking System (CMBS)) in the model year 2006 Acura RL.
- 2005: Mercedes-Benz S-Class (W221) upgraded ACC to completely halt the car if necessary (now called "Distronic Plus" on E-Class and most Mercedes sedans).
- 2006: Volkswagen Passat B6 introduced radar ACC supplied by Autocruise and TRW, functioning from 30 to 210 km/h (19 to 130 mph). It supported additional functions AWV1 and AWV2 to prevent collisions by using the brake system.
- 2006: Audi introduced full speed range ACC plus on the Audi Q7. In low-speed mode, it warns the driver of a potential collision and prepares emergency braking as needed. The system was supplied by Bosch.
- 2006: Nissan introduced "Intelligent Cruise Control with Distance Control Assist" on Nissan Fuga. It pushes the gas pedal against the foot when the navigation system observes an unsafe speed. If the Autonomous cruise control system is used, the Distance Control Assistance reduced speed automatically and warned the driver with an audible bell sound.
- 2006: September 2006 Toyota introduced its "all-speed tracking function" for the Lexus LS 460. The radar-assisted system maintained continuous control from speeds from 0 to 100 km/h (0 to 62 mph) and is designed to work under stop/go situations such as highway traffic congestion.
- 2007: BMW introduced full-speed Active Cruise Control Stop-and-Go on the BMW 5 Series (E60).
- 2008: Lincoln introduced radar ACC on the 2009 Lincoln MKS.
- 2008: SsangYong Motor Company introduced radar "Active Cruise Control" on the SsangYong Chairman
- 2008: Volkswagen Passat CC, B6 and Touareg GP. The ACC system was updated to support a full auto stop and added Front Assist function to prevent collisions working separately of ACC. Front Assist cannot brake automatically, it only increases the pressure in the brake system and warns the driver.
- 2008: Volkswagen Golf 6 introduced ACC with lidar.
- 2009: Hyundai introduced radar ACC on Hyundai Equus in Korean market.
- 2009: ACC and CMBS also became available as optional feature for the 2010 Acura MDX Mid Model Change (MMC) and the newly introduced model year 2010 Acura ZDX.
- 2010: Ford debuted its first ACC on the sixth generation Ford Taurus (option on most models, standard on the SHO)
- 2010: Audi introduced a GPS-guided radar ACC on Audi A8#D4
- 2010: Volkswagen Passat B7, CC. Update of ACC and updated Front Assist. Introduced emergency braking, named "City". The car could brake automatically to prevent a collision.
- 2010: Jeep introduced ACC on the 2011 Jeep Grand Cherokee
- 2012: Volkswagen made ACC standard on the Volkswagen Golf MK7 SE and above.
- 2013: Mercedes introduced "Distronic Plus with Steering Assist" (traffic jam assist) on the Mercedes-Benz S-Class (W222)
- 2013: BMW introduced Active Cruise Control with Traffic Jam Assistant.
- 2014: Chrysler introduced full speed range radar "Adaptive Cruise Control with Stop+" on the 2015 Chrysler 200.
- 2014: Tesla Motors introduced autopilot feature to Model S cars, enabling semi-autonomous cruise control.
- 2015: Ford introduced the first pickup truck with ACC on the 2015 Ford F150.
- 2015: Honda introduced its European CR-V 2015 with predictive cruise control.
- 2015: Volvo began offering ACC on all its models.
- 2017: Cadillac introduced its Super Cruise semi-autonomous feature in the model year 2018 CT6 (for cars produced on or after 6 September 2017). The system used onboard radar and cameras along with lidar mapping data, allowing the driver to go hands-free on limited-access highways.
- 2017: Toyota introduced its safety sense on all models as a standard feature. Toyota Safety Sense P (TSS-P) includes DRCC (dynamic radar cruise control) that uses a front-grille-mounted radar and a forward-facing camera that is designed to detect a vehicle in front and automatically adjust the vehicle's speed to help maintain a pre-set distance behind a vehicle ahead.

## Vehicle models supporting adaptive cruise control

The three main categories of ACC are:

- Vehicles with *Full Speed Range 0MPH* are able to bring the car to a full stop to 0 mph (0 km/h) and need to be re-activated to continue moving with something like a tap of the gas pedal.
- Vehicles with *Traffic Jam Assist / Stop & Go* auto-resume from standstill to creep with stop and go traffic.
- Vehicles with *Partial cruise control* cuts off and turns off below a set minimum speed, requiring driver intervention.
- Vehicles with fully automated speed control can respond to traffic signals and non-vehicular on-road activity.

| Make | Full speed range ACC | Partial cruise control |   |   |
|---|---|---|---|---|
| Models | Notes | Models | Notes |   |
| Aftermarket |   |   | Any Vehicle 1990+ | Uses OpenCV with no braking. Motor Authority Review |
| Acura | RLX (2014+), MDX (2014+), TLX (2015+) |   | 2005 RL, MDX, ZDX, 2016 MDX is 0 mph type, 2016 ILX, RDX |   |
| Alfa Romeo | Giulia (2016+) | Adaptive Cruise Control with Stop & Go |   |   |
| Audi | A8, A7 (2010+), A6 (2011+); A7 (2013+), Q7 (2007+), A3 Prestige (2013+), Q5 (2013+), A5 (2016+), A4 (2016+) | Adaptive Cruise Control with Stop & Go | A3, A4(2008–16, questionable for 2005–07), A5(2007–15), Q5 (2008–12), A6 (questionable for 2004–10), A7, A8 (2002–09) (also uses data from navigation and front camera sensors), Q7 |   |
| Bentley | Continental GT (2009+) | Follow-to-Stop option |   |   |
| BMW | 3 and 5-series (2007+), 7-series (2009+), X5 (2011+) excl Diesel, i3 (2014+), X3 (2014+) | Active Cruise Control with Stop & Go (BMW Option Code S5DFA) | Series 7, 5, 6, 3 (2000+), Mini (2014+) | Stop & Go/Lane Assist controls steering for up to 30 seconds of hands-off driving. Highway driving only. Available on 3, 5, 6 and 7 models. (BMW Option Code S541A) Active Cruise Control |
| Buick | Enclave (2018+), Envision (2017+), Regal/Regal Sportback/ Regal TourX (2016+), Lacrosse (2017+) |   | Lacrosse (2014–2016), Regal (2014–2015) |   |
| Cadillac | XTS, ATS, SRX (2013+), CTS (2014+), ELR, Escalade/Escalade ESV (2015+ Premium trim) | Also includes full power automatic braking under 20 mph (32 km/h) (GM Option 'RPO' Code KSG) | 2004 XLR, 2005 STS, 2006 DTS (shuts off below 25 mph (40 km/h)) |   |
| Chevrolet | Bolt & Bolt EUV (2022+), Impala (2014+), Malibu (2016+), Volt (2017+), Traverse (2018+ High Country trim only), Tahoe/Suburban (2017+ Premier trim), Blazer (2019+), Equinox (2019+), Silverado (2020+ LT, LTZ and High Country trims) | Adaptive Cruise Control - Advanced with Traffic Jam Assist (GM Option 'RPO' Code KSG) | Tahoe/Suburban (2015-2016 LTZ trim), | Adaptive Cruise Control - Camera, Disables when the vehicle slows to under 10 mph (16 km/h) (GM Option 'RPO' Code K59) |
| Chrysler | 200c (2015+), 300 (2015+ in S, C, or C Platinum trims), Pacifica & Pacifica Hybrid (2017+ in Touring L Plus or Limited trims) | Active Cruise Control with Stop & Go. | 2007–2014 300C | Laser, for a limited time, now uses a Bosch radar-based system |
| Citroen | C4 Picasso & Grand C4 Picasso (2013–22), C5 Aircross | Adaptive Cruise Control with Stop & Go | C4 (2004–10), C4 Picasso (2006–13), Berlingo (2018+), C4 Cactus |   |
| Dodge | Charger (2015+), Challenger (2015+) |   | 2011 Charger, 2011 Durango | Radar, by Bosch |
| Ford | Everest (2015+, Trend and Titanium models only), Fusion (2017+), F-150 (2018+), Expedition (2018+), Mustang (2015+, Premium models only), Focus (2018+) | Adaptive cruise control with stop-and-go (optional) | 2015-2017 F150 2011+Explorer, 2017+ Fiesta, 2013+ Ford FLEX, 2006 Mondeo, 2013 Kuga, 2013-2016 Fusion, S-Max, Galaxy, 2010+ Taurus, 2011+ Edge, 2017+ Super Duty, 2019+ Ranger | Disables and does not work or brake under 20 mph (32 km/h); - Radar Adaptive Cruise Control and Collision Warning with Brake Support |
| GMC | Acadia (2017+ Denali), Yukon/Yukon XL (2017+ Denali), Terrain (2019+), Sierra (2020+ SLT, AT4 and Denali) | Adaptive Cruise Control - Advanced with Traffic Jam Assist (GM Option 'RPO' Code KSG) | Yukon/Yukon XL (2015-2016 Denali) | Adaptive Cruise Control - Camera, Disables when the vehicle slows to under 10 mph (16 km/h) (GM Option 'RPO' Code K59) |
| Honda | Accord (2018+), CRV (2017+), Available with Honda Sensing package (2016+) | Adaptive Cruise Control (ACC) with Low-Speed Follow | 2003 Inspire, 2005 Legend, 2013 Accord (USA), 2007 CR-V series III, 2015 Honda CRV, 2016+ Honda Pilot, 2018 Honda Odyssey | Adaptive Cruise Control and Collision Mitigating Braking System with Honda Sensing |
| Hyundai | Azera (2016+), Equus (2012+), Genesis (2015+), Sonata (2015+), Santa Fe (2017+), Santa Fe Sport (2017+), Ioniq (2017+), Palisade (2019+), Ioniq 5 (2022+) |   | Genesis (2010+), Elantra (2017+) |   |
| Infiniti | EX (2010+)*, Q50 (2014+) | Older laser based system* | 2006 EX, M, Q45, QX56, G35, FX35/45/50, G37 | Shuts off below 3 mph, EX: in North America as an option, shuts off below 40 km/h (25 mph) |
| Jaguar |   |   | XK8 / XKR (X100) (1999–2006), XK / XKR (X150) (2006–2014), S-Type, XJ, XF |   |
| Jeep | Cherokee (2014+, Limited and TrailHawk Models), Grand Cherokee (2012+), Wrangler (2018+) | Adaptive Cruise Control (ACC) - Stop/Start again option on 2017 models but not prior models. | 2011–2013 Grand Cherokee (Option on Limited & Overland, standard on Summit) | Radar, by Bosch disengages below 15 mph (24 km/h) |
| Kia | Cadenza (2014+), Sedona (2015+), K900 (2015+), Optima (2016+), Sorento (2016+), Niro (2017+), Telluride (2019+), EV6 (2022+) | Advanced Smart Cruise Control (ASCC) |   |   |
| Land Rover | Range Rover (L405) (2013+) |   | Range Rover Sport (L320) (2005–2013) Range Rover (L322) (2010–2012) | Above 20 mph (32 km/h). Later models (~2010-) can add full speed range by (unofficial) software upgrade. Discovery 3 and 4 can retrofit L320 system with custom mounting hardware |
| Lincoln | Continental (2017+), MKZ (2017+) | Adaptive cruise control with stop-and-go. | MKS (2009+), MKT (2010+), MKX (2011+), MKZ (2013+), MKC (2015+) | Radar Adaptive Cruise Control and Collision Warning with Brake Support |
| Lexus | LS 460 (2006+), GS hybrid (2013+), NX (2015+), NX hybrid (2015+), GS non-hybrid (2016+), RX (2016+), RX hybrid (2016+), UX (2019+), ES (2019+) | Dynamic Radar Cruise Control LS 460 full ACC not available in US until 2013 | 2000 LS430/460 (laser and radar), RX (laser and radar), GS, IS, ES 350, and LX 570 (shuts off below 25 mph (40 km/h)) |   |
| Mazda | CX-5 (2017+), CX-9 (2017+), Mazda3 (2020+), Mazda CX-30 (2020+), Mazda6 (2021+) | Mazda Radar Cruise Control with Stop and Go | Mazda6 (2014+), Mazda3, CX-5 (2016+) | Radar Cruise Control and Forward Obstruction Warning |
| Mitsubishi | Outlander (2014+) |   |   |   |
| Mercedes-Benz | S (2006+), B, E, CLS, CL (2009+); A, CLA, M, G, GL (2013+) | Distronic Plus | 1998 S, E, CLS, SL, CL, M, GL, CLK, 2012 C | Distronic |
| Nissan | Murano (2015+), Maxima (2016+), Altima (2016+), Sentra (2017+), Note (2017+), Leaf (2018+), Titan (2020+) | Stops vehicle but resets after 3 seconds, requiring brake application to sit still and setting cruise speed again. | 1998 Cima, Primera T-Spec Models | Intelligent Cruise Control (ICC) |
| Peugeot | 3008 and 5008 (2017+), 308 (2017+), 508 (2018+), 208 (2019+), 2008 (2019+) | Adaptive Cruise Control with Stop & Go | 3008 and 5008 (2009–16), Partner (2018+) |   |
| Porsche | Panamera (2010+); Cayenne (2011+), Cayman (2013+), Boxster(2012+) | Porsche Active Safe (PAS), PDK transmission only. |   |   |
| Ram | 1500/2500/3500 (2019+) | Adaptive Cruise with Stop |   |   |
| SEAT | León (2012+), Ateca |   |   |   |
| Skoda | Octavia (2013+), Fabia (2014+), Superb (2014+) |   |   |   |
| Subaru | Legacy, Outback (2013+), Forester (2014+), Impreza (2015+), WRX (2016+), Crosstrek (2016+), Ascent (2019+) | 0 mph EyeSight Non-Radar Camera System |   |   |
| Suzuki | Swift 2017+ |   | Vitara (2015+), Sx4 Scross (2016+) | Radar |
| Tesla | Model S (late 2014+), Model X, Model 3, Model Y | Traffic-Aware Cruise Control (TACC) with Stop-and-Go |   |   |
| Toyota | Prius + Prius Prime (2016+), Camry (2018+), C-HR (2018+), Avalon (2017+), Land Cruiser (2018+), Rav 4 (2019+), Corolla (only Hatchback) (2019), Corolla Sedan (2017+) Toyota Safety Sense P (TSS-P), Corolla Sedan and Hatchback (2020+) | Toyota Safety Sense (TSS-P) (on 2017+ Land Cruiser, Avalon and Avalon Hybrid, Prius, Corolla, Prius Prime, RAV4 and RAV4 Hybrid, Highlander and Highlander Hybrid), Toyota Safety Sense (TSS) 2.0 on 2019+ RAV4 and 2020+ Corolla has full speed range. | 1997 Celsior, 2004 Sienna (XLE Limited Edition), Avalon, Sequoia (Platinum Edition), Avensis, 2009 Corolla (Japan), 2017+ Corolla, 2010+ Prius, 2013+ Prius v, 2014+ Highlander, 2015+ Camry, 2016+ RAV4 | Dynamic Laser Cruise Control (DLCC) on 2009+ Sienna XLE Limited, Avalon Limited and Sequoia Platinum shuts off below 25 mph (40 km/h) (US) |
| Vauxhall / Opel |   |   | Insignia, Zafira Tourer (on selected variants of SE, SRi, Elite, VXR), Astra |   |
| Volkswagen | Phaeton (2010+), Passat B8 (2014+), Touareg (2011+), Golf Mk7 (2013+), Polo (2014+), Jetta (2016+ SEL Trim), Tiguan SEL (2018+), ATLAS SEL (2018+) | Tiguan SEL and ATLAS SEL (2018+) ACC stop-and-go | Passat, Phaeton all generations, Touareg |   |
| Volvo | All Volvo models 2015+ Starting in 2008 ACC was available as an option on V40, S60, V60, XC60, V70, XC70 and S80 | ACC also includes automatic braking. Newest models feature full power auto-brake with pedestrian and cyclist detection. |   |   |

### Mercedes Distronic Plus

In 1999, Mercedes introduced Distronic, the first radar-assisted adaptive system, on the Mercedes-Benz S-Class (W220) and the CL-Class. Distronic adjusts the vehicle speed automatically to the car in front in order to always maintain a safe distance to other cars on the road.

In 2005, Mercedes refined the system ("Distronic Plus") making the Mercedes-Benz S-Class (W221) the first car to receive the upgraded system. Distronic Plus could now completely halt the car if necessary on most sedans. In an episode of *Top Gear*, Jeremy Clarkson demonstrated the effectiveness of the system by coming to a complete halt from motorway speeds to a round-about and getting out, without touching the pedals.

In 2016, Mercedes introduced Active Brake Assist 4, the first emergency braking assistant with pedestrian recognition.

One crash caused by Distronic Plus dates to 2005, when the German news magazine *Stern* was testing Mercedes' original Distronic system. During the test, the system did not always manage to brake in time. Ulrich Mellinghoff, then Head of Safety, NVH, and Testing at the Mercedes-Benz Technology Centre, stated that some tests failed because the vehicle was tested in a metallic hall, which caused problems with radar. Later iterations received an upgraded radar and other sensors, which are not disrupted by a metallic environment. In 2008, Mercedes conducted a study comparing the crash rates of Distronic Plus vehicles and vehicles without it, and concluded that those equipped with Distronic Plus have an around 20% lower crash rate.

## Aftermarket

For some models of cars, Comma.ai offers an aftermarket alternative to factory-built ACC systems through its openpilot software paired with Comma hardware. When installed in a compatible vehicle, OpenPilot replaces or adds to existing ADAS features. This effectively brings Level-2 capabilities to some cars that originally did not have them.
