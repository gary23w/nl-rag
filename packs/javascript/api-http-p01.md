---
title: "HTTP (part 1/3)"
source: https://nodejs.org/api/http.html
domain: javascript
license: CC-BY-SA-2.5 (MDN) / MIT (Node.js)
tags: javascript, typescript, node.js, nodejs, npm
fetched: 2026-07-02
part: 1/3
---

# HTTP

Node.js

# Node.js v26.4.0 documentation

- Node.js v26.4.0
- Table of contents
- IndexIndex
- Other versions26.x 25.x 24.x **LTS**23.x 22.x **LTS**21.x 20.x 19.x 18.x 17.x 16.x 15.x 14.x 13.x 12.x 11.x 10.x 9.x 8.x 7.x 6.x 5.x 4.x 0.12.x 0.10.x
- Options View on single page View as JSON

## HTTP

Stability: 2 - Stable

This module, containing both a client and server, can be imported via `require('node:http')` (CommonJS) or `import * as http from 'node:http'` (ES module).

The HTTP interfaces in Node.js are designed to support many features of the protocol which have been traditionally difficult to use. In particular, large, possibly chunk-encoded, messages. The interface is careful to never buffer entire requests or responses, so the user is able to stream data.

HTTP message headers are represented by an object like this:`{ "content-length": "123", "content-type": "text/plain", "connection": "keep-alive", "host": "example.com", "accept": "*/*" }`

Keys are lowercased. Values are not modified.

In order to support the full spectrum of possible HTTP applications, the Node.js HTTP API is very low-level. It deals with stream handling and message parsing only. It parses a message into headers and body but it does not parse the actual headers or the body.

See `message.headers` for details on how duplicate headers are handled.

The raw headers as they were received are retained in the `rawHeaders` property, which is an array of `[key, value, key2, value2, ...]`. For example, the previous message header object might have a `rawHeaders` list like the following:`[ "ConTent-Length", "123456", "content-LENGTH", "123", "content-type", "text/plain", "CONNECTION", "keep-alive", "Host", "example.com", "accepT", "*/*" ]`

### Class: `http.Agent`

An `Agent` is responsible for managing connection persistence and reuse for HTTP clients. It maintains a queue of pending requests for a given host and port, reusing a single socket connection for each until the queue is empty, at which time the socket is either destroyed or put into a pool where it is kept to be used again for requests to the same host and port. Whether it is destroyed or pooled depends on the `keepAlive` option.

Pooled connections have TCP Keep-Alive enabled for them, but servers may still close idle connections, in which case they will be removed from the pool and a new connection will be made when a new HTTP request is made for that host and port. Servers may also refuse to allow multiple requests over the same connection, in which case the connection will have to be remade for every request and cannot be pooled. The `Agent` will still make the requests to that server, but each one will occur over a new connection.

When a connection is closed by the client or the server, it is removed from the pool. Any unused sockets in the pool will be unrefed so as not to keep the Node.js process running when there are no outstanding requests. (see `socket.unref()`).

It is good practice, to `destroy()` an `Agent` instance when it is no longer in use, because unused sockets consume OS resources.

Sockets are removed from an agent when the socket emits either a `'close'` event or an `'agentRemove'` event. When intending to keep one HTTP request open for a long time without keeping it in the agent, something like the following may be done:`http.get(options, (res) => { // Do stuff }).on('socket', (socket) => { socket.emit('agentRemove'); });`

An agent may also be used for an individual request. By providing `{agent: false}` as an option to the `http.get()` or `http.request()` functions, a one-time use `Agent` with default options will be used for the client connection.

`agent:false`:`http.get({ hostname: 'localhost', port: 80, path: '/', agent: false, // Create a new agent just for this one request }, (res) => { // Do stuff with response });`

#### `new Agent([options])`

- `options` `<Object>` Set of configurable options to set on the agent. Can have the following fields:
  - `keepAlive` `<boolean>` Keep sockets around even when there are no outstanding requests, so they can be used for future requests without having to reestablish a TCP connection. Not to be confused with the `keep-alive` value of the `Connection` header. The `Connection: keep-alive` header is always sent when using an agent except when the `Connection` header is explicitly specified or when the `keepAlive` and `maxSockets` options are respectively set to `false` and `Infinity`, in which case `Connection: close` will be used. **Default:** `false`.
  - `keepAliveMsecs` `<number>` When using the `keepAlive` option, specifies the initial delay for TCP Keep-Alive packets. Ignored when the `keepAlive` option is `false` or `undefined`. **Default:** `1000`.
  - `agentKeepAliveTimeoutBuffer` `<number>` Milliseconds to subtract from the server-provided `keep-alive: timeout=...` hint when determining socket expiration time. This buffer helps ensure the agent closes the socket slightly before the server does, reducing the chance of sending a request on a socket that’s about to be closed by the server. **Default:** `1000`.
  - `maxSockets` `<number>` Maximum number of sockets to allow per host. If the same host opens multiple concurrent connections, each request will use new socket until the `maxSockets` value is reached. If the host attempts to open more connections than `maxSockets`, the additional requests will enter into a pending request queue, and will enter active connection state when an existing connection terminates. This makes sure there are at most `maxSockets` active connections at any point in time, from a given host. **Default:** `Infinity`.
  - `maxTotalSockets` `<number>` Maximum number of sockets allowed for all hosts in total. Each request will use a new socket until the maximum is reached. **Default:** `Infinity`.
  - `maxFreeSockets` `<number>` Maximum number of sockets per host to leave open in a free state. Only relevant if `keepAlive` is set to `true`. **Default:** `256`.
  - `scheduling` `<string>` Scheduling strategy to apply when picking the next free socket to use. It can be `'fifo'` or `'lifo'`. The main difference between the two scheduling strategies is that `'lifo'` selects the most recently used socket, while `'fifo'` selects the least recently used socket. In case of a low rate of request per second, the `'lifo'` scheduling will lower the risk of picking a socket that might have been closed by the server due to inactivity. In case of a high rate of request per second, the `'fifo'` scheduling will maximize the number of open sockets, while the `'lifo'` scheduling will keep it as low as possible. **Default:** `'lifo'`.
  - `timeout` `<number>` Socket timeout in milliseconds. This will set the timeout when the socket is created.
  - `proxyEnv` `<Object>` | `<undefined>` Environment variables for proxy configuration. See Built-in Proxy Support for details. **Default:** `undefined`
    - `HTTP_PROXY` `<string>` | `<undefined>` URL for the proxy server that HTTP requests should use. If undefined, no proxy is used for HTTP requests.
    - `HTTPS_PROXY` `<string>` | `<undefined>` URL for the proxy server that HTTPS requests should use. If undefined, no proxy is used for HTTPS requests.
    - `NO_PROXY` `<string>` | `<undefined>` Patterns specifying the endpoints that should not be routed through a proxy.
    - `http_proxy` `<string>` | `<undefined>` Same as `HTTP_PROXY`. If both are set, `http_proxy` takes precedence.
    - `https_proxy` `<string>` | `<undefined>` Same as `HTTPS_PROXY`. If both are set, `https_proxy` takes precedence.
    - `no_proxy` `<string>` | `<undefined>` Same as `NO_PROXY`. If both are set, `no_proxy` takes precedence.
  - `defaultPort` `<number>` Default port to use when the port is not specified in requests. **Default:** `80`.
  - `protocol` `<string>` The protocol to use for the agent. **Default:** `'http:'`.

