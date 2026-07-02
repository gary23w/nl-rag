---
title: "Untitled (part 1/2)"
source: https://docs.ethers.org/v6/api/providers/
domain: ethers-js
license: MIT (ethers.js docs)
tags: ethers.js, ethers, ethereum provider, contract abstraction
fetched: 2026-07-02
part: 1/2
---

# Untitled

Providers

A Provider provides a connection to the blockchain, which can be used to query its current state, simulate execution and send transactions to update the state.

It is one of the most fundamental components of interacting with a blockchain application, and there are many ways to connect, such as over HTTP, WebSockets or injected providers such as MetaMask.

TYPES

<src>

BlockTag

⇒

BigNumberish

|

string

A BlockTag specifies a specific block.

numeric value - specifies the block height, where the genesis block is block 0; many operations accept a negative value which indicates the block number should be deducted from the most recent block. A numeric value may be a number, bigint, or a decimal of hex string.

blockhash - specifies a specific block by its blockhash; this allows potentially orphaned blocks to be specifed, without ambiguity, but many backends do not support this for some operations.

<src>

BrowserProviderOptions

⇒

{ cacheTimeout?:

number

, polling?:

boolean

, pollingInterval?:

number

, providerInfo?:

Eip6963ProviderInfo

, staticNetwork?:

null

|

boolean

|

Network

}

<src>

DebugEventBrowserProvider

⇒

{ action:

"sendEip1193Payload"

, payload:

{ method:

string

, params:

Array<

any

>

}

}

|

{ action:

"receiveEip1193Result"

, result:

any

}

|

{ action:

"receiveEip1193Error"

, error:

Error

}

The possible additional events dispatched when using the "debug" event on a BrowserProvider.

<src>

GasCostParameters

⇒

{ txAccessListAddress?:

number

, txAccessListStorageKey?:

number

, txBase?:

number

, txCreate?:

number

, txDataNonzero?:

number

, txDataZero?:

number

}

The gas cost parameters for a GasCostPlugin.

<src>

OrphanFilter

⇒

{ hash:

string

, number:

number

, orphan:

"drop-block"

}

|

{ orphan:

"drop-transaction"

, other?:

{ blockHash:

string

, blockNumber:

number

, hash:

string

}

, tx:

{ blockHash:

string

, blockNumber:

number

, hash:

string

}

}

|

{ orphan:

"reorder-transaction"

, other?:

{ blockHash:

string

, blockNumber:

number

, hash:

string

}

, tx:

{ blockHash:

string

, blockNumber:

number

, hash:

string

}

}

|

{ log:

{ address:

string

, blockHash:

string

, blockNumber:

number

, data:

string

, index:

number

, topics:

ReadonlyArray<

string

>

, transactionHash:

string

}

, orphan:

"drop-log"

}

An Orphan Filter allows detecting when an orphan block has resulted in dropping a block or transaction or has resulted in transactions changing order.

Not currently fully supported.

<src>

ProviderEvent

⇒

string

|

Array<

string

|

Array<

string

>

>

|

EventFilter

|

OrphanFilter

A ProviderEvent provides the types of events that can be subscribed to on a Provider.

Each provider may include additional possible events it supports, but the most commonly supported are:

"block" - calls the listener with the current block number on each new block.

"error" - calls the listener on each async error that occurs during the event loop, with the error.

"debug" - calls the listener on debug events, which can be used to troubleshoot network errors, provider problems, etc.

transaction hash - calls the listener on each block after the transaction has been mined; generally .once is more appropriate for this event.

Array - calls the listener on each log that matches the filter.

EventFilter - calls the listener with each matching log

<src>

TopicFilter

⇒

Array<

null

|

string

|

Array<

string

>

>

A TopicFilter provides a struture to define bloom-filter queries.

Each field that is null matches any value, a field that is a string must match exactly that value and array is effectively an OR-ed set, where any one of those values must match.

<src>

WebSocketCreator

⇒

() =>

WebSocketLike

A function which can be used to re-create a WebSocket connection on disconnect.

FUNCTIONS

<src>

copyRequest

(

req

:

TransactionRequest

)

⇒

PreparedTransactionRequest

Returns a copy of req with all properties coerced to their strict types.

<src>

getDefaultProvider

(

network

?:

string

|

Networkish

|

WebSocketLike

,

options

?:

any

)

⇒

AbstractProvider

Returns a default provider for network.

If network is a WebSocketLike or string that begins with "ws:" or "wss:", a WebSocketProvider is returned backed by that WebSocket or URL.

If network is a string that begins with "HTTP:" or "HTTPS:", a JsonRpcProvider is returned connected to that URL.

Otherwise, a default provider is created backed by well-known public Web3 backends (such as INFURA) using community-provided API keys.

The options allows specifying custom API keys per backend (setting an API key to "-" will omit that provider) and options.exclusive can be set to either a backend name or and array of backend names, which will whitelist only those backends.

Current backend strings supported are:

"alchemy" "ankr" "cloudflare" "chainstack" "etherscan" "infura" "publicPolygon" "quicknode"

provider = getDefaultProvider("http://localhost:8545/");

provider = getDefaultProvider("mainnet");

provider = getDefaultProvider("matic", {

etherscan: "MY_API_KEY",

exclusive: [ "etherscan", "infura" ]

});

class

Block

inherits from

BlockParams

A Block represents the data associated with a full block on Ethereum.

PROPERTIES

<src>

block

.

baseFeePerGas

⇒

null

|

bigint

read-only

The base fee per gas that all transactions in this block were charged.

This adjusts after each block, depending on how congested the network is.

<src>

block

.

blobGasUsed

⇒

null

|

bigint

read-only

The total amount of blob gas consumed by the transactions within the block. See EIP-4844.

<src>

block

.

date

⇒

null

|

Date

read-only

The Date this block was included at.

<src>

