---
title: "Bitcoin protocol"
source: https://en.wikipedia.org/wiki/Bitcoin_protocol
domain: bitcoin
license: CC-BY-SA-4.0
tags: bitcoin, btc, bitcoin protocol, utxo model, satoshi nakamoto
fetched: 2026-07-02
---

# Bitcoin protocol

The **bitcoin protocol** is the set of rules that govern the functioning of bitcoin. Its key components and principles are: a peer-to-peer decentralized network with no central oversight; the blockchain technology, a public ledger that records all bitcoin transactions; mining and proof of work, the process to create new bitcoins and verify transactions; and cryptographic security.

Users broadcast cryptographically signed messages to the network using bitcoin cryptocurrency wallet software. These messages are proposed transactions, changes to be made in the ledger. Each node has a copy of the ledger's entire transaction history. If a transaction violates the rules of the bitcoin protocol, it is ignored, as transactions only occur when the entire network reaches a consensus that they should take place. This "full network consensus" is achieved when each node on the network verifies the results of a proof-of-work operation called *mining*. Mining packages groups of transactions into blocks, and produces a hash code that follows the rules of the bitcoin protocol. Creating this hash requires expensive energy, but a network node can verify the hash is valid using very little energy. If a miner proposes a block to the network, and its hash is valid, the block and its ledger changes are added to the blockchain, and the network moves on to yet unprocessed transactions. In case there is a dispute, then the longest chain is considered to be correct. A new block is created every 10 minutes, on average.

Changes to the bitcoin protocol require consensus among the network participants. The bitcoin protocol has inspired the creation of numerous other digital currencies and blockchain-based technologies, making it a foundational technology in the field of cryptocurrencies.

## Blockchain

Blockchain technology is a decentralized and secure digital ledger that records transactions across a network of computers. It ensures transparency, immutability, and tamper resistance, making data manipulation difficult. Blockchain is the underlying technology for cryptocurrencies like bitcoin and has applications beyond finance, such as supply chain management and smart contracts.

### Transactions

The network requires minimal structure to share transactions. An ad hoc decentralized network of volunteers is sufficient. Messages are broadcast on a best-effort basis, and nodes can leave and rejoin the network at will. Upon reconnection, a node downloads and verifies new blocks from other nodes to complete its local copy of the blockchain.

## Mining

Bitcoin uses a proof-of-work system or a proof-of-transaction to form a distributed timestamp server as a peer-to-peer network. This work is often called *bitcoin mining*. During mining, practically all of the computing power of the bitcoin network is used to solve cryptographic tasks, which is proof of work. Their purpose is to ensure that the generation of valid blocks involves a certain amount of effort so that subsequent modification of the blockchain, such as in the 51% attack scenario, can be practically ruled out. Because of the difficulty, miners form "mining pools" to get payouts despite these high power requirements, costly hardware deployments, and hardware under control. As a result of the Chinese ban on bitcoin mining in 2021, the United States currently holds the largest share of bitcoin mining pools.

Requiring a proof of work to accept a new block to the blockchain was Satoshi Nakamoto's key innovation. The mining process involves identifying a block that, when hashed twice with SHA-256, yields a number smaller than the given difficulty target. While the average work required increases in inverse proportion to the difficulty target, a hash can always be verified by executing a single round of double SHA-256.

For the bitcoin timestamp network, a valid proof of work is found by incrementing a nonce until a value is found that gives the block's hash the required number of leading zero bits. Once the hashing has produced a valid result, the block cannot be changed without redoing the work. As later blocks are chained after it, the work to change the block would include redoing the work for each subsequent block. If there is a deviation in consensus then a blockchain fork can occur.

Majority consensus in bitcoin is represented by the longest chain, which required the greatest amount of effort to produce. If a majority of computing power is controlled by honest nodes, the honest chain will grow fastest and outpace any competing chains. To modify a past block, an attacker would have to redo the proof-of-work of that block and all blocks after it and then surpass the work of the honest nodes. The probability of a slower attacker catching up diminishes exponentially as subsequent blocks are added.

To compensate for increasing hardware speed and varying interest in running nodes over time, the difficulty of finding a valid hash is adjusted roughly every two weeks. If blocks are generated too quickly, the difficulty increases and more hashes are required to make a block and to generate new bitcoins.

