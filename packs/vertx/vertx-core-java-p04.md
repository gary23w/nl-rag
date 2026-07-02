---
title: "Vert.x Core (part 4/8)"
source: https://vertx.io/docs/vertx-core/java/
domain: vertx
license: CC-BY-SA-4.0
tags: vert.x toolkit, eclipse vertx, reactive toolkit, event loop server
fetched: 2026-07-02
part: 4/8
---

## Writing HTTP servers and clients

Vert.x allows you to easily write non-blocking HTTP clients and servers.

Vert.x supports the HTTP/1.0, HTTP/1.1, HTTP/2 and HTTP/3 protocols.

The base API for HTTP is the same for HTTP/1.x, HTTP/2 and HTTP/3, specific API features are available for dealing with the protocol peculiarities.

### Creating an HTTP Server

The simplest way to create an HTTP server, using default config is as follows:

```
HttpServer server = vertx.createHttpServer();
```

By default, the server supports HTTP/1, HTTP/2 in plain text and WebSocket

### Configuring an HTTP server

If you don’t want the default, a server can be configured by passing in a `HttpServerConfig` instance when creating it:

```
HttpServerConfig config = new HttpServerConfig()
  .setVersions(HttpVersion.HTTP_1_1)
  .setFormDecoderConfig(new FormDecoderConfig()
    .setMaxFields(512))
  .setHttp1Config(new Http1ServerConfig()
    .setMaxInitialLineLength(1024))
  .setCompressionConfig(new CompressionConfig()
    .setCompressionEnabled(true)
    .addGzip());

HttpServer server = vertx.createHttpServer(config);
```

Configuration addresses the following parts:

- Accepted versions
- Timeouts and limits
- HTTP/1.x specific configuration
- HTTP/2 specific configuration
- HTTP/3 specific configuration
- WebSocket
- TLS
- Transport: TCP and QUIC
- Content compression
- Observability
- Network logging

### Configuring an HTTPS server

Vert.x HTTP servers can be configured to use HTTPS in exactly the same way as TCP or QUIC servers.

```
ServerSSLOptions sslOptions = new ServerSSLOptions()
  .setKeyCertOptions(
    new JksOptions().
      setPath("/path/to/your/server-keystore.jks").
      setPassword("password-of-your-keystore")
  );

HttpServer server = vertx.createHttpServer(sslOptions);
```

|   | there is no ssl setting on `HttpServerConfig` like there used to be on `HttpServerOptions`, providing ssl options when creating a server indicates the server uses TLS. |
|---|---|

You can read more about SSL server configuration

### Configuring an HTTP/1.x server

Vert.x supports HTTP/1.1 and HTTP/1.0 over plaintext and TLS.

```
HttpServerConfig config = new HttpServerConfig()
  .setHttp1Config(new Http1ServerConfig()
    .setMaxInitialLineLength(1024));
```

`Http1ServerConfig` captures the configuration of HTTP/1.x specific aspects.

### Configuring an HTTP/2 server

Vert.x supports HTTP/2 over TLS `h2` and over TCP `h2c`.

- `h2` identifies the HTTP/2 protocol when used over TLS
- `h2c` identifies the HTTP/2 protocol when using in clear text over TCP, such connections are established either with an HTTP/1.1 upgraded request or directly

To handle `h2` requests, TLS must be enabled:

```
HttpServerConfig config = new HttpServerConfig()
  .setHttp2Config(new Http2ServerConfig()
    .setInitialSettings(new Http2Settings()
      .setMaxConcurrentStreams(250)));
```

The rise of quantum computers will make key exchange protocols such as x25519 obsolete as they will be able to "crack" secret keys quickly. Vert.x proposes a quantum-safe key exchange protocol, x25519MLKEM768 (official recommendation of NIST) to ensure sessions over TLS are safe against quantum computers.

Hybrid key exchange must be enabled with `setUseHybridKeyExchangeProtocol` and **requires OpenSSL** — it does not work with the JDK SSL engine. You must configure `OpenSSLEngineOptions` and add the following dependencies:

- `io.netty:netty-tcnative-classes` (version managed by the Netty BOM)
- An OpenSSL provider such as `io.smallrye:smallrye-openssl`

If OpenSSL is not available at runtime, the TLS handshake will fail rather than silently falling back to a non-quantum-safe key exchange.

With plain text (TLS is disabled), the server handles `h2c` requests that wants to upgrade connections presenting an HTTP/1.1 upgrade request to HTTP/2. It also accepts direct `h2c` (with prior knowledge) connections beginning with the `PRI * HTTP/2.0\r\nSM\r\n` preface.

|   | browsers do not support `h2c`, for serving websites you should use `h2` and not `h2c`. |
|---|---|

`Http2ServerConfig` captures the configuration of HTTP/2 specific aspects.

When a server accepts an HTTP/2 connection, it sends to the client its `initial settings`. These settings define how the client can use the connection, the default initial settings for a server are:

- `getMaxConcurrentStreams`: `100` as recommended by the HTTP/2 RFC
- the default HTTP/2 settings values for the remaining settings

### Configuring an HTTP/3 server

Vert.x supports HTTP/3 over QUIC, we recommend reading the QUIC server section.

QUIC is new transport layer for HTTP that replaces TCP and has TLS built-in, in fact TLS is mandatory.

The implementation of QUIC relies on Netty and QUICHE, a savoury implementation of QUIC which requires native dependencies depending on OS/platform selection, you can learn more about running native QUIC.

```
HttpServerConfig config = new HttpServerConfig()
  .setVersions(HttpVersion.HTTP_3);
```

`Http3ServerConfig` captures the configuration of HTTP/3 specific aspects.

QUIC implements some of the features of HTTP/2, such as the maximum number of concurrent streams a connection can handle:

```
HttpServerConfig config = new HttpServerConfig()
  .setVersions(HttpVersion.HTTP_3);

QuicServerConfig quicConfig = config.getQuicConfig();
quicConfig.setTransportConfig(new QuicConfig()
  .setInitialMaxStreamsBidi(250));
```