block

.

difficulty

⇒

bigint

read-only

The difficulty target.

On legacy networks, this is the proof-of-work target required for a block to meet the protocol rules to be included.

On modern networks, this is a random number arrived at using randao. @TODO: Find links?

<src>

block

.

excessBlobGas

⇒

null

|

bigint

read-only

The running total of blob gas consumed in excess of the target, prior to the block. See EIP-4844.

<src>

block

.

extraData

⇒

string

read-only

Any extra data the validator wished to include.

<src>

block

.

gasLimit

⇒

bigint

read-only

The total gas limit for this block.

<src>

block

.

gasUsed

⇒

bigint

read-only

The total gas used in this block.

<src>

block

.

hash

⇒

null

|

string

read-only

The block hash.

This hash includes all properties, so can be safely used to identify an exact set of block properties.

<src>

block

.

length

⇒

number

read-only

The number of transactions in this block.

<src>

block

.

miner

⇒

string

read-only

The miner coinbase address, wihch receives any subsidies for including this block.

<src>

block

.

nonce

⇒

string

read-only

The nonce.

On legacy networks, this is the random number inserted which permitted the difficulty target to be reached.

<src>

block

.

number

⇒

number

read-only

The block number, sometimes called the block height. This is a sequential number that is one higher than the parent block.

<src>

block

.

parentBeaconBlockRoot

⇒

null

|

string

The hash tree root of the parent beacon block for the given execution block. See EIP-4788.

<src>

block

.

parentHash

⇒

string

read-only

The block hash of the parent block.

<src>

block

.

prefetchedTransactions

⇒

Array<

TransactionResponse

>

read-only

Returns the complete transactions, in the order they were executed within the block.

This is only available for blocks which prefetched transactions, by passing true to prefetchTxs into provider.getBlock.

<src>

block

.

prevRandao

⇒

null

|

string

read-only

The latest RANDAO mix of the post beacon state of the previous block.

<src>

block

.

provider

⇒

Provider

read-only

The provider connected to the block used to fetch additional details if necessary.

<src>

block

.

receiptsRoot

⇒

null

|

string

read-only

The hash of the transaction receipts trie.

<src>

block

.

stateRoot

⇒

null

|

string

read-only

The root hash for the global state after applying changes in this block.

<src>

block

.

timestamp

⇒

number

read-only

The timestamp for this block, which is the number of seconds since epoch that this block was included.

<src>

block

.

transactions

⇒

ReadonlyArray<

string

>

read-only

Returns the list of transaction hashes, in the order they were executed within the block.

<src>

block

.

transactionsRoot

⇒

null

|

string

read-only

The hash of the transactions.

CREATING INSTANCES

<src>

new

Block

(

block

:

BlockParams

,

provider

:

Provider

)

Create a new Block object.

This should generally not be necessary as the unless implementing a low-level library.

METHODS

<src>

block

.

getPrefetchedTransaction

(

indexOrHash

:

number

|

string

)

⇒

TransactionResponse

If a Block was fetched with a request to include the transactions this will allow synchronous access to those transactions.

If the transactions were not prefetched, this will throw.

<src>

block

.

getTransaction

(

indexOrHash

:

number

|

string

)

⇒

Promise<

TransactionResponse

>

Get the transaction at indexe within this block.

<src>

block

.

isLondon

(

)

⇒

boolean

Returns true if this block is an EIP-2930 block.

<src>

block

.

isMined

(

)

⇒

boolean

Returns true if this block been mined. This provides a type guard for all properties on a MinedBlock.

<src>

block

.

toJSON

(

)

⇒

any

Returns a JSON-friendly value.

interface

BrowserDiscoverOptions

Specifies how EIP-6963 discovery should proceed.

See: BrowserProvider-discover

PROPERTIES

<src>

browserDiscoverOptions

.

anyProvider

⇒

boolean

Return the first detected provider. Otherwise wait for timeout and allowing filtering before selecting the desired provider.

<src>

browserDiscoverOptions

.

filter

⇒

(

found:

Array<

Eip6963ProviderInfo

>

) =>

null

|

BrowserProvider

|

Eip6963ProviderInfo

Explicitly choose which provider to used once scanning is complete.

<src>

browserDiscoverOptions

.

provider

⇒

Eip1193Provider

Override provider detection with this provider.

<src>

browserDiscoverOptions

.

timeout

⇒

number

Duration to wait to detect providers. (default: 300ms)

<src>

browserDiscoverOptions

.

window

⇒

any

Use the provided window context. Useful in non-standard environments or to hijack where a provider comes from.

class

BrowserProvider

A BrowserProvider is intended to wrap an injected provider which adheres to the EIP-1193 standard, which most (if not all) currently do.

PROPERTIES

<src>

browserProvider

.

providerInfo

⇒

null

|

Eip6963ProviderInfo

read-only

CREATING INSTANCES

<src>

new

BrowserProvider

(

ethereum

:

Eip1193Provider

,

network

?:

Networkish

,

options

?:

BrowserProviderOptions

)

Connect to the ethereum provider, optionally forcing the network.

METHODS

<src>

browserProvider

.

_send

(

payload

:

JsonRpcPayload

|

Array<

JsonRpcPayload

>

)

⇒

Promise<

Array<

JsonRpcResult

|

JsonRpcError

>

>

<src>

browserProvider

.

getRpcError

(

payload

:

JsonRpcPayload

,

error

:

JsonRpcError

)

⇒

Error

<src>

browserProvider

.

getSigner

(

address

?:

number

|

string

)

⇒

Promise<

JsonRpcSigner

>

<src>

browserProvider

.

hasSigner

(

address

:

number

|

string

)

⇒

Promise<

boolean

>

Resolves to true if the provider manages the address.

<src>

browserProvider

.

send

(

method

:

string

,

params

:

Array<

any

>

|

Record<

string

,

any

>

)

