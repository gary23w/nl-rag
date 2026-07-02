---
title: "HTTP (part 2/3)"
source: https://nodejs.org/api/http.html
domain: javascript
license: CC-BY-SA-2.5 (MDN) / MIT (Node.js)
tags: javascript, typescript, node.js, nodejs, npm
fetched: 2026-07-02
part: 2/3
---

# HTTP

Boolean (read-only). True if headers were sent, false otherwise.

#### `response.removeHeader(name)`

- `name` `<string>`

Removes a header that's queued for implicit sending.`response.removeHeader('Content-Encoding');`

#### `response.req`

- Type: `<http.IncomingMessage>`

A reference to the original HTTP `request` object.

#### `response.sendDate`

- Type: `<boolean>`

When true, the Date header will be automatically generated and sent in the response if it is not already present in the headers. Defaults to true.

This should only be disabled for testing; the Date header is required in most HTTP responses (see RFC 9110 Section 6.6.1 for details).

#### `response.setHeader(name, value)`

- `name` `<string>`
- `value` `<number>` | `<string>` | `<string>`[]
- Returns: `<http.ServerResponse>`

Returns the response object.

Sets a single header value for implicit headers. If this header already exists in the to-be-sent headers, its value will be replaced. Use an array of strings here to send multiple headers with the same name. Non-string values will be stored without modification. Therefore, `response.getHeader()` may return non-string values. However, the non-string values will be converted to strings for network transmission. The same response object is returned to the caller, to enable call chaining.`response.setHeader('Content-Type', 'text/html');`

or`response.setHeader('Set-Cookie', ['type=ninja', 'language=javascript']);`

Attempting to set a header field name or value that contains invalid characters will result in a `TypeError` being thrown.

When headers have been set with `response.setHeader()`, they will be merged with any headers passed to `response.writeHead()`, with the headers passed to `response.writeHead()` given precedence.`// Returns content-type = text/plain const server = http.createServer((req, res) => { res.setHeader('Content-Type', 'text/html'); res.setHeader('X-Foo', 'bar'); res.writeHead(200, { 'Content-Type': 'text/plain' }); res.end('ok'); });`

If `response.writeHead()` method is called and this method has not been called, it will directly write the supplied header values onto the network channel without caching internally, and the `response.getHeader()` on the header will not yield the expected result. If progressive population of headers is desired with potential future retrieval and modification, use `response.setHeader()` instead of `response.writeHead()`.

#### `response.setTimeout(msecs[, callback])`

- `msecs` `<number>`
- `callback` `<Function>`
- Returns: `<http.ServerResponse>`

Sets the Socket's timeout value to `msecs`. If a callback is provided, then it is added as a listener on the `'timeout'` event on the response object.

If no `'timeout'` listener is added to the request, the response, or the server, then sockets are destroyed when they time out. If a handler is assigned to the request, the response, or the server's `'timeout'` events, timed out sockets must be handled explicitly.

#### `response.socket`

- Type: `<stream.Duplex>`

Reference to the underlying socket. Usually users will not want to access this property. In particular, the socket will not emit `'readable'` events because of how the protocol parser attaches to the socket. After `response.end()`, the property is nulled.import http from 'node:http'; const server = http.createServer((req, res) => { const ip = res.socket.remoteAddress; const port = res.socket.remotePort; res.end(`Your IP address is ${ip} and your source port is ${port}.`); }).listen(3000);const http = require('node:http'); const server = http.createServer((req, res) => { const ip = res.socket.remoteAddress; const port = res.socket.remotePort; res.end(`Your IP address is ${ip} and your source port is ${port}.`); }).listen(3000);

This property is guaranteed to be an instance of the `<net.Socket>` class, a subclass of `<stream.Duplex>`, unless the user specified a socket type other than `<net.Socket>`.

#### `response.statusCode`

- Type: `<number>` **Default:** `200`

