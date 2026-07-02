---
title: "Android (operating system) (part 2/3)"
source: https://en.wikipedia.org/wiki/Android_(operating_system)
domain: board-support-package
license: CC-BY-SA-4.0
tags: board support package, embedded systems
fetched: 2026-07-02
part: 2/3
---

## Development

Android is developed by Google until the latest changes and updates are ready to be released, at which point the source code is made available to the Android Open Source Project (AOSP), an open source initiative led by Google. The first source code release happened as part of the initial release in 2007. All releases are under the Apache License.

The AOSP code can be found with minimal modifications on select devices, mainly the former Nexus and current Android One series of devices. However, most original equipment manufacturers (OEMs) customize the source code to run on their hardware.

Android's source code does not contain the device drivers, often proprietary, that are needed for certain hardware components, and does not contain the source code of Google Play Services, which many apps depend on. As a result, most Android devices, including Google's own, ship with a combination of free and open source and proprietary software, with the software required for accessing Google services falling into the latter category. In response to this, there are some projects that build complete operating systems based on AOSP as free software, the first being CyanogenMod (see section Open-source community below).

### Update schedule

| Version | Release date |
|---|---|
| 1.0 | September 23, 2008 |
| 1.1 | February 9, 2009 |
| 1.5 (Cupcake) | April 27, 2009 |
| 1.6 (Donut) | September 15, 2009 |
| 2.0–2.1 (Eclair) | October 26, 2009 |
| 2.2 (Froyo) | May 20, 2010 |
| 2.3 (Gingerbread) | December 6, 2010 |
| 3.0 (Honeycomb) | February 22, 2011 |
| 4.0 (Ice Cream Sandwich) | October 18, 2011 |
| 4.1–4.3 (Jelly Bean) | July 9, 2012 |
| 4.4 (KitKat) | October 31, 2013 |
| 5.0–5.1 (Lollipop) | November 12, 2014 |
| 6.0 (Marshmallow) | October 5, 2015 |
| 7.0–7.1 (Nougat) | August 22, 2016 |
| 8.0–8.1 (Oreo) | August 21, 2017 |
| 9 (Pie) | August 6, 2018 |
| 10 | September 3, 2019 |
| 11 | September 8, 2020 |
| 12–12L | October 4, 2021 |
| 13 | August 15, 2022 |
| 14 | October 4, 2023 |
| 15 | October 15, 2024 |
| 16 | June 10, 2025 |
| 17 | June 16, 2026 |

Google provides annual Android releases, both for factory installation in new devices, and for over-the-air updates to existing devices. The latest major release is Android 17.

The extensive variation of hardware in Android devices has caused significant delays for software upgrades and security patches. Each upgrade has had to be specifically tailored, a time- and resource-consuming process. Except for devices within the Google Nexus and Pixel brands, updates have often arrived months after the release of the new version, or not at all. Manufacturers often prioritize their newest devices and leave old ones behind. Additional delays can be introduced by wireless carriers who, after receiving updates from manufacturers, further customize Android to their needs and conduct extensive testing on their networks before sending out the upgrade. There are also situations in which upgrades are impossible due to a manufacturer not updating necessary drivers.

The lack of after-sale support from manufacturers and carriers has been widely criticized by consumer groups and the technology media. Some commentators have noted that the industry has a financial incentive not to upgrade their devices, as the lack of updates for existing devices fuels the purchase of newer ones, an attitude described as "insulting". *The Guardian* complained that the method of distribution for updates is complicated only because manufacturers and carriers have designed it that way. In 2011, Google partnered with a number of industry players to announce an "Android Update Alliance", pledging to deliver timely updates for every device for 18 months after its release; however, there has not been another official word about that alliance since its announcement.

In 2012, Google began de-coupling certain aspects of the operating system (particularly its central applications) so they could be updated through the Google Play store independently of the OS. One of those components, Google Play Services, is a closed-source system-level process providing APIs for Google services, installed automatically on nearly all devices running Android 2.2 "Froyo" and higher. With these changes, Google can add new system functions and update apps without having to distribute an upgrade to the operating system itself. As a result, Android 4.2 and 4.3 "Jelly Bean" contained relatively fewer user-facing changes, focusing more on minor changes and platform improvements.