⇒

Promise<

any

>

STATIC METHODS

<src>

BrowserProvider

.

discover

(

options

?:

BrowserDiscoverOptions

)

⇒

Promise<

null

|

BrowserProvider

>

Discover and connect to a Provider in the Browser using the EIP-6963 discovery mechanism. If no providers are present, null is resolved.

interface

ContractRunner

A ContractRunner is a generic interface which defines an object capable of interacting with a Contract on the network.

The more operations supported, the more utility it is capable of.

The most common ContractRunners are Providers which enable read-only access and Signers which enable write-access.

PROPERTIES

<src>

contractRunner

.

call

⇒

(

tx:

TransactionRequest

) =>

Promise<

string

>

Required for pure, view or static calls to contracts.

<src>

contractRunner

.

estimateGas

⇒

(

tx:

TransactionRequest

) =>

Promise<

bigint

>

Required to estimate gas.

<src>

contractRunner

.

provider

⇒

null

|

Provider

The provider used for necessary state querying operations.

This can also point to the ContractRunner itself, in the case of an AbstractProvider.

<src>

contractRunner

.

resolveName

⇒

(

name:

string

) =>

Promise<

null

|

string

>

Required to support ENS names

<src>

contractRunner

.

sendTransaction

⇒

(

tx:

TransactionRequest

) =>

Promise<

TransactionResponse

>

Required for state mutating calls

interface

Eip1193Provider

The interface to an EIP-1193 provider, which is a standard used by most injected providers, which the BrowserProvider accepts and exposes the API of.

METHODS

<src>

eip1193Provider

.

request

(

request

:

{ method:

string

, params?:

Array<

any

>

|

Record<

string

,

any

>

}

)

⇒

Promise<

any

>

See EIP-1193 for details on this method.

interface

Eip6963ProviderInfo

Provider info provided by the EIP-6963 discovery mechanism.

PROPERTIES

<src>

eip6963ProviderInfo

.

icon

⇒

string

<src>

eip6963ProviderInfo

.

name

⇒

string

<src>

eip6963ProviderInfo

.

rdns

⇒

string

<src>

eip6963ProviderInfo

.

uuid

⇒

string

class

EnsPlugin

inherits from

NetworkPlugin

An EnsPlugin allows a Network to specify the ENS Registry Contract address and the target network to use when using that contract.

Various testnets have their own instance of the contract to use, but in general, the mainnet instance supports multi-chain addresses and should be used.

PROPERTIES

<src>

ensPlugin

.

address

⇒

string

read-only

The ENS Registrty Contract address.

<src>

ensPlugin

.

targetNetwork

⇒

number

read-only

The chain ID that the ENS contract lives on.

<src>

ensPlugin

.

universalResolver

⇒

string

read-only

The Universal Resolver Contract Address.

CREATING INSTANCES

<src>

new

EnsPlugin

(

address

?:

null

|

string

,

targetNetwork

?:

null

|

number

,

universalResolver

?:

string

)

Creates a new EnsPlugin connected to address on the targetNetwork. The default ENS address and mainnet is used if unspecified.

interface

EventFilter

An EventFilter allows efficiently filtering logs (also known as events) using bloom filters included within blocks.

PROPERTIES

<src>

eventFilter

.

address

⇒

AddressLike

|

Array<

AddressLike

>

<src>

eventFilter

.

topics

⇒

TopicFilter

class

FeeData

A FeeData wraps all the fee-related values associated with the network.

PROPERTIES

<src>

feeData

.

gasPrice

⇒

null

|

bigint

read-only

The gas price for legacy networks.

<src>

feeData

.

maxFeePerGas

⇒

null

|

bigint

read-only

The maximum fee to pay per gas.

The base fee per gas is defined by the network and based on congestion, increasing the cost during times of heavy load and lowering when less busy.

The actual fee per gas will be the base fee for the block and the priority fee, up to the max fee per gas.

This will be null on legacy networks (i.e. pre-EIP-1559)

<src>

feeData

.

maxPriorityFeePerGas

⇒

null

|

bigint

read-only

The additional amout to pay per gas to encourage a validator to include the transaction.

The purpose of this is to compensate the validator for the adjusted risk for including a given transaction.

This will be null on legacy networks (i.e. pre-EIP-1559)

CREATING INSTANCES

<src>

new

FeeData

(

gasPrice

?:

null

|

bigint

,

maxFeePerGas

?:

null

|

bigint

,

maxPriorityFeePerGas

?:

null

|

bigint

)

Creates a new FeeData for gasPrice, maxFeePerGas and maxPriorityFeePerGas.

METHODS

<src>

feeData

.

toJSON

(

)

⇒

any

Returns a JSON-friendly value.

class

FeeDataNetworkPlugin

inherits from

NetworkPlugin

A FeeDataNetworkPlugin allows a network to provide and alternate means to specify its fee data.

For example, a network which does not support EIP-1559 may choose to use a Gas Station site to approximate the gas price.

PROPERTIES

<src>

feeDataNetworkPlugin

.

feeDataFunc

⇒

(

provider:

Provider

) =>

Promise<

FeeData

>

read-only

The fee data function provided to the constructor.

CREATING INSTANCES

<src>

new

FeeDataNetworkPlugin

(

feeDataFunc

:

(

provider:

Provider

) =>

Promise<

FeeData

>

)

Creates a new FeeDataNetworkPlugin.

METHODS

<src>

feeDataNetworkPlugin

.

getFeeData

(

provider

:

Provider

)

⇒

Promise<

FeeData

>

Resolves to the fee data.

class

FetchUrlFeeDataNetworkPlugin

inherits from

NetworkPlugin

PROPERTIES

<src>

fetchUrlFeeDataNetworkPlugin

.

processFunc

⇒

(

f:

() =>

Promise<

FeeData

>

,

p:

Provider

,

r:

FetchRequest

) =>

