---
title: "Vert.x Core (part 7/8)"
source: https://vertx.io/docs/vertx-core/java/
domain: vertx
license: CC-BY-SA-4.0
tags: vert.x toolkit, eclipse vertx, reactive toolkit, event loop server
fetched: 2026-07-02
part: 7/8
---

## Datagram sockets (UDP)

Using User Datagram Protocol (UDP) with Vert.x is a piece of cake.

UDP is a connection-less transport which basically means you have no persistent connection to a remote peer.

Instead, you can send and receive packages and the remote address is contained in each of them.

Beside this UDP is not as safe as TCP to use, which means there are no guarantees that a send Datagram packet will receive it’s endpoint at all.

The only guarantee is that it will either receive complete or not at all.

Also, you usually can’t send data which is bigger then the MTU size of your network interface, this is because each packet will be send as one packet.

But, be aware even if the packet size is smaller then the MTU it may still fail.

At which size it will fail depends on the Operating System etc. So rule of thumb is to try to send small packets.

Because of the nature of UDP it is best fit for Applications where you are allowed to drop packets (like for example a monitoring application).

The benefits are that it has a lot less overhead compared to TCP, which can be handled by the NetServer and NetClient (see above).

### Creating a DatagramSocket

To use UDP you first need to create a `DatagramSocket`. It does not matter here if you only want to send data or send and receive.

```
DatagramSocket socket = vertx.createDatagramSocket(new DatagramSocketOptions());
```

The returned `DatagramSocket` will not be bound to a specific port. This is not a problem if you only want to send data (like a client), but more on this in the next section.

### Sending Datagram packets

As mentioned before, User Datagram Protocol (UDP) sends data in packets to remote peers but is not connected to them in a persistent fashion.

This means each packet can be sent to a different remote peer.

Sending packets is as easy as shown here:

```
DatagramSocket socket = vertx.createDatagramSocket(new DatagramSocketOptions());
Buffer buffer = Buffer.buffer("content");
// Send a Buffer
socket
  .send(buffer, 1234, "10.0.0.1")
  .onComplete(asyncResult -> System.out.println("Send succeeded? " + asyncResult.succeeded()));
// Send a String
socket
  .send("A string used as content", 1234, "10.0.0.1")
  .onComplete(asyncResult -> System.out.println("Send succeeded? " + asyncResult.succeeded()));
```

### Receiving Datagram packets

If you want to receive packets you need to bind the `DatagramSocket` by calling `listen(…)` on it.

This way you will be able to receive DatagramPacket`s that were sent to the address and port on which the `DatagramSocket listens.

Beside this you also want to set a `Handler` which will be called for each received `DatagramPacket`.

The `DatagramPacket` has the following methods:

- `sender`: The InetSocketAddress which represent the sender of the packet
- `data`: The Buffer which holds the data which was received.

So to listen on a specific address and port you would do something like shown here:

```
DatagramSocket socket = vertx.createDatagramSocket(new DatagramSocketOptions());
socket
  .handler(packet -> {
    // Do something with the packet
  })
  .listen(1234, "0.0.0.0")
  .onComplete(asyncResult -> System.out.println("Send succeeded? " + asyncResult.succeeded()));
;
```

Be aware that even if the {code AsyncResult} is successed it only means it might be written on the network stack, but gives no guarantee that it ever reached or will reach the remote peer at all.

If you need such a guarantee then you want to use TCP with some handshaking logic build on top.

### Multicast

#### Sending Multicast packets

Multicast allows multiple sockets to receive the same packets. This works by having the sockets join the same multicast group to which you can then send packets.

We will look at how you can join a Multicast Group and receive packets in the next section.

Sending multicast packets is not different from sending normal Datagram packets. The difference is that you pass in a multicast group address to the send method.

This is show here:

```
DatagramSocket socket = vertx.createDatagramSocket(new DatagramSocketOptions());
Buffer buffer = Buffer.buffer("content");
// Send a Buffer to a multicast address
socket
  .send(buffer, 1234, "230.0.0.1")
  .onComplete(asyncResult -> System.out.println("Send succeeded? " + asyncResult.succeeded()));
```

All sockets that have joined the multicast group 230.0.0.1 will receive the packet.

##### Receiving Multicast packets

If you want to receive packets for specific Multicast group you need to bind the `DatagramSocket` by calling `listen(…)` on it to join the Multicast group.

This way you will receive DatagramPackets that were sent to the address and port on which the `DatagramSocket` listens and also to those sent to the Multicast group.

Beside this you also want to set a Handler which will be called for each received DatagramPacket.

The `DatagramPacket` has the following methods:

- `sender()`: The InetSocketAddress which represent the sender of the packet
- `data()`: The Buffer which holds the data which was received.

So to listen on a specific address and port and also receive packets for the Multicast group 230.0.0.1 you would do something like shown here:

```
DatagramSocket socket = vertx.createDatagramSocket(new DatagramSocketOptions());
socket
  .handler(packet -> {
    // Do something with the packet
  })
  .listen(1234, "0.0.0.0")
  .compose(v -> socket.listenMulticastGroup("230.0.0.1")) // join the multicast group
  .onComplete(asyncResult -> System.out.println("Listen succeeded? " + asyncResult.succeeded()));
```

##### Unlisten / leave a Multicast group

