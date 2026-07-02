---
title: "Railway signalling (part 1/2)"
source: https://en.wikipedia.org/wiki/Railway_signalling
domain: en-50128-railway
license: CC-BY-SA-4.0
tags: en 50128, railway software safety, cenelec railway standard, signalling software
fetched: 2026-07-02
part: 1/2
---

# Railway signalling

**Railway signalling** (British English), or **railroad signaling** (American English), is a system used to control the movement of railway traffic. Trains move on fixed rails, making them uniquely susceptible to collision. This susceptibility is exacerbated by the enormous weight and inertia of a train, which makes it difficult to quickly stop when encountering an obstacle. In the UK, the Regulation of Railways Act 1889 introduced a series of requirements on matters such as the implementation of interlocked block signalling and other safety measures as a direct result of the Armagh rail disaster in that year.

Most forms of train control involve movement authority being passed from those responsible for each section of a rail network (e.g. a signalman or stationmaster) to the train crew. The set of rules and the physical equipment used to accomplish this determine what is known as the *method of working* (UK), *method of operation* (US) or *safe-working* (Aus.). Not all these methods require the use of physical signals, and some systems are specific to single-track railways.

The earliest rail cars were hauled by horses or mules. A mounted flagman on a horse preceded some early trains. Hand and arm signals were used to direct the "train drivers". Foggy and poor-visibility conditions later gave rise to flags and lanterns. Wayside signalling dates back as far as 1832, and used elevated flags or balls that could be seen from afar.


## Timetable operation

The simplest form of operation, at least in terms of equipment, is to run the system according to a timetable. Every train crew understands and adheres to a fixed schedule. Trains may only run on each track section at a scheduled time, during which they have 'possession' and no other train may use the same section.

When trains run in opposite directions on a single-track railway, meeting points ("meets") are scheduled, at which each train must wait for the other at a passing place. Neither train is permitted to move before the other has arrived. In the US, the display of two green flags (green lights at night) is an indication that another train is following the first and the waiting train must wait for the next train to pass. In addition, the train carrying the flags gives eight blasts on the whistle as it approaches. The waiting train must return eight blasts before the flag carrying train may proceed.

The timetable system has several disadvantages. First, there is no positive confirmation that the track ahead is clear, only that it is scheduled to be clear. The system does not allow for engine failures and other such problems, but the timetable is set up so that there should be sufficient time between trains for the crew of a failed or delayed train to walk far enough to set warning flags, flares, and *detonators* or *torpedoes* (UK and US terminology, respectively) to alert any other train crew.

A second problem is the system's inflexibility. Trains cannot be added, delayed, or rescheduled without advance notice.

A third problem is a corollary of the second: the system is inefficient. To provide flexibility, the timetable must give trains a broad allocation of time to allow for delays, so the line is not in the possession of each train for longer than is otherwise necessary.

Nonetheless, this system permits operation on a vast scale, with no requirements for any kind of communication that travels faster than a train. Timetable operation was the normal mode of operation in North America in the early days of the railroad.

### Timetable and train order

With the advent of the telegraph in 1841, a more sophisticated system became possible because this provided a means whereby messages could be transmitted ahead of the trains. The telegraph allows the dissemination of any timetable changes, known as *train orders*. These allow the cancellation, rescheduling and addition of train services.

North American practice meant that train crews generally received their orders at the next station at which they stopped, or were sometimes handed up to a locomotive 'on the run' via a long staff. Train orders allowed dispatchers to set up meets at sidings, force a train to wait in a siding for a priority train to pass, and to maintain at least one block spacing between trains going the same direction.

Timetable and train order operation was commonly used on American railroads until the 1960s, including some quite large operations such as the Wabash Railroad and the Nickel Plate Road. Train order traffic control was used in Canada until the late 1980s on the Algoma Central Railway and some spurs of the Canadian Pacific Railway.

Timetable and train order was not used widely outside North America, and has been phased out in favour of radio dispatch on many light-traffic lines and electronic signals on high-traffic lines. More details of North American operating methods is given below.

A similar method, known as 'Telegraph and Crossing Order' was used on some busy single lines in the UK during the 19th century. However, a series of head-on collisions resulted from authority to proceed being wrongly given or misunderstood by the train crew - the worst of which was the collision between Norwich and Brundall, Norfolk, in 1874. As a result, the system was phased out in favour of token systems. This eliminated the danger of ambiguous or conflicting instructions being given because token systems rely on objects to give authority, rather than verbal or written instructions; whereas it is very difficult to completely prevent conflicting orders being given, it is relatively simple to prevent conflicting tokens being handed out.


