---
title: "Near-field communication"
source: https://en.wikipedia.org/wiki/Near-field_communication
domain: web-nfc
license: CC-BY-SA-4.0
tags: web nfc api, near field communication, ndef record message, contactless tag reading
fetched: 2026-07-02
---

# Near-field communication

**Near-field communication** (**NFC**) is a set of communication protocols that enables communication between two electronic devices over a distance of 4 cm (1+1⁄2 in) or less. NFC offers a low-speed connection through a simple setup that can be used for the bootstrapping of capable wireless connections. Like other proximity card technologies, NFC is based on inductive coupling between two electromagnetic coils present on an NFC-enabled device such as a smartphone. NFC communicating in one or both directions uses a frequency of 13.56 MHz in the globally available unlicensed radio-frequency ISM band, compliant with the ISO/IEC 18000-3 air-interface standard at data rates ranging from 106 to 848 kbit/s.

The NFC Forum has helped define and promote the technology, setting standards for certifying device compliance. Secure communications are available by applying encryption algorithms, as is done for credit cards, and if they fit the criteria for being considered a personal area network.

## NFC standards

NFC standards cover communications protocols and data exchange formats and are based on existing radio-frequency identification (RFID) standards including ISO/IEC 14443 and FeliCa. The standards include ISO/IEC 18092 and those defined by the NFC Forum. In addition to the NFC Forum, the GSMA group defined a platform for the deployment of GSMA NFC Standards within mobile handsets. GSMA's efforts include Trusted Services Manager, Single Wire Protocol, testing/certification and secure element. NFC-enabled portable devices can be provided with application software, for example to read electronic tags or make payments when connected to an NFC-compliant system. These are standardized to NFC protocols, replacing proprietary technologies used by earlier systems.

A patent licensing program for NFC is under deployment by France Brevets, a patent fund created in 2011. This program was under development by Via Licensing Corporation, an independent subsidiary of Dolby Laboratories, and was terminated in May 2012. A platform-independent free and open source NFC library, libnfc, is available under the GNU Lesser General Public License.

Present and anticipated applications include contactless transactions, data exchange and simplified setup of more complex communications such as Wi-Fi. In addition, when one of the connected devices has Internet connectivity, the other can exchange data with online services.

### NFC wireless charging (WLC)

Near-field communication (NFC) technology not only supports data transmission but also enables wireless charging, providing a dual functionality that is particularly beneficial for small portable devices. The NFC Forum has developed a specific wireless charging specification, known as NFC Wireless Charging (WLC), which allows devices to charge with up to 1 W of power over distances of up to 2 cm (3⁄4 in). This capability is especially suitable for smaller devices like earbuds, wearables, and other compact Internet of Things (IoT) appliances.

Compared to the more widely known Qi wireless charging standard by the Wireless Power Consortium, which offers up to 15 W of power over distances up to 4 cm (1+5⁄8 in), NFC WLC provides a lower power output but benefits from a significantly smaller antenna size (as small as 3 × 3 mm). This makes NFC WLC an ideal solution for devices where space is at a premium and high-power charging is less critical.

The NFC Forum also facilitates a certification program, labeled as Test Release 13.1 (TR13.1), ensuring that products adhere to the WLC 2.0 specification. This certification aims to establish trust and consistency across NFC implementations, minimizing risks for manufacturers and providing assurance to consumers about the reliability and functionality of their NFC-enabled wireless charging devices.

## History

NFC technology is rooted in radio-frequency identification technology (known as RFID) which allows compatible hardware to both supply power to and communicate with an otherwise unpowered and passive electronic tag using radio waves. This is used for identification, authentication and tracking. Similar ideas in advertising and industrial applications were not generally successful commercially, outpaced by technologies such as QR codes, barcodes and UHF RFID tags.

The first patent to be associated with the abbreviation "RFID" was granted to Charles Walton on May 17, 1983. In 1997, an early form was patented and first used in *Star Wars* character toys for Hasbro. The patent was originally held by Andrew White and Marc Borrett at Innovision Research and Technology. The device allowed data communication between two units in close proximity.

