---
title: "Vert.x Core (part 6/8)"
source: https://vertx.io/docs/vertx-core/java/
domain: vertx
license: CC-BY-SA-4.0
tags: vert.x toolkit, eclipse vertx, reactive toolkit, event loop server
fetched: 2026-07-02
part: 6/8
---

# Vert.x Core

Here’s an example:

```
client.request(HttpMethod.PUT, "some-uri")
  .onSuccess(request -> {
    request.response().onSuccess(response -> {
      System.out.println("Received response with status code " + response.statusCode());
    });

    request.putHeader("Expect", "100-Continue");

    request.continueHandler(v -> {
      // OK to send rest of body
      request.write("Some data");
      request.write("Some more data");
      request.end();
    });

    request.writeHead();
  });
```

On the server side a Vert.x http server can be configured to automatically send back 100 Continue interim responses when it receives an `Expect: 100-Continue` header.

This is done by setting the option `setHandle100ContinueAutomatically`.

If you’d prefer to decide whether to send back continue responses manually, then this property should be set to `false` (the default), then you can inspect the headers and call `writeContinue` to have the client continue sending the body:

```
httpServer.requestHandler(request -> {
  if (request.getHeader("Expect").equalsIgnoreCase("100-Continue")) {

    // Send a 100 continue response
    request.response().writeContinue();

    // The client should send the body when it receives the 100 response
    request.bodyHandler(body -> {
      // Do something with body
    });

    request.endHandler(v -> {
      request.response().end();
    });
  }
});
```

You can also reject the request by sending back a failure status code directly: in this case the body should either be ignored or the connection should be closed (100-Continue is a performance hint and cannot be a logical protocol constraint):

```
httpServer.requestHandler(request -> {
  if (request.getHeader("Expect").equalsIgnoreCase("100-Continue")) {

    //
    boolean reject = true;
    if (reject) {

      // Reject with a failure code and close the connection
      // this is probably best with persistent connection
      request.response()
        .setStatusCode(405)
        .putHeader("Connection", "close")
        .end();
    } else {

      // Reject with a failure code and ignore the body
      // this may be appropriate if the body is small
      request.response()
        .setStatusCode(405)
        .end();
    }
  }
});
```

### HTTP connections

The `HttpConnection` offers an API to deal with HTTP connection events, lifecycle and settings.

HTTP/1.x implements partially the `HttpConnection` API.

HTTP/2 implements fully the `HttpConnection` API.

HTTP/3 implements partially the `HttpConnection` API.

The Javadoc indicates the level of support for every supported protocol.

#### Server connections

The `connection` method returns the request connection on the server:

```
HttpConnection connection = request.connection();
```

A connection handler can be set on the server to be notified of any incoming connection:

```
HttpServer server = vertx.httpServerBuilder()
  .with(httpConfig)
  .withConnectHandler(connection -> {
    System.out.println("A client connected");
  })
  .build();
```

#### Client connections

The `connection` method returns the request connection on the client:

```
HttpConnection connection = request.connection();
```

A connection handler can be set on a client builder to be notified when a connection has been established happens:

```
vertx
  .httpClientBuilder()
  .with(config)
  .withConnectHandler(connection -> {
    System.out.println("Connected to the server");
  })
  .build();
```

#### Connection settings

The configuration of multiplexed HTTP connection is configured by the `HttpSettings` object.

Each endpoint must respect the settings sent by the other side of the connection.

When a connection is established, the client and the server exchange initial settings. Initial settings are configured by

- `Http2ClientConfig#setInitialSettings` on the client and `Http2ServerConfig#setInitialSettings` on the server.
- `Http3ClientConfig#setInitialSettings` on the client and `Http3ServerConfig#setInitialSettings` on the server.

```
HttpSettings settings = connection.remoteSettings();

// HTTP/2
Integer http2MaxFrameSize = settings.get(Http2Settings.MAX_FRAME_SIZE);

// HTTP/3
Long http3MaxFieldSectionSize = settings.get(Http3Settings.MAX_FIELD_SECTION_SIZE);
```

|   | a few HTTP/2 settings such as MAX_CONCURRENT_STREAMS are implemented by QUIC at the transport level for HTTP/3, you can refer to the QUIC transport configuration. |
|---|---|

### Connection shutdown

HTTP server and client support graceful shutdown.

You can shut down a `server` or `client`.

Calling `shutdown` initiates the shut-down phase whereby the server or client are given the opportunity to perform clean-up actions.

- A standalone HTTP server unbinds
- A shared HTTP server is removed from the set of accepting servers
- An HTTP client refuses to send any new requests

When all connections inflight requests are processed, the server or client is then closed.

In addition, HTTP/2 and HTTP/3 connections send a `GOAWAY` frame to signal the remote endpoint that the connection cannot be used anymore.

```
server
  .shutdown()
  .onSuccess(res -> {
    System.out.println("Server is now closed");
  });
```

Shutdown waits until all sockets are closed or the shutdown timeout fires. When the timeout fires, all sockets are forcibly closed.

Each opened HTTP connections is notified with a shutdown event, allowing to perform cleanup before the actual connection is closed.

```
server.connectionHandler(conn -> {
  conn.shutdownHandler(v -> {
    // Perform clean-up
  });
});
```