## Block signalling

Trains cannot collide with each other if they are not permitted to occupy the same section of track at the same time, so railway lines are divided into sections known as *blocks*. In normal circumstances, only one train is permitted in each block at a time. This principle forms the basis of most railway safety systems. Blocks can either be fixed (block limits are fixed along the line) or moving blocks (ends of blocks defined relative to moving trains).

### History of block signalling

On double tracked railway lines, which enabled trains to travel in one direction on each track, it was necessary to space trains far enough apart to ensure that they could not collide. In the very early days of railways, men (originally called 'policemen', which is the origin of UK signalmen being referred to as "bob", "bobby" or "officer", when train-crew are speaking to them via a signal telephone) were employed to stand at intervals ("blocks") along the line with a stopwatch and use hand signals to inform train drivers that a train had passed more or less than a certain number of minutes previously. This was called "time interval working". If a train had passed very recently, the following train was expected to slow down to allow more space to develop.

The watchmen had no way of knowing whether a train had cleared the line ahead, so if a preceding train stopped for any reason, the crew of a following train would have no way of knowing unless it was clearly visible. As a result, accidents were common in the early days of railways. With the invention of the electrical telegraph, it became possible for staff at a station or signal box to send a message (usually a specific number of rings on a bell) to confirm that a train had passed and that a specific block was clear. This was called the "absolute block system".

Fixed mechanical signals began to replace hand signals from the 1830s. These were originally worked locally, but it later became normal practice to operate all the signals on a particular block with levers grouped together in a signal box. When a train passed into a block, a signalman would protect that block by setting its signal to 'danger'. When an 'all clear' message was received, the signalman would move the signal into the 'clear' position.

The absolute block system came into use gradually during the 1850s and 1860s and became mandatory in the United Kingdom after Parliament passed legislation in 1889 following a number of accidents, most notably the Armagh rail disaster. This required block signalling for all passenger railways, together with interlocking, both of which form the basis of modern signalling practice today. Similar legislation was passed by the United States around the same time.

Not all blocks are controlled using fixed signals. On some single track railways in the UK, particularly those with low usage, it is common to use token systems that rely on the train driver's physical possession of a unique token as authority to occupy the line, normally in addition to fixed signals.

### Entering and leaving a manually controlled block

Before allowing a train to enter a block, a signalman must be certain that it is not already occupied. When a train leaves a block, they must inform the signalman controlling entry to the block. Even if the signalman receives advice that the previous train has left a block, they are usually required to seek permission from the next signal box to admit the next train. When a train arrives at the end of a block section, before the signalman sends the message that the train has arrived, they must be able to see the end-of-train marker on the back of the last vehicle. This ensures that no part of the train has become detached and remains within the section. The end of train marker might be a coloured disc (usually red) by day or a coloured oil or electric lamp (again, usually red). If a train enters the next block before the signalman sees that the disc or lamp is missing, they ask the next signal box to stop the train and investigate.

### Permissive and absolute blocks

Under a permissive block system, trains are permitted to pass signals indicating the line ahead is occupied, but only at such a speed that they can stop safely should an obstacle come into view. This allows improved efficiency in some situations and is mostly used in the United States. In most countries it is restricted to freight trains only, and it may be restricted depending on the level of visibility.

Permissive block working may also be used in an emergency, either when a driver is unable to contact a signalman after being held at a danger signal for a specific time, although this is only permitted when the signal does not protect any conflicting moves, and also when the signalman is unable to contact the next signal box to make sure the previous train has passed, for example if the telegraph wires are down. In these cases, trains must proceed at very low speed (typically 32 km/h (20 mph) or less) so that they are able to stop short of any obstruction. In most cases, this is not allowed during times of poor visibility (e.g., fog or falling snow).

Even with an absolute block system, multiple trains may enter a block with authorization. This may be necessary in order to split or join trains together, or to rescue failed trains. In giving authorization, the signalman also ensures that the driver knows precisely what to expect ahead. The driver must operate the train in a safe manner taking this information into account. Generally, the signal remains at danger, and the driver is given verbal authority, usually by a yellow flag, to pass a signal at danger, and the presence of the train in front is explained. Where trains regularly enter occupied blocks, such as stations where coupling takes place, a subsidiary signal, sometimes known as a "calling on" signal, is provided for these movements, otherwise they are accomplished through train orders.

### Automatic block