QUIC servers can be subject to amplification attacks.

By default, a server is configured with a basic token validation which works well for development purpose, we recommend configuring token validation based on cryptography instead.

### Hybrid HTTP server

A server can handle both TCP (HTTP/1.x and HTTP/2) and QUIC (HTTP/3).

```
HttpServerConfig config = new HttpServerConfig()
  .setVersions(HttpVersion.HTTP_1_1, HttpVersion.HTTP_2, HttpVersion.HTTP_3);

ServerSSLOptions sslOptions = new ServerSSLOptions()
  .setKeyCertOptions(new JksOptions().setPath("/path/to/my/keystore"));

HttpServer server = vertx.createHttpServer(config, sslOptions);
```

Hybrid servers bind two ports

- a TCP port serving HTTP/1.x and/or HTTP/2 traffic
- a QUIC port (UDP) serving HTTP/3 traffic

Each port can be configured independently

```
HttpServerConfig config = new HttpServerConfig()
  .setVersions(HttpVersion.HTTP_1_1, HttpVersion.HTTP_2, HttpVersion.HTTP_3)
  .setTcpPort(tcpPort)
  .setQuicPort(quicPort);
```

Or can be the same (TCP and UDP ports are distinct)

```
HttpServerConfig config = new HttpServerConfig()
  .setVersions(HttpVersion.HTTP_1_1, HttpVersion.HTTP_2, HttpVersion.HTTP_3)
  .setPort(port);
```

Unless DNS configuration relies on HTTPS resource records to the HTTP/3 endpoint, the recommended way an HTTP server can advertise an HTTP/3 endpoint is to emit an HTTP Alternative Services notification.

```
response.writeAltSvc("h3=\":443\"");
```

Calling `writeAltSvc` writes

- an HTTP header for HTTP/1.1 requests
- a custom frame for HTTP/2 requests

### Advanced HTTP server creation

You can pass configuration to `createHttpServer` methods to configure an HTTP server.

Alternatively you can build a server with the builder `API` :

```
HttpServer server = vertx
  .httpServerBuilder()
  .with(config)
  .build();
```

In addition to `HttpServerConfig` and `ServerSSLOptions`, you can set

- a connection event handler notified when a client connects to this server
- `SSLEngineOptions` to configure the SSL engine

### Start the Server Listening

To tell the server to listen for incoming requests you use one of the `listen` alternatives.

To tell the server to listen at the host and port as specified in the configuration:

```
HttpServer server = vertx.createHttpServer();
server.listen();
```

Or to specify the host and port in the call to listen, ignoring what is configured in the configuration:

```
HttpServer server = vertx.createHttpServer();
server.listen(8080, "myhost.com");
```

The default host is `0.0.0.0` which means 'listen on all available addresses' and the default port is `80`.

The actual bind is asynchronous so the server might not actually be listening until some time **after** the call to listen has returned.

If you want to be notified when the server is actually listening you can provide a handler to the `listen` call. For example:

```
HttpServer server = vertx.createHttpServer();
server
  .listen(8080, "myhost.com")
  .onComplete(res -> {
    if (res.succeeded()) {
      System.out.println("Server is now listening!");
    } else {
      System.out.println("Failed to bind!");
    }
  });
```

### Listening to Unix domain sockets

When running on JDK 16+, or using a native transport, a server can listen to Unix domain sockets:

```
HttpServer httpServer = vertx.createHttpServer();

// Only available when running on JDK16+, or using a native transport
SocketAddress address = SocketAddress.domainSocketAddress("/var/tmp/myservice.sock");

httpServer
  .requestHandler(req -> {
    // Handle application
  })
  .listen(address)
  .onComplete(ar -> {
    if (ar.succeeded()) {
      // Bound to socket
    } else {
      // Handle failure
    }
  });
```

### Getting notified of incoming requests

To be notified when a request arrives you need to set a `requestHandler`:

```
HttpServer server = vertx.createHttpServer();
server.requestHandler(request -> {
  // Handle the request in here
});
```

### Handling requests

When a request arrives, the request handler is called passing in an instance of `HttpServerRequest`. This object represents the server side HTTP request.

The handler is called when the headers of the request have been fully read.

If the request contains a body, that body will arrive at the server some time after the request handler has been called.

The server request object allows you to retrieve the `uri`, `path`, `params` and `headers`, amongst other things.

Each server request object is associated with one server response object. You use `response` to get a reference to the `HttpServerResponse` object.

Here’s a simple example of a server handling a request and replying with "hello world" to it.

```
vertx
  .createHttpServer()
  .requestHandler(request -> {
    request.response().end("Hello world");
  })
  .listen(8080);
```

#### Request version

The version of HTTP specified in the request can be retrieved with `version`

#### Request method

Use `method` to retrieve the HTTP method of the request. (i.e. whether it’s GET, POST, PUT, DELETE, HEAD, OPTIONS, etc).

#### Request URI

Use `uri` to retrieve the URI of the request.

Note that this is the actual URI as passed in the HTTP request, and it’s almost always a relative URI.

The URI is as defined in Section 5.1.2 of the HTTP specification - Request-URI

#### Request path

Use `path` to return the path part of the URI

For example, if the request URI was `a/b/c/page.html?param1=abc&param2=xyz

Then the path would be `/a/b/c/page.html`

#### Request query string

Use `query` to return the query string part of the URI

For example, if the request URI was `a/b/c/page.html?param1=abc&param2=xyz`

Then the query would be `param1=abc&param2=xyz`

#### Request headers

Use `headers` to return the headers of the HTTP request.

This returns an instance of `MultiMap` - which is like a normal Map or Hash but allows multiple values for the same key - this is because HTTP allows multiple header values with the same key.

It also has case-insensitive keys, that means you can do the following:

```
MultiMap headers = request.headers();

// Get the User-Agent:
System.out.println("User agent is " + headers.get("user-agent"));

