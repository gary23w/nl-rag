---
title: "Wired Equivalent Privacy"
source: https://en.wikipedia.org/wiki/Wired_Equivalent_Privacy
domain: wifi-security-wpa
license: CC-BY-SA-4.0
tags: wi-fi protected access, wireless security, wlan authentication, 802.1x port authentication
fetched: 2026-07-02
---

# Wired Equivalent Privacy

**Wired Equivalent Privacy** (**WEP**) is an obsolete security algorithm for 802.11 wireless networks. It was introduced as part of the original IEEE 802.11 standard ratified in 1997. The intention was to provide a level of security and privacy comparable to that of a traditional wired network. WEP, recognizable by its key of 10 or 26 hexadecimal digits (40 or 104 bits), was at one time widely used, and was often the first security choice presented to users by router configuration tools. After a severe design flaw in the algorithm was disclosed in 2001, WEP was no longer considered a secure method of wireless connection; however, in the vast majority of cases, Wi-Fi hardware devices relying on WEP security could not be upgraded to secure operation. Some of WEP's design flaws were addressed in WEP2, but it also proved insecure, and never saw wide adoption or standardization.

In 2003, the Wi-Fi Alliance announced that WEP and WEP2 had been superseded by Wi-Fi Protected Access (WPA). In 2004, with the ratification of the full 802.11i standard (i.e. WPA2), the IEEE declared that both WEP-40 and WEP-104 have been deprecated. WPA retained some design characteristics of WEP that remained problematic.

WEP was the only encryption protocol available to 802.11a and 802.11b devices built before the WPA standard, which was available for 802.11g devices. However, some 802.11b devices were later provided with firmware or software updates to enable WPA, and newer devices had it built in.

## History

WEP was ratified as a Wi-Fi security standard in September 17, 1999. The first versions of WEP were not particularly strong, even for the time they were released, due to U.S. restrictions on the export of various cryptographic technologies. These restrictions led to manufacturers restricting their devices to only 64-bit encryption. When the restrictions were lifted, the encryption was increased to 128 bits. Despite the introduction of 256-bit WEP, 128-bit remains one of the most common implementations.

## Encryption details

WEP was included as the privacy component of the original IEEE 802.11 standard ratified in 1997. WEP uses the stream cipher RC4 for confidentiality, and the CRC-32 checksum for integrity. It was deprecated in 2004 and is documented in the current standard.

Standard 64-bit WEP uses a 40-bit key (also known as WEP-40), which is concatenated with a 24-bit initialization vector (IV) to form the RC4 key. At the time that the original WEP standard was drafted, the U.S. Government's export restrictions on cryptographic technology limited the key size. Once the restrictions were lifted, manufacturers of access points implemented an extended 128-bit WEP protocol using a 104-bit key size (WEP-104).

A 64-bit WEP key is usually entered as a string of 10 hexadecimal (base 16) characters (0–9 and A–F). Each character represents 4 bits, 10 digits of 4 bits each gives 40 bits; adding the 24-bit IV produces the complete 64-bit WEP key (4 bits × 10 + 24-bit IV = 64-bit WEP key). Most devices also allow the user to enter the key as 5 ASCII characters (0–9, a–z, A–Z), each of which is turned into 8 bits using the character's byte value in ASCII (8 bits × 5 + 24-bit IV = 64-bit WEP key); however, this restricts each byte to be a printable ASCII character, which is only a small fraction of possible byte values, greatly reducing the space of possible keys.

A 128-bit WEP key is usually entered as a string of 26 hexadecimal characters. 26 digits of 4 bits each gives 104 bits; adding the 24-bit IV produces the complete 128-bit WEP key (4 bits × 26 + 24-bit IV = 128-bit WEP key). Most devices also allow the user to enter it as 13 ASCII characters (8 bits × 13 + 24-bit IV = 128-bit WEP key).