Promise<

{ gasPrice?:

null

|

bigint

, maxFeePerGas?:

null

|

bigint

, maxPriorityFeePerGas?:

null

|

bigint

}

>

read-only

The callback to use when computing the FeeData.

<src>

fetchUrlFeeDataNetworkPlugin

.

url

⇒

string

read-only

The URL to initialize the FetchRequest with in processFunc.

CREATING INSTANCES

<src>

new

FetchUrlFeeDataNetworkPlugin

(

url

:

string

,

processFunc

:

(

f:

() =>

Promise<

FeeData

>

,

p:

Provider

,

r:

FetchRequest

) =>

Promise<

{ gasPrice?:

null

|

bigint

, maxFeePerGas?:

null

|

bigint

, maxPriorityFeePerGas?:

null

|

bigint

}

>

)

Creates a new FetchUrlFeeDataNetworkPlugin which will be used when computing the fee data for the network.

interface

Filter

inherits from

EventFilter

A Filter allows searching a specific range of blocks for mathcing logs.

PROPERTIES

<src>

filter

.

fromBlock

⇒

BlockTag

The start block for the filter (inclusive).

<src>

filter

.

toBlock

⇒

BlockTag

The end block for the filter (inclusive).

interface

FilterByBlockHash

inherits from

EventFilter

A FilterByBlockHash allows searching a specific block for mathcing logs.

PROPERTIES

<src>

filterByBlockHash

.

blockHash

⇒

string

The blockhash of the specific block for the filter.

class

GasCostPlugin

inherits from

NetworkPlugin

A GasCostPlugin allows a network to provide alternative values when computing the intrinsic gas required for a transaction.

PROPERTIES

<src>

gasCostPlugin

.

effectiveBlock

⇒

number

read-only

The block number to treat these values as valid from.

This allows a hardfork to have updated values included as well as mulutiple hardforks to be supported.

<src>

gasCostPlugin

.

txAccessListAddress

⇒

number

read-only

The fee per address in the EIP-2930 access list.

<src>

gasCostPlugin

.

txAccessListStorageKey

⇒

number

read-only

The fee per storage key in the EIP-2930 access list.

<src>

gasCostPlugin

.

txBase

⇒

number

read-only

The transactions base fee.

<src>

gasCostPlugin

.

txCreate

⇒

number

read-only

The fee for creating a new account.

<src>

gasCostPlugin

.

txDataNonzero

⇒

number

read-only

The fee per non-zero-byte in the data.

<src>

gasCostPlugin

.

txDataZero

⇒

number

read-only

The fee per zero-byte in the data.

CREATING INSTANCES

<src>

new

GasCostPlugin

(

effectiveBlock

?:

number

,

costs

?:

GasCostParameters

)

Creates a new GasCostPlugin from effectiveBlock until the latest block or another GasCostPlugin supercedes that block number, with the associated costs.

class

IpcSocketProvider

inherits from

SocketProvider

,

JsonRpcApiProvider

An IpcSocketProvider connects over an IPC socket on the host which provides fast access to the node, but requires the node and the script run on the same machine.

PROPERTIES

<src>

ipcSocketProvider

.

socket

⇒

Socket

read-only

The connected socket.

CREATING INSTANCES

<src>

new

IpcSocketProvider

(

path

:

string

,

network

?:

Networkish

,

options

?:

JsonRpcApiProviderOptions

)

class

Log

inherits from

LogParams

A Log in Ethereum represents an event that has been included in a transaction using the LOG* opcodes, which are most commonly used by Solidity's emit for announcing events.

PROPERTIES

<src>

log

.

address

⇒

string

read-only

The address of the contract that emitted this log.

<src>

log

.

blockHash

⇒

string

read-only

The block hash of the block this log occurred in. Use the log.getBlock to get the Block.

<src>

log

.

blockNumber

⇒

number

read-only

The block number of the block this log occurred in. It is preferred to use the block.hash when fetching the related Block, since in the case of an orphaned block, the block at that height may have changed.

<src>

log

.

data

⇒

string

read-only

The data included in this log when it was emitted.

<src>

log

.

index

⇒

number

read-only

The index within the block this log occurred at. This is generally not useful to developers, but can be used with the various roots to proof inclusion within a block.

<src>

log

.

provider

⇒

Provider

read-only

The provider connected to the log used to fetch additional details if necessary.

<src>

log

.

removed

⇒

boolean

read-only

If the Log represents a block that was removed due to an orphaned block, this will be true.

This can only happen within an orphan event listener.

<src>

log

.

topics

⇒

ReadonlyArray<

string

>

read-only

The indexed topics included in this log when it was emitted.

All topics are included in the bloom filters, so they can be efficiently filtered using the provider.getLogs method.

<src>

log

.

transactionHash

⇒

string

read-only

The transaction hash of the transaction this log occurred in. Use the log.getTransaction to get the TransactionResponse.

<src>

log

.

transactionIndex

⇒

number

read-only

The index within the transaction of this log.

METHODS

<src>

log

.

getBlock

(

)

⇒

Promise<

Block

>

Returns the block that this log occurred in.

<src>

log

.

getTransaction

(

)

⇒

Promise<

TransactionResponse

>

Returns the transaction that this log occurred in.

<src>

log

.

getTransactionReceipt

(

)

⇒

Promise<

TransactionReceipt

>

Returns the transaction receipt fot the transaction that this log occurred in.

<src>

log

.

toJSON

(

)

⇒

any

Returns a JSON-compatible object.

interface

MinedBlock

inherits from

Block

,

BlockParams

An Interface to indicate a Block has been included in the blockchain. This asserts a Type Guard that necessary properties are non-null.

Before a block is included, it is a pending block.

PROPERTIES

<src>

minedBlock

.

date

⇒

Date

read-only

