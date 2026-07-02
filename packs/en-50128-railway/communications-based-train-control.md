---
title: "Communications-based train control"
source: https://en.wikipedia.org/wiki/Communications-based_train_control
domain: en-50128-railway
license: CC-BY-SA-4.0
tags: en 50128, railway software safety, cenelec railway standard, signalling software
fetched: 2026-07-02
---

# Communications-based train control

CBTC deployment in

Madrid Metro

, Spain

Santo Amaro station on

Line 5

of the partially CBTC-enabled

São Paulo Metro

**Communications-based train control** (**CBTC**) is a railway signaling system that uses telecommunications between the train and track equipment for traffic management and infrastructure control. CBTC allows a train's position to be known more accurately than with traditional signaling systems. This can make railway traffic management safer and more efficient. Rapid transit systems (and other railway systems) are able to reduce headways while maintaining or even improving safety.

A CBTC system is a "continuous, automatic train control system utilizing high-resolution train location determination, independent from track circuits; continuous, high-capacity, bidirectional train-to-wayside data communications; and trainborne and wayside processors capable of implementing automatic train protection (ATP) functions, as well as optional automatic train operation (ATO) and **automatic train supervision** (**ATS**) functions," as defined in the IEEE 1474 standard.

## Background and origin

CBTC is a signalling standard defined by the IEEE 1474 standard. The original version was introduced in 1999 and updated in 2004. The aim was to create consistency and standardisation between digital railway signalling systems that allow for an increase in train capacity through what the standard defines as high-resolution train location determination. The standard therefore does not require the use of moving block railway signalling, but in practice this is the most common arrangement.

### Moving block

Traditional signalling systems detect trains in discrete sections of the track called 'blocks', each protected by signals that prevent a train entering an occupied block. Since every block is a fixed section of track, these systems are referred to as fixed block systems.

In a moving block CBTC system the protected section for each train is a "block" that moves with and trails behind it, and provides continuous communication of the train's exact position via radio, inductive loop, etc.

As a result, Bombardier opened the world's first radio-based CBTC system at San Francisco airport's automated people mover (APM) in February 2003. A few months later, in June 2003, Alstom introduced the railway application of its radio technology on the Singapore North East Line. CBTC has its origins in the loop-based systems developed by Alcatel SEL (later Thales, now Hitachi Rail) for the Bombardier Automated Rapid Transit (ART) systems in Canada during the mid-1980s.

These systems, which were also referred to as transmission-based train control (TBTC), made use of inductive loop transmission techniques for track to train communication, introducing an alternative to track circuit based communication. This technology, operating in the 30–60 kHz frequency range to communicate trains and wayside equipment, was widely adopted by the metro operators in spite of some electromagnetic compatibility (EMC) issues, as well as other installation and maintenance concerns (see SelTrac for further information regarding transmission-based train-control).

As with new application of any technology, some problems arose at the beginning, mainly due to compatibility and interoperability aspects. However, there have been relevant improvements since then, and currently the reliability of the radio-based communication systems has grown significantly.

Moreover, it is important to highlight that not all the systems using radio communication technology are considered to be CBTC systems. So, for clarity and to keep in line with the state-of-the-art solutions for operator's requirements, this article only covers the latest moving block principle based (either true moving block or virtual block, so not dependent on track-based detection of the trains) CBTC solutions that make use of the radio communications.

## Main features

### CBTC and moving block

CBTC systems are modern railway signaling systems that can mainly be used in urban railway lines (either light or heavy) and APMs, although it could also be deployed on commuter lines. For main lines, a similar system might be the European Railway Traffic Management System ERTMS Level 3 (not yet fully defined ). In the modern CBTC systems the trains continuously calculate and communicate their status via radio to the wayside equipment distributed along the line. This status includes, among other parameters, the exact position, speed, travel direction and braking distance.

This information allows calculation of the area potentially occupied by the train on the track. It also enables the wayside equipment to define the points on the line that must never be passed by the other trains on the same track. These points are communicated to make the trains automatically and continuously adjust their speed while maintaining the safety and comfort (jerk) requirements. So, the trains continuously receive information regarding the distance to the preceding train and are then able to adjust their safety distance accordingly.

