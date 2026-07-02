---
title: "Mobile security (part 2/2)"
source: https://en.wikipedia.org/wiki/Mobile_security
domain: mobile-app-security
license: CC-BY-SA-4.0
tags: mobile application security, mobile secure storage, app transport security, reverse engineering resistance
fetched: 2026-07-02
part: 2/2
---

## Malicious software (malware)

As smartphones are a permanent point of access to the Internet (they are often turned on), they can be compromised with malware as easily as computers. A malware is a computer program that aims to harm the system in which it resides.

Trojans, worms and viruses are all considered malware. A Trojan is a program on a device that allows external users to connect discreetly. A worm is a program that reproduces on multiple computers across a network. A virus is a malicious software designed to spread to other computers by inserting itself into legitimate programs and running programs in parallel.

Malware is far less numerous and serious to smartphones as it is to computers. Nonetheless, recent studies show that the evolution of malware in smartphones have rocketed in the last few years posing a threat to analysis and detection. In 2017, mobile malware variants increased by 54%.

### Problematic common apps and pre-installed software

Various common apps installed by millions can intrude on privacy, even if they were installed from a trusted software distribution service like the Google Play Store. For example, in 2022 it was shown that the popular app TikTok collects a lot of data and is required to make it available to the Chinese Communist Party (CCP) due to a national security law. This includes personal information on millions of Americans.

The firmware and "stock software" preinstalled on devices – and updated with preinstalled software – can also have undesired components or privacy-intruding default configurations or substantial security vulnerabilities. In 2019, Kryptowire identified Android devices with malicious firmware that collected and transmitted sensitive data without users' consent.

Analysis of data traffic by popular smartphones running variants of Android found substantial by-default data collection and sharing with no opt-out by pre-installed software. This issue also can't be addressed by conventional security patches. Outgoing Internet traffic can be analyzed with packet analyzers and with firewall apps like the NetGuard firewall app for Android that allows reading blocked traffic logs.

### Malware attacks

Typically, an attack on a smartphone made by malware takes place in three phases: the infection of a host, the accomplishment of its goal, and the spread of the malware to other systems. Malware often uses the resources offered by infected smartphones. It will use the output devices such as Bluetooth or infrared, but it may also use the address book or email address of the person to infect the user's acquaintances. The malware exploits the trust that is given to data sent by an acquaintance.

#### Infection

Infection is the method used by malware to gain access to the smartphone; it may exploit an internal vulnerability or rely on the gullibility of the user. Infections are classified into four classes according to their degree of user interaction:

1. Explicit permission – The most benign interaction is to ask the user if it is allowed to infect the machine, clearly indicating its potential malicious behavior. This is typical behavior of a proof of concept malware.
2. Implied permission – This infection is based on the fact that the user has a habit of installing software. Most Trojans try to seduce the user into installing attractive applications (like games or useful applications) that actually contain malware.
3. Common interaction – This infection is related to a common behavior, such as opening an MMS or email.
4. No interaction – The device is infected without the user taking action. This class of infection is the most dangerous, as it is both unapproved and automatic.

**Accomplishment of its goal**

Once the malware has infected a phone, it will also seek to accomplish its goal, which is usually one of the following:

- Monetary damages – The attacker can steal user data and either sell them to the same user or sell to a third party.
- Data or device damage – Malware can partially damage the device or delete or modify data on the device.
- Concealed damage – The two aforementioned types of damage are detectable, but the malware can also leave a backdoor for future attacks or even conduct wiretaps.

#### Spread to other systems

Once the malware has infected a smartphone, it aims to spread to a new host. This usually occurs to proximate devices via Wi-Fi, Bluetooth, or infrared; or to remote networks via telephone calls, SMS, or emails.

### Examples

#### Viruses and Trojans

