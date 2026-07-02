---
title: "Micronaut Core (part 12/27)"
source: https://docs.micronaut.io/latest/guide/index.html
domain: micronaut
license: CC-BY-SA-4.0
tags: micronaut framework, micronaut jvm, compile-time injection, microservices framework
fetched: 2026-07-02
part: 12/27
---

## 6.13.1 Using the @Body Annotation

To parse the request body, you first indicate to the Micronaut framework which parameter receives the data with the Body annotation.

The following example implements a simple echo server that echoes the body sent in the request:

Using the @Body annotation

```java
import io.micronaut.http.HttpResponse;
import io.micronaut.http.MediaType;
import io.micronaut.http.annotation.Body;
import io.micronaut.http.annotation.Controller;
import io.micronaut.http.annotation.Post;
import jakarta.validation.constraints.Size;

@Controller("/receive")
public class MessageController {

@Post(value = "/echo", consumes = MediaType.TEXT_PLAIN) // (1)
String echo(@Size(max = 1024) @Body String text) { // (2)
    return text; // (3)
}

}
```

Using the @Body annotation

```kotlin
import io.micronaut.http.HttpResponse
import io.micronaut.http.MediaType
import io.micronaut.http.annotation.Body
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Post
import jakarta.validation.constraints.Size

@Controller("/receive")
open class MessageController {

@Post(value = "/echo", consumes = [MediaType.TEXT_PLAIN]) // (1)
open fun echo(@Size(max = 1024) @Body text: String): String { // (2)
    return text // (3)
}

}
```

Using the @Body annotation

```groovy
import io.micronaut.http.HttpResponse
import io.micronaut.http.MediaType
import io.micronaut.http.annotation.Body
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Post
import jakarta.validation.constraints.Size

@Controller("/receive")
class MessageController {

@Post(value = "/echo", consumes = MediaType.TEXT_PLAIN) // (1)
String echo(@Size(max = 1024) @Body String text) { // (2)
    text // (3)
}

}
```

| **1** | The Post annotation is used with a MediaType of `text/plain` (the default is `application/json`). |
|---|---|
| **2** | The Body annotation is used with a `jakarta.validation.constraints.Size` that limits the size of the body to at most 1KB. This constraint does **not** limit the amount of data read/buffered by the server. |
| **3** | The body is returned as the result of the method |

Note that reading the request body is done in a non-blocking manner in that the request contents are read as the data becomes available and accumulated into the String passed to the method.

|   | The `micronaut.server.maxRequestSize` setting in your configuration file (e.g. `application.yml`) limits the size of the data (the default maximum request size is 10MB) read/buffered by the server. `@Size` is **not** a replacement for this setting. |
|---|---|

Regardless of the limit, for a large amount of data accumulating the data into a String in-memory may lead to memory strain on the server. A better approach is to include a Reactive library in your project (such as `Reactor`, `RxJava`,or `Akka`) that supports the Reactive streams implementation and stream the data it becomes available:

Using Reactive Streams to Read the request body

```java
import io.micronaut.http.HttpResponse;
import io.micronaut.http.MediaType;
import io.micronaut.http.annotation.Body;
import io.micronaut.http.annotation.Controller;
import io.micronaut.http.annotation.Post;
import jakarta.validation.constraints.Size;

import org.reactivestreams.Publisher;
import reactor.core.publisher.Flux;
import io.micronaut.core.async.annotation.SingleResult;

@Controller("/receive")
public class MessageController {

@Post(value = "/echo-publisher", consumes = MediaType.TEXT_PLAIN) // (1)
@SingleResult
Publisher<HttpResponse<String>> echoFlow(@Body Publisher<String> text) { //(2)
    return Flux.from(text)
            .collect(StringBuffer::new, StringBuffer::append) // (3)
            .map(buffer -> HttpResponse.ok(buffer.toString()));
}

}
```

Using Reactive Streams to Read the request body

```kotlin
import io.micronaut.http.HttpResponse
import io.micronaut.http.MediaType
import io.micronaut.http.annotation.Body
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Post
import jakarta.validation.constraints.Size

import org.reactivestreams.Publisher
import io.micronaut.core.async.annotation.SingleResult
import reactor.core.publisher.Flux

@Controller("/receive")
open class MessageController {

@Post(value = "/echo-publisher", consumes = [MediaType.TEXT_PLAIN]) // (1)
@SingleResult
open fun echoFlow(@Body text: Publisher<String>): Publisher<HttpResponse<String>> { //(2)
    return Flux.from(text)
        .collect({ StringBuffer() }, { obj, str -> obj.append(str) }) // (3)
        .map { buffer -> HttpResponse.ok(buffer.toString()) }
}

}
```

Using Reactive Streams to Read the request body

```groovy
import io.micronaut.http.HttpResponse
import io.micronaut.http.MediaType
import io.micronaut.http.annotation.Body
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Post
import jakarta.validation.constraints.Size

import org.reactivestreams.Publisher
import io.micronaut.core.async.annotation.SingleResult
import reactor.core.publisher.Flux

@Controller("/receive")
class MessageController {

@Post(value = "/echo-publisher", consumes = MediaType.TEXT_PLAIN) // (1)
@SingleResult
Publisher<HttpResponse<String>> echoFlow(@Body Publisher<String> text) { // (2)
    return Flux.from(text)
            .collect({ x -> new StringBuffer() }, { StringBuffer sb, String s -> sb.append(s) }) // (3)
            .map({ buffer -> HttpResponse.ok(buffer.toString()) });
}

}
```

