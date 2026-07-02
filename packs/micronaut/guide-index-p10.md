---
title: "Micronaut Core (part 10/27)"
source: https://docs.micronaut.io/latest/guide/index.html
domain: micronaut
license: CC-BY-SA-4.0
tags: micronaut framework, micronaut jvm, compile-time injection, microservices framework
fetched: 2026-07-02
part: 10/27
---

## URI Path Variables

URI variables can be referenced via method arguments. When the path variable matches the method argument name, they are bound together automatically. If you want to use different names or specify a default value for a missing URI Variable, the PathVariable annotation can be used. The following example illustrates these options:

URI Variables Example

```java
import io.micronaut.http.annotation.Controller;
import io.micronaut.http.annotation.Get;
import io.micronaut.http.annotation.PathVariable;

@Controller("/issues") // (1)
public class IssuesController {

    @Get("/{number}") // (2)
    public String issue(Integer number) { // (3)
        return "Issue # " + number + "!"; // (4)
    }

    @Get("/issue/{number}")
    public String issueFromId(@PathVariable("number") Integer id) { // (5)
        return "Issue # " + id + "!";
    }

}
```

URI Variables Example

```kotlin
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Get
import io.micronaut.http.annotation.PathVariable
```

URI Variables Example

```groovy
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Get
import io.micronaut.http.annotation.PathVariable

@Controller("/issues") // (1)
class IssuesController {

    @Get("/{number}") // (2)
    String issue(Integer number) { // (3)
        "Issue # " + number + "!" // (4)
    }

    @Get("/issue/{number}")
    String issueFromId(@PathVariable("number") Integer id) { // (5)
        "Issue # " + id + "!"
    }

}
```

| **1** | The `@Controller` annotation is specified with a base URI of `/issues` |
|---|---|
| **2** | The Get annotation maps the method to an HTTP GET with a URI variable embedded in the URI named `number` |
| **3** | The method argument `number` is bound automatically to the path variable `{number}` because the names match |
| **4** | The value of the URI variable is referenced in the implementation |
| **5** | The method argument requires the PathVariable annotation when method argument and path variable names don’t match |

The Micronaut framework maps the URI `/issues/{number}` for the above controller. We can assert this is the case by writing unit tests:

Testing URI Variables

```java
import io.micronaut.context.ApplicationContext;
import io.micronaut.http.client.HttpClient;
import io.micronaut.http.client.exceptions.HttpClientResponseException;
import io.micronaut.runtime.server.EmbeddedServer;
import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertThrows;

class IssuesControllerTest {

    private static EmbeddedServer server;
    private static HttpClient client;

    @BeforeAll // (1)
    static void setupServer() {
        server = ApplicationContext.run(EmbeddedServer.class);
        client = server
                    .getApplicationContext()
                    .createBean(HttpClient.class, server.getURL());
    }

    @AfterAll // (2)
    static void stopServer() {
        if (server != null) {
            server.stop();
        }
        if (client != null) {
            client.stop();
        }
    }

    @Test
    void testIssue() {
        String body = client.toBlocking().retrieve("/issues/12"); // (3)

        assertNotNull(body);
        assertEquals("Issue # 12!", body); // (4)
    }

    @Test
    void testIssueFromId() {
        String body = client.toBlocking().retrieve("/issues/issue/13");

        assertNotNull(body);
        assertEquals("Issue # 13!", body); // (5)
    }

    @Test
    void testShowWithInvalidInteger() {
        HttpClientResponseException e = assertThrows(HttpClientResponseException.class, () ->
                client.toBlocking().exchange("/issues/hello"));

        assertEquals(400, e.getStatus().getCode()); // (6)
    }

    @Test
    void testIssueWithoutNumber() {
        HttpClientResponseException e = assertThrows(HttpClientResponseException.class, () ->
                client.toBlocking().exchange("/issues/"));

        assertEquals(404, e.getStatus().getCode()); // (7)
    }

}
```

Testing URI Variables

```kotlin
import io.kotest.matchers.shouldBe
import io.kotest.matchers.shouldNotBe
import io.kotest.assertions.throwables.shouldThrow
import io.kotest.core.spec.style.StringSpec
import io.micronaut.context.ApplicationContext
import io.micronaut.http.client.HttpClient
import io.micronaut.http.client.exceptions.HttpClientResponseException
import io.micronaut.runtime.server.EmbeddedServer
```