The invention of train detection systems such as track circuits allowed the replacement of manual block systems such as absolute block with automatic block signalling. Under automatic block signalling, signals indicate whether or not a train may enter a block based on automatic train detection indicating whether a block is clear. The signals may also be controlled by a signalman, so that they only provide a *proceed* indication if the signalman sets the signal accordingly and the block is clear.

### Fixed block

Most blocks are "fixed", i.e. they include the section of track between two fixed points. On timetable, train order, and token-based systems, blocks usually start and end at selected stations. On signalling-based systems, blocks start and end at signals.

The lengths of blocks are designed to allow trains to operate as frequently as necessary. A lightly used line might have blocks many kilometres long, but a busy commuter line might have blocks a few hundred metres long.

A train is not permitted to enter a block until a signal indicates that the train may proceed, a dispatcher or signalman instructs the driver accordingly, or the driver takes possession of the appropriate token. In most cases, a train cannot enter the block until not only the block itself is clear of trains, but there is also an empty section beyond the end of the block for at least the distance required to stop the train. In signalling-based systems with closely spaced signals, this overlap could be as far as the signal following the one at the end of the section, effectively enforcing a space between trains of two blocks.

When calculating the size of the blocks, and therefore the spacing between the signals, the following have to be taken into account:

- Line speed (the maximum permitted speed over the line-section)
- Train speed (the maximum speed of different types of traffic)
- Gradient (to compensate for longer or shorter braking distances)
- The braking characteristics of trains (different types of train, e.g., freight, high-speed passenger, have different inertial figures)
- Sighting (how far ahead a driver can see a signal)
- Reaction time (of the driver)

Historically, some lines operated so that certain large or high speed trains were signalled under different rules and only given the right of way if two blocks in front of the train were clear.

### Moving block

Under a moving block system, computers calculate a safe zone around each moving train that no other train is allowed to enter. The system depends on knowledge of the precise location and speed and direction of each train, which is determined by a combination of several sensors such as radio frequency identification along the track, ultra-wideband, radar, inertial measurement units, accelerometers and trainborne speedometers (GNSS/GPS systems cannot be relied upon because they do not work in tunnels). Moving block setups require instructions to be directly passed to the train instead of using lineside signals. This has the advantage of increasing track capacity by allowing trains to run closer together while maintaining the required safety margins.


## Centralized traffic control

Centralized traffic control (CTC) is a form of railway signalling that originated in North America. CTC consolidates train routing decisions that were previously carried out by local signal operators or the train crews themselves. The system consists of a centralized train dispatcher's office that controls railroad interlockings and traffic flows in portions of the rail system designated as CTC territory.


## Train detection

Train detection refers to the presence or absence of trains on a defined section of line.

### Track circuits

The most common way to determine whether a section of line is occupied is by use of a track circuit. The rails at either end of each section are electrically isolated from the next section, and an electric current is fed to both running rails at one end. A relay at the other end is connected to both rails. When the section is unoccupied, the relay coil completes an electrical circuit, and is energized. However, when a train enters the section, it short-circuits the current in the rails, and the relay is de-energized. This method does not explicitly need to check that the entire train has left the section. If part of the train remains in the section, the track circuit detects that part.

This type of circuit detects the absence of trains, both for setting the signal indication and for providing various interlocking functions—for example, preventing points from being moved while a train is approaching them. Electrical circuits also *prove* that points are locked in the appropriate position before the signal protecting that route can be cleared. UK trains and staff working in track circuit block areas carry track circuit operating clips (TCOC) so that, in the event of something fouling an adjacent running-line, the track circuit can be short-circuited. This places the signal protecting that line to 'danger' to stop an approaching train before the signaller can be alerted.

### Axle counters

An alternate method of determining the occupied status of a block uses devices located at its beginning and end that count the number of axles that enter and leave the block section. If the number of axles leaving the block section equals those that entered it, the block is assumed to be clear. Axle counters provide similar functions to track circuits, but also exhibit a few other characteristics. In a damp environment an axle counted section can be far longer than a track circuited one. The low ballast resistance of very long track circuits reduces their sensitivity. Track circuits can automatically detect some types of track defect such as a broken rail. In the event of power restoration after a power failure, an axle counted section is left in an undetermined state until a train has passed through the affected section. A track circuited section immediately detects the presence of a train in section.


## Fixed signals

On most railways, physical signals are erected at the lineside to indicate to drivers whether the line ahead is occupied and to ensure that sufficient space exists between trains to allow them to stop.

### Mechanical signals

