---
title: "Radio-frequency identification (part 1/2)"
source: https://en.wikipedia.org/wiki/Radio-frequency_identification
domain: web-nfc
license: CC-BY-SA-4.0
tags: web nfc api, near field communication, ndef record message, contactless tag reading
fetched: 2026-07-02
part: 1/2
---

# Radio-frequency identification

**Radio-frequency identification** (**RFID**) uses electromagnetic fields to automatically identify and track tags attached to objects. An RFID system consists of a tiny radio transponder called a tag, a radio receiver, and a transmitter. When triggered by an electromagnetic interrogation pulse from a nearby RFID reader device, the tag transmits digital data, usually an identifying inventory number, back to the reader. This number can be used to track inventory goods.

Passive tags are powered by energy from the RFID reader's interrogating radio waves. Active tags are powered by a battery and thus can be read at a greater range from the RFID reader, up to hundreds of meters.

Unlike a barcode, the tag does not need to be within the line of sight of the reader, so it may be embedded in the tracked object. RFID is one method of automatic identification and data capture (AIDC).

RFID tags are used in many industries. For example, an RFID tag attached to an automobile during production can be used to track its progress through the assembly line, RFID-tagged pharmaceuticals can be tracked through warehouses, and implanting RFID microchips in livestock and pets enables positive identification of animals. Tags can also be used in shops to expedite checkout, and to prevent theft by customers and employees.

Since RFID tags can be attached to physical money, clothing, and possessions, or implanted in animals and people, the possibility of reading personally linked information without consent has raised privacy concerns. These concerns resulted in standard specifications development addressing privacy and security issues.

In 2014, the world RFID market was worth US$8.89 billion, up from US$7.77 billion in 2013 and US$6.96 billion in 2012. This figure includes tags, readers, and software/services for RFID cards, labels, fobs, and all other form factors. The market value is expected to rise from US$12.08 billion in 2020 to US$16.23 billion by 2029.

In 2024, about 50 billion tag chips were sold, according to Atlas RFID and RAIN Alliance webinars in July 2025.


## History

In 1945, Leon Theremin invented the "Thing", a listening device for the Soviet Union which retransmitted incident radio waves with the added audio information. Sound waves vibrated a diaphragm, which slightly altered the shape of the resonator, which modulated the reflected radio frequency. Even though this device was a covert listening device, rather than an identification tag, it is considered to be a predecessor of RFID because it was passive, being energised and activated by waves from an outside source.

Similar technology, such as the Identification friend or foe transponder, was routinely used by the Allies and Germany in World War II to identify aircraft as friendly or hostile. Transponders are still used by most powered aircraft. An early work exploring RFID is the landmark 1948 paper by Harry Stockman, who predicted that "Considerable research and development work has to be done before the remaining basic problems in reflected-power communication are solved, and before the field of useful applications is explored."

Mario Cardullo's device, patented on January 23, 1973, was the first true ancestor of modern RFID, as it was a passive radio transponder with memory. The initial device was passive, powered by the interrogating signal, and was demonstrated in 1971 to the New York Port Authority and other potential users. It consisted of a transponder with 16 bit memory for use as a toll device. The basic Cardullo patent covers the use of radio frequency (RF), sound and light as transmission carriers. The original business plan presented to investors in 1969 showed uses in transportation (automotive vehicle identification, automatic toll system, electronic license plate, electronic manifest, vehicle routing, vehicle performance monitoring), banking (electronic chequebook, electronic credit card), security (personnel identification, automatic gates, surveillance) and medical (identification, patient history).

In 1973, an early demonstration of *reflected power* (modulated backscatter) RFID tags, both passive and semi-passive, was performed by Steven Depp, Alfred Koelle and Robert Freyman at the Los Alamos National Laboratory. The portable system operated at 915 MHz and used 12-bit tags. This technique is used by the majority of today's UHFID and microwave RFID tags.

In 1983, the first patent to be associated with the abbreviation RFID was granted to Charles Walton.

In 1996, the first patent for a batteryless RFID passive tag with limited interference was granted to David Everett, John Frech, Theodore Wright, and Kelly Rodriguez.


## Design

A radio-frequency identification system uses *tags*, or *labels* attached to the objects to be identified. Two-way radio transmitter-receivers called *interrogators* or *readers* send a signal to the tag and read its response.

### Tags

RFID tags are made out of three pieces:

- a micro chip (an integrated circuit which stores and processes information and modulates and demodulates radio-frequency (RF) signals)
- an antenna for receiving and transmitting the signal
- a substrate

The tag information is stored in non-volatile memory. The RFID tags includes either fixed or programmable logic for processing the transmission and sensor data, respectively.