There are sometimes situations where you want to receive packets for a Multicast group for a limited time.

In this situations you can first start to listen for them and then later unlisten.

This is shown here:

```
DatagramSocket socket = vertx.createDatagramSocket(new DatagramSocketOptions());
socket
  .handler(packet -> {
    // Do something with the packet
  })
  .listen(1234, "0.0.0.0")
  .compose(v -> socket.listenMulticastGroup("230.0.0.1")) // join the multicast group
  .onComplete(asyncResult -> {
    if (asyncResult.succeeded()) {
      // will now receive packets for group

      // do some work

      socket.unlistenMulticastGroup("230.0.0.1").onComplete(asyncResult2 -> {
        System.out.println("Unlisten succeeded? " + asyncResult2.succeeded());
      });
    } else {
      System.out.println("Listen failed" + asyncResult.cause());
    }
  });
```

##### Blocking multicast

Beside unlisten a Multicast address it’s also possible to just block multicast for a specific sender address.

Be aware this only work on some Operating Systems and kernel versions. So please check the Operating System documentation if it’s supported.

This an expert feature.

To block multicast from a specific address you can call `blockMulticastGroup(…)` on the DatagramSocket like shown here:

```
DatagramSocket socket = vertx.createDatagramSocket(new DatagramSocketOptions());

// Some code

// This would block packets which are send from 10.0.0.2
socket
  .blockMulticastGroup("230.0.0.1", "10.0.0.2")
  .onComplete(asyncResult -> System.out.println("block succeeded? " + asyncResult.succeeded()));
```

#### DatagramSocket properties

When creating a `DatagramSocket` there are multiple properties you can set to change it’s behaviour with the `DatagramSocketOptions` object. Those are listed here:

- `setSendBufferSize` Sets the send buffer size in bytes.
- `setReceiveBufferSize` Sets the TCP receive buffer size in bytes.
- `setReuseAddress` If true then addresses in TIME_WAIT state can be reused after they have been closed.
- `setTrafficClass`
- `setBroadcast` Sets or clears the SO_BROADCAST socket option. When this option is set, Datagram (UDP) packets may be sent to a local interface’s broadcast address.
- `setMulticastNetworkInterface` Sets or clears the IP_MULTICAST_LOOP socket option. When this option is set, multicast packets will also be received on the local interface.
- `setMulticastTimeToLive` Sets the IP_MULTICAST_TTL socket option. TTL stands for "Time to Live," but in this context it specifies the number of IP hops that a packet is allowed to go through, specifically for multicast traffic. Each router or gateway that forwards a packet decrements the TTL. If the TTL is decremented to 0 by a router, it will not be forwarded.

#### DatagramSocket Local Address

You can find out the local address of the socket (i.e. the address of this side of the UDP Socket) by calling `localAddress`. This will only return an `InetSocketAddress` if you bound the `DatagramSocket` with `listen(…)` before, otherwise it will return null.

#### Closing a DatagramSocket

You can close a socket by invoking the `close` method. This will close the socket and release all resources


## DNS client

Often you will find yourself in situations where you need to obtain DNS informations in an asynchronous fashion. Unfortunally this is not possible with the API that is shipped with the Java Virtual Machine itself. Because of this Vert.x offers it’s own API for DNS resolution which is fully asynchronous.

To obtain a DnsClient instance you will create a new via the Vertx instance.

```
DnsClient client = vertx.createDnsClient(53, "10.0.0.1");
```

You can also create the client with options and configure the query timeout.

```
DnsClient client = vertx.createDnsClient(new DnsClientOptions()
  .setPort(53)
  .setHost("10.0.0.1")
  .setQueryTimeout(10000)
);
```

Creating the client with no arguments or omitting the server address will use the address of the server used internally for non blocking address resolution.

```
DnsClient client1 = vertx.createDnsClient();

// Just the same but with a different query timeout
DnsClient client2 = vertx.createDnsClient(new DnsClientOptions().setQueryTimeout(10000));
```

A client uses a single event loop for querying purposes, it can safely be used from any thread, including non Vert.x thread.

### lookup

Try to lookup the A (ipv4) or AAAA (ipv6) record for a given name. The first which is returned will be used, so it behaves the same way as you may be used from when using "nslookup" on your operation system.

To lookup the A / AAAA record for "vertx.io" you would typically use it like:

```
DnsClient client = vertx.createDnsClient(53, "9.9.9.9");
client
  .lookup("vertx.io")
  .onComplete(ar -> {
    if (ar.succeeded()) {
      System.out.println(ar.result());
    } else {
      System.out.println("Failed to resolve entry" + ar.cause());
    }
  });
```

### lookup4

Try to lookup the A (ipv4) record for a given name. The first which is returned will be used, so it behaves the same way as you may be used from when using "nslookup" on your operation system.

To lookup the A record for "vertx.io" you would typically use it like:

```
DnsClient client = vertx.createDnsClient(53, "9.9.9.9");
client
  .lookup4("vertx.io")
  .onComplete(ar -> {
    if (ar.succeeded()) {
      System.out.println(ar.result());
    } else {
      System.out.println("Failed to resolve entry" + ar.cause());
    }
  });
```

### lookup6

Try to lookup the AAAA (ipv6) record for a given name. The first which is returned will be used, so it behaves the same way as you may be used from when using "nslookup" on your operation system.

