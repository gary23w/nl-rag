---
title: "Vert.x Core (part 2/8)"
source: https://vertx.io/docs/vertx-core/java/
domain: vertx
license: CC-BY-SA-4.0
tags: vert.x toolkit, eclipse vertx, reactive toolkit, event loop server
fetched: 2026-07-02
part: 2/8
---

## JSON

Unlike some other languages, Java does not have first class support for JSON so we provide two classes to make handling JSON in your Vert.x applications a bit easier.

### JSON objects

The `JsonObject` class represents JSON objects.

A JSON object is basically just a map which has string keys and values can be of one of the JSON supported types (string, number, boolean).

JSON objects also support null values.

#### Creating JSON objects

Empty JSON objects can be created with the default constructor.

You can create a JSON object from a string JSON representation as follows:

```
String jsonString = "{\"foo\":\"bar\"}";
JsonObject object = new JsonObject(jsonString);
```

You can create a JSON object from a map as follows:

```
Map<String, Object> map = new HashMap<>();
map.put("foo", "bar");
map.put("xyz", 3);
JsonObject object = new JsonObject(map);
```

#### Putting entries into a JSON object

Use the `put` methods to put values into the JSON object.

The method invocations can be chained because of the fluent API:

```
JsonObject object = new JsonObject();
object.put("foo", "bar").put("num", 123).put("mybool", true);
```

#### Getting values from a JSON object

You get values from a JSON object using the `getXXX` methods, for example:

```
String val = jsonObject.getString("some-key");
int intVal = jsonObject.getInteger("some-other-key");
```

#### Mapping between JSON objects and Java objects

You can create a JSON object from the fields of a Java object as follows:

You can instantiate a Java object and populate its fields from a JSON object as follows:

```
request.bodyHandler(buff -> {
  JsonObject jsonObject = buff.toJsonObject();
  User javaObject = jsonObject.mapTo(User.class);
});
```

Note that both of the above mapping directions use Jackson’s `ObjectMapper#convertValue()` to perform the mapping. See the Jackson documentation for information on the impact of field and constructor visibility, caveats on serialization and deserialization across object references, etc.

However, in the simplest case, both `mapFrom` and `mapTo` should succeed if all fields of the Java class are public (or have public getters/setters), and if there is a public default constructor (or no defined constructors).

Referenced objects will be transitively serialized/deserialized to/from nested JSON objects as long as the object graph is acyclic.

#### Encoding a JSON object to a String

You use `encode` to encode the object to a String form.

### JSON arrays

The `JsonArray` class represents JSON arrays.

A JSON array is a sequence of values (string, number, boolean).

JSON arrays can also contain null values.

#### Creating JSON arrays

Empty JSON arrays can be created with the default constructor.

You can create a JSON array from a string JSON representation as follows:

```
String jsonString = "[\"foo\",\"bar\"]";
JsonArray array = new JsonArray(jsonString);
```

#### Adding entries into a JSON array

You add entries to a JSON array using the `add` methods.

```
JsonArray array = new JsonArray();
array.add("foo").add(123).add(false);
```

#### Getting values from a JSON array

You get values from a JSON array using the `getXXX` methods, for example:

```
String val = array.getString(0);
Integer intVal = array.getInteger(1);
Boolean boolVal = array.getBoolean(2);
```

#### Encoding a JSON array to a String

You use `encode` to encode the array to a String form.

#### Creating arbitrary JSON

Creating JSON object and array assumes you are using valid string representation.

When you are unsure of the string validity then you should use instead `Json.decodeValue`

```
Object object = Json.decodeValue(arbitraryJson);
if (object instanceof JsonObject) {
  // That's a valid json object
} else if (object instanceof JsonArray) {
  // That's a valid json array
} else if (object instanceof String) {
  // That's valid string
} else {
  // etc...
}
```

### Jackson

`JsonObject` / JsonArray`encoding and decoding is backed by the Jackson library, `Json static methods uses it as well.

#### Supported Jackson versions

