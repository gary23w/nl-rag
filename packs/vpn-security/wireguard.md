---
title: "WireGuard"
source: https://en.wikipedia.org/wiki/WireGuard
domain: vpn-security
license: CC-BY-SA-4.0
tags: virtual private network, vpn tunneling protocol, ipsec vpn, wireguard protocol, split tunneling
fetched: 2026-07-02
---

# WireGuard

**WireGuard** is a communication protocol and free and open-source software that implements encrypted virtual private networks (VPNs). It aims to be lighter and better performing than IPsec and OpenVPN, two common tunneling protocols. The WireGuard protocol passes traffic over UDP.

In March 2020, the Linux version of the software reached a stable production release and was incorporated into the Linux 5.6 kernel, and backported to earlier Linux kernels in some Linux distributions. The Linux kernel components are licensed under the GNU General Public License (GPL) version 2; other implementations are under GPLv2 or other free/open-source licenses.

## Protocol

The WireGuard protocol is a variant of the Noise Protocol Framework `IK` handshake pattern. The key exchange, or handshake, combines long-term and ephemeral Diffie-Hellman values using Curve25519. Each pair generates a set of public and private key pairs using Curve 25519, the public keys are exchanged, with each pair then assigned an IP address (generally RFC 1918) to utilize with the WireGuard tunnel. Once the keys have been confirmed by both peers, the Noise Protocol is used to generate a shared ChaCha20 session key for symmetric encryption authenticated with Poly1305. SipHash24 is used for hashtable keys while BLAKE2s cryptographic hash functions, a faster and more compact version of SHA-3, are incorporated. Key derivation functions are handled using HKDF and Base64-encoded private keys, public keys and preshared keys.

WireGuard’s proof starts by modeling its two-message Noise-based handshake (plus optional PSK) in CryptoVerif’s calculus of cryptographic games, abstracting ChaCha20-Poly1305, Curve25519, HKDF, the hash chain, and related primitives under standard IND-CPA/INT-CTXT and random-oracle assumptions. From that model, CryptoVerif’s automated game hops show, across unlimited parallel sessions, that the protocol guarantees mutual authentication, IND-CCA session-key secrecy, forward secrecy and post-compromise security even if long-term keys later leak and state is wiped. In May 2019, researchers from INRIA published a machine-checked proof of the WireGuard protocol, produced using the CryptoVerif proof assistant.

### Optional pre-shared symmetric key mode

WireGuard supports pre-shared symmetric key mode, which provides an additional layer of symmetric encryption to mitigate future advances in quantum computing. This addresses the risk that traffic may be stored until quantum computers are capable of breaking Curve25519, at which point traffic could be decrypted. Pre-shared keys are "usually troublesome from a key management perspective and might be more likely stolen", but in the shorter term, if the symmetric key is compromised, the Curve25519 keys still provide more than sufficient protection.

### Networking

WireGuard uses only UDP, due to the potential disadvantages of TCP-over-TCP. Tunneling TCP over a TCP-based connection can induce a dramatic loss in transmission performance due to the TCP meltdown problem.

Its default server port is UDP 51820.

WireGuard fully supports IPv6, both inside and outside of tunnel. It supports only layer 3 for both IPv4 and IPv6 and can encapsulate v4-in-v6 and vice versa.

#### MTU overhead

The overhead of WireGuard breaks down as follows:

- 20-byte IPv4 header or 40-byte IPv6 header
- 8-byte UDP header
- 4-byte type
- 4-byte key index
- 8-byte nonce
- *n*-byte encrypted data
- 16-byte authentication tag

#### MTU operational considerations

Assuming the underlay network transporting the WireGuard packets maintains a 1500 byte MTU, configuring the WireGuard interface to 1420 bytes MTU for all involved peers is ideal for being transported over IPv6 + IPv4. However, when exclusively utilizing legacy IPv4 transport, a higher MTU of 1440 bytes for the WireGuard interface suffices.

From an operational perspective and for network configuration uniformity, leaving the default 1420 byte MTU network-wide for the WireGuard interfaces would be advantageous. This approach ensures consistency and facilitates a smoother transition to enabling IPv6 for the WireGuard peers and interfaces in the future.

However, for mobile clients with varying forms of network connectivity and varying MTU across numerous network connections, an MTU of 1280 can be beneficial allowing for IPv6 transport inside the tunnel as that is its minimum allowed MTU, and allow the WireGuard tunnel to function over most forms of connectivity. Hosts often avoid sending packets > 1280 due to PMTUD reliability.

The MTU of a WireGuard interface is determined by the encapsulating, or *outer*, IP protocol—not the IP version carried inside the tunnel. When WireGuard packets are transported over IPv4, the outer-header overhead is 60 bytes (20-byte IPv4 header, 8-byte UDP header, and 32-byte WireGuard header). When transported over IPv6, the outer-header overhead rises to 80 bytes. This distinction means that even if a peer is reachable only via IPv4, other peers in the same mesh may connect over IPv6 or through translation mechanisms. Translation increases header size and enforces IPv6’s 1280-byte minimum path MTU, requiring that implementers budget for the 80-byte IPv6 overhead when setting a consistent interface MTU.

