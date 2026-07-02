---
title: "HTTP (part 3/3)"
source: https://nodejs.org/api/http.html
domain: javascript
license: CC-BY-SA-2.5 (MDN) / MIT (Node.js)
tags: javascript, typescript, node.js, nodejs, npm
fetched: 2026-07-02
part: 3/3
---

#### Event: `'drain'`

Emitted when the buffer of the message is free again.

#### Event: `'finish'`

Emitted when the transmission is finished successfully.

#### Event: `'prefinish'`

Emitted after `outgoingMessage.end()` is called. When the event is emitted, all data has been processed but not necessarily completely flushed.

#### `outgoingMessage.addTrailers(headers)`

- `headers` `<Object>`

Adds HTTP trailers (headers but at the end of the message) to the message.Trailers will **only** be emitted if the message is chunked encoded. If not, the trailers will be silently discarded.HTTP requires the `Trailer` header to be sent to emit trailers, with a list of header field names in its value, e.g.`message.writeHead(200, { 'Content-Type': 'text/plain', 'Trailer': 'Content-MD5' }); message.write(fileData); message.addTrailers({ 'Content-MD5': '7895bf4b8828b55ceaf47747b4bca667' }); message.end();`Attempting to set a header field name or value that contains invalid characters will result in a `TypeError` being thrown.

#### `outgoingMessage.appendHeader(name, value)`

- `name` `<string>` Header name
- `value` `<string>` | `<string>`[] Header value
- Returns: `<this>`

Append a single header value to the header object.If the value is an array, this is equivalent to calling this method multiple times.If there were no previous values for the header, this is equivalent to calling `outgoingMessage.setHeader(name, value)`.Depending of the value of `options.uniqueHeaders` when the client request or the server were created, this will end up in the header being sent multiple times or a single time with values joined using `;`.

#### `outgoingMessage.connection`

Stability: 0 - Deprecated: Use `outgoingMessage.socket` instead.

Alias of `outgoingMessage.socket`.

#### `outgoingMessage.cork()`

See `writable.cork()`.

#### `outgoingMessage.destroy([error])`

- `error` `<Error>` Optional, an error to emit with `error` event
- Returns: `<this>`

Destroys the message. Once a socket is associated with the message and is connected, that socket will be destroyed as well.

#### `outgoingMessage.end(chunk[, encoding][, callback])`

- `chunk` `<string>` | `<Buffer>` | `<Uint8Array>`
- `encoding` `<string>` Optional, **Default**: `utf8`
- `callback` `<Function>` Optional
- Returns: `<this>`

Finishes the outgoing message. If any parts of the body are unsent, it will flush them to the underlying system. If the message is chunked, it will send the terminating chunk `0\r\n\r\n`, and send the trailers (if any).If `chunk` is specified, it is equivalent to calling `outgoingMessage.write(chunk, encoding)`, followed by `outgoingMessage.end(callback)`.If `callback` is provided, it will be called when the message is finished (equivalent to a listener of the `'finish'` event).

#### `outgoingMessage.flushHeaders()`

Flushes the message headers.For efficiency reason, Node.js normally buffers the message headers until `outgoingMessage.end()` is called or the first chunk of message data is written. It then tries to pack the headers and data into a single TCP packet.It is usually desired (it saves a TCP round-trip), but not when the first data is not sent until possibly much later. `outgoingMessage.flushHeaders()` bypasses the optimization and kickstarts the message.

#### `outgoingMessage.getHeader(name)`

- `name` `<string>` Name of header
- Returns: `<number>` | `<string>` | `<string>`[] | `<undefined>`

Gets the value of the HTTP header with the given name. If that header is not set, the returned value will be `undefined`.

#### `outgoingMessage.getHeaderNames()`

- Returns: `<string>`[]

Returns an array containing the unique names of the current outgoing headers. All names are lowercase.

#### `outgoingMessage.getHeaders()`

- Returns: `<Object>`

Returns a shallow copy of the current outgoing headers. Since a shallow copy is used, array values may be mutated without additional calls to various header-related HTTP module methods. The keys of the returned object are the header names and the values are the respective header values. All header names are lowercase.The object returned by the `outgoingMessage.getHeaders()` method does not prototypically inherit from the JavaScript `Object`. This means that typical `Object` methods such as `obj.toString()`, `obj.hasOwnProperty()`, and others are not defined and will not work.`outgoingMessage.setHeader('Foo', 'bar'); outgoingMessage.setHeader('Set-Cookie', ['foo=bar', 'bar=baz']); const headers = outgoingMessage.getHeaders(); // headers === { foo: 'bar', 'set-cookie': ['foo=bar', 'bar=baz'] }`

