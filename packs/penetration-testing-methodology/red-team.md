---
title: "Red team"
source: https://en.wikipedia.org/wiki/Red_team
domain: penetration-testing-methodology
license: CC-BY-SA-4.0
tags: penetration testing, red team assessment, vulnerability scanner, security exploit, open source intelligence
fetched: 2026-07-02
---

# Red team

A **red team** is a group that simulates an adversary, attempts a physical or digital intrusion against an organization at the direction of that organization, then reports back so that the organization can improve their defenses. Red teams work for the organization or are hired by the organization. Their work is legal, but it can surprise some employees who may not know that red teaming is occurring, or who may be deceived by the red team. Some definitions of red team are broader, and they include any group within an organization that is directed to think outside the box and look at alternative scenarios that are considered less plausible. This directive can be an important defense against false assumptions and groupthink. The term *red teaming* originated in the 1960s in the United States.

Technical red teaming focuses on compromising networks and computers digitally. There may also be a blue team, a term for cybersecurity employees who are responsible for defending an organization's networks and computers against attack. In technical red teaming, attack vectors are used to gain access, and then reconnaissance is performed to discover more devices to potentially compromise. Credential hunting involves scouring a computer for credentials such as passwords and session cookies, and once these are found, can be used to compromise additional computers. During intrusions from third parties, a red team may team up with the blue team to assist in defending the organization. Rules of engagement and standard operating procedures are often utilized to ensure that the red team does not cause damage during their exercises.

Physical red teaming focuses on sending a team to gain entry to restricted areas. This is done to test and optimize physical security such as fences, cameras, alarms, locks, and employee behavior. As with technical red teaming, rules of engagement are used to ensure that red teams do not cause excessive damage during their exercises. Physical red teaming will often involve a reconnaissance phase where information is gathered and weaknesses in security are identified, and then that information will be used to conduct an operation (typically at night) to gain physical entry to the premises. Security devices will be identified and defeated using tools and techniques. Physical red teamers will be given specific objectives such as gaining access to a server room and taking a portable hard drive, or gaining access to an executive's office and taking confidential documents.

Red teams are used in several fields, including cybersecurity, airport security, law enforcement, the military, and intelligence agencies. In the United States government, red teams are used by the Army, Marine Corps, Department of Defense, Federal Aviation Administration, and Transportation Security Administration.

## History

The concept of red teaming and blue teaming emerged in the early 1960s. One early example of red teaming involved the think tank RAND Corporation, which did simulations for the United States military during the Cold War. "Red team" and the color red were used to represent the Soviet Union, and "blue team" and the color blue were used to represent the United States. Another early example involved United States Secretary of Defense Robert McNamara, who assembled a red team and a blue team to explore which government contractor should be awarded an experimental aircraft contract. Another early example modeled negotiating an arms control treaty and evaluating its effectiveness.

Red teams are sometimes associated with "contrarian thinking" and fighting groupthink, the tendency of groups to make and keep assumptions even in the face of evidence to the contrary. One example of a group that was not called a red team, but that arguably was one of the earliest examples of forming a group to fight groupthink, is the Israeli Ipcha Mistraba that was formed after Israeli decision-making failures during the Yom Kippur War in 1973. The attack against Israel nearly took Israel by surprise despite ample evidence of an impending attack, and almost resulted in Israel's defeat. Ipcha Mistabra was formed after the war, and given the duty of always presenting a contrarian, unexpected, or unorthodox analysis of foreign policy and intelligence reports, so that things would be less likely to be overlooked going forward.

In the early 2000s, there are examples of red teams being used for tabletop exercises. A tabletop exercise is often used by first responders and involves acting out and planning for worst-case scenarios, similar to playing a tabletop board game. In response to the September 11 attacks, with anti-terrorism in mind, the Central Intelligence Agency created a new Red Cell, and red teams were used for modeling responses to asymmetric warfare such as terrorism. In response to the failures of the Iraq War, red teaming became more common in the United States Army.

Over time, the practice of red teaming expanded to other industries and organizations, including corporations, government agencies, and non-profit organizations. The approach has become increasingly popular in the world of cybersecurity, where red teams are used to simulate real-world attacks on an organization's digital infrastructure and test the effectiveness of their cybersecurity measures, and is progressing into the analysis of generative AI technologies such as LLMs.