RFID tags can be either passive, active or battery-assisted passive. An active tag has an on-board battery and periodically transmits its ID signal. A battery-assisted passive tag has a small battery on board and is activated when in the presence of an RFID reader. A passive tag is cheaper and smaller because it has no battery; instead, the tag uses the radio energy transmitted by the reader. However, to operate a passive tag, it must be illuminated with a power level roughly a thousand times stronger than an active tag for signal transmission.

Tags may either be read-only, having a factory-assigned serial number that is used as a key into a database, or may be read/write, where object-specific data can be written into the tag by the system user. Field programmable tags may be write-once, read-multiple; blank tags may be written with an electronic product code by the user.

The RFID tag receives the message and then responds with its identification and other information. This may be only a unique tag serial number, or may be product-related information such as a stock number, lot or batch number, production date, or other specific information. Since tags have individual serial numbers, the RFID system design can discriminate among several tags that might be within the range of the RFID reader and read them simultaneously.

### Readers

RFID systems can be classified by the type of tag and reader. There are 3 types:

- A **passive reader active tag** (**PRAT**) system has a passive reader which only receives radio signals from active tags (battery-operated, transmit only). The reception range of a PRAT system reader can be adjusted from 1–2,000 feet (0–600 m), allowing flexibility in applications such as asset protection and supervision.
- An **active reader passive tag** (**ARPT**) system has an active reader, which transmits interrogator signals and also receives authentication replies from passive tags.
- An **active reader active tag** (**ARAT**) system uses active tags activated with an interrogator signal from the active reader. A variation of this system could also use a battery-assisted passive (BAP) tag, which acts like a passive tag but has a small battery to power the tag's return reporting signal.

Fixed readers are set up to create a specific interrogation zone which can be tightly controlled. This allows a highly defined reading area for when tags go in and out of the interrogation zone. Mobile readers may be handheld or mounted on carts or vehicles.

### Frequencies

| Band | Regulations | Range | Data speed | ISO/IEC 18000 section | Remarks | Approximate tag cost in volume (2006) |
|---|---|---|---|---|---|---|
| LF: 120–150 kHz | Unregulated | 10 cm (4 in) | Low | Part 2 | Animal identification, factory data collection | US$1 |
| HF: 13.56 MHz | ISM band worldwide | 0.1–1 m (4 in – 3 ft 3 in) | Low to moderate | Part 3 | Smart cards (ISO/IEC 15693, ISO/IEC 14443 A, B), ISO-non-compliant smart cards (iCLASS, Legic, FeliCa ...), ISO-compatible smart cards (MIFARE, Seos) | US$0.05 to US$5 |
| UHF: 433 MHz | Short range devices | 1–100 m (3–300 ft) | Moderate | Part 7 | Defense applications, Underground Miner Tracking with active tags | US$5 |
| UHF: 865–868 MHz (Europe) 902–928 MHz (North America) | ISM band | 1–12 m (3–40 ft) | Moderate to high | Part 6 | EAN, various standards; used by railroads | US$0.04 to US$1.00 (passive tags) |
| microwave: 2450–5800 MHz | ISM band | 1–2 m (3–7 ft) | High | Part 4 | 802.11 WLAN, Bluetooth standards | US$25 (active tags) |
| microwave: 3.1–10 GHz | Ultra wide band | up to 200 m (700 ft) | High | Not defined | Requires semi-active or active tags | US$5 projected |
| mm-wave: 24.125 GHz | ISM band worldwide | 10–200 m (30–700 ft) | High | Not defined | Requires semi-passive tags. Uses retrodirective backscatter approaches to achieve extended ranges | US$10 projected |

### Signaling

Signaling between the reader and the tag is done in several different incompatible ways, depending on the frequency band used by the tag. Tags operating on LF and HF bands are, in terms of radio wavelength, very close to the reader antenna because they are only a small percentage of a wavelength away. In this near field region, the tag is closely coupled electrically with the transmitter in the reader. The tag can modulate the field produced by the reader by changing the electrical loading the tag represents. By switching between lower and higher relative loads, the tag produces a change that the reader can detect. At UHF and higher frequencies, the tag is more than one radio wavelength away from the reader, requiring a different approach. The tag can backscatter a signal. Active tags may contain functionally separated transmitters and receivers, and the tag need not respond on a frequency related to the reader's interrogation signal.

An Electronic Product Code (EPC) is one common type of data stored in a tag. When written into the tag by an RFID printer, the tag contains a 96-bit string of data. The first eight bits are a header which identifies the version of the protocol. The next 28 bits identify the organization that manages the data for this tag; the organization number is assigned by the EPCGlobal consortium. The next 24 bits are an object class, identifying the kind of product. The last 36 bits are a unique serial number for a particular tag. These last two fields are set by the organization that issued the tag. Rather like a URL, the total electronic product code number can be used as a key into a global database to uniquely identify a particular product.

