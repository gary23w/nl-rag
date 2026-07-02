---
title: "Vert.x Core (part 5/8)"
source: https://vertx.io/docs/vertx-core/java/
domain: vertx
license: CC-BY-SA-4.0
tags: vert.x toolkit, eclipse vertx, reactive toolkit, event loop server
fetched: 2026-07-02
part: 5/8
---

#### HTTPS requests

A client configured with SSL trust can perform HTTPS request.

```
HttpClientAgent client = vertx.createHttpClient(new HttpClientConfig()
  .setSsl(true), sslOptions);

// Use the global default configuration with TLS enabled
client
  .request(new RequestOptions()
    .setHost("localhost")
    .setPort(8080)
    .setURI("/"))
  .compose(request -> request.send())
  .onSuccess(response -> {
    System.out.println("Received response with status code " + response.statusCode());
  });
```

The `setSsl` setting acts as the default client setting.

SSL can also be enabled/disabled per request with `RequestOptions` or when specifying a scheme with `setAbsoluteURI` method.

```
HttpClientAgent client = vertx.createHttpClient(new HttpClientConfig(), sslOptions);

// Override the default configuration and use TLS
client
  .request(new RequestOptions()
    .setHost("localhost")
    .setPort(8080)
    .setURI("/")
    .setSsl(true))
  .compose(request -> request.send())
  .onSuccess(response -> {
    System.out.println("Received response with status code " + response.statusCode());
  });
```

The `setSsl` overrides the default client setting

- setting the value to `false` will disable SSL/TLS even if the client is configured to use SSL/TLS
- setting the value to `true` will enable SSL/TLS even if the client is configured to not use SSL/TLS, the actual client SSL/TLS (such as trust, key/certificate, ciphers, ALPN, …) will be reused

Likewise `setAbsoluteURI` scheme also overrides the default client setting.

#### Request protocol

By default, a request use one of the HTTP versions configured by `HttpClientConfig`.

The config versions is an ordered list, the client uses the first version of the list.

You can also set a version on the request when the request requires a specific version:

```
client
  .request(new RequestOptions()
    .setProtocolVersion(HttpVersion.HTTP_2)
    .setHost("localhost")
    .setPort(8080)
    .setURI("/"))
  .compose(request -> request.send())
  .onSuccess(response -> {
    System.out.println("Received response with status code " + response.statusCode());
  });
```

This can be used with a hybrid HTTP client to request an HTTP/3 server: a hybrid client can only determine the IP address for HTTP over TCP using DNS. Setting the request version instructs the client that correct HTTP version to use:

```
client
  .request(new RequestOptions()
    .setProtocolVersion(HttpVersion.HTTP_3)
    .setAbsoluteURI("https://google.com"))
  .compose(request -> request.send())
  .onSuccess(response -> {
    System.out.println("Received response with HTTP version " + response.request().version());
  });
```

This gap is addressed by:

- HTTP Alternative Services, fully supported
- Service Binding and Parameter Specification via the DNS, it should be implemented in the near future

Calling `setFollowAlternativeServices` configures the client to handle alt-svc notifications and use server advertised protocols.

```
HttpClientConfig config = new HttpClientConfig()
  .setFollowAlternativeServices(true)
  .setVersions(HttpVersion.HTTP_1_1, HttpVersion.HTTP_3)
  .setSsl(true);
HttpClientAgent client = vertx.createHttpClient(config, sslOptions);
```

For instance, `https://google/com` responds to HTTP/1.1 requests with an alternative service for `h3` at same address and port (UDP), subsequent calls to this server can use HTTP/3 instead of HTTP/1.1.

```
client
  .request(new RequestOptions().setAbsoluteURI("https://google.com"))
  .compose(request -> request.send())
  .onSuccess(response -> {
    System.out.println("Received response with HTTP version " + response.request().version());
  });
```

The client processes alt-svc notifications in the background and tries to connect to the advertised servers before considering them as valid.

#### Request timeouts

You can set an idle timeout to prevent your application from unresponsive servers using `setIdleTimeout` or `idleTimeout`. When the request does not return any data within the timeout the request will be `cancelled`.

```
Future<Buffer> fut = client
  .request(new RequestOptions()
    .setHost(host)
    .setPort(port)
    .setURI(uri)
    .setIdleTimeout(timeoutMS))
  .compose(request -> request
    .send()
    .compose(HttpClientResponse::body));
```

|   | the timeout starts when the `HttpClientRequest` is available, implying a connection was obtained from the pool. |
|---|---|

