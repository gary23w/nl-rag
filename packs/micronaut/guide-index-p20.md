---
title: "Micronaut Core (part 20/27)"
source: https://docs.micronaut.io/latest/guide/index.html
domain: micronaut
license: CC-BY-SA-4.0
tags: micronaut framework, micronaut jvm, compile-time injection, microservices framework
fetched: 2026-07-02
part: 20/27
---

## Query values formatting

The Format annotation can be used together with `@QueryValue` annotation to format query values.

The supported values are: `"csv"`, `"ssv"`, `"pipes"`, `"multi"` and `"deep-object"`, where the meaning is similar to Open API v3 query parameter’s `style` attribute.

The format can only be applied to `java.lang.Iterable`, `java.util.Map` or POJO with Introspected annotation. Examples of how different values will be formatted are given in the table below:

| Format | Iterable example | Map or POJO example |
|---|---|---|
| Original value | `["Mike", "Adam", "Kate"]` | `{"name": "Mike", "age": 30"}` |
| `"CSV"` | `"param=Mike,Adam,Kate"` | `"param=name,Mike,age,30"` |
| `"SSV"` | `"param=Mike Adam Kate"` | `"param=name Mike age 30"` |
| `"PIPES"` | `"param=Mike\|Adam\|Kate"` | `"param=name\|Mike\|age\|30"` |
| `"MULTI"` | `"param=Mike&param=Adam&param=Kate"` | `"name=Mike&age=30"` |
| `"DEEP_OBJECT"` | `"param[0]=Mike&param[1]=Adam&param[2]=Kate"` | `"param[name]=Mike&param[age]=30"` |

#### Type-Based Binding Parameters

Some parameters are recognized by their type instead of their annotation. The following table summarizes these parameter types and their purpose, and provides an example:

| Type | Description | Example |
|---|---|---|
| BasicAuth | Sets the `Authorization` header | `BasicAuth basicAuth` |
| HttpHeaders | Adds multiple headers to the request | `HttpHeaders headers` |
| Cookies | Adds multiple cookies to the request | `Cookies cookies` |
| Cookie | Adds a cookie to the request | `Cookie cookie` |
| Locale | Sets the `Accept-Language` header. Annotate with @QueryValue or @PathVariable to populate a URI variable. | `Locale locale` |

#### Custom Binding

The ClientArgumentRequestBinder API binds client arguments to the request. Custom binder classes registered as beans are automatically used during the binding process. Annotation-based binders are searched for first, with type-based binders being searched if a binder was not found.

##### Binding By Annotation

To control how an argument is bound to the request based on an annotation on the argument, create a bean of type AnnotatedClientArgumentRequestBinder. Any custom annotations must be annotated with @Bindable.

In this example, see the following client:

Client With @Metadata Argument

```java
@Client("/")
public interface MetadataClient {

    @Get("/client/bind")
    String get(@Metadata Map<String, Object> metadata);
}
```

Client With @Metadata Argument

```kotlin
@Client("/")
interface MetadataClient {

    @Get("/client/bind")
    operator fun get(@Metadata metadata: Map<String, Any>): String
}
```

Client With @Metadata Argument

```groovy
@Client("/")
interface MetadataClient {

    @Get("/client/bind")
    String get(@Metadata Map metadata)
}
```

The argument is annotated with the following annotation:

@Metadata Annotation

```java
import io.micronaut.core.bind.annotation.Bindable;

import java.lang.annotation.Documented;
import java.lang.annotation.Retention;
import java.lang.annotation.Target;

import static java.lang.annotation.ElementType.PARAMETER;
import static java.lang.annotation.RetentionPolicy.RUNTIME;

@Documented
@Retention(RUNTIME)
@Target(PARAMETER)
@Bindable
public @interface Metadata {
}
```

@Metadata Annotation

```kotlin
import io.micronaut.core.bind.annotation.Bindable
import kotlin.annotation.AnnotationRetention.RUNTIME
import kotlin.annotation.AnnotationTarget.VALUE_PARAMETER

@MustBeDocumented
@Retention(RUNTIME)
@Target(VALUE_PARAMETER)
@Bindable
annotation class Metadata
```

@Metadata Annotation

```groovy
import io.micronaut.core.bind.annotation.Bindable

import java.lang.annotation.Documented
import java.lang.annotation.Retention
import java.lang.annotation.Target

import static java.lang.annotation.ElementType.PARAMETER
import static java.lang.annotation.RetentionPolicy.RUNTIME

@Documented
@Retention(RUNTIME)
@Target(PARAMETER)
@Bindable
@interface Metadata {
}
```

