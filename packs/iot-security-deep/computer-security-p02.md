---
title: "Computer security (part 2/3)"
source: https://en.wikipedia.org/wiki/Computer_security
domain: iot-security-deep
license: CC-BY-SA-4.0
tags: iot security, embedded device hardening, botnet compromise defense, mirai botnet mitigation, over the air update
fetched: 2026-07-02
part: 2/3
---

## Systems at risk

The growth in the number of computer systems and the increasing reliance upon them by individuals, businesses, industries, and governments means that there are an increasing number of systems at risk.

### Financial systems

The computer systems of financial regulators and financial institutions like the U.S. Securities and Exchange Commission, SWIFT, investment banks, and commercial banks are prominent hacking targets for cybercriminals interested in manipulating markets and making illicit gains. Websites and apps that accept or store credit card numbers, brokerage accounts, and bank account information are also prominent hacking targets, because of the potential for immediate financial gain from transferring money, making purchases, or selling the information on the black market. In-store payment systems and ATMs have also been tampered with in order to gather customer account data and PINs.

The UCLA Internet Report: Surveying the Digital Future (2000) found that the privacy of personal data created barriers to online sales and that more than nine out of 10 internet users were somewhat or very concerned about credit card security.

The most common web technologies for improving security between browsers and websites are named SSL (Secure Sockets Layer), and its successor TLS (Transport Layer Security), identity management and authentication services, and domain name services allow companies and consumers to engage in secure communications and commerce. Several versions of SSL and TLS are commonly used today in applications such as web browsing, e-mail, internet faxing, instant messaging, and VoIP (voice-over-IP). There are various interoperable implementations of these technologies, including at least one implementation that is open source. Open source allows anyone to view the application's source code, and look for and report vulnerabilities.

The credit card companies Visa and MasterCard cooperated to develop the secure EMV chip which is embedded in credit cards. Further developments include the Chip Authentication Program where banks give customers hand-held card readers to perform online secure transactions. Other developments in this arena include the development of technology such as Instant Issuance which has enabled shopping mall kiosks acting on behalf of banks to issue on-the-spot credit cards to interested customers.

### Utilities and industrial equipment

Computers control functions at many utilities, including coordination of telecommunications, the power grid, nuclear power plants, and valve opening and closing in water and gas networks. The Internet is a potential attack vector for such machines if connected, but the Stuxnet worm demonstrated that even equipment controlled by computers not connected to the Internet can be vulnerable. In 2014, the Computer Emergency Readiness Team, a division of the Department of Homeland Security, investigated 79 hacking incidents at energy companies.

### Aviation

The aviation industry is very reliant on a series of complex systems which could be attacked. A simple power outage at one airport can cause repercussions worldwide, much of the system relies on radio transmissions which could be disrupted, and controlling aircraft over oceans is especially dangerous because radar surveillance only extends 175 to 225 miles offshore. There is also potential for attack from within an aircraft.

Implementing fixes in aerospace systems poses a unique challenge because efficient air transportation is heavily affected by weight and volume. Improving security by adding physical devices to airplanes could increase their unloaded weight, and could potentially reduce cargo or passenger capacity.

In Europe, with the (Pan-European Network Service) and NewPENS, and in the US with the NextGen program, air navigation service providers are moving to create their own dedicated networks.

Many modern passports are now biometric passports, containing an embedded microchip that stores a digitized photograph and personal information such as name, gender, and date of birth. In addition, more countries are introducing facial recognition technology to reduce identity-related fraud. The introduction of the ePassport has assisted border officials in verifying the identity of the passport holder, thus allowing for quick passenger processing. Plans are under way in the US, the UK, and Australia to introduce SmartGate kiosks with both retina and fingerprint recognition technology. The airline industry is moving from the use of traditional paper tickets towards the use of electronic tickets (e-tickets). These have been made possible by advances in online credit card transactions in partnership with the airlines. Long-distance bus companies are also switching over to e-ticketing transactions today.

The consequences of a successful attack range from loss of confidentiality to loss of system integrity, air traffic control outages, loss of aircraft, and even loss of life.

### Consumer devices

