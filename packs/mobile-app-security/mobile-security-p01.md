---
title: "Mobile security (part 1/2)"
source: https://en.wikipedia.org/wiki/Mobile_security
domain: mobile-app-security
license: CC-BY-SA-4.0
tags: mobile application security, mobile secure storage, app transport security, reverse engineering resistance
fetched: 2026-07-02
part: 1/2
---

# Mobile security

**Mobile security**, or **mobile device security**, is the protection of smartphones, tablets, and laptops from threats associated with wireless computing. It has become increasingly important in mobile computing. The security of personal and business information now stored on smartphones is of particular concern.

Increasingly, users and businesses use smartphones not only to communicate, but also to plan and organize their work and private life. Within companies, these technologies are causing profound changes in the organization of information systems and have therefore become the source of new risks. Indeed, smartphones collect and compile an increasing amount of sensitive information to which access must be controlled to protect the privacy of the user and the intellectual property of the company.

The majority of attacks are aimed at smartphones. These attacks take advantage of vulnerabilities discovered in smartphones that can result from different modes of communication, including Short Message Service (SMS, text messaging), Multimedia Messaging Service (MMS), wireless connections, Bluetooth, and GSM, the de facto international standard for mobile communications. Smartphone operating systems or browsers are another weakness. Some malware makes use of the common user's limited knowledge. Only 2.1% of users reported having first-hand contact with mobile malware, according to a 2008 McAfee study, which found that 11.6% of users had heard of someone else being harmed by the problem. Yet, it is predicted that this number will rise. As of December 2023, there were about 5.4 million global mobile cyberattacks per month. This is a 147% increase from the previous year.

Security countermeasures are being developed and applied to smartphones, from security best practices in software to the dissemination of information to end users. Countermeasures can be implemented at all levels, including operating system development, software design, and user behavior modifications.


## Challenges of smartphone mobile security

### Threats