- Cabir (also known as Caribe, SybmOS/Cabir, Symbian/Cabir, and EPOC.cabir) is the name of a computer worm developed in 2004, designed to infect mobile phones running Symbian OS. It is believed to have been the first computer worm able to infect mobile phones.
- Commwarrior, created on March 7, 2005, was the first worm able to infect many machines from MMS. It is sent as COMMWARRIOR.ZIP containing the file COMMWARRIOR.SIS. When this file is executed, Commwarrior attempts to connect to nearby devices by Bluetooth or infrared under a random name. It then attempts to send MMS message to the contacts in the smartphone with different header messages for each person, who receive the MMS and often open them without further verification.
- Phage was the first Palm OS virus discovered. It transfers to the Palm from a PC via synchronization. It infects all applications in the smartphone and embeds its own code to function without the user and the system detecting it. From the system's perspective, all the applications behave as expected.
- RedBrowser is a Trojan based on Java. The Trojan masquerades as a program called "RedBrowser" which allows the user to visit WAP sites without a WAP connection. During application installation, the user sees a request on their phone that the application needs permission to send messages. If the user accepts, RedBrowser can send SMS to paid call centers. This program uses the smartphone's connection to social networks (e.g., Facebook, Twitter) to get the contact information for the user's acquaintances (provided the required permissions have been given) and will send them messages.
- WinCE.PmCryptic.A is a malicious software on Windows Mobile which aims to earn money for its authors. It uses the infestation of memory cards that are inserted in the smartphone to spread more effectively.
- CardTrap is a virus that is available on different types of smartphones, which aims to deactivate the system and third-party applications. It works by replacing the files used to start the smartphone and applications to prevent them from executing. There are different variants of this virus such as Cardtrap.A for SymbOS devices. It also infects the memory card with malware capable of infecting Windows.
- Ghost Push is malicious software on Android OS which automatically roots the Android device and installs malicious applications directly to system partition. It then unroots the device to prevent users from removing the threat by master reset (the threat can be removed only by reflashing). It cripples the system resources, executes quickly, and is hard to detect.

#### Ransomware

Mobile ransomware is a type of malware that locks users out of their mobile devices in a pay-to-unlock-your-device ploy. It has significantly grown as a threat category since 2014. Mobile users are often less security-conscious – particularly as it pertains to scrutinizing applications and web links – and trust the mobile device's native protection capability.

Mobile ransomware poses a significant threat to businesses reliant on instant access and availability of their proprietary information and contacts. The likelihood of a traveling businessman paying a ransom to unlock their device is significantly higher since they are at a disadvantage given inconveniences such as timeliness and less direct access to IT staff. Recent ransomware attacks have caused many Internet-connected devices to not work and are costly for companies to recover from.

#### Spyware

- Pegasus – In 2021, journalists and researchers reported the discovery of spyware developed and distributed by a private company which can and has been used to infect both iOS and Android smartphones often – partly via use of 0-day exploits – without the need for any user-interaction or significant clues to the user. The spyware is then used to exfiltrate data, track user locations, capture film through its camera, and activate the microphone at any time.
- Flexispy is a Symbian application that can be considered a Trojan. The program sends all information received and sent from the smartphone to a Flexispy server. It was originally created to protect children and spy on adulterous spouses.

### Portability of malware across platforms

Attackers can make their malware target multiple platforms. Some malware attacks operating systems but is able to spread across different systems.

To begin with, malware can use runtime environments like Java virtual machine or the .NET Framework. They can also use other libraries present in many operating systems. Some malware carries several executable files in order to run in multiple environments, utilizing these during the propagation process. In practice, this type of malware requires a connection between the two operating systems to use as an attack vector. Memory cards can be used for this purpose, or synchronization software can be used to propagate the virus.

Mobile security is divided into different categories, as methods do not all act at the same level and are designed to prevent different threats. These methods range from the management of security by the operating system (protecting the system from corruption by an application) to the behavioral education of the user (preventing the installation of a suspicious software).

Among the mechanisms that handle device-access protection, some services or third-party tools can assist in unlocking or resetting locked devices after a factory reset or FRP (Factory Reset Protection).