#### `outgoingMessage.hasHeader(name)`

- `name` `<string>`
- Returns: `<boolean>`

Returns `true` if the header identified by `name` is currently set in the outgoing headers. The header name is case-insensitive.`const hasContentType = outgoingMessage.hasHeader('content-type');`

#### `outgoingMessage.headersSent`

- Type: `<boolean>`

Read-only. `true` if the headers were sent, otherwise `false`.

#### `outgoingMessage.pipe()`

Overrides the `stream.pipe()` method inherited from the legacy `Stream` class which is the parent class of `http.OutgoingMessage`.Calling this method will throw an `Error` because `outgoingMessage` is a write-only stream.

#### `outgoingMessage.removeHeader(name)`

- `name` `<string>` Header name

Removes a header that is queued for implicit sending.`outgoingMessage.removeHeader('Content-Encoding');`

#### `outgoingMessage.setHeader(name, value)`

- `name` `<string>` Header name
- `value` `<number>` | `<string>` | `<string>`[] Header value
- Returns: `<this>`

Sets a single header value. If the header already exists in the to-be-sent headers, its value will be replaced. Use an array of strings to send multiple headers with the same name.

#### `outgoingMessage.setHeaders(headers)`

- `headers` `<Headers>` | `<Map>`
- Returns: `<this>`

Sets multiple header values for implicit headers. `headers` must be an instance of `Headers` or `Map`, if a header already exists in the to-be-sent headers, its value will be replaced.`const headers = new Headers({ foo: 'bar' }); outgoingMessage.setHeaders(headers);`or`const headers = new Map([['foo', 'bar']]); outgoingMessage.setHeaders(headers);`When headers have been set with `outgoingMessage.setHeaders()`, they will be merged with any headers passed to `response.writeHead()`, with the headers passed to `response.writeHead()` given precedence.`// Returns content-type = text/plain const server = http.createServer((req, res) => { const headers = new Headers({ 'Content-Type': 'text/html' }); res.setHeaders(headers); res.writeHead(200, { 'Content-Type': 'text/plain' }); res.end('ok'); });`

#### `outgoingMessage.setTimeout(msecs[, callback])`

- `msecs` `<number>`
- `callback` `<Function>` Optional function to be called when a timeout occurs. Same as binding to the `timeout` event.
- Returns: `<this>`

Once a socket is associated with the message and is connected, `socket.setTimeout()` will be called with `msecs` as the first parameter.

#### `outgoingMessage.socket`

- Type: `<stream.Duplex>`

Reference to the underlying socket. Usually, users will not want to access this property.After calling `outgoingMessage.end()`, this property will be nulled.

#### `outgoingMessage.uncork()`

See `writable.uncork()`

#### `outgoingMessage.writableCorked`

- Type: `<number>`

The number of times `outgoingMessage.cork()` has been called.

#### `outgoingMessage.writableEnded`

- Type: `<boolean>`

Is `true` if `outgoingMessage.end()` has been called. This property does not indicate whether the data has been flushed. For that purpose, use `message.writableFinished` instead.

#### `outgoingMessage.writableFinished`

- Type: `<boolean>`

Is `true` if all data has been flushed to the underlying system.

#### `outgoingMessage.writableHighWaterMark`

- Type: `<number>`

The `highWaterMark` of the underlying socket if assigned. Otherwise, the default buffer level when `writable.write()` starts returning false (`16384`).

#### `outgoingMessage.writableLength`

- Type: `<number>`

The number of buffered bytes.

#### `outgoingMessage.writableObjectMode`

- Type: `<boolean>`

Always `false`.

#### `outgoingMessage.write(chunk[, encoding][, callback])`

- `chunk` `<string>` | `<Buffer>` | `<Uint8Array>`
- `encoding` `<string>` **Default**: `utf8`
- `callback` `<Function>`
- Returns: `<boolean>`

Sends a chunk of the body. This method can be called multiple times.The `encoding` argument is only relevant when `chunk` is a string. Defaults to `'utf8'`.The `callback` argument is optional and will be called when this chunk of data is flushed.Returns `true` if the entire data was flushed successfully to the kernel buffer. Returns `false` if all or part of the data was queued in the user memory. The `'drain'` event will be emitted when the buffer is free again.

### `http.METHODS`

- Type: `<string>`[]

A list of the HTTP methods that are supported by the parser.

### `http.STATUS_CODES`

- Type: `<Object>`

A collection of all the standard HTTP response status codes, and the short description of each. For example, `http.STATUS_CODES[404] === 'Not Found'`.