When using implicit headers (not calling `response.writeHead()` explicitly), this property controls the status code that will be sent to the client when the headers get flushed.`response.statusCode = 404;`

After response header was sent to the client, this property indicates the status code which was sent out.

#### `response.statusMessage`

- Type: `<string>`

When using implicit headers (not calling `response.writeHead()` explicitly), this property controls the status message that will be sent to the client when the headers get flushed. If this is left as `undefined` then the standard message for the status code will be used.`response.statusMessage = 'Not found';`

After response header was sent to the client, this property indicates the status message which was sent out.

#### `response.strictContentLength`

- Type: `<boolean>` **Default:** `false`

If set to `true`, Node.js will check whether the `Content-Length` header value and the size of the body, in bytes, are equal. Mismatching the `Content-Length` header value will result in an `Error` being thrown, identified by `code:` `'ERR_HTTP_CONTENT_LENGTH_MISMATCH'`.

#### `response.uncork()`

See `writable.uncork()`.

#### `response.writableEnded`

- Type: `<boolean>`

Is `true` after `response.end()` has been called. This property does not indicate whether the data has been flushed, for this use `response.writableFinished` instead.

#### `response.writableFinished`

- Type: `<boolean>`

Is `true` if all data has been flushed to the underlying system, immediately before the `'finish'` event is emitted.

#### `response.write(chunk[, encoding][, callback])`

- `chunk` `<string>` | `<Buffer>` | `<Uint8Array>`
- `encoding` `<string>` **Default:** `'utf8'`
- `callback` `<Function>`
- Returns: `<boolean>`

If this method is called and `response.writeHead()` has not been called, it will switch to implicit header mode and flush the implicit headers.

This sends a chunk of the response body. This method may be called multiple times to provide successive parts of the body.

If `rejectNonStandardBodyWrites` is set to true in `createServer` then writing to the body is not allowed when the request method or response status do not support content. If an attempt is made to write to the body for a HEAD request or as part of a `204` or `304`response, a synchronous `Error` with the code `ERR_HTTP_BODY_NOT_ALLOWED` is thrown.

`chunk` can be a string or a buffer. If `chunk` is a string, the second parameter specifies how to encode it into a byte stream. `callback` will be called when this chunk of data is flushed.

This is the raw HTTP body and has nothing to do with higher-level multi-part body encodings that may be used.

The first time `response.write()` is called, it will send the buffered header information and the first chunk of the body to the client. The second time `response.write()` is called, Node.js assumes data will be streamed, and sends the new data separately. That is, the response is buffered up to the first chunk of the body.

Returns `true` if the entire data was flushed successfully to the kernel buffer. Returns `false` if all or part of the data was queued in user memory. `'drain'` will be emitted when the buffer is free again.

#### `response.writeContinue()`

Sends an HTTP/1.1 100 Continue message to the client, indicating that the request body should be sent. See the `'checkContinue'` event on `Server`.

#### `response.writeEarlyHints(hints[, callback])`

- `hints` `<Object>`
- `callback` `<Function>`

Sends an HTTP/1.1 103 Early Hints message to the client with a Link header, indicating that the user agent can preload/preconnect the linked resources. The `hints` is an object containing the values of headers to be sent with early hints message. The optional `callback` argument will be called when the response message has been written.

**Example**`const earlyHintsLink = '</styles.css>; rel=preload; as=style'; response.writeEarlyHints({ 'link': earlyHintsLink, }); const earlyHintsLinks = [ '</styles.css>; rel=preload; as=style', '</scripts.js>; rel=preload; as=script', ]; response.writeEarlyHints({ 'link': earlyHintsLinks, 'x-trace-id': 'id for diagnostics', }); const earlyHintsCallback = () => console.log('early hints message sent'); response.writeEarlyHints({ 'link': earlyHintsLinks, }, earlyHintsCallback);`

#### `response.writeHead(statusCode[, statusMessage][, headers])`

- `statusCode` `<number>`
- `statusMessage` `<string>`
- `headers` `<Object>` | `<Array>`
- Returns: `<http.ServerResponse>`

