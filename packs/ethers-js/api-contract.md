---
title: "Untitled"
source: https://docs.ethers.org/v6/api/contract/
domain: ethers-js
license: MIT (ethers.js docs)
tags: ethers.js, ethers, ethereum provider, contract abstraction
fetched: 2026-07-02
---

# Untitled

Contracts

A Contract object is a meta-class (a class whose definition is defined at runtime), which communicates with a deployed smart contract on the blockchain and provides a simple JavaScript interface to call methods, send transaction, query historic logs and listen for its events.

TYPES

<src>

ContractEventName

⇒

string

|

ContractEvent

|

TopicFilter

|

DeferredTopicFilter

The name for an event used for subscribing to Contract events.

string - An event by name. The event must be non-ambiguous. The parameters will be dereferenced when passed into the listener.

ContractEvent - A filter from the contract.filters, which will pass only the EventPayload as a single parameter, which includes a .signature property that can be used to further filter the event.

TopicFilter - A filter defined using the standard Ethereum API which provides the specific topic hash or topic hashes to watch for along with any additional values to filter by. This will only pass a single parameter to the listener, the EventPayload which will include additional details to refine by, such as the event name and signature.

DeferredTopicFilter - A filter created by calling a ContractEvent with parameters, which will create a filter for a specific event signature and dereference each parameter when calling the listener.

class

BaseContract

inherits from

Addressable

PROPERTIES

<src>

baseContract

.

fallback

⇒

null

|

WrappedFallback

read-only

The fallback or receive function if any.

<src>

baseContract

.

filters

⇒

Record<

string

,

ContractEvent

>

read-only

All the Events available on this contract.

<src>

baseContract

.

interface

⇒

Interface

read-only

The contract Interface.

<src>

baseContract

.

runner

⇒

null

|

ContractRunner

read-only

The connected runner. This is generally a Provider or a Signer, which dictates what operations are supported.

For example, a Contract connected to a Provider may only execute read-only operations.

<src>

baseContract

.

target

⇒

string

|

Addressable

read-only

The target to connect to.

This can be an address, ENS name or any Addressable, such as another contract. To get the resolved address, use the getAddress method.

CREATING INSTANCES

<src>

new

BaseContract

(

target

:

string

|

Addressable

,

abi

:

Interface

|

InterfaceAbi

,

runner

?:

null

|

ContractRunner

,

deployTx

?:

null

|

TransactionResponse

)

Creates a new contract connected to target with the abi and optionally connected to a runner to perform operations on behalf of.

METHODS

<src>

baseContract

.

addListener

(

event

:

ContractEventName

,

listener

:

Listener

)

⇒

Promise<

this

>

Alias for [on].

<src>

baseContract

.

attach

(

target

:

string

|

Addressable

)

⇒

BaseContract

Return a new Contract instance with the same ABI and runner, but a different target.

<src>

baseContract

.

connect

(

runner

:

null

|

ContractRunner

)

⇒

BaseContract

Return a new Contract instance with the same target and ABI, but a different runner.

<src>

baseContract

.

deploymentTransaction

(

)

⇒

null

|

ContractTransactionResponse

Return the transaction used to deploy this contract.

This is only available if this instance was returned from a ContractFactory.

<src>

baseContract

.

emit

(

event

:

ContractEventName

,

args

:

Array<

any

>

)

⇒

Promise<

boolean

>

Emit an event calling all listeners with args.

Resolves to true if any listeners were called.

<src>

baseContract

.

getAddress

(

)

⇒

Promise<

string

>

Return the resolved address of this Contract.

<src>

baseContract

.

getDeployedCode

(

)

⇒

Promise<

null

|

string

>

Return the deployed bytecode or null if no bytecode is found.

<src>

baseContract

.

getEvent

(

key

:

string

|

EventFragment

)

⇒

ContractEvent

Return the event for a given name. This is useful when a contract event name conflicts with a JavaScript name such as prototype or when using a Contract programmatically.

<src>

baseContract

.

getFunction

(

key

:

string

|

FunctionFragment

)

⇒

T

