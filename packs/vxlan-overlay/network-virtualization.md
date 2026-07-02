---
title: "Network virtualization"
source: https://en.wikipedia.org/wiki/Network_virtualization
domain: vxlan-overlay
license: CC-BY-SA-4.0
tags: vxlan overlay, network overlay, layer 2 tunneling, network virtualization
fetched: 2026-07-02
---

# Network virtualization

In computing, **network virtualization** is the process of combining hardware and software network resources and network functionality into a single, software-based administrative entity, a **virtual network**. Network virtualization involves platform virtualization, often combined with resource virtualization.

Network virtualization is categorized as either **external virtualization**, combining many networks or parts of networks into a virtual unit, or **internal virtualization**, providing network-like functionality to software containers on a single network server.

In software testing, software developers use network virtualization to test software which are under development in a simulation of the network environments in which the software is intended to operate. As a component of application performance engineering, network virtualization enables developers to emulate connections between applications, services, dependencies, and end users in a test environment without having to physically test the software on all possible hardware or system software. The validity of the test depends on the accuracy of the network virtualization in emulating real hardware and operating systems.

## Components

Various equipment and software vendors offer network virtualization by combining any of the following:

- Network hardware, such as switches and network adapters, also known as network interface cards (NICs)
- Network elements, such as firewalls and load balancers
- Networks, such as virtual LANs (VLANs) and containers such as virtual machines (VMs)
- Network storage devices
- Network machine-to-machine elements, such as telecommunications devices
- Network mobile elements, such as laptop computers, tablet computers, and smartphones
- Network media, such as Ethernet and Fibre Channel

## External virtualization

External network virtualization combines or subdivides one or more local area networks (LANs) into virtual networks to improve a large network's or data center's efficiency. A virtual local area network (VLAN) and network switch comprise the key components. Using this technology, a system administrator can configure systems physically attached to the same local network into separate virtual networks. Conversely, an administrator can combine systems on separate local area networks (LANs) into a single VLAN spanning segments of a large network.

External network virtualization is envisioned to be placed in the middle of the network stack and help integrating different architectures proposed for next generation networks.

## Internal virtualization

**Internal network virtualization** configures a single system with OS-level virtualization, such as Xen hypervisor control programs, or pseudo-interfaces, such as a VNIC, to emulate a physical network with software. This can improve a single system's efficiency by isolating applications to separate containers or pseudo-interfaces.

### Examples

Citrix and Vyatta have built a virtual network protocol stack combining Vyatta's routing, firewall, and VPN functions with Citrix's Netscaler load balancer, branch repeater wide area network (WAN) optimization, and secure sockets layer VPN.

OpenSolaris network virtualization provides a so-called "network in a box" (see OpenSolaris Network Virtualization and Resource Control).

Microsoft Virtual Server uses virtual machines to make a "network in a box" for x86 systems. These containers can run different operating systems, such as Microsoft Windows or Linux, either associated with or independent of a specific network interface controller (NIC).

## Use in testing

Network virtualization may be used in application development and testing to mimic real-world hardware and system software. In application performance engineering, network virtualization enables emulation of connections between applications, services, dependencies, and end users for software testing.

## Wireless network virtualization

Wireless network virtualization can have a very broad scope ranging from spectrum sharing, infrastructure virtualization, to air interface virtualization. Similar to wired network virtualization, in which physical infrastructure owned by one or more providers can be shared among multiple service providers, wireless network virtualization needs the physical wireless infrastructure and radio resources to be abstracted and isolated to a number of virtual resources, which then can be offered to different service providers. In other words, virtualization, regardless of wired or wireless networks, can be considered as a process splitting the entire network system. However, the distinctive properties of the wireless environment, in terms of time-various channels, attenuation, mobility, broadcast, etc., make the problem more complicated. Furthermore, wireless network virtualization depends on specific access technologies, and wireless network contains much more access technologies compared to wired network virtualization and each access technology has its particular characteristics, which makes convergence, sharing and abstraction difficult to achieve. Therefore, it may be inaccurate to consider wireless network virtualization as a subset of network virtualization.

## Performance

Until 1 Gbit/s networks, network virtualization was not suffering from the overhead of the software layers or hypervisor layers providing the interconnects. With the rise of high bandwidth, 10 Gbit/s and beyond, the rates of packets exceed the capabilities of processing of the networking stacks. In order to keep offering high throughput processing, some combinations of software and hardware helpers are deployed in the so-called "network in a box" associated with either a hardware-dependent network interface controller (NIC) using SRIOV extensions of the hypervisor or either using a fast path technology between the NIC and the payloads (virtual machines or containers).

For example, in case of Openstack, network is provided by Neutron which leverages many features from the Linux kernel for networking: iptables, iproute2, L2 bridge, L3 routing or OVS. Since the Linux kernel cannot sustain the 10G packet rate, then some bypass technologies for a fast path are used. The main bypass technologies are either based on a limited set of features such as Open vSwitch (OVS) with its DPDK user space implementation or based on a full feature and offload of Linux processing such as 6WIND virtual accelerator.