You can set a connect timeout to prevent your application from unresponsive busy client connection pool. The `Future<HttpClientRequest>` is failed when a connection is not obtained before the timeout delay.

The connect timeout option is not related to the TCP connect timeout, when a request is made against a pooled HTTP client, the timeout applies to the duration to obtain a connection from the pool to serve the request, the timeout might fire because the server does not respond in time or the pool is too busy to serve a request.

You can configure both timeout using `setTimeout`

```
Future<Buffer> fut = client
  .request(new RequestOptions()
    .setHost(host)
    .setPort(port)
    .setURI(uri)
    .setTimeout(timeoutMS))
  .compose(request -> request
    .send()
    .compose(HttpClientResponse::body));
```

#### Writing custom frames

HTTP/2 and HTTP/3 are framed protocol with various frames for the HTTP request/response model. The protocol allows other kind of frames to be sent or received.

To send such frames, you can use the `writeCustomFrame` on the response. Here’s an example:

```
int frameType = 40;
int frameStatus = 10;
Buffer payload = Buffer.buffer("some data");

// Sending a frame to the server
request.writeCustomFrame(frameType, frameStatus, payload);
```

These frames are sent immediately and are not subject to flow control - when such frame is sent there it may be done before other data frames.

#### Stream cancellation

`cancel` is a best effort to cancel a stream by the underlying HTTP protocol.

- HTTP/1.x does not allow a clean cancellation of a request or a response stream, for example when a client uploads a resource already present on the server, the server needs to accept the entire response: the implementation closes the connection when the current request is inflight.
- HTTP/2 supports stream reset at any time during the request/response: the implementation sends an HTTP/2 reset frame with the error `0x08`
- HTTP/3 relies on QUIC capabilities: the implementation performs a QUIC reset or abort reading with the code `0x10c`

```
request.cancel();
```

The request handler are notified of stream cancellation events with the `request handler` and `response handler`:

```
request.exceptionHandler(err -> {
  if (err instanceof StreamResetException) {
    StreamResetException reset = (StreamResetException) err;
    System.out.println("Stream reset " + reset.getCode());
  }
});
```

|   | stream reset should be avoided because the implementation works partially for HTTP/3 and reset error codes depends on the version of the protocol. |
|---|---|

### Handling HTTP responses

You receive an instance of `HttpClientResponse` into the handler that you specify in of the request methods or by setting a handler directly on the `HttpClientRequest` object.

You can query the status code and the status message of the response with `statusCode` and `statusMessage`.

```
request
  .send()
  .onSuccess(response -> {

    // the status code - e.g. 200 or 404
    System.out.println("Status code is " + response.statusCode());

    // the status message e.g. "OK" or "Not Found".
    System.out.println("Status message is " + response.statusMessage());
  });
```

#### Using the response as a stream

The `HttpClientResponse` instance is also a `ReadStream` which means you can pipe it to any `WriteStream` instance.

#### Response headers and trailers

Http responses can contain headers. Use `headers` to get the headers.

The object returned is a `MultiMap` as HTTP headers can contain multiple values for single keys.

```
String contentType = response.headers().get("content-type");
String contentLength = response.headers().get("content-lengh");
```

Chunked HTTP responses can also contain trailers - these are sent in the last chunk of the response body.

You use `trailers` to get the trailers. Trailers are also a `MultiMap`.

#### Reading the response body

The response handler is called when the headers of the response have been read from the wire.

If the response has a body this might arrive in several pieces some time after the headers have been read. We don’t wait for all the body to arrive before calling the response handler as the response could be very large and we might be waiting a long time, or run out of memory for large responses.

As parts of the response body arrive, the `handler` is called with a `Buffer` representing the piece of the body:

```
client
  .request(HttpMethod.GET, "some-uri")
  .compose(request -> request.send())
  .onSuccess(response -> {
    response.handler(buffer -> {
      System.out.println("Received a part of the response body: " + buffer);
    });
  });
```

If you know the response body is not very large and want to aggregate it all in memory before handling it, you can either aggregate it yourself:

```
request
  .send()
  .onSuccess(response -> {

    // Create an empty buffer
    Buffer totalBuffer = Buffer.buffer();

    response.handler(buffer -> {
      System.out.println("Received a part of the response body: " + buffer.length());

      totalBuffer.appendBuffer(buffer);
    });

    response.endHandler(v -> {
      // Now all the body has been read
      System.out.println("Total response body length is " + totalBuffer.length());
    });
  });
```