Older forms of signal displayed their different aspects by their physical position. The earliest types comprised a board that was either turned face-on and fully visible to the driver, or rotated so as to be practically invisible. While this type of signal is still in use in some countries (e.g., France and Germany), by far the most common form of mechanical signal worldwide is the semaphore signal. This comprises a pivoted arm or blade that can be inclined at different angles. A horizontal arm is the most restrictive indication (for 'danger', 'caution', 'stop and proceed' or 'stop and stay' depending on the type of signal).

To enable trains to run at night, one or more lights are usually provided at each signal. Typically this comprises a permanently lit oil lamp with movable coloured spectacles in front that alter the colour of the light. The driver therefore had to learn one set of indications for daytime viewing and another for nighttime viewing.

Whilst it is normal to associate the presentation of a green light with a safe condition, this was not historically the case. In the very early days of railway signalling, the first coloured lights (associated with the turned signals above) presented a white light for 'clear' and a red light for 'danger'. Green was originally used to indicate 'caution' but fell out of use when the time interval system was discontinued. A green light subsequently replaced white for 'clear', to address concerns that a broken red lens could be taken by a driver as a false 'clear' indication. It was not until scientists at Corning Glassworks perfected a shade of yellow without any tinges of green or red that yellow became the accepted colour for 'caution'.

Mechanical signals are usually remotely operated by wire from a lever in a signal box, but electrical or hydraulic operation is normally used for signals that are located too distant for manual operation.

### Colour light signals

On most modern railways, colour light signals have largely replaced mechanical ones. Colour light signals have the advantage of displaying the same aspects by night as by day, and require less maintenance than mechanical signals.

Although signals vary widely between countries, and even between railways within a given country, a typical system of aspects would be:

- Green: Proceed at line speed. Expect to find next signal displaying green or yellow.
- Yellow: Prepare to find next signal displaying red.
- Red: Stop.

On some railways, colour light signals display the same set of aspects as shown by the lights on mechanical signals during darkness.

### Route signalling and speed signalling

*Route signalling* and *speed signalling* are two different ways of notifying trains about junctions.

Under **route signalling**, a driver is informed which route the train will take beyond each signal (unless only one route is possible). This is achieved by a *route indicator* attached to the signal. The driver uses their route knowledge, reinforced by speed restriction signs fixed at the lineside, to drive the train at the correct speed for the route to be taken. This method has the disadvantage that the driver may be unfamiliar with the required speed over a junction onto which they have been diverted due to some emergency condition. Several accidents have been caused by this alone. For this reason, in the UK, where all lines are route signalled, drivers are only allowed to drive on routes that they have been trained on and must regularly travel over the lesser used diversionary routes to keep their route knowledge up to date.

Many route signalling systems use *approach control* (see below) to inform a driver of an upcoming change of route.

Under **speed signalling**, the signal aspect informs the driver at what speed they may proceed over a junction, but not necessarily the route the train will take. Speed signalling requires a far greater range of signal aspects than route signalling, but less dependence is placed on drivers' route knowledge, although the need for drivers to learn the route is not eliminated as speed signalling does not usually inform drivers of speed limit changes outside junctions. Usually speed limit signs are used in addition to speed signals, with the driver following whichever shows the lower speed.

Many systems have come to use elements of both systems to give drivers as much information as possible. This can mean that speed signalling systems may use route indications in conjunction with speed aspects to better inform drivers of their route; for example, route indications may be used at major stations to indicate to arriving trains to which platform they are routed. Likewise, some route signalling systems indicate approach speed using theatre displays so that drivers know what speed they must travel.

- (An example of a signal from Melbourne Victoria: this signal is displaying a speed signalling aspect, in conjunction with a route indicator) An example of a signal from Melbourne Victoria: this signal is displaying a speed signalling aspect, in conjunction with a route indicator

### Approach release

When the train is routed towards a diverging route that must be taken at a speed significantly less than the mainline speed, the driver must be given adequate prior warning.

Under *route signalling*, the aspects necessary to control speed do not exist, so a system known as *approach release* is often employed. This involves holding the junction signal at a restrictive aspect (typically *stop*) so that the signals on the approach show the correct sequence of caution aspects. The driver brakes in accordance with the caution aspect, without necessarily being aware that the diverging route has in fact been set. As the train approaches the junction signal, its aspect may clear to whatever aspect the current track occupancy ahead permits. Where the turnout speed is the same, or nearly the same, as the mainline speed, approach release is unnecessary.

Under *speed signalling*, the signals approaching the divergence display aspects appropriate to control the trains speed, so no *approach release* is required.