`options` in `socket.connect()` are also supported.

To configure any of them, a custom `http.Agent` instance must be created.`import { Agent, request } from 'node:http'; const keepAliveAgent = new Agent({ keepAlive: true }); options.agent = keepAliveAgent; request(options, onResponseCallback);``const http = require('node:http'); const keepAliveAgent = new http.Agent({ keepAlive: true }); options.agent = keepAliveAgent; http.request(options, onResponseCallback);`

#### `agent.createConnection(options[, callback])`

- `options` `<Object>` Options containing connection details. Check `net.createConnection()` for the format of the options. For custom agents, this object is passed to the custom `createConnection` function.
- `callback` `<Function>` (Optional, primarily for custom agents) A function to be called by a custom `createConnection` implementation when the socket is created, especially for asynchronous operations.
  - `err` `<Error>` | `<null>` An error object if socket creation failed.
  - `socket` `<stream.Duplex>` The created socket.
- Returns: `<stream.Duplex>` The created socket. This is returned by the default implementation or by a custom synchronous `createConnection` implementation. If a custom `createConnection` uses the `callback` for asynchronous operation, this return value might not be the primary way to obtain the socket.

Produces a socket/stream to be used for HTTP requests.

By default, this function behaves identically to `net.createConnection()`, synchronously returning the created socket. The optional `callback` parameter in the signature is **not** used by this default implementation.

However, custom agents may override this method to provide greater flexibility, for example, to create sockets asynchronously. When overriding `createConnection`: **Synchronous socket creation**: The overriding method can return the socket/stream directly. **Asynchronous socket creation**: The overriding method can accept the `callback` and pass the created socket/stream to it (e.g., `callback(null, newSocket)`). If an error occurs during socket creation, it should be passed as the first argument to the `callback` (e.g., `callback(err)`).

The agent will call the provided `createConnection` function with `options` and this internal `callback`. The `callback` provided by the agent has a signature of `(err, stream)`.

#### `agent.keepSocketAlive(socket)`

- `socket` `<stream.Duplex>`

Called when `socket` is detached from a request and could be persisted by the `Agent`. Default behavior is to:`socket.setKeepAlive(true, this.keepAliveMsecs); socket.unref(); return true;`

This method can be overridden by a particular `Agent` subclass. If this method returns a falsy value, the socket will be destroyed instead of persisting it for use with the next request.

The `socket` argument can be an instance of `<net.Socket>`, a subclass of `<stream.Duplex>`.

#### `agent.reuseSocket(socket, request)`

- `socket` `<stream.Duplex>`
- `request` `<http.ClientRequest>`

Called when `socket` is attached to `request` after being persisted because of the keep-alive options. Default behavior is to:`socket.ref();`

This method can be overridden by a particular `Agent` subclass.

The `socket` argument can be an instance of `<net.Socket>`, a subclass of `<stream.Duplex>`.

#### `agent.destroy()`

Destroy any sockets that are currently in use by the agent.

It is usually not necessary to do this. However, if using an agent with `keepAlive` enabled, then it is best to explicitly shut down the agent when it is no longer needed. Otherwise, sockets might stay open for quite a long time before the server terminates them.

#### `agent.freeSockets`

- Type: `<Object>`

An object which contains arrays of sockets currently awaiting use by the agent when `keepAlive` is enabled. Do not modify.

Sockets in the `freeSockets` list will be automatically destroyed and removed from the array on `'timeout'`.

#### `agent.getName([options])`

- `options` `<Object>` A set of options providing information for name generation
  - `host` `<string>` A domain name or IP address of the server to issue the request to
  - `port` `<number>` Port of remote server
  - `localAddress` `<string>` Local interface to bind for network connections when issuing the request
  - `family` `<integer>` Must be 4 or 6 if this doesn't equal `undefined`.
- Returns: `<string>`

Get a unique name for a set of request options, to determine whether a connection can be reused. For an HTTP agent, this returns `host:port:localAddress` or `host:port:localAddress:family`. For an HTTPS agent, the name includes the CA, cert, ciphers, and other HTTPS/TLS-specific options that determine socket reusability.

#### `agent.maxFreeSockets`

- Type: `<number>`

By default set to 256. For agents with `keepAlive` enabled, this sets the maximum number of sockets that will be left open in the free state.

#### `agent.maxSockets`

- Type: `<number>`

By default set to `Infinity`. Determines how many concurrent sockets the agent can have open per origin. Origin is the returned value of `agent.getName()`.

#### `agent.maxTotalSockets`

- Type: `<number>`

By default set to `Infinity`. Determines how many concurrent sockets the agent can have open. Unlike `maxSockets`, this parameter applies across all origins.

#### `agent.requests`

- Type: `<Object>`

An object which contains queues of requests that have not yet been assigned to sockets. Do not modify.

#### `agent.sockets`

- Type: `<Object>`

An object which contains arrays of sockets currently in use by the agent. Do not modify.

### Class: `http.ClientRequest`

- Extends: `<http.OutgoingMessage>`

This object is created internally and returned from `http.request()`. It represents an *in-progress* request whose header has already been queued. The header is still mutable using the `setHeader(name, value)`, `getHeader(name)`, `removeHeader(name)` API. The actual header will be sent along with the first data chunk or when calling `request.end()`.

