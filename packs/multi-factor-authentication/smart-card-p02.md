---
title: "Smart card (part 2/2)"
source: https://en.wikipedia.org/wiki/Smart_card
domain: multi-factor-authentication
license: CC-BY-SA-4.0
tags: multi factor authentication, time based one time password, hmac based one time password, hardware security token, smart card authentication
fetched: 2026-07-02
part: 2/2
---

## Applications

### Financial

Smart cards serve as credit or ATM cards, fuel cards, mobile phone SIMs, authorization cards for pay television, household utility pre-payment cards, high-security identification and access badges, and public transport and public phone payment cards.

Smart cards may also be used as electronic wallets. The smart card chip can be "loaded" with funds to pay parking meters, vending machines or merchants. Cryptographic protocols protect the exchange of money between the smart card and the machine. No connection to a bank is needed. The holder of the card may use it even if not the owner. Examples are Mondex (1993), Proton, Geldkarte, Chipknip and Moneo. The German Geldkarte is also used to validate customer age at vending machines for cigarettes.

These are the best known payment cards (classic plastic card):

- Visa: Visa Contactless, Quick VSDC, "qVSDC", Visa Wave, MSD, payWave
- Mastercard: PayPass Magstripe, PayPass MChip
- American Express: ExpressPay
- Discover: Zip
- Unionpay: QuickPass

Roll-outs started in 2005 in the U.S. Asia and Europe followed in 2006. Contactless (non-PIN) transactions cover a payment range of ~$5–50. There is an ISO/IEC 14443 PayPass implementation. Some, but not all, PayPass implementations conform to EMV.

Non-EMV cards work like magnetic stripe cards. This is common in the U.S. (PayPass Magstripe and Visa MSD). The cards do not hold or maintain the account balance. All payment passes without a PIN, usually in off-line mode. The security of such a transaction is no greater than with a magnetic stripe card transaction.

EMV cards can have either contact or contactless interfaces. They work as if they were a normal EMV card with a contact interface. Via the contactless interface they work somewhat differently, in that the card commands enabled improved features such as lower power and shorter transaction times. EMV standards include provisions for contact and contactless communications. Typically modern payment cards are based on hybrid card technology and support both contact and contactless communication modes.

### SIM

The subscriber identity modules used in mobile-phone systems are reduced-size smart cards, using otherwise identical technologies.

### Identification

Smart-cards can authenticate identity. Sometimes they employ a public key infrastructure (PKI). The card stores an encrypted digital certificate issued from the PKI provider along with other relevant information. Examples include the U.S. Department of Defense (DoD) Common Access Card (CAC), and other cards used by other governments for their citizens. If they include biometric identification data, cards can provide superior two- or three-factor authentication.

Smart cards are not always privacy-enhancing, because the subject may carry incriminating information on the card. Contactless smart cards that can be read from within a wallet or even a garment simplify authentication; however, criminals may access data from these cards.

Cryptographic smart cards are often used for single sign-on. Most advanced smart cards include specialized cryptographic hardware that uses algorithms such as RSA and Digital Signature Algorithm (DSA). Today's cryptographic smart cards generate key pairs on board, to avoid the risk from having more than one copy of the key (since by design there usually isn't a way to extract private keys from a smart card). Such smart cards are mainly used for digital signatures and secure identification.

The most common way to access cryptographic smart card functions on a computer is to use a vendor-provided PKCS#11 library. On Microsoft Windows the Cryptographic Service Provider (CSP) API is also supported.

The most widely used cryptographic algorithms in smart cards (excluding the GSM so-called "crypto algorithm") are Triple DES and RSA. The key set is usually loaded (DES) or generated (RSA) on the card at the personalization stage.

Some of these smart cards are also made to support the National Institute of Standards and Technology (NIST) standard for Personal Identity Verification, FIPS 201.

Turkey implemented the first smart card driver's license system in 1987. Turkey had a high level of road accidents and decided to develop and use digital tachograph devices on heavy vehicles, instead of the existing mechanical ones, to reduce speed violations. Since 1987, the professional driver's licenses in Turkey have been issued as smart cards. A professional driver is required to insert his driver's license into a digital tachograph before starting to drive. The tachograph unit records speed violations for each driver and gives a printed report. The driving hours for each driver are also being monitored and reported. In 1990 the European Union conducted a feasibility study through BEVAC Consulting Engineers, titled "Feasibility study with respect to a European electronic drivers license (based on a smart-card) on behalf of Directorate General VII". In this study, chapter seven describes Turkey's experience.

