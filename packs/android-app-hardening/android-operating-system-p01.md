---
title: "Android (operating system) (part 1/3)"
source: https://en.wikipedia.org/wiki/Android_(operating_system)
domain: android-app-hardening
license: CC-BY-SA-4.0
tags: android application hardening, android keystore system, android permission model, network security config
fetched: 2026-07-02
part: 1/3
---

# Android (operating system)

**Android** is an open-source operating system developed by Google. Android is based on a modified version of the Linux kernel and other free and open-source software, designed primarily for touchscreen-based mobile devices such as smartphones and tablet computers. Android has historically been developed by a consortium of developers known as the Open Handset Alliance, but its most widely used version is primarily developed by Google. First released in 2008, Android is the world's most widely used operating system; and most used operating system for smartphones. The latest version, released on June 16, 2026, is Android 17.

At its core, the operating system is known as the **Android Open Source Project** (**AOSP**) and is free and open-source software (FOSS) primarily licensed under the Apache License. However, most devices run the proprietary Android version developed by Google, which ships with additional proprietary closed-source software pre-installed, most notably Google Mobile Services (GMS), which includes core apps such as Google Chrome, the digital distribution platform Google Play, and the associated Google Play Services development platform. Other Google services including Firebase Cloud Messaging, used for push notifications, are recommended for applications. While AOSP is free, the "Android" name and logo are trademarks of Google, who restrict the use of Android branding on "uncertified" products. The majority of smartphones based on AOSP run Google's ecosystem—which is known simply as Android—some with vendor-customized user interfaces and software suites, for example One UI. Numerous modified distributions exist, which include competing Amazon Fire OS, community-developed LineageOS; the source code has also been used to develop a variety of Android distributions on a range of other devices, such as Android TV for televisions, Wear OS for wearables, and Android Automotive for in-car systems. Commercial products like micro consoles and virtual reality headset have also used Android.

Software packages on Android, which use the APK format, are generally distributed through a proprietary application store; non-Google platforms include vendor-specific Amazon Appstore, Samsung Galaxy Store, Huawei AppGallery, and third-party companies Aptoide, Cafe Bazaar, GetJar or open source F-Droid. Since 2011 Android has been the most used operating system worldwide on smartphones. It has the largest installed base of any operating system in the world with over three billion monthly active users and accounting for 46% of the global operating system market.


## History

### 2000s

**Android Inc.** was founded in Palo Alto, California, in October 2003 by Andy Rubin and Chris White, with Rich Miner and Nick Sears joining later. Rubin had previously been the creator of the T-Mobile Sidekick under his previous company Danger, Inc. Rubin and White started out to build an operating system for digital cameras viz *FotoFrame*. The company name was changed to *Android* as Rubin already owned the domain name `android.com`. After having built a prototype internally known as the "Fadden demo" predominantly by purchasing licensing agreements for most of the software components built around a custom JavaScript front-end, the company failed to convince investors, and so in April 2004 they pivoted to building an operating system for phones at the suggestion of Nick Sears, as a rival to Symbian and Microsoft Windows Mobile. Rubin pitched the Android project as having "tremendous potential in developing smarter mobile devices that are more aware of its owner's location and preferences". Due to difficulty attracting investors early on, Android faced potential eviction from its office space. Steve Perlman, a close friend of Rubin, brought him $10,000 in cash in an envelope, and shortly thereafter wired an undisclosed amount as seed funding. Perlman refused a stake in the company, and has stated "I did it because I believed in the thing, and I wanted to help Andy."

In 2005, Rubin tried to negotiate deals with Samsung and HTC. Shortly afterwards, Google acquired the company in July of that year for at least $50 million; this was Google's "best deal ever" according to Google's then-vice president of corporate development, David Lawee, in 2010. Android's key employees, including Rubin, Miner, Sears, and White, joined Google as part of the acquisition. Not much was known about the secretive Android Inc. at the time, with the company having provided few details other than that it was making software for mobile phones. At Google, the team led by Rubin developed a mobile device platform powered by the Linux kernel. Google marketed the platform to handset makers and carriers on the promise of providing a flexible, upgradeable system. Google had "lined up a series of hardware components and software partners and signaled to carriers that it was open to various degrees of cooperation".

