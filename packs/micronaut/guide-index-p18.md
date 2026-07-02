---
title: "Micronaut Core (part 18/27)"
source: https://docs.micronaut.io/latest/guide/index.html
domain: micronaut
license: CC-BY-SA-4.0
tags: micronaut framework, micronaut jvm, compile-time injection, microservices framework
fetched: 2026-07-02
part: 18/27
---

## 6.33.9 Starting Secondary Servers

The Micronaut framework supports the programmatic creation of additional Netty servers through the NettyEmbeddedServerFactory interface.

This is useful in cases where you, for example, need to expose distinct servers over different ports with potentially differing configurations (HTTPS, thread resources etc).

The following example demonstrates how to define a Factory Bean that starts an additional server using a programmatically created configuration:

Programmatically creating Secondary servers

```java
import java.util.Collections;
import io.micronaut.context.annotation.Bean;
import io.micronaut.context.annotation.Context;
import io.micronaut.context.annotation.Factory;
import io.micronaut.context.annotation.Requires;
import io.micronaut.context.env.Environment;
import io.micronaut.core.util.StringUtils;
import io.micronaut.discovery.ServiceInstanceList;
import io.micronaut.discovery.StaticServiceInstanceList;
import io.micronaut.http.server.netty.NettyEmbeddedServer;
import io.micronaut.http.server.netty.NettyEmbeddedServerFactory;
import io.micronaut.http.server.netty.configuration.NettyHttpServerConfiguration;
import io.micronaut.http.ssl.ServerSslConfiguration;
import jakarta.inject.Named;

@Factory
public class SecondaryNettyServer {
    public static final String SERVER_ID = "another"; // (1)

    @Named(SERVER_ID)
    @Context
    @Bean(preDestroy = "close") // (2)
    @Requires(beans = Environment.class)
    NettyEmbeddedServer nettyEmbeddedServer(NettyEmbeddedServerFactory serverFactory) { // (3)
        // configure server programmatically
        final NettyHttpServerConfiguration configuration =
                new NettyHttpServerConfiguration(); // (4)
        final ServerSslConfiguration sslConfiguration = new ServerSslConfiguration(); // (5)
        sslConfiguration.setBuildSelfSigned(true);
        sslConfiguration.setEnabled(true);
        sslConfiguration.setPort(-1); // random port
        final NettyEmbeddedServer embeddedServer = serverFactory.build(configuration, sslConfiguration); // (6)
        embeddedServer.start(); // (7)
        return embeddedServer; // (8)
    }

    @Bean
    ServiceInstanceList serviceInstanceList( // (9)
            @Named(SERVER_ID) NettyEmbeddedServer nettyEmbeddedServer) {
        return new StaticServiceInstanceList(
                SERVER_ID,
                Collections.singleton(nettyEmbeddedServer.getURI())
        );
    }
}
```

Programmatically creating Secondary servers

```kotlin
import io.micronaut.context.annotation.Bean
import io.micronaut.context.annotation.Context
import io.micronaut.context.annotation.Factory
import io.micronaut.context.annotation.Requires
import io.micronaut.context.env.Environment
import io.micronaut.core.util.StringUtils
import io.micronaut.discovery.ServiceInstanceList
import io.micronaut.discovery.StaticServiceInstanceList
import io.micronaut.http.server.netty.NettyEmbeddedServer
import io.micronaut.http.server.netty.NettyEmbeddedServerFactory
import io.micronaut.http.server.netty.configuration.NettyHttpServerConfiguration
import io.micronaut.http.ssl.ServerSslConfiguration
import jakarta.inject.Named

@Factory
class SecondaryNettyServer {
    companion object {
        const val SERVER_ID = "another" // (1)
    }

    @Named(SERVER_ID)
    @Context
    @Bean(preDestroy = "close") // (2)
    @Requires(beans = [Environment::class])
    fun nettyEmbeddedServer(
        serverFactory: NettyEmbeddedServerFactory // (3)
    ) : NettyEmbeddedServer {
        val configuration = NettyHttpServerConfiguration() // (4)
        val sslConfiguration = ServerSslConfiguration() // (5)

        sslConfiguration.setBuildSelfSigned(true)
        sslConfiguration.isEnabled = true
        sslConfiguration.port = -1 // random port

        // configure server programmatically
        val embeddedServer = serverFactory.build(configuration, sslConfiguration) // (6)
        embeddedServer.start() // (7)
        return embeddedServer // (8)
    }

    @Bean
    fun serviceInstanceList( // (9)
        @Named(SERVER_ID) nettyEmbeddedServer: NettyEmbeddedServer
    ): ServiceInstanceList {
        return StaticServiceInstanceList(
            SERVER_ID, setOf(nettyEmbeddedServer.uri)
        )
    }
}
```

Programmatically creating Secondary servers