Desktop computers and laptops are commonly targeted to gather passwords or financial account information or to construct a botnet to attack another target. Smartphones, tablet computers, smart watches, and other mobile devices such as quantified self devices like activity trackers have sensors such as cameras, microphones, GPS receivers, compasses, and accelerometers which could be exploited, and may collect personal information, including sensitive health information. WiFi, Bluetooth, and cell phone networks on any of these devices could be used as attack vectors, and sensors might be remotely activated after a successful breach.

The increasing number of home automation devices such as the Nest thermostat are also potential targets.

### Healthcare

Today many healthcare providers and health insurance companies use the internet to provide enhanced products and services. Examples are the use of tele-health to potentially offer better quality and access to healthcare, or fitness trackers to lower insurance premiums. Patient records are increasingly being placed on secure in-house networks, alleviating the need for extra storage space.

### Large corporations

Large corporations are common targets. In many cases attacks are aimed at financial gain through identity theft and involve data breaches. Examples include the loss of millions of clients' credit card and financial details by Home Depot, Staples, Target Corporation, and Equifax.

Medical records have been targeted in general identify theft, health insurance fraud, and impersonating patients to obtain prescription drugs for recreational purposes or resale. Although cyber threats continue to increase, 62% of all organizations did not increase security training for their business in 2015.

Not all attacks are financially motivated, however: security firm HBGary Federal had a serious series of attacks in 2011 from hacktivist group Anonymous in retaliation for the firm's CEO claiming to have infiltrated their group, and Sony Pictures was hacked in 2014 with the apparent dual motive of embarrassing the company through data leaks and crippling the company by wiping workstations and servers.

### Automobiles

Vehicles are increasingly computerized, with engine timing, cruise control, anti-lock brakes, seat belt tensioners, door locks, airbags and advanced driver-assistance systems on many models. Additionally, connected cars may use WiFi and Bluetooth to communicate with onboard consumer devices and the cell phone network. Self-driving cars are expected to be even more complex. All of these systems carry some security risks, and such issues have gained wide attention.

Simple examples of risk include a malicious compact disc being used as an attack vector, and the car's onboard microphones being used for eavesdropping. However, if access is gained to a car's internal controller area network, the danger is much greater – and in a widely publicized 2015 test, hackers remotely carjacked a vehicle from 10 miles away and drove it into a ditch.

Manufacturers are reacting in numerous ways, with Tesla in 2016 pushing out some security fixes *over the air* into its cars' computer systems. In the area of autonomous vehicles, in September 2016 the United States Department of Transportation announced some initial safety standards, and called for states to come up with uniform policies.

Additionally, e-Drivers' licenses are being developed using the same technology. For example, Mexico's licensing authority (ICV) has used a smart card platform to issue the first e-Drivers' licenses to the city of Monterrey, in the state of Nuevo León.

### Shipping

Shipping companies have adopted RFID (Radio Frequency Identification) technology as an efficient, digitally secure, tracking device. Unlike a barcode, RFID can be read up to 20 feet away. RFID is used by FedEx and UPS.

### Government

Government and military computer systems are commonly attacked by activists and foreign powers. This includes local and regional government infrastructure such as traffic light controls, police and intelligence agency communications, personnel records, as well as student records.

### Internet of things and physical vulnerabilities

The Internet of things (IoT) is the network of physical objects such as devices, vehicles, and buildings that are embedded with electronics, software, sensors, and network connectivity that enables them to collect and exchange data. Concerns have been raised that this is being developed without appropriate consideration of the security challenges involved.

While the IoT creates opportunities for more direct integration of the physical world into computer-based systems, it also provides opportunities for misuse. In particular, as the Internet of Things spreads widely, cyberattacks are likely to become an increasingly physical (rather than simply virtual) threat. If a front door's lock is connected to the Internet, and can be locked/unlocked from a phone, then a criminal could enter the home at the press of a button from a stolen or hacked phone. People could stand to lose much more than their credit card numbers in a world controlled by IoT-enabled devices. Thieves have also used electronic means to circumvent non-Internet-connected hotel door locks.

An attack aimed at physical infrastructure or human lives is often called a cyber-kinetic attack. As IoT devices and appliances become more widespread, the prevalence and potential damage of cyber-kinetic attacks can increase substantially.

### Medical systems