Speculation about Google's intention to enter the mobile communications market continued to build through December 2006. An early prototype had a close resemblance to a BlackBerry phone, with no touchscreen and a physical QWERTY keyboard, but the arrival of Apple's 2007 iPhone meant that Android "had to go back to the drawing board". Google later changed its Android specification documents to state that "Touchscreens will be supported", although "the Product was designed with the presence of discrete physical buttons as an assumption, therefore a touchscreen cannot completely replace physical buttons". By 2008, both Nokia and BlackBerry announced touch-based smartphones to rival the iPhone 3G, and Android's focus eventually switched to just touchscreens. The first commercially available smartphone running Android was the HTC Dream, also known as T-Mobile G1, announced on September 23, 2008.

On November 5, 2007, the Open Handset Alliance, a consortium of technology companies including Google, device manufacturers such as HTC, Motorola and Samsung, wireless carriers such as Sprint and T-Mobile, and chipset makers such as Qualcomm and Texas Instruments, unveiled itself, with a goal to develop "the first truly open and comprehensive platform for mobile devices". Within a year, the Open Handset Alliance faced two other open source competitors, the Symbian Foundation and the LiMo Foundation, the latter also developing a Linux-based mobile operating system like Google. In September 2007, Google had filed several patent applications in the area of mobile telephony.

On September 23, 2008, Android was introduced by Andy Rubin, Larry Page, Sergey Brin, Cole Brodman, Christopher Schlaeffer and Peter Chou at a press conference in a New York City subway station.

Since 2008, Android has seen numerous updates which have incrementally improved the operating system, adding new features and fixing bugs in previous releases. The first two Android versions were internally codenamed Astro Boy and Bender but licensing issues meant subsequent releases were named after dessert or sugary treat in an alphabetical order, with the first few Android versions being called "Petit Four", "Cupcake", "Donut", "Eclair", and "Froyo", in that order. During its announcement of Android KitKat in 2013, Google explained that "Since these devices make our lives so sweet, each Android version is named after a dessert", although a Google spokesperson told CNN in an interview that "It's kind of like an internal team thing, and we prefer to be a little bit—how should I say—a bit inscrutable in the matter, I'll say".

### 2010s

In 2010, Google launched its Nexus series of devices, a lineup in which Google partnered with different device manufacturers to produce new devices and introduce new Android versions. The series was described as having "played a pivotal role in Android's history by introducing new software iterations and hardware standards across the board", and became known for its "bloat-free" software with "timely ... updates". At its developer conference in May 2013, Google announced a special version of the Samsung Galaxy S4, where, instead of using Samsung's own Android customization, the phone ran "stock Android" and was promised to receive new system updates fast. The device would become the start of the Google Play edition program, and was followed by other devices, including the HTC One Google Play edition, and Moto G Google Play edition. In 2015, *Ars Technica* wrote that "Earlier this week, the last of the Google Play edition Android phones in Google's online storefront were listed as "no longer available for sale" and that "Now they're all gone, and it looks a whole lot like the program has wrapped up".

From 2008 to 2013, Hugo Barra served as product spokesperson, representing Android at press conferences and Google I/O, Google's annual developer-focused conference. He left Google in August 2013 to join Chinese phone maker Xiaomi. Less than six months earlier, Google's then-CEO Larry Page announced in a blog post that Andy Rubin had moved from the Android division to take on new projects at Google, and that Sundar Pichai would become the new Android lead. Pichai himself would eventually switch positions, becoming the new CEO of Google in August 2015 following the company's restructure into the Alphabet conglomerate, making Hiroshi Lockheimer the new head of Android.

On Android 4.4, *KitKat*, shared writing access to MicroSD memory cards has been locked for user-installed applications, to which only the dedicated directories with respective package names, located inside `Android/data/`, remained writeable. Writing access has been reinstated with Android 5 *Lollipop* through the backwards-incompatible *Google Storage Access Framework* interface.

In June 2014, Google announced Android One, a set of "hardware reference models" that would "allow [device makers] to easily create high-quality phones at low costs", designed for consumers in developing countries. In September, Google announced the first set of Android One phones for release in India. However, *Recode* reported in June 2015 that the project was "a disappointment", citing "reluctant consumers and manufacturing partners" and "misfires from the search company that has never quite cracked hardware". Plans to relaunch Android One surfaced in August 2015, with Africa announced as the next location for the program a week later. A report from *The Information* in January 2017 stated that Google is expanding its low-cost Android One program into the United States, although *The Verge* notes that the company will presumably not produce the actual devices itself. Google introduced the Pixel and Pixel XL smartphones in October 2016, marketed as being the first phones made by Google, and exclusively featured certain software features, such as the Google Assistant, before wider rollout. The Pixel phones replaced the Nexus series, with a new generation of Pixel phones launched in October 2017.

