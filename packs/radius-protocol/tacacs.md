---
title: "TACACS"
source: https://en.wikipedia.org/wiki/TACACS
domain: radius-protocol
license: CC-BY-SA-4.0
tags: radius protocol, aaa authentication, diameter protocol, access accounting
fetched: 2026-07-02
---

# TACACS

**Terminal Access Controller Access-Control System** (**TACACS**, /ˈtækæks/) refers to a family of related protocols handling remote authentication and related services for network access control through a centralized server. The original **TACACS** protocol, which dates back to 1984, was used for communicating with an authentication server, common in older UNIX networks including but not limited to the ARPANET, MILNET and BBNNET. It spawned related protocols:

- **Extended TACACS** (**XTACACS**) is a proprietary extension to TACACS introduced by Cisco Systems in 1990 without backwards compatibility to the original protocol. TACACS and XTACACS both allow a remote access server to communicate with an authentication server in order to determine if the user has access to the network.
- **TACACS Plus** (**TACACS+**) is a protocol developed by Cisco and released as an open standard beginning in 1993. Although derived from TACACS, TACACS+ is a separate protocol that handles authentication, authorization, and accounting (AAA) services. TACACS+ has largely replaced its predecessors.

## History

TACACS was originally developed in 1984 by BBN, later known as BBN Technologies, for administration of ARPANET and MILNET, which ran unclassified network traffic for DARPA at the time and would later evolve into the U.S. Department of Defense's NIPRNet. Originally designed as a means to automate authentication – allowing someone who was already logged into one host in the network to connect to another on the same network without needing to re-authenticate – it was first formally described by BBN's Brian Anderson TAC Access Control System Protocols, BBN Tech Memo CC-0045 with minor TELNET double login avoidance change in December 1984 in IETF RFC 927. Cisco Systems began supporting TACACS in its networking products in the late 1980s, eventually adding several extensions to the protocol. In 1990, Cisco's extensions on top of TACACS became a proprietary protocol called Extended TACACS (XTACACS). Although TACACS and XTACACS are not open standards, Craig Finseth of the University of Minnesota, with Cisco's assistance, published a description of the protocols in 1993 as IETF RFC 1492 for informational purposes.

## Technical descriptions

### TACACS

TACACS is defined in RFC 1492, and uses (either TCP or UDP) port 49 by default. TACACS allows a client to accept a username and password and send a query to a TACACS authentication server, sometimes called a TACACS daemon. It determines whether to accept or deny the authentication request and sends a response back. The TIP (routing node accepting dial-up line connections, which the user would normally want to log in into) would then allow access or not, based upon the response. In this way, the process of making the decision is "opened up" and the algorithms and data used to make the decision are under the complete control of whoever is running the TACACS daemon.

### XTACACS

Extended TACACS (XTACACS) extends the TACACS protocol with additional functionality. It also separates the authentication, authorization, and accounting (AAA) functions out into separate processes, allowing them to be handled by separate servers and technologies.

### TACACS+

TACACS+ is a Cisco-designed extension to TACACS that is described in RFC 8907. TACACS+ includes a mechanism that can be used to obfuscate the body of each packet, while leaving the header clear-text. Moreover, it provides granular control in the form of command-by-command authorization.

TACACS+ has generally replaced TACACS and XTACACS in more recently built or updated networks. TACACS+ is an entirely new protocol which is not compatible with its predecessors, TACACS and XTACACS.

### Comparison with RADIUS

There are a number of differences between the two protocols which make them substantially different in normal usage.

TACACS+ can only use TCP, while RADIUS normally operates over UDP, but can also use TCP (RFC6613), and for additional security, TLS (RFC 6614) and DTLS (RFC7360).

TACACS+ can operate in two modes. One mode is where all traffic including passwords are sent in clear-text, and the only security is IP address filtering. The other mode is data obfuscation (RFC 8907 Section 4.5), where the packet header is clear-text, but the body including passwords is obfuscated with an MD5-based method. The MD5-based obfuscation method is similar to that used for the RADIUS User-Password attribute (RFC 2865 Section 5.2), and therefore has similar security properties.

Another difference is that TACACS+ is used only for administrator access to networking equipment, while RADIUS is most often used for end-user authentication. TACACS+ supports "command authorization", where an administrator can log in to a piece of networking equipment, and attempt to issue commands. The equipment will use TACACS+ to send each command to a TACACS+ server, which can choose to authorize, or reject the command.

Similar functionality exists in RADIUS in RFC 5607, but support for that standard appears to be poor or non-existent.

TACACS+ offers robust functionality for administrator authentication and command authorization, but is essentially never used for authenticating end-user access to networks. In contrast, RADIUS offers minimal functionality for administrator authentication and command authorization, while offering strong support (and is widely used) for end-user authentication, authorization, and accounting.

As such, the two protocols have little overlap in functionality or in common usage.

## Standards documents

- RFC 927 – TACACS User Identification Telnet Option
- RFC 1492 – An Access Control Protocol, Sometimes Called TACACS
- RFC 8907 – The Terminal Access Controller Access-Control System Plus (TACACS+) Protocol
- RFC 9105 – A YANG Data Model for Terminal Access Controller Access-Control System Plus (TACACS+)