Testing URI Variables

```groovy
import io.micronaut.http.client.HttpClient
import io.micronaut.http.client.exceptions.HttpClientResponseException
import io.micronaut.runtime.server.EmbeddedServer
import spock.lang.AutoCleanup
import spock.lang.Shared
import spock.lang.Specification

class IssuesControllerTest extends Specification {

    @Shared
    @AutoCleanup // (2)
    EmbeddedServer embeddedServer = ApplicationContext.run(EmbeddedServer) // (1)

    @Shared
    @AutoCleanup // (2)
    HttpClient client = HttpClient.create(embeddedServer.URL) // (1)

    void "test issue"() {
        when:
        String body = client.toBlocking().retrieve("/issues/12") // (3)

        then:
        body != null
        body == "Issue # 12!" // (4)
    }

    void "test issue from id"() {
        when:
        String body = client.toBlocking().retrieve("/issues/issue/13")

        then:
        body != null
        body == "Issue # 13!" // (5)
    }

    void "/issues/{number} with an invalid Integer number responds 400"() {
        when:
        client.toBlocking().exchange("/issues/hello")

        then:
        def e = thrown(HttpClientResponseException)
        e.status.code == 400 // (6)
    }

    void "/issues/{number} without number responds 404"() {
        when:
        client.toBlocking().exchange("/issues/")

        then:
        def e = thrown(HttpClientResponseException)
        e.status.code == 404 // (7)
    }

}
```

| **1** | The embedded server and HTTP client are started |
|---|---|
| **2** | The server and client are cleaned up after the tests finish |
| **3** | The tests send a request to the URI `/issues/12` |
| **4** | And then asserts the response is "Issue # 12" |
| **5** | Another test using the end point defined with `@PathVariable` asserts the response is "Issue # 13" |
| **6** | Another test asserts a 400 response is returned when an invalid number is sent in the URL |
| **7** | Another test asserts a 404 response is returned when no number is provided in the URL. The variable being present is required for the route to be executed. |

Note that the URI template in the previous example requires that the `number` variable is specified. You can specify optional URI templates with the syntax: `/issues{/number}` and by annotating the `number` parameter with `@Nullable`. Alternatively, you can use the `defaultValue` element of the PathVariable annotation to specify a default value when the URI variable is missing. For example:

```java
@Get("/default{/number}") // (1)
public String issueFromIdOrDefault(@PathVariable(defaultValue = "0") Integer number) { // (2)
    return "Issue # " + number + "!";
}
```

```groovy
@Get("/default{/number}") // (1)
String issueFromIdOrDefault(@PathVariable(defaultValue = "0") Integer number) { // (2)
    "Issue # " + number + "!"
}
```

| **1** | The forward slash inside the braces designates `number` as an optional URI variable |
|---|---|
| **2** | The `defaultValue` attribute specifies the default value for `number` when the URI variable is missing |

```java
@Test
void testDefaultIssue() {
    String body = client.toBlocking().retrieve("/issues/default");

    assertNotNull(body);
    assertEquals("Issue # 0!", body); // (1)
}

@Test
void testNotDefaultIssue() {
    String body = client.toBlocking().retrieve("/issues/default/1");

    assertNotNull(body);
    assertEquals("Issue # 1!", body); // (2)
}
```

```groovy
void "test default issue"() {
    when:
    String body = client.toBlocking().retrieve("/issues/default")

    then:
    body != null
    body == "Issue # 0!" // (1)
}

void "test not default issue"() {
    when:
    String body = client.toBlocking().retrieve("/issues/default/1")

    then:
    body != null
    body == "Issue # 1!" // (2)
}
```

