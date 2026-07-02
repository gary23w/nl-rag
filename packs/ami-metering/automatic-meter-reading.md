---
title: "Automatic meter reading"
source: https://en.wikipedia.org/wiki/Automatic_meter_reading
domain: ami-metering
license: CC-BY-SA-4.0
tags: ami metering, advanced metering infrastructure, smart meter network, meter data collection
fetched: 2026-07-02
---

# Automatic meter reading

**Automatic meter reading** (**AMR**) is the technology of automatically collecting consumption, diagnostic, and status data from water meter or energy metering devices (gas, electric) and transferring that data to a central database for billing, troubleshooting, and analyzing. This technology mainly saves utility providers the expense of periodic trips to each physical location to read a meter. Another advantage is that billing can be based on near real-time consumption rather than on estimates based on past or predicted consumption. This timely information coupled with analysis can help both utility providers and customers better control the use and production of electric energy, gas usage, or water consumption.

AMR technologies include handheld, mobile and network technologies based on telephony platforms (wired and wireless), radio frequency (RF), or powerline transmission.

## Technologies

### Touch technology

With touch-based AMR, a meter reader carries a handheld computer or data collection device with a wand or probe. The device automatically collects the readings from a meter by touching or placing the read probe close to a reading coil enclosed in the touchpad. When a button is pressed, the probe sends an interrogate signal to the touch module to collect the meter reading. The software in the device matches the serial number to one in the route database, and saves the meter reading for later download to a billing or data collection computer. Since the meter reader still has to go to the site of the meter, this is sometimes referred to as "on-site" AMR. Another form of contact reader uses a standardized infrared port to transmit data. Protocols are standardized between manufacturers by such documents as ANSI C12.18 or IEC 61107.

### AMR hosting

AMR hosting is a back-office solution which allows a user to track their electricity, water, or gas consumption over the Internet. All data is collected in near real-time, and is stored in a database by data acquisition software. The user can view the data via a web application, and can analyze the data using various online analysis tools such as charting load profiles, analyzing tariff components, and verify their utility bill.

### Radio frequency network

Radio frequency based AMR can take many forms. The more common ones are handheld, mobile, satellite and fixed network solutions. There are both two-way RF systems and one-way RF systems in use that use both licensed and unlicensed RF bands.

In a two-way or "wake up" system, a radio signal is normally sent to an AMR meter's unique serial number, instructing its transceiver to power-up and transmit its data. The meter transceiver and the reading transceiver both send and receive radio signals. In a one-way "bubble-up" or continuous broadcast type system, the meter transmits continuously and data is sent every few seconds. This means the reading device can be a receiver only, and the meter a transmitter only. Data travels only from the meter transmitter to the reading receiver. There are also hybrid systems that combine one-way and two-way techniques, using one-way communication for reading and two-way communication for programming functions.

RF-based meter reading usually eliminates the need for the meter reader to enter the property or home, or to locate and open an underground meter pit. The utility saves money by increased speed of reading, has less liability from entering private property, and has fewer missed readings from being unable to access the meter.

The technology based on RF is not readily accepted everywhere. In several Asian countries, the technology faces a barrier of regulations in place pertaining to use of the radio frequency of any radiated power. For example, in India the radio frequency which is generally in ISM band is not free to use even for low power radio of 10 mW. The majority of manufacturers of electricity meters have radio frequency devices in the frequency band of 433/868 MHz for large scale deployment in European countries. The frequency band of 2.4 GHz can be now used in India for outdoor as well as indoor applications, but few manufacturers have shown products within this frequency band. Initiatives in radio frequency AMR in such countries are being taken up with regulators wherever the cost of licensing outweighs the benefits of AMR.

#### Handheld

In handheld AMR, a meter reader carries a handheld computer with a built-in or attached receiver/transceiver (radio frequency or touch) to collect meter readings from an AMR capable meter. This is sometimes referred to as "walk-by" meter reading since the meter reader walks by the locations where meters are installed as they go through their meter reading route. Handheld computers may also be used to manually enter readings without the use of AMR technology as an alternate but this will not support exhaustive data which can be accurately read using the meter reading electronically.

#### Mobile

Mobile or "drive-by" meter reading is where a reading device is installed in a vehicle. The meter reader drives the vehicle while the reading device automatically collects the meter readings. Often, for mobile meter reading, the reading equipment includes navigational and mapping features provided by GPS and mapping software. With mobile meter reading, the reader does not normally have to read the meters in any particular route order, but just drives the service area until all meters are read. Components often consist of a laptop or proprietary computer, software, RF receiver/transceiver, and external vehicle antennas.