### Security in operating systems

The first layer of security in a smartphone is the operating system. Beyond needing to handle the usual roles (e.g., resource management, scheduling processes) on the device, it must also establish the protocols for introducing external applications and data without introducing risk.

A central paradigm in mobile operating systems is the idea of a sandbox. Since smartphones are currently designed to accommodate many applications, they must have mechanisms to ensure these applications are safe for the phone itself, for other applications and data on the system, and for the user. If a malicious program reaches a mobile device, the vulnerable area presented by the system must be as small as possible. Sandboxing extends this idea to compartmentalize different processes, preventing them from interacting and damaging each other. Based on the history of operating systems, sandboxing has different implementations. For example, where iOS will focus on limiting access to its public API for applications from the App Store by default, Managed Open In allows you to restrict which apps can access which types of data. Android bases its sandboxing on its legacy of Linux and TrustedBSD.

The following points highlight mechanisms implemented in operating systems, especially Android.

**Rootkit detectors**

The intrusion of a

rootkit

in the system is a great danger in the same way as on a computer. It is important to prevent such intrusions, and to be able to detect them as often as possible. Indeed, there is concern that with this type of malicious program, an attacker could partially or completely bypass the device security, or acquire administrator rights. If this happens, nothing prevents the attacker from studying or disabling the safety features that were circumvented, deploying the applications they want, or disseminating a method of intrusion by a rootkit to a wider audience.

An example of a defense mechanism against this is the

chain of trust

(such as in iOS). This mechanism relies on signatures from applications required to start the operating system, and a certificate signed by the manufacturer (Apple). In the event that the signature checks are inconclusive, the device detects this and stops the boot-up.

If the operating system is compromised due to jailbreaking, rootkit detection may not work if it is disabled by the jailbreak method or software is loaded after jailbreak disables Rootkit Detection.

**Process isolation**

Android uses mechanisms of user process isolation inherited from Linux. Each application has a user associated with it, and a tuple (

UID

,

GID

). This approach serves as a sandbox: while applications can be malicious, they cannot get out of the sandbox reserved for them by their identifiers, and thus cannot interfere with the proper functioning of the system. For example, since it is impossible for a process to end the process of another user, an application can thus not stop the execution of another application.

**File permissions**

From the legacy of Linux,

filesystem permissions

mechanisms also help with sandboxing. Permissions prevent a process from editing any files it wants. It is therefore not possible to freely corrupt files necessary for the operation of another application or system. Furthermore, in Android there is the method of locking memory permissions. It is not possible to change the permissions of files installed on the SD card from the phone, and consequently it is impossible to install applications.

**Memory protection**

In the same way as on a computer, memory protection prevents

privilege escalation

. This could occur if a process managed to reach an area allocated to other processes, where it could write in the memory of a process with rights superior to its own (with 'root' in the worst case) and perform actions beyond its permissions. It would suffice to insert function calls are authorized by the privileges of the malicious application.

**Development through runtime environments**

Software is often developed in high-level languages, which can control what is being done by a running program. For example,

Java virtual machines

continuously monitor the actions of the execution threads they manage, monitor and assign resources, and prevent malicious actions. Buffer overflows can be prevented by these controls.

### Security software

Above the operating system security, there is a layer of security software. This layer is composed of individual components to strengthen various vulnerabilities: prevent malware, intrusions, the identification of a user as a human, and user authentication. It contains software components that have learned from their experience with computer security; however, on smartphones, this software must deal with greater constraints (see limitations).

**Antivirus and firewall**

An antivirus software can be deployed on a device to verify that it is not infected by a known threat, usually by signature detection software that detects malicious executable files. A mobile antivirus product would scan files and compare them against a database of known mobile malware code signatures.

A firewall, meanwhile, can watch over the existing traffic on the network and ensure that a malicious application does not seek to communicate through it. It may equally verify that an installed application does not seek to establish suspicious communication, which may prevent an intrusion attempt.