Return the function for a given name. This is useful when a contract method name conflicts with a JavaScript name such as prototype or when using a Contract programmatically.

<src>

baseContract

.

listenerCount

(

event

?:

ContractEventName

)

⇒

Promise<

number

>

Resolves to the number of listeners of event or the total number of listeners if unspecified.

<src>

baseContract

.

listeners

(

event

?:

ContractEventName

)

⇒

Promise<

Array<

Listener

>

>

Resolves to the listeners subscribed to event or all listeners if unspecified.

<src>

baseContract

.

off

(

event

:

ContractEventName

,

listener

?:

Listener

)

⇒

Promise<

this

>

Remove the listener from the listeners for event or remove all listeners if unspecified.

<src>

baseContract

.

on

(

event

:

ContractEventName

,

listener

:

Listener

)

⇒

Promise<

this

>

Add an event listener for the event.

<src>

baseContract

.

once

(

event

:

ContractEventName

,

listener

:

Listener

)

⇒

Promise<

this

>

Add an event listener for the event, but remove the listener after it is fired once.

<src>

baseContract

.

queryFilter

(

event

:

ContractEventName

,

fromBlock

?:

BlockTag

,

toBlock

?:

BlockTag

)

⇒

Promise<

Array<

EventLog

|

Log

>

>

Provide historic access to event data for event in the range fromBlock (default: 0) to toBlock (default: "latest") inclusive.

<src>

baseContract

.

removeAllListeners

(

event

?:

ContractEventName

)

⇒

Promise<

this

>

Remove all the listeners for event or remove all listeners if unspecified.

<src>

baseContract

.

removeListener

(

event

:

ContractEventName

,

listener

:

Listener

)

⇒

Promise<

this

>

Alias for [off].

<src>

baseContract

.

waitForDeployment

(

)

⇒

Promise<

this

>

Resolve to this Contract once the bytecode has been deployed, or resolve immediately if already deployed.

STATIC METHODS

<src>

BaseContract

.

buildClass

(

abi

:

Interface

|

InterfaceAbi

)

⇒

TODO(A2Bconstructor(@TODO-001))

Create a new Class for the abi.

<src>

BaseContract

.

from

(

target

:

string

,

abi

:

Interface

|

InterfaceAbi

,

runner

?:

null

|

ContractRunner

)

⇒

BaseContract

&

Omit<

T

,

keyof<

BaseContract

>

>

Create a new BaseContract with a specified Interface.

interface

BaseContractMethod

A Contract method can be called directly, or used in various ways.

PROPERTIES

<src>

baseContractMethod

.

fragment

⇒

FunctionFragment

The fragment of the Contract method. This will throw on ambiguous method names.

<src>

baseContractMethod

.

name

⇒

string

The name of the Contract method.

METHODS

<src>

baseContractMethod

.

estimateGas

(

args

:

ContractMethodArgs<

A

>

)

⇒

Promise<

bigint

>

Estimate the gas to send the contract method with args.

<src>

baseContractMethod

.

getFragment

(

args

:

ContractMethodArgs<

A

>

)

⇒

FunctionFragment

Returns the fragment constrained by args. This can be used to resolve ambiguous method names.

<src>

baseContractMethod

.

populateTransaction

(

args

:

ContractMethodArgs<

A

>

)

⇒

Promise<

ContractTransaction

>

Returns a populated transaction that can be used to perform the contract method with args.

<src>

baseContractMethod

.

send

(

args

:

ContractMethodArgs<

A

>

)

⇒

Promise<

ContractTransactionResponse

>

Send a transaction for the contract method with args.

<src>

baseContractMethod

.

staticCall

(

args

:

ContractMethodArgs<

A

>

)

⇒

Promise<

R

>

Call the contract method with args and return the value.

If the return value is a single type, it will be dereferenced and returned directly, otherwise the full Result will be returned.

<src>

baseContractMethod

.

staticCallResult

(

args

:

ContractMethodArgs<

A

>

)

⇒

Promise<

Result

>

Call the contract method with args and return the Result without any dereferencing.

interface

ConstantContractMethod

inherits from

