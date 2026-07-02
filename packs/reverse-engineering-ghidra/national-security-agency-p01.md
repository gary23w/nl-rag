---
title: "National Security Agency (part 1/2)"
source: https://en.wikipedia.org/wiki/National_Security_Agency
domain: reverse-engineering-ghidra
license: CC-BY-SA-4.0
tags: ghidra reverse engineering, software reverse engineering, binary decompiler analysis, disassembly workflow, malware code analysis
fetched: 2026-07-02
part: 1/2
---

# National Security Agency

The **National Security Agency** (**NSA**) is an intelligence agency of the United States Department of Defense, under the authority of the director of national intelligence (DNI). The NSA is responsible for global monitoring, collection, and processing of information and data for intelligence and counterintelligence purposes, specializing in a discipline known as signals intelligence (SIGINT). The NSA is also tasked with the protection of U.S. communications networks and information systems. The NSA relies on a variety of measures to accomplish its mission, the majority of which are clandestine. The NSA has roughly 32,000 employees.

Originating as a unit to decipher coded communications in World War II, it was officially formed as the NSA by President Harry S. Truman in 1952. Between then and the end of the Cold War, it became the largest of the U.S. intelligence organizations in terms of personnel and budget. Still, information available as of 2013 indicates that the Central Intelligence Agency (CIA) pulled ahead in this regard, with a budget of $14.7 billion. The NSA currently conducts worldwide mass data collection and has been known to physically bug electronic systems as one method to this end. The NSA is also alleged to have been behind such attack software as Stuxnet, which severely damaged Iran's nuclear program. The NSA, alongside the CIA, maintains a physical presence in many countries across the globe; the CIA/NSA joint Special Collection Service (a highly classified intelligence team) inserts eavesdropping devices in high-value targets (such as presidential palaces or embassies). SCS collection tactics allegedly encompass "close surveillance, burglary, wiretapping, [and] breaking".

Unlike the CIA and the Defense Intelligence Agency (DIA), both of which specialize primarily in foreign human espionage, the NSA does not publicly conduct human intelligence gathering. The NSA is entrusted with assisting with and coordinating SIGINT elements for other government organizations—which Executive Order prevents from engaging in such activities on their own. As part of these responsibilities, the agency has a co-located organization called the Central Security Service (CSS), which facilitates cooperation between the NSA and other U.S. defense cryptanalysis components. To further ensure streamlined communication between the signals intelligence community divisions, the NSA director simultaneously serves as the Commander of the United States Cyber Command and as Chief of the Central Security Service.

The NSA's actions have been a matter of political controversy on several occasions, including its role in providing intelligence during the Gulf of Tonkin incident, which contributed to the escalation of U.S. involvement in the Vietnam War. Declassified documents later revealed that the NSA misinterpreted or overstated signals intelligence, leading to reports of a second North Vietnamese attack that likely never occurred. The agency has also received scrutiny for spying on anti–Vietnam War leaders and the agency's participation in economic espionage. In 2013, the NSA had many of its secret surveillance programs revealed to the public by Edward Snowden, a former NSA contractor. According to the leaked documents, the NSA intercepts and stores the communications of over a billion people worldwide, including United States citizens. The documents also revealed that the NSA tracks hundreds of millions of people's movements using cell phone metadata. Internationally, research has pointed to the NSA's ability to surveil the domestic Internet traffic of foreign countries through "boomerang routing".


## History

### Formation

The origins of the National Security Agency can be traced back to April 28, 1917, three weeks after the U.S. Congress declared war on Germany in World War I. A code and cipher decryption unit was established as the Cable and Telegraph Section, which was also known as the Cipher Bureau. It was headquartered in Washington, D.C., and was part of the war effort under the executive branch without direct congressional authorization. During the war, it was relocated in the army's organizational chart several times. On July 5, 1917, Herbert O. Yardley was assigned to head the unit. At that point, the unit consisted of Yardley and two civilian clerks. It absorbed the Navy's cryptanalysis functions in July 1918. World War I ended on November 11, 1918, and the army cryptographic section of Military Intelligence (MI-8) moved to New York City on May 20, 1919, where it continued intelligence activities as the Code Compilation Company under the direction of Yardley.

### The Black Chamber