### Difficulty and mining pools

Early bitcoin miners

used GPUs for mining

, as they were better suited to the

proof-of-work

algorithm than

CPUs

.

Later amateurs mined bitcoins with specialized

FPGA

and

ASIC

chips. The chips pictured have become obsolete due to increasing difficulty.

Today, bitcoin mining companies

dedicate facilities

to housing and operating large amounts of high-performance mining hardware.

Bitcoin mining is a competitive endeavor. An "arms race" has been observed through the various hashing technologies that have been used to mine bitcoins: basic central processing units (CPUs), high-end graphics processing units (GPUs), field-programmable gate arrays (FPGAs) and application-specific integrated circuits (ASICs) all have been used, each reducing the profitability of the less-specialized technology. Bitcoin-specific ASICs are now the primary method of mining bitcoin and have surpassed GPU speed by as much as 300-fold. The difficulty of the mining process is periodically adjusted to the mining power active on the network. As bitcoins have become more difficult to mine, computer hardware manufacturing companies have seen an increase in sales of high-end ASIC products.

Computing power is often bundled together or "pooled" to reduce variance in miner income. Individual mining rigs often have to wait for long periods to confirm a block of transactions and receive payment. In a pool, all participating miners get paid every time a participating server solves a block. This payment depends on the amount of work an individual miner contributed to help find that block, and the payment system used by the pool.

### Environmental effects

The environmental impact of bitcoin has been characterized in the literature as significant, particularly due to its energy use, greenhouse gas emissions, and electronic waste. Bitcoin mining, the process by which bitcoins are created and transactions are finalized, is energy-consuming and results in carbon emissions. According to the 2025 Cambridge Digital Mining Industry Report, surveyed miners reported that 48% of their electricity came from fossil fuels and 52% from sustainable energy sources, including renewables and nuclear. Moreover, bitcoins are mined on specialized computer hardware resulting in electronic waste. As of 2025, several empirical studies report an association between higher bitcoin-mining electricity use and worse environmental-sustainability indicators. Bitcoin's environmental impact has attracted the attention of regulators, leading to incentives or restrictions in various jurisdictions.

A 2023 study in *ACS Sustainable Chemistry & Engineering* found potential economic benefits from using bitcoin mining at planned renewable-energy installations in the United States.

### Mined bitcoins

By convention, the first transaction in a block is a special transaction that produces new bitcoins owned by the creator of the block. This is the incentive for nodes to support the network. It provides a way to move new bitcoins into circulation. The reward for mining halves every 210,000 blocks. It started at 50 bitcoin, dropped to 25 in late 2012, dropped again to 12.5 on the summer of 2016, and to 6.25 bitcoin in 2020. The most recent halving, which occurred on 20 April 2024 at 12:09am UTC (with block number 840,000), reduced the block reward to 3.125 bitcoins. The next halving is expected to occur in 2028, when the block reward will fall to 1.625 bitcoins. This halving process is programmed to continue a maximum of 64 times before new coin creation ceases.

## Payment verification

Each miner can choose which transactions are included in or exempted from a block. A greater number of transactions in a block does not equate to greater computational power required to solve that block.

As noted in Nakamoto's whitepaper, it is possible to verify bitcoin payments without running a full network node (simplified payment verification, SPV). A user only needs a copy of the block headers of the longest chain, which are available by querying network nodes until it is apparent that the longest chain has been obtained; then, get the Merkle tree branch linking the transaction to its block. Linking the transaction to a place in the chain demonstrates that a network node has accepted it, and blocks added after it further establish the confirmation.

## Protocol features

### Security

Various potential attacks on the bitcoin network and its use as a payment system, real or theoretical, have been considered. The bitcoin protocol includes several features that protect it against some of those attacks, such as unauthorized spending, double spending, forging bitcoins, and tampering with the blockchain. Other attacks, such as theft of private keys, require due care by users.

#### Unauthorized spending

Unauthorized spending is mitigated by bitcoin's implementation of public-private key cryptography. For example, when Alice sends a bitcoin to Bob, Bob becomes the new owner of the bitcoin. Eve, observing the transaction, might want to spend the bitcoin Bob just received, but she cannot sign the transaction without the knowledge of Bob's private key.

#### Double spending

