---
title: "Micronaut Core (part 21/27)"
source: https://docs.micronaut.io/latest/guide/index.html
domain: micronaut
license: CC-BY-SA-4.0
tags: micronaut framework, micronaut jvm, compile-time injection, microservices framework
fetched: 2026-07-02
part: 21/27
---

## 7.6 HTTP Client Filters

Often, you need to include the same HTTP headers or URL parameters in a set of requests against a third-party API or when calling another Microservice.

To simplify this, you can define ClientFilter classes that are applied to all matching HTTP client requests. The details of how filters worked are described in the server filter documentation. Here we will only show some client filters.

As an example, say you want to build a client to communicate with the Bintray REST API. It would be tedious to specify authentication for every single HTTP call.

To resolve this you can define a filter. The following is an example `BintrayService`:

```java
class BintrayApi {
    public static final String URL = 'https://api.bintray.com'
}

@Singleton
class BintrayService {
    final HttpClient client;
    final String org;

    BintrayService(
            @Client(BintrayApi.URL) HttpClient client,           // (1)
            @Value("${bintray.organization}") String org ) {
        this.client = client;
        this.org = org;
    }

    Flux<HttpResponse<String>> fetchRepositories() {
        return Flux.from(client.exchange(HttpRequest.GET(
                "/repos/" + org), String.class)); // (2)
    }

    Flux<HttpResponse<String>> fetchPackages(String repo) {
        return Flux.from(client.exchange(HttpRequest.GET(
                "/repos/" + org + "/" + repo + "/packages"), String.class)); // (2)
    }
}
```

```kotlin
class BintrayApi {
    public static final String URL = 'https://api.bintray.com'
}

@Singleton
internal class BintrayService(
    @param:Client(BintrayApi.URL) val client: HttpClient, // (1)
    @param:Value("\${bintray.organization}") val org: String) {

    fun fetchRepositories(): Flux<HttpResponse<String>> {
        return Flux.from(client.exchange(HttpRequest.GET<Any>("/repos/$org"), String::class.java)) // (2)
    }

    fun fetchPackages(repo: String): Flux<HttpResponse<String>> {
        return Flux.from(client.exchange(HttpRequest.GET<Any>("/repos/$org/$repo/packages"), String::class.java)) // (2)
    }
}
```

```groovy
class BintrayApi {
    public static final String URL = 'https://api.bintray.com'
}

@Singleton
class BintrayService {
    final HttpClient client
    final String org

    BintrayService(
            @Client(BintrayApi.URL) HttpClient client, // (1)
            @Value('${bintray.organization}') String org ) {
        this.client = client
        this.org = org
    }

    Flux<HttpResponse<String>> fetchRepositories() {
        client.exchange(HttpRequest.GET("/repos/$org"), String) // (2)
    }

    Flux<HttpResponse<String>> fetchPackages(String repo) {
        client.exchange(HttpRequest.GET("/repos/${org}/${repo}/packages"), String) // (2)
    }
}
```

| **1** | An ReactorHttpClient is injected for the Bintray API |
|---|---|
| **2** | The organization is configurable via configuration |

The Bintray API is secured. To authenticate you add an `Authorization` header for every request. You can modify `fetchRepositories` and `fetchPackages` methods to include the necessary HTTP Header for each request, but using a filter is much simpler:

```java
@ClientFilter("/repos/**") // (1)
class BintrayFilter {

    final String username;
    final String token;

    BintrayFilter(
            @Value("${bintray.username}") String username, // (2)
            @Value("${bintray.token}") String token ) { // (2)
        this.username = username;
        this.token = token;
    }

    @RequestFilter
    public void filter(MutableHttpRequest<?> request) {
        request.basicAuth(username, token); // (3)
    }
}
```

```kotlin
@Filter("/repos/**") // (1)
internal class BintrayFilter(
        @param:Value("\${bintray.username}") val username: String, // (2)
        @param:Value("\${bintray.token}") val token: String)// (2)
    : HttpClientFilter {

    override fun doFilter(request: MutableHttpRequest<*>, chain: ClientFilterChain): Publisher<out HttpResponse<*>> {
        return chain.proceed(
            request.basicAuth(username, token) // (3)
        )
    }
}
```

```groovy
@ClientFilter('/repos/**') // (1)
class BintrayFilter {

    final String username
    final String token

    BintrayFilter(
            @Value('${bintray.username}') String username, // (2)
            @Value('${bintray.token}') String token ) { // (2)
        this.username = username
        this.token = token
    }

    @RequestFilter
    void filter(MutableHttpRequest<?> request) {
        request.basicAuth(username, token) // (3)
    }
}
```

| **1** | You can match only a subset of paths with a Client filter. |
|---|---|
| **2** | The `username` and `token` are injected via configuration |
| **3** | The `basicAuth` method includes HTTP Basic credentials |

Now when you invoke the `bintrayService.fetchRepositories()` method, the `Authorization` HTTP header is included in the request.

### Injecting Another Client into a ClientFilter

To create an ReactorHttpClient, the Micronaut framework needs to resolve all `ClientFilter` beans, which creates a circular dependency when injecting another ReactorHttpClient or a `@Client` bean into an instance of a `ClientFilter`.

To resolve this issue, use the BeanProvider interface to inject another ReactorHttpClient or a `@Client` bean into an instance of `ClientFilter`.

The following example which implements a filter allowing authentication between services on Google Cloud Run demonstrates how to use BeanProvider to inject another client:

```java
import io.micronaut.context.BeanProvider;
import io.micronaut.context.annotation.Requires;
import io.micronaut.context.env.Environment;
import io.micronaut.http.HttpRequest;
import io.micronaut.http.MutableHttpRequest;
import io.micronaut.http.annotation.ClientFilter;
import io.micronaut.http.annotation.RequestFilter;
import io.micronaut.http.client.HttpClient;
import io.micronaut.scheduling.TaskExecutors;
import io.micronaut.scheduling.annotation.ExecuteOn;

import java.io.UnsupportedEncodingException;
import java.net.URI;
import java.net.URLEncoder;

@Requires(env = Environment.GOOGLE_COMPUTE)
@ClientFilter(patterns = "/google-auth/api/**")
public class GoogleAuthFilter {

    private final BeanProvider<HttpClient> authClientProvider;

    public GoogleAuthFilter(BeanProvider<HttpClient> httpClientProvider) { // (1)
        this.authClientProvider = httpClientProvider;
    }

    @RequestFilter
    @ExecuteOn(TaskExecutors.BLOCKING)
    public void filter(MutableHttpRequest<?> request) throws Exception {
        String uri = encodeURI(request);
        String t = authClientProvider.get().toBlocking().retrieve(HttpRequest.GET(uri) // (2)
            .header("Metadata-Flavor", "Google"));
        request.bearerAuth(t);
    }

    private String encodeURI(MutableHttpRequest<?> request) throws UnsupportedEncodingException {
        URI fullURI = request.getUri();
        String receivingURI = fullURI.getScheme() + "://" + fullURI.getHost();
        return "http://metadata/computeMetadata/v1/instance/service-accounts/default/identity?audience=" +
                URLEncoder.encode(receivingURI, "UTF-8");
    }
}
```

```kotlin
import io.micronaut.context.BeanProvider
import io.micronaut.context.annotation.Requires
import io.micronaut.context.env.Environment
import io.micronaut.http.HttpRequest
import io.micronaut.http.HttpResponse
import io.micronaut.http.MutableHttpRequest
import io.micronaut.http.annotation.Filter
import io.micronaut.http.client.HttpClient
import io.micronaut.http.filter.ClientFilterChain
import io.micronaut.http.filter.HttpClientFilter
import org.reactivestreams.Publisher
import reactor.core.publisher.Mono
import java.net.URLEncoder

@Requires(env = [Environment.GOOGLE_COMPUTE])
@Filter(patterns = ["/google-auth/api/**"])
class GoogleAuthFilter (
    private val authClientProvider: BeanProvider<HttpClient>) : HttpClientFilter { // (1)

    override fun doFilter(request: MutableHttpRequest<*>,
                          chain: ClientFilterChain): Publisher<out HttpResponse<*>?> {
        return Mono.fromCallable { encodeURI(request) }
            .flux()
            .map { authURI: String ->
                authClientProvider.get().retrieve(HttpRequest.GET<Any>(authURI)
                    .header("Metadata-Flavor", "Google") // (2)
                )
            }.flatMap { t -> chain.proceed(request.bearerAuth(t.toString())) }
    }

    private fun encodeURI(request: MutableHttpRequest<*>): String {
        val receivingURI = "${request.uri.scheme}://${request.uri.host}"
        return "http://metadata/computeMetadata/v1/instance/service-accounts/default/identity?audience=" +
                URLEncoder.encode(receivingURI, "UTF-8")
    }

}
```

```groovy
import io.micronaut.http.MutableHttpRequest
import io.micronaut.http.annotation.ClientFilter
import io.micronaut.http.annotation.RequestFilter
import io.micronaut.http.client.HttpClient
import io.micronaut.scheduling.TaskExecutors
import io.micronaut.scheduling.annotation.ExecuteOn

@Requires(env = Environment.GOOGLE_COMPUTE)
@ClientFilter(patterns = "/google-auth/api/**")
class GoogleAuthFilter {

    private final BeanProvider<HttpClient> authClientProvider

    GoogleAuthFilter(BeanProvider<HttpClient> httpClientProvider) { // (1)
        this.authClientProvider = httpClientProvider
    }

    @RequestFilter
    @ExecuteOn(TaskExecutors.BLOCKING)
    void filter(MutableHttpRequest<?> request) {
        String authURI = encodeURI(request)
        String token = authClientProvider.get().toBlocking().retrieve(HttpRequest.GET(authURI).header( // (2)
                "Metadata-Flavor", "Google"
        ))

        request.bearerAuth(token)
    }

    private static String encodeURI(MutableHttpRequest<?> request) {
        String receivingURI = "$request.uri.scheme://$request.uri.host"
        "http://metadata/computeMetadata/v1/instance/service-accounts/default/identity?audience=" +
                URLEncoder.encode(receivingURI, "UTF-8")
    }
}
```

| **1** | The BeanProvider interface is used to inject another client, avoiding a circular reference |
|---|---|
| **2** | The `get()` method of the `Provider` interface is used to obtain the client instance. |

### Filter Matching By Annotation

For cases where a filter should be applied to a client regardless of the URL, filters can be matched by the presence of an annotation applied to both the filter and the client. Given the following client:

```java
import io.micronaut.http.annotation.Get;
import io.micronaut.http.client.annotation.Client;

@BasicAuth // (1)
@Client("/message")
public interface BasicAuthClient {

    @Get
    String getMessage();
}
```

```kotlin
import io.micronaut.http.annotation.Get
import io.micronaut.http.client.annotation.Client

@BasicAuth // (1)
@Client("/message")
interface BasicAuthClient {

    @Get
    fun getMessage(): String
}
```