// You can also do this and get the same result:
System.out.println("User agent is " + headers.get("User-Agent"));
```

#### Request authority

Use `authority` to return the authority of the HTTP request.

For HTTP/1.x requests the `host` header is returned, for HTTP/2 and HTTP/3 requests the `:authority` pseudo header is returned.

#### Request parameters

Use `params` to return the parameters of the HTTP request.

Just like `headers` this returns an instance of `MultiMap` as there can be more than one parameter with the same name.

Request parameters are sent on the request URI, after the path. For example if the URI was `/page.html?param1=abc&param2=xyz`

Then the parameters would contain the following:

```
param1: 'abc'
param2: 'xyz
```

Note that these request parameters are retrieved from the URL of the request. If you have form attributes that have been sent as part of the submission of an HTML form submitted in the body of a `multi-part/form-data` request then they will not appear in the params here.

#### Remote address

The address of the sender of the request can be retrieved with `remoteAddress`.

#### Absolute URI

The URI passed in an HTTP request is usually relative. If you wish to retrieve the absolute URI corresponding to the request, you can get it with `absoluteURI`

#### End handler

The `endHandler` of the request is invoked when the entire request, including any body has been fully read.

#### Reading Data from the Request Body

Often an HTTP request contains a body that we want to read. As previously mentioned the request handler is called when just the headers of the request have arrived so the request object does not have a body at that point.

This is because the body may be very large (e.g. a file upload) and we don’t generally want to buffer the entire body in memory before handing it to you, as that could cause the server to exhaust available memory.

To receive the body, you can use the `handler` on the request, this will get called every time a chunk of the request body arrives. Here’s an example:

```
request.handler(buffer -> {
  System.out.println("I have received a chunk of the body of length " + buffer.length());
});
```

The object passed into the handler is a `Buffer`, and the handler can be called multiple times as data arrives from the network, depending on the size of the body.

In some cases (e.g. if the body is small) you will want to aggregate the entire body in memory, so you could do the aggregation yourself as follows:

```
Buffer totalBuffer = Buffer.buffer();

request.handler(buffer -> {
  System.out.println("I have received a chunk of the body of length " + buffer.length());
  totalBuffer.appendBuffer(buffer);
});

request.endHandler(v -> {
  System.out.println("Full body received, length = " + totalBuffer.length());
});
```

This is such a common case, that Vert.x provides a `bodyHandler` to do this for you. The body handler is called once when all the body has been received:

```
request.bodyHandler(totalBuffer -> {
  System.out.println("Full body received, length = " + totalBuffer.length());
});
```

#### Streaming requests

The request object is a `ReadStream` so you can pipe the request body to any `WriteStream` instance.

See the chapter on streams for a detailed explanation.

#### Handling HTML forms

HTML forms can be submitted with either a content type of `application/x-www-form-urlencoded` or `multipart/form-data`.

For url encoded forms, the form attributes are encoded in the url, just like normal query parameters.

For multi-part forms they are encoded in the request body, and as such are not available until the entire body has been read from the wire.

Multi-part forms can also contain file uploads.

If you want to retrieve the attributes of a multi-part form you should tell Vert.x that you expect to receive such a form **before** any of the body is read by calling `setExpectMultipart` with `true`, and then you should retrieve the actual attributes using `formAttributes` once the entire body has been read:

```
server.requestHandler(request -> {
  request.setExpectMultipart(true);
  request.endHandler(v -> {
    // The body has now been fully read, so retrieve the form attributes
    MultiMap formAttributes = request.formAttributes();
  });
});
```

Form attributes have a maximum size of `8192` bytes. When the client submits a form with an attribute size greater than this value, the file upload triggers an exception on `HttpServerRequest` exception handler. You can set a different maximum size with `setMaxAttributeSize`.

```
HttpServerConfig config = new HttpServerConfig()
  .setFormDecoderConfig(
    new FormDecoderConfig().setMaxAttributeSize(maxAttrSize));
```

#### Handling form file uploads

Vert.x can also handle file uploads which are encoded in a multi-part request body.

To receive file uploads you tell Vert.x to expect a multi-part form and set an `uploadHandler` on the request.

This handler will be called once for every upload that arrives on the server.

The object passed into the handler is a `HttpServerFileUpload` instance.

```
server.requestHandler(request -> {
  request.setExpectMultipart(true);
  request.uploadHandler(upload -> {
    System.out.println("Processing a file upload " + upload.name());
  });
});
```

File uploads can be large we don’t provide the entire upload in a single buffer as that might result in memory exhaustion, instead, the upload data is received in chunks:

```
request.uploadHandler(upload -> {
  upload.handler(chunk -> {
    System.out.println("Received a chunk of the upload of length " + chunk.length());
  });
});
```

The upload object is a `ReadStream` so you can pipe the request body to any `WriteStream` instance. See the chapter on streams for a detailed explanation.

If you just want to upload the file to disk somewhere you can use `streamToFileSystem`:

```
request.uploadHandler(upload -> {
  upload.streamToFileSystem("myuploads_directory/" + upload.filename());
});
```

|   | Make sure you check the filename in a production system to avoid malicious clients uploading files to arbitrary places on your filesystem. See security notes for more information. |
|---|---|

#### Handling cookies

You use `getCookie` to retrieve a cookie by name, or use `cookies` to retrieve all the cookies.

To remove a cookie, use `removeCookie`.

To add a cookie use `addCookie`.

The set of cookies will be written back in the response automatically when the response headers are written so the browser can store them.

Cookies are described by instances of `Cookie`. This allows you to retrieve the name, value, domain, path and other normal cookie properties.

Same Site Cookies let servers require that a cookie shouldn’t be sent with cross-site (where Site is defined by the registrable domain) requests, which provides some protection against cross-site request forgery attacks. This kind of cookies are enabled using the setter: `setSameSite`.

Same site cookies can have one of 3 values:

- None - The browser will send cookies with both cross-site requests and same-site requests.
- Strict - The browser will only send cookies for same-site requests (requests originating from the site that set the cookie). If the request originated from a different URL than the URL of the current location, none of the cookies tagged with the Strict attribute will be included.
- Lax - Same-site cookies are withheld on cross-site subrequests, such as calls to load images or frames, but will be sent when a user navigates to the URL from an external site; for example, by following a link.

Here’s an example of querying and adding cookies:

```
Cookie someCookie = request.getCookie("mycookie");
String cookieValue = someCookie.getValue();

