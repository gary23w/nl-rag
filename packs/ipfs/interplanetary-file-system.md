---
title: "InterPlanetary File System"
source: https://en.wikipedia.org/wiki/InterPlanetary_File_System
domain: ipfs
license: CC-BY-SA-4.0 / CC-BY-4.0 (ipfs docs)
tags: ipfs, content addressing, distributed hash table, ipns
fetched: 2026-07-02
---

# InterPlanetary File System

The **InterPlanetary File System** (**IPFS**) is a protocol, hypermedia and file sharing peer-to-peer network for sharing data using a distributed hash table to store provider information. By using content addressing, IPFS uniquely identifies each file in a global namespace that connects IPFS hosts, creating a distributed system of file storage and sharing.

IPFS allows users to host and receive content in a manner similar to BitTorrent. As opposed to a centrally located server, IPFS is built around a decentralized system of user-operators who hold a portion of the overall data. Any user in the network can serve a file by its content address, and other peers in the network can find and request that content from any node who has it using a distributed hash table (DHT).

In contrast to traditional location-based protocols like HTTP and HTTPS, IPFS uses content-based addressing to provide a decentralized alternative for distributing the World Wide Web.

## Design

The InterPlanetary File System (IPFS) is a decentralized protocol, hypermedia, and peer-to-peer (P2P) network for distributed file storage and sharing. By using content-addressing, IPFS uniquely identifies files in a global namespace that interlinks IPFS hosts, creating a hypermedia system that enables efficient and reliable data distribution.

IPFS allows users to host and receive content in a manner similar to BitTorrent. As opposed to a centrally located server, IPFS is built around a decentralized system of user-operators who hold a portion of the overall data, creating a resilient system of file storage and sharing. Any user in the network can serve a file by its content address, and other peers in the network can find and request that content from any node who has it using a distributed hash table (DHT). In contrast to BitTorrent, IPFS aims to create a single global network. This means that if two users publish a block of data with the same hash, the peers downloading content from one user will also exchange data with those downloading it from the second.

Key features of IPFS include:

- Content-addressed file storage: Each file is uniquely identified based on its content hash, ensuring data integrity and facilitating efficient retrieval.
- Peer-to-peer architecture: A distributed network of nodes facilitates direct file sharing without the need for centralized servers.
- Versioned file system: Supports file versioning and allows users to track changes over time.
- Interoperability with distributed applications: IPFS integrates with decentralized applications (dApps), offering a storage layer for blockchain and Web3 ecosystems.

IPFS gateways allow browsers and tools that lack native IPFS support to access IPFS content over HTTP. Users may choose not to install an IPFS client on their device and instead use a public gateway. A list of these gateways is maintained on the IPFS GitHub page.

## History

IPFS was created by Juan Benet, who later founded Protocol Labs in May 2014. An alpha version was launched in February 2015, and by October of the same year was described by TechCrunch as "quickly spreading by word of mouth." Network service provider Cloudflare started using IPFS in 2018 and launched its own IPFS gateway in 2022.

In March 2020, the Opera browser provided access to the centralized resources of the Unstoppable Domains provider by hosting content in IPFS.

## Applications

- Filecoin is a cryptocurrency used to implement an IPFS-based cooperative storage cloud, also authored by Protocol Labs.
- The shadow libraries Anna's Archive and Library Genesis host books via IPFS.
- The Brave browser added support in 2021, however support for local nodes and the ipfs:// scheme was removed in 2024 due to low usage and lack of support.

- IPFS is used as a storage layer for some decentralized applications and Web3 projects, including NFT platforms and blockchain-based services, because content addressing and distributed storage can improve data persistence and reduce reliance on single centralized servers.

### Anti-censorship

- The Catalan independence referendum, taking place in September–October 2017, was deemed illegal by the Constitutional Court of Spain and many related websites were blocked. Subsequently, the Catalan Pirate Party mirrored the website on IPFS to bypass the High Court of Justice of Catalonia order of blocking.
- During the block of Wikipedia in Turkey, IPFS was used to create a mirror of Wikipedia, which allowed access to archived static Wikipedia content despite the ban. The mirror has now been expanded to more languages, such as English, Ukrainian, Russian, Arabic, and Chinese. A collection of the mirrors can be viewed by using its CID at an IPFS Gateway.

### Malware

Phishing attacks have also been distributed through Cloudflare's IPFS gateway since July 2018. The phishing scam HTML is stored on IPFS, and displayed via Cloudflare's gateway. The connection shows as secure via a Cloudflare TLS certificate.

The IPStorm botnet, first detected in June 2019, uses IPFS so it can hide its command-and-control amongst the flow of legitimate data on the IPFS network. Security researchers had previously identified the possibility of using IPFS as a botnet command-and-control system.
