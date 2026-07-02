---
title: "Computer security (part 3/3)"
source: https://en.wikipedia.org/wiki/Computer_security
domain: iot-security-deep
license: CC-BY-SA-4.0
tags: iot security, embedded device hardening, botnet compromise defense, mirai botnet mitigation, over the air update
fetched: 2026-07-02
part: 3/3
---

## Terminology

The following terms used with regards to computer security are explained below:

- Access authorization restricts access to a computer to a group of users through the use of authentication systems. These systems can protect either the whole computer, such as through an interactive login screen, or individual services, such as a FTP server. There are many methods for identifying and authenticating users, such as passwords, identification cards, smart cards, and biometric systems.
- Anti-virus software consists of computer programs that attempt to identify, thwart, and eliminate computer viruses and other malicious software (malware).
- Applications are executable code, so general corporate practice is to restrict or block users the power to install them; to install them only when there is a demonstrated need (e.g. software needed to perform assignments); to install only those which are known to be reputable (preferably with access to the computer code used to create the application), and to reduce the attack surface by installing as few as possible. They are typically run with least privilege, with a robust process in place to identify, test and install any released security patches or updates for them.
  - For example, programs can be installed into an individual user's account, which limits the program's potential access, as well as being a means control which users have specific exceptions to policy. In Linux, FreeBSD, OpenBSD, and other Unix-like operating systems there is an option to further restrict an application using chroot or other means of restricting the application to its own 'sandbox'. For example. Linux provides namespaces, and Cgroups to further restrict the access of an application to system resources.
  - Generalized security frameworks such as SELinux or AppArmor help administrators control access.
  - Java and other languages which compile to Java byte code and run in the Java virtual machine can have their access to other applications controlled at the virtual machine level.
  - Some software can be run in software containers which can even provide their own set of system libraries, limiting the software's, or anyone controlling it, access to the server's versions of the libraries.
- Authentication techniques can be used to ensure that communication end-points are who they say they are.
- Automated theorem proving and other verification tools can be used to enable critical algorithms and code used in secure systems to be mathematically proven to meet their specifications.
- Backups are one or more copies kept of important computer files. Typically, multiple copies will be kept at different locations so that if a copy is stolen or damaged, other copies will still exist.
- Capability and access control list techniques can be used to ensure privilege separation and mandatory access control. Capabilities vs. ACLs discusses their use.
- Chain of trust techniques can be used to attempt to ensure that all software loaded has been certified as authentic by the system's designers.
- Confidentiality is the nondisclosure of information except to another authorized person.
- Cryptographic techniques can be used to defend data in transit between systems, reducing the probability that the data exchange between systems can be intercepted or modified.
- Cyber attribution, is an attribution of cybercrime, i.e., finding who perpetrated a cyberattack.
- Cyberwarfare is an Internet-based conflict that involves politically motivated attacks on information and information systems. Such attacks can, for example, disable official websites and networks, disrupt or disable essential services, steal or alter classified data, and cripple financial systems.
- Data integrity is the accuracy and consistency of stored data, indicated by an absence of any alteration in data between two updates of a data record.

- Encryption is used to protect the confidentiality of a message. Cryptographically secure ciphers are designed to make any practical attempt of breaking them infeasible. Symmetric-key ciphers are suitable for bulk encryption using shared keys, and public-key encryption using digital certificates can provide a practical solution for the problem of securely communicating when no key is shared in advance.
- Endpoint security software aids networks in preventing malware infection and data theft at network entry points made vulnerable by the prevalence of potentially infected devices such as laptops, mobile devices, and USB drives.
- Firewalls serve as a gatekeeper system between networks, allowing only traffic that matches defined rules. They often include detailed logging, and may include intrusion detection and intrusion prevention features. They are near-universal between company local area networks and the Internet, but can also be used internally to impose traffic rules between networks if network segmentation is configured.
- A hacker is someone who seeks to breach defenses and exploit weaknesses in a computer system or network.
- Honey pots are computers that are intentionally left vulnerable to attack by crackers. They can be used to catch crackers and to identify their techniques.
- Intrusion-detection systems are devices or software applications that monitor networks or systems for malicious activity or policy violations.
- A microkernel is an approach to operating system design which has only the near-minimum amount of code running at the most privileged level – and runs other elements of the operating system such as device drivers, protocol stacks and file systems, in the safer, less privileged user space.
- Pinging. The standard ping application can be used to test if an IP address is in use. If it is, attackers may then try a port scan to detect which services are exposed.
- A port scan is used to probe an IP address for open ports to identify accessible network services and applications.
- A key logger is spyware that silently captures and stores each keystroke that a user types on the computer's keyboard.
- Social engineering is the use of deception to manipulate individuals to breach security.
- Logic bombs is a type of malware added to a legitimate program that lies dormant until it is triggered by a specific event.
- A unikernel is a computer program that runs on a minimalistic operating system where a single application is allowed to run (as opposed to a general purpose operating system where many applications can run at the same time). This approach to minimizing the attack surface is adopted mostly in cloud environments where software is deployed in virtual machines.
- Zero trust security means that no one is trusted by default from inside or outside the network, and verification is required from everyone trying to gain access to resources on the network.


