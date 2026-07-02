---
title: "IEEE 802.1Q"
source: https://en.wikipedia.org/wiki/IEEE_802.1Q
domain: ieee-802-1-tsn
license: CC-BY-SA-4.0
tags: ieee 802.1 tsn, stream reservation, frame preemption, credit-based shaper
fetched: 2026-07-02
---

# IEEE 802.1Q

**IEEE 802.1Q**, often referred to as **Dot1q**, is the networking standard that supports virtual local area networking (VLANs) on an IEEE 802.3 Ethernet network. The standard defines a system of **VLAN tagging** for Ethernet frames and the accompanying procedures to be used by bridges and switches in handling such frames. The standard also contains provisions for a quality-of-service prioritization scheme commonly known as IEEE 802.1p and defines the Generic Attribute Registration Protocol.

Portions of the network that are VLAN-aware (i.e., IEEE 802.1Q conformant) can include VLAN tags. When a frame enters the VLAN-aware portion of the network, a tag is added to represent the VLAN membership. Each frame must be distinguishable as being within exactly one VLAN. A frame in the VLAN-aware portion of the network that does not contain a VLAN tag is assumed to be flowing on the **native VLAN**.

The standard was developed by IEEE 802.1, a working group of the IEEE 802 standards committee, and continues to be actively revised with notable amendments including IEEE 802.1ad, IEEE 802.1ak and IEEE 802.1s. The 802.1Q-2014 revision incorporated the IEEE 802.1D-2004 standard, which originally defined bridging and Spanning Tree Protocol.

## Frame format

Insertion of 802.1Q tag in an Ethernet frame

802.1Q adds a 32-bit field between the source MAC address and the EtherType fields of the original frame. Under 802.1Q, the maximum frame size is extended from 1,518 bytes to 1,522 bytes. The minimum frame size remains 64 bytes, but a bridge may extend the minimum frame size from 64 to 68 bytes on transmission. This allows a tag to be popped without needing additional padding. Two bytes are used for the tag protocol identifier (TPID), the other two bytes for tag control information (TCI). The TCI field is further divided into PCP, DEI, and VID.

| 16 bits | 3 bits | 1 bit | 12 bits |
|---|---|---|---|
| TPID | TCI |   |   |
| PCP | DEI | VID |   |

**Tag protocol identifier (TPID)**

A 16-bit field set to a value of 0x8100

in order to identify the frame as an IEEE 802.1Q-tagged frame. This field is located at the same position as the EtherType field in untagged frames, and is thus used to distinguish the frame from untagged frames.

**Tag control information (TCI)**

A 16-bit field containing the following sub-fields:

**Priority code point (PCP)**

A 3-bit field which refers to the

IEEE 802.1p

class of service (CoS)

and maps to the frame priority level. Different PCP values can be used to prioritize different classes of traffic.

**Drop eligible indicator (DEI)**

A 1-bit field. (formerly CFI

) May be used separately or in conjunction with PCP to indicate frames eligible to be dropped in the presence of congestion.

**VLAN identifier (VID)**

A 12-bit field specifying the VLAN to which the frame belongs. The values of 0 and 4095 (0x000 and 0xFFF in

hexadecimal

) are reserved. All other values may be used as VLAN identifiers, allowing up to 4,094 VLANs. The reserved value 0x000 indicates that the frame does not carry a VLAN ID; in this case, the 802.1Q tag specifies only a priority (in PCP and DEI fields) and is referred to as a

priority tag

. On bridges, VID 0x001 (the default VLAN ID) is often reserved for a

network management

VLAN; this is vendor-specific. The VID value 0xFFF is reserved for implementation use; it must not be configured or transmitted. 0xFFF can be used to indicate a wildcard match in management operations or filtering database entries.

For frames (other than 802.3 frames) using Subnetwork Access Protocol (SNAP) encapsulation with an organizationally unique identifier (OUI) field of 00-00-00 (so that the protocol ID field in the SNAP header is an EtherType as specified in RFC 1042), the EtherType value in the SNAP header is set to 0x8100 and the aforementioned extra 4 bytes are appended after the SNAP header. In other words, the VLAN tag follows the SNAP header. For 802.3 frames in LLC-SNAP format, the order is opposite; the VLAN tag is placed *before* the LLC-SNAP header.

Because inserting the VLAN tag changes the frame, 802.1Q encapsulation forces a recalculation of the original frame check sequence field in the Ethernet trailer.

The IEEE 802.3ac standard increased the maximum Ethernet frame size from 1518 bytes to 1522 bytes to accommodate the four-byte VLAN tag. Some network devices that do not support the larger frame size will process these frames successfully but may report them as *baby giant* anomalies.

### Double tagging

IEEE 802.1ad introduced the concept of double tagging. Double tagging can be useful for Internet service providers (ISPs), allowing them to use their VLANs internally while carrying traffic from clients that is already VLAN tagged. The outer (next to the source MAC and representing ISP VLAN) S-TAG (service tag) comes first, followed by the inner C-TAG (customer tag). In such cases, 802.1ad specifies a TPID of 0x88a8 for service-provider outer S-TAG.

Insertion of 802.1ad double tag in an Ethernet frame

## Other protocols

IEEE 802.1Q defines the Multiple VLAN Registration Protocol (MVRP), an application of the Multiple Registration Protocol, allowing bridges to negotiate the set of VLANs to be used over a specific link. MVRP replaced the slower GARP VLAN Registration Protocol (GVRP) in 2007 with the IEEE 802.1ak-2007 amendment.

The 2003 revision of the standard was the first to include the Multiple Spanning Tree Protocol (MSTP), which was originally defined in IEEE 802.1s.