Sends a response header to the request. The status code is a 3-digit HTTP status code, like `404`. The last argument, `headers`, are the response headers. Optionally one can give a human-readable `statusMessage` as the second argument.

`headers` may be an `Array` where the keys and values are in the same list. It is *not* a list of tuples. So, the even-numbered offsets are key values, and the odd-numbered offsets are the associated values. The array is in the same format as `request.rawHeaders`.

Returns a reference to the `ServerResponse`, so that calls can be chained.`const body = 'hello world'; response .writeHead(200, { 'Content-Length': Buffer.byteLength(body), 'Content-Type': 'text/plain', }) .end(body);`

This method must only be called once on a message and it must be called before `response.end()` is called.

If `response.write()` or `response.end()` are called before calling this, the implicit/mutable headers will be calculated and call this function.

When headers have been set with `response.setHeader()`, they will be merged with any headers passed to `response.writeHead()`, with the headers passed to `response.writeHead()` given precedence.

If this method is called and `response.setHeader()` has not been called, it will directly write the supplied header values onto the network channel without caching internally, and the `response.getHeader()` on the header will not yield the expected result. If progressive population of headers is desired with potential future retrieval and modification, use `response.setHeader()` instead.`// Returns content-type = text/plain const server = http.createServer((req, res) => { res.setHeader('Content-Type', 'text/html'); res.setHeader('X-Foo', 'bar'); res.writeHead(200, { 'Content-Type': 'text/plain' }); res.end('ok'); });`

`Content-Length` is read in bytes, not characters. Use `Buffer.byteLength()` to determine the length of the body in bytes. Node.js will check whether `Content-Length` and the length of the body which has been transmitted are equal or not.

Attempting to set a header field name or value that contains invalid characters will result in a `TypeError` being thrown.

#### `response.writeInformation(statusCode[, headers][, callback])`

- `statusCode` `<number>` An HTTP 1xx informational status code, between `100` and `199` inclusive, excluding `101` (Switching Protocols) which is only available through the `'upgrade'` event.
- `headers` `<Object>` | `<Array>` An optional set of headers to send with the informational response. Accepts the same shapes as `response.writeHead()`.
- `callback` `<Function>` Optional, called once the message has been written to the socket.

Sends an arbitrary HTTP/1.1 1xx informational response to the client. This is a generic equivalent of `response.writeContinue()`, `response.writeProcessing()` and `response.writeEarlyHints()`, and can be called multiple times before the final response. After the final response headers have been sent (via `response.writeHead()` or an implicit header), calling this method throws `ERR_HTTP_HEADERS_SENT`.

Clients receive these responses via the `'information'` event on `http.ClientRequest`.`response.writeInformation(110, { 'X-Progress': '50%' });`

#### `response.writeProcessing()`

Sends an HTTP/1.1 102 Processing message to the client, indicating that the request body should be sent.

### Class: `http.IncomingMessage`

- Extends: `<stream.Readable>`

An `IncomingMessage` object is created by `http.Server` or `http.ClientRequest` and passed as the first argument to the `'request'` and `'response'` event respectively. It may be used to access response status, headers, and data.

Different from its `socket` value which is a subclass of `<stream.Duplex>`, the `IncomingMessage` itself extends `<stream.Readable>` and is created separately to parse and emit the incoming HTTP headers and payload, as the underlying socket may be reused multiple times in case of keep-alive.

#### Event: `'aborted'`

Stability: 0 - Deprecated. Listen for `'close'` event instead.

Emitted when the request has been aborted.

#### Event: `'close'`

Emitted when the request has been completed.

#### `message.aborted`

Stability: 0 - Deprecated. Check `message.destroyed` from `<stream.Readable>`.

- Type: `<boolean>`

The `message.aborted` property will be `true` if the request has been aborted.

#### `message.complete`

- Type: `<boolean>`

The `message.complete` property will be `true` if a complete HTTP message has been received and successfully parsed.