Vert.x depends on the latest available LTS version of Jackson 2: 2.21.x

Since Vert.x 5.1, Jackson 3 is supported and utilized when Jackson 2 is not available on the class/module path, the Jackson 3 version shall be the latest available LTS version of Jackson 3: 3.1.x

#### Read constraint configuration

Since Jackson 2.15, upper bound constraints have been added to limit the bytes cumulated when parsing a JSON input.

You can override the default configuration of the underlying parsers used by Vert.x with the following system properties:

- `vertx.jackson.defaultReadMaxNestingDepth`: Maximum Nesting depth
- `vertx.jackson.defaultReadMaxDocumentLength`: Maximum Document length
- `vertx.jackson.defaultReadMaxNumberLength`: Maximum Number value length
- `vertx.jackson.defaultReadMaxStringLength`: Maximum String value length
- `vertx.jackson.defaultReadMaxNameLength`: Maximum Property name length
- `vertx.jackson.defaultMaxTokenCount`: Maximum Token count

You can refer to this for more information.

#### Databind support

Jackson Databind extension is supported, powering JSON/Object mapping facilities such as `mapTo` or `Json.encode`.

By choice, Jackson Databind is not a dependency of `io.vertx:vertx-core`, it should be explicitly as a dependency of your project.


## Json Pointers

Vert.x provides an implementation of Json Pointers from RFC6901. You can use pointers both for querying and for writing. You can build your `JsonPointer` using a string, a URI or manually appending paths:

```
JsonPointer pointer1 = JsonPointer.from("/hello/world");
// Build a pointer manually
JsonPointer pointer2 = JsonPointer.create()
  .append("hello")
  .append("world");
```

After instantiating your pointer, use `queryJson` to query a JSON value. You can update a Json Value using `writeJson`:

```
Object result1 = objectPointer.queryJson(jsonObject);
// Query a JsonArray
Object result2 = arrayPointer.queryJson(jsonArray);
// Write starting from a JsonObject
objectPointer.writeJson(jsonObject, "new element");
// Write starting from a JsonObject
arrayPointer.writeJson(jsonArray, "new element");
```

You can use Vert.x Json Pointer with any object model by providing a custom implementation of `JsonPointerIterator`


## Buffers

Most data is shuffled around inside Vert.x using buffers.

A buffer is a sequence of zero or more bytes that can read from or written to and which expands automatically as necessary to accommodate any bytes written to it. You can perhaps think of a buffer as smart byte array.

### Creating buffers

Buffers can create by using one of the static `Buffer.buffer` methods.

Buffers can be initialised from strings or byte arrays, or empty buffers can be created.

Here are some examples of creating buffers:

Create a new empty buffer:

```
Buffer buff = Buffer.buffer();
```

Create a buffer from a String. The String will be encoded in the buffer using UTF-8.

```
Buffer buff = Buffer.buffer("some string");
```

Create a buffer from a String: The String will be encoded using the specified encoding, e.g:

```
Buffer buff = Buffer.buffer("some string", "UTF-16");
```

Create a buffer from a byte[]

```
byte[] bytes = new byte[] {1, 3, 5};
Buffer buff = Buffer.buffer(bytes);
```

Create a buffer with an initial size hint. If you know your buffer will have a certain amount of data written to it you can create the buffer and specify this size. This makes the buffer initially allocate that much memory and is more efficient than the buffer automatically resizing multiple times as data is written to it.

Note that buffers created this way **are empty**. It does not create a buffer filled with zeros up to the specified size.

```
Buffer buff = Buffer.buffer(10000);
```

### Writing to a Buffer

There are two ways to write to a buffer: appending, and random access. In either case buffers will always expand automatically to encompass the bytes. It’s not possible to get an `IndexOutOfBoundsException` with a buffer.

#### Appending to a Buffer

To append to a buffer, you use the `appendXXX` methods. Append methods exist for appending various different types.

The return value of the `appendXXX` methods is the buffer itself, so these can be chained:

```
Buffer buff = Buffer.buffer();

buff.appendInt(123).appendString("hello\n");

socket.write(buff);
```

#### Random access buffer writes

You can also write into the buffer at a specific index, by using the `setXXX` methods. Set methods exist for various different data types. All the set methods take an index as the first argument - this represents the position in the buffer where to start writing the data.

The buffer will always expand as necessary to accommodate the data.

```
Buffer buff = Buffer.buffer();

buff.setInt(1000, 123);
buff.setString(0, "hello");
```

### Reading from a Buffer

Data is read from a buffer using the `getXXX` methods. Get methods exist for various datatypes. The first argument to these methods is an index in the buffer from where to get the data.

```
Buffer buff = Buffer.buffer();
for (int i = 0; i < buff.length(); i += 4) {
  System.out.println("int value at " + i + " is " + buff.getInt(i));
}
```

### Working with unsigned numbers

Unsigned numbers can be read from or appended/set to a buffer with the `getUnsignedXXX`, `appendUnsignedXXX` and `setUnsignedXXX` methods. This is useful when implementing a codec for a network protocol optimized to minimize bandwidth consumption.

In the following example, value 200 is set at specified position with just one byte:

```
Buffer buff = Buffer.buffer(128);
int pos = 15;
buff.setUnsignedByte(pos, (short) 200);
System.out.println(buff.getUnsignedByte(pos));
```

The console shows '200'.

### Buffer length

Use `length` to obtain the length of the buffer. The length of a buffer is the index of the byte in the buffer with the largest index + 1.

### Copying buffers

Use `copy` to make a copy of the buffer

### Slicing buffers

A sliced buffer is a new buffer which backs onto the original buffer, i.e. it does not copy the underlying data. Use `slice` to create a sliced buffers

### Buffer re-use

After writing a buffer to a socket or other similar place, they cannot be re-used.


## Writing TCP servers and clients

Vert.x allows you to easily write non-blocking TCP clients and servers.

### Creating a TCP server

The simplest way to create a TCP server, using all default options is as follows:

```
NetServer server = vertx.createNetServer();
```

### Configuring a TCP server

If you don’t want the default, a server can be configured by passing in a `TcpServerConfig` instance when creating it:

```
TcpServerConfig config = new TcpServerConfig()
  .setPort(4321);

NetServer server = vertx.createNetServer(config);
```

### Start the Server Listening

To tell the server to listen for incoming requests you use one of the `listen` alternatives.

To tell the server to listen at the host and port as specified in the options:

```
NetServer server = vertx.createNetServer();
server.listen();
```

Or to specify the host and port in the call to listen, ignoring what is configured in the options:

```
NetServer server = vertx.createNetServer();
server.listen(1234, "localhost");
```

The default host is `0.0.0.0` which means 'listen on all available addresses' and the default port is `0`, which is a special value that instructs the server to find a random unused local port and use that.

The actual bind is asynchronous, so the server might not actually be listening until some time **after** the call to listen has returned.

If you want to be notified when the server is actually listening you can provide a handler to the `listen` call. For example:

```
NetServer server = vertx.createNetServer();
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

To find out the real port the server is listening on you can call `actualPort`.

```
NetServer server = vertx.createNetServer();
server
  .listen(0, "localhost")
  .onComplete(res -> {
    if (res.succeeded()) {
      System.out.println("Server is now listening on actual port: " + server.actualPort());
    } else {
      System.out.println("Failed to bind!");
    }
  });
```

### Listening to Unix domain sockets

When running on JDK 16+, or using a native transport, a server can listen to Unix domain sockets:

```
NetServer netServer = vertx.createNetServer();

// Only available when running on JDK16+, or using a native transport
SocketAddress address = SocketAddress.domainSocketAddress("/var/tmp/myservice.sock");