```groovy
import io.micronaut.http.annotation.Get
import io.micronaut.http.client.annotation.Client

@BasicAuth // (1)
@Client("/message")
interface BasicAuthClient {

    @Get
    String getMessage()
}
```

| **1** | The `@BasicAuth` annotation is applied to the client |
|---|---|

The following filter will filter the client requests:

```java
import io.micronaut.http.MutableHttpRequest;
import io.micronaut.http.annotation.ClientFilter;
import io.micronaut.http.annotation.RequestFilter;
import jakarta.inject.Singleton;

@BasicAuth // (1)
@Singleton // (2)
@ClientFilter
public class BasicAuthClientFilter {

    @RequestFilter
    public void filter(MutableHttpRequest<?> request) {
        request.basicAuth("user", "pass");
    }
}
```

```kotlin
import io.micronaut.http.HttpResponse
import io.micronaut.http.MutableHttpRequest
import io.micronaut.http.filter.ClientFilterChain
import io.micronaut.http.filter.HttpClientFilter
import org.reactivestreams.Publisher

import jakarta.inject.Singleton

@BasicAuth // (1)
@Singleton // (2)
class BasicAuthClientFilter : HttpClientFilter {

    override fun doFilter(request: MutableHttpRequest<*>,
                          chain: ClientFilterChain): Publisher<out HttpResponse<*>> {
        return chain.proceed(request.basicAuth("user", "pass"))
    }
}
```

```groovy
import io.micronaut.http.MutableHttpRequest
import io.micronaut.http.annotation.ClientFilter
import io.micronaut.http.annotation.RequestFilter
import jakarta.inject.Singleton

@BasicAuth // (1)
@Singleton // (2)
@ClientFilter
class BasicAuthClientFilter {

    @RequestFilter
    void filter(MutableHttpRequest<?> request) {
        request.basicAuth("user", "pass")
    }
}
```

| **1** | The same annotation, `@BasicAuth`, is applied to the filter |
|---|---|
| **2** | Normally the `@Filter` annotation makes filters singletons by default. Because the `@Filter` annotation is not used, the desired scope must be applied |

The `@BasicAuth` annotation is just an example and can be replaced with your own.

```java
import io.micronaut.http.annotation.FilterMatcher;

import java.lang.annotation.Documented;
import java.lang.annotation.Retention;
import java.lang.annotation.Target;

import static java.lang.annotation.ElementType.PARAMETER;
import static java.lang.annotation.ElementType.TYPE;
import static java.lang.annotation.RetentionPolicy.RUNTIME;

@FilterMatcher // (1)
@Documented
@Retention(RUNTIME)
@Target({TYPE, PARAMETER})
public @interface BasicAuth {
}
```

```kotlin
import io.micronaut.http.annotation.FilterMatcher
import kotlin.annotation.AnnotationRetention.RUNTIME
import kotlin.annotation.AnnotationTarget.CLASS
import kotlin.annotation.AnnotationTarget.VALUE_PARAMETER

@FilterMatcher // (1)
@MustBeDocumented
@Retention(RUNTIME)
@Target(CLASS, VALUE_PARAMETER)
annotation class BasicAuth
```

```groovy
import io.micronaut.http.annotation.FilterMatcher

import java.lang.annotation.Documented
import java.lang.annotation.Retention
import java.lang.annotation.Target

import static java.lang.annotation.ElementType.PARAMETER
import static java.lang.annotation.ElementType.TYPE
import static java.lang.annotation.RetentionPolicy.RUNTIME

@FilterMatcher // (1)
@Documented
@Retention(RUNTIME)
@Target([TYPE, PARAMETER])
@interface BasicAuth {
}
```

| **1** | The only requirement for custom annotations is that the @FilterMatcher annotation must be present |
|---|---|


## 7.7 HTTP/2 Support

By default, Micronaut’s HTTP client is configured to support HTTP 1.1. To enable support for HTTP/2, set the supported HTTP version in configuration:

Enabling HTTP/2 in Clients

```properties
micronaut.http.client.http-version=2.0
```

```yaml
micronaut:
  http:
    client:
      http-version: 2.0
```

```toml
[micronaut]
  [micronaut.http]
    [micronaut.http.client]
      http-version=2.0
```

```groovy
micronaut {
  http {
    client {
      httpVersion = 2.0
    }
  }
}
```

```hocon
{
  micronaut {
    http {
      client {
        http-version = 2.0
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
        "http-version": 2.0
      }
    }
  }
}
```

Or by specifying the HTTP version to use when injecting the client:

Injecting an HTTP/2 Client

```java
@Inject
@Client(httpVersion=HttpVersion.HTTP_2_0)
ReactorHttpClient client;
```


## 7.8 HTTP/3 Support

Since Micronaut framework 4.x, Micronaut’s Netty-based HTTP client can be configured to support HTTP/3.

Instead of the TCP used for HTTP/1.1 and HTTP/2, HTTP/3 runs on UDP. If the client is configured with the special `h3` value for the `alpn-modes` property, the client will automatically use HTTP/3 over UDP instead of HTTP/1.1 or HTTP/2 over TCP. At this time, the client cannot fall back to TCP if the server does not support HTTP/3.

Enabling HTTP/3 in Clients

```yaml
micronaut:
  http:
    client:
      alpn-modes: [h3]
```

Additionally, the netty HTTP/3 codec needs to be present on the classpath:

`implementation("io.micronaut:micronaut-http-netty-http3")` `<dependency> <groupId>io.micronaut</groupId> <artifactId>micronaut-http-netty-http3</artifactId> </dependency>`


## 7.9 HTTP Client Sample

|   | Read the HTTP Client Guide (Java, Groovy, Kotlin), a step-by-step tutorial, to learn more. |
|---|---|