HTC's then-executive Jason Mackenzie called monthly security updates "unrealistic" in 2015, and Google was trying to persuade carriers to exclude security patches from the full testing procedures. In May 2016, Bloomberg Businessweek reported that Google was making efforts to keep Android more up-to-date, including accelerated rates of security updates, rolling out technological workarounds, reducing requirements for phone testing, and ranking phone makers in an attempt to "shame" them into better behavior. As stated by *Bloomberg*: "As smartphones get more capable, complex and hackable, having the latest software work closely with the hardware is increasingly important". Hiroshi Lockheimer, the Android lead, admitted that "It's not an ideal situation", further commenting that the lack of updates is "the weakest link on security on Android". Wireless carriers were described in the report as the "most challenging discussions", due to their slow approval time while testing on their networks, despite some carriers, including Verizon Wireless and Sprint Corporation, already shortening their approval times. In a further effort for persuasion, Google shared a list of top phone makers measured by updated devices with its Android partners, and is considering making the list public. Mike Chan, co-founder of phone maker Nextbit and former Android developer, said that "The best way to solve this problem is a massive re-architecture of the operating system", "or Google could invest in training manufacturers and carriers 'to be good Android citizens'".

In May 2017, with the announcement of Android 8.0, Google introduced Project Treble, a major re-architect of the Android OS framework designed to make it easier, faster, and less costly for manufacturers to update devices to newer versions of Android. Project Treble separates the vendor implementation (device-specific, lower-level software written by silicon manufacturers) from the Android OS framework via a new "vendor interface". In Android 7.0 and earlier, no formal vendor interface exists, so device makers must update large portions of the Android code to move a device to a newer version of the operating system. With Treble, the new stable vendor interface provides access to the hardware-specific parts of Android, enabling device makers to deliver new Android releases simply by updating the Android OS framework, "without any additional work required from the silicon manufacturers."

In September 2017, Google's Project Treble team revealed that, as part of their efforts to improve the security lifecycle of Android devices, Google had managed to get the Linux Foundation to agree to extend the support lifecycle of the Linux Long-Term Support (LTS) kernel branch from the 2 years that it has historically lasted to 6 years for future versions of the LTS kernel, starting with Linux kernel 4.4.

In May 2019, with the announcement of Android 10, Google introduced Project Mainline to simplify and expedite delivery of updates to the Android ecosystem. Project Mainline enables updates to core OS components through the Google Play Store. As a result, important security and performance improvements that previously needed to be part of full OS updates can be downloaded and installed as easily as an app update.

Google reported rolling out new amendments in Android 12 aimed at making the use of third-party application stores easier. This announcement rectified the concerns reported regarding the development of Android apps, including a fight over an alternative in-app payment system and difficulties faced by businesses moving online because of COVID-19.

### Linux kernel

Android's kernel is based on the Linux kernel's long-term support (LTS) branches. As of 2024, Android (14) uses versions 6.1 or 5.15 (for "Feature kernels", can be older for "Launch kernels", e.g. android12-5.10, android11-5.4, depending on Android version down to e.g. android11-5.4, android-4.14-stable, android-4.9-q), and older Android versions, use version 5.15 or a number of older kernels. The actual kernel depends on the individual device.

Android's variant of the Linux kernel has further architectural changes that are implemented by Google outside the typical Linux kernel development cycle, such as the inclusion of components like device trees, ashmem, ION, and different out of memory (OOM) handling. Certain features that Google contributed back to the Linux kernel, notably a power management feature called "wakelocks", were initially rejected by mainline kernel developers partly because they felt that Google did not show any intent to maintain its own code. Google announced in April 2010 that they would hire two employees to work with the Linux kernel community, but Greg Kroah-Hartman, the current Linux kernel maintainer for the stable branch, said in December 2010 that he was concerned that Google was no longer trying to get their code changes included in mainstream Linux. Google engineer Patrick Brady once stated in the company's developer conference that "Android is not Linux", with *Computerworld* adding that "Let me make it simple for you, without Linux, there is no Android". *Ars Technica* wrote that "Although Android is built on top of the Linux kernel, the platform has very little in common with the conventional desktop Linux stack".

