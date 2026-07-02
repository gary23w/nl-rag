---
title: "Radio-frequency identification (part 2/2)"
source: https://en.wikipedia.org/wiki/Radio-frequency_identification
domain: supply-chain-visibility
license: CC-BY-SA-4.0
tags: supply chain visibility, track and trace, radio-frequency identification, bullwhip effect
fetched: 2026-07-02
part: 2/2
---

## Problems and concerns

### RFID tags’ environmental footprint, e‑waste status, and privacy

Large-scale RFID deployment has prompted discussion of the environmental footprint and end-of-life status of RFID tags themselves, since common “label/inlay” tags are micro-electronic devices (a silicon IC connected to an antenna and incorporated into packaging materials) that are often embedded into everyday goods such as apparel and consumer packaging. Industry shipment data highlight the scale: the RAIN Alliance reported 44.8 billion RAIN UHF tag IC shipments in 2023, and (citing a VDC Research forecast commissioned by the RAIN Alliance) reported a projection of 88.5 billion shipments by 2026; a later RAIN/VDC report described a pathway toward 115 billion by 2028 and discussed longer-term trillion-scale opportunities as use cases expand.

Life-cycle studies report that per-tag climate impacts can vary with tag design and system boundaries. Nguyen & Perret (IEEE JRFID, 2024) report tag-level global-warming results comparing a chip-based UHF RFID inlay, a chipless RFID tag, and a barcode label (e.g., UHF RFID 0.336 kg CO2-eq; chipless RFID 0.148 kg CO2-eq; barcode 0.0269 kg CO2-eq; chip incremental ≈0.222 kg CO2-eq from a “tag without chip” scenario), while other LCAs (e.g., Aliakbarian et al., 2024; Zhang et al., 2025) illustrate sensitivity to constructions, assumptions, and end-of-life scenarios.

Under EU law, RoHS 2011/65/EU defines electrical and electronic equipment (EEE) as equipment dependent on electric currents or electromagnetic fields to work properly, while WEEE 2012/19/EU defines waste electrical and electronic equipment (WEEE) as discarded EEE including “all components, sub-assemblies and consumables” present at discarding; Eurostat repeats these definitions for WEEE monitoring. In the United States, e-waste regulation is comparatively fragmented: the EPA notes that 25 states plus the District of Columbia have electronics recycling laws.

End-of-life studies emphasize practical constraints: the EU-funded SMART TRASH study notes that waste processing facilities are generally not designed to separate RFID chips (except possibly in dedicated streams such as WEEE) and highlights contamination concerns; a packaging end-of-life assessment reports that tag particulates can be transferred into recyclate; and one supply-chain LCA states that RFID tags attached to milk cartons typically end up in landfills as electronic waste because consumers discard cartons with tags attached.

Mitigation approaches discussed in the literature include eco-design, take-back/reuse schemes, and substitution with chipless RFID where feasible (tags “not equipped with” an ASIC), though chipless approaches have technical performance trade-offs and infrastructure constraints. If future policy or enforcement interpreted embedded tags as bringing otherwise non-electronic goods within WEEE scope, producer responsibility requirements for collection, reporting and financing of end-of-life treatment could expand, increasing compliance costs and strengthening incentives for reusable tags, removable identifiers, or chipless/printed alternatives.

Separate from environmental issues, RFID has long raised privacy concerns because tags can be read without line-of-sight at distances of meters depending on frequency and tag type, enabling unauthorized reading and potential tracking/profiling; an ACM review highlights covert reading of personal items and the possibility of tracking consumers’ spending patterns and whereabouts, and the European Commission issued a recommendation on implementing privacy and data-protection principles in RFID applications. Research using RFID readers and tag detections has also been used to derive “co-presence” networks (co-location inferred from which readers detect which tags), illustrating how RFID-derived co-location patterns can be analyzed.

### Data flooding

Not every successful reading of a tag (an observation) is useful for business purposes. A large amount of data may be generated that is not useful for managing inventory or other applications. For example, a customer moving a product from one shelf to another, or a pallet load of articles that passes several readers while being moved in a warehouse, are events that do not produce data that are meaningful to an inventory control system.

Event filtering is required to reduce this data inflow to a meaningful depiction of moving goods passing a threshold. Various concepts have been designed, mainly offered as *middleware* performing the filtering from noisy and redundant raw data to significant processed data.

### Global standardization