The default shut-down timeout is 30 seconds, you can override the timeout

```
server
  .shutdown(60, TimeUnit.SECONDS)
  .onSuccess(res -> {
    System.out.println("Server is now closed");
  });
```

#### Connection close

Connection `close` closes the connection:

- it closes the socket for HTTP/1.x
- a shutdown with no delay for HTTP/2 and HTTP/3, the `GOAWAY` frame will still be sent before the connection is closed

|   | a close is equivalent to a connection shutdown without a grace period |
|---|---|

The `closeHandler` notifies when a connection is closed.

### Client sharing

You can share an HTTP client between multiple verticles or instances of the same verticle. Such client should be created outside of a verticle otherwise it will be closed when the verticle that created it is undeployed

```
HttpClientConfig config = new HttpClientConfig()
  .setShared(true);

HttpClientAgent client = vertx.createHttpClient(config);
vertx.deployVerticle(() -> new AbstractVerticle() {
  @Override
  public void start() throws Exception {
    // Use the client
  }
}, new DeploymentOptions().setInstances(4));
```

You can also create a shared HTTP client in each verticle:

```
vertx.deployVerticle(() -> new AbstractVerticle() {
  HttpClientAgent client;
  @Override
  public void start() {
    // Get or create a shared client
    // this actually creates a lease to the client
    // when the verticle is undeployed, the lease will be released automaticaly
    client = vertx.createHttpClient(new HttpClientConfig()
      .setShared(true)
      .setName("my-client"));
  }
}, new DeploymentOptions().setInstances(4));
```

The first time a shared client is created it will create and return a client. Subsequent calls will reuse this client and create a lease to this client. The client is closed after all leases have been disposed.

By default, a client reuses the current event-loop when it needs to create a TCP connection. The HTTP client will therefore randomly use event-loops of verticles using it in a safe fashion.

You can assign a number of event loop a client will use independently of the client using it

```
vertx.deployVerticle(() -> new AbstractVerticle() {
  HttpClientAgent client;
  @Override
  public void start() {
    // The client creates and use two event-loops for 4 instances
    client = vertx.createHttpClient(
      new HttpClientConfig()
        .setShared(true)
        .setName("my-client"),
      new PoolOptions().setEventLoopSize(2));
  }
}, new DeploymentOptions().setInstances(4));
```

### TCP Server sharing

When several HTTP servers listen on the same port, vert.x orchestrates the request handling using a round-robin strategy.

Let’s take a verticle creating an HTTP server such as:

io.vertx.examples.http.sharing.HttpServerVerticle

```
vertx.createHttpServer().requestHandler(request -> {
  request.response().end("Hello from server " + this);
}).listen(8080);
```

This service is listening on the TCP port 8080.

So, when this verticle is instantiated multiple times as with: `deploymentOptions.setInstances(2)`, what’s happening ?

If both verticles bound to the same port, you would receive a socket bind exception.

Fortunately, Vert.x is handling this case for you.

When you deploy another server on the same host and port as an existing server it doesn’t actually try and create a new server listening on the same host/port. It binds only once to the socket. When receiving a request it calls the server handlers following a round-robin strategy.

Let’s now imagine a client calling multiples times the server.

Vert.x delegates the requests to one of the server sequentially:

```
Hello from i.v.e.h.s.HttpServerVerticle@1
Hello from i.v.e.h.s.HttpServerVerticle@2
Hello from i.v.e.h.s.HttpServerVerticle@1
Hello from i.v.e.h.s.HttpServerVerticle@2
...
```

Consequently, the servers can scale over available cores while each Vert.x verticle instance remains strictly single threaded, and you don’t have to do any special tricks like writing load-balancers in order to scale your server on your multi-core machine.

You can bind on a shared random ports using a negative port value, the first bind will pick a port randomly, subsequent binds on the same port value will share this random port.

io.vertx.examples.http.sharing.HttpServerVerticle

```
vertx.createHttpServer().requestHandler(request -> {
  request.response().end("Hello from server " + this);
}).listen(-1);
```

### QUIC server sharing

QUIC server requires to set the `setLoadBalanced` configuration flag prior bind the server.

QUIC server sharing works differently than TCP, the underlying UDP socket is bound multiple times with the `SO_REUSEPORT` option.

When the server accepts a QUIC connection, the crafted connection ID encodes information capable of identifying the actual QUIC server assigned to the connection, other servers will forward inbound UDP packets to the connection’s assigned server.

|   | this feature is experimental. |
|---|---|

### Automatic clean-up in verticles

If you’re creating http servers and clients from inside verticles, those servers and clients will be automatically closed when the verticle is undeployed.

### Logging network activity

For debugging purposes, network activity can be logged.

On the server:

```
HttpServerConfig config = new HttpServerConfig()
  .setLogConfig(new LogConfig()
    .setEnabled(true));

HttpServer server = vertx.createHttpServer(config);
```

On the client

```
HttpClientConfig config = new HttpClientConfig()
  .setLogConfig(new LogConfig()
    .setEnabled(true));

HttpClientAgent client = vertx.createHttpClient(config);
```

See network activity logging for TCP / QUIC for detailed explanations.

### Server Name Indication (SNI)