Often more than one tag will respond to a tag reader. For example, many individual products with tags may be shipped in a common box or on a common pallet. Collision detection is important to allow reading of data in these situations. Two different types of protocols are used to singulate a particular tag, allowing its data to be read in the midst of many similar tags: In a Slotted Aloha system, the reader broadcasts an initialization command and a parameter that the tags individually use to pseudo-randomly delay their responses. When using an **adaptive binary tree** protocol, the reader sends an initialization symbol and then transmits one bit of ID data at a time; only tags with matching bits respond, and eventually only one tag matches the complete ID string. Both methods have drawbacks when used with many tags or with multiple overlapping readers.

### Bulk reading

**Bulk reading** is a strategy for interrogating multiple tags at the same time, but lacks sufficient precision for inventory control. A group of objects, all of them RFID tagged, are read completely from one single reader position at one time. However, as tags respond strictly sequentially, the time needed for bulk reading grows linearly with the number of labels to be read. This means it takes at least twice as long to read twice as many labels. Due to collision effects, the time required is greater.

A group of tags has to be illuminated by the interrogating signal just like a single tag. This is not a challenge concerning energy, but with respect to visibility; if any of the tags are shielded by other tags, they might not be sufficiently illuminated to return a sufficient response. The response conditions for inductively coupled HF RFID tags and coil antennas in magnetic fields appear better than for UHF or SHF dipole fields, but then distance limits apply and may prevent success.

Under operational conditions, bulk reading is not reliable. Bulk reading can be a rough guide for logistics decisions, but due to a high proportion of reading failures, it is not currently suitable for inventory management. However, when a single RFID tag might be seen as not guaranteeing a proper read, multiple RFID tags, where at least one will respond, may be a safer approach for detecting a known grouping of objects. In this respect, bulk reading is a fuzzy method for process support. From the perspective of cost and effect, bulk reading is not reported as an economical approach to secure process control in logistics.

### Miniaturization

RFID tags are easy to conceal or incorporate in other items. For example, in 2009, researchers at Bristol University successfully glued RFID micro-transponders to live ants in order to study their behavior. This trend towards increasingly miniaturized RFIDs is likely to continue as technology advances.

Hitachi holds the record for the smallest RFID chip, at 0.05 mm × 0.05 mm. This is 1/64th the size of the previous record holder, the mu-chip. Manufacture is enabled by using the silicon-on-insulator (SOI) process. These dust-sized chips can store 38-digit numbers using 128-bit Read Only Memory (ROM). A major challenge is the attachment of antennas, thus limiting read range to only millimeters.

#### TFID (Terahertz Frequency Identification)

In early 2020, MIT researchers demonstrated a terahertz frequency identification (TFID) tag that is barely 1 square millimeter in size. The devices are essentially a piece of silicon that are inexpensive, small, and function like larger RFID tags. Because of the small size, manufacturers could tag any product and track logistics information for minimal cost.


## Uses

An RFID tag can be affixed to an object and used to track tools, equipment, inventory, assets, people, or other objects.

RFID offers advantages over manual systems or use of barcodes. The tag can be read if passed near a reader, even if it is covered by the object or not visible. The tag can be read inside a case, carton, box or other container, and unlike barcodes, RFID tags can be read hundreds at a time; barcodes can only be read one at a time using current devices. Some RFID tags, such as battery-assisted passive tags, are also able to monitor temperature and humidity.

In 2011, the cost of passive tags started at US$0.09 each; special tags, meant to be mounted on metal or withstand gamma sterilization, could cost up to US$5. Active tags for tracking containers, medical assets, or monitoring environmental conditions in data centers started at US$50 and could be over US$100 each. Battery-Assisted Passive (BAP) tags were in the US$3–10 range.

RFID can be used in a variety of applications, such as:

- Access management
- Tracking of goods
- Tracking of persons and animals
- Toll collection and contactless payment
- Machine readable travel documents
- Smartdust (for massively distributed sensor networks)
- Locating lost airport baggage
- Timing sporting events
- Tracking and billing processes
- Monitoring the physical state of perishable goods

In 2010, three factors drove a significant increase in RFID usage: decreased cost of equipment and tags, increased performance to a reliability of 99.9%, and a stable international standard around HF and UHF passive RFID. The adoption of these standards were driven by EPCglobal, a joint venture between GS1 and GS1 US, which were responsible for driving global adoption of the barcode in the 1970s and 1980s. The EPCglobal Network was developed by the Auto-ID Center.