There is also a system of *flashing yellows* used in the UK that allows trains to approach a diverging route at higher speed. This informs the driver that the route ahead is set onto a diverging line. With the advent of faster modern day trains and junctions a better system for advising drivers was required and so the following system was developed way back in the early 1980s. The system has been refined over the years, now being used internationally and it is also used on lower speed 3-aspect signalling systems where the *single flashing yellow* is the driver's first indication.

On the 4-aspect system, if the route through the junction is clear the junction signal will display a single *steady yellow* aspect together with an illuminated junction indicator showing the selected route.

The signal prior to the junction signal will now show a *single flashing yellow* aspect and the signal prior to that one will display *two flashing yellow* aspects. The driver's route knowledge tells them permissible speed across the diverging junction, and they will begin to slow the train upon seeing the *two flashing yellows*. The flashing signals tell the driver that the route through the junction is set and is clear, but that beyond that the first signal on the diverging route is *red* so they must be prepared to stop there.

As the train approaches the junction signal, the signal may *step up* to a less restrictive aspect (single *yellow*, *two yellows* or *green*) depending on how far ahead the line is clear.

### Speed-controlled approach

Some systems use mechanical speed control systems in conjunction with signalling to ensure the speed of a train is limited to a specific value, in order to ensure the train is travelling at a speed in which it is able to stop before an obstruction. These systems most often use mechanical train stop devices (a small arm coming up from the rails that will apply the brakes of a train when run over) to "trip" the brakes of a train that is travelling too fast. Normally, once a train reaches a certain point on the tracks, it sets off a timer, when the timer runs out the train stop arm will lower, allowing a train to go past uninterrupted. The timing is designed so that if the train is travelling at the intended speed (or slower) then the train will be able to continue without issue, but if the train is travelling too fast, then the Train Stop will trip the train and bring it to a halt. This system can be used to ensure a train is travelling at a certain speed, which allows designers to be confident that shorter signal overlaps will be sufficient, and thus employment of this system can help to greatly improve capacity of a railway line.

The system is most often used on approach to dead end junctions to stop trains from crashing into the buffers at the end, as has happened in places such as Moorgate. It is also used on high traffic lines to allow for higher capacity, such as the City Circle Railway in Sydney, where it was used on the western half from 1932 to allow 42 trains per hour to traverse the line in each direction, each station would have multiple train stops along the length of the platforms that would progressively lower to ensure an arriving train would not crash into the departing train, less than 100 meters ahead. This system was modified in the early 1990s, so that an arriving train would not be able to enter the platform until the previous train had departed, however the trips continue to be used to overcome the signal overlap normally required.

These systems are often used in conjunction with *progressive speed signalling* (see below).

### Progressive speed signalling

*Progressive speed signalling* refers to systems that impose speed restrictions on cautionary aspects. On systems that do not have progressive speed signalling, aspects warning of an upcoming red signal do not force the driver to take any action; it is up to their own judgment when to start slowing down in preparation to stop at the red signal. With progressive speed signalling, each cautionary aspect before a red signal imposes a successively lower speed limit on the driver. It should not be confused with speed signalling as used at junctions; progressive speed signalling can be used in conjunction with route signalling.


## Signalling the layout

*Signalling the layout* refers to the design process of placing signals on a railway layout.

Due to the low friction between train wheels and rails, trains require large distances to stop safely. Train drivers cannot always stop due to an obstruction they can see. Trains run on fixed rails which guide them, so they must be routed around each other to avoid collision.

The signalling system key goal is to prevent the collision of trains, its secondary goal is to provide as much use of a given track as possible.

### Service braking distance

Service braking distance (SBD) is a critical factor in designing railway signal layouts. Due to the low friction between rail and wheel, and the heaviness of trains, braking distance of a train can be many kilometers. In order to ensure safe spacing of trains, SBD must be used in calculations when placing signals. When signalling a line, the SBD used for that line must be the worse performing train (heaviest, weakest braking, freight trains, locomotive hauled). By accounting for the worst possible train, trains with better braking (multiple units, light, advanced braking, passenger) will also be safe and protected.

Braking distance calculation: $\mathrm {SBD} ={\frac {V^{2}}{2r}}$

Where *V* is train speed before braking and *r* is braking rate. A typical value for r could be $0.5\mathrm {\,m/s^{2}}$ .

#### Example calculation

$V=160\mathrm {\,km/h} =44.44\mathrm {\,m/s}$

$r=0.5\mathrm {\,m/s^{2}}$

$BD={\frac {(44.44\mathrm {\,m/s} )^{2}}{2(0.5\mathrm {\,m/s^{2}} )}}=1974.9\mathrm {\,m}$