To get the response, add a listener for `'response'` to the request object. `'response'` will be emitted from the request object when the response headers have been received. The `'response'` event is executed with one argument which is an instance of `http.IncomingMessage`.

During the `'response'` event, one can add listeners to the response object; particularly to listen for the `'data'` event.

If no `'response'` handler is added, then the response will be entirely discarded. However, if a `'response'` event handler is added, then the data from the response object **must** be consumed, either by calling `response.read()` whenever there is a `'readable'` event, or by adding a `'data'` handler, or by calling the `.resume()` method. Until the data is consumed, the `'end'` event will not fire. Also, until the data is read it will consume memory that can eventually lead to a 'process out of memory' error.

For backward compatibility, `res` will only emit `'error'` if there is an `'error'` listener registered.

Set `Content-Length` header to limit the response body size. If `response.strictContentLength` is set to `true`, mismatching the `Content-Length` header value will result in an `Error` being thrown, identified by `code:` `'ERR_HTTP_CONTENT_LENGTH_MISMATCH'`.

`Content-Length` value should be in bytes, not characters. Use `Buffer.byteLength()` to determine the length of the body in bytes.

#### Event: `'abort'`

Stability: 0 - Deprecated. Listen for the `'close'` event instead.

Emitted when the request has been aborted by the client. This event is only emitted on the first call to `abort()`.

#### Event: `'close'`

Indicates that the request is completed, or its underlying connection was terminated prematurely (before the response completion).

#### Event: `'connect'`

- `response` `<http.IncomingMessage>`
- `socket` `<stream.Duplex>`
- `head` `<Buffer>`

Emitted each time a server responds to a request with a `CONNECT` method. If this event is not being listened for, clients receiving a `CONNECT` method will have their connections closed.

This event is guaranteed to be passed an instance of the `<net.Socket>` class, a subclass of `<stream.Duplex>`, unless the user specifies a socket type other than `<net.Socket>`.

A client and server pair demonstrating how to listen for the `'connect'` event:import { createServer, request } from 'node:http'; import { connect } from 'node:net'; import { URL } from 'node:url'; // Create an HTTP tunneling proxy const proxy = createServer((req, res) => { res.writeHead(200, { 'Content-Type': 'text/plain' }); res.end('okay'); }); proxy.on('connect', (req, clientSocket, head) => { // Connect to an origin server const { port, hostname } = new URL(`http://${req.url}`); const serverSocket = connect(port || 80, hostname, () => { clientSocket.write('HTTP/1.1 200 Connection Established\r\n' + 'Proxy-agent: Node.js-Proxy\r\n' + '\r\n'); serverSocket.write(head); serverSocket.pipe(clientSocket); clientSocket.pipe(serverSocket); }); }); // Now that proxy is running proxy.listen(1337, '127.0.0.1', () => { // Make a request to a tunneling proxy const options = { port: 1337, host: '127.0.0.1', method: 'CONNECT', path: 'www.google.com:80', }; const req = request(options); req.end(); req.on('connect', (res, socket, head) => { console.log('got connected!'); // Make a request over an HTTP tunnel socket.write('GET / HTTP/1.1\r\n' + 'Host: www.google.com:80\r\n' + 'Connection: close\r\n' + '\r\n'); socket.on('data', (chunk) => { console.log(chunk.toString()); }); socket.on('end', () => { proxy.close(); }); }); });const http = require('node:http'); const net = require('node:net'); const { URL } = require('node:url'); // Create an HTTP tunneling proxy const proxy = http.createServer((req, res) => { res.writeHead(200, { 'Content-Type': 'text/plain' }); res.end('okay'); }); proxy.on('connect', (req, clientSocket, head) => { // Connect to an origin server const { port, hostname } = new URL(`http://${req.url}`); const serverSocket = net.connect(port || 80, hostname, () => { clientSocket.write('HTTP/1.1 200 Connection Established\r\n' + 'Proxy-agent: Node.js-Proxy\r\n' + '\r\n'); serverSocket.write(head); serverSocket.pipe(clientSocket); clientSocket.pipe(serverSocket); }); }); // Now that proxy is running proxy.listen(1337, '127.0.0.1', () => { // Make a request to a tunneling proxy const options = { port: 1337, host: '127.0.0.1', method: 'CONNECT', path: 'www.google.com:80', }; const req = http.request(options); req.end(); req.on('connect', (res, socket, head) => { console.log('got connected!'); // Make a request over an HTTP tunnel socket.write('GET / HTTP/1.1\r\n' + 'Host: www.google.com:80\r\n' + 'Connection: close\r\n' + '\r\n'); socket.on('data', (chunk) => { console.log(chunk.toString()); }); socket.on('end', () => { proxy.close(); }); }); });

#### Event: `'continue'`

Emitted when the server sends a '100 Continue' HTTP response, usually because the request contained 'Expect: 100-continue'. This is an instruction that the client should send the request body.

#### Event: `'finish'`

Emitted when the request has been sent. More specifically, this event is emitted when the last segment of the request headers and body have been handed off to the operating system for transmission over the network. It does not imply that the server has received anything yet.

#### Event: `'information'`

- `info` `<Object>`
  - `httpVersion` `<string>`
  - `httpVersionMajor` `<integer>`
  - `httpVersionMinor` `<integer>`
  - `statusCode` `<integer>`
  - `statusMessage` `<string>`
  - `headers` `<Object>`
  - `rawHeaders` `<string>`[]

Emitted when the server sends a 1xx intermediate response (excluding 101 Upgrade). The listeners of this event will receive an object containing the HTTP version, status code, status message, key-value headers object, and array with the raw header names followed by their respective values.import { request } from 'node:http'; const options = { host: '127.0.0.1', port: 8080, path: '/length_request', }; // Make a request const req = request(options); req.end(); req.on('information', (info) => { console.log(`Got information prior to main response: ${info.statusCode}`); });const http = require('node:http'); const options = { host: '127.0.0.1', port: 8080, path: '/length_request', }; // Make a request const req = http.request(options); req.end(); req.on('information', (info) => { console.log(`Got information prior to main response: ${info.statusCode}`); });

