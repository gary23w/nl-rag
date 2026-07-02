---
title: "Vert.x Core (part 3/8)"
source: https://vertx.io/docs/vertx-core/java/
domain: vertx
license: CC-BY-SA-4.0
tags: vert.x toolkit, eclipse vertx, reactive toolkit, event loop server
fetched: 2026-07-02
part: 3/8
---

## Writing QUIC servers and clients

Vert.x allows you to easily write non-blocking QUIC clients and servers.

### Configuration of native dependency

The implementation of QUIC relies on Netty and QUICHE, a savoury implementation of QUIC which requires native dependencies depending on OS/platform selection.

You need to add the following dependency at **runtime**:

```
<dependency>
  <groupId>io.netty</groupId>
  <artifactId>netty-codec-native-quic</artifactId>
  <classifier>linux-x86_64</classifier>
</dependency>
```

OS/platform can be

- linux-aarch_64
- linux-x86_64
- osx-aarch_64
- osx-x86_64
- windows-x86_64

### Creating a QUIC server

The simplest way to create a QUIC server, is as follows:

```
ServerSSLOptions sslOptions = new ServerSSLOptions()
  .setKeyCertOptions(
    new JksOptions().
      setPath("/path/to/your/server-keystore.jks").
      setPassword("password-of-your-keystore")
  )
  .setApplicationLayerProtocols(List.of(APPLICATION_PROTOCOL));

QuicServer server = vertx.createQuicServer(sslOptions);
```

Unlike TCP, QUIC always requires the usage of TLS and thus requires to provide SSL configuration.

QUIC mandates the usage of application layer protocol negotiation (ALPN) and therefore an application protocol should be set with `setApplicationLayerProtocols`, without it, no client will be capable of handshaking with this server, the protocol is a simple string that identifies the protocol such as `h3` for HTTP/3.

|   | there is no need to explicitly enable ALPN since it is mandatory |
|---|---|

You can read more about SSL server configuration.

### Configuring a QUIC server

If you don’t want the default, a server can be configured by passing in a `QuicServerConfig` instance when creating it:

```
QuicServerConfig config = new QuicServerConfig()
  .setPort(4321);

QuicServer server = vertx.createQuicServer(config, sslOptions);
```

### Start the Server Listening

To tell the server to listen for incoming requests you use one of the `listen` alternatives.

To tell the server to listen at the host and port as specified in the options:

```
QuicServer server = vertx.createQuicServer(sslOptions);
server.listen();
```

Or to specify the host and port in the call to listen, ignoring what is configured in the options:

```
QuicServer server = vertx.createQuicServer(sslOptions);
server.listen(1234, "localhost");
```

The default host is `0.0.0.0` which means 'listen on all available addresses' and the default port is `0`, which is a special value that instructs the server to find a random unused local port and use that.

The actual bind is asynchronous, so the server might not actually be listening until some time **after** the call to listen has returned.

If you want to be notified when the server is actually listening you can provide a handler to the `listen` call. For example:

```
QuicServer server = vertx.createQuicServer(sslOptions);
server
  .listen(1234, "localhost")
  .onComplete(res -> {
    if (res.succeeded()) {
      System.out.println("Server is now listening!");
    } else {
      System.out.println("Failed to bind!");
    }
  });
```

### Listening on a random port

If `0` is used as the listening port, the server will find an unused random port to listen on.

To find out the real port the server is listening on you can use the asynchronous result of `listen`.

```
QuicServer server = vertx.createQuicServer(sslOptions);
server
  .listen(0, "localhost")
  .onComplete(res -> {
    if (res.succeeded()) {
      SocketAddress bindAddr = res.result();
      System.out.println("Server is now listening on actual port: " + bindAddr.port());
    } else {
      System.out.println("Failed to bind!");
    }
  });
```

### Getting notified of incoming connections

To be notified when a connection is made you need to set a `connectHandler`:

```
QuicServer server = vertx.createQuicServer(sslOptions);
server.connectHandler(connection -> {
  // Handle the connection in here
});
```