ContractMethod

,

BaseContractMethod

A pure of view method on a Contract.

class

Contract

A BaseContract with no type guards on its methods or events.

interface

ContractDeployTransaction

A deployment transaction for a contract.

interface

ContractEvent

PROPERTIES

<src>

contractEvent

.

fragment

⇒

EventFragment

The fragment of the Contract event. This will throw on ambiguous method names.

<src>

contractEvent

.

name

⇒

string

The name of the Contract event.

METHODS

<src>

contractEvent

.

getFragment

(

args

:

ContractEventArgs<

A

>

)

⇒

EventFragment

Returns the fragment constrained by args. This can be used to resolve ambiguous event names.

class

ContractEventPayload

inherits from

ContractUnknownEventPayload

,

EventPayload

A ContractEventPayload is included as the last parameter to Contract Events when the event is known.

PROPERTIES

<src>

contractEventPayload

.

args

⇒

Result

read-only

The parsed arguments passed to the event by emit.

<src>

contractEventPayload

.

eventName

⇒

string

read-only

The event name.

<src>

contractEventPayload

.

eventSignature

⇒

string

read-only

The event signature.

<src>

contractEventPayload

.

fragment

⇒

EventFragment

read-only

The matching event.

<src>

contractEventPayload

.

log

⇒

EventLog

read-only

The log, with parsed properties.

class

ContractFactory

A ContractFactory is used to deploy a Contract to the blockchain.

PROPERTIES

<src>

contractFactory

.

bytecode

⇒

string

read-only

The Contract deployment bytecode. Often called the initcode.

<src>

contractFactory

.

interface

⇒

Interface

read-only

The Contract Interface.

<src>

contractFactory

.

runner

⇒

null

|

ContractRunner

read-only

The ContractRunner to deploy the Contract as.

CREATING INSTANCES

<src>

new

ContractFactory

(

abi

:

Interface

|

InterfaceAbi

,

bytecode

:

BytesLike

|

{ object:

string

}

,

runner

?:

null

|

ContractRunner

)

Create a new ContractFactory with abi and bytecode, optionally connected to runner.

The bytecode may be the bytecode property within the standard Solidity JSON output.

METHODS

<src>

contractFactory

.

attach

(

target

:

string

|

Addressable

)

⇒

BaseContract

&

Omit<

I

,

keyof<

BaseContract

>

>

<src>

contractFactory

.

connect

(

runner

:

null

|

ContractRunner

)

⇒

ContractFactory

<

A

,

I

>

Return a new ContractFactory with the same ABI and bytecode, but connected to runner.

<src>

contractFactory

.

deploy

(

args

:

ContractMethodArgs<

A

>

)

⇒

Promise<

BaseContract

&

{ deploymentTransaction:

ContractTransactionResponse

}

&

Omit<

I

,

keyof<

BaseContract

>

>

>

Resolves to the Contract deployed by passing args into the constructor.

This will resolve to the Contract before it has been deployed to the network, so the baseContract.waitForDeployment should be used before sending any transactions to it.

<src>

contractFactory

.

getDeployTransaction

(

args

:

ContractMethodArgs<

A

>

)

⇒

Promise<

ContractDeployTransaction

>

Resolves to the transaction to deploy the contract, passing args into the constructor.

STATIC METHODS

<src>

ContractFactory

.

fromSolidity

(

output

:

any

,

runner

?:

ContractRunner

)

⇒

ContractFactory

<

A

,

I

>

Create a new ContractFactory from the standard Solidity JSON output.

interface

ContractInterface

A Contract with no method constraints.

interface

ContractMethod

inherits from

BaseContractMethod

A contract method on a Contract.

interface

ContractTransaction

inherits from

PreparedTransactionRequest

When populating a transaction this type is returned.

PROPERTIES

<src>

contractTransaction

.

data

⇒

string

The transaction data.

<src>

contractTransaction

.

from

⇒

string

The from address, if any.

<src>

contractTransaction

.

to

⇒

string

The target address.

class

ContractTransactionReceipt

inherits from

TransactionReceipt

,