Without any additional code, the client attempts to convert the metadata to a string and append it as a query parameter. In this case that isn’t the desired effect, so a custom binder is needed.

The following binder handles arguments passed to clients that are annotated with the `@Metadata` annotation, and mutate the request to contain the desired headers. The implementation could be modified to accept more types of data other than `Map`.

Annotation Argument Binder

```java
import org.jspecify.annotations.NonNull;
import io.micronaut.core.convert.ArgumentConversionContext;
import io.micronaut.core.naming.NameUtils;
import io.micronaut.core.util.StringUtils;
import io.micronaut.http.MutableHttpRequest;
import io.micronaut.http.client.bind.AnnotatedClientArgumentRequestBinder;
import io.micronaut.http.client.bind.ClientRequestUriContext;

import jakarta.inject.Singleton;
import java.util.Map;

@Singleton
public class MetadataClientArgumentBinder implements AnnotatedClientArgumentRequestBinder<Metadata> {

    @NonNull
    @Override
    public Class<Metadata> getAnnotationType() {
        return Metadata.class;
    }

    @Override
    public void bind(@NonNull ArgumentConversionContext<Object> context,
                     @NonNull ClientRequestUriContext uriContext,
                     @NonNull Object value,
                     @NonNull MutableHttpRequest<?> request) {
        if (value instanceof Map<?,?> map) {
            for (Map.Entry<?, ?> entry: map.entrySet()) {
                String key = NameUtils.hyphenate(StringUtils.capitalize(entry.getKey().toString()), false);
                request.header("X-Metadata-" + key, entry.getValue().toString());
            }
        }
    }
}
```

Annotation Argument Binder

```kotlin
import io.micronaut.core.convert.ArgumentConversionContext
import io.micronaut.core.naming.NameUtils
import io.micronaut.core.util.StringUtils
import io.micronaut.http.MutableHttpRequest
import io.micronaut.http.client.bind.AnnotatedClientArgumentRequestBinder
import io.micronaut.http.client.bind.ClientRequestUriContext
import jakarta.inject.Singleton

@Singleton
class MetadataClientArgumentBinder : AnnotatedClientArgumentRequestBinder<Metadata> {

    override fun getAnnotationType(): Class<Metadata> {
        return Metadata::class.java
    }

    override fun bind(context: ArgumentConversionContext<Any>,
                      uriContext: ClientRequestUriContext,
                      value: Any,
                      request: MutableHttpRequest<*>) {
        if (value is Map<*, *>) {
            for ((key1, value1) in value) {
                val key = NameUtils.hyphenate(StringUtils.capitalize(key1.toString()), false)
                request.header("X-Metadata-$key", value1.toString())
            }
        }
    }
}
```

Annotation Argument Binder

```groovy
import org.jspecify.annotations.NonNull
import io.micronaut.core.convert.ArgumentConversionContext
import io.micronaut.core.naming.NameUtils
import io.micronaut.core.util.StringUtils
import io.micronaut.http.MutableHttpRequest
import io.micronaut.http.client.bind.AnnotatedClientArgumentRequestBinder
import io.micronaut.http.client.bind.ClientRequestUriContext

import jakarta.inject.Singleton

@Singleton
class MetadataClientArgumentBinder implements AnnotatedClientArgumentRequestBinder<Metadata> {

    final Class<Metadata> annotationType = Metadata

    @Override
    void bind(@NonNull ArgumentConversionContext<Object> context,
              @NonNull ClientRequestUriContext uriContext,
              @NonNull Object value,
              @NonNull MutableHttpRequest<?> request) {
        if (value instanceof Map) {
            for (entry in value.entrySet()) {
                String key = NameUtils.hyphenate(StringUtils.capitalize(entry.key as String), false)
                request.header("X-Metadata-$key", entry.value as String)
            }
        }
    }
}
```

##### Binding By Type

To bind to the request based on the type of the argument, create a bean of type TypedClientArgumentRequestBinder.

In this example, see the following client:

Client With Metadata Argument

```java
@Client("/")
public interface MetadataClient {

    @Get("/client/bind")
    String get(Metadata metadata);
}
```

Client With Metadata Argument

```kotlin
@Client("/")
interface MetadataClient {

    @Get("/client/bind")
    operator fun get(metadata: Metadata?): String?
}
```

Client With Metadata Argument

```groovy
@Client("/")
interface MetadataClient {

    @Get("/client/bind")
    String get(Metadata metadata)
}
```

Without any additional code, the client attempts to convert the metadata to a string and append it as a query parameter. In this case that isn’t the desired effect, so a custom binder is needed.