*Service braking distance is not an emergency application of brakes.* SBD is the normal application of braking by the driver. For safety reasons we cannot use the minimum braking distance when brakes are applied at maximum: some margin of error must be introduced, which is SBD.

The minimum distance between the first signal at caution and the signal at danger is SBD. This allows the driver to come to a halt from first seeing the caution signal to arriving at the signal at danger.

There is also a maximum distance between signals, usually 1.5×SBD. While it is not intuitive to let there be a maximum distance between signals (ie, if there is a large distance between them it gives the train lots of space to stop), it is required to make sure that signals give clear information. If a distant signal is too far from the next stop signal, the driver may not fully brake assuming he has lots of time to brake, which could lead to an error. By having a maximum distance between the first caution and next signal at danger, it eliminates confusion.

A standard braking distance for average trains (in UK signalling), travelling at a speed of 100 mph (160 km/h) can be taken as 2000 meters.

### Overlaps

Railway blocks require a certain safety margin in case of driver error or external factors (weather conditions, leaf fall). Overlaps take the form of additional detection sections (track circuit or axle counters) which extend past a signal which can display a stop. In UK signalling the standard minimum overlap is 180 m. Overlaps shorter than this must have additional protection measures to prevent signals passed at danger (SPAD).

### Headway

Headway time (HT) is the minimum time between trains, or how many trains can safely and without braking pass a point per unit time:

$\mathrm {HT} ={\frac {\mathrm {HD} }{V}}$

Where HD = headway distance, *V* = maximum permissible line speed.

Headway distance (HD) can be calculated:

$\mathrm {HD} =S+P+O+L$

Where:

- *S* is sighting distance
- *P* is distance from stop aspect to least restrictive aspect (i.e.: the distance from a signal at red to the nearest signal at green, as a train approaches).
- *O* is overlap distance
- *L* is length of train

#### Block distance

Block distance (*D*) is the distance between two signals capable of showing red. It varies between two-, three- and four-aspect signalling. It is a critical number in designing the signalling layout.

Blocks are made up of train detection sections (often shown as a short vertical line). Blocks can be made of one or many detection sections.

##### Two-aspect signalling

There are equations to determine a suitable *D* value.

To satisfy the required headway: $D\leq P-1.5(\mathrm {SBD} )$

To satisfy safety and cost: $P\geq 4(\mathrm {SBD} )$ ∗∗

Generally two-aspect signalling is used when *P* is a lot larger than SBD.

∗∗If *P* is 4 times or less than SBD, two-aspect signalling should not be chosen. This is because the distance between stop signal will be so close that the distant signals starts to encroach on the previous stop signal, creating confusion for the driver. Additionally, since every stop signal needs a distant signal, when they get so close together, it actually becomes cheaper to move on to three-aspect signalling at this point. When $P<4(\mathrm {SBD} )$ , it is both cheaper and safer to use three-aspect signalling. This is not a hard rule, it is still technically possible to use two aspects at this point, but not recommended.

##### Three-aspect signalling

To satisfy safety requirements: $\mathrm {SBD} \leq D\leq 1.5(\mathrm {SBD} )$

To satisfy headway requirements: $D\leq {\frac {P}{2}}$

Three-aspect signalling creates significantly increased capacity over two-aspect signalling.

##### Four-aspect signalling

To satisfy safety requirements: $0.5(\mathrm {SBD} )\leq D\leq 0.75(\mathrm {SBD} )$

To satisfy headway requirements: $D\leq {\frac {P}{3}}$

Four-aspect signalling adds an additional warning signal, which is often a double yellow. This further divides up the railway and allows for more capacity.

#### Example calculation 1

For example, we have a railway with maximum speed (*V*) of 160 km/h (44 m/s). Given a train with standard braking, the service braking distance (SBD) is 2000 m. Standard sighting distance (*S*) of 300 m. Standard overlap (*O*) of 180 m. Train length (*L*) is 200 m.

If a train is required to run every 1 hour (3600 s), what distance must signals be placed to achieve this headway?

Headway: $\mathrm {HT} =\mathrm {HD} /V$

Headway distance: $\mathrm {HD} =\mathrm {HT} \cdot V$

Also: $\mathrm {HD} =S+P+O+L$

${\begin{aligned}P&=\mathrm {HD} -S-O-L\\&=(\mathrm {HT} \cdot V)-S-O-L\\&=3600\mathrm {\,s} (44.44\mathrm {\,m/s} )-300\mathrm {\,m} -180\mathrm {\,m} -200\mathrm {\,m} \\&=159304\mathrm {\,m} .\end{aligned}}$