From the signalling system perspective, the first figure shows the total occupancy of the leading train by including the whole blocks which the train is located on. This is due to the fact that it is impossible for the system to know exactly where the train actually is within these blocks. Therefore, the fixed block system only allows the following train to move up to the last unoccupied block's border.

In a moving block system as shown in the second figure, the train position and its braking curve is continuously calculated by the trains, and then communicated via radio to the wayside equipment. Thus, the wayside equipment is able to establish protected areas, each one called Limit of Movement Authority (LMA), up to the nearest obstacle (in the figure the tail of the train in front). Movement Authority (MA) is the permission for a train to move to a specific location within the constraints of the infrastructure and with supervision of speed.

End of Authority is the location to which the train is permitted to proceed and where target speed is equal to zero. End of Movement is the location to which the train is permitted to proceed according to an MA. When transmitting an MA, it is the end of the last section given in the MA.

It is important to mention that the occupancy calculated in these systems must include a safety margin for location uncertainty (in yellow in the figure) added to the length of the train. Both of them form what is usually called 'Footprint'. This safety margin depends on the accuracy of the odometry system in the train.

CBTC systems based on moving block allows the reduction of the safety distance between two consecutive trains. This distance is varying according to the continuous updates of the train location and speed, maintaining the safety requirements. This results in a reduced headway between consecutive trains and an increased transport capacity.

### Grades of automation

Modern CBTC systems allow different levels of automation or grades of automation (GoA), as defined and classified in the IEC 62290–1. In fact, CBTC is not a synonym for "driverless" or "automated trains" although it is considered as a basic enabler technology for this purpose.

There are four grades of automation available:

- GoA 0 – On-sight, with no automation
- GoA 1 – Manual, with a driver controlling all train operations.
- GoA 2 – Semi-automatic Operation (STO), starting and stopping are automated, but a driver who sits in the cab operates the doors and drives in emergencies
- GoA 3 – Driverless Train Operation (DTO), starting and stopping are automated, but a crew member operates the doors from within the train
- GoA 4 – Unattended Train Operation (UTO), starting, stopping and doors are all automated, with no required crew member on board

### Main applications

CBTC systems allow optimal use of the railway infrastructure as well as achieving maximum capacity and minimum headway between operating trains, while maintaining the safety requirements. These systems are suitable for the new highly demanding urban lines, but also to be overlaid on existing lines in order to improve their performance.

Of course, in the case of upgrading existing lines the design, installation, test and commissioning stages are much more critical. This is mainly due to the challenge of deploying the overlying system without disrupting the revenue service.

### Main benefits

The evolution of the technology and the experience gained in operation over the last 30 years means that modern CBTC systems are more reliable and less prone to failure than older train control systems. CBTC systems normally have less wayside equipment and their diagnostic and monitoring tools have been improved, which makes them easier to implement and, more importantly, easier to maintain.

CBTC technology is evolving, making use of the latest techniques and components to offer more compact systems and simpler architectures. For instance, with the advent of modern electronics it has been possible to build in redundancy so that single failures do not adversely impact operational availability.

Moreover, these systems offer complete flexibility in terms of operational schedules or timetables, enabling urban rail operators to respond to the specific traffic demand more swiftly and efficiently and to solve traffic congestion problems. In fact, automatic operation systems have the potential to significantly reduce the headway and improve the traffic capacity compared to manual driving systems.

Finally, it is important to mention that the CBTC systems have proven to be more energy efficient than traditional manually driven systems. The use of new functionalities, such as automatic driving strategies or a better adaptation of the transport offer to the actual demand, allows significant energy savings reducing the power consumption.

### Risks

The primary risk of an electronic train control system is that if the communications link between any of the trains is disrupted, all or part of the system might have to enter a failsafe state until the problem is remedied. Depending on the severity of the communication loss, this state can range from vehicles temporarily reducing speed, coming to a halt or operating in a degraded mode until communications are re-established. If communication outage is permanent, some sort of contingency operation must be implemented which may consist of manual operation using absolute block or, in the worst case, the substitution of an alternative form of transportation.