### Getting notified of incoming streams

When a connection is made the handler will be called with an instance of `QuicConnection`.

A QUIC connection multiplexes QUIC streams which is what your application actually interacts with.

You can then set a `streamHandler` to handle incoming streams

```
QuicServer server = vertx.createQuicServer(sslOptions);
server.connectHandler(connection -> {
  // Handle the connection in here
  connection.streamHandler(stream -> {
    // Handle streams here
  });
});
```

This is a channel-like interface to the actual connection, and allows you to read and write data as well as do various other things like close the stream.

A stream handler can be set on the server directly, the connection can still be obtained

```
QuicServer server = vertx.createQuicServer(sslOptions);
server.streamHandler(stream -> {
  // Handle streams here
  QuicConnection connection = stream.connection();
});
```

### Reading data from a stream

To read data from the stream you set the `handler` on the stream.

This handler will be called with an instance of `Buffer` every time data is received on the socket.

```
connection.streamHandler(stream -> {
  stream.handler(buffer -> {
    System.out.println("I received some bytes: " + buffer.length());
  });
});
```

### Writing data to a stream

You write to a stream using one of `write`.

```
Buffer buffer = Buffer.buffer().appendFloat(12.34f).appendInt(123);
stream.write(buffer);

// Write a string in UTF-8 encoding
stream.write("some data");

// Write a string using the specified encoding
stream.write("some data", "UTF-16");
```

Write operations are asynchronous and may not occur until some time after the call to write has returned.

### Streaming

Instances of `QuicStream` are also `ReadStream` and `WriteStream` instances, so they can be used to pipe data to or from other read and write streams.

See the chapter on streams for more information.

### Sending files or resources from the classpath

Files and classpath resources can be written to the socket directly using `sendFile`.

Please see the chapter about serving files from the classpath for restrictions of the classpath resolution or disabling it.

```
stream
  .sendFile("myfile.dat")
  .onSuccess(v -> System.out.println("File successfully sent"))
  .onFailure(err -> System.out.println("Could not send file: " + err.getMessage()));
```

### Lifecycle of a stream

Any side of a stream can cleanly terminate its output, signaling no more data will be emitted.

```
stream.end();
```

You can set an end handler to be notified when the opposite side has terminated its output.

```
stream.endHandler(v -> {
  // Clean termination (received a STREAM frame with the FIN bit)
});
```

A stream is closed when output is shut down on both sides.

If you want to be notified when a stream is closed, you can set a `closeHandler` on it:

```
stream.closeHandler(v -> {
  System.out.println("The stream has been closed");
});
```

Any side of a stream can abruptly terminate the stream, `reset` sends a reset frame signaling no more data will be emitted. Reset requires an error code argument used to convey application level error.

```
stream.reset(ERROR_CODE);
```

Likewise, `abort` instructs the other side that no more data should be emitted: aborting asks the other side to reset the stream with the provided code.

```
stream.abort(ERROR_CODE);
```

If you want to be notified when a stream is reset, you can set a `resetHandler` on it:

```
stream.resetHandler(errorCode -> {
  System.out.println("The stream has been reset with error code " + errorCode);
});
```

You can set an `exceptionHandler` to receive any exceptions that happen on the stream.

### Local and remote addresses

The local address of a `QuicConnection` can be retrieved using `localAddress`.

The remote address, (i.e. the address of the other end of the connection) of a `QuicConnection` can be retrieved using `remoteAddress`.

### QUIC graceful shut down

You can shut down a `server` or `client`.

Calling `shutdown` initiates the shut-down phase whereby the server or client are given the opportunity to perform clean-up actions and handle shutdown at the protocol level.

```
server
  .shutdown()
  .onSuccess(res -> {
    System.out.println("Server is now closed");
  });
```

Shut-down waits until all connections/streams are closed or the shut-down timeout fires. When the timeout fires, all resources are forcibly closed.