On March 25, 2002, Philips and Sony agreed to establish a technology specification and created a technical outline. Philips Semiconductors applied for the six fundamental patents of NFC, invented by the Austrian and French engineers Franz Amtmann and Philippe Maugars who received the European Inventor Award in 2015. NFC was approved as an ISO/IEC standard on December 8, 2003, and later as an ECMA standard.

In 2004, Nokia, Philips and Sony established the NFC Forum. That same year, Nokia launched NFC shell add-on for Nokia 5140 and later Nokia 3220 models, to be shipped in 2005. The year 2005 saw mobile phone experimentations in transports, with payment in May in Hanau (Nokia) and validation aboard in October in Nice with Orange and payment in shops in October in Caen (Samsung) with first reception of "Fly Tag" informations.

Initial specifications for NFC Tags were released in 2006, along with specifications for "SmartPoster" records. In 2007, Innovision's NFC tags were used in the first consumer trial in the UK, in the Nokia 6131 handset. AirTag launched what it called the first NFC SDK in 2008.

In January 2009, the NFC Forum released Peer-to-Peer standards to transfer contacts, URLs, initiate Bluetooth, etc. NFC was first used in transports by China Unicom and Yucheng Transportation Card in the tramways and bus of Chongqing on January 19, 2009, then implemented for the first time in a metro network, by China Unicom in Beijing on December 31, 2010.

In 2010, Innovision released a suite of designs and patents for low cost, mass-market mobile phones and other devices. The Nokia C7, the first NFC-capable smartphone, was released in 2010, with the NFC feature enabled by software update in early 2011. The Samsung Nexus S, the first Android NFC phone, was shown in 2010. On May 21, 2010, Nice, France, launched, with "Cityzi", the "Nice City of contactless mobile" project, the first in Europe to provide inhabitants with NFC bank cards and mobile phones (like Samsung Player One S5230), and a "bouquet of services" covering transportation (tramways and bus), tourism and student's services.

In 2011, independent development of lightweight NFC stacks addressed the resource constraints of early mobile secure elements (Java Card). Engineers such as Dan Hughes (who later applied these concepts to the Radix distributed ledger) worked on custom implementations to enable peer-to-peer payments on limited-memory devices prior to the standardization of host card emulation. Google I/O "How to NFC" demonstrated NFC to initiate a game and to share a contact, URL, app or video in 2011. NFC support became part of the Symbian mobile operating system with the release of Symbian Anna version in 2011. In 2012, UK restaurant chain EAT. and Everything Everywhere (Orange Mobile Network Operator), partnered on the UK's first nationwide NFC-enabled smartposter campaign. A dedicated mobile phone app is triggered when the NFC-enabled mobile phone comes into contact with the smartposter. Sony introduced NFC "Smart Tags" to change modes and profiles on a Sony smartphone at close range in 2012, included with the Sony Xperia P Smartphone released the same year. Samsung and VISA announced their partnership to develop mobile payments in 2013. In 2013, IBM scientists, in an effort to curb fraud and security breaches, developed an NFC-based mobile authentication security technology. This technology works on similar principles to dual-factor authentication security.

In October 2014, Dinube became the first non-card payment network to introduce NFC contactless payments natively on a mobile device, i.e. no need for an external case attached or NFC 'sticker' nor for a card. Based on Host card emulation with its own *application identifier* (AID), contactless payment was available on Android KitKat upwards and commercial release commenced in June 2015. In 2014, AT&T, Verizon and T-Mobile released Softcard (formerly ISIS mobile wallet). It runs on NFC-enabled Android phones and iPhone 4 and iPhone 5 when an external NFC case is attached. The technology was purchased by Google and the service ended on March 31, 2015. On October 20, 2014, Apple Pay was launched in the United States. At launch, the contactless payment service was supported exclusively on the iPhone 6 and 6 Plus which featured the Apple's first embedded NFC hardware configuration.

