---
title: "Micronaut Core (part 13/27)"
source: https://docs.micronaut.io/latest/guide/index.html
domain: micronaut
license: CC-BY-SA-4.0
tags: micronaut framework, micronaut jvm, compile-time injection, microservices framework
fetched: 2026-07-02
part: 13/27
---

## 6.18.3 Global Error Handling

Global error handler

```java
@Error(global = true) // (1)
public HttpResponse<JsonError> error(HttpRequest request, Throwable e) {
    JsonError error = new JsonError("Bad Things Happened: " + e.getMessage()) // (2)
            .link(Link.SELF, Link.of(request.getUri()));

    return HttpResponse.<JsonError>serverError()
            .body(error); // (3)
}
```

Global error handler

```kotlin
@Error(global = true) // (1)
fun error(request: HttpRequest<*>, e: Throwable): HttpResponse<JsonError> {
    val error = JsonError("Bad Things Happened: ${e.message}") // (2)
            .link(Link.SELF, Link.of(request.uri))

    return HttpResponse.serverError<JsonError>()
            .body(error) // (3)
}
```

Global error handler

```groovy
@Error(global = true) // (1)
HttpResponse<JsonError> error(HttpRequest request, Throwable e) {
    JsonError error = new JsonError("Bad Things Happened: " + e.message) // (2)
            .link(Link.SELF, Link.of(request.uri))

    HttpResponse.<JsonError>serverError()
            .body(error) // (3)
}
```

| **1** | The @Error declares the method a global error handler |
|---|---|
| **2** | A JsonError instance is returned for all errors |
| **3** | An INTERNAL_SERVER_ERROR response is returned |

Global status handler

```java
@Error(status = HttpStatus.NOT_FOUND)
public HttpResponse<JsonError> notFound(HttpRequest request) { // (1)
    JsonError error = new JsonError("Person Not Found") // (2)
            .link(Link.SELF, Link.of(request.getUri()));

    return HttpResponse.<JsonError>notFound()
            .body(error); // (3)
}
```

Global status handler

```kotlin
@Error(status = HttpStatus.NOT_FOUND)
fun notFound(request: HttpRequest<*>): HttpResponse<JsonError> { // (1)
    val error = JsonError("Person Not Found") // (2)
            .link(Link.SELF, Link.of(request.uri))

    return HttpResponse.notFound<JsonError>()
            .body(error) // (3)
}
```

Global status handler

```groovy
@Error(status = HttpStatus.NOT_FOUND)
HttpResponse<JsonError> notFound(HttpRequest request) { // (1)
    JsonError error = new JsonError("Person Not Found") // (2)
            .link(Link.SELF, Link.of(request.uri))

    HttpResponse.<JsonError>notFound()
            .body(error) // (3)
}
```

| **1** | The @Error declares which HttpStatus error code to handle (in this case 404) |
|---|---|
| **2** | A JsonError instance is returned for all 404 responses |
| **3** | An NOT_FOUND response is returned |

|   | A few things to note about the @Error annotation. You cannot declare identical global `@Error` annotations. Identical non-global `@Error` annotations cannot be declared in the same controller. If an `@Error` annotation with the same parameter exists as global and another as local, the local one takes precedence. |
|---|---|


## 6.18.4 ExceptionHandler

Alternatively, you can implement an ExceptionHandler, a generic hook for handling exceptions that occur during execution of an HTTP request.

|   | An `@Error` annotation capturing an exception has precedence over an implementation of `ExceptionHandler` capturing the same exception. |
|---|---|


## 6.18.4.1 Built-In Exception Handlers

The Micronaut framework ships with several built-in handlers:

| Exception | Handler |
|---|---|
| `jakarta.validation.ConstraintViolationException` | ConstraintExceptionHandler |
| ContentLengthExceededException | ContentLengthExceededHandler |
| ConversionErrorException | ConversionErrorHandler |
| DuplicateRouteException | DuplicateRouteHandler |
| HttpStatusException | HttpStatusHandler |
| UnsupportedMediaException | HttpStatusHandler |
| NotFoundException | HttpStatusHandler |
| NotAcceptableException | HttpStatusHandler |
| NotAllowedException | NotAllowedExceptionHandler |
| `com.fasterxml.jackson.core.JsonProcessingException` | JsonExceptionHandler |
| `java.net.URISyntaxException` | URISyntaxHandler |
| UnsatisfiedArgumentException | UnsatisfiedArgumentHandler |
| UnsatisfiedRouteException | UnsatisfiedRouteHandler |


## 6.18.4.2 Custom Exception Handler

Imagine your e-commerce app throws an `OutOfStockException` when a book is out of stock:

```java
public class OutOfStockException extends RuntimeException {
}
```

```kotlin
class OutOfStockException : RuntimeException()
```

```groovy
class OutOfStockException extends RuntimeException {
}
```

Along with `BookController`:

```java
@Controller("/books")
public class BookController {

    @Produces(MediaType.TEXT_PLAIN)
    @Get("/stock/{isbn}")
    Integer stock(String isbn) {
        throw new OutOfStockException();
    }
}
```

```kotlin
@Controller("/books")
class BookController {

    @Produces(MediaType.TEXT_PLAIN)
    @Get("/stock/{isbn}")
    internal fun stock(isbn: String): Int? {
        throw OutOfStockException()
    }
}
```

```groovy
@Controller("/books")
class BookController {

    @Produces(MediaType.TEXT_PLAIN)
    @Get("/stock/{isbn}")
    Integer stock(String isbn) {
        throw new OutOfStockException()
    }
}
```

The server returns a 500 (Internal Server Error) status code if you don’t handle the exception.

To respond with 400 Bad Request as the response when the `OutOfStockException` is thrown, you can register a `ExceptionHandler`:

```java
@Produces
@Singleton
@Requires(classes = {OutOfStockException.class, ExceptionHandler.class})
public class OutOfStockExceptionHandler implements ExceptionHandler<OutOfStockException, HttpResponse> {

    private final ErrorResponseProcessor<?> errorResponseProcessor;

    public OutOfStockExceptionHandler(ErrorResponseProcessor<?> errorResponseProcessor) {
        this.errorResponseProcessor = errorResponseProcessor;
    }

    @Override
    public HttpResponse handle(HttpRequest request, OutOfStockException e) {
        return errorResponseProcessor.processResponse(ErrorContext.builder(request)
                .cause(e)
                .errorMessage("No stock available")
                .build(), HttpResponse.badRequest()); // (1)
    }
}
```

```kotlin
@Produces
@Singleton
@Requirements(
    Requires(classes = [OutOfStockException::class, ExceptionHandler::class])
)
class OutOfStockExceptionHandler(private val errorResponseProcessor: ErrorResponseProcessor<Any>) :
    ExceptionHandler<OutOfStockException, HttpResponse<*>> {

    override fun handle(request: HttpRequest<*>, exception: OutOfStockException): HttpResponse<*> {
        return errorResponseProcessor.processResponse(
                ErrorContext.builder(request)
                    .cause(exception)
                    .errorMessage("No stock available")
                    .build(), HttpResponse.badRequest<Any>()) // (1)
    }
}
```

```groovy
@Produces
@Singleton
@Requires(classes = [OutOfStockException, ExceptionHandler])
class OutOfStockExceptionHandler implements ExceptionHandler<OutOfStockException, HttpResponse> {

    private final ErrorResponseProcessor<?> errorResponseProcessor

    OutOfStockExceptionHandler(ErrorResponseProcessor<?> errorResponseProcessor) {
        this.errorResponseProcessor = errorResponseProcessor
    }

    @Override
    HttpResponse handle(HttpRequest request, OutOfStockException e) {
        errorResponseProcessor.processResponse(ErrorContext.builder(request)
                .cause(e)
                .errorMessage("No stock available")
                .build(), HttpResponse.badRequest()) // (1)
    }
}
```