In August 2011, Linus Torvalds said that "eventually Android and Linux would come back to a common kernel, but it will probably not be for four to five years". In December 2011, Greg Kroah-Hartman announced the start of Android Mainlining Project, which aims to put some Android drivers, patches and features back into the Linux kernel, starting in Linux 3.3. Linux included the autosleep and wakelocks capabilities in the 3.5 kernel, after many previous attempts at a merger. The interfaces are the same but the upstream Linux implementation allows for two different suspend modes: to memory (the traditional suspend that Android uses), and to disk (hibernate, as it is known on the desktop). Google maintains a public code repository that contains their experimental work to re-base Android off the latest stable Linux versions.

Android is a Linux distribution according to the Linux Foundation, Google's open-source chief Chris DiBona, and several journalists. Others, such as Google engineer Patrick Brady, say that Android is not Linux in the traditional Unix-like Linux distribution sense; Android does not include the GNU C Library (it uses Bionic as an alternative C library) and some other components typically found in Linux distributions.

With the release of Android Oreo in 2017, Google began to require that devices shipped with new SoCs had Linux kernel version 4.4 or newer, for security reasons. Existing devices upgraded to Oreo, and new products launched with older SoCs, were exempt from this rule.

### Rooting

The flash storage on Android devices is split into several partitions, such as `/system/` for the operating system itself, and `/data/` for user data and application installations.

In contrast to typical desktop Linux distributions, Android device owners are not given root access to the operating system and sensitive partitions such as `/system/` are partially read-only. However, root access can be obtained by exploiting security flaws in Android, which is used frequently by the open-source community to enhance the capabilities and customizability of their devices, but also by malicious parties to install viruses and malware. Root access can also be obtained by unlocking the bootloader which is available on most Android devices, for example on most Google Pixel, OnePlus and Nothing models `OEM Unlocking` option in the developer settings allows the user to unlock the bootloader with Fastboot, afterward, custom software may be installed. Some OEMs have their own methods. The unlocking process resets the system to factory state, erasing all user data. Proprietary frameworks like Samsung Knox limit or block attempts at rooting. Google's Play Integrity API allows developers to check for any signs of tampering, although the fairness of the tests have been criticized.

### Software stack

On top of the Linux kernel, there are the middleware, libraries and APIs written in C, and application software running on an application framework which includes Java-compatible libraries. Development of the Linux kernel continues independently of Android's other source code projects.

Android uses Android Runtime (ART) as its runtime environment (introduced in version 4.4), which uses ahead-of-time (AOT) compilation to entirely compile the application bytecode into machine code upon the installation of an application. In Android 4.4, ART was an experimental feature and not enabled by default; it became the only runtime option in the next major version of Android, 5.0. In versions no longer supported, until version 5.0 when ART took over, Android previously used Dalvik as a process virtual machine with trace-based just-in-time (JIT) compilation to run Dalvik "dex-code" (Dalvik Executable), which is usually translated from the Java bytecode. Following the trace-based JIT principle, in addition to interpreting the majority of application code, Dalvik performs the compilation and native execution of select frequently executed code segments ("traces") each time an application is launched. For its Java library, the Android platform uses a subset of the now discontinued Apache Harmony project. In December 2015, Google announced that the next version of Android would switch to a Java implementation based on the OpenJDK project.

Android's standard C library, Bionic, was developed by Google specifically for Android, as a derivation of the BSD's standard C library code. Bionic itself has been designed with several major features specific to the Linux kernel. The main benefits of using Bionic instead of the GNU C Library (glibc) or uClibc are its smaller runtime footprint, and optimization for low-frequency CPUs. At the same time, Bionic is licensed under the terms of the BSD licence, which Google finds more suitable for the Android's overall licensing model.

