---
title: "Cryptocurrency wallet"
source: https://en.wikipedia.org/wiki/Cryptocurrency_wallet
domain: account-abstraction
license: CC-BY-SA-4.0 / CC-BY-4.0 (ethereum.org)
tags: account abstraction, smart contract wallet, erc-4337, user operation
fetched: 2026-07-02
---

# Cryptocurrency wallet

A **cryptocurrency wallet** is a device, physical medium, program or an online service which stores the public and/or private keys for cryptocurrency transactions. In addition to this basic function of storing the keys, a cryptocurrency wallet more often offers the functionality of encrypting and/or signing information. Signing can for example result in executing a smart contract, a cryptocurrency transaction (see "bitcoin transaction" image), identification, or legally signing a 'document' (see "application form" image).

## History

In 2008 bitcoin was introduced as the first cryptocurrency following the principle outlined by Satoshi Nakamoto in the paper “Bitcoin: A Peer-to-Peer Electronic Cash System.” The project was described as an electronic payment system using cryptographic proof instead of trust. It also mentioned using cryptographic proof to verify and record transactions on a blockchain.

The first wallet program, simply named *Bitcoin*, and sometimes referred to as the *Satoshi client*, was released in January 2009 by Satoshi Nakamoto as open-source software. In version 0.5 the client moved from the wxWidgets user interface toolkit to Qt, and the whole bundle was referred to as *Bitcoin-Qt*. After the release of version 0.9, the software bundle was renamed *Bitcoin Core* to distinguish itself from the underlying network. Bitcoin Core is, perhaps, the best known implementation or client. Forks of Bitcoin Core exist, such as Bitcoin XT, Bitcoin Unlimited, and Parity Bitcoin.

## Types of Wallets

### Software wallets

Software wallets is a broad category of software applications that allow users to manage and transfer digital assets, and sign messages. These can be hot or cold wallets. They can be run as desktop apps, mobile apps, web extensions, or web wallets.

There are several modes in which software wallets can operate. They have an inverse relationship with regard to trustlessness and computational requirements.

- *Full clients* verify transactions directly by downloading a full copy of the blockchain (over 670 GB as of September 2025). They do not require trust in any external parties. Full clients check the validity of mined blocks, preventing them from transacting on a chain that breaks or alters network rules. Because of its size and complexity, downloading and verifying the entire blockchain is not suitable for all computing devices.
- *Lightweight clients* consult full nodes to send and receive transactions without requiring a local copy of the entire blockchain (see *simplified payment verification* – *SPV*). This makes lightweight clients much faster to set up and allows them to be used on low-power, low-bandwidth devices such as smartphones. When using a lightweight wallet, however, the user must trust full nodes, as it can report faulty values back to the user. Lightweight clients follow the longest blockchain and do not ensure it is valid, requiring trust in full nodes.

Third-party internet services called *online wallets* or *webwallets* offer similar functionality but may be easier to use. In this case, credentials to access funds are stored with the online wallet provider rather than on the user's hardware. As a result, the user must have complete trust in the online wallet provider. A malicious provider or a breach in server security may cause entrusted crypto to be stolen. An example of such a security breach occurred with Mt. Gox in 2011.

### Cold storage

A paper wallet with a

banknote

-like design. Both the private key and the address are visible in

text form

and as

2D barcodes

.

A paper wallet with the address visible for adding or checking stored funds. The part of the page containing the private key is folded over and sealed.

A brass

token

with a private key hidden beneath a

tamper-evident

security hologram

. A part of the address is visible through a transparent part of the hologram.

A hardware wallet

peripheral

which processes bitcoin payments without exposing any credentials to the computer

"Cold storage" simply means keeping the private keys out of reach of hackers by storing or generating them on a device that is not connected to the internet. The credentials necessary to spend crypto can be stored offline in a number of different ways, from simple paper printouts of private keys, to specialized hardware wallets.

#### Paper wallets