| **1** | The default ErrorResponseProcessor is used to create the body of the response |
|---|---|


## 6.18.5 Error Formatting

The Micronaut framework produces error responses via a bean of type ErrorResponseProcessor.

JSON error responses are provided with a bean of type JsonErrorResponseBodyProvider. The default implementation outputs vnd.error responses.

HTML error responses are provided via a bean of type HtmlErrorResponseBodyProvider. The default implementation outputs HTML which can be localized with codes such as: `<status>.error.bold`, `<status>.error.title`, `<status>.error`. For example, you could localize the default 404 error page into Spanish:

```properties
404.error.bold=La página que buscabas no existe
404.error.title=No encontrado
404.error=Es posible que haya escrito mal la dirección o que la página se haya movido.
```

If customization of the response other than items related to the errors is desired, the exception handler that is handling the exception needs to be overridden.


## 6.19 API Versioning

Since 1.1.x, the Micronaut framework supports API versioning via a dedicated @Version annotation.

The following example demonstrates how to version an API:

Versioning an API

```java
import io.micronaut.core.version.annotation.Version;
import io.micronaut.http.annotation.Controller;
import io.micronaut.http.annotation.Get;

@Controller("/versioned")
class VersionedController {

    @Version("1") // (1)
    @Get("/hello")
    String helloV1() {
        return "helloV1";
    }

    @Version("2") // (2)
    @Get("/hello")
    String helloV2() {
        return "helloV2";
    }
```

Versioning an API

```kotlin
import io.micronaut.core.version.annotation.Version
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Get

@Controller("/versioned")
internal class VersionedController {

    @Version("1") // (1)
    @Get("/hello")
    fun helloV1(): String {
        return "helloV1"
    }

    @Version("2") // (2)
    @Get("/hello")
    fun helloV2(): String {
        return "helloV2"
    }
```

Versioning an API

```groovy
import io.micronaut.core.version.annotation.Version
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Get

@Controller("/versioned")
class VersionedController {

    @Version("1") // (1)
    @Get("/hello")
    String helloV1() {
        "helloV1"
    }

    @Version("2") // (2)
    @Get("/hello")
    String helloV2() {
        "helloV2"
    }
```

| **1** | The `helloV1` method is declared as version `1` |
|---|---|
| **2** | The `helloV2` method is declared as version `2` |

Then enable versioning by setting `micronaut.router.versioning.enabled` to `true` in your configuration file (e.g `application.yml`):

Enabling Versioning

```properties
micronaut.router.versioning.enabled=true
```

```yaml
micronaut:
  router:
    versioning:
      enabled: true
```

```toml
[micronaut]
  [micronaut.router]
    [micronaut.router.versioning]
      enabled=true
```

```groovy
micronaut {
  router {
    versioning {
      enabled = true
    }
  }
}
```

```hocon
{
  micronaut {
    router {
      versioning {
        enabled = true
      }
    }
  }
}
```

```json
{
  "micronaut": {
    "router": {
      "versioning": {
        "enabled": true
      }
    }
  }
}
```

By default, the Micronaut framework has two strategies for resolving the version based on an HTTP header named `X-API-VERSION` or a request parameter named `api-version`, however this is configurable. A full configuration example can be seen below:

Configuring Versioning

```properties
micronaut.router.versioning.enabled=true
micronaut.router.versioning.parameter.enabled=false
micronaut.router.versioning.parameter.names=v,api-version
micronaut.router.versioning.header.enabled=true
micronaut.router.versioning.header.names[0]=X-API-VERSION
micronaut.router.versioning.header.names[1]=Accept-Version
```

```yaml
micronaut:
  router:
    versioning:
      enabled: true
      parameter:
        enabled: false
        names: 'v,api-version'
      header:
        enabled: true
        names:
          - 'X-API-VERSION'
          - 'Accept-Version'
```

