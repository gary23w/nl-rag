---
title: "Multi-user MIMO"
source: https://en.wikipedia.org/wiki/Multi-user_MIMO
domain: radio-access-network
license: CC-BY-SA-4.0
tags: radio access network, cloud ran, base station, mobile backhaul
fetched: 2026-07-02
---

# Multi-user MIMO

**Multi-user MIMO** (**MU-MIMO**) is a family of multiple-input and multiple-output (MIMO) techniques in which a wireless communication system communicates with multiple users at the same time by using the spatial dimension of the radio channel. In a typical MU-MIMO system, a base station, access point, or other multi-antenna device transmits to, or receives from, several user devices over the same time-frequency resources.

MU-MIMO extends single-user MIMO (SU-MIMO), where one multi-antenna transmitter communicates with one multi-antenna receiver. It is closely related to space-division multiple access (SDMA), because users are separated by their spatial channel characteristics rather than only by time, frequency, or code resources.

MU-MIMO is used in cellular networks and wireless LAN systems, and is related to techniques such as massive MIMO, coordinated multipoint transmission and reception (CoMP), and cooperative MIMO.

## Overview

In SU-MIMO, the antennas used for spatial multiplexing usually belong to one transmitter and one receiver. In MU-MIMO, the spatial streams may be assigned to different users. This can increase system throughput when the users have sufficiently distinct channel conditions.

MU-MIMO systems are commonly described using two channel models:

- **MIMO broadcast channel** (MIMO BC), used for downlink communication from one transmitter, such as a base station or access point, to multiple users.
- **MIMO multiple-access channel** (MIMO MAC), used for uplink communication from multiple users to one receiver, such as a base station or access point.

The performance of MU-MIMO depends on the number of antennas, the accuracy of channel state information, scheduling, interference management, and the signal-processing techniques used at the transmitter and receiver.

## MIMO broadcast channel

The **MIMO broadcast channel** describes a downlink system in which one multi-antenna transmitter sends data to multiple receivers. In wireless networks, this transmitter is commonly a base station or access point.

Downlink MU-MIMO usually requires the transmitter to have channel state information at the transmitter (CSIT). This information is used for user scheduling, beamforming, and precoding. If the transmitter has accurate CSIT, it can direct different spatial streams toward different users while reducing interference between them.

Precoding methods for the MIMO broadcast channel include dirty paper coding, zero-forcing precoding, block diagonalization, and other linear or hybrid precoding techniques.

## MIMO multiple-access channel

The **MIMO multiple-access channel** describes an uplink system in which multiple users transmit to one multi-antenna receiver. In cellular systems, the receiver is usually a base station; in wireless local-area networks, it may be an access point.

Uplink MU-MIMO relies on receiver-side processing to separate the users' signals. Techniques include joint detection, interference cancellation, and SDMA-based scheduling. Channel state information at the receiver (CSIR) is typically obtained from uplink pilot or reference signals. Compared with downlink CSIT, receiver-side channel estimation is often simpler because the receiver can directly estimate the channels from the transmitted pilots.

MIMO MAC systems can outperform point-to-point MIMO systems when the receiver has enough antennas and processing capability to separate signals from multiple users.

Several wireless technologies are closely related to MU-MIMO.

**Space-division multiple access** uses spatial separation to serve multiple users over the same time-frequency resources. MU-MIMO can be considered an implementation of SDMA in multi-antenna systems.

**Massive MIMO** uses a large number of antennas, usually at a base station, to serve many users simultaneously. Massive MIMO systems often use MU-MIMO principles, but at a larger antenna scale.

**Coordinated multipoint** systems coordinate transmission or reception across multiple base stations or access points. These systems can reduce inter-cell interference and improve performance for users near cell edges.

**Cooperative MIMO**, also called **network MIMO** or **ad hoc MIMO**, uses antennas distributed across multiple cooperating nodes rather than antennas located on one device. This approach is related to cooperative diversity, relay networks, and distributed antenna systems.