### `http.createServer([options][, requestListener])`

- `options` `<Object>`
  - `connectionsCheckingInterval`: Sets the interval value in milliseconds to check for request and headers timeout in incomplete requests. **Default:** `30000`.
  - `headersTimeout`: Sets the timeout value in milliseconds for receiving the complete HTTP headers from the client. See `server.headersTimeout` for more information. **Default:** `60000`.
  - `highWaterMark` `<number>` Optionally overrides all `socket`s' `readableHighWaterMark` and `writableHighWaterMark`. This affects `highWaterMark` property of both `IncomingMessage` and `ServerResponse`. **Default:** See `stream.getDefaultHighWaterMark()`.
  - `httpValidation` `<string>` Controls HTTP header value validation strictness for incoming requests. Accepted values are:
    - `'strict'`: Strictest validation; rejects any non-ASCII or control characters in header values.
    - `'relaxed'`: Allows a limited set of non-ASCII characters in header values, aligning with the Fetch specification.
    - `'insecure'`: Disables all header value validation (equivalent to `insecureHTTPParser: true`). Cannot be used together with `insecureHTTPParser`. **Default:** `'strict'`.
  - `insecureHTTPParser` `<boolean>` If set to `true`, it will use an HTTP parser with leniency flags enabled. Using the insecure parser should be avoided. See `--insecure-http-parser` for more information. **Default:** `false`.
  - `IncomingMessage` `<http.IncomingMessage>` Specifies the `IncomingMessage` class to be used. Useful for extending the original `IncomingMessage`. **Default:** `IncomingMessage`.
  - `joinDuplicateHeaders` `<boolean>` If set to `true`, this option allows joining the field line values of multiple headers in a request with a comma (`,`) instead of discarding the duplicates. For more information, refer to `message.headers`. **Default:** `false`.
  - `keepAlive` `<boolean>` If set to `true`, it enables keep-alive functionality on the socket immediately after a new incoming connection is received, similarly on what is done in `socket.setKeepAlive()`. **Default:** `false`.
  - `keepAliveInitialDelay` `<number>` If set to a positive number, it sets the initial delay before the first keepalive probe is sent on an idle socket. **Default:** `0`.
  - `keepAliveTimeout`: The number of milliseconds of inactivity a server needs to wait for additional incoming data, after it has finished writing the last response, before a socket will be destroyed. See `server.keepAliveTimeout` for more information. **Default:** `5000`.
  - `maxHeaderSize` `<number>` Optionally overrides the value of `--max-http-header-size` for requests received by this server, i.e. the maximum length of request headers in bytes. **Default:** 16384 (16 KiB).
  - `noDelay` `<boolean>` If set to `true`, it disables the use of Nagle's algorithm immediately after a new incoming connection is received. **Default:** `true`.
  - `requestTimeout`: Sets the timeout value in milliseconds for receiving the entire request from the client. See `server.requestTimeout` for more information. **Default:** `300000`.
  - `requireHostHeader` `<boolean>` If set to `true`, it forces the server to respond with a 400 (Bad Request) status code to any HTTP/1.1 request message that lacks a Host header (as mandated by the specification). **Default:** `true`.
  - `ServerResponse` `<http.ServerResponse>` Specifies the `ServerResponse` class to be used. Useful for extending the original `ServerResponse`. **Default:** `ServerResponse`.
  - `shouldUpgradeCallback(request)` `<Function>` A callback which receives an incoming request and returns a boolean, to control which upgrade attempts should be accepted. Accepted upgrades will fire an `'upgrade'` event (or their sockets will be destroyed, if no listener is registered) while rejected upgrades will fire a `'request'` event like any non-upgrade request. This options defaults to `() => server.listenerCount('upgrade') > 0`.
  - `uniqueHeaders` `<Array>` A list of response headers that should be sent only once. If the header's value is an array, the items will be joined using `;`.
  - `rejectNonStandardBodyWrites` `<boolean>` If set to `true`, an error is thrown when writing to an HTTP response which does not have a body. **Default:** `false`.
  - `optimizeEmptyRequests` `<boolean>` If set to `true`, requests without `Content-Length` or `Transfer-Encoding` headers (indicating no body) will be initialized with an already-ended body stream, so they will never emit any stream events (like `'data'` or `'end'`). You can use `req.readableEnded` to detect this case. **Default:** `false`.
- `requestListener` `<Function>`
- Returns: `<http.Server>`