```toml
[micronaut]
  [micronaut.router]
    [micronaut.router.versioning]
      enabled=true
      [micronaut.router.versioning.parameter]
        enabled=false
        names="v,api-version"
      [micronaut.router.versioning.header]
        enabled=true
        names=[
          "X-API-VERSION",
          "Accept-Version"
        ]
```

```groovy
micronaut {
  router {
    versioning {
      enabled = true
      parameter {
        enabled = false
        names = "v,api-version"
      }
      header {
        enabled = true
        names = ["X-API-VERSION", "Accept-Version"]
      }
    }
  }
}
```

```hocon
{
  micronaut {
    router {
      versioning {
        enabled = true
        parameter {
          enabled = false
          names = "v,api-version"
        }
        header {
          enabled = true
          names = ["X-API-VERSION", "Accept-Version"]
        }
      }
    }
  }
}
```

```json
{
  "micronaut": {
    "router": {
      "versioning": {
        "enabled": true,
        "parameter": {
          "enabled": false,
          "names": "v,api-version"
        },
        "header": {
          "enabled": true,
          "names": ["X-API-VERSION", "Accept-Version"]
        }
      }
    }
  }
}
```

- This example enables versioning
- `parameter.enabled` enables or disables parameter-based versioning
- `parameter.names` specifies the parameter names as a comma-separated list
- `header.enabled` enables or disables header-based versioning
- `header.names` specifies the header names as a list

If this is not enough you can also implement the RequestVersionResolver interface which receives the HttpRequest and can implement any strategy you choose.

### Default Version

It is possible to supply a default version through configuration.

Configuring Default Version

```properties
micronaut.router.versioning.enabled=true
micronaut.router.versioning.default-version=3
```

```yaml
micronaut:
  router:
    versioning:
      enabled: true
      default-version: 3
```

```toml
[micronaut]
  [micronaut.router]
    [micronaut.router.versioning]
      enabled=true
      default-version=3
```

```groovy
micronaut {
  router {
    versioning {
      enabled = true
      defaultVersion = 3
    }
  }
}
```

```hocon
{
  micronaut {
    router {
      versioning {
        enabled = true
        default-version = 3
      }
    }
  }
}
```

```json
{
  "micronaut": {
    "router": {
      "versioning": {
        "enabled": true,
        "default-version": 3
      }
    }
  }
}
```

- This example enables versioning and sets the default version

A route is **not** matched if the following conditions are met:

- The default version is configured
- No version is found in the request
- The route defines a version
- The route version does not match the default version

If the incoming request specifies a version, the default version has no effect.

### Versioning Client Requests

Micronaut’s Declarative HTTP client also supports automatic versioning of outgoing requests via the @Version annotation.

By default, if you annotate a client interface with @Version, the value supplied to the annotation is included using the `X-API-VERSION` header.

For example:

```java
import io.micronaut.core.version.annotation.Version;
import io.micronaut.http.annotation.Get;
import io.micronaut.http.client.annotation.Client;
import org.reactivestreams.Publisher;
import io.micronaut.core.async.annotation.SingleResult;

@Client("/hello")
@Version("1") // (1)
public  interface HelloClient {

    @Get("/greeting/{name}")
    String sayHello(String name);

    @Version("2")
    @Get("/greeting/{name}")
    @SingleResult
    Publisher<String> sayHelloTwo(String name); // (2)
}
```

```kotlin
import io.micronaut.core.version.annotation.Version
import io.micronaut.http.annotation.Get
import io.micronaut.http.client.annotation.Client
import reactor.core.publisher.Mono

@Client("/hello")
@Version("1") // (1)
interface HelloClient {

    @Get("/greeting/{name}")
    fun sayHello(name : String) : String

    @Version("2")
    @Get("/greeting/{name}")
    fun sayHelloTwo(name : String) : Mono<String>  // (2)
}
```