## 7.10 Connection pooling in the netty client

The netty client uses a *connection pool* to share HTTP connections between requests for greater efficiency. The pools are scoped by service (the service ID you can configure in the `@Client` annotation), and by authority (host and port), so if you configure e.g. the maximum number of connections, what is meant is the number of connections *per host*.

You can configure the pool through the `micronaut.http.client.pool.*` properties or, for specific services, via `micronaut.http.services.*.pool.*`. I’ll only mention the simple property name from here on.

HTTP/1.1 and HTTP/2.0 connections are handled and configured separately, because the latter can handle many concurrent requests on the same connection. For the purposes of pooling, HTTP/3 connections are treated as HTTP/2.0 connections.

When a request is initiated, it is added to a *pending request queue*. The maximum size of this queue is configured with `max-pending-acquires`, the default is no limit. If the limit is exceeded, the request is rejected. You can also configure an `acquire-timeout` (no timeout by default).

Once a request is in the pending request queue, it is dispatched to an existing connection. If all connections are busy but there are still pending requests, a decision is made on whether to create new connections:

- The maximum number of pending connections (i.e. connections that are still being established) may not exceed `max-pending-connections` (default: 4).
- For HTTP/1.1, the maximum number of connections may not exceed `max-concurrent-http1-connections` (no limit by default).
- For HTTP/2.0, the maximum number of connections may not exceed `max-concurrent-http2-connections` (default: 1).
- There will be at most as many pending connections as there are pending requests.

The HTTP version is determined by any existing connections in the pool. If the pool is empty, both limits apply, so by default only one connection is opened at first. For HTTP/2.0, there is also a `max-concurrent-requests-per-http2-connection` setting that controls how many requests may run on the same HTTP/2.0 connection simultaneously.

Note that a pending connection is not actually associated to a request until it is fully established. A pending request may time out, but the connection that was created for it will still enter the pool and may be used by another request.

Once a connection is in the pool, there are multiple ways it may terminate and exit the pool. During a request, the connection may see a read timeout configured by `read-timeout`. When the connection is idle (no request), a similar read timeout can be configured by `connection-pool-idle-timeout`. A fixed maximum connection lifetime may be configured using `connect-ttl`, after which the connection will wind down (no new request will be sent and the connection will terminate after all requests are done). Certain HTTP errors may also lead to a connection shutdown for safety.

# 8 Certificate providers


## Certificate providers

Certificate providers let you externalize how TLS key and trust material is supplied to the framework. Each provider is a named bean and can be referenced from server and client SSL configuration using:

- `micronaut.server.ssl.key-name` / `micronaut.server.ssl.trust-name`
- `micronaut.http.client.ssl.key-name` / `micronaut.http.client.ssl.trust-name`

Micronaut ships three provider types: - File-based: load from files on disk with optional auto-reload - Resource-based: load from Micronaut resources (classpath:, file:, string:, base64:) - Self-signed: generate ephemeral certificates (testing/dev)


## File-based provider (PEM with separate key and cert, auto-refresh)

The file provider loads a private key and certificate chain from disk and can automatically reload when files change.

```properties
micronaut.ssl.enabled=true
micronaut.server.ssl.key-name=cert-a
micronaut.server.ssl.key.password=
micronaut.http.client.ssl.trust-name=cert-a
micronaut.certificate.file.cert-a.format=pem
micronaut.certificate.file.cert-a.path=/path/to/server.key.pem
micronaut.certificate.file.cert-a.certificate-path=/path/to/server.crt.pem
```

```yaml
micronaut:
  ssl:
    enabled: true
  server:
    ssl:
      # Use the named provider "cert-a" for the server's key/cert
      key-name: cert-a
      key:
        password: ""
  http:
    client:
      ssl:
        # Trust the same material for the client
        trust-name: cert-a

  certificate:
    file:
      cert-a:
        format: pem
        path: /path/to/server.key.pem
        certificate-path: /path/to/server.crt.pem
```

```toml
[micronaut]
  [micronaut.ssl]
    enabled=true
  [micronaut.server]
    [micronaut.server.ssl]
      key-name="cert-a"
      [micronaut.server.ssl.key]
        password=""
  [micronaut.http]
    [micronaut.http.client]
      [micronaut.http.client.ssl]
        trust-name="cert-a"
  [micronaut.certificate]
    [micronaut.certificate.file]
      [micronaut.certificate.file.cert-a]
        format="pem"
        path="/path/to/server.key.pem"
        certificate-path="/path/to/server.crt.pem"
```

```groovy
micronaut {
  ssl {
    enabled = true
  }
  server {
    ssl {
      keyName = "cert-a"
      key {
        password = ""
      }
    }
  }
  http {
    client {
      ssl {
        trustName = "cert-a"
      }
    }
  }
  certificate {
    file {
      certA {
        format = "pem"
        path = "/path/to/server.key.pem"
        certificatePath = "/path/to/server.crt.pem"
      }
    }
  }
}
```

```hocon
{
  micronaut {
    ssl {
      enabled = true
    }
    server {
      ssl {
        key-name = "cert-a"
        key {
          password = ""
        }
      }
    }
    http {
      client {
        ssl {
          trust-name = "cert-a"
        }
      }
    }
    certificate {
      file {
        cert-a {
          format = "pem"
          path = "/path/to/server.key.pem"
          certificate-path = "/path/to/server.crt.pem"
        }
      }
    }
  }
}
```