Or you can use the convenience `body` which is called with the entire body when the response has been fully read:

```
request
  .send()
  .compose(response -> response.body())
  .onSuccess(body -> {

    // Now all the body has been read
    System.out.println("Total response body length is " + body.length());
  });
```

#### Response end handler

The response `endHandler` is called when the entire response body has been read or immediately after the headers have been read and the response handler has been called if there is no body.

#### Request and response flow composition

The client interface is very simple and follows this pattern:

1. `request` a connection
2. `send` or `write`/`end` the request to the server
3. handle the beginning of the `HttpClientResponse`
4. process the response events

You can use Vert.x future composition methods to make your code simpler, however the API is event driven, and you need to understand it otherwise you might experience possible data races (i.e. loosing events leading to corrupted data).

|   | Vert.x Web Client is a higher level API alternative (in fact it is built on top of this client) you might consider if this client is too low level for your use cases |
|---|---|

The client API intentionally does not return a `Future<HttpClientResponse>` because setting a completion handler on the future can be racy when this is set outside the event-loop.

Potential race in request/response composition

```
Future<HttpClientResponse> get = client.get("some-uri");

// Assuming we have a client that returns a future response
// assuming this is *not* on the event-loop
// introduce a potential data race for the sake of this example
Thread.sleep(100);

get.onSuccess(response -> {

  // Response events might have happened already
  response
    .body()
    .onComplete(ar -> {

    });
});
```

Confining the `HttpClientRequest` usage within a verticle is the easiest solution as the Verticle will ensure that events are processed sequentially avoiding races.

```
vertx.deployVerticle(() -> new AbstractVerticle() {
  @Override
  public void start() {

    HttpClient client = vertx.createHttpClient();

    Future<HttpClientRequest> future = client.request(HttpMethod.GET, "some-uri");
  }
}, new DeploymentOptions());
```

When you are interacting with the client possibly outside a verticle then you can safely perform composition as long as you do not delay the response events, e.g. processing directly the response on the event-loop.

```
Future<JsonObject> future = client
  .request(HttpMethod.GET, "some-uri")
  .compose(request -> request
    .send()
    .compose(response -> {
      // Process the response on the event-loop which guarantees no races
      if (response.statusCode() == 200 &&
        response.getHeader(HttpHeaders.CONTENT_TYPE).equals("application/json")) {
        return response
          .body()
          .map(buffer -> buffer.toJsonObject());
      } else {
        return Future.failedFuture("Incorrect HTTP response");
      }
    }));

// Listen to the composed final json result
future.onComplete(ar -> {
  if (ar.succeeded()) {
    System.out.println("Received json result " + ar.result());
  } else {
    System.out.println("Something went wrong " + ar.cause().getMessage());
  }
});
```

You can also guard the response body with HTTP responses expectations.

```
Future<JsonObject> future = client
  .request(HttpMethod.GET, "some-uri")
  .compose(request -> request
    .send()
    .expecting(HttpResponseExpectation.SC_OK.and(HttpResponseExpectation.JSON))
    .compose(response -> response
      .body()
      .map(buffer -> buffer.toJsonObject())));

// Listen to the composed final json result
future.onComplete(ar -> {
  if (ar.succeeded()) {
    System.out.println("Received json result " + ar.result());
  } else {
    System.out.println("Something went wrong " + ar.cause().getMessage());
  }
});
```

If you need to delay the response processing then you need to `pause` the response or use a `pipe`, this might be necessary when another asynchronous operation is involved.

```
Future<Void> future = client
  .request(HttpMethod.GET, "some-uri")
  .compose(request -> request
    .send()
    .compose(response -> {
      // Process the response on the event-loop which guarantees no races
      if (response.statusCode() == 200) {

        // Create a pipe, this pauses the response
        Pipe<Buffer> pipe = response.pipe();

        // Write the file on the disk
        return fileSystem
          .open("/some/large/file", new OpenOptions().setWrite(true))
          .onFailure(err -> pipe.close())
          .compose(file -> pipe.to(file));
      } else {
        return Future.failedFuture("Incorrect HTTP response");
      }
    }));
```

#### Response expectations

As seen above, you must perform sanity checks manually after the response is received.

You can trade flexibility for clarity and conciseness using *response expectations*.

`Response expectations` can guard the control flow when the response does not match a criteria.

The HTTP Client comes with a set of out of the box predicates ready to use:

```
Future<Buffer> fut = client
  .request(options)
  .compose(request -> request
    .send()
    .expecting(HttpResponseExpectation.SC_SUCCESS)
    .compose(response -> response.body()));
```

