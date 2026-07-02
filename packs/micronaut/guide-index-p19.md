---
title: "Micronaut Core (part 19/27)"
source: https://docs.micronaut.io/latest/guide/index.html
domain: micronaut
license: CC-BY-SA-4.0
tags: micronaut framework, micronaut jvm, compile-time injection, microservices framework
fetched: 2026-07-02
part: 19/27
---

## 7.3.5 Configuring HTTP clients

### Global Configuration for All Clients

The default HTTP client configuration is a Configuration Properties named DefaultHttpClientConfiguration that allows configuring the default behaviour for all HTTP clients. For example, in your configuration file (e.g `application.yml`):

Altering default HTTP client configuration

```properties
micronaut.http.client.read-timeout=5s
```

```yaml
micronaut:
  http:
    client:
      read-timeout: 5s
```

```toml
[micronaut]
  [micronaut.http]
    [micronaut.http.client]
      read-timeout="5s"
```

```groovy
micronaut {
  http {
    client {
      readTimeout = "5s"
    }
  }
}
```

```hocon
{
  micronaut {
    http {
      client {
        read-timeout = "5s"
      }
    }
  }
}
```

```json
{
  "micronaut": {
    "http": {
      "client": {
        "read-timeout": "5s"
      }
    }
  }
}
```

The above example sets the `readTimeout` property of the HttpClientConfiguration class.

### Client Specific Configuration

To have separate configuration per-client, there are a couple of options. You can configure Service Discovery manually in your configuration file (e.g. `application.yml`) and apply per-client configuration:

Manually configuring HTTP services

```properties
micronaut.http.services.foo.urls[0]=http://foo1
micronaut.http.services.foo.urls[1]=http://foo2
micronaut.http.services.foo.read-timeout=5s
```

```yaml
micronaut:
  http:
    services:
      foo:
        urls:
          - http://foo1
          - http://foo2
        read-timeout: 5s
```

```toml
[micronaut]
  [micronaut.http]
    [micronaut.http.services]
      [micronaut.http.services.foo]
        urls=[
          "http://foo1",
          "http://foo2"
        ]
        read-timeout="5s"
```

```groovy
micronaut {
  http {
    services {
      foo {
        urls = ["http://foo1", "http://foo2"]
        readTimeout = "5s"
      }
    }
  }
}
```

```hocon
{
  micronaut {
    http {
      services {
        foo {
          urls = ["http://foo1", "http://foo2"]
          read-timeout = "5s"
        }
      }
    }
  }
}
```

```json
{
  "micronaut": {
    "http": {
      "services": {
        "foo": {
          "urls": ["http://foo1", "http://foo2"],
          "read-timeout": "5s"
        }
      }
    }
  }
}
```

- The `read-timeout` is applied to the `foo` client.

For the Netty HTTP client, you can also plug in a custom DNS resolver by referencing a named Netty `AddressResolverGroup` bean with the `address-resolver-group-name` property. This is useful when you need custom name resolution behavior for a specific client.

Define a named

AddressResolverGroup

bean

```java
import io.micronaut.context.annotation.Factory;
import io.netty.resolver.AddressResolverGroup;
import io.netty.resolver.DefaultAddressResolverGroup;
import jakarta.inject.Named;
import jakarta.inject.Singleton;

@Factory
class CustomAddressResolverGroupFactory {

    @Singleton
    @Named("custom") // (1)
    AddressResolverGroup<?> customAddressResolverGroup() {
        return DefaultAddressResolverGroup.INSTANCE; // (2)
    }
}
```

Define a named

AddressResolverGroup

bean

```kotlin
import io.micronaut.context.annotation.Factory
import io.netty.resolver.AddressResolverGroup
import io.netty.resolver.DefaultAddressResolverGroup
import jakarta.inject.Named
import jakarta.inject.Singleton

@Factory
class CustomAddressResolverGroupFactory {

    @Singleton
    @Named("custom") // (1)
    fun customAddressResolverGroup(): AddressResolverGroup<*> {
        return DefaultAddressResolverGroup.INSTANCE // (2)
    }
}
```