## Cybersecurity

**Technical red teaming** involves testing the digital security of an organization by attempting to infiltrate their computer systems digitally.

### Terminology

A *blue team* is a group in charge of defending against intrusions.

In cybersecurity, a *penetration test* involves ethical hackers ("pen testers") attempting to break into a computer system, with no element of surprise. The organization is aware of the penetration test and is ready to mount a defense.

A *red team* goes a step further, and adds physical penetration, social engineering, and an element of surprise. The blue team is given no advance warning of a red team, and will treat it as a real intrusion. One role of a permanent, in-house red team is to improve the security culture of the organization.

A ***purple team*** is the temporary combination of both teams and can provide rapid information responses during a test. One advantage of purple teaming is that the red team can launch certain attacks repeatedly, and the blue team can use that to set up detection software, calibrate it, and steadily increase detection rate. Purple teams may engage in "threat hunting" sessions, where both the red team and the blue team look for real intruders. Involving other employees in the purple team is also beneficial, for example software engineers who can help with logging and software alerts, and managers who can help identify the most financially damaging scenarios. One danger of purple teaming is complacence and the development of groupthink, which can be combatted by hiring people with different skillsets or hiring an external vendor.

A *white team* is a group that oversees and manages operations between red teams and blue teams. For example, this may be a company's managers that determine the rules of engagement for the red team.

### Attack

The initial entry point of a red team or an adversary is called the beachhead. A mature blue team is often adept at finding the beachhead and evicting attackers. A role of the red team is to increase the skills of the blue team.

When infiltrating, there is a stealthy "surgical" approach that stays under the radar of the blue team and requires a clear objective, and a noisy "carpet bombing" approach that is more like a brute force attack. Carpet bombing is often the more useful approach for red teams, because it can discover unexpected vulnerabilities.

There are a variety of cybersecurity threats. Threats may range from something traditional such as hacking the network's domain controller, or something less orthodox such as setting up cryptocurrency mining, or providing too much employee access to personally identifiable information (PII) which opens the company up to General Data Protection Regulation (GDPR) fines. Any of these threats can be red teamed, in order to explore how severe the issue is. Tabletop exercises, where intrusions are acted out over a tabletop similar to how one would play a board game, can be used to simulate intrusions that are too expensive, too complicated, or illegal to execute live. It can be useful to attempt intrusions against the red team and the blue team, in addition to more traditional targets.

Once access to a network is achieved, reconnaissance can be conducted. The data gathered can be placed in a graph database, which is software that visually plots nodes, relationships, and properties. Typical nodes might be computers, users, or permission groups. Red teams will usually have very good graph databases of their own organization, because they can utilize home-field advantage, including working with the blue team to create a thorough map of the network, and a thorough list of users and administrators. A query language such as Cypher can be used to create and modify graph databases. Any type of administrator account is valuable to place in the graph database, including administrators of third-party tools such as Amazon Web Services (AWS). Data can sometimes be exported from tools and then inserted into the graph database.

Once the red team has compromised a computer, website, or system, a powerful technique is credential hunting. These can be in the form of clear text passwords, ciphertext, hashes, or access tokens. The red team gets access to a computer, looks for credentials that can be used to access a different computer, then this is repeated, with the goal of accessing many computers. Credentials can be stolen from many locations, including files, source code repositories such as Git, computer memory, and tracing and logging software. Techniques such as pass the cookie and pass the hash can be used to get access to websites and machines without entering a password. Techniques such as optical character recognition (OCR), exploiting default passwords, spoofing a credential prompt, and phishing can also be used.

The red team can utilize computer programming and command-line interface (CLI) scripts to automate some of their tasks. For example, CLI scripts can utilize the Component Object Model (COM) on Microsoft Windows machines in order to automate tasks in Microsoft Office applications. Useful tasks might include sending emails, searching documents, encrypting, or retrieving data. Red teams can take control of a browser using Internet Explorer's COM, Google Chrome's remote debugging feature, or the testing framework Selenium.

### Defense

During a real intrusion, the red team can be repurposed to work with the blue team to help with defense. Specifically, they can provide analysis of what the intruders will likely try to do next. During an intrusion, both the red team and the blue team have a home-field advantage because they are more familiar with the organization's networks and systems than the intruder.