| **1** | In this case the method is altered to receive and return an `Publisher` type. |
|---|---|
| **2** | This example uses Project Reactor and returns a single item. Because of that the response type is annotated also with SingleResult. The Micronaut framework only emits the response once the operation completes without blocking. |
| **3** | The `collect` method is used to accumulate the data in this simulated example, but it could for example write the data to a logging service, database, etc. chunk by chunk |

|   | Body arguments of types that do not require conversion cause the Micronaut framework to skip decoding of the request! |
|---|---|


## 6.13.2 Reactive Responses

The previous section introduced the notion of Reactive programming using Project Reactor and Micronaut.

The Micronaut framework supports returning common reactive types such as Mono (or Single Maybe Observable types from RxJava), an instance of Publisher or CompletableFuture from any controller method.

|   | To use Project Reactor's `Flux` or `Mono` you need to add the Micronaut Reactor dependency to your project to include the necessary converters. |
|---|---|

|   | To use RxJava's `Flowable`, `Single` or `Maybe` you need to add the Micronaut RxJava dependency to your project to include the necessary converters. |
|---|---|

The argument designated as the body of the request using the Body annotation can also be a reactive type or a CompletableFuture.

When returning a reactive type, The Micronaut framework subscribes to the returned reactive type on the same thread as the request (a Netty Event Loop thread). It is therefore important that if you perform any blocking operations, you offload those operations to an appropriately configured thread pool, for example using the Project Reactor or RxJava `subscribeOn(..)` facility or @ExecuteOn.

|   | See the section on Configuring Thread Pools for information on the thread pools that the Micronaut framework sets up and how to configure them. |
|---|---|

To summarize, the following table illustrates some common response types and their handling:

| Type | Description | Example Signature |
|---|---|---|
| Publisher | Any type that implements the Publisher interface | `Publisher<String> hello()` |
| CompletableFuture | A Java `CompletableFuture` instance | `CompletableFuture<String> hello()` |
| HttpResponse | An HttpResponse and optional response body | `HttpResponse<Publisher<String>> hello()` |
| CharSequence | Any implementation of `CharSequence` | `String hello()` |
| T | Any simple POJO type | `Book show()` |

|   | When returning a Reactive type, its type affects the returned response. For example, when returning a Flux, the Micronaut framework cannot know the size of the response, so `Transfer-Encoding` type of `Chunked` is used. Whilst for types that emit a single result such as `Mono` the `Content-Length` header is populated. |
|---|---|


## 6.14 JSON Binding

The most common data interchange format nowadays is JSON.

By default, the Controller annotation specifies that the controllers in Micronaut framework consume and produce JSON by default.

Since Micronaut Framework 4.0, users must choose how they want to serialize (Jackson Databind or Micronaut Serialization). Both approaches allow the usage of Jackson Annotations.

With either approach, the Micronaut framework reads incoming JSON in a non-blocking manner.


## 6.14.1 Serialize using Micronaut Serialization

Micronaut Serialization offers reflection-free serialization using build-time Bean Introspections. It supports alternative formats such as JSON-P or JSON-B. You need to add the following dependencies:

`annotationProcessor("io.micronaut.serde:micronaut-serde-processor")` `<annotationProcessorPaths> <path> <groupId>io.micronaut.serde</groupId> <artifactId>micronaut-serde-processor</artifactId> </path> </annotationProcessorPaths>` `implementation("io.micronaut.serde:micronaut-serde-jackson")` `<dependency> <groupId>io.micronaut.serde</groupId> <artifactId>micronaut-serde-jackson</artifactId> </dependency>`


## 6.14.2 Serialization using Jackson Databind

To serialize using Jackson Databind include the following dependency:

`implementation("io.micronaut:micronaut-jackson-databind")` `<dependency> <groupId>io.micronaut</groupId> <artifactId>micronaut-jackson-databind</artifactId> </dependency>`

### Kotlin Data Classes Jackson Databind Serialization

|   | If you use Kotlin Data Classes and Jackson Databind. Your data classes will be accessed via reflection for serialization. When you use native image, you need to annotate those data classes with @ReflectiveAccess. Learn more about Micronaut GraalVM integration. |
|---|---|

```kotlin
@ReflectiveAccess
@Introspected
data class Greeting(@JsonProperty("message") val message: String)
```


## 6.14.3 JsonMapper

You may be familiar with Jackson’s `ObjectMapper`. For implementation-agnostic application code, we recommend depending on JsonMapper, which is Micronaut’s JSON abstraction for common mapping operations. Micronaut Serialization and Micronaut Jackson Databind both provide implementations of JsonMapper, and Micronaut Serialization also defines its own `ObjectMapper` interface that extends JsonMapper.

If you are intentionally writing implementation-specific code, you can still use the corresponding implementation API such as Jackson’s `ObjectMapper` or Micronaut Serialization’s `ObjectMapper`.

You can inject a bean of type `JsonMapper` or manually instantiate one via `JsonMapper.createDefault()`.


## 6.14.4 Binding using Reactive Frameworks

From a developer perspective however, you can generally just work with Plain Old Java Objects (POJOs) and can optionally use a Reactive framework such as RxJava or Project Reactor. The following is an example of a controller that reads and saves an incoming POJO in a non-blocking way from JSON:

Using Reactive Streams to Read the JSON

```java
@Controller("/people")
public class PersonController {

    Map<String, Person> inMemoryDatastore = new ConcurrentHashMap<>();

@Post("/saveReactive")
@SingleResult
public Publisher<HttpResponse<Person>> save(@Body Publisher<Person> person) { // (1)
    return Mono.from(person).map(p -> {
                inMemoryDatastore.put(p.getFirstName(), p); // (2)
                return HttpResponse.created(p); // (3)
            }
    );
}

}
```

Using Reactive Streams to Read the JSON