The following binder handles arguments passed to clients of type `Metadata` and mutate the request to contain the desired headers.

Typed Argument Binder

```java
import org.jspecify.annotations.NonNull;
import io.micronaut.core.convert.ArgumentConversionContext;
import io.micronaut.core.type.Argument;
import io.micronaut.http.MutableHttpRequest;
import io.micronaut.http.client.bind.ClientRequestUriContext;
import io.micronaut.http.client.bind.TypedClientArgumentRequestBinder;

import jakarta.inject.Singleton;

@Singleton
public class MetadataClientArgumentBinder implements TypedClientArgumentRequestBinder<Metadata> {

    @Override
    @NonNull
    public Argument<Metadata> argumentType() {
        return Argument.of(Metadata.class);
    }

    @Override
    public void bind(@NonNull ArgumentConversionContext<Metadata> context,
                     @NonNull ClientRequestUriContext uriContext,
                     @NonNull Metadata value,
                     @NonNull MutableHttpRequest<?> request) {
        request.header("X-Metadata-Version", value.getVersion().toString());
        request.header("X-Metadata-Deployment-Id", value.getDeploymentId().toString());
    }
}
```

Typed Argument Binder

```kotlin
import io.micronaut.core.convert.ArgumentConversionContext
import io.micronaut.core.type.Argument
import io.micronaut.http.MutableHttpRequest
import io.micronaut.http.client.bind.ClientRequestUriContext
import io.micronaut.http.client.bind.TypedClientArgumentRequestBinder
import jakarta.inject.Singleton

@Singleton
class MetadataClientArgumentBinder : TypedClientArgumentRequestBinder<Metadata> {

    override fun argumentType(): Argument<Metadata> {
        return Argument.of(Metadata::class.java)
    }

    override fun bind(
        context: ArgumentConversionContext<Metadata>,
        uriContext: ClientRequestUriContext,
        value: Metadata,
        request: MutableHttpRequest<*>
    ) {
        request.header("X-Metadata-Version", value.version.toString())
        request.header("X-Metadata-Deployment-Id", value.deploymentId.toString())
    }
}
```

Typed Argument Binder

```groovy
import org.jspecify.annotations.NonNull
import io.micronaut.core.convert.ArgumentConversionContext
import io.micronaut.core.type.Argument
import io.micronaut.http.MutableHttpRequest
import io.micronaut.http.client.bind.ClientRequestUriContext
import io.micronaut.http.client.bind.TypedClientArgumentRequestBinder

import jakarta.inject.Singleton

@Singleton
class MetadataClientArgumentBinder implements TypedClientArgumentRequestBinder<Metadata> {

    @Override
    @NonNull
    Argument<Metadata> argumentType() {
        Argument.of(Metadata)
    }

    @Override
    void bind(@NonNull ArgumentConversionContext<Metadata> context,
              @NonNull ClientRequestUriContext uriContext,
              @NonNull Metadata value,
              @NonNull MutableHttpRequest<?> request) {
        request.header("X-Metadata-Version", value.version.toString())
        request.header("X-Metadata-Deployment-Id", value.deploymentId.toString())
    }
}
```

### Binding On Method

It is also possible to create a binder, that would change the request with an annotation on the method. For example:

Client With Annotated Method

```java
@Client("/")
public interface NameAuthorizedClient {

    @Get("/client/authorized-resource")
    @NameAuthorization(name="Bob") // (1)
    String get();
}
```

Client With Annotated Method

```kotlin
@Client("/")
public interface NameAuthorizedClient {

    @Get("/client/authorized-resource")
    @NameAuthorization(name="Bob") // (1)
    fun get(): String
}
```

Client With Annotated Method

```groovy
@Client("/")
public interface NameAuthorizedClient {

    @Get("/client/authorized-resource")
    @NameAuthorization(name="Bob") // (1)
    String get()
}
```

| **1** | The `@NameAuthorization` is annotating a method |
|---|---|

The annotation is defined as:

Annotation Definition

```java
@Documented
@Retention(RUNTIME)
@Target(METHOD) // (1)
@Bindable
public @interface NameAuthorization {
    @AliasFor(member = "name")
    String value() default "";

    @AliasFor(member = "value")
    String name() default "";
}
```

Annotation Definition

```kotlin
@MustBeDocumented
@Retention(RUNTIME)
@Target(FUNCTION) // (1)
@Bindable
annotation class NameAuthorization(val name: String = "")
```

Annotation Definition

```groovy
@Documented
@Retention(RUNTIME)
@Target(METHOD) // (1)
@Bindable
@interface NameAuthorization {
    @AliasFor(member = "name")
    String value() default ""

    @AliasFor(member = "value")
    String name() default ""
}
```