// Do something with cookie...

// Add a cookie - this will get written back in the response automatically
request.response().addCookie(Cookie.cookie("othercookie", "somevalue"));
```

#### Handling compressed body

Vert.x can handle compressed body payloads which are encoded by the client with the *deflate*, *gzip*, *snappy* or *brotli* algorithms.

To enable decompression set `setDecompressionEnabled` on the compression configuration when creating the server.

Snappy is supported without external dependencies.

You need to have Brotli4j on the classpath to decompress Brotli, and Zstd-jni for Zstandard:

- Maven (in your `pom.xml`):

```
<dependency>
  <groupId>com.aayushatharva.brotli4j</groupId>
  <artifactId>brotli4j</artifactId>
  <version>${brotli4j.version}</version>
</dependency>
<dependency>
  <groupId>com.github.luben</groupId>
  <artifactId>zstd-jni</artifactId>
  <version>${zstd-jini.version}</version>
</dependency>
```

- Gradle (in your `build.gradle` file):

```
dependencies {
  implementation 'com.aayushatharva.brotli4j:brotli4j:${brotli4j.version}'
  runtimeOnly 'com.aayushatharva.brotli4j:native-$system-and-arch:${brotli4j.version}'
  implementation 'com.github.luben:zstd-jni:${zstd-jini.version}'
}
```

When using Gradle, you need to add the runtime native library manually depending on your OS and architecture. See the Gradle section of Brotli4j for more details.

By default, decompression is disabled.

#### Receiving custom frames

HTTP/2 and HTTP/3 are framed protocol with various frames for the HTTP request/response model. The protocol allows other kind of frames to be sent or received.

To receive custom frames, you can use the `customFrameHandler` on the request, this will get called every time a custom frame arrives. Here’s an example:

```
request.customFrameHandler(frame -> {

  System.out.println("Received a frame type=" + frame.type() +
    " payload" + frame.payload().toString());
});
```

Custom frames are not subject to flow control - the frame handler will be called immediately when a custom frame is received independently of the streaming state.

### Sending back responses

The server response object is an instance of `HttpServerResponse` and is obtained from the request with `response`.

You use the response object to write a response back to the HTTP client.

#### Setting status code and message

The default HTTP status code for a response is `200`, representing `OK`.

Use `setStatusCode` to set a different code.

You can also specify a custom status message with `setStatusMessage`.

If you don’t specify a status message, the default one corresponding to the status code will be used.

|   | for HTTP/2 the status won’t be present in the response since the protocol won’t transmit the message to the client |
|---|---|

#### Writing HTTP responses

To write data to an HTTP response, you use one of the `write` operations.

These can be invoked multiple times before the response is ended. They can be invoked in a few ways:

With a single buffer:

```
HttpServerResponse response = request.response();
response.write(buffer);
```

With a string. In this case the string will encoded using UTF-8 and the result written to the wire.

```
HttpServerResponse response = request.response();
response.write("hello world!");
```

With a string and an encoding. In this case the string will encoded using the specified encoding and the result written to the wire.

```
HttpServerResponse response = request.response();
response.write("hello world!", "UTF-16");
```

Writing to a response is asynchronous and always returns immediately after write has been queued.

If you are just writing a single string or buffer to the HTTP response you can write it and end the response in a single call to the `end`

The first call to write results in the response header being written to the response. Consequently, if you are not using HTTP chunking then you must set the `Content-Length` header before writing to the response, since it will be too late otherwise. If you are using HTTP chunking you do not have to worry.

#### Ending HTTP responses

Once you have finished with the HTTP response you should `end` it.

This can be done in several ways:

With no arguments, the response is simply ended.

```
HttpServerResponse response = request.response();
response.write("hello world!");
response.end();
```

It can also be called with a string or buffer in the same way `write` is called. In this case it’s just the same as calling write with a string or buffer followed by calling end with no arguments. For example:

```
HttpServerResponse response = request.response();
response.end("hello world!");
```

#### Setting response headers

HTTP response headers can be added to the response by adding them directly to the `headers`:

```
HttpServerResponse response = request.response();
MultiMap headers = response.headers();
headers.set("content-type", "text/html");
headers.set("other-header", "wibble");
```

Or you can use `putHeader`

```
HttpServerResponse response = request.response();
response.putHeader("content-type", "text/html").putHeader("other-header", "wibble");
```

Headers must all be added before any parts of the response body are written.

#### Chunked HTTP responses and trailers

Vert.x supports HTTP Chunked Transfer Encoding.

This allows the HTTP response body to be written in chunks, and is normally used when a large response body is being streamed to a client and the total size is not known in advance.

You put the HTTP response into chunked mode as follows:

```
HttpServerResponse response = request.response();
response.setChunked(true);
```

Default is non-chunked. When in chunked mode, each call to one of the `write` methods will result in a new HTTP chunk being written out.

When in chunked mode you can also write HTTP response trailers to the response. These are actually written in the final chunk of the response.

|   | chunked response has no effect for an HTTP/2 or HTTP/3 stream |
|---|---|

To add trailers to the response, add them directly to the `trailers`.

```
HttpServerResponse response = request.response();
response.setChunked(true);
MultiMap trailers = response.trailers();
trailers.set("X-wibble", "woobble").set("X-quux", "flooble");
```

Or use `putTrailer`.

```
HttpServerResponse response = request.response();
response.setChunked(true);
response
  .putTrailer("X-wibble", "woobble")
  .putTrailer("X-quux", "flooble");
