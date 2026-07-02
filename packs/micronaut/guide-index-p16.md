---
title: "Micronaut Core (part 16/27)"
source: https://docs.micronaut.io/latest/guide/index.html
domain: micronaut
license: CC-BY-SA-4.0
tags: micronaut framework, micronaut jvm, compile-time injection, microservices framework
fetched: 2026-07-02
part: 16/27
---

## 6.30 HTTP/2 Support

Since Micronaut framework 2.x, Micronaut Netty-based HTTP server can be configured to support HTTP/2.

#### Configuring the Server for HTTP/2

The first step is to set the supported HTTP version in the server configuration:

Enabling HTTP/2 Support

```properties
micronaut.server.http-version=2.0
```

```yaml
micronaut:
  server:
    http-version: 2.0
```

```toml
[micronaut]
  [micronaut.server]
    http-version=2.0
```

```groovy
micronaut {
  server {
    httpVersion = 2.0
  }
}
```

```hocon
{
  micronaut {
    server {
      http-version = 2.0
    }
  }
}
```

```json
{
  "micronaut": {
    "server": {
      "http-version": 2.0
    }
  }
}
```

With this configuration, the Micronaut framework enables support for the `h2c` protocol (see HTTP/2 over cleartext) which is fine for development.

Since browsers don’t support `h2c` and in general HTTP/2 over TLS (the `h2` protocol), it is recommended for production that you enable HTTPS support. For development this can be done with:

Enabling

h2

Protocol Support

```properties
micronaut.server.http-version=2.0
micronaut.server.ssl.enabled=true
micronaut.server.ssl.buildSelfSigned=true
```

```yaml
micronaut:
  server:
    http-version: 2.0
    ssl:
      enabled: true
      buildSelfSigned: true
```

```toml
[micronaut]
  [micronaut.server]
    http-version=2.0
    [micronaut.server.ssl]
      enabled=true
      buildSelfSigned=true
```

```groovy
micronaut {
  server {
    httpVersion = 2.0
    ssl {
      enabled = true
      buildSelfSigned = true
    }
  }
}
```

```hocon
{
  micronaut {
    server {
      http-version = 2.0
      ssl {
        enabled = true
        buildSelfSigned = true
      }
    }
  }
}
```

```json
{
  "micronaut": {
    "server": {
      "http-version": 2.0,
      "ssl": {
        "enabled": true,
        "buildSelfSigned": true
      }
    }
  }
}
```

For production, see the configuring HTTPS section of the documentation.

Note that if your deployment environment uses JDK 8, or for improved support for OpenSSL, define the following dependencies on Netty Tomcat Native:

`runtimeOnly("io.netty:netty-tcnative:2.0.58.Final")` `<dependency> <groupId>io.netty</groupId> <artifactId>netty-tcnative</artifactId> <version>2.0.58.Final</version> <scope>runtime</scope> </dependency>`

`runtimeOnly("io.netty:netty-tcnative-boringssl-static:2.0.58.Final")` `<dependency> <groupId>io.netty</groupId> <artifactId>netty-tcnative-boringssl-static</artifactId> <version>2.0.58.Final</version> <scope>runtime</scope> </dependency>`

In addition to a dependency on the appropriate native library for your architecture. For example:

Configuring Tomcat Native

```groovy
runtimeOnly "io.netty:netty-tcnative-boringssl-static:2.0.58.Final:${Os.isFamily(Os.FAMILY_MAC) ? (Os.isArch("aarch64") ? "osx-aarch_64" : "osx-x86_64") : 'linux-x86_64'}"
```

See the documentation on Tomcat Native for more information.

#### HTTP/2 Server Push Support

Support for server push has been added in Micronaut framework 3.2. Server push allows for a single request to trigger multiple responses. This is most often used in the case of browser based resources. The goal is to improve latency for the client, because they do not have to request that resource manually anymore, and can save a round trip.

A new interface, PushCapableHttpRequest, has been created to support the feature. Simply add a PushCapableHttpRequest parameter to a controller method and use its API to trigger additional requests.

|   | PushCapableHttpRequest extends HttpRequest so it’s not necessary to have both as arguments in a controller method. |
|---|---|

Before triggering additional requests, the `isServerPushSupported()` method should be called to ensure the feature is available. Once it’s known the feature is supported, use the `serverPush(HttpRequest)` method to trigger additional requests. For example: `request.serverPush(HttpRequest.GET("/static/style.css"))`).


## 6.31 HTTP/3 Support

Since Micronaut framework 4.x, Micronaut’s Netty-based HTTP server can be configured to support HTTP/3.

#### Configuring the Server for HTTP/3

Instead of the TCP used for HTTP/1.1 and HTTP/2, HTTP/3 runs on UDP. To expose an HTTP/3 server, you need to define a listener with the special `QUIC` protocol family:

Enabling HTTP/3 Support

```yaml
micronaut:
  server:
    netty:
      listeners:
        http3Listener:
          family: QUIC
          port: 8443
```

|   | that defining this listener will disable the implicit TCP listeners. You can add them manually as described in the listener section. |
|---|---|

Additionally, the netty HTTP/3 codec needs to be present on the classpath:

`implementation("io.micronaut:micronaut-http-netty-http3")` `<dependency> <groupId>io.micronaut</groupId> <artifactId>micronaut-http-netty-http3</artifactId> </dependency>`


## 6.32 Server Events

The HTTP server emits a number of Bean Events, defined in the io.micronaut.runtime.server.event package, that you can write listeners for. The following table summarizes these:

| Event | Description |
|---|---|
| ServerStartupEvent | Emitted when the server completes startup |
| ServerShutdownEvent | Emitted when the server shuts down |
| ServiceReadyEvent | Emitted after all ServerStartupEvent listeners have been invoked and exposes the EmbeddedServerInstance |
| ServiceStoppedEvent | Emitted after all ServerShutdownEvent listeners have been invoked and exposes the EmbeddedServerInstance |

