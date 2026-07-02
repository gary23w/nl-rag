---
title: "Polkadot (blockchain platform)"
source: https://en.wikipedia.org/wiki/Polkadot_(blockchain_platform)
domain: cross-chain-bridge
license: CC-BY-SA-4.0 / CC-BY-4.0 (ethereum.org)
tags: cross-chain bridge, blockchain bridge, wrapped asset, chain interoperability
fetched: 2026-07-02
---

# Polkadot (blockchain platform)

**Polkadot** is a decentralized, nominated proof-of-stake blockchain with smart contract functionality. The cryptocurrency native to the blockchain is the DOT.

Designed to facilitate interoperability, Polkadot enables independent blockchains to exchange data and assets securely without relying on centralized intermediaries. This cross-chain communication framework allows for the development of decentralized applications (dApps) and services that span multiple blockchains within a unified network architecture.

## History

### Founding and ICO (2016–2019)

Polkadot was created by the Ethereum co-founder Gavin Wood, Robert Habermeier and Peter Czaban. The white paper for Polkadot was published by Wood in 2016. The Polkadot SDK and other core technology components are being developed by Parity Technologies. The project raised over $144.3 million in its Initial coin offering in October 2017.

In 2017, Gavin Wood, Aeron Buchanan, Peter Czaban, Reto Trinkler, and Mathias Bucher, established the Web3 Foundation, a non-profit organization based in Zug, Switzerland, to promote and provide funding for blockchain-based decentralized web technologies. The Polkadot SDK and other core technology components are being developed by Parity Technologies, a blockchain infrastructure company founded in 2015 by Gavin Wood and Jutta Steiner.

In October 2017, Polkadot raised over $144.3 million in its initial coin offering (ICO). Shortly after the ICO, a vulnerability in the multi-signature wallets developed by Parity Technologies led to the freezing of approximately $150 million worth of Ethereum, including a significant portion of the funds raised. Over 500 wallets were impacted, including Polkadot’s wallet, which held a significant portion of the $144.3 million raised during its ICO. In 2019, Polkadot raised an additional $43 million through a private token sale.

### Network Launch and Parachains (2020–2021)

In May 2020, Polkadot launched its mainnet under a proof-of-authority consensus model, managed by the Web3 Foundation during its early phase. By June 2020, the network transitioned to a Nominated Proof-of-Stake (NPoS) consensus mechanism, allowing token holders to nominate validators to secure the network and process transactions.

In December 2021, Polkadot introduced parachain functionality, allowing multiple blockchains to run simultaneously and connect to the network's *Relay Chain*.

In December 2024, Polkadot's canary network Kusama underwent a stress test known as "The Spammening," handling approximately 143,000 transactions per second (TPS) at just 23% capactiy.

## Concepts

### Multi-chain ecosystem

Polkadot is founded on the premise that there will be a multitude of blockchains in the future. It provides an open-source software development kit called Polkadot SDK that can be used by development teams to build their own blockchains. These blockchains can function independently, known as "solochains," or integrate into the Polkadot network as "parachains," thereby benefiting from shared security and cross-chain communication capabilities.

### Sovereignty, shared security and interoperability

Polkadot offers three properties to parachains: sovereignty, shared security and interoperability.

- **Sovereignty** refers to the idea that individual blockchains are sovereign in the way they conduct themselves. Blockchains define their own rules for how users can interact on them. Each parachain maintains autonomy over its governance and transaction processing, allowing it to define its own rules and optimize for specific functionalities without being constrained by the decisions or limitations of other chains.

- **Shared security** means that one chain provides cryptoeconomic security to other chains. The Polkadot network has a primary blockchain named the **relay chain**, which provides security for parachains. This way, parachains enjoy high cryptoeconomic security, relieving them from the burden to source their own security through means that compromise their sovereignty. This pooled security model ensures that parachains inherit robust cryptoeconomic security without the necessity of establishing their own validator networks, thereby reducing resource expenditure and enhancing overall network integrity.

- **Interoperability** is created through a common standard of data exchange, called XCM. Since parachains have shared security, bridging times between parachains are typically under a minute.

### Cross-Consensus Message Passing (XCMP)

XCMP is Polkadot's protocol for facilitating communication between parachains. It enables the transfer of arbitrary data across chains, supporting a wide range of applications, including token transfers, smart contract interactions, and more complex cross-chain operations. XCMP operates by allowing parachains to send messages to each other through the Relay Chain.

## Governance

Polkadot implements an on-chain governance system, allowing stakeholders to influence the network's development and decision-making processes. Over time, its governance model has transitioned from Governance V1 to OpenGov, to address concerns of decentralization and community involvement. Polkadot Council members and *Relay Chain* Validators are selected via Phragmen election method.

## Technical details

### Proof of stake

The network uses a nominated proof-of-stake consensus algorithm. The protocol used, Blind Assignment for Blockchain Extension (BABE), is derived from Ouroboros. Validators are responsible for block production and validation, while nominators support validators by staking DOT tokens on their behalf.