After the disbandment of the U.S. Army cryptographic section of military intelligence known as MI-8, the U.S. government created the Cipher Bureau, also known as Black Chamber, in 1919. The Black Chamber was the United States' first peacetime cryptanalytic organization. Jointly funded by the Army and the State Department, the Cipher Bureau was disguised as a New York City commercial code company; it produced and sold such codes for business use. Its true mission, however, was to break the communications (chiefly diplomatic) of other nations. At the Washington Naval Conference, it aided American negotiators by providing them with the decrypted traffic of many of the conference delegations, including the Japanese. The Black Chamber successfully persuaded Western Union, the largest U.S. telegram company at the time, as well as several other communications companies, to illegally give the Black Chamber access to cable traffic of foreign embassies and consulates. Soon, these companies publicly discontinued their collaboration. Despite the Chamber's initial successes, it was shut down in 1929 by U.S. secretary of state Henry L. Stimson, who defended his decision by stating, "Gentlemen do not read each other's mail."

### World War II and its aftermath

During World War II, the Signal Intelligence Service (SIS) was created to intercept and decipher the communications of the Axis powers. When the war ended, the SIS was reorganized as the Army Security Agency (ASA), and it was placed under the leadership of the Director of Military Intelligence.

On May 20, 1949, all cryptologic activities were centralized under a national organization called the Armed Forces Security Agency (AFSA). This organization was originally established within the U.S. Department of Defense under the command of the Joint Chiefs of Staff. The AFSA was tasked with directing the Department of Defense communications and electronic intelligence activities, except those of U.S. military intelligence units. However, the AFSA was unable to centralize communications intelligence and failed to coordinate with civilian agencies that shared its interests, such as the Department of State, the Central Intelligence Agency (CIA) and the Federal Bureau of Investigation (FBI). In December 1951, President Harry S. Truman ordered a panel to investigate how AFSA had failed to achieve its goals. The results of the investigation led to improvements and its redesignation as the National Security Agency.

The National Security Council issued a memorandum of October 24, 1952, that revised National Security Council Intelligence Directive (NSCID) 9. On the same day, Truman issued a second memorandum that called for the establishment of the NSA. The actual establishment of the NSA was done by a November 4 memo by Robert A. Lovett, the Secretary of Defense, changing the name of the AFSA to the NSA, and making the new agency responsible for all communications intelligence. Since President Truman's memo was a classified document, the existence of the NSA was not known to the public at that time. Due to its ultra-secrecy, the U.S. intelligence community referred to the NSA as "No Such Agency".

### Vietnam War

In the 1960s, the NSA played a key role in expanding American commitment to the Vietnam War by providing evidence of a North Vietnamese attack on the American Naval destroyer USS *Maddox* during the Gulf of Tonkin incident. A secret operation, code-named "MINARET", was set up by the NSA to monitor the phone communications of Senators Frank Church and Howard Baker, as well as key leaders of the civil rights movement, including Martin Luther King Jr., and prominent U.S. journalists and athletes who criticized the Vietnam War. However, the project turned out to be controversial, and an internal review by the NSA concluded that its Minaret program was "disreputable if not outright illegal".

The NSA has mounted a major effort to secure tactical communications among U.S. armed forces during the war with mixed success. The NESTOR family of compatible secure voice systems it developed was widely deployed during the Vietnam War, with about 30,000 NESTOR sets produced. However, a variety of technical and operational problems limited their use, allowing the North Vietnamese to exploit and intercept U.S. communications.

### Church Committee hearings

In the aftermath of the Watergate scandal, a congressional hearing in 1975 led by Senator Frank Church revealed that the NSA, in collaboration with Britain's SIGINT intelligence agency, Government Communications Headquarters (GCHQ), had routinely intercepted the international communications of prominent anti-Vietnam war leaders such as Jane Fonda and Dr. Benjamin Spock. The NSA tracked these individuals in a secret filing system that was destroyed in 1974. Following the resignation of President Richard Nixon, there were several investigations into suspected misuse of FBI, CIA and NSA facilities. Senator Frank Church uncovered previously unknown activity, such as a CIA plot (ordered by the administration of President John F. Kennedy) to assassinate Fidel Castro. The investigation also uncovered NSA's wiretaps on targeted U.S. citizens. After the Church Committee hearings, the Foreign Intelligence Surveillance Act of 1978 was passed. This was designed to limit the practice of mass surveillance in the United States.

### 1980s to 1990s

In 1986, the NSA intercepted the communications of the Libyan government during the immediate aftermath of the Berlin discotheque bombing. The White House asserted that the NSA interception had provided "irrefutable" evidence that Libya was behind the bombing, which U.S. President Ronald Reagan cited as a justification for the 1986 United States bombing of Libya.