```groovy
import io.micronaut.context.annotation.Bean
import io.micronaut.context.annotation.Context
import io.micronaut.context.annotation.Factory
import io.micronaut.context.annotation.Requires
import io.micronaut.context.env.Environment
import io.micronaut.core.util.StringUtils
import io.micronaut.discovery.ServiceInstanceList
import io.micronaut.discovery.StaticServiceInstanceList
import io.micronaut.http.server.netty.NettyEmbeddedServer
import io.micronaut.http.server.netty.NettyEmbeddedServerFactory
import io.micronaut.http.server.netty.configuration.NettyHttpServerConfiguration
import io.micronaut.http.ssl.ServerSslConfiguration
import jakarta.inject.Named

@Factory
class SecondaryNettyServer {
    static final String SERVER_ID = "another" // (1)

    @Named(SERVER_ID)
    @Context
    @Bean(preDestroy = "stop") // (2)
    @Requires(beans = Environment.class)
    NettyEmbeddedServer nettyEmbeddedServer(NettyEmbeddedServerFactory serverFactory) { // (3)
        def configuration =
                new NettyHttpServerConfiguration() // (4)
        def sslConfiguration = new ServerSslConfiguration() // (5)
        sslConfiguration.setBuildSelfSigned(true)
        sslConfiguration.enabled = true
        sslConfiguration.port = -1 // random port
        // configure server programmatically
        final NettyEmbeddedServer embeddedServer = serverFactory.build(configuration, sslConfiguration) // (5)
        embeddedServer.start() // (6)
        return embeddedServer // (7)
    }

    @Bean
    ServiceInstanceList serviceInstanceList( // (8)
                                             @Named(SERVER_ID) NettyEmbeddedServer nettyEmbeddedServer) {
        return new StaticServiceInstanceList(
                SERVER_ID,
                [ nettyEmbeddedServer.URI ]
        )
    }
}
```

| **1** | Define a unique name for the server |
|---|---|
| **2** | Define a @Context scoped bean using the server name and including `preDestroy="close"` to ensure the server is shutdown when the context is closed |
| **3** | Inject the NettyEmbeddedServerFactory into a Factory Bean |
| **4** | Programmatically create the NettyHttpServerConfiguration |
| **5** | Optionally create the ServerSslConfiguration |
| **6** | Use the `build` method to build the server instance |
| **7** | Start the server with the `start` method |
| **8** | Return the server instance as a managed bean |
| **9** | Optionally define an instance of ServiceInstanceList if you wish to inject HTTP Clients by the server name |

With this class in place when the ApplicationContext starts the server will also be started with the appropriate configuration.

Thanks to the definition of the ServiceInstanceList in step 8, you can then inject a client into your tests to test the secondary server:

Injecting the server or client

```java
@Client(path = "/", id = SecondaryNettyServer.SERVER_ID)
@Inject
HttpClient httpClient; // (1)

@Named(SecondaryNettyServer.SERVER_ID)
EmbeddedServer embeddedServer; // (2)
```

Injecting the server or client

```kotlin
@Inject
@field:Client(path = "/", id = SecondaryNettyServer.SERVER_ID)
lateinit var httpClient : HttpClient // (1)

@Inject
@field:Named(SecondaryNettyServer.SERVER_ID)
lateinit var embeddedServer : EmbeddedServer // (2)
```

Injecting the server or client

```groovy
@Client(path = "/", id = SecondaryNettyServer.SERVER_ID)
@Inject
HttpClient httpClient // (1)

@Named(SecondaryNettyServer.SERVER_ID)
EmbeddedServer embeddedServer // (2)
```

| **1** | Use the server name to inject a client by ID |
|---|---|
| **2** | Use the `@Named` annotation as a qualifier to inject the embedded server instance |


## 6.34 Server Side View Rendering

The Micronaut framework supports Server Side View Rendering.

See the documentation for Micronaut Views for more information.


## 6.35 OpenAPI / Swagger Support

To configure the Micronaut integration with OpenAPI/Swagger, please follow these instructions


## 6.36 GraphQL Support

GraphQL is a query language for building APIs that provides an intuitive and flexible syntax and a system for describing data requirements and interactions.

See the documentation for Micronaut GraphQL for more information on how to build GraphQL applications with Micronaut.

# 7 The HTTP Client

Client communication between Microservices is a critical component of any Microservice architecture. With that in mind, Micronaut framework includes an HTTP client that has both a low-level API and a higher-level AOP-driven API.

|   | Regardless whether you choose to use Micronaut’s HTTP server, you may wish to use the Micronaut HTTP client in your application since it is a feature-rich client implementation. |
|---|---|


## 7.1 HTTP Client Implementations

There are several implementations of the Micronaut HTTP Client.


## 7.1.1 HTTP Client based on Netty

To use an implementation based on Netty, add the following dependency to your build:

`implementation("io.micronaut:micronaut-http-client")` `<dependency> <groupId>io.micronaut</groupId> <artifactId>micronaut-http-client</artifactId> </dependency>`


## Disable hostname verification in ssl config

It may be necessary in a testing or development environment to disable hostname verification.

To disable hostname verification in your test classpath, you could create a Bean Replacement in `src/test/java`:

```java
package io.micronaut.http.client.netty.ssl;

import io.micronaut.context.annotation.BootstrapContextCompatible;
import io.micronaut.context.annotation.Replaces;
import io.micronaut.context.annotation.Requires;
import io.micronaut.context.annotation.Secondary;
import io.micronaut.context.env.Environment;
import io.micronaut.core.io.ResourceResolver;
import io.micronaut.http.client.HttpVersionSelection;
import io.micronaut.http.ssl.SslConfiguration;
import io.netty.handler.ssl.SslContextBuilder;
import jakarta.inject.Singleton;

@Requires(env = Environment.TEST)
@Singleton
@BootstrapContextCompatible
@Secondary
@Replaces(NettyClientSslBuilder.class)
class NettyClientSslBuilderReplacement extends NettyClientSslBuilder {
    NettyClientSslBuilderReplacement(ResourceResolver resourceResolver) {
        super(resourceResolver);
    }

    @Override
    protected SslContextBuilder createSslContextBuilder(SslConfiguration ssl, HttpVersionSelection versionSelection) {
        SslContextBuilder builder = super.createSslContextBuilder(ssl, versionSelection);
        builder.endpointIdentificationAlgorithm(null);
        return builder;
    }
}
```

|   | Disabling host name verification leaves your application potentially vulnerable to Man-in-the-Middle attacks and should only be done with the utmost care typically only in a development / testing environment. Never disable host name verification in production or in a scenario where you are making remote calls over the internet. |
|---|---|


## 7.1.2 HTTP Client based on the Java HTTP Client

To use an implementation based on Java HTTP Client, add the following dependency to your build:

`implementation("io.micronaut:micronaut-http-client-jdk")` `<dependency> <groupId>io.micronaut</groupId> <artifactId>micronaut-http-client-jdk</artifactId> </dependency>`

|   | This implementation of the Micronaut HTTP Client is available since Micronaut Framework 4.0. |
|---|---|

The implementation based on Java HTTP Client does not support the following features:

- Proxy request support (we do support HTTP Proxies).
- Client Filters.
- Streaming support.
- Multipart requests.
- H2C and HTTP/3.
- pcap logging

If you require any of these, we recommend you use the implementation of the HTTP Client based on Netty.


## 7.2 Low-Level and High-Level APIs

Since the higher level API is built on the low-level HTTP client, we first introduce the low-level client.


## 7.3 Using the Low-Level HTTP Client

The HttpClient interface forms the basis for the low-level API. This interfaces declares methods to help ease executing HTTP requests and receiving responses.

The majority of the methods in the HttpClient interface return Reactive Streams Publisher instances, which is not always the most useful interface to work against.

Micronaut’s Reactor HTTP Client dependency ships with a sub-interface named ReactorHttpClient. It provides a variation of the HttpClient interface that returns Project Reactor Flux types.

|   | See the guide for Micronaut HTTP Client to learn more. |
|---|---|


## 7.3.1 Sending your first HTTP request

#### Obtaining a HttpClient

There are a few ways to obtain a reference to an HttpClient. The most common is to use the Client annotation. For example:

Injecting an HTTP client

```java
@Client("https://api.twitter.com/1.1") @Inject HttpClient httpClient;
```

The above example injects a client that targets the Twitter API.

```kotlin
@field:Client("\${myapp.api.twitter.url}") @Inject lateinit var httpClient: HttpClient
```

The above Kotlin example injects a client that targets the Twitter API using a configuration path. Note the required escaping (backslash) on `"\${path.to.config}"` which is necessary due to Kotlin string interpolation.

The Client annotation is also a custom scope that manages the creation of HttpClient instances and ensures they are stopped when the application shuts down.

The value you pass to the Client annotation can be one of the following:

- An absolute URI, e.g. `https://api.twitter.com/1.1`
- A relative URI, in which case the targeted server will be the current server (useful for testing)
- A service identifier. See the section on Service Discovery for more information on this topic.

Another way to create an `HttpClient` is with the static `create` method of HttpClient, however this approach is not recommended as you must ensure you manually shutdown the client, and of course no dependency injection will occur for the created client.

#### Performing an HTTP GET

Generally there are two methods of interest when working with the `HttpClient`. The first is `retrieve`, which executes an HTTP request and returns the body in whichever type you request (by default a `String`) as `Publisher`.

The `retrieve` method accepts an HttpRequest or a `String` URI to the endpoint you wish to request.

The following example shows how to use `retrieve` to execute an HTTP `GET` and receive the response body as a `String`:

Using retrieve

```java
String uri = UriBuilder.of("/hello/{name}")
                       .expand(Collections.singletonMap("name", "John"))
                       .toString();
assertEquals("/hello/John", uri);

String result = client.toBlocking().retrieve(uri);

assertEquals("Hello John", result);
```

Using retrieve

```kotlin
val uri = UriBuilder.of("/hello/{name}")
                    .expand(Collections.singletonMap("name", "John"))
                    .toString()
uri shouldBe "/hello/John"

val result = client.toBlocking().retrieve(uri)

result shouldBe "Hello John"
```

Using retrieve

```groovy
when:
String uri = UriBuilder.of("/hello/{name}")
                       .expand(name: "John")
then:
"/hello/John" == uri

when:
String result = client.toBlocking().retrieve(uri)

then:
"Hello John" == result
```