Medical devices have either been successfully attacked or had potentially deadly vulnerabilities demonstrated, including both in-hospital diagnostic equipment and implanted devices including pacemakers and insulin pumps. There are many reports of hospitals and hospital organizations getting hacked, including ransomware attacks, Windows XP exploits, viruses, and data breaches of sensitive data stored on hospital servers. On 28 December 2016 the US Food and Drug Administration released its recommendations for how medical device manufacturers should maintain the security of Internet-connected devices – but no structure for enforcement.

### Energy sector

In distributed generation systems, the risk of a cyberattack is real, according to *Daily Energy Insider*. An attack could cause a loss of power in a large area for a long period of time, and such an attack could have just as severe consequences as a natural disaster. The District of Columbia is considering creating a Distributed Energy Resources (DER) Authority within the city, with the goal being for customers to have more insight into their own energy use and giving the local electric utility, Pepco, the chance to better estimate energy demand. The D.C. proposal, however, would "allow third-party vendors to create numerous points of energy distribution, which could potentially create more opportunities for cyberattackers to threaten the electric grid."

### Telecommunications

Perhaps the most widely known digitally secure telecommunication device is the SIM (Subscriber Identity Module) card, a device that is embedded in most of the world's cellular devices before any service can be obtained. The SIM card is just the beginning of this digitally secure environment.

The Smart Card Web Servers draft standard (SCWS) defines the interfaces to an HTTP server in a smart card. Tests are being conducted to secure OTA ("over-the-air") payment and credit card information from and to a mobile phone. Combination SIM/DVD devices are being developed through Smart Video Card technology which embeds a DVD-compliant optical disc into the card body of a regular SIM card.

Other telecommunication developments involving digital security include mobile signatures, which use the embedded SIM card to generate a legally binding electronic signature.


## Cost and impact of security breaches

Serious financial damage has been caused by security breaches, but because there is no standard model for estimating the cost of an incident, the only data available is that which is made public by the organizations involved. "Several computer security consulting firms produce estimates of total worldwide losses attributable to virus and worm attacks and to hostile digital acts in general. The 2003 loss estimates by these firms range from $13 billion (worms and viruses only) to $226 billion (for all forms of covert attacks). The reliability of these estimates is often challenged; the underlying methodology is basically anecdotal."

However, reasonable estimates of the financial cost of security breaches can actually help organizations make rational investment decisions. According to the classic Gordon-Loeb Model analyzing the optimal investment level in information security, one can conclude that the amount a firm spends to protect information should generally be only a small fraction of the expected loss (i.e., the expected value of the loss resulting from a cyber/information security breach).


## Attacker motivation

As with physical security, the motivations for breaches of computer security vary between attackers. Some are thrill-seekers or vandals, some are activists, others are criminals looking for financial gain. State-sponsored attackers are now common and well resourced but started with amateurs such as Markus Hess who hacked for the KGB, as recounted by Clifford Stoll in *The Cuckoo's Egg*.

Attackers motivations can vary for all types of attacks from pleasure to political goals. For example, hacktivists may target a company or organization that carries out activities they do not agree with. This would be to create bad publicity for the company by having its website crash.

High capability hackers, often with larger backing or state sponsorship, may attack based on the demands of their financial backers. These attacks are more likely to attempt more serious attack. An example of a more serious attack was the 2015 Ukraine power grid hack, which reportedly utilised the spear-phishing, destruction of files, and denial-of-service attacks to carry out the full attack.

Additionally, recent attacker motivations can be traced back to extremist organizations seeking to gain political advantage or disrupt social agendas. The growth of the internet, mobile technologies, and inexpensive computing devices have led to a rise in capabilities but also to the risk to environments that are deemed as vital to operations. All critical targeted environments are susceptible to compromise and this has led to a series of proactive studies on how to migrate the risk by taking into consideration motivations by these types of actors. Several stark differences exist between the hacker motivation and that of nation state actors seeking to attack based on an ideological preference.

A key aspect of threat modeling for any system is identifying the motivations behind potential attacks and the individuals or groups likely to carry them out. The level and detail of security measures will differ based on the specific system being protected. For instance, a home personal computer, a bank, and a classified military network each face distinct threats, despite using similar underlying technologies.


## Computer security incident management