| **1** | It is defined to be used on methods |
|---|---|

The following binder specifies the behaviour:

Annotation Definition

```java
@Singleton // (1)
public class NameAuthorizationBinder implements AnnotatedClientRequestBinder<NameAuthorization> { // (2)
    @NonNull
    @Override
    public Class<NameAuthorization> getAnnotationType() {
        return NameAuthorization.class;
    }

    @Override
    public void bind( // (3)
            @NonNull MethodInvocationContext<Object, Object> context,
            @NonNull ClientRequestUriContext uriContext,
            @NonNull MutableHttpRequest<?> request
    ) {
        context.getValue(NameAuthorization.class)
                .ifPresent(name -> uriContext.addQueryParameter("name", String.valueOf(name)));

    }
}
```

Annotation Definition

```kotlin
import io.micronaut.http.client.bind.AnnotatedClientRequestBinder

@Singleton // (1)
class NameAuthorizationBinder: AnnotatedClientRequestBinder<NameAuthorization> { // (2)
    override fun getAnnotationType(): Class<NameAuthorization> {
        return NameAuthorization::class.java
    }

    override fun bind( // (3)
            context: MethodInvocationContext<Any, Any>,
            uriContext: ClientRequestUriContext,
            request: MutableHttpRequest<*>
    ) {
        context.getValue(NameAuthorization::class.java, "name")
                .ifPresent { name -> uriContext.addQueryParameter("name", name.toString()) }

    }
}
```

Annotation Definition

```groovy
@Singleton // (1)
public class NameAuthorizationBinder implements AnnotatedClientRequestBinder<NameAuthorization> { // (2)
    @NonNull
    @Override
    Class<NameAuthorization> getAnnotationType() {
        return NameAuthorization.class
    }

    @Override
    void bind( // (3)
            @NonNull MethodInvocationContext<Object, Object> context,
            @NonNull ClientRequestUriContext uriContext,
            @NonNull MutableHttpRequest<?> request
    ) {
        context.getValue(NameAuthorization.class)
                .ifPresent(name -> uriContext.addQueryParameter("name", String.valueOf(name)))

    }
}
```

| **1** | The `@Singleton` annotation registers it in Micronaut context |
|---|---|
| **2** | It implements the `AnnotatedClientRequestBinder<NameAuthorization>` |
| **3** | The custom `bind` method is used to implement the behaviour of the binder |


## 7.5.2 Streaming with @Client

The @Client annotation can also handle streaming HTTP responses.

### Streaming JSON with @Client

For example, to write a client that streams data from the controller defined in the JSON Streaming section of the documentation, you can define a client that returns an unbound Publisher such as Reactor’s Flux or a RxJava’s Flowable:

HeadlineClient.java

```java
import io.micronaut.http.annotation.Get;
import io.micronaut.http.client.annotation.Client;
import org.reactivestreams.Publisher;

import static io.micronaut.http.MediaType.APPLICATION_JSON_STREAM;

@Client("/streaming")
public interface HeadlineClient {

    @Get(value = "/headlines", processes = APPLICATION_JSON_STREAM) // (1)
    Publisher<Headline> streamHeadlines(); // (2)

}
```

HeadlineClient.java

```kotlin
import io.micronaut.http.MediaType.APPLICATION_JSON_STREAM
import io.micronaut.http.annotation.Get
import io.micronaut.http.client.annotation.Client
import reactor.core.publisher.Flux

@Client("/streaming")
interface HeadlineClient {

    @Get(value = "/headlines", processes = [APPLICATION_JSON_STREAM]) // (1)
    fun streamHeadlines(): Flux<Headline>  // (2)

}
```

HeadlineClient.java

```groovy
import io.micronaut.http.annotation.Get
import io.micronaut.http.client.annotation.Client
import org.reactivestreams.Publisher

import static io.micronaut.http.MediaType.APPLICATION_JSON_STREAM

@Client("/streaming")
interface HeadlineClient {

    @Get(value = "/headlines", processes = APPLICATION_JSON_STREAM) // (1)
    Publisher<Headline> streamHeadlines() // (2)

}
```

| **1** | The `@Get` method processes responses of type `APPLICATION_JSON_STREAM` |
|---|---|
| **2** | The return type is `Publisher` |

The following example shows how the previously defined `HeadlineClient` can be invoked from a test:

Streaming HeadlineClient