Note that in this example, for illustration purposes we call `toBlocking()` to return a blocking version of the client. However, in production code you should not do this and instead rely on the non-blocking nature of the Micronaut HTTP server.

For example the following `@Controller` method calls another endpoint in a non-blocking manner:

Using the HTTP client without blocking

```java
import io.micronaut.http.annotation.Body;
import io.micronaut.http.annotation.Controller;
import io.micronaut.http.annotation.Get;
import io.micronaut.http.annotation.Post;
import io.micronaut.http.annotation.Status;
import io.micronaut.http.client.HttpClient;
import io.micronaut.http.client.annotation.Client;
import org.reactivestreams.Publisher;
import reactor.core.publisher.Mono;
import io.micronaut.core.async.annotation.SingleResult;
import static io.micronaut.http.HttpRequest.GET;
import static io.micronaut.http.HttpStatus.CREATED;
import static io.micronaut.http.MediaType.TEXT_PLAIN;

@Get("/hello/{name}")
@SingleResult
Publisher<String> hello(String name) { // (1)
    return Mono.from(httpClient.retrieve(GET("/hello/" + name))); // (2)
}
```

Using the HTTP client without blocking

```kotlin
import io.micronaut.http.HttpRequest.GET
import io.micronaut.http.HttpStatus.CREATED
import io.micronaut.http.MediaType.TEXT_PLAIN
import io.micronaut.http.annotation.Body
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Get
import io.micronaut.http.annotation.Post
import io.micronaut.http.annotation.Status
import io.micronaut.http.client.HttpClient
import io.micronaut.http.client.annotation.Client
import org.reactivestreams.Publisher
import reactor.core.publisher.Flux
import io.micronaut.core.async.annotation.SingleResult

@Get("/hello/{name}")
@SingleResult
internal fun hello(name: String): Publisher<String> { // (1)
    return Flux.from(httpClient.retrieve(GET<Any>("/hello/$name")))
                     .next() // (2)
}
```

Using the HTTP client without blocking

```groovy
import io.micronaut.http.annotation.Body
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Get
import io.micronaut.http.annotation.Post
import io.micronaut.http.annotation.Status
import io.micronaut.http.client.HttpClient
import io.micronaut.http.client.annotation.Client
import org.reactivestreams.Publisher
import io.micronaut.core.async.annotation.SingleResult
import reactor.core.publisher.Mono
import static io.micronaut.http.HttpRequest.GET
import static io.micronaut.http.HttpStatus.CREATED
import static io.micronaut.http.MediaType.TEXT_PLAIN

@Get("/hello/{name}")
@SingleResult
Publisher<String> hello(String name) { // (1)
    Mono.from(httpClient.retrieve( GET("/hello/" + name))) // (2)
}
```

| **1** | The `hello` method returns a Mono which may or may not emit an item. If an item is not emitted, a 404 is returned. |
|---|---|
| **2** | The `retrieve` method is called which returns a Flux. This has a `firstElement` method that returns the first emitted item or nothing |

|   | Using Reactor (or RxJava if you prefer) you can easily and efficiently compose multiple HTTP client calls without blocking (which limits the throughput and scalability of your application). |
|---|---|

#### Debugging / Tracing the HTTP Client

To debug requests being sent and received from the HTTP client you can enable tracing logging via your `logback.xml` file:

logback.xml

```xml
<logger name="io.micronaut.http.client" level="TRACE"/>
```

#### Client Specific Debugging / Tracing

To enable client-specific logging you can configure the default logger for all HTTP clients. You can also configure different loggers for different clients using Client-Specific Configuration. For example, in your configuration file (e.g `application.yml`):

```properties
micronaut.http.client.logger-name=mylogger
micronaut.http.services.otherClient.logger-name=other.client
```

```yaml
micronaut:
  http:
    client:
      logger-name: mylogger
    services:
      otherClient:
        logger-name: other.client
```

```toml
[micronaut]
  [micronaut.http]
    [micronaut.http.client]
      logger-name="mylogger"
    [micronaut.http.services]
      [micronaut.http.services.otherClient]
        logger-name="other.client"
```

```groovy
micronaut {
  http {
    client {
      loggerName = "mylogger"
    }
    services {
      otherClient {
        loggerName = "other.client"
      }
    }
  }
}
```

```hocon
{
  micronaut {
    http {
      client {
        logger-name = "mylogger"
      }
      services {
        otherClient {
          logger-name = "other.client"
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
      "client": {
        "logger-name": "mylogger"
      },
      "services": {
        "otherClient": {
          "logger-name": "other.client"
        }
      }
    }
  }
}
```

Then enable logging in `logback.xml`:

logback.xml

```xml
<logger name="mylogger" level="DEBUG"/>
<logger name="other.client" level="TRACE"/>
```

#### Customizing the HTTP Request

The previous example demonstrates using the static methods of the HttpRequest interface to construct a MutableHttpRequest instance. Like the name suggests, a `MutableHttpRequest` can be mutated, including the ability to add headers, customize the request body, etc. For example:

Passing an HttpRequest to retrieve

```java
Flux<String> response = Flux.from(client.retrieve(
        GET("/hello/John")
        .header("X-My-Header", "SomeValue")
));
```