### Commerce

RFID provides a way for organizations to identify and manage stock, tools and equipment (asset tracking), etc. without manual data entry. Manufactured products such as automobiles or garments can be tracked through the factory and through shipping to the customer. Automatic identification with RFID can be used for inventory systems. Many organisations require that their vendors place RFID tags on all shipments to improve supply chain management. Warehouse Management System incorporate this technology to speed up the receiving and delivery of the products and reduce the cost of labor needed in their warehouses.

#### Retail

RFID is used for item-level tagging in retail stores. This can enable more accurate and lower-labor-cost supply chain and store inventory tracking, as is done at Lululemon, though physically locating items in stores requires more expensive technology. RFID tags can be used at checkout; for example, at some stores of the French retailer Decathlon, customers perform self-checkout by either using a smartphone or putting items into a bin near the register that scans the tags without having to orient each one toward the scanner. Some stores use RFID-tagged items to trigger systems that provide customers with more information or suggestions, such as fitting rooms at Chanel and the "Color Bar" at Kendra Scott stores.

Item tagging can also provide protection against theft by customers and employees by using electronic article surveillance (EAS). Tags of different types can be physically removed with a special tool or deactivated electronically when payment is made. On leaving the shop, customers have to pass near an RFID detector; if they have items with active RFID tags, an alarm sounds, indicating an unpaid-for item.

Casinos can use RFID to authenticate poker chips, and can selectively invalidate any chips known to be stolen.

#### Access control

RFID tags are widely used in identification badges, replacing earlier magnetic stripe cards. These badges need only be held within a certain distance of the reader to authenticate the holder. Tags can also be placed on vehicles, which can be read at a distance, to allow entrance to controlled areas without having to stop the vehicle and present a card or enter an access code.

#### Advertising

In 2010, Vail Resorts began using UHF Passive RFID tags in ski passes.

Automotive brands have adopted RFID for social media product placement more quickly than other industries. Mercedes was an early adopter in 2011 at the PGA Golf Championships, and a Hyundai stand in the 2013 Geneva Motor Show uses RFID for streamlining social activation marketing.

#### Promotion tracking

To prevent retailers diverting products, manufacturers are exploring the use of RFID tags on promoted merchandise so that they can track exactly which product has sold through the supply chain at fully discounted prices.

### Transportation and logistics

Yard management, shipping and freight and distribution centers use RFID tracking. In the railroad industry, RFID tags mounted on locomotives and rolling stock identify the owner, identification number and type of equipment and its characteristics. This can be used with a database to identify the type, origin, destination, etc. of the commodities being carried.

In commercial aviation, RFID is used to support maintenance on commercial aircraft. A standard for RFID baggage tags has been established by the IATA at the Passenger Services Conference in Geneva of November 2005. The Las Vegas McCarran International Airport and Hong Kong International Airport were among several airports to have tests conducted, concurring the presence of functional RFID baggage tags.

Some countries are using RFID for vehicle registration and enforcement. RFID can help detect and retrieve stolen cars.

RFID is used in intelligent transportation systems. In New York City, RFID readers are deployed at intersections to track E-ZPass tags as a means for monitoring the traffic flow. The data is fed through the broadband wireless infrastructure to the traffic management center to be used in adaptive traffic control of the traffic lights.

Where ship, rail, or highway tanks are being loaded, a fixed RFID antenna contained in a transfer hose can read an RFID tag affixed to the tank, positively identifying it.

### Infrastructure management and protection

At least one company has introduced RFID to identify and locate underground infrastructure assets such as gas pipelines, sewer lines, electrical cables, communication cables, etc.

### Passports

The first RFID passports ("E-passport") were issued by Malaysia in 1998. In addition to information also contained on the visual data page of the passport, Malaysian e-passports record the travel history (time, date, and place) of entry into and exit out of the country.

Other countries that insert RFID in passports include Norway (2005), Japan (March 1, 2006), most EU countries (around 2006), Singapore (2006), Australia, Hong Kong, the United States (2007), the United Kingdom and Northern Ireland (2006), India (June 2008), Serbia (July 2008), Republic of Korea (August 2008), Taiwan (December 2008), Albania (January 2009), The Philippines (August 2009), Republic of Macedonia (2010), Argentina (2012), Canada (2013), Uruguay (2015) and Israel (2017).

Standards for RFID passports are determined by the International Civil Aviation Organization (ICAO), and are contained in ICAO Document 9303, Part 1, Volumes 1 and 2 (6th edition, 2006). ICAO refers to the ISO/IEC 14443 RFID chips in e-passports as "contactless integrated circuits". ICAO standards provide for e-passports to be identifiable by a standard e-passport logo on the front cover.