| **1** | This test illustrates the substitution of a default `PathVariable' value when the URI variable is missing |
|---|---|
| **2** | And another test to illustrate when the optional URI variable is provided |

The following table provides examples of URI templates and what they match:

| Template | Description | Matching URI |
|---|---|---|
| `/books/{id}` | Simple match | `/books/1` |
| `/books/{id:2}` | A variable of two characters max | `/books/10` |
| `/books{/id}` | An optional URI variable | `/books/10` or `/books` |
| `/book{/id:[a-zA-Z]+}` | An optional URI variable with regex | `/books/foo` |
| `/books{?max,offset}` | Optional query parameters | `/books?max=10&offset=10` |
| `/books{/path:.*}{.ext}` | Regex path match with extension | `/books/foo/bar.xml` |


## URI Reserved Character Matching

By default, URI variables as defined by the RFC-6570 URI template spec cannot include reserved characters such as `/`, `?` etc.

This can be problematic if you wish to match or expand entire paths. As per section 3.2.3 of the specification, you can use reserved expansion or matching using the `+` operator.

For example the URI `/books/{+path}` matches both `/books/foo` and `/books/foo/bar` since the `+` indicates that the variable `path` should include reserved characters (in this case `/`).


## Routing Annotations

The previous example uses the @Get annotation to add a method that accepts HTTP GET requests. The following table summarizes the available annotations and how they map to HTTP methods:

| Annotation | HTTP Method |
|---|---|
| @Delete | DELETE |
| @Get | GET |
| @Head | HEAD |
| @Options | OPTIONS |
| @Patch | PATCH |
| @Put | PUT |
| @Post | POST |
| @Trace | TRACE |

|   | All the method annotations default to `/`. |
|---|---|


## Route Conditions

The RouteCondition annotation allows you to define a condition that must evaluate to `true` for a route to match a request. The condition is specified as a Micronaut Expression Language (EL) expression and is evaluated at request time.

Within the expression, a `request` variable is available that references the current HttpRequest.

This is useful for routing requests based on query parameters, headers, or any other aspect of the request. For example, you can use `@RouteCondition` to route requests to different methods depending on the value of a query parameter:

Route Condition Example

```java
import io.micronaut.http.annotation.Controller;
import io.micronaut.http.annotation.Get;
import io.micronaut.http.annotation.RouteCondition;

@Controller("/api")
public class RouteConditionController {

    @Get("/hello")
    @RouteCondition("#{request.parameters.getFirst('v').orElse(null) != '2'}")
    public String helloV1() {
        return "Hello v1";
    }

    @Get("/hello")
    @RouteCondition("#{request.parameters.getFirst('v').orElse(null) == '2'}") // (1)
    public String helloV2() {
        return "Hello v2";
    }
}
```

Route Condition Example

```kotlin
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Get
import io.micronaut.http.annotation.RouteCondition

@Controller("/api")
class RouteConditionController {

    @Get("/hello")
    @RouteCondition("#{request.parameters.getFirst('v').orElse(null) != '2'}")
    fun helloV1(): String {
        return "Hello v1"
    }

    @Get("/hello")
    @RouteCondition("#{request.parameters.getFirst('v').orElse(null) == '2'}") // (1)
    fun helloV2(): String {
        return "Hello v2"
    }
}
```

Route Condition Example

```groovy
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Get
import io.micronaut.http.annotation.RouteCondition

@Controller("/api")
class RouteConditionController {

    @Get("/hello")
    @RouteCondition("#{request.parameters.getFirst('v').orElse(null) != '2'}")
    String helloV1() {
        "Hello v1"
    }

    @Get("/hello")
    @RouteCondition("#{request.parameters.getFirst('v').orElse(null) == '2'}") // (1)
    String helloV2() {
        "Hello v2"
    }
}
```

| **1** | The route condition expression evaluates whether the `v` query parameter equals `2`. If it does, the request is routed to `helloV2()`. If not, the route is not matched and the request falls through to `helloV1()`. |
|---|---|

|   | The RouteCondition annotation only applies to server-side routes and is ignored when placed on declarative HTTP client routes. |
|---|---|

|   | The `request` variable in the expression is an instance of HttpRequest. You can access headers via `request.headers`, query parameters via `request.parameters`, and other request attributes as needed. |
|---|---|


## @Options

CORS support handles OPTIONS preflight requests. However, if you want to dispatch OPTIONS requests without an Origin HTTP Header, you can enable it via:

```properties
micronaut.server.dispatch-options-requests=true
```

```yaml
micronaut:
  server:
    dispatch-options-requests: true