An organization's red team may be an attractive target for real attackers. Red team member's machines may contain sensitive information about the organization. In response, red team member's machines are often secured. Techniques for securing machines include configuring the operating system's firewall, restricting Secure Shell (SSH) and Bluetooth access, improving logging and alerts, securely deleting files, and encrypting hard drives.

One tactic is to engage in "active defense", which involves setting up decoys and honeypots to help track the location of intruders. These honeypots can help alert the blue team to a network intrusion that might otherwise have gone undetected. Various software can be used to set up a honeypot file depending on the operating system: macOS tools include OpenBMS, Linux tools include auditd plugins, and Windows tools include System Access Control Lists (SACL). Notifications can include popups, emails, and writing to a log file. Centralized monitoring, where important log files are quickly sent to logging software on a different machine, is a useful network defense technique.

### Managing a red team

The use of rules of engagement can help to delineate which systems are off-limits, prevent security incidents, and ensure that employee privacy is respected. The use of a standard operating procedure (SOP) can ensure that the proper people are notified and involved in planning, and improve the red team process, making it mature and repeatable. Red team activities typically have a regular rhythm.

Tracking certain metrics or key performance indicators (KPIs) can help to make sure a red team is achieving the desired output. Examples of red team KPIs include performing a certain number of penetration tests per year, or by growing the team by a certain number of pen testers within a certain time period. It can also be useful to track the number of compromised machines, compromisable machines, and other metrics related to infiltration. These statistics can be graphed by day and placed on a dashboard displayed in the security operations center (SOC) to provide motivation to the blue team to detect and close breaches.

In order to identify worst offenders, compromises can be graphed and grouped by where in the software they were discovered, company office location, job title, or department. Monte Carlo simulations can be used to identify which intrusion scenarios are most likely, most damaging, or both. A Test Maturity Model, a type of Capability Maturity Model, can be used to assess how mature a red team is, and what the next step is to grow. The MITRE ATT&CK Navigator, a list of tactics, techniques, and procedures (TTPs) including advanced persistent threats (APTs), can be consulted to see how many TTPs a red team is exploiting, and give additional ideas for TTPs to utilize in the future.

## Physical intrusion

**Physical red teaming** or physical penetration testing involves testing the physical security of a facility, including the security practices of its employees and security equipment. Examples of security equipment include security cameras, locks, and fences. In physical red teaming, computer networks are not usually the target. Unlike cybersecurity, which typically has many layers of security, there may only be one or two layers of physical security present.

Having a "rules of engagement" document that is shared with the client is helpful, to specify which TTPs will be used, what locations may be targeted, what may not be targeted, how much damage to equipment such as locks and doors is permitted, what the plan is, what the milestones are, and sharing contact information. The rules of engagement may be updated after the reconnaissance phase, with another round of back and forth between the red team and the client. The data gathered during the reconnaissance phase can be used to create an operational plan, both for internal use, and to send to the client for approval.

### Reconnaissance

Part of physical red teaming is performing reconnaissance. The type of reconnaissance gathered usually includes information about people, places, security devices, and weather. Reconnaissance has a military origin, and military reconnaissance techniques are applicable to physical red teaming. Red team reconnaissance equipment might include military clothing since it does not rip easily, red lights to preserve night vision and be less detectable, radios and earpieces, camera and tripod, binoculars, night vision equipment, and an all-weather notebook. Some methods of field communication include a Bluetooth earpiece dialed into a cell phone conference call during the day, and two-way radios with earpieces at night. In case of compromise, red team members often carry identification and an authorization letter with multiple after-hours contacts who can vouch for the legality and legitimacy of the red team's activities.

Before physical reconnaissance occurs, open-source intelligence (OSINT) gathering can occur by researching locations and staff members via the Internet, including the company's website, social media accounts, search engines, mapping websites, and job postings (which give hints about the technology and software the company uses). It is a good practice to do multiple days of reconnaissance, to reconnoiter both during the day and at night, to bring at least three operators, to utilize a nearby staging area that is out of sight of the target, and to do reconnaissance and infiltration as two separate trips rather than combining them.