152-bit and 256-bit WEP systems are available from some vendors. As with the other WEP variants, 24 bits of that is for the IV, leaving 128 or 232 bits for actual protection. These 128 or 232 bits are typically entered as 32 or 58 hexadecimal characters (4 bits × 32 + 24-bit IV = 152-bit WEP key, 4 bits × 58 + 24-bit IV = 256-bit WEP key). Most devices also allow the user to enter it as 16 or 29 ASCII characters (8 bits × 16 + 24-bit IV = 152-bit WEP key, 8 bits × 29 + 24-bit IV = 256-bit WEP key).

## Authentication

Two methods of authentication can be used with WEP: Open System authentication and Shared Key authentication.

In Open System authentication, the WLAN client does not provide its credentials to the access point during authentication. Any client can authenticate with the access point and then attempt to associate. In effect, no authentication occurs. Subsequently, WEP keys can be used for encrypting data frames. At this point, the client must have the correct keys.

In Shared Key authentication, the WEP key is used for authentication in a four-step challenge–response handshake:

1. The client sends an authentication request to the access point.
2. The access point replies with a clear-text challenge.
3. The client encrypts the challenge-text using the configured WEP key and sends it back in another authentication request.
4. The access point decrypts the response. If this matches the challenge text, the access point sends back a positive reply.

After the authentication and association, the pre-shared WEP key is also used for encrypting the data frames using RC4.

At first glance, it might seem as though Shared Key authentication is more secure than Open System authentication since the latter offers no real authentication. However, it is quite the reverse. It is possible to derive the keystream used for the handshake by capturing the challenge frames in Shared Key authentication. Therefore, data can be more easily intercepted and decrypted with Shared Key authentication than with Open System authentication. If privacy is a primary concern, it is more advisable to use Open System authentication for WEP authentication, rather than Shared Key authentication; however, this also means that any WLAN client can connect to the AP. (Both authentication mechanisms are weak; Shared Key WEP is deprecated in favor of WPA/WPA2.)

## Weak security

Because RC4 is a stream cipher, the same traffic key must never be used twice. The purpose of an IV, which is transmitted as plaintext, is to prevent any repetition, but a 24-bit IV is not long enough to ensure this on a busy network. The way the IV was used also opened WEP to a related-key attack. For a 24-bit IV, there is a 50% probability the same IV will repeat after 5,000 packets.

In August 2001, Scott Fluhrer, Itsik Mantin, and Adi Shamir published a cryptanalysis of WEP that exploits the way the RC4 ciphers and IV are used in WEP, resulting in a passive attack that can recover the RC4 key after eavesdropping on the network. Depending on the amount of network traffic, and thus the number of packets available for inspection, a successful key recovery could take as little as one minute. If an insufficient number of packets are being sent, there are ways for an attacker to send packets on the network and thereby stimulate reply packets, which can then be inspected to find the key. The attack was soon implemented, and automated tools have since been released. It is possible to perform the attack with a personal computer, off-the-shelf hardware, and freely available software such as aircrack-ng to crack *any* WEP key in minutes.

Cam-Winget et al. surveyed a variety of shortcomings in WEP. They wrote "*Experiments in the field show that, with proper equipment, it is practical to eavesdrop on WEP-protected networks from distances of a mile or more from the target.*" They also reported two generic weaknesses:

- the use of WEP was optional, resulting in many installations never even activating it, and
- by default, WEP relies on a single shared key among users, which leads to practical problems in handling compromises, which often leads to ignoring compromises.

In 2005, a group from the U.S. Federal Bureau of Investigation gave a demonstration where they cracked a WEP-protected network in three minutes using publicly available tools. Andreas Klein presented another analysis of the RC4 stream cipher. Klein showed that there are more correlations between the RC4 keystream and the key than the ones found by Fluhrer, Mantin, and Shamir, which can additionally be used to break WEP in WEP-like usage modes.