```java
@Test
void testClientAnnotationStreaming() {
    try(EmbeddedServer embeddedServer = ApplicationContext.run(EmbeddedServer.class)) {
        HeadlineClient headlineClient = embeddedServer
                                            .getApplicationContext()
                                            .getBean(HeadlineClient.class); // (1)

        Mono<Headline> firstHeadline = Mono.from(headlineClient.streamHeadlines()); // (2)

        Headline headline = firstHeadline.block(); // (3)

        assertNotNull(headline);
        assertTrue(headline.getText().startsWith("Latest Headline"));
    }
}
```

Streaming HeadlineClient

```kotlin
"test client annotation streaming" {
    val headlineClient = embeddedServer
            .applicationContext
            .getBean(HeadlineClient::class.java) // (1)

    val firstHeadline = headlineClient.streamHeadlines().next() // (2)

    val headline = firstHeadline.block() // (3)

    headline shouldNotBe null
    headline.text shouldStartWith "Latest Headline"
}
```

Streaming HeadlineClient

```groovy
void "test client annotation streaming"() throws Exception {
    when:
    def headlineClient = embeddedServer.applicationContext
            .getBean(HeadlineClient) // (1)

    Mono<Headline> firstHeadline = Mono.from(headlineClient.streamHeadlines()) // (2)

    Headline headline = firstHeadline.block() // (3)

    then:
    headline
    headline.text.startsWith("Latest Headline")
}
```

| **1** | The client is retrieved from the ApplicationContext |
|---|---|
| **2** | The `next` method emits the first element emmited by the Flux into a Mono. |
| **3** | The `block()` method retrieves the result in the test. |

### Streaming Clients and Response Types

The example defined in the previous section expects the server to respond with a stream of JSON objects, and the content type to be `application/x-json-stream`. For example:

A JSON Stream

```json
{"title":"The Stand"}
{"title":"The Shining"}
```

The reason for this is simple; a sequence of JSON object is not, in fact, valid JSON and hence the response content type cannot be `application/json`. For the JSON to be valid it would have to return an array:

A JSON Array

```json
[
    {"title":"The Stand"},
    {"title":"The Shining"}
]
```

Micronaut’s client does however support streaming of both individual JSON objects via `application/x-json-stream` and also JSON arrays defined with `application/json`.

If the server returns `application/json` and a non-single Publisher is returned (such as a Reactor’s Flux or a RxJava’s Flowable), the client streams the array elements as they become available.

### Streaming Clients and Read Timeout

When streaming responses from servers, the underlying HTTP client will not apply the default `readTimeout` setting (which defaults to 10 seconds) of the HttpClientConfiguration since the delay between reads for streaming responses may differ from normal reads.

Instead, the `read-idle-timeout` setting (which defaults to 5 minutes) dictates when to close a connection after it becomes idle.

If you stream data from a server that defines a longer delay than 5 minutes between items, you should adjust `readIdleTimeout`. The following configuration in your configuration file (e.g. `application.yml`) demonstrates how:

Adjusting the readIdleTimeout

```properties
micronaut.http.client.read-idle-timeout=10m
```

```yaml
micronaut:
  http:
    client:
      read-idle-timeout: 10m
```

```toml
[micronaut]
  [micronaut.http]
    [micronaut.http.client]
      read-idle-timeout="10m"
```

```groovy
micronaut {
  http {
    client {
      readIdleTimeout = "10m"
    }
  }
}
```

```hocon
{
  micronaut {
    http {
      client {
        read-idle-timeout = "10m"
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
        "read-idle-timeout": "10m"
      }
    }
  }
}
```

The above example sets the `readIdleTimeout` to ten minutes.

### Streaming Server Sent Events

The Micronaut framework features a native client for Server Sent Events (SSE) defined by the interface SseClient.

You can use this client to stream SSE events from any server that emits them.

|   | Although SSE streams are typically consumed by a browser `EventSource`, there are cases where you may wish to consume an SSE stream via SseClient, such as in unit tests or when a Micronaut service acts as a gateway for another service. |
|---|---|

The @Client annotation also supports consuming SSE streams. For example, consider the following controller method that produces a stream of SSE events:

SSE Controller

```java
@Get(value = "/headlines", processes = MediaType.TEXT_EVENT_STREAM) // (1)
Publisher<Event<Headline>> streamHeadlines() {
    return Flux.<Event<Headline>>create((emitter) -> {  // (2)
        Headline headline = new Headline();
        headline.setText("Latest Headline at " + ZonedDateTime.now());
        emitter.next(Event.of(headline));
        emitter.complete();
    }, FluxSink.OverflowStrategy.BUFFER)
            .repeat(100) // (3)
            .delayElements(Duration.of(1, ChronoUnit.SECONDS)); // (4)
}
```