A smartphone user is exposed to various threats when they use their phone. In just the last two quarters of 2012, the number of unique mobile threats grew by 261%, according to ABI Research. These threats can disrupt the operation of the smartphone and transmit or modify user data. Applications must guarantee privacy and integrity of the information they handle. In addition, since some apps could themselves be malware, their functionality and activities should be limited (for example, restricting the apps from accessing location information via the Global Positioning System (GPS), blocking access to the user's address book, preventing the transmission of data on the network, or sending SMS messages that are billed to the user). Malicious apps can also be installed without the owners' permission or knowledge.

Vulnerability in mobile devices refers to aspects of system security that are susceptible to attacks. A vulnerability occurs when there is system weakness, an attacker has access to the weakness, and the attacker has competency to exploit the weakness.

Potential attackers began looking for vulnerabilities when Apple's iPhone and the first Android devices came onto the market. Since the introduction of apps (particularly mobile banking apps), which are vital targets for hackers, malware has been rampant. The Department of Homeland Security's cybersecurity department claims that the number of vulnerable points in smartphone operating systems has increased. As mobile phones are connected to utilities and appliances, hackers, cybercriminals, and even intelligence officials have access to these devices.

Starting in 2011, it became increasingly popular to let employees use their own devices for work-related purposes. The Crowd Research Partners study, published in 2017, reports that during 2017, most businesses that mandated the use of mobile devices were subjected to malware attacks and breaches. It has become common for rogue applications to be installed on user devices without the user's permission. They breach privacy, which hinders the effectiveness of the devices.

Since the recent rise of mobile attacks, hackers have increasingly targeted smartphones through credential theft and snooping. The number of attacks targeting smartphones and other devices has risen by 50 percent. According to the study, mobile banking applications are responsible for the increase in attacks.

Malware—such as ransomware, worms, botnets, Trojans, and viruses—have been developed to exploit vulnerabilities in mobile devices. Malware is distributed by attackers so they can gain access to private information or digitally harm a user. For example, should malware breach a user's banking service, it may be able to access their transaction information, their rights to log in, and their money. Some malware is developed with anti-detection techniques to avoid detection. Attackers who use malware can avoid detection by hiding malicious code.

Trojan-droppers can also avoid detection of malware. Despite the fact that the malware inside a device does not change, the dropper generates new hashes each time. Additionally, droppers can also create a multitude of files, which can lead to the creation of viruses. Android mobile devices are prone to Trojan-droppers. The banking Trojans also enable attacks on the banking applications on the phone, which leads to the theft of data for use in stealing money and funds.

Jailbreaks for iOS devices work by disabling the signing of codes on iPhones so that applications not downloaded from the App Store can be operated. In this way, all the protection layers offered by iOS are disrupted, exposing the device to malware. These outside applications don't run in a sandbox, which exposes potential security problems. Some attack vectors change the mobile devices' configuration settings by installing malicious credentials and virtual private networks (VPNs) to direct information to malicious systems. In addition, spyware can be installed on mobile devices in order to track an individual.

Triade malware comes pre-installed on some mobile devices. In addition to Haddad, there is Lotoor, which exploits vulnerabilities in the system to repackage legitimate applications. The devices are also vulnerable due to spyware and leaky behaviors through applications. Mobile devices are also effective conveyance systems for malware threats, breaches of information, and thefts.

Wi-Fi interference technologies can also attack mobile devices through potentially insecure networks. By compromising the network, hackers are able to gain access to key data. Devices connected to public networks are at risk of attacks. A VPN, on the other hand, can be used to secure networks. As soon as a system is threatened, an active VPN will operate. There are also social engineering techniques, such as phishing, in which unsuspecting victims are sent links to lead them to malicious websites. The attackers can then hack into the victim's device and copy all of its information.

Some mobile device attacks can be prevented. For example, containerization allows the creation of a hardware infrastructure that separates business data from other data. Additionally, network protection detects malicious traffic and rogue access points. Data security is also ensured through authentication.

There are a number of threats to mobile devices, including annoyance, stealing money, invading privacy, propagation, and malicious tools. There are three prime targets for attackers:

1. Data – Smartphones are devices for data management and may contain sensitive data like credit card numbers, authentication information, private information, activity logs (calendar, call logs).
2. Identity – Smartphones are highly customizable, so the device or its contents can easily be associated with a specific person.
3. Availability – Attacking a smartphone can limit or deprive a user's access to it.

Attacks on mobile security systems include:

- Botnets – Attackers infect multiple machines with malware that victims generally acquire via e-mail attachments or from compromised applications or websites. The malware then gives hackers remote control of "zombie" devices, which can then be instructed to perform harmful acts.
- Malicious applications – Hackers upload malicious programs or games to third-party smartphone application marketplaces. The programs steal personal information and open backdoor communication channels to install additional applications and cause other problems.
- Malicious links on social networks – An effective way to spread malware where hackers can place Trojans, spyware, and backdoors.
- Spyware – Hackers use this to hijack phones, allowing them to hear calls, see text messages and e-mails, and track a user's location through GPS updates.

The source of these attacks are the same actors found in the non-mobile computing space:

- Professionals, whether commercial or military, who focus on the three targets mentioned above. They steal sensitive data from the general public, as well as undertake industrial espionage. They will also use the identity of those attacked to achieve other attacks.
- Thieves who want to gain income through data or identities they have stolen. The thieves will attack many people to increase their potential income.
- Black hat hackers who specifically attack availability. Their goal is to develop viruses, and cause damage to the device. In some cases, hackers have an interest in stealing data on devices.
- Grey hat hackers who reveal vulnerabilities. Their goal is to expose vulnerabilities of the device. Grey hat hackers do not intend on damaging the device or stealing data.

### Consequences

When a smartphone is infected by an attacker, the attacker can attempt several things:

- The attacker can manipulate the smartphone as a zombie machine: a machine with which the attacker can communicate and send commands which will be used to send unsolicited messages (spam) via SMS or email.
- The attacker can easily force the smartphone to make phone calls. For example, one can use the API (library that contains the basic functions not present in the smartphone) PhoneMakeCall by Microsoft, which collects telephone numbers from any source (such as yellow pages) and then calls them. The attacker can use this method to call paid services, resulting in charges to the smartphone owner. Dangerously, the smartphone could call and disrupt emergency services.
- A compromised smartphone can record conversations between the user and others and send them to a third party. This can cause user privacy and industrial security problems.
- An attacker can also steal a user's identity, usurp their identity (with a copy of the user's SIM card or even the telephone itself), and thus impersonate the owner. This raises security concerns in countries where smartphones can be used to place orders, view bank accounts, or are used as an identity card.
- The attacker can reduce the usability of the smartphone, by discharging the battery. For example, they can launch an application that will run continuously on the smartphone processor, requiring a lot of energy and draining the battery. Frank Stajano and Ross Anderson first described this form of attack, calling it an attack of "battery exhaustion" or "sleep deprivation torture".
- The attacker can make the smartphone unusable. This attack can delete the boot scripts, resulting in a phone without a functioning operating system; modify certain files to make it unusable, such as a script that launches at startup that forces the smartphone to restart; or embed a startup application that will empty the battery.
- The attacker can remove the user's data, whether personal (photos, music, videos) or professional (contacts, calendars, notes).


