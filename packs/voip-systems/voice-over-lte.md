---
title: "Voice over LTE"
source: https://en.wikipedia.org/wiki/Voice_over_LTE
domain: voip-systems
license: CC-BY-SA-4.0
tags: voice over ip, rtp transport, voice over lte, voip codec
fetched: 2026-07-02
---

# Voice over LTE

**Voice over Long-Term Evolution** (acronym **VoLTE**) is an LTE high-speed wireless communication standard for voice calls and SMS using mobile phones and data terminals. VoLTE has up to three times the voice and data capacity of older 3G UMTS and up to six times more than 2G GSM. It uses less bandwidth because VoLTE's packet headers are smaller than those of unoptimized VoIP/LTE. VoLTE calls are usually charged at the same rate as other calls.

To make a VoLTE call, the device, its firmware, and the mobile telephone providers on each end, as well as the inter-carrier connectivity must all implement the service in the area, and be able to work together. VoLTE has been marketed as "HD voice" by some carriers, but this is a broader concept. Moreover, HD+ (EVS) is used only in LTE and NR; HD voice was available in 3G too.

## Overview

VoLTE is based on the IP Multimedia Subsystem (IMS) architectural framework, with specific profiles for control and media planes of voice service. This facilitates VoLTE on the LTE wireless broadband service defined by GSMA in PRD IR.92. The approach results in the voice service (control and media planes) being delivered as data flows within the LTE data bearer, with no dependency on (or ultimately, requirement for) the circuit-switched voice network to be in the call path.

As of February 2019 there were 253 operators investing in VoLTE in 113 countries globally, including 184 operators with commercially launched VoLTE-HD voice service in 87 countries, up from 137 operators in 65 countries 12 months previously, according to data from the Global Mobile Suppliers Association. By August 2019, these numbers had risen to 262 operators investing in VoLTE in 120 countries and 194 operators with launched VoLTE-HD voice services in 91 countries.

## Requirements

- Phone service provider has to enable the voice service on its LTE cellular network. Called "VoLTE profiles", it contains the necessary information, for each service provider, to enable VoLTE on the customer's equipment.
- Device manufacturers have to update their devices, for all providers all over the world, with each operator's profile.
- If the VoLTE profile of a mobile provider is present within the device, the operating system will automatically connect and enable Voice over LTE.

## VoLTE Roaming

VoLTE Roaming historically was required to make VoLTE Calls when roaming on another 4G/LTE network. Now countries with only 3G cores use 3G-to-VoLTE Roaming Interworking.

Devices without VoLTE Roaming cannot make VoLTE calls when roaming on another network. VoLTE Roaming uses the S8HR Architecture, this architecture routes the calls to the home mobile network or to a 3G home network using 3G-to-VoLTE Roaming Interworking . Roaming devices that lack VoLTE Roaming support can use 2G or 3G Networks (if available) for making and receiving calls (via Circuit Switched Fallback). In countries without either 2G or 3G Networks, Roaming devices will not have access to call service from the connected Roaming Network.

VoLTE Roaming Support requires an Android Device with Android 12 (2021) or newer or an iPhone with iOS 15 (2021) or newer. As of April 2023 Devices from Android 4 - 11 made up approximately 70% of the Global Android Device Market according to Google. These older devices are largely in demographics that are less likely to roam.

## VoLTE Emergency Calling

Not all devices that have been sold as 'VoLTE capable' support making calls to Emergency Numbers over 4G/LTE with VoLTE. Some carriers and manufacturers have disabled the ability for phones to call Emergency Services with VoLTE and the devices are reliant on 2G or 3G Networks to make calls to Emergency Services.

In 2022 at the European Emergency Number Association (EENA) Conference Telecoms Expert Rudolf van der Berg made a presentation to the Conference outlining serious compatibility issues with VoLTE Calling and Emergency Calling. One of the major issues he raised is that many 4G/LTE Phones (both European & International) are completely unable to call (911/112) Emergency services without the presence of 2G/3G (Circuit Switched Calling) Networks.

A device can have working VoLTE Calling (IMS Registration) on a network but may not be able to successfully make calls to emergency numbers over 4G. For Android devices there are methods to test a device for 4G Emergency Calling support, however such testing can require third-party software and tools to perform. Simply dialing an Emergency Number on a 4G device is **not** sufficient to test if a device can make VoLTE Emergency Calls.

Depending on signal strength and other factors a device may default to 2G or 3G networks (if available). Furthermore, a 4G/LTE device may say *“Emergency Calls Only”* within the system settings or notifications area but that message does not prove the device can actually make an Emergency call over 4G/LTE. Additionally a device may be configured for 4G Emergency Calls in a given region but fail to connect when placing a 4G Call in another country. These devices will generally get stuck on 'calling' and the call will never go through, even though a 2G or 3G network is available.