101 Upgrade statuses do not fire this event due to their break from the traditional HTTP request/response chain, such as web sockets, in-place TLS upgrades, or HTTP 2.0. To be notified of 101 Upgrade notices, listen for the `'upgrade'` event instead.

#### Event: `'response'`

- `response` `<http.IncomingMessage>`

Emitted when a response is received to this request. This event is emitted only once.

#### Event: `'socket'`

- `socket` `<stream.Duplex>`

This event is guaranteed to be passed an instance of the `<net.Socket>` class, a subclass of `<stream.Duplex>`, unless the user specifies a socket type other than `<net.Socket>`.

#### Event: `'timeout'`

Emitted when the underlying socket times out from inactivity. This only notifies that the socket has been idle. The request must be destroyed manually.

See also: `request.setTimeout()`.

#### Event: `'upgrade'`

- `response` `<http.IncomingMessage>`
- `stream` `<stream.Duplex>`
- `head` `<Buffer>`

Emitted each time a server responds to a request with an upgrade. If this event is not being listened for and the response status code is 101 Switching Protocols, clients receiving an upgrade header will have their connections closed.

This event is guaranteed to be passed an instance of the `<net.Socket>` class, a subclass of `<stream.Duplex>`, unless the user specifies a socket type other than `<net.Socket>`.

A client server pair demonstrating how to listen for the `'upgrade'` event.`import http from 'node:http'; import process from 'node:process'; // Create an HTTP server const server = http.createServer((req, res) => { res.writeHead(200, { 'Content-Type': 'text/plain' }); res.end('okay'); }); server.on('upgrade', (req, stream, head) => { stream.write('HTTP/1.1 101 Web Socket Protocol Handshake\r\n' + 'Upgrade: WebSocket\r\n' + 'Connection: Upgrade\r\n' + '\r\n'); stream.pipe(stream); // echo back }); // Now that server is running server.listen(1337, '127.0.0.1', () => { // make a request const options = { port: 1337, host: '127.0.0.1', headers: { 'Connection': 'Upgrade', 'Upgrade': 'websocket', }, }; const req = http.request(options); req.end(); req.on('upgrade', (res, stream, upgradeHead) => { console.log('got upgraded!'); stream.end(); process.exit(0); }); });``const http = require('node:http'); // Create an HTTP server const server = http.createServer((req, res) => { res.writeHead(200, { 'Content-Type': 'text/plain' }); res.end('okay'); }); server.on('upgrade', (req, stream, head) => { stream.write('HTTP/1.1 101 Web Socket Protocol Handshake\r\n' + 'Upgrade: WebSocket\r\n' + 'Connection: Upgrade\r\n' + '\r\n'); stream.pipe(stream); // echo back }); // Now that server is running server.listen(1337, '127.0.0.1', () => { // make a request const options = { port: 1337, host: '127.0.0.1', headers: { 'Connection': 'Upgrade', 'Upgrade': 'websocket', }, }; const req = http.request(options); req.end(); req.on('upgrade', (res, stream, upgradeHead) => { console.log('got upgraded!'); stream.end(); process.exit(0); }); });`

#### `request.abort()`

Stability: 0 - Deprecated: Use `request.destroy()` instead.

Marks the request as aborting. Calling this will cause remaining data in the response to be dropped and the socket to be destroyed.

#### `request.aborted`

Stability: 0 - Deprecated. Check `request.destroyed` instead.

- Type: `<boolean>`

The `request.aborted` property will be `true` if the request has been aborted.

#### `request.connection`

Stability: 0 - Deprecated. Use `request.socket`.

- Type: `<stream.Duplex>`

See `request.socket`.

#### `request.cork()`

See `writable.cork()`.

#### `request.end([data[, encoding]][, callback])`

- `data` `<string>` | `<Buffer>` | `<Uint8Array>`
- `encoding` `<string>`
- `callback` `<Function>`
- Returns: `<this>`

Finishes sending the request. If any parts of the body are unsent, it will flush them to the stream. If the request is chunked, this will send the terminating `'0\r\n\r\n'`.

If `data` is specified, it is equivalent to calling `request.write(data, encoding)` followed by `request.end(callback)`.

If `callback` is specified, it will be called when the request stream is finished.

#### `request.destroy([error])`

- `error` `<Error>` Optional, an error to emit with `'error'` event.
- Returns: `<this>`

Destroy the request. Optionally emit an `'error'` event, and emit a `'close'` event. Calling this will cause remaining data in the response to be dropped, and the socket to be destroyed if used, or returned to the corresponding Agent pool otherwise if possible.

See `writable.destroy()` for further details.

##### `request.destroyed`

- Type: `<boolean>`

Is `true` after `request.destroy()` has been called.

See `writable.destroyed` for further details.

#### `request.finished`

Stability: 0 - Deprecated. Use `request.writableEnded`.

- Type: `<boolean>`

The `request.finished` property will be `true` if `request.end()` has been called. `request.end()` will automatically be called if the request was initiated via `http.get()`.

#### `request.flushHeaders()`

Flushes the request headers.

For efficiency reasons, Node.js normally buffers the request headers until `request.end()` is called or the first chunk of request data is written. It then tries to pack the request headers and data into a single TCP packet.

That's usually desired (it saves a TCP round-trip), but not when the first data is not sent until possibly much later. `request.flushHeaders()` bypasses the optimization and kickstarts the request.

#### `request.getHeader(name)`

- `name` `<string>`
- Returns: `<any>`

Reads out a header on the request. The name is case-insensitive. The type of the return value depends on the arguments provided to `request.setHeader()`.`request.setHeader('content-type', 'text/html'); request.setHeader('Content-Length', Buffer.byteLength(body)); request.setHeader('Cookie', ['type=ninja', 'language=javascript']); const contentType = request.getHeader('Content-Type'); // 'contentType' is 'text/html' const contentLength = request.getHeader('Content-Length'); // 'contentLength' is of type number const cookie = request.getHeader('Cookie'); // 'cookie' is of type string[]`

#### `request.getHeaderNames()`

- Returns: `<string>`[]

Returns an array containing the unique names of the current outgoing headers. All header names are lowercase.`request.setHeader('Foo', 'bar'); request.setHeader('Cookie', ['foo=bar', 'bar=baz']); const headerNames = request.getHeaderNames(); // headerNames === ['foo', 'cookie']`