Since 2006, RFID tags included in new United States passports store the same information that is printed within the passport, and include a digital picture of the owner. The United States Department of State initially stated the chips could only be read from a distance of 10 centimetres (3.9 in), but after widespread criticism and a clear demonstration that special equipment can read the test passports from 10 metres (33 ft) away, the passports were designed to incorporate a thin metal lining to make it more difficult for unauthorized readers to skim information when the passport is closed. The department will also implement Basic Access Control (BAC), which functions as a personal identification number (PIN) in the form of characters printed on the passport data page. Before a passport's tag can be read, this PIN must be entered into an RFID reader. The BAC also enables the encryption of any communication between the chip and interrogator.

### Transportation payments

In many countries, RFID tags can be used to pay for mass transit fares on bus, trains, or subways, or to collect tolls on highways.

Some bike lockers are operated with RFID cards assigned to individual users. A prepaid card is required to open or enter a facility or locker and is used to track and charge based on how long the bike is parked.

The Zipcar car-sharing service uses RFID cards for locking and unlocking cars and for member identification.

In Singapore, RFID replaces paper Season Parking Ticket (SPT).

### Animal identification

RFID tags for animals represent one of the earliest uses of RFID. Originally meant for large ranches and rough terrain, since the outbreak of mad-cow disease, RFID has become crucial in animal identification management. An implantable RFID tag or transponder can also be used for animal identification. The transponders are better known as Passive Integrated Transponder (PIT) tags, passive RFID, or **chips** on animals. The Canadian Cattle Identification Agency began using RFID tags as a replacement for barcode tags. Currently, CCIA tags are used in Wisconsin and by United States farmers on a voluntary basis. The USDA is currently developing its own program.

RFID tags are required for all cattle sold in Australia and in some states, sheep and goats as well.

### Human implantation

Biocompatible microchip implants that use RFID technology are being routinely implanted in humans. The first-ever human to receive an RFID microchip implant was American artist Eduardo Kac in 1997. Kac implanted the microchip live on television (and also live on the Internet) in the context of his artwork *Time Capsule*. A year later, British professor of cybernetics Kevin Warwick had an RFID chip implanted in his arm by his general practitioner, George Boulos. In 2004, the 'Baja Beach Club' operated by Conrad Chase in Barcelona and Rotterdam offered implanted chips to identify their VIP customers, who could in turn use it to pay for service. In 2009, British scientist Mark Gasson had an advanced glass capsule RFID device surgically implanted into his left hand and subsequently demonstrated how a computer virus could wirelessly infect his implant and then be transmitted on to other systems.

The Food and Drug Administration in the United States approved the use of RFID chips in humans in 2004.

There is controversy regarding human applications of implantable RFID technology including concerns that individuals could potentially be tracked by carrying an identifier unique to them. Privacy advocates have protested against implantable RFID chips, warning of potential abuse. Some are concerned this could lead to abuse by an authoritarian government, to removal of freedoms, and to the emergence of an "ultimate panopticon", a society where all citizens behave in a socially accepted manner because others might be watching.

On July 22, 2006, Reuters reported that two hackers, Newitz and Westhues, at a conference in New York City demonstrated that they could clone the RFID signal from a human implanted RFID chip, indicating that the device was not as secure as was previously claimed.

The UFO religion Universe People is notorious online for their vocal opposition to human RFID chipping, which they claim is a saurian attempt to enslave the human race; one of their web domains is "dont-get-chipped".

### Institutions

#### Hospitals and healthcare

Adoption of RFID in the medical industry has been widespread and very effective. Hospitals are among the first users to combine both active and passive RFID. Active tags track high-value, or frequently moved items, and passive tags track smaller, lower cost items that only need room-level identification. Medical facility rooms can collect data from transmissions of RFID badges worn by patients and employees, as well as from tags assigned to items such as mobile medical devices. The U.S. Department of Veterans Affairs (VA) recently announced plans to deploy RFID in hospitals across America to improve care and reduce costs.

Since 2004, a number of U.S. hospitals have begun implanting patients with RFID tags and using RFID systems; the systems are typically used for workflow and inventory management. The use of RFID to prevent mix-ups between sperm and ova in IVF clinics is also being considered.

In October 2004, the FDA approved the USA's first RFID chips that can be implanted in humans. The 134 kHz RFID chips, from VeriChip Corp. can incorporate personal medical information and could save lives and limit injuries from errors in medical treatments, according to the company. Anti-RFID activists Katherine Albrecht and Liz McIntyre discovered an FDA Warning Letter that spelled out health risks. According to the FDA, these include "adverse tissue reaction", "migration of the implanted transponder", "failure of implanted transponder", "electrical hazards" and "magnetic resonance imaging [MRI] incompatibility."