In May 2019, the operating system became entangled in the trade war between China and the United States involving Huawei, which, like many other tech firms, had become dependent on access to the Android platform. In the summer of 2019, Huawei announced it would create an alternative operating system to Android known as Harmony OS, and has filed for intellectual property rights across major global markets. Under such sanctions Huawei has long-term plans to replace Android in 2022 with the new operating system, as Harmony OS was originally designed for internet of things devices, rather than for smartphones and tablets.

On August 22, 2019, it was announced that Android "Q" would officially be branded as Android 10, ending the historic practice of naming major versions after desserts. Google stated that these names were not "inclusive" to international users (due either to the aforementioned foods not being internationally known, or being difficult to pronounce in some languages). On the same day, *Android Police* reported that Google had commissioned a statue of a giant number "10" to be installed in the lobby of the developers' new office. Android 10 was released on September 3, 2019, to Google Pixel phones first.

### 2020s

In late 2021, some users reported that they were unable to dial emergency services. The problem was caused by a combination of bugs in Android and in the Microsoft Teams app; both companies released updates addressing the issue.

On December 12, 2024, Google announced Android XR. It is a new operating system developed by Google, designed for virtual reality and augmented reality devices, such as VR headsets and smart glasses. It was built in collaboration with Samsung and Qualcomm. The platform is also focused on supporting developers with tools like ARCore and Unity to build applications for upcoming XR devices.

In March 2025, Google announced its plans to consolidate Android development to internal sources. While public developers will no longer be able to contribute, the Android source will still be published.


## Features

### Interface

Android's default user interface is mainly based on direct manipulation, using touch inputs that loosely correspond to real-world actions, like swiping, tapping, pinching, and reverse pinching to manipulate on-screen objects, along with a virtual keyboard. Game controllers and full-size physical keyboards are supported via Bluetooth or USB. The response to user input is designed to be immediate and provides a fluid touch interface, often using the vibration capabilities of the device to provide haptic feedback to the user. Internal hardware, such as accelerometers, gyroscopes and proximity sensors are used by some applications to respond to additional user actions, for example adjusting the screen from portrait to landscape depending on how the device is oriented, or allowing the user to steer a vehicle in a racing game by rotating the device, simulating control of a steering wheel.

#### Home screen

Android devices boot to the home screen, the primary navigation and information "hub" on Android devices, analogous to the desktop found on personal computers. Android home screens are typically made up of app icons and widgets; app icons launch the associated app, whereas widgets display live, auto-updating content, such as a weather forecast, the user's email inbox, or a news ticker directly on the home screen. A home screen may be made up of several pages, between which the user can swipe back and forth. Third-party apps available on Google Play and other app stores can extensively re-theme the home screen, and even mimic the look of other operating systems, such as Windows Phone. Most manufacturers customize the look and features of their Android devices to differentiate themselves from their competitors.

#### Status bar

Along the top of the screen is a status bar, showing information about the device and its connectivity. This status bar can be pulled (swiped) down to reveal a notification screen where apps display important information or updates, as well as quick access to system controls and toggles such as display brightness, connectivity settings (WiFi, Bluetooth, cellular data), audio mode, and flashlight. Vendors may implement extended settings such as the ability to adjust the flashlight brightness.

#### Notifications

Notifications are "short, timely, and relevant information about your app when it's not in use", and when tapped, users are directed to a screen inside the app relating to the notification. Beginning with Android 4.1 "Jelly Bean", "expandable notifications" allow the user to tap an icon on the notification in order for it to expand and display more information and possible app actions right from the notification.

#### App lists

An "All Apps" screen lists all installed applications, with the ability for users to drag an app from the list onto the home screen. The app list may be accessed using a gesture or a button, depending on the Android version. A "Recents" screen, also known as "Overview", lets users switch between recently used apps.

The recent list may appear side-by-side or overlapping, depending on the Android version and manufacturer.

#### Navigation buttons

Many early Android OS smartphones were equipped with a dedicated search button for quick access to a web search engine and individual apps' internal search feature. More recent devices typically allow the former through a long press or swipe away from the home button.

The dedicated option key, also known as menu key, and its on-screen simulation, is no longer supported since Android version 10. Google recommends mobile application developers to locate menus within the user interface. On more recent phones, its place is occupied by a task key used to access the list of recently used apps when actuated. Depending on device, its long press may simulate a menu button press or engage split screen view, the latter of which is the default behaviour since stock Android version 7.