Aiming for a different licensing model, toward the end of 2012, Google switched the Bluetooth stack in Android from the GPL-licensed BlueZ to the Apache-licensed BlueDroid. A new Bluetooth stack, called Gabeldorsche, was developed to try to fix the bugs in the BlueDroid implementation.

Android does not have a native X Window System by default, nor does it support the full set of standard GNU libraries. This made it difficult to port existing Linux applications or libraries to Android, until version r5 of the Android Native Development Kit brought support for applications written completely in C or C++. Libraries written in C may also be used in applications by injection of a small shim and usage of the JNI.

In current versions of Android, "Toybox", a collection of command-line utilities (mostly for use by apps, as Android does not provide a command-line interface by default), is used (since the release of Marshmallow) replacing a similar "Toolbox" collection found in previous Android versions.

Android has another operating system, Trusty OS, within it, as a part of "Trusty" "software components supporting a Trusted Execution Environment (TEE) on mobile devices." "Trusty and the Trusty API are subject to change. [..] Applications for the Trusty OS can be written in C/C++ (C++ support is limited), and they have access to a small C library. [..] All Trusty applications are single-threaded; multithreading in Trusty userspace currently is unsupported. [..] Third-party application development is not supported in" the current version, and software running on the OS and processor for it, run the "DRM framework for protected content. [..] There are many other uses for a TEE such as mobile payments, secure banking, full-disk encryption, multi-factor authentication, device reset protection, replay-protected persistent storage, wireless display ("cast") of protected content, secure PIN and fingerprint processing, and even malware detection."

### Open-source community

Android's source code is released by Google under an open-source license, and its open nature has encouraged a large community of developers and enthusiasts to use the open-source code as a foundation for community-driven projects, which deliver updates to older devices, add new features for advanced users or bring Android to devices originally shipped with other operating systems. These community-developed releases often bring new features and updates to devices faster than through the official manufacturer/carrier channels, with a comparable level of quality; provide continued support for older devices that no longer receive official updates; or bring Android to devices that were officially released running other operating systems, such as the HP TouchPad. Community releases often come pre-rooted and contain modifications not provided by the original vendor, such as the ability to overclock or over/undervolt the device's processor, or security enhancements beyond what is included in the stock OS.

CyanogenMod was the most widely used community firmware; after its abrupt discontinuation in 2016, a community fork known as LineageOS was established as a spiritual continuation of the project.

Historically, device manufacturers and mobile carriers have typically been unsupportive of third-party firmware development. Manufacturers express concern about improper functioning of devices running unofficial software and the support costs resulting from this. Moreover, modified firmware such as CyanogenMod sometimes offer features, such as tethering, for which carriers would otherwise charge a premium. As a result, technical obstacles including locked bootloaders and restricted access to root permissions are common in many devices. However, as community-developed software has grown more popular, and following a statement by the Librarian of Congress in the United States that permits the "jailbreaking" of mobile devices, manufacturers and carriers have softened their position regarding third party development, with some, including HTC, Motorola, Samsung and Sony, providing support and encouraging development. As a result of this, over time the need to circumvent hardware restrictions to install unofficial firmware has lessened as an increasing number of devices are shipped with unlocked or unlockable bootloaders, similar to Nexus series of phones, although usually requiring that users waive their devices' warranties to do so. However, despite manufacturer acceptance, some carriers in the US still require that phones are locked down.

Android was also ported by the community to Apple's iPhone, iPad and iPod touch devices as a consequence of porting the Linux kernel on Apple devices. In 2010, OpeniBoot and subsequently iDroid were released to allow dual booting iOS and Android 2.3.3 'Gingerbread' on jailbroken iPhone or iPod Touch devices, which was ultimately declared as discontinued in 2012. In 2020, David Wang under his company Corellium released Project Sandcastle which made Android run on the iPhone 7.

### Device codenames

Internally, Android identifies each supported device by its **device codename**, a short string, which may or may not be similar to the model name used in marketing the device. For example, the device codename of the Pixel smartphone is *sailfish*.

The device codename is usually not visible to the end user, but is important for determining compatibility with modified Android versions. It is sometimes also mentioned in articles discussing a device, because it allows to distinguish different hardware variants of a device, even if the manufacturer offers them under the same name. The device codename is available to running applications under `android.os.Build.DEVICE`.