```json
{
  "micronaut": {
    "ssl": {
      "enabled": true
    },
    "server": {
      "ssl": {
        "key-name": "cert-a",
        "key": {
          "password": ""
        }
      }
    },
    "http": {
      "client": {
        "ssl": {
          "trust-name": "cert-a"
        }
      }
    },
    "certificate": {
      "file": {
        "cert-a": {
          "format": "pem",
          "path": "/path/to/server.key.pem",
          "certificate-path": "/path/to/server.crt.pem"
        }
      }
    }
  }
}
```


## Resource-based provider (inline PEM and cert-only trust store)

The resource provider loads the material from any Micronaut resource location.

```properties
micronaut.ssl.enabled=true
micronaut.server.ssl.key-name=cert-a
micronaut.http.client.ssl.trust-name=trust-a
micronaut.certificate.resource.cert-a.resource=string:-----BEGIN PRIVATE KEY-----
...base64...
-----END PRIVATE KEY-----
-----BEGIN CERTIFICATE-----
...base64...
-----END CERTIFICATE-----

micronaut.certificate.resource.trust-a.resource=string:-----BEGIN CERTIFICATE-----
...base64...
-----END CERTIFICATE-----
```

```yaml
micronaut:
  ssl:
    enabled: true
  server:
    ssl:
      key-name: cert-a
  http:
    client:
      ssl:
        trust-name: trust-a
  certificate:
    resource:
      cert-a:
        resource: "string:-----BEGIN PRIVATE KEY-----\n...base64...\n-----END PRIVATE KEY-----\n-----BEGIN CERTIFICATE-----\n...base64...\n-----END CERTIFICATE-----\n"
      trust-a:
        resource: "string:-----BEGIN CERTIFICATE-----\n...base64...\n-----END CERTIFICATE-----\n"
```

```toml
[micronaut]
  [micronaut.ssl]
    enabled=true
  [micronaut.server]
    [micronaut.server.ssl]
      key-name="cert-a"
  [micronaut.http]
    [micronaut.http.client]
      [micronaut.http.client.ssl]
        trust-name="trust-a"
  [micronaut.certificate]
    [micronaut.certificate.resource]
      [micronaut.certificate.resource.cert-a]
        resource="string:-----BEGIN PRIVATE KEY-----\n...base64...\n-----END PRIVATE KEY-----\n-----BEGIN CERTIFICATE-----\n...base64...\n-----END CERTIFICATE-----\n"
      [micronaut.certificate.resource.trust-a]
        resource="string:-----BEGIN CERTIFICATE-----\n...base64...\n-----END CERTIFICATE-----\n"
```

```groovy
micronaut {
  ssl {
    enabled = true
  }
  server {
    ssl {
      keyName = "cert-a"
    }
  }
  http {
    client {
      ssl {
        trustName = "trust-a"
      }
    }
  }
  certificate {
    resource {
      certA {
        resource = "string:-----BEGIN PRIVATE KEY-----\n...base64...\n-----END PRIVATE KEY-----\n-----BEGIN CERTIFICATE-----\n...base64...\n-----END CERTIFICATE-----\n"
      }
      trustA {
        resource = "string:-----BEGIN CERTIFICATE-----\n...base64...\n-----END CERTIFICATE-----\n"
      }
    }
  }
}
```

```hocon
{
  micronaut {
    ssl {
      enabled = true
    }
    server {
      ssl {
        key-name = "cert-a"
      }
    }
    http {
      client {
        ssl {
          trust-name = "trust-a"
        }
      }
    }
    certificate {
      resource {
        cert-a {
          resource = "string:-----BEGIN PRIVATE KEY-----\n...base64...\n-----END PRIVATE KEY-----\n-----BEGIN CERTIFICATE-----\n...base64...\n-----END CERTIFICATE-----\n"
        }
        trust-a {
          resource = "string:-----BEGIN CERTIFICATE-----\n...base64...\n-----END CERTIFICATE-----\n"
        }
      }
    }
  }
}
```

```json
{
  "micronaut": {
    "ssl": {
      "enabled": true
    },
    "server": {
      "ssl": {
        "key-name": "cert-a"
      }
    },
    "http": {
      "client": {
        "ssl": {
          "trust-name": "trust-a"
        }
      }
    },
    "certificate": {
      "resource": {
        "cert-a": {
          "resource": "string:-----BEGIN PRIVATE KEY-----\n...base64...\n-----END PRIVATE KEY-----\n-----BEGIN CERTIFICATE-----\n...base64...\n-----END CERTIFICATE-----\n"
        },
        "trust-a": {
          "resource": "string:-----BEGIN CERTIFICATE-----\n...base64...\n-----END CERTIFICATE-----\n"
        }
      }
    }
  }
}
```

For JKS/PKCS12, you can embed binary content via base64:…. For example: resource: "base64:<base64-encoded .p12/.jks bytes>" and set password if required.


## Self-signed provider

The self-signed provider generates temporary certificates. It requires the netty-pkitesting dependency:

`runtimeOnly("io.netty:netty-pkitesting")` `<dependency> <groupId>io.netty</groupId> <artifactId>netty-pkitesting</artifactId> <scope>runtime</scope> </dependency>`

```properties
micronaut.ssl.enabled=true
micronaut.server.ssl.key-name=cert-server
micronaut.server.ssl.trust-name=cert-client
micronaut.server.ssl.client-authentication=need
micronaut.http.client.ssl.key-name=cert-client
micronaut.http.client.ssl.trust-name=cert-server
micronaut.certificate.self-signed.cert-client.subject=CN=foo
```