To lookup the A record for "vertx.io" you would typically use it like:

```
DnsClient client = vertx.createDnsClient(53, "9.9.9.9");
client
  .lookup6("vertx.io")
  .onComplete(ar -> {
    if (ar.succeeded()) {
      System.out.println(ar.result());
    } else {
      System.out.println("Failed to resolve entry" + ar.cause());
    }
  });
```

### resolveA

Try to resolve all A (ipv4) records for a given name. This is quite similar to using "dig" on unix like operation systems.

To lookup all the A records for "vertx.io" you would typically do:

```
DnsClient client = vertx.createDnsClient(53, "9.9.9.9");
client
  .resolveA("vertx.io")
  .onComplete(ar -> {
    if (ar.succeeded()) {
      List<String> records = ar.result();
      for (String record : records) {
        System.out.println(record);
      }
    } else {
      System.out.println("Failed to resolve entry" + ar.cause());
    }
  });
```

### resolveAAAA

Try to resolve all AAAA (ipv6) records for a given name. This is quite similar to using "dig" on unix like operation systems.

To lookup all the AAAAA records for "vertx.io" you would typically do:

```
DnsClient client = vertx.createDnsClient(53, "9.9.9.9");
client
  .resolveAAAA("vertx.io")
  .onComplete(ar -> {
    if (ar.succeeded()) {
      List<String> records = ar.result();
      for (String record : records) {
        System.out.println(record);
      }
    } else {
      System.out.println("Failed to resolve entry" + ar.cause());
    }
  });
```

### resolveCNAME

Try to resolve all CNAME records for a given name. This is quite similar to using "dig" on unix like operation systems.

To lookup all the CNAME records for "vertx.io" you would typically do:

```
DnsClient client = vertx.createDnsClient(53, "9.9.9.9");
client
  .resolveCNAME("vertx.io")
  .onComplete(ar -> {
    if (ar.succeeded()) {
      List<String> records = ar.result();
      for (String record : records) {
        System.out.println(record);
      }
    } else {
      System.out.println("Failed to resolve entry" + ar.cause());
    }
  });
```

### resolveMX

Try to resolve all MX records for a given name. The MX records are used to define which Mail-Server accepts emails for a given domain.

To lookup all the MX records for "vertx.io" you would typically do:

```
DnsClient client = vertx.createDnsClient(53, "9.9.9.9");
client
  .resolveMX("vertx.io")
  .onComplete(ar -> {
    if (ar.succeeded()) {
      List<MxRecord> records = ar.result();
      for (MxRecord record : records) {
        System.out.println(record);
      }
    } else {
      System.out.println("Failed to resolve entry" + ar.cause());
    }
  });
```

Be aware that the List will contain the `MxRecord` sorted by the priority of them, which means MX records with smaller priority coming first in the List.

The `MxRecord` allows you to access the priority and the name of the MX record by offer methods for it like:

```
record.priority();
record.name();
```

### resolveTXT

Try to resolve all TXT records for a given name. TXT records are often used to define extra information for a domain.

To resolve all the TXT records for "vertx.io" you could use something along these lines:

```
DnsClient client = vertx.createDnsClient(53, "9.9.9.9");
client
  .resolveTXT("vertx.io")
  .onComplete(ar -> {
    if (ar.succeeded()) {
      List<String> records = ar.result();
      for (String record : records) {
        System.out.println(record);
      }
    } else {
      System.out.println("Failed to resolve entry" + ar.cause());
    }
  });
```

### resolveNS

Try to resolve all NS records for a given name. The NS records specify which DNS Server hosts the DNS informations for a given domain.

To resolve all the NS records for "vertx.io" you could use something along these lines:

```
DnsClient client = vertx.createDnsClient(53, "9.9.9.9");
client
  .resolveNS("vertx.io")
  .onComplete(ar -> {
    if (ar.succeeded()) {
      List<String> records = ar.result();
      for (String record : records) {
        System.out.println(record);
      }
    } else {
      System.out.println("Failed to resolve entry" + ar.cause());
    }
  });
```

### resolveSRV

Try to resolve all SRV records for a given name. The SRV records are used to define extra information like port and hostname of services. Some protocols need this extra information.

To lookup all the SRV records for "vertx.io" you would typically do:

```
DnsClient client = vertx.createDnsClient(53, "9.9.9.9");
client
  .resolveSRV("vertx.io")
  .onComplete(ar -> {
    if (ar.succeeded()) {
      List<SrvRecord> records = ar.result();
      for (SrvRecord record : records) {
        System.out.println(record);
      }
    } else {
      System.out.println("Failed to resolve entry" + ar.cause());
    }
  });
```

Be aware that the List will contain the SrvRecords sorted by the priority of them, which means SrvRecords with smaller priority coming first in the List.

The `SrvRecord` allows you to access all information contained in the SRV record itself:

```
record.priority();
record.name();
record.weight();
record.port();
record.protocol();
record.service();
record.target();
```

Please refer to the API docs for the exact details.

### resolvePTR

Try to resolve the PTR record for a given name. The PTR record maps an ipaddress to a name.

To resolve the PTR record for the ipaddress 10.0.0.1 you would use the PTR notion of "1.0.0.10.in-addr.arpa"