Computer security incident management is an organized approach to addressing and managing the aftermath of a computer security incident or compromise with the goal of preventing a breach or thwarting a cyberattack. An incident that is not identified and managed at the time of intrusion typically escalates to a more damaging event such as a data breach or system failure. The intended outcome of a computer security incident response plan is to contain the incident, limit damage and assist recovery to business as usual. Responding to compromises quickly can mitigate exploited vulnerabilities, restore services and processes and minimize losses. Incident response planning allows an organization to establish a series of best practices to stop an intrusion before it causes damage. Typical incident response plans contain a set of written instructions that outline the organization's response to a cyberattack. Without a documented plan in place, an organization may not successfully detect an intrusion or compromise and stakeholders may not understand their roles, processes and procedures during an escalation, slowing the organization's response and resolution.

There are four key components of a computer security incident response plan:

1. Preparation: Preparing stakeholders on the procedures for handling computer security incidents or compromises
2. Detection and analysis: Identifying and investigating suspicious activity to confirm a security incident, prioritizing the response based on impact and coordinating notification of the incident
3. Containment, eradication and recovery: Isolating affected systems to prevent escalation and limit impact, pinpointing the genesis of the incident, removing malware, affected systems and bad actors from the environment and restoring systems and data when a threat no longer remains
4. Post incident activity: Post mortem analysis of the incident, its root cause and the organization's response with the intent of improving the incident response plan and future response efforts.


## Notable attacks and breaches

Some illustrative examples of different types of computer security breaches are given below.

### Robert Morris and the first computer worm

In 1988, 60,000 computers were connected to the Internet, and most were mainframes, minicomputers and professional workstations. On 2 November 1988, many started to slow down, because they were running a malicious code that demanded processor time and that spread itself to other computers – the first internet computer worm. The software was traced back to 23-year-old Cornell University graduate student Robert Tappan Morris who said "he wanted to count how many machines were connected to the Internet".

### Rome Laboratory

In 1994, over a hundred intrusions were made by unidentified crackers into the Rome Laboratory, the US Air Force's main command and research facility. Using trojan horses, hackers were able to obtain unrestricted access to Rome's networking systems and remove traces of their activities. The intruders were able to obtain classified files, such as air tasking order systems data and furthermore able to penetrate connected networks of National Aeronautics and Space Administration's Goddard Space Flight Center, Wright-Patterson Air Force Base, some Defense contractors, and other private sector organizations, by posing as a trusted Rome center user.

### TJX customer credit card details

In early 2007, American apparel and home goods company TJX announced that it was the victim of an unauthorized computer systems intrusion and that the hackers had accessed a system that stored data on credit card, debit card, check, and merchandise return transactions.

### Stuxnet attack

In 2010, the computer worm known as Stuxnet reportedly ruined almost one-fifth of Iran's nuclear centrifuges. It did so by disrupting industrial programmable logic controllers (PLCs) in a targeted attack. This is generally believed to have been launched by Israel and the United States to disrupt Iran's nuclear program – although neither has publicly admitted this.

### Global surveillance disclosures

In early 2013, documents provided by Edward Snowden were published by *The Washington Post* and *The Guardian* exposing the massive scale of NSA global surveillance. There were also indications that the NSA may have inserted a backdoor in a NIST standard for encryption. This standard was later withdrawn due to widespread criticism. The NSA additionally were revealed to have tapped the links between Google's data centers.

### Target and Home Depot breaches

A Ukrainian hacker known as Rescator broke into Target Corporation computers in 2013, stealing roughly 40 million credit cards, and then Home Depot computers in 2014, stealing between 53 and 56 million credit card numbers. Warnings were delivered at both corporations, but ignored; physical security breaches using self checkout machines are believed to have played a large role. "The malware utilized is absolutely unsophisticated and uninteresting," says Jim Walter, director of threat intelligence operations at security technology company McAfee – meaning that the heists could have easily been stopped by existing antivirus software had administrators responded to the warnings. The size of the thefts has resulted in major attention from state and Federal United States authorities and the investigation is ongoing.

### Office of Personnel Management data breach