In 1999, a multi-year investigation by the European Parliament highlighted the NSA's role in economic espionage in a report entitled 'Development of Surveillance Technology and Risk of Abuse of Economic Information'. That year, the NSA founded the NSA Hall of Honor, a memorial at the National Cryptologic Museum in Fort Meade, Maryland. The memorial is a, "tribute to the pioneers and heroes who have made significant and long-lasting contributions to American cryptology". NSA employees must be retired for more than fifteen years to qualify for the memorial.

NSA's infrastructure deteriorated in the 1990s as defense budget cuts resulted in maintenance deferrals. On January 24, 2000, NSA headquarters suffered a total network outage for three days caused by an overloaded network. Incoming traffic was successfully stored on agency servers, but it could not be directed and processed. The agency carried out emergency repairs for $3 million to get the system running again (some incoming traffic was also directed instead to Britain's GCHQ for the time being). Director Michael Hayden called the outage a "wake-up call" for the need to invest in the agency's infrastructure.

In the 1990s the defensive arm of the NSA—the Information Assurance Directorate (IAD)—started working more openly; the first public technical talk by an NSA scientist at a major cryptography conference was J. Solinas' presentation on efficient Elliptic Curve Cryptography algorithms at Crypto 1997. The IAD's cooperative approach to academia and industry culminated in its support for a transparent process for replacing the outdated Data Encryption Standard (DES) by an Advanced Encryption Standard (AES). Cybersecurity policy expert Susan Landau attributes the NSA's harmonious collaboration with industry and academia in the selection of the AES in 2000—and the Agency's support for the choice of a strong encryption algorithm designed by Europeans rather than by Americans—to Brian Snow, who was the Technical Director of IAD and represented the NSA as cochairman of the Technical Working Group for the AES competition, and Michael Jacobs, who headed IAD at the time.

After the terrorist attacks of September 11, 2001, the NSA believed that it had public support for a dramatic expansion of its surveillance activities. According to Neal Koblitz and Alfred Menezes, the period when the NSA was a trusted partner with academia and industry in the development of cryptographic standards started to come to an end when, as part of the change in the NSA in the post-September 11 era, Snow was replaced as Technical Director, Jacobs retired, and IAD could no longer effectively oppose proposed actions by the offensive arm of the NSA.

### War on terror

In the aftermath of the September 11 attacks, the NSA created new IT systems to deal with the flood of information from new technologies like the Internet and cell phones. ThinThread contained advanced data mining capabilities. It also had a "privacy mechanism"; surveillance was stored encrypted; decryption required a warrant. The research done under this program may have contributed to the technology used in later systems. ThinThread was canceled when Michael Hayden chose Trailblazer, which did not include ThinThread's privacy system.

Trailblazer Project ramped up in 2002 and was worked on by Science Applications International Corporation (SAIC), Boeing, Computer Sciences Corporation, IBM, and Litton Industries. Some NSA whistleblowers complained internally about major problems surrounding Trailblazer. This led to investigations by Congress and the NSA and DoD Inspectors General. The project was canceled in early 2004. Turbulence started in 2005. It was developed in small, inexpensive "test" pieces, rather than one grand plan like Trailblazer. It also included offensive cyber-warfare capabilities, like injecting malware into remote computers. Congress criticized Turbulence in 2007 for having similar bureaucratic problems as Trailblazer. It was to be a realization of information processing at higher speeds in cyberspace.

### Global surveillance program disclosures

The massive extent of the NSA's spying, both foreign and domestic, was revealed to the public in a series of detailed disclosures of internal NSA documents beginning in June 2013. Most of the disclosures were leaked by former NSA contractor Edward Snowden. On 4 September 2020, the NSA's surveillance program was ruled unlawful by the US Court of Appeals. The court also added that the US intelligence leaders, who publicly defended it, were not telling the truth.


## Mission

NSA's eavesdropping mission includes radio broadcasting, both from various organizations and individuals, the Internet, telephone calls, and other intercepted forms of communication. Its secure communications mission includes military, diplomatic, and all other sensitive, confidential, or secret government communications.

According to a 2010 article in *The Washington Post*, "every day, collection systems at the National Security Agency intercept and store 1.7  billion e-mails, phone calls and other types of communications. The NSA sorts a fraction of those into 70 separate databases."

Because of its listening task, NSA/CSS has been heavily involved in cryptanalytic research, continuing the work of predecessor agencies which had broken many World War II codes and ciphers (see, for instance, Purple, Venona project, and JN-25). In 2004, NSA Central Security Service and the National Cyber Security Division of the Department of Homeland Security (DHS) agreed to expand the NSA Centers of Academic Excellence in Information Assurance Education Program.