Argentina's Mendoza province began using smart card driver's licenses in 1995. Mendoza also had a high level of road accidents, driving offenses, and a poor record of recovering fines. Smart licenses hold up-to-date records of driving offenses and unpaid fines. They also store personal information, license type and number, and a photograph. Emergency medical information such as blood type, allergies, and biometrics (fingerprints) can be stored on the chip if the card holder wishes. The Argentina government anticipates that this system will help to collect more than $10 million per year in fines.

In 1999 Gujarat was the first Indian state to introduce a smart card license system. As of 2005, it has issued 5 million smart card driving licenses to its people.

In 2002, the Estonian government started to issue smart cards named ID Kaart as primary identification for citizens to replace the usual passport in domestic and EU use. As of 2010 about 1 million smart cards have been issued (total population is about 1.3 million) and they are widely used in internet banking, buying public transport tickets, authorization on various websites etc.

By the start of 2009, the entire population of Belgium was issued eID cards that are used for identification. These cards contain two certificates: one for authentication and one for signature. This signature is legally enforceable. More and more services in Belgium use eID for authorization.

Spain started issuing national ID cards (DNI) in the form of smart cards in 2006 and gradually replaced all the older ones with smart cards. The idea was that many or most bureaucratic acts could be done online but it was a failure because the Administration did not adapt and still mostly requires paper documents and personal presence.

On 14 August 2012, the ID cards in Pakistan were replaced. The Smart Card is a third generation chip-based identity document that is produced according to international standards and requirements. The card has over 36 physical security features and has the latest encryption codes. This smart card replaced the NICOP (the ID card for overseas Pakistani).

Smart cards may identify emergency responders and their skills. Cards like these allow first responders to bypass organizational paperwork and focus more time on the emergency resolution. In 2004, The Smart Card Alliance expressed the needs: "to enhance security, increase government efficiency, reduce identity fraud, and protect personal privacy by establishing a mandatory, Government-wide standard for secure and reliable forms of identification". emergency response personnel can carry these cards to be positively identified in emergency situations. WidePoint Corporation, a smart card provider to FEMA, produces cards that contain additional personal information, such as medical records and skill sets.

In 2007, the Open Mobile Alliance (OMA) proposed a new standard defining V1.0 of the Smart Card Web Server (SCWS), an HTTP server embedded in a SIM card intended for a smartphone user. The non-profit trade association SIMalliance has been promoting the development and adoption of SCWS. SIMalliance states that SCWS offers end-users a familiar, OS-independent, browser-based interface to secure, personal SIM data. As of mid-2010, SIMalliance had not reported widespread industry acceptance of SCWS. The OMA has been maintaining the standard, approving V1.1 of the standard in May 2009, and V1.2 was expected to be approved in October 2012.

Smart cards are also used to identify user accounts on arcade machines.

### Public transit

Smart cards, used as transit passes, and integrated ticketing are used by many public transit operators. Card users may also make small purchases using the cards. Some operators offer points for usage, exchanged at retailers or for other benefits. Examples include Singapore's CEPAS, Malaysia's Touch 'n Go, Ontario's Presto card, Hong Kong's Octopus card, Tokyo's Suica and PASMO cards, London's Oyster card, Ireland's Leap Card, Brussels' MoBIB, Québec's Opus card, Boston's CharlieCard, San Francisco's Clipper card, Washington, D.C.'s SmarTrip, Auckland's AT Hop, Brisbane's go card, Perth's SmartRider, Sydney's Opal card and Victoria's myki. However, these present a privacy risk because they allow the mass transit operator (and the government) to track an individual's movement. In Finland, for example, the Data Protection Ombudsman prohibited the transport operator Helsinki Metropolitan Area Council (YTV) from collecting such information, despite YTV's argument that the card owner has the right to a list of trips paid with the card. Earlier, such information was used in the investigation of the Myyrmanni bombing.

