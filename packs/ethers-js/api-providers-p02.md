---
title: "Untitled (part 2/2)"
source: https://docs.ethers.org/v6/api/providers/
domain: ethers-js
license: MIT (ethers.js docs)
tags: ethers.js, ethers, ethereum provider, contract abstraction
fetched: 2026-07-02
part: 2/2
---

# Untitled

In modern networks, for transactions that are included this is the effective gas price (the fee per gas that was actually charged), while for transactions that have not been included yet is the maxFeePerGas.

For legacy transactions, or transactions on legacy networks, this is the fee that will be charged per unit of gas the transaction consumes.

<src>

transactionResponse

.

hash

⇒

string

read-only

The transaction hash.

<src>

transactionResponse

.

index

⇒

number

read-only

The index within the block that this transaction resides at.

<src>

transactionResponse

.

maxFeePerBlobGas

⇒

null

|

bigint

read-only

The EIP-4844 max fee per BLOb gas.

<src>

transactionResponse

.

maxFeePerGas

⇒

null

|

bigint

read-only

The maximum fee (per unit of gas) to allow this transaction to charge the sender.

<src>

transactionResponse

.

maxPriorityFeePerGas

⇒

null

|

bigint

read-only

The maximum priority fee (per unit of gas) to allow a validator to charge the sender. This is inclusive of the maxFeeFeePerGas.

<src>

transactionResponse

.

nonce

⇒

number

read-only

The nonce, which is used to prevent replay attacks and offer a method to ensure transactions from a given sender are explicitly ordered.

When sending a transaction, this must be equal to the number of transactions ever sent by from.

<src>

transactionResponse

.

provider

⇒

Provider

read-only

The provider this is connected to, which will influence how its methods will resolve its async inspection methods.

<src>

transactionResponse

.

signature

⇒

Signature

read-only

The signature.

<src>

transactionResponse

.

to

⇒

null

|

string

read-only

The receiver of this transaction.

If null, then the transaction is an initcode transaction. This means the result of executing the data will be deployed as a new contract on chain (assuming it does not revert) and the address may be computed using getCreateAddress.

<src>

transactionResponse

.

type

⇒

number

read-only

The EIP-2718 transaction envelope type. This is 0 for legacy transactions types.

<src>

transactionResponse

.

value

⇒

bigint

read-only

The value, in wei. Use formatEther to format this value as ether.

METHODS

<src>

transactionResponse

.

confirmations

(

)

⇒

Promise<

number

>

Resolve to the number of confirmations this transaction has.

<src>

transactionResponse

.

getBlock

(

)

⇒

Promise<

null

|

Block

>

Resolves to the Block that this transaction was included in.

This will return null if the transaction has not been included yet.

<src>

transactionResponse

.

getTransaction

(

)

⇒

Promise<

null

|

TransactionResponse

>

Resolves to this transaction being re-requested from the provider. This can be used if you have an unmined transaction and wish to get an up-to-date populated instance.

<src>

transactionResponse

.

isBerlin

(

)

⇒

boolean

Returns true if the transaction is a Berlin (i.e. type == 1) transaction. See EIP-2930.

This provides a Type Guard that this transaction will have the null-ness for hardfork-specific properties set correctly.

<src>

transactionResponse

.

isCancun

(

)

⇒

boolean

Returns true if hte transaction is a Cancun (i.e. type == 3) transaction. See EIP-4844.

<src>

transactionResponse

.

isLegacy

(

)

⇒

boolean

Returns true if the transaction is a legacy (i.e. type == 0) transaction.

This provides a Type Guard that this transaction will have the null-ness for hardfork-specific properties set correctly.

<src>

transactionResponse

.

isLondon

(

)

⇒

boolean

Returns true if the transaction is a London (i.e. type == 2) transaction. See EIP-1559.

This provides a Type Guard that this transaction will have the null-ness for hardfork-specific properties set correctly.

<src>

transactionResponse

.

isMined

(

)

⇒

boolean

Returns true if this transaction has been included.

This is effective only as of the time the TransactionResponse was instantiated. To get up-to-date information, use getTransaction.

This provides a Type Guard that this transaction will have non-null property values for properties that are null for unmined transactions.

<src>

transactionResponse

.

removedEvent

(

)

⇒

OrphanFilter

Returns a filter which can be used to listen for orphan events that evict this transaction.

<src>

transactionResponse

.

reorderedEvent

(

other

?:

TransactionResponse

)

⇒

OrphanFilter

Returns a filter which can be used to listen for orphan events that re-order this event against other.

<src>

transactionResponse

.

replaceableTransaction

(

startBlock

:

number

)

⇒

TransactionResponse

Returns a new TransactionResponse instance which has the ability to detect (and throw an error) if the transaction is replaced, which will begin scanning at startBlock.