#### `request.getHeaders()`

- Returns: `<Object>`

Returns a shallow copy of the current outgoing headers. Since a shallow copy is used, array values may be mutated without additional calls to various header-related http module methods. The keys of the returned object are the header names and the values are the respective header values. All header names are lowercase.

The object returned by the `request.getHeaders()` method *does not* prototypically inherit from the JavaScript `Object`. This means that typical `Object` methods such as `obj.toString()`, `obj.hasOwnProperty()`, and others are not defined and *will not work*.`request.setHeader('Foo', 'bar'); request.setHeader('Cookie', ['foo=bar', 'bar=baz']); const headers = request.getHeaders(); // headers === { foo: 'bar', 'cookie': ['foo=bar', 'bar=baz'] }`

#### `request.getRawHeaderNames()`

- Returns: `<string>`[]

Returns an array containing the unique names of the current outgoing raw headers. Header names are returned with their exact casing being set.`request.setHeader('Foo', 'bar'); request.setHeader('Set-Cookie', ['foo=bar', 'bar=baz']); const headerNames = request.getRawHeaderNames(); // headerNames === ['Foo', 'Set-Cookie']`

#### `request.hasHeader(name)`

- `name` `<string>`
- Returns: `<boolean>`

Returns `true` if the header identified by `name` is currently set in the outgoing headers. The header name matching is case-insensitive.`const hasContentType = request.hasHeader('content-type');`

#### `request.maxHeadersCount`

- Type: `<number>` **Default:** `2000`

Limits maximum response headers count. If set to 0, no limit will be applied.

#### `request.path`

- Type: `<string>` The request path.

#### `request.method`

- Type: `<string>` The request method.

#### `request.host`

- Type: `<string>` The request host.

#### `request.protocol`

- Type: `<string>` The request protocol.

#### `request.removeHeader(name)`

- `name` `<string>`

Removes a header that's already defined into headers object.`request.removeHeader('Content-Type');`

#### `request.reusedSocket`

- Type: `<boolean>` Whether the request is send through a reused socket.

When sending request through a keep-alive enabled agent, the underlying socket might be reused. But if server closes connection at unfortunate time, client may run into a 'ECONNRESET' error.`import http from 'node:http'; const agent = new http.Agent({ keepAlive: true }); // Server has a 5 seconds keep-alive timeout by default http .createServer((req, res) => { res.write('hello\n'); res.end(); }) .listen(3000); setInterval(() => { // Adapting a keep-alive agent http.get('http://localhost:3000', { agent }, (res) => { res.on('data', (data) => { // Do nothing }); }); }, 5000); // Sending request on 5s interval so it's easy to hit idle timeout``const http = require('node:http'); const agent = new http.Agent({ keepAlive: true }); // Server has a 5 seconds keep-alive timeout by default http .createServer((req, res) => { res.write('hello\n'); res.end(); }) .listen(3000); setInterval(() => { // Adapting a keep-alive agent http.get('http://localhost:3000', { agent }, (res) => { res.on('data', (data) => { // Do nothing }); }); }, 5000); // Sending request on 5s interval so it's easy to hit idle timeout`

By marking a request whether it reused socket or not, we can do automatic error retry base on it.`import http from 'node:http'; const agent = new http.Agent({ keepAlive: true }); function retriableRequest() { const req = http .get('http://localhost:3000', { agent }, (res) => { // ... }) .on('error', (err) => { // Check if retry is needed if (req.reusedSocket && err.code === 'ECONNRESET') { retriableRequest(); } }); } retriableRequest();``const http = require('node:http'); const agent = new http.Agent({ keepAlive: true }); function retriableRequest() { const req = http .get('http://localhost:3000', { agent }, (res) => { // ... }) .on('error', (err) => { // Check if retry is needed if (req.reusedSocket && err.code === 'ECONNRESET') { retriableRequest(); } }); } retriableRequest();`

#### `request.setHeader(name, value)`

- `name` `<string>`
- `value` `<any>`

Sets a single header value for headers object. If this header already exists in the to-be-sent headers, its value will be replaced. Use an array of strings here to send multiple headers with the same name. Non-string values will be stored without modification. Therefore, `request.getHeader()` may return non-string values. However, the non-string values will be converted to strings for network transmission.`request.setHeader('Content-Type', 'application/json');`

or`request.setHeader('Cookie', ['type=ninja', 'language=javascript']);`

When the value is a string an exception will be thrown if it contains characters outside the `latin1` encoding.

If you need to pass UTF-8 characters in the value please encode the value using the RFC 8187 standard.const filename = 'Rock 🎵.txt'; request.setHeader('Content-Disposition', `attachment; filename*=utf-8''${encodeURIComponent(filename)}`);

#### `request.setNoDelay([noDelay])`

- `noDelay` `<boolean>`

Once a socket is assigned to this request and is connected `socket.setNoDelay()` will be called.

#### `request.setSocketKeepAlive([enable][, initialDelay])`

- `enable` `<boolean>`
- `initialDelay` `<number>`

Once a socket is assigned to this request and is connected `socket.setKeepAlive()` will be called.

#### `request.setTimeout(timeout[, callback])`

- `timeout` `<number>` Milliseconds before a request times out.
- `callback` `<Function>` Optional function to be called when a timeout occurs. Same as binding to the `'timeout'` event.
- Returns: `<http.ClientRequest>`

Once a socket is assigned to this request and is connected `socket.setTimeout()` will be called.

#### `request.socket`

- Type: `<stream.Duplex>`