```

#### Serving files directly from disk or the classpath

If you were writing a web server, one way to serve a file from disk would be to open it as an `AsyncFile` and pipe it to the HTTP response.

Or you could load it in one go using `readFile` and write it straight to the response.

Alternatively, Vert.x provides a method which allows you to serve a file from disk or the filesystem to an HTTP response in one operation. Where supported by the underlying operating system this may result in the OS directly transferring bytes from the file to the socket without being copied through user-space at all.

This is done by using `sendFile`, and is usually more efficient for large files, but may be slower for small files.

Here’s a very simple web server that serves files from the file system using sendFile:

```
vertx.createHttpServer().requestHandler(request -> {
  String file = "";
  if (request.path().equals("/")) {
    file = "index.html";
  } else if (!request.path().contains("..")) {
    file = request.path();
  }
  request.response().sendFile("web/" + file);
}).listen(8080);
```

The HTTP response uses the file name extension to set the HTTP response content type header when the file name extension is well known by `MimeMapping` (lookup is case-insensitive).

Sending a file is asynchronous and may not complete until some time after the call has returned. If you want to be notified when the file has been written you can use `sendFile`.

Please see the chapter about serving files from the classpath for restrictions about the classpath resolution or disabling it.

|   | If you use `sendFile` while using HTTPS it will copy through user-space, since if the kernel is copying data directly from disk to socket it doesn’t give us an opportunity to apply any encryption. |
|---|---|

|   | If you’re going to write web servers directly using Vert.x be careful that users cannot exploit the path to access files outside the directory from which you want to serve them or the classpath It may be safer instead to use Vert.x Web. |
|---|---|

When there is a need to serve just a segment of a file, say starting from a given byte, you can achieve this by doing:

```
vertx.createHttpServer().requestHandler(request -> {
  long offset = 0;
  try {
    offset = Long.parseLong(request.getParam("start"));
  } catch (NumberFormatException e) {
    // error handling...
  }

  long end = Long.MAX_VALUE;
  try {
    end = Long.parseLong(request.getParam("end"));
  } catch (NumberFormatException e) {
    // error handling...
  }

  request.response().sendFile("web/mybigfile.txt", offset, end);
}).listen(8080);
```

You are not required to supply the length if you want to send a file starting from an offset until the end, in this case you can just do:

```
vertx.createHttpServer().requestHandler(request -> {
  long offset = 0;
  try {
    offset = Long.parseLong(request.getParam("start"));
  } catch (NumberFormatException e) {
    // error handling...
  }

  request.response().sendFile("web/mybigfile.txt", offset);
}).listen(8080);
```

#### Piping responses

The server response is a `WriteStream` so you can pipe to it from any `ReadStream`, e.g. `AsyncFile`, `NetSocket`, `WebSocket` or `HttpServerRequest`.

Here’s an example which echoes the request body back in the response for any PUT methods. It uses a pipe for the body, so it will work even if the HTTP request body is much larger than can fit in memory at any one time:

```
vertx.createHttpServer().requestHandler(request -> {
  HttpServerResponse response = request.response();
  if (request.method() == HttpMethod.PUT) {
    response.setChunked(true);
    request.pipeTo(response);
  } else {
    response.setStatusCode(400).end();
  }
}).listen(8080);
```

You can also use the `send` method to send a `ReadStream`.

Sending a stream is a pipe operation, however as this is a method of `HttpServerResponse`, it will also take care of chunking the response when the `content-length` is not set.

```
vertx.createHttpServer().requestHandler(request -> {
  HttpServerResponse response = request.response();
  if (request.method() == HttpMethod.PUT) {
    response.send(request);
  } else {
    response.setStatusCode(400).end();
  }
}).listen(8080);
```

#### Sending custom frames

HTTP/2 and HTTP/3 are framed protocol with various frames for the HTTP request/response model. The protocol allows other kind of frames to be sent or received.

To send such frames, you can use the `writeCustomFrame` on the response. Here’s an example:

```
int frameType = 40;
int frameStatus = 10;
Buffer payload = Buffer.buffer("some data");

// Sending a frame to the client
response.writeCustomFrame(frameType, frameStatus, payload);
```

These frames are sent immediately and are not subject to flow control - when such frame is sent there it may be done before other data frames.

#### Stream cancellation

`cancel` is a best effort to cancel a stream by the underlying HTTP protocol.

- HTTP/1.x does not allow a clean cancellation of a request or a response stream, for example when a client uploads a resource already present on the server, the server needs to accept the entire response: the implementation closes the connection when the current request is inflight.
- HTTP/2 supports stream reset at any time during the request/response: the implementation sends an HTTP/2 reset frame with the error `0x08`
- HTTP/3 relies on QUIC capabilities: the implementation performs a QUIC reset or abort reading with the code `0x10c`

```
request.response().cancel();
```

The request handler are notified of stream reset events with the `request handler` and `response handler`:

```
request.response().exceptionHandler(err -> {
  if (err instanceof StreamResetException) {
    StreamResetException reset = (StreamResetException) err;
    System.out.println("Stream reset " + reset.getCode());
  }
});
```

|   | stream reset should be avoided because the implementation works partially for HTTP/3 and reset error codes depends on the version of the protocol. |
|---|---|

#### Handling exceptions

You can set an `exceptionHandler` to receive any exceptions that happens before the connection is passed to the `requestHandler` or to the `webSocketHandler`, e.g. during the TLS handshake.

#### Handling invalid requests

Vert.x will handle invalid HTTP requests and provides a default handler that will handle the common case appropriately, e.g. it does respond with `REQUEST_HEADER_FIELDS_TOO_LARGE` when a request header is too long.

You can set your own `invalidRequestHandler` to process invalid requests. Your implementation can handle specific cases and delegate other cases to to `HttpServerRequest.DEFAULT_INVALID_REQUEST_HANDLER`.

### HTTP Compression

Vert.x comes with support for HTTP Compression out of the box.

This means you are able to automatically compress the body of the responses before they are sent back to the client.

If the client does not support HTTP compression the responses are sent back without compressing the body.

This allows to handle Client that support HTTP Compression and those that not support it at the same time.

To enable compression use can configure it with `setCompressionEnabled`.

By default, compression is not enabled.

When HTTP compression is enabled the server will check if the client includes an `Accept-Encoding` header which includes the supported compressions. Commonly used are deflate and gzip. Both are supported by Vert.x.

If such a header is found the server will automatically compress the body of the response with one of the supported compressions and send it back to the client.

Whenever the response needs to be sent without compression you can set the header `content-encoding` to `identity`:

```
request.response()
  .putHeader(HttpHeaders.CONTENT_ENCODING, HttpHeaders.IDENTITY)
  .sendFile("/path/to/image.jpg");