|   | Doing significant work within a listener for a ServerStartupEvent will increase startup time. |
|---|---|

The following example defines a ApplicationEventListener that listens for ServerStartupEvent:

Listening for Server Startup Events

```java
import io.micronaut.context.event.ApplicationEventListener;
...
@Singleton
public class StartupListener implements ApplicationEventListener<ServerStartupEvent> {
    @Override
    public void onApplicationEvent(ServerStartupEvent event) {
        // logic here
        ...
    }
}
```

Alternatively, you can also use the @EventListener annotation on a method of any bean that accepts `ServerStartupEvent`:

Using

@EventListener

with

ServerStartupEvent

```java
import io.micronaut.runtime.event.annotation.EventListener;
import io.micronaut.runtime.server.event.ServerStartupEvent;
import jakarta.inject.Singleton;
...
@Singleton
public class MyBean {

    @EventListener
    public void onStartup(ServerStartupEvent event) {
        // logic here
        ...
    }
}
```


## 6.33 Configuring the HTTP Server

The HTTP server features a number of configuration options. They are defined in the NettyHttpServerConfiguration configuration class, which extends HttpServerConfiguration.

The following example shows how to tweak configuration options for the server via your configuration file (e.g `application.yml`):

Configuring HTTP server settings

```properties
micronaut.server.maxRequestSize=1MB
micronaut.server.host=localhost
micronaut.server.netty.maxHeaderSize=500KB
micronaut.server.netty.worker.threads=8
micronaut.server.netty.childOptions.autoRead=true
```

```yaml
micronaut:
  server:
    maxRequestSize: 1MB
    host: localhost
    netty:
      maxHeaderSize: 500KB
      worker:
        threads: 8
      childOptions:
        autoRead: true
```

```toml
[micronaut]
  [micronaut.server]
    maxRequestSize="1MB"
    host="localhost"
    [micronaut.server.netty]
      maxHeaderSize="500KB"
      [micronaut.server.netty.worker]
        threads=8
      [micronaut.server.netty.childOptions]
        autoRead=true
```

```groovy
micronaut {
  server {
    maxRequestSize = "1MB"
    host = "localhost"
    netty {
      maxHeaderSize = "500KB"
      worker {
        threads = 8
      }
      childOptions {
        autoRead = true
      }
    }
  }
}
```

```hocon
{
  micronaut {
    server {
      maxRequestSize = "1MB"
      host = "localhost"
      netty {
        maxHeaderSize = "500KB"
        worker {
          threads = 8
        }
        childOptions {
          autoRead = true
        }
      }
    }
  }
}
```

```json
{
  "micronaut": {
    "server": {
      "maxRequestSize": "1MB",
      "host": "localhost",
      "netty": {
        "maxHeaderSize": "500KB",
        "worker": {
          "threads": 8
        },
        "childOptions": {
          "autoRead": true
        }
      }
    }
  }
}
```

- By default, Micronaut framework binds to all network interfaces. Use `localhost` to bind only to loopback network interface
- `maxHeaderSize` sets the maximum header size
- `worker.threads` specifies the number of Netty worker threads
- `autoRead` enables request body auto read

🔗

