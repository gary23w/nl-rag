---
title: "Quickstart"
source: https://docs.web3js.org/guides/getting_started/quickstart
domain: web3js
license: LGPL-3.0 (web3.js docs)
tags: web3.js, web3js, ethereum javascript api, web3 provider
fetched: 2026-07-02
---

# Quickstart

Use the live code editor to try Web3.js in your browser now! Keep reading to learn how to use Web3.js in a local development environment.

## Live Code Editor

## Installation

If NPM is being used as package manager, install Web3.js with the following command:

```
npm i web3
```

For projects using Yarn as a package manager, use:

```
yarn add web3
```

Note: Installing Web3.js in this way will bring in all Web3.js sub-packages. If you only need specific packages, it is recommended to install them individually (e.g, if you want the Contract package, use `npm i web3-eth-contract` instead)

## Importing Web3.js

Web3.js v4 supports both CommonJS (CJS) and native ECMAScript module (ESM) imports. For importing the main Web3 class in CJS, use:

```js
const { Web3 } = require('web3');
```

For ESM-style imports, use:

```ts
import { Web3 } from 'web3';
```

## Initialize `Web3` with a Provider

Providers are services that are responsible for enabling connectivity with the Ethereum network. The `Web3` object must be initialized with a valid provider to function as intended. Web3.js supports HTTP, WebSocket, and IPC providers, and exposes packages for working with each type of provider.

Web3.js is in compliance with EIP-1193, the Ethereum Provider JavaScript API, so any EIP-1193 provider can be used to initialize the `Web3` object.

```ts
import { Web3 } from 'web3';

const web3 = new Web3('https://mainnet.infura.io/v3/YOUR_INFURA_ID');

web3.eth.getBlockNumber().then(console.log);
```

## Querying the Blockchain

After instantiating the `Web3` instance with a provider, the `web3-eth` package can be used to fetch data from the Ethereum network:

```ts
await web3.eth.getBalance('0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045');

await web3.eth.getBlockNumber();

await web3.eth.getChainId();

await web3.eth.getTransactionCount('0x37826D8B5F4B175517A0f42c886f8Fca38C55Fe7');

await web3.eth.getGasPrice();
```

## Setting Up a Wallet

To send transactions to the Ethereum network (e.g. transferring ETH or interacting with smart contracts), it's necessary to use an account with funds to cover gas fees.

The `Wallet` object is designed to manage a set of accounts that can be used to send transactions with `web3.eth.sendTransaction` or `web3.eth.contract.methods.contractfunction().send()`.

### Create a Random Account

Using the `Wallet` to create a random account is a good way to accelerate the development process, but it's not suitable for mainnet or production uses, since random accounts will not have funds to cover gas fees. Use the `Wallet.create` method to create a random account.

```ts
web3.eth.accounts.wallet.create(1);
```

### Add an Account from a Private Key

Use the `Wallet.add` method to use a private key to add an existing account to a wallet.

warning

Private keys are sensitive data and should be treated as such. Make sure that private keys are kept private, which includes making sure they are not committed to code repositories.

```ts
const account = web3.eth.accounts.wallet.add(
	'0x50d349f5cf627d44858d6fcb6fbf15d27457d35c58ba2d5cfeaf455f25db5bec',
);

console.log(account[0].address);

console.log(account[0].privateKey);
```

### Transfer ETH

This is an example of using a private key to add an account to a wallet, and then using that account to transfer ETH:

```ts
const account = web3.eth.accounts.wallet.add(
	'0x50d349f5cf627d44858d6fcb6fbf15d27457d35c58ba2d5cfeaf455f25db5bec',
);

const tx = {
	from: account[0].address,
	to: '0xa3286628134bad128faeef82f44e99aa64085c94',
	value: web3.utils.toWei('1', 'ether'),
};

const txReceipt = await web3.eth.sendTransaction(tx);

console.log('Tx hash:', txReceipt.transactionHash);
```

## Interact with Smart Contracts

Smart contracts are programs that run on the Ethereum network. Keep reading to learn how to use Web3.js to interact with smart contracts.

### Instantiate a Smart Contract

The first step to interacting with a smart contract is to instantiate it, which requires the ABI and address of the smart contract. The following examples demonstrates instantiating the Uniswap token smart contract:

```ts
const address = '0x1f9840a85d5af5bf1d1762f925bdaddc4201f984';

const ABI = [
	{
		name: 'symbol',
		outputs: [{ type: 'string' }],
		type: 'function',
	},
	{
		name: 'totalSupply',
		outputs: [{ type: 'uint256' }],
		type: 'function',
	},
];

const uniswapToken = new web3.eth.Contract(abi, address);
```

### Read Methods

Since reading data from a smart contract does not consume any gas, it's not necessary to use an account to do so. Here are some examples of reading data from the Uniswap token smart contract:

```ts
const symbol = await uniswapToken.methods.symbol().call();

console.log('Uniswap symbol:', symbol);

const totalSupply = await uniswapToken.methods.totalSupply().call();

console.log('Uniswap Total supply:', totalSupply);
```

### Write Methods

Writing data to a smart contract consumes gas and requires the use of an account with funds. The following example demonstrates such an interaction:

```ts
const to = '0xcf185f2F3Fe19D82bFdcee59E3330FD7ba5f27ce';

const value = web3.utils.toWei('1', 'ether');

const txReceipt = await uniswapToken.methods.transfer(to, value).send({ from: account[0].address });

console.log('Tx hash:', txReceipt.transactionHash);
```

### Query Past Events

Smart contracts emit events to communicate important interactions. This example demonstrates how to query the Uniswap token smart contract for all `Transfer` events that occurred after a certain block number:

```ts
const eventTransfer = await uniswapToken.getPastEvents('Transfer', { fromBlock: 18850576 });

console.log(eventTransfer);
```

note

You can only query logs from the most recent 100,000 blocks.

### Subscribing to Events

Web3.js allows user to subscribe to events for real-time notification of important contract interactions. Here is an example of creating a subscription to the Uniswap token's `Transfer` event:

note

HTTP providers do not support real-time event subscriptions. Use one of the other provider types to subscribe to real-time events.

```ts
import { Web3 } from 'web3';

const web3 = new Web3('wss://ethereum.publicnode.com');

const uniswapToken = new web3.eth.Contract(abi, address);

const subscription = uniswapToken.events.Transfer();

subscription.on('data', console.log);
```
