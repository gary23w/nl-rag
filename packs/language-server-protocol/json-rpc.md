---
title: "JSON-RPC"
source: https://en.wikipedia.org/wiki/JSON-RPC
domain: language-server-protocol
license: CC-BY-SA-4.0
tags: language server protocol, lsp editor tooling, code intelligence protocol, json-rpc editor
fetched: 2026-07-02
---

# JSON-RPC

**JSON-RPC** (**JavaScript Object Notation-Remote Procedure Call**) is a JSON-based wire protocol for remote procedure calls (RPC). It is similar to the XML-RPC protocol, defining only a few data types and commands. JSON-RPC allows for notifications (data sent to the server that does not require a response) and for multiple calls to be sent to the server which may be answered asynchronously.

The JSON-RPC protocol is transport-independent and can be carried over many different data transport protocols, including file descriptor I/O, HTTP and TCP. It does not directly provide any support for authentication or authorization.

## History

| Version | Description | Dated |
|---|---|---|
| 1.0 | Original version | 2005 |
| 1.1 WD | Working draft. Adds named parameters, adds specific error codes, and adds introspection functions. | 2006-08-07 |
| 1.1 Alt | Suggestion for a simple JSON-RPC 1.1. Alternative proposal to 1.1 WD. | 2007-05-06 |
| 1.1 Object Specification | Object Specification. Alternative proposal to 1.1 WD/1.1ALT. | 2007-07-30 |
| 1.2 | Proposal. A later revision of this document was renamed to 2.0. | 2007-12-27 |
| 2.0 | Specification proposal | 2009-05-24 |
| 2.0 (Revised-) | Specification | 2010-03-26 |

## Usage

JSON-RPC works by sending a request to a server implementing this protocol. The client in that case is typically software intending to call a single method of a remote system. Multiple input parameters can be passed to the remote method as an array or object, whereas the method itself can return multiple output data as well. (This depends on the implemented version.)

All transfer types are single objects, serialized using JSON.

### Request

A request is a call to a specific method provided by a remote system. It can contain three members:

- `method` - A string with the name of the method to be invoked. Method names that begin with "rpc." are reserved for rpc-internal methods.
- `params` - An object or array of values to be passed as parameters to the defined method. This member may be omitted.
- `id` - A string or non-fractional number used to match the response with the request that it is replying to. This member may be omitted if no response should be returned.

### Response

The receiver of the request must reply with a valid response to all received requests. A response can contain the members mentioned below.

- `result` - The data returned by the invoked method. If an error occurred while invoking the method, this member must not exist.
- `error` - An error object if there was an error invoking the method, otherwise this member must not exist. The object must contain members *code* (integer) and *message* (string). An optional *data* member can contain further server-specific data. There are pre-defined error codes which follow those defined for XML-RPC.
- `id` - The id of the request it is responding to.

| Error Code | Message | Description |
|---|---|---|
| −32700 | Parse error | Invalid JSON was received |
| −32600 | Invalid Request | The JSON sent is not a valid Request object |
| −32601 | Method not found | The method does not exist / is not available |
| −32602 | Invalid params | Invalid method parameter(s) |
| −32603 | Internal error | Internal JSON-RPC error |
| −32000 to −32099 | Server error | Reserved for implementation-defined server errors |

Since there are situations where no response is needed or even desired, notifications were introduced. A notification is similar to a request except for the id, which is not needed because no response will be returned. In this case the `id` property should be omitted (Version 2.0) or be `null` (Version 1.0).

## Examples

In these examples, `-->` denotes data sent to a service (*request*), while `<--` denotes data coming from a service. Although `<--` is often called a *response* in client–server computing, depending on the JSON-RPC version it does not necessarily imply an *answer* to a request*.*

### Version 2.0

Request and response:

```mw
--> {"jsonrpc": "2.0", "method": "subtract", "params": {"minuend": 42, "subtrahend": 23}, "id": 3}
<-- {"jsonrpc": "2.0", "result": 19, "id": 3}
```

Notification (no response, and no id):

```mw
--> {"jsonrpc": "2.0", "method": "update", "params": [1,2,3,4,5]}
```

Parse error:

```mw
--> {"jsonrpc": "2.0", "method": "subtract", "params":
<-- {"jsonrpc": "2.0", "error": {"code": -32700, "message": "Parse error"}, "id": null}
```

Invalid Request:

```mw
--> {"jsonrpc": "2.0", "method": 1, "params": "bar"}
<-- {"jsonrpc": "2.0", "error": {"code": -32600, "message": "Invalid Request"}, "id": null}
```

Method not found:

```mw
--> {"jsonrpc": "2.0", "method": "foobar", "id": 1}
<-- {"jsonrpc": "2.0", "error": {"code": -32601, "message": "Method not found"}, "id": 1}
```

Invalid params:

```mw
--> {"jsonrpc": "2.0", "method": "subtract", "params": {"minuend": 42}, "id": 2}
<-- {"jsonrpc": "2.0", "error": {"code": -32602, "message": "Invalid params", "data": "Missing required parameter: subtrahend"}, "id": 2}
```

Internal error:

```mw
--> {"jsonrpc": "2.0", "method": "getData", "params": [], "id": 4}
<-- {"jsonrpc": "2.0", "error": {"code": -32603, "message": "Internal error"}, "id": 4}
```

Batch request with errors:

```mw
--> [
      {"jsonrpc": "2.0", "method": "subtract", "params": [42, 23], "id": 1},
      {"jsonrpc": "2.0", "method": "foobar", "id": 2},
      {"foo": "bar"}
    ]
<-- [
      {"jsonrpc": "2.0", "result": 19, "id": 1},
      {"jsonrpc": "2.0", "error": {"code": -32601, "message": "Method not found"}, "id": 2},
      {"jsonrpc": "2.0", "error": {"code": -32600, "message": "Invalid Request"}, "id": null}
    ]
```

### Version 1.1 (Working Draft)

Request and response:

```mw
--> {"version": "1.1", "method": "confirmFruitPurchase", "params": [["apple", "orange", "mangoes"], 1.123], "id": "194521489"}
<-- {"version": "1.1", "result": "done", "error": null, "id": "194521489"}
```

### Version 1.0

Request and response:

```mw
--> {"method": "echo", "params": ["Hello JSON-RPC"], "id": 1}
<-- {"result": "Hello JSON-RPC", "error": null, "id": 1}
```