SSE Controller

```kotlin
@Get(value = "/headlines", processes = [TEXT_EVENT_STREAM]) // (1)
internal fun streamHeadlines(): Flux<Event<Headline>> {
    return Flux.create<Event<Headline>>( { emitter -> // (2)
        val headline = Headline()
        headline.text = "Latest Headline at ${ZonedDateTime.now()}"
        emitter.next(Event.of(headline))
        emitter.complete()
    }, FluxSink.OverflowStrategy.BUFFER)
        .repeat(100) // (3)
        .delayElements(Duration.of(1, ChronoUnit.SECONDS)) // (4)
}
```

SSE Controller

```groovy
@Get(value = "/headlines", processes = MediaType.TEXT_EVENT_STREAM) // (1)
Flux<Event<Headline>> streamHeadlines() {
    Flux.<Event<Headline>>create( { emitter -> // (2)
        Headline headline = new Headline(text: "Latest Headline at ${ZonedDateTime.now()}")
        emitter.next(Event.of(headline))
        emitter.complete()
    }, FluxSink.OverflowStrategy.BUFFER)
            .repeat(100) // (3)
            .delayElements(Duration.of(1, ChronoUnit.SECONDS)) // (4)
}
```

| **1** | The controller defines a @Get annotation that produces a `MediaType.TEXT_EVENT_STREAM` |
|---|---|
| **2** | The method uses Reactor to emit a `Headline` object |
| **3** | The `repeat` method repeats the emission 100 times |
| **4** | With a delay of one second between each |

Notice that the return type of the controller is also Event and that the `Event.of` method creates events to stream to the client.

To define a client that consumes the events, define a method that processes `MediaType.TEXT_EVENT_STREAM`:

SSE Client

```java
@Client("/streaming/sse")
public interface HeadlineClient {

    @Get(value = "/headlines", processes = TEXT_EVENT_STREAM)
    Publisher<Event<Headline>> streamHeadlines();
}
```

SSE Client

```kotlin
@Client("/streaming/sse")
interface HeadlineClient {

    @Get(value = "/headlines", processes = [TEXT_EVENT_STREAM])
    fun streamHeadlines(): Flux<Event<Headline>>
}
```

SSE Client

```groovy
@Client("/streaming/sse")
interface HeadlineClient {

    @Get(value = "/headlines", processes = TEXT_EVENT_STREAM)
    Publisher<Event<Headline>> streamHeadlines()
}
```

The generic type of the `Flux` can be either an Event, in which case you will receive the full event object, or a POJO, in which case you will receive only the data contained within the event converted from JSON.


## 7.5.3 Error Responses

If an HTTP response is returned with a code of 400 or higher, an HttpClientResponseException is created. The exception contains the original response. How that exception is thrown depends on the method return type.

- For reactive response types, the exception is passed through the publisher as an error.
- For blocking response types, the exception is thrown and should be caught and handled by the caller.

|   | The one exception to this rule is HTTP Not Found (404) responses. This exception only applies to the declarative client. |
|---|---|

HTTP Not Found (404) responses for blocking return types is **not** considered an error condition and the client exception will **not** be thrown. That behavior includes methods that return `void`.

If the method returns an `HttpResponse`, the original response is returned. If the return type is `Optional`, an empty optional is returned. For all other types, `null` is returned.

When combining client calls with Retryable, all thrown exceptions will be retried by default. This will include all 4XX responses, except HTTP Not Found (404) as noted above. Specific retry criteria can be configured with a RetryPredicate to filter out responses that shouldn’t be retried.


## 7.5.4 Customizing Request Headers

Customizing the request headers deserves special mention as there are several ways that can be accomplished.


## Populating Headers Using Configuration

The @Header annotation can be declared at the type level and is repeatable such that it is possible to drive the request headers sent via configuration using annotation metadata.

The following example serves to illustrate this:

Defining Headers via Configuration

```java
@Client("/pets")
@Header(name="X-Pet-Client", value="${pet.client.id}")
public interface PetClient extends PetOperations {

    @Override
    @SingleResult
    Publisher<Pet> save(String name, int age);

    @Get("/{name}")
    @SingleResult
    Publisher<Pet> get(String name);
}
```

Defining Headers via Configuration

```kotlin
@Client("/pets")
@Header(name = "X-Pet-Client", value = "\${pet.client.id}")
interface PetClient : PetOperations {

    @SingleResult
    override fun save(name: String, age: Int): Publisher<Pet>

    @Get("/{name}")
    @SingleResult
    operator fun get(name: String): Publisher<Pet>
}
```

Defining Headers via Configuration