Define a named

AddressResolverGroup

bean

```groovy
import io.micronaut.context.annotation.Factory
import io.netty.resolver.AddressResolverGroup
import io.netty.resolver.DefaultAddressResolverGroup
import jakarta.inject.Named
import jakarta.inject.Singleton

@Factory
class CustomAddressResolverGroupFactory {

    @Singleton
    @Named("custom") // (1)
    AddressResolverGroup<?> customAddressResolverGroup() {
        DefaultAddressResolverGroup.INSTANCE // (2)
    }
}
```

| **1** | Name the resolver bean so clients can reference it. |
|---|---|
| **2** | Return the `AddressResolverGroup` instance used by the Netty client. |

In the test suites, the named client is configured programmatically with the same properties:

Programmatic client configuration example

```java
static Map<String, Object> serviceConfiguration() {
    return Map.of(
        "micronaut.http.services.foo.urls[0]", "https://api.example.com", // (1)
        "micronaut.http.services.foo.address-resolver-group-name", "custom" // (2)
    );
}
```

Programmatic client configuration example

```kotlin
fun serviceConfiguration(): Map<String, Any> {
    return mapOf(
        "micronaut.http.services.foo.urls[0]" to "https://api.example.com", // (1)
        "micronaut.http.services.foo.address-resolver-group-name" to "custom" // (2)
    )
}
```

Programmatic client configuration example

```groovy
static Map<String, Object> serviceConfiguration() {
    [
        "micronaut.http.services.foo.urls[0]": "https://api.example.com", // (1)
        "micronaut.http.services.foo.address-resolver-group-name": "custom" // (2)
    ]
}
```

| **1** | Configure the service URL for the named client. |
|---|---|
| **2** | Reference the named resolver bean with `address-resolver-group-name`. |

The configured name must match an existing bean. When `address-resolver-group-name` is set, `dns-resolution-mode` is ignored.

WARN: This client configuration can be used in conjunction with the `@Client` annotation, either by injecting an `HttpClient` directly or use on a client interface. In any case, all other attributes on the annotation **will be ignored** except the service id.

Then, inject the named client configuration:

Injecting an HTTP client

```java
@Client("foo") @Inject ReactorHttpClient httpClient;
```

You can also define a bean that extends from HttpClientConfiguration and ensure that the `jakarta.inject.Named` annotation names it appropriately:

Defining an HTTP client configuration bean

```java
@Named("twitter")
@Singleton
class TwitterHttpClientConfiguration extends HttpClientConfiguration {
   public TwitterHttpClientConfiguration(ApplicationConfiguration configuration) {
        super(configuration);
    }
}
```

This configuration will be picked up if you inject a service named `twitter` with `@Client` using Service Discovery:

Injecting an HTTP client

```java
@Client("twitter") @Inject ReactorHttpClient httpClient;
```

Alternatively, if you don’t use service discovery you can use the `configuration` member of `@Client` to refer to a specific type:

Injecting an HTTP client

```java
@Client(value = "https://api.twitter.com/1.1",
        configuration = TwitterHttpClientConfiguration.class)
@Inject
ReactorHttpClient httpClient;
```

### Connection Pooling and HTTP/2

Connections using normal HTTP (without TLS/SSL) use HTTP/1.1. This can be configured using the `plaintext-mode` configuration option.

Secure connections (i.e. HTTP**S**, with TLS/SSL) use a feature called "Application Layer Protocol Negotiation" (ALPN) that is part of TLS to select the HTTP version. If the server supports HTTP/2, the Micronaut HTTP Client will use that capability by default, but if it doesn’t, HTTP/1.1 is still supported. This is configured using the `alpn-modes` option, which is a list of supported ALPN protocol IDs (`"h2"` and `"http/1.1"`).

|   | The HTTP/2 standard forbids the use of certain less secure TLS cipher suites for HTTP/2 connections. When the HTTP client supports HTTP/2 (which is the default), it will not support those cipher suites. Removing `"h2"` from `alpn-modes` will enable support for all cipher suites. |
|---|---|