The block date, created from the timestamp.

<src>

minedBlock

.

hash

⇒

string

read-only

The block hash.

<src>

minedBlock

.

miner

⇒

string

read-only

The miner of the block, also known as the author or block producer.

<src>

minedBlock

.

number

⇒

number

read-only

The block number also known as the block height.

<src>

minedBlock

.

timestamp

⇒

number

read-only

The block timestamp, in seconds from epoch.

interface

MinedTransactionResponse

inherits from

TransactionResponse

,

TransactionResponseParams

A MinedTransactionResponse is an interface representing a transaction which has been mined and allows for a type guard for its property values being defined.

PROPERTIES

<src>

minedTransactionResponse

.

blockHash

⇒

string

The block hash this transaction occurred in.

<src>

minedTransactionResponse

.

blockNumber

⇒

number

The block number this transaction occurred in.

<src>

minedTransactionResponse

.

date

⇒

Date

The date this transaction occurred on.

class

NetworkPlugin

A NetworkPlugin provides additional functionality on a Network.

PROPERTIES

<src>

networkPlugin

.

name

⇒

string

read-only

The name of the plugin.

It is recommended to use reverse-domain-notation, which permits unique names with a known authority as well as hierarchal entries.

CREATING INSTANCES

<src>

new

NetworkPlugin

(

name

:

string

)

Creates a new NetworkPlugin.

METHODS

<src>

networkPlugin

.

clone

(

)

⇒

NetworkPlugin

Creates a copy of this plugin.

<src>

networkPlugin

.

inspect

(

)

⇒

string

<src>

networkPlugin

.

toString

(

)

⇒

string

class

NonceManager

inherits from

AbstractSigner

,

Signer

A NonceManager wraps another Signer and automatically manages the nonce, ensuring serialized and sequential nonces are used during transaction.

PROPERTIES

<src>

nonceManager

.

signer

⇒

Signer

The Signer being managed.

CREATING INSTANCES

<src>

new

NonceManager

(

signer

:

Signer

)

Creates a new NonceManager to manage signer.

METHODS

<src>

nonceManager

.

increment

(

)

⇒

void

Manually increment the nonce. This may be useful when managng offline transactions.

<src>

nonceManager

.

reset

(

)

⇒

void

Resets the nonce, causing the NonceManager to reload the current nonce from the blockchain on the next transaction.

interface

PreparedTransactionRequest

A PreparedTransactionRequest is identical to a TransactionRequest except all the property types are strictly enforced.

PROPERTIES

<src>

preparedTransactionRequest

.

accessList

⇒

AccessList

The EIP-2930 access list. Storage slots included in the access list are warmed by pre-loading them, so their initial cost to fetch is guaranteed, but then each additional access is cheaper.

<src>

preparedTransactionRequest

.

authorizationList

⇒

Array<

Authorization

>

The EIP-7702 authorizations (if any).

<src>

preparedTransactionRequest

.

blockTag

⇒

BlockTag

When using call or estimateGas, this allows a specific block to be queried. Many backends do not support this and when unsupported errors are silently squelched and "latest" is used.

<src>

preparedTransactionRequest

.

chainId

⇒

bigint

The chain ID for the network this transaction is valid on.

<src>

preparedTransactionRequest

.

customData

⇒

any

A custom object, which can be passed along for network-specific values.

<src>

preparedTransactionRequest

.

data

⇒

string

The transaction data.

<src>

preparedTransactionRequest

.

enableCcipRead

⇒

boolean

When using call, this enables CCIP-read, which permits the provider to be redirected to web-based content during execution, which is then further validated by the contract.

There are potential security implications allowing CCIP-read, as it could be used to expose the IP address or user activity during the fetch to unexpected parties.

<src>

preparedTransactionRequest

.

from

⇒

AddressLike

The sender of the transaction.

<src>

preparedTransactionRequest

.

gasLimit

⇒

bigint

The maximum amount of gas to allow this transaction to consume.

<src>

preparedTransactionRequest

.

gasPrice

⇒

bigint

The gas price to use for legacy transactions or transactions on legacy networks.

Most of the time the max*FeePerGas is preferred.

<src>

preparedTransactionRequest

.

maxFeePerGas

⇒

bigint

The EIP-1559 maximum total fee to pay per gas. The actual value used is protocol enforced to be the block's base fee.

<src>

preparedTransactionRequest

.

maxPriorityFeePerGas

⇒

bigint

The EIP-1559 maximum priority fee to pay per gas.

<src>

preparedTransactionRequest

.

nonce

⇒

number

The nonce of the transaction, used to prevent replay attacks.

<src>

preparedTransactionRequest

.

to

⇒

AddressLike

The target of the transaction.

<src>

preparedTransactionRequest

.

type

⇒

number

The transaction type.

<src>

preparedTransactionRequest

.

value

⇒

bigint

The transaction value (in wei).

interface

Provider

inherits from

ContractRunner

,

EventEmitterable

,

NameResolver

A Provider is the primary method to interact with the read-only content on Ethereum.

It allows access to details about accounts, blocks and transactions and the ability to query event logs and simulate contract execution.

Account data includes the balance, transaction count, code and state trie storage.

Simulating execution can be used to call, estimate gas and get transaction results.

The broadcastTransaction is the only method which allows updating the blockchain, but it is usually accessed by a Signer, since a private key must be used to sign the transaction before it can be broadcast.

PROPERTIES

<src>

provider

.

provider

⇒

this

The provider iteself.

This is part of the necessary API for executing a contract, as it provides a common property on any ContractRunner that can be used to access the read-only portion of the runner.

METHODS

<src>

provider

.

broadcastTransaction

(

signedTx

:

string

)

⇒

Promise<

TransactionResponse

>

Broadcasts the signedTx to the network, adding it to the memory pool of any node for which the transaction meets the rebroadcast requirements.

<src>

provider