As part of the National Security Presidential Directive 54/Homeland Security Presidential Directive 23 (NSPD 54), signed on January 8, 2008, by President Bush, the NSA became the lead agency to monitor and protect all of the federal government's computer networks from cyber-terrorism. A part of the NSA's mission is to serve as a combat support agency for the Department of Defense.


## Operations

Operations by the National Security Agency can be divided into three types:

- Collection overseas, which falls under the responsibility of the Global Access Operations (GAO) division.
- Domestic collection, which falls under the responsibility of the Special Source Operations (SSO) division.
- Hacking operations, which fall under the responsibility of the Tailored Access Operations (TAO) division.

### Collection overseas

#### Echelon

"Echelon" was created in the incubator of the Cold War. Today it is a legacy system, and several NSA stations are closing. NSA/CSS, in combination with the equivalent agencies in the United Kingdom (Government Communications Headquarters), Canada (Communications Security Establishment), Australia (Australian Signals Directorate), and New Zealand (Government Communications Security Bureau), otherwise known as the UKUSA group, was reported to be in command of the operation of the so-called ECHELON system. Its capabilities were suspected to include the ability to monitor a large proportion of the world's transmitted civilian telephone, fax, and data traffic.

During the early 1970s, the first of what became more than eight large satellite communications dishes were installed at Menwith Hill. Investigative journalist Duncan Campbell reported in 1988 on the "ECHELON" surveillance program, an extension of the UKUSA Agreement on global signals intelligence SIGINT, and detailed how the eavesdropping operations worked. On November 3, 1999, the BBC reported that they had confirmation from the Australian Government of the existence of a powerful "global spying network" code-named Echelon, that could "eavesdrop on every single phone call, fax or e-mail, anywhere on the planet" with Britain and the United States as the chief protagonists. They confirmed that Menwith Hill was "linked directly to the headquarters of the US National Security Agency (NSA) at Fort Meade in Maryland". NSA's United States Signals Intelligence Directive 18 (USSID 18) strictly prohibited the interception or collection of information about "... U.S. persons, entities, corporations or organizations...." without explicit written legal permission from the United States Attorney General when the subject is located abroad, or the Foreign Intelligence Surveillance Court when within U.S. borders. Alleged Echelon-related activities, including its use for motives other than national security, including political and industrial espionage, received criticism from countries outside the UKUSA alliance.

#### Other SIGINT overseas operations

The NSA was also involved in planning to blackmail people with "SEXINT", intelligence gained about a potential target's sexual activity and preferences. Those targeted had not committed any apparent crime nor were they charged with one. To support its facial recognition program, the NSA is intercepting "millions of images per day". The Real Time Regional Gateway is a data collection program introduced in 2005 in Iraq by the NSA during the Iraq War that consisted of gathering all electronic communication, storing it, then searching and otherwise analyzing it. It was effective in providing information about Iraqi insurgents who had eluded less comprehensive techniques. This "collect it all" strategy introduced by NSA director, Keith B. Alexander, is believed by Glenn Greenwald of *The Guardian* to be the model for the comprehensive worldwide mass archiving of communications which NSA is engaged in as of 2013.

A dedicated unit of the NSA locates targets for the CIA for extrajudicial assassination in the Middle East. The NSA has also spied extensively on the European Union, the United Nations, and numerous governments including allies and trading partners in Europe, South America, and Asia. In June 2015, WikiLeaks published documents showing that NSA spied on French companies. WikiLeaks also published documents showing that NSA spied on federal German ministries since the 1990s. Even Germany's Chancellor Angela Merkel's cellphones and phones of her predecessors had been intercepted.

#### Boundless Informant

In June 2013, Edward Snowden revealed that between 8 February and 8 March 2013, the NSA collected about 124.8 billion telephone data items and 97.1 billion computer data items throughout the world, as was displayed in charts from an internal NSA tool codenamed Boundless Informant. Initially, it was reported that some of these data reflected eavesdropping on citizens in countries like Germany, Spain, and France, but later on, it became clear that those data were collected by European agencies during military missions abroad and were subsequently shared with NSA.

#### Bypassing encryption

In 2013, reporters uncovered a secret memo that claims the NSA created and pushed for the adoption of the Dual EC DRBG encryption standard that contained built-in vulnerabilities in 2006 to the United States National Institute of Standards and Technology (NIST), and the International Organization for Standardization (aka ISO). This memo appears to give credence to previous speculation by cryptographers at Microsoft Research. Edward Snowden claims that the NSA often bypasses the encryption process altogether by lifting information before encryption or after decryption.