```

```toml
[micronaut]
  [micronaut.server]
    dispatch-options-requests=true
```

```groovy
micronaut {
  server {
    dispatchOptionsRequests = true
  }
}
```

```hocon
{
  micronaut {
    server {
      dispatch-options-requests = true
    }
  }
}
```

```json
{
  "micronaut": {
    "server": {
      "dispatch-options-requests": true
    }
  }
}
```


## Multiple URIs

Each of the routing annotations supports multiple URI templates. For each template, a route is created. This feature is useful for example to change the path of the API and leave the existing path as is for backwards compatibility. For example:

Multiple URIs

```java
import io.micronaut.http.annotation.Controller;
import io.micronaut.http.annotation.Get;

@Controller("/hello")
public class BackwardCompatibleController {

    @Get(uris = {"/{name}", "/person/{name}"}) // (1)
    public String hello(String name) { // (2)
        return "Hello, " + name;
    }
}
```

Multiple URIs

```kotlin
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Get

@Controller("/hello")
class BackwardCompatibleController {

    @Get(uris = ["/{name}", "/person/{name}"]) // (1)
    fun hello(name: String): String { // (2)
        return "Hello, $name"
    }
}
```

Multiple URIs

```groovy
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Get

@Controller("/hello")
class BackwardCompatibleController {

    @Get(uris = ["/{name}", "/person/{name}"]) // (1)
    String hello(String name) { // (2)
        "Hello, $name"
    }
}
```

| **1** | Specify multiple templates |
|---|---|
| **2** | Bind to the template arguments as normal |

|   | Route validation is more complicated with multiple templates. If a variable that would normally be required does not exist in all templates, that variable is considered optional since it may not exist for every execution of the method. |
|---|---|


## Building Routes Programmatically

If you prefer to not use annotations and instead declare all routes in code then never fear, the Micronaut framework has a flexible RouteBuilder API that makes it a breeze to define routes programmatically.

To start, subclass DefaultRouteBuilder and inject the controller to route to into the method, and define your routes:

URI Variables Example

```java
import io.micronaut.context.ExecutionHandleLocator;
import io.micronaut.web.router.DefaultRouteBuilder;

import jakarta.inject.Inject;
import jakarta.inject.Singleton;

@Singleton
public class MyRoutes extends DefaultRouteBuilder { // (1)

    public MyRoutes(ExecutionHandleLocator executionHandleLocator,
                    UriNamingStrategy uriNamingStrategy) {
        super(executionHandleLocator, uriNamingStrategy);
    }

    @Inject
    void issuesRoutes(IssuesController issuesController) { // (2)
        GET("/issues/show/{number}", issuesController, "issue", Integer.class); // (3)
    }
}
```

URI Variables Example

```kotlin
import io.micronaut.context.ExecutionHandleLocator
import io.micronaut.web.router.DefaultRouteBuilder
import io.micronaut.web.router.RouteBuilder
import jakarta.inject.Inject
import jakarta.inject.Singleton

@Singleton
class MyRoutes(executionHandleLocator: ExecutionHandleLocator,
               uriNamingStrategy: RouteBuilder.UriNamingStrategy) :
        DefaultRouteBuilder(executionHandleLocator, uriNamingStrategy) { // (1)

    @Inject
    fun issuesRoutes(issuesController: IssuesController) { // (2)
        GET("/issues/show/{number}", issuesController, "issue", Int::class.java) // (3)
    }
}
```

URI Variables Example

```groovy
import io.micronaut.context.ExecutionHandleLocator
import io.micronaut.core.convert.ConversionService
import io.micronaut.web.router.GroovyRouteBuilder

import jakarta.inject.Inject
import jakarta.inject.Singleton

@Singleton
class MyRoutes extends GroovyRouteBuilder { // (1)

    MyRoutes(ExecutionHandleLocator executionHandleLocator,
             UriNamingStrategy uriNamingStrategy,
             ConversionService conversionService) {
        super(executionHandleLocator, uriNamingStrategy, conversionService)
    }