```kotlin
@Controller("/people")
class PersonController {

    internal var inMemoryDatastore: MutableMap<String, Person> = ConcurrentHashMap()

@Post("/saveReactive")
@SingleResult
fun save(@Body person: Publisher<Person>): Publisher<HttpResponse<Person>> { // (1)
    return Mono.from(person).map { p ->
        inMemoryDatastore[p.firstName] = p // (2)
        HttpResponse.created(p) // (3)
    }
}

}
```

Using Reactive Streams to Read the JSON

```groovy
@Controller("/people")
class PersonController {

    Map<String, Person> inMemoryDatastore = new ConcurrentHashMap<>()

@Post("/saveReactive")
@SingleResult
Publisher<HttpResponse<Person>> save(@Body Publisher<Person> person) { // (1)
    Mono.from(person).map({ p ->
        inMemoryDatastore.put(p.getFirstName(), p) // (2)
        HttpResponse.created(p) // (3)
    })
}

}
```

| **1** | The method receives a `Publisher` which emits the POJO once the JSON has been read |
|---|---|
| **2** | The `map` method stores the instance in a `Map` |
| **3** | An HttpResponse is returned |

Using cURL from the command line, you can POST JSON to the `/people` URI:

Using cURL to Post JSON

```
$ curl -X POST localhost:8080/people -d '{"firstName":"Fred","lastName":"Flintstone","age":45}'
```


## 6.14.5 Binding Using CompletableFuture

The same method as the previous example can also be written with the CompletableFuture API instead:

Using CompletableFuture to Read the JSON

```java
@Controller("/people")
public class PersonController {

    Map<String, Person> inMemoryDatastore = new ConcurrentHashMap<>();

@Post("/saveFuture")
public CompletableFuture<HttpResponse<Person>> save(@Body CompletableFuture<Person> person) {
    return person.thenApply(p -> {
                inMemoryDatastore.put(p.getFirstName(), p);
                return HttpResponse.created(p);
            }
    );
}

}
```

Using CompletableFuture to Read the JSON

```kotlin
@Controller("/people")
class PersonController {

    internal var inMemoryDatastore: MutableMap<String, Person> = ConcurrentHashMap()

@Post("/saveFuture")
fun save(@Body person: CompletableFuture<Person>): CompletableFuture<HttpResponse<Person>> {
    return person.thenApply { p ->
        inMemoryDatastore[p.firstName] = p
        HttpResponse.created(p)
    }
}

}
```

Using CompletableFuture to Read the JSON

```groovy
@Controller("/people")
class PersonController {

    Map<String, Person> inMemoryDatastore = new ConcurrentHashMap<>()

@Post("/saveFuture")
CompletableFuture<HttpResponse<Person>> save(@Body CompletableFuture<Person> person) {
    person.thenApply({ p ->
        inMemoryDatastore.put(p.getFirstName(), p)
        HttpResponse.created(p)
    })
}

}
```

The above example uses the `thenApply` method to achieve the same as the previous example.


## 6.14.6 Binding using POJOs

Note however you can just as easily write:

Binding JSON POJOs

```java
@Controller("/people")
public class PersonController {

    Map<String, Person> inMemoryDatastore = new ConcurrentHashMap<>();

@Post
public HttpResponse<Person> save(@Body Person person) {
    inMemoryDatastore.put(person.getFirstName(), person);
    return HttpResponse.created(person);
}

}
```

Binding JSON POJOs

```kotlin
@Controller("/people")
class PersonController {

    internal var inMemoryDatastore: MutableMap<String, Person> = ConcurrentHashMap()

@Post
fun save(@Body person: Person): HttpResponse<Person> {
    inMemoryDatastore[person.firstName] = person
    return HttpResponse.created(person)
}

}
```

Binding JSON POJOs

```groovy
@Controller("/people")
class PersonController {

    Map<String, Person> inMemoryDatastore = new ConcurrentHashMap<>()

@Post
HttpResponse<Person> save(@Body Person person) {
    inMemoryDatastore.put(person.getFirstName(), person)
    HttpResponse.created(person)
}

}
```

The Micronaut framework only executes your method once the data has been read in a non-blocking manner.

|   | You can customize the output in various ways, such as using Jackson annotations. |
|---|---|


## 6.14.7 Jackson Configuration

If you use `micronaut-jackson-databind`, the Jackson `ObjectMapper` can be configured through configuration with the JacksonConfiguration class. This section is specific to the Jackson implementation; for application code that should remain portable across Micronaut JSON implementations, prefer depending on JsonMapper.

All Jackson configuration keys start with `jackson`.

| dateFormat | String | The date format |
|---|---|---|
| locale | String | Uses Locale.forLanguageTag. Example: `en-US` |
| timeZone | String | Uses TimeZone.getTimeZone. Example: `PST` |
| serializationInclusion | String | One of JsonInclude.Include. Example: `ALWAYS` |
| propertyNamingStrategy | String | Name of an instance of PropertyNamingStrategy. Example: `SNAKE_CASE` |
| defaultTyping | String | The global defaultTyping for polymorphic type handling from enum ObjectMapper.DefaultTyping. Example: `NON_FINAL` |

Example:

```properties
jackson.serializationInclusion=ALWAYS
```

```yaml
jackson:
  serializationInclusion: ALWAYS
```

```toml
[jackson]
  serializationInclusion="ALWAYS"
```

```groovy
jackson {
  serializationInclusion = "ALWAYS"
}
```

```hocon
{
  jackson {
    serializationInclusion = "ALWAYS"
  }
}
```

```json
{
  "jackson": {
    "serializationInclusion": "ALWAYS"
  }
}
```


## 6.14.7.1 Features