```
DnsClient client = vertx.createDnsClient(53, "9.9.9.9");
client
  .resolvePTR("1.0.0.10.in-addr.arpa")
  .onComplete(ar -> {
    if (ar.succeeded()) {
      String record = ar.result();
      System.out.println(record);
    } else {
      System.out.println("Failed to resolve entry" + ar.cause());
    }
  });
```

### reverseLookup

Try to do a reverse lookup for an ipaddress. This is basically the same as resolve a PTR record, but allows you to just pass in the ipaddress and not a valid PTR query string.

To do a reverse lookup for the ipaddress 10.0.0.1 do something similar like this:

```
DnsClient client = vertx.createDnsClient(53, "9.9.9.9");
client
  .reverseLookup("10.0.0.1")
  .onComplete(ar -> {
    if (ar.succeeded()) {
      String record = ar.result();
      System.out.println(record);
    } else {
      System.out.println("Failed to resolve entry" + ar.cause());
    }
  });
```

### Error handling

As you saw in previous sections the DnsClient allows you to pass in a Handler which will be notified with an AsyncResult once the query was complete. In case of an error it will be notified with a DnsException which will hole a `DnsResponseCode` that indicate why the resolution failed. This DnsResponseCode can be used to inspect the cause in more detail.

Possible DnsResponseCodes are:

- `NOERROR` No record was found for a given query
- `FORMERROR` Format error
- `SERVFAIL` Server failure
- `NXDOMAIN` Name error
- `NOTIMPL` Not implemented by DNS Server
- `REFUSED` DNS Server refused the query
- `YXDOMAIN` Domain name should not exist
- `YXRRSET` Resource record should not exist
- `NXRRSET` RRSET does not exist
- `NOTZONE` Name not in zone
- `BADVERS` Bad extension mechanism for version
- `BADSIG` Bad signature
- `BADKEY` Bad key
- `BADTIME` Bad timestamp

All of those errors are "generated" by the DNS Server itself.

You can obtain the DnsResponseCode from the DnsException like:

```
DnsClient client = vertx.createDnsClient(53, "10.0.0.1");
client
  .lookup("nonexisting.vert.xio")
  .onComplete(ar -> {
    if (ar.succeeded()) {
      String record = ar.result();
      System.out.println(record);
    } else {
      Throwable cause = ar.cause();
      if (cause instanceof DnsException) {
        DnsException exception = (DnsException) cause;
        DnsResponseCode code = exception.code();
        // ...
      } else {
        System.out.println("Failed to resolve entry" + ar.cause());
      }
    }
  });
```


## Vert.x Virtual Threads

Use virtual threads to write Vert.x code that looks like it is synchronous.

You still write the traditional Vert.x code processing events, but you have the opportunity to write synchronous code for complex workflows and use thread locals in such workflows.

### Introduction

The non-blocking nature of Vert.x leads to asynchronous APIs. Asynchronous APIs can take various forms including callback style, promises and reactive extensions.

In some cases, programming using asynchronous APIs can be more challenging than using a direct synchronous style, in particular if you have several operations that you want to do sequentially. Also, error propagation is often more complex when using asynchronous APIs.

Virtual thread support allows you to work with asynchronous APIs, but using a direct synchronous style that you’re already familiar with.

It does this by using Java 21 virtual threads. Virtual threads are very lightweight threads that do not correspond to underlying kernel threads. When they are blocked they do not block a kernel thread.

### Using virtual threads

You can deploy virtual thread verticles.

A virtual thread verticle is capable of awaiting Vert.x futures and gets the result synchronously.

When the verticle **awaits** a result, the verticle can still process events like an event-loop verticle.

```
AbstractVerticle verticle = new AbstractVerticle() {
  @Override
  public void start() {
    HttpClient client = vertx.createHttpClient();
    HttpClientRequest req = client.request(
      HttpMethod.GET,
      8080,
      "localhost",
      "/").await();
    HttpClientResponse resp = req.send().await();
    int status = resp.statusCode();
    Buffer body = resp.body().await();
  }
};

// Run the verticle a on virtual thread
vertx.deployVerticle(verticle, new DeploymentOptions().setThreadingModel(ThreadingModel.VIRTUAL_THREAD));
```

|   | Using virtual threads requires Java 21 or above. |
|---|---|

#### Blocking within a virtual thread verticle

You can use `await` to suspend the current virtual thread until the awaited result is available.

The virtual thread is effectively blocked, but the application can still process events.

When a virtual thread awaits for a result and the verticle needs to process a task, a new virtual thread is created to handle this task.

When the result is available, the virtual thread execution is resumed and scheduled after the current task is suspended or finished.

|   | Like any verticle at most one task is executed at the same time. |
|---|---|

You can await on a Vert.x `Future`

```
Buffer body = response.body().await();
```

or on a JDK `CompletionStage`

```
Buffer body = Future.fromCompletionStage(completionStage).await();
```

You can also transform a Vert.x `ReadStream` to a Java blocking stream:

```
server.requestHandler(request -> {
  Stream<Buffer> blockingStream = request.blockingStream();
  HttpServerResponse response = request.response();
  response.setChunked(true);
  blockingStream
    .map(buff -> "" + buff.length())
    .forEach(size -> response.write(size));
  response.end();
});
```

#### Field visibility

A virtual thread verticle can interact safely with fields before an `await` call. However, if you are reading a field before an `await` call and reusing the value after the call, you should keep in mind that this value might have changed.