As a result, high availability of CBTC systems is crucial for proper operation, especially if such systems are used to increase transport capacity and reduce headway. System redundancy and recovery mechanisms must then be thoroughly checked to achieve a high robustness in operation. With the increased availability of the CBTC system, there is also a need for extensive training and periodical refresh of system operators on the recovery procedures. In fact, one of the major system hazards in CBTC systems is the probability of human error and improper application of recovery procedures if the system becomes unavailable.

Communications failures can result from equipment malfunction, electromagnetic interference, weak signal strength or saturation of the communications medium. In this case, an interruption can result in a service brake or emergency brake application as real time situational awareness is a critical safety requirement for CBTC and if these interruptions are frequent enough it could seriously impact service. This is the reason why, historically, CBTC systems first implemented radio communication systems in 2003, when the required technology was mature enough for critical applications.

In systems with poor line of sight or spectrum/bandwidth limitations a larger than anticipated number of transponders may be required to enhance the service. This is usually more of an issue with applying CBTC to existing transit systems in tunnels that were not designed from the outset to support it. An alternate method to improve system availability in tunnels is the use of leaky feeder cable that, while having higher initial costs (material + installation) achieves a more reliable radio link.

With the emerging services over open ISM radio bands (i.e. 2.4 GHz and 5.8 GHz) and the potential disruption over critical CBTC services, there is an increasing pressure in the international community (ref. report 676 of UITP organization, Reservation of a Frequency Spectrum for Critical Safety Applications dedicated to Urban Rail Systems) to reserve a frequency band specifically for radio-based urban rail systems. Such decision would help standardize CBTC systems across the market (a growing demand from most operators) and ensure availability for those critical systems.

As a CBTC system is required to have high availability and particularly, allow for a graceful degradation, a secondary method of signaling might be provided to ensure some level of non-degraded service upon partial or complete CBTC unavailability. This is particularly relevant for brownfield implementations (lines with an already existing signalling system) where the infrastructure design cannot be controlled and coexistence with legacy systems is required, at least, temporarily.

For example, the BMT Canarsie Line in New York City was outfitted with a backup automatic block signaling system capable of supporting 12 trains per hour (tph), compared with the 26 tph of the CBTC system. Although this is a rather common architecture for resignalling projects, it can negate some of the cost savings of CBTC if applied to new lines. This is still a key point in the CBTC development (and is still being discussed), since some providers and operators argue that a fully redundant architecture of the CBTC system may however achieve high availability values by itself.

In principle, CBTC systems may be designed with centralized supervision systems in order to improve maintainability and reduce installation costs. If so, there is an increased risk of a single point of failure that could disrupt service over an entire system or line. Fixed block systems usually work with distributed logic that are normally more resistant to such outages. Therefore, a careful analysis of the benefits and risks of a given CBTC architecture (centralized vs. distributed) must be done during system design.

When CBTC is applied to systems that previously ran under complete human control with operators working on sight it may actually result in a reduction in capacity (albeit with an increase in safety). This is because CBTC operates with less positional certainty than human sight and also with greater margins for error as worst-case train parameters are applied for the design (e.g. guaranteed emergency brake rate vs. nominal brake rate). For instance, CBTC introduction in Philly's Center City trolley tunnel resulted initially in a marked increase in travel time and corresponding decrease in capacity when compared with the unprotected manual driving. This was the offset to finally eradicate vehicle collisions which on-sight driving cannot avoid and showcases the usual conflicts between operation and safety.

## Architecture

The typical architecture of a modern CBTC system comprises the following main subsystems:

1. **Wayside equipment**, which includes balises, interlockings and the subsystems controlling every zone in the line or network (typically containing the wayside ATP and ATO functionalities). Depending on the suppliers, the architectures may be centralized or distributed. The control of the system is performed from a central command automatic train supervision (ATS) system, though local control subsystems may be also included as a fallback.
2. **CBTC onboard equipment**, including ATP and ATO subsystems in the vehicles.
3. **Train to wayside communication subsystem**, currently based on radio links.

Thus, although a CBTC architecture is always depending on the supplier and its technical approach, the following logical components may be found generally in a typical CBTC architecture:

- **Onboard ATP system**. This subsystem is in charge of the continuous control of the train speed according to the safety profile, and applying the brake if it is necessary. It is also in charge of the communication with the wayside ATP subsystem in order to exchange the information needed for a safe operation (sending speed and braking distance, and receiving the limit of movement authority for a safe operation).
- **Onboard ATO system**. It is responsible for the automatic control of the traction and braking effort in order to keep the train under the threshold established by the ATP subsystem. Its main task is either to facilitate the driver or attendant functions, or even to operate the train in a fully automatic mode while maintaining the traffic regulation targets and passenger comfort. It also allows the selection of different automatic driving strategies to adapt the runtime or even reduce the power consumption.
- **Wayside ATP system**. This subsystem undertakes the management of all the communications with the trains in its area. Additionally, it calculates the limits of movement authority that every train must respect while operating in the mentioned area. This task is therefore critical for the operation safety.
- **Wayside ATO system**. It is in charge of controlling the destination and regulation targets of every train. The wayside ATO functionality provides all the trains in the system with their destination as well as with other data such as the dwell time in the stations. Additionally, it may also perform auxiliary and non-safety related tasks, for instance alarm/event communication and management, or handling skip/hold station commands.
- **Communication system**. The CBTC systems integrate a digital networked radio system by means of antennas or leaky feeder cable for the bi-directional communication between the track equipment and the trains. The 2,4GHz band is commonly used in these systems (same as WiFi), though other alternative frequencies such as 900 MHz (US), 5.8 GHz or other licensed bands may be used as well.
- **ATS system**. The ATS system is commonly integrated within most of the CBTC solutions. Its main task is to act as the interface between the operator and the system, managing the traffic according to the specific regulation criteria. Other tasks may include the event and alarm management as well as acting as the interface with external systems.
- **Interlocking system**. When needed as an independent subsystem (for instance as a fallback system), it will be in charge of the vital control of the trackside objects such as switches or signals, as well as other related functionality. In the case of simpler networks or lines, the functionality of the interlocking may be integrated into the wayside ATP system.

## Projects

CBTC technology has been (and is being) successfully implemented for a variety of applications as shown in the figure below (mid 2011). They range from some implementations with short track, limited numbers of vehicles and few operating modes (such as the airport APMs in Heathrow or Gatwick), to complex overlays on existing railway networks carrying more than a million passengers each day and with more than 100 trains (such as London Underground Jubilee Line and Northern Line, MTR Tuen Ma Line, Klang Valley Mass Rapid Transit, Kajang Line, and Putrajaya Line).

Despite the difficulty, the table below tries to summarize and reference the main radio-based CBTC systems deployed around the world as well as those ongoing projects being developed. Besides, the table distinguishes between the implementations performed over existing and operative systems (brownfield) and those undertaken on completely new lines (greenfield).

### List

Location/system

Lines

Supplier

Solution

Commissioning

km

No. of trains

Type of field

Grade of automation

Notes

Toronto Subway

Line 3 (SRT)

Thales

SelTrac

1985

6.4

7

Greenfield

UTO

With train attendants who monitor door status, and drive trains in the event of a disruption.

Réseau express métropolitain

(Montréal)

A1-4

Alstom

Urbalis 400

2023-2027

67

212

Greenfield

UTO

Initially opened in 2023, The full 67 km is projected to be opened in 2027

SkyTrain (Vancouver)

Expo Line

,

Millennium Line

,

Canada Line

Thales

SelTrac

1985

85.4

176

Greenfield

UTO

Detroit

Detroit People Mover

Thales

SelTrac

1987

4.7

12

Greenfield

UTO

London

Docklands Light Railway

Thales

SelTrac

1987

38

149

Greenfield

DTO

With train attendants (T\train captains) who drive trains in the event of a disruption.

San Francisco Airport

AirTrain

Bombardier

CITYFLO

650

2003

5

38

Greenfield

UTO

Seattle-Tacoma Airport

Satellite Transit System

Bombardier

CITYFLO

650

2003

3

22

Brownfield

UTO

Singapore MRT

North East Line

Alstom

Urbalis 300

2003

20

43

Greenfield

UTO

With train attendants (train captains) who drive trains in the event of a disruption.

Hong Kong MTR

Tuen Ma line

Thales

SelTrac

2020 (Tuen Ma Line Phase 1)