#### Satellite

Transmitters for data collection satellites can be installed in the field next to existing meters. The satellite AMR devices communicate with the meter for readings, and then sends those readings over a fixed or mobile satellite network. This network requires a clear view to the sky for the satellite transmitter/receiver, but eliminates the need to install fixed towers or send out field technicians, thereby being particularly suited for areas with low geographic meter density.

#### RF technologies commonly used for AMR

- Narrow Band (single fixed radio frequency)
- Spread spectrum
  - Direct-sequence spread spectrum (DSSS)
  - Frequency-hopping spread spectrum (FHSS)

There are also meters using AMR with RF technologies such as cellular phone data systems, Zigbee, Bluetooth, Wavenis and others. Some systems operate with U.S. Federal Communications Commission (FCC) licensed frequencies and others under FCC Part 15, which allows use of unlicensed radio frequencies.

#### Wi-Fi

WiSmart is a versatile platform which can be used by a variety of electrical home appliances in order to provide wireless TCP/IP communication using the 802.11 b/g protocol.

Devices such as the Smart Thermostat permit a utility to lower a home's power consumption to help manage power demand.

The city of Corpus Christi became one of the first cities in the United States to implement citywide Wi-Fi, which had been free until May 31, 2007, mainly to facilitate AMR after a meter reader was attacked by a dog. Today many meters are designed to transmit using Wi-Fi, even if a Wi-Fi network is not available, and they are read using a drive-by local Wi-Fi hand held receiver.

The meters installed in Corpus Christi are not directly Wi-Fi enabled, but rather transmit narrow-band burst telemetry on the 460 MHz band. This narrow-band signal has much greater range than Wi-Fi, so the number of receivers required for the project are far fewer. Special receiver stations then decode the narrow-band signals and resend the data via Wi-Fi.

Most of the automated utility meters installed in the Corpus Christi area are battery powered. Wi-Fi technology is unsuitable for long-term battery-powered operation.

### Power line communication

PLC is a method where electronic data is transmitted over power lines back to the substation, then relayed to a central computer in the utility's main office. This would be considered a type of fixed network system—the network being the distribution network which the utility has built and maintains to deliver electric power. Such systems are primarily used for electric meter reading. Some providers have interfaced gas and water meters to feed into a PLC type system.

## Brief history

In 1972, Theodore George "Ted" Paraskevakos, while working with Boeing in Huntsville, Alabama, developed a sensor monitoring system which used digital transmission for security, fire and medical alarm systems as well as meter reading capabilities for all utilities. This technology was a spin-off of the automatic telephone line identification system, now known as caller ID.

In 1974, Paraskevakos was awarded a U.S. patent for this technology. In 1977, he launched Metretek, Inc., which developed and produced the first fully automated, commercially available remote meter reading and load management system. Since this system was developed pre-Internet, Metretek utilized the IBM series 1 mini-computer. For this approach, Paraskevakos and Metretek were awarded multiple patents.

The primary driver for the automation of meter reading is not to reduce labor costs, but to obtain data that is difficult to obtain. As an example, many water meters are installed in locations that require the utility to schedule an appointment with the homeowner in order to obtain access to the meter. In many areas, consumers have demanded that their monthly water bill be based on an actual reading, instead of (for example) an estimated monthly usage based on just one actual meter reading made every 12 months. Early AMR systems often consisted of walk-by and drive-by AMR for residential customers, and telephone-based AMR for commercial or industrial customers. What was once a need for monthly data became a need for daily and even hourly readings of the meters. Consequently, the sales of drive-by and telephone AMR has declined in the US, while sales of fixed networks has increased. The US Energy Policy Act of 2005 asks that electric utility regulators consider the support for a "...time-based rate schedule *(to)* enable the electric consumer to manage energy use and cost through advanced metering and **communications technology**."

The trend now is to consider the use of advanced meters as part of an advanced metering infrastructure.

### Advanced AMR and AMI

Originally AMR devices just collected meter readings electronically and matched them with accounts. As technology has advanced, additional data could then be captured, stored, and transmitted to the main computer, and often the metering devices could be controlled remotely. This can include events alarms such as tamper, leak detection, low battery, or reverse flow. Many AMR devices can also capture interval data, and log meter events. The logged data can be used to collect or control time of use or rate of use data that can be used for water or energy usage profiling, time of use billing, demand forecasting, demand response, rate of flow recording, leak detection, flow monitoring, water and energy conservation enforcement, remote shutoff, etc. Advanced metering infrastructure, or AMI is the new term coined to represent the networking technology of fixed network meter systems that go beyond AMR into remote utility management. The meters in an AMI system are often referred to as smart meters, since they often can use collected data based on programmed logic.