A paper wallet is created with a keypair generated on a computer with no internet connection; the private key is written or printed onto the paper and then erased from the computer. The paper wallet can then be stored in a safe physical location for later retrieval. Physical wallets can also take the form of metal token coins with a private key accessible under a security hologram in a recess struck on the reverse side. The security hologram self-destructs when removed from the token, showing that the private key has been accessed. Originally, these tokens were struck in brass and other base metals, but later used precious metals as bitcoin grew in value and popularity. Coins with stored face value as high as ₿1,000 have been struck in gold. The British Museum's coin collection includes four specimens from the earliest series of funded bitcoin tokens; one is currently on display in the museum's money gallery. In 2013, a Utah manufacturer of these tokens was ordered by the Financial Crimes Enforcement Network (FinCEN) to register as a money services business before producing any more funded bitcoin tokens.

#### Hardware wallets

A hardware "wallet" is a small and portable computer peripheral that signs transactions as requested by the user. These devices store private keys and carry out signing and encryption internally, and do not share any sensitive information with the host computer except already signed (and thus unalterable) transactions. Because hardware wallets never expose their private keys, even computers that may be compromised by malware do not have a vector to access or steal them.The user sets a passcode when setting up a hardware signer. As hardware signers are tamper-resistant, without the passcode the assets cannot be accessed.

### Multisignature wallet

In contrast to simple cryptocurrency wallets requiring just one party to sign a transaction, multi-sig wallets require multiple parties to sign a transaction. Multisignature wallets are designed to increase security by requiring a predefined threshold of signatures from independent private keys to authorize any transaction. In deterministic multisig wallets, a hierarchy of keys (often following a dedicated path such as `m/48'`) allows multiple participants to derive compatible public keys from a single master seed while maintaining independent private key control. There are various use cases for multisignature wallets, including enhanced security, treasury management, partnership management, escrow services, inheritance planning, regulatory compliance and backup recovery.

## Technology

### Private and public key generation

A cryptocurrency wallet works by a theoretical or random number being generated and used with a length that depends on the algorithm size of the cryptocurrency's technology requirements. The number is converted to a private key using the specific requirements of the cryptocurrency cryptography algorithm requirement. A public key is then generated from the private key using whichever cryptographic algorithm is required. The private key is used by the owner to access and send cryptocurrency and is private to the owner, whereas the public key is to be shared to any third party to receive cryptocurrency.

Up to this stage no computer or electronic device is required and all key pairs can be mathematically derived and written down by hand. The private key and public key pair (known as an address) are not known by the blockchain or anyone else. The blockchain will only record the transaction of the public address when cryptocurrency is sent to it, thus recording in the blockchain ledger the transaction of the public address.

### Duplicate private keys

Collision (two or more wallets having the same private key) is theoretically possible, since keys can be generated without being used for transactions, and are therefore offline until recorded in the blockchain ledger. However, this possibility is effectively negated because the theoretical probability of two or more private keys being the same is extremely low. The number of possible wallets and thus private keys is extremely high, so duplicating or hacking a certain key would be inconceivable.

### Seed phrases

In modern convention a seed phrase is now utilised which is a random 12 to 24 (or even greater) list of dictionary words which is an unencrypted form of the private key. (Words are easier to memorize than numerals). When online, exchange and hardware wallets are generated using random numbers, and the user is asked to supply a seed phrase. If the wallet is misplaced, damaged or compromised, the seed phrase can be used to re-access the wallet and associated keys and cryptocurrency *in toto*.

### Wallets

A number of technologies known as wallets exist that store the key value pair of private and public key known as wallets. A wallet hosts the details of the key pair making cryptocurrency transactions possible. Multiple methods exist for storing keys or seeds in a wallet.

A *brainwallet* or *brain wallet* is a type of wallet in which one memorizes a passcode (a private key or seed phrase). Brainwallets may be attractive due to plausible deniability or protection against governmental seizure, but are vulnerable to password guessing (especially large-scale offline guessing). Several hundred brainwallets exist on the Bitcoin blockchain, but most of them have been drained, sometimes repeatedly.

### Crypto wallets vis-à-vis DApp browsers

DApp browsers are specialized software that supports decentralized applications. DApp browsers are considered to be the browsers of Web3 and are the gateway to access the decentralized applications which are based on blockchain technology. That means all DApp browsers must have a unique code system to unify all the different codes of the DApps.