In September 2015, Google's Android Pay function was launched, a direct rival to Apple Pay, and its roll-out across the US commenced. In November 2015, Swatch and Visa Inc. announced a partnership to enable NFC financial transactions using the "Swatch Bellamy" wristwatch. The system is currently online in Asia, through a partnership with China UnionPay and Bank of Communications. The partnership will bring the technology to the US, Brazil, and Switzerland.

Ultra-wideband (UWB) another radio technology has been hailed as a future possible alternatives to NFC technology due to further distances of data transmission, as well as Bluetooth and wireless technology.

## Design

NFC is a set of short-range wireless technologies, typically requiring a separation of 10 cm (3+7⁄8 in) or less. NFC operates at 13.56 MHz on ISO/IEC 18000-3 air interface and at rates ranging from 106 kbit/s to 424 kbit/s. NFC always involves an initiator and a target; the initiator actively generates an RF field that can power a passive target. This enables NFC targets to take very simple form factors such as unpowered tags, stickers, key fobs, or cards. NFC peer-to-peer communication is possible, provided both devices are powered.

NFC tags contain data and are typically read-only, but may be writable. They can be custom-encoded by their manufacturers or use NFC Forum specifications. The tags can securely store personal data such as debit and credit card information, loyalty program data, PINs and networking contacts, among other information. The NFC Forum defines five types of tags that provide different communication speeds and capabilities in terms of configurability, memory, security, data retention and write endurance.

As with proximity card technology, NFC uses inductive coupling between two nearby loop antennas effectively forming an air-core transformer. Because the distances involved are tiny compared to the wavelength of electromagnetic radiation (radio waves) of that frequency (about 22 metres), the interaction is described as near field. An alternating magnetic field is the main coupling factor and almost no power is radiated in the form of radio waves (which are electromagnetic waves, also involving an oscillating electric field); that minimises interference between such devices and any radio communications at the same frequency or with other NFC devices much beyond its intended range. NFC operates within the globally available and unlicensed radio frequency ISM band of 13.56 MHz. Most of the RF energy is concentrated in the ±7 kHz bandwidth allocated for that band, but the emission's spectral width can be as wide as 1.8 MHz in order to support high data rates.

Working distance with compact standard antennas and realistic power levels could be up to about 20 cm (7+7⁄8 in) (but practically speaking, working distances never exceed 10 cm or 3+7⁄8 in). Note that because the pickup antenna may be quenched in an eddy current by nearby metallic surfaces, the tags may require a minimum separation from such surfaces.

The ISO/IEC 18092 standard supports data rates of 106, 212 or 424 kbit/s.

The communication takes place between an active "initiator" device and a target device which may either be:

**Passive**

The initiator device provides a carrier field and the target device, acting as a

transponder

, communicates by modulating the incident field. In this mode, the target device may draw its operating power from the initiator-provided magnetic field.

**Active**

Both initiator and target device communicate by alternately generating their own fields. A device stops transmitting in order to receive data from the other. This mode requires that both devices include power supplies.

| Speed (kbit/s) | Active device | Passive device |
|---|---|---|
| 424 | Manchester, 10% ASK | Manchester, 10% ASK |
| 212 | Manchester, 10% ASK | Manchester, 10% ASK |
| 106 | Modified Miller, 100% ASK | Manchester, 10% ASK |

NFC employs two different codings to transfer data. If an active device transfers data at 106 kbit/s, a modified Miller coding with 100 percent modulation is used. In all other cases Manchester coding is used with a modulation ratio of 10 percent.

Every active NFC device can work in one or more of three modes:

**NFC card emulation**

Enables NFC-enabled devices such as smartphones to act like smart cards, allowing users to perform transactions such as payment or ticketing. See

Host card emulation

**NFC reader/writer**

Enables NFC-enabled devices to read information stored on inexpensive NFC tags embedded in labels or smart posters.

**NFC peer-to-peer**