Vert.x http servers can be configured to use SNI in exactly the same way as {@linkplain io.vertx.core.net net servers}.

Vert.x http client will present the actual hostname as *server name* during the TLS handshake.

### Using HA PROXY protocol

HA PROXY protocol provides a convenient way to safely transport connection information such as a client’s address across multiple layers of NAT or TCP proxies.

HA PROXY protocol can be enabled by setting the option `setUseProxyProtocol` and adding the following dependency in your classpath:

```
<dependency>
  <groupId>io.netty</groupId>
  <artifactId>netty-codec-haproxy</artifactId>
  <!--<version>Should align with netty version that Vert.x uses</version>-->
</dependency>
```

```
HttpServerConfig config = new HttpServerConfig();
config
  .getTcpConfig()
  .setUseProxyProtocol(true);

HttpServer server = vertx.createHttpServer(config);
server.requestHandler(request -> {
  // Print the actual client address provided by the HA proxy protocol instead of the proxy address
  System.out.println(request.remoteAddress());

  // Print the address of the proxy
  System.out.println(request.localAddress());
});
```

### Throttling inbound and outbound bandwidth of TCP connections

Like for TCP servers, you can set traffic shaping options through `getTcpConfig`.

```
HttpServerConfig config = new HttpServerConfig()
  .setHost("localhost")
  .setPort(1234);

config.getTcpConfig()
  .setTrafficShapingOptions(new TrafficShapingOptions()
    .setInboundGlobalBandwidth(64 * 1024)
    .setOutboundGlobalBandwidth(128 * 1024));

HttpServer server = vertx.createHttpServer(config);
```

These traffic shaping options can also be dynamically updated after server start.

```
HttpServerConfig config = new HttpServerConfig()
  .setHost("localhost")
  .setPort(1234);

config.getTcpConfig()
  .setTrafficShapingOptions(new TrafficShapingOptions()
    .setInboundGlobalBandwidth(64 * 1024)
    .setOutboundGlobalBandwidth(128 * 1024));

HttpServer server = vertx.createHttpServer(config);
TrafficShapingOptions update = new TrafficShapingOptions()
  .setInboundGlobalBandwidth(2 * 64 * 1024) // twice
  .setOutboundGlobalBandwidth(128 * 1024); // unchanged

server
  .listen(1234, "localhost")
  // wait until traffic shaping handler is created for updates
  .onSuccess(v -> server.updateTrafficShapingOptions(update));
```

### HTTP/2 features

#### Connection ping

HTTP/2 connection ping is useful for determining the connection round-trip time or check the connection validity: `ping` sends a `PING` frame to the remote endpoint:

```
Buffer data = Buffer.buffer();
for (byte i = 0;i < 8;i++) {
  data.appendByte(i);
}
connection
  .ping(data)
  .onSuccess(pong -> System.out.println("Remote side replied"));
```

Vert.x will send automatically an acknowledgement when a `PING` frame is received, an handler can be set to be notified for each ping received:

```
connection.pingHandler(ping -> {
  System.out.println("Got pinged by remote side");
});
```

The handler is just notified, the acknowledgement is sent whatsoever. Such feature is aimed for implementing protocols on top of HTTP/2.

|   | this only applies to the HTTP/2 protocol |
|---|---|

#### HTTP/2 RST flood protection

An HTTP/2 server is protected against RST flood DDOS attacks (CVE-2023-44487): there is an upper bound to the number of `RST` frames a server can receive in a time window. The default configuration sets the upper bound to `200` for a duration of `30` seconds.

You can use `setRstFloodMaxRstFramePerWindow` and `setRstFloodWindowDuration` to override these settings.

#### Updating HTTP/2 settings

HTTP/2 settings can be changed at any time after the connection is established:

```
connection.updateSettings(new Http2Settings().setMaxConcurrentStreams(100));
```

As the remote side should acknowledge on reception of the settings update, it’s possible to give a callback to be notified of the acknowledgment:

```
connection
  .updateSettings(new Http2Settings().setMaxConcurrentStreams(100))
  .onSuccess(v -> System.out.println("The settings update has been acknowledged "));
```

Conversely, the `remoteSettingsHandler` is notified when the new remote settings are received:

```
connection.remoteSettingsHandler(settings -> {
  System.out.println("Received new settings");
});
```

|   | this only applies to the HTTP/2 protocol, HTTP/3 settings are set initially and never changed |
|---|---|

### WebSockets

WebSockets are a web technology that allows a full duplex socket-like connection between HTTP servers and HTTP clients (typically browsers).

Vert.x supports WebSockets on both the client and server-side.

#### WebSockets on the server

There are two ways of handling WebSockets on the server side.

##### WebSocket handler

The first way involves providing a `webSocketHandler` on the server instance.

When a WebSocket connection is made to the server, the handler will be called, passing in an instance of `ServerWebSocket`.

```
server.webSocketHandler(webSocket -> {
  System.out.println("Connected!");
});
```

##### Server WebSocket handshake

By default, the server accepts any inbound WebSocket.

You can set a WebSocket handshake handler to control the outcome of a WebSocket handshake, i.e. accept or reject an incoming WebSocket.

You can choose to reject the WebSocket by calling `accept` or `reject`.