```groovy
import io.micronaut.core.version.annotation.Version
import io.micronaut.http.annotation.Get
import io.micronaut.http.client.annotation.Client
import reactor.core.publisher.Mono

@Client("/hello")
@Version("1") // (1)
interface HelloClient {

    @Get("/greeting/{name}")
    String sayHello(String name)

    @Version("2")
    @Get("/greeting/{name}")
    Mono<String> sayHelloTwo(String name) // (2)
}
```

| **1** | The @Version annotation can be used at the type level to specify the version to use for all methods |
|---|---|
| **2** | When defined at the method level it is used only for that method |

The default behaviour for how the version is sent for each call can be configured with DefaultClientVersioningConfiguration:

🔗

| Property | Type | Description | Default value |
|---|---|---|---|
| `micronaut.http.client.versioning.default.headers` | java.util.List | The list of request header names. |   |
| `micronaut.http.client.versioning.default.parameters` | java.util.List | The list of request query parameter names. |   |

For example to use `Accept-Version` as the header name:

Configuring Client Versioning

```properties
micronaut.http.client.versioning.default.headers[0]=Accept-Version
micronaut.http.client.versioning.default.headers[1]=X-API-VERSION
```

```yaml
micronaut:
  http:
    client:
      versioning:
        default:
          headers:
            - 'Accept-Version'
            - 'X-API-VERSION'
```

```toml
[micronaut]
  [micronaut.http]
    [micronaut.http.client]
      [micronaut.http.client.versioning]
        [micronaut.http.client.versioning.default]
          headers=[
            "Accept-Version",
            "X-API-VERSION"
          ]
```

```groovy
micronaut {
  http {
    client {
      versioning {
        'default' {
          headers = ["Accept-Version", "X-API-VERSION"]
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
      client {
        versioning {
          default {
            headers = ["Accept-Version", "X-API-VERSION"]
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
      "client": {
        "versioning": {
          "default": {
            "headers": ["Accept-Version", "X-API-VERSION"]
          }
        }
      }
    }
  }
}
```

The `default` key refers to the default configuration. You can specify client-specific configuration by using the value passed to `@Client` (typically the service ID). For example:

Configuring Versioning

```properties
micronaut.http.client.versioning.greeting-service.headers[0]=Accept-Version
micronaut.http.client.versioning.greeting-service.headers[1]=X-API-VERSION
```

```yaml
micronaut:
  http:
    client:
      versioning:
        greeting-service:
          headers:
            - 'Accept-Version'
            - 'X-API-VERSION'
```

```toml
[micronaut]
  [micronaut.http]
    [micronaut.http.client]
      [micronaut.http.client.versioning]
        [micronaut.http.client.versioning.greeting-service]
          headers=[
            "Accept-Version",
            "X-API-VERSION"
          ]
```

```groovy
micronaut {
  http {
    client {
      versioning {
        greetingService {
          headers = ["Accept-Version", "X-API-VERSION"]
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
      client {
        versioning {
          greeting-service {
            headers = ["Accept-Version", "X-API-VERSION"]
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
      "client": {
        "versioning": {
          "greeting-service": {
            "headers": ["Accept-Version", "X-API-VERSION"]
          }
        }
      }
    }
  }
}
```

The above uses a key named `greeting-service` which can be used to configure a client annotated with `@Client('greeting-service')`.


## 6.20 Handling Form Data

To make data binding model customizations consistent between form data and JSON, the Micronaut framework uses Jackson to implement binding data from form submissions.

The advantage of this approach is that the same Jackson annotations used for customizing JSON binding can be used for form submissions.

|   | Form URL encoded content type and Jackson annotations are not supported by the Micronaut HTTP Client. |
|---|---|

In practice this means that to bind regular form data, the only change required to the previous JSON binding code is updating the MediaType consumed:

Binding Form Data to POJOs

```java
@Controller("/people")
class PersonController {

    Map<String, Person> inMemoryDatastore = new ConcurrentHashMap<>();

    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Post
    HttpResponse<Person> save(@Body Person person) {
        inMemoryDatastore.put(person.getFirstName(), person);
        return HttpResponse.created(person);
    }

}
```