Enables two NFC-enabled devices to communicate with each other to exchange information in an

ad hoc

fashion.

NFC tags are passive data stores which can be read, and under some circumstances written to, by an NFC device. They typically contain data (as of 2015 between 96 and 8,192 bytes) and are read-only in normal use, but may be rewritable. Applications include secure personal data storage (e.g. debit or credit card information, loyalty program data, personal identification numbers (PINs), contacts). NFC tags can be custom-encoded by their manufacturers or use the industry specifications.

## Security

Although the range of NFC is limited to a few centimeters, standard plain NFC is not protected against eavesdropping and can be vulnerable to data modifications. Applications may use higher-layer cryptographic protocols to establish a secure channel.

The RF signal for the wireless data transfer can be picked up with antennas. The distance from which an attacker is able to eavesdrop the RF signal depends on multiple parameters, but is typically less than 10 meters. Also, eavesdropping is highly affected by the communication mode. A passive device that doesn't generate its own RF field is much harder to eavesdrop on than an active device. An attacker can typically eavesdrop within 10 m of an active device and 1 m for passive devices.

Because NFC devices usually include ISO/IEC 14443 protocols, relay attacks are feasible. For this attack the adversary forwards the request of the reader to the victim and relays its answer to the reader in real time, pretending to be the owner of the victim's smart card. This is similar to a man-in-the-middle attack. One libnfc code example demonstrates a relay attack using two stock commercial NFC devices. This attack can be implemented using only two NFC-enabled mobile phones.

## Standards

NFC standards cover communications protocols and data exchange formats, and are based on existing RFID standards including ISO/IEC 14443 and FeliCa. The standards include ISO/IEC 18092 and those defined by the NFC Forum.

### ISO/IEC

NFC is standardized in ECMA-340 and ISO/IEC 18092. These standards specify the modulation schemes, coding, transfer speeds and frame format of the RF interface of NFC devices, as well as initialization schemes and conditions required for data collision-control during initialization for both passive and active NFC modes. They also define the transport protocol, including protocol activation and data-exchange methods. The air interface for NFC is standardized in:

- ISO/IEC 18092 / ECMA-340—*Near Field Communication Interface and Protocol-1* (NFCIP-1)
- ISO/IEC 21481 / ECMA-352—*Near Field Communication Interface and Protocol-2* (NFCIP-2)

NFC incorporates a variety of existing standards including ISO/IEC 14443 Type A and Type B, and FeliCa (also simply named F or NFC-F). NFC-enabled phones work at a basic level with existing readers. In "card emulation mode" an NFC device should transmit, at a minimum, a unique ID number to a reader. In addition, NFC Forum defined a common data format called *NFC Data Exchange Format* (NDEF) that can store and transport items ranging from any MIME-typed object to ultra-short RTD-documents, such as URLs. The NFC Forum added the *Simple NDEF Exchange Protocol* (SNEP) to the spec that allows sending and receiving messages between two NFC devices.

### GSMA

The GSM Association (GSMA) is a trade association representing nearly 800 mobile telephony operators and more than 200 product and service companies across 219 countries. Many of its members have led NFC trials and are preparing services for commercial launch.

GSM is involved with several initiatives:

- Standards: GSMA is developing certification and testing standards to ensure global interoperability of NFC services.
- *Pay-Buy-Mobile initiative*: Seeks to define a common global approach to using NFC technology to link mobile devices with payment and contactless systems.
- On November 17, 2010, after two years of discussions, AT&T, Verizon and T-Mobile launched a joint venture to develop a platform through which point of sale payments could be made using NFC in cell phones. Initially known as Isis Mobile Wallet and later as Softcard, the venture was designed to usher in broad deployment of NFC technology, allowing their customers' NFC-enabled cell phones to function similarly to credit cards throughout the US. Following an agreement with—and IP purchase by—Google, the Softcard payment system was shuttered in March, 2015, with an endorsement for its earlier rival, Google Wallet.

### StoLPaN