## Attacks based on communication

### Attacks based on SMS and MMS

Some attacks derive from flaws in the management of Short Message Service (SMS) and Multimedia Messaging Service (MMS).

Some mobile phone models have problems in managing binary SMS messages. By sending an ill-formed block, it is possible to cause the phone to restart, leading to the denial-of-service attacks. If a user with a Siemens S55 received a text message containing a Chinese character, it would lead to a denial of service. In another case, while the standard requires that the maximum size of a Nokia Mail address is 32 characters, some Nokia phones did not verify this standard, so if a user enters an email address over 32 characters, that leads to complete dysfunction of the e-mail handler and puts it out of commission. This attack is called "curse of silence". A study on the safety of the SMS infrastructure revealed that SMS messages sent from the Internet can be used to perform a distributed denial of service (DDoS) attack against the mobile telecommunications infrastructure of a big city. The attack exploits the delays in the delivery of messages to overload the network.

Another potential attack could begin with a phone that sends an MMS to other phones, with an attachment. This attachment is infected with a virus. Upon receipt of the MMS, the user can choose to open the attachment. If it is opened, the phone is infected, and the virus sends an MMS with an infected attachment to all the contacts in the address book. There is a real-world example of this attack: the virus Commwarrior sends MMS messages (including an infected file) to all recipients in a mobile phone's address book. If a recipient installs the infected file, the virus repeats, sending messages to recipients taken from the new address book.

### Attacks based on communication networks

#### GSM networks

The attacker may try to break the encryption of a GSM mobile network. The network encryption algorithms belong to the family of algorithms called A5. Due to the policy of security through obscurity, it has not been possible to openly test the robustness of these algorithms. There were originally two variants of the algorithm: A5/1 and A5/2 (stream ciphers), where the former was designed to be relatively strong, and the latter was purposely designed to be weak to allow easy cryptanalysis and eavesdropping. ETSI forced some countries (typically outside Europe) to use A5/2. Since the encryption algorithm was made public, it was proved to be breakable: A5/2 could be broken on the fly, and A5/1 in about 6 hours. In July 2007, the 3GPP approved a change request to prohibit the implementation of A5/2 in any new mobile phones, decommissioning the algorithm; it is no longer implemented in mobile phones.

Stronger public algorithms have been added to the GSM standard: the A5/3 and A5/4 (Block ciphers), otherwise known as KASUMI or UEA1 published by ETSI. If the network does not support A5/1, or any other A5 algorithm implemented by the phone, then the base station can specify A5/0 which is the null algorithm, whereby the radio traffic is sent unencrypted. Even if mobile phones are able to use 3G or 4G (which have much stronger encryption than 2G GSM), the base station can downgrade the radio communication to 2G GSM and specify A5/0 (no encryption). This is the basis for eavesdropping attacks on mobile radio networks using a fake base station commonly called an IMSI catcher.

In addition, tracing of mobile terminals is difficult since each time the mobile terminal is accessing or being accessed by the network, a new temporary identity (TMSI) is allocated to the mobile terminal. The TMSI is used as the identity of the mobile terminal the next time it accesses the network. The TMSI is sent to the mobile terminal in encrypted messages.