Binding Form Data to POJOs

```groovy
@Controller("/people")
class PersonController {

    Map<String, Person> inMemoryDatastore = new ConcurrentHashMap<>()

    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Post
    HttpResponse<Person> save(@Body Person person) {
        inMemoryDatastore.put(person.getFirstName(), person)
        HttpResponse.created(person);
    }

}
```

|   | To avoid denial-of-service attacks, collection types and arrays created during binding are limited by the setting `jackson.arraySizeThreshold` in your configuration file (e.g `application.yml`) |
|---|---|

Alternatively, instead of using a POJO you can bind form data directly to method parameters (which works with JSON too!):

Binding Form Data to Parameters

```java
@Controller("/people")
class PersonController {

    Map<String, Person> inMemoryDatastore = new ConcurrentHashMap<>();

    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Post("/saveWithArgs")
    HttpResponse<Person> save(String firstName, String lastName, @Nullable Integer age) {
        Person p = new Person(firstName, lastName);
        if (age != null) {
            p.setAge(age);
        }
        inMemoryDatastore.put(p.getFirstName(), p);
        return HttpResponse.created(p);
    }

}
```

Binding Form Data to Parameters

```groovy
@Controller("/people")
class PersonController {

    Map<String, Person> inMemoryDatastore = new ConcurrentHashMap<>()

    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Post("/saveWithArgs")
    HttpResponse<Person> save(String firstName, String lastName, @Nullable Integer age) {
        Person p = new Person()
        p.firstName = firstName
        p.lastName = lastName
        if (age != null) {
            p.setAge(age)
        }
        inMemoryDatastore.put(p.firstName, p)
        return HttpResponse.created(p);
    }

}
```

As you can see from the example above, this approach lets you use features such as support for `@Nullable` or Optional types and restrict the parameters to be bound. When using POJOs you must be careful to use Jackson annotations to exclude properties that should not be bound.


## 6.21 Forms

The Micronaut HTTP server includes support for forms, both using `multipart/form-data` and using `application/x-www-form-urlencoded` format.


## 6.21.1 Detailed Form API

The lowest-level form API in the Micronaut HTTP server is the FormCapableHttpRequest. It provides a reactive Publisher of the form fields. This publisher can be subscribed to at most once. Each field is represented by a RawFormField containing the field metadata and field body as a ByteBody.

The most important information in the field metadata is the field name. This corresponds to the `name` attribute on a form `input` element.

File uploads contain additional metadata: The file name, and optionally, the file content type.

Note that there is no restriction on this metadata. Multiple fields may have the same name (browsers will do this when uploading multiple files), and any of the metadata fields may be missing entirely.

### Field Body

The field body is represented by a ByteBody, which is an asynchronous, streaming API. Large form fields may be processed lazily: As long as you do not consume the data from the `ByteBody`, the form data will not be read from the client, and e.g. an upload may stall. You will also not see any other fields on the main publisher, since they can only be received once all data for the current form field has arrived.

For short form fields, the `ByteBody` may be fully buffered internally, but you should not rely on this.


## 6.22 Writing Response Data

### Reactively Writing Response Data

Micronaut’s HTTP server supports writing chunks of response data by returning a Publisher that emits objects that can be encoded to the HTTP response.

The following table summarizes example return type signatures and the behaviour the server exhibits to handle them:

| Return Type | Description |
|---|---|
| `Publisher<String>` | A Publisher that emits each chunk of content as a String |
| `Flux<byte[]>` | A Flux that emits each chunk of content as a `byte[]` without blocking |
| `Flux<ByteBuf>` | A Reactor `Flux` that emits each chunk as a Netty `ByteBuf` |
| `Flux<Book>` | When emitting a POJO, each emitted object is encoded as JSON by default without blocking |
| `Flowable<byte[]>` | A Flux that emits each chunk of content as a `byte[]` without blocking |
| `Flowable<ByteBuf>` | A Reactor `Flux` that emits each chunk as a Netty `ByteBuf` |
| `Flowable<Book>` | When emitting a POJO, each emitted object is encoded as JSON by default without blocking |