In March 2024 prior to the Switch-off of 3G Networks in Australia, the Federal Government announced that more than 740,000 4G VoLTE enabled phones may no longer be able to call Emergency Services after the 3G Networks were switched off. In early April 2024 this number was increased to more than 1 million devices in the media with no change to the government reporting. After the completion of the review the number was less than 70,000 of devices that may not be able to call Emergency Services.

Telstra was originally set to switch off their 3G Network on 30 June 2024. Telstra extended their switch off to 31 August in early May 2024. On 14 August 2024, Telstra and Optus further extended the 3G switch off date to 28 October 2024. Vodafone completed their 3G switch off in early January 2024.

## Evolved packet system fallback

**Evolved packet system (**acronym **EPS) fallback** is a crucial mechanism used in early 5G networks, that seamlessly shifts voice calls to the LTE network through VoLTE whenever Voice over NR (VoNR) is not available or that the user’s equipment (UE) doesn’t support it.

This mechanism in early 5G deployments is essential because expanding 5G takes time and allows calls to drop to the widely available LTE network through Single Radio Voice Call Continuity (SRVCC) for handovers or simple redirection to LTE radio access, preventing dropped calls and maintaining Quality of Service (QoS), even if it inherently brings higher latency.

## Problems

There have been several issues with VoLTE deployment:

- VoLTE was not made available to all subscribers
- Some providers' VoLTE service was incompatible with other providers' equipment
- Some older LTE devices are not compatible with VoLTE, and their manufacturers did not update them
- Millions of devices have become and still are becoming obsolescent because of VoLTE incompatibilities
- Some emergency services were unreachable on VoLTE
- In the United States, many M2M devices were not compatible with LTE, which is required for VoLTE
- Many second-range brands and devices are not supported by VoLTE operators
- Before buying a specific device, there is no way to check which VoLTE operators support it

## Device compatibility issues

VoLTE has been supported by all Qualcomm Snapdragon chipsets since at least 2014 (e.g. Snapdragon 800/801), but some Android device manufacturers disabled it in software. Manufacturers of many devices omitted the carrier network configurations/profiles required to support VoLTE calling on all networks.

Unlike calling with 2G and 3G, there is no single configuration for VoLTE that all devices and networks support. Some networks support the GSMA IR.92 'Open Market Device' Configuration. This configuration is intended to be a generic/global VoLTE configuration that can be used by Open Market (non-carrier) devices. 4G or LTE devices that lack native VoLTE calling support are reliant on a 2G or 3G network to make or receive calls via circuit-switched fallback (CSFB), and will otherwise have no call service.

A device marketed as having VoLTE support may only be able to make calls on certain networks, due to varying network configurations and VoLTE standardisation issues.

In some instances (depending on brand, market, or region), devices have been sold that are unable to make VoLTE calls on any network, while the same devices purchased directly from a carrier (with carrier software) support VoLTE on that carrier's network. Some handsets purchased from another carrier or from another market may have software that is not configured to support VoLTE on all networks within a given country. This issue primarily affects Android and other non-Apple devices. The iPhone 6 (2014) and newer, with at least iOS 10, support VoLTE calling on most networks. The iPhone 5 and 5s do not support VoLTE calling, even though they include LTE.

For example, for an Android device to have VoLTE calling on the Telstra network, the device needs to be running a Telstra modem configuration. Devices that are running the GSMA 'Open Market Device' configuration or a configuration from another carrier cannot make VoLTE calls on the Telstra network. This prevents Telstra customers from using Open Market Devices. Open Market configuration devices can work on competing Australian providers Optus & Vodafone.

With some Qualcomm based Android devices it is possible to modify the device firmware with special software and manually load a compatible carrier modem configuration, enabling VoLTE calling; a carrier may not recognise the device as supported, though it works correctly.

For example, starting in May 2024 Telstra starting forcing a pre-recorded message with all outbound calls advising affected customers of the need to upgrade in advance of the 3G shutdown in August. However even customers with modified devices with working VoLTE calling on Telstra were hearing the message every time they made a 4G VoLTE call. This is due to Telstra relying on established lists of 'compatible' devices (i.e. Device IMEI/TAC codes).

Android users are able to confirm if VoLTE is working by checking for the Device 'IMS Status' within a hidden Radio Info Debug menu.

If the IMS Status shows "**IMS Registration: Registered**" and "**Voice over LTE: Available**" then VoLTE is enabled and working. An IMS Status of "**Not Registered**" and "**Voice over LTE: Unavailable**" indicates VoLTE is not enabled or working. However the IMS Status debug **does not** confirm working 4G Emergency Calling support.