```
int value = counter;
value += getRemoteValue().await();
// the counter value might have changed
counter = value;
```

You should read/write fields before calling `await` to avoid this.

```
counter += getRemoteValue().await();
```

|   | this is the same behavior with an event-loop verticle |
|---|---|

#### Awaiting multiple futures

When you need to await multiple futures, you can use Vert.x `CompositeFuture`:

```
Future<String> f1 = getRemoteString();
Future<Integer> f2 = getRemoteValue();
CompositeFuture res = Future.all(f1, f2).await();
String v1 = res.resultAt(0);
Integer v2 = res.resultAt(1);
```

#### Blocking without await

When your application blocks without using `await`, e.g. using `ReentrantLock#lock`, the Vert.x scheduler is not aware of it and cannot schedule events on the verticle: it behaves like a worker verticle, yet using virtual threads.

This use case is not encouraged yet not forbidden, however the verticle should be deployed with several instances to deliver the desired concurrency, like a worker verticle.

#### Thread local support

Thread locals are only reliable within the execution of a context task.

```
ThreadLocal<String> local = new ThreadLocal();
local.set(userId);
HttpClientRequest req = client.request(HttpMethod.GET, 8080, "localhost", "/").await();
HttpClientResponse resp = req.send().await();
```


## Streams

There are several objects in Vert.x that allow items to be read from and written.

In Vert.x, write calls return immediately, and writes are queued internally.

It’s not hard to see that if you write to an object faster than it can actually write the data to its underlying resource, then the write queue can grow unbounded - eventually resulting in memory exhaustion.

To solve this problem a simple flow control (*back-pressure*) capability is provided by some objects in the Vert.x API.

Any flow control aware object that can be *written-to* implements `WriteStream`, while any flow control object that can be *read-from* is said to implement `ReadStream`.

Let’s take an example where we want to read from a `ReadStream` then write the data to a `WriteStream`.

A very simple example would be reading data from a `NetSocket` then writing it to an `AsyncFile`.

|   | This works between any `ReadStream` and `WriteStream` compliant object, including HTTP requests, HTTP responses, async files I/O, WebSockets, etc. |
|---|---|

A naive way to do this would be to directly take the data that has been read and immediately write it:

```
NetServer server = vertx.createNetServer(
    new NetServerOptions().setPort(1234).setHost("localhost")
);
server.connectHandler(sock -> {
  sock.handler(buffer -> {
    // Write the data straight to the AsyncFile
    asyncFile.write(buffer);
  });
}).listen();
```

There is a problem with the example above: if data is read from the socket faster than it can be written to the file, it will build up in the write queue of the `AsyncFile`, eventually running out of RAM. This might happen, for example, if the actual file is stored on a slow network file system, effectively putting back-pressure on the connection.

Since `AsyncFile` implements `WriteStream`, we can check if the `WriteStream` is full before writing to it:

```
NetServer server = vertx.createNetServer(
    new NetServerOptions().setPort(1234).setHost("localhost")
);
server.connectHandler(sock -> {
  sock.handler(buffer -> {
    if (!asyncFile.writeQueueFull()) {
      asyncFile.write(buffer);
    }
  });
}).listen();
```

This example won’t run out of RAM, but we’ll end up losing data if the write queue gets full. What we really want to do is pause the `NetSocket` when the write queue is full:

```
NetServer server = vertx.createNetServer(
    new NetServerOptions().setPort(1234).setHost("localhost")
);
server.connectHandler(sock -> {
  sock.handler(buffer -> {
    asyncFile.write(buffer);
    if (asyncFile.writeQueueFull()) {
      sock.pause();
    }
  });
}).listen();
```

We’re almost there, but not quite. The `NetSocket` now gets paused when the file is full, but we also need to unpause it when the write queue has processed its backlog:

```
NetServer server = vertx.createNetServer(
    new NetServerOptions().setPort(1234).setHost("localhost")
);
server.connectHandler(sock -> {
  sock.handler(buffer -> {
    asyncFile.write(buffer);
    if (asyncFile.writeQueueFull()) {
      sock.pause();
      asyncFile.drainHandler(done -> {
        sock.resume();
      });
    }
  });
}).listen();
```

And there we have it. The `drainHandler` event handler will get called when the write queue is ready to accept more data, this resumes the `NetSocket` that allows more data to be read.

This use case is quite common while writing Vert.x applications, so we added the `pipeTo` method that does all of this hard work for you. You just feed it the `WriteStream` and use it:

```
NetServer server = vertx.createNetServer(
  new NetServerOptions().setPort(1234).setHost("localhost")
);
server.connectHandler(sock -> {
  sock.pipeTo(asyncFile);
}).listen();
```

This does exactly the same thing as the more verbose example, plus it handles stream failures and termination: the destination `WriteStream` is ended when the pipe completes with success or a failure.

You can be notified when the operation completes:

```
server.connectHandler(sock -> {

  // Pipe the socket providing a handler to be notified of the result
  sock.pipeTo(asyncFile)
    .onComplete(ar -> {
      if (ar.succeeded()) {
        System.out.println("Pipe succeeded");
      } else {
        System.out.println("Pipe failed");
      }
    });
}).listen();
```

When you deal with an asynchronous destination, you can create a `Pipe` instance that pauses the source and resumes it when the source is piped to the destination:

```
server.connectHandler(sock -> {

  // Create a pipe to use asynchronously
  Pipe<Buffer> pipe = sock.pipe();

  // Open a destination file
  fs.open("/path/to/file", new OpenOptions())
    .onComplete(ar -> {
      if (ar.succeeded()) {
        AsyncFile file = ar.result();

        // Pipe the socket to the file and close the file at the end
        pipe.to(file);
      } else {
        sock.close();
      }
  });
}).listen();
```

When you need to abort the transfer, you need to close it:

```
vertx.createHttpServer()
  .requestHandler(request -> {

    // Create a pipe that to use asynchronously
    Pipe<Buffer> pipe = request.pipe();

    // Open a destination file
    fs.open("/path/to/file", new OpenOptions())
      .onComplete(ar -> {
        if (ar.succeeded()) {
          AsyncFile file = ar.result();

          // Pipe the socket to the file and close the file at the end
          pipe.to(file);
        } else {
          // Close the pipe and resume the request, the body buffers will be discarded
          pipe.close();

          // Send an error response
          request.response().setStatusCode(500).end();
        }
      });
  }).listen(8080);
```

When the pipe is closed, the streams handlers are unset and the `ReadStream` resumed.

As seen above, by default the destination is always ended when the stream completes, you can control this behavior on the pipe object:

- `endOnFailure` controls the behavior when a failure happens
- `endOnSuccess` controls the behavior when the read stream ends
- `endOnComplete` controls the behavior in all cases

Here is a short example:

```
src.pipe()
  .endOnSuccess(false)
  .to(dst)
  .onComplete(rs -> {
    // Append some text and close the file
    dst.end(Buffer.buffer("done"));
  });
```

Let’s now look at the methods on `ReadStream` and `WriteStream` in more detail:

### ReadStream

`ReadStream` is implemented by `HttpClientResponse`, `DatagramSocket`, `HttpClientRequest`, `HttpServerFileUpload`, `HttpServerRequest`, `MessageConsumer`, `NetSocket`, `WebSocket` and `AsyncFile`.

- `handler`: set a handler which will receive items from the ReadStream.
- `pause`: pause the stream. When paused no items will be received in the handler.
- `fetch`: fetch a specified amount of item from the stream. The handler will be called if any item arrives. Fetches are cumulative.
- `resume`: resume the stream. The handler will be called if any item arrives. Resuming is equivalent of fetching `Long.MAX_VALUE` items.
- `exceptionHandler`: called when an exception occurs on the ReadStream.
- `endHandler`: called when the end of stream is reached. This might be when EOF is reached if the ReadStream represents a file, or when end of request is reached if it’s an HTTP request, or when the connection is closed if it’s a TCP socket.

A read stream is either in *flowing* or *fetch* mode

- when the stream is in *flowing* mode, elements are delivered to the handler
- when the stream is in *fetch* mode, only the number of requested elements will be delivered to the handler

When a hot read stream is obtained (e.g. `HttpServerRequest`), the read stream is in flowing mode, when a cold read stream is obtained (e.g. `AsyncFile`), the read stream is in fetch mode with no demand.

`pause`, `resume` and `fetch` change the mode

- `resume()` sets the *flowing* mode
- `pause()` sets the *fetch* mode and resets the demand to `0`
- `fetch(long)` requests a specific amount of elements and adds it to the actual demand

### WriteStream

`WriteStream` is implemented by `HttpClientRequest`, `HttpServerResponse` `WebSocket`, `NetSocket` and `AsyncFile`.

Functions:

- `write`: write an object to the WriteStream. This method will never block. Writes are queued internally and asynchronously written to the underlying resource.
- `setWriteQueueMaxSize`: set the number of object at which the write queue is considered *full*, and the method `writeQueueFull` returns `true`. Note that, when the write queue is considered full, if write is called the data will still be accepted and queued. The actual number depends on the stream implementation, for `Buffer` the size represents the actual number of bytes written and not the number of buffers.
- `writeQueueFull`: returns `true` if the write queue is considered full.
- `exceptionHandler`: Will be called if an exception occurs on the `WriteStream`.
- `drainHandler`: The handler will be called if the `WriteStream` is considered no longer full.

### Reducing streams

Java collectors can reduce a `ReadStream` to a result in a similar fashion `java.util.Stream` does, yet in an asynchronous fashion.

```
Future<Long> result = stream.collect(Collectors.counting());

result.onSuccess(count -> System.out.println("Stream emitted " + count + " elements"));
```

Note that `collect` overrides any previously handler set on the stream.


## Record Parser

The record parser allows you to easily parse protocols which are delimited by a sequence of bytes, or fixed size records. It transforms a sequence of input buffer to a sequence of buffer structured as configured (either fixed size or separated records).

For example, if you have a simple ASCII text protocol delimited by '\n' and the input is the following:

```
buffer1:HELLO\nHOW ARE Y
buffer2:OU?\nI AM
buffer3: DOING OK
buffer4:\n
```

The record parser would produce

```
buffer1:HELLO
buffer2:HOW ARE YOU?
buffer3:I AM DOING OK
```

Let’s see the associated code:

```
final RecordParser parser = RecordParser.newDelimited("\n", h -> {
  System.out.println(h.toString());
});

parser.handle(Buffer.buffer("HELLO\nHOW ARE Y"));
parser.handle(Buffer.buffer("OU?\nI AM"));
parser.handle(Buffer.buffer("DOING OK"));
parser.handle(Buffer.buffer("\n"));
```