#### Libraries

Libraries have used RFID to replace the barcodes on library items. The tag can contain identifying information or may just be a key into a database. An RFID system may replace or supplement bar codes and may offer another method of inventory management and self-service checkout by patrons. It can also act as a security device, taking the place of the more traditional electromagnetic security strip.

It is estimated that over 30 million library items worldwide now contain RFID tags, including some in the Vatican Library in Rome.

Since RFID tags can be read through an item, there is no need to open a book cover or DVD case to scan an item, and a stack of books can be read simultaneously. Book tags can be read while books are in motion on a conveyor belt, which reduces staff time. This can all be done by the borrowers themselves, reducing the need for library staff assistance. With portable readers, inventories could be done on a whole shelf of materials within seconds. However, as of 2008, this technology remained too costly for many smaller libraries, and the conversion period has been estimated at 11 months for an average-size library. A 2004 Dutch estimate was that a library which lends 100,000 books per year should plan on a cost of €50,000 (borrow- and return-stations: 12,500 each, detection porches 10,000 each; tags 0.36 each). RFID taking a large burden off staff could also mean that fewer staff will be needed, resulting in some of them getting laid off, but that has so far not happened in North America where recent surveys have not returned a single library that cut staff because of adding RFID. In fact, library budgets are being reduced for personnel and increased for infrastructure, making it necessary for libraries to add automation to compensate for the reduced staff size. Also, the tasks that RFID takes over are largely not the primary tasks of librarians. A finding in the Netherlands is that borrowers are pleased with the fact that staff are now more available for answering questions.

Privacy concerns have been raised surrounding library use of RFID. Because some RFID tags can be read up to 100 metres (330 ft) away, there is some concern over whether sensitive information could be collected from an unwilling source. However, library RFID tags do not contain any patron information, and the tags used in the majority of libraries use a frequency only readable from approximately 10 feet (3.0 m). Another concern is that a non-library agency could potentially record the RFID tags of every person leaving the library without the library administrator's knowledge or consent. One simple option is to let the book transmit a code that has meaning only in conjunction with the library's database. Another possible enhancement would be to give each book a new code every time it is returned. In future, should readers become ubiquitous (and possibly networked), then stolen books could be traced even outside the library. Tag removal could be made difficult if the tags are so small that they fit invisibly inside a (random) page, possibly put there by the publisher.

#### Museums

RFID technologies are now also implemented in end-user applications in museums. An example was the custom-designed temporary research application, "eXspot", at the Exploratorium, a science museum in San Francisco, California. A visitor entering the museum received an RF tag that could be carried as a card. The eXspot system enabled the visitor to receive information about specific exhibits. Aside from the exhibit information, the visitor could take photographs of themselves at the exhibit. It was also intended to allow the visitor to take data for later analysis. The collected information could be retrieved at home from a "personalized" website keyed to the RFID tag.

#### Schools and universities

In 2004, school authorities in the Japanese city of Osaka made a decision to start chipping children's clothing, backpacks, and student IDs in a primary school. Later, in 2007, a school in Doncaster, England, piloted a monitoring system designed to keep tabs on pupils by tracking radio chips in their uniforms. St Charles Sixth Form College in west London, England, starting in 2008, uses an RFID card system to check in and out of the main gate, to both track attendance and prevent unauthorized entrance. Similarly, Whitcliffe Mount School in Cleckheaton, England, uses RFID to track pupils and staff in and out of the building via a specially designed card. In the Philippines, during 2012, some schools already use RFID in IDs for borrowing books. Gates in those particular schools also have RFID scanners for buying items at school shops and canteens. RFID is also used in school libraries, and to sign in and out for student and teacher attendance.

### Sports

RFID for timing races began in the early 1990s with pigeon racing, introduced by the company Deister Electronics in Germany. RFID can provide race start and end timings for individuals in large races where it is impossible to get accurate stopwatch readings for every entrant.

In races using RFID, racers wear tags that are read by antennas placed alongside the track or on mats across the track. UHF tags provide accurate readings with specially designed antennas. Rush error, lap count errors and accidents at race start are avoided, as anyone can start and finish at any time without being in a batch mode.

The design of the chip and of the antenna controls the range from which it can be read. Short range compact chips are twist tied to the shoe, or strapped to the ankle with hook-and-loop fasteners. The chips must be about 400 mm from the mat, therefore giving very good temporal resolution. Alternatively, a chip plus a very large (125 mm square) antenna can be incorporated into the bib number worn on the athlete's chest at a height of about 1.25 m (4.1 ft).