XKeyscore rules (as specified in a file xkeyscorerules100.txt, sourced by German TV stations NDR and WDR, who claim to have excerpts from its source code) reveal that the NSA tracks users of privacy-enhancing software tools, including Tor; an anonymous email service provided by the MIT Computer Science and Artificial Intelligence Laboratory (CSAIL) in Cambridge, Massachusetts; and readers of the *Linux Journal*.

#### Software backdoors

Linus Torvalds, the founder of Linux kernel, joked during a LinuxCon keynote on September 18, 2013, that the NSA, who is the founder of SELinux, wanted a backdoor in the kernel. However, later, Linus' father, a Member of the European Parliament (MEP), revealed that the NSA actually did this.

> When my oldest son was asked the same question: "Has he been approached by the NSA about backdoors?" he said "No", but at the same time he nodded. Then he was sort of in the legal free. He had given the right answer, everybody understood that the NSA had approached him.

— Nils Torvalds, LIBE Committee Inquiry on Electronic Mass Surveillance of EU Citizens – 11th Hearing, 11 November 2013

IBM Notes was the first widely adopted software product to use public key cryptography for client-server and server–server authentication and encryption of data. Until US laws regulating encryption were changed in 2000, IBM and Lotus were prohibited from exporting versions of Notes that supported symmetric encryption keys that were longer than 40 bits. In 1997, Lotus negotiated an agreement with the NSA that allowed the export of a version that supported stronger keys with 64 bits, but 24 of the bits were encrypted with a special key and included in the message to provide a "workload reduction factor" for the NSA. This strengthened the protection for users of Notes outside the US against private-sector industrial espionage, but not against spying by the US government.

#### Boomerang routing

While it is assumed that foreign transmissions terminating in the U.S. (such as a non-U.S. citizen accessing a U.S. website) subject non-U.S. citizens to NSA surveillance, recent research into boomerang routing has raised new concerns about the NSA's ability to surveil the domestic Internet traffic of foreign countries. Boomerang routing occurs when an Internet transmission that originates and terminates in a single country transits another. Research at the University of Toronto has suggested that approximately 25% of Canadian domestic traffic may be subject to NSA surveillance activities as a result of the boomerang routing of Canadian Internet service providers.

#### Implanting hardware equipment

Intercepted packages are opened carefully by NSA employees.

A "load station" implanting a beacon

A document included in the NSA files released with Glenn Greenwald's book *No Place to Hide* details how the agency's Tailored Access Operations (TAO) and other NSA units gained access to hardware equipment. They intercepted routers, servers, and other network hardware equipment being shipped to organizations targeted for surveillance and installing covert implant firmware onto them before they are delivered. This was described by an NSA manager as "some of the most productive operations in TAO because they preposition access points into hard target networks around the world."

Computers that were seized by the NSA due to interdiction are often modified with a physical device known as Cottonmouth. It is a device that can be inserted at the USB port of a computer to establish remote access to the targeted machine. According to the NSA's Tailored Access Operations (TAO) group implant catalog, after implanting Cottonmouth, the NSA can establish a network bridge "that allows the NSA to load exploit software onto modified computers as well as allowing the NSA to relay commands and data between hardware and software implants."

### Domestic collection

NSA's mission, as outlined in Executive Order 12333 in 1981, is to collect information that constitutes "foreign intelligence or counterintelligence" while *not* "acquiring information concerning the domestic activities of United States persons". NSA has declared that it relies on the FBI to collect information on foreign intelligence activities within the borders of the United States while confining its activities within the United States to the embassies and missions of foreign nations.

The appearance of a 'Domestic Surveillance Directorate' of the NSA was soon exposed as a hoax in 2013. NSA's domestic surveillance activities are limited by the requirements imposed by the Fourth Amendment to the U.S. Constitution. The Foreign Intelligence Surveillance Court for example held in October 2011, citing multiple Supreme Court precedents, that the Fourth Amendment prohibitions against unreasonable searches and seizures apply to the contents of all communications, whatever the means, because "a person's private communications are akin to personal papers." However, these protections do not apply to non-U.S. persons located outside of U.S. borders, so the NSA's foreign surveillance efforts are subject to far fewer limitations under U.S. law. The specific requirements for domestic surveillance operations are contained in the Foreign Intelligence Surveillance Act of 1978 (FISA), which does not extend protection to non-U.S. citizens located outside of U.S. territory.

#### President's Surveillance Program