In 2006, Bittau, Handley, and Lackey showed that the 802.11 protocol itself can be used against WEP to enable earlier attacks that were previously thought impractical. After eavesdropping a single packet, an attacker can rapidly bootstrap to be able to transmit arbitrary data. The eavesdropped packet can then be decrypted one byte at a time (by transmitting about 128 packets per byte to decrypt) to discover the local network IP addresses. Finally, if the 802.11 network is connected to the Internet, the attacker can use 802.11 fragmentation to replay eavesdropped packets while crafting a new IP header onto them. The access point can then be used to decrypt these packets and relay them on to a buddy on the Internet, allowing real-time decryption of WEP traffic within a minute of eavesdropping the first packet.

In 2007, Erik Tews, Andrei Pyshkin, and Ralf-Philipp Weinmann were able to extend Klein's 2005 attack and optimize it for usage against WEP. With the new attack it is possible to recover a 104-bit WEP key with a probability of 50% using only 40,000 captured packets. For 60,000 available data packets, the success probability is about 80%, and for 85,000 data packets, about 95%. Using active techniques like Wi-Fi deauthentication attacks and ARP re-injection, 40,000 packets can be captured in less than one minute under good conditions. The actual computation takes about 3 seconds and 3 MB of main memory on a Pentium-M 1.7 GHz and can additionally be optimized for devices with slower CPUs. The same attack can be used for 40-bit keys with an even higher success probability.

In 2008 the Payment Card Industry Security Standards Council (PCI SSC) updated the Data Security Standard (DSS) to prohibit use of WEP as part of any credit-card processing after 30 June 2010, and prohibit any new system from being installed that uses WEP after 31 March 2009. The use of WEP contributed to the TJ Maxx parent company network invasion.

### Caffe Latte attack

The Caffe Latte attack is another way to defeat WEP. It is not necessary for the attacker to be in the area of the network using this exploit. By using a process that targets the Windows wireless stack, it is possible to obtain the WEP key from a remote client. By sending a flood of encrypted ARP requests, the assailant takes advantage of the shared key authentication and the message modification flaws in 802.11 WEP. The attacker uses the ARP responses to obtain the WEP key in less than 6 minutes.

## Countermeasures

Use of encrypted tunneling protocols (e.g., IPsec, Secure Shell) can provide secure data transmission over an insecure network. However, replacements for WEP have been developed with the goal of restoring security to the wireless network itself.

### 802.11i (WPA and WPA2)

The recommended solution to WEP security problems is to switch to WPA2. WPA was an intermediate solution for hardware that could not support WPA2. Both WPA and WPA2 are much more secure than WEP. To add support for WPA or WPA2, some old Wi-Fi access points might need to be replaced or have their firmware upgraded. WPA was designed as an interim software-implementable solution for WEP that could forestall immediate deployment of new hardware. However, TKIP (the basis of WPA) has reached the end of its designed lifetime, has been partially broken, and has been officially deprecated with the release of the 802.11-2012 standard.

### Implemented non-standard fixes

#### WEP2

This stopgap enhancement to WEP was present in some of the early 802.11i drafts. It was implementable on *some* (not all) hardware not able to handle WPA or WPA2, and extended both the IV and the key values to 128 bits. It was hoped to eliminate the duplicate IV deficiency as well as stop brute-force key attacks.

After it became clear that the overall WEP algorithm was deficient (and not just the IV and key sizes) and would require even more fixes, both the WEP2 name and original algorithm were dropped. The two extended key lengths remained in what eventually became WPA's TKIP.

#### WEPplus

WEPplus, also known as WEP+, is a proprietary enhancement to WEP by Agere Systems (formerly a subsidiary of Lucent Technologies) that enhances WEP security by avoiding "weak IVs". It is only completely effective when WEPplus is used at *both ends* of the wireless connection. As this cannot easily be enforced, it remains a serious limitation. It also does not necessarily prevent replay attacks, and is ineffective against later statistical attacks that do not rely on weak IVs.

#### Dynamic WEP

Dynamic WEP refers to the combination of 802.1x technology and the Extensible Authentication Protocol. Dynamic WEP changes WEP keys dynamically. It is a vendor-specific feature provided by several vendors such as 3Com.

The dynamic change idea made it into 802.11i as part of TKIP, but not for the WEP protocol itself.