Reference to the underlying socket. Usually users will not want to access this property. In particular, the socket will not emit `'readable'` events because of how the protocol parser attaches to the socket.import http from 'node:http'; const options = { host: 'www.google.com', }; const req = http.get(options); req.end(); req.once('response', (res) => { const ip = req.socket.localAddress; const port = req.socket.localPort; console.log(`Your IP address is ${ip} and your source port is ${port}.`); // Consume response object });const http = require('node:http'); const options = { host: 'www.google.com', }; const req = http.get(options); req.end(); req.once('response', (res) => { const ip = req.socket.localAddress; const port = req.socket.localPort; console.log(`Your IP address is ${ip} and your source port is ${port}.`); // Consume response object });

This property is guaranteed to be an instance of the `<net.Socket>` class, a subclass of `<stream.Duplex>`, unless the user specified a socket type other than `<net.Socket>`.

#### `request.uncork()`

See `writable.uncork()`.

#### `request.writableEnded`

- Type: `<boolean>`

Is `true` after `request.end()` has been called. This property does not indicate whether the data has been flushed, for this use `request.writableFinished` instead.

#### `request.writableFinished`

- Type: `<boolean>`

Is `true` if all data has been flushed to the underlying system, immediately before the `'finish'` event is emitted.

#### `request.write(chunk[, encoding][, callback])`

- `chunk` `<string>` | `<Buffer>` | `<Uint8Array>`
- `encoding` `<string>`
- `callback` `<Function>`
- Returns: `<boolean>`

Sends a chunk of the body. This method can be called multiple times. If no `Content-Length` is set, data will automatically be encoded in HTTP Chunked transfer encoding, so that server knows when the data ends. The `Transfer-Encoding: chunked` header is added. Calling `request.end()` is necessary to finish sending the request.

The `encoding` argument is optional and only applies when `chunk` is a string. Defaults to `'utf8'`.

The `callback` argument is optional and will be called when this chunk of data is flushed, but only if the chunk is non-empty.

Returns `true` if the entire data was flushed successfully to the kernel buffer. Returns `false` if all or part of the data was queued in user memory. `'drain'` will be emitted when the buffer is free again.

When `write` function is called with empty string or buffer, it does nothing and waits for more input.

### Class: `http.Server`

- Extends: `<net.Server>`

#### Event: `'checkContinue'`

- `request` `<http.IncomingMessage>`
- `response` `<http.ServerResponse>`

Emitted each time a request with an HTTP `Expect: 100-continue` is received. If this event is not listened for, the server will automatically respond with a `100 Continue` as appropriate.

Handling this event involves calling `response.writeContinue()` if the client should continue to send the request body, or generating an appropriate HTTP response (e.g. 400 Bad Request) if the client should not continue to send the request body.

When this event is emitted and handled, the `'request'` event will not be emitted.

#### Event: `'checkExpectation'`

- `request` `<http.IncomingMessage>`
- `response` `<http.ServerResponse>`

Emitted each time a request with an HTTP `Expect` header is received, where the value is not `100-continue`. If this event is not listened for, the server will automatically respond with a `417 Expectation Failed` as appropriate.

When this event is emitted and handled, the `'request'` event will not be emitted.

#### Event: `'clientError'`

- `exception` `<Error>`
- `socket` `<stream.Duplex>`

If a client connection emits an `'error'` event, it will be forwarded here. Listener of this event is responsible for closing/destroying the underlying socket. For example, one may wish to more gracefully close the socket with a custom HTTP response instead of abruptly severing the connection. The socket **must be closed or destroyed** before the listener ends.

This event is guaranteed to be passed an instance of the `<net.Socket>` class, a subclass of `<stream.Duplex>`, unless the user specifies a socket type other than `<net.Socket>`.

Default behavior is to try close the socket with an HTTP '400 Bad Request', or an HTTP '431 Request Header Fields Too Large' in the case of an `HPE_HEADER_OVERFLOW` error. If the socket is not writable or headers of the current attached `http.ServerResponse` has been sent, it is immediately destroyed.

`socket` is the `net.Socket` object that the error originated from.`import http from 'node:http'; const server = http.createServer((req, res) => { res.end(); }); server.on('clientError', (err, socket) => { socket.end('HTTP/1.1 400 Bad Request\r\n\r\n'); }); server.listen(8000);``const http = require('node:http'); const server = http.createServer((req, res) => { res.end(); }); server.on('clientError', (err, socket) => { socket.end('HTTP/1.1 400 Bad Request\r\n\r\n'); }); server.listen(8000);`

When the `'clientError'` event occurs, there is no `request` or `response` object, so any HTTP response sent, including response headers and payload, *must* be written directly to the `socket` object. Care must be taken to ensure the response is a properly formatted HTTP response message.

`err` is an instance of `Error` with two extra columns: `bytesParsed`: the bytes count of request packet that Node.js may have parsed correctly; `rawPacket`: the raw packet of current request.

In some cases, the client has already received the response and/or the socket has already been destroyed, like in case of `ECONNRESET` errors. Before trying to send data to the socket, it is better to check that it is still writable.`server.on('clientError', (err, socket) => { if (err.code === 'ECONNRESET' || !socket.writable) { return; } socket.end('HTTP/1.1 400 Bad Request\r\n\r\n'); });`

#### Event: `'close'`

Emitted when the server closes.

#### Event: `'connect'`

- `request` `<http.IncomingMessage>` Arguments for the HTTP request, as it is in the `'request'` event
- `socket` `<stream.Duplex>` Network socket between the server and client
- `head` `<Buffer>` The first packet of the tunneling stream (may be empty)

Emitted each time a client requests an HTTP `CONNECT` method. If this event is not listened for, then clients requesting a `CONNECT` method will have their connections closed.

This event is guaranteed to be passed an instance of the `<net.Socket>` class, a subclass of `<stream.Duplex>`, unless the user specifies a socket type other than `<net.Socket>`.

After this event is emitted, the request's socket will not have a `'data'` event listener, meaning it will need to be bound in order to handle data sent to the server on that socket.

#### Event: `'connection'`

- `socket` `<stream.Duplex>`

This event is emitted when a new TCP stream is established. `socket` is typically an object of type `net.Socket`. Usually users will not want to access this event. In particular, the socket will not emit `'readable'` events because of how the protocol parser attaches to the socket. The `socket` can also be accessed at `request.socket`.

This event can also be explicitly emitted by users to inject connections into the HTTP server. In that case, any `Duplex` stream can be passed.

If `socket.setTimeout()` is called here, the timeout will be replaced with `server.keepAliveTimeout` when the socket has served a request (if `server.keepAliveTimeout` is non-zero).

This event is guaranteed to be passed an instance of the `<net.Socket>` class, a subclass of `<stream.Duplex>`, unless the user specifies a socket type other than `<net.Socket>`.

#### Event: `'dropRequest'`

- `request` `<http.IncomingMessage>` Arguments for the HTTP request, as it is in the `'request'` event
- `socket` `<stream.Duplex>` Network socket between the server and client

When the number of requests on a socket reaches the threshold of `server.maxRequestsPerSocket`, the server will drop new requests and emit `'dropRequest'` event instead, then send `503` to client.

#### Event: `'request'`

- `request` `<http.IncomingMessage>`
- `response` `<http.ServerResponse>`

Emitted each time there is a request. There may be multiple requests per connection (in the case of HTTP Keep-Alive connections).

#### Event: `'upgrade'`

- `request` `<http.IncomingMessage>` Arguments for the HTTP request, as it is in the `'request'` event
- `stream` `<stream.Duplex>` The upgraded stream between the server and client
- `head` `<Buffer>` The first packet of the upgraded stream (may be empty)

Emitted each time a client's HTTP upgrade request is accepted. By default all HTTP upgrade requests are ignored (i.e. only regular `'request'` events are emitted, sticking with the normal HTTP request/response flow) unless you listen to this event, in which case they are all accepted (i.e. the `'upgrade'` event is emitted instead, and future communication must handled directly through the raw stream). You can control this more precisely by using the server `shouldUpgradeCallback` option.

Listening to this event is optional and clients cannot insist on a protocol change.

If an upgrade is accepted by `shouldUpgradeCallback` but no event handler is registered then the socket will be destroyed, resulting in an immediate connection closure for the client.

In the uncommon case that the incoming request has a body, this body will be parsed as normal, separate to the upgrade stream, and the raw stream data will only begin after it has completed. To ensure that reading from the stream isn't blocked by waiting for the request body to be read, any reads on the stream will start the request body flowing automatically. If you want to read the request body, ensure that you do so (i.e. you attach `'data'` listeners) before starting to read from the upgraded stream.

The stream argument will typically be the `<net.Socket>` instance used by the request, but in some cases (such as with a request body) it may be a duplex stream. If required, you can access the raw connection underlying the request via `request.socket`, which is guaranteed to be an instance of `<net.Socket>` unless the user specified another socket type.

#### `server.close([callback])`

- `callback` `<Function>`

Stops the server from accepting new connections and closes all connections connected to this server which are not sending a request or waiting for a response. See `net.Server.close()`.`const http = require('node:http'); const server = http.createServer({ keepAliveTimeout: 60000 }, (req, res) => { res.writeHead(200, { 'Content-Type': 'application/json' }); res.end(JSON.stringify({ data: 'Hello World!', })); }); server.listen(8000); // Close the server after 10 seconds setTimeout(() => { server.close(() => { console.log('server on port 8000 closed successfully'); }); }, 10000);`

#### `server.closeAllConnections()`

Closes all established HTTP(S) connections connected to this server, including active connections connected to this server which are sending a request or waiting for a response. This does *not* destroy sockets upgraded to a different protocol, such as WebSocket or HTTP/2. This is a forceful way of closing all connections and should be used with caution. Whenever using this in conjunction with `server.close`, calling this *after* `server.close` is recommended as to avoid race conditions where new connections are created between a call to this and a call to `server.close`. `const http = require('node:http'); const server = http.createServer({ keepAliveTimeout: 60000 }, (req, res) => { res.writeHead(200, { 'Content-Type': 'application/json' }); res.end(JSON.stringify({ data: 'Hello World!', })); }); server.listen(8000); // Close the server after 10 seconds setTimeout(() => { server.close(() => { console.log('server on port 8000 closed successfully'); }); // Closes all connections, ensuring the server closes successfully server.closeAllConnections(); }, 10000);`

#### `server.closeIdleConnections()`

Closes all connections connected to this server which are not sending a request or waiting for a response. Starting with Node.js 19.0.0, there's no need for calling this method in conjunction with `server.close` to reap `keep-alive` connections. Using it won't cause any harm though, and it can be useful to ensure backwards compatibility for libraries and applications that need to support versions older than 19.0.0. Whenever using this in conjunction with `server.close`, calling this *after* `server.close` is recommended as to avoid race conditions where new connections are created between a call to this and a call to `server.close`. `const http = require('node:http'); const server = http.createServer({ keepAliveTimeout: 60000 }, (req, res) => { res.writeHead(200, { 'Content-Type': 'application/json' }); res.end(JSON.stringify({ data: 'Hello World!', })); }); server.listen(8000); // Close the server after 10 seconds setTimeout(() => { server.close(() => { console.log('server on port 8000 closed successfully'); }); // Closes idle connections, such as keep-alive connections. Server will close // once remaining active connections are terminated server.closeIdleConnections(); }, 10000);`

#### `server.headersTimeout`

- Type: `<number>` **Default:** The minimum between `server.requestTimeout` or `60000`.

Limit the amount of time the parser will wait to receive the complete HTTP headers.

If the timeout expires, the server responds with status 408 without forwarding the request to the request listener and then closes the connection.

It must be set to a non-zero value (e.g. 120 seconds) to protect against potential Denial-of-Service attacks in case the server is deployed without a reverse proxy in front.

#### `server.listen()`

Starts the HTTP server listening for connections. This method is identical to `server.listen()` from `net.Server`.

#### `server.listening`

- Type: `<boolean>` Indicates whether or not the server is listening for connections.

#### `server.maxHeadersCount`

- Type: `<number>` **Default:** `2000`

Limits maximum incoming headers count. If set to 0, no limit will be applied.

#### `server.requestTimeout`

- Type: `<number>` **Default:** `300000`

Sets the timeout value in milliseconds for receiving the entire request from the client.

If the timeout expires, the server responds with status 408 without forwarding the request to the request listener and then closes the connection.

It must be set to a non-zero value (e.g. 120 seconds) to protect against potential Denial-of-Service attacks in case the server is deployed without a reverse proxy in front.

#### `server.setTimeout([msecs][, callback])`

- `msecs` `<number>` **Default:** 0 (no timeout)
- `callback` `<Function>`
- Returns: `<http.Server>`

Sets the timeout value for sockets, and emits a `'timeout'` event on the Server object, passing the socket as an argument, if a timeout occurs.

If there is a `'timeout'` event listener on the Server object, then it will be called with the timed-out socket as an argument.

By default, the Server does not timeout sockets. However, if a callback is assigned to the Server's `'timeout'` event, timeouts must be handled explicitly.

#### `server.maxRequestsPerSocket`

- Type: `<number>` Requests per socket. **Default:** 0 (no limit)

The maximum number of requests socket can handle before closing keep alive connection.

A value of `0` will disable the limit.

When the limit is reached it will set the `Connection` header value to `close`, but will not actually close the connection, subsequent requests sent after the limit is reached will get `503 Service Unavailable` as a response.

#### `server.timeout`

- Type: `<number>` Timeout in milliseconds. **Default:** 0 (no timeout)

The number of milliseconds of inactivity before a socket is presumed to have timed out.

A value of `0` will disable the timeout behavior on incoming connections.

The socket timeout logic is set up on connection, so changing this value only affects new connections to the server, not any existing connections.

#### `server.keepAliveTimeout`

- Type: `<number>` Timeout in milliseconds. **Default:** `5000` (5 seconds).

The number of milliseconds of inactivity a server needs to wait for additional incoming data, after it has finished writing the last response, before a socket will be destroyed.

This timeout value is combined with the `server.keepAliveTimeoutBuffer` option to determine the actual socket timeout, calculated as: socketTimeout = keepAliveTimeout + keepAliveTimeoutBuffer If the server receives new data before the keep-alive timeout has fired, it will reset the regular inactivity timeout, i.e., `server.timeout`.

A value of `0` will disable the keep-alive timeout behavior on incoming connections. A value of `0` makes the HTTP server behave similarly to Node.js versions prior to 8.0.0, which did not have a keep-alive timeout.

The socket timeout logic is set up on connection, so changing this value only affects new connections to the server, not any existing connections.

#### `server.keepAliveTimeoutBuffer`

- Type: `<number>` Timeout in milliseconds. **Default:** `1000` (1 second).

An additional buffer time added to the `server.keepAliveTimeout` to extend the internal socket timeout.

This buffer helps reduce connection reset (`ECONNRESET`) errors by increasing the socket timeout slightly beyond the advertised keep-alive timeout.

This option applies only to new incoming connections.

#### `server[Symbol.asyncDispose]()`

Calls `server.close()` and returns a promise that fulfills when the server has closed.

### Class: `http.ServerResponse`

- Extends: `<http.OutgoingMessage>`

This object is created internally by an HTTP server, not by the user. It is passed as the second parameter to the `'request'` event.

#### Event: `'close'`

Indicates that the response is completed, or its underlying connection was terminated prematurely (before the response completion).

#### Event: `'finish'`

Emitted when the response has been sent. More specifically, this event is emitted when the last segment of the response headers and body have been handed off to the operating system for transmission over the network. It does not imply that the client has received anything yet.

#### `response.addTrailers(headers)`

- `headers` `<Object>`

This method adds HTTP trailing headers (a header but at the end of the message) to the response.

Trailers will **only** be emitted if chunked encoding is used for the response; if it is not (e.g. if the request was HTTP/1.0), they will be silently discarded.

HTTP requires the `Trailer` header to be sent in order to emit trailers, with a list of the header fields in its value. E.g.,`response.writeHead(200, { 'Content-Type': 'text/plain', 'Trailer': 'Content-MD5' }); response.write(fileData); response.addTrailers({ 'Content-MD5': '7895bf4b8828b55ceaf47747b4bca667' }); response.end();`

Attempting to set a header field name or value that contains invalid characters will result in a `TypeError` being thrown.

#### `response.connection`

Stability: 0 - Deprecated. Use `response.socket`.

- Type: `<stream.Duplex>`

See `response.socket`.

#### `response.cork()`

See `writable.cork()`.

#### `response.end([data[, encoding]][, callback])`

- `data` `<string>` | `<Buffer>` | `<Uint8Array>`
- `encoding` `<string>`
- `callback` `<Function>`
- Returns: `<this>`

This method signals to the server that all of the response headers and body have been sent; that server should consider this message complete. The method, `response.end()`, MUST be called on each response.

If `data` is specified, it is similar in effect to calling `response.write(data, encoding)` followed by `response.end(callback)`.

If `callback` is specified, it will be called when the response stream is finished.

#### `response.finished`

Stability: 0 - Deprecated. Use `response.writableEnded`.

- Type: `<boolean>`

The `response.finished` property will be `true` if `response.end()` has been called.

#### `response.flushHeaders()`

Flushes the response headers. See also: `request.flushHeaders()`.

#### `response.getHeader(name)`

- `name` `<string>`
- Returns: `<number>` | `<string>` | `<string>`[] | `<undefined>`

Reads out a header that's already been queued but not sent to the client. The name is case-insensitive. The type of the return value depends on the arguments provided to `response.setHeader()`.`response.setHeader('Content-Type', 'text/html'); response.setHeader('Content-Length', Buffer.byteLength(body)); response.setHeader('Set-Cookie', ['type=ninja', 'language=javascript']); const contentType = response.getHeader('content-type'); // contentType is 'text/html' const contentLength = response.getHeader('Content-Length'); // contentLength is of type number const setCookie = response.getHeader('set-cookie'); // setCookie is of type string[]`

#### `response.getHeaderNames()`

- Returns: `<string>`[]

Returns an array containing the unique names of the current outgoing headers. All header names are lowercase.`response.setHeader('Foo', 'bar'); response.setHeader('Set-Cookie', ['foo=bar', 'bar=baz']); const headerNames = response.getHeaderNames(); // headerNames === ['foo', 'set-cookie']`

#### `response.getHeaders()`

- Returns: `<Object>`

Returns a shallow copy of the current outgoing headers. Since a shallow copy is used, array values may be mutated without additional calls to various header-related http module methods. The keys of the returned object are the header names and the values are the respective header values. All header names are lowercase.

The object returned by the `response.getHeaders()` method *does not* prototypically inherit from the JavaScript `Object`. This means that typical `Object` methods such as `obj.toString()`, `obj.hasOwnProperty()`, and others are not defined and *will not work*.`response.setHeader('Foo', 'bar'); response.setHeader('Set-Cookie', ['foo=bar', 'bar=baz']); const headers = response.getHeaders(); // headers === { foo: 'bar', 'set-cookie': ['foo=bar', 'bar=baz'] }`

#### `response.hasHeader(name)`

- `name` `<string>`
- Returns: `<boolean>`

Returns `true` if the header identified by `name` is currently set in the outgoing headers. The header name matching is case-insensitive.`const hasContentType = response.hasHeader('content-type');`

#### `response.headersSent`

- Type: `<boolean>`