### Extensibility

WireGuard is designed to be extended by third-party programs and scripts. This has been used to augment WireGuard with various features including more user-friendly management interfaces (including easier setting up of keys), logging, dynamic firewall updates, dynamic IP assignment, and LDAP integration. It is supported natively and by a number of commercial VPN services such as NordVPN, IPVanish, Mullvad, and TunnelBear. One WireGuard-based fork, AmneziaWG, adds traffic-obfuscation mechanisms intended to make WireGuard traffic less identifiable to deep packet inspection systems.

Excluding such complex features from the minimal core codebase improves its stability and security. For ensuring security, WireGuard restricts the options for implementing cryptographic controls, limits the choices for key exchange processes, and maps algorithms to a small subset of modern cryptographic primitives. If a flaw is found in any of the primitives, a new version can be released that resolves the issue.

## Reception

A review by *Ars Technica* found that WireGuard was easy to set up and use, used strong ciphers, and had a minimal codebase that provided for a small attack surface. The review included a quote from Linus Torvalds who stated:

> "Can I just once again state my love for [WireGuard] and hope it gets merged soon? Maybe the code isn't perfect, but I've skimmed it, and compared to the horrors that are OpenVPN and IPSec, it's a work of art."

A 2024 report concluded that WireGuard had potential as a lightweight robust solution for Internet of things security.

WireGuard has received funding from the Open Technology Fund and donations from *Jump Trading*, Mullvad, Tailscale, *Fly.io*, and the NLnet Foundation.

Oregon senator Ron Wyden has recommended to the National Institute of Standards and Technology (NIST) that they evaluate WireGuard as a replacement for existing technologies.

## Availability

### Implementations

Implementations of the WireGuard protocol include:

- Donenfeld's initial implementation, written in C and Go.
- Cloudflare's BoringTun, a user space implementation written in Rust.
- Matt Dunwoodie's implementation for OpenBSD, written in C.
- Ryota Ozaki's wg(4) implementation for NetBSD, written in C.
- The FreeBSD implementation is written in C and shares most of the data path with the OpenBSD implementation.
- Native Windows kernel implementation named "wireguard-nt", since August 2021.
- AVM Fritz!Box modem-routers that support Fritz!OS version 7.39 and later. Permits site-to-site WireGuard connections from version 7.50 onwards.
- Vector Packet Processing user space implementation written in C.

## History

Early snapshots of the code base exist from 30 June 2016. The logo is inspired by a stone engraving of the mythological Python that Jason Donenfeld saw while visiting a museum in Delphi.

On 9 December 2019, David Miller – primary maintainer of the Linux networking stack – accepted the WireGuard patches into the "net-next" maintainer tree, for inclusion in an upcoming kernel.

On 28 January 2020, Linus Torvalds merged David Miller's net-next tree, and WireGuard entered the mainline Linux kernel tree.

On 20 March 2020, Debian developers enabled the module build options for WireGuard in their kernel config for the Debian 11 version (testing).

On 29 March 2020 WireGuard was incorporated into the Linux 5.6 release tree. The Windows version of the software remains at beta. This led to Android developers adding native kernel support for WireGuard in their Generic Kernel Image on 30 March 2020.

On 22 April 2020, NetworkManager developer Beniamino Galvani merged GUI support for WireGuard in GNOME.

On 12 May 2020, Matt Dunwoodie proposed patches for native kernel support of WireGuard in OpenBSD. On 22 June 2020, after the work of Matt Dunwoodie and Jason A. Donenfeld, WireGuard support was imported into OpenBSD.

On 23 November 2020, Jason A. Donenfeld released an update of the Windows package improving installation, stability, ARM support, and enterprise features.

On 29 November 2020, WireGuard support was imported into the FreeBSD 13 kernel.

On 19 January 2021, WireGuard support was added for preview in pfSense Community Edition (CE) 2.5.0 development snapshots.

In March 2021, kernel-mode WireGuard support was removed from FreeBSD 13.0, still in testing, after an urgent code cleanup in FreeBSD WireGuard could not be completed quickly. FreeBSD-based pfSense Community Edition (CE) 2.5.0 and pfSense Plus 21.02 removed kernel-based WireGuard as well.

In May 2021, WireGuard support was re-introduced back into pfSense CE and pfSense Plus development snapshots as an experimental package written by a member of the pfSense community, Christian McDonald. The WireGuard package for pfSense incorporates the ongoing kernel-mode WireGuard development work by Jason A. Donenfeld that was originally sponsored by Netgate.

In June 2021, the official package repositories for both pfSense CE 2.5.2 and pfSense Plus 21.05 included the WireGuard package.

In 2023, WireGuard received over 209,000€ support from Germany's Sovereign Tech Fund.

In June 2025, IPFire has added support for WireGuard using the Linux kernel implementation.

In January 2026 Iran International reported that WireGuard was being used in Iran in the aftermath of the 2026 Iran protests, albeit with limited success.