George W. Bush, president during the 9/11 terrorist attacks, approved the Patriot Act shortly after the attacks to take anti-terrorist security measures. Titles 1, 2, and 9 specifically authorized measures that would be taken by the NSA. These titles granted enhanced domestic security against terrorism, surveillance procedures, and improved intelligence, respectively. On March 10, 2004, there was a debate between President Bush and White House Counsel Alberto Gonzales, Attorney General John Ashcroft, and Acting Attorney General James Comey. The Attorneys General were unsure if the NSA's programs could be considered constitutional. They threatened to resign over the matter, but ultimately the NSA's programs continued. On March 11, 2004, President Bush signed a new authorization for mass surveillance of Internet records, in addition to the surveillance of phone records. This allowed the president to be able to override laws such as the Foreign Intelligence Surveillance Act, which protected civilians from mass surveillance. In addition to this, President Bush also signed that the measures of mass surveillance were also retroactively in place.

One such surveillance program, authorized by the U.S. Signals Intelligence Directive 18 of President George Bush, was the Highlander Project undertaken for the National Security Agency by the U.S. Army 513th Military Intelligence Brigade. NSA relayed telephone (including cell phone) conversations obtained from ground, airborne, and satellite monitoring stations to various U.S. Army Signal Intelligence Officers, including the 201st Military Intelligence Battalion. Conversations of citizens of the U.S. were intercepted, along with those of other nations. Proponents of the surveillance program claim that the President has executive authority to order such action, arguing that laws such as FISA are overridden by the President's Constitutional powers. In addition, some argued that FISA was implicitly overridden by a subsequent statute, the Authorization for Use of Military Force, although the Supreme Court's ruling in *Hamdan v. Rumsfeld* deprecates this view.

#### The PRISM program

Under the PRISM program, which started in 2007, NSA gathers Internet communications from foreign targets from nine major U.S. Internet-based communication service providers: Microsoft, Yahoo, Google, Facebook, PalTalk, AOL, Skype, YouTube and Apple. Data gathered include email, videos, photos, VoIP chats such as Skype, and file transfers.

Former NSA director General Keith Alexander claimed that in September 2009 the NSA prevented Najibullah Zazi and his friends from carrying out a terrorist attack. However, no evidence has been presented demonstrating that the NSA has ever been instrumental in preventing a terrorist attack.

#### The FASCIA database

**FASCIA** is a database created and used by the U.S. National Security Agency that contains trillions of device-location records that are collected from a variety of sources. Its existence was revealed during the 2013 global surveillance disclosure by Edward Snowden.

The FASCIA database stores various types of information, including Location Area Codes (LACs), Cell Tower IDs (CeLLIDs), Visitor Location Registers (VLRs), International Mobile Station Equipment Identity (IMEIs) and MSISDNs (Mobile Subscriber Integrated Services Digital Network-Numbers). Over about seven months, more than 27 terabytes of location data were collected and stored in the database.

#### Commercial Solutions for Classified (CSfC)

Commercial Solutions for Classified (CSfC) is a key component of the NSA's commercial cybersecurity strategy. CSfC-validated commercial products are proven to meet rigorous security requirements for protection of classified National Security Systems (NSS) data. Once validated, the Department of Defense (DoD), Intelligence Community, Military Services, and other U.S. government agencies are able to implement these commercial hardware and software technologies into their data protection and cybersecurity solutions.

### Hacking operations

Besides the more traditional ways of eavesdropping to collect signals intelligence, the NSA is also engaged in hacking computers, smartphones, and their networks. A division that conducts such operations is the Tailored Access Operations (TAO) division, which has been active since at least circa 1998.

According to the *Foreign Policy* magazine, "... the Office of Tailored Access Operations, or TAO, has successfully penetrated Chinese computer and telecommunications systems for almost 15 years, generating some of the best and most reliable intelligence information about what is going on inside the People's Republic of China." In an interview with *Wired* magazine, Edward Snowden said the Tailored Access Operations division accidentally caused Syria's internet blackout in 2012.


## Organizational structure

The NSA is led by the Director of the National Security Agency (DIRNSA), who also serves as Chief of the Central Security Service (CHCSS) and Commander of the United States Cyber Command (USCYBERCOM) and is the highest-ranking military official of these organizations. He is assisted by a Deputy Director, who is the highest-ranking civilian within the NSA/CSS. NSA also has an Inspector General, head of the Office of the Inspector General (OIG); a General Counsel, head of the Office of the General Counsel (OGC); and a Director of Compliance, who is head of the Office of the Director of Compliance (ODOC). The National Security Agency Office of Inspector General has worked on cases in collaboration with the United States Department of Justice and the Central Intelligence Agency Office of Inspector General. Unlike other intelligence organizations such as the CIA or DIA, the NSA has always been particularly reticent concerning its internal organizational structure.