Each opened connection and stream is notified with a shutdown event, allowing to perform a protocol level close before the actual close.

```
stream.shutdownHandler(v -> {
  stream
    // Write close frame
    .write(closeFrame())
    // Wait until we receive the remote close frame
    .compose(success -> closeFrameHandler(stream))
    // Close the socket
    .eventually(() -> stream.close());
});
```

Any stream without a shutdown handler is closed immediately

The default shut-down timeout is 30 seconds, you can override the amount of time

```
server
  .shutdown(Duration.ofSeconds(60))
  .onSuccess(res -> {
    System.out.println("Server is now closed");
  });
```

You can also shut down QUIC connection individually

```
server
  .shutdown()
  .onSuccess(res -> {
    System.out.println("Connection is now closed");
  });
```

### QUIC close

You can close a `server` or `client` to immediately close all open connections/streams and releases all resources. Unlike `shutdown` there is not grace period.

The close is actually asynchronous and might not complete until some time after the call has returned. You can use the returned future to be notified when the actual close has completed.

This future is completed when the close has fully completed.

```
server
  .close()
  .onSuccess(res -> {
    System.out.println("Server is now closed");
  });
```

### Automatic clean-up in verticles

If you’re creating QUIC servers and clients from inside verticles, those servers and clients will be automatically closed when the verticle is undeployed.

### Creating a QUIC client

The simplest way to create a QUIC client, using all default options is as follows:

```
ClientSSLOptions sslOptions = new ClientSSLOptions()
  .setTrustOptions(new JksOptions().
    setPath("/path/to/your/truststore.jks").
    setPassword("password-of-your-truststore")
  )
  .setApplicationLayerProtocols(List.of(APPLICATION_PROTOCOL));

QuicClient client = vertx.createQuicClient(sslOptions);
```

QUIC mandates the usage of application layer protocol negotiation (ALPN) and therefore an application protocol should be set with `setApplicationLayerProtocols`, without it, this client will not be capable of handshaking with any server.

### Configuring a QUIC client

If you don’t want the default, a client can be configured by passing in a `QuicClientConfig` instance when creating it:

```
QuicClientConfig config = new QuicClientConfig()
  .setConnectTimeout(Duration.ofSeconds(10));

QuicClient client = vertx.createQuicClient(config, sslOptions);
```

### Making connections

To make a connection to a server you use `connect`, specifying the port and host of the server, returning a future completed with the `QuicConnection`

```
QuicClientConfig options = new QuicClientConfig()
  .setConnectTimeout(Duration.ofSeconds(10));
QuicClient client = vertx.createQuicClient(options, sslOptions);
client
  .connect(4321, "localhost")
  .onComplete(res -> {
    if (res.succeeded()) {
      System.out.println("Connected!");
      QuicConnection connection = res.result();
    } else {
      System.out.println("Failed to connect: " + res.cause().getMessage());
    }
  });
```

### Configuring connection attempts

A client can be configured to automatically retry connecting to the server in the event that it cannot connect. This is configured with `setReconnectInterval` and `setReconnectAttempts`.

|   | Currently, Vert.x will not attempt to reconnect if a connection fails, reconnect attempts and interval only apply to creating initial connections. |
|---|---|

```
QuicClientConfig options = new QuicClientConfig().
  setReconnectAttempts(10).
  setReconnectInterval(Duration.ofMillis(500));

QuicClient client = vertx.createQuicClient(options, sslOptions);
```

By default, multiple connection attempts are disabled.

### Opening streams

A QUIC connection multiplexes QUIC streams which is what your application actually interacts with.

To open a stream you use `openStream`, returning a future completed with the `QuicStream`

```
connection
  .openStream()
  .onComplete(res -> {
    if (res.succeeded()) {
      QuicStream stream = res.result();
      stream.write("hello");
    } else {
      System.out.println("Failed to open: " + res.cause().getMessage());
    }
  });
```

|   | Opening the stream only allocates it locally, the remote side of the connection is not aware of the presence of the stream until you actually send data. |
|---|---|