Passive and active RFID systems are used in off-road events such as Orienteering, Enduro and Hare and Hounds racing. Riders have a transponder on their person, normally on their arm. When they complete a lap they swipe or touch the receiver which is connected to a computer and log their lap time.

RFID is being adapted by many recruitment agencies which have a PET (physical endurance test) as their qualifying procedure, especially in cases where the candidate volumes may run into millions (Indian Railway recruitment cells, police and power sector).

A number of ski resorts have adopted RFID tags to provide skiers hands-free access to ski lifts. Skiers do not have to take their passes out of their pockets. Ski jackets have a left pocket into which the chip+card fits. This nearly contacts the sensor unit on the left of the turnstile as the skier pushes through to the lift. These systems were based on high frequency (HF) at 13.56 MHz. The bulk of ski areas in Europe, from Verbier to Chamonix, use these systems.

The NFL in the United States equips players with RFID chips that measures speed, distance and direction traveled by each player in real-time. Currently, cameras stay focused on the quarterback; however, numerous plays are happening simultaneously on the field. The RFID chip will provide new insight into these simultaneous plays. The chip triangulates the player's position within six inches and will be used to digitally broadcast replays. The RFID chip will make individual player information accessible to the public. The data will be available via the NFL 2015 app. The RFID chips are manufactured by Zebra Technologies. Zebra Technologies tested the RFID chip in 18 stadiums last year to track vector data.

### Complement to barcode

RFID tags are not necessarily "superior" to barcodes. RFID tags are often a complement, but not a substitute, for Universal Product Code (UPC) or European Article Number (EAN) barcodes. They may never completely replace barcodes, due in part to their higher cost and the advantage of multiple data sources on the same object. Also, unlike RFID labels, barcodes can be generated and distributed electronically by e-mail or mobile phone, for printing or display by the recipient. An example is airline boarding passes. The new EPC, along with several other schemes, is widely available at reasonable cost.

The storage of data associated with tracking items will require many terabytes. Filtering and categorizing RFID data is needed to create useful information. It is likely that goods will be tracked by the pallet using RFID tags, and at package level with UPC or EAN from unique barcodes.

The unique identity is a mandatory requirement for RFID tags, despite special choice of the numbering scheme. RFID tag data capacity is large enough that each individual tag will have a unique code, while current barcodes are limited to a single type code for a particular product. The uniqueness of RFID tags means that a product may be tracked as it moves from location to location while being delivered to a person. This may help to combat theft and other forms of product loss. The tracing of products is an important feature that is well supported with RFID tags containing a unique identity of the tag and the serial number of the object. This may help companies cope with quality deficiencies and resulting recall campaigns, but also contributes to concern about tracking and profiling of persons after the sale.

### Waste management

Since around 2007, there has been increasing development in the use of RFID in the waste management industry. RFID tags are installed on waste collection carts, linking carts to the owner's account for easy billing and service verification. The tag is embedded into a garbage and recycle container, and the RFID reader is affixed to the garbage and recycle trucks. RFID also measures a customer's set-out rate and provides insight as to the number of carts serviced by each waste collection vehicle. This RFID process replaces traditional "pay as you throw" (PAYT) municipal solid waste usage-pricing models.

### Telemetry

Active RFID tags have the potential to function as low-cost remote sensors that broadcast telemetry back to a base station. Applications of tagometry data could include sensing of road conditions by implanted beacons, weather reports, and noise level monitoring.

Passive RFID tags can also report sensor data. For example, the Wireless Identification and Sensing Platform is a passive tag that reports temperature, acceleration and capacitance to commercial Gen2 RFID readers.

It is possible that active or battery-assisted passive (BAP) RFID tags could broadcast a signal to an in-store receiver to determine whether the RFID tag – and by extension, the product it is attached to – is in the store.


## Regulation and standardization

To avoid injuries to humans and animals, RF transmission needs to be controlled. A number of organizations have set standards for RFID, including the International Organization for Standardization (ISO), the International Electrotechnical Commission (IEC), ASTM International, the DASH7 Alliance and EPCglobal.

Several specific industries have also set guidelines, including the Financial Services Technology Consortium (FSTC) for tracking IT Assets with RFID, the Computer Technology Industry Association CompTIA for certifying RFID engineers, and the International Air Transport Association (IATA) for luggage in airports.

Every country can set its own rules for frequency allocation for RFID tags, and not all radio bands are available in all countries. These frequencies are known as the ISM bands (Industrial Scientific and Medical bands). The return signal of the tag may still cause interference for other radio users.