You can also create custom predicates when existing predicates don’t fit your needs:

```
HttpResponseExpectation methodsExpectation =
  resp -> {
    String methods = resp.getHeader("Access-Control-Allow-Methods");
    return methods != null && methods.contains("POST");
  };

// Send pre-flight CORS request
client
  .request(new RequestOptions()
    .setMethod(HttpMethod.OPTIONS)
    .setPort(8080)
    .setHost("myserver.mycompany.com")
    .setURI("/some-uri")
    .putHeader("Origin", "Server-b.com")
    .putHeader("Access-Control-Request-Method", "POST"))
  .compose(request -> request
    .send()
    .expecting(methodsExpectation))
  .onComplete(res -> {
    if (res.succeeded()) {
      // Process the POST request now
    } else {
      System.out.println("Something went wrong " + res.cause().getMessage());
    }
  });
```

#### Predefined expectations

As a convenience, the HTTP Client ships a few predicates for common uses cases .

For status codes, e.g. `HttpResponseExpectation.SC_SUCCESS` to verify that the response has a `2xx` code, you can also create a custom one:

```
client
  .request(options)
  .compose(request -> request
    .send()
    .expecting(HttpResponseExpectation.status(200, 202)))
  .onSuccess(res -> {
    // ....
  });
```

For content types, e.g. `HttpResponseExpectation.JSON` to verify that the response body contains JSON data, you can also create a custom one:

```
client
  .request(options)
  .compose(request -> request
    .send()
    .expecting(HttpResponseExpectation.contentType("some/content-type")))
  .onSuccess(res -> {
    // ....
  });
```

Please refer to the `HttpResponseExpectation` documentation for a full list of predefined expectations.

#### Creating custom failures

By default, expectations (including the predefined ones) conveys a simple error message. You can customize the exception class by changing the error converter:

```
Expectation<HttpResponseHead> expectation = HttpResponseExpectation.SC_SUCCESS
  .wrappingFailure((resp, err) -> new MyCustomException(resp.statusCode(), err.getMessage()));
```

|   | creating exception in Java can have a performance cost when it captures a stack trace, so you might want to create exceptions that do not capture the stack trace. By default exceptions are reported using an exception that does not capture the stack trace. |
|---|---|

#### Reading cookies from the response

You can retrieve the list of cookies from a response using `cookies`.

Alternatively you can just parse the `Set-Cookie` headers yourself in the response.

#### 30x redirection handling

The client can be configured to follow HTTP redirections provided by the `Location` response header when the client receives:

- a `301`, `302`, `307` or `308` status code along with an HTTP GET or HEAD method
- a `303` status code, in addition the directed request perform an HTTP GET method

Here’s an example:

```
client
  .request(HttpMethod.GET, "some-uri")
  .compose(request -> request
    .setFollowRedirects(true)
    .send())
  .onSuccess(response -> {
    System.out.println("Received response with status code " + response.statusCode());
  });
```

The maximum redirects is `16` by default and can be changed with `setMaxRedirects`.

```
HttpClientAgent client = vertx.createHttpClient(
  new HttpClientConfig()
    .setMaxRedirects(32));

client
  .request(HttpMethod.GET, "some-uri")
  .compose(request -> request.setFollowRedirects(true).send())
  .onSuccess(response -> {
    System.out.println("Received response with status code " + response.statusCode());
  });
```

One size does not fit all and the default redirection policy may not be adapted to your needs.

The default redirection policy can changed with a custom implementation:

```
HttpClientAgent client = vertx.httpClientBuilder()
  .withRedirectHandler(response -> {

    // Only follow 301 code
    if (response.statusCode() == 301 && response.getHeader("Location") != null) {

      // Compute the redirect URI
      String absoluteURI = resolveURI(response.request().absoluteURI(), response.getHeader("Location"));

      // Create a new ready to use request that the client will use
      return Future.succeededFuture(new RequestOptions().setAbsoluteURI(absoluteURI));
    }

    // We don't redirect
    return null;
  })
  .build();
```

The policy handles the original `HttpClientResponse` received and returns either `null` or a `Future<HttpClientRequest>`.

- when `null` is returned, the original response is processed
- when a future is returned, the request will be sent on its successful completion
- when a future is returned, the exception handler set on the request is called on its failure

The returned request must be unsent so the original request handlers can be sent and the client can send it after.

Most of the original request settings will be propagated to the new request:

- request headers, unless if you have set some headers
- request body unless the returned request uses a `GET` method
- response handler
- request exception handler
- request timeout

#### Creating HTTP tunnels

HTTP tunnels can be created with `connect`:

```
client.request(HttpMethod.CONNECT, "some-uri")
  // Connect to the server
  .compose(request -> request
    .connect()
    .expecting(HttpResponseExpectation.SC_OK))
  .onSuccess(response -> {
    // Tunnel created, raw buffers are transmitted on the wire
    NetSocket socket = response.netSocket();
  });
```

The handler will be called after the HTTP response header is received, the socket will be ready for tunneling and will send and receive buffers.

`connect` works like `send`, but it reconfigures the transport to exchange raw buffers.

#### Receiving custom frames

HTTP/2 and HTTP/3 are framed protocol with various frames for the HTTP request/response model. The protocol allows other kind of frames to be sent or received.

To receive custom frames, you can use the `customFrameHandler` on the response, this will get called every time a custom frame arrives. Here’s an example:

```
response.customFrameHandler(frame -> {

  System.out.println("Received a frame type=" + frame.type() +
    " payload" + frame.payload().toString());
});
```

### Enabling decompression on the client

The http client comes with support for HTTP decompression out of the box.

This means the client can let the remote http server know that it supports compression, and will be able to handle compressed response bodies.

An http server is free to either compress with one of the supported compression algorithms or to send the body back without compressing it at all. So this is only a hint for the Http server which it may ignore at will.

To tell the http server which compression algorithm is supported by the client it will include an `Accept-Encoding` header with the supported compression algorithm as value. Multiple compression algorithms are supported. In case of Vert.x this will result in the following header added:

```
Accept-Encoding: gzip, deflate
```

The server will choose then from one of these. You can detect if a server compressed the body by checking for the `Content-Encoding` header in the response sent back from it.

If the body of the response was compressed via gzip it will include for example the following header:

```
Content-Encoding: gzip
```

To enable decompression set `setDecompressionEnabled` on the configuration used when creating the client.

By default decompression is disabled.

|   | QUIC clients do not yet support compression |
|---|---|

### Client side load balancing

By default, when the client resolves a hostname to a list of several IP addresses, the client uses the first returned IP address.

The http client can be configured to perform client side load balancing instead

```
HttpClientAgent client = vertx
  .httpClientBuilder()
  .withLoadBalancer(LoadBalancer.ROUND_ROBIN)
  .build();
```

Vert.x provides out of the box several load balancing policies you can use

- `Round-robin`
- `Least requests`
- `Power of two choices`
- `Consistent hashing`

Most load balancing policies are pretty much self-explanatory.

Hash based routing can be achieved with the `LoadBalancer.CONSISTENT_HASHING` policy.

```
HttpClientAgent client = vertx
  .httpClientBuilder()
  .withLoadBalancer(LoadBalancer.CONSISTENT_HASHING)
  .build();

HttpServer server = vertx.createHttpServer()
  .requestHandler(inboundReq -> {

    // Get a routing key, in this example we will hash the incoming request host/ip
    // it could be anything else, e.g. user id, request id, ...
    String routingKey = inboundReq.remoteAddress().hostAddress();

    client.request(new RequestOptions()
        .setHost("example.com")
        .setURI("/test")
        .setRoutingKey(routingKey))
      .compose(outboundReq -> outboundReq.send()
        .expecting(HttpResponseExpectation.SC_OK)
        .compose(HttpClientResponse::body))
      .onComplete(ar -> {
        if (ar.succeeded()) {
          Buffer response = ar.result();
        }
      });
  });

server.listen(servicePort);
```

The default consistent hashing policy uses 4 virtual nodes per server and uses a random policy in the absence of a routing key.

You can create a policy configuration that best fit your needs

```
LoadBalancer loadBalancer = LoadBalancer.consistentHashing(10, LoadBalancer.POWER_OF_TWO_CHOICES);
```

Custom load balancing policies can also be used.

```
LoadBalancer loadBalancer = endpoints -> {
  // Returns an endpoint selector for the given endpoints
  // a selector is a stateful view of the provided immutable list of endpoints
  return () -> indexOfEndpoint(endpoints);
};

HttpClientAgent client = vertx
  .httpClientBuilder()
  .withLoadBalancer(loadBalancer)
  .build();
```

### HTTP/1.x pooling and keep alive

Http keep alive allows http connections to be used for more than one request. This can be a more efficient use of connections when you’re making multiple requests to the same server.

For HTTP/1.x versions, the http client supports pooling of connections, allowing you to reuse connections between requests.