By default, the connection opens a bidirectional stream.

QUIC supports unidirectional streams too, you can open them as well when the remote side allows it.

```
connection
  .openStream(false)
  .onComplete(res -> {
    if (res.succeeded()) {
      // Obtained a write-only streams
      QuicStream stream = res.result();
      stream.write("hello");
    } else {
      System.out.println("Failed to open: " + res.cause().getMessage());
    }
  });
```

### QUIC transport configuration

QUIC uses transport parameters to determine the connection behavior, e.g. the maximum number of streams an endpoint allows.

`QuicConfig` configures transport parameters, you should be aware of a few of them.

The following parameters are client/server sensitive and configure the limit per connection:

- `initial_max_streams_bidi`: the maximum number of bidirectional streams the endpoint can receive
- `initial_max_streams_uni`: the maximum number of unidirectional streams the endpoint can receive
- `initial_max_data`: the maximum number of bytes that can be sent on a connection
- `initial_max_stream_data_bidi_local`: the flow control limit for locally initiated bidirectional streams
- `initial_max_stream_data_bidi_remote`: the flow control limit for peer initiated bidirectional streams
- `initial_max_stream_data_uni`: the flow control limit for unidirectional streams

| parameter | default value | default client | default server |
|---|---|---|---|
| initial_max_streams_bidi | 0 | 0 | 256 |
| initial_max_streams_uni | 0 | 0 | 0 |
| initial_max_data | 10_485_760 | 10_485_760 | 10_485_760 |
| initial_max_stream_data_bidi_local | 0 | 1_048_576 | 0 |
| initial_max_stream_data_bidi_bemote | 0 | 0 | 1_048_576 |
| initial_max_stream_data_uni | 0 | 0 | 0 |

These default parameters model a traditional client / server in which the client opens bidirectional streams like TCP does.

Each protocol should define proper defaults, e.g. HTTP/3 relies on unidirectional streams and therefore configures a few parameters differently for this purpose.

Vert.x HTTP/3 provides sensitive QUIC transport configuration as well.

### QUIC datagram extension

You can configure your endpoint to support the QUIC Datagram Extension.

```
endpointConfig
  .getTransportConfig()
  .setDatagramConfig(new QuicDatagramConfig()
    .setEnabled(true));
```

Once your endpoint is started, you should check the extension is available.

```
long maxLength = connection.maxDatagramLength();
if (maxLength > 0) {
  connection.datagramHandler(dgram -> {
    connection.writeDatagram(dgram);
  });
}
```

### QUIC client address validation

QUIC is based on UDP and can be subject to amplification attacks.

Address validations ensures that a QUIC server cannot be used for such attacks.

By default, Vert.x performs basic address validation, but this is not sufficient for production.

We recommend configuring address validation based on cryptographic key instead for production.

```
QuicServerConfig config = new QuicServerConfig()
  .setClientAddressValidation(QuicClientAddressValidation.CRYPTO)
  .setClientAddressValidationKey(new JksOptions()
    .setPath("/path/to/your/key.jks")
    .setPassword("wibble")
  );
```

Depending on the nature of the key, either symmetric (MAC) or asymmetric (Digital Signature) is achieved.

The following signing algorithms are supported:

- HS256: HmacSHA256/HmacSHA384/HmacSHA512
- RSA: SHA256withRSA/SHA384withRSA/SHA512withRSA
- ECDSA: SHA256withECDSA/SHA384withECDSA/SHA512withECDSA

By default, a validation token is valid for 30 seconds, you can configure also configure it.

```
QuicServerConfig config = new QuicServerConfig()
  .setClientAddressValidation(QuicClientAddressValidation.CRYPTO)
  .setClientAddressValidationKey(key)
  .setClientAddressValidationTimeWindow(Duration.ofSeconds(15));
```

### Logging network activity

For debugging purposes, stream network activity can be logged:

```
QuicServerConfig options = new QuicServerConfig()
  .setLogConfig(new LogConfig()
    .setEnabled(true));

QuicServer server = vertx.createQuicServer(options, sslOptions);
```