Each HTTP/1.1 connection can only support one request at a time, but can be reused for subsequent requests using the `keep-alive` mechanism. HTTP/2 connections can support any number of concurrent requests.

To remove the overhead of opening a new connection for each request, the Micronaut HTTP Client will reuse HTTP connections wherever possible. They are managed in a *connection pool*. HTTP/1.1 connections are kept around using keep-alive and are used for new requests, and for HTTP/2, a single connection is used for all requests.

Manually configuring HTTP services

```properties
micronaut.http.services.foo.urls[0]=http://foo1
micronaut.http.services.foo.urls[1]=http://foo2
micronaut.http.services.foo.pool.max-concurrent-http1-connections=50
micronaut.http.services.foo.pool.enabled=true
micronaut.http.services.foo.pool.max-connections=50
```

```yaml
micronaut:
  http:
    services:
      foo:
        urls:
          - http://foo1
          - http://foo2
        pool:
          max-concurrent-http1-connections: 50
          enabled: true
          max-connections: 50
```

```toml
[micronaut]
  [micronaut.http]
    [micronaut.http.services]
      [micronaut.http.services.foo]
        urls=[
          "http://foo1",
          "http://foo2"
        ]
        [micronaut.http.services.foo.pool]
          max-concurrent-http1-connections=50
          enabled=true
          max-connections=50
```

```groovy
micronaut {
  http {
    services {
      foo {
        urls = ["http://foo1", "http://foo2"]
        pool {
          maxConcurrentHttp1Connections = 50
          enabled = true
          maxConnections = 50
        }
      }
    }
  }
}
```

```hocon
{
  micronaut {
    http {
      services {
        foo {
          urls = ["http://foo1", "http://foo2"]
          pool {
            max-concurrent-http1-connections = 50
            enabled = true
            max-connections = 50
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
    "http": {
      "services": {
        "foo": {
          "urls": ["http://foo1", "http://foo2"],
          "pool": {
            "max-concurrent-http1-connections": 50,
            "enabled": true,
            "max-connections": 50
          }
        }
      }
    }
  }
}
```

- Limit maximum concurrent HTTP/1.1 connections
- `max-concurrent-http1-connections` limits the maximum concurrent HTTP/1.1 connections to 50.
- `pool` enables the pool and sets the maximum number of connections for it

See the API for ConnectionPoolConfiguration for details on available pool configuration options.

By setting the `pool.enabled` property to `false`, you can disable connection reuse. The pool is still used and other configuration options (e.g. concurrent HTTP 1 connections) still apply, but one connection will only serve one request.

### Configuring Event Loop Groups

By default, the Micronaut framework shares a common Netty `EventLoopGroup` for worker threads and all HTTP client threads.

This `EventLoopGroup` can be configured via the `micronaut.netty.event-loops.default` property:

Configuring The Default Event Loop

```properties
micronaut.netty.event-loops.default.num-threads=10
```

```yaml
micronaut:
  netty:
    event-loops:
      default:
        num-threads: 10
```

```toml
[micronaut]
  [micronaut.netty]
    [micronaut.netty.event-loops]
      [micronaut.netty.event-loops.default]
        num-threads=10
```

```groovy
micronaut {
  netty {
    eventLoops {
      'default' {
        numThreads = 10
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
    "netty": {
      "event-loops": {
        "default": {
          "num-threads": 10
        }
      }
    }
  }
}
```

You can also use the `micronaut.netty.event-loops` setting to configure one or more additional event loops. The following table summarizes the properties:

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

For example, if your interactions with an HTTP client involve CPU-intensive work, it may be worthwhile configuring a separate `EventLoopGroup` for one or all clients.

The following example configures an additional event loop group called "other" with 10 threads:

Configuring Additional Event Loops

```properties
micronaut.netty.event-loops.other.num-threads=10
```

```yaml
micronaut:
  netty:
    event-loops:
      other:
        num-threads: 10
```

```toml
[micronaut]
  [micronaut.netty]
    [micronaut.netty.event-loops]
      [micronaut.netty.event-loops.other]
        num-threads=10
```