For pooling to work, keep alive must be true using `setKeepAlive` on the HTTP/1.1 configuration used when configuring the client. The default value is true.

When keep alive is enabled. Vert.x will add a `Connection: Keep-Alive` header to each HTTP/1.0 request sent. When keep alive is disabled. Vert.x will add a `Connection: Close` header to each HTTP/1.1 request sent to signal that the connection will be closed after completion of the response.

The maximum number of connections to pool **for each server** is configured using `setHttp1MaxSize`

When making a request with pooling enabled, Vert.x will create a new connection if there are less than the maximum number of connections already created for that server, otherwise it will add the request to a queue.

Keep alive connections will be closed by the client automatically after a timeout. The timeout can be specified by the server using the `keep-alive` header:

```
keep-alive: timeout=30
```

You can set the default timeout using `setKeepAliveTimeout` - any connections not used within this timeout will be closed. Please note the timeout value is in seconds not milliseconds.

### HTTP/1.1 pipe-lining

The client also supports pipe-lining of requests on a connection.

Pipe-lining means another request is sent on the same connection before the response from the preceding one has returned. Pipe-lining is not appropriate for all requests.

To enable pipe-lining, it must be enabled using `setPipelining`. By default, pipe-lining is disabled.

When pipe-lining is enabled requests will be written to connections without waiting for previous responses to return.

The number of pipe-lined requests over a single connection is limited by `setPipeliningLimit`. This option defines the maximum number of http requests sent to the server awaiting for a response. This limit ensures the fairness of the distribution of the client requests over the connections to the same server.

### Multiplexed HTTP

Multiplexed HTTP protocols (HTTP/2 and HTTP/3) advocate to use a single connection to a server, by default the http client uses a single connection for each server, all the streams to the same server are multiplexed over the same connection.

When the client needs to use more than a single connection and use pooling

- `setHttp2MaxSize`
- `setHttp3MaxSize`

When it is desirable to limit the number of multiplexed streams per connection and use a connection pool instead of a single connection, `setMultiplexingLimit` or `setMultiplexingLimit` can be used.

```
Http2ClientConfig http2Config = new Http2ClientConfig()
  .setMultiplexingLimit(10);

HttpClient client = vertx.createHttpClient(
  new HttpClientConfig()
    .setHttp2Config(http2Config),
  new PoolOptions()
    .setHttp2MaxSize(3)
);
```

The multiplexing limit for a connection is a setting set on the client that limits the number of streams of a single connection. The effective value can be even lower if the server sets a lower limit with the `SETTINGS_MAX_CONCURRENT_STREAMS` setting.

HTTP/2 or HTTP/3 connections will not be closed by the client automatically. To close them you can call `close` or close the client instance.

Alternatively you can set idle timeout using `setIdleTimeout` - any connections not used within this timeout will be closed. Please note the idle timeout value is in seconds not milliseconds.

### Un-pooled client connections

Most HTTP interactions are performed using `HttpClientAgent` request/response API: the client obtains a connection from its pool of connections to perform a request.

Alternatively, you can connect directly to a server (bypassing the connection pool) and get an HTTP client connection.

```
HttpConnectOptions connectOptions = new HttpConnectOptions()
  .setHost("example.com")
  .setPort(80);

Future<HttpClientConnection> fut = client.connect(connectOptions);
```

The `HttpClientConnection` can create `HttpClientRequest`

```
connection
  .request()
  .onSuccess(request -> {
    request.setMethod(HttpMethod.GET);
    request.setURI("/some-uri");
    Future<HttpClientResponse> response = request.send();
  });
```

|   | `HttpClientConnection` extends `HttpClient` |
|---|---|

A client connection can handle a certain amount of concurrent requests. When the max number of connection is reached, any subsequent request is queued until a slot is available.

### 100-Continue handling

According to the HTTP 1.1 specification a client can set a header `Expect: 100-Continue` and send the request header before sending the rest of the request body.

The server can then respond with an interim response status `Status: 100 (Continue)` to signify to the client that it is ok to send the rest of the body.

The idea here is it allows the server to authorise and accept/reject the request before large amounts of data are sent. Sending large amounts of data if the request might not be accepted is a waste of bandwidth and ties up the server in reading data that it will just discard.

Vert.x allows you to set a `continueHandler` on the client request object

This will be called if the server sends back a `Status: 100 (Continue)` response to signify that it is ok to send the rest of the request.

This is used in conjunction with `writeHead` to write the head of the request.