netServer
  .connectHandler(so -> {
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

### Getting notified of incoming connections

To be notified when a connection is made you need to set a `connectHandler`:

```
NetServer server = vertx.createNetServer();
server.connectHandler(socket -> {
  // Handle the connection in here
});
```

When a connection is made the handler will be called with an instance of `NetSocket`.

This is a socket-like interface to the actual connection, and allows you to read and write data as well as do various other things like close the socket.

### Reading data from the socket

To read data from the socket you set the `handler` on the socket.

This handler will be called with an instance of `Buffer` every time data is received on the socket.

```
NetServer server = vertx.createNetServer();
server.connectHandler(socket -> {
  socket.handler(buffer -> {
    System.out.println("I received some bytes: " + buffer.length());
  });
});
```

### Writing data to a socket

You write to a socket using one of `write`.

```
Buffer buffer = Buffer.buffer().appendFloat(12.34f).appendInt(123);
socket.write(buffer);

// Write a string in UTF-8 encoding
socket.write("some data");

// Write a string using the specified encoding
socket.write("some data", "UTF-16");
```

Write operations are asynchronous and may not occur until some time after the call to write has returned.

### Closed handler

If you want to be notified when a socket is closed, you can set a `closeHandler` on it:

```
socket.closeHandler(v -> {
  System.out.println("The socket has been closed");
});
```

### Handling exceptions

You can set an `exceptionHandler` to receive any exceptions that happen on the socket.

You can set an `exceptionHandler` to receive any exceptions that happens before the connection is passed to the `connectHandler` , e.g during the TLS handshake.

### Local and remote addresses

The local address of a `NetSocket` can be retrieved using `localAddress`.

The remote address, (i.e. the address of the other end of the connection) of a `NetSocket` can be retrieved using `remoteAddress`.

### Sending files or resources from the classpath

Files and classpath resources can be written to the socket directly using `sendFile`. This can be a very efficient way to send files, as it can be handled by the OS kernel directly where supported by the operating system.

Please see the chapter about serving files from the classpath for restrictions of the classpath resolution or disabling it.

```
socket
  .sendFile("myfile.dat")
  .onSuccess(v -> System.out.println("File successfully sent"))
  .onFailure(err -> System.out.println("Could not send file: " + err.getMessage()));
```

### Streaming sockets

Instances of `NetSocket` are also `ReadStream` and `WriteStream` instances, so they can be used to pipe data to or from other read and write streams.

See the chapter on streams for more information.

### TCP graceful shut down

You can shut down a `server` or `client`.

Calling `shutdown` initiates the shut-down phase whereby the server or client are given the opportunity to perform clean-up actions and handle shutdown at the protocol level.

```
server
  .shutdown()
  .onSuccess(res -> {
    System.out.println("Server is now closed");
  });
```

Shut-down waits until all sockets are closed or the shut-down timeout fires. When the timeout fires, all sockets are forcibly closed.

Each opened socket is notified with a shutdown event, allowing to perform a protocol level close before the actual socket close.

```
socket.shutdownHandler(v -> {
  socket
    // Write close frame
    .write(closeFrame())
    // Wait until we receive the remote close frame
    .compose(success -> closeFrameHandler(socket))
    // Close the socket
    .eventually(() -> socket.close());
});
```

Any socket without a shutdown handler is closed immediately

The default shut-down timeout is 30 seconds, you can override the amount of time

```
server
  .shutdown(Duration.ofSeconds(60))
  .onSuccess(res -> {
    System.out.println("Server is now closed");
  });
```

### TCP close

You can close a `server` or `client` to immediately close all open connections and releases all resources. Unlike `shutdown` there is not grace period.

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

If you’re creating TCP servers and clients from inside verticles, those servers and clients will be automatically closed when the verticle is undeployed.

### Scaling - sharing TCP servers

The handlers of any TCP server are always executed on the same event loop thread.

This means that if you are running on a server with a lot of cores, and you only have this one instance deployed then you will have at most one core utilised on your server.

In order to utilise more cores of your server you will need to deploy more instances of the server.

You can instantiate more instances programmatically in your code:

```
class MyVerticle extends VerticleBase {

  NetServer server;

  @Override
  public Future<?> start() {
    server = vertx.createNetServer();
    server.connectHandler(socket -> {
      socket.handler(buffer -> {
        // Just echo back the data
        socket.write(buffer);
      });
    });
    return server.listen(1234, "localhost");
  }
}

// Create a few instances so we can utilise cores
vertx.deployVerticle(MyVerticle.class, new DeploymentOptions().setInstances(10));
```

Once you do this you will find the echo server works functionally identically to before, but all your cores on your server can be utilised and more work can be handled.

At this point you might be asking yourself **'How can you have more than one server listening on the same host and port? Surely you will get port conflicts as soon as you try and deploy more than one instance?'**

*Vert.x does a little magic here.**

When you deploy another server on the same host and port as an existing server it doesn’t actually try and create a new server listening on the same host/port.

Instead it internally maintains just a single server, and, as incoming connections arrive it distributes them in a round-robin fashion to any of the connect handlers.

Consequently Vert.x TCP servers can scale over available cores while each instance remains single threaded.

### Creating a TCP client

The simplest way to create a TCP client, using all default options is as follows:

```
NetClient client = vertx.createNetClient();
```

### Configuring a TCP client

If you don’t want the default, a client can be configured by passing in a `TcpClientConfig` instance when creating it:

```
TcpClientConfig config = new TcpClientConfig()
  .setConnectTimeout(Duration.ofSeconds(10));

NetClient client = vertx.createNetClient(config);
```

### Making connections

To make a connection to a server you use `connect`, specifying the port and host of the server, returning a future completed with the `NetSocket`

```
TcpClientConfig options = new TcpClientConfig()
  .setConnectTimeout(Duration.ofSeconds(10));
NetClient client = vertx.createNetClient(options);
client
  .connect(4321, "localhost")
  .onComplete(res -> {
    if (res.succeeded()) {
      System.out.println("Connected!");
      NetSocket socket = res.result();
    } else {
      System.out.println("Failed to connect: " + res.cause().getMessage());
    }
  });
```

### Making connections to Unix domain sockets

When running on JDK 16+, or using a native transport, a client can connect to Unix domain sockets:

```
NetClient netClient = vertx.createNetClient();

// Only available when running on JDK16+, or using a native transport
SocketAddress addr = SocketAddress.domainSocketAddress("/var/tmp/myservice.sock");

// Connect to the server
netClient
  .connect(addr)
  .onComplete(ar -> {
    if (ar.succeeded()) {
      // Connected
    } else {
      // Handle failure
    }
  });
```

### Configuring connection attempts

A client can be configured to automatically retry connecting to the server in the event that it cannot connect. This is configured with `setReconnectInterval` and `setReconnectAttempts`.

|   | Currently, Vert.x will not attempt to reconnect if a connection fails, reconnect attempts and interval only apply to creating initial connections. |
|---|---|

```
TcpClientConfig options = new TcpClientConfig().
  setReconnectAttempts(10).
  setReconnectInterval(Duration.ofMillis(500));

NetClient client = vertx.createNetClient(options);
```

By default, multiple connection attempts are disabled.

### Logging network activity

For debugging purposes, network activity can be logged:

```
TcpServerConfig options = new TcpServerConfig()
  .setLogConfig(new LogConfig()
    .setEnabled(true));

NetServer server = vertx.createNetServer(options);
```

Here is the output of a simple HTTP server

```
id: 0x359e3df6, L:/127.0.0.1:8080 - R:/127.0.0.1:65351] READ: 78B
         +-------------------------------------------------+
         |  0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f |
+--------+-------------------------------------------------+----------------+
|00000000| 47 45 54 20 2f 20 48 54 54 50 2f 31 2e 31 0d 0a |GET / HTTP/1.1..|
|00000010| 48 6f 73 74 3a 20 6c 6f 63 61 6c 68 6f 73 74 3a |Host: localhost:|
|00000020| 38 30 38 30 0d 0a 55 73 65 72 2d 41 67 65 6e 74 |8080..User-Agent|
|00000030| 3a 20 63 75 72 6c 2f 37 2e 36 34 2e 31 0d 0a 41 |: curl/7.64.1..A|
|00000040| 63 63 65 70 74 3a 20 2a 2f 2a 0d 0a 0d 0a       |ccept: */*....  |
+--------+-------------------------------------------------+----------------+
[id: 0x359e3df6, L:/127.0.0.1:8080 - R:/127.0.0.1:65351] WRITE: 50B
         +-------------------------------------------------+
         |  0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f |
+--------+-------------------------------------------------+----------------+
|00000000| 48 54 54 50 2f 31 2e 31 20 32 30 30 20 4f 4b 0d |HTTP/1.1 200 OK.|
|00000010| 0a 63 6f 6e 74 65 6e 74 2d 6c 65 6e 67 74 68 3a |.content-length:|
|00000020| 20 31 31 0d 0a 0d 0a 48 65 6c 6c 6f 20 57 6f 72 | 11....Hello Wor|
|00000030| 6c 64                                           |ld              |
+--------+-------------------------------------------------+----------------+
[id: 0x359e3df6, L:/127.0.0.1:8080 - R:/127.0.0.1:65351] READ COMPLETE
[id: 0x359e3df6, L:/127.0.0.1:8080 - R:/127.0.0.1:65351] FLUSH
```

By default, binary data is logged in hex format.

You can reduce the data format verbosity to only print the buffer length instead of the entire data by setting the log data fomat.

```
TcpServerConfig options = new TcpServerConfig()
  .setLogConfig(new LogConfig()
    .setEnabled(true)
    .setDataFormat(ByteBufFormat.SIMPLE));

NetServer server = vertx.createNetServer(options);
```

Here is the same output with simple buffer format

```
[id: 0xda8d41dc, L:/127.0.0.1:8080 - R:/127.0.0.1:65399] READ: 78B
[id: 0xda8d41dc, L:/127.0.0.1:8080 - R:/127.0.0.1:65399] WRITE: 50B
[id: 0xda8d41dc, L:/127.0.0.1:8080 - R:/127.0.0.1:65399] READ COMPLETE
[id: 0xda8d41dc, L:/127.0.0.1:8080 - R:/127.0.0.1:65399] FLUSH
[id: 0xda8d41dc, L:/127.0.0.1:8080 - R:/127.0.0.1:65399] READ COMPLETE
[id: 0xda8d41dc, L:/127.0.0.1:8080 ! R:/127.0.0.1:65399] INACTIVE
[id: 0xda8d41dc, L:/127.0.0.1:8080 ! R:/127.0.0.1:65399] UNREGISTERED
```

Clients can also log network activity

```
TcpClientConfig options = new TcpClientConfig()
  .setLogConfig(new LogConfig()
    .setEnabled(true));

NetClient client = vertx.createNetClient(options);
```

Network activity is logged by Netty with the `DEBUG` level and with the `io.netty.handler.logging.LoggingHandler` name. When using network activity logging there are a few things to keep in mind:

- logging is not performed by Vert.x logging but by Netty
- this is **not** a production feature

You should read the Netty logging section.

### Throttling inbound and outbound bandwidth of TCP connections

TCP server can be configured with traffic shaping options to enable bandwidth limiting. Both inbound and outbound bandwidth can be limited through `TrafficShapingOptions`. You can set traffic shaping options through `TcpServerConfig`.

```
TcpServerConfig config = new TcpServerConfig()
  .setHost("localhost")
  .setPort(1234)
  .setTrafficShapingOptions(new TrafficShapingOptions()
    .setInboundGlobalBandwidth(64 * 1024)
    .setOutboundGlobalBandwidth(128 * 1024));

NetServer server = vertx.createNetServer(config);
```

These traffic shaping options can also be dynamically updated after server start.

```
TcpServerConfig config = new TcpServerConfig()
  .setHost("localhost")
  .setPort(1234)
  .setTrafficShapingOptions(new TrafficShapingOptions()
    .setInboundGlobalBandwidth(64 * 1024)
    .setOutboundGlobalBandwidth(128 * 1024));

NetServer server = vertx.createNetServer(config);

TrafficShapingOptions update = new TrafficShapingOptions()
  .setInboundGlobalBandwidth(2 * 64 * 1024) // twice
  .setOutboundGlobalBandwidth(128 * 1024); // unchanged

server
  .listen(1234, "localhost")
  // wait until traffic shaping handler is created for updates
  .onSuccess(v -> server.updateTrafficShapingOptions(update));
```

### Configuring servers and clients to work with SSL/TLS

TCP clients and servers can be configured to use Transport Layer Security - earlier versions of TLS were known as SSL.

The APIs of the servers and clients are identical whether SSL/TLS is used, and it’s enabled by configuring the `TcpClientConfig` or `TcpServerConfig` instances used to create the servers or clients.

#### Enabling SSL/TLS on the server

Server SSL/TLS is enabled with the `TcpServerConfig` `ssl` setting.

By default, it is disabled.

```
ServerSSLOptions sslOptions = new ServerSSLOptions()
  .setKeyCertOptions(
    new JksOptions().
      setPath("/path/to/your/server-keystore.jks").
      setPassword("password-of-your-keystore")
  );

TcpServerConfig config = new TcpServerConfig()
  .setSsl(true);

NetServer server = vertx.createNetServer(config, sslOptions);
```

You can read more about SSL server configuration

#### Enabling SSL/TLS on the client

Client SSL/TLS is enabled with the `TcpClientConfig` `ssl` property or `ssl` property.

The former defines the default client behavior.

When enabled, the client performs an SSL/TLS handshake with the provided SSL configuration.

```
ClientSSLOptions sslOptions = new ClientSSLOptions()
  .setTrustOptions(new JksOptions().
    setPath("/path/to/your/truststore.jks").
    setPassword("password-of-your-truststore")
  );

TcpClientConfig config = new TcpClientConfig()
  .setSsl(true);

NetClient client = vertx.createNetClient(config, sslOptions);
```

The latter provides a fine-grained per socket configuration

```
ClientSSLOptions sslOptions = new ClientSSLOptions()
  .setTrustOptions(new JksOptions().
    setPath("/path/to/your/truststore.jks").
    setPassword("password-of-your-truststore")
  );

TcpClientConfig config = new TcpClientConfig();

NetClient client = vertx.createNetClient(config, sslOptions);

Future<NetSocket> future = client.connect(new ConnectOptions()
  .setHost(host)
  .setPort(port)
  .setSsl(true)
);
```

You can also set `ClientSSLOptions` at connect time.

```
NetClient client = vertx.createNetClient();

ClientSSLOptions sslOptions = new ClientSSLOptions()
  .setTrustOptions(new JksOptions().
    setPath("/path/to/your/truststore.jks").
    setPassword("password-of-your-truststore")
  );

Future<NetSocket> future = client.connect(new ConnectOptions()
  .setHost(host)
  .setPort(port)
  .setSsl(true)
  .setSslOptions(sslOptions)
);
```

You can read more about SSL client configuration.

#### Client Server Name Indication (SNI)

The client implicitly sends the connecting host as an SNI server name for Fully Qualified Domain Name (FQDN).

You can provide an explicit server name when connecting a socket

```
NetClient client = vertx.createNetClient(
  new TcpClientConfig().setSsl(true),
  new ClientSSLOptions().setTrustOptions(trustOptions)
);

// Connect to 'localhost' and present 'server.name' server name
client
  .connect(1234, "localhost", "server.name")
  .onComplete(res -> {
    if (res.succeeded()) {
      System.out.println("Connected!");
      NetSocket socket = res.result();
    } else {
      System.out.println("Failed to connect: " + res.cause().getMessage());
    }
  });
```

It can be used for different purposes:

- present a server name different than the server host
- present a server name while connecting to an IP
- force to present a server name when using shortname

#### Client host verification

By default, host verification is **not** configured on the client. This verifies the CN portion of the server certificate against the server hostname to avoid Man-in-the-middle attacks.

You must configure it explicitly on your client

- `""` (empty string) disables host verification
- `"HTTPS"` enables HTTP over TLS verification
- `LDAPS` enables LDAP v3 extension for TLS verification

```
TcpClientConfig config = new TcpClientConfig().
  setSsl(true);

ClientSSLOptions sslOptions = new ClientSSLOptions()
  .setTrustOptions(trustOptions)
  .setHostnameVerificationAlgorithm(verificationAlgorithm);

NetClient client = vertx.createNetClient(config, sslOptions);
```

|   | the Vert.x HTTP client uses the TCP client and configures with `"HTTPS"` the verification algorithm. |
|---|---|

#### Upgrading connections to SSL/TLS

A non SSL/TLS connection can be upgraded to SSL/TLS using `upgradeToSsl`.

```
socket.upgradeToSsl()
  .onSuccess(v -> {
    // Upgrade worked
  }).onFailure(err -> {
    // Upgrade failed
  });

// Use the specified SSL options
socket.upgradeToSsl(sslOptions)
  .onSuccess(v -> {
    // Upgrade worked
  }).onFailure(err -> {
    // Upgrade failed
  });
```

|   | usually client and server perform the handshake upgrade simultaneously, this is usually known as StartTLS and it used in protocols that start a conversation in plain text and decide to upgrade the connection with a TLS handshake |
|---|---|

#### Updating SSL/TLS configuration

You can use the `updateSSLOptions` method to update the key/certifications or trust on a TCP server or client (e.g. to implement certificate rotation).

```
Future<Boolean> fut = server.updateSSLOptions(new ServerSSLOptions()
  .setKeyCertOptions(
    new JksOptions()
      .setPath("/path/to/your/server-keystore.jks").
      setPassword("password-of-your-keystore")));
```

When the update succeeds the new SSL configuration is used, otherwise the previous configuration is preserved.

|   | The options object is compared (using `equals`) against the existing options to prevent an update when the objects are equals since loading options can be costly. When object are equals, you can use the `force` parameter to force the update. |
|---|---|

### Using a proxy for client connections

The `NetClient` supports either an HTTP/1.x *CONNECT*, *SOCKS4a* or *SOCKS5* proxy.

The proxy can be configured in the `TcpClientConfig` by setting a `ProxyOptions` object containing proxy type, hostname, port and optionally username and password.

Here’s an example:

```
TcpClientConfig config = new TcpClientConfig()
  .setProxyOptions(new ProxyOptions().setType(ProxyType.SOCKS5)
    .setHost("localhost").setPort(1080)
    .setUsername("username").setPassword("secret"));
NetClient client = vertx.createNetClient(config);
```

The DNS resolution is always done on the proxy server, to achieve the functionality of a SOCKS4 client, it is necessary to resolve the DNS address locally.

You can use `setNonProxyHosts` to configure a list of host bypassing the proxy. The lists accepts `*` wildcard for matching domains:

```
TcpClientConfig config = new TcpClientConfig()
  .setProxyOptions(new ProxyOptions().setType(ProxyType.SOCKS5)
    .setHost("localhost").setPort(1080)
    .setUsername("username").setPassword("secret"))
  .addNonProxyHost("*.foo.com")
  .addNonProxyHost("localhost");
NetClient client = vertx.createNetClient(config);
```

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
TcpServerConfig config = new TcpServerConfig().setUseProxyProtocol(true);
NetServer server = vertx.createNetServer(config);
server.connectHandler(so -> {
  // Print the actual client address provided by the HA proxy protocol instead of the proxy address
  System.out.println(so.remoteAddress());

  // Print the address of the proxy
  System.out.println(so.localAddress());
});
```