If you use `micronaut-jackson-databind`, all Jackson’s features can be configured with their name as the key and a boolean to indicate enabled or disabled. Please check the configuration reference for the property names.

Example:

```properties
jackson.serialization-features.indentOutput=true
jackson.serialization-features.writeDatesAsTimestamps=false
jackson.deserialization-features.useBigIntegerForInts=true
jackson.deserialization-features.failOnUnknownProperties=false
```

```yaml
jackson:
  serialization-features:
    indentOutput: true
    writeDatesAsTimestamps: false
  deserialization-features:
    useBigIntegerForInts: true
    failOnUnknownProperties: false
```

```toml
[jackson]
  [jackson.serialization-features]
    indentOutput=true
    writeDatesAsTimestamps=false
  [jackson.deserialization-features]
    useBigIntegerForInts=true
    failOnUnknownProperties=false
```

```groovy
jackson {
  serializationFeatures {
    indentOutput = true
    writeDatesAsTimestamps = false
  }
  deserializationFeatures {
    useBigIntegerForInts = true
    failOnUnknownProperties = false
  }
}
```

```hocon
{
  jackson {
    serialization-features {
      indentOutput = true
      writeDatesAsTimestamps = false
    }
    deserialization-features {
      useBigIntegerForInts = true
      failOnUnknownProperties = false
    }
  }
}
```

```json
{
  "jackson": {
    "serialization-features": {
      "indentOutput": true,
      "writeDatesAsTimestamps": false
    },
    "deserialization-features": {
      "useBigIntegerForInts": true,
      "failOnUnknownProperties": false
    }
  }
}
```


## 6.14.7.2 Further customising `JsonFactory`

If you use `micronaut-jackson-databind`, there may be situations where you wish to customise the `JsonFactory` used by the `ObjectMapper` beyond the configuration of features (for example to allow custom character escaping). This can be achieved by providing your own `JsonFactory` bean, or by providing a `BeanCreatedEventListener<JsonFactory>` which configures the default bean on startup.


## 6.14.7.3 Support for `@JsonView`

If you use `micronaut-jackson-databind`, you can use the `@JsonView` annotation on controller methods if you set `jackson.json-view.enabled` to `true` in your configuration file (e.g `application.yml`).

Jackson’s `@JsonView` annotation lets you control which properties are exposed on a per-response basis. See Jackson JSON Views for more information.


## 6.14.7.4 Beans

If you use `micronaut-jackson-databind`, in addition to configuration, beans can be registered to customize Jackson. All beans that extend any of the following classes are registered with the object mapper:

- Module
- JsonDeserializer
- JsonSerializer
- KeyDeserializer
- BeanDeserializerModifier
- BeanSerializerModifier


## 6.14.7.5 Service Loader

Any modules registered via the service loader are also added to the default object mapper.


## 6.14.7.6 Number Precision

During JSON parsing, the framework may convert any incoming data to an intermediate object model. By default, this model uses `BigInteger`, `long` and `double` for numeric values. This means some information that could be represented by `BigDecimal` may be lost. For example, numbers with many decimal places that cannot be represented by `double` may be truncated, even if the target type for deserialization uses `BigDecimal`. Metadata on the number of trailing zeroes (`BigDecimal.precision()`), e.g. the difference between `0.12` and `0.120`, is also discarded.

If you need full accuracy for number types, use the following configuration:

```properties
jackson.deserialization.useBigIntegerForInts=true
jackson.deserialization.useBigDecimalForFloats=true
```

```yaml
jackson:
  deserialization:
    useBigIntegerForInts: true
    useBigDecimalForFloats: true
```

```toml
[jackson]
  [jackson.deserialization]
    useBigIntegerForInts=true
    useBigDecimalForFloats=true
```

```groovy
jackson {
  deserialization {
    useBigIntegerForInts = true
    useBigDecimalForFloats = true
  }
}
```

```hocon
{
  jackson {
    deserialization {
      useBigIntegerForInts = true
      useBigDecimalForFloats = true
    }
  }
}
```

```json
{
  "jackson": {
    "deserialization": {
      "useBigIntegerForInts": true,
      "useBigDecimalForFloats": true
    }
  }
}
```


## 6.15 Plain Text Responses

By default, a Micronaut Controller responds with content-type `application/json`. However, you can respond with content type `text/plain` by annotating the controller method with the @Produces annotation.

HTTP Response with text/plain Content-Type

```java
@Controller("/txt")
public class TextPlainController {

    @Get("/date")
    @Produces(MediaType.TEXT_PLAIN) // (1)
    String date() {
        return new Calendar.Builder().setDate(2023,7,4).build().toString(); // (2)
    }

}
```

HTTP Response with text/plain Content-Type

```groovy
@Controller('/txt')
class TextPlainController {

    @Get('/date')
    @Produces(MediaType.TEXT_PLAIN) // (1)
    String date() {
        new Calendar.Builder().setDate(2023,7,4).build().toString() // (2)
    }

}
```

| **1** | The Controller endpoint specifies a response’s Content-Type of `text/plain`. |
|---|---|
| **2** | The endpoint returns type `String`, and the implementation explicitly converts the data to a string using the `toString()` method. |

|   | Micronaut Framework 4.x `text/plain` responses are more restrictive about allowed types than Micronaut Framework 3.x. To return plain text responses for answers other than `java.lang.String`, manually call the object `toString()` method. Alternatively, set the `micronaut.http.legacy-text-conversion` configuration option to `true` to restore the old – but not recommended – Micronaut Framework 3.x behavior. |
|---|---|


## 6.16 Data Validation

It is easy to validate incoming data with Micronaut controllers using Validation Advice.

The Micronaut framework provides native support for the `jakarta.validation` annotations with the `micronaut-validation` dependency:

`annotationProcessor("io.micronaut.validation:micronaut-validation-processor")` `<annotationProcessorPaths> <path> <groupId>io.micronaut.validation</groupId> <artifactId>micronaut-validation-processor</artifactId> </path> </annotationProcessorPaths>`

`implementation("io.micronaut.validation:micronaut-validation")` `<dependency> <groupId>io.micronaut.validation</groupId> <artifactId>micronaut-validation</artifactId> </dependency>`

Or full JSR 380 compliance with the `micronaut-hibernate-validator` dependency:

`implementation("io.micronaut.beanvalidation:micronaut-hibernate-validator")` `<dependency> <groupId>io.micronaut.beanvalidation</groupId> <artifactId>micronaut-hibernate-validator</artifactId> </dependency>`

We can validate parameters using `jakarta.validation` annotations and the Validated annotation at the class level.

Example

```java
import io.micronaut.http.HttpResponse;
import io.micronaut.http.annotation.Controller;
import io.micronaut.http.annotation.Get;
import io.micronaut.validation.Validated;

import jakarta.validation.constraints.NotBlank;
import java.util.Collections;

@Validated // (1)
@Controller("/email")
public class EmailController {

    @Get("/send")
    public HttpResponse send(@NotBlank String recipient, // (2)
                             @NotBlank String subject) { // (2)
        return HttpResponse.ok(Collections.singletonMap("msg", "OK"));
    }
}
```

Example

```kotlin
import io.micronaut.http.HttpResponse
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Get
import io.micronaut.validation.Validated
import jakarta.validation.constraints.NotBlank

@Validated // (1)
@Controller("/email")
open class EmailController {

    @Get("/send")
    open fun send(@NotBlank recipient: String, // (2)
                  @NotBlank subject: String): HttpResponse<*> { // (2)
        return HttpResponse.ok(mapOf("msg" to "OK"))
    }
}
```

Example

```groovy
import io.micronaut.http.HttpResponse
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Get
import io.micronaut.validation.Validated

import jakarta.validation.constraints.NotBlank

@Validated // (1)
@Controller("/email")
class EmailController {

    @Get("/send")
    HttpResponse send(@NotBlank String recipient, // (2)
                      @NotBlank String subject) { // (2)
        HttpResponse.ok(msg: "OK")
    }
}
```

| **1** | Annotate controller with Validated |
|---|---|
| **2** | `subject` and `recipient` cannot be blank. |

If a validation error occurs a `jakarta.validation.ConstraintViolationException` is thrown. By default, the integrated `io.micronaut.validation.exception.ConstraintExceptionHandler` handles the exception, leading to a behaviour as shown in the following test:

Example Test

```java
@Test
void testParametersAreValidated() {
    HttpClientResponseException e = assertThrows(HttpClientResponseException.class, () ->
        client.toBlocking().exchange("/email/send?subject=Hi&recipient="));
    HttpResponse<?> response = e.getResponse();

    assertEquals(HttpStatus.BAD_REQUEST, response.getStatus());

    response = client.toBlocking().exchange("/email/send?subject=Hi&recipient=me@micronaut.example");

    assertEquals(HttpStatus.OK, response.getStatus());
}
```

Example Test

```kotlin
"test params are validated"() {
    val e = shouldThrow<HttpClientResponseException> {
        client.toBlocking().exchange<Any>("/email/send?subject=Hi&recipient=")
    }
    var response = e.response

    response.status shouldBe HttpStatus.BAD_REQUEST

    response = client.toBlocking().exchange<Any>("/email/send?subject=Hi&recipient=me@micronaut.example")

    response.status shouldBe HttpStatus.OK
}
```

Example Test

```groovy
def "test parameter validation"() {
    when:
    client.toBlocking().exchange('/email/send?subject=Hi&recipient=')

    then:
    def e = thrown(HttpClientResponseException)
    def response = e.response
    response.status == HttpStatus.BAD_REQUEST

    when:
    response = client.toBlocking().exchange('/email/send?subject=Hi&recipient=me@micronaut.example')

    then:
    response.status == HttpStatus.OK
}
```

To use your own `ExceptionHandler` to handle the constraint exceptions, annotate it with `@Replaces(ConstraintExceptionHandler.class)`

Often you may want to use POJOs as controller method parameters.

```java
import io.micronaut.core.annotation.Introspected;

import jakarta.validation.constraints.NotBlank;

@Introspected
public class Email {

    @NotBlank // (1)
    String subject;

    @NotBlank // (1)
    String recipient;

    public String getSubject() {
        return subject;
    }

    public void setSubject(String subject) {
        this.subject = subject;
    }

    public String getRecipient() {
        return recipient;
    }

    public void setRecipient(String recipient) {
        this.recipient = recipient;
    }
}
```

```kotlin
import io.micronaut.core.annotation.Introspected
import jakarta.validation.constraints.NotBlank

@Introspected
open class Email {

    @NotBlank // (1)
    var subject: String? = null

    @NotBlank // (1)
    var recipient: String? = null
}
```

```groovy
import io.micronaut.core.annotation.Introspected

import jakarta.validation.constraints.NotBlank

@Introspected
class Email {

    @NotBlank // (1)
    String subject

    @NotBlank // (1)
    String recipient
}
```

| **1** | You can use `jakarta.validation` annotations in your POJOs. |
|---|---|

Annotate your controller with Validated, and annotate the binding POJO with `@Valid`.

Example