As of the mid-1990s, the National Security Agency was organized into five Directorates:

- The Operations Directorate, which was responsible for SIGINT collection and processing.
- The Technology and Systems Directorate, which develops new technologies for SIGINT collection and processing.
- The Information Systems Security Directorate, which was responsible for NSA's communications and information security missions.
- The Plans, Policy, and Programs Directorate, which provided staff support and general direction for the Agency.
- The Support Services Directorate, which provided logistical and administrative support activities.

Each of these directorates consisted of several groups or elements, designated by a letter. There were for example the A Group, which was responsible for all SIGINT operations against the Soviet Union and Eastern Europe, and the G Group, which was responsible for SIGINT related to all non-communist countries. These groups were divided into units designated by an additional number, like unit A5 for breaking Soviet codes, and G6, being the office for the Middle East, North Africa, Cuba, and Central and South America.

### Directorates

As of 2013, NSA has about a dozen directorates, which are designated by a letter, although not all of them are publicly known.

In the year 2000, a leadership team was formed consisting of the director, the deputy director, and the directors of the Signals Intelligence (SID), the Information Assurance (IAD) and the Technical Directorate (TD). The chiefs of other main NSA divisions became associate directors of the senior leadership team. After President George W. Bush initiated the President's Surveillance Program (PSP) in 2001, the NSA created a 24-hour Metadata Analysis Center (MAC), followed in 2004 by the Advanced Analysis Division (AAD), with the mission of analyzing content, Internet metadata and telephone metadata. Both units were part of the Signals Intelligence Directorate.

In 2016, a proposal combined the Signals Intelligence Directorate with the Information Assurance Directorate into a Directorate of Operations.

### NSANet

NSANet stands for National Security Agency Network and is the official NSA intranet. It is a classified network, for information up to the level of TS/SCI to support the use and sharing of intelligence data between NSA and the signals intelligence agencies of the four other nations of the Five Eyes partnership. The management of NSANet has been delegated to the Central Security Service Texas (CSSTEXAS).

NSANet is a highly secured computer network consisting of fiber-optic and satellite communication channels that are almost completely separated from the public Internet. The network allows NSA personnel and civilian and military intelligence analysts anywhere in the world to have access to the agency's systems and databases. This access is tightly controlled and monitored. For example, every keystroke is logged, activities are audited at random, and downloading and printing of documents from NSANet are recorded. In 1998, NSANet, along with NIPRNet and SIPRNet, had "significant problems with poor search capabilities, unorganized data, and old information". In 2004, the network was reported to have used over twenty commercial off-the-shelf operating systems. Some universities that do highly sensitive research are allowed to connect to it. The thousands of Top Secret internal NSA documents that were taken by Edward Snowden in 2013 were stored in "a file-sharing location on the NSA's intranet site"; so, they could easily be read online by NSA personnel. Everyone with a TS/SCI clearance had access to these documents. As a system administrator, Snowden was responsible for moving accidentally misplaced highly sensitive documents to safer storage locations.

### Watch centers

The NSA maintains at least two watch centers:

- National Security Operations Center (NSOC), which is the NSA's current operations center and focal point for time-sensitive SIGINT reporting for the United States SIGINT System (USSS). This center was established in 1968 as the National SIGINT Watch Center (NSWC) and was renamed into National SIGINT Operations Center (NSOC) in 1973. This "nerve center of the NSA" got its current name in 1996.
- NSA/CSS Threat Operations Center (NTOC), which is the primary NSA/CSS partner for Department of Homeland Security response to cyber incidents. The NTOC establishes real-time network awareness and threat characterization capabilities to forecast, alert, and attribute malicious activity and enable the coordination of Computer Network Operations. The NTOC was established in 2004 as a joint Information Assurance and Signals Intelligence project.

### NSA Police

The NSA has its law enforcement team, known as the *NSA Police* (and formerly as *NSA Security Protective Force*) which provides law enforcement services, emergency response, and physical security to its officials and properties.

NSA Police are armed federal officers. NSA Police has a K9 division, which generally conducts explosive detection screening of mail, vehicles, and cargo entering NSA grounds. They use marked vehicles to carry out patrols.


## Employees

The number of NSA employees is officially classified but there are several sources providing estimates. In 1961, the NSA had 59,000 military and civilian employees, which grew to 93,067 in 1969, of which 19,300 worked at the headquarters at Fort Meade. In the early 1980s, NSA had roughly 50,000 military and civilian personnel. By 1989 this number had grown again to 75,000, of which 25,000 worked at the NSA headquarters. Between 1990 and 1995 the NSA's budget and workforce were cut by one-third, which led to a substantial loss of experience.