**Choose the aspect:**

Generally the option with the least cost is chosen first. Since *P* is large ( $>4\mathrm {SBD}$ ), we should choose two-aspect.

The block section (or distance between two stop signals) can be calculated as:

${\begin{aligned}D&\leq P-1.5(\mathrm {SBD} )\\D&\leq 159304\mathrm {\,m} -3000\mathrm {\,m} \\D&\leq 156304\mathrm {\,m} .\end{aligned}}$

*D* cannot be larger than 156304 m, otherwise the required headway (1 train per hour) cannot be met. It is possible to have a lower *D* (increasing possible headway), but we want the lowest cost while achieving desired headway of trains, so close to the max is usually chosen.

#### Example calculation 2

For example, we have a railway with maximum speed (*V*) of 200 km/h (56 m/s). Assuming braking rate of $r=0.5\mathrm {\,m/s^{2}} .$

Standard sighting distance (*S*) of 400 m. Standard overlap (*O*) of 180 m. Train length (*L*) is 300 m. If we ask asked to run a train every 2 minutes (or 30 trains an hour), what distance must signals be placed to achieve this headway?

$\mathrm {SBD} ={\frac {V^{2}}{2r}}={\frac {(55.56\mathrm {\,m/s} )^{2}}{2(0.5\mathrm {\,m/s^{2}} )}}=3085\mathrm {\,m} .$

Headway: $\mathrm {HT} =\mathrm {HD} /V$ .

Headway time: $\mathrm {HT} =120\mathrm {\,s}$ .

Speed: $V=55.56\mathrm {\,m/s}$ .

Headway distance: $\mathrm {HD} =\mathrm {HT} \cdot V=120\mathrm {\,s} \cdot 55.56\mathrm {\,m/s} =6667.2\mathrm {\,m}$ .

${\begin{aligned}P&=\mathrm {HD} -S-O-L\\&=6667.2\mathrm {\,m} -400\mathrm {\,m} -180\mathrm {\,m} -300\mathrm {\,m} \\&=5787.2\mathrm {\,m} .\end{aligned}}$

**Choose the aspect:**

Reminder of SBD:

${\begin{aligned}\mathrm {SBD} &=3085\mathrm {\,m} \\1.5(\mathrm {SBD} )&=4627.5\mathrm {\,m} .\end{aligned}}$

We have found *P*, now we must choose the cheapest aspect type for which *P* and SBD satisfy all equations.

**Does this P satisfy the requirement for two-aspect?**

Since *P* (5787 m) is less than 4SBD (4 × 3085 m = 12340 m), we cannot use two-aspect since the distant signals will be too close to the previous stop signals, creating confusion for the driver. *Two-aspect cannot be used.*

**Does this P satisfy the requirement for three-aspect?** ${\begin{aligned}\mathrm {SBD} &\leq D\leq 1.5(\mathrm {SBD} )\\3085\mathrm {\,m} &\leq D\leq 4627.5\mathrm {\,m} \\\\D&\leq P/2\\D&\leq (5787.2\mathrm {\,m} )/2\\D&\leq 2893.6\mathrm {\,m} .\end{aligned}}$

*Three-aspect cannot work in this situation as both equations cannot be satisfied.* *D* must be greater than 3085 m and less than 2893 m, which is not possible.

**Does this P satisfy the requirement for four-aspect?**

${\begin{aligned}0.5(\mathrm {SBD} )&\leq D\leq 0.75(\mathrm {SBD} )\\1542.5\mathrm {\,m} &\leq D\leq 2313.75\mathrm {\,m} \\\\D&\leq P/3\\D&\leq (5787.2\mathrm {\,m} )/3\\D&\leq 1929.1\mathrm {\,m} .\end{aligned}}$

*This satisfies both equations, which means four-aspect can be used.* *D* must be between 1542 m and 2313 m for braking purposes. *D* must be less than 1929 m to achieve the desired headway between trains.

The block section (or distance between two stop signals) must be in this range:

$1542.5\mathrm {\,m} <D<1929.1\mathrm {\,m} .$

The flexibility on range allows signals to be moved around if other external factors require the signal to be moved.

### Junctions

Once headway calculations are done, other infrastructure must be accounted for (why a flexible range of block distance is required). Railway junctions are moveable infrastructure which must be protected by signals. If a train goes over a railway switch/point and that point is in the wrong position, it can damage the points or cause derailment.

Junctions must be protected by a signal capable of displaying a *stop* aspect. The signal will let the driver know if it is safe to traverse the junction. Using train detection areas, the signalling interlocking can determine if it is safe for a train to pass.

