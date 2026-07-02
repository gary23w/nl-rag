---
title: "Class of service"
source: https://en.wikipedia.org/wiki/Class_of_service
domain: diffserv
license: CC-BY-SA-4.0
tags: differentiated services, per-hop behavior, traffic classification, explicit congestion notification
fetched: 2026-07-02
---

# Class of service

**Class of service** (**COS** or **CoS**) is a parameter used in data and voice protocols to differentiate the types of payloads contained in the packet being transmitted. The objective of such differentiation is generally associated with assigning priorities to the data payload or access levels to the telephone call.

## Data services

As related to network technology, COS is a 3-bit field that is present in an Ethernet frame header when 802.1Q VLAN tagging is present. The field specifies a priority value between 0 and 7, more commonly known as CS0 through CS7, that can be used by quality of service (QoS) disciplines to differentiate and shape/police network traffic.

COS operates only on 802.1Q VLAN Ethernet at the data link layer (layer 2), while other QoS mechanisms (such as DiffServ, also known as DSCP) operate at the IP network layer (layer 3) or use a local QoS tagging system that does not modify the actual packet, such as Cisco's "QoS-Group".

Network devices (i.e., routers, switches, etc.) can be configured to use existing COS values on incoming packets from other devices (trust mode) or can rewrite the COS value to something completely different. Most Internet Service Providers do not trust incoming QoS markings from their customers, so COS is generally limited to use within an organization's intranet.

Service providers offering private-line WAN services will typically offer services that can utilize COS/QoS.

## Voice services

As related to legacy telephone systems, COS is often used to define the permissions an extension will have on a PBX or Centrex. Certain groups of users may have a need for extended voicemail message retention, while another group may need the ability to forward calls to a cell phone, and still others have no need to make calls outside the office. Permissions for a group of extensions can be changed by modifying a COS variable applied to the entire group.

COS is also used on trunks to define if they are full-duplex, incoming only, or outgoing only.

## Classification of service

The term can be used generically to refer to the classification of network traffic within network equipment based on packet inspection. Cisco implements such classification through either access-lists or Network-Based Application Recognition (NBAR). NBAR works with the existing QoS system.