**Visual notifications**

In order to make the user aware of any abnormal actions, such as a call they did not initiate, one can link some functions to a visual notification that is impossible to circumvent. For example, when a call is triggered, the called number should always be displayed. Thus, if a call is triggered by a malicious application, the user can see, and take appropriate action.

**Turing test**

It is important to confirm certain actions by a user decision. The

Turing test

is used to distinguish between a human and a virtual user, often in the form of a

CAPTCHA

.

**Biometric identification**

Another method to use is

biometrics

,

a technique of identifying a person by means of their morphology (e.g., by

recognition of the face

or eye) or their behavior (e.g., their

signature or way of writing

). One advantage of using biometric security is that users can avoid having to remember a password or other secret combination to authenticate and prevent malicious users from accessing their devices. In a system with strong biometric security, only the primary user can access the smartphone.

### Resource monitoring in the smartphone

Should a malicious application pass the security barriers, it can take the actions for which it was designed. However, this activity can be sometimes detected by monitoring the various resources used on the phone. Depending on the goals of the malware, the consequences of infection are not always the same; all malicious applications are not intended to harm the devices on which they are deployed.

The following resources are only indications and do not provide certainty about the legitimacy of the activity of an application. However, these criteria can help target suspicious applications, especially if several criteria are combined.

**Battery**

Some malware is aimed at exhausting the energy resources of the phone. Monitoring the energy consumption of the phone can be a way to detect certain malware applications.

**Memory usage**

Memory usage is inherent in any application. However, if one finds that an unnecessary or unexpected proportion of memory is used by an application, it may be flagged as suspicious.

**Network traffic**

As part of normal operation on a smartphone, many applications are bound to connect via the network. However, an application using a lot of bandwidth can be strongly suspected of attempting to communicate a lot of information and disseminate data to many other devices. This observation only allows a suspicion, because some legitimate applications can be very resource-intensive in terms of network communications, the best example being

streaming video

.

**Services**

One can monitor the activity of various services of a smartphone. During certain moments, some services should not be active, and if one is detected, the application should be suspected. For example, the sending of an SMS when the user is filming video: this communication does not make sense and is suspicious; malware may attempt to send SMS while its activity is masked.

### Network surveillance

Network traffic exchanged by phones can be monitored. One can place safeguards in network routing points in order to detect abnormal behavior. As the mobile's use of network protocols is much more constrained than that of a computer, expected network data streams can be predicted (e.g., the protocol for sending an SMS), which permits detection of anomalies in mobile networks.

**Spam filters**

Similar to email exchanges,

spam

can be detected through means of mobile communications (SMS, MMS). It is therefore possible to detect and minimize this kind of attempt by filters deployed on network infrastructure that is relaying these messages.

**Encryption of stored or transmitted information**

Because it is always possible that data exchanged can be intercepted, communications and information storage rely on encryption to prevent a malicious entity from using any data obtained during communications. However, this poses the problem of key exchange for encryption algorithms, which requires a secure channel.

**Telecom network monitoring**

The networks for SMS and MMS exhibit predictable behavior, and there is not as much liberty compared with what one can do with protocols such as

TCP

or UDP. This implies that one cannot predict the flow of data from common web protocols; a protocol might generate very little traffic by consulting simple pages (rarely) or generate heavy traffic by using video streaming. On the other hand, messages exchanged via mobile phone have a framework and a specific model, and the user does not, in a normal case, have the freedom to intervene in the details of these communications. Therefore, if an abnormality is found in the flux of network data in the mobile networks, the potential threat can be quickly detected.

### Manufacturer surveillance

In the production and distribution chain for mobile devices, manufacturers are responsibility for ensuring that devices are delivered in a basic configuration without vulnerabilities. Most users are not experts and many of them are not aware of the existence of security vulnerabilities, so the device configuration as provided by manufacturers will be retained by many users. Some smartphone manufacturers add Titan M2s (a security hardware chip) to increase mobile security.