2021 (Tuen Ma Line and former West Rail Line)

57

65

Greenfield (Tai Wai to Hung Hom section only)

Brownfield (other sections)

STO

Existing sections were upgraded from SelTrac IS

Disneyland Resort line

2005

3

3

Greenfield

UTO

Las Vegas

Monorail

Thales

SelTrac

2004

6

36

Greenfield

UTO

Dallas–Fort Worth Airport

Skylink

Bombardier

CITYFLO

650

2005

10

64

Greenfield

UTO

Lausanne Metro

Line M2

Alstom

Urbalis 300

2008

6

18

Greenfield

UTO

London Heathrow Airport

Heathrow APM

Bombardier

CITYFLO

650

2008

1

9

Greenfield

UTO

Madrid Metro

,

Bombardier

CITYFLO

650

2008

48

143

Brownfield

STO

McCarran Airport

McCarran Airport APM

Bombardier

CITYFLO

650

2008

2

10

Brownfield

UTO

Bangkok BTS Skytrain

Silom Line

,

Sukhumvit Line

Bombardier

CITYFLO

450

2009 (Mo Chit - On Nut & National Stadium - Wongwian Yai sections)

2011 (On Nut extension)

2015 (Samrong extension)

2018 (Kheha extension)

2019 (Khu Khot extension)

64.26

98

Brownfield (Mo Chit to On Nut and National Stadium to Saphan Taksin sections)

Greenfield (other sections)

STO

Upgraded from Siemens Trainguard LZB700M CTC in 2009.

Gold Line

CITYFLO

650

2020

1.7

3

Greenfield

UTO

Bangkok MRT

Purple Line

Bombardier

CITYFLO

650

2015

23

21

Greenfield

STO

With train attendants who drive trains in the event of a disruption. These train attendants are on standby in the train.

Pink

,

Yellow

2021

62.52

58

UTO

Barcelona Metro

,

,

Siemens

Trainguard MT CBTC

2009 (Line 9, Line 11)

2010 (Line 10)

46

50

Greenfield

UTO

New York City Subway

BMT Canarsie Line

,

IRT Flushing Line

Siemens

Trainguard MT CBTC

2009

17

69

Brownfield

STO

Singapore MRT

Circle Line

Alstom

Urbalis 300

2009

35

64

Greenfield

UTO

With train attendants (Rovers) who drive trains in the event of a disruption. These train attendants are also on standby between

Botanic Gardens

and

Caldecott

stations.

Taipei Metro

Neihu-Mucha

Bombardier

CITYFLO

650

2009

26

76

Greenfield and Brownfield

UTO

Washington-Dulles Airport

Dulles APM

Thales

SelTrac

2009

8

29

Greenfield

UTO

São Paulo Metro

1

,

2

,

3

Alstom

Urbalis

2010

62

142

Greenfield and Brownfield

UTO

CBTC operates in Lines 1 and 2 and it is being installed in Line 3

4

Siemens

Trainguard MT CBTC

13

29

Greenfield

First UTO line in Latin America

London Underground

Jubilee line

Thales

SelTrac

2010

37

63

Brownfield

STO

London Gatwick Airport

Shuttle Transit APM

Bombardier

CITYFLO

650

2010

1

6

Brownfield

UTO

Milan Metro

1

Alstom

Urbalis

2010

27

68

Brownfield

STO

Philadelphia SEPTA

SEPTA subway–surface trolley lines

Bombardier

CITYFLO

650

2010

8

115

STO

B&G Metro

Busan-Gimhae Light Rail Transit

Thales

SelTrac

2011

23.5

25

Greenfield

UTO

Dubai Metro

Red

,

Green

Thales

SelTrac

2011

70

85

Greenfield

UTO

Madrid Metro

Extension MetroEste

Invensys

Sirius

2011

9

?

Brownfield

STO

Paris Métro

1

Siemens

Trainguard MT CBTC

2011

16

53

Brownfield

DTO

Sacramento International Airport

Sacramento APM

Bombardier

CITYFLO

650

2011

1

2

Greenfield

UTO

Yongin

EverLine

Bombardier

CITYFLO

650

2011

19

30

UTO

Algiers Metro

1