This property is particularly useful as a means of determining if a client or server fully transmitted a message before a connection was terminated:`const req = http.request({ host: '127.0.0.1', port: 8080, method: 'POST', }, (res) => { res.resume(); res.on('end', () => { if (!res.complete) console.error( 'The connection was terminated while the message was still being sent'); }); });`

#### `message.connection`

Stability: 0 - Deprecated. Use `message.socket`.

Alias for `message.socket`.

#### `message.destroy([error])`

- `error` `<Error>`
- Returns: `<this>`

Calls `destroy()` on the socket that received the `IncomingMessage`. If `error` is provided, an `'error'` event is emitted on the socket and `error` is passed as an argument to any listeners on the event.

#### `message.headers`

- Type: `<Object>`

The request/response headers object.

Key-value pairs of header names and values. Header names are lower-cased.`// Prints something like: // // { 'user-agent': 'curl/7.22.0', // host: '127.0.0.1:8000', // accept: '*/*' } console.log(request.headers);`

Duplicates in raw headers are handled in the following ways, depending on the header name: Duplicates of `age`, `authorization`, `content-length`, `content-type`, `etag`, `expires`, `from`, `host`, `if-modified-since`, `if-unmodified-since`, `last-modified`, `location`, `max-forwards`, `proxy-authorization`, `referer`, `retry-after`, `server`, or `user-agent` are discarded. To allow duplicate values of the headers listed above to be joined, use the option `joinDuplicateHeaders` in `http.request()` and `http.createServer()`. See RFC 9110 Section 5.3 for more information. `set-cookie` is always an array. Duplicates are added to the array. For duplicate `cookie` headers, the values are joined together with `;`. For all other headers, the values are joined together with `,`.

#### `message.headersDistinct`

- Type: `<Object>`

Similar to `message.headers`, but there is no join logic and the values are always arrays of strings, even for headers received just once.`// Prints something like: // // { 'user-agent': ['curl/7.22.0'], // host: ['127.0.0.1:8000'], // accept: ['*/*'] } console.log(request.headersDistinct);`

#### `message.httpVersion`

- Type: `<string>`

In case of server request, the HTTP version sent by the client. In the case of client response, the HTTP version of the connected-to server. Probably either `'1.1'` or `'1.0'`.

Also `message.httpVersionMajor` is the first integer and `message.httpVersionMinor` is the second.

#### `message.method`

- Type: `<string>`

**Only valid for request obtained from `http.Server`.**

The request method as a string. Read only. Examples: `'GET'`, `'DELETE'`.

#### `message.rawHeaders`

- Type: `<string>`[]

The raw request/response headers list exactly as they were received.

The keys and values are in the same list. It is *not* a list of tuples. So, the even-numbered offsets are key values, and the odd-numbered offsets are the associated values.

Header names are not lowercased, and duplicates are not merged.`// Prints something like: // // [ 'user-agent', // 'this is invalid because there can be only one', // 'User-Agent', // 'curl/7.22.0', // 'Host', // '127.0.0.1:8000', // 'ACCEPT', // '*/*' ] console.log(request.rawHeaders);`

#### `message.rawTrailers`

- Type: `<string>`[]

The raw request/response trailer keys and values exactly as they were received. Only populated at the `'end'` event.

#### `message.setTimeout(msecs[, callback])`

- `msecs` `<number>`
- `callback` `<Function>`
- Returns: `<http.IncomingMessage>`

Calls `message.socket.setTimeout(msecs, callback)`.

#### `message.signal`

- Type: `<AbortSignal>`

An `<AbortSignal>` that is aborted when the underlying socket closes or the request is destroyed. The signal is created lazily on first access — no `<AbortController>` is allocated for requests that never use this property.