- Low-frequency (LF: 125–134.2 kHz and 140–148.5 kHz) (LowFID) tags and high-frequency (HF: 13.56 MHz) (HighFID) tags can be used globally without a license.
- Ultra-high-frequency (UHF: 865–928 MHz) (Ultra-HighFID or UHFID) tags cannot be used globally as there is no single global standard, and regulations differ from country to country.

In North America, UHF can be used unlicensed for 902–928 MHz (±13 MHz from the 915 MHz center frequency), but restrictions exist for transmission power. In Europe, RFID and other low-power radio applications are regulated by ETSI recommendations EN 300 220 and EN 302 208, and ERO recommendation 70 03, allowing RFID operation with somewhat complex band restrictions from 865–868 MHz. Readers are required to monitor a channel before transmitting ("Listen Before Talk"); this requirement has led to some restrictions on performance, the resolution of which is a subject of current research. The North American UHF standard is not accepted in France as it interferes with its military bands. On July 25, 2012, Japan changed its UHF band to 920 MHz, more closely matching the United States' 915 MHz band, establishing an international standard environment for RFID.

In some countries, a site license is needed, which needs to be applied for at the local authorities, and can be revoked.

As of 31 October 2014, regulations are in place in 78 countries representing approximately 96.5% of the world's GDP, and work on regulations was in progress in three countries representing approximately 1% of the world's GDP.

Standards that have been made regarding RFID include:

- ISO 11784/11785 – Animal identification. Uses 134.2 kHz.
- ISO 14223 – Radiofrequency identification of animals – Advanced transponders
- ISO/IEC 14443: This standard is a popular HF (13.56 MHz) standard for HighFIDs which is being used as the basis of RFID-enabled passports under ICAO 9303. The Near Field Communication standard that lets mobile devices act as RFID readers/transponders is also based on ISO/IEC 14443.
- ISO/IEC 15693: This is also a popular HF (13.56 MHz) standard for HighFIDs widely used for non-contact smart payment and credit cards.
- ISO/IEC 18000: Information technology—Radio frequency identification for item management:
- ISO/IEC 18092 Information technology—Telecommunications and information exchange between systems—Near Field Communication—Interface and Protocol (NFCIP-1)
- ISO 18185: This is the industry standard for electronic seals or "e-seals" for tracking cargo containers using the 433 MHz and 2.4 GHz frequencies.
- ISO/IEC 21481 Information technology—Telecommunications and information exchange between systems—Near Field Communication Interface and Protocol −2 (NFCIP-2)
- ASTM D7434, Standard Test Method for Determining the Performance of Passive Radio Frequency Identification (RFID) Transponders on Palletized or Unitized Loads
- ASTM D7435, Standard Test Method for Determining the Performance of Passive Radio Frequency Identification (RFID) Transponders on Loaded Containers
- ASTM D7580, Standard Test Method for Rotary Stretch Wrapper Method for Determining the Readability of Passive RFID Transponders on Homogenous Palletized or Unitized Loads
- ISO 28560-2— specifies encoding standards and data model to be used within libraries.

In order to ensure global interoperability of products, several organizations have set up additional standards for RFID testing. These standards include conformance, performance and interoperability tests.

### EPC Gen2

EPC Gen2 is short for *EPCglobal UHF Class 1 Generation 2*.

EPCglobal, a joint venture between GS1 and GS1 US, is working on international standards for the use of mostly passive RFID and the Electronic Product Code (EPC) in the identification of many items in the supply chain for companies worldwide.

One of the missions of EPCglobal was to simplify the Babel of protocols prevalent in the RFID world in the 1990s. Two tag air interfaces (the protocol for exchanging information between a tag and a reader) were defined (but not ratified) by EPCglobal prior to 2003. These protocols, commonly known as Class 0 and Class 1, saw significant commercial implementation in 2002–2005.

In 2004, the Hardware Action Group created a new protocol, the Class 1 Generation 2 interface, which addressed a number of problems that had been experienced with Class 0 and Class 1 tags. The EPC Gen2 standard was approved in December 2004. This was approved after a contention from Intermec that the standard may infringe a number of their RFID-related patents. It was decided that the standard itself does not infringe their patents, making the standard royalty free. The EPC Gen2 standard was adopted with minor modifications as ISO 18000-6C in 2006.

The updated Class 1 Generation 2 version 3.0 standard was ratified in January 2024. The new standard includes a longer power-up period (2500 microseconds instead of 1500), and the option to reduce power slightly during a command, in order to reduce the chances of partial responses from tags at the edge of the read zone. New commands QueryX and QueryY, combining Select and Query, have been added, in addition to various other minor changes and additions.

In 2007, the lowest cost of Gen2 EPC inlay was offered by the now-defunct company SmartCode, at a price of $0.05 apiece in volumes of 100 million or more.