```

Be aware that compression may be able to reduce network traffic but is more CPU-intensive.

To address this latter issue Vert.x allows you to tune the 'compression level' parameter that is native of the gzip/deflate compression algorithms and also set the minimum response content size threshold for compression.

Compression level allows to configure gzip/deflate algorithms in terms of the compression ratio of the resulting data and the computational cost of the compress/decompress operation.

The compression level is an integer value ranged from '1' to '9', where '1' means lower compression ratio but fastest algorithm and '9' means maximum compression ratio available but a slower algorithm.

Using compression levels higher that 1-2 usually allows to save just some bytes in size - the gain is not linear, and depends on the specific data to be compressed - but it comports a non-trascurable cost in term of CPU cycles required to the server while generating the compressed response data ( Note that at moment Vert.x doesn’t support any form caching of compressed response data, even for static files, so the compression is done on-the-fly at every request body generation ) and in the same way it affects client(s) while decoding (inflating) received responses, operation that becomes more CPU-intensive the more the level increases.

It may not make sense to compress responses under certain size thresholds where the trade-off between CPU and saved network bytes is not beneficial. The minimum response content size threshold for compression can be configured via `setContentSizeThreshold`. For example, if set to '100', responses under 100 bytes will not be compressed. By default, it is '0' which means all content can be compressed.

|   | QUIC servers do not yet support compression |
|---|---|

### HTTP compression algorithms

Vert.x supports multiple compression algorithms:

- Gzip
- Deflate
- Snappy
- Brotli
- Zstandard

you can configure them easily.

```
new HttpServerConfig()
  .setCompressionConfig(new CompressionConfig()
    .setCompressionEnabled(true)
    .addGzip()
    .addDeflate()
  );
```

Brotli and zstandard libraries need to be added to your dependencies.

- Maven (in your `pom.xml`):

```
<dependency>
  <groupId>com.aayushatharva.brotli4j</groupId>
  <artifactId>brotli4j</artifactId>
  <version>${brotli4j.version}</version>
</dependency>
<dependency>
  <groupId>com.github.luben</groupId>
  <artifactId>zstd-jni</artifactId>
  <version>${zstd-jini.version}</version>
</dependency>
```

- Gradle (in your `build.gradle` file):

```
dependencies {
  implementation 'com.aayushatharva.brotli4j:brotli4j:${brotli4j.version}'
  runtimeOnly 'com.aayushatharva.brotli4j:native-$system-and-arch:${brotli4j.version}'
  implementation 'com.github.luben:zstd-jni:${zstd-jini.version}'
}
```

When using Gradle, you need to add the runtime native library manually depending on your OS and architecture. See the Gradle section of Brotli4j for more details.

You can configure compressors according to your needs

```
new HttpServerConfig()
  .setCompressionConfig(new CompressionConfig()
    .addGzip(6, 15, 8));
```

### Creating an HTTP client

You create an `HttpClient` instance with the default configuration as follows:

```
HttpClientAgent client = vertx.createHttpClient();
```

By default, the client supports HTTP/1, HTTP/2 in plain text.

### Configuring an HTTP client

If you want to configure the client, you create it as follows:

```
HttpClientConfig config = new HttpClientConfig()
  .setVersions(HttpVersion.HTTP_1_1)
  .setMaxRedirects(5)
  .setHttp1Config(new Http1ClientConfig()
    .setMaxInitialLineLength(1024));

HttpClientAgent client = vertx.createHttpClient(config);
```

Configuration addresses the following parts:

- HTTP versions
- timeouts and limits
- HTTP/1.x specific configuration
- HTTP/2 specific configuration
- HTTP/3 specific configuration
- TLS
- Transport: TCP and QUIC
- Decompression
- Observability
- Network logging

### Configuring an HTTPS client

Vert.x HTTP clients can be configured to use HTTPS in exactly the same way as TCP or QUIC clients.

```
ClientSSLOptions sslOptions = new ClientSSLOptions()
  .setTrustOptions(
    new JksOptions().
      setPath("/path/to/your/truststore.jks").
      setPassword("password-of-your-truststore")
  );

HttpClientConfig config = new HttpClientConfig()
  .setSsl(true);

HttpClientAgent client = vertx.createHttpClient(config);
```

You can read more about SSL client configuration

### Configuring an HTTP/1.x client

Vert.x supports HTTP/1.1 and HTTP/1.0 over plaintext and TLS.

```
HttpClientConfig config = new HttpClientConfig()
  .setVersions(HttpVersion.HTTP_1_1)
  .setSsl(true)
  .setHttp1Config(new Http1ClientConfig()
    .setMaxInitialLineLength(1024));
```

`Http1ClientConfig` captures the configuration of HTTP/1.x specific aspects.

### Configuring an HTTP/2 client

Vert.x supports HTTP/2 over TLS `h2` and over TCP `h2c`.

To perform `h2` requests, TLS must be enabled:

```
HttpClientConfig config = new HttpClientConfig()
  .setVersions(HttpVersion.HTTP_2)
  .setSsl(true)
  .setHttp2Config(new Http2ClientConfig()
    .setKeepAliveTimeout(Duration.ofSeconds(10)));