**Remove debug mode**

Phones are sometimes set in a debug mode during manufacturing, but this mode must be disabled before the phone is sold. This mode allows access to features not intended for routine use by a user. Due to the speed of development and production, distractions occur, and some devices are sold in debug mode. This kind of deployment exposes mobile devices to exploits that utilize this oversight.

**Default settings**

When a smartphone is sold, its default settings must be correct, and not leave security gaps. The default configuration is not always changed, so a good initial setup is essential for users. There are, for example, default configurations that are vulnerable to denial-of-service attacks.

**Security audit of apps**

App stores have emerged alongside smartphones. Both users and providers are tasked with examining the immense volume of apps available, from different points of view (e.g., security, content). Security audits should be particularly cautious, because if a fault is not detected, the application can spread very quickly within a few days, and infect a significant number of devices.

**Detect suspicious applications demanding rights**

When installing applications, it is good to warn the user against sets of permissions that, grouped together, seem potentially dangerous, or at least suspicious. Frameworks like such as Kirin, on Android, attempt to detect and prohibit certain sets of permissions.

**Revocation procedures**

First developed for Android, a process known as 'remote revocation' can remotely and globally uninstall an application from any device that has it. This means the spread of a malicious application that evaded security checks can be immediately stopped when the threat is discovered.

**Avoid heavily customized systems**

Manufacturers are tempted to overlay custom layers on existing operating systems, with the dual purpose of offering customized options and disabling or charging for certain features. This has the dual effect of risking the introduction of new bugs in the system, coupled with an incentive for users to modify the systems to circumvent the manufacturer's restrictions. These systems are rarely as stable and reliable as the original and may suffer from phishing attempts or other exploits.

**Improve software patch processes**

New versions of various software components of a smartphone, including operating systems, are regularly published. These 'patches' correct flaws over time. Nevertheless, manufacturers often do not deploy these updates to their devices in a timely fashion, and sometimes not at all. Thus, vulnerabilities can persist when they could be corrected; while they exist and are generally known, they are easily exploitable.

### User awareness

The user has a large responsibility in the cycle of security. This can be as simple as using a password, or as detailed as precisely controlling which permissions are granted to applications. This precaution is especially important if the user is an employee of a company who stores business data on the device.

Much malicious behavior is allowed by user carelessness. Smartphone users were found to ignore security messages during application installation, especially during application selection and checking application reputation, reviews, security, and agreement messages. A recent survey by internet security experts BullGuard showed a lack of insight concerning the rising number of malicious threats affecting mobile phones, with 53% of users claiming that they are unaware of security software for smartphones. A further 21% argued that such protection was unnecessary, and 42% admitted it hadn't crossed their mind ("Using APA," 2011). These statistics show that consumers are not concerned about security risks because they believe it is not a serious problem. However, in truth, smartphones are effectively handheld computers and are just as vulnerable.

The following are precautions that a user can take to manage security on a smartphone:

**Be skeptical**

A user should not believe everything that may be presented, as some information may be wrong, misleading, phishing, or attempting to distribute a malicious application. It is therefore advisable to check an application's reputation before buying or installing it.

**Permissions given to applications**

The mass distribution of applications necessitates different permissions mechanisms for each operating system. It is necessary to clarify these permissions mechanisms to users, as they differ between systems and can be confusing. In addition, it is rarely feasible (or possible) to modify large sets of permissions requested by an application. However, this can be a source of risk because a user can grant an application excessive rights beyond what is necessary. For example, a note-taking application does not require access to the geolocation service to function. During installation, the user must consider an application's privileges and should not accept the installation if the requested rights are inconsistent.

**Be careful**

A user's phone can be protected through simple gestures and precautions, such as locking the smartphone when it is not in use, not leaving the device unattended, not blindly trusting applications, not storing sensitive data, or encrypting sensitive data that cannot be separated from the device.