```groovy
@Client("/pets")
@Header(name="X-Pet-Client", value='${pet.client.id}')
interface PetClient extends PetOperations {

    @Override
    @SingleResult
    Publisher<Pet> save(@NotBlank String name, @Min(1L) int age)

    @Get("/{name}")
    @SingleResult
    Publisher<Pet> get(String name)
}
```

The above example defines a @Header annotation on the `PetClient` interface that reads the `pet.client.id` property using property placeholder configuration.

Then set the following in your configuration file (e.g. `application.yml`) to populate the value:

Configuring Headers

```properties
pet.client.id=foo
```

```yaml
pet:
  client:
    id: foo
```

```toml
[pet]
  [pet.client]
    id="foo"
```

```groovy
pet {
  client {
    id = "foo"
  }
}
```

```hocon
{
  pet {
    client {
      id = "foo"
    }
  }
}
```

```json
{
  "pet": {
    "client": {
      "id": "foo"
    }
  }
}
```

Alternatively you can supply a `PET_CLIENT_ID` environment variable and the value will be populated.


## Populating Headers using a Client Filter

Alternatively, to dynamically populate headers, another option is to use a Client Filter.

For more information on writing client filters see the Client Filters section of the guide.


## 7.5.5 Customizing Jackson Settings

As mentioned previously, Jackson is used for message encoding to JSON. A default Jackson `ObjectMapper` is configured and used by Micronaut HTTP clients.

This section covers Jackson-specific configuration. If your code should remain portable across Micronaut JSON implementations, prefer depending on JsonMapper instead of Jackson’s `ObjectMapper`.

You can override the settings used to construct the `ObjectMapper` with properties defined by the JacksonConfiguration class in your configuration file (e.g `application.yml`).

For example, the following configuration enables indented output for Jackson:

Example Jackson Configuration

```properties
jackson.serialization.indentOutput=true
```

```yaml
jackson:
  serialization:
    indentOutput: true
```

```toml
[jackson]
  [jackson.serialization]
    indentOutput=true
```

```groovy
jackson {
  serialization {
    indentOutput = true
  }
}
```

```hocon
{
  jackson {
    serialization {
      indentOutput = true
    }
  }
}
```

```json
{
  "jackson": {
    "serialization": {
      "indentOutput": true
    }
  }
}
```

However, these settings apply globally and impact both how the HTTP server renders JSON and how JSON is sent from the HTTP client. Given that, sometimes it is useful to provide client-specific Jackson settings. You can do this with the @JacksonFeatures annotation on a client:

As an example, the following snippet is taken from Micronaut’s native Eureka client (which of course uses Micronaut’s HTTP client):

Example of JacksonFeatures

```java
@Client(id = EurekaClient.SERVICE_ID,
        path = "/eureka",
        configuration = EurekaConfiguration.class)
@JacksonFeatures(
    enabledSerializationFeatures = WRAP_ROOT_VALUE,
    disabledSerializationFeatures = WRITE_SINGLE_ELEM_ARRAYS_UNWRAPPED,
    enabledDeserializationFeatures = {UNWRAP_ROOT_VALUE, ACCEPT_SINGLE_VALUE_AS_ARRAY}
)
public interface EurekaClient {
    ...
}
```

The Eureka serialization format for JSON uses the `WRAP_ROOT_VALUE` serialization feature of Jackson, hence it is enabled just for that client.

|   | If the customization offered by `JacksonFeatures` is not enough, you can also write a BeanCreatedEventListener for the `ObjectMapper` and add whatever customizations you need. |
|---|---|


## 7.5.6 Retry and Circuit Breaker

Recovering from failure is critical for HTTP clients, and that is where Micronaut’s integrated Retry Advice comes in handy.

|   | Since Micronaut Framework 4.0, declarative clients annotated with @Client no longer invoke fallbacks by default. To restore the previous behaviour add the following dependency and annotate any declarative clients with @Recoverable. |
|---|---|

`implementation("io.micronaut:micronaut-retry")` `<dependency> <groupId>io.micronaut</groupId> <artifactId>micronaut-retry</artifactId> </dependency>`

You can declare the @Retryable or @CircuitBreaker annotations on any @Client interface and the retry policy will be applied, for example:

Declaring @Retryable

```java
@Client("/pets")
@Retryable
public interface PetClient extends PetOperations {

    @Override
    @SingleResult
    Publisher<Pet> save(String name, int age);
}
```

Declaring @Retryable

```kotlin
@Client("/pets")
@Retryable
interface PetClient : PetOperations {

    override fun save(name: String, age: Int): Mono<Pet>
}
```