Siemens

Trainguard MT CBTC

2012

9

14

Greenfield

STO

Istanbul Metro

M4

Thales

SelTrac

2012

21.7

Greenfield

M5

Bombardier

CityFLO 650

2017-2018

16.9

21

Greenfield

UTO

Opened in 2 phases the first in 2017 and the second in 2018

Ankara Metro

M1

Ansaldo STS

CBTC

2018

14.6

Brownfield

STO

M2

Ansaldo STS

CBTC

2014

16.5

Greenfield

STO

M3

Ansaldo STS

CBTC

2014

15.5

Greenfield

STO

M4

Ansaldo STS

CBTC

2017

9.2

Greenfield

STO

Mexico City Metro

Alstom

Urbalis

2012

25

30

Greenfield

STO

Siemens

Trainguard MT CBTC

2022-2024

18

39

Brownfield

DTO

New York City Subway

IND Culver Line

Thales & Siemens

Various

2012

Greenfield

A test track was retrofitted in 2012; the line's other tracks will be retrofitted by the early 2020s.

Phoenix Sky Harbor Airport

PHX Sky Train

Bombardier

CITYFLO

650

2012

3

18

Greenfield

UTO

Riyadh

KAFD Monorail

Bombardier

CITYFLO

650

2012

4

12

Greenfield

UTO

São Paulo Commuter Lines

8

,

10

,

11

Invensys

Sirius

2012

107

136

Brownfield

UTO

Caracas Metro

1

Invensys

Sirius

2013

21

48

Brownfield

Málaga Metro

,

Alstom

Urbalis

2013

17

15

Greenfield

ATO

Paris Métro

3

,

5

Ansaldo STS / Siemens

Inside RATP's

Ouragan project

2010, 2013

26

40

Brownfield

STO

13

Thales

SelTrac

23

66

Toronto subway

1

Alstom

Urbalis 400

2017 to 2022

76.78

65

Brownfield

(Finch to Sheppard West)

Greenfield

(Sheppard West to Vaughan)

STO

CBTC active between

Vaughan Metropolitan Centre

and

Eglinton

stations as of October 2021.

The entire line is scheduled to be fully upgraded by 2022.

Singapore MRT

Downtown Line

Invensys

Sirius

2013

42

92

Greenfield

UTO

With train attendants who drive trains in the event of a disruption.

Budapest Metro

M2

,

M4

Siemens

Trainguard MT CBTC

2013 (M2)

2014 (M4)

17

41

Line M2: STO

Line M4: UTO

Dubai Metro

Al Sufouh LRT

Alstom

Urbalis

2014

10

11

Greenfield

STO

Edmonton LRT

Capital Line

,

Metro Line

Thales

SelTrac

2014

24 double track

94

Brownfield

DTO

Helsinki Metro

1

Siemens

Trainguard MT CBTC

2014

35

45.5

Greenfield and Brownfield

STO

Hong Kong International Airport

Hong Kong International Airport Automated People Mover

Thales

SelTrac

2014

4

14

Brownfield

UTO

Incheon Subway

2

Thales

SelTrac

2014

29

37

Greenfield

UTO

Jeddah Airport

King Abdulaziz APM

Bombardier

CITYFLO

650

2014

2

6

Greenfield

UTO

London Underground

Northern line

Thales

SelTrac

2014

58

106

Brownfield

STO

Salvador Metro

4

Thales

SelTrac

2014

33

29

Greenfield

DTO

Massachusetts Bay Transportation Authority

Mattapan Line

Argenia

SafeNet CBTC

2014

6

12

Greenfield

STO

Munich Airport

Munich Airport T2 APM

Bombardier

CITYFLO

650

2014

1

12

Greenfield

UTO

Shinbundang Line

Dx Line

Thales

SelTrac

2014

30.5

12

Greenfield

UTO

Panama Metro

1

Alstom

Urbalis

2014

13.7

17

Greenfield

ATO

São Paulo Metro

15

Bombardier

CITYFLO

650

2014

14

27

Greenfield

UTO

Amsterdam Metro

50

,

51

,

52

,

53

,

54

Alstom

Urbalis

2015

62

85

Greenfield and Brownfield

STO

Delhi Metro