```groovy
micronaut {
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

Once an additional event loop has been configured you can alter the HTTP client configuration to use it:

Altering the Event Loop Group used by Clients

```properties
micronaut.http.client.event-loop-group=other
```

```yaml
micronaut:
  http:
    client:
      event-loop-group: other
```

```toml
[micronaut]
  [micronaut.http]
    [micronaut.http.client]
      event-loop-group="other"
```

```groovy
micronaut {
  http {
    client {
      eventLoopGroup = "other"
    }
  }
}
```

```hocon
{
  micronaut {
    http {
      client {
        event-loop-group = "other"
      }
    }
  }
}
```

```json
{
  "micronaut": {
    "http": {
      "client": {
        "event-loop-group": "other"
      }
    }
  }
}
```


## 7.3.6 Error Responses

If an HTTP response is returned with a code of 400 or higher, an HttpClientResponseException is created. The exception contains the original response. How that exception gets thrown depends on the return type of the method.

For blocking clients, the exception is thrown and should be caught and handled by the caller. For reactive clients, the exception is passed through the publisher as an error.


## 7.3.7 Bind Errors

Often you want to consume an endpoint and bind to a POJO if the request is successful and bind to a different POJO if an error occurs. The following example shows how to invoke `exchange` with a success and error type.

```java
@Controller("/books")
public class BooksController {

    @Get("/{isbn}")
    public HttpResponse find(String isbn) {
        if (isbn.equals("1680502395")) {
            Map<String, Object> m = new HashMap<>();
            m.put("status", 401);
            m.put("error", "Unauthorized");
            m.put("message", "No message available");
            m.put("path", "/books/" + isbn);
            return HttpResponse.status(HttpStatus.UNAUTHORIZED).body(m);
        }

        return HttpResponse.ok(new Book("1491950358", "Building Microservices"));
    }
}
```

```kotlin
@Controller("/books")
class BooksController {

    @Get("/{isbn}")
    fun find(isbn: String): HttpResponse<*> {
        if (isbn == "1680502395") {
            val m = mapOf(
                "status" to 401,
                "error" to "Unauthorized",
                "message" to "No message available",
                "path" to "/books/$isbn"
            )
            return HttpResponse.status<Any>(HttpStatus.UNAUTHORIZED).body(m)
        }

        return HttpResponse.ok(Book("1491950358", "Building Microservices"))
    }
}
```

```groovy
@Controller("/books")
class BooksController {