**Disconnect unused peripheral devices**

According to

NIST Guidelines for Managing the Security of Mobile Devices 2013

, it is recommended to "Restrict user and application access to hardware, such as the digital camera, GPS, Bluetooth interface, USB interface, and removable storage". This can include removing permissions and configurations for unused peripheral devices.

#### Enable Android Device Encryption

The latest Android

smartphones come with a built-in encryption setting for securing all the information saved on your device. This makes it difficult for a hacker to extract and decipher the information in case your device is compromised. It can be accessed via:

Settings → Security → Encrypt Phone + Encrypt SD Card.

**Ensure data**

Smartphones have significant memory capacity and can carry several gigabytes of data. The user must be careful about what data it carries and whether they should be protected (such as files containing bank information or business data). The user must have the prudence to avoid the transmission of sensitive data on a smartphone, which can be easily stolen. Furthermore, when a user gets rid of a device, they must be sure to remove all personal data first.

These precautions reduce the ability for people or malicious applications to exploit a user's smartphone. If users are careful, many attacks can be defeated, especially phishing and applications seeking only to obtain rights on a device.

### Centralized storage

One form of mobile protection allows companies to control the delivery and storage of text messages, by hosting the messages on a company server, rather than on the sender or receiver's phone. When certain conditions are met, such as an expiration date, the messages are deleted.

### Limitations

The security mechanisms mentioned in this article are to a large extent inherited from knowledge and experience with computer security. The elements composing the two device types are similar, and there are common measures that can be used, such as antivirus software and firewalls. However, the implementation of these solutions is not necessarily possible (or is at least highly constrained) within a mobile device. The reason for this difference is the technical resources available to computers and mobile devices: even though the computing power of smartphones is becoming faster, they have other limitations:

- **Single-task system** – Some operating systems, including some still commonly used, are single-tasking. Only the foreground task is executed. It is difficult to introduce applications such as antivirus and firewall on such systems, because they cannot perform their monitoring while the user is operating the device, when monitoring is most needed.
- **Energy autonomy** – A critical limitation for smartphones is energy autonomy. It is important that security mechanisms not consume too much battery resources, which could dramatically undermine the smartphone's autonomy and usage.
- **Network** – Directly related to battery life, network utilization should not be too high. From the point of view of energy consumption, network utilization is one of the most expensive resources. Nonetheless, some calculations may need to be relocated to remote servers in order to preserve the battery. This balance can make implementation of certain intensive computation mechanisms a delicate situation.

Furthermore, it is common that even if updates exist, or can be developed, they are not always deployed. For example, a user may not be aware of operating system updates; or a user may discover known vulnerabilities that are not corrected until the end of a long development cycle, which allows time to exploit the loopholes.

### Next generation of mobile security

The following mobile environments are expected to make up future security frameworks:

**Rich operating system**

This category will contain traditional mobile operating systems like Android, iOS, Symbian OS, or Windows Phone. They will provide the traditional functionality and security of an OS to the applications.

**Secure Operating System (Secure OS)**

This category features a secure kernel which will run in parallel with a fully featured Rich OS, on the same processor core. It will include drivers for the Rich OS ("normal world") to communicate with the secure kernel ("secure world"). The trusted infrastructure could include interfaces like the display or keypad to regions of PCI-E address space and memories.

**Trusted Execution Environment (TEE)**

This environment will be made up of hardware and software. It helps control of access rights and houses sensitive applications, which need to be isolated from the Rich OS. It effectively acts as a firewall between the "normal world" and "secure world".

**Secure Element (SE)**

The SE consists of tamper-resistant hardware and associated software or separate isolated hardware. It can provide high levels of security and work in tandem with the TEE. The SE will be mandatory for hosting proximity payment applications or official electronic signatures. SE may connect, disconnect, block peripheral devices, and operate separate set of hardware.

**Security Applications (SA)**

Numerous security applications are available on app stores, providing protection from viruses and performing vulnerability assessment.