The frequencies used for UHF RFID in the USA are as of 2007 incompatible with those of Europe or Japan. Furthermore, no emerging standard has yet become as universal as the barcode. To address international trade concerns, it is necessary to use a tag that is operational within all of the international frequency domains.

### Security concerns

A primary RFID security concern is the illicit tracking of RFID tags. Tags, which are world-readable, pose a risk to both personal location privacy and corporate/military security. Such concerns have been raised with respect to the United States Department of Defense's adoption of RFID tags for supply chain management. More generally, privacy organizations have expressed concerns in the context of ongoing efforts to embed electronic product code (EPC) RFID tags in general-use products. This is mostly as a result of the fact that RFID tags can be read, and legitimate transactions with readers can be eavesdropped on, from non-trivial distances. RFID used in access control, payment and eID (e-passport) systems operate at a shorter range than EPC RFID systems but are also vulnerable to skimming and eavesdropping, albeit at shorter distances.

A second method of prevention is by using cryptography. Rolling codes and challenge–response authentication (CRA) are commonly used to foil monitor-repetition of the messages between the tag and reader, as any messages that have been recorded would prove to be unsuccessful on repeat transmission. Rolling codes rely upon the tag's ID being changed after each interrogation, while CRA uses software to ask for a cryptographically coded response from the tag. The protocols used during CRA can be symmetric, or may use public key cryptography.

While a variety of secure protocols have been suggested for RFID tags, in order to support long read range at low cost, many RFID tags have barely enough power available to support very low-power and therefore simple security protocols such as cover-coding.

Unauthorized reading of RFID tags presents a risk to privacy and to business secrecy. Unauthorized readers can potentially use RFID information to identify or track packages, persons, carriers, or the contents of a package. Several prototype systems are being developed to combat unauthorized reading, including RFID signal interruption, as well as the possibility of legislation, and 700 scientific papers have been published on this matter since 2002. There are also concerns that the database structure of Object Naming Service may be susceptible to infiltration, similar to denial-of-service attacks, after the EPCglobal Network ONS root servers were shown to be vulnerable.

### Health

Microchip-induced tumors have been noted during animal trials.

### Shielding

In an effort to prevent the passive "skimming" of RFID-enabled cards or passports, the U.S. General Services Administration (GSA) issued a set of test procedures for evaluating electromagnetically opaque sleeves. For shielding products to be in compliance with FIPS-201 guidelines, they must meet or exceed this published standard; compliant products are listed on the website of the U.S. CIO's FIPS-201 Evaluation Program. The United States government requires that when new ID cards are issued, they must be delivered with an approved shielding sleeve or holder. Although many wallets and passport holders are advertised to protect personal information, there is little evidence that RFID skimming is a serious threat; data encryption and use of EMV chips rather than RFID makes this sort of theft rare.

There are contradictory opinions as to whether aluminum can prevent reading of RFID chips. Some people claim that aluminum shielding, essentially creating a Faraday cage, does work. Others claim that simply wrapping an RFID card in aluminum foil only makes transmission more difficult and is not completely effective at preventing it.

Shielding effectiveness depends on the frequency being used. Low-frequency LowFID tags, like those used in implantable devices for humans and pets, are relatively resistant to shielding, although thick metal foil will prevent most reads. High frequency HighFID tags (13.56 MHz—smart cards and access badges) are sensitive to shielding and are difficult to read when within a few centimetres of a metal surface. UHF Ultra-HighFID tags (pallets and cartons) are difficult to read when placed within a few millimetres of a metal surface, although their read range is actually increased when they are spaced 2–4 cm from a metal surface due to positive reinforcement of the reflected wave and the incident wave at the tag.

### Privacy

The use of RFID has engendered considerable controversy and some consumer privacy advocates have initiated product boycotts. Consumer privacy experts Katherine Albrecht and Liz McIntyre are two prominent critics of the "spychip" technology. The two main privacy concerns regarding RFID are as follows:

- As the owner of an item may not necessarily be aware of the presence of an RFID tag and the tag can be read at a distance without the knowledge of the individual, sensitive data may be acquired without consent.
- If a tagged item is paid for by credit card or in conjunction with use of a loyalty card, then it would be possible to indirectly deduce the identity of the purchaser by reading the globally unique ID of that item contained in the RFID tag. This is a possibility if the person watching also had access to the loyalty card and credit card data, and the person with the equipment knows where the purchaser is going to be.