```
server.webSocketHandshakeHandler(handshake -> {
  authenticate(handshake.headers(), ar -> {
    if (ar.succeeded()) {
      if (ar.result()) {
        // Terminate the handshake with the status code 101 (Switching Protocol)
        handshake.accept();
      } else {
        // Reject the handshake with 401 (Unauthorized)
        handshake.reject(401);
      }
    } else {
      // Will send a 500 error
      handshake.reject(500);
    }
  });
});
```

|   | the WebSocket will be automatically accepted after the handler is called unless the WebSocket’s handshake has been set |
|---|---|

##### Upgrading to WebSocket

The second way of handling WebSockets is to handle the HTTP Upgrade request that was sent from the client, and call `toWebSocket` on the server request.

```
server.requestHandler(request -> {
  switch (request.path()) {
    case "/myapi":

      Future<ServerWebSocket> fut = request.toWebSocket();
      fut.onSuccess(ws -> {
        // Do something
      });
      break;

    default:

      // Reject
      request.response().setStatusCode(400).end();
      break;
  }
});
```

##### The server WebSocket

The `ServerWebSocket` instance enables you to retrieve the `headers`, `path`, `query` and `URI` of the HTTP request of the WebSocket handshake.

#### WebSockets on the client

e Vert.x `WebSocketClient` supports WebSockets.

```
You can connect a WebSocket to a server using one of the `link:../../apidocs/io/vertx/core/http/WebSocketClient.html#connect-int-java.lang.String-java.lang.String-[connect]` operations.
```

```
The returned future will be completed with an instance of `link:../../apidocs/io/vertx/core/http/WebSocket.html[WebSocket]` when the connection has been made:
```

```
WebSocketClient client = vertx.createWebSocketClient();

client
  .connect(80, "example.com", "/some-uri")
  .onSuccess(ws -> {
    ws.textMessageHandler(msg -> {
      // Handle msg
    });
    System.out.println("Connected!");
  });
```

en connecting from a non Vert.x thread, you can create a `ClientWebSocket`, configure its handlers and then connect to the server:

```
[source,java]
----
WebSocketClient client = vertx.createWebSocketClient();
```

client .webSocket() .textMessageHandler(msg → { // Handle msg }) .connect(80, "example.com", "/some-uri") .onSuccess(ws → { System.out.println("Connected!"); }); ----

By default, the client sets the `origin` header to the server host, e.g http://www.example.com. Some servers will refuse such request, you can configure the client to not set this header.

```
WebSocketConnectOptions options = new WebSocketConnectOptions()
  .setHost(host)
  .setPort(port)
  .setURI(requestUri)
  .setAllowOriginHeader(false);
client
  .connect(options)
  .onSuccess(ws -> {
    System.out.println("Connected!");
  });
```

You can also set a different header:

```
WebSocketConnectOptions options = new WebSocketConnectOptions()
  .setHost(host)
  .setPort(port)
  .setURI(requestUri)
  .addHeader(HttpHeaders.ORIGIN, origin);
client
  .connect(options)
  .onSuccess(ws -> {
    System.out.println("Connected!");
  });
```

|   | older versions of the WebSocket protocol use `sec-websocket-origin` instead |
|---|---|

#### Writing messages to WebSockets

If you wish to write a single WebSocket message to the WebSocket you can do this with `writeBinaryMessage` or `writeTextMessage` :

```
Buffer buffer = Buffer.buffer().appendInt(123).appendFloat(1.23f);
webSocket.writeBinaryMessage(buffer);

// Write a simple text message
String message = "hello";
webSocket.writeTextMessage(message);
```

If the WebSocket message is larger than the maximum WebSocket frame size as configured with `setMaxFrameSize` then Vert.x will split it into multiple WebSocket frames before sending it on the wire.

#### Writing frames to WebSockets

A WebSocket message can be composed of multiple frames. In this case the first frame is either a *binary* or *text* frame followed by zero or more *continuation* frames.

The last frame in the message is marked as *final*.

To send a message consisting of multiple frames you create frames using `WebSocketFrame.binaryFrame` , `WebSocketFrame.textFrame` or `WebSocketFrame.continuationFrame` and write them to the WebSocket using `writeFrame`.

Here’s an example for binary frames:

```
WebSocketFrame frame1 = WebSocketFrame.binaryFrame(buffer1, false);
webSocket.writeFrame(frame1);

WebSocketFrame frame2 = WebSocketFrame.continuationFrame(buffer2, false);
webSocket.writeFrame(frame2);

// Write the final frame
WebSocketFrame frame3 = WebSocketFrame.continuationFrame(buffer2, true);
webSocket.writeFrame(frame3);
```

In many cases you just want to send a WebSocket message that consists of a single final frame, so we provide a couple of shortcut methods to do that with `writeFinalBinaryFrame` and `writeFinalTextFrame`.

Here’s an example:

```
webSocket.writeFinalTextFrame("Geronimo!");

// Send a WebSocket message consisting of a single final binary frame:

Buffer buff = Buffer.buffer().appendInt(12).appendString("foo");