```

`Http2ClientConfig` captures the configuration of HTTP/2 specific aspects.

### Configuring an HTTP/3 client

Vert.x supports HTTP/3 over QUIC, we recommend reading the QUIC client section.

The implementation of QUIC relies on Netty and QUICHE, a savoury implementation of QUIC which requires native dependencies depending on OS/platform selection, you can learn more about running native QUIC.

```
HttpClientConfig config = new HttpClientConfig()
  .setVersions(HttpVersion.HTTP_3)
  .setSsl(true)
  .setHttp3Config(new Http3ClientConfig()
    .setKeepAliveTimeout(Duration.ofSeconds(10)));
```

`Http3ClientConfig` captures the configuration of HTTP/3 specific aspects.

### Hybrid HTTP client

A client can mix TCP and QUIC at the same time.

```
HttpClientConfig config = new HttpClientConfig()
  .setVersions(HttpVersion.HTTP_1_1, HttpVersion.HTTP_2, HttpVersion.HTTP_3)
  .setSsl(true)
  .setFollowAlternativeServices(true);

ClientSSLOptions sslOptions = new ClientSSLOptions()
  .setKeyCertOptions(new JksOptions().setPath("/path/to/my/keystore"));

HttpClientAgent client = vertx.createHttpClient(config, sslOptions);
```

### Making connections to Unix domain sockets

When running on JDK 16+, or using a native transport, a client can connect to Unix domain sockets:

```
HttpClient httpClient = vertx.createHttpClient();

// Only available when running on JDK16+, or using a native transport
SocketAddress addr = SocketAddress.domainSocketAddress("/var/tmp/myservice.sock");

// Send request to the server
httpClient.request(new RequestOptions()
    .setServer(addr)
    .setHost("localhost")
    .setPort(8080)
    .setURI("/"))
  .compose(request -> request.send().compose(HttpClientResponse::body))
  .onComplete(ar -> {
    if (ar.succeeded()) {
      // Process response
    } else {
      // Handle failure
    }
  });
```

### Pool configuration

For performance purpose, the client uses connection pooling when interacting with HTTP servers.

The concurrency of an HTTP/1.1 server is defined by the client, i.e. the client uses a client defined number of connections to improve performance. However, the concurrency of an HTTP/2 or HTTP/3 server is defined by the maximum number of concurrent streams a server allows on a single connection.

By default, the pool creates up to 5 connections per HTTP/1.1 server and a single connection for other protocols, as recommended.

You can override the pool configuration like this:

```
PoolOptions options = new PoolOptions().setHttp1MaxSize(10);
HttpClientAgent client = vertx.createHttpClient(options);
```

Normally, you should not need more than a single connection for HTTP/2 or HTTP/3.

You can configure various pool `options` as follows

- `options#setHttp1MaxSize` the maximum number of opened per HTTP/1.x server (5 by default)
- `options#setHttp2MaxSize` the maximum number of opened per HTTP/2 server (1 by default), you **should** not change this value since a single HTTP/2 connection is capable of delivering the same performance level than multiple HTTP/1.x connections
- `options#setHttp3MaxSize` the maximum number of opened per HTTP/3 server (1 by default), you **should** not change this value since a single HTTP/3 connection is capable of delivering the same performance level than multiple HTTP/1.x connections
- `options#setCleanerPeriod` the period in milliseconds at which the pool checks expired connections (1 second by default)
- `options#setEventLoopSize` sets the number of event loops the pool use the default value `0` configures the pool to use the event loop of the caller a positive value configures the pool load balance the creation of connection over a list of event loops determined by the value
- `options#setMaxWaitQueueSize` the maximum number of HTTP requests waiting until a connection is available, when the queue is full, the request is rejected

### Advanced HTTP client creation

You can pass configuration to `createHttpClient` methods to configure an HTTP client.

Alternatively you can build a client with the builder `API` :

```
HttpClientAgent client = vertx
  .httpClientBuilder()
  .with(config)
  .build();
```