#### Split-screen view

Native support for split screen view has been added in stock Android version 7.0 *Nougat*.

Split screen was removed on Go Edition version of Android to optimize the User experience for low end devices (8.1-15)

The earliest vendor-customized Android-based smartphones known to have featured a split-screen view mode are the 2012 Samsung Galaxy S3 and Note 2, the former of which received this feature with the *premium suite* upgrade delivered in TouchWiz with Android 4.1 Jelly Bean.

#### Charging while powered off

When connecting or disconnecting charging power and when briefly actuating the power button or home button, all while the device is powered off, a visual battery meter whose appearance varies among vendors appears on the screen, allowing the user to quickly assess the charge status of a powered-off device without having to start it. Some display the battery percentage.

#### Desktop mode

Android has supported a rudimentary Desktop Mode in developer options. A native desktop mode was rolled out in March 2026 to Pixel devices from the Pixel 8 onward; tablets received it with Android 16 QPR3, with the intention to roll this feature out to more devices in the future.

### Applications

Most Android devices come with preinstalled Google apps including Gmail, Google Maps, Google Chrome, YouTube, Google TV, and others.

Applications ("apps"), which extend the functionality of devices, are written using the Android software development kit (SDK) and, often, Kotlin programming language, which replaced Java as Google's preferred language for Android app development in May 2019, and was originally announced in May 2017. Java is still supported (originally the only option for user-space programs, and is often mixed with Kotlin), as is C++. Java or other JVM languages, such as Kotlin, may be combined with C/C++, together with a choice of non-default runtimes that allow better C++ support.

The SDK includes a comprehensive set of development tools, including a debugger, software libraries, a handset emulator based on QEMU, documentation, sample code, and tutorials. Initially, Google's supported integrated development environment (IDE) was Eclipse using the Android Development Tools (ADT) plugin; in December 2014, Google released Android Studio, based on IntelliJ IDEA, as its primary IDE for Android application development. Other development tools are available, including a native development kit (NDK) for applications or extensions in C or C++, Google App Inventor, a visual environment for novice programmers, and various cross platform mobile web applications frameworks. In January 2014, Google unveiled a framework based on Apache Cordova for porting Chrome HTML 5 web applications to Android, wrapped in a native application shell. Additionally, Firebase was acquired by Google in 2014 that provides helpful tools for app and web developers.

Android has a growing selection of third-party applications, which can be acquired by users by downloading and installing the application's APK (Android application package) file, or by downloading them using an application store program that allows users to install, update, and remove applications from their devices. Google Play Store is the primary application store installed on Android devices that comply with Google's compatibility requirements and license the Google Mobile Services software. Google Play Store allows users to browse, download and update applications published by Google and third-party developers; as of January 2021, there are more than three million applications available for Android in Play Store. As of July 2013, 50 billion application installations had been performed. Some carriers offer direct carrier billing for Google Play application purchases, where the cost of the application is added to the user's monthly bill. As of May 2017, there are over one billion active users a month for Gmail, Android, Chrome, Google Play and Maps.

Due to the open nature of Android, a number of third-party application marketplaces also exist for Android, either to provide a substitute for devices that are not allowed to ship with Google Play Store, provide applications that cannot be offered on Google Play Store due to policy violations, or for other reasons. Examples of these third-party stores have included the Amazon Appstore, GetJar, and SlideMe. F-Droid, another alternative marketplace, seeks to only provide applications that are distributed under free and open source licenses.

In October 2020, Google removed several Android applications from Play Store, as they were identified breaching its data collection rules. The firm was informed by International Digital Accountability Council (IDAC) that apps for children like *Number Coloring*, *Princess Salon* and *Cats & Cosplay*, with collective downloads of 20 million, were violating Google's policies.

At the Windows 11 announcement event in June 2021, Microsoft showcased the new Windows Subsystem for Android (WSA) to enable support for the Android Open Source Project (AOSP), but it has since been deprecated. It was intended to allow users to run Android apps and games on their Windows 11 desktop. Microsoft ended WSA support on March 5, 2025.

### Storage

The storage of Android devices can be expanded using secondary devices such as SD cards. Android recognizes two types of secondary storage: *portable* storage (which is used by default), and *adoptable* storage. Portable storage is treated as an external storage device. Adoptable storage, introduced on Android 6.0, allows the internal storage of the device to be spanned with the SD card, treating it as an extension of the internal storage. This has the disadvantage of preventing the memory card from being used with another device unless it is reformatted.