The UK's Department for Transport mandated smart cards to administer travel entitlements for elderly and disabled residents. These schemes let residents use the cards for more than just bus passes. They can also be used for taxi and other concessionary transport. One example is the "Smartcare go" scheme provided by Ecebs. The UK systems use the ITSO Ltd specification. Other schemes in the UK include period travel passes, carnets of tickets or day passes and stored value which can be used to pay for journeys. Other concessions for school pupils, students and job seekers are also supported. These are mostly based on the ITSO Ltd specification.

Many smart transport schemes include the use of low cost smart tickets for simple journeys, day passes and visitor passes. Examples include Glasgow SPT subway. These smart tickets are made of paper or PET which is thinner than a PVC smart card e.g. Confidex smart media. The smart tickets can be supplied pre-printed and over-printed or printed on demand.

In Sweden, as of 2018–19, the old SL Access smart card system has started to be phased out and replaced by smart phone apps. The phone apps have less cost, at least for the transit operators who don't need any electronic equipment (the riders provide that). The riders are able buy tickets anywhere and don't need to load money onto smart cards. New NFC smart cards are still in use for foreseeable future (as of 2024).

### Video games

In Japanese amusement arcades, contactless smart cards (usually referred to as "IC cards") are used by game manufacturers as a method for players to access in-game features (both online like Konami E-Amusement and Sega ALL.Net and offline) and as a memory support to save game progress. Depending on a case by case scenario, the machines can use a game-specific card or a "universal" one usable on multiple machines from the same manufacturer/publisher. Amongst the most widely used there are Banapassport by Bandai Namco, E-amusement pass by Konami, Aime by Sega and Nesica by Taito.

In 2018, in an effort to make arcade game IC cards more user friendly, Konami, Bandai Namco and Sega have agreed on a unified system of cards named *Amusement IC*. Thanks to this agreement, the three companies are now using a unified card reader in their arcade cabinets, so that players are able to use their card, no matter if a Banapassport, an e-Amusement Pass or an Aime, with hardware and ID services of all three manufacturers. A common logo for *Amusement IC* cards has been created, and this is now displayed on compatible cards from all three companies. In January 2019, Taito announced that their Nesica card was also joining the *Amusement IC* agreement with the other three companies.

### Computer security

Smart cards can be used as a security token.

Mozilla's Firefox web browser can use smart cards to store certificates for use in secure web browsing.

Some disk encryption systems, such as VeraCrypt and Microsoft's BitLocker, can use smart cards to securely hold encryption keys, and also to add another layer of encryption to critical parts of the secured disk.

GnuPG, the well known encryption suite, also supports storing keys in a smart card.

Smart cards are also used for single sign-on to log on to computers.

### Schools

Smart cards are being provided to students at some schools and colleges. Uses include:

- Tracking student attendance
- As an electronic purse, to pay for items at canteens, vending machines, laundry facilities, etc.
- Tracking and monitoring food choices at the canteen, to help the student maintain a healthy diet
- Tracking loans from the school library
- Access control for admittance to restricted buildings, dormitories, and other facilities. This requirement may be enforced at all times (such as for a laboratory containing valuable equipment), or just during after-hours periods (such as for an academic building that is open during class times, but restricted to authorized personnel at night), depending on security needs.
- Access to transportation services

### Healthcare

Smart health cards can improve the security and privacy of patient information, provide a secure carrier for portable medical records, reduce health care fraud, support new processes for portable medical records, provide secure access to emergency medical information, enable compliance with government initiatives (e.g., organ donation) and mandates, and provide the platform to implement other applications as needed by the health care organization.

### Other uses

Smart cards are widely used to encrypt digital television streams. VideoGuard is a specific example of how smart card security worked.

### Multiple-use systems

The Malaysian government promotes MyKad as a single system for all smart-card applications. MyKad started as identity cards carried by all citizens and resident non-citizens. Available applications now include identity, travel documents, drivers license, health information, an electronic wallet, ATM bank-card, public toll-road and transit payments, and public key encryption infrastructure. The personal information inside the MYKAD card can be read using special APDU commands.


## Security

Smart cards have been advertised as suitable for personal identification tasks, because they are engineered to be tamper resistant. The chip usually implements some cryptographic algorithm. There are, however, several methods for recovering some of the algorithm's internal state.