StoLPaN (Store Logistics and Payment with NFC) is a pan-European consortium supported by the European Commission's Information Society Technologies program. StoLPaN will examine the potential for NFC local wireless mobile communication.

### NFC Forum

NFC Forum is a non-profit industry association formed on March 18, 2004, by NXP Semiconductors, Sony and Nokia to advance the use of NFC wireless interaction in consumer electronics, mobile devices and PCs. Its specifications include the five distinct tag types that provide different communication speeds and capabilities covering flexibility, memory, security, data retention and write endurance. NFC Forum promotes implementation and standardization of NFC technology to ensure interoperability between devices and services. As of January 2020, the NFC Forum had over 120 member companies.

NFC Forum promotes NFC and certifies device compliance and whether it fits in a personal area network.

### Other standardization bodies

GSMA defined a platform for the deployment of GSMA NFC Standards within mobile handsets. GSMA's efforts include, Single Wire Protocol, testing and certification and secure element. The GSMA standards surrounding the deployment of NFC protocols (governed by NFC Forum) on mobile handsets are neither exclusive nor universally accepted. For example, Google's deployment of Host Card Emulation on Android KitKat provides for software control of a universal radio. In this HCE Deployment the NFC protocol is leveraged without the GSMA standards.

Other standardization bodies involved in NFC include:

- ETSI / SCP (Smart Card Platform) to specify the interface between the SIM card and the NFC chipset.
- EMVCo for the impacts on the EMV payment applications

## Applications

NFC allows one- and two-way communication between endpoints, suitable for many applications.

NFC devices can act as electronic identity documents and keycards. They are used in contactless payment systems and allow mobile payment replacing or supplementing systems such as credit cards and electronic ticket smart cards. These are sometimes called *NFC/CTLS* or *CTLS NFC*, with *contactless* abbreviated as *CTLS*. NFC can be used to share small files such as contacts and for bootstrapping fast connections to share larger media such as photos, videos, and other files.

### Commerce

NFC devices can be used in contactless payment systems, similar to those used in credit cards and electronic ticket smart cards, and allow mobile payment to replace/supplement these systems.

In Android 4.4, Google introduced platform support for secure NFC-based transactions through Host Card Emulation (HCE), for payments, loyalty programs, card access, transit passes and other custom services. HCE allows any Android 4.4 app to emulate an NFC smart card, letting users initiate transactions with their device. Apps can use a new Reader Mode to act as readers for HCE cards and other NFC-based transactions.

On September 9, 2014, Apple announced support for NFC-powered transactions as part of Apple Pay. With the introduction of iOS 11, Apple devices allow third-party developers to read data from NFC tags.

As of 2022, there are five major NFC apps available in the UK: Apple Pay, Google Pay, Samsung Pay, Barclays Contactless Mobile and Fitbit Pay. The UK Finance's UK Payment Markets Summary 2021 looked at Apple Pay, Google Pay and Samsung Pay and found 17.3 million UK adults had registered for mobile payment (up 75% from the year before) and of those, 84% had made a mobile payment.

### Bootstrapping other connections

NFC offers a low-speed connection with simple setup that can be used to bootstrap more capable wireless connections. For example, Android Beam software uses NFC to enable pairing and establish a Bluetooth connection when doing a file transfer and then disabling Bluetooth on both devices upon completion. Nokia, Samsung, BlackBerry and Sony have used NFC technology to pair Bluetooth headsets, media players and speakers with one tap. The same principle can be applied to the configuration of Wi-Fi networks. Samsung Galaxy devices have a feature named S-Beam—an extension of Android Beam that uses NFC (to share MAC address and IP addresses) and then uses Wi-Fi Direct to share files and documents. The advantage of using Wi-Fi Direct over Bluetooth is that it permits much faster data transfers, running up to 300 Mbit/s.

NFC can be used for social networking, for sharing contacts, text messages and forums, links to photos, videos or files and entering multiplayer mobile games.

### Identity and access tokens