In 2012, the NSA said more than 30,000 employees worked at Fort Meade and other facilities. In 2012, John C. Inglis, the deputy director, said that the total number of NSA employees is "somewhere between 37,000 and one billion" as a joke, and stated that the agency is "probably the biggest employer of introverts." In 2013 *Der Spiegel* stated that the NSA had 40,000 employees. More widely, it has been described as the world's largest single employer of mathematicians. Some NSA employees form part of the workforce of the National Reconnaissance Office (NRO), the agency that provides the NSA with satellite signals intelligence. As of 2013 about 1,000 system administrators work for the NSA.

### Personnel security

The NSA received criticism early on in 1960 after two agents had defected to the Soviet Union. Investigations by the House Un-American Activities Committee and a special subcommittee of the United States House Committee on Armed Services revealed severe cases of ignorance of personnel security regulations, prompting the former personnel director and the director of security to step down and leading to the adoption of stricter security practices. Nonetheless, security breaches reoccurred only a year later when in an issue of *Izvestia* of July 23, 1963, a former NSA employee published several cryptologic secrets. The very same day, an NSA clerk-messenger committed suicide as ongoing investigations disclosed that he had sold secret information to the Soviets regularly. The reluctance of congressional houses to look into these affairs prompted a journalist to write, "If a similar series of tragic blunders occurred in any ordinary agency of Government an aroused public would insist that those responsible be officially censured, demoted, or fired." David Kahn criticized the NSA's tactics of concealing its doings as smug and the Congress' blind faith in the agency's right-doing as shortsighted and pointed out the necessity of surveillance by the Congress to prevent abuse of power.

Edward Snowden's leaking of the existence of PRISM in 2013 caused the NSA to institute a "two-man rule", where two system administrators are required to be present when one accesses certain sensitive information. Snowden claims he suggested such a rule in 2009.

#### Polygraphing

The NSA conducts polygraph tests of employees. For new employees, the tests are meant to discover enemy spies who are applying to the NSA and to uncover any information that could make an applicant pliant to coercion. As part of the latter, historically *EPQs* or "embarrassing personal questions" about sexual behavior had been included in the NSA polygraph. The NSA also conducts five-year periodic reinvestigation polygraphs of employees, focusing on counterintelligence programs. In addition, the NSA conducts periodic polygraph investigations to find spies and leakers; those who refuse to take them may receive "termination of employment", according to a 1982 memorandum from the director of the NSA.

There are also "special access examination" polygraphs for employees who wish to work in highly sensitive areas, and those polygraphs cover counterintelligence questions and some questions about behavior. NSA's brochure states that the average test length is between two and four hours. A 1983 report of the Office of Technology Assessment stated that "It appears that the NSA [National Security Agency] (and possibly CIA) use the polygraph not to determine deception or truthfulness per se, but as a technique of interrogation to encourage admissions." Sometimes applicants in the polygraph process confess to committing felonies such as murder, rape, and selling of illegal drugs. Between 1974 and 1979, of the 20,511 job applicants who took polygraph tests, 695 (3.4%) confessed to previous felony crimes; almost all of those crimes had been undetected.

In 2010 the NSA produced a video explaining its polygraph process. The video, ten minutes long, is titled "The Truth About the Polygraph" and was posted to the Web site of the Defense Security Service. Jeff Stein of *The Washington Post* said that the video portrays "various applicants, or actors playing them—it's not clear—describing everything bad they had heard about the test, the implication being that none of it is true." AntiPolygraph.org argues that the NSA-produced video omits some information about the polygraph process; it produced a video responding to the NSA video. George Maschke, the founder of the Web site, accused the NSA polygraph video of being "Orwellian".

In 2013, an article indicated that after Edward Snowden revealed his identity in 2013, the NSA began requiring polygraphing of employees once per quarter.

### Arbitrary firing

The number of exemptions from legal requirements has been criticized. When in 1964 Congress was hearing a bill giving the director of the NSA the power to fire at will any employee, *The Washington Post* wrote: "This is the very definition of arbitrariness. It means that an employee could be discharged and disgraced based on anonymous allegations without the slightest opportunity to defend himself." Yet, the bill was accepted by an overwhelming majority. Also, every person hired to a job in the US after 2007, at any private organization, state or federal government agency, *must* be reported to the New Hire Registry, ostensibly to look for child support evaders, *except* that employees of an intelligence agency may be excluded from reporting if the director deems it necessary for national security reasons.