Returns a new instance of `http.Server`.The `requestListener` is a function which is automatically added to the `'request'` event.`import http from 'node:http'; // Create a local server to receive data from const server = http.createServer((req, res) => { res.writeHead(200, { 'Content-Type': 'application/json' }); res.end(JSON.stringify({ data: 'Hello World!', })); }); server.listen(8000);``const http = require('node:http'); // Create a local server to receive data from const server = http.createServer((req, res) => { res.writeHead(200, { 'Content-Type': 'application/json' }); res.end(JSON.stringify({ data: 'Hello World!', })); }); server.listen(8000);``import http from 'node:http'; // Create a local server to receive data from const server = http.createServer(); // Listen to the request event server.on('request', (request, res) => { res.writeHead(200, { 'Content-Type': 'application/json' }); res.end(JSON.stringify({ data: 'Hello World!', })); }); server.listen(8000);``const http = require('node:http'); // Create a local server to receive data from const server = http.createServer(); // Listen to the request event server.on('request', (request, res) => { res.writeHead(200, { 'Content-Type': 'application/json' }); res.end(JSON.stringify({ data: 'Hello World!', })); }); server.listen(8000);`

### `http.get(options[, callback])`

### `http.get(url[, options][, callback])`

- `url` `<string>` | `<URL>`
- `options` `<Object>` Accepts the same `options` as `http.request()`, with the method set to GET by default.
- `callback` `<Function>`
- Returns: `<http.ClientRequest>`