    @Inject
    void issuesRoutes(IssuesController issuesController) { // (2)
        GET("/issues/show/{number}", issuesController.&issue) // (3)
    }
}
```

| **1** | Route definitions should subclass DefaultRouteBuilder |
|---|---|
| **2** | Use `@Inject` to inject a method with the controller to route to |
| **3** | Use methods such as `RouteBuilder::GET(String,Class,String,Class…)` to route to controller methods. Note that even though the issues controller is used, the route has no knowledge of its `@Controller` annotation and thus the full path must be specified. |

|   | Unfortunately due to type erasure, a Java method lambda reference cannot be used with the API. For Groovy there is a `GroovyRouteBuilder` class which can be subclassed that allows passing Groovy method references. |
|---|---|


## Route Compile-Time Validation

The Micronaut framework supports validating route arguments at compile time with the validation library. To get started, add the `micronaut-http-validation` dependency to your build:

`annotationProcessor("io.micronaut:micronaut-http-validation")` `<annotationProcessorPaths> <path> <groupId>io.micronaut</groupId> <artifactId>micronaut-http-validation</artifactId> </path> </annotationProcessorPaths>`

With the correct dependency on your classpath, route arguments will automatically be checked at compile time. Compilation will fail if any of the following conditions are met:

- The URI template contains a variable that is optional, but the method parameter is not annotated with `@Nullable` or is an `java.util.Optional`.

An optional variable is one that allows the route to match a URI even if the value is not present. For example `/foo{/bar}` matches requests to `/foo` and `/foo/abc`. The non-optional variant would be `/foo/{bar}`. See the URI Path Variables section for more information.

- The URI template contains a variable that is missing from the method arguments.

|   | To disable route compile-time validation, set the system property `-Dmicronaut.route.validation=false`. For Java and Kotlin users using Gradle, the same effect can be achieved by removing the `micronaut-http-validation` dependency from the `annotationProcessor`/`kapt` scope. |
|---|---|


## Routing non-standard HTTP methods

The `@CustomHttpMethod` annotation supports non-standard HTTP methods for a client or server. Specifications like RFC-4918 Webdav require additional methods like REPORT or LOCK for example.

RoutingExample

```java
@CustomHttpMethod(method = "LOCK", value = "/{name}")
String lock(String name)
```

The annotation can be used anywhere the standard method annotations can be used, including controllers and declarative HTTP clients.


## RouteMatch

The RouteMatch API provides information about an executable Route.

Given a request you can retrieve a RouteMatch with:

```java
String index(HttpRequest<?> request) {
    RouteMatch<?> routeMatch = RouteAttributes.getRouteMatch(request)
            .orElse(null);
```

```groovy
String index(HttpRequest<?> request) {
    RouteMatch<?> routeMatch = RouteAttributes.getRouteMatch(request)
            .orElse(null)
```


## 6.4 Simple Request Binding

The examples in the previous section demonstrate how the Micronaut framework lets you bind method parameters from URI path variables. This section shows how to bind arguments from other parts of the request.


## Binding Annotations

All binding annotations support customization of the name of the variable being bound from with their `name` member.

The following table summarizes the annotations and their purpose, and provides examples:

| Annotation | Description | Example |
|---|---|---|
| @Body | Binds from the body of the request | `@Body String body` |
| @CookieValue | Binds a parameter from a cookie | `@CookieValue String myCookie` |
| @Header | Binds a parameter from an HTTP header | `@Header String requestId` |
| @QueryValue | Binds from a request query parameter | `@QueryValue String myParam` |
| @Part | Binds from a part of a multipart request | `@Part CompletedFileUpload file` |
| @RequestAttribute | Binds from an attribute of the request. Attributes are typically created in filters | `@RequestAttribute String myAttribute` |
| @PathVariable | Binds from the path of the request | `@PathVariable String id` |
| @RequestBean | Binds any Bindable value to single Bean object | `@RequestBean MyBean bean` |

The method parameter name is used when a value is not specified in a binding annotation. In other words the following two methods are equivalent and both bind from a cookie named `myCookie`:

```java
@Get("/cookieName")
public String cookieName(@CookieValue("myCookie") String myCookie) {
    // ...
}

@Get("/cookieInferred")
public String cookieInferred(@CookieValue String myCookie) {
    // ...
}
```

```kotlin
@Get("/cookieName")
fun cookieName(@CookieValue("myCookie") myCookie: String): String {
    // ...
}

@Get("/cookieInferred")
fun cookieInferred(@CookieValue myCookie: String): String {
    // ...
}
```

```groovy
@Get("/cookieName")
String cookieName(@CookieValue("myCookie") String myCookie) {
    // ...
}

@Get("/cookieInferred")
String cookieInferred(@CookieValue String myCookie) {
    // ...
}
```

Because hyphens are not allowed in variable names, it may be necessary to set the name in the annotation. The following definitions are equivalent:

```java
@Get("/headerName")
public String headerName(@Header("Content-Type") String contentType) {
    // ...
}

@Get("/headerInferred")
public String headerInferred(@Header String contentType) {
    // ...
}
```

```kotlin
@Get("/headerName")
fun headerName(@Header("Content-Type") contentType: String): String {
    // ...
}

@Get("/headerInferred")
fun headerInferred(@Header contentType: String): String {
    // ...
}
```

```groovy
@Get("/headerName")
String headerName(@Header("Content-Type") String contentType) {
    // ...
}

@Get("/headerInferred")
String headerInferred(@Header String contentType) {
    // ...
}
```


## Stream Support

The Micronaut framework also supports binding the body to an `InputStream`. If the method is reading the stream, the method execution must be offloaded to another thread pool to avoid blocking the event loop.

Performing Blocking I/O With InputStream

```java
@Post(value = "/read", processes = MediaType.TEXT_PLAIN)
@ExecuteOn(TaskExecutors.IO) // (1)
String read(@Body InputStream inputStream) throws IOException { // (2)
    return IOUtils.readText(new BufferedReader(new InputStreamReader(inputStream))); // (3)
}
```

Performing Blocking I/O With InputStream

```kotlin
@Post(value = "/read", processes = [MediaType.TEXT_PLAIN])
@ExecuteOn(TaskExecutors.IO) // (1)
fun read(@Body inputStream: InputStream): String { // (2)
    return IOUtils.readText(BufferedReader(InputStreamReader(inputStream))) // (3)
}
```

Performing Blocking I/O With InputStream

```groovy
@Post(value = "/read", processes = MediaType.TEXT_PLAIN)
@ExecuteOn(TaskExecutors.IO) // (1)
String read(@Body InputStream inputStream) throws IOException { // (2)
    IOUtils.readText(new BufferedReader(new InputStreamReader(inputStream))) // (3)
}
```

| **1** | The controller method is executed on the IO thread pool |
|---|---|
| **2** | The body is passed to the method as an input stream |
| **3** | The stream is read |


## Binding from Multiple Query values

Instead of binding from a single section of the request, it may be desirable to bind all query values for example to a POJO. This can be achieved by using the exploded operator (`?pojo*`) in the URI template. For example:

Binding Request parameters to POJO

```java
import io.micronaut.http.HttpStatus;
import io.micronaut.http.annotation.Controller;
import io.micronaut.http.annotation.Get;
import org.jspecify.annotations.Nullable;

import jakarta.validation.Valid;

@Controller("/api")
public class BookmarkController {

    @Get("/bookmarks/list{?paginationCommand*}")
    public HttpStatus list(@Valid @Nullable PaginationCommand paginationCommand) {
        return HttpStatus.OK;
    }
}
```

Binding Request parameters to POJO

```kotlin
import io.micronaut.http.HttpStatus
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Get
import jakarta.validation.Valid

@Controller("/api")
open class BookmarkController {

    @Get("/bookmarks/list{?paginationCommand*}")
    open fun list(@Valid paginationCommand: PaginationCommand): HttpStatus {
        return HttpStatus.OK
    }
}
```

Binding Request parameters to POJO

```groovy
import io.micronaut.http.HttpStatus
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Get

import jakarta.annotation.Nullable
import jakarta.validation.Valid

@Controller("/api")
class BookmarkController {

    @Get("/bookmarks/list{?paginationCommand*}")
    HttpStatus list(@Valid @Nullable PaginationCommand paginationCommand) {
        HttpStatus.OK
    }
}
```


## Binding from Multiple Bindable values

Instead of binding just query values, it is also possible to bind any Bindable value to a POJO (e.g. to bind `HttpRequest`, `@PathVariable`, `@QueryValue` and `@Header` to a single POJO). This can be achieved with the `@RequestBean` annotation and a custom Bean class with fields with Bindable annotations, or fields that can be bound by type (e.g. `HttpRequest`, `BasicAuth`, `Authentication`, etc).

For example:

Binding Bindable values to POJO

```java
@Controller("/api")
public class MovieTicketController {

    // You can also omit query parameters like:
    // @Get("/movie/ticket/{movieId}
    @Get("/movie/ticket/{movieId}{?minPrice,maxPrice}")
    public HttpStatus list(@Valid @RequestBean MovieTicketBean bean) {
        return HttpStatus.OK;
    }
}
```

Binding Bindable values to POJO

```kotlin
@Controller("/api")
open class MovieTicketController {

    // You can also omit query parameters like:
    // @Get("/movie/ticket/{movieId}
    @Get("/movie/ticket/{movieId}{?minPrice,maxPrice}")
    open fun list(@Valid @RequestBean bean: MovieTicketBean): HttpStatus {
        return HttpStatus.OK
    }

}
```

Binding Bindable values to POJO

```groovy
@Controller("/api")
class MovieTicketController {

    // You can also omit query parameters like:
    // @Get("/movie/ticket/{movieId}
    @Get("/movie/ticket/{movieId}{?minPrice,maxPrice}")
    HttpStatus list(@Valid @RequestBean MovieTicketBean bean) {
        HttpStatus.OK
    }
}
```

which uses this bean class:

Bean definition

```java
@Introspected
public class MovieTicketBean {

    private HttpRequest<?> httpRequest;

    @PathVariable
    private String movieId;

    @Nullable
    @QueryValue
    @PositiveOrZero
    private Double minPrice;

    @Nullable
    @QueryValue
    @PositiveOrZero
    private Double maxPrice;

    public MovieTicketBean(HttpRequest<?> httpRequest,
                           String movieId,
                           Double minPrice,
                           Double maxPrice) {
        this.httpRequest = httpRequest;
        this.movieId = movieId;
        this.minPrice = minPrice;
        this.maxPrice = maxPrice;
    }

    public HttpRequest<?> getHttpRequest() {
        return httpRequest;
    }

    public String getMovieId() {
        return movieId;
    }

    @Nullable
    public Double getMaxPrice() {
        return maxPrice;
    }

    @Nullable
    public Double getMinPrice() {
        return minPrice;
    }
}
```

Bean definition

```kotlin
@Introspected
data class MovieTicketBean(
    val httpRequest: HttpRequest<Any>,
    @field:PathVariable val movieId: String,
    @field:QueryValue @field:PositiveOrZero @field:Nullable val minPrice: Double,
    @field:QueryValue @field:PositiveOrZero @field:Nullable val maxPrice: Double
)
```

Bean definition

```groovy
@Introspected
class MovieTicketBean {

    private HttpRequest<?> httpRequest

    @PathVariable
    String movieId

    @Nullable
    @QueryValue
    @PositiveOrZero
    Double minPrice

    @Nullable
    @QueryValue
    @PositiveOrZero
    Double maxPrice
}
```

The bean class has to be introspected with `@Introspected`. It can be one of:

1. Mutable Bean class with setters and getters
2. Immutable Bean class with getters and an all-argument constructor (or `@Creator` annotation on a constructor or static method). Arguments of the constructor must match field names so the object can be instantiated without reflection.

|   | Since Java does not retain argument names in bytecode, you must compile code with `-parameters` to use an immutable bean class from another jar. Another option is to extend Bean class in your source. |
|---|---|


## Bindable Types

Generally any type that can be converted from a String representation to a Java type via the ConversionService API can be bound to.

This includes most common Java types. However, you can simply add additional TypeConverter either by defining it as a bean or by registering it in a TypeConverterRegistrar via the service loader.

The handling of nullability deserves special mention. Consider for example the following example:

```java
@Get("/headerInferred")
public String headerInferred(@Header String contentType) {
    // ...
}
```

```kotlin
@Get("/headerInferred")
fun headerInferred(@Header contentType: String): String {
    // ...
}
```

```groovy
@Get("/headerInferred")
String headerInferred(@Header String contentType) {
    // ...
}
```

In this case, if the HTTP header `Content-Type` is not present in the request, the route is considered invalid, since it cannot be satisfied, and an HTTP 400 `BAD REQUEST` is returned.

To make the `Content-Type` header optional, you can instead write:

```java
@Get("/headerNullable")
public String headerNullable(@Nullable @Header String contentType) {
    // ...
}
```

```kotlin
@Get("/headerNullable")
fun headerNullable(@Header contentType: String?): String? {
    // ...
}
```

```groovy
@Get("/headerNullable")
String headerNullable(@Nullable @Header String contentType) {
    // ...
}
```

A `null` string is passed if the header is absent from the request.

|   | `java.util.Optional` can also be used, but that is discouraged for method parameters. |
|---|---|

Additionally, any `DateTime` that conforms to RFC-1123 can be bound to a parameter. Alternatively the format can be customized with the Format annotation:

```java
@Get("/date")
public String date(@Header ZonedDateTime date) {
    // ...
}

@Get("/dateFormat")
public String dateFormat(@Format("dd/MM/yyyy hh:mm:ss a z") @Header ZonedDateTime date) {
    // ...
}
```

```kotlin
@Get("/date")
fun date(@Header date: ZonedDateTime): String {
    // ...
}

@Get("/dateFormat")
fun dateFormat(@Format("dd/MM/yyyy hh:mm:ss a z") @Header date: ZonedDateTime): String {
    // ...
}
```

```groovy
@Get("/date")
String date(@Header ZonedDateTime date) {
    // ...
}

@Get("/dateFormat")
String dateFormat(@Format("dd/MM/yyyy hh:mm:ss a z") @Header ZonedDateTime date) {
    // ...
}
```


## Type-Based Binding Parameters

Some parameters are recognized by their type instead of their annotation. The following table summarizes the parameter types, their purpose, and provides an example:

| Type | Description | Example |
|---|---|---|
| BasicAuth | Allows binding of basic authorization credentials | `BasicAuth basicAuth` |


## Variable resolution

The Micronaut framework tries to populate method arguments in the following order:

1. URI variables like `/{id}`.
2. From query parameters if the request is a `GET` request (e.g. `?foo=bar`).
3. If there is a `@Body` and request allows the body, bind the body to it.
4. If the request can have a body and no `@Body` is defined then try to parse the body (either JSON or form data) and bind the method arguments from the body (see the example).
5. Finally, if the method arguments cannot be populated return `400 BAD REQUEST`.

Binding Method Arguments From Body with no

@Body

```java
@Controller("/point")
public class PointController {

    @Post(uri = "/no-body-json")
    @Status(HttpStatus.CREATED)
    Point noBodyJson(Integer x, Integer y) { // (1)
        return new Point(x,y);
    }

    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Post("/no-body-form")
    @Status(HttpStatus.CREATED)
    Point noBodyForm(Integer x, Integer y) {  // (2)
        return new Point(x,y);
    }
}
```

Binding Method Arguments From Body with no

@Body

```kotlin
@Controller("/point")
class PointController {

    @Post(uri = "/no-body-json")
    @Status(HttpStatus.CREATED)
    fun noBodyJson(x: Int, y: Int) = Point(x,y) // (1)

    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Post("/no-body-form")
    @Status(HttpStatus.CREATED)
    fun noBodyForm(x: Int, y: Int) = Point(x,y)  // (2)
}
```

Binding Method Arguments From Body with no

@Body

```groovy
@Controller("/point")
class PointController {

    @Post(uri = "/no-body-json")
    @Status(HttpStatus.CREATED)
    Point noBodyJson(Integer x, Integer y) { // (1)
        new Point(x: x,y: y)
    }

    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Post("/no-body-form")
    @Status(HttpStatus.CREATED)
    Point noBodyForm(Integer x, Integer y) {  // (2)
        new Point(x: x, y: y)
    }
}
```

| **1** | JSON request body binds to method controller arguments, e.g. '{"x":10,"y":20}' (with "application/json") |
|---|---|
| **2** | Form data also works, e.g. 'x=10&y=20' (with "application/x-www-form-urlencoded") |
