---
title: "DDoS mitigation"
source: https://en.wikipedia.org/wiki/DDoS_mitigation
domain: ddos-defense
license: CC-BY-SA-4.0
tags: ddos mitigation, denial of service attack, distributed denial of service, rate limiting, syn flood defense
fetched: 2026-07-02
---

# DDoS mitigation

**DDoS mitigation** is a set of network management techniques and tools for resisting or mitigating the impact of distributed denial-of-service (DDoS) attacks on networks attached to the Internet by protecting the target and relay networks. DDoS attacks are a constant threat to businesses and organizations, delaying service performance or shutting down websites entirely.

DDoS mitigation works by identifying baseline conditions for network traffic by analyzing "traffic patterns" to allow threat detection and alerting. DDoS mitigation also requires identifying incoming traffic to separate human traffic from human-like bots and hijacked web browsers. This process involves comparing signatures and examining different attributes of the traffic, including IP addresses, cookie variations, HTTP headers, and browser fingerprints.

After the attack is detected, the next process is filtering. Filtering can be done through anti-DDoS technology like connection tracking, IP reputation lists, deep packet inspection, blacklisting/whitelisting, or rate limiting.

One technique is to pass network traffic addressed to a potential target network through high-capacity networks, with "traffic scrubbing" filters.

Manual DDoS mitigation is no longer recommended due to the size of attacks often outstripping the human resources available in many firms/organizations. Other methods to prevent DDoS attacks can be implemented such as on-premises or cloud-based solution providers. On-premises mitigation technology (most commonly a hardware device) is often placed in front of the network. This would limit the maximum bandwidth available to what is provided by the Internet service provider. Common methods involve hybrid solutions, by combining on-premises filtering with cloud-based solutions.

## Methods of attack

DDoS attacks are executed against websites and networks of selected victims. A number of vendors offer "DDoS-resistant" hosting services, mostly based on techniques similar to content delivery networks. Distribution avoids a single point of congestion and prevents the DDoS attack from concentrating on a single target.

One technique of DDoS attacks is to use misconfigured third-party networks, allowing the amplification of spoofed UDP packets. Proper configuration of network equipment, enabling ingress filtering and egress filtering, as documented in BCP 38 and RFC 6959, prevents amplification and spoofing, thus reducing the number of relay networks available to attackers.

DDoS attacks are typically categorized into three types: volumetric, protocol-based, and application-layer attacks.

**Volumetric attacks**

These attacks aim to consume bandwidth by flooding a network or service with massive volumes of traffic.

- UDP floods target random ports with UDP packets, causing the host to repeatedly search for non-existent applications and reply with ICMP errors.
- ICMP floods overwhelm the target with ping requests, exhausting available processing power and bandwidth.
- DNS amplification involves exploiting open DNS resolvers to send amplified traffic to the victim using spoofed requests.

**Protocol attacks**

These focus on exhausting resources of network infrastructure by misusing communication protocol behavior.

- SYN floods exploit the TCP handshake by initiating multiple half-open connections, overwhelming the server's connection table.
- Ping of Death uses oversized or malformed ping packets to crash or destabilize systems.
- Smurf attacks send spoofed ICMP requests to broadcast addresses, prompting all devices on the network to respond to the victim’s IP.

**Application layer attacks**

These attacks mimic legitimate traffic to deplete application server resources, making them particularly difficult to detect.

- HTTP floods send large numbers of GET or POST requests, overloading servers with processing demands.
- Slowloris maintains many open connections to a web server by sending partial requests slowly, exhausting server threads.
- DNS query floods overwhelm DNS servers with rapid requests, preventing legitimate domain resolution.

## Methods of mitigation

- Use of Client Puzzle Protocol, or guided tour puzzle protocol
- Use of content delivery networks
- Blacklisting of IP addresses
- Use of intrusion detection systems and firewalls

## Mitigation validation

DDoS mitigation defenses such as traffic scrubbing, rate limiting, and content delivery networks require continuous validation to confirm they are performing as intended. Mitigation tools can produce false positives, blocking legitimate users by misidentifying their traffic as malicious, and gaps in filtering rules can go undetected until an actual attack causes service disruption.

Continuous DDoS testing addresses this by running nondisruptive attack simulations against operational services across each layer of the mitigation stack, providing ongoing visibility into how many packets mitigation solutions are dropping, what level of service remains available under attack conditions, and whether scrubbing and filtering thresholds are calibrated to current traffic baselines. This type of testing also generates auditable reporting that aligns DDoS risk management with business continuity and regulatory objectives.