```java
import io.micronaut.http.HttpResponse;
import io.micronaut.http.annotation.Body;
import io.micronaut.http.annotation.Controller;
import io.micronaut.http.annotation.Post;
import io.micronaut.validation.Validated;

import jakarta.validation.Valid;
import java.util.Collections;

@Validated // (1)
@Controller("/email")
public class EmailController {

    @Post("/send")
    public HttpResponse send(@Body @Valid Email email) { // (2)
        return HttpResponse.ok(Collections.singletonMap("msg", "OK"));
    }
}
```

Example

```kotlin
import io.micronaut.http.HttpResponse
import io.micronaut.http.annotation.Body
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Post
import io.micronaut.validation.Validated
import jakarta.validation.Valid

@Validated // (1)
@Controller("/email")
open class EmailController {

    @Post("/send")
    open fun send(@Body @Valid email: Email): HttpResponse<*> { // (2)
        return HttpResponse.ok(mapOf("msg" to "OK"))
    }
}
```

Example

```groovy
import io.micronaut.http.HttpResponse
import io.micronaut.http.annotation.Body
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Post
import io.micronaut.validation.Validated

import jakarta.validation.Valid

@Validated // (1)
@Controller("/email")
class EmailController {

    @Post("/send")
    HttpResponse send(@Body @Valid Email email) { // (2)
        HttpResponse.ok(msg: "OK")
    }
}
```

| **1** | Annotate the controller with Validated |
|---|---|
| **2** | Annotate the POJO to validate with `@Valid` |

Validation of POJOs is shown in the following test:

```java
@Test
void testPojoValidation() {
    HttpClientResponseException e = assertThrows(HttpClientResponseException.class, () -> {
        Email email = new Email();
        email.subject = "Hi";
        email.recipient = "";
        client.toBlocking().exchange(HttpRequest.POST("/email/send", email));
    });
    HttpResponse<?> response = e.getResponse();

    assertEquals(HttpStatus.BAD_REQUEST, response.getStatus());

    Email email = new Email();
    email.subject = "Hi";
    email.recipient = "me@micronaut.example";
    response = client.toBlocking().exchange(HttpRequest.POST("/email/send", email));

    assertEquals(HttpStatus.OK, response.getStatus());
}
```

```kotlin
"test pojo validation" {
    val e = shouldThrow<HttpClientResponseException> {
        val email = Email()
        email.subject = "Hi"
        email.recipient = ""
        client.toBlocking().exchange<Email, Any>(HttpRequest.POST("/email/send", email))
    }
    var response = e.response

    response.status shouldBe HttpStatus.BAD_REQUEST

    val email = Email()
    email.subject = "Hi"
    email.recipient = "me@micronaut.example"
    response = client.toBlocking().exchange<Email, Any>(HttpRequest.POST("/email/send", email))

    response.status shouldBe HttpStatus.OK
}
```

```groovy
def "invoking /email/send parse parameters in a POJO and validates"() {
    when:
    Email email = new Email(subject: 'Hi', recipient: '')
    client.toBlocking().exchange(HttpRequest.POST('/email/send', email))

    then:
    def e = thrown(HttpClientResponseException)
    def response = e.response
    response.status == HttpStatus.BAD_REQUEST

    when:
    email = new Email(subject: 'Hi', recipient: 'me@micronaut.example')
    response = client.toBlocking().exchange(HttpRequest.POST('/email/send', email))

    then:
    response.status == HttpStatus.OK
}
```

|   | Bean injection is supported in custom constraints with the Hibernate Validator configuration. |
|---|---|


## 6.16.1 Validation Groups

You can enforce a subset of constraints using validation groups using `groups` on Validated. More information is available in the Bean Validation specification

```java
import jakarta.validation.groups.Default;

public interface FinalValidation extends Default {} // (1)
```

```kotlin
import jakarta.validation.groups.Default

interface FinalValidation : Default {} // (1)
```

```groovy
import jakarta.validation.groups.Default

interface FinalValidation extends Default {} // (1)
```

| **1** | Define a custom validation group. This one extends `Default` so any validations done with this group will include constraints in the `Default` group. |
|---|---|

```java
import io.micronaut.core.annotation.Introspected;

import jakarta.validation.constraints.NotBlank;

@Introspected
public class Email {

    @NotBlank // (1)
    String subject;

    @NotBlank(groups = FinalValidation.class) // (2)
    String recipient;

    public String getSubject() {
        return subject;
    }

    public void setSubject(String subject) {
        this.subject = subject;
    }

    public String getRecipient() {
        return recipient;
    }

    public void setRecipient(String recipient) {
        this.recipient = recipient;
    }
}
```

```kotlin
import io.micronaut.core.annotation.Introspected
import jakarta.validation.constraints.NotBlank

@Introspected
open class Email {

    @NotBlank // (1)
    var subject: String? = null

    @NotBlank(groups = [FinalValidation::class]) // (2)
    var recipient: String? = null
}
```

```groovy
import io.micronaut.core.annotation.Introspected

import jakarta.validation.constraints.NotBlank

@Introspected
class Email {

    @NotBlank // (1)
    String subject

    @NotBlank(groups = FinalValidation) // (2)
    String recipient
}
```

| **1** | Specify a constraint using the Default validation group. This constraint will only be enforced when `Default` is active. |
|---|---|
| **2** | Specify a constraint using the custom `FinalValidation` validation group. This constraint will only be enforced when `FinalValidation` is active. |

Annotate your controller with Validated, specifying the validation groups that will be active or letting it default to `Default`. Also annotate the binding POJO with `@Valid`.

Example