Here is the output of a simple QUIC server

```
[id: 0x7eb26864, QuicStreamAddress{streamId=0}] REGISTERED
[id: 0x7eb26864, QuicStreamAddress{streamId=0}] ACTIVE
[id: 0x7eb26864, QuicStreamAddress{streamId=0}] READ: 58B
         +-------------------------------------------------+
         |  0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f |
+--------+-------------------------------------------------+----------------+
|00000000| 4c 6f 72 65 6d 20 69 70 73 75 6d 20 64 6f 6c 6f |Lorem ipsum dolo|
|00000010| 72 20 73 69 74 20 61 6d 65 74 2c 20 63 6f 6e 73 |r sit amet, cons|
|00000020| 65 63 74 65 74 75 72 20 61 64 69 70 69 73 63 69 |ectetur adipisci|
|00000030| 6e 67 20 65 6c 69 74 2e 2e 2e                   |ng elit...      |
+--------+-------------------------------------------------+----------------+
[id: 0x7eb26864, QuicStreamAddress{streamId=0}] WRITE: 58B
         +-------------------------------------------------+
         |  0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f |
+--------+-------------------------------------------------+----------------+
|00000000| 4c 6f 72 65 6d 20 69 70 73 75 6d 20 64 6f 6c 6f |Lorem ipsum dolo|
|00000010| 72 20 73 69 74 20 61 6d 65 74 2c 20 63 6f 6e 73 |r sit amet, cons|
|00000020| 65 63 74 65 74 75 72 20 61 64 69 70 69 73 63 69 |ectetur adipisci|
|00000030| 6e 67 20 65 6c 69 74 2e 2e 2e                   |ng elit...      |
+--------+-------------------------------------------------+----------------+
[id: 0x7eb26864, QuicStreamAddress{streamId=0}] READ COMPLETE
[id: 0x7eb26864, QuicStreamAddress{streamId=0}] FLUSH
[id: 0x7eb26864, QuicStreamAddress{streamId=0}] USER_EVENT: io.netty.channel.socket.ChannelInputShutdownEvent@78311b8
[id: 0x7eb26864, QuicStreamAddress{streamId=0}] USER_EVENT: io.netty.channel.socket.ChannelInputShutdownReadComplete@6932d2cd
[id: 0x7eb26864, QuicStreamAddress{streamId=0}] INACTIVE
[id: 0x7eb26864, QuicStreamAddress{streamId=0}] UNREGISTERED
```

By default, binary data is logged in hex format.

You can reduce the data format verbosity to only print the buffer length instead of the entire data by setting the log data format.

```
QuicServerConfig options = new QuicServerConfig()
  .setLogConfig(new LogConfig()
    .setEnabled(true)
    .setDataFormat(ByteBufFormat.SIMPLE));

QuicServer server = vertx.createQuicServer(options, sslOptions);
```

Here is the same output with simple buffer format

```
[id: 0x681541d4, QuicStreamAddress{streamId=0}] REGISTERED
[id: 0x681541d4, QuicStreamAddress{streamId=0}] ACTIVE
[id: 0x681541d4, QuicStreamAddress{streamId=0}] READ: 58B
[id: 0x681541d4, QuicStreamAddress{streamId=0}] WRITE: 58B
[id: 0x681541d4, QuicStreamAddress{streamId=0}] READ COMPLETE
[id: 0x681541d4, QuicStreamAddress{streamId=0}] FLUSH
[id: 0x681541d4, QuicStreamAddress{streamId=0}] USER_EVENT: io.netty.channel.socket.ChannelInputShutdownEvent@78311b8
[id: 0x681541d4, QuicStreamAddress{streamId=0}] USER_EVENT: io.netty.channel.socket.ChannelInputShutdownReadComplete@6932d2cd
[id: 0x681541d4, QuicStreamAddress{streamId=0}] INACTIVE
[id: 0x681541d4, QuicStreamAddress{streamId=0}] UNREGISTERED
```