Declaring @Retryable

```groovy
@Client("/pets")
@Retryable
interface PetClient extends PetOperations {

    @Override
    Mono<Pet> save(String name, int age)
}
```

For more information on customizing retry, see the section on Retry Advice.


## 7.5.7 Client Fallbacks

In distributed systems, failure happens, and it is best to be prepared for it and handle it gracefully.

In addition, when developing Microservices it is quite common to work on a single Microservice without other Microservices the project requires being available.

With that in mind, the Micronaut framework features a native fallback mechanism that is integrated into Retry Advice that allows falling back to another implementation in the case of failure.

Using the @Fallback annotation, you can declare a fallback implementation of a client to be used when all possible retries have been exhausted.

In fact the mechanism is not strictly linked to Retry; you can declare any class as @Recoverable, and if a method call fails (or, in the case of reactive types, an error is emitted) a class annotated with `@Fallback` will be searched for.

To illustrate this, consider again the `PetOperations` interface declared earlier. You can define a `PetFallback` class that will be called in the case of failure:

Defining a Fallback

```java
@Fallback
public class PetFallback implements PetOperations {
    @Override
    @SingleResult
    public Publisher<Pet> save(String name, int age) {
        Pet pet = new Pet();
        pet.setAge(age);
        pet.setName(name);
        return Mono.just(pet);
    }
}
```

Defining a Fallback

```kotlin
@Fallback
open class PetFallback : PetOperations {
    override fun save(name: String, age: Int): Mono<Pet> {
        val pet = Pet()
        pet.age = age
        pet.name = name
        return Mono.just(pet)
    }
}
```

Defining a Fallback

```groovy
@Fallback
class PetFallback implements PetOperations {
    @Override
    Mono<Pet> save(String name, int age) {
        Pet pet = new Pet(age: age, name: name)
        return Mono.just(pet)
    }
}
```

|   | If you only need fallbacks to help with testing against external Microservices, you can define fallbacks in the `src/test/java` directory, so they are not included in production code. You will have to specify `@Recoverable(api = PetOperations.class)` on the declarative client if you are using fallbacks without hystrix. |
|---|---|

As you can see the fallback does not perform any network operations and is quite simple, hence will provide a successful result in the case of an external system being down.

Of course, the actual behaviour of the fallback is up to you. You can for example implement a fallback that pulls data from a local cache when real data is not available, and sends alert emails or other notifications to operations about downtime.


## 7.5.8 Netflix Hystrix Support

|   | Using the CLI If you create your project using the Micronaut CLI, supply the `netflix-hystrix` feature to configure Hystrix in your project: $ mn create-app my-app --features netflix-hystrix |
|---|---|

Netflix Hystrix is a fault tolerance library developed by the Netflix team and is designed to improve resilience of interprocess communication.

The Micronaut framework integrates with Hystrix through the `netflix-hystrix` module, which you can add to your build:

`implementation("io.micronaut.netflix:micronaut-netflix-hystrix")` `<dependency> <groupId>io.micronaut.netflix</groupId> <artifactId>micronaut-netflix-hystrix</artifactId> </dependency>`


## Using the @HystrixCommand Annotation

With the above dependency declared you can annotate any method (including methods defined on `@Client` interfaces) with the HystrixCommand annotation, and method’s execution will be wrapped in a Hystrix command. For example:

Using @HystrixCommand

```groovy
@HystrixCommand
String hello(String name) {
    return "Hello $name"
}
```

|   | This works for reactive return types such as Flux, and the reactive type will be wrapped in a `HystrixObservableCommand`. |
|---|---|

The HystrixCommand annotation also integrates with Micronaut’s support for Retry Advice and Fallbacks

|   | For information on how to customize the Hystrix thread pool, group, and properties, see the Javadoc for HystrixCommand. |
|---|---|


## Enabling Hystrix Stream and Dashboard

You can enable a Server Sent Event stream to feed into the Hystrix Dashboard by setting the `hystrix.stream.enabled` setting to `true` in your configuration file (e.g `application.yml`):

Enabling Hystrix Stream

```properties
hystrix.stream.enabled=true
```

```yaml
hystrix:
  stream:
    enabled: true
```

```toml
[hystrix]
  [hystrix.stream]
    enabled=true
```

```groovy
hystrix {
  stream {
    enabled = true
  }
}
```

```hocon
{
  hystrix {
    stream {
      enabled = true
    }
  }
}
```

```json
{
  "hystrix": {
    "stream": {
      "enabled": true
    }
  }
}
```

This exposes a `/hystrix.stream` endpoint with the format the Hystrix Dashboard expects.