NFC-enabled devices can act as electronic identity documents found in passports and ID cards, and keycards for the use in fare cards, transit passes, login cards, car keys and access badges . NFC's short range and encryption support make it more suitable than less private RFID systems.

### Smartphone automation and NFC tags

NFC-equipped smartphones can be paired with NFC Tags or stickers that can be programmed by NFC apps. These programs can allow a change of phone settings, texting, app launching, or command execution.

Such apps do not rely on a company or manufacturer, but can be utilized immediately with an NFC-equipped smartphone and an NFC tag.

The NFC Forum published the Signature Record Type Definition (RTD) 2.0 in 2015 to add integrity and authenticity for NFC Tags. This specification allows an NFC device to verify tag data and identify the tag author.

### Gaming

NFC has been used in video games starting with *Skylanders: Spyro's Adventure*. After connecting the included "Portal of Power" (a toy pedestal that contains an NFC reader) to their game system, players can summon any of the game's 32 unique playable characters ("Skylanders") by physically placing a figurine of their desired Skylander atop the "Portal", which reads the NFC tag embedded within the figurine, and loads the corresponding character into play. Each collectible figurine contains personal data, so no two are exactly alike. Nintendo's Wii U was the first console system to include NFC technology out of the box- the Wii U GamePad controller was NFC-enabled. This made it compatible with Nintendo's Amiibo range of accessories. Like Skylanders, Amiibo figurines contain NFC tags, and can unlock relevant in-game content when placed on a supported NFC reader, though what particular Amiibo are supported (if any), and what affect each one has, can vary from game to game. NFC technology was later included in the Nintendo 3DS range (being built into the New Nintendo 3DS/XL and in a separately sold reader which uses Infrared to communicate to older 3DS family consoles) and the Nintendo Switch range (being built within the right Joy-Con controller and directly in the Nintendo Switch Lite), all of which remain compatible with Amiibo.

### Sports

Adidas Telstar 18 is a soccer ball that contains an NFC chip within. The chip enables users to interact with the ball using a smartphone.

## Bluetooth comparison

| Aspect | NFC | Bluetooth | Bluetooth low energy |
|---|---|---|---|
| Tag requires power | No | Yes |   |
| Cost of tag | US$0.10 | US$5.00 |   |
| RFID compatible | ISO/IEC 18000-3 | Active |   |
| Standardisation body | ISO/IEC | Bluetooth SIG |   |
| Network standard | ISO/IEC 13157 etc. | was IEEE 802.15.1; now by SIG specs |   |
| Topology | Point-to-point | Wireless personal area network (WPAN) |   |
| Cryptography | Not with RFID | Available |   |
| Range | < 20 cm (7+7⁄8 in) | ≈ 100 m (class 1) | ≈ 50 m |
| Frequency | 13.56 MHz | 2.4–2.5 GHz |   |
| Bit rate | 424 kbit/s | 2.1 Mbit/s | 1 Mbit/s |
| Set-up time | < 0.1 s | < 6 s | < 0.006 s |
| Current consumption | < 15 mA (read) | Varies with class | < 15 mA (read and transmit) |

NFC and Bluetooth are both relatively short-range communication technologies available on mobile phones. NFC operates at slower speeds than Bluetooth and has a much shorter range, but consumes far less power and doesn't require pairing.

NFC sets up more quickly than standard Bluetooth, but has a lower transfer rate than Bluetooth low energy. With NFC, instead of performing manual configurations to identify devices, the connection between two NFC devices is automatically established in less than 0.1 second. The maximum data transfer rate of NFC (424 kbit/s) is slower than that of Bluetooth V2.1 (2.1 Mbit/s).

NFC's maximum working distance of less than 20 cm (7+7⁄8 in) reduces the likelihood of unwanted interception, making it particularly suitable for crowded areas that complicate correlating a signal with its transmitting physical device (and by extension, its user).