    @Get("/{isbn}")
    HttpResponse find(String isbn) {
        if (isbn == "1680502395") {
            Map<String, Object> m = [
                    status : 401,
                    error  : "Unauthorized",
                    message: "No message available",
                    path   : "/books/" + isbn]
            return HttpResponse.status(HttpStatus.UNAUTHORIZED).body(m)
        }

        return HttpResponse.ok(new Book("1491950358", "Building Microservices"))
    }
}
```

```java
@Test
void afterAnHttpClientExceptionTheResponseBodyCanBeBoundToAPOJO() {
    try {
        client.toBlocking().exchange(HttpRequest.GET("/books/1680502395"),
                Argument.of(Book.class), // (1)
                Argument.of(CustomError.class)); // (2)
    } catch (HttpClientResponseException e) {
        assertEquals(HttpStatus.UNAUTHORIZED, e.getResponse().getStatus());
        Optional<CustomError> jsonError = e.getResponse().getBody(CustomError.class);
        assertTrue(jsonError.isPresent());
        assertEquals(401, jsonError.get().status);
        assertEquals("Unauthorized", jsonError.get().error);
        assertEquals("No message available", jsonError.get().message);
        assertEquals("/books/1680502395", jsonError.get().path);
    }
}
```

```kotlin
"after an httpclient exception the response body can be bound to a POJO" {
    try {
        client.toBlocking().exchange(HttpRequest.GET<Any>("/books/1680502395"),
                Argument.of(Book::class.java), // (1)
                Argument.of(CustomError::class.java)) // (2)
    } catch (e: HttpClientResponseException) {
        e.response.status shouldBe HttpStatus.UNAUTHORIZED
    }
}
```

```groovy
def "after an HttpClientException the response body can be bound to a POJO"() {
    when:
    client.toBlocking().exchange(HttpRequest.GET("/books/1680502395"),
            Argument.of(Book), // (1)
            Argument.of(CustomError)) // (2)

    then:
    def e = thrown(HttpClientResponseException)
    e.response.status == HttpStatus.UNAUTHORIZED

    when:
    Optional<CustomError> jsonError = e.response.getBody(CustomError)

    then:
    jsonError.isPresent()
    jsonError.get().status == 401
    jsonError.get().error == 'Unauthorized'
    jsonError.get().message == 'No message available'
    jsonError.get().path == '/books/1680502395'
}
```

| **1** | Success Type |
|---|---|
| **2** | Error Type |


## 7.4 Proxying Requests with ProxyHttpClient

A common requirement in Microservice environments is to proxy requests in a Gateway Microservice to other backend Microservices.

The regular HttpClient API is designed around simplifying message exchange and is not designed for proxying requests. For this case, use the ProxyHttpClient, which can be used from an HTTP Server Filter to proxy requests to backend Microservices.

The following example demonstrates rewriting requests under the URI `/proxy` to the URI `/real` onto the same server (although in a real environment you generally proxy to another server):

Proxy filter that rewrites original requests

```java
import io.micronaut.core.async.publisher.Publishers;
import io.micronaut.core.util.StringUtils;
import io.micronaut.http.HttpRequest;
import io.micronaut.http.MutableHttpResponse;
import io.micronaut.http.annotation.Filter;
import io.micronaut.http.client.ProxyHttpClient;
import io.micronaut.http.filter.HttpServerFilter;
import io.micronaut.http.filter.ServerFilterChain;
import io.micronaut.runtime.server.EmbeddedServer;
import org.reactivestreams.Publisher;

@Filter("/proxy/**")
public class ProxyFilter implements HttpServerFilter { // (1)

    private final ProxyHttpClient client;
    private final EmbeddedServer embeddedServer;

    public ProxyFilter(ProxyHttpClient client,
                       EmbeddedServer embeddedServer) { // (2)
        this.client = client;
        this.embeddedServer = embeddedServer;
    }

    @Override
    public Publisher<MutableHttpResponse<?>> doFilter(HttpRequest<?> request,
                                                      ServerFilterChain chain) {
        return Publishers.map(client.proxy( // (3)
                request.mutate() // (4)
                        .uri(b -> b // (5)
                                .scheme("http")
                                .host(embeddedServer.getHost())
                                .port(embeddedServer.getPort())
                                .replacePath(StringUtils.prependUri(
                                        "/real",
                                        request.getPath().substring("/proxy".length())
                                ))
                        )
                        .header("X-My-Request-Header", "XXX") // (6)
        ), response -> response.header("X-My-Response-Header", "YYY"));
    }
}
```

Proxy filter that rewrites original requests

```kotlin
import io.micronaut.core.async.publisher.Publishers
import io.micronaut.core.util.StringUtils
import io.micronaut.http.HttpRequest
import io.micronaut.http.MutableHttpResponse
import io.micronaut.http.annotation.Filter
import io.micronaut.http.client.ProxyHttpClient
import io.micronaut.http.filter.HttpServerFilter
import io.micronaut.http.filter.ServerFilterChain
import io.micronaut.http.uri.UriBuilder
import io.micronaut.runtime.server.EmbeddedServer
import org.reactivestreams.Publisher

