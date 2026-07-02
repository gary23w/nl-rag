---
title: "How IPFS works"
source: https://docs.ipfs.tech/concepts/how-ipfs-works/
domain: merkle-tree
license: CC-BY-SA-4.0
tags: merkle tree, hash tree, merkle root, merkle proof
fetched: 2026-07-02
---

# # How IPFS works

In this conceptual guide, you'll learn about the major subsystems that IPFS is composed of, and how they work. The three key responsibilities of the IPFS subsystems are:

- **Representing and addressing data**
- **Routing data**
- **Transferring data**

While these are the key responsibilities, IPFS's functionality spans beyond these three.

Data in IPFS is addressed by its contents (content addressing), rather than a location, such as an IP address (location addressing).

This guide is part 3 of a 3-part introduction to the basic concepts of IPFS. The first part, What IPFS is and isn't, defines IPFS, while the second part, **IPFS and the problems it solves**, covers the problems with the internet and current protocols like HTTP that IPFS solves.

## # Subsystems overview

All IPFS subsystems, ordered by purpose, are listed below, with links to the major subsystems discussed in this guide.

| Purpose | Subsystem |
|---|---|
| Representing and organizing the data | CIDs, IPLD, UnixFS, MFS, DAG-CBOR, DAG-JSON, CAR files |
| Content routing, linking between CID and IP addresses | Kademlia DHT, Delegated routing over HTTP, Bitswap, mDNS |
| Transferring data | Bitswap, HTTP Gateways, Sneakernet, Graphsync, more in development |
| Addressing for data and peers | Multiformats |
| Bridging between IPFS and HTTP | IPFS Gateways, Pinning API Spec |
| Peer-to-peer connectivity | libp2p (TCP, QUIC, WebRTC, WebTransport) |
| Mutability and dynamic naming | IPNS (Interplanetary Naming System), DNSLink |

## # How IPFS represents and addresses data

IPFS represents data as content-addressed blocks, and operates on those data blocks using the following subsystems:

- Content Identifier (CID)
- InterPlanetary Linked Data (IPLD)
- Content Addressable aRchive (CAR) files

### # Content Identifier (CID)

In IPFS, data is chunked into blocks, which are assigned a unique identifier called a Content Identifier (CID). In general, the CID is computed by combining the hash of the data with its codec. The codec is generated using Multiformats.

Because CIDs are based on content, not location:

- You can fetch data by *what it is*, not where it's stored.
- You can verify data by recomputing the CID and comparing it to what you requested.

**Learn more** Learn more about CIDs in the CID deep dive.

### # InterPlanetary Linked Data (IPLD)

IPFS uses InterPlanetary Linked Data (IPLD) to work with CIDs and content-addressed data. IPFS uses IPLD to represent relationships between content-addressed data, such as file directories and other hierarchical structures, using a Directed Acyclic Graph (DAG) called a Merkle DAG. Using IPLD for the general functionality, IPFS is able provide a more tailored, specific mechanism for representing and addressing files, directories, and their symlinks, called UnixFS. With UnixFS, IPFS can chunk and link data too big to fit in a single block, and use the chunked representation to store and manage the data.

IPLD provides IPFS with the following benefits:

- The ability to represent and work with arbitrary data, whether that data is standard files and directories, linked data, a Merkle DAG, or another data type.
- Base functionality to structure, serialize, traverse and link content-addressed data, which can be leveraged by abstractions like UnixFS for more specific use cases.
- Interoperable protocols.
- Easy upgradeability.
- Backwards compatibility.

**Learn more** Want to learn more about IPLD? See the official docs (opens new window).

### # Content Addressable aRchive (CAR) files

IPFS uses Content Addressable aRchive (CAR) files to store and transfer a serialized archive of IPLD content-addressed data. CAR files are similar to TAR files, in that they that are designed for storing collections of content addressed data.

## # How content routing works in IPFS

*Content routing* refers to the way in which IPFS determines where to find a given CID on the network; specifically, which network peers are providing the CIDs you are requesting. In other words, a node cannot simply find data in the network with a CID alone; it requires information about the IP addresses and ports of its peers on the network. To route content, IPFS uses the following subsystems:

- Kademlia Distributed Hash Table (DHT)
- Bitswap
- mDNS
- Delegated routing over HTTP

### # Kademlia Distributed Hash Table (DHT)

IPFS uses Kademlia, a Distributed Hash Table (DHT) designed for decentralized peer-to-peer networks. Kademlia helps you find peers in the IPFS network storing the data you are seeking. The Kademlia DHT can be thought of as a large table distributed across many nodes that stores information about which peers (IPs) have which data (CIDs). Kademlia provides a highly efficient, self-organizing system that withstands node churn. Kademlia uses libp2p to establish connectivity.

**Learn more**

Want to learn more about Kademlia and DHTs? See the Distributed Hash Tables (DHTs) conceptual guide.

### # Bitswap (for content routing)

IPFS nodes use Bitswap, a message-based, peer-to-peer network protocol for the transfer of data, that is *also* used for routing data. With Bitswap, an IPFS node can ask any of the peers that it is connected to if they have any of the CIDs that node is looking for, all without traversing the Kademlia DHT. Peers also store wantlists, so that if a peer receives the requested data at a later time, it can then send it to the node that originally requested. Like Kademlia, Bitswap uses libp2p to establish connectivity.

**Learn more**

Want to learn more about Bitswap? See the Bitswap deep dive.

### # Delegated routing over HTTP

Delegated content routing is a mechanism for IPFS implementations to use for offloading content routing to another process/server using an HTTP API. For example, if an IPFS node does not implement the DHT, a delegated router can search the DHT for peers on its behalf. The main benefit of delegated routing is that nodes are not required to implement routing functionality themselves if they do not have the computing resources to do so, or wish to build an IPFS system with a custom backend for routing. So, delegated routing over HTTPS provides IPFS nodes with a standard interface that allows more flexibility in terms of how content routing works.

**Learn more**

For further information, see the Delegated Content Routing HTTP API spec (opens new window)..

### # mDNS

To quickly and efficiently discover peers in local networks, IPFS uses Multicast Domain Name System (mDNS), a type of DNS protocol that resolves human-readable internet domain names to IP names without the use of a name server.

The use of mDNS enables quick and efficient discovery of IPFS nodes in local networks without any coordination, e.g., without internet connectivity or access to bootstrap nodes.

## # How IPFS transfers data

In addition to routing data, nodes in the IPFS network must efficiently distribute and deliver the content addressed data, taking into account that there are some nodes in the network who already have a copy of the data, and other nodes who do not have a copy of the data, but want one. To handle the transfer of data, IPFS uses the following subsystems:

- Bitswap
- IPFS HTTP Gateways
- Sneakernet

### # Bitswap (for data transfer)

As discussed in How content routing works in IPFS, IPFS nodes use Bitswap, a message-based, peer-to-peer network protocol for both content routing and the transfer of data. With Bitswap, any peers that an IPFS node is connected to can transfer requested blocks directly to that node without needing to traverse the DHT. Peers also store wantlists, so that if a peer receives requested data at a later time, it can then transfer it to the node that originally requested.

**Learn more**

Want to learn more about Bitswap? See the Bitswap deep dive.

### # IPFS HTTP Gateways

HTTP Gateways allow applications that do not support or implement all IPFS subsystems to fetch data from the IPFS network using an HTTP interface. In its simplest form, a gateway is an IPFS Node that also exposes an HTTP Gateway API (opens new window).

**Learn more**

Want to learn more about IPFS Gateways? See the IPFS Gateway conceptual guide.

### # Sneakernet

For use cases where transfer of data over a network connection is not an option, IPFS supports the use of sneakernet to transfer content-addressed data between IPFS nodes. Using IPFS, CAR files (discussed in How IPFS represents and addresses data) can be transferred between two network drives without any network connectivity. Because of IPFS, the data is verifiable and will have the same CID on both sides of the air gap.

## # Further reading

- Are you looking for a deep dive into the design, architecture and theory of IPFS? See the original IPFS whitepaper.
- Dive deeper into the related concepts of immutability, hashing, content-addressing and CIDs.
- Learn about IPFS pinning, along with the differences between persistence, permanence, and pinning.
- Understand privacy and encryption in IPFS.
- Learn more about IPFS nodes, including the different types.