.

call

(

tx

:

TransactionRequest

)

⇒

Promise<

string

>

Simulate the execution of tx. If the call reverts, it will throw a CallExceptionError which includes the revert data.

<src>

provider

.

destroy

(

)

⇒

void

Shutdown any resources this provider is using. No additional calls should be made to this provider after calling this.

<src>

provider

.

estimateGas

(

tx

:

TransactionRequest

)

⇒

Promise<

bigint

>

Estimates the amount of gas required to execute tx.

<src>

provider

.

getBalance

(

address

:

AddressLike

,

blockTag

?:

BlockTag

)

⇒

Promise<

bigint

>

Get the account balance (in wei) of address. If blockTag is specified and the node supports archive access for that blockTag, the balance is as of that BlockTag.

<src>

provider

.

getBlock

(

blockHashOrBlockTag

:

BlockTag

|

string

,

prefetchTxs

?:

boolean

)

⇒

Promise<

null

|

Block

>

Resolves to the block for blockHashOrBlockTag.

If prefetchTxs, and the backend supports including transactions with block requests, all transactions will be included and the Block object will not need to make remote calls for getting transactions.

<src>

provider

.

getBlockNumber

(

)

⇒

Promise<

number

>

Get the current block number.

<src>

provider

.

getCode

(

address

:

AddressLike

,

blockTag

?:

BlockTag

)

⇒

Promise<

string

>

Get the bytecode for address.

<src>

provider

.

getFeeData

(

)

⇒

Promise<

FeeData

>

Get the best guess at the recommended FeeData.

<src>

provider

.

getLogs

(

filter

:

Filter

|

FilterByBlockHash

)

⇒

Promise<

Array<

Log

>

>

Resolves to the list of Logs that match filter

<src>

provider

.

getNetwork

(

)

⇒

Promise<

Network

>

Get the connected Network.

<src>

provider

.

getStorage

(

address

:

AddressLike

,

position

:

BigNumberish

,

blockTag

?:

BlockTag

)

⇒

Promise<

string

>

Get the storage slot value for address at slot position.

<src>

provider

.

getTransaction

(

hash

:

string

)

⇒

Promise<

null

|

TransactionResponse

>

Resolves to the transaction for hash.

If the transaction is unknown or on pruning nodes which discard old transactions this resolves to null.

<src>

provider

.

getTransactionCount

(

address

:

AddressLike

,

blockTag

?:

BlockTag

)

⇒

Promise<

number

>

Get the number of transactions ever sent for address, which is used as the nonce when sending a transaction. If blockTag is specified and the node supports archive access for that blockTag, the transaction count is as of that BlockTag.

<src>

provider

.

getTransactionReceipt

(

hash

:

string

)

⇒

Promise<

null

|

TransactionReceipt

>

Resolves to the transaction receipt for hash, if mined.

If the transaction has not been mined, is unknown or on pruning nodes which discard old transactions this resolves to null.

<src>

provider

.

getTransactionResult

(

hash

:

string

)

⇒

Promise<

null

|

string

>

Resolves to the result returned by the executions of hash.

This is only supported on nodes with archive access and with the necessary debug APIs enabled.

<src>

provider

.

lookupAddress

(

address

:

string

,

coinType

?:

BigNumberish

)

⇒

Promise<

null

|

string

>

Resolves to the ENS name associated for the address or null if the primary name is not configured.

Users must perform additional steps to configure a primary name, which is not currently common.

<src>

provider

.

resolveName

(

ensName

:

string

,

coinType

?:

BigNumberish

)

⇒

Promise<

null

|

string

>

Resolves to the address configured for the ensName or null if unconfigured.

<src>

provider

.

waitForBlock

(

blockTag

?:

BlockTag

)

⇒

Promise<

Block

>

Resolves to the block at blockTag once it has been mined.

This can be useful for waiting some number of blocks by using the currentBlockNumber + N.

<src>

provider

.

waitForTransaction

