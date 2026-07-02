---
title: "Introduction to Accounts & Wallets"
source: https://docs.web3js.org/guides/wallet/
domain: web3js
license: LGPL-3.0 (web3.js docs)
tags: web3.js, web3js, ethereum javascript api, web3 provider
fetched: 2026-07-02
---

# Introduction to Accounts & Wallets

The concept of an account is central to Ethereum and it can be used to refer to two types of entities that are native to Ethereum: externally-owned accounts and contract accounts. This document relates *exclusively* to **externally-owned accounts**. An externally-owned account is associated with a "key pair", which is a general concept that is related to public-key cryptography. The key pair consists of a private key, which must always be kept secret, and a public key, which is used to derive a public identifier (address) for an account. Ethereum accounts have an ETH balance, which can be transferred to other accounts or used to pay for interactions with smart contracts. Anyone with access to an account's private key has the ability to control that account's ETH balance, so it's important that an account's private key is always kept secret. In addition to the general guidelines for protecting private keys, private keys should never be included in client-side code that can be seen by end users and should never be committed to code repositories.

In the context of this document, the term "wallet" refers to a collection of accounts and should not be confused with wallet "applications".

## Accounts

The `web3-eth-accounts` package contains functions to generate Ethereum accounts, sign transactions and data, and more. In Web3.js, the `Web3Account` interface is used to represent an externally-owned account. The following snippet demonstrates using Web3.js to generate a new random account and then using that account to sign a message:

```js
const account = web3.eth.accounts.create();

console.log(account);

const signature = account.sign('Hello, Web3.js!');
```

Note that many of these values will change each time the code is executed, since a new account is created each time.

In addition to generating new random accounts, the Account package can also be used to load an existing account from its private key, as in the following snippet:

```js
const account = web3.eth.accounts.privateKeyToAccount('<redacted>');

console.log(account);

const signature = account.sign('Hello, Web3.js!');
```

### Account Methods

The following is a list of `Accounts` methods in the `web3.eth.accounts` package with descriptions and example usage:

- create
- decrypt
- encrypt
- hashMessage
- parseAndValidatePrivateKey
- privateKeyToAccount
- privateKeyToAddress
- privateKeyToPublicKey
- recover
- recoverTransaction
- sign
- signRaw
- signTransaction

## Wallets

A Web3.js wallet is a collection of accounts and is represented with the `Wallet` class. When a wallet is used to track an account, that account is added to an internal context (i.e. `Web3Context`), which makes it easier to use that account in the future - this is described in more detail in the transactions tutorial. The following snippet demonstrates creating a wallet with 2 new random accounts and using the second account to sign a message:

```js
const wallet = web3.eth.accounts.wallet.create(2);

console.log(wallet);

const signature = wallet[1].sign('Hello, Web3.js!');

console.log(signature);
```

Note that many of these values will change each time the code is executed, since new accounts are created each time.

In addition to generating new random accounts, a wallet can also be used to load an existing account from its private key, as in the following snippet:

```js
const wallet = web3.eth.accounts.wallet.add('<redacted>');

console.log(wallet);
```

New accounts can be added to an existing wallet, as is demonstrated by the following code snippet:

```js
const wallet = web3.eth.accounts.wallet.create(1);

console.log(wallet);

wallet.create(1);

console.log(wallet);

const newAccount = web3.eth.accounts.create();
wallet.add(newAccount);

console.log(wallet);
```

### Wallet Methods

The following is a list of `Wallet` methods in the `web3.eth.accounts.wallet` package with description and example usage:

- add
- clear
- create
- decrypt
- encrypt
- get
- load
- remove
- save
- getStorage

## Next Steps

This document is just an introduction to Web3.js accounts and wallets. Here are some suggestions for what to review next:

- Learn how to transfer ETH from one account to another.
- Build a front-end application that uses injected accounts from the MetaMask wallet.
- Use an account to deploy and interact with a smart contract.