In April 2015, the Office of Personnel Management discovered it had been hacked more than a year earlier in a data breach, resulting in the theft of approximately 21.5 million personnel records handled by the office. The Office of Personnel Management hack has been described by federal officials as among the largest breaches of government data in the history of the United States. Data targeted in the breach included personally identifiable information such as Social Security numbers, names, dates and places of birth, addresses, and fingerprints of current and former government employees as well as anyone who had undergone a government background check. It is believed the hack was perpetrated by Chinese hackers.

### Ashley Madison breach

In July 2015, a hacker group known as The Impact Team successfully breached the extramarital relationship website Ashley Madison, created by Avid Life Media. The group claimed that they had taken not only company data but user data as well. After the breach, The Impact Team dumped emails from the company's CEO, to prove their point, and threatened to dump customer data unless the website was taken down permanently. When Avid Life Media did not take the site offline the group released two more compressed files, one 9.7GB and the second 20GB. After the second data dump, Avid Life Media CEO Noel Biderman resigned; but the website remained to function.

### Colonial Pipeline ransomware attack

In June 2021, the cyberattack took down the largest fuel pipeline in the U.S. and led to shortages across the East Coast.


## Legal issues and global regulation

International legal issues of cyberattacks are complicated in nature. There is no global base of common rules to judge, and eventually punish, cybercrimes and cybercriminals - and where security firms or agencies do locate the cybercriminal behind the creation of a particular piece of malware or form of cyberattack, often the local authorities cannot take action due to lack of laws under which to prosecute. Proving attribution for cybercrimes and cyberattacks is also a major problem for all law enforcement agencies. "Computer viruses switch from one country to another, from one jurisdiction to another – moving around the world, using the fact that we don't have the capability to globally police operations like this. So the Internet is as if someone [had] given free plane tickets to all the online criminals of the world." The use of techniques such as dynamic DNS, fast flux and bullet proof servers add to the difficulty of investigation and enforcement.


## Role of government

The role of the government is to make regulations to force companies and organizations to protect their systems, infrastructure and information from any cyberattacks, but also to protect its own national infrastructure such as the national power-grid.

The government's regulatory role in cyberspace is complicated. For some, cyberspace was seen as a virtual space that was to remain free of government intervention, as can be seen in many of today's libertarian blockchain and bitcoin discussions.

Many government officials and experts think that the government should do more and that there is a crucial need for improved regulation, mainly due to the failure of the private sector to solve efficiently the cybersecurity problem. R. Clarke said during a panel discussion at the RSA Security Conference in San Francisco, he believes that the "industry only responds when you threaten regulation. If the industry doesn't respond (to the threat), you have to follow through." On the other hand, executives from the private sector agree that improvements are necessary, but think that government intervention would affect their ability to innovate efficiently. Daniel R. McCarthy analyzed this public-private partnership in cybersecurity and reflected on the role of cybersecurity in the broader constitution of political order.

On 22 May 2020, the UN Security Council held its second ever informal meeting on cybersecurity to focus on cyber challenges to international peace. According to UN Secretary-General António Guterres, new technologies are too often used to violate rights.


## International actions

Many different teams and organizations exist, including:

- The Forum of Incident Response and Security Teams (FIRST) is the global association of CSIRTs. The US-CERT, AT&T, Apple, Cisco, McAfee, Microsoft are all members of this international team.
- The Council of Europe helps protect societies worldwide from the threat of cybercrime through the Convention on Cybercrime.
- The purpose of the Messaging Anti-Abuse Working Group (MAAWG) is to bring the messaging industry together to work collaboratively and to successfully address the various forms of messaging abuse, such as spam, viruses, denial-of-service attacks and other messaging exploitations. France Telecom, Facebook, AT&T, Apple, Cisco, Sprint are some of the members of the MAAWG.
- ENISA : The European Network and Information Security Agency (ENISA) is an agency of the European Union with the objective to improve network and information security in the European Union.

### Europe

On 14 April 2016, the European Parliament and the Council of the European Union adopted the General Data Protection Regulation (GDPR). The GDPR, which came into force on 25 May 2018, grants individuals within the European Union (EU) and the European Economic Area (EEA) the right to the protection of personal data. The regulation requires that any entity that processes personal data incorporate data protection by design and by default. It also requires that certain organizations appoint a Data Protection Officer (DPO).