Recon teams can use techniques to conceal themselves and equipment. For example, a passenger van can be rented and the windows can be blacked out to conceal photography and videography of the target. Examining and videoing the locks of a building during a walk-around can be concealed by the recon pretending to be on the phone. In the event of compromise, such as employees becoming suspicious, a story can be rehearsed ahead of time until it can be recited confidently. If the team has split up, the compromise of one operator can result in the team leader pulling the other operators out. Concealed video cameras can be used to capture footage for later review, and debriefs can be done quickly after leaving the area so that fresh information is quickly documented.

### Infiltration

Most physical red team operations occur at night, due to reduced security of the facility and so that darkness can conceal activities. An ideal infiltration is usually invisible both outside the facility (the approach is not detected by bystanders or security devices) and inside the facility (no damage is done and nothing is bumped or left out of place), and does not alert anyone that a red team was there.

#### Preparation

The use of a load out list can help ensure that important red team equipment is not forgotten. The use of military equipment such as MOLLE vests and small tactical bags can provide useful places to store tools, but has the downsides of being conspicuous and increasing encumbrance. Black clothing or dark camouflage can be helpful in rural areas, whereas street clothes in shades of gray and black may be preferred in urban areas. Other urban disguise items include a laptop bag, or a pair of headphones around the neck. Various types of shoe coverings can be used to minimize footprints both outdoors and indoors.

#### Approach

Light discipline (keeping lights from vehicles, flashlights, and other tools to a minimum) reduces the chance of compromise. Some tactics of light discipline include using red flashlights, using only one vehicle, and keeping the vehicle's headlights off.

Sometimes there are security changes between reconnaissance and infiltration, so it is a good practice for teams that are approaching a target to "assess and acclimate", to see if any new security measures can be seen. Compromises during infiltration are most likely to occur during the approach to the facility. Employees, security, police, and bystanders are the most likely compromise a physical red team. Bystanders are rarer in rural areas, but also much more suspicious.

Proper movement can help a red team avoid being spotted while approaching a target, and may include rushing, crawling, avoiding silhouetting when on hills, walking in formations such as single file, and walking in short bursts then pausing. The use of hand signals may be used to reduce noise.

#### Entering the facility

Common security devices include doors, locks, fences, alarms, motion sensors, and ground sensors. Doors and locks are often faster and quieter to bypass with tools and shims, rather than lock picking. RFID locks are common at businesses, and covert RFID readers combined with social engineering during reconnaissance can be used to duplicate an authorized employee's badge. Barbed wire on fences can be bypassed by placing a thick blanket over it. Anti-climb fences can be bypassed with ladders.

Alarms can sometimes be neutralized with a radio jammer that targets the frequencies that alarms use for their internal and external communications. Motion sensors can be defeated with a special body-sized shield that blocks a person's heat signature. Ground sensors are prone to false positives, which can lead security personnel to not trust them or ignore them.

#### Inside the facility

Once inside, if there is suspicion that the building is occupied, disguising oneself as a cleaner or employee using the appropriate clothing is a good tactic. Noise discipline is often important once inside a building, as there are less ambient sounds to mask red team noises.

Red teams usually have goal locations selected and tasks pre-planned for each team or team member, such as entering a server room or an executive's office. However, it can be difficult to figure out a room's location in advance, so this is often figured out on the fly. Reading emergency exit route signs and the use of a watch with a compass can assist with navigating inside of buildings.

Commercial buildings will often have some lights left on. It is good practice to not turn lights on or off, as this may alert someone. Instead, utilizing already unlit areas is preferred for red team operations, with rushing and freezing techniques to be used to quickly move through illuminated areas. Standing full-height in front of windows and entering buildings via lobbies is often avoided due to the risks of being seen.

A borescope can be used to peer around corners and under doors, to help spot people, cameras, or motion detectors.

Once the target room has been reached, if something needs to be found such as a specific document or specific equipment, the room can be divided into sections, with each red team member focusing on a section.

Passwords are often located under keyboards. Techniques can be used to avoid disturbing the placement of objects in offices such as keyboards and chairs, as adjusting these will often be noticed. Lights and locks can be left in their original state of on or off, locked or unlocked. Steps can be taken to ensure that equipment is not left behind, such as having a list of all equipment brought in and checking that all items are accounted for.

It is good practice to radio situation reports (SITREPs) to the team leader when unusual things happen. The team leader can then decide if the operation should continue, should be aborted, or if a team member should surrender by showing their authorization letter and ID. When confronted by civilians such as employees, red team operators can attempt social engineering. When confronted by law enforcement, it is good practice to immediately surrender due to the potential legal and safety consequences.