#### Converging Junctions

For converging junctions, the minimum distance for a protecting signal away from the junction is the overlap distance (in UK signalling it is usually 180m). It is measured from the clearance point (CP) of the junction.

There is not necessarily a maximum specified distance to a converging junction. The train does not need to slow down regardless of the position of the points. Even if a train passes over the switches in the wrong position, the force of the train will force the switches over.

Fouling Point and Clearance Point

The fouling point (FP) is the position where two trains would have a side-on collision when approaching a junction. It is measured perpendicularly away from the rails.

The clearance point (CP) is the position in which a train can stop safely in front of a junction to allow another train to safely pass by. The CP is measured a set distance away from the FP.

Signals protecting the junction must be placed at least the length of the overlap away from the clearance point.

#### Diverging Junctions

For diverging junctions, the minimum distance for a protecting signal away from the junction is the overlap distance (in UK signalling it is usually 180m). The diagrams use show route signalling as examples.

For diverging junctions, the maximum distance for a protecting signal away from the junction is a specified distance, which is set by the local railway standards (in UK signalling it is 800m).

Drivers must slow down when taking the diverging route on a set of points (when not going straight through). Therefore a maximum specified distance is required to make sure the instructions to the driver are clear and not forgotten.

So when placing signals that protect diverging junctions, the distance must be between *180m and 800m* (UK signalling).

### Other important factors in placing signals

The position of signals is initially found by using headway calculations, then taking into account the track layout (points, gradients, speed limits), operational requirements, rolling stock and capacity requirements. However, when it comes to the physical positioning of signals, other factors come into consideration:

- Line curvature – may impede vision of signals on the track. Sighting distance may be affected.
- Viaducts, bridges and tunnels – Signals should not be placed so that a train will come to a standstill before a red signal, while it is on a structure. This would make evacuating a train difficult in an emergency.
- Excessive artificial lighting – In areas such as stations, buildings, cities; there may be excessive artificial lighting which could confuse the driver.
- Sunlight – Certain areas of the railway, at certain times of the day, may be strong affected by sunlight.
- The consequences if a signal is passed at danger – Signals must be placed so that if a signal at red is passed by a train, the impact of this will be as low as possible.


## Safety systems

A train driver failing to respond to a signal's indication can be catastrophic. As a result, various auxiliary safety systems have been devised. Any such system requires installation of some degree of train borne and wayside equipment. Some systems only intervene in the event of a signal being passed at danger (SPAD). Others include audible and/or visual indications inside the driver's cab to supplement the line side signals. Automatic brake application occurs if the driver should fail to acknowledge a warning. The most advanced train control systems have no driver at all relying on computers to drive the system entirely such as Skytrain in Vancouver, Canada and the metro system in Doha, Qatar.

In-cab safety systems are of great benefit during fog, when poor visibility would otherwise require that restrictive measures be put in place. Safety systems are also important in urban rail where it is impossible to see around corners in subway and metro tunnels. On-board and wayside computers can track trains around tight corners at higher speeds ensuring safety.


## Cab signalling

Cab signalling is a subsystem that communicates signalling information into the train cab such as driving position, speed and failure alarms. Cab signaling units are important human factors engineering subsystems in modern train signalling systems.

If there is an active cab, the orientation of the train is decided, i.e. the side of the active cab is considered as the front of the train. In modern systems, a train protection system is overlaid on top of the cab signalling system and will automatically apply the brakes and bring the train to a stop if the driver fails to control the speed of the train in accordance with the system's safety requirements. Cab signalling systems rely on tachometers, accelerometers, ultra-wideband units, inertia measurement units, track circuits, to transponders that communicate with the cab, and communication-based train control systems.


## Interlocking

In the early days of the railways, signalmen were responsible for ensuring any points (US: switches) were set correctly before allowing a train to proceed. Mistakes, however, led to accidents, sometimes with fatalities. The concept of the mechanical interlocking of point switches, signals and other appliances was introduced to improve safety. This prevents a signalman from operating appliances in an unsafe sequence using mechanical means, such as clearing a signal while one or more sets of points are not set correctly for the route. Early interlocking systems used mechanical devices both to operate the signalling appliances and to ensure their safe operation.

Beginning around the 1930s, electrical relay interlockings were used. Since the mid 1980s, new interlocking systems have tended to be of the electronic variety. Microprocessors decide what point switch movements are permissible. Modern interlocking systems and subsystems allow and prohibit certain point switch positions to enhance train safety.