webSocket.writeFinalBinaryFrame(buff);
```

#### Reading frames from WebSockets

To read frames from a WebSocket you use the `frameHandler`.

The frame handler will be called with instances of `WebSocketFrame` when a frame arrives, for example:

```
webSocket.frameHandler(frame -> {
  System.out.println("Received a frame of size!");
});
```

#### Closing WebSockets

Use `close` to close the WebSocket connection when you have finished with it.

#### Piping WebSockets

The `WebSocket` instance is also a `ReadStream` and a `WriteStream` so it can be used with pipes.

When using a WebSocket as a write stream or a read stream it can only be used with WebSockets connections that are used with binary frames that are no split over multiple frames.

### Using a proxy for HTTP/HTTPS connections

The `HttpClient` supports accessing HTTP/HTTPS URLs via an HTTP proxy (e.g. Squid), a *SOCKS4a*, or a *SOCKS5* proxy. The `CONNECT` protocol uses HTTP/1.x but can connect to HTTP/1.x and HTTP/2 servers.

Connecting to `h2c` (unencrypted HTTP/2 servers) is likely not supported by http proxies since they will support HTTP/1.1 only.

The proxy can be configured in the `HttpClientConfig` by setting a `ProxyOptions` object containing proxy type, hostname, port and optionally username and password or a prebuilt `Proxy-Authorization` value.

Here’s an example of using an HTTP proxy:

```
HttpClientConfig config = new HttpClientConfig();
config.getTcpConfig()
  .setProxyOptions(new ProxyOptions()
    .setType(ProxyType.HTTP)
    .setHost("localhost")
    .setPort(3128)
    .setUsername("username")
    .setPassword("secret"));
HttpClientAgent client = vertx.createHttpClient(config);
```

When the client connects to an HTTP URL, it connects to the proxy server and provides the full URL in the HTTP request, like `GET http://www.somehost.com/path/file.html HTTP/1.1`.

When the client connects to an HTTPS URL, it asks the proxy to create a tunnel to the remote host with the `CONNECT` method.

For a SOCKS5 proxy:

```
HttpClientConfig config = new HttpClientConfig();
config.getTcpConfig()
  .setProxyOptions(new ProxyOptions()
    .setType(ProxyType.SOCKS5)
    .setHost("localhost")
    .setPort(1080)
    .setUsername("username")
    .setPassword("secret"));
HttpClientAgent client = vertx.createHttpClient(config);
```

The DNS resolution is always done on the proxy server, to achieve the functionality of a SOCKS4 client, it is necessary to resolve the DNS address locally.

`ProxyOptions` can also be set per request:

```
client.request(new RequestOptions()
    .setHost("example.com")
    .setProxyOptions(proxyOptions))
  .compose(request -> request
    .send()
    .compose(HttpClientResponse::body))
  .onSuccess(body -> {
    System.out.println("Received response");
  });
```

|   | Client connection pooling is aware of proxies (including authentication). Consequently, two requests to the same host through different proxies do not share the same pooled connection. |
|---|---|

You can use `setNonProxyHosts` to configure a list of host bypassing the proxy. The list accepts `*` wildcard for matching domains:

```
HttpClientConfig config = new HttpClientConfig();
config.getTcpConfig()
  .setProxyOptions(new ProxyOptions()
    .setType(ProxyType.SOCKS5)
    .setHost("localhost").setPort(1080)
    .setUsername("username")
    .setPassword("secret"))
  .addNonProxyHost("*.foo.com")
  .addNonProxyHost("localhost");
HttpClientAgent client = vertx.createHttpClient(config);
```

By default, a 10 seconds connection timeout is set for the proxy handler in the Vert.x HTTP client. If the target server takes longer than that to accept the connection, or if the proxy is too busy and delays completion of the handshake with the client, you might increase this timeout:

```
proxyOptions.setConnectTimeout(Duration.ofSeconds(60));
```

#### Handling of other protocols

The HTTP proxy implementation supports getting ftp:// urls if the proxy supports that.

When the HTTP request URI contains the full URL then the client will not compute a full HTTP url and instead use the full URL specified in the request URI:

```
HttpClientConfig config = new HttpClientConfig();
config.getTcpConfig()
  .setProxyOptions(new ProxyOptions()
    .setType(ProxyType.HTTP));
HttpClientAgent client = vertx.createHttpClient(config);
client
  .request(HttpMethod.GET, "ftp://ftp.gnu.org/gnu/")
  .compose(request -> request.send())
  .onSuccess(response -> {
    System.out.println("Received response with status code " + response.statusCode());
  });
```


## Using the SharedData API

As its name suggests, the `SharedData` API allows you to safely share data between:

- different parts of your application, or
- different applications in the same Vert.x instance, or
- different applications across a cluster of Vert.x instances.

In practice, it provides:

- synchronous maps (local-only)
- asynchronous maps
- asynchronous locks
- asynchronous counters

|   | The behavior of the distributed data structure depends on the cluster manager you use. Backup (replication) and behavior when a network partition is faced are defined by the cluster manager and its configuration. Please refer to the cluster manager documentation as well as to the underlying framework manual. |
|---|---|

### Local maps

`Local maps` allow you to share data safely between different event loops (e.g. different verticles) in the same Vert.x instance.

They only allow certain data types to be used as keys and values:

- immutable types (e.g. strings, booleans, … etc), or
- types implementing the `Shareable` interface (buffers, JSON arrays, JSON objects, or your own shareable objects).

In the latter case the key/value will be copied before putting it into the map.

This way we can ensure there is no *shared access to mutable state* between different threads in your Vert.x application. And you won’t have to worry about protecting that state by synchronising access to it.

|   | As a convenience, objects implementing `ClusterSerializable` or `java.io.Serializable` can be used as keys and values too. In this case, the key/value will be copied before putting it into the map by serializing/deserializing. Therefore, it is recommended to consider implementing `Shareable` instead for better performance. |
|---|---|

Here’s an example of using a shared local map:

```
SharedData sharedData = vertx.sharedData();

LocalMap<String, String> map1 = sharedData.getLocalMap("mymap1");

map1.put("foo", "bar"); // Strings are immutable so no need to copy

LocalMap<String, Buffer> map2 = sharedData.getLocalMap("mymap2");

map2.put("eek", Buffer.buffer().appendInt(123)); // This buffer will be copied before adding to map

// Then... in another part of your application:

map1 = sharedData.getLocalMap("mymap1");

String val = map1.get("foo");

map2 = sharedData.getLocalMap("mymap2");

Buffer buff = map2.get("eek");
```

### Asynchronous shared maps

`Asynchronous shared maps` allow data to be put in the map and retrieved locally or from any other node.

This makes them really useful for things like storing session state in a farm of servers hosting a Vert.x Web application.

They only allow certain data types to be used as keys and values:

- immutable types (e.g. strings, booleans, … etc), or
- types implementing the `ClusterSerializable` interface (buffers, JSON arrays, JSON objects, or your own cluster serializable objects), or
- types implementing the `java.io.Serializable` interface.

Getting the map is asynchronous and the result is returned to you in the handler that you specify. Here’s an example:

```
SharedData sharedData = vertx.sharedData();

sharedData.
  <String, String>getAsyncMap("mymap")
  .onComplete(res -> {
    if (res.succeeded()) {
      AsyncMap<String, String> map = res.result();
    } else {
      // Something went wrong!
    }
  });
```

When Vert.x is clustered, data that you put into the map is accessible locally as well as on any of the other cluster members.

|   | In clustered mode, asynchronous shared maps rely on distributed data structures provided by the cluster manager. Beware that the latency relative to asynchronous shared map operations can be much higher in clustered than in local mode. |
|---|---|

If your application doesn’t need data to be shared with every other node, you can retrieve a local-only map:

```
SharedData sharedData = vertx.sharedData();

sharedData.
  <String, String>getLocalAsyncMap("mymap")
  .onComplete(res -> {
    if (res.succeeded()) {
      // Local-only async map
      AsyncMap<String, String> map = res.result();
    } else {
      // Something went wrong!
    }
  });
```

#### Putting data in a map

You put data in a map with `put`.

The actual put is asynchronous and the returned future is notified once it is complete:

```
map
  .put("foo", "bar")
  .onComplete(resPut -> {
    if (resPut.succeeded()) {
      // Successfully put the value
    } else {
      // Something went wrong!
    }
  });
```

#### Getting data from a map

You get data from a map with `get`.

The actual get is asynchronous and the returned future is notified with the result some time later:

```
map
  .get("foo")
  .onComplete(resGet -> {
    if (resGet.succeeded()) {
      // Successfully got the value
      Object val = resGet.result();
    } else {
      // Something went wrong!
    }
  });
```

##### Other map operations

You can also remove entries from an asynchronous map, clear them and get the size.

See the `API docs` for a detailed list of map operations.

### Asynchronous locks

`Asynchronous locks` allow you to obtain exclusive locks locally or across the cluster. This is useful when you want to do something or access a resource on only one node of a cluster at any one time.

Asynchronous locks have an asynchronous API unlike most lock APIs which block the calling thread until the lock is obtained.

To obtain a lock use `getLock`. This won’t block, but when the lock is available, the returned future is completed with an instance of `Lock`, signalling that you now own the lock.

While you own the lock, no other caller, locally or on the cluster, will be able to obtain the lock.

When you’ve finished with the lock, you call `release` to release it, so another caller can obtain it:

```
SharedData sharedData = vertx.sharedData();

sharedData
  .getLock("mylock")
  .onComplete(res -> {
    if (res.succeeded()) {
      // Got the lock!
      Lock lock = res.result();

      // 5 seconds later we release the lock so someone else can get it

      vertx.setTimer(5000, tid -> lock.release());

    } else {
      // Something went wrong
    }
  });
```

You can also get a lock with a timeout. If it fails to obtain the lock within the timeout the handler will be called with a failure:

```
SharedData sharedData = vertx.sharedData();

sharedData
  .getLockWithTimeout("mylock", 10000)
  .onComplete(res -> {
    if (res.succeeded()) {
      // Got the lock!
      Lock lock = res.result();

    } else {
      // Failed to get lock
    }
  });
```

See the `API docs` for a detailed list of lock operations.

|   | In clustered mode, asynchronous locks rely on distributed data structures provided by the cluster manager. Beware that the latency relative to asynchronous shared lock operations can be much higher in clustered than in local mode. |
|---|---|

If your application doesn’t need the lock to be shared with every other node, you can retrieve a local-only lock:

