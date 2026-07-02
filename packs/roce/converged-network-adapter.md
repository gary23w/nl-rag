---
title: "Converged network adapter"
source: https://en.wikipedia.org/wiki/Converged_network_adapter
domain: roce
license: CC-BY-SA-4.0
tags: rdma over converged ethernet, lossless ethernet, priority flow control, data center bridging
fetched: 2026-07-02
---

# Converged network adapter

A **converged network adapter** (**CNA**), also called a converged network interface controller (C-NIC), is a computer input/output device that combines the functionality of a host bus adapter (HBA) with a network interface controller (NIC). In other words, it "converges" access to, respectively, a storage area network and a general-purpose computer network.

## Support

Some products were marketed around 2005 with the term C-NIC which combined iSCSI storage functionality with Gigabit Ethernet. Later products used the marketing term converged network adapter (CNA), combining Fibre Channel over Ethernet with 10 Gigabit Ethernet, for example.

### Brocade

Brocade Communications Systems offers two types of CNAs, with PCI Express generation 2.0 interfaces. The only difference between the two models are the number of interfaces on the cards: one or two. The two port model will allow connection to two different switches to create a redundant configuration without having to use two PCI slots.

### Broadcom

In 2009 Broadcom entered the CNA market. Broadcom offers their CNAs under their own brand name but also sell the application-specific integrated circuits and other related components to others. Their intended customers are the larger builders of server systems such as Dell and HP. These vendors can then include the ten Gigabit CNA with their servers: as embedded interface on the motherboard (LOM or LAN on motherboard), via a mezzanine card in blade servers or as PCI extension-card.

### Emulex

Emulex offers CNAs under the Emulex brand name as the OneConnect ten Gigabit series of dual port optical and copper adapters. They also OEM their adapters for Cisco, Dell, EMC, Fujitsu, HDS, HP, IBM and NetApp.

### QLogic

QLogic offers CNAs via their QLogic 8200 & 8300 series Converged Network Adapters. They offer single and dual port PCI cards with copper or optical fibre interfaces. QLogic CNAs are available under the QLogic brandname and as OEM cards. The QME CNA and drivers were supported by Citrix, NetApp, EMC and IBM.

### Hewlett-Packard

HP claims that their BL460c G7 was the first blade server that offers FCoE via a *LOM* (LAN on motherboard) instead of using a PCI slot or mezzanine card.

### Dell

Dell uses the QLogic 8100 series in their PowerEdge servers. For the M-series, blade-servers for the M1000e use the custom made dual-port mezzanine card QME8142. For the normal tower and rack servers Dell offers an OEM version of the standard QME8152.

### Cisco

Cisco Systems offered Fibre Channel over Ethernet in their Unified Computing System product line via *Virtual Interface Cards* (VICs). These cards make it possible to create multiple virtual HBAs or NICs within each physical VIC.

### Intel

Intel demonstrates how the term *Converged Network Adapter* is really a marketing term, as they sell the X710-DA2/DA4 adapters that don't actually support FCoE.