## Security and privacy

In 2020, Google launched the Android Partner Vulnerability Initiative to improve the security of Android. They also formed an Android security team.

### Common security threats

Research from security company Trend Micro lists premium service abuse as the most common type of Android malware, where text messages are sent from infected phones to premium-rate telephone numbers without the consent or even knowledge of the user. Other malware displays unwanted and intrusive advertisements on the device, or sends personal information to unauthorised third parties. Security threats on Android are reportedly growing exponentially; however, Google engineers have argued that the malware and virus threat on Android is being exaggerated by security companies for commercial reasons, and have accused the security industry of playing on fears to sell virus protection software to users. Google maintains that dangerous malware is actually extremely rare, and a survey conducted by F-Secure showed that only 0.5% of Android malware reported had come from the Google Play store.

In 2021, journalists and researchers reported the discovery of spyware, called Pegasus, developed and distributed by a private company which can and has been used to infect both iOS and Android smartphones often – partly via use of 0-day exploits – without the need for any user-interaction or significant clues to the user and then be used to exfiltrate data, track user locations, capture film through its camera, and activate the microphone at any time. Analysis of data traffic by popular smartphones running variants of Android found substantial by-default data collection and sharing with no opt-out by this pre-installed software. Both of these issues are not addressed or cannot be addressed by security patches.

#### Scope of surveillance by public institutions

As part of the broader 2013 mass surveillance disclosures it was revealed in September 2013 that the American and British intelligence agencies, the National Security Agency (NSA) and Government Communications Headquarters (GCHQ), respectively, have access to the user data on iPhone, BlackBerry, and Android devices. They were reportedly able to read almost all smartphone information, including SMS, location, emails, and notes. In January 2014, further reports revealed the intelligence agencies' capabilities to intercept the personal information transmitted across the Internet by social networks and other popular applications such as *Angry Birds*, which collect personal information of their users for advertising and other commercial reasons. GCHQ has, according to *The Guardian*, a wiki-style guide of different apps and advertising networks, and the different data that can be siphoned from each. Later that week, the Finnish Angry Birds developer Rovio announced that it was reconsidering its relationships with its advertising platforms in the light of these revelations, and called upon the wider industry to do the same.

The documents revealed a further effort by the intelligence agencies to intercept Google Maps searches and queries submitted from Android and other smartphones to collect location information in bulk. The NSA and GCHQ insist their activities comply with all relevant domestic and international laws, although the Guardian stated "the latest disclosures could also add to mounting public concern about how the technology sector collects and uses information, especially for those outside the US, who enjoy fewer privacy protections than Americans."

Leaked documents codenamed Vault 7 and dated from 2013 to 2016, detail the capabilities of the Central Intelligence Agency (CIA) to perform electronic surveillance and cyber warfare, including the ability to compromise the operating systems of most smartphones (including Android).

#### Security patches

In August 2015, Google announced that devices in the Google Nexus series would begin to receive monthly security patches. Google also wrote that "Nexus devices will continue to receive major updates for at least two years and security patches for the longer of three years from initial availability or 18 months from last sale of the device via the Google Store." The following October, researchers at the University of Cambridge concluded that 87.7% of Android phones in use had known but unpatched security vulnerabilities due to lack of updates and support. Ron Amadeo of *Ars Technica* wrote also in August 2015 that "Android was originally designed, above all else, to be widely adopted. Google was starting from scratch with zero percent market share, so it was happy to give up control and give everyone a seat at the table in exchange for adoption. [...] Now, though, Android has around 75–80 percent of the worldwide smartphone market—making it not just the world's most popular mobile operating system but arguably the most popular operating system, period. As such, security has become a big issue. Android still uses a software update chain-of-command designed back when the Android ecosystem had zero devices to update, and it just doesn't work". Following news of Google's monthly schedule, some manufacturers, including Samsung and LG, promised to issue monthly security updates, but, as noted by Jerry Hildenbrand in *Android Central* in February 2016, "instead we got a few updates on specific versions of a small handful of models. And a bunch of broken promises".