The Automatic Meter Reading Association (AMRA) endorses the National Association of Regulatory Utility Commissioners (NARUC) resolution to eliminate regulatory barriers to the broad implementation of advanced metering infrastructure (AMI). The resolution, passed in February 2007, acknowledged the role of AMI in supporting the implementation of dynamic pricing and the resulting benefits to consumers. The resolution further identified the value of AMI in achieving significant utility operational cost savings in the areas of outage management, revenue protection and asset management. The resolution also called for AMI business case analysis to identify cost-effective deployment strategies, endorsed timely cost recovery for prudently incurred AMI expenditures and made additional recommendations on rate making and tax treatment of such investments.

### Benefits of advanced metering

Advanced metering systems can provide benefits for utilities, retail providers and customers. Benefits will be recognized by the utilities with increased efficiencies, outage detection, tamper notification and reduced labor cost as a result of automating reads, connections and disconnects. Retail providers will be able to offer new innovative products in addition to customizing packages for their customers. In addition, with the meter data being readily available, more flexible billing cycles would be available to their customers instead of following the standard utility read cycles. With timely usage information available to the customer, benefits will be seen through opportunities to manage their energy consumption and change from one REP to another with actual meter data. Because of these benefits, many utilities are moving towards implementing some types of AMR solutions.

In many cases, smart metering is required by law (e.g. Pennsylvania's Act 129 (2008)).

The benefits of smart metering for the utility.

- Accurate meter reading, no more estimates
- Improved billing
- Accurate profile classes and measurement classes, true costs applied
- Improved security and tamper detection for equipment
- Energy management through profile data graphs
- Less financial burden correcting mistakes
- Less accrued expenditure
- Transparency of "cost to read" metering
- Improved procurement power though more accurate data — "de-risking" price
- In cases of shortages, utility will be able to manage/allocate supply.

The benefits of smart metering for the customer.

- Improved billing and tracking of usage.

### Disadvantages of advanced metering

- Risk of loss of privacy — details of use reveal information about user activities
- Greater potential for monitoring by other/unauthorized third parties
- Potentially reduced reliability (more complicated meters, more potential for interference by third parties)
- Increased security risks from network or remote access

### Notable deployments

Construction practices, weather, and the need for information drive utilities in different parts of the world towards AMR at different rates. In the US, there have been significant fixed network deployments of both RF based and PLC based technologies. Some countries have either deployed or plan to deploy AMR systems throughout the entire country.

#### SPAR

By using a combination of AMR and energy analytics reports, SPAR were able to reduce energy consumption by 20%.

#### Australia

AMI in Australia has grown from both government policy which sought to rectify observed market inefficiencies, and distribution businesses who looked to gain operational efficiencies. In July 2008, there was a mandated program being planned in Victoria for the deployment of 2.6 million meters over a 4-year period. The anticipated peak installation rate of AMI meters was 5,000 per day across Victoria. The program governance was provided by an industry steering committee.

In 2009 the Victorian Auditor General undertook a review of the program and found that there were "significant inadequacies" in advice to Government and that project governance "has not been appropriate". The Victorian government subsequently announced a moratorium of the program

- Public Utility Commission of Texas Report 2006
- Pennsylvania, (Exelon-PECO) 2.2 million meters deployed
- Missouri, (Ameren) 1.7 million meters deployed.

## The future of AMR

With the growing adoption of AMI meters and systems, AMR has been in decline in the U.S. electric utility sector. However, in the gas and water sectors, where it tends to be more expensive and complicated to replace meters, AMR remains prevalent, and some utilities continue to invest in new AMR meter deployments. Going forward, utilities face a choice to replace AMR with AMI—often at great expense and time investment—or to explore an AMx strategy using modern signal collection and processing technology that allows for more frequent wireless data collection from existing AMR meters (in some cases down to every 30 seconds) while offering increased interoperability with other (potentially more advanced) meters in areas where they make offer incremental benefits. Whereas the first approach is likely to continue the gradual decline of AMR, the latter approach could lead to a resurgence of interest in next-generation AMR meters that can unlock near-real-time data at lower cost and with longer useful lives, while also virtually eliminating the need for trucks to drive by for data collection.
