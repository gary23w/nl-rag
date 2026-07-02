---
title: "Battery charger"
source: https://en.wikipedia.org/wiki/Battery_charger
domain: battery-chemistry-embedded
license: CC-BY-SA-4.0
tags: rechargeable battery, nickel metal hydride battery, lead acid battery, energy density
fetched: 2026-07-02
---

# Battery charger

A **battery charger**, **recharger**, or simply **charger**, is a device that stores energy in an electric battery by running current through it. The charging protocol—how much voltage and current, for how long and what to do when charging is complete—depends on the size and type of the battery being charged. Some battery types have high tolerance for overcharging after the battery has been fully charged and can be recharged by connection to a constant voltage source or a constant current source, depending on battery type.

Simple chargers of this type must be manually disconnected at the end of the charge cycle. Other battery types use a timer to cut off when charging should be complete. Other battery types cannot withstand over-charging, becoming damaged (reduced capacity, reduced lifetime), over heating or even exploding. The charger may have temperature or voltage sensing circuits and a microprocessor controller to safely adjust the charging current and voltage, determine the state of charge, and cut off at the end of charge. Chargers may elevate the output voltage proportionally with current to compensate for impedance in the wires.

A trickle charger provides a relatively small amount of current, only enough to counteract self-discharge of a battery that is idle for a long time. Some battery types cannot tolerate trickle charging; attempts to do so may result in damage. Lithium-ion batteries cannot handle indefinite trickle charging. Slow battery chargers may take several hours to complete a charge. High-rate chargers may restore most capacity much faster, but high-rate chargers can be more than some battery types can tolerate. Such batteries require active monitoring of the battery to protect it from any abusive use. Electric vehicles ideally need high-rate chargers. For public access, installation of such chargers and the distribution support for them is an issue in the proposed adoption of electric cars.

## C-rate

Charge and discharge rates are often given as *C* or *C-rate*, which is a measure of the rate at which a battery is charged or discharged relative to its capacity. The C-rate is defined as the charge or discharge current divided by the battery's capacity to store an electrical charge. While rarely stated explicitly, the unit of the C-rate is h−1, equivalent to stating the battery's capacity to store an electrical charge in unit hour times current in the same unit as the charge or discharge current. The C-rate is never negative, so whether it describes a charging or discharging process depends on the context.

For example, for a battery with a capacity of 500 mAh, a discharge rate of 5000 mA (i.e., 5 A) corresponds to a C-rate of 10C, meaning that such a current can discharge 10 such batteries in one hour. Likewise, for the same battery a charge current of 250 mA corresponds to a C-rate of C/2, meaning that this current will increase the state of charge of this battery by 50% in one hour.