When returning a reactive type, the server uses a `Transfer-Encoding` of `chunked` and keeps writing data until the Publisher `onComplete` method is called.

The server requests a single item from the Publisher, writes it, and requests the next, controlling back pressure.

|   | It is up to the implementation of the Publisher to schedule any blocking I/O work that may be done as a result of subscribing to the publisher. |
|---|---|

|   | To use Project Reactor's `Flux` or `Mono` you need to add the Micronaut Reactor dependency to your project to include the necessary converters. |
|---|---|

|   | To use RxJava's `Flowable`, `Single` or `Maybe` you need to add the Micronaut RxJava dependency to your project to include the necessary converters. |
|---|---|

### Performing Blocking I/O

In some cases you may wish to integrate a library that does not support non-blocking I/O.

#### Writable

In this case you can return a Writable object from any controller method. The Writable interface has various signatures that allow writing to traditional blocking streams like Writer or OutputStream.

When returning a Writable, the blocking I/O operation is shifted to the I/O thread pool so the Netty event loop is not blocked.

|   | See the section on configuring Server Thread Pools for details on how to configure the I/O thread pool to meet your application requirements. |
|---|---|

The following example demonstrates how to use this API with Groovy’s `SimpleTemplateEngine` to write a server side template:

Performing Blocking I/O With Writable

```java
import groovy.text.SimpleTemplateEngine;
import groovy.text.Template;
import io.micronaut.core.io.Writable;
import io.micronaut.core.util.CollectionUtils;
import io.micronaut.http.MediaType;
import io.micronaut.http.annotation.Controller;
import io.micronaut.http.annotation.Get;
import io.micronaut.http.server.exceptions.HttpServerException;

@Controller("/template")
public class TemplateController {

    private final SimpleTemplateEngine templateEngine = new SimpleTemplateEngine();
    private final Template template = initTemplate(); // (1)

    @Get(value = "/welcome", produces = MediaType.TEXT_PLAIN)
    Writable render() { // (2)
        return writer -> template.make( // (3)
            CollectionUtils.mapOf(
                    "firstName", "Fred",
                    "lastName", "Flintstone"
            )
        ).writeTo(writer);
    }

    private Template initTemplate() {
        try {
            return templateEngine.createTemplate(
                    "Dear $firstName $lastName. Nice to meet you."
            );
        } catch (Exception e) {
            throw new HttpServerException("Cannot create template");
        }
    }
}
```

Performing Blocking I/O With Writable

```kotlin
import groovy.text.SimpleTemplateEngine
import groovy.text.Template
import io.micronaut.core.io.Writable
import io.micronaut.http.MediaType
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Get
import io.micronaut.http.server.exceptions.HttpServerException
import java.io.Writer

@Controller("/template")
class TemplateController {

    private val templateEngine = SimpleTemplateEngine()
    private val template = initTemplate() // (1)

    @Get(value = "/welcome", produces = [MediaType.TEXT_PLAIN])
    internal fun render(): Writable { // (2)
        return { writer: Writer ->
            template.make( // (3)
                    mapOf(
                        "firstName" to "Fred",
                        "lastName" to "Flintstone"
                    )
            ).writeTo(writer)
        } as Writable
    }

    private fun initTemplate(): Template {
        return try {
            templateEngine.createTemplate(
                "Dear \$firstName \$lastName. Nice to meet you."
            )
        } catch (e: Exception) {
            throw HttpServerException("Cannot create template")
        }
    }
}
```

Performing Blocking I/O With Writable