This is useful for cancelling downstream asynchronous work such as database queries or `fetch` calls when a client disconnects mid-request.`import http from 'node:http'; http.createServer(async (req, res) => { try { const data = await fetch('https://example.com/api', { signal: req.signal }); res.end(JSON.stringify(await data.json())); } catch (err) { if (err.name === 'AbortError') return; res.statusCode = 500; res.end('Internal Server Error'); } }).listen(3000);``const http = require('node:http'); http.createServer(async (req, res) => { try { const data = await fetch('https://example.com/api', { signal: req.signal }); res.end(JSON.stringify(await data.json())); } catch (err) { if (err.name === 'AbortError') return; res.statusCode = 500; res.end('Internal Server Error'); } }).listen(3000);`

#### `message.socket`

- Type: `<stream.Duplex>`

The `net.Socket` object associated with the connection.

With HTTPS support, use `request.socket.getPeerCertificate()` to obtain the client's authentication details.

This property is guaranteed to be an instance of the `<net.Socket>` class, a subclass of `<stream.Duplex>`, unless the user specified a socket type other than `<net.Socket>` or internally nulled.

#### `message.statusCode`

- Type: `<number>`

**Only valid for response obtained from `http.ClientRequest`.**

The 3-digit HTTP response status code. E.G. `404`.

#### `message.statusMessage`

- Type: `<string>`

**Only valid for response obtained from `http.ClientRequest`.**

The HTTP response status message (reason phrase). E.G. `OK` or `Internal Server Error`.

#### `message.trailers`

- Type: `<Object>`

The request/response trailers object. Only populated at the `'end'` event.

#### `message.trailersDistinct`

- Type: `<Object>`

Similar to `message.trailers`, but there is no join logic and the values are always arrays of strings, even for headers received just once. Only populated at the `'end'` event.

#### `message.url`

- Type: `<string>`

**Only valid for request obtained from `http.Server`.**

Request URL string. This contains only the URL that is present in the actual HTTP request. Take the following request:`GET /status?name=ryan HTTP/1.1 Accept: text/plain`

To parse the URL into its parts:new URL(`http://${process.env.HOST ?? 'localhost'}${request.url}`);

When `request.url` is `'/status?name=ryan'` and `process.env.HOST` is undefined:$ node > new URL(`http://${process.env.HOST ?? 'localhost'}${request.url}`); URL { href: 'http://localhost/status?name=ryan', origin: 'http://localhost', protocol: 'http:', username: '', password: '', host: 'localhost', hostname: 'localhost', port: '', pathname: '/status', search: '?name=ryan', searchParams: URLSearchParams { 'name' => 'ryan' }, hash: '' }

Ensure that you set `process.env.HOST` to the server's host name, or consider replacing this part entirely. If using `req.headers.host`, ensure proper validation is used, as clients may specify a custom `Host` header.

### Class: `http.OutgoingMessage`

- Extends: `<Stream>`

This class serves as the parent class of `http.ClientRequest` and `http.ServerResponse`. It is an abstract outgoing message from the perspective of the participants of an HTTP transaction.

#### Event: `'drain'`

Emitted when the buffer of the message is free again.

#### Event: `'finish'`

Emitted when the transmission is finished successfully.

#### Event: `'prefinish'`

Emitted after `outgoingMessage.end()` is called. When the event is emitted, all data has been processed but not necessarily completely flushed.

#### `outgoingMessage.addTrailers(headers)`

- `headers` `<Object>`

Adds HTTP trailers (headers but at the end of the message) to the message.

Trailers will **only** be emitted if the message is chunked encoded. If not, the trailers will be silently discarded.

HTTP requires the `Trailer` header to be sent to emit trailers, with a list of header field names in its value, e.g.`message.writeHead(200, { 'Content-Type': 'text/plain', 'Trailer': 'Content-MD5' }); message.write(fileData); message.addTrailers({ 'Content-MD5': '7895bf4b8828b55ceaf47747b4bca667' }); message.end();`

Attempting to set a header field name or value that contains invalid characters will result in a `TypeError` being thrown.

#### `outgoingMessage.appendHeader(name, value)`