Android 4.4 introduced the Storage Access Framework (SAF), a set of APIs for accessing files on the device's filesystem. As of Android 11, Android has required apps to conform to a data privacy policy known as *scoped storage*, under which apps may only automatically have access to certain directories (such as those for pictures, music, and video), and app-specific directories they have created themselves. Apps are required to use the SAF to access any other part of the filesystem.

### Memory management

Since Android devices are usually battery-powered, Android is designed to manage processes to keep power consumption at a minimum. When an application is not in use the system suspends its operation so that, while available for immediate use rather than closed, it does not use battery power or CPU resources. Android manages the applications stored in memory automatically: when memory is low, the system will begin invisibly and automatically closing inactive processes, starting with those that have been inactive for the longest amount of time. Lifehacker reported in 2011 that third-party task-killer applications were doing more harm than good.

### Developer options

Some settings for use by developers for debugging and power users are located in a "Developer options" sub menu, such as the ability to highlight updating parts of the display, show an overlay with the current status of the touch screen, show touching spots for possible use in screencasting, notify the user of unresponsive background processes with the option to end them ("Show all ANRs", i.e. "App's Not Responding"), prevent a Bluetooth audio client from controlling the system volume ("Disable absolute volume"), and adjust the duration of transition animations or deactivate them completely to speed up navigation.

Developer options are initially hidden since Android 4.2 "Jelly Bean", but can be enabled by actuating the operating system's build number in the device information seven times. Hiding developers options again requires deleting user data for the "Settings" app, possibly resetting some other preferences, or in recent Android versions, turning off the Developer options master switch.


## Hardware

The main hardware platform for Android is 64-bit ARM (i.e. the ARMv8-A architecture) and the 32-bit ARMv7-A architecture, with x86-64 and the 32-bit x86 architectures also being officially supported in later versions of Android. The unofficial Android-x86 project provided support for x86 architectures ahead of the official support. Since 2012, Android devices with Intel processors began to appear, including phones and tablets. While gaining support for 64-bit platforms, Android was first made to run on 64-bit x86 and then on ARM64. An unofficial experimental port of the operating system to 64-bit RISC-V architecture was released in 2021. 32- and 64-bit MIPS was once supported.

Requirements for the minimum amount of RAM for smartphones running Android 15 range from 4 GB of RAM for full Android to 2 GB, in which case the smartphone manufacturers must use the Android Go Edition. Android supports all versions of OpenGL ES and Vulkan (and version 1.1 available for some devices).

Android devices incorporate many optional hardware components, including still or video cameras, GPS, orientation sensors, dedicated gaming controls, accelerometers, gyroscopes, barometers, magnetometers, proximity sensors, pressure sensors, thermometers, and touchscreens. Some hardware components are not required, but became standard in certain classes of devices, such as smartphones, and additional requirements apply if they are present. Some other hardware was initially required, but those requirements have been relaxed or eliminated altogether. For example, as Android was developed initially as a phone OS, hardware such as microphones were required, while over time the phone function became optional. Android used to require an autofocus camera, which was relaxed to a fixed-focus camera if present at all, since the camera was dropped as a requirement entirely when Android started to be used on set-top boxes.

In addition to running on smartphones and tablets, several vendors run Android natively on regular PC hardware with a keyboard and mouse. In addition to their availability on commercially available hardware, similar PC hardware-friendly versions of Android are freely available from the Android-x86 project, including customized Android 4.4. Using the Android emulator that is part of the Android SDK, or third-party emulators, Android can also run non-natively on x86 architectures. Chinese companies are building a PC and mobile operating system, based on Android, to "compete directly with Microsoft Windows and Google Android". The Chinese Academy of Engineering noted that "more than a dozen" companies were customizing Android following a Chinese ban on the use of Windows 8 on government PCs.


## Devices

Android runs on a wide variety of devices such as smartphones, tablets, cars, computers, smart watches, and smart TVs. However, the vast majority of Android-powered devices are smartphones. Unlike its two main competitors in the mobile operating system space, namely iOS and HarmonyOS, Android devices are made by many different original equipment manufacturers. These OEMs include Samsung, Xiaomi, Vivo, Oppo, iQOO, OnePlus, Honor, Google, Sony, Lenovo, Sharp, Realme, Nothing, and Tecno.