Passing an HttpRequest to retrieve

```kotlin
val response = client.retrieve(
        GET<Any>("/hello/John")
                .header("X-My-Header", "SomeValue")
)
```

Passing an HttpRequest to retrieve

```groovy
Flux<String> response = Flux.from(client.retrieve(
        GET("/hello/John")
        .header("X-My-Header", "SomeValue")
))
```

The above example adds a header (`X-My-Header`) to the response before it is sent. The MutableHttpRequest interface has more convenience methods that make it easy to modify the request in common ways.

#### Reading JSON Responses

Microservices typically use a message encoding format such as JSON. Micronaut’s HTTP client leverages Jackson for JSON parsing, hence any type Jackson can decode can be passed as a second argument to `retrieve`.

For example consider the following `@Controller` method that returns a JSON response:

Returning JSON from a controller

```java
@Get("/greet/{name}")
Message greet(String name) {
    return new Message("Hello " + name);
}
```

Returning JSON from a controller

```kotlin
@Get("/greet/{name}")
internal fun greet(name: String): Message {
    return Message("Hello $name")
}
```

Returning JSON from a controller

```groovy
@Get("/greet/{name}")
Message greet(String name) {
    new Message("Hello $name")
}
```

The method above returns a POJO of type `Message` which looks like:

Message POJO

```java
import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;

public class Message {

    private final String text;

    @JsonCreator
    public Message(@JsonProperty("text") String text) {
        this.text = text;
    }

    public String getText() {
        return text;
    }
}
```

Message POJO

```kotlin
import com.fasterxml.jackson.annotation.JsonCreator
import com.fasterxml.jackson.annotation.JsonProperty

class Message @JsonCreator
constructor(@param:JsonProperty("text") val text: String)
```

Message POJO

```groovy
import com.fasterxml.jackson.annotation.JsonCreator
import com.fasterxml.jackson.annotation.JsonProperty

class Message {

    final String text

    @JsonCreator
    Message(@JsonProperty("text") String text) {
        this.text = text
    }
}
```

|   | Jackson annotations are used to map the constructor |
|---|---|

On the client you can call this endpoint and decode the JSON into a map using the `retrieve` method as follows:

Decoding the response body to a Map

```java
Flux<Map> response = Flux.from(client.retrieve(
        GET("/greet/John"), Map.class
));
```

Decoding the response body to a Map

```kotlin
var response: Flux<Map<*, *>> = Flux.from(client.retrieve(
        GET<Any>("/greet/John"), Map::class.java
))
```

Decoding the response body to a Map

```groovy
Flux<Map> response = Flux.from(client.retrieve(
        GET("/greet/John"), Map
))
```

The above example decodes the response into a Map representing the JSON. You can use the `Argument.of(..)` method to customize the type of the key and value:

Decoding the response body to a Map

```java
response = Flux.from(client.retrieve(
        GET("/greet/John"),
        Argument.of(Map.class, String.class, String.class) // (1)
));
```

Decoding the response body to a Map

```kotlin
response = Flux.from(client.retrieve(
        GET<Any>("/greet/John"),
        Argument.of(Map::class.java, String::class.java, String::class.java) // (1)
))
```

Decoding the response body to a Map

```groovy
response = Flux.from(client.retrieve(
        GET("/greet/John"),
        Argument.of(Map, String, String) // (1)
))
```

| **1** | The `Argument.of` method returns a `Map` where the key and value types are `String` |
|---|---|

Whilst retrieving JSON as a map can be desirable, typically you want to decode objects into POJOs. To do that, pass the type instead:

Decoding the response body to a POJO

```java
Flux<Message> response = Flux.from(client.retrieve(
        GET("/greet/John"), Message.class
));

assertEquals("Hello John", response.blockFirst().getText());
```

Decoding the response body to a POJO

```kotlin
val response = Flux.from(client.retrieve(
        GET<Any>("/greet/John"), Message::class.java
))

response.blockFirst()!!.text shouldBe "Hello John"
```

Decoding the response body to a POJO

```groovy
when:
Flux<Message> response = Flux.from(client.retrieve(
        GET("/greet/John"), Message
))

then:
"Hello John" == response.blockFirst().getText()
```

Note how you can use the same Java type on both the client and the server. The implication of this is that typically you define a common API project where you define the interfaces and types that define your API.

#### Decoding Other Content Types

If the server you communicate with uses a custom content type that is not JSON, by default Micronaut’s HTTP client will not know how to decode this type.

To resolve this, register MediaTypeCodec as a bean, and it will be automatically picked up and used to decode (or encode) messages.

#### Receiving the Full HTTP Response

Sometimes receiving just the body of the response is not enough, and you need other information from the response such as headers, cookies, etc. In this case, instead of `retrieve` use the `exchange` method:

Receiving the Full HTTP Response

```java
Flux<HttpResponse<Message>> call = Flux.from(client.exchange(
        GET("/greet/John"), Message.class // (1)
));

HttpResponse<Message> response = call.blockFirst();
Optional<Message> message = response.getBody(Message.class); // (2)
// check the status
assertEquals(HttpStatus.OK, response.getStatus()); // (3)
// check the body
assertTrue(message.isPresent());
assertEquals("Hello John", message.get().getText());
```