@Filter("/proxy/**")
class ProxyFilter(
    private val client: ProxyHttpClient, // (2)
    private val embeddedServer: EmbeddedServer
) : HttpServerFilter { // (1)

    override fun doFilter(request: HttpRequest<*>,
                          chain: ServerFilterChain): Publisher<MutableHttpResponse<*>> {
        return Publishers.map(client.proxy( // (3)
            request.mutate() // (4)
                .uri { b: UriBuilder -> // (5)
                    b.apply {
                        scheme("http")
                        host(embeddedServer.host)
                        port(embeddedServer.port)
                        replacePath(StringUtils.prependUri(
                            "/real",
                            request.path.substring("/proxy".length))
                        )
                    }
                }
                .header("X-My-Request-Header", "XXX") // (6)
        ), { response: MutableHttpResponse<*> -> response.header("X-My-Response-Header", "YYY") })
    }
}
```

Proxy filter that rewrites original requests

```groovy
import io.micronaut.core.async.publisher.Publishers
import io.micronaut.core.util.StringUtils
import io.micronaut.http.HttpRequest
import io.micronaut.http.MutableHttpResponse
import io.micronaut.http.annotation.Filter
import io.micronaut.http.client.ProxyHttpClient
import io.micronaut.http.filter.HttpServerFilter
import io.micronaut.http.filter.ServerFilterChain
import io.micronaut.http.uri.UriBuilder
import io.micronaut.runtime.server.EmbeddedServer
import org.reactivestreams.Publisher

@Filter("/proxy/**")
class ProxyFilter implements HttpServerFilter { // (1)

    private final ProxyHttpClient client
    private final EmbeddedServer embeddedServer

    ProxyFilter(ProxyHttpClient client,
                EmbeddedServer embeddedServer) { // (2)
        this.client = client
        this.embeddedServer = embeddedServer
    }

    @Override
    Publisher<MutableHttpResponse<?>> doFilter(HttpRequest<?> request,
                                               ServerFilterChain chain) {
        Publishers.map(client.proxy( // (3)
                request.mutate() // (4)
                        .uri { UriBuilder b -> // (5)
                            b.with {
                                scheme("http")
                                host(embeddedServer.host)
                                port(embeddedServer.port)
                                replacePath(StringUtils.prependUri(
                                        "/real",
                                        request.path.substring("/proxy".length())
                                ))
                            }
                        }
                        .header("X-My-Request-Header", "XXX") // (6)
        ), { it.header("X-My-Response-Header", "YYY") })
    }
}
```

| **1** | The filter extends HttpServerFilter |
|---|---|
| **2** | The ProxyHttpClient is injected into the constructor. |
| **3** | The `proxy` method proxies the request |
| **4** | The request is mutated to modify the URI and include an additional header |
| **5** | The UriBuilder API rewrites the URI |
| **6** | Additional request and response headers are included |

|   | The ProxyHttpClient API is a low-level API that can be used to build a higher-level abstraction such as an API Gateway. |
|---|---|


## 7.5 Declarative HTTP Clients with @Client

Now that you have an understanding of the workings of the lower-level HTTP client, let’s take a look at Micronaut’s support for declarative clients via the Client annotation.

Essentially, the `@Client` annotation can be declared on any interface or abstract class, and through the use of Introduction Advice the abstract methods are implemented for you at compile time, greatly simplifying the creation of HTTP clients.

Let’s start with a simple example. Given the following class:

Pet.java

```java
public class Pet {
    private String name;
    private int age;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }
}
```

Pet.java

```kotlin
class Pet {
    var name: String? = null
    var age: Int = 0
}
```

Pet.java

```groovy
class Pet {
    String name
    int age
}
```

You can define a common interface for saving new `Pet` instances:

PetOperations.java

```java
import io.micronaut.http.annotation.Post;
import io.micronaut.validation.Validated;
import org.reactivestreams.Publisher;
import io.micronaut.core.async.annotation.SingleResult;
import jakarta.validation.constraints.Min;
import jakarta.validation.constraints.NotBlank;

@Validated
public interface PetOperations {
    @Post
    @SingleResult
    Publisher<Pet> save(@NotBlank String name, @Min(1L) int age);
}
```

PetOperations.java

```kotlin
import io.micronaut.http.annotation.Post
import io.micronaut.validation.Validated
import jakarta.validation.constraints.Min
import jakarta.validation.constraints.NotBlank
import io.micronaut.core.async.annotation.SingleResult
import org.reactivestreams.Publisher