Once the encryption algorithm of GSM is broken, the attacker can intercept all unencrypted communications made by the victim's smartphone.

#### Wi-Fi

An attacker can try to eavesdrop on Wi-Fi communications to derive information (e.g., username, password). This type of attack is not unique to smartphones, but they are very vulnerable to these attacks because often Wi-Fi is their only means of communication and access the internet. The security of wireless networks (WLAN) is thus an important subject.

Initially, wireless networks were secured by WEP keys. The weakness of WEP is its short encryption key, which is the same for all connected clients. In addition, several reductions in the search space of the keys have been found by researchers. Now, most wireless networks are protected by the WPA security protocol. WPA is based on the Temporal Key Integrity Protocol (TKIP), which was designed to allow migration from WEP to WPA on the equipment already deployed. The major improvements in security are the dynamic encryption keys. For small networks, the WPA uses a "pre-shared key" which is based on a shared key. Encryption can be vulnerable if the length of the shared key is short. With limited opportunities for input (i.e., only the numeric keypad), mobile phone users might define short encryption keys that contain only numbers. This increases the likelihood that an attacker succeeds with a brute-force attack. The successor to WPA, called WPA2, is supposed to be safe enough to withstand a brute force attack.

The ability to access free and fast Wi-Fi gives a business an edge over those who do not. Free Wi-Fi is usually provided by organizations such as airports, coffee shops, and restaurants for a number of reasons, including encouraging customers to spend more time and money on the premises, and helping users stay productive. Another reason is enhancing customer tracking: many restaurants and coffee shops compile data about their customers so they can target advertisements directly to their devices. This means that customers know what services the facility provides. Generally, individuals filter business premises based on Internet connections as another reason to gain a competitive edge. Network security is the responsibility of the organizations, as unsecured Wi-Fi networks are prone to numerous risks. The man-in-the-middle attack entails the interception and modification of data between parties. Additionally, malware can be distributed via the free Wi-Fi network and hackers can exploit software vulnerabilities to smuggle malware onto connected devices. It is also possible to eavesdrop and sniff Wi-Fi signals using special software and devices, capturing login credentials and hijacking accounts.

As with GSM, if the attacker succeeds in breaking the identification key, both the phone and the entire network it is connected to become exposed to attacks.

Many smartphones remember wireless LANs they have previously connected to, allowing users to not have to re-identify with each connection. However, an attacker could create a Wi-Fi access point twin with the same parameters and characteristics as a real network. By automatically connecting to the fraudulent network, a smartphone becomes susceptible to the attacker, who can intercept any unencrypted data.

Lasco is a worm that initially infects a remote device using the SIS file format, a type of script file that can be executed by the system without user interaction. The smartphone thus believes the file to come from a trusted source and downloads it, infecting the machine.

#### Bluetooth

Security issues related to Bluetooth on mobile devices have been studied and have shown numerous problems on different phones. One easy to exploit vulnerability is that unregistered services do not require authentication, and vulnerable applications have a virtual serial port used to control the phone. An attacker only needed to connect to the port to take full control of the device.

In another example, an attacker sends a file via Bluetooth to a phone within range with Bluetooth in discovery mode. If the recipient accepts, a virus is transmitted. An example of this is a worm called Cabir. The worm searches for nearby phones with Bluetooth in discoverable mode and sends itself to the target device. The user must accept the incoming file and install the program, after which the worm infects the machine.


## Attacks based on vulnerabilities in software applications

Other attacks are based on flaws in the OS or applications on the phone.

### Web browser

The mobile web browser is an emerging attack vector for mobile devices. Just as common Web browsers, mobile web browsers are extended from pure web navigation with widgets and plug-ins or are completely native mobile browsers.

Jailbreaking the iPhone with firmware 1.1.1 was based entirely on vulnerabilities on the web browser. In this case, there was a vulnerability based on a stack-based buffer overflow in a library used by the web browser (LibTIFF). A similar vulnerability in the web browser for Android was discovered in October 2008. Like the iPhone vulnerability, it was due to an obsolete and vulnerable library, but significantly differed in that Android's sandboxing architecture limited the effects of this vulnerability to the Web browser process.