```
SharedData sharedData = vertx.sharedData();

sharedData
  .getLocalLock("mylock")
  .onComplete(res -> {
    if (res.succeeded()) {
      // Local-only lock
      Lock lock = res.result();

      // 5 seconds later we release the lock so someone else can get it

      vertx.setTimer(5000, tid -> lock.release());

    } else {
      // Something went wrong
    }
  });
```

Sometimes, you use the lock API to retrieve an asynchronous result and apply the acquire/release pattern around the asynchronous call. Vert.x provides a simplified lock API to simplify this pattern.

```
SharedData sharedData = vertx.sharedData();

Future<String> res = sharedData.withLock("mylock", () -> {
  // Obtained the lock!
  Future<String> future = getAsyncString();
  // It will be released upon completion of this future
  return future;
});
```

The lock is acquired before calling the supplier and released when the future returned by the supplier completes.

### Asynchronous counters

It’s often useful to maintain an atomic counter locally or across the different nodes of your application.

You can do this with `Counter`.

You obtain an instance with `getCounter`:

```
SharedData sharedData = vertx.sharedData();

sharedData
  .getCounter("mycounter")
  .onComplete(res -> {
    if (res.succeeded()) {
      Counter counter = res.result();
    } else {
      // Something went wrong!
    }
  });
```

Once you have an instance you can retrieve the current count, atomically increment it, decrement and add a value to it using the various methods.

See the `API docs` for a detailed list of counter operations.

|   | In clustered mode, asynchronous counters rely on distributed data structures provided by the cluster manager. Beware that the latency relative to asynchronous shared counter operations can be much higher in clustered than in local mode. |
|---|---|

If your application doesn’t need the counter to be shared with every other node, you can retrieve a local-only counter:

```
SharedData sharedData = vertx.sharedData();

sharedData
  .getLocalCounter("mycounter")
  .onComplete(res -> {
    if (res.succeeded()) {
      // Local-only counter
      Counter counter = res.result();
    } else {
      // Something went wrong!
    }
  });
```


## Using the file system with Vert.x

The Vert.x `FileSystem` object provides many operations for manipulating the file system.

There is one file system object per Vert.x instance, and you obtain it with `fileSystem`.

A blocking and a non blocking version of each operation is provided. The non blocking versions take a handler which is called when the operation completes or an error occurs.

Here’s an example of an asynchronous copy of a file:

```
FileSystem fs = vertx.fileSystem();

// Copy file from foo.txt to bar.txt
fs.copy("foo.txt", "bar.txt")
  .onComplete(res -> {
    if (res.succeeded()) {
      // Copied ok!
    } else {
      // Something went wrong
    }
  });
```

The blocking versions are named `xxxBlocking` and return the results or throw exceptions directly. In many cases, depending on the operating system and file system, some of the potentially blocking operations can return quickly, which is why we provide them, but it’s highly recommended that you test how long they take to return in your particular application before using them from an event loop, so as not to break the Golden Rule.

Here’s the copy using the blocking API:

```
FileSystem fs = vertx.fileSystem();

// Copy file from foo.txt to bar.txt synchronously
fs.copyBlocking("foo.txt", "bar.txt");
```

Many operations exist to copy, move, truncate, chmod and many other file operations. We won’t list them all here, please consult the `API docs` for the full list.

Let’s see a couple of examples using asynchronous methods:

```
vertx.fileSystem()
  .readFile("target/classes/readme.txt")
  .onComplete(result -> {
    if (result.succeeded()) {
      System.out.println(result.result());
    } else {
      System.err.println("Oh oh ..." + result.cause());
    }
  });

// Copy a file
vertx.fileSystem()
  .copy("target/classes/readme.txt", "target/classes/readme2.txt")
  .onComplete(result -> {
    if (result.succeeded()) {
      System.out.println("File copied");
    } else {
      System.err.println("Oh oh ..." + result.cause());
    }
  });

// Write a file
vertx.fileSystem()
  .writeFile("target/classes/hello.txt", Buffer.buffer("Hello"))
  .onComplete(result -> {
    if (result.succeeded()) {
      System.out.println("File written");
    } else {
      System.err.println("Oh oh ..." + result.cause());
    }
  });

// Check existence and delete
vertx.fileSystem()
  .exists("target/classes/junk.txt")
  .compose(exist -> {
    if (exist) {
      return vertx.fileSystem().delete("target/classes/junk.txt");
    } else {
      return Future.failedFuture("File does not exist");
    }
  }).onComplete(result -> {
    if (result.succeeded()) {
      System.out.println("File deleted");
    } else {
      System.err.println("Oh oh ... - cannot delete the file: " + result.cause().getMessage());
    }
  });
```

### Asynchronous files

Vert.x provides an asynchronous file abstraction that allows you to manipulate a file on the file system.

You open an `AsyncFile` as follows:

```
OpenOptions options = new OpenOptions();
fileSystem
  .open("myfile.txt", options)
  .onComplete(res -> {
    if (res.succeeded()) {
      AsyncFile file = res.result();
    } else {
      // Something went wrong!
    }
  });
```

`AsyncFile` implements `ReadStream` and `WriteStream` so you can *pipe* files to and from other stream objects such as net sockets, http requests and responses, and WebSockets.