TransactionReceiptParams

A ContractTransactionReceipt includes the parsed logs from a TransactionReceipt.

PROPERTIES

<src>

contractTransactionReceipt

.

logs

⇒

Array<

EventLog

|

Log

>

read-only

The parsed logs for any Log which has a matching event in the Contract ABI.

class

ContractTransactionResponse

inherits from

TransactionResponse

,

TransactionResponseParams

A ContractTransactionResponse will return a ContractTransactionReceipt when waited on.

METHODS

<src>

contractTransactionResponse

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

ContractTransactionReceipt

>

Resolves once this transaction has been mined and has confirms blocks including it (default: 1) with an optional timeout.

This can resolve to null only if confirms is 0 and the transaction has not been mined, otherwise this will wait until enough confirmations have completed.

class

ContractUnknownEventPayload

inherits from

EventPayload

A ContractUnknownEventPayload is included as the last parameter to Contract Events when the event does not match any events in the ABI.

PROPERTIES

<src>

contractUnknownEventPayload

.

log

⇒

Log

read-only

The log with no matching events.

CREATING INSTANCES

<src>

new

ContractUnknownEventPayload

(

contract

:

BaseContract

,

listener

:

null

|

Listener

,

filter

:

ContractEventName

,

log

:

Log

)

METHODS

<src>

contractUnknownEventPayload

.

getBlock

(

)

⇒

Promise<

Block

>

Resolves to the block the event occured in.

<src>

contractUnknownEventPayload

.

getTransaction

(

)

⇒

Promise<

TransactionResponse

>

Resolves to the transaction the event occured in.

<src>

contractUnknownEventPayload

.

getTransactionReceipt

(

)

⇒

Promise<

TransactionReceipt

>

Resolves to the transaction receipt the event occured in.

interface

DeferredTopicFilter

When creating a filter using the contract.filters, this is returned.

PROPERTIES

<src>

deferredTopicFilter

.

fragment

⇒

EventFragment

METHODS

<src>

deferredTopicFilter

.

getTopicFilter

(

)

⇒

Promise<

TopicFilter

>

class

EventLog

inherits from

Log

,

LogParams

An EventLog contains additional properties parsed from the Log.

PROPERTIES

<src>

eventLog

.

args

⇒

Result

read-only

The parsed arguments passed to the event by emit.

<src>

eventLog

.

eventName

⇒

string

read-only

The name of the event.

<src>

eventLog

.

eventSignature

⇒

string

read-only

The signature of the event.

<src>

eventLog

.

fragment

⇒

EventFragment

read-only

The matching event.

<src>

eventLog

.

interface

⇒

Interface

read-only

The Contract Interface.

interface

Overrides

The overrides for a contract transaction.

class

UndecodedEventLog

inherits from

Log

,

LogParams

An EventLog contains additional properties parsed from the Log.

PROPERTIES

<src>

undecodedEventLog

.

error

⇒

Error

read-only

The error encounted when trying to decode the log.

interface

WrappedFallback

A Fallback or Receive function on a Contract.

METHODS

<src>

wrappedFallback

.

estimateGas

(

overrides

?:

Omit<

TransactionRequest

,

"to"

>

)

⇒

Promise<

bigint

>

Estimate the gas to send a transaction to the contract fallback.

For non-receive fallback, data may be overridden.

<src>

wrappedFallback

.

populateTransaction

(

overrides

?:

Omit<

TransactionRequest

,

"to"

>

)

⇒

Promise<

ContractTransaction

>

Returns a populated transaction that can be used to perform the fallback method.

For non-receive fallback, data may be overridden.

<src>

wrappedFallback

.

send

(

overrides

?:

Omit<

TransactionRequest

,

"to"

>

)

⇒

Promise<

ContractTransactionResponse

>

Send a transaction to the contract fallback.

For non-receive fallback, data may be overridden.

<src>

wrappedFallback

.

staticCall

(

overrides

?:

Omit<

TransactionRequest

,

"to"

>

)

⇒

Promise<

string

>

Call the contract fallback and return the result.

For non-receive fallback, data may be overridden.