Smartphones are also susceptible to traditional forms of web-based attacks, including phishing, malicious websites, and background-running malware. Unlike computers, however, robust antivirus solutions for smartphones are not yet widely available.

Industry mobile security research also highlights rising risks from application reverse engineering, runtime tampering, and API exploitation in mobile apps.

The Internet offers numerous interactive features that ensure a higher engagement rate, capture more and relevant data, and increase brand loyalty. Blogs, forums, social networks, and wikis are some of the most common interactive websites. Due to the tremendous growth of the Internet, there has been a rapid rise in the number of security breaches experienced by individuals and businesses.

Mobile browser users can balance usage and caution in several ways, such as reviewing computer security regularly, using secure and secret passwords, and correcting, upgrading, and replacing the necessary features. Installation of antivirus and anti-spyware programs is the most effective way of protecting the computer, as they offer protection against malware, spyware, and viruses. Additionally, they use firewalls, which are typically installed between trusted networks or devices and the Internet. By acting as a web server, the firewall prevents external users from accessing the internal computer system.

### Operating system

Sometimes it is possible to overcome the security safeguards by modifying the operating system (OS) itself, such as the manipulation of firmware and malicious signature certificates. These attacks are difficult.

In 2004, vulnerabilities in virtual machines running on certain devices were revealed. It was possible to bypass the bytecode verifier and access the native underlying operating system. The results of this research were not published in detail. The firmware security of Nokia's Symbian Platform Security Architecture (PSA) is based on a central configuration file called SWIPolicy. In 2008, it was possible to manipulate the Nokia firmware before it was installed. In fact, some downloadable versions of this file were human-readable, so it was possible to modify and change the image of the firmware. This vulnerability was solved by an update from Nokia.

In theory, smartphones have an advantage over hard drives since the OS files are in read-only memory (ROM) and cannot be changed by malware. However, in some systems it was possible to circumvent this: in the Symbian OS, it was possible to overwrite a file with a file of the same name. On the Windows OS, it was possible to change a pointer from a general configuration file to an editable file.

When an application is installed, the signing of this application is verified by a series of certificates. One can create a valid signature without using a valid certificate and add it to the list. In the Symbian OS, all certificates are in the directory `c:\resource\swicertstore\dat`. With firmware changes explained above, it is very easy to insert a seemingly valid but malicious certificate.

Android is the OS that has been attacked the most, because it has the largest userbase. A cybersecurity company reported to have blocked about 18 million attacks in 2016.


## Attacks based on hardware vulnerabilities

### Electromagnetic waveforms

In 2015, researchers at the French government agency *Agence nationale de la sécurité des systèmes d'information* (ANSSI, lit. 'French National Agency for the Security of Information Systems') demonstrated the capability to trigger the voice interface of certain smartphones remotely by using "specific electromagnetic waveforms". The exploit took advantage of antenna-properties of headphone wires while plugged into the audio-output jacks of the vulnerable smartphones and effectively spoofed audio input to inject commands via the audio interface.

### Juice jacking

Juice jacking is a physical or hardware vulnerability specific to mobile platforms. Utilizing the dual purpose of the USB charge port, many devices have been susceptible to having data exfiltrated from, or malware installed onto, a mobile device by utilizing malicious charging kiosks set up in public places or hidden in normal charge adapters.

### Jailbreaking and rooting

Jailbreaking is also a physical access vulnerability, in which a mobile device user hacks into device to unlock it, exploiting weaknesses in the operating system. Mobile device users take control of their own device by jailbreaking it, allowing them to customize the interface by installing applications, change system settings that are not allowed on the devices, tweak OS processes, and run uncertified programs. This openness exposes the device to a variety of malicious attacks which can compromise private data.


## Password cracking

In 2010, researchers from the University of Pennsylvania investigated the possibility of cracking a device's password through a smudge attack (literally imaging the finger smudges on the screen to discern the user's password). The researchers were able to discern the device password up to 68% of the time under certain conditions. Outsiders may perform over-the-shoulder surveillance on victims, such as watching specific keystrokes or pattern gestures, to unlock device password or passcode.
