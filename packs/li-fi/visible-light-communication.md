---
title: "Visible light communication"
source: https://en.wikipedia.org/wiki/Visible_light_communication
domain: li-fi
license: CC-BY-SA-4.0
tags: li-fi optical, visible light communication, free-space optics, photonic data transfer
fetched: 2026-07-02
---

# Visible light communication

In telecommunications, **visible light communication** (**VLC**) is the use of visible light (light with a frequency of 400–800 THz, wavelength of 780–375 nm) as a transmission medium. VLC is a subset of optical wireless communications technologies.

The technology uses fluorescent lamps (ordinary lamps, not special communications devices) to transmit signals at 10 kbit/s, or LEDs for up to 500 Mbit/s over short distances. Systems such as RONJA can transmit at full Ethernet speed (10 Mbit/s) over distances of 1–2 kilometres (0.6–1.2 mi).

Specially designed electronic devices generally containing a photodiode receive signals from light sources, although in some cases a cell phone camera or a digital camera will be sufficient. The image sensor used in these devices is in fact an array of photodiodes (pixels), and in some applications its use may be preferred over a single photodiode. Such a sensor may provide either multi-channel (down to 1 pixel = 1 channel) or a spatial awareness of multiple light sources.

VLC can be used as a communications medium for ubiquitous computing, because light-producing devices (such as indoor/outdoor lamps, TVs, traffic signs, commercial displays and car headlights/taillights) are used everywhere.

## Uses

One of the main characteristics of VLC is the incapacity of light to surpass physical opaque barriers. This characteristic can be considered a weak point of VLC, due to the susceptibility of interference from physical objects, but is also one of its many strengths: unlike radio waves, light waves are confined in the enclosed spaces they are transmitted, which enforces a physical safety barrier that requires a receptor of that signal to have physical access to the place where the transmission is occurring.

A promising application of VLC is the Indoor Positioning System (IPS), an analogue to GPS which is built to operate in enclosed spaces where GPS satellite transmissions cannot reach. For instance, commercial buildings, shopping malls, parking garages, as well as subways and tunnel systems are all possible applications for VLC-based indoor positioning systems. Additionally, once the VLC lamps are able to perform lighting at the same time as data transmission, it can simply occupy the installation of traditional single-function lamps.

Other applications for VLC involve communication between appliances of a smart home or office. With increasing IoT-capable devices, connectivity through traditional radio waves might be subjected to interference. Light bulbs with VLC capabilities can transmit data and commands for such devices.

## History

The history of visible light communications dates back to the 1880s in Washington, D.C., when the Scottish-born scientist Alexander Graham Bell invented the photophone, which transmitted speech on modulated sunlight over several hundred meters. This pre-dates the transmission of speech by radio.

More recent work began in 2003 at Nakagawa Laboratory, in Keio University, Japan, using LEDs to transmit data by visible light. Since then there have been numerous research activities focussed on VLC.

In 2006, researchers from CICTR at Penn State proposed a combination of power line communication (PLC) and white light LED to provide broadband access for indoor applications. This research suggested that VLC could be deployed as a perfect last-mile solution in the future.

In January 2010 a team of researchers from Siemens and Fraunhofer Institute for Telecommunications, Heinrich Hertz Institute, in Berlin, demonstrated transmission at 500 Mbit/s with a white LED over a distance of 5 metres (16 ft), and 100 Mbit/s over longer distance using five LEDs.

The VLC standardization process is conducted within the IEEE 802.15.7 working group.

In December 2010 St. Cloud, Minnesota, signed a contract with LVX [1] Minnesota and became the first to commercially deploy this technology.

In July 2011 a presentation at TED Global gave a live demonstration of high-definition video being transmitted from a standard LED lamp, and proposed the term Li-Fi to refer to a subset of VLC technology.

Recently, VLC-based indoor positioning systems have become an attractive topic. ABI research forecasts that it could be a key solution to unlocking the $5 billion "indoor location market". Publications have been coming from Nakagawa Laboratory, ByteLight filed a patent on a light positioning system using LED digital pulse recognition in March 2012. COWA at Penn State and other researchers around the world.

Another recent application is in the world of toys, thanks to cost-efficient and low-complexity implementation, which only requires one microcontroller and one LED as optical front-end.

VLCs can be used for providing security. They are especially useful in body sensor networks and personal area networks.

Recently Organic LEDs (OLED) have been used as optical transceivers to build up VLC communication links up to 10 Mbit/s.

In October 2014, Axrtek launched a commercial bidirectional RGB LED VLC system called MOMO that transmits down and up at speeds of 300 Mbit/s and with a range of 25 feet.

In May 2015, Philips collaborated with supermarket company Carrefour to deliver VLC location-based services to shoppers' smartphones in a hypermarket in Lille, France. In June 2015, two Chinese companies, Kuang-Chi and Ping An Bank, partnered to introduce a payment card that communicates information through a unique visible light. In March 2017, Philips set up the first VLC location-based services to shoppers' smartphones in Germany. The installation was presented at EuroShop in Düsseldorf (5–9 March). As first supermarket in Germany an Edeka supermarket in Düsseldorf-Bilk is using the system, which offers a 30 centimeter positioning accuracy can be achieved, which meets the special demands in food retail. Indoor positioning systems based on VLC can be used in places such as hospitals, eldercare homes, warehouses, and large, open offices to locate people and control indoor robotic vehicles.

There is wireless network that for data transmission uses visible light, and does not use intensity modulation of optical sources. The idea is to use vibration generator instead of optical sources for data transmission.

## Modulation techniques