In a March 2017 post on Google's Security Blog, Android security leads Adrian Ludwig and Mel Miller wrote that "More than 735 million devices from 200+ manufacturers received a platform security update in 2016" and that "Our carrier and hardware partners helped expand deployment of these updates, releasing updates for over half of the top 50 devices worldwide in the last quarter of 2016". They also wrote that "About half of devices in use at the end of 2016 had not received a platform security update in the previous year", stating that their work would continue to focus on streamlining the security updates program for easier deployment by manufacturers. Furthermore, in a comment to *TechCrunch*, Ludwig stated that the wait time for security updates had been reduced from "six to nine weeks down to just a few days", with 78% of flagship devices in North America being up-to-date on security at the end of 2016.

Patches to bugs found in the core operating system often do not reach users of older and lower-priced devices. However, the open-source nature of Android allows security contractors to take existing devices and adapt them for highly secure uses. For example, Samsung has worked with General Dynamics through their Open Kernel Labs acquisition to rebuild *Jelly Bean* on top of their hardened microvisor for the "Knox" project.

### Location-tracking

Android smartphones have the ability to report the location of Wi-Fi access points, encountered as phone users move around, to build databases containing the physical locations of hundreds of millions of such access points. These databases form electronic maps to locate smartphones, allowing them to run apps like Foursquare, Google Latitude, Facebook Places, and to deliver location-based ads. Third party monitoring software such as TaintDroid, an academic research-funded project, can, in some cases, detect when personal information is being sent from applications to remote servers.

### Further notable exploits

In 2018, Norwegian security firm Promon has unearthed a serious Android security hole which can be exploited to steal login credentials, access messages, and track location, which could be found in all versions of Android, including Android 10. The vulnerability came by exploiting a bug in the multitasking system enabling a malicious app to overlay legitimate apps with fake login screens that users are not aware of when handing in security credentials. Users can also be tricked into granting additional permissions to the malicious apps, which later enable them to perform various nefarious activities, including intercepting texts or calls and stealing banking credentials. *Avast Threat Labs* also discovered that many pre-installed apps on several hundred new Android devices contain dangerous malware and adware. Some of the preinstalled malware can commit ad fraud or even take over its host device.

In 2020, the Which? watchdog reported that more than a billion Android devices released in 2012 or earlier, which was 40% of Android devices worldwide, were at risk of being hacked. This conclusion stemmed from the fact that no security updates were issued for the Android versions below 7.0 in 2019. Which? collaborated with the AV Comparatives anti-virus lab to infect five phone models with malware, and it succeeded in each case. Google refused to comment on the watchdog's speculations.

On August 5, 2020, Twitter published a blog urging its users to update their applications to the latest version with regards to a security concern that allowed others to access direct messages. A hacker could easily use the "Android system permissions" to fetch the account credentials in order to do so. The security issue is only with Android 8 (Android Oreo) and Android 9 (Android Pie). Twitter confirmed that updating the app will restrict such practices.

### Technical security features

Android applications run in a sandbox, an isolated area of the system that does not have access to the rest of the system's resources, unless access permissions are explicitly granted by the user when the application is installed, however this may not be possible for pre-installed apps. It is not possible, for example, to turn off the microphone access of the pre-installed camera app without disabling the camera completely. This is valid also in Android versions 7 and 8.

Since February 2012, Google has used its Google Bouncer malware scanner to watch over and scan apps available in the Google Play store. A "Verify Apps" feature was introduced in November 2012, as part of the Android 4.2 "Jelly Bean" operating system version, to scan all apps, both from Google Play and from third-party sources, for malicious behaviour. Originally only doing so during installation, Verify Apps received an update in 2014 to "constantly" scan apps, and in 2017 the feature was made visible to users through a menu in Settings.

