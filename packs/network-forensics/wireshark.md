---
title: "Wireshark"
source: https://en.wikipedia.org/wiki/Wireshark
domain: network-forensics
license: CC-BY-SA-4.0
tags: network forensics investigation, packet capture reconstruction, traffic flow analysis, network evidence collection, deep packet inspection
fetched: 2026-07-02
---

# Wireshark

**Wireshark** is free and open-source packet analyzer software. It is used for computer network analysis and troubleshooting, software and communications protocol development, and education. Originally named **Ethereal**, the project was renamed Wireshark in May 2006 due to trademark issues.

Wireshark is cross-platform, using the Qt widget toolkit in current releases to implement its user interface, and using pcap to capture packets; it runs on Linux, macOS, BSD, Solaris, some other Unix-like operating systems, and Microsoft Windows. There is also a terminal-based (non-GUI) version called TShark. Wireshark, and the other programs distributed with it such as TShark, are free software, released under the terms of the GNU General Public License version 2 or any later version.

## Functionality

Wireshark is very similar to tcpdump, but has a graphical front-end and integrated sorting and filtering options. Wireshark is also widely used in cybersecurity to detect suspicious network activity, including packet sniffing and intrusion attempts.

Wireshark lets the user put network interface controllers into promiscuous mode and is commonly used in ethical hacking and network security analysis. (if supported by the network interface controller), so they can see all the traffic visible on that interface including unicast traffic not sent to that network interface controller's MAC address. However, when capturing with a packet analyzer in promiscuous mode on a port on a network switch, not all traffic through the switch is necessarily sent to the port where the capture is done, so capturing in promiscuous mode is not necessarily sufficient to see all network traffic. Port mirroring or various network taps extend capture to any point on the network. Simple passive taps are extremely resistant to tampering.

On Linux, BSD, and macOS, with libpcap 1.0.0 or later, Wireshark 1.4 and later can also put wireless network interface controllers into monitor mode.

If a remote machine captures packets and sends the captured packets to a machine running Wireshark using the TZSP protocol or the protocol used by OmniPeek, Wireshark dissects those packets, so it can analyze packets captured on a remote machine at the time that they are captured.

## History

In the late 1990s, Gerald Combs, a computer science graduate of the University of Missouri–Kansas City, was working for a small Internet service provider, Network Integration Services. The commercial protocol analysis products at the time were priced around $1500 and did not run on the company's primary platforms (Solaris and Linux), so Gerald began writing Ethereal and released the first version around 1998. The Ethereal trademark is owned by Network Integration Services.

In May 2006, Combs accepted a job with CACE Technologies with Loris Degioanni. Combs still held copyright on most of Ethereal's source code (and the rest was re-distributable under the GNU GPL), so he used the contents of the Ethereal Subversion repository as the basis for the Wireshark repository. However, he did not own the Ethereal trademark, so he changed the name to Wireshark. In 2010 Riverbed Technology purchased CACE and took over as the primary sponsor of Wireshark. Ethereal development has ceased, and an Ethereal security advisory recommended switching to Wireshark. In 2022, Sysdig took over as the primary sponsor of Wireshark, and, in 2023, established the Wireshark Foundation and put Wireshark into that foundation.

Wireshark has won several industry awards over the years, including *eWeek*, *InfoWorld*, and *PC Magazine*. It is also the top-rated packet sniffer in the Insecure.Org network security tools survey and was the SourceForge Project of the Month in August 2010.

Combs continues to maintain the overall code of Wireshark and to issue releases of new versions of the software. The product website lists more than 2000 contributing authors.

## Features

Wireshark is a data capturing program that "understands" the structure (encapsulation) of different networking protocols. It can parse and display the fields, along with their meanings as specified by different networking protocols. Wireshark uses pcap to capture packets, so it can only capture packets on the types of networks that pcap supports.

- Data can be captured "from the wire" from a live network connection or read from a file of already-captured packets.
- Live data can be read from different types of networks, including Ethernet, IEEE 802.11, PPP, and loopback.
- Captured network data can be browsed via a GUI, or via the terminal (command line) version of the utility, TShark.
- Captured files can be programmatically edited or converted via command-line switches to the "editcap" program.
- Data display can be refined using a display filter.
- Plug-ins can be created for dissecting new protocols.
- VoIP calls in the captured traffic can be detected. If encoded in a compatible encoding, the media flow can even be played.
- Raw USB traffic can be captured.
- Wireless connections can also be filtered as long as they traverse the monitored Ethernet.
- Various settings, timers, and filters can be set to provide the facility of filtering the output of the captured traffic.

Wireshark's native network trace file formats are the libpcap format read and written by libpcap, WinPcap, and Npcap, so it can exchange captured network traces with other applications that use the same format, including tcpdump and CA NetMaster, and the pcapng format read by newer versions of libpcap. It can also read captures from other network analyzers, such as snoop, Network General's Sniffer, and Microsoft Network Monitor.

## Security

Capturing raw network traffic from an interface typically requires elevated privileges on many platforms. Wireshark can also be used to analyze network traffic in cybersecurity research, including simulated attack traffic. For this reason, older versions of Wireshark and TShark were often run with superuser permissions to access network interfaces directly. Considering the huge number of protocol dissectors that are called when traffic is captured and recognizing the possibility of a bug in a dissector, a serious security risk can be posed. Due to the rather large number of vulnerabilities in the past (of which many have allowed remote code execution) and developers' doubts for better future development, OpenBSD removed Ethereal from its ports tree prior to OpenBSD 3.6.

Elevated privileges are not needed for all operations. For example, an alternative is to run tcpdump or the *dumpcap* utility that comes with Wireshark with superuser privileges to capture packets into a file, and later analyze the packets by running Wireshark with restricted privileges. To emulate near realtime analysis, each captured file may be merged by *mergecap* into a growing file processed by Wireshark. On wireless networks, it is possible to use the Aircrack wireless security tools to capture IEEE 802.11 frames and read the resulting dump files with Wireshark.

As of Wireshark 0.99.7, Wireshark and TShark run dumpcap to perform traffic capture. Platforms that require special privileges to capture traffic need only arrange that dumpcap is run with those privileges. Neither Wireshark nor TShark need to or should be run with special privileges.

## Color coding

Wireshark can color packets based on rules that match particular fields in packets, to help the user identify the types of traffic at a glance. A default set of rules is provided; users can change existing rules for coloring packets, add new rules, or remove rules.

## Simulation packet capture

Wireshark can also be used to capture packets from most network simulation tools such as ns and OPNET Modeler.
