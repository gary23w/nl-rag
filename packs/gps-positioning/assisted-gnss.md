---
title: "Assisted GNSS"
source: https://en.wikipedia.org/wiki/Assisted_GNSS
domain: gps-positioning
license: CC-BY-SA-4.0
tags: gps positioning, satellite navigation, gnss positioning, nmea sentence
fetched: 2026-07-02
---

# Assisted GNSS

**Assisted GNSS** (**A-GNSS**) is a GNSS augmentation system that often significantly improves the startup performance—i.e., time-to-first-fix (TTFF)—of a global navigation satellite system (GNSS). A-GNSS works by providing the necessary data to the device via a radio network instead of the slow satellite link, essentially "warming up" the receiver for a fix. When applied to GPS, it is known as **assisted GPS** or **augmented GPS** (abbreviated generally as **A-GPS** and less commonly as **aGPS**). Other local names include **A-GANSS** for Galileo and **A-Beidou** for BeiDou.

A-GPS is extensively used with GPS-capable cellular phones, as its development was accelerated by the U.S. FCC's 911 requirement to make cell phone location data available to emergency call dispatchers.

## Background

Every GPS device requires orbital data about the satellites to calculate its position. The data rate of the satellite signal is only 50 bit/s, so downloading orbital information like ephemerides and/or the almanac directly from satellites typically takes a long time, and if the satellite signals are lost during the acquisition of this information, it is discarded and the standalone system has to start from scratch. In exceptionally poor signal conditions, for example in urban areas, satellite signals may exhibit multipath propagation where signals skip off structures, or are weakened by meteorological conditions or tree canopies. Some standalone GPS navigators used in poor conditions can't fix a position because of satellite signal fracture and must wait for better satellite reception. A regular GPS unit may need as long as 12.5 minutes (the time needed to download the GPS almanac and ephemerides) to resolve the problem and be able to provide a correct location.

## Operation

In A-GPS, the network operator deploys an A-GPS server, a cache server for GPS data. These A-GPS servers download the orbital information from the satellite and store it in the database. An A-GPS-capable device can connect to these servers and download this information using mobile-network radio bearers such as GSM, CDMA, WCDMA, LTE or even using other radio bearers such as Wi-Fi or LoRa. Usually the data rate of these bearers is high, hence downloading orbital information takes less time. Utilizing this system can come at a cost to the user. For billing purposes, network providers often count this as a data access, which can cost money, depending on the tariff.

To be precise, A-GPS features depend mostly on an Internet network or connection to an ISP (or CNP, in the case of CP/mobile-phone device linked to a cellular network provider data service). A mobile device with just an L1 front-end radio receiver and no GPS acquisition, tracking, and positioning engine only works when it has an internet connection to an ISP/CNP, where the position fix is calculated offboard the device itself. It doesn't work in areas with no coverage or internet link (or nearby base transceiver station (BTS) towers, in the case on CNP service coverage area). Without any of those resources, it can't connect to the A-GPS servers usually provided by CNPs. On the other hand, a mobile device with a GPS chipset requires no data connection to capture and process GPS data into a position solution, since it receives data directly from the GPS satellites and is able to calculate a position fix itself. However, the availability of a data connection can provide assistance to improve the performance of the GPS chip on the mobile device.

### Modes of operation

Assistance falls into two categories:

**Mobile Station Based (MSB)**

Information used to acquire satellites more quickly.

- It can supply ephemeris (precise orbital data, effective for a short time) or almanac (rough orbital data, effective for 1–7 days) for the GPS satellites to the GPS receiver, enabling the GPS receiver to lock to the satellites more rapidly in some cases.
- The network can provide precise time.

**Mobile Station Assisted (MSA)**

Calculation of position by the server using information from the GPS receiver.

- The device captures a snapshot of the GPS signal, with approximate time, for the server to later process into a position.
- The assistance server has a good satellite signal and plentiful computation power, so it can compare fragmentary signals relayed to it.
- Accurate, surveyed coordinates for the cell site towers allow better knowledge of local ionospheric conditions and other conditions affecting the GPS signal than the GPS receiver alone, enabling more precise calculation of position.

Not every A-GNSS server provides MSA mode operation due to the computational cost and the declining number of mobile terminals incapable of performing their own calculations. Google's SUPL server is one that does not.

A typical A-GPS-enabled receiver uses a data connection (Internet or other) to contact the assistance server for aGPS information. If it also has functioning autonomous GPS, it may use standalone GPS, which is sometimes slower on time to first fix, but does not depend on the network, and therefore can work beyond network range and without incurring data-usage fees. Some A-GPS devices do not have the option of falling back to standalone or autonomous GPS.

Many mobile phones combine A-GPS and other location services, including Wi-Fi positioning system and cell-site multilateration and sometimes a hybrid positioning system.

High-Sensitivity GPS is an allied technology that addresses some of these issues in a way that does not require additional infrastructure. However, unlike some forms of A-GPS, high-sensitivity GPS cannot provide a fix instantaneously when the GPS receiver has been off for some time.

## Standards

A-GPS protocols are part of Positioning Protocol defined by two different standardization bodies, 3GPP and Open Mobile Alliance (OMA).

**Control Plane Protocol**

Defined by the 3GPP for various generations of mobile phone systems. These protocols are defined for

circuit switched

networks. The following positioning protocols have been defined.

- RRLP – 3GPP defined RRLP (Radio Resource Location Protocol) to support positioning protocol on GSM networks.
- TIA 801 – CDMA2000 family defined this protocol for CDMA 2000 networks.
- RRC position protocol – 3GPP defined this protocol as part of the RRC standard for UMTS network.
- LPP – 3GPP defined LPP or LTE positioning protocol for LTE networks.

**User Plane Protocol**

Defined by the OMA to support positioning protocols in

packet switched

networks. Three generations of

Secure User Plane Location

(SUPL) protocol have been defined, from version 1.0 to 3.0.

### SUPL

The SUPL (Secure User Plane Location) protocol, unlike its control-plane equivalents restricted to mobile networks, runs on the Internet's TCP/IP infrastructure. Consequently, its application extends beyond the original intended use of mobile devices and may be used by general-purpose computers. SUPL 3.0 legitimizes such use by adding admission for WLAN and broadband connections.

Actions defined by SUPL 3.0 include a wide range of services like geofencing and billing. The A-GNSS functions are defined in the SUPL Positioning Functional Group. It includes:

- SUPL Assistance Delivery Function (SADF), which provides the basic information sent to the device in both A-GNSS modes.
- SUPL Reference Retrieval Function (SRRF), which tells the server to prepare the information mentioned above by receiving from the satellites.
- SUPL Position Calculation Function (SPCF), which lets the client or the server ask for the client's location. The server-generated location may result from MSA or from mobile cell. If a MSB (SET based) mode is used, the client reports its location to the server instead.

The specifics of communication is defined in the ULP (Userplane Location Protocol) substandard of SUPL suite. As of December 2018, GNSS systems supported include GPS, Galileo, GLONASS, and BeiDou.

### PSDS

The PSDS (Predicted Satellite Data Service) is a general term for vendor-specific services that provide almanac data that is effective for an extended time (e.g. 7 days), enabling offline A-GPS. Hardware manufacturers such as Qualcomm (gpsOneXTRA), Samsung, and Broadcom each run their own servers and use their own data formats. GrapheneOS runs a caching proxy for these services to help mask user identity.