Most concerns revolve around the fact that RFID tags affixed to products remain functional even after the products have been purchased and taken home; thus, they may be used for surveillance and other purposes unrelated to their supply chain inventory functions.

The RFID Network responded to these fears in the first episode of their syndicated cable TV series, saying that they are unfounded, and let RF engineers demonstrate how RFID works. They provided images of RF engineers driving an RFID-enabled van around a building and trying to take an inventory of items inside. They also discussed satellite tracking of a passive RFID tag.

The concerns raised may be addressed in part by use of the Clipped Tag. The Clipped Tag is an RFID tag designed to increase privacy for the purchaser of an item. The Clipped Tag has been suggested by IBM researchers Paul Moskowitz and Guenter Karjoth. After the point of sale, a person may tear off a portion of the tag. This allows the transformation of a long-range tag into a proximity tag that still may be read, but only at short range – less than a few inches or centimeters. The modification of the tag may be confirmed visually. The tag may still be used later for returns, recalls, or recycling.

However, read range is a function of both the reader and the tag itself. Improvements in technology may increase read ranges for tags. Tags may be read at longer ranges than they are designed for by increasing reader power. The limit on read distance then becomes the signal-to-noise ratio of the signal reflected from the tag back to the reader. Researchers at two security conferences have demonstrated that passive Ultra-HighFID tags normally read at ranges of up to 30 feet can be read at ranges of 50 to 69 feet using suitable equipment.

In January 2004, privacy advocates from CASPIAN and the German privacy group FoeBuD were invited to the METRO Future Store in Germany, where an RFID pilot project was implemented. It was uncovered by accident that METRO "Payback" customer loyalty cards contained RFID tags with customer IDs, a fact that was disclosed neither to customers receiving the cards, nor to this group of privacy advocates. This happened despite assurances by METRO that no customer identification data was tracked and all RFID usage was clearly disclosed.

During the UN World Summit on the Information Society (WSIS) in November 2005, Richard Stallman, the founder of the free software movement, protested the use of RFID security cards by covering his card with aluminum foil.

In 2004–2005, the Federal Trade Commission staff conducted a workshop and review of RFID privacy concerns and issued a report recommending best practices.

RFID was one of the main topics of the 2006 Chaos Communication Congress (organized by the Chaos Computer Club in Berlin) and triggered a large press debate. Topics included electronic passports, Mifare cryptography and the tickets for the FIFA World Cup 2006. Talks showed how the first real-world mass application of RFID at the 2006 FIFA Football World Cup worked. The group monochrom staged a "Hack RFID" song.

### Government control

Some individuals have grown to fear the loss of rights due to RFID human implantation.

By early 2007, Chris Paget of San Francisco, California, showed that RFID information could be pulled from a US passport card by using only $250 worth of equipment. This suggests that with the information captured, it would be possible to clone such cards.

According to ZDNet, critics believe that RFID will lead to tracking individuals' every movement and will be an invasion of privacy. In the book *SpyChips: How Major Corporations and Government Plan to Track Your Every Move* by Katherine Albrecht and Liz McIntyre, one is encouraged to "imagine a world of no privacy. Where your every purchase is monitored and recorded in a database and your every belonging is numbered. Where someone many states away or perhaps in another country has a record of everything you have ever bought. What's more, they can be tracked and monitored remotely".

### Deliberate destruction in clothing and other items

According to an RSA laboratories FAQ, RFID tags can be destroyed by a standard microwave oven; however, some types of RFID tags, particularly those constructed to radiate using large metallic antennas (in particular RF tags and EPC tags), may catch fire if subjected to this process for too long (as would any metallic item inside a microwave oven). This simple method cannot safely be used to deactivate RFID features in electronic devices, or those implanted in living tissue, because of the risk of damage to the "host". However the time required is extremely short (a second or two of radiation) and the method works in many other non-electronic and inanimate items, long before heat or fire become of concern.

Some RFID tags implement a "kill command" mechanism to permanently and irreversibly disable them. This mechanism can be applied if the chip itself is trusted or the mechanism is known by the person that wants to "kill" the tag.

UHF RFID tags that comply with the EPC2 Gen 2 Class 1 standard usually support this mechanism, while protecting the chip from being killed with a password. Guessing or cracking this needed 32-bit password for killing a tag would not be difficult for a determined attacker.