They also allow you to read and write directly to them.

#### Random access writes

To use an `AsyncFile` for random access writing you use the `write` method.

The parameters to the method are:

- `buffer`: the buffer to write.
- `position`: an integer position in the file where to write the buffer. If the position is greater or equal to the size of the file, the file will be enlarged to accommodate the offset.

Here is an example of random access writes:

```
vertx.fileSystem()
  .open("target/classes/hello.txt", new OpenOptions())
  .onComplete(result -> {
    if (result.succeeded()) {
      AsyncFile file = result.result();
      Buffer buff = Buffer.buffer("foo");
      for (int i = 0; i < 5; i++) {
        file
          .write(buff, buff.length() * i)
          .onComplete(ar -> {
            if (ar.succeeded()) {
              System.out.println("Written ok!");
              // etc
            } else {
              System.err.println("Failed to write: " + ar.cause());
            }
          });
      }
    } else {
      System.err.println("Cannot open file " + result.cause());
    }
  });
```

#### Random access reads

To use an `AsyncFile` for random access reads you use the `read` method.

The parameters to the method are:

- `buffer`: the buffer into which the data will be read.
- `offset`: an integer offset into the buffer where the read data will be placed.
- `position`: the position in the file where to read data from.
- `length`: the number of bytes of data to read
- `handler`: the result handler

Here’s an example of random access reads:

```
vertx.fileSystem()
  .open("target/classes/les_miserables.txt", new OpenOptions())
  .onComplete(result -> {
    if (result.succeeded()) {
      AsyncFile file = result.result();
      Buffer buff = Buffer.buffer(1000);
      for (int i = 0; i < 10; i++) {
        file
          .read(buff, i * 100, i * 100, 100)
          .onComplete(ar -> {
            if (ar.succeeded()) {
              System.out.println("Read ok!");
            } else {
              System.err.println("Failed to write: " + ar.cause());
            }
          });
      }
    } else {
      System.err.println("Cannot open file " + result.cause());
    }
  });
```

#### Opening Options

When opening an `AsyncFile`, you pass an `OpenOptions` instance. These options describe the behavior of the file access. For instance, you can configure the file permissions with the `setRead`, `setWrite` and `setPerms` methods.

You can also configure the behavior if the open file already exists with `setCreateNew` and `setTruncateExisting`.

You can also mark the file to be deleted on close or when the JVM is shutdown with `setDeleteOnClose`.

#### Flushing data to underlying storage.

In the `OpenOptions`, you can enable/disable the automatic synchronisation of the content on every write using `setDsync`. In that case, you can manually flush any writes from the OS cache by calling the `flush` method.

This method can also be called with a handler which will be called when the flush is complete.

#### Using AsyncFile as ReadStream and WriteStream

`AsyncFile` implements `ReadStream` and `WriteStream`. You can then use them with a *pipe* to pipe data to and from other read and write streams. For example, this would copy the content to another `AsyncFile`:

```
final AsyncFile output = vertx.fileSystem().openBlocking("target/classes/plagiary.txt", new OpenOptions());

vertx.fileSystem()
  .open("target/classes/les_miserables.txt", new OpenOptions())
  .compose(file -> file
    .pipeTo(output)
    .eventually(() -> file.close()))
  .onComplete(result -> {
    if (result.succeeded()) {
      System.out.println("Copy done");
    } else {
      System.err.println("Cannot copy file " + result.cause().getMessage());
    }
  });
```

You can also use the *pipe* to write file content into HTTP responses, or more generally in any `WriteStream`.

#### Accessing files from the classpath

When vert.x cannot find the file on the filesystem it tries to resolve the file from the class path. Note that classpath resource paths never start with a `/`.

Due to the fact that Java does not offer async access to classpath resources, the file is copied to the filesystem in a worker thread when the classpath resource is accessed the very first time and served from there asynchronously. When the same resource is accessed a second time, the file from the filesystem is served directly from the filesystem. The original content is served even if the classpath resource changes (e.g. in a development system).

This caching behaviour can be set on the `setFileCachingEnabled` option. The default value of this option is `true` unless the system property `vertx.disableFileCaching` is defined.

The path where the files are cached is `/tmp/vertx-cache-UUID` by default and can be customized by setting the system property `vertx.cacheDirBase`. When using this property, note that it should refer to a directory prefix in a process read/writeable location, for example: `-Dvertx.cacheDirBase=/tmp/my-vertx-cache` (Note that there’s no UUID).

Each vert.x process will append it’s own UUID in order to keep caches independently of different applications running on the same machine.

The whole classpath resolving feature can be disabled system-wide by setting the system property `vertx.disableFileCPResolving` to `true`.

|   | these system properties are evaluated once when the `io.vertx.core.file.FileSystemOptions` class is loaded, so these properties should be set before loading this class or as a JVM system property when launching it. |
|---|---|

If you want to disable classpath resolving for a particular application but keep it enabled by default system-wide, you can do so via the `setClassPathResolvingEnabled` option.

#### Closing an AsyncFile

To close an `AsyncFile` call the `close` method. Closing is asynchronous and if you want to be notified when the close has been completed you can specify a handler function as an argument.