In former Android versions, before installing an application, the Google Play store displayed a list of the requirements an app needs to function. After reviewing these permissions, the user could choose to accept or refuse them, installing the application only if they accepted. In Android 6.0 "Marshmallow", the permissions system was changed; apps are no longer automatically granted all of their specified permissions at installation time. An opt-in system is used instead, in which users are prompted to grant or deny individual permissions to an app when they are needed for the first time. Applications remember the grants, which can be revoked by the user at any time. Pre-installed apps, however, are not always part of this approach. In some cases it may not be possible to deny certain permissions to pre-installed apps, nor be possible to disable them. The Google Play Services app cannot be uninstalled, nor disabled. Any force stop attempt results in the app restarting itself. The new permissions model is used only by applications developed for Marshmallow using its software development kit (SDK), and older apps will continue to use the previous all-or-nothing approach. Permissions can still be revoked for those apps, though this might prevent them from working properly, and a warning is displayed to that effect.

In September 2014, Jason Nova of *Android Authority* reported on a study by the German security company Fraunhofer AISEC in antivirus software and malware threats on Android. Nova wrote that "The Android operating system deals with software packages by sandboxing them; this does not allow applications to list the directory contents of other apps to keep the system safe. By not allowing the antivirus to list the directories of other apps after installation, applications that show no inherent suspicious behavior when downloaded are cleared as safe. If then later on parts of the app are activated that turn out to be malicious, the antivirus will have no way to know since it is inside the app and out of the antivirus' jurisdiction". The study by Fraunhofer AISEC, examining antivirus software from Avast, AVG, Bitdefender, ESET, F-Secure, Kaspersky, Lookout, McAfee (formerly Intel Security), Norton, Sophos, and Trend Micro, revealed that "the tested antivirus apps do not provide protection against customized malware or targeted attacks", and that "the tested antivirus apps were also not able to detect malware which is completely unknown to date but does not make any efforts to hide its malignity".

In August 2013, Google announced Android Device Manager (renamed Find My Device in May 2017), a service that allows users to remotely track, locate, and wipe their Android device, with an Android app for the service released in December. In December 2016, Google introduced a Trusted Contacts app, letting users request location-tracking of loved ones during emergencies. In 2020, Trusted Contacts was shut down and the location-sharing feature rolled into Google Maps.

On October 8, 2018, Google announced new Google Play store requirements to combat oversharing of potentially sensitive information, including call and text logs. The issue stems from the fact that many apps request permissions to access users' personal information, even if this information is not needed for the app to function, and some users unquestionably grant these permissions. Alternatively, a permission might be listed in the app manifest as required (as opposed to optional) and the app would not install unless user grants the permission; users can withdraw any, even required, permissions from any app in the device settings after app installation, but few users do this. Google promised to work with developers and create exceptions if their apps require phone or SMS permissions for core functionality. The enforcement of this policy began on January 6, 2019, 90 days after its announcement. Furthermore, Google announced a new "target API level requirement" (`targetSdkVersion` in manifest) of at least Android 8.0 (API level 26) for all new apps and app updates. The API level requirement was intended to combat the practice of app developers bypassing some permission screens by specifying early Android versions that had a coarser permission model.

#### Verified Boot

The Android Open Source Project implements a verified boot chain with intentions to verify that executed code, such as the kernel or bootloader, comes from an official source instead of a malicious actor. This implementation establishes a full chain of trust, as it initially starts at a hardware level. Subsequently, the boot loader is verified and system partitions such as `system` and `vendor` are checked for integrity.

Furthermore, this process verifies that a previous version of Android has not been installed. This effectively provides rollback protection, which mitigates exploits that are similar to a downgrade attack.

##### dm-verity

Android (all supported versions, as far back as version 4.4 of the Android Open Source Project) has the option to provide a verified boot chain with `dm-verity`. This is a feature in the Linux kernel that allows for transparent integrity checking of block devices.

This feature is designed to mitigate persistent rootkits.

### Google Play Services and vendor changes

Dependence on proprietary Google Play Services and customizations added on top of the operating system by vendors who license Android from Google is causing privacy concerns.


## Criticism and controversy

### Privacy and GDPR compliance

#### France

In 2019, Google was fined €50 million by the French CNIL for a lack of information regarding their users.