```groovy
import groovy.text.SimpleTemplateEngine
import groovy.text.Template
import io.micronaut.core.io.Writable
import io.micronaut.http.MediaType
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Get
import io.micronaut.http.server.exceptions.HttpServerException

@Controller("/template")
class TemplateController {

    private final SimpleTemplateEngine templateEngine = new SimpleTemplateEngine()
    private final Template template = initTemplate() // (1)

    @Get(value = "/welcome", produces = MediaType.TEXT_PLAIN)
    Writable render() { // (2)
        { writer ->
            template.make( // (3)
                    firstName: "Fred",
                    lastName: "Flintstone"
            ).writeTo(writer)
        }
    }

    private Template initTemplate() {
        try {
            return templateEngine.createTemplate(
                    'Dear $firstName $lastName. Nice to meet you.'
            )
        } catch (Exception e) {
            throw new HttpServerException("Cannot create template")
        }
    }
}
```

| **1** | The controller creates a simple template |
|---|---|
| **2** | The controller method returns a Writable |
| **3** | The returned function receives a Writer and calls `writeTo` on the template. |

#### InputStream

Another option is to return an input stream. This is useful for many scenarios that interact with other APIs that expose a stream.

Performing Blocking I/O With InputStream

```java
@Get(value = "/write", produces = MediaType.TEXT_PLAIN)
InputStream write() {
    byte[] bytes = "test".getBytes(StandardCharsets.UTF_8);
    return new ByteArrayInputStream(bytes); // (1)
}
```

Performing Blocking I/O With InputStream

```kotlin
@Get(value = "/write", produces = [MediaType.TEXT_PLAIN])
fun write(): InputStream {
    val bytes = "test".toByteArray(StandardCharsets.UTF_8)
    return ByteArrayInputStream(bytes) // (1)
}
```

Performing Blocking I/O With InputStream

```groovy
@Get(value = "/write", produces = MediaType.TEXT_PLAIN)
InputStream write() {
    byte[] bytes = "test".getBytes(StandardCharsets.UTF_8);
    new ByteArrayInputStream(bytes) // (1)
}
```

| **1** | The input stream is returned and its contents will be the response body |
|---|---|

|   | The reading of the stream will be offloaded to the IO thread pool if the controller method is executed on the event loop. |
|---|---|

### 404 Responses

Often, you want to respond 404 (Not Found) when you don’t find an item in your persistence layer or in similar scenarios.

See the following example:

```java
@Controller("/books")
public class BooksController {

    @Get("/stock/{isbn}")
    public Map stock(String isbn) {
        return null; //(1)
    }

    @Get("/maybestock/{isbn}")
    @SingleResult
    public Publisher<Map> maybestock(String isbn) {
        return Mono.empty(); //(2)
    }
}
```

```kotlin
@Controller("/books")
class BooksController {

    @Get("/stock/{isbn}")
    fun stock(isbn: String): Map<*, *>? {
        return null //(1)
    }

    @Get("/maybestock/{isbn}")
    fun maybestock(isbn: String): Mono<Map<*, *>> {
        return Mono.empty() //(2)
    }
}
```

```groovy
@Controller("/books")
class BooksController {

    @Get("/stock/{isbn}")
    Map stock(String isbn) {
        null //(1)
    }

    @Get("/maybestock/{isbn}")
    Mono<Map> maybestock(String isbn) {
        Mono.empty() //(2)
    }
}
```

| **1** | Returning `null` triggers a 404 (Not Found) response. |
|---|---|
| **2** | Returning an empty `Mono` triggers a 404 (Not Found) response. |

|   | Responding with an empty `Publisher` or `Flux` is a streaming response, which results in an empty array being returned if the content type is JSON. Annotate the method with SingleResult to disable streaming. |
|---|---|

To disable 404 on a null body or an empty publisher set `micronaut.server.not-found-on-missing-body` to `false`.


## 6.23 File Uploads

Handling of file uploads has special treatment in Micronaut. Support is provided for streaming of uploads in a non-blocking manner through streaming uploads or completed uploads.

To receive data from a multipart request, set the `consumes` argument of the method annotation to MULTIPART_FORM_DATA. For example:

```java
@Post(consumes = MediaType.MULTIPART_FORM_DATA)
HttpResponse upload( ... )
```