While crypto wallets are focused on the exchange, purchase, sale of digital assets and support narrowly targeted applications, the browsers support different kinds of applications of various formats, including exchange, games, NFTs marketplaces, etc.

## Characteristics

In addition to the basic function of storing the keys, a cryptocurrency wallet may also have one or more of the following characteristics.

### Simple cryptocurrency wallet

A simple cryptocurrency wallet contains pairs of public and private cryptographic keys. The keys can be used to track ownership, receipt or spend cryptocurrencies. A public key allows others to make payments to the address derived from it, whereas a private key enables the spending of cryptocurrency from that address.

The cryptocurrency itself is not in the wallet. In the case of bitcoin and cryptocurrencies derived from it, the cryptocurrency is decentrally stored and maintained in a publicly available distributed ledger called the *blockchain*.

### Multi-chain cryptocurrency wallet

Multi-chain wallets are designed to support multiple blockchain networks, enabling users to store, manage, and transact different types of cryptocurrencies from a single interface. Unlike single-chain wallets, which are limited to a specific blockchain, multi-chain wallets provide a unified experience for handling various assets. These wallets enhance convenience and security by reducing the need for multiple wallet applications and providing integrated features for multiple digital assets.

Features of a multi-chain wallet:

- **Support for Multiple Blockchains:** Users can hold and manage various blockchains such as Bitcoin, Ethereum, Klever Blockchain, Binance Smart Chain, and more within one wallet.
- **Enhanced Security:** Typically incorporate advanced security measures including two-factor authentication and seed phrase backup.
- **Interoperability:** Facilitates seamless transactions across different blockchain networks.
- **User-friendly Interface:** Designed to be accessible and intuitive, making it easier for users to navigate and manage their assets.

Popular multi-chain wallets include Trust Wallet, Klever Wallet and Exodus, each offering unique features and support for multiple blockchains, therefore, hundreds of cryptocurrencies.

### eID wallet

Some wallets are specifically designed to be compatible with a framework. The European Union is creating an eIDAS compatible European Self-Sovereign Identity Framework (ESSIF) which runs on the European Blockchain Services Infrastructure (EBSI). The EBSI wallet is designed to (securely) provide information, an eID and to sign 'transactions'.

### Key derivation

#### Sequential deterministic wallet

A sequential deterministic wallet utilizes a simple method of generating addresses from a known starting string or "seed". This would utilize a cryptographic hash function, e.g. SHA-256 (seed + n), where n is an ASCII-coded number that starts from 1 and increments as additional keys are needed.

#### Hierarchical deterministic wallet

The hierarchical deterministic (HD) wallet was publicly described in BIP32. As a deterministic wallet, it derives keys from a single master root seed, but instead of having a single "chain" of key pairs, an HD wallet supports multiple independent key pair chains.

This allows a single seed to be used to generate an entire tree of key pairs with a stratified structure.

BIP39 proposed the use of a set of human-readable words to derive the seed used to generate a wallet’s master private key. This mnemonic phrase allows for easier wallet backup and recovery, due to all keys of a wallet being derivable from a single plaintext string.

#### Non-deterministic wallet

In a non-deterministic wallet, each key is randomly generated independently and is not derived from a common seed. Therefore, any backups of the wallet must store each and every private key used as an address, as well as a buffer of future keys that may have already been issued as addresses but have not yet received payments.

## Concerns

A wallet can also have known or unknown vulnerabilities. A supply chain attack or side-channel attack are ways of introducing vulnerabilities. In extreme cases even a computer which is not connected to any network can be hacked.

To mitigate the risk of crypto wallet hacking, one can choose for a cold wallet, which remains offline and disconnected from the internet. A cold wallet refers to a physical device, such as a pen drive, that is utilized as a secure storage medium for transferring money from a hot wallet.

## Security

When using a merchant site that accepts server-side digital wallets, customers enter their name, payment, and delivery information. Following the purchase, the customer is requested to register for a wallet with a user name and password for future purchases.

Wallets are free for consumers but cost retailers. Wallet sellers may receive a portion of merchant purchases made through their wallets. In other circumstances, digital wallet vendors conduct cardholder-merchant transactions for a set fee.