| Property | Type | Description | Default value |
|---|---|---|---|
| `micronaut.server.http-version` | HttpVersion |   |   |
| `micronaut.server.thread-selection` | ThreadSelection |   |   |
| `micronaut.server.redispatch-non-blocking-only` | boolean |   |   |
| `micronaut.server.default-charset` | java.nio.charset.Charset |   |   |
| `micronaut.server.port` | int |   |   |
| `micronaut.server.host` | java.lang.String |   |   |
| `micronaut.server.read-timeout` | java.lang.Integer |   |   |
| `micronaut.server.max-request-size` | long |   |   |
| `micronaut.server.max-request-buffer-size` | long |   |   |
| `micronaut.server.read-idle-timeout` | java.time.Duration |   |   |
| `micronaut.server.write-idle-timeout` | java.time.Duration |   |   |
| `micronaut.server.idle-timeout` | java.time.Duration |   |   |
| `micronaut.server.server-header` | java.lang.String |   |   |
| `micronaut.server.date-header` | boolean |   |   |
| `micronaut.server.log-handled-exceptions` | boolean |   |   |
| `micronaut.server.client-address-header` | java.lang.String |   |   |
| `micronaut.server.context-path` | java.lang.String |   |   |
| `micronaut.server.dual-protocol` | boolean |   |   |
| `micronaut.server.http-to-https-redirect` | boolean |   |   |
| `micronaut.server.dispatch-options-requests` | boolean |   |   |
| `micronaut.server.validate-url` | boolean |   |   |
| `micronaut.server.escape-html-url` | boolean |   |   |
| `micronaut.server.not-found-on-missing-body` | boolean |   |   |
| `micronaut.server.semicolon-is-normal-char` | boolean |   |   |
| `micronaut.server.max-params` | int |   |   |
| `micronaut.server.netty.server-type` | NettyHttpServerConfiguration$HttpServerType | Set the server type. |   |
| `micronaut.server.netty.close-on-expectation-failed` | boolean | If a 100-continue response is detected but the content length is too large then true means close the connection. otherwise the connection will remain open and data will be consumed and discarded until the next request is received. <p>only relevant when {@link HttpServerType#FULL_CONTENT} is set</p> |   |
| `micronaut.server.netty.fallback-protocol` | java.lang.String | Sets the fallback protocol to use when negotiating via ALPN. |   |
| `micronaut.server.netty.log-level` | io.netty.handler.logging.LogLevel | Sets the Netty log level. |   |
| `micronaut.server.netty.max-initial-line-length` | int | Sets the maximum initial line length for the HTTP request. Default value (4096). |   |
| `micronaut.server.netty.max-header-size` | int | Sets the maximum header size. Default value (8192). |   |
| `micronaut.server.netty.max-chunk-size` | int | Sets the maximum size of any single request chunk. Default value (8192). |   |
| `micronaut.server.netty.max-h2c-upgrade-request-size` | int | Sets the maximum size of the body of the HTTP1.1 request used to upgrade a connection to HTTP2 clear-text (h2c). This initial request cannot be streamed and is instead buffered in full, so the default value (8192) is relatively small. <i>If this value is too small for your use case, instead consider using an empty initial "upgrade request" (e.g. {@code OPTIONS /}), or switch to normal HTTP2.</i> <p> <i>Does not affect normal HTTP2 (TLS).</i> |   |
| `micronaut.server.netty.chunked-supported` | boolean | Sets whether chunked transfer encoding is supported. Default value (true). |   |
| `micronaut.server.netty.use-native-transport` | boolean | Sets whether to use netty’s native transport (epoll or kqueue) if available . Default value (false). |   |
| `micronaut.server.netty.validate-headers` | boolean | Sets whether to validate incoming headers. Default value (true). |   |
| `micronaut.server.netty.initial-buffer-size` | int | Sets the initial buffer size. Default value (128). |   |
| `micronaut.server.netty.compression-threshold` | int | Sets the minimum size of a request body must be in order to be compressed. Default value (1024). |   |
| `micronaut.server.netty.compression-level` | int | Sets the compression level (0-9). Default value (6). |   |
| `micronaut.server.netty.max-zstd-encode-size` | int | Sets the maximum size of data that can be encoded using the zstd algorithm. Default value (1024 * 1024 * 32). |   |
| `micronaut.server.netty.child-options` | java.util.Map | Sets the Netty child worker options. |   |
| `micronaut.server.netty.options` | java.util.Map | Sets the channel options. |   |
| `micronaut.server.netty.keep-alive-on-server-error` | boolean | Whether to send connection keep alive on internal server errors. Default value ({@value DEFAULT_KEEP_ALIVE_ON_SERVER_ERROR}). |   |
| `micronaut.server.netty.pcap-logging-path-pattern` | java.lang.String | The path pattern to use for logging incoming connections to pcap. This is an unsupported option: Behavior may change, or it may disappear entirely, without notice! |   |
| `micronaut.server.netty.listeners` | java.util.List | Set the explicit netty listener configurations, or {@code null} if they should be implicit. |   |
| `micronaut.server.netty.eager-parsing` | boolean | Parse incoming JSON data eagerly, before route binding. Default value {@value DEFAULT_EAGER_PARSING}. |   |
| `micronaut.server.netty.json-buffer-max-components` | int | Maximum number of buffers to keep around in JSON parsing before they should be consolidated. Defaults to 4096. |   |
| `micronaut.server.netty.request-decompression-enabled` | boolean | Enable or disable automatic request content decompression in the Netty HTTP server. Disabling this can be useful for proxy or testing scenarios where the compressed payload and Content-Encoding header need to be observed. |   |
| `micronaut.server.netty.legacy-multiplex-handlers` | boolean | Prior to 4.4.0, the Micronaut HTTP server used a multi-pipeline approach for handling HTTP/2 connections where every request got its own netty pipeline with HTTP/2 to HTTP/1.1 converters on the pipeline. This allowed for using mostly unchanged HTTP/1.1 in the request handling and any NettyServerCustomizers. <p> As of 4.4.0, this approach was replaced with a more performant HTTP/2-specific implementation. This means worse compatibility with HTTP/1.1-based code paths and customizers, however. Setting this option to {@code true} returns to the old behavior. |   |
| `micronaut.server.netty.form-max-fields` | int | The maximum number of form fields permitted in a request. |   |
| `micronaut.server.netty.field-max-buffered-bytes` | long | The maximum number of bytes that are allowed to be buffered per form value. If there are multiple fields, this limit is counted separately for each. |   |
| `micronaut.server.netty.field-max-bytes` | long | The maximum number of bytes per form <i>value</i>. If there are multiple fields, this limit is counted separately for each. |   |
| `micronaut.server.netty.form-max-buffered-bytes` | long | The maximum number of bytes the entire form is allowed to buffer internally. If multiple fields are buffered, this limit is shared. |   |
| `micronaut.server.netty.form-max-bytes` | long | The maximum number of bytes of all form <i>values</i>. If there are multiple fields, this limit is shared. |   |
| `micronaut.server.netty.form-decoder-quirks` | java.util.Set | The decoder quirks for the <a href="https://github.com/netty-contrib/codec-multipart/">next-generation multipart parser</a>, if present. No quirks by default. |   |

### Using Native Transports

The native Netty transports add features specific to a particular platform, generate less garbage, and generally improve performance when compared to the NIO-based transport.

To enable native transports, first add a dependency:

For macOS on x86:

`runtimeOnly("io.netty:netty-transport-native-kqueue::osx-x86_64")` `<dependency> <groupId>io.netty</groupId> <artifactId>netty-transport-native-kqueue</artifactId> <scope>runtime</scope> <classifier>osx-x86_64</classifier> </dependency>`

For macOS on M1:

`runtimeOnly("io.netty:netty-transport-native-kqueue::osx-aarch_64")` `<dependency> <groupId>io.netty</groupId> <artifactId>netty-transport-native-kqueue</artifactId> <scope>runtime</scope> <classifier>osx-aarch_64</classifier> </dependency>`

For Linux on x86:

`runtimeOnly("io.netty:netty-transport-native-epoll::linux-x86_64")` `<dependency> <groupId>io.netty</groupId> <artifactId>netty-transport-native-epoll</artifactId> <scope>runtime</scope> <classifier>linux-x86_64</classifier> </dependency>`

or

`runtimeOnly("io.netty:netty-transport-native-io_uring::linux-x86_64")` `<dependency> <groupId>io.netty</groupId> <artifactId>netty-transport-native-io_uring</artifactId> <scope>runtime</scope> <classifier>linux-x86_64</classifier> </dependency>`

For Linux on ARM64:

`runtimeOnly("io.netty:netty-transport-native-epoll::linux-aarch_64")` `<dependency> <groupId>io.netty</groupId> <artifactId>netty-transport-native-epoll</artifactId> <scope>runtime</scope> <classifier>linux-aarch_64</classifier> </dependency>`

or

`runtimeOnly("io.netty:netty-transport-native-io_uring::linux-aarch_64")` `<dependency> <groupId>io.netty</groupId> <artifactId>netty-transport-native-io_uring</artifactId> <scope>runtime</scope> <classifier>linux-aarch_64</classifier> </dependency>`

Then configure the default event loop group to prefer native transports:

Configuring The Default Event Loop to Prefer Native Transports

```properties
micronaut.netty.event-loops.default.transport=io_uring,epoll,kqueue,nio
```

```yaml
micronaut:
  netty:
    event-loops:
      default:
        transport: io_uring,epoll,kqueue,nio
```

```toml
[micronaut]
  [micronaut.netty]
    [micronaut.netty.event-loops]
      [micronaut.netty.event-loops.default]
        transport="io_uring,epoll,kqueue,nio"
```

```groovy
micronaut {
  netty {
    eventLoops {
      'default' {
        transport = "io_uring,epoll,kqueue,nio"
      }
    }
  }
}
```

```hocon
{
  micronaut {
    netty {
      event-loops {
        default {
          transport = "io_uring,epoll,kqueue,nio"
        }
      }
    }
  }
}
```

```json
{
  "micronaut": {
    "netty": {
      "event-loops": {
        "default": {
          "transport": "io_uring,epoll,kqueue,nio"
        }
      }
    }
  }
}
```

The first available transport out of those listed will be used. If you want to make sure native transports will be used in all environments, remove the `nio` entry. An exception will be thrown if no native transport is available.

|   | Netty enables simplistic sampling resource leak detection which reports there is a leak or not, at the cost of small overhead. You can enable it by setting property `netty.resource-leak-detector-level` to one of: `DISABLED` (default), `SIMPLE`, `PARANOID` or `ADVANCED`. |
|---|---|


## 6.33.1 Configuring Server Thread Pools

The HTTP server is built on Netty which is designed as a non-blocking I/O toolkit in an event loop model.

The Netty worker event loop uses the "default" named event loop group. This can be configured through `micronaut.netty.event-loops.default`.

|   | The event loop configuration under `micronaut.server.netty.worker` is only used if the `event-loop-group` is set to a name which doesn’t correspond to any `micronaut.netty.event-loops` configuration. This behavior is deprecated and will be removed in a future version. Use `micronaut.netty.event-loops.*` for any event loop group configuration beyond setting the name through `event-loop-group`. This does not apply to the parent event loop configuration (`micronaut.server.netty.parent`). |
|---|---|

🔗

| Property | Type | Description | Default value |
|---|---|---|---|
| `micronaut.server.netty.worker.event-loop-group` | java.lang.String | Sets the name to use. |   |
| `micronaut.server.netty.worker.threads` | int | Sets the number of threads for the event loop group. |   |
| `micronaut.server.netty.worker.io-ratio` | java.lang.Integer | Sets the I/O ratio. |   |
| `micronaut.server.netty.worker.executor` | java.lang.String | A named executor service to use for event loop threads (optional). This property is very specialized. In particular, it will <i>not</i> solve read timeouts or fix blocking operations on the event loop, in fact it may do the opposite. Don’t use unless you really know what this does. |   |
| `micronaut.server.netty.worker.prefer-native-transport` | boolean | Set whether to prefer the native transport if available |   |
| `micronaut.server.netty.worker.shutdown-quiet-period` | java.time.Duration | Set the shutdown quiet period |   |
| `micronaut.server.netty.worker.shutdown-timeout` | java.time.Duration | Set the shutdown timeout (must be >= shutdownQuietPeriod) |   |
| `micronaut.server.netty.worker.thread-core-ratio` | double | The number of threads per core to use if {@link #getNumThreads()} is set to 0. |   |
| `micronaut.server.netty.worker.transport` | java.util.List | The transports to use for this event loop, in order of preference. Supported values are {@code io_uring,epoll,kqueue,nio}. The first available transport out of those listed will be used (nio is always available). If no listed transport is available, an exception will be thrown. <p>By default, only {@code nio} is used, even if native transports are available. If the legacy {@link #isPreferNativeTransport() prefer-native-transport} property is set to {@code true}, this defaults to {@code io_uring,epoll,kqueue,nio}. |   |
| `micronaut.server.netty.worker.loom-carrier` | boolean | When set to {@code true}, use a special <i>experimental</i> event loop that can also execute virtual threads, in order to improve virtual thread performance. |   |

|   | The parent event loop can be configured with `micronaut.server.netty.parent` with the same configuration options. |
|---|---|

The server can also be configured to use a different named worker event loop:

Using a different event loop for the server

```properties
micronaut.server.netty.worker.event-loop-group=other
micronaut.netty.event-loops.other.num-threads=10
```

```yaml
micronaut:
  server:
    netty:
      worker:
        event-loop-group: other
  netty:
    event-loops:
      other:
        num-threads: 10
```

```toml
[micronaut]
  [micronaut.server]
    [micronaut.server.netty]
      [micronaut.server.netty.worker]
        event-loop-group="other"
  [micronaut.netty]
    [micronaut.netty.event-loops]
      [micronaut.netty.event-loops.other]
        num-threads=10
```

```groovy
micronaut {
  server {
    netty {
      worker {
        eventLoopGroup = "other"
      }
    }
  }
  netty {
    eventLoops {
      other {
        numThreads = 10
      }
    }
  }
}
```

```hocon
{
  micronaut {
    server {
      netty {
        worker {
          event-loop-group = "other"
        }
      }
    }
    netty {
      event-loops {
        other {
          num-threads = 10
        }
      }
    }
  }
}
```

```json
{
  "micronaut": {
    "server": {
      "netty": {
        "worker": {
          "event-loop-group": "other"
        }
      }
    },
    "netty": {
      "event-loops": {
        "other": {
          "num-threads": 10
        }
      }
    }
  }
}
```

|   | The default value for the number of threads is the value of the system property `io.netty.eventLoopThreads`, or if not specified, the available processors x 2. |
|---|---|

See the following table for configuring event loops:

🔗

| Property | Type | Description | Default value |
|---|---|---|---|
| `micronaut.netty.event-loops.*.num-threads` | int | The number of threads | 0 |
| `micronaut.netty.event-loops.*.thread-core-ratio` | double | The number of threads per core to use if {@link #getNumThreads()} is set to 0. | 1.0 |
| `micronaut.netty.event-loops.*.io-ratio` | java.lang.Integer | The IO ratio (optional) |   |
| `micronaut.netty.event-loops.*.prefer-native-transport` | boolean | Whether native transport is to be preferred | false |
| `micronaut.netty.event-loops.*.transport` | java.util.List | The transports to use for this event loop, in order of preference. Supported values are {@code io_uring,epoll,kqueue,nio}. The first available transport out of those listed will be used (nio is always available). If no listed transport is available, an exception will be thrown. <p>By default, only {@code nio} is used, even if native transports are available. If the legacy {@link #isPreferNativeTransport() prefer-native-transport} property is set to {@code true}, this defaults to {@code io_uring,epoll,kqueue,nio}. |   |
| `micronaut.netty.event-loops.*.executor` | java.lang.String | A named executor service to use for event loop threads (optional). This property is very specialized. In particular, it will <i>not</i> solve read timeouts or fix blocking operations on the event loop, in fact it may do the opposite. Don’t use unless you really know what this does. |   |
| `micronaut.netty.event-loops.*.shutdown-quiet-period` | java.time.Duration | The shutdown quiet period |   |
| `micronaut.netty.event-loops.*.shutdown-timeout` | java.time.Duration | The shutdown timeout (must be >= shutdownQuietPeriod) |   |
| `micronaut.netty.event-loops.*.loom-carrier` | boolean | When set to {@code true}, use a special <i>experimental</i> event loop that can also execute virtual threads, in order to improve virtual thread performance. | false |


## 6.33.1.1 Blocking Operations

When dealing with blocking operations, the Micronaut framework shifts the blocking operations to an unbound, caching I/O thread pool by default. You can configure the I/O thread pool using the ExecutorConfiguration named `io`. For example:

Configuring the Server I/O Thread Pool

```properties
micronaut.executors.io.type=fixed
micronaut.executors.io.nThreads=75
```

```yaml
micronaut:
  executors:
    io:
      type: fixed
      nThreads: 75
```

```toml
[micronaut]
  [micronaut.executors]
    [micronaut.executors.io]
      type="fixed"
      nThreads=75
```

```groovy
micronaut {
  executors {
    io {
      type = "fixed"
      nThreads = 75
    }
  }
}
```

```hocon
{
  micronaut {
    executors {
      io {
        type = "fixed"
        nThreads = 75
      }
    }
  }
}
```

```json
{
  "micronaut": {
    "executors": {
      "io": {
        "type": "fixed",
        "nThreads": 75
      }
    }
  }
}
```

The above configuration creates a fixed thread pool with 75 threads.


## 6.33.1.2 Virtual Threads

Since Java 19, the JVM includes experimental support for virtual threads ("project loom"). As it is a preview feature, you need to pass `--enable-preview` as a JVM parameter to enable it.

The Micronaut framework will detect virtual thread support and use it for the executor named `blocking` if available. If virtual threads are not supported, this executor will be aliased to the `io` thread pool.

To use the `blocking` executor, simply mark e.g. a controller with `ExecuteOn`:

Configuring the Server I/O Thread Pool

```java
@Controller("/hello")
class HelloWorldController {

    @ExecuteOn(TaskExecutors.BLOCKING)
    @Produces(MediaType.TEXT_PLAIN)
    @Get("/world")
    String index() {
        return "Hello World";
    }
}
```

Configuring the Server I/O Thread Pool

```groovy
@Controller("/hello")
class HelloWorldController {

    @ExecuteOn(TaskExecutors.BLOCKING)
    @Produces(MediaType.TEXT_PLAIN)
    @Get("/world")
    String index() {
        "Hello World"
    }
}
```

### Event loop carrier

Micronaut HTTP Server Netty 4.9 introduces an **experimental** mode to run virtual threads on the Netty event loop. This can improve performance of virtual threads, since it avoids a context switch between the Netty event loop and the JDK ForkJoinPool.

This mode requires access to internal JDK APIs. Please run your application with `--add-opens=java.base/java.lang=ALL-UNNAMED`. Then, enable the `loom-carrier` flag for the event loop, e.g. `micronaut.netty.event-loops.loom-carrier=true`

Enabling the event loop carrier

```properties
micronaut.netty.event-loops.default.loom-carrier=true
```

```yaml
micronaut:
  netty:
    event-loops:
      default:
        loom-carrier: true
```

```toml
[micronaut]
  [micronaut.netty]
    [micronaut.netty.event-loops]
      [micronaut.netty.event-loops.default]
        loom-carrier=true
```

```groovy
micronaut {
  netty {
    eventLoops {
      'default' {
        loomCarrier = true
      }
    }
  }
}
```

```hocon
{
  micronaut {
    netty {
      event-loops {
        default {
          loom-carrier = true
        }
      }
    }
  }
}
```

```json
{
  "micronaut": {
    "netty": {
      "event-loops": {
        "default": {
          "loom-carrier": true
        }
      }
    }
  }
}
```


## 6.33.1.3 @Blocking

You can use the @Blocking annotation to mark methods as blocking.

If you set `micronaut.server.thread-selection` to `AUTO`, the Micronaut framework offloads the execution of methods annotated with `@Blocking` to the IO thread pool (See: TaskExecutors).

|   | `@Blocking` only works if you are using `AUTO` thread selection. Micronaut framework defaults to `MANUAL` thread selection since Micronaut 2.0. We recommend the usage of @ExecuteOn annotation to execute the blocking operations on a different thread pool. `@ExecutesOn` works for both `MANUAL` and `AUTO` thread selection. |
|---|---|

There are some places where the Micronaut framework uses @Blocking internally:

| Blocking Type | Description |
|---|---|
| BlockingHttpClient | Intended for testing, provides blocking versions for a subset of HttpClient operations. |
| IOUtils | Reads the contents of a `BufferedReader` in a blocking manner, and returns that as a `String`. |
| BootstrapPropertySourceLocator | Resolves either remote or local PropertySource instances for the current `Environment`. |

|   | Micronaut Data also utilizes `@Blocking` internally for some transaction operations, CRUD interceptors, and repositories. |
|---|---|


## 6.33.2 Configuring the Netty Client Pipeline

You can customize the Netty client pipeline by writing a Bean Event Listener that listens for the creation of a Registry.

The ChannelPipelineCustomizer interface defines constants for the names of the various handlers that the Micronaut framework registers.

As an example the following code sample demonstrates registering the Logbook library which includes additional Netty handlers to perform request and response logging:

Customizing the Netty server pipeline for Logbook

```java
import io.micronaut.context.annotation.Requires;
import io.micronaut.context.event.BeanCreatedEvent;
import io.micronaut.context.event.BeanCreatedEventListener;
import io.micronaut.http.client.netty.NettyClientCustomizer;
import io.micronaut.http.netty.channel.ChannelPipelineCustomizer;
import io.netty.channel.Channel;
import jakarta.inject.Singleton;
import org.zalando.logbook.Logbook;
import org.zalando.logbook.netty.LogbookClientHandler;

@Requires(beans = Logbook.class)
@Singleton
public class LogbookNettyClientCustomizer
    implements BeanCreatedEventListener<NettyClientCustomizer.Registry> { // (1)
    private final Logbook logbook;

    public LogbookNettyClientCustomizer(Logbook logbook) {
        this.logbook = logbook;
    }

    @Override
    public NettyClientCustomizer.Registry onCreated(
        BeanCreatedEvent<NettyClientCustomizer.Registry> event) {

        NettyClientCustomizer.Registry registry = event.getBean();
        registry.register(new Customizer(null)); // (2)
        return registry;
    }

    private class Customizer implements NettyClientCustomizer { // (3)
        private final Channel channel;

        Customizer(Channel channel) {
            this.channel = channel;
        }

        @Override
        public NettyClientCustomizer specializeForChannel(Channel channel, ChannelRole role) {
            return new Customizer(channel); // (4)
        }

        @Override
        public void onRequestPipelineBuilt() {
            channel.pipeline().addBefore( // (5)
                ChannelPipelineCustomizer.HANDLER_MICRONAUT_HTTP_RESPONSE,
                "logbook",
                new LogbookClientHandler(logbook)
            );
        }
    }
}
```

Customizing the Netty server pipeline for Logbook

```kotlin
import io.micronaut.context.annotation.Requires
import io.micronaut.context.event.BeanCreatedEvent
import io.micronaut.context.event.BeanCreatedEventListener
import io.micronaut.http.client.netty.NettyClientCustomizer
import io.micronaut.http.client.netty.NettyClientCustomizer.ChannelRole
import io.micronaut.http.netty.channel.ChannelPipelineCustomizer
import io.netty.channel.Channel
import jakarta.inject.Singleton
import org.zalando.logbook.Logbook
import org.zalando.logbook.netty.LogbookClientHandler

@Requires(beans = [Logbook::class])
@Singleton
class LogbookNettyClientCustomizer(private val logbook: Logbook) :
    BeanCreatedEventListener<NettyClientCustomizer.Registry> { // (1)

    override fun onCreated(event: BeanCreatedEvent<NettyClientCustomizer.Registry>): NettyClientCustomizer.Registry {
        val registry = event.bean
        registry.register(Customizer(null)) // (2)
        return registry
    }

    private inner class Customizer constructor(private val channel: Channel?) :
        NettyClientCustomizer { // (3)

        override fun specializeForChannel(channel: Channel, role: ChannelRole) = Customizer(channel) // (4)

        override fun onRequestPipelineBuilt() {
            channel!!.pipeline().addBefore( // (5)
                ChannelPipelineCustomizer.HANDLER_HTTP_STREAM,
                "logbook",
                LogbookClientHandler(logbook)
            )
        }
    }
}
```

Customizing the Netty server pipeline for Logbook

```groovy
import io.micronaut.http.client.netty.NettyClientCustomizer
import io.micronaut.http.netty.channel.ChannelPipelineCustomizer
import io.netty.channel.Channel
import jakarta.inject.Singleton
import org.zalando.logbook.Logbook
import org.zalando.logbook.netty.LogbookClientHandler

@Requires(beans = Logbook.class)
@Singleton
class LogbookNettyClientCustomizer
        implements BeanCreatedEventListener<NettyClientCustomizer.Registry> { // (1)
    private final Logbook logbook;

    LogbookNettyClientCustomizer(Logbook logbook) {
        this.logbook = logbook
    }

    @Override
    NettyClientCustomizer.Registry onCreated(
            BeanCreatedEvent<NettyClientCustomizer.Registry> event) {

        NettyClientCustomizer.Registry registry = event.getBean()
        registry.register(new Customizer(null)) // (2)
        return registry
    }

    private class Customizer implements NettyClientCustomizer { // (3)
        private final Channel channel

        Customizer(Channel channel) {
            this.channel = channel
        }

        @Override
        NettyClientCustomizer specializeForChannel(Channel channel, ChannelRole role) {
            return new Customizer(channel) // (4)
        }

        @Override
        void onRequestPipelineBuilt() {
            channel.pipeline().addBefore( // (5)
                    ChannelPipelineCustomizer.HANDLER_MICRONAUT_HTTP_RESPONSE,
                    "logbook",
                    new LogbookClientHandler(logbook)
            )
        }
    }
}
```

| **1** | `LogbookNettyClientCustomizer` listens for a Registry and requires the definition of a `Logbook` bean |
|---|---|
| **2** | The root customizer is initialized without a channel and registered |
| **3** | The actual customizer implements NettyClientCustomizer |
| **4** | When a new channel is created, a new, specialized customizer is created for that channel |
| **5** | When the client signals that the stream pipeline has been fully constructed, the logbook handler is registered |


## 6.33.3 Configuring the Netty Server Pipeline

You can customize the Netty server pipeline by writing a Bean Event Listener that listens for the creation of Registry.

The ChannelPipelineCustomizer interface defines constants for the names of the various handlers the Micronaut framework registers.

As an example the following code sample demonstrates registering the Logbook library which includes additional Netty handlers to perform request and response logging:

Customizing the Netty server pipeline for Logbook

```java
import io.micronaut.context.annotation.Requires;
import io.micronaut.context.event.BeanCreatedEvent;
import io.micronaut.context.event.BeanCreatedEventListener;
import io.micronaut.http.netty.channel.ChannelPipelineCustomizer;
import io.micronaut.http.server.netty.NettyServerCustomizer;
import io.netty.channel.Channel;
import jakarta.inject.Singleton;
import org.zalando.logbook.Logbook;
import org.zalando.logbook.netty.LogbookServerHandler;

@Requires(beans = Logbook.class)
@Singleton
public class LogbookNettyServerCustomizer
    implements BeanCreatedEventListener<NettyServerCustomizer.Registry> { // (1)
    private final Logbook logbook;

    public LogbookNettyServerCustomizer(Logbook logbook) {
        this.logbook = logbook;
    }

    @Override
    public NettyServerCustomizer.Registry onCreated(
        BeanCreatedEvent<NettyServerCustomizer.Registry> event) {

        NettyServerCustomizer.Registry registry = event.getBean();
        registry.register(new Customizer(null)); // (2)
        return registry;
    }

    private class Customizer implements NettyServerCustomizer { // (3)
        private final Channel channel;

        Customizer(Channel channel) {
            this.channel = channel;
        }

        @Override
        public NettyServerCustomizer specializeForChannel(Channel channel, ChannelRole role) {
            return new Customizer(channel); // (4)
        }

        @Override
        public void onStreamPipelineBuilt() {
            channel.pipeline().addBefore( // (5)
                ChannelPipelineCustomizer.HANDLER_MICRONAUT_INBOUND,
                "logbook",
                new LogbookServerHandler(logbook)
            );
        }
    }
}
```

Customizing the Netty server pipeline for Logbook

```kotlin
import io.micronaut.context.annotation.Requires
import io.micronaut.context.event.BeanCreatedEvent
import io.micronaut.context.event.BeanCreatedEventListener
import io.micronaut.http.netty.channel.ChannelPipelineCustomizer
import io.micronaut.http.server.netty.NettyServerCustomizer
import io.micronaut.http.server.netty.NettyServerCustomizer.ChannelRole
import io.netty.channel.Channel
import jakarta.inject.Singleton
import org.zalando.logbook.Logbook
import org.zalando.logbook.netty.LogbookServerHandler

@Requires(beans = [Logbook::class])
@Singleton
class LogbookNettyServerCustomizer(private val logbook: Logbook) :
    BeanCreatedEventListener<NettyServerCustomizer.Registry> { // (1)

    override fun onCreated(event: BeanCreatedEvent<NettyServerCustomizer.Registry>): NettyServerCustomizer.Registry {
        val registry = event.bean
        registry.register(Customizer(null)) // (2)
        return registry
    }

    private inner class Customizer constructor(private val channel: Channel?) :
        NettyServerCustomizer { // (3)

        override fun specializeForChannel(channel: Channel, role: ChannelRole) = Customizer(channel) // (4)

        override fun onStreamPipelineBuilt() {
            channel!!.pipeline().addBefore( // (5)
                ChannelPipelineCustomizer.HANDLER_MICRONAUT_INBOUND,
                "logbook",
                LogbookServerHandler(logbook)
            )
        }
    }
}
```

Customizing the Netty server pipeline for Logbook

```groovy
import io.micronaut.context.annotation.Requires
import io.micronaut.context.event.BeanCreatedEvent
import io.micronaut.context.event.BeanCreatedEventListener
import io.micronaut.http.netty.channel.ChannelPipelineCustomizer
import io.micronaut.http.server.netty.NettyServerCustomizer
import io.netty.channel.Channel
import org.zalando.logbook.Logbook
import org.zalando.logbook.netty.LogbookServerHandler

import jakarta.inject.Singleton

@Requires(beans = Logbook.class)
@Singleton
class LogbookNettyServerCustomizer
        implements BeanCreatedEventListener<NettyServerCustomizer.Registry> { // (1)
    private final Logbook logbook;

    LogbookNettyServerCustomizer(Logbook logbook) {
        this.logbook = logbook
    }

    @Override
    NettyServerCustomizer.Registry onCreated(
            BeanCreatedEvent<NettyServerCustomizer.Registry> event) {

        NettyServerCustomizer.Registry registry = event.getBean()
        registry.register(new Customizer(null)) // (2)
        return registry
    }

    private class Customizer implements NettyServerCustomizer { // (3)
        private final Channel channel

        Customizer(Channel channel) {
            this.channel = channel
        }

        @Override
        NettyServerCustomizer specializeForChannel(Channel channel, ChannelRole role) {
            return new Customizer(channel) // (4)
        }

        @Override
        void onStreamPipelineBuilt() {
            channel.pipeline().addBefore( // (5)
                    ChannelPipelineCustomizer.HANDLER_HTTP_STREAM,
                    "logbook",
                    new LogbookServerHandler(logbook)
            )
        }
    }
}
```

| **1** | `LogbookNettyServerCustomizer` listens for a Registry and requires the definition of a `Logbook` bean |
|---|---|
| **2** | The root customizer is initialized without a channel and registered |
| **3** | The actual customizer implements NettyServerCustomizer |
| **4** | When a new channel is created, a new, specialized customizer is created for that channel |
| **5** | When the server signals that the stream pipeline has been fully constructed, the logbook handler is registered |

|   | As of version 4.5.0, the Micronaut netty HTTP server does not use per-request channels for HTTP/2 anymore. This makes many pipeline modifications (including logbook) difficult or impossible to implement. To revert to the old behavior, use the `micronaut.server.netty.legacy-multiplex-handlers=true` property. |
|---|---|


## 6.33.4 Advanced Listener Configuration

Instead of configuring a single port, you can also specify each listener manually.

```properties
micronaut.server.netty.listeners.httpListener.host=127.0.0.1
micronaut.server.netty.listeners.httpListener.port=8086
micronaut.server.netty.listeners.httpListener.ssl=false
micronaut.server.netty.listeners.httpsListener.port=8087
micronaut.server.netty.listeners.httpsListener.ssl=true
```

```yaml
micronaut:
  server:
    netty:
      listeners:
        httpListener:
          host: 127.0.0.1
          port: 8086
          ssl: false
        httpsListener:
          port: 8087
          ssl: true
```

```toml
[micronaut]
  [micronaut.server]
    [micronaut.server.netty]
      [micronaut.server.netty.listeners]
        [micronaut.server.netty.listeners.httpListener]
          host="127.0.0.1"
          port=8086
          ssl=false
        [micronaut.server.netty.listeners.httpsListener]
          port=8087
          ssl=true
```

```groovy
micronaut {
  server {
    netty {
      listeners {
        httpListener {
          host = "127.0.0.1"
          port = 8086
          ssl = false
        }
        httpsListener {
          port = 8087
          ssl = true
        }
      }
    }
  }
}
```

```hocon
{
  micronaut {
    server {
      netty {
        listeners {
          httpListener {
            host = "127.0.0.1"
            port = 8086
            ssl = false
          }
          httpsListener {
            port = 8087
            ssl = true
          }
        }
      }
    }
  }
}
```

```json
{
  "micronaut": {
    "server": {
      "netty": {
        "listeners": {
          "httpListener": {
            "host": "127.0.0.1",
            "port": 8086,
            "ssl": false
          },
          "httpsListener": {
            "port": 8087,
            "ssl": true
          }
        }
      }
    }
  }
}
```

- `httpListener` is a listener name, and can be an arbitrary value
- `host` is optional, and by default binds to all interfaces

|   | If you specify listeners manually, other configuration such as `micronaut.server.port` will be ignored. |
|---|---|

SSL can be enabled or disabled for each listener individually. When enabled, the SSL will be configured as described above.

The embedded server also supports binding to unix domain sockets using netty. This requires the following dependency:

`implementation("io.netty:netty-transport-native-unix-common")` `<dependency> <groupId>io.netty</groupId> <artifactId>netty-transport-native-unix-common</artifactId> </dependency>`

The server must also be configured to use native transport (epoll or kqueue).

```properties
micronaut.server.netty.listeners.unixListener.family=UNIX
micronaut.server.netty.listeners.unixListener.path=/run/micronaut.socket
micronaut.server.netty.listeners.unixListener.ssl=true
```

```yaml
micronaut:
  server:
    netty:
      listeners:
        unixListener:
          family: UNIX
          path: /run/micronaut.socket
          ssl: true
```

```toml
[micronaut]
  [micronaut.server]
    [micronaut.server.netty]
      [micronaut.server.netty.listeners]
        [micronaut.server.netty.listeners.unixListener]
          family="UNIX"
          path="/run/micronaut.socket"
          ssl=true
```

```groovy
micronaut {
  server {
    netty {
      listeners {
        unixListener {
          family = "UNIX"
          path = "/run/micronaut.socket"
          ssl = true
        }
      }
    }
  }
}
```

```hocon
{
  micronaut {
    server {
      netty {
        listeners {
          unixListener {
            family = "UNIX"
            path = "/run/micronaut.socket"
            ssl = true
          }
        }
      }
    }
  }
}
```

```json
{
  "micronaut": {
    "server": {
      "netty": {
        "listeners": {
          "unixListener": {
            "family": "UNIX",
            "path": "/run/micronaut.socket",
            "ssl": true
          }
        }
      }
    }
  }
}
```

- `unixListener` is a listener name, and can be an arbitrary value

|   | To use an abstract domain socket instead of a normal one, prefix the path with a NUL character, like `"\0/run/micronaut.socket"` |
|---|---|