Running current through batteries generates internal heat, roughly proportional to the current involved (a battery's current state of charge, condition / history, etc. are also factors). If the charging process is endothermic (which is the case for Ni–Cd batteries, whereas charging nickel–metal hydride batteries is exothermic) the charging process initially cools the battery, but as it reaches full charge, the cooling effect stops and the cell heats up. Detecting a temperature rise of 10 °C (18 °F) is one way of determining when to stop charging. Battery cells which have been built to allow higher C-rates than usual must make provision for increased heating.

But high C-ratings are attractive to end users because such batteries can be charged more quickly, and produce higher current output in use. High C-rates typically require the charger to carefully monitor battery parameters such as terminal voltage and temperature to prevent overcharging and so damage to the cells. Such high-charging rates are possible only with some battery types. Others will be damaged or possibly overheat or catch fire. Some batteries may even explode. For example, an automobile SLI (starting, lighting, ignition) lead–acid battery carries several risks of explosion.

## Type

### Simple charger

A simple charger works by supplying a constant DC or pulsed DC power source to a battery being charged. A simple charger typically does not alter its output based on charging time or the charge on the battery. This simplicity means that a simple charger is inexpensive, but there are tradeoffs. Typically, a carefully designed simple charger takes longer to charge a battery because it is set to use a lower (i.e., safer) charging rate. Even so, many batteries left on a simple charger for too long will be weakened or destroyed due to over-charging. These chargers also vary in that they can supply either a constant voltage or a constant current, to the battery.

Simple AC-powered battery chargers usually have much higher ripple current and ripple voltage than other kinds of battery chargers because they are inexpensively designed and built. Generally, when the ripple current is within a battery's manufacturer recommended level, the ripple voltage will also be well within the recommended level. The maximum ripple current for a typical 12 V 100 Ah VRLA battery is 5 amperes. As long as the ripple current is not excessive (more than 3 to 4 times the level recommended by the battery manufacturer), the expected life of a ripple-charged VRLA battery will be within 3% of the life of a constant DC-charged battery.

### Fast charger

Fast chargers make use of control circuitry to rapidly charge the batteries without damaging any of the cells in the battery. The control circuitry can be built into the battery (generally for each cell) or in the external charging unit, or split between both. Most such chargers have a cooling fan to help keep the temperature of the cells at safe levels. Most fast chargers are also capable of acting as standard overnight chargers if used with standard Ni–MH cells that do not have the special control circuitry.

### Three-stage charger

To accelerate the charging time and provide continuous charging, an intelligent charger attempts to detect the state of charge and condition of the battery and applies a three-stage charging scheme. The following description assumes a sealed lead–acid traction battery at 25 °C (77 °F). The first stage is referred to as "bulk absorption"; the charging current is held high and constant and is limited by the capacity of the charger. When the voltage on the battery reaches its outgassing voltage (2.22 volts per cell) the charger switches to the second stage, and the voltage is held constant (2.40 volts per cell). The delivered current declines at the maintained voltage, and when the current reaches less than 0.005C the charger enters its third stage and the charger output is held constant at 2.25 volts per cell. In the third stage, the charging current is very small, 0.005C, and at this voltage the battery can be maintained at full charge and compensate for self-discharge.

### Induction-powered charger

Inductive battery chargers use electromagnetic induction to charge batteries. A charging station sends electromagnetic energy through inductive coupling to an electrical device, which stores the energy in the batteries. This is achieved without the need for metal contacts between the charger and the battery. Inductive battery chargers are commonly used in electric toothbrushes and other devices used in bathrooms. Because there are no open electrical contacts, there is no risk of electrocution. Nowadays it is being used to charge wireless phones.

### Smart charger

A smart charger can respond to the condition of a battery and modify its charging parameters accordingly, whereas "dumb" chargers apply a steady voltage, possibly through a fixed resistance. It should not be confused with a smart battery that contains a computer chip and communicates digitally with a smart charger about battery condition. A smart battery requires a smart charger. Some smart chargers can also charge "dumb" batteries, which lack any internal electronics.

The output current of a smart charger depends upon the battery's state. An intelligent charger may monitor the battery's voltage, temperature or charge time to determine the optimum charge current or terminate charging. For Ni–Cd and Ni–MH batteries, the voltage of the battery increases slowly during the charging process, until the battery is fully charged. After that, the voltage *decreases* because of increasing temperature, which indicates to an intelligent charger that the battery is fully charged. Such chargers are often labeled as a ΔV, "delta-V", or sometimes "delta peak" charger, indicating that they monitor voltage change.

This can cause even an intelligent charger not to sense that the batteries are already fully charged, and continue charging, the result of which may be overcharging. Many intelligent chargers employ a variety of cut-off systems to prevent overcharging. A typical smart charger fast-charges a battery up to about 85% of its maximum capacity in less than an hour, then switches to trickle charging, which takes several hours to top off the battery to its full capacity.

### Motion-powered charger

Several companies have begun making devices that charge batteries using energy from human motion, such as walking. An example, made by Tremont Electric, consists of a magnet held between two springs that can charge a battery as the device is moved up and down. Such products have not yet achieved significant commercial success.

A pedal-powered charger for mobile phones fitted into desks has been created for installation in public spaces, such as airports, railway stations and universities. They have been installed in a number of countries on several continents.

### Pulse charger

Some chargers use *pulse technology*, in which a series of electrical pulses is fed to the battery. The DC pulses have a strictly controlled rise time, pulse width, pulse repetition rate (frequency) and amplitude. This technology works with any size and type of battery, including automotive and valve-regulated ones. With pulse charging, high instantaneous voltages are applied without overheating the battery. In a lead–acid battery, this breaks down lead-sulfate crystals, thus greatly extending the battery service life.

Several kinds of pulse chargers are patented, while others are open source hardware. Some chargers use pulses to check the current battery state when the charger is first connected, then use constant current charging during fast charge, then use pulse mode to trickle charge it. Some chargers use "negative pulse charging", also called "reflex charging" or "burp charging". These chargers use both positive and brief negative current pulses. There is no significant evidence that negative pulse charging is more effective than ordinary pulse charging.

### Solar charger

Solar chargers convert light energy into low-voltage DC current. They are generally portable, but can also be fixed mounted. Fixed mount solar chargers are also known as solar panels. These are often connected to the electrical grid via control and interface circuits, whereas portable solar chargers are used off-grid (i.e. cars, boats, or RVs).

Although portable solar chargers obtain energy only from the sun, they can charge in low light like at sunset. Portable solar chargers are often used for trickle charging, though some can completely recharge batteries.

### Timer-based charger

The output of a timer charger is terminated after a predetermined time interval. Timer chargers were the most common type for high-capacity Ni–Cd cells in the late 1990s to charge low-capacity consumer Ni–Cd cells. Often a timer charger and set of batteries could be bought as a bundle and the charger time is set for those batteries specifically. If batteries of lower capacity are charged, then they would be overcharged, and if batteries of higher capacity were timer-charged, they would not reach full capacity. Timer based chargers also had the drawback that charging batteries that were not fully discharged would result in over-charging.

### Trickle charger

A trickle charger is typically low-current (usually between 5–1,500 mA). They are generally used to charge small capacity batteries (2–30 Ah). They are also used to maintain larger capacity batteries (> 30 Ah) in cars and boats. In larger applications, the current of the battery charger is only sufficient to provide trickle current. Depending on the technology of the trickle charger, it can be left connected to the battery indefinitely. Some battery types are not suitable for trickle charging. For instance, most Li-ion batteries cannot be safely trickle charged and can cause a fire or explosion.

### DC-DC charger

Charge DC (battery) from DC source without conversion to AC. Modern DC-DC chargers often include isolator and DC-DC converter. Some may also have BMS (including balance), be bidirectional (jump start primary car battery from secondary battery) and wireless control (Bluetooth, WiFi, NFC, 5G).

### Universal battery charger–analyzer

The most sophisticated chargers are used in critical applications (e.g. military or aviation batteries). These heavy-duty automatic "intelligent charging" systems can be programmed with complex charging cycles specified by the battery manufacturer. The best are universal (i.e. can charge all battery types), and include automatic capacity testing and analyzing functions.

### USB-based charger

Since the Universal Serial Bus specification provides five-volt power, it is possible to use a USB cable to connect a device to a power supply. Products based on this approach include chargers for cellular phones, portable digital audio players, and tablet computers. They may be fully compliant USB peripheral devices or uncontrolled, simple chargers. Another type of USB charger called "USB (rechargeable) battery" is fitted into the case of standard batteries (1.5 V AA, C, D, and 9 V block) together with a Li-ion rechargeable battery, voltage converter, and USB connector.

### Solar charger

## Applications

Since a battery charger is intended to be connected to a battery, it may not have voltage regulation or filtering of the DC voltage output; it is cheaper to make them that way. Battery chargers equipped with both voltage regulation and filtering are sometimes termed battery eliminators.

### Battery charger for vehicles

There are two main types of chargers used for vehicles:

- To recharge a fuel vehicle's starter battery, where a modular charger is used; typically an 3-stage charger.
- To recharge an electric vehicle (EV) battery pack; see Charging station.

Chargers for car batteries come in varying ratings. Chargers that are rated up to two amperes may be used to maintain charge on parked vehicle batteries or for small batteries on garden tractors or similar equipment. A motorist may keep a charger rated a few amperes to ten or fifteen amperes for maintenance of automobile batteries or to recharge a vehicle battery that has accidentally discharged. Service stations and commercial garages will have a large charger to fully charge a battery in an hour or two; often these chargers can briefly source the hundreds of amperes required to crank an internal combustion engine starter.

### Electric vehicle batteries

Electric vehicle battery chargers (ECS) come in a variety of brands and characteristics. These chargers vary from 1 kW to 22 kW maximum charge rate. Some use algorithm charge curves, others use constant voltage, constant current. Some are programmable by the end user through a CAN port, some have dials for maximum voltage and amperage, some are preset to specified battery pack voltage, ampere-hour and chemistry. Prices range from $400 to $4,500. A 10-ampere-hour battery could take 15 hours to reach a fully charged state from a fully discharged condition with a 1-ampere charger as it would require roughly 1.5 times the battery's capacity. Public EV charging stations often provide 6 kW (host power of 208 to 240 V AC off a 40-ampere circuit). 6 kW will recharge an EV roughly six times faster than 1 kW overnight charging. Rapid charging results in even faster recharge times and is limited only by available AC power, battery type, and the type of charging system.

Onboard EV chargers (change AC power to DC power to recharge the EV's pack) can be:

- Isolated: they make no physical connection between the A/C electrical mains and the batteries being charged. These typically employ some form of inductive connection between the grid and a charging vehicle. Some isolated chargers may be used in parallel. This allows for an increased charge current and reduced charging times. The battery has a maximum current rating that cannot be exceeded
- Non-isolated: the battery charger has a direct electrical connection to the A/C outlet's wiring. Non-isolated chargers cannot be used in parallel.

Power-factor correction (PFC) chargers can more closely approach the maximum current the plug can deliver, shortening charging time.

#### Charge stations

Project Better Place was deploying a network of charging stations and subsidizing vehicle battery costs through leases and credits until filing for bankruptcy in May 2013.

#### Induction-powered charging

Researchers at the Korea Advanced Institute of Science and Technology (KAIST) have developed an electric transport system, called Online Electric Vehicle (OLEV), where the vehicles get their power needs from cables underneath the surface of the road via inductive charging, a power source is placed underneath the road surface and power is wirelessly picked up on the vehicle itself.

### Mobile phone charger

Most mobile phone chargers are not really chargers, only power adapters that provide a power source for the charging circuitry which is almost always contained within the mobile phone. Some higher-end models feature multiple ports which are equipped with a display which indicates output current. Some support communication protocols for charging parameters such as Qualcomm Quick Charge or MediaTek Pump Express. Chargers for 12 V automobile auxiliary power outlets may support input voltages of up to 24 or 32 V DC to ensure compatibility, and are sometimes equipped with a display to monitor current or the voltage of the vehicle's electrical system.

China, the European Union, and other countries are making a national standard on mobile phone chargers using the USB standard. In June 2009, 10 of the world's largest mobile phone manufacturers signed a Memorandum of Understanding to develop specifications for and support a microUSB-equipped common external power supply (EPS) for all data-enabled mobile phones sold in the EU. On October 22, 2009, the International Telecommunication Union announced that microUSB would be the standard for a universal charger for mobile handsets. In October 2022 the EU's Common Charger Directive was approved with the new rules applying to mobile phones and a number of other devices, which came into force in December 2024.

### Stationary battery plants

Telecommunications, electric power, and computer uninterruptible power supply facilities may have very large standby battery banks (installed in battery rooms) to maintain critical loads for several hours during interruptions of primary grid power. Such chargers are permanently installed and equipped with temperature compensation, supervisory alarms for various system faults, and often redundant independent power supplies and redundant rectifier systems.

Chargers for stationary battery plants may have adequate voltage regulation and filtration and sufficient current capacity to allow the battery to be disconnected for maintenance, while the charger supplies the direct current (DC) system load. The capacity of the charger is specified to maintain the system load and recharge a completely discharged battery within, say, 8 hours or other intervals.

## Prolonging battery life

A properly designed charger can allow batteries to reach their full cycle life. Excess charging current, lengthy overcharging, or cell reversal in a multiple cell pack cause damage to cells and limit the life expectancy of a battery.

Most modern cell phones, laptop and tablet computers, and most electric vehicles use lithium-ion batteries. These batteries last longest if the battery is frequently charged; fully discharging the cells will degrade their capacity relatively quickly, but most such batteries are used in equipment which can sense the approach of full discharge and discontinue equipment use. When stored after charging, lithium battery cells degrade more while fully charged than if they are only 40–50% charged. As with all battery types, degradation also occurs faster at higher temperatures.

Degradation in lithium-ion batteries is caused by an increased internal battery resistance often due to the cell oxidation. This decreases the efficiency of the battery, resulting in less net current available to be drawn from the battery. However, if Li-ion cells are discharged below a certain voltage a chemical reaction occurs that make them dangerous if recharged, which is why many such batteries in consumer goods now have an "electronic fuse" that permanently disables them if the voltage falls below a set level. The electronic fuse circuitry draws a small amount of current from the battery, which means that if a laptop battery is left for a long time without charging it, and with a very low initial state of charge, the battery may be permanently destroyed.

Motor vehicles, such as boats, RVs, ATVs, motorcycles, cars, trucks, etc. have used lead–acid batteries. These batteries employ a sulfuric acid electrolyte and can generally be charged and discharged without exhibiting memory effect, though sulfation (a chemical reaction in the battery which deposits a layer of sulfates on the lead) will occur over time. Typically sulfated batteries are simply replaced with new batteries, and the old ones recycled. Lead–acid batteries will experience substantially longer life when a maintenance charger is used to "float charge" the battery. This prevents the battery from ever being below 100% charge, preventing sulfate from forming. Proper temperature compensated float voltage should be used to achieve the best results.

## Recent advances

Battery charging technology is developing to support the increasing demands of electric vehicles (EVs), consumer electronics, and sustainable energy systems. Modern chargers may feature Internet of things (IoT) connectivity for real-time monitoring, adaptive charging protocols, remote management, predictive maintenance, and may enhance safety and efficiency.

Artificial intelligence (AI) is being integrated into battery management systems to optimize charging rates, predict battery health, extend usable life, and maximize energy efficiency.

As a result of electric mobility and smart device proliferation, the global battery charger market is projected (as of 2025) to see significant growth over the following decade. Smart chargers integrating IoT, AI, and adaptive features are expected to outpace traditional models globally.