Differential power analysis involves measuring the precise time and electric current required for certain encryption or decryption operations. This can deduce the on-chip private key used by public key algorithms such as RSA. Some implementations of symmetric ciphers can be vulnerable to timing or power attacks as well.

Smart cards can be physically disassembled by using acid, abrasives, solvents, or some other technique to obtain unrestricted access to the on-board microprocessor. Although such techniques may involve a risk of permanent damage to the chip, they permit much more detailed information (e.g., photomicrographs of encryption hardware) to be extracted.


## Advantages

The primary advantage of smart cards is their flexibility. Smart cards have multiple functions which simultaneously can be an ID, a credit card, a stored-value cash card, and a repository of personal information such as telephone numbers or medical history. The card can be easily replaced if lost, and, the requirement for a PIN (or other form of security) provides additional security from unauthorised access to information by others. At the first attempt to use it illegally, the card would be deactivated by the card reader itself.

The secondary advantage is security. Smart cards can be electronic key rings, giving the bearer ability to access information and physical places without need for online connections. They are encryption devices, so that the user can encrypt and decrypt information without relying on unknown, and therefore potentially untrustworthy, appliances such as ATMs. Smart cards are very flexible in providing authentication at different level of the bearer and the counterpart. Finally, with the information about the user that smart cards can provide to the other parties, they are useful devices for customizing products and services. Smart cards can also have multiple credentials for different applications. This encourages better security as the user only has to manage a single card which is not only less cognitive load and more convenient.

The tertiary advantage is reduced cost. Smart cards are easily produced and have vastly improved security allowing institutions to reduce their security spending.

Other general benefits of smart cards are:

- Portability
- Increasing data storage capacity
- Reliability that is virtually unaffected by electrical and magnetic fields.


## Smart cards and electronic commerce

Smart cards can be used in electronic commerce, over the Internet, though the business model used in current electronic commerce applications still cannot use the full feature set of the electronic medium. An advantage of smart cards for electronic commerce is their use customize services. For example, for the service supplier to deliver the customized service, the user may need to provide each supplier with their profile, a boring and time-consuming activity. A smart card can contain a non-encrypted profile of the bearer, so that the user can get customized services even without previous contacts with the supplier.


## Disadvantages

The plastic or paper card in which the chip is embedded is fairly flexible. The larger the chip, the higher the probability that normal use could damage it. Cards are often carried in wallets or pockets, a harsh environment for a chip and antenna in contactless cards. PVC cards can crack or break if bent/flexed excessively. However, for large banking systems, failure-management costs can be more than offset by fraud reduction.

The production, use and disposal of PVC plastic is known to be more harmful to the environment than other plastics. Alternative materials including chlorine free plastics and paper are available for some smart applications.

If the account holder's computer hosts malware, the smart card security model may be broken. Malware can override the communication (both input via keyboard and output via application screen) between the user and the application. Man-in-the-browser malware (e.g., the Trojan Silentbanker) could modify a transaction, unnoticed by the user. Banks like Fortis and Belfius in Belgium and Rabobank ("random reader") in the Netherlands combine a smart card with an unconnected card reader to avoid this problem. The customer enters a challenge received from the bank's website, a PIN and the transaction amount into the reader. The reader returns an 8-digit signature. This signature is manually entered into the personal computer and verified by the bank, preventing point-of-sale-malware from changing the transaction amount.

Smart cards have also been the targets of security attacks. These attacks range from physical invasion of the card's electronics, to non-invasive attacks that exploit weaknesses in the card's software or hardware. The usual goal is to expose private encryption keys and then read and manipulate secure data such as funds. Once an attacker develops a non-invasive attack for a particular smart card model, he or she is typically able to perform the attack on other cards of that model in seconds, often using equipment that can be disguised as a normal smart card reader. While manufacturers may develop new card models with additional information security, it may be costly or inconvenient for users to upgrade vulnerable systems. Tamper-evident and audit features in a smart card system help manage the risks of compromised cards.

Another problem is the lack of standards for functionality and security. To address this problem, the Berlin Group launched the ERIDANE Project to propose "a new functional and security framework for smart-card based Point of Interaction (POI) equipment".