Receiving the Full HTTP Response

```kotlin
val call = client.exchange(
        GET<Any>("/greet/John"), Message::class.java // (1)
)

val response = Flux.from(call).blockFirst()!!
val message = response.getBody(Message::class.java) // (2)
// check the status
response.status shouldBe HttpStatus.OK // (3)
// check the body
message.isPresent shouldBe true
message.get().text shouldBe "Hello John"
```

Receiving the Full HTTP Response

```groovy
when:
Flux<HttpResponse<Message>> call = Flux.from(client.exchange(
        GET("/greet/John"), Message // (1)
))

HttpResponse<Message> response = call.blockFirst();
Optional<Message> message = response.getBody(Message) // (2)
// check the status
then:
HttpStatus.OK == response.getStatus() // (3)
// check the body
message.isPresent()
"Hello John" == message.get().getText()
```

| **1** | The `exchange` method receives the HttpResponse |
|---|---|
| **2** | The body is retrieved using the `getBody(..)` method of the response |
| **3** | Other aspects of the response such as the HttpStatus can be checked |

The above example receives the full HttpResponse from which you can obtain headers and other useful information.


## 7.3.2 Posting a Request Body

All the examples so far have used the same HTTP method i.e `GET`. The HttpRequest interface has factory methods for all the different HTTP methods. The following table summarizes them:

| Method | Description | Allows Body |
|---|---|---|
| HttpRequest.GET(java.lang.String) | Constructs an HTTP `GET` request | `false` |
| HttpRequest.OPTIONS(java.lang.String) | Constructs an HTTP `OPTIONS` request | `false` |
| HttpRequest.HEAD(java.lang.String) | Constructs an HTTP `HEAD` request | `false` |
| HttpRequest.POST(java.lang.String,T) | Constructs an HTTP `POST` request | `true` |
| HttpRequest.PUT(java.lang.String,T) | Constructs an HTTP `PUT` request | `true` |
| HttpRequest.PATCH(java.lang.String,T) | Constructs an HTTP `PATCH` request | `true` |
| HttpRequest.DELETE(java.lang.String) | Constructs an HTTP `DELETE` request | `true` |

A `create` method also exists to construct a request for any HttpMethod type. Since the `POST`, `PUT` and `PATCH` methods require a body, a second argument which is the body object is required.

The following example demonstrates how to send a simple `String` body:

Sending a

String

body

```java
Flux<HttpResponse<String>> call = Flux.from(client.exchange(
        POST("/hello", "Hello John") // (1)
            .contentType(MediaType.TEXT_PLAIN_TYPE)
            .accept(MediaType.TEXT_PLAIN_TYPE), // (2)
        String.class // (3)
));
```

Sending a

String

body

```kotlin
val call = client.exchange(
        POST("/hello", "Hello John") // (1)
                .contentType(MediaType.TEXT_PLAIN_TYPE)
                .accept(MediaType.TEXT_PLAIN_TYPE), String::class.java // (3)
)
```

Sending a

String

body

```groovy
Flux<HttpResponse<String>> call = Flux.from(client.exchange(
        POST("/hello", "Hello John") // (1)
            .contentType(MediaType.TEXT_PLAIN_TYPE)
            .accept(MediaType.TEXT_PLAIN_TYPE), // (2)
        String // (3)
))
```

| **1** | The `POST` method is used; the first argument is the URI and the second is the body |
|---|---|
| **2** | The content type and accepted type are set to `text/plain` (the default is `application/json`) |
| **3** | The expected response type is a `String` |


## Sending JSON

The previous example sends plain text. To send JSON, pass the object to encode to JSON (whether that be a Map or a POJO) as long as Jackson is able to encode it.

For example, you can create a `Message` from the previous section and pass it to the `POST` method:

Sending a JSON body

```java
Flux<HttpResponse<Message>> call = Flux.from(client.exchange(
        POST("/greet", new Message("Hello John")), // (1)
        Message.class // (2)
));
```

Sending a JSON body

```kotlin
val call = client.exchange(
        POST("/greet", Message("Hello John")), Message::class.java // (2)
)
```

Sending a JSON body

```groovy
Flux<HttpResponse<Message>> call = Flux.from(client.exchange(
        POST("/greet", new Message("Hello John")), // (1)
        Message // (2)
))
```

| **1** | An instance of `Message` is created and passed to the `POST` method |
|---|---|
| **2** | The same class decodes the response |

With the above example the following JSON is sent as the body of the request:

Resulting JSON

```json
{"text":"Hello John"}
```

The JSON can be customized using Jackson Annotations.


## Using a URI Template

If include some properties of the object in the URI, you can use a URI template.

For example imagine you have a `Book` class with a `title` property. You can include the `title` in the URI template and then populate it from an instance of `Book`. For example:

Sending a JSON body with a URI template

```java
Flux<HttpResponse<Book>> call = Flux.from(client.exchange(
        POST("/amazon/book/{title}", new Book("The Stand")),
        Book.class
));
```