@Validated
interface PetOperations {
    @Post
    @SingleResult
    fun save(@NotBlank name: String, @Min(1L) age: Int): Publisher<Pet>
}
```

PetOperations.java

```groovy
import io.micronaut.http.annotation.Post
import io.micronaut.validation.Validated
import org.reactivestreams.Publisher
import io.micronaut.core.async.annotation.SingleResult
import jakarta.validation.constraints.Min
import jakarta.validation.constraints.NotBlank

@Validated
interface PetOperations {
    @Post
    @SingleResult
    Publisher<Pet> save(@NotBlank String name, @Min(1L) int age)
}
```

Note how the interface uses Micronaut’s HTTP annotations which are usable on both the server and client side. You can also use `jakarta.validation` constraints to validate arguments.

|   | Be aware that some annotations, such as Produces and Consumes, have different semantics between server and client side usage. For example, `@Produces` on a controller method (server side) indicates how the method’s **return value** is formatted, while `@Produces` on a client indicates how the method’s **parameters** are formatted when sent to the server. While this may seem a little confusing, it is logical considering the different semantics between a server producing/consuming vs a client: a server consumes an argument and **returns** a response to the client, whereas a client consumes an argument and **sends** output to a server. |
|---|---|

Additionally, to use the `jakarta.validation` features, add the `validation` module to your build:

`implementation("io.micronaut:micronaut-validation")` `<dependency> <groupId>io.micronaut</groupId> <artifactId>micronaut-validation</artifactId> </dependency>`

On the server-side of the Micronaut framework you can implement the `PetOperations` interface:

PetController.java

```java
import io.micronaut.http.annotation.Controller;
import org.reactivestreams.Publisher;
import reactor.core.publisher.Mono;
import io.micronaut.core.async.annotation.SingleResult;

@Controller("/pets")
public class PetController implements PetOperations {

    @Override
    @SingleResult
    public Publisher<Pet> save(String name, int age) {
        Pet pet = new Pet();
        pet.setName(name);
        pet.setAge(age);
        // save to database or something
        return Mono.just(pet);
    }
}
```

PetController.java

```kotlin
import io.micronaut.http.annotation.Controller
import reactor.core.publisher.Mono
import io.micronaut.core.async.annotation.SingleResult
import org.reactivestreams.Publisher

@Controller("/pets")
open class PetController : PetOperations {

    @SingleResult
    override fun save(name: String, age: Int): Publisher<Pet> {
        val pet = Pet()
        pet.name = name
        pet.age = age
        // save to database or something
        return Mono.just(pet)
    }
}
```

PetController.java

```groovy
import io.micronaut.http.annotation.Controller
import org.reactivestreams.Publisher
import io.micronaut.core.async.annotation.SingleResult
import reactor.core.publisher.Mono

@Controller("/pets")
class PetController implements PetOperations {

    @Override
    @SingleResult
    Publisher<Pet> save(String name, int age) {
        Pet pet = new Pet(name: name, age: age)
        // save to database or something
        return Mono.just(pet)
    }
}
```

You can then define a declarative client in `src/test/java` that uses `@Client` to automatically implement a client at compile time:

PetClient.java

```java
import io.micronaut.http.client.annotation.Client;
import org.reactivestreams.Publisher;
import io.micronaut.core.async.annotation.SingleResult;
import jakarta.validation.constraints.Min;
import jakarta.validation.constraints.NotBlank;

@Client("/pets") // (1)
public interface PetClient extends PetOperations { // (2)

    @Override
    @SingleResult
    Publisher<Pet> save(@NotBlank String name, @Min(1L) int age); // (3)
}
```

PetClient.java

```kotlin
import io.micronaut.http.client.annotation.Client
import io.micronaut.core.async.annotation.SingleResult
import org.reactivestreams.Publisher

@Client("/pets") // (1)
interface PetClient : PetOperations { // (2)

    @SingleResult
    override fun save(name: String, age: Int): Publisher<Pet> // (3)
}
```

PetClient.java

```groovy
import io.micronaut.http.client.annotation.Client
import org.reactivestreams.Publisher
import io.micronaut.core.async.annotation.SingleResult

@Client("/pets") // (1)
interface PetClient extends PetOperations { // (2)