```java
import io.micronaut.http.HttpResponse;
import io.micronaut.http.annotation.Body;
import io.micronaut.http.annotation.Controller;
import io.micronaut.http.annotation.Post;
import io.micronaut.validation.Validated;

import jakarta.validation.Valid;
import java.util.Collections;

@Validated // (1)
@Controller("/email")
public class EmailController {

    @Post("/createDraft")
    public HttpResponse createDraft(@Body @Valid Email email) { // (2)
        return HttpResponse.ok(Collections.singletonMap("msg", "OK"));
    }

    @Post("/send")
    @Validated(groups = FinalValidation.class) // (3)
    public HttpResponse send(@Body @Valid Email email) { // (4)
        return HttpResponse.ok(Collections.singletonMap("msg", "OK"));
    }
}
```

Example

```kotlin
import io.micronaut.http.HttpResponse
import io.micronaut.http.annotation.Body
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Post
import io.micronaut.validation.Validated
import jakarta.validation.Valid

@Validated // (1)
@Controller("/email")
open class EmailController {

    @Post("/createDraft")
    open fun createDraft(@Body @Valid email: Email): HttpResponse<*> { // (2)
        return HttpResponse.ok(mapOf("msg" to "OK"))
    }

    @Post("/send")
    @Validated(groups = [FinalValidation::class]) // (3)
    open fun send(@Body @Valid email: Email): HttpResponse<*> { // (4)
        return HttpResponse.ok(mapOf("msg" to "OK"))
    }
}
```

Example

```groovy
import io.micronaut.http.HttpResponse
import io.micronaut.http.annotation.Body
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Post
import io.micronaut.validation.Validated

import jakarta.validation.Valid

@Validated // (1)
@Controller("/email")
class EmailController {

    @Post("/createDraft")
    HttpResponse createDraft(@Body @Valid Email email) { // (2)
        HttpResponse.ok(msg: "OK")
    }

    @Post("/send")
    @Validated(groups = [FinalValidation]) // (3)
    HttpResponse send(@Body @Valid Email email) { // (4)
        HttpResponse.ok(msg: "OK")
    }
}
```

| **1** | Annotating with Validated without specifying groups means that the `Default` group will be active. Since this is defined on the class, it will apply to all methods. |
|---|---|
| **2** | Constraints in the `Default` validation group will be enforced, inheriting from the class. The effect is that `@NotBlank` on `email.recipient` will not be enforced when this method is called. |
| **3** | Specifying `groups` means that these validation groups will be enforced when this method is called. Note that `FinalValidation` extends `Default` so constraints from both groups will be enforced. |
| **4** | Constraints in the `Default` and `FinalValidation` validation groups will be enforced, since `FinalValidation` extends `Default`. The effect is that both `@NotBlank` constraints in `email` will be enforced when this method is called. |

Validation of POJOs using the default validation group is shown in the following test:

```java
@Test
void testPojoValidation_defaultGroup() {
    HttpClientResponseException e = assertThrows(HttpClientResponseException.class, () -> {
        Email email = new Email();
        email.subject = "";
        email.recipient = "";
        client.toBlocking().exchange(HttpRequest.POST("/email/createDraft", email));
    });
    HttpResponse<?> response = e.getResponse();

    assertEquals(HttpStatus.BAD_REQUEST, response.getStatus());

    Email email = new Email();
    email.subject = "Hi";
    email.recipient = "";
    response = client.toBlocking().exchange(HttpRequest.POST("/email/createDraft", email));

    assertEquals(HttpStatus.OK, response.getStatus());
}
```

```kotlin
"test pojo validation using default validation groups" {
    val e = shouldThrow<HttpClientResponseException> {
        val email = Email()
        email.subject = ""
        email.recipient = ""
        client.toBlocking().exchange<Email, Any>(HttpRequest.POST("/email/createDraft", email))
    }
    var response = e.response

    response.status shouldBe HttpStatus.BAD_REQUEST

    val email = Email()
    email.subject = "Hi"
    email.recipient = ""
    response = client.toBlocking().exchange<Email, Any>(HttpRequest.POST("/email/createDraft", email))

    response.status shouldBe HttpStatus.OK
}
```

```groovy
def "invoking /email/createDraft parse parameters in a POJO and validates using default validation groups"() {
    when:
    Email email = new Email(subject: '', recipient: '')
    client.toBlocking().exchange(HttpRequest.POST('/email/createDraft', email))

    then:
    def e = thrown(HttpClientResponseException)
    def response = e.response
    response.status == HttpStatus.BAD_REQUEST

    when:
    email = new Email(subject: 'Hi', recipient: '')
    response = client.toBlocking().exchange(HttpRequest.POST('/email/createDraft', email))

    then:
    response.status == HttpStatus.OK
}
```

Validation of POJOs using the custom `FinalValidation` validation group is shown in the following test:

```java
@Test
void testPojoValidation_finalValidationGroup() {
    HttpClientResponseException e = assertThrows(HttpClientResponseException.class, () -> {
        Email email = new Email();
        email.subject = "Hi";
        email.recipient = "";
        client.toBlocking().exchange(HttpRequest.POST("/email/send", email));
    });
    HttpResponse<?> response = e.getResponse();

    assertEquals(HttpStatus.BAD_REQUEST, response.getStatus());

    Email email = new Email();
    email.subject = "Hi";
    email.recipient = "me@micronaut.example";
    response = client.toBlocking().exchange(HttpRequest.POST("/email/send", email));

    assertEquals(HttpStatus.OK, response.getStatus());
}
```

```kotlin
"test pojo validation using FinalValidation validation group" {
    val e = shouldThrow<HttpClientResponseException> {
        val email = Email()
        email.subject = "Hi"
        email.recipient = ""
        client.toBlocking().exchange<Email, Any>(HttpRequest.POST("/email/send", email))
    }
    var response = e.response

    response.status shouldBe HttpStatus.BAD_REQUEST

    val email = Email()
    email.subject = "Hi"
    email.recipient = "me@micronaut.example"
    response = client.toBlocking().exchange<Email, Any>(HttpRequest.POST("/email/send", email))

    response.status shouldBe HttpStatus.OK
}
```