Line 7, Line 9

Bombardier

CITYFLO

650

2018 (Temp. Driver on Board) 2021 (Full ATO Operations) 2024 (transitioning to UTO)

55

São Paulo Metro

5

Bombardier

CITYFLO

650

2015

20

34

Brownfield & Greenfield

UTO

Buenos Aires Underground

Siemens

Trainguard MT CBTC

2016

8

20

?

?

4.5

18

Hong Kong MTR

South Island line

Alstom

Urbalis 400

2016

7

10

Greenfield

UTO

Hyderabad Metro

L1, L2, L3

Thales

SelTrac

2016

72

57

Greenfield

STO

Kochi Metro

L1

Alstom

Urbalis 400

2016

26

25

Greenfield

ATO

New York City Subway

IRT Flushing Line

Thales

SelTrac

2016

17

46

Brownfield and Greenfield

STO

IND Queens Boulevard Line

Siemens/Thales

Trainguard MT CBTC

2017–2022

21.9

309

Brownfield

ATO

Train conductors will be located aboard the train because other parts of the routes using the Queens Boulevard Line will not be equipped with CBTC.

Kuala Lumpur Metro (LRT)

Line 5, Kelana Jaya Line

Thales

SelTrac

2016

91.5

126

Brownfield

UTO

Metro Santiago

Alstom

Urbalis

2016

20

42

Greenfield and Brownfield

DTO

Walt Disney World

Walt Disney World Monorail System

Thales

SelTrac

2016

22

15

Brownfield

UTO

Delhi Metro

Line-8

Nippon Signal

SPARCS

2017 (Temp. Driver on Board) 2021 (Full ATO Operations)

Greenfield

UTO

Lille Metro

1

Alstom

Urbalis

2017

15

27

Brownfield

UTO

Lucknow Metro

L1

Alstom

Urbalis

2017

23

20

Greenfield

ATO

Metro Santiago

Thales

SelTrac

2017

15.4

15

Greenfield

UTO

Stockholm Metro

Red line

Ansaldo STS

CBTC

2017

41

30

Brownfield

STO->UTO

Singapore MRT

North–South Line

Thales

SelTrac

2017

45.3

198

Brownfield

UTO

With train attendants (train captains) who drive trains in the event of a disruption. These train attendants are on standby in the train.

East–West Line

2018

57.2

198

Brownfield (original line)

Greenfield

(Tuas West Extension only)

With train attendants who drive trains in the event of a disruption. These train attendants are on standby in the train.

Copenhagen S-Train

All lines

Siemens

Trainguard MT CBTC

2021

170

136

Brownfield

STO

Doha Metro

L1

Thales

SelTrac

2018

33

35

Greenfield

ATO

New York City Subway

IND Eighth Avenue Line

Siemens/Thales

Trainguard MT CBTC

2018–2024

9.3

Brownfield

ATO

Train conductors will be located aboard the train because other parts of the routes using the Eighth Avenue Line will not be equipped with CBTC.

O-Train

Thales

SelTrac

2018

12.5

34

Greenfield

STO

Port Authority Trans-Hudson (PATH)

All lines

Siemens

Trainguard MT CBTC

2018

22.2

50

Brownfield

ATO

Rennes ART

B

Siemens

Trainguard MT CBTC

2018

12

19

Greenfield

UTO

Riyadh Metro

L4, L5 and L6

Alstom

Urbalis

2018

64

69

Greenfield

ATO

Sosawonsi Co. (

Gyeonggi-do

)

Seohae Line

Siemens

Trainguard MT CBTC

2018

23.3

7

Greenfield

ATO

Buenos Aires Underground

TBD

TBD

2019

11

26

TBD

TBD

Gimpo

Gimpo Goldline

Nippon Signal

SPARCS

2019

23.63

23

Greenfield

UTO

Jakarta MRT

North–south line

Nippon Signal

SPARCS

2019

20.1

16

Greenfield

STO

Panama Metro

2

Alstom

Urbalis

2019

21

21

Greenfield

ATO

Metro Santiago

Thales

SelTrac

2019

21.7

22

Greenfield

UTO

Sydney Metro

Metro North West & Bankstown Line

Alstom

Urbalis 400