Since most requests are GET requests without bodies, Node.js provides this convenience method. The only difference between this method and `http.request()` is that it sets the method to GET by default and calls `req.end()` automatically. The callback must take care to consume the response data for reasons stated in `http.ClientRequest` section.The `callback` is invoked with a single argument that is an instance of `http.IncomingMessage`.JSON fetching example:http.get('http://localhost:8000/', (res) => { const { statusCode } = res; const contentType = res.headers['content-type']; let error; // Any 2xx status code signals a successful response but // here we're only checking for 200. if (statusCode !== 200) { error = new Error('Request Failed.\n' + `Status Code: ${statusCode}`); } else if (!/^application\/json/.test(contentType)) { error = new Error('Invalid content-type.\n' + `Expected application/json but received ${contentType}`); } if (error) { console.error(error.message); // Consume response data to free up memory res.resume(); return; } res.setEncoding('utf8'); let rawData = ''; res.on('data', (chunk) => { rawData += chunk; }); res.on('end', () => { try { const parsedData = JSON.parse(rawData); console.log(parsedData); } catch (e) { console.error(e.message); } }); }).on('error', (e) => { console.error(`Got error: ${e.message}`); }); // Create a local server to receive data from const server = http.createServer((req, res) => { res.writeHead(200, { 'Content-Type': 'application/json' }); res.end(JSON.stringify({ data: 'Hello World!', })); }); server.listen(8000);

### `http.globalAgent`

- Type: `<http.Agent>`

Global instance of `Agent` which is used as the default for all HTTP client requests. Diverges from a default `Agent` configuration by having `keepAlive` enabled and a `timeout` of 5 seconds.

### `http.maxHeaderSize`

- Type: `<number>`

Read-only property specifying the maximum allowed size of HTTP headers in bytes. Defaults to 16 KiB. Configurable using the `--max-http-header-size` CLI option.This can be overridden for servers and client requests by passing the `maxHeaderSize` option.

### `http.request(options[, callback])`

### `http.request(url[, options][, callback])`

- `url` `<string>` | `<URL>`
- `options` `<Object>`
  - `agent` `<http.Agent>` | `<boolean>` Controls `Agent` behavior. Possible values:
    - `undefined` (default): use `http.globalAgent` for this host and port.
    - `Agent` object: explicitly use the passed in `Agent`.
    - `false`: causes a new `Agent` with default values to be used.
  - `auth` `<string>` Basic authentication (`'user:password'`) to compute an Authorization header.
  - `createConnection` `<Function>` A function that produces a socket/stream to use for the request when the `agent` option is not used. This can be used to avoid creating a custom `Agent` class just to override the default `createConnection` function. See `agent.createConnection()` for more details. Any `Duplex` stream is a valid return value.
  - `defaultPort` `<number>` Default port for the protocol. **Default:** `agent.defaultPort` if an `Agent` is used, else `undefined`.
  - `family` `<number>` IP address family to use when resolving `host` or `hostname`. Valid values are `4` or `6`. When unspecified, both IP v4 and v6 will be used.
  - `headers` `<Object>` | `<Array>` An object or an array of strings containing request headers. The array is in the same format as `message.rawHeaders`.
  - `hints` `<number>` Optional `dns.lookup()` hints.
  - `host` `<string>` A domain name or IP address of the server to issue the request to. **Default:** `'localhost'`.
  - `hostname` `<string>` Alias for `host`. To support `url.parse()`, `hostname` will be used if both `host` and `hostname` are specified.
  - `httpValidation` `<string>` Controls HTTP header value validation strictness for outgoing requests. Accepted values are:
    - `'strict'`: Strictest validation; rejects any non-ASCII or control characters in header values.
    - `'relaxed'`: Allows a limited set of non-ASCII characters in header values, aligning with the Fetch specification.
    - `'insecure'`: Disables all header value validation (equivalent to `insecureHTTPParser: true`). Cannot be used together with `insecureHTTPParser`. **Default:** `'strict'`.
  - `insecureHTTPParser` `<boolean>` If set to `true`, it will use an HTTP parser with leniency flags enabled. Using the insecure parser should be avoided. See `--insecure-http-parser` for more information. **Default:** `false`
  - `joinDuplicateHeaders` `<boolean>` It joins the field line values of multiple headers in a request with `,` instead of discarding the duplicates. See `message.headers` for more information. **Default:** `false`.
  - `localAddress` `<string>` Local interface to bind for network connections.
  - `localPort` `<number>` Local port to connect from.
  - `lookup` `<Function>` Custom lookup function. **Default:** `dns.lookup()`.
  - `maxHeaderSize` `<number>` Optionally overrides the value of `--max-http-header-size` (the maximum length of response headers in bytes) for responses received from the server. **Default:** 16384 (16 KiB).
  - `method` `<string>` A string specifying the HTTP request method. **Default:** `'GET'`.
  - `path` `<string>` Request path. Should include query string if any. E.G. `'/index.html?page=12'`. An exception is thrown when the request path contains illegal characters. Currently, only spaces are rejected but that may change in the future. **Default:** `'/'`.
  - `port` `<number>` Port of remote server. **Default:** `defaultPort` if set, else `80`.
  - `protocol` `<string>` Protocol to use. **Default:** `'http:'`.
  - `setDefaultHeaders` `<boolean>`: Specifies whether or not to automatically add default headers such as `Connection`, `Content-Length`, `Transfer-Encoding`, and `Host`. If set to `false` then all necessary headers must be added manually. Defaults to `true`.
  - `setHost` `<boolean>`: Specifies whether or not to automatically add the `Host` header. If provided, this overrides `setDefaultHeaders`. Defaults to `true`.
  - `signal` `<AbortSignal>`: An AbortSignal that may be used to abort an ongoing request.
  - `socketPath` `<string>` Unix domain socket. Cannot be used if one of `host` or `port` is specified, as those specify a TCP Socket.
  - `timeout` `<number>`: A number specifying the socket timeout in milliseconds. This will set the timeout before the socket is connected.
  - `uniqueHeaders` `<Array>` A list of request headers that should be sent only once. If the header's value is an array, the items will be joined using `;`.
- `callback` `<Function>`
- Returns: `<http.ClientRequest>`

`options` in `socket.connect()` are also supported.Node.js maintains several connections per server to make HTTP requests. This function allows one to transparently issue requests.`url` can be a string or a `URL` object. If `url` is a string, it is automatically parsed with `new URL()`. If it is a `URL` object, it will be automatically converted to an ordinary `options` object.If both `url` and `options` are specified, the objects are merged, with the `options` properties taking precedence.The optional `callback` parameter will be added as a one-time listener for the `'response'` event.`http.request()` returns an instance of the `http.ClientRequest` class. The `ClientRequest` instance is a writable stream. If one needs to upload a file with a POST request, then write to the `ClientRequest` object.import http from 'node:http'; import { Buffer } from 'node:buffer'; const postData = JSON.stringify({ 'msg': 'Hello World!', }); const options = { hostname: 'www.google.com', port: 80, path: '/upload', method: 'POST', headers: { 'Content-Type': 'application/json', 'Content-Length': Buffer.byteLength(postData), }, }; const req = http.request(options, (res) => { console.log(`STATUS: ${res.statusCode}`); console.log(`HEADERS: ${JSON.stringify(res.headers)}`); res.setEncoding('utf8'); res.on('data', (chunk) => { console.log(`BODY: ${chunk}`); }); res.on('end', () => { console.log('No more data in response.'); }); }); req.on('error', (e) => { console.error(`problem with request: ${e.message}`); }); // Write data to request body req.write(postData); req.end();const http = require('node:http'); const postData = JSON.stringify({ 'msg': 'Hello World!', }); const options = { hostname: 'www.google.com', port: 80, path: '/upload', method: 'POST', headers: { 'Content-Type': 'application/json', 'Content-Length': Buffer.byteLength(postData), }, }; const req = http.request(options, (res) => { console.log(`STATUS: ${res.statusCode}`); console.log(`HEADERS: ${JSON.stringify(res.headers)}`); res.setEncoding('utf8'); res.on('data', (chunk) => { console.log(`BODY: ${chunk}`); }); res.on('end', () => { console.log('No more data in response.'); }); }); req.on('error', (e) => { console.error(`problem with request: ${e.message}`); }); // Write data to request body req.write(postData); req.end();In the example `req.end()` was called. With `http.request()` one must always call `req.end()` to signify the end of the request - even if there is no data being written to the request body.If any error is encountered during the request (be that with DNS resolution, TCP level errors, or actual HTTP parse errors) an `'error'` event is emitted on the returned request object. As with all `'error'` events, if no listeners are registered the error will be thrown.There are a few special headers that should be noted. Sending a 'Connection: keep-alive' will notify Node.js that the connection to the server should be persisted until the next request. Sending a 'Content-Length' header will disable the default chunked encoding. Sending an 'Expect' header will immediately send the request headers. Usually, when sending 'Expect: 100-continue', both a timeout and a listener for the `'continue'` event should be set. See RFC 2616 Section 8.2.3 for more information. Sending an Authorization header will override using the `auth` option to compute basic authentication. Example using a `URL` as `options`:`const options = new URL('http://abc:xyz@example.com'); const req = http.request(options, (res) => { // ... });`In a successful request, the following events will be emitted in the following order: `'socket'` `'response'` `'data'` any number of times, on the `res` object (`'data'` will not be emitted at all if the response body is empty, for instance, in most redirects) `'end'` on the `res` object `'close'` In the case of a connection error, the following events will be emitted: `'socket'` `'error'` `'close'` In the case of a premature connection close before the response is received, the following events will be emitted in the following order: `'socket'` `'error'` with an error with message `'Error: socket hang up'` and code `'ECONNRESET'` `'close'` In the case of a premature connection close after the response is received, the following events will be emitted in the following order: `'socket'` `'response'` `'data'` any number of times, on the `res` object (connection closed here) `'aborted'` on the `res` object `'close'` `'error'` on the `res` object with an error with message `'Error: aborted'` and code `'ECONNRESET'` `'close'` on the `res` object If `req.destroy()` is called before a socket is assigned, the following events will be emitted in the following order: (`req.destroy()` called here) `'error'` with an error with message `'Error: socket hang up'` and code `'ECONNRESET'`, or the error with which `req.destroy()` was called `'close'` If `req.destroy()` is called before the connection succeeds, the following events will be emitted in the following order: `'socket'` (`req.destroy()` called here) `'error'` with an error with message `'Error: socket hang up'` and code `'ECONNRESET'`, or the error with which `req.destroy()` was called `'close'` If `req.destroy()` is called after the response is received, the following events will be emitted in the following order: `'socket'` `'response'` `'data'` any number of times, on the `res` object (`req.destroy()` called here) `'aborted'` on the `res` object `'close'` `'error'` on the `res` object with an error with message `'Error: aborted'` and code `'ECONNRESET'`, or the error with which `req.destroy()` was called `'close'` on the `res` object If `req.abort()` is called before a socket is assigned, the following events will be emitted in the following order: (`req.abort()` called here) `'abort'` `'close'` If `req.abort()` is called before the connection succeeds, the following events will be emitted in the following order: `'socket'` (`req.abort()` called here) `'abort'` `'error'` with an error with message `'Error: socket hang up'` and code `'ECONNRESET'` `'close'` If `req.abort()` is called after the response is received, the following events will be emitted in the following order: `'socket'` `'response'` `'data'` any number of times, on the `res` object (`req.abort()` called here) `'abort'` `'aborted'` on the `res` object `'error'` on the `res` object with an error with message `'Error: aborted'` and code `'ECONNRESET'`. `'close'` `'close'` on the `res` object Setting the `timeout` option or using the `setTimeout()` function will not abort the request or do anything besides add a `'timeout'` event.Passing an `AbortSignal` and then calling `abort()` on the corresponding `AbortController` will behave the same way as calling `.destroy()` on the request. Specifically, the `'error'` event will be emitted with an error with the message `'AbortError: The operation was aborted'`, the code `'ABORT_ERR'` and the `cause`, if one was provided.

### `http.validateHeaderName(name[, label])`

- `name` `<string>`
- `label` `<string>` Label for error message. **Default:** `'Header name'`.

Performs the low-level validations on the provided `name` that are done when `res.setHeader(name, value)` is called.Passing illegal value as `name` will result in a `TypeError` being thrown, identified by `code: 'ERR_INVALID_HTTP_TOKEN'`.It is not necessary to use this method before passing headers to an HTTP request or response. The HTTP module will automatically validate such headers.Example:`import { validateHeaderName } from 'node:http'; try { validateHeaderName(''); } catch (err) { console.error(err instanceof TypeError); // --> true console.error(err.code); // --> 'ERR_INVALID_HTTP_TOKEN' console.error(err.message); // --> 'Header name must be a valid HTTP token [""]' }``const { validateHeaderName } = require('node:http'); try { validateHeaderName(''); } catch (err) { console.error(err instanceof TypeError); // --> true console.error(err.code); // --> 'ERR_INVALID_HTTP_TOKEN' console.error(err.message); // --> 'Header name must be a valid HTTP token [""]' }`

### `http.validateHeaderValue(name, value)`

- `name` `<string>`
- `value` `<any>`

Performs the low-level validations on the provided `value` that are done when `res.setHeader(name, value)` is called.Passing illegal value as `value` will result in a `TypeError` being thrown. Undefined value error is identified by `code: 'ERR_HTTP_INVALID_HEADER_VALUE'`. Invalid value character error is identified by `code: 'ERR_INVALID_CHAR'`. It is not necessary to use this method before passing headers to an HTTP request or response. The HTTP module will automatically validate such headers.Examples:`import { validateHeaderValue } from 'node:http'; try { validateHeaderValue('x-my-header', undefined); } catch (err) { console.error(err instanceof TypeError); // --> true console.error(err.code === 'ERR_HTTP_INVALID_HEADER_VALUE'); // --> true console.error(err.message); // --> 'Invalid value "undefined" for header "x-my-header"' } try { validateHeaderValue('x-my-header', 'oʊmɪɡə'); } catch (err) { console.error(err instanceof TypeError); // --> true console.error(err.code === 'ERR_INVALID_CHAR'); // --> true console.error(err.message); // --> 'Invalid character in header content ["x-my-header"]' }``const { validateHeaderValue } = require('node:http'); try { validateHeaderValue('x-my-header', undefined); } catch (err) { console.error(err instanceof TypeError); // --> true console.error(err.code === 'ERR_HTTP_INVALID_HEADER_VALUE'); // --> true console.error(err.message); // --> 'Invalid value "undefined" for header "x-my-header"' } try { validateHeaderValue('x-my-header', 'oʊmɪɡə'); } catch (err) { console.error(err instanceof TypeError); // --> true console.error(err.code === 'ERR_INVALID_CHAR'); // --> true console.error(err.message); // --> 'Invalid character in header content ["x-my-header"]' }`

### `http.setMaxIdleHTTPParsers(max)`

- `max` `<number>` **Default:** `1000`.

Set the maximum number of idle HTTP parsers.

### `http.setGlobalProxyFromEnv([proxyEnv])`

- `proxyEnv` `<Object>` An object containing proxy configuration. This accepts the same options as the `proxyEnv` option accepted by `Agent`. **Default:** `process.env`.
- Returns: `<Function>` A function that restores the original agent and dispatcher settings to the state before this `http.setGlobalProxyFromEnv()` is invoked.

Dynamically resets the global configurations to enable built-in proxy support for `fetch()` and `http.request()`/`https.request()` at runtime, as an alternative to using the `--use-env-proxy` flag or `NODE_USE_ENV_PROXY` environment variable. It can also be used to override settings configured from the environment variables.As this function resets the global configurations, any previously configured `http.globalAgent`, `https.globalAgent` or undici global dispatcher would be overridden after this function is invoked. It's recommended to invoke it before any requests are made and avoid invoking it in the middle of any requests.See Built-in Proxy Support for details on proxy URL formats and `NO_PROXY` syntax.

### Class: `WebSocket`

A browser-compatible implementation of `<WebSocket>`.

### Built-in Proxy Support

Stability: 1.1 - Active development

When Node.js creates the global agent, if the `NODE_USE_ENV_PROXY` environment variable is set to `1` or `--use-env-proxy` is enabled, the global agent will be constructed with `proxyEnv: process.env`, enabling proxy support based on the environment variables.To enable proxy support dynamically and globally, use `http.setGlobalProxyFromEnv()`.Custom agents can also be created with proxy support by passing a `proxyEnv` option when constructing the agent. The value can be `process.env` if they just want to inherit the configuration from the environment variables, or an object with specific setting overriding the environment.The following properties of the `proxyEnv` are checked to configure proxy support. `HTTP_PROXY` or `http_proxy`: Proxy server URL for HTTP requests. If both are set, `http_proxy` takes precedence. `HTTPS_PROXY` or `https_proxy`: Proxy server URL for HTTPS requests. If both are set, `https_proxy` takes precedence. `NO_PROXY` or `no_proxy`: Comma-separated list of hosts to bypass the proxy. If both are set, `no_proxy` takes precedence. If the request is made to a Unix domain socket, the proxy settings will be ignored.

#### Proxy URL Format

Proxy URLs can use either HTTP or HTTPS protocols: HTTP proxy: `http://proxy.example.com:8080` HTTPS proxy: `https://proxy.example.com:8080` Proxy with authentication: `http://username:password@proxy.example.com:8080`

#### `NO_PROXY` Format

The `NO_PROXY` environment variable supports several formats: `*` - Bypass proxy for all hosts `example.com` - Exact host name match `.example.com` - Domain suffix match (matches `sub.example.com`) `*.example.com` - Wildcard domain match `192.168.1.100` - Exact IP address match `192.168.1.1-192.168.1.100` - IP address range `example.com:8080` - Hostname with specific port Multiple entries should be separated by commas.

#### Example

To start a Node.js process with proxy support enabled for all requests sent through the default global agent, either use the `NODE_USE_ENV_PROXY` environment variable:`NODE_USE_ENV_PROXY=1 HTTP_PROXY=http://proxy.example.com:8080 NO_PROXY=localhost,127.0.0.1 node client.js`Or the `--use-env-proxy` flag.`HTTP_PROXY=http://proxy.example.com:8080 NO_PROXY=localhost,127.0.0.1 node --use-env-proxy client.js`To enable proxy support dynamically and globally with `process.env` (the default option of `http.setGlobalProxyFromEnv()`):`const http = require('node:http'); // Reads proxy-related environment variables from process.env const restore = http.setGlobalProxyFromEnv(); // Subsequent requests will use the configured proxies from environment variables http.get('http://www.example.com', (res) => { // This request will be proxied if HTTP_PROXY or http_proxy is set }); fetch('https://www.example.com', (res) => { // This request will be proxied if HTTPS_PROXY or https_proxy is set }); // To restore the original global agent and dispatcher settings, call the returned function. // restore();``import http from 'node:http'; // Reads proxy-related environment variables from process.env http.setGlobalProxyFromEnv(); // Subsequent requests will use the configured proxies from environment variables http.get('http://www.example.com', (res) => { // This request will be proxied if HTTP_PROXY or http_proxy is set }); fetch('https://www.example.com', (res) => { // This request will be proxied if HTTPS_PROXY or https_proxy is set }); // To restore the original global agent and dispatcher settings, call the returned function. // restore();`To enable proxy support dynamically and globally with custom settings:`const http = require('node:http'); const restore = http.setGlobalProxyFromEnv({ http_proxy: 'http://proxy.example.com:8080', https_proxy: 'https://proxy.example.com:8443', no_proxy: 'localhost,127.0.0.1,.internal.example.com', }); // Subsequent requests will use the configured proxies http.get('http://www.example.com', (res) => { // This request will be proxied through proxy.example.com:8080 }); fetch('https://www.example.com', (res) => { // This request will be proxied through proxy.example.com:8443 });``import http from 'node:http'; http.setGlobalProxyFromEnv({ http_proxy: 'http://proxy.example.com:8080', https_proxy: 'https://proxy.example.com:8443', no_proxy: 'localhost,127.0.0.1,.internal.example.com', }); // Subsequent requests will use the configured proxies http.get('http://www.example.com', (res) => { // This request will be proxied through proxy.example.com:8080 }); fetch('https://www.example.com', (res) => { // This request will be proxied through proxy.example.com:8443 });`To create a custom agent with built-in proxy support:const http = require('node:http'); // Creating a custom agent with custom proxy support. const agent = new http.Agent({ proxyEnv: { HTTP_PROXY: 'http://proxy.example.com:8080' } }); http.request({ hostname: 'www.example.com', port: 80, path: '/', agent, }, (res) => { // This request will be proxied through proxy.example.com:8080 using the HTTP protocol. console.log(`STATUS: ${res.statusCode}`); });Alternatively, the following also works:`const http = require('node:http'); // Use lower-cased option name. const agent1 = new http.Agent({ proxyEnv: { http_proxy: 'http://proxy.example.com:8080' } }); // Use values inherited from the environment variables, if the process is started with // HTTP_PROXY=http://proxy.example.com:8080 this will use the proxy server specified // in process.env.HTTP_PROXY. const agent2 = new http.Agent({ proxyEnv: process.env });`