NFC is compatible with existing passive RFID (13.56 MHz ISO/IEC 18000-3) infrastructures. It requires comparatively low power, similar to the Bluetooth V4.0 low-energy protocol. However, when NFC works with an unpowered device (e.g. on a phone that may be turned off, a contactless smart credit card, a smart poster), the NFC power consumption is greater than that of Bluetooth V4.0 Low Energy, since illuminating the passive tag needs extra power.

## Devices

In 2011, handset vendors released more than 40 NFC-enabled handsets with the Android mobile operating system. BlackBerry devices support NFC using BlackBerry Tag on devices running BlackBerry OS 7.0 and greater.

MasterCard added further NFC support for PayPass for the Android and BlackBerry platforms, enabling PayPass users to make payments using their Android or BlackBerry smartphones. A partnership between Samsung and Visa added a 'payWave' application on the Galaxy S4 smartphone.

In 2012, Microsoft added native NFC functionality in their mobile OS with Windows Phone 8, as well as the Windows 8 operating system. Microsoft provides the "Wallet hub" in Windows Phone 8 for NFC payment, and can integrate multiple NFC payment services within a single application.

In 2014, iPhone 6 was released from Apple to support NFC. and since September 2019 in iOS 13 Apple now allows NFC tags to be read out as well as labeled using an NFC app.

## Deployments

As of April 2011 hundreds of NFC trials had been conducted. Some firms moved to full-scale service deployments, spanning one or more countries. Multi-country deployments include Orange's rollout of NFC technology to banks, retailers, transport, and service providers in multiple European countries, and Airtel Africa and Oberthur Technologies deploying to 15 countries throughout Africa.

- China Telecom (China's 3rd largest mobile operator) made its NFC rollout in November 2013. The company signed up multiple banks to make their payment apps available on its SIM Cards. China telecom stated that the wallet would support coupons, membership cards, fuel cards and boarding passes. The company planned to achieve targets of rolling out 40 NFC phone models and 30 Mn NFC SIMs by 2014.
- Softcard (formerly Isis Mobile Wallet), a joint venture from Verizon Wireless, AT&T and T-Mobile, focuses on in-store payments making use of NFC technology. After doing pilots in some regions, they launched across the US.
- Vodafone launched the NFC-based Vodafone SmartPass mobile payment service in Spain in partnership with Visa. It enables consumers with an NFC-enabled SIM card in a mobile device to make contactless payments via their SmartPass credit balance at any POS.
- OTI, an Israeli company that designs and develops contactless microprocessor-based smart card technology, contracted to supply NFC-readers to one of its channel partners in the US. The partner was required to buy $10MM worth of OTI NFC readers over 3 years.
- Rogers Communications launched virtual wallet Suretap to enable users to make payments with their phone in Canada in April 2014. Suretap users can load up gift cards and prepaid MasterCards from national retailers.
- Sri Lanka's first workforce smart card uses NFC.
- As of December 13, 2013 Tim Hortons TimmyME BlackBerry 10 Application allowed users to link their prepaid Tim Card to the app, allowing payment by tapping the NFC-enabled device to a standard contactless terminal.
- Google Wallet allows consumers to store credit card and store loyalty card information in a virtual wallet and then use an NFC-enabled device at terminals that also accept MasterCard PayPass transactions.
- Germany, Austria, Finland, New Zealand, Italy, Iran, Turkey and Greece trialed NFC ticketing systems for public transport. The Lithuanian capital of Vilnius fully replaced paper tickets for public transportation with ISO/IEC 14443 Type A cards on July 1, 2013.
- NFC sticker-based payments in Australia's Bankmecu and card issuer Cuscal completed an NFC payment sticker trial, enabling consumers to make contactless payments at Visa payWave terminals using a smart sticker stuck to their phone.
- India was implementing NFC-based transactions in box offices for ticketing purposes.
- A partnership of Google and Equity Bank in Kenya introduced NFC payment systems for public transport in the Capital city Nairobi under the branding BebaPay.
- January 2019 saw the start of trial using NFC-enabled Android mobile phones to pay public transport fares in Victoria, Australia.
