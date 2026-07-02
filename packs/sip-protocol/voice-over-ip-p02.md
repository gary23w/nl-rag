---
title: "Voice over IP (part 2/2)"
source: https://en.wikipedia.org/wiki/Voice_over_IP
domain: sip-protocol
license: CC-BY-SA-4.0
tags: sip protocol, session initiation protocol, voip signaling, voice over ip signaling
fetched: 2026-07-02
part: 2/2
---

## History

The early developments of packet network designs by Paul Baran and other researchers were motivated by a desire for a higher degree of circuit redundancy and network availability in the face of infrastructure failures than was possible in the circuit-switched networks in telecommunications of the mid-twentieth century. Danny Cohen first demonstrated a form of packet voice in 1973 which was developed into Network Voice Protocol which operated across the early ARPANET.

On the early ARPANET, real-time voice communication was not possible with uncompressed pulse-code modulation (PCM) digital speech packets, which had a bit rate of 64 kbps, much greater than the 2.4 kbps bandwidth of early modems. The solution to this problem was linear predictive coding (LPC), a speech coding data compression algorithm that was first proposed by Fumitada Itakura of Nagoya University and Shuzo Saito of Nippon Telegraph and Telephone (NTT) in 1966. LPC was capable of speech compression down to 2.4 kbps, leading to the first successful real-time conversation over ARPANET in 1974, between Culler-Harrison Incorporated in Goleta, California, and MIT Lincoln Laboratory in Lexington, Massachusetts. LPC has since been the most widely used speech coding method. Code-excited linear prediction (CELP), a type of LPC algorithm, was developed by Manfred R. Schroeder and Bishnu S. Atal in 1985. LPC algorithms remain an audio coding standard in modern VoIP technology.

In the two decades following the 1974 demo, various forms of packet telephony were developed and industry interest groups formed to support the new technologies. Following the termination of the ARPANET project, and expansion of the Internet for commercial traffic, IP telephony was tested and deemed infeasible for commercial use until the introduction of VocalChat in the early 1990s and then in Feb 1995 the official release of Internet Phone (or iPhone for short) commercial software by VocalTec, based on a patent by Lior Haramaty and Alon Cohen, and followed by other VoIP infrastructure components such as telephony gateways and switching servers. Soon after it became an established area of interest in commercial labs of the major IT concerns, notably at AT&T, where Marian Croak and her team filed many patents related to the technology. By the late 1990s, the first softswitches became available, and new protocols, such as H.323, MGCP and Session Initiation Protocol (SIP) gained widespread attention. In the early 2000s, the proliferation of high-bandwidth always-on Internet connections to residential dwellings and businesses spawned an industry of Internet telephony service providers (ITSPs). The development of open-source telephony software, such as Asterisk PBX, fueled widespread interest and entrepreneurship in voice-over-IP services, applying new Internet technology paradigms, such as cloud services to telephony.

### Milestones

- 1966: Linear predictive coding (LPC) proposed by Fumitada Itakura of Nagoya University and Shuzo Saito of Nippon Telegraph and Telephone (NTT).
- 1973: Packet voice application by Danny Cohen.
- 1974: The Institute of Electrical and Electronics Engineers (IEEE) publishes a paper entitled "A Protocol for Packet Network Interconnection".
- 1974: Network Voice Protocol (NVP) tested over ARPANET in August 1974, carrying barely intelligible 16 kpbs CVSD encoded voice.
- 1974: The first successful real-time conversation over ARPANET was achieved using 2.4 kpbs LPC, between Culler-Harrison Incorporated in Goleta, California, and MIT Lincoln Laboratory in Lexington, Massachusetts.
- 1977: Danny Cohen and Jon Postel of the USC Information Sciences Institute, and Vint Cerf of the Defense Advanced Research Projects Agency (DARPA), agree to separate IP from TCP, and create UDP for carrying real-time traffic.
- 1981: IPv4 is described in RFC 791.
- 1985: The National Science Foundation commissions the creation of NSFNET.
- 1985: Code-excited linear prediction (CELP), a type of LPC algorithm, developed by Manfred R. Schroeder and Bishnu S. Atal.
- 1986: Proposals from various standards organizations for Voice over ATM, in addition to commercial packet voice products from companies such as StrataCom
- 1991: Speak Freely, a voice-over-IP application, was released to the public domain.
- 1992: The Frame Relay Forum conducts development of standards for voice over Frame Relay.
- 1992: InSoft Inc. announces and launches its desktop conferencing product Communique, which includes VoIP and video. The company is credited with developing the first generation of commercial, US-based VoIP, Internet media streaming and real-time Internet telephony/collaborative software and standards that would provide the basis for the Real Time Streaming Protocol (RTSP) standard.
- 1993 Release of VocalChat, a commercial packet network PC voice communication software from VocalTec.
- 1994: MTALK, a freeware LAN VoIP application for Linux
- 1995:
  - VocalTec releases *Internet Phone* commercial Internet phone software.
  - Intel, Microsoft and Radvision initiated standardization activities for VoIP communications system.
- 1996:
  - ITU-T begins development of standards for the transmission and signaling of voice communications over Internet Protocol networks with the H.323 standard.
  - US telecommunications companies petition the US Congress to ban Internet phone technology.
  - G.729 speech codec introduced, using CELP (LPC) algorithm.
- 1997: Level 3 began development of its first softswitch, a term they coined in 1998.
- 1999:
  - The Session Initiation Protocol (SIP) specification RFC 2543 is released.
  - Mark Spencer of Digium develops Asterisk, the first open source private branch exchange (PBX) software.
  - A discrete cosine transform (DCT) variant called the modified discrete cosine transform (MDCT) is adopted for the Siren codec, used in the G.722.1 wideband audio coding standard.
  - The MDCT is adapted into the LD-MDCT algorithm, used in the AAC-LD standard.
- 2001: INOC-DBA, the first inter-provider SIP network is deployed; this is also the first voice network to reach all seven continents.
- 2003: Skype released in August 2003. This was the creation of Niklas Zennström and Janus Friis, in cooperation with four Estonian developers. It quickly became a popular program that helped democratize VoIP.
- 2004: Early commercial VoIP service providers proliferate.
- 2005: PhoneGnome VoIP service is launched by TelEvolution, Inc. of California.
- 2006: G.729.1 wideband codec introduced, using MDCT and CELP (LPC) algorithms.
- 2007: VoIP device manufacturers and sellers boom in Asia, specifically in the Philippines where many families of overseas workers reside.
- 2009: SILK codec introduced, using LPC algorithm, and used for voice calling in Skype.
- 2010: Apple introduces FaceTime, which uses the LD-MDCT-based AAC-LD codec.
- 2011:
  - Rise of WebRTC technology, which supports VoIP directly in browsers.
  - CELT codec introduced, using MDCT algorithm.
- 2012: Opus codec introduced, using MDCT and LPC algorithms.