This should generally not be used by developers and is intended primarily for internal use. Setting an incorrect startBlock can have devastating performance consequences if used incorrectly.

<src>

transactionResponse

.

toJSON

(

)

⇒

any

Returns a JSON-compatible representation of this transaction.

<src>

transactionResponse

.

wait

(

confirms

?:

number

,

timeout

?:

number

)

⇒

Promise<

null

|

TransactionReceipt

>

Resolves once this transaction has been mined and has confirms blocks including it (default: 1) with an optional timeout.

This can resolve to null only if confirms is 0 and the transaction has not been mined, otherwise this will wait until enough confirmations have completed.

interface

WebSocketLike

A generic interface to a Websocket-like object.

PROPERTIES

<src>

webSocketLike

.

onerror

⇒

null

|

PAREN<

(

args:

Array<

any

>

) =>

any

>

<src>

webSocketLike

.

onmessage

⇒

null

|

PAREN<

(

args:

Array<

any

>

) =>

any

>

<src>

webSocketLike

.

onopen

⇒

null

|

PAREN<

(

args:

Array<

any

>

) =>

any

>

<src>

webSocketLike

.

readyState

⇒

number

METHODS

<src>

webSocketLike

.

close

(

code

?:

number

,

reason

?:

string

)

⇒

void

<src>

webSocketLike

.

send

(

payload

:

any

)

⇒

void

class

WebSocketProvider

inherits from

SocketProvider

,

JsonRpcApiProvider

A JSON-RPC provider which is backed by a WebSocket.

WebSockets are often preferred because they retain a live connection to a server, which permits more instant access to events.

However, this incurs higher server infrasturture costs, so additional resources may be required to host your own WebSocket nodes and many third-party services charge additional fees for WebSocket endpoints.

PROPERTIES

<src>

webSocketProvider

.

websocket

⇒

WebSocketLike

read-only

CREATING INSTANCES

<src>

new

WebSocketProvider

(

url

:

string

|

WebSocketLike

|

WebSocketCreator

,

network

?:

Networkish

,

options

?:

JsonRpcApiProviderOptions

)

Networks

A Network encapsulates the various properties required to interact with a specific chain.

TYPES

<src>

Networkish

⇒

Network

|

number

|

bigint

|

string

|

{ chainId?:

number

, ensAddress?:

string

, ensNetwork?:

number

, ensUniversalResolver?:

string

, name?:

string

}

A Networkish can be used to allude to a Network, by specifing:

a Network object a well-known (or registered) network name a well-known (or registered) chain ID an object with sufficient details to describe a network

class

Network

A Network provides access to a chain's properties and allows for plug-ins to extend functionality.

PROPERTIES

<src>

network

.

chainId

⇒

bigint

The network chain ID.

<src>

network

.

name

⇒

string

The network common name.

This is the canonical name, as networks migh have multiple names.

<src>

network

.

plugins

⇒

Array<

NetworkPlugin

>

read-only

Returns the list of plugins currently attached to this Network.

CREATING INSTANCES

<src>

new

Network

(

name

:

string

,

chainId

:

BigNumberish

)

Creates a new Network for name and chainId.

<src>

Network

.

from

(

network

?:

Networkish

)

⇒

Network

Returns a new Network for the network name or chainId.

METHODS

<src>

network

.

attachPlugin

(

plugin

:

NetworkPlugin

)

⇒

this

Attach a new plugin to this Network. The network name must be unique, excluding any fragment.

<src>

network

.

clone

(

)

⇒

Network

Create a copy of this Network.

<src>

network

.

computeIntrinsicGas

(

tx

:

TransactionLike

)

⇒

number

Compute the intrinsic gas required for a transaction.

A GasCostPlugin can be attached to override the default values.

<src>

network

.

getPlugin

(

name

:

string

)

⇒

null

|

T

Return the plugin, if any, matching name exactly. Plugins with fragments will not be returned unless name includes a fragment.

<src>

network

.

getPlugins

(

basename

:

string

)

⇒

Array<

T

>

Gets a list of all plugins that match name, with otr without a fragment.

<src>

network

.

inspect

(

)

⇒

string

<src>

network

.

matches

(

other

:

Networkish

)

⇒

boolean

Returns true if other matches this network. Any chain ID must match, and if no chain ID is present, the name must match.

This method does not currently check for additional properties, such as ENS address or plug-in compatibility.

<src>

network

.

toJSON

(

)

⇒

any

Returns a JSON-compatible representation of a Network.

<src>

network

.

toString

(

)

⇒

string

STATIC METHODS

<src>

Network

.

register

(

nameOrChainId

:

string

|

number

|

bigint

,

networkFunc

:

() =>

Network

)

⇒

void

Register nameOrChainId with a function which returns an instance of a Network representing that chain.