The IT Security Association TeleTrusT exist in Germany since June 1986, which is an international competence network for IT security.


## National actions

To protect national network and system security, many countries have established strategies and staffing for computer emergency response teams, proactive cyber defence, and cyber threat intelligence. National policy actions typically include cybersecurity regulations and information security standards.

### Canada

Since 2010, Canada has had a cyber security strategy. This functions as a counterpart document to the National Strategy and Action Plan for Critical Infrastructure. The strategy has three main pillars: securing government systems, securing vital private cyber systems, and helping Canadians to be secure online. There is also a Cyber Incident Management Framework to provide a coordinated response in the event of a cyber incident.

The Canadian Cyber Incident Response Centre (CCIRC) is responsible for mitigating and responding to threats to Canada's critical infrastructure and cyber systems. It provides support to mitigate cyber threats, technical support to respond & recover from targeted cyber attacks, and provides online tools for members of Canada's critical infrastructure sectors. It posts regular cyber security bulletins & operates an online reporting tool where individuals and organizations can report a cyber incident.

To inform the general public on how to protect themselves online, Public Safety Canada has partnered with STOP.THINK.CONNECT, a coalition of non-profit, private sector, and government organizations, and launched the Cyber Security Cooperation Program. They also run the GetCyberSafe portal for Canadian citizens, and Cyber Security Awareness Month during October.

Public Safety Canada aims to begin an evaluation of Canada's cybersecurity strategy in early 2015.

### Australia

Australian federal government announced an $18.2 million investment to fortify the cyber security resilience of small and medium enterprises (SMEs) and enhance their capabilities in responding to cyber threats. This financial backing is an integral component of the 2023-2030 Australian Cyber Security Strategy. A substantial allocation of $7.2 million is earmarked for the establishment of a voluntary cyber health check program, facilitating businesses in conducting a comprehensive and tailored self-assessment of their cyber security upskill.

This avant-garde health assessment serves as a diagnostic tool, enabling enterprises to ascertain the robustness of Australia's cyber security regulations. Furthermore, it affords them access to a repository of educational resources and materials, fostering the acquisition of skills necessary for an elevated cyber security posture. This groundbreaking initiative was jointly disclosed by Minister for Cyber Security Clare O'Neil and Minister for Small Business Julie Collins.

### Hong Kong

Hong Kong's Protection of Critical Infrastructures (Computer Systems) Bill (the “Bill”) was passed by the Legislative Council on 19 March 2025, with the purpose to “establish legal requirements for organisations designated as critical infrastructure operators”. To defend the economy and public safety against the cyber threats of severe disruption, Hong Kong’s new Protection of Critical Infrastructures (Computer Systems) Ordinance (Cap.653) (Ordinance), together with its Code of Practice (CoP) guidelines for gatekeepers at the front line of defence, came into effect on 1 January 2026.

### India

Some provisions for cybersecurity have been incorporated into rules framed under the Information Technology Act 2000.

The National Cyber Security Policy 2013 is a policy framework by the Ministry of Electronics and Information Technology (MeitY) which aims to protect the public and private infrastructure from cyberattacks, and safeguard "information, such as personal information (of web users), financial and banking information and sovereign data". CERT- In is the nodal agency which monitors the cyber threats in the country. The post of National Cyber Security Coordinator has also been created in the Prime Minister's Office (PMO).

The Indian Companies Act 2013 has also introduced cyber law and cyber security obligations on the part of Indian directors. Some provisions for cyber security have been incorporated into rules framed under the Information Technology Act 2000 Update in 2013.

### South Korea

Following cyberattacks in the first half of 2013, when the government, news media, television stations, and bank websites were compromised, the national government committed to the training of 5,000 new cybersecurity experts by 2017. The South Korean government blamed its northern counterpart for these attacks, as well as incidents that occurred in 2009, 2011, and 2012, but Pyongyang denies the accusations.

### United Kingdom

In 2016 the National Cyber Security Centre was formed as the central body overseeing cybersecurity in the UK, as part of GCHQ. The UK government published a National Cyber Security Strategy in 2022 assigning £2.6bn for industry, skills and national security. In addition, the National Cyber Force, launched in 2020, works with GCHQ and the Ministry of Defence and aims to "transform the UK's ability to contest adversaries in cyber space, to protect the country, its people and our way of life".