For VoLTE calling to be "Available" on a device, VoLTE has to be both provisioned/enabled in the Firmware and a carrier compatible modem configuration/profile must be loaded on the device. Typically the modem configurations are automatically loaded by the device firmware when inserting a sim card. However not all devices are configured to detect the sim cards for all networks and enable VoLTE Calling.

The IMS Status debug can also indicate if Wi-Fi Calling (Voice over Wi-Fi) and Video Calling (ViLTE/Video Telephony) are available. (Note: For Wi-Fi Calling to say Available the device has to be connected to a suitable Wi-Fi Network).

Additionally, devices with a "UT Interface" status of "Unavailable" will be unable to change Call Forwarding or Call Busy Settings over 4G/LTE. Note: UT Interface is not required for VoLTE Calling, UT Interface is only required to change supplementary service settings (i.e. call forwarding) on a 4G/LTE only network. Devices without an "Available" UT Interface are reliant on 2G/3G networks to change call forwarding/busy settings.

## History

Beginning in August 2012, MetroPCS launched the world's first commercial VoLTE services in Dallas, Texas, in the United States, alongside the first VoLTE phone, the LG Connect 4G. In May 2014, Singtel introduced the world's first commercial "full-featured" VoLTE service in Singapore, only in combination with Galaxy Note 3, it was subsequently expanded. In June 2014, KT showcased the world's first cross-border roaming services based on Voice over LTE. The South Korean operator partnered with China Mobile to develop VoLTE roaming services.

In November 2014, Verizon and AT&T announced the companies are enabling VoLTE-to-VoLTE connections between their respective customers. VoLTE interoperability between Verizon and AT&T customers began in 2015. Testing and design were performed between both companies using third party networks such as Alcatel-Lucent. This was stated to have been completed in November 2017.

On July 11, 2015, SEATEL Cambodia announced the world's first commercial 100% VoLTE service without 2G/3G in Cambodia.

As of 2020, almost all new phones for sale have the potential to support VoLTE.

On December 31, 2022, Verizon shut down their CDMA network, therefore requiring devices to support LTE or 5G. Customers with CDMA-only devices and LTE devices without VoLTE support would have been required to switch to a VoLTE-capable device by that date. Verizon stopped activating CDMA-only devices on their network in 2018, and had previously planned to shut down 3G service in 2019, but extended the timeline for shutting down the 3G network twice — first to December 31, 2020, and then to December 31, 2022, which the VP of Network Engineering says "will not be extended again." The company indicated the delays were in an effort to "minimize disruptions" to its customers still utilizing the 3G network. As of March 2021, less than 1% of Verizon's customers were still using 3G, and many of the 3G-connected devices are integrated devices, such as smart utility meters and home burglar alarms.

Additionally, certain Verizon-compatible handsets were blocked from Verizon's CDMA network even before December 31, 2022, even if the device supported CDMA (for instance, unlocked devices with support for Sprint or China Telecom), therefore requiring VoLTE support when used on Verizon. This includes 5G-capable and OnePlus handsets. Devices lacking CDMA support starting with the Pixel 6 and iPhone 14 series as well as select older devices sold on GSM carriers will only work on Verizon in VoLTE mode.

## Voice quality

To ensure compatibility, 3GPP demand at least AMR-NB codec (narrow band), but the recommended speech codec for VoLTE is Adaptive Multi-Rate Wideband (AMR-WB), also known under the trademark HD Voice after GSMA's certification program. This codec is mandated in 3GPP networks that are capable of 16 kHz sampling.

In addition, many carriers and devices can use Enhanced Voice Services (EVS). This is an up to superwideband (20–16,000 Hz) or fullband (20–20,000 Hz) codec backwards-compatible with AMR-WB. This codec is also known under the trademark HD Voice+, after GSMA's certification program. GSMA has proposed to make EVS mandatory just like AMR-WB. (Both the carrier(s), any interconnect and the two calling devices must be capable of using the codec for it to be used.) The AMR-WB+ codec has a wide bit-rate range, from 5.2 to 48 kbit/s. EVS offers a wide range of bit rates from 5.9 kbit/s to 128 kbit/s, allowing service providers to *optimize network capacity and call quality as desired* for their service, so VoLTE does not ensure high call quality.

Fraunhofer IIS has previously demonstrated an implementation of the AAC-ELD codec in VoLTE that they call "Full-HD Voice". It has not gained any standard status or real-world adoption. They have since reused the term "Full-HD Voice" for EVS in fullband mode (HD+ is also used).