Sending a JSON body with a URI template

```kotlin
val call = client.exchange(
        POST("/amazon/book/{title}", Book("The Stand")),
        Book::class.java
)
```

Sending a JSON body with a URI template

```groovy
Flux<HttpResponse<Book>> call = client.exchange(
        POST("/amazon/book/{title}", new Book("The Stand")),
        Book
);
```

In the above case the `title` property is included in the URI.


## Sending Form Data

You can also encode a POJO or a map as form data instead of JSON. Just set the content type to `application/x-www-form-urlencoded` on the post request:

Sending a Form Data

```java
Flux<HttpResponse<Book>> call = Flux.from(client.exchange(
        POST("/amazon/book/{title}", new Book("The Stand"))
        .contentType(MediaType.APPLICATION_FORM_URLENCODED),
        Book.class
));
```

Sending a Form Data

```kotlin
val call = client.exchange(
        POST("/amazon/book/{title}", Book("The Stand"))
                .contentType(MediaType.APPLICATION_FORM_URLENCODED),
        Book::class.java
)
```

Sending a Form Data

```groovy
Flux<HttpResponse<Book>> call = client.exchange(
        POST("/amazon/book/{title}", new Book("The Stand"))
        .contentType(MediaType.APPLICATION_FORM_URLENCODED),
        Book
)
```

Note that Jackson can bind form data too, so to customize the binding process use Jackson annotations.


## 7.3.3 Multipart Client Uploads

The Micronaut HTTP Client supports multipart requests. To build a multipart request, set the content type to `multipart/form-data` and set the body to an instance of MultipartBody.

For example:

Creating the body

```java
import io.micronaut.http.client.multipart.MultipartBody;

String toWrite = "test file";
File file = File.createTempFile("data", ".txt");
FileWriter writer = new FileWriter(file);
writer.write(toWrite);
writer.close();

MultipartBody requestBody = MultipartBody.builder()     // (1)
        .addPart(                                       // (2)
            "data",
            file.getName(),
            MediaType.TEXT_PLAIN_TYPE,
            file
        ).build();                                      // (3)
```

Creating the body

```kotlin
import io.micronaut.http.client.multipart.MultipartBody

val toWrite = "test file"
val file = File.createTempFile("data", ".txt")
val writer = FileWriter(file)
writer.write(toWrite)
writer.close()

val requestBody = MultipartBody.builder()     // (1)
        .addPart(                             // (2)
                "data",
                file.name,
                MediaType.TEXT_PLAIN_TYPE,
                file
        ).build()                             // (3)
```

Creating the body

```groovy
import io.micronaut.scheduling.TaskExecutors
import io.micronaut.scheduling.annotation.ExecuteOn
import org.reactivestreams.Publisher

File file = new File(uploadDir, "data.txt")
file.text = "test file"
file.createNewFile()

MultipartBody requestBody = MultipartBody.builder()     // (1)
        .addPart(                                       // (2)
            "data",
            file.name,
            MediaType.TEXT_PLAIN_TYPE,
            file
        ).build()                                       // (3)
```

| **1** | Create a MultipartBody builder for adding parts to the body. |
|---|---|
| **2** | Add a part to the body, in this case a file. There are different variations of this method in MultipartBody.Builder. |
| **3** | The build method assembles all parts from the builder into a MultipartBody. At least one part is required. |

Creating a request

```java
HttpRequest.POST("/multipart/upload", requestBody)    // (1)
           .contentType(MediaType.MULTIPART_FORM_DATA_TYPE) // (2)
```

Creating a request

```kotlin
HttpRequest.POST("/multipart/upload", requestBody)    // (1)
           .contentType(MediaType.MULTIPART_FORM_DATA_TYPE) // (2)
```

Creating a request

```groovy
HttpRequest.POST("/multipart/upload", requestBody)      // (1)
           .contentType(MediaType.MULTIPART_FORM_DATA_TYPE) // (2)
```

| **1** | The multipart request body with different types of data. |
|---|---|
| **2** | Set the content-type header of the request to `multipart/form-data`. |


## 7.3.4 Streaming JSON over HTTP

Micronaut’s HTTP client includes support for streaming data over HTTP via the ReactorStreamingHttpClient interface which includes methods specific to streaming including:

| Method | Description |
|---|---|
| `dataStream(HttpRequest<I> request)` | Returns a stream of data as a Flux of ByteBuffer |
| `exchangeStream(HttpRequest<I> request)` | Returns the HttpResponse wrapping a Flux of ByteBuffer |
| `jsonStream(HttpRequest<I> request)` | Returns a non-blocking stream of JSON objects |

To use JSON streaming, declare a controller method on the server that returns a `application/x-json-stream` of JSON objects. For example:

Streaming JSON on the Server