Clients can also log network activity

```
QuicClientConfig options = new QuicClientConfig()
  .setLogConfig(new LogConfig()
    .setEnabled(true));

QuicClient client = vertx.createQuicClient(options, sslOptions);
```

Network activity is logged by Netty with the `DEBUG` level and with the `io.netty.handler.logging.LoggingHandler` name. When using network activity logging there are a few things to keep in mind:

- logging is not performed by Vert.x logging but by Netty
- this is **not** a production feature

You should read the Netty logging section.

### QLog configuration

Vert.x QUIC implementation is based on Netty and QUICHE, a savoury implementation of QUIC.

QUICHE logs in the QLog JSON-SEQ format, QUICHE output is file based. It is configured independently of your JVM logging.

You can use `QLogConfig` to configure QLog.

```
QuicServerConfig cfg = new QuicServerConfig()
  .setQLogConfig(new QLogConfig()
    .setPath("/path/to/log/dir/")
    .setTitle("Server logging")
    .setDescription("Logging of QUIC server"));
```

The logging granularity is per connection, that is, each connection will be logged in its own file.

|   | this should not be used in production, only for the purpose of logging QUICHE |
|---|---|

### Configuring SSL/TLS

#### Configuring SSL/TLS per connection

The client performs an SSL/TLS handshake with the client provided SSL configuration.

You can perform a fine-grained per connection configuration

```
ClientSSLOptions sslOptions = new ClientSSLOptions()
  .setTrustOptions(new JksOptions().
    setPath("/path/to/your/truststore.jks").
    setPassword("password-of-your-truststore")
  )
  .setApplicationLayerProtocols(List.of(APPLICATION_PROTOCOL));

Future<QuicConnection> future = client.connect(
  port,
  host,
  new QuicConnectOptions().setSslOptions(sslOptions)
);
```

#### Client host verification

By default, host verification is **not** configured on the client. This verifies the CN portion of the server certificate against the server hostname to avoid Man-in-the-middle attacks.

You must configure it explicitly on your client

- `""` (empty string) disables host verification
- `"HTTPS"` enables HTTP over TLS verification
- `LDAPS` enables LDAP v3 extension for TLS verification

```
ClientSSLOptions sslOptions = new ClientSSLOptions()
  .setTrustOptions(trustOptions)
  .setApplicationLayerProtocols(List.of(APPLICATION_PROTOCOL))
  .setHostnameVerificationAlgorithm(verificationAlgorithm);
```

|   | the Vert.x HTTP client uses the QUIC client and configures with `"HTTPS"` the verification algorithm. |
|---|---|

#### Updating SSL/TLS configuration

You can use the `updateSSLOptions` method to update the key/certifications or trust on a QUIC server or client (e.g. to implement certificate rotation).

```
Future<Boolean> fut = server.updateSSLOptions(new ServerSSLOptions()
  .setKeyCertOptions(
    new JksOptions()
      .setPath("/path/to/your/server-keystore.jks").
      setPassword("password-of-your-keystore"))
  .setApplicationLayerProtocols(List.of(APPLICATION_PROTOCOL)));
```

When the update succeeds the new SSL configuration is used, otherwise the previous configuration is preserved.

|   | The options object is compared (using `equals`) against the existing options to prevent an update when the objects are equals since loading options can be costly. When object are equals, you can use the `force` parameter to force the update. |
|---|---|

#### SSL/TLS key logging

QUICHE relies on BoringSSL and supports SSL/TLS key logging.

```
QuicServerConfig serverCfg = new QuicServerConfig()
  .setClientAddressValidation(QuicClientAddressValidation.NONE)
  .setKeyLogFile("/path/to/keylogfile.txt");
```

|   | this requires to disable client address validation to work properly. |
|---|---|

When configured, BoringSSL logs keys for decrypting SSL/TLS in the configured log, which can be then used by tools such as Wireshark to decrypt QUIC traffic.