#### Exiting the facility

The ideal way to exit a facility is slowly and carefully, similar to how entry was achieved. There is sometimes an urge to rush out after achieving a mission goal, but this is not good practice. Exiting slowly and carefully maintains situational awareness, in case a previously empty area now has someone in it or approaching it. While the entrance path is normally taken during exit, a closer or alternative exit can also be used.

The goal of all team members is to reach the rally point, or possibly a second emergency rally point. The rally point is usually at a different location than the dropoff point.

## Users

### Companies and organizations

Private companies sometimes use red teams to supplement their normal security procedures and personnel. For example, Microsoft and Google utilize red teams to help secure their systems. Some financial institutions in Europe use the TIBER-EU framework.

### Intelligence agencies

When applied to intelligence work, red teaming is sometimes called **alternative analysis**. Alternative analysis involves bringing in fresh analysts to double-check the conclusions of another team, to challenge assumptions and make sure nothing was overlooked. Three red teams were used to review the intelligence that led to the killing of Osama bin Laden in 2011, including red teams from outside the Central Intelligence Agency, because there were major diplomatic and public relations consequences for launching a military operation into Pakistan, so it was important to double-check the original team's intelligence and conclusions.

After failures to anticipate the Yom Kippur War, the Israeli Defense Forces' Intelligence Directorate formed a red team called *Ipcha Mistabra* ("on the contrary") to re-examine discarded assumptions and avoid complacency. The North Atlantic Treaty Organization (NATO) utilizes alternative analysis.

### Militaries

Militaries typically uses red teaming for alternative analysis, simulations, and vulnerability probes. In military wargaming, the opposing force (OPFOR) in a simulated conflict may be referred to as a Red Cell. The key theme is that the adversary (red team) leverages tactics, techniques, and equipment as appropriate to emulate the desired actor. The red team challenges operational planning by playing the role of a mindful adversary.

The United Kingdom Ministry of Defence has a red team program.

Red teams were used in the United States Armed Forces much more frequently after a 2003 Defense Science Review Board recommended them to help prevent the shortcomings that led to the September 11 attacks. The U.S. Army created the Army Directed Studies Office in 2004. This was the first service-level red team, and until 2011 was the largest in the Department of Defense (DoD). The University of Foreign Military and Cultural Studies provides courses for red team members and leaders. Most resident courses are conducted at Fort Leavenworth and target students from U.S. Army Command and General Staff College (CGSC) or equivalent intermediate and senior level schools. Courses include topics such as critical thinking, groupthink mitigation, cultural empathy, and self-reflection.

The Marine Corps red team concept commenced in 2010 when the Commandant of the Marine Corps (CMC) General James F. Amos attempted to implement it. Amos drafted a white paper titled, *Red Teaming in the Marine Corps*. In this document, Amos discussed how the concept of the red team needs to challenge the process of planning and making decisions by applying critical thinking from the tactical to strategic level. In June 2013, the Marine Corps staffed the red team billets outlined in the draft white paper. In the Marine Corps, all Marines designated to fill red team positions complete either six-week or nine-week red team training courses provided by the University of Foreign Military and Cultural Studies (UFMCS).

The DoD uses cyber red teams to conduct adversarial assessments on their networks. These red teams are certified by the National Security Agency and accredited by the United States Strategic Command.

### Airport security

The United States Federal Aviation Administration (FAA) has been implementing red teams since Pan Am Flight 103 over Lockerbie, Scotland, which suffered a terrorist attack in 1988. Red teams conduct tests at about 100 US airports annually. Tests were on hiatus after the September 11 attacks in 2001, and resumed in 2003 under the Transportation Security Administration, who assumed the FAA's aviation security role after 9/11. Before the September 11 attacks, FAA use of red teaming revealed severe weaknesses in security at Logan International Airport in Boston, where two of the four hijacked 9/11 flights originated. Some former FAA investigators who participated on these teams feel that the FAA deliberately ignored the results of the tests, and that this resulted in part in the 9/11 terrorist attack on the US.

The United States Transportation Security Administration has used red teaming in the past. In one red team operation, undercover agents were able to fool Transportation Security Officers and bring weapons and fake explosives through security 67 out of 70 times in 2015.