```java
import io.micronaut.http.MediaType;
import io.micronaut.http.annotation.Controller;
import io.micronaut.http.annotation.Get;
import org.reactivestreams.Publisher;
import reactor.core.publisher.Mono;
import java.time.Duration;
import java.time.ZonedDateTime;
import java.time.temporal.ChronoUnit;

@Get(value = "/headlines", processes = MediaType.APPLICATION_JSON_STREAM) // (1)
Publisher<Headline> streamHeadlines() {
    return Mono.fromCallable(() -> {  // (2)
        Headline headline = new Headline();
        headline.setText("Latest Headline at " + ZonedDateTime.now());
        return headline;
    }).repeat(100) // (3)
      .delayElements(Duration.of(1, ChronoUnit.SECONDS)); // (4)
}
```

Streaming JSON on the Server

```kotlin
import io.micronaut.http.MediaType.APPLICATION_JSON_STREAM
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Get
import reactor.core.publisher.Flux
import reactor.core.publisher.Mono
import java.time.Duration
import java.time.ZonedDateTime
import java.time.temporal.ChronoUnit
import java.util.concurrent.TimeUnit.SECONDS

@Get(value = "/headlines", processes = [APPLICATION_JSON_STREAM]) // (1)
internal fun streamHeadlines(): Flux<Headline> {
    return Mono.fromCallable { // (2)
        val headline = Headline()
        headline.text = "Latest Headline at ${ZonedDateTime.now()}"
        headline
    }.repeat(100) // (3)
     .delayElements(Duration.of(1, ChronoUnit.SECONDS)) // (4)
}
```

Streaming JSON on the Server

```groovy
import io.micronaut.http.MediaType
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Get
import reactor.core.publisher.Flux
import reactor.core.publisher.Mono

import java.time.Duration
import java.time.ZonedDateTime
import java.time.temporal.ChronoUnit
import java.util.concurrent.TimeUnit

@Get(value = "/headlines", processes = MediaType.APPLICATION_JSON_STREAM) // (1)
Flux<Headline> streamHeadlines() {
    Mono.fromCallable({ // (2)
        new Headline(text: "Latest Headline at ${ZonedDateTime.now()}")
    }).repeat(100) // (3)
            .delayElements(Duration.of(1, ChronoUnit.SECONDS)) // (4)
}
```

| **1** | The `streamHeadlines` method produces `application/x-json-stream` |
|---|---|
| **2** | A Flux is created from a `Callable` function (note no blocking occurs within the function, so this is ok, otherwise you should `subscribeOn` an I/O thread pool). |
| **3** | The Flux repeats 100 times |
| **4** | The Flux emits items with a delay of one second between each |

|   | The server does not have to be written in Micronaut, any server that supports JSON streaming will do. |
|---|---|

Then on the client, subscribe to the stream using `jsonStream` and every time the server emits a JSON object the client will decode and consume it:

Streaming JSON on the Client

```java
Flux<Headline> headlineStream = Flux.from(client.jsonStream(
        GET("/streaming/headlines"), Headline.class)); // (1)
CompletableFuture<Headline> future = new CompletableFuture<>(); // (2)
headlineStream.subscribe(new Subscriber<>() {
    @Override
    public void onSubscribe(Subscription s) {
        s.request(1); // (3)
    }

    @Override
    public void onNext(Headline headline) {
        System.out.println("Received Headline = " + headline.getText());
        future.complete(headline); // (4)
    }

    @Override
    public void onError(Throwable t) {
        future.completeExceptionally(t); // (5)
    }

    @Override
    public void onComplete() {
        // no-op // (6)
    }
});
```

Streaming JSON on the Client

```kotlin
val headlineStream = client.jsonStream(
    GET<Any>("/streaming/headlines"), Headline::class.java) // (1)
val future = CompletableFuture<Headline>() // (2)
headlineStream.subscribe(object : Subscriber<Headline> {
    override fun onSubscribe(s: Subscription) {
        s.request(1) // (3)
    }

    override fun onNext(headline: Headline) {
        println("Received Headline = ${headline.text!!}")
        future.complete(headline) // (4)
    }

    override fun onError(t: Throwable) {
        future.completeExceptionally(t) // (5)
    }

    override fun onComplete() {
        // no-op // (6)
    }
})
```

Streaming JSON on the Client

```groovy
Flux<Headline> headlineStream = Flux.from(client.jsonStream(
        GET("/streaming/headlines"), Headline)) // (1)
CompletableFuture<Headline> future = new CompletableFuture<>() // (2)
headlineStream.subscribe(new Subscriber<Headline>() {
    @Override
    void onSubscribe(Subscription s) {
        s.request(1) // (3)
    }

    @Override
    void onNext(Headline headline) {
        println "Received Headline = $headline.text"
        future.complete(headline) // (4)
    }

    @Override
    void onError(Throwable t) {
        future.completeExceptionally(t) // (5)
    }

    @Override
    void onComplete() {
        // no-op // (6)
    }
})
```

| **1** | The `jsonStream` method returns a Flux |
|---|---|
| **2** | A `CompletableFuture` is used to receive a value, but what you do with each emitted item is application-specific |
| **3** | The Subscription requests a single item. You can use the Subscription to regulate back pressure and demand. |
| **4** | The `onNext` method is called when an item is emitted |
| **5** | The `onError` method is called when an error occurs |
| **6** | The `onComplete` method is called when all `Headline` instances have been emitted |

Note neither the server nor the client in the example above perform any blocking I/O.
