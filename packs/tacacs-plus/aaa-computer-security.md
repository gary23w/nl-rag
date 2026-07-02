---
title: "Authentication, authorization, and accounting"
source: https://en.wikipedia.org/wiki/AAA_(computer_security)
domain: tacacs-plus
license: CC-BY-SA-4.0
tags: tacacs plus, device administration aaa, command authorization, network device auth
fetched: 2026-07-02
---

# Authentication, authorization, and accounting

(Redirected from

AAA (computer security)

)

**Authentication, authorization, and accounting** (AAA) is a framework used to control and track access within a computer network.

Authentication is concerned with proving identity, authorization with granting permissions, accounting with maintaining a continuous and robust audit trail via logging.

Common network protocols providing this functionality include TACACS+, RADIUS, and Diameter.

## Disambiguation

In some related but distinct contexts, the term AAA has been used to refer to protocol-specific information. For example, Diameter uses the URI scheme AAA, which also stands for "Authentication, Authorization and Accounting", as well as the Diameter-based Protocol AAAS, which stands for "Authentication, Authorization and Accounting with Secure Transport". These protocols were defined by the Internet Engineering Task Force in RFC 6733 and are intended to provide an AAA framework for applications, such as network access or IP mobility in both local and roaming situations.

However, the AAA paradigm is used more widely in the computer security industry.

## Usage of AAA servers in CDMA networks

AAA servers in CDMA data networks are entities that provide Internet Protocol (IP) functionality to support the functions of authentication, authorization and accounting. The AAA server in the CDMA wireless data network architecture is similar to the HLR in the CDMA wireless voice network architecture.

Types of AAA servers include the following:

- **Access Network AAA (AN-AAA)**: Communicates with the RNC in the Access Network (AN) to enable authentication and authorization functions to be performed at the AN. The interface between AN and AN-AAA is known as the A12 interface.
- **Broker AAA (B-AAA)**: Acts as an intermediary to proxy AAA traffic between roaming partner networks (i.e., between the H-AAA server in the home network and V-AAA server in the serving network). B-AAA servers are used in CRX networks to enable CRX providers to offer billing settlement functions.
- **Home AAA (H-AAA)**: The AAA server in the roamer's home network. The H-AAA is similar to the HLR in voice. The H-AAA stores user profile information, responds to authentication requests, and collects accounting information.
- **Visited AAA (V-AAA)**: The AAA server in the visited network from which a roamer is receiving service. The V-AAA in the serving network communicates with the H-AAA in a roamer's home network. Authentication requests and accounting information are forwarded by the V-AAA to the H-AAA, either directly or through a B-AAA.

Current AAA servers communicate using the RADIUS protocol. As such, TIA specifications refer to AAA servers as RADIUS servers. While at one point it was expected that Diameter was to replace RADIUS, that has not happened. Diameter is largely used only in the mobile (3G/4G/5G) space, and RADIUS is used everywhere else.

The behavior of AAA servers (radius servers) in the CDMA2000 wireless IP network is specified in TIA-835.