In order to send data, a modulation of light is required. A modulation is the form in which the light signal varies in order to represent different symbols. In order for the data to be decoded. Unlike radio transmission, a VLC modulation requires the light signal to be modulated around a positive dc value, responsible for the lighting aspect of the lamp. The modulation will thus be an alternating signal around the positive dc level, with a high-enough frequency to be imperceptible to the human eye.

Due to this superposition of signals, implementation of VLC transmitter usually require a high-efficiency, higher-power, slower response DC converter responsible for the LED bias that will provide lighting, alongside a lower-efficiency, lower-power, but higher response velocity amplifier in order to synthesize the required AC current modulation.

There are several modulation techniques available, forming three main groups: single-carrier modulated transmission (SCMT), multi-carrier modulated transmission (MCMT) and pulse-based transmission (PBT).

### Single-carrier modulated transmission

The single-carrier modulated transmission comprises modulation techniques established for traditional forms of transmission, such as radio. A sinusoidal wave is added to the lighting DC level, allowing digital information to be coded in the characteristics of the wave. By keying between two or several different values of a given characteristic, symbols attributed to each value are transmitted on the light link.

Possible techniques are amplitude-shift keying (ASK), phase-shift keying (PSK) and frequency-shift keying (FSK). Out of these three, FSK is capable of larger bitrate transmission once it allows more symbols to be easily differentiated on frequency switching. An additional technique called quadrature amplitude modulation (QAM) has also been proposed, where both amplitude and phase of the sinusoidal voltage are keyed simultaneously in order to increase the possible number of symbols.

### Multi-carrier modulated transmission

Multi-carrier modulated transmission works on the same way of single-carrier modulated transmission methods, but embed two or more sinusoidal waves modulated for data transmission. This type of modulation is among the hardest and more complex to synthesize and decode. However, it presents the advantage of excelling in multipath transmission, where the receptor is not in direct view of the transmitter and therefore makes the transmission depend on reflection of the light in other barriers.

### Pulse-based transmission

Pulse-based transmission encompasses modulation techniques in which the data is encoded not on a sinusoidal wave, but on a pulsed wave. Unlike sinusoidal alternating signals, in which the periodic average will always be null, pulsed waves based on high–low states will present inherit average values. This brings two main advantages for the pulse-based transmission modulations:

- It can be implemented with a single high-power, high-efficiency, DC converter of slow response and an additional power switch operating in fast speeds to deliver current to the LED at determined instants.
- Once the average value depends on the pulse width of the data signal, the same switch that operates the data transmission can provide dimming control, greatly simplifying the DC converter.

Due to these important implementation advantages, these dimming-capable modulations have been standardized in IEEE 802.15.7, in which are described three modulation techniques: on–off keying (OOK), variable pulse position modulation (VPPM) and color-shift keying (CSK).

#### On–off keying

On the on–off keying technique, the LED is switched on and off repeatedly, and the symbols are differentiated by the pulse width, with a wider pulse representing the logical high "1", while narrower pulses representing logical low "0". Because the data is encoded on the pulse width, the information sent will affect the dimming level if not corrected: for instance, a bitstream with several high values "1" will appear brighter than a bitstream with several low values "0". In order to avoid this problem, the modulation requires a compensation pulse that will be inserted on the data period whenever necessary to equalize the brightness overall. The lack of this compensation symbol could introduce perceived flickering, which is undesirable.

Because of the additional compensation pulse, modulating this wave is slightly more complex than modulating the VPPM. However, the information encoded on the pulse width is easy to differentiate and decode, so the complexity of the transmitter is balanced by the simplicity of the receiver.

#### Variable pulse position modulation

Variable pulse position also switches the LED on and off repeatedly, but encode the symbols on the pulse position inside the data period. Whenever the pulse is located at the immediate beginning of the data period, the transmitted symbol is standardized as logical low "0", with logical high "1" being composed of pulses that end with the data period. Because the information is encoded at the location of the pulse inside the data period, both pulses can and will have the same width, and thus, no compensation symbol is required. Dimming is performed by the transmitting algorithm, that will select the width of the data pulses accordingly.

The lack of a compensation pulse makes VPPM marginally simpler to encode when compared to OOK. However, a slightly more complex demodulation compensates for that simplicity on the VPPM technique. This decoding complexity mostly comes from the information being encoded at different rising edges for each symbol, which makes the sampling harder in a microcontroller. Additionally, in order to decode the location of a pulse within the data period, the receptor must be somehow synchronized with the transmitter, knowing exactly when a data period starts and how long it lasts. These characteristics makes the demodulation of a VPPM signal slightly more difficult to implement.

#### Color-shift keying

Color-shift keying (CSK), outlined in IEEE 802.15.7, is an intensity modulation based modulation scheme for VLC. CSK is intensity-based, as the modulated signal takes on an instantaneous color equal to the physical sum of three (red/green/blue) LED instantaneous intensities. This modulated signal jumps instantaneously, from symbol to symbol, across different visible colors; hence, CSK can be construed as a form of frequency shifting. However, this instantaneous variation in the transmitted color is not to be humanly perceptible, because of the limited temporal sensitivity in the human vision – the "critical flicker fusion threshold" (CFF) and the "critical color fusion threshold" (CCF), both of which cannot resolve temporal changes shorter than 0.01 second. The LEDs’ transmissions are, therefore, preset to time-average (over the CFF and the CCF) to a specific time-constant color. Humans can thus perceive only this preset color that seems constant over time, but cannot perceive the instantaneous color that varies rapidly in time. In other words, CSK transmission maintains a constant time-averaged luminous flux, even as its symbol sequence varies rapidly in chromaticity.
