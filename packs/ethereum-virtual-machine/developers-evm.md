---
title: "Ethereum Virtual Machine (EVM)"
source: https://ethereum.org/en/developers/docs/evm/
domain: ethereum-virtual-machine
license: CC-BY-SA-4.0 / CC-BY-4.0 (ethereum.org)
tags: evm, ethereum virtual machine, evm opcode, evm bytecode
fetched: 2026-07-02
---

# Ethereum Virtual Machine (EVM)

Edit page

(opens in a new tab)

The Ethereum Virtual Machine (EVM) is a decentralized virtual environment that executes code consistently and securely across all Ethereum nodes. Nodes run the EVM to execute smart contracts, using "gas" to measure the computational effort required for operations, ensuring efficient resource allocation and network security.

## Prerequisites

Some basic familiarity with common terminology in computer science such as bytes (opens in a new tab), memory (opens in a new tab), and a stack (opens in a new tab) are necessary to understand the EVM. It would also be helpful to be comfortable with cryptography/blockchain concepts like hash functions (opens in a new tab) and the Merkle tree (opens in a new tab).

## From ledger to state machine

The analogy of a 'distributed ledger' is often used to describe blockchains like Bitcoin, which enable a decentralized currency using fundamental tools of cryptography. The ledger maintains a record of activity which must adhere to a set of rules that govern what someone can and cannot do to modify the ledger. For example, a Bitcoin address cannot spend more Bitcoin than it has previously received. These rules underpin all transactions on Bitcoin and many other blockchains.

While Ethereum has its own native cryptocurrency (ether) that follows almost exactly the same intuitive rules, it also enables a much more powerful function: smart contracts. For this more complex feature, a more sophisticated analogy is required. Instead of a distributed ledger, Ethereum is a distributed state machine (opens in a new tab). Ethereum's state is a large data structure which holds not only all accounts and balances, but a *machine state*, which can change from block to block according to a pre-defined set of rules, and which can execute arbitrary machine code. The specific rules of changing state from block to block are defined by the EVM.

(A diagram showing the make up of the EVM) *Diagram adapted from Ethereum EVM illustrated (opens in a new tab)*

## The Ethereum state transition function

The EVM behaves as a mathematical function would: Given an input, it produces a deterministic output. It therefore is quite helpful to more formally describe Ethereum as having a **state transition function**:

```
Y(S, T)= S'
```

Given an old valid state `(S)` and a new set of valid transactions `(T)`, the Ethereum state transition function `Y(S, T)` produces a new valid output state `S'`

### State

In the context of Ethereum, the state is an enormous data structure called a modified Merkle Patricia Trie, which keeps all accounts linked by hashes and reducible to a single root hash stored on the blockchain.

### Transactions

Transactions are cryptographically signed instructions from accounts. There are two types of transactions: those which result in message calls and those which result in contract creation.

Contract creation results in the creation of a new contract account containing compiled smart contract bytecode. Whenever another account makes a message call to that contract, it executes its bytecode.

## EVM instructions

The EVM executes as a stack machine (opens in a new tab) with a depth of 1024 items. Each item is a 256-bit word, which was chosen for the ease of use with 256-bit cryptography (such as Keccak-256 hashes or secp256k1 signatures).

During execution, the EVM maintains a transient *memory* (as a word-addressed byte array), which does not persist between transactions.

### Transient storage

Transient storage is a per-transaction key–value store accessed through the `TSTORE` and `TLOAD` opcodes. It persists across all internal calls during the same transaction but is cleared at the end of the transaction. Unlike memory, transient storage is modeled as part of the EVM state rather than the execution frame, yet it is not committed to the global state. Transient storage enables gas-efficient temporary state sharing across internal calls during a transaction.

### Storage

Contracts contain a Merkle Patricia *storage* trie (as a word-addressable word array), associated with the account in question and part of the global state. This persistent storage differs from transient storage, which is available only for the duration of a single transaction and does not form part of the account's persistent storage trie.

### Opcodes

Compiled smart contract bytecode executes as a number of EVM opcodes, which perform standard stack operations like `XOR`, `AND`, `ADD`, `SUB`, etc. The EVM also implements a number of blockchain-specific stack operations, such as `ADDRESS`, `BALANCE`, `BLOCKHASH`, etc. The opcode set also includes `TSTORE` and `TLOAD`, which provide access to transient storage.

(A diagram showing where gas is needed for EVM operations) *Diagrams adapted from Ethereum EVM illustrated (opens in a new tab)*

## EVM implementations

All implementations of the EVM must adhere to the specification described in the Ethereum Yellowpaper.

Over Ethereum's ten year history, the EVM has undergone several revisions, and there are several implementations of the EVM in various programming languages.

Ethereum execution clients include an EVM implementation. Additionally, there are multiple standalone implementations, including:

- Py-EVM (opens in a new tab) - *Python*
- evmone (opens in a new tab) - *C++*
- ethereumjs-vm (opens in a new tab) - *JavaScript*
- revm (opens in a new tab) - *Rust*

## Tutorials: Ethereum Virtual Machine (EVM) / Opcodes on Ethereum

- Understanding the Yellow Paper's EVM Specifications *– A guided walkthrough of the formal EVM spec from the Ethereum Yellow Paper.*
- Reverse Engineering a Contract *– How to reverse-engineer a compiled smart contract using EVM opcodes.*