    @Override
    @SingleResult
    Publisher<Pet> save(String name, int age) // (3)
}
```

| **1** | The Client annotation is used with a value relative to the current server, in this case `/pets` |
|---|---|
| **2** | The interface extends from `PetOperations` |
| **3** | The `save` method is overridden. See the warning below. |

|   | Notice in the above example we override the `save` method. This is necessary if you compile without the `-parameters` option since Java does not retain parameters names in bytecode otherwise. Overriding is not necessary if you compile with `-parameters`. In addition, when overriding methods you should ensure any validation annotations are declared again since these are not Inherited annotations. |
|---|---|

Once you have defined a client you can `@Inject` it wherever you need it.

Recall that the value of `@Client` can be:

- An absolute URI, e.g. `https://api.twitter.com/1.1`
- A relative URI, in which case the server targeted is the current server (useful for testing)
- A service identifier. See the section on Service Discovery for more information on this topic.

In production, you typically use a service ID and Service Discovery to discover services automatically.

Another important thing to notice regarding the `save` method in the example above is that it returns a Single type.

This is a non-blocking reactive type - typically you want your HTTP clients to not block. There are cases where you may want an HTTP client that does block (such as in unit tests), but this is rare.

The following table illustrates common return types usable with @Client:

| Type | Description | Example Signature |
|---|---|---|
| Publisher | Any type that implements the Publisher interface | `Flux<String> hello()` |
| HttpResponse | An HttpResponse and optional response body type | `Mono<HttpResponse<String>> hello()` |
| Publisher | A Publisher implementation that emits a POJO | `Mono<Book> hello()` |
| CompletableFuture | A Java `CompletableFuture` instance | `CompletableFuture<String> hello()` |
| CharSequence | A blocking native type. Such as `String` | `String hello()` |
| T | Any simple POJO type. | `Book show()` |

Generally, any reactive type that can be converted to the Publisher interface is supported as a return type, including (but not limited to) the reactive types defined by RxJava 1.x, RxJava 2.x, and Reactor 3.x.

Returning CompletableFuture instances is also supported. Note that returning any other type *results in a blocking request* and is not recommended other than for testing.


## 7.5.1 Customizing Parameter Binding

The previous example presented a simple example using method parameters to represent the body of a `POST` request:

PetOperations.java

```java
@Post
@SingleResult
Publisher<Pet> save(@NotBlank String name, @Min(1L) int age);
```

The `save` method performs an HTTP `POST` with the following JSON by default:

Example Produced JSON

```json
{"name":"Dino", "age":10}
```

You may however want to customize what is sent as the body, the parameters, URI variables, etc. The @Client annotation is very flexible in this regard and supports the same io.micronaut.http.annotation as Micronaut’s HTTP server.

For example, the following defines a URI template, and the `name` parameter is used as part of the URI template, whilst @Body declares that the contents to send to the server are represented by the `Pet` POJO:

PetOperations.java

```java
@Post("/{name}")
Mono<Pet> save(
    @NotBlank String name, (1)
    @Body @Valid Pet pet) (2)
```

| **1** | The name parameter, included as part of the URI, and declared `@NotBlank` |
|---|---|
| **2** | The `pet` parameter, used to encode the body and declared `@Valid` |

The following table summarizes the parameter annotations and their purpose, and provides an example:

| Annotation | Description | Example |
|---|---|---|
| @Body | Specifies the parameter for the body of the request | `@Body String body` |
| @CookieValue | Specifies parameters to be sent as cookies | `@CookieValue String myCookie` |
| @Header | Specifies parameters to be sent as HTTP headers | `@Header String requestId` |
| @QueryValue | Customizes the name of the URI parameter to bind from | `@QueryValue("userAge") Integer age` |
| @PathVariable | Binds a parameter exclusively from a Path Variable. | `@PathVariable Long id` |
| @RequestAttribute | Specifies parameters to be set as request attributes | `@RequestAttribute Integer locationId` |

|   | Always use @Produces or @Consumes instead of supplying a header for `Content-Type` or `Accept`. |
|---|---|