Two years later, in 2021, researcher Douglas Leith, using a sort of data interception, showed that several data are sent from Android device to Google's servers, even when the phone is sleeping (IDLE) with no Google account registered into it. Several Google applications send data, such as Chrome, Message or Docs, however YouTube is the only one to add a unique identifier data.

In 2022, Leith showed that an Android phone sent various data related to communications, including phone and text messages to Google. Timestamp, sender and receiver, plus several other data, are sent to Google Play Services infrastructure, even if the "Usage and Diag" feature is disabled. Those data are marked with a Unique Identifier of an Android device, and do not comply with GDPR.

#### Australia

In 2022, Google was sanctioned A$60 Million (US$40 million) by the Federal Court of Australia for misleading consumers about Google's collection of location data from Android phones. The Australian Competition and Consumer Commission (ACCC) found that between January 2017 and December 2018, Google had presented the "Location History" setting as the only Google account setting that affected the collection of location data, whilst another, separate setting that also allowed the collection of location data under "Web & App Activity" was enabled by default. The ACCC estimates that around 1.3 million Australian Google account owners were impacted by this design. Google has since taken remedial steps to address the behavior.

#### United States of America

A similar case to the 2019 French case regarding location tracking, was brought in the U.S. in a privacy lawsuit filed by a coalition of attorneys general from 40 U.S. states. A penalty of USD 391 Million was agreed between Google and the DoJ. The New York Times released at that time a long-term investigation about those privacy concerns.

### Short software support lifespans

Android devices, particularly low-end and mid-range models, have been criticized for their short software support lifespans. Starting in the 2010s, many users found that their devices received only one or two major updates and a limited number of security patches. This lack of long-term support stemmed from manufacturers' unwillingness to invest in costly software upgrades, which were often tied to contractual agreements with chipset suppliers like Qualcomm. As a result, Android developed a reputation for rapid device obsolescence.

To address this concern, Google introduced Project Treble, a framework designed to streamline the development and deployment of Android updates via Google Play Services, reducing manufacturers' involvement in the update process.

However, for many devices, significant improvements were still limited by the chipset manufacturers. Fairphone, a company focused on sustainability, explained that its inability to extend software support was due to Qualcomm's policies rather than its own. Apple executives also highlighted Android's fragmented update ecosystem in their critiques of the platform, while quietly admitting that Qualcomm had also made it difficult for them to offer updates to the iPhone.

In response to this problem, several community-driven initiatives emerged to provide alternative operating systems for unsupported devices including LineageOS, Sailfish OS, Ubuntu Touch, and PostmarketOS.

Starting in 2022, Samsung, the largest Android smartphone manufacturer, announced extended software support from previous two years, first to four years, followed by five years in 2023 and six years in 2024.

Shortly thereafter, Qualcomm followed suit, offering extending support timelines for OEM building phones with its chipsets, first to seven years in 2024, followed by eight years in 2025. However, the support commitment was only for its most powerful chipsets, and did not make a similar commitment for chipsets used in low-end and mid-range phones.

These changes bring Samsung and potentially some Qualcomm-powered devices closer to competing platforms, such as Apple, whose iPhones have received four to eight years of support.

### Google's developer verification program

In 2025, Google announced that all developers must register under its developer program in order to distribute applications on certified Android phones, whether it is done through the Play Store, sideloaded APKs, or third-party stores like F-Droid, citing security reasons. This measure will be effective starting September 2026. The measure will not directly affect degoogled custom ROMs, such as GrapheneOS.

Google has faced a backlash by experts, developers, activists, lawyers and other groups, which founded the Keep Android Open initiative to raise awareness and signed an open letter urging Google to rescind the policy. They argue that Google will become a gatekeeper as it will be able to decide which apps can be installed and which others will not, provided that "sideloading" will be considerably tampered by the measure (at least 9 steps needed and it would imply waiting 24 hours before an install).

The Electronic Frontier Foundation has denounced that the fact that developers will be required to pay a fee and provide government-issued identification will dishearten free and open-source communities, as several of them operate with limited or no funding, and that it further expands Google's Play Store monopoly over alternative app stores. They also criticize that it creates "an ever-expanding pathway to internet censorship" alleging more centralization of power.