2019

37

22

Brownfield

UTO

Singapore MRT

Thomson–East Coast Line

Alstom

Urbalis 400

2020

43

91

Greenfield

UTO

Suvarnabhumi Airport APM

MNTB to SAT-1

Siemens

Trainguard MT CBTC

2020

1

6

Greenfield

UTO

Bucharest Metro

Line M5

Alstom

Urbalis 400

2020

6.9

13

STO

To be fully operational after the delivery of the 13 Alstom Metropolis BM4 trains.

Bay Area Rapid Transit

Red Line

,

Orange Line

,

Yellow Line

,

Green Line

,

Blue Line

Hitachi Rail STS

CBTC

2030

211.5

Brownfield

STO

Lahore

Orange Line

Alstom-Casco

Urabliss888

2020

27

27 (CRRC)

Greenfield

ATO

Hong Kong MTR

East Rail line

Siemens

Trainguard MT CBTC

2021

41.5

37

Brownfield

STO

Lisbon Metro

Blue Line

,

Yellow Line

,

Green Line

Siemens

Trainguard MT CBTC

2021-2027

33.7

84

Brownfield

STO

Baselland Transport (BLT)

Line 19 Waldenburgerbahn

Stadler

NOVA Pro CBTC

2022

13.2

10

Greenfield

STO

São Paulo Metro

17

Thales

SelTrac

2022

17.7

24

Greenfield

UTO

Under construction

Melbourne

Cranbourne line

,

Pakenham line

,

Sunbury line

,

Metro Tunnel

Bombardier

CITYFLO 650

2023

115.8

70

Brownfield

STO

CBTC only available between

West Footscray

and

Clayton

stations

São Paulo Metro

Line 6

Nippon Signal

SPARCS

2023

15

24

Greenfield

UTO

Under construction

Tokyo

Tokyo Metro Marunouchi Line

Mitsubishi

?

2023

27.4

53

Brownfield

?

Tokyo Metro Hibiya Line

?

?

20.3

42

?

Seoul

Sillim Line

LS ELECTRIC

LTran-CX

2023

7.8

?

?

?

JR West

Wakayama Line

?

?

2023

42.5

?

Brownfield

?

Kuala Lumpur Metro (LRT)

Line 11, Shah Alam Line

Thales

SelTrac

2024

36

25

Brownfield

UTO

Marmaray

Lines

Commuter Lines

Invensys

Sirius

?

77

?

Greenfield

STO

Hong Kong MTR

Kwun Tong line

,

Tsuen Wan line

,

Island line

,

Tseung Kwan O line

Alstom-Hitachi Rail (formerly Thales)

Advanced SelTrac

2026-2029

58.1

128

Brownfield

STO & DTO

New York City Subway

IND Crosstown Line

Hitachi Rail (formerly Thales)

SelTrac

2029

16

309

Brownfield

STO

Porto Metro

Alstom

Cityflo 250

2024

3.0

18

Greenfield

STO

Ahmedabad

MEGA

Nippon Signal

SPARCS

?

39.259

96 coaches (rolling stock)

?

?

Baltimore

Baltimore Metro SubwayLink

Hitachi Rail STS

CBTC

2025

24.8

78

Brownfield

STO

New railcars and signalling system undergoing testing, expected to enter service in mid-2025

Transport for London

Elizabeth line

Siemens

Trainguard MT CBTC

2022

42

70

Brownfield

STO

Paddington to Abbey Wood / Stratford

Jabodebek LRT

Bekasi Line

,

Cibubur Line

Siemens

Trainguard MT CBTC

2023

44.4

31

Greenfield

DTO

Oslo Metro

All lines

Siemens

Trainguard MT CBTC

2025-2030

85

115

Greenfield (

Fornebu Line

)

Brownfield (other lines)

STO

Being gradually rolled out throughout the system, first commissioned between

Brattlikollen

and Lambertseter on

Lambertseter Line

.

Atlanta MARTA

All lines

Stadler

NOVA Pro CBTC

2024

77

354

Brownfield

STO

Hartsfield–Jackson Atlanta International Airport

The Plane Train

Alstom

?

2024

4.5

63

Brownfield

UTO

## Notes and references