## History

Since the Internet's arrival and with the digital transformation initiated in recent years, the notion of cybersecurity has become a familiar subject in both our professional and personal lives. Cybersecurity and cyber threats have been consistently present for the last 60 years of technological change. In the 1970s and 1980s, computer security was mainly limited to academia until the conception of the Internet, where, with increased connectivity, computer viruses and network intrusions began to take off. After the spread of viruses in the 1990s, the 2000s marked the institutionalization of organized attacks such as distributed denial of service. This led to the formalization of cybersecurity as a professional discipline.

The April 1967 session organized by Willis Ware at the Spring Joint Computer Conference, and the later publication of the Ware Report, were foundational moments in the history of the field of computer security. Ware's work straddled the intersection of material, cultural, political, and social concerns.

A 1977 NIST publication introduced the *CIA triad* of confidentiality, integrity, and availability as a clear and simple way to describe key security goals. While still relevant, many more elaborate frameworks have since been proposed.

However, in the 1970s and 1980s, there were no grave computer threats because computers and the internet were still in the early stages of development, and security threats were easily identifiable. More often, threats came from malicious insiders who gained unauthorized access to sensitive documents and files. Although malware and network breaches existed during the early years, they did not use them for financial gain. By the second half of the 1970s, established computer firms like IBM started offering commercial access control systems and computer security software products.

One of the earliest examples of an attack on a computer network was the computer worm Creeper written by Bob Thomas at BBN, which propagated through the ARPANET in 1971. The program was purely experimental in nature and carried no malicious payload. A later program, Reaper, was created by Ray Tomlinson in 1972 and used to destroy Creeper.

Between September 1986 and June 1987, a group of German hackers performed the first documented case of cyber espionage. The group hacked into American defense contractors, universities, and military base networks and sold gathered information to the Soviet KGB. The group was led by Markus Hess, who was arrested on 29 June 1987. He was convicted of espionage (along with two co-conspirators) on 15 Feb 1990.

In 1988, one of the first computer worms, called the Morris worm, was distributed via the Internet. It gained significant mainstream media attention.

Netscape started developing the protocol SSL, shortly after the National Center for Supercomputing Applications (NCSA) launched Mosaic 1.0, the first web browser, in 1993. Netscape had SSL version 1.0 ready in 1994, but it was never released to the public due to many serious security vulnerabilities. However, in 1995, Netscape launched Version 2.0.

The National Security Agency (NSA) is responsible for the protection of U.S. information systems and also for collecting foreign intelligence. The agency analyzes commonly used software and system configurations to find security flaws, which it can use for offensive purposes against competitors of the United States.

NSA contractors created and sold *click-and-shoot* attack tools to US agencies and close allies, but eventually, the tools made their way to foreign adversaries. In 2016, NSAs own hacking tools were hacked, and Russia and North Korea have used it. NSA's employees and contractors have been recruited at high salaries by adversaries, anxious to compete in cyberwarfare. In 2007, the United States and Israel began exploiting security flaws in the Microsoft Windows operating system to attack and damage equipment used in Iran to refine nuclear materials. Iran responded by heavily investing in their own cyberwarfare capability, which it began using against the United States.


## Notable scholars

- Ross J. Anderson
- Annie Anton
- Adam Back
- Daniel J. Bernstein
- Matt Blaze
- Stefan Brands
- Josh Brunty
- L. Jean Camp
- Lorrie Cranor
- Dorothy E. Denning
- Peter J. Denning
- Cynthia Dwork
- Chuck Easttom
- Deborah Estrin
- Joan Feigenbaum
- Ian Goldberg
- Shafi Goldwasser
- Lawrence A. Gordon
- Peter Gutmann
- Paul Kocher
- Monica S. Lam
- Butler Lampson
- Brian LaMacchia
- Susan Landau
- Carl Landwehr
- Kevin Mitnick
- Peter G. Neumann
- Susan Nycum
- Paul C. van Oorschot
- Fred Piper
- Roger R. Schell
- Bruce Schneier
- Dawn Song
- Gene Spafford
- Salvatore J. Stolfo
- Willis Ware
- Moti Yung
