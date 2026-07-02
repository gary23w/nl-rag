---
title: "Infrastructure as a service"
source: https://en.wikipedia.org/wiki/Infrastructure_as_a_service
domain: aws-ec2
license: CC-BY-SA-4.0
tags: aws ec2, amazon ec2, elastic compute, cloud virtual machine
fetched: 2026-07-02
---

# Infrastructure as a service

**Infrastructure as a service** (**IaaS**) is a cloud computing service model where a cloud services vendor provides computing resources such as storage, network, servers, and virtualization (which emulates computer hardware). This service frees users from maintaining their own data center, but they must install and maintain the operating system and application software. IaaS provides users with high-level APIs to control details of the underlying network infrastructure, such as backup, data partitioning, scaling, security, and physical computing resources. Services can be scaled on-demand by the user. According to the Internet Engineering Task Force (IETF), such infrastructure is the most basic cloud-service model. IaaS can be hosted in a public cloud (where users share hardware, storage, and network devices), a private cloud (users do not share resources), or a hybrid cloud (combination of both).

## Overview

The US National Institute of Standards and Technology (NIST) defines infrastructure as a service as:

> The capability provided to the consumer is provision processing, storage, networks, as well as other fundamental computing resources where the consumer is able to deploy & run arbitrary software, which can include operating systems and applications. The consumer does not manage or control the underlying cloud infrastructure but has control over operating systems, storage, & deployed applications; and possibly limited control of select networking components (e.g., host firewalls).

IaaS clouds often offer additional resources such as a virtual-machine disk-image library, raw block storage, file or object storage, firewalls, load balancers, IP addresses, virtual local area networks (VLANs), and software bundles.

IaaS-cloud providers supply resources on-demand from the large pools of equipment installed in data centers. For wide-area connectivity, customers can use either the Internet or carrier clouds (dedicated virtual private networks, VPNs). To deploy their applications, users install operating-system images and the application software on the cloud infrastructure. Users patch and maintain the operating systems. IaaS services are typically billed as a utility: cost reflects the amount of resources allocated or consumed.

Typically, IaaS involves the use of a cloud orchestration technology such as OpenStack, Apache CloudStack, or OpenNebula. It manages the creation of a virtual machine (VM) and decides on the hypervisor (i.e. physical host) in order to start it. A hypervisor runs virtual machines (VMs) as guests. Pools of hypervisors in the cloud operational system can support large numbers of virtual machines and the ability to scale services up and down according to demand by customers. Hypervisors include Xen, Oracle VirtualBox, Oracle VM, KVM, VMware ESX/ESXi, or Microsoft Hyper-V. It also enables VM migration between hosts, allocates storage volumes, and attaches them to VMs that track usage information for billing.

An alternative to hypervisors is Linux containers, which run in isolated partitions of a Linux kernel that runs directly on the physical hardware. Containers are isolated, secured and managed using Linux cgroups and namespaces. Containerisation offers higher performance than virtualization because there is no hypervisor overhead.

## Economic impact

The global IaaS market is projected to reach a value of $411.9 billion by 2030, expanding at a compound annual growth rate (CAGR) of 22.6% from 2023 to 2030. This growth is primarily driven by the adoption of cloud-based infrastructure within the Banking, Financial Services, and Insurance (BFSI) sector, which employs these technologies to enhance scalability and reduce operational costs.

## Government usage

The UK Government encourages departments to use public cloud solutions as a first option. IaaS is in use within the UK Government but the technology community within government recommends consideration of Platform as a Service (PaaS) in cases where a department may not have IaaS skills and management capacity.