```groovy
def "invoking /email/send parse parameters in a POJO and validates using FinalValidation validation group"() {
    when:
    Email email = new Email(subject: 'Hi', recipient: '')
    client.toBlocking().exchange(HttpRequest.POST('/email/send', email))

    then:
    def e = thrown(HttpClientResponseException)
    def response = e.response
    response.status == HttpStatus.BAD_REQUEST

    when:
    email = new Email(subject: 'Hi', recipient: 'me@micronaut.example')
    response = client.toBlocking().exchange(HttpRequest.POST('/email/send', email))

    then:
    response.status == HttpStatus.OK
}
```


## 6.17 Serving Static Resources

Static resource resolution is enabled by default. The Micronaut framework supports resolving resources from the classpath or the file system.

See the information below for available configuration options:

🔗

| Property | Type | Description | Default value |
|---|---|---|---|
| `micronaut.router.static-resources.*.enabled` | boolean | Sets whether this specific mapping is enabled. Default value (true). |   |
| `micronaut.router.static-resources.*.mapping` | java.lang.String | The path resources should be served from. Uses ant path matching. Default value ("/**"). |   |
| `micronaut.router.static-resources.*.paths` | java.util.List | A list of paths either starting with `classpath:` or `file:`. You can serve files from anywhere on disk or the classpath. For example to serve static resources from `src/main/resources/public`, you would use `classpath:public` as the path. |   |

|   | Read the Serving static resources in a Micronaut Application guide, a step-by-step tutorial, to learn how to expose static resources such as CSS or images in a Micronaut Framework application. |
|---|---|


## 6.18 Error Handling

Sometimes with distributed applications, bad things happen. Having a good way to handle errors is important.


## 6.18.1 Status Handlers

The @Error annotation supports defining either an exception class or an HTTP status. Methods annotated with @Error must be defined within a class annotated with @Controller. The annotation also supports the notion of global and local, local being the default.

Local error handlers only respond to exceptions thrown as a result of the route being matched to another method in the same controller. Global error handlers can be invoked as a result of any thrown exception. A local error handler is always searched for first when resolving which handler to execute.

|   | When defining an error handler for an exception, you can specify the exception instance as an argument to the method and omit the exception property of the annotation. |
|---|---|

|   | See the guide for Error Handling to learn more. |
|---|---|


## 6.18.2 Local Error Handling

For example, the following method handles JSON parse exceptions from Jackson for the scope of the declaring controller:

Local exception handler

```java
@Error
public HttpResponse<JsonError> jsonError(HttpRequest request, JsonSyntaxException e) { // (1)
    JsonError error = new JsonError("Invalid JSON: " + e.getMessage()) // (2)
            .link(Link.SELF, Link.of(request.getUri()));

    return HttpResponse.<JsonError>status(HttpStatus.BAD_REQUEST, "Fix Your JSON")
            .body(error); // (3)
}
```

Local exception handler

```kotlin
@Error
fun jsonError(request: HttpRequest<*>, e: JsonSyntaxException): HttpResponse<JsonError> { // (1)
    val error = JsonError("Invalid JSON: ${e.message}") // (2)
            .link(Link.SELF, Link.of(request.uri))

    return HttpResponse.status<JsonError>(HttpStatus.BAD_REQUEST, "Fix Your JSON")
            .body(error) // (3)
}
```

Local exception handler

```groovy
@Error
HttpResponse<JsonError> jsonError(HttpRequest request, JsonSyntaxException e) { // (1)
    JsonError error = new JsonError("Invalid JSON: " + e.message) // (2)
            .link(Link.SELF, Link.of(request.uri))

    HttpResponse.<JsonError>status(HttpStatus.BAD_REQUEST, "Fix Your JSON")
            .body(error) // (3)
}
```

| **1** | A method that explicitly handles `JsonSyntaxException` is declared |
|---|---|
| **2** | An instance of JsonError is returned. |
| **3** | A custom response is returned to handle the error |

Local status handler

```java
@Error(status = HttpStatus.NOT_FOUND)
public HttpResponse<JsonError> notFound(HttpRequest request) { // (1)
    JsonError error = new JsonError("Person Not Found") // (2)
            .link(Link.SELF, Link.of(request.getUri()));

    return HttpResponse.<JsonError>notFound()
            .body(error); // (3)
}
```

Local status handler

```kotlin
@Error(status = HttpStatus.NOT_FOUND)
fun notFound(request: HttpRequest<*>): HttpResponse<JsonError> { // (1)
    val error = JsonError("Person Not Found") // (2)
            .link(Link.SELF, Link.of(request.uri))

    return HttpResponse.notFound<JsonError>()
            .body(error) // (3)
}
```

Local status handler

```groovy
@Error(status = HttpStatus.NOT_FOUND)
HttpResponse<JsonError> notFound(HttpRequest request) { // (1)
    JsonError error = new JsonError("Person Not Found") // (2)
            .link(Link.SELF, Link.of(request.uri))

    HttpResponse.<JsonError>notFound()
            .body(error) // (3)
}
```

| **1** | The Error declares which HttpStatus error code to handle (in this case 404) |
|---|---|
| **2** | A JsonError instance is returned for all 404 responses |
| **3** | An NOT_FOUND response is returned |

Similar to other controller methods, error handlers can use request binding annotations on parameters e.g. to access header values. However, binding the request body comes with additional restrictions depending on the HTTP server implementation used. If the body has already been bound to a parameter of the original controller method, it may not be possible to bind the body to a different type, as the original bytes may already have been discarded.
