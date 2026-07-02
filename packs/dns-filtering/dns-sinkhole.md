---
title: "DNS sinkhole"
source: https://en.wikipedia.org/wiki/DNS_sinkhole
domain: dns-filtering
license: CC-BY-SA-4.0
tags: dns filtering, dns sinkhole, content filtering, protective dns
fetched: 2026-07-02
---

# DNS sinkhole

A **DNS sinkhole**, also known as a **sinkhole server**, **Internet sinkhole**, or **Blackhole DNS** is a Domain Name System (DNS) server that is configured to hand out non-routable addresses for a certain set of domain names. Computers that use the sinkhole fail to access the real site. The higher up the DNS resolution chain the sinkhole is, the more requests will fail, because of the greater number of lower nameservers that in turn serve a greater number of clients. Some of the larger botnets have been made unusable by top-level domain sinkholes that span the entire Internet. DNS Sinkholes are effective at detecting and blocking bots and other malicious traffic.

By default, the local hosts file on a computer is checked before DNS servers, and can be used to block sites in the same way.

## Applications

Sinkholes can be used both constructively, to contain threats such as WannaCry and Avalanche, and destructively, for example disrupting DNS services in a DoS attack.

DNS sinkholing can be used to protect users by intercepting DNS request attempting to connect to known malicious domains and instead returning an IP address of a sinkhole server defined by the DNS sinkhole administrator. One example of blocking malicious domains is to stop botnets, by interrupting the DNS names the botnet is programmed to use for coordination. Another use is to block ad serving sites, either using a host's file-based sinkhole or by locally running a DNS server (e.g., using a Pi-hole). Local DNS servers effectively block ads for all devices on the network.