A specific problem that an internet payment system must solve is double-spending, whereby a user pays the same coin to two or more different recipients. An example of such a problem would be if Eve sent a bitcoin to Alice and later sent the same bitcoin to Bob. The bitcoin network guards against double-spending by recording all bitcoin transfers in a ledger (the blockchain) that is visible to all users, and ensuring for all transferred bitcoins that they have not been previously spent.

#### Race attack

If Eve offers to pay Alice a bitcoin in exchange for goods and signs a corresponding transaction, it is still possible that she also creates a different transaction at the same time sending the same bitcoin to Bob. By the rules, the network accepts only one of the transactions. This is called a race attack, since there is a race between the recipients to accept the transaction first. Alice can reduce the risk of race attack stipulating that she will not deliver the goods until Eve's payment to Alice appears in the blockchain.

A variant race attack (which has been called a Finney attack by reference to Hal Finney) requires the participation of a miner. Instead of sending both payment requests (to pay Bob and Alice with the same coins) to the network, Eve issues only Alice's payment request to the network, while the accomplice tries to mine a block that includes the payment to Bob instead of Alice. There is a positive probability that the rogue miner will succeed before the network, in which case the payment to Alice will be rejected. As with the plain race attack, Alice can reduce the risk of a Finney attack by waiting for the payment to be included in the blockchain.

#### History modification

Each block that is added to the blockchain, starting with the block containing a given transaction, is called a confirmation of that transaction. Ideally, merchants and services that receive payment in bitcoin should wait for at least a few confirmations to be distributed over the network before assuming that the payment was done. The more confirmations that the merchant waits for, the more difficult it is for an attacker to successfully reverse the transaction—unless the attacker controls more than half the total network power, in which case it is called a 51% attack, or a majority attack. Although more difficult for attackers of a smaller size, there may be financial incentives that make history modification attacks profitable.

#### Quantum-Enabled Attacks

The cryptographic primitives employed by Bitcoin are pre-quantum and therefore vulnerable to an attack from a adversary with a cryptographically-relevant, general-purpose quantum computer.

The Bitcoin protocol uses the Elliptic Curve Digital Signature Algorithm (ECDSA) to sign and verify transactions. ECDSA is vulnerable to attacks from a quantum computer due to its reliance on the security of the discrete logarithm problem. The Bitcoin protocol allows senders to send Bitcoin to the hash of the recipient's public key. The hash obscures the public key of the recipient and is therefore quantum-resistant while unspent. However, in order for the recipient to transact with the received bitcoin, the recipient would need to broadcast their public key. This broadcast could allow a quantum-enabled attacker to derive the private key from the public key and steal the Bitcoin.

Additionally, the security of the proof of work may be vulnerable to a general-purpose quantum computer with sufficient depth and stability to perform hashing. Grover's algorithm can be applied to the hash-based proof of work of the Bitcoin protocol to quadratically reduce the time it takes to find a valid nonce. If such quantum computers were available that could perform Grover's algorithm on a hash-based, proof-of-work blockchain, an attacker would very likely be capable of performing a 51% attack due to the massive speed-up.

### Scalability

Bitcoin scalability refers to the capability of the Bitcoin network to handle large amounts of transaction data on its platform. Records (known as *blocks*) in the Bitcoin blockchain are limited in size and frequency to prioritize security and decentralization by keeping the cost of running a Bitcoin node affordable. With an average block creation time of 10 minutes and a block size limit of around 1 megabyte, the base layer processes an estimated 3.3 to 7 transactions per second.

Several Layer 2 solutions have been implemented as a result. The Lightning Network allows near-instant, low-fee payments that settle on the Bitcoin base layer. The Liquid Network is a sidechain built on top of Bitcoin which processes blocks every minute instead of every 10 minutes.

### Privacy

#### Deanonymisation of clients

Deanonymisation is a strategy in data mining in which anonymous data is cross-referenced with other sources of data to re-identify the anonymous data source. Along with transaction graph analysis, which may reveal connections between bitcoin addresses (pseudonyms), there is a possible attack which links a user's pseudonym to its IP address. If the peer is using Tor, the attack includes a method to separate the peer from the Tor network, forcing them to use their real IP address for any further transactions. The cost of the attack on the full bitcoin network was estimated to be under €1500 per month, as of 2014.