### United States

#### Strategies and directives

In 2013, executive order 13636 *Improving Critical Infrastructure Cybersecurity* was signed, which prompted the creation of the NIST Cybersecurity Framework.

The 2018 cyber strategy called for specific measures to harden U.S. government networks from attacks, such as the June 2015 intrusion into the U.S. Office of Personnel Management (OPM), which compromised the records of about 4.2 million current and former government employees.

In response to the Colonial Pipeline ransomware attack President Joe Biden signed Executive Order 14028 on May 12, 2021, to increase software security standards for sales to the government, tighten detection and security on existing systems, improve information sharing and training, establish a Cyber Safety Review Board, and improve incident response.

The Biden administration released a comprehensive National Cybersecurity Strategy in 2023.

##### Legislation

The 1986 Computer Fraud and Abuse Act prohibits unauthorized access or damage of protected computers as defined in 18 U.S.C. § 1030(e)(2).

##### Standardized government testing services

The General Services Administration (GSA) has standardized the *penetration test* service as a pre-vetted support service, to rapidly address potential vulnerabilities, and stop adversaries before they impact US federal, state and local governments. These services are commonly referred to as Highly Adaptive Cybersecurity Services (HACS).

##### Agencies

The Department of Homeland Security has a dedicated division responsible for the response system, risk management program and requirements for cyber security in the United States called the National Cyber Security Division. The division is home to US-CERT operations and the National Cyber Alert System. The National Cybersecurity and Communications Integration Center brings together government organizations responsible for protecting computer networks and networked infrastructure.

The third priority of the FBI is to: "Protect the United States against cyber-based attacks and high-technology crimes", and they, along with the National White Collar Crime Center (NW3C), and the Bureau of Justice Assistance (BJA) are part of the multi-agency task force, The Internet Crime Complaint Center, also known as IC3.

In addition to its own specific duties, the FBI participates alongside non-profit organizations such as InfraGard.

The Computer Crime and Intellectual Property Section (CCIPS) operates in the United States Department of Justice Criminal Division. The CCIPS is in charge of investigating computer crime and intellectual property crime and is specialized in the search and seizure of digital evidence in computers and networks. In 2017, CCIPS published A Framework for a Vulnerability Disclosure Program for Online Systems to help organizations "clearly describe authorized vulnerability disclosure and discovery conduct, thereby substantially reducing the likelihood that such described activities will result in a civil or criminal violation of law under the Computer Fraud and Abuse Act (18 U.S.C. § 1030)."

The United States Cyber Command, also known as USCYBERCOM, "has the mission to direct, synchronize, and coordinate cyberspace planning and operations to defend and advance national interests in collaboration with domestic and international partners." It has no role in the protection of civilian networks.

The U.S. Federal Communications Commission's role in cybersecurity is to strengthen the protection of critical communications infrastructure, to assist in maintaining the reliability of networks during disasters, to aid in swift recovery after, and to ensure that first responders have access to effective communications services.

The Food and Drug Administration has issued guidance for medical devices, and the National Highway Traffic Safety Administration is concerned with automotive cyber security. After being criticized by the Government Accountability Office, and following successful attacks on airports and claimed attacks on airplanes, the Federal Aviation Administration has devoted funding to securing systems on board the planes of private manufacturers, and the Aircraft Communications Addressing and Reporting System. Concerns have also been raised about the future Next Generation Air Transportation System.

The US Department of Defense (DoD) issued DoD Directive 8570 in 2004, supplemented by DoD Directive 8140, requiring all DoD employees and all DoD contract personnel involved in information assurance roles and activities to earn and maintain various industry Information Technology (IT) certifications in an effort to ensure that all DoD personnel involved in network infrastructure defense have minimum levels of IT industry recognized knowledge, skills and abilities (KSA). Andersson and Reimers (2019) report these certifications range from CompTIA's A+ and Security+ through the ICS2.org's CISSP, etc.

*Computer emergency response team* is a name given to expert groups that handle computer security incidents. In the US, two distinct organizations exist, although they do work closely together.