You can also produce fixed sized chunks as follows:

```
RecordParser.newFixed(4, h -> {
  System.out.println(h.toString());
});
```

For more details, check out the `RecordParser` class.


## Json Parser

You can easily parse JSON structures but that requires to provide the JSON content at once, but it may not be convenient when you need to parse very large structures.

The non-blocking JSON parser is an event driven parser able to deal with very large structures. It transforms a sequence of input buffer to a sequence of JSON parse events.

```
JsonParser parser = JsonParser.newParser();

// Set handlers for various events
parser.handler(event -> {
  switch (event.type()) {
    case START_OBJECT:
      // Start an objet
      break;
    case END_OBJECT:
      // End an objet
      break;
    case START_ARRAY:
      // Start an array
      break;
    case END_ARRAY:
      // End an array
      break;
    case VALUE:
      // Handle a value
      String field = event.fieldName();
      if (field != null) {
        // In an object
      } else {
        // In an array or top level
        if (event.isString()) {

        } else {
          // ...
        }
      }
      break;
  }
});
```

The parser is non-blocking and emitted events are driven by the input buffers.

```
JsonParser parser = JsonParser.newParser();

// start array event
// start object event
// "firstName":"Bob" event
parser.handle(Buffer.buffer("[{\"firstName\":\"Bob\","));

// "lastName":"Morane" event
// end object event
parser.handle(Buffer.buffer("\"lastName\":\"Morane\"},"));

// start object event
// "firstName":"Luke" event
// "lastName":"Lucky" event
// end object event
parser.handle(Buffer.buffer("{\"firstName\":\"Luke\",\"lastName\":\"Lucky\"}"));

// end array event
parser.handle(Buffer.buffer("]"));

// Always call end
parser.end();
```

Event driven parsing provides more control but comes at the price of dealing with fine grained events, which can be inconvenient sometimes. The JSON parser allows you to handle JSON structures as values when it is desired:

```
JsonParser parser = JsonParser.newParser();

parser.objectValueMode();

parser.handler(event -> {
  switch (event.type()) {
    case START_ARRAY:
      // Start the array
      break;
    case END_ARRAY:
      // End the array
      break;
    case VALUE:
      // Handle each object
      break;
  }
});

parser.handle(Buffer.buffer("[{\"firstName\":\"Bob\"},\"lastName\":\"Morane\"),...]"));
parser.end();
```

The value mode can be set and unset during the parsing allowing you to switch between fine grained events or JSON object value events.

```
JsonParser parser = JsonParser.newParser();

parser.handler(event -> {
  // Start the object

  switch (event.type()) {
    case START_OBJECT:
      // Set object value mode to handle each entry, from now on the parser won't emit start object events
      parser.objectValueMode();
      break;
    case VALUE:
      // Handle each object
      // Get the field in which this object was parsed
      String id = event.fieldName();
      System.out.println("User with id " + id + " : " + event.value());
      break;
    case END_OBJECT:
      // Set the object event mode so the parser emits start/end object events again
      parser.objectEventMode();
      break;
  }
});

parser.handle(Buffer.buffer("{\"39877483847\":{\"firstName\":\"Bob\"},\"lastName\":\"Morane\"),...}"));
parser.end();
```

You can do the same with arrays as well

```
JsonParser parser = JsonParser.newParser();

parser.handler(event -> {
  // Start the object

  switch (event.type()) {
    case START_OBJECT:
      // Set array value mode to handle each entry, from now on the parser won't emit start array events
      parser.arrayValueMode();
      break;
    case VALUE:
      // Handle each array
      // Get the field in which this object was parsed
      System.out.println("Value : " + event.value());
      break;
    case END_OBJECT:
      // Set the array event mode so the parser emits start/end object events again
      parser.arrayEventMode();
      break;
  }
});

parser.handle(Buffer.buffer("[0,1,2,3,4,...]"));
parser.end();
```

You can also decode POJOs

```
parser.handler(event -> {
  // Handle each object
  // Get the field in which this object was parsed
  String id = event.fieldName();
  User user = event.mapTo(User.class);
  System.out.println("User with id " + id + " : " + user.firstName + " " + user.lastName);
});
```

Whenever the parser fails to process a buffer, an exception will be thrown unless you set an exception handler:

```
JsonParser parser = JsonParser.newParser();

parser.exceptionHandler(err -> {
  // Catch any parsing or decoding error
});
```

The parser also parses json streams:

- concatenated json streams: `{"temperature":30}{"temperature":50}`
- line delimited json streams: `{"an":"object"}\r\n3\r\n"a string"\r\nnull`

For more details, check out the `JsonParser` class.


## Thread safety

Most Vert.x objects are safe to access from different threads. *However* performance is optimised when they are accessed from the same context they were created from.

For example if you have deployed a verticle which creates a `NetServer` which provides `NetSocket` instances in it’s handler, then it’s best to always access that socket instance from the event loop of the verticle.

If you stick to the standard Vert.x verticle deployment model and avoid sharing objects between verticles then this should be the case without you having to think about it.


## Running blocking code

In a perfect world, there will be no war or hunger, all APIs will be written asynchronously and bunny rabbits will skip hand-in-hand with baby lambs across sunny green meadows.