In addition to `HttpClientConfig`, {`ClientSSLOptions` and `PoolOptions`, you can set

- a connection event handler notified when the client connects to a server
- a redirection handler to implement an alternative HTTP redirect behavior
- `SSLEngineOptions` to configure the SSL engine

### Making requests

The http client is very flexible and there are various ways you can make requests with it.

The first step when making a request is obtaining an HTTP connection to the remote server:

```
client
  .request(HttpMethod.GET, 8080, "myserver.mycompany.com", "/some-uri")
  .onSuccess(ar1 -> {
    // Connected to the server
  });
```

The client will connect to the remote server or reuse an available connection from the client connection pool.

#### Default host and port

Often you want to make many requests to the same host/port with an http client. To avoid you repeating the host/port every time you make a request you can configure the client with a default host/port:

```
HttpClientConfig config = new HttpClientConfig()
  .setDefaultHost("wibble.com");

// Can also set default port if you want...
HttpClientAgent client = vertx.createHttpClient(config);
client
  .request(HttpMethod.GET, "/some-uri")
  .compose(request -> request.send())
  .onSuccess(response -> {
    System.out.println("Received response with status code " + response.statusCode());
  });
```

#### Writing request headers

You can write headers to a request using the `HttpHeaders` as follows:

```
HttpClientAgent client = vertx.createHttpClient();

// Write some headers using the headers multi-map
MultiMap headers = HttpHeaders.set("content-type", "application/json").set("other-header", "foo");

client
  .request(HttpMethod.GET, "some-uri")
  .compose(request -> {
    request.headers().addAll(headers);
    return request.send();
  })
  .onSuccess(response -> {
    System.out.println("Received response with status code " + response.statusCode());
  });
```

The headers are an instance of `MultiMap` which provides operations for adding, setting and removing entries. Http headers allow more than one value for a specific key.

You can also write headers using `putHeader`

```
request.putHeader("content-type", "application/json")
  .putHeader("other-header", "foo");
```

If you wish to write headers to the request you must do so before any part of the request body is written.

#### Writing request and processing response

The `HttpClientRequest` `request` methods connects to the remote server or reuse an existing connection. The request instance obtained is pre-populated with some data such like the host or the request URI, but you need to send this request to the server.

You can call `send` to send a request such as an HTTP `GET` and process the asynchronous `HttpClientResponse`.

```
client
  .request(HttpMethod.GET, 8080, "myserver.mycompany.com", "/some-uri")
  // Send the request
  .compose(request -> request.send())
  // And process the response
  .onSuccess(response -> {
    System.out.println("Received response with status code " + response.statusCode());
  });
```

You can also send the request with a body.

`send` with a string, the `Content-Length` header will be set for you if it was not previously set.

```
client
  .request(HttpMethod.GET, 8080, "myserver.mycompany.com", "/some-uri")
  // Send the request
  .compose(request -> request.send("Hello World"))
  // And process the response
  .onComplete(ar -> {
    if (ar.succeeded()) {
      HttpClientResponse response = ar.result();
      System.out.println("Received response with status code " + response.statusCode());
    } else {
      System.out.println("Something went wrong " + ar.cause().getMessage());
    }
  });
```

`send` with a buffer, the `Content-Length` header will be set for you if it was not previously set.

```
request
  .send(Buffer.buffer("Hello World"))
  .onComplete(ar -> {
    if (ar.succeeded()) {
      HttpClientResponse response = ar.result();
      System.out.println("Received response with status code " + response.statusCode());
    } else {
      System.out.println("Something went wrong " + ar.cause().getMessage());
    }
  });
```

`send` with a stream, if the `Content-Length` header was not previously set, the request is sent with a chunked `Content-Encoding`.

```
request
  .putHeader(HttpHeaders.CONTENT_LENGTH, "1000")
  .send(stream)
  .onComplete(ar -> {
    if (ar.succeeded()) {
      HttpClientResponse response = ar.result();
      System.out.println("Received response with status code " + response.statusCode());
    } else {
      System.out.println("Something went wrong " + ar.cause().getMessage());
    }
  });
```

#### Streaming Request body

The `send` method send requests at once.

Sometimes you’ll want to have low level control on how you write requests bodies.

The `HttpClientRequest` can be used to write the request body.

Here are some examples of writing a POST request with a body:

```
HttpClientAgent client = vertx.createHttpClient();

client.request(HttpMethod.POST, "some-uri")
  .onSuccess(request -> {
    request
      .response()
      .onSuccess(response -> {
        System.out.println("Received response with status code " + response.statusCode());
      });

    // Now do stuff with the request
    request.putHeader("content-length", "1000");
    request.putHeader("content-type", "text/plain");
    request.write(body);

    // Make sure the request is ended when you're done with it
    request.end();
  });
```

Methods exist to write strings in UTF-8 encoding and in any specific encoding and to write buffers:

```
request.write("some data");

// Write string encoded in specific encoding
request.write("some other data", "UTF-16");

// Write a buffer
request.write(Buffer.buffer()
  .appendInt(123)
  .appendLong(245L)
);
```

When you’re writing to a request, the first call to `write` will result in the request headers being written out to the wire.

The actual write is asynchronous and might not occur until some time after the call has returned.

Non-chunked HTTP requests with a request body require a `Content-Length` header to be provided.

Consequently, if you are not using chunked HTTP then you must set the `Content-Length` header before writing to the request, as it will be too late otherwise.

If you are calling one of the `end` methods that take a string or buffer then Vert.x will automatically calculate and set the `Content-Length` header before writing the request body.

If you are using HTTP chunking a `Content-Length` header is not required, so you do not have to calculate the size up-front.

#### Ending streamed HTTP requests

Once you have finished with the HTTP request you must end it with one of the `end` operations.

Ending a request causes any headers to be written, if they have not already been written and the request to be marked as complete.

Requests can be ended in several ways. With no arguments the request is simply ended:

```
request.end();
```

Or a string or buffer can be provided in the call to `end`. This is like calling `write` with the string or buffer before calling `end` with no arguments

```
request.end("some-data");

// End it with a buffer
Buffer buffer = Buffer.buffer().appendFloat(12.3f).appendInt(321);
request.end(buffer);
```

#### Using the request as a stream

An `HttpClientRequest` instance is also a `WriteStream` instance.

You can pipe to it from any `ReadStream` instance.

For, example, you could pipe a file on disk to an http request body as follows:

```
request.setChunked(true);
file.pipeTo(request);
```

#### Chunked HTTP requests

Vert.x supports HTTP Chunked Transfer Encoding for requests.

This allows the HTTP request body to be written in chunks, and is normally used when a large request body is being streamed to the server, whose size is not known in advance.

You put the HTTP request into chunked mode using `setChunked`.

In chunked mode each call to write will cause a new chunk to be written to the wire. In chunked mode there is no need to set the `Content-Length` of the request up-front.

```
request.setChunked(true);

// Write some chunks
for (int i = 0; i < 10; i++) {
  request.write("this-is-chunk-" + i);
}

request.end();
```

#### Form submissions

You can send http form submissions bodies with the `send` variant.

```
ClientForm form = ClientForm.form();
form.attribute("firstName", "Dale");
form.attribute("lastName", "Cooper");

// Submit the form as a form URL encoded body
request
  .send(form)
  .onSuccess(res -> {
    // OK
  });
```

By default, the form is submitted with the `application/x-www-form-urlencoded` content type header. You can set the `content-type` header to `multipart/form-data` instead

```
ClientForm form = ClientForm.form();
form.attribute("firstName", "Dale");
form.attribute("lastName", "Cooper");

// Submit the form as a multipart form body
request
  .putHeader("content-type", "multipart/form-data")
  .send(form)
  .onSuccess(res -> {
    // OK
  });
```

If you want to upload files and send attributes, you can create a `ClientMultipartForm` instead.

```
ClientMultipartForm form = ClientMultipartForm.multipartForm()
  .attribute("imageDescription", "a very nice image")
  .binaryFileUpload(
    "imageFile",
    "image.jpg",
    "/path/to/image",
    "image/jpeg");

// Submit the form as a multipart form body
request
  .send(form)
  .onSuccess(res -> {
    // OK
  });
```