(

hash

:

string

,

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

Waits until the transaction hash is mined and has confirms confirmations.

interface

Signer

inherits from

Addressable

,

ContractRunner

,

NameResolver

A Signer represents an account on the Ethereum Blockchain, and is most often backed by a private key represented by a mnemonic or residing on a Hardware Wallet.

The API remains abstract though, so that it can deal with more advanced exotic Signing entities, such as Smart Contract Wallets or Virtual Wallets (where the private key may not be known).

PROPERTIES

<src>

signer

.

provider

⇒

null

|

Provider

The Provider attached to this Signer (if any).

METHODS

<src>

signer

.

authorize

(

authorization

:

AuthorizationRequest

)

⇒

Promise<

Authorization

>

Signs an authorization to be used in EIP-7702 transactions.

<src>

signer

.

call

(

tx

:

TransactionRequest

)

⇒

Promise<

string

>

Evaluates the tx by running it against the current Blockchain state. This cannot change state and has no cost in ether, as it is effectively simulating execution.

This can be used to have the Blockchain perform computations based on its state (e.g. running a Contract's getters) or to simulate the effect of a transaction before actually performing an operation.

<src>

signer

.

connect

(

provider

:

null

|

Provider

)

⇒

Signer

Returns a new instance of this Signer connected to provider or detached from any Provider if null.

<src>

signer

.

estimateGas

(

tx

:

TransactionRequest

)

⇒

Promise<

bigint

>

Estimates the required gas required to execute tx on the Blockchain. This will be the expected amount a transaction will require as its gasLimit to successfully run all the necessary computations and store the needed state that the transaction intends.

Keep in mind that this is best efforts, since the state of the Blockchain is in flux, which could affect transaction gas requirements.

<src>

signer

.

getAddress

(

)

⇒

Promise<

string

>

Get the address of the Signer.

<src>

signer

.

getNonce

(

blockTag

?:

BlockTag

)

⇒

Promise<

number

>

Gets the next nonce required for this Signer to send a transaction.

<src>

signer

.

populateAuthorization

(

auth

:

AuthorizationRequest

)

⇒

Promise<

AuthorizationRequest

>

Prepares an AuthorizationRequest for authorization by populating any missing properties:

resolves address (if an Addressable or ENS name) populates nonce via signer.getNonce("pending") populates chainId via signer.provider.getNetwork()

<src>

signer

.

populateCall

(

tx

:

TransactionRequest

)

⇒

Promise<

TransactionLike

<

string

>

>

Prepares a {@link TransactionRequest} for calling:

resolves to and from addresses if from is specified , check that it matches this Signer

<src>

signer

.

populateTransaction

(

tx

:

TransactionRequest

)

⇒

Promise<

TransactionLike

<

string

>

>

Prepares a {@link TransactionRequest} for sending to the network by populating any missing properties:

resolves to and from addresses if from is specified , check that it matches this Signer populates nonce via signer.getNonce("pending") populates gasLimit via signer.estimateGas(tx) populates chainId via signer.provider.getNetwork() populates type and relevant fee data for that type (gasPrice for legacy transactions, maxFeePerGas for EIP-1559, etc)

<src>

signer

.

resolveName

(

name

:

string

)

⇒

Promise<

null

|

string

>

Resolves an ENS Name to an address.

<src>

signer

.

sendTransaction

(

tx

:

TransactionRequest

)

⇒

Promise<

TransactionResponse

>

Sends tx to the Network. The signer.populateTransaction(tx) is called first to ensure all necessary properties for the transaction to be valid have been popualted first.

<src>

signer

.

signMessage

(

message

:

string

|

Uint8Array

)

⇒

Promise<

string

>

Signs an EIP-191 prefixed personal message.

If the message is a string, it is signed as UTF-8 encoded bytes. It is not interpretted as a BytesLike; so the string "0x1234" is signed as six characters, not two bytes.

To sign that example as two bytes, the Uint8Array should be used (i.e. new Uint8Array([ 0x12, 0x34 ])).

<src>

signer

.

signTransaction

(

tx

:

TransactionRequest

)

⇒

Promise<

string

>

Signs tx, returning the fully signed transaction. This does not populate any additional properties within the transaction.

<src>

signer

.

signTypedData

(

domain

:

TypedDataDomain

,

types

:

Record<

string

,

Array<

TypedDataField

>

>

,

value

:

Record<

string

,

any

>

)

⇒

Promise<

string

>

Signs the EIP-712 typed data.

class

TransactionReceipt

inherits from

TransactionReceiptParams

A TransactionReceipt includes additional information about a transaction that is only available after it has been mined.

PROPERTIES

<src>

transactionReceipt

.

blobGasPrice

⇒

null

|

bigint

read-only

The price paid per BLOB in gas. See EIP-4844.

<src>

transactionReceipt

.

blobGasUsed

⇒

null

|

bigint

read-only

The gas used for BLObs. See EIP-4844.

<src>

transactionReceipt

.

blockHash

⇒

string

read-only

The block hash of the Block this transaction was included in.

<src>

transactionReceipt

.

blockNumber

⇒

number

read-only

The block number of the Block this transaction was included in.

<src>

transactionReceipt

.

contractAddress

⇒

null

|

string

read-only

The address of the contract if the transaction was directly responsible for deploying one.

This is non-null only if the to is empty and the data was successfully executed as initcode.

<src>

transactionReceipt

.

cumulativeGasUsed

⇒

bigint

read-only

The amount of gas used by all transactions within the block for this and all transactions with a lower index.

This is generally not useful for developers but can be used to validate certain aspects of execution.

<src>

transactionReceipt

.

fee

⇒

bigint

read-only

The total fee for this transaction, in wei.

<src>

transactionReceipt

.

from

⇒

string

read-only

The sender of the transaction.

<src>

transactionReceipt

.

gasPrice

⇒

bigint

read-only

The actual gas price used during execution.

Due to the complexity of EIP-1559 this value can only be caluclated after the transaction has been mined, snce the base fee is protocol-enforced.

<src>

transactionReceipt

.

gasUsed

⇒

bigint

read-only

The actual amount of gas used by this transaction.

When creating a transaction, the amount of gas that will be used can only be approximated, but the sender must pay the gas fee for the entire gas limit. After the transaction, the difference is refunded.

<src>

transactionReceipt

.

hash

⇒

string

read-only

The transaction hash.

<src>

transactionReceipt

.

index

⇒

number

read-only

The index of this transaction within the block transactions.

<src>

transactionReceipt

.

logs

⇒

ReadonlyArray<

Log

>

read-only

The logs for this transaction.

<src>

transactionReceipt

.

logsBloom

⇒

string

read-only

The bloom filter bytes that represent all logs that occurred within this transaction. This is generally not useful for most developers, but can be used to validate the included logs.

<src>

transactionReceipt

.

provider

⇒

Provider

read-only

The provider connected to the log used to fetch additional details if necessary.

<src>

transactionReceipt

.

root

⇒

null

|

string

read-only

The root hash of this transaction.

This is no present and was only included in pre-byzantium blocks, but could be used to validate certain parts of the receipt.

<src>

transactionReceipt

.

status

⇒

null

|

number

read-only

The status of this transaction, indicating success (i.e. 1) or a revert (i.e. 0).

This is available in post-byzantium blocks, but some backends may backfill this value.

<src>

transactionReceipt

.

to

⇒

null

|

string

read-only

The address the transaction was sent to.

<src>

transactionReceipt

.

type

⇒

number

read-only

The EIP-2718 transaction type.

METHODS

<src>

transactionReceipt

.

confirmations

(

)

⇒

Promise<

number

>

Resolves to the number of confirmations this transaction has.

<src>

transactionReceipt

.

getBlock

(

)

⇒

Promise<

Block

>

Resolves to the block this transaction occurred in.

<src>

transactionReceipt

.

getResult

(

)

⇒

Promise<

string

>

Resolves to the return value of the execution of this transaction.

Support for this feature is limited, as it requires an archive node with the debug_ or trace_ API enabled.

<src>

transactionReceipt

.

getTransaction

(

)

⇒

Promise<

TransactionResponse

>

Resolves to the transaction this transaction occurred in.

<src>

transactionReceipt

.

toJSON

(

)

⇒

any

Returns a JSON-compatible representation.

interface

TransactionRequest

A TransactionRequest is a transactions with potentially various properties not defined, or with less strict types for its values.

This is used to pass to various operations, which will internally coerce any types and populate any necessary values.

PROPERTIES

<src>

transactionRequest

.

accessList

⇒

null

|

AccessListish

The EIP-2930 access list. Storage slots included in the access list are warmed by pre-loading them, so their initial cost to fetch is guaranteed, but then each additional access is cheaper.

<src>

transactionRequest

.

authorizationList

⇒

null

|

Array<

AuthorizationLike

>

The EIP-7702 authorizations (if any).

<src>

transactionRequest

.

blobs

⇒

null

|

Array<

BlobLike

>

Any blobs to include in the transaction (see EIP-4844).

<src>

transactionRequest

.

blobVersionedHashes

⇒

null

|

Array<

string

>

The blob versioned hashes (see EIP-4844).

<src>

transactionRequest

.

blobWrapperVersion

⇒

null

|

number

The EIP-7594 BLOb Wrapper Version used for PeerDAS.

For networks that use EIP-7594, this property is required to serialize the sidecar correctly.

<src>

transactionRequest

.

blockTag

⇒

BlockTag

When using call or estimateGas, this allows a specific block to be queried. Many backends do not support this and when unsupported errors are silently squelched and "latest" is used.

<src>

transactionRequest

.

chainId

⇒

null

|

BigNumberish

The chain ID for the network this transaction is valid on.

<src>

transactionRequest

.

customData

⇒

any

A custom object, which can be passed along for network-specific values.

<src>

transactionRequest

.

data

⇒

null

|

string

The transaction data.

<src>

transactionRequest

.

enableCcipRead

⇒

boolean

When using call, this enables CCIP-read, which permits the provider to be redirected to web-based content during execution, which is then further validated by the contract.

There are potential security implications allowing CCIP-read, as it could be used to expose the IP address or user activity during the fetch to unexpected parties.

<src>

transactionRequest

.

from

⇒

null

|

AddressLike

The sender of the transaction.

<src>

transactionRequest

.

gasLimit

⇒

null

|

BigNumberish

The maximum amount of gas to allow this transaction to consume.

<src>

transactionRequest

.

gasPrice

⇒

null

|

BigNumberish

The gas price to use for legacy transactions or transactions on legacy networks.

Most of the time the max*FeePerGas is preferred.

<src>

transactionRequest

.

kzg

⇒

null

|

KzgLibraryLike

An external library for computing the KZG commitments and proofs necessary for EIP-4844 transactions (see EIP-4844).

This is generally null, unless you are creating BLOb transactions.

<src>

transactionRequest

.

maxFeePerBlobGas

⇒

null

|

BigNumberish

The maximum fee per blob gas (see EIP-4844).

<src>

transactionRequest

.

maxFeePerGas

⇒

null

|

BigNumberish

The EIP-1559 maximum total fee to pay per gas. The actual value used is protocol enforced to be the block's base fee.

<src>

transactionRequest

.

maxPriorityFeePerGas

⇒

null

|

BigNumberish

The EIP-1559 maximum priority fee to pay per gas.

<src>

transactionRequest

.

nonce

⇒

null

|

number

The nonce of the transaction, used to prevent replay attacks.

<src>

transactionRequest

.

to

⇒

null

|

AddressLike

The target of the transaction.

<src>

transactionRequest

.

type

⇒

null

|

number

The transaction type.

<src>

transactionRequest

.

value

⇒

null

|

BigNumberish

The transaction value (in wei).

class

TransactionResponse

inherits from

TransactionResponseParams

A TransactionResponse includes all properties about a transaction that was sent to the network, which may or may not be included in a block.

The transactionResponse.isMined can be used to check if the transaction has been mined as well as type guard that the otherwise possibly null properties are defined.

PROPERTIES

<src>

transactionResponse

.

accessList

⇒

null

|

AccessList

read-only

The EIP-2930 access list for transaction types that support it, otherwise null.

<src>

transactionResponse

.

authorizationList

⇒

null

|

Array<

Authorization

>

read-only

The EIP-7702 authorizations (if any).

<src>

transactionResponse

.

blobVersionedHashes

⇒

null

|

Array<

string

>

read-only

The EIP-4844 BLOb versioned hashes.

<src>

transactionResponse

.

blockHash

⇒

null

|

string

read-only

The blockHash of the block that this transaction was included in.

This is null for pending transactions.

<src>

transactionResponse

.

blockNumber

⇒

null

|

number

read-only

The block number of the block that this transaction was included in.

This is null for pending transactions.

<src>

transactionResponse

.

chainId

⇒

bigint

read-only

The chain ID.

<src>

transactionResponse

.

data

⇒

string

read-only

The data.

<src>

transactionResponse

.

from

⇒

string

read-only

The sender of this transaction. It is implicitly computed from the transaction pre-image hash (as the digest) and the signature using ecrecover.

<src>

transactionResponse

.

gasLimit

⇒

bigint

read-only

The maximum units of gas this transaction can consume. If execution exceeds this, the entries transaction is reverted and the sender is charged for the full amount, despite not state changes being made.

<src>

transactionResponse

.

gasPrice

⇒

bigint

read-only

The gas price can have various values, depending on the network.