```yaml
micronaut:
  ssl:
    enabled: true
  server:
    ssl:
      key-name: cert-server
      trust-name: cert-client
      client-authentication: need
  http:
    client:
      ssl:
        key-name: cert-client
        trust-name: cert-server

  certificate:
    self-signed:
      cert-server: {}
      # Second provider with a custom subject
      cert-client:
        subject: "CN=foo"
```

```toml
[micronaut]
  [micronaut.ssl]
    enabled=true
  [micronaut.server]
    [micronaut.server.ssl]
      key-name="cert-server"
      trust-name="cert-client"
      client-authentication="need"
  [micronaut.http]
    [micronaut.http.client]
      [micronaut.http.client.ssl]
        key-name="cert-client"
        trust-name="cert-server"
  [micronaut.certificate]
    [micronaut.certificate.self-signed]
      [micronaut.certificate.self-signed.cert-server]
      [micronaut.certificate.self-signed.cert-client]
        subject="CN=foo"
```

```groovy
micronaut {
  ssl {
    enabled = true
  }
  server {
    ssl {
      keyName = "cert-server"
      trustName = "cert-client"
      clientAuthentication = "need"
    }
  }
  http {
    client {
      ssl {
        keyName = "cert-client"
        trustName = "cert-server"
      }
    }
  }
  certificate {
    selfSigned {
      certServer {
      }
      certClient {
        subject = "CN=foo"
      }
    }
  }
}
```

```hocon
{
  micronaut {
    ssl {
      enabled = true
    }
    server {
      ssl {
        key-name = "cert-server"
        trust-name = "cert-client"
        client-authentication = "need"
      }
    }
    http {
      client {
        ssl {
          key-name = "cert-client"
          trust-name = "cert-server"
        }
      }
    }
    certificate {
      self-signed {
        cert-server {
        }
        cert-client {
          subject = "CN=foo"
        }
      }
    }
  }
}
```

```json
{
  "micronaut": {
    "ssl": {
      "enabled": true
    },
    "server": {
      "ssl": {
        "key-name": "cert-server",
        "trust-name": "cert-client",
        "client-authentication": "need"
      }
    },
    "http": {
      "client": {
        "ssl": {
          "key-name": "cert-client",
          "trust-name": "cert-server"
        }
      }
    },
    "certificate": {
      "self-signed": {
        "cert-server": {
        },
        "cert-client": {
          "subject": "CN=foo"
        }
      }
    }
  }
}
```

For per-listener SSL in Netty server, you can also set `key-name` and `trust-name` under `micronaut.server.netty.listeners.<listener>.ssl`.

# 9 Context propagation

Micronaut’s Propagated Context API provides a single, consistent way to pass request scoped data across threads, reactors, and coroutines without relying directly on `ThreadLocal`.

### PropagatedContext building blocks

The central type is PropagatedContext. It is an immutable container that holds any number of PropagatedContextElement instances. Elements are lightweight descriptors of the data you want to make available downstream—for example a trace identifier, security information, or a copy of the logging MDC. Because the context is immutable you build a new instance whenever you add or remove an element:

```java
PropagatedContext base = PropagatedContext.getOrEmpty();
PropagatedContext enriched = base.plus(new TraceIdContextElement(traceId));
```

If an element needs to interact with thread-local state (for example to update the MDC) it can also implement ThreadPropagatedContextElement, which allows Micronaut to capture the previous thread-local state and restore it later. When you want to surface a JDK `ScopedValue`, implement ScopedValuePropagatedContextElement and Micronaut will automatically bind the provided `ScopedValue` and value while the context is propagated.

Example MDC element implementing

ThreadPropagatedContextElement

```java
public record MdcPropagationContext(Map<String, String> state) implements ThreadPropagatedContextElement<Map<String, String>> { (1)

    public MdcPropagationContext() {
        this(MDC.getCopyOfContextMap());
    }

    @Override
    public Map<String, String> updateThreadContext() {
        Map<String, String> oldState = MDC.getCopyOfContextMap();
        setCurrent(state); (2)
        return oldState; (3)
    }

    @Override
    public void restoreThreadContext(Map<String, String> oldState) {
        setCurrent(oldState); (4)
    }

    private void setCurrent(Map<String, String> contextMap) {
        if (contextMap == null) {
            MDC.clear();
        } else {
            MDC.setContextMap(contextMap);
        }
    }
}
```

| **1** | Accept the MDC state that should be propagated. |
|---|---|
| **2** | In `updateThreadContext` push the MDC state into the current thread. |
| **3** | Capture the previous MDC so it can be restored. |
| **4** | Restore the previous MDC state when the scope exits. |

|   | ThreadPropagatedContextElement mirrors the behaviour of Kotlin’s `kotlinx.coroutines.ThreadContextElement`, which makes it easy to integrate with coroutines. |
|---|---|

|   | ScopedValuePropagatedContextElement lets you expose existing `ScopedValue` keys so Micronaut can apply `ScopedValue.where(key, value)` for every element before executing your code. |
|---|---|

Example of chaining multiple scoped value bindings:

```java
class UserContextElement implements ScopedValuePropagatedContextElement<String> {

    static final ScopedValue<String> USER_ID = ScopedValue.newInstance();

    private final String userId;

    UserContextElement(String userId) {
        this.userId = userId;
    }

    @Override
    public ScopedValue<String> scopedValue() {
        return USER_ID;
    }

    @Override
    public String scopedValueValue() {
        return userId;
    }

    String currentUserId() {
        return USER_ID.isBound() ? USER_ID.get() : null;
    }
}
```

To bind and read the value purely with the JDK `ScopedValue` API:

```java
PropagatedContext context = PropagatedContext.getOrEmpty()
    .plus(new UserContextElement("42"));

String userId = context.propagate(() -> {
    if (UserContextElement.USER_ID.isBound()) {
        return UserContextElement.USER_ID.get();
    }
    return null;
});
```

#### Hybrid example: thread local by default, scoped value when enabled

Sometimes you need a single element that works in both propagation modes. Implementing both interfaces lets you update a `ThreadLocal` in the default mode and automatically bind a `ScopedValue` when scoped-value mode is enabled:

```java
class RequestContextElement implements ScopedValuePropagatedContextElement<String>,
        ThreadPropagatedContextElement<String> {

    private static final ScopedValue<String> REQUEST_ID = ScopedValue.newInstance();
    private static final ThreadLocal<String> THREAD_REQUEST_ID = new ThreadLocal<>();

    private final String requestId;

    RequestContextElement(String requestId) {
        this.requestId = requestId;
    }

    String currentRequestId() {
        return REQUEST_ID.isBound() ? REQUEST_ID.get() : THREAD_REQUEST_ID.get();
    }

    @Override
    public ScopedValue<String> scopedValue() {
        return REQUEST_ID;
    }

    @Override
    public String scopedValueValue() {
        return requestId;
    }

    @Override
    public @Nullable String updateThreadContext() {
        if (REQUEST_ID.isBound()) {
            return null; // scoped value already in place
        }
        String previous = THREAD_REQUEST_ID.get();
        THREAD_REQUEST_ID.set(requestId);
        return previous;
    }

    @Override
    public void restoreThreadContext(@Nullable String previous) {
        if (previous == null && REQUEST_ID.isBound()) {
            return; // we skipped thread local updates
        }
        if (previous == null) {
            THREAD_REQUEST_ID.remove();
        } else {
            THREAD_REQUEST_ID.set(previous);
        }
    }
}
```

When Micronaut runs in thread-local mode the element transparently updates the `ThreadLocal`, so `currentRequestId()` keeps working with existing integrations. If you switch to scoped-value mode, the `ScopedValue` binding happens first, `updateThreadContext()` returns `null`, and the `ThreadLocal` branch is skipped entirely.

MDC propagation example

```java
public String createUser(String name) {
    try {
        UUID newUserId = UUID.randomUUID();
        MDC.put("userId", newUserId.toString());
        return PropagatedContext.getOrEmpty()
            .plus(new MdcPropagationContext())
            .propagate(() -> createUserInternal(newUserId, name));
    } finally {
        MDC.remove("userId");
    }
}
```

|   | Since Micronaut Framework 4 the runtime no longer “captures whatever happens to be in scope.” You are responsible for obtaining the current context with `PropagatedContext.getOrEmpty()`, adding elements, and propagating the resulting instance explicitly. |
|---|---|

### Using the `propagate(…)` helpers

Once you have a context you can execute work with that context in scope by using one of the helper methods. Each helper returns the result of the lambda you pass in, and inside that lambda `PropagatedContext.get()` (or `getOrEmpty()`) gives you the propagated elements:

```java
PropagatedContext context = PropagatedContext.getOrEmpty()
    .plus(new TraceIdContextElement(traceId));

String response = context.propagate(() -> {
    // Inside the lambda the context is bound
    TraceIdContextElement element = PropagatedContext.get().get(TraceIdContextElement.class);
    return downstream.callWith(element.traceId());
}); // Supplier<T>

context.propagate(() -> {
    TraceIdContextElement element = PropagatedContext.get().get(TraceIdContextElement.class);
    logger.debug("executed with propagated state {}", element.traceId());
}); // Runnable

Integer status = context.propagateCall(() -> client.status()); // Callable<T>
```

For cases where you need to hand off work—for example to an executor—you can also pre-wrap a `Runnable`, `Callable`, or `Supplier` via `PropagatedContext.wrap(…)`.

### Default thread-local propagation with optional Scoped Values

Micronaut Framework 5 targets Java 25 by default. Since Java 21 the JDK ships **Scoped Values** (`java.lang.ScopedValue`) as a structured alternative to classic thread locals. Even though Scoped Values are available on Java 25, Micronaut keeps `thread-local` as the default propagation mode so existing integrations that require thread-local state continue to work without extra configuration.

Scoped Values still participate in virtual threads, enforce well-defined lifetimes, and prevent the accidental leaks that long-running thread pools often suffer when `ThreadLocal` is used directly. When you want those semantics, set the propagation mode to `scoped-value` explicitly.

### Avoid try-with-resources unless thread-local propagation is mandatory

The PropagatedContext interface exposes a `propagate()` method that returns an auto-closeable scope so that you can use Java’s try-with-resources syntax. The lambda helpers remain the preferred approach:

```java
PropagatedContext context = PropagatedContext.getOrEmpty().plus(new CustomElement());
context.propagate(() -> {
    // work that needs the propagated state
});
```

The try-with-resources pattern exists primarily for legacy integrations that require `ThreadLocal` propagation. Whenever you can, call one of the lambda-based `propagate(…)` helpers shown earlier instead—they work in both propagation modes. Only fall back to the scope API when the surrounding code expects a `ThreadLocal` to be present. Because the scope relies on thread-local state, invoking `propagate()` while the mode is `scoped-value` throws an `IllegalStateException` instructing you to switch back to thread-local support.

To opt into scoped-value mode globally (default: `thread-local`), set `micronaut.propagation`:

```yaml
micronaut:
  propagation: scoped-value
```

Or change it programmatically during application bootstrap:

```java
import io.micronaut.context.annotation.Context;
import io.micronaut.context.event.ContextStartedEvent;
import io.micronaut.context.event.ApplicationEventListener;
import io.micronaut.core.propagation.PropagatedContextConfiguration;

@Context
class ScopedValuePropagationListener implements ApplicationEventListener<ContextStartedEvent> {

    @Override
    public void onApplicationEvent(ContextStartedEvent event) {
        PropagatedContextConfiguration.set(PropagatedContextConfiguration.Mode.SCOPED_VALUE);
    }
}
```

Switching back to thread-local mode later is as simple as calling `PropagatedContextConfiguration.set(PropagatedContextConfiguration.Mode.THREAD_LOCAL);`.

|   | Prefer `scoped-value` when your integrations only need lambda-based propagation. Scoped Values integrate seamlessly with virtual threads, express the intent that the state only lives within a structured scope, and eliminate the risk of leaking `ThreadLocal` data between unrelated requests. |
|---|---|

### When scoped values are not sufficient

Some integrations still require `ThreadLocal` semantics because their APIs expose explicit “update” callbacks instead of accepting a lambda to execute with the context in scope. In those scenarios switch Micronaut’s propagation mode to `thread-local` before invoking the libraries involved. Common examples include:

- **Kotlin coroutines** – when wiring custom coroutine dispatchers or using `withContext`, the runtime expects Micronaut to call `MicronautPropagatedContext.updateThreadContext`. That API assumes a `ThreadLocal`, so you must run in thread-local mode whenever coroutine propagation is active. If you see `Scope propagation requires thread-local support` while running coroutine-based code, enable the thread-local mode.
- **Reactor instrumentation** – certain Micrometer/`ContextView` bridges expose callbacks that pull data from a `ThreadLocal` instead of accepting a lambda. If your reactive pipelines depend on that behaviour, configure thread-local propagation so the state is visible.

After the critical section completes you can switch the propagation mode back to `scoped-value` to regain the benefits of structured lifetimes.


## 9.1 Reactor context propagation

Since Micronaut Framework version 4, Project Reactor integration no longer captures the state automatically. Micronaut Framework users need to extend the propagation context manually.

Before version 4, Micronaut Framework required the instrumentation of every reactive operator to capture the current state to propagate it. It added an unwanted overhead and forced us to maintain complicated Reactor operators' instrumentation.

Since 3.5.0, Reactor-Core embeds support for the `io.micrometer:context-propagation` SPI. This allows to achieve the same thread-local propagation by including the Micrometer Context Propagation dependency.

The framework automatically adds the `PropagatedContext` to Project Reactor’s context for interceptors and the HTTP filters. You can access it via the utility class ReactorPropagation.

|   | ReactorPropagation is an experimental class and might change in the future. |
|---|---|

It is possible to use Micrometer Context Propagation, which Reactor supports for propagation and restoring the thread-local context.

To enable it, include the dependency:

`implementation("io.micrometer:context-propagation")` `<dependency> <groupId>io.micrometer</groupId> <artifactId>context-propagation</artifactId> </dependency>`

After that, all the thread-local propagated elements can restore their thread-local value.

|   | The thread-local values are read-only. To modify them, the `PropagatedContext` instance needs to be changed and put into the Reactor’s context. |
|---|---|

To add the context in the middle of the reactive chain, do something like the following:

```java
import io.micronaut.core.async.propagation.ReactorPropagation;
import io.micronaut.core.propagation.PropagatedContext;
import io.micronaut.core.propagation.PropagatedContextElement;
import io.micronaut.http.annotation.Controller;
import io.micronaut.http.annotation.Get;
import io.micronaut.http.annotation.QueryValue;
import reactor.core.publisher.Mono;

@Controller
class HelloController {

    @Get("/hello")
    Mono<String> hello(@QueryValue("name") String name) {
        PropagatedContext propagatedContext = PropagatedContext.get().plus(new MyContextElement(name)); // (1)
        return Mono.just("Hello, " + name)
            .contextWrite(ctx -> ReactorPropagation.addPropagatedContext(ctx, propagatedContext)); // (2)
    }
}

record MyContextElement(String value) implements PropagatedContextElement { }
```

```groovy
import io.micronaut.core.async.propagation.ReactorPropagation
import io.micronaut.core.propagation.PropagatedContext
import io.micronaut.core.propagation.PropagatedContextElement
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Get
import io.micronaut.http.annotation.QueryValue
import reactor.core.publisher.Mono

@Controller
class HelloController {

    @Get('/hello')
    Mono<String> hello(@QueryValue('name') String name) {
        PropagatedContext propagatedContext = PropagatedContext.get() + new MyContextElement(name) // (1)
        return Mono.just("Hello, $name")
                .contextWrite(ctx -> ReactorPropagation.addPropagatedContext(ctx, propagatedContext)) // (2)
    }
}

record MyContextElement(String value) implements PropagatedContextElement { }
```

| **1** | Obtain the current context that has been modified, e.g. with `PropagatedContext.get().plus(…)`, etc. |
|---|---|
| **2** | Add the context into the reactive chain. |

If you have Micrometer Context Propagation on the classpath but don’t want to use it, apply the following configuration:

Disable Micrometer Context Propagation in Reactor

```properties
reactor.enable-automatic-context-propagation=false
```

```yaml
reactor:
    enable-automatic-context-propagation: false
```

```toml
[reactor]
  enable-automatic-context-propagation=false
```

```groovy
reactor {
  enableAutomaticContextPropagation = false
}
```

```hocon
{
  reactor {
    enable-automatic-context-propagation = false
  }
}
```

```json
{
  "reactor": {
    "enable-automatic-context-propagation": false
  }
}
```