- US-CERT: part of the National Cyber Security Division of the United States Department of Homeland Security.
- CERT/CC: created by the Defense Advanced Research Projects Agency (DARPA) and run by the Software Engineering Institute (SEI).

In the context of U.S. nuclear power plants, the U.S. Nuclear Regulatory Commission (NRC) outlines cyber security requirements under 10 CFR Part 73, specifically in 10 CFR 73.54. The Nuclear Energy Institute's NEI 08-09 document, *Cyber Security Plan for Nuclear Power Reactors*, outlines a comprehensive framework for cybersecurity in the nuclear power industry.


## Modern warfare

There is growing concern that cyberspace will become the next theater of warfare. As Mark Clayton from *The Christian Science Monitor* wrote in a 2015 article titled "The New Cyber Arms Race":

> In the future, wars will not just be fought by soldiers with guns or with planes that drop bombs. They will also be fought with the click of a mouse a half a world away that unleashes carefully weaponized computer programs that disrupt or destroy critical industries like utilities, transportation, communications, and energy. Such attacks could also disable military networks that control the movement of troops, the path of jet fighters, the command and control of warships.

This has led to new terms such as *cyberwarfare* and *cyberterrorism*. The United States Cyber Command was created in 2009 and many other countries have similar forces.

There are a few critics that question whether cyber security is as significant a threat as it is made out to be.


## Careers

Cyber security is a fast-growing field of IT concerned with reducing organizations' risk of getting hacked or data breaches. According to research from the Enterprise Strategy Group, 46% of organizations say that they have a "problematic shortage" of cyber security skills in 2016, up from 28% in 2015. Commercial, government and non-governmental organizations all employ cybersecurity professionals. The fastest increases in demand for cyber security workers are in industries managing increasing volumes of consumer data such as finance, health care, and retail. However, the use of the term *cybersecurity* is more prevalent in government job descriptions.

Cybersecurity job titles and descriptions include:

**Security analyst**

Analyzes and assesses vulnerabilities in the infrastructure (software, hardware, networks), investigates using available tools and countermeasures to remedy the detected vulnerabilities and recommends solutions and best practices. Analyzes and assesses damage to the data/infrastructure as a result of security incidents, examines available recovery tools and processes, and recommends solutions. Tests for compliance with security policies and procedures. May assist in the creation, implementation, or management of security solutions.

**Security engineer**

Performs security monitoring, security and data/logs analysis, and forensic analysis, to detect security incidents, and mount the incident response. Investigates and utilizes new technologies and processes to enhance security capabilities and implement improvements. May also review code or perform other

security engineering

methodologies.

**Security architect**

Designs a security system or major components of a security system, and may head a security design team building a new security system.

**Chief Information Security Officer (CISO)**

A high-level management position responsible for the entire information security division/staff. The position may include hands-on technical work.

**Chief Security Officer (CSO)**

A high-level management position responsible for the entire security division/staff. A newer position is now deemed needed as security risks grow.

**Data Protection Officer (DPO)**

A DPO is tasked with monitoring compliance with data protection laws (such as

GDPR

), data protection policies, awareness-raising, training, and audits.

**Security consultant/specialist/intelligence**

Broad titles that encompass any one or all of the other roles or titles tasked with protecting computers, networks, software, data or information systems against viruses, worms, spyware, malware, intrusion detection, unauthorized access, denial-of-service attacks, and an ever-increasing list of attacks by hackers acting as individuals or as part of organized crime or foreign governments.

Student programs are also available for people interested in beginning a career in cyber security. Meanwhile, an alternative option for information security professionals of varied experience levels to keep studying is online security training, including webcasts. A wide range of courses are also available.

In the United Kingdom, a nationwide set of cyber security forums, known as the U.K Cyber Security Forum, were established supported by the Government's cyber security strategy in order to encourage start-ups and innovation and to address the skills gap identified by the U.K Government.

In Singapore, the Cyber Security Agency has issued a Singapore Operational Technology (OT) Cybersecurity Competency Framework (OTCCF). The framework defines emerging cybersecurity roles in Operational Technology. The OTCCF was endorsed by the Infocomm Media Development Authority (IMDA). It outlines the different OT cybersecurity job positions as well as the technical skills and core competencies necessary. It also depicts the many career paths available, including vertical and lateral advancement opportunities.