**But… the real world is not like that. (Have you watched the news lately?)**

Fact is, many, if not most libraries, especially in the JVM ecosystem have synchronous APIs and many of the methods are likely to block. A good example is the JDBC API - it’s inherently synchronous, and no matter how hard it tries, Vert.x cannot sprinkle magic pixie dust on it to make it asynchronous.

We’re not going to rewrite everything to be asynchronous overnight so we need to provide you a way to use "traditional" blocking APIs safely within a Vert.x application.

As discussed before, you can’t call blocking operations directly from an event loop, as that would prevent it from doing any other useful work. So how can you do this?

It’s done by calling `executeBlocking` with blocking code to execute, as return you get a future completed with the result of the blocking code execution.

```
vertx.executeBlocking(() -> {
  // Call some blocking API that takes a significant amount of time to return
  return someAPI.blockingMethod("hello");
}).onComplete(res -> {
  System.out.println("The result is: " + res.result());
});
```

|   | Blocking code should block for a reasonable amount of time (i.e no more than a few seconds). Long blocking operations or polling operations (i.e a thread that spin in a loop polling events in a blocking fashion) are precluded. When the blocking operation lasts more than the 10 seconds, a message will be printed on the console by the blocked thread checker. Long blocking operations should use a dedicated thread managed by the application, which can interact with verticles using the event-bus or `runOnContext` |
|---|---|

By default, if executeBlocking is called several times from the same context (e.g. the same verticle instance) then the different executeBlocking are executed *serially* (i.e. one after another).

If you don’t care about ordering you can call `executeBlocking` specifying `false` as the argument to `ordered`. In this case any executeBlocking may be executed in parallel on the worker pool.

An alternative way to run blocking code is to use a worker verticle

A worker verticle is always executed with a thread from the worker pool.

By default blocking code is executed on the Vert.x worker pool, configured with `setWorkerPoolSize`.

Additional pools can be created for different purposes:

```
WorkerExecutor executor = vertx.createSharedWorkerExecutor("my-worker-pool");
executor.executeBlocking(() -> {
  // Call some blocking API that takes a significant amount of time to return
  return someAPI.blockingMethod("hello");
}).onComplete(res -> {
  System.out.println("The result is: " + res.result());
});
```

The worker executor must be closed when it’s not necessary anymore:

```
executor.close();
```

When several workers are created with the same name, they will share the same pool. The worker pool is destroyed when all the worker executors using it are closed.

When an executor is created in a Verticle, Vert.x will close it automatically for you when the Verticle is undeployed.

Worker executors can be configured when created:

```
int poolSize = 10;

// 2 minutes
long maxExecuteTime = 2;
TimeUnit maxExecuteTimeUnit = TimeUnit.MINUTES;

WorkerExecutor executor = vertx.createSharedWorkerExecutor("my-worker-pool", poolSize, maxExecuteTime, maxExecuteTimeUnit);
```

|   | the configuration is set when the worker pool is created |
|---|---|


## Vert.x SPI

A Vert.x instance has a few extension points knows as *SPI* (Service Provider Interface).

Such SPI are often loaded from the classpath using Java’s `ServiceLoader` mechanism.

### Metrics and tracing SPI

By default, Vert.x does not record any metrics nor does any tracing. Instead, it provides an SPI for others to implement which can be added to the classpath. The metrics SPI is a feature which allows implementers to capture events from Vert.x in order to collect and report metrics, likewise the tracing SPI does the same for traces.

For more information on this, please consult https://vertx.io/docs/#monitoring

### Cluster Manager SPI

In Vert.x a cluster manager is used for various functions including:

- Discovery and group membership of Vert.x nodes in a cluster
- Maintaining cluster wide topic subscriber lists (so we know which nodes are interested in which event bus addresses)
- Distributed Map support
- Distributed Locks
- Distributed Counters

Cluster managers *do not* handle the event bus inter-node transport, this is done directly by Vert.x with TCP connections.

The default cluster manager used in the Vert.x distributions is one that uses Hazelcast but this can be easily replaced by a different implementation as Vert.x cluster managers are pluggable.

A cluster manager must implement the interface `ClusterManager`. Vert.x locates cluster managers at run-time by using the Java Service Loader functionality to locate instances of `ClusterManager` on the classpath.

If you are using Vert.x at the command line and you want to use clustering you should make sure the `lib` directory of the Vert.x installation contains your cluster manager jar.

If you are using Vert.x from a Maven or Gradle project just add the cluster manager jar as a dependency of your project.

For more information on this, please consult https://vertx.io/docs/#clustering


## Vert.x Builder

`Vertx.vertx` and `Vertx.clusteredVertx` static methods are the easiest way obtain an instance of `Vertx`.

You can also use the builder pattern to create a `Vertx` instance. The builder lets you programmatically configure a few providers (SPI) which are usually loaded using `VertxOptions` and/or Java Service Loader plugins.

- Native transport
- Cluster manager
- Tracing
- Metrics instance

```
Vertx vertx = Vertx.builder()
  .with(options)
  .withTracer(tracerFactory)
  .withMetrics(metricsFactory)
  .build();
```

Clustered instances can also be created.

```
Future<Vertx> vertx = Vertx.builder()
  .with(options)
  .withClusterManager(clusterManager)
  .buildClustered();
```
