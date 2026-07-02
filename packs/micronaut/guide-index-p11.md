---
title: "Micronaut Core (part 11/27)"
source: https://docs.micronaut.io/latest/guide/index.html
domain: micronaut
license: CC-BY-SA-4.0
tags: micronaut framework, micronaut jvm, compile-time injection, microservices framework
fetched: 2026-07-02
part: 11/27
---

## 6.5 Custom Argument Binding

The Micronaut framework uses an ArgumentBinderRegistry to look up ArgumentBinder beans capable of binding to the arguments in controller methods. The default implementation looks for an annotation on the argument that is meta-annotated with @Bindable. If one exists the argument binder registry searches for an argument binder that supports that annotation.

If no fitting annotation is found, the Micronaut framework tries to find an argument binder that supports the argument type.

An argument binder returns a ArgumentBinder.BindingResult. The binding result gives the Micronaut framework more information than just the value. Binding results are either satisfied or unsatisfied, and either empty or not empty. If an argument binder returns an unsatisfied result, the binder may be called again at different times in request processing. Argument binders are initially called before the body is read and before any filters are executed. If a binder relies on any of that data, and it is not present, return a ArgumentBinder.BindingResult#UNSATISFIED result. Returning an ArgumentBinder.BindingResult#EMPTY or satisfied result will be the final result and the binder will not be called again for that request.

|   | At the end of processing if the result is still ArgumentBinder.BindingResult#UNSATISFIED, it is considered ArgumentBinder.BindingResult#EMPTY. |
|---|---|

Key interfaces are:

### AnnotatedRequestArgumentBinder

Argument binders that bind based on the presence of an annotation must implement AnnotatedRequestArgumentBinder, and can be used by creating an annotation that is annotated with Bindable. For example:

An example of a binding annotation

```java
import io.micronaut.context.annotation.AliasFor;
import io.micronaut.core.bind.annotation.Bindable;

import java.lang.annotation.Retention;
import java.lang.annotation.Target;

import static java.lang.annotation.ElementType.ANNOTATION_TYPE;
import static java.lang.annotation.ElementType.FIELD;
import static java.lang.annotation.ElementType.PARAMETER;
import static java.lang.annotation.RetentionPolicy.RUNTIME;

@Target({FIELD, PARAMETER, ANNOTATION_TYPE})
@Retention(RUNTIME)
@Bindable //(1)
public @interface ShoppingCart {

    @AliasFor(annotation = Bindable.class, member = "value")
    String value() default "";
}
```

An example of a binding annotation

```kotlin
import io.micronaut.core.bind.annotation.Bindable
import kotlin.annotation.AnnotationRetention.RUNTIME
import kotlin.annotation.AnnotationTarget.ANNOTATION_CLASS
import kotlin.annotation.AnnotationTarget.FIELD
import kotlin.annotation.AnnotationTarget.VALUE_PARAMETER

@Target(FIELD, VALUE_PARAMETER, ANNOTATION_CLASS)
@Retention(RUNTIME)
@Bindable //(1)
annotation class ShoppingCart(val value: String = "")
```

An example of a binding annotation

```groovy
import groovy.transform.CompileStatic
import io.micronaut.context.annotation.AliasFor
import io.micronaut.core.bind.annotation.Bindable

import java.lang.annotation.Retention
import java.lang.annotation.Target

import static java.lang.annotation.ElementType.ANNOTATION_TYPE
import static java.lang.annotation.ElementType.FIELD
import static java.lang.annotation.ElementType.PARAMETER
import static java.lang.annotation.RetentionPolicy.RUNTIME

@CompileStatic
@Target([FIELD, PARAMETER, ANNOTATION_TYPE])
@Retention(RUNTIME)
@Bindable //(1)
@interface ShoppingCart {
    @AliasFor(annotation = Bindable, member = "value")
    String value() default ""
}
```

| **1** | The binding annotation must itself be annotated as Bindable |
|---|---|

Example of annotated data binding

```java
import io.micronaut.core.convert.ArgumentConversionContext;
import io.micronaut.core.convert.ConversionService;
import io.micronaut.core.type.Argument;
import io.micronaut.http.HttpRequest;
import io.micronaut.http.bind.binders.AnnotatedRequestArgumentBinder;
import io.micronaut.http.cookie.Cookie;
import io.micronaut.jackson.serialize.JacksonObjectSerializer;

import jakarta.inject.Singleton;
import java.util.Map;
import java.util.Optional;

@Singleton
public class ShoppingCartRequestArgumentBinder
        implements AnnotatedRequestArgumentBinder<ShoppingCart, Object> { //(1)

    private final ConversionService conversionService;
    private final JacksonObjectSerializer objectSerializer;

    public ShoppingCartRequestArgumentBinder(ConversionService conversionService,
                                             JacksonObjectSerializer objectSerializer) {
        this.conversionService = conversionService;
        this.objectSerializer = objectSerializer;
    }

    @Override
    public Class<ShoppingCart> getAnnotationType() {
        return ShoppingCart.class;
    }

    @Override
    public BindingResult<Object> bind(
            ArgumentConversionContext<Object> context,
            HttpRequest<?> source) { //(2)

        String parameterName = context.getAnnotationMetadata()
                .stringValue(ShoppingCart.class)
                .orElse(context.getArgument().getName());

        Cookie cookie = source.getCookies().get("shoppingCart");
        if (cookie == null) {
            return BindingResult.EMPTY;
        }

        Optional<Map<String, Object>> cookieValue = objectSerializer.deserialize(
                cookie.getValue().getBytes(),
                Argument.mapOf(String.class, Object.class));

        return () -> cookieValue.flatMap(map -> {
            Object obj = map.get(parameterName);
            return conversionService.convert(obj, context);
        });
    }
}
```

Example of annotated data binding

```kotlin
import io.micronaut.core.bind.ArgumentBinder.BindingResult
import io.micronaut.core.convert.ArgumentConversionContext
import io.micronaut.core.convert.ConversionService
import io.micronaut.core.type.Argument
import io.micronaut.http.HttpRequest
import io.micronaut.http.bind.binders.AnnotatedRequestArgumentBinder
import io.micronaut.jackson.serialize.JacksonObjectSerializer
import java.util.Optional
import jakarta.inject.Singleton

@Singleton
class ShoppingCartRequestArgumentBinder(
        private val conversionService: ConversionService,
        private val objectSerializer: JacksonObjectSerializer
) : AnnotatedRequestArgumentBinder<ShoppingCart, Any> { //(1)

    override fun getAnnotationType(): Class<ShoppingCart> {
        return ShoppingCart::class.java
    }

    override fun bind(context: ArgumentConversionContext<Any>,
                      source: HttpRequest<*>): BindingResult<Any> { //(2)

        val parameterName = context.annotationMetadata
            .stringValue(ShoppingCart::class.java)
            .orElse(context.argument.name)

        val cookie = source.cookies.get("shoppingCart") ?: return BindingResult.EMPTY

        val cookieValue: Optional<Map<String, Any>> = objectSerializer.deserialize(
                cookie.value.toByteArray(),
                Argument.mapOf(String::class.java, Any::class.java))

        return BindingResult {
            cookieValue.flatMap { map: Map<String, Any> ->
                conversionService.convert(map[parameterName], context)
            }
        }
    }
}
```

Example of annotated data binding

```groovy
import groovy.transform.CompileStatic
import io.micronaut.core.convert.ArgumentConversionContext
import io.micronaut.core.convert.ConversionService
import io.micronaut.core.type.Argument
import io.micronaut.http.HttpRequest
import io.micronaut.http.bind.binders.AnnotatedRequestArgumentBinder
import io.micronaut.http.cookie.Cookie
import io.micronaut.jackson.serialize.JacksonObjectSerializer

import jakarta.inject.Singleton

@CompileStatic
@Singleton
class ShoppingCartRequestArgumentBinder
        implements AnnotatedRequestArgumentBinder<ShoppingCart, Object> { //(1)

    private final ConversionService conversionService
    private final JacksonObjectSerializer objectSerializer

    ShoppingCartRequestArgumentBinder(
            ConversionService conversionService,
            JacksonObjectSerializer objectSerializer) {
        this.conversionService = conversionService
        this.objectSerializer = objectSerializer
    }

    @Override
    Class<ShoppingCart> getAnnotationType() {
        ShoppingCart
    }

    @Override
    BindingResult<Object> bind(
            ArgumentConversionContext<Object> context,
            HttpRequest<?> source) { //(2)

        String parameterName = context.annotationMetadata
                .stringValue(ShoppingCart)
                .orElse(context.argument.name)

        Cookie cookie = source.cookies.get("shoppingCart")
        if (!cookie) {
            return BindingResult.EMPTY
        }

        Optional<Map<String, Object>> cookieValue = objectSerializer.deserialize(
                cookie.value.bytes,
                Argument.mapOf(String, Object))

        return (BindingResult) { ->
            cookieValue.flatMap({value ->
                conversionService.convert(value.get(parameterName), context)
            })
        }
    }
}
```

| **1** | The custom argument binder must implement AnnotatedRequestArgumentBinder, including both the annotation type to trigger the binder (in this case, `MyBindingAnnotation`) and the type of the argument expected (in this case, `Object`) |
|---|---|
| **2** | Override the `bind` method with the custom argument binding logic - in this case, we resolve the name of the annotated argument, extract a value from a cookie with that same name, and convert that value to the argument type |

|   | It is common to use ConversionService to convert the data to the type of the argument. |
|---|---|

Once the binder is created, we can annotate an argument in our controller method which will be bound using the custom logic we’ve specified.

A controller operation with this annotated binding

```java
    @Get("/annotated")
    HttpResponse<String> checkSession(@ShoppingCart Long sessionId) { //(1)
        return HttpResponse.ok("Session:" + sessionId);
    }
    // end::method
}
```

A controller operation with this annotated binding

```kotlin
@Get("/annotated")
fun checkSession(@ShoppingCart sessionId: Long): HttpResponse<String> { //(1)
    return HttpResponse.ok("Session:$sessionId")
}
```

A controller operation with this annotated binding

```groovy
    @Get("/annotated")
    HttpResponse<String> checkSession(@ShoppingCart Long sessionId) { //(1)
        HttpResponse.ok("Session:" + sessionId)
    }
    // end::method
}
```

| **1** | The parameter is bound with the binder associated with `MyBindingAnnotation`. This takes precedence over a type-based binder, if applicable. |
|---|---|

### TypedRequestArgumentBinder

Argument binders that bind based on the type of the argument must implement TypedRequestArgumentBinder. For example, given this class:

Example of POJO

```java
import io.micronaut.core.annotation.Introspected;

@Introspected
public class ShoppingCart {

    private String sessionId;
    private Integer total;

    public String getSessionId() {
        return sessionId;
    }

    public void setSessionId(String sessionId) {
        this.sessionId = sessionId;
    }

    public Integer getTotal() {
        return total;
    }

    public void setTotal(Integer total) {
        this.total = total;
    }
}
```

Example of POJO

```kotlin
import io.micronaut.core.annotation.Introspected

@Introspected
class ShoppingCart {
    var sessionId: String? = null
    var total: Int? = null
}
```

Example of POJO

```groovy
import io.micronaut.core.annotation.Introspected

@Introspected
class ShoppingCart {
    String sessionId
    Integer total
}
```

We can define a `TypedRequestArgumentBinder` for this class, as seen below:

Example of typed data binding

```java
import io.micronaut.core.convert.ArgumentConversionContext;
import io.micronaut.core.type.Argument;
import io.micronaut.http.HttpRequest;
import io.micronaut.http.bind.binders.TypedRequestArgumentBinder;
import io.micronaut.http.cookie.Cookie;
import io.micronaut.jackson.serialize.JacksonObjectSerializer;

import jakarta.inject.Singleton;
import java.util.Optional;

@Singleton
public class ShoppingCartRequestArgumentBinder
        implements TypedRequestArgumentBinder<ShoppingCart> {

    private final JacksonObjectSerializer objectSerializer;

    public ShoppingCartRequestArgumentBinder(JacksonObjectSerializer objectSerializer) {
        this.objectSerializer = objectSerializer;
    }

    @Override
    public BindingResult<ShoppingCart> bind(ArgumentConversionContext<ShoppingCart> context,
                                            HttpRequest<?> source) { //(1)

        Cookie cookie = source.getCookies().get("shoppingCart");
        if (cookie == null) {
            return Optional::empty;
        }

        return () -> objectSerializer.deserialize( //(2)
                cookie.getValue().getBytes(),
                ShoppingCart.class);
    }

    @Override
    public Argument<ShoppingCart> argumentType() {
        return Argument.of(ShoppingCart.class); //(3)
    }
}
```

Example of typed data binding

```kotlin
import io.micronaut.core.bind.ArgumentBinder
import io.micronaut.core.bind.ArgumentBinder.BindingResult
import io.micronaut.core.convert.ArgumentConversionContext
import io.micronaut.core.type.Argument
import io.micronaut.http.HttpRequest
import io.micronaut.http.bind.binders.TypedRequestArgumentBinder
import io.micronaut.jackson.serialize.JacksonObjectSerializer
import java.util.Optional
import jakarta.inject.Singleton

@Singleton
class ShoppingCartRequestArgumentBinder(private val objectSerializer: JacksonObjectSerializer) :
    TypedRequestArgumentBinder<ShoppingCart> {

    override fun bind(
        context: ArgumentConversionContext<ShoppingCart>,
        source: HttpRequest<*>
    ): BindingResult<ShoppingCart> { //(1)

        val cookie = source.cookies["shoppingCart"]

        return if (cookie == null)
            BindingResult {
                Optional.empty()
            }
        else {
            BindingResult {
                objectSerializer.deserialize( // (2)
                    cookie.value.toByteArray(),
                    ShoppingCart::class.java
                )
            }
        }
    }

    override fun argumentType(): Argument<ShoppingCart> {
        return Argument.of(ShoppingCart::class.java) //(3)
    }
}
```

Example of typed data binding

```groovy
import io.micronaut.core.convert.ArgumentConversionContext
import io.micronaut.core.type.Argument
import io.micronaut.http.HttpRequest
import io.micronaut.http.bind.binders.TypedRequestArgumentBinder
import io.micronaut.http.cookie.Cookie
import io.micronaut.jackson.serialize.JacksonObjectSerializer

import jakarta.inject.Singleton

@Singleton
class ShoppingCartRequestArgumentBinder
        implements TypedRequestArgumentBinder<ShoppingCart> {

    private final JacksonObjectSerializer objectSerializer

    ShoppingCartRequestArgumentBinder(JacksonObjectSerializer objectSerializer) {
        this.objectSerializer = objectSerializer
    }

    @Override
    BindingResult<ShoppingCart> bind(ArgumentConversionContext<ShoppingCart> context,
                                     HttpRequest<?> source) { //(1)

        Cookie cookie = source.cookies.get("shoppingCart")
        if (!cookie) {
            return BindingResult.EMPTY
        }

        return () -> objectSerializer.deserialize( //(2)
                cookie.value.bytes,
                ShoppingCart)
    }

    @Override
    Argument<ShoppingCart> argumentType() {
        Argument.of(ShoppingCart) //(3)
    }
}
```

| **1** | Override the `bind` method with the data type to bind, in this example the `ShoppingCart` type |
|---|---|
| **2** | After retrieving the data (in this case, by deserializing JSON text from a cookie), return as a ArgumentBinder.BindingResult |
| **3** | Also override the `argumentType` method, which is used by the ArgumentBinderRegistry. |

Once the binder is created, it is used for any controller argument of the associated type:

A controller operation with this typed binding

```java
@Get("/typed")
public HttpResponse<?> loadCart(ShoppingCart shoppingCart) { //(1)
    Map<String, Object> responseMap = new HashMap<>();
    responseMap.put("sessionId", shoppingCart.getSessionId());
    responseMap.put("total", shoppingCart.getTotal());

    return HttpResponse.ok(responseMap);
}
```

A controller operation with this typed binding

```kotlin
@Get("/typed")
fun loadCart(shoppingCart: ShoppingCart): HttpResponse<*> { //(1)
    return HttpResponse.ok(mapOf(
        "sessionId" to shoppingCart.sessionId,
        "total" to shoppingCart.total))
}
```

A controller operation with this typed binding

```groovy
@Get("/typed")
HttpResponse<Map<String, Object>> loadCart(ShoppingCart shoppingCart) { //(1)
    HttpResponse.ok(
            sessionId: shoppingCart.sessionId,
            total: shoppingCart.total)
}
```

| **1** | The parameter is bound using the custom logic defined for this type in our `TypedRequestArgumentBinder` |
|---|---|


## 6.6 Host Resolution

You may need to resolve the host name of the current server. The Micronaut framework includes an implementation of the HttpHostResolver interface.

The default implementation looks for host information in the following places in order:

1. The supplied configuration
2. The `Forwarded` header
3. `X-Forwarded-` headers. If the `X-Forwarded-Host` header is not present, the other `X-Forwarded` headers are ignored.
4. The `Host` header
5. The properties on the request URI
6. The properties on the embedded server URI

The behavior of which headers to pull the relevant data can be changed with the following configuration:

🔗

| Property | Type | Description | Default value |
|---|---|---|---|
| `micronaut.server.host-resolution.host-header` | java.lang.String | The host header name |   |
| `micronaut.server.host-resolution.protocol-header` | java.lang.String | The protocol header name |   |
| `micronaut.server.host-resolution.port-header` | java.lang.String | The port header name |   |
| `micronaut.server.host-resolution.port-in-host` | boolean | If the host header supports a port |   |
| `micronaut.server.host-resolution.allowed-hosts` | java.util.List | The list of hosts to validate the resolved host against. |   |

The above configuration also supports an allowed host list. Configuring this list ensures any resolved host matches one of the supplied regular expression patterns. That is useful to prevent host cache poisoning attacks and is recommended to be configured.


## 6.7 Locale Resolution

The Micronaut framework supports several strategies for resolving locales for a given request. The getLocale-- method is available on the request, however it only supports parsing the `Accept-Language` header. For other use cases where the locale can be in a cookie, the user’s session, or should be set to a fixed value, HttpLocaleResolver can be used to determine the current locale.

The LocaleResolver API does not need to be used directly. Simply define a parameter to a controller method of type `java.util.Locale` and the locale will be resolved and injected automatically.

There are several configuration options to control how to resolve the locale:

🔗

| Property | Type | Description | Default value |
|---|---|---|---|
| `micronaut.server.locale-resolution.fixed` | java.util.Locale | Set the language tag for the locale. Supports BCP 47 language tags (e.g. "en-US") and ISO standard (e.g "en_US"). |   |
| `micronaut.server.locale-resolution.session-attribute` | java.lang.String | Sets the key in the session to look for the locale. |   |
| `micronaut.server.locale-resolution.default-locale` | java.util.Locale | Sets the locale that will be used if the locale cannot be resolved through any means. Defaults to the system default. |   |
| `micronaut.server.locale-resolution.cookie-name` | java.lang.String | Sets the name of the cookie that is used to store the locale. |   |
| `micronaut.server.locale-resolution.header` | boolean | Set to true if the locale should be resolved from the `Accept-Language` header. Default value (true). |   |

Locales can be configured in the "en_GB" format, or in the BCP 47 (Language tag) format. If multiple methods are configured, the fixed locale takes precedence, followed by session/cookie, then header.

If any of the built-in methods do not meet your use case, create a bean of type HttpLocaleResolver and set its order (through the `getOrder` method) relative to the existing resolvers.


## 6.8 Client IP Address

You may need to resolve the originating IP address of an HTTP Request. The Micronaut framework includes an implementation of HttpClientAddressResolver.

The default implementation resolves the client address in the following places in order:

1. The configured header
2. The `Forwarded` header
3. The `X-Forwarded-For` header
4. The remote address on the request

The first priority header name can be configured with `micronaut.server.client-address-header`.


## 6.9 The HttpRequest and HttpResponse

If you need more control over request processing you can write a method that receives the complete HttpRequest.

In fact, there are several higher-level interfaces that can be bound to controller method parameters. These include:

| Interface | Description | Example |
|---|---|---|
| HttpRequest | The full `HttpRequest` | `String hello(HttpRequest request)` |
| HttpHeaders | All HTTP headers present in the request | `String hello(HttpHeaders headers)` |
| HttpParameters | All HTTP parameters (either from URI variables or request parameters) present in the request | `String hello(HttpParameters params)` |
| Cookies | All Cookies present in the request | `String hello(Cookies cookies)` |

|   | The HttpRequest should be declared parametrized with a concrete generic type if the request body is needed, e.g. `HttpRequest<MyClass> request`. The body may not be available from the request otherwise. |
|---|---|

In addition, for full control over the emitted HTTP response you can use the static factory methods of the HttpResponse class which return a MutableHttpResponse.

The following example implements the previous `MessageController` example using the HttpRequest and HttpResponse objects:

Request and Response Example

```java
import io.micronaut.http.HttpRequest;
import io.micronaut.http.HttpResponse;
import io.micronaut.http.annotation.Controller;
import io.micronaut.http.annotation.Get;
import io.micronaut.http.context.ServerRequestContext;
import reactor.core.publisher.Mono;

@Controller("/request")
public class MessageController {

@Get("/hello") // (1)
public HttpResponse<String> hello(HttpRequest<?> request) {
    String name = request.getParameters()
                         .getFirst("name")
                         .orElse("Nobody"); // (2)

    return HttpResponse.ok("Hello " + name + "!!")
             .header("X-My-Header", "Foo"); // (3)
}

}
```

Request and Response Example

```kotlin
import io.micronaut.http.HttpRequest
import io.micronaut.http.HttpResponse
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Get
import io.micronaut.http.context.ServerRequestContext
import reactor.core.publisher.Mono
import reactor.util.context.ContextView

@Controller("/request")
class MessageController {

@Get("/hello") // (1)
fun hello(request: HttpRequest<*>): HttpResponse<String> {
    val name = request.parameters
                      .getFirst("name")
                      .orElse("Nobody") // (2)

    return HttpResponse.ok("Hello $name!!")
            .header("X-My-Header", "Foo") // (3)
}

}
```

Request and Response Example

```groovy
import io.micronaut.http.HttpRequest
import io.micronaut.http.HttpResponse
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Get
import io.micronaut.http.context.ServerRequestContext
import reactor.core.publisher.Mono

@Controller("/request")
class MessageController {

@Get("/hello") // (1)
HttpResponse<String> hello(HttpRequest<?> request) {
    String name = request.parameters
                         .getFirst("name")
                         .orElse("Nobody") // (2)

    HttpResponse.ok("Hello " + name + "!!")
             .header("X-My-Header", "Foo") // (3)
}

}
```

| **1** | The method is mapped to the URI `/hello` and accepts a HttpRequest |
|---|---|
| **2** | The HttpRequest is used to obtain the value of a query parameter named `name`. |
| **3** | The HttpResponse.ok(T) method returns a MutableHttpResponse with a text body. A header named `X-My-Header` is also added to the response. |

The HttpRequest is also available from a static context via ServerRequestContext.

Using the ServerRequestContext

```java
import io.micronaut.http.HttpRequest;
import io.micronaut.http.HttpResponse;
import io.micronaut.http.annotation.Controller;
import io.micronaut.http.annotation.Get;
import io.micronaut.http.context.ServerRequestContext;
import reactor.core.publisher.Mono;

@Controller("/request")
public class MessageController {

@Get("/hello-static") // (1)
public HttpResponse<String> helloStatic() {
    HttpRequest<?> request = ServerRequestContext.currentRequest() // (1)
            .orElseThrow(() -> new RuntimeException("No request present"));
    String name = request.getParameters()
            .getFirst("name")
            .orElse("Nobody");

    return HttpResponse.ok("Hello " + name + "!!")
            .header("X-My-Header", "Foo");
}

}
```

Using the ServerRequestContext

```kotlin
import io.micronaut.http.HttpRequest
import io.micronaut.http.HttpResponse
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Get
import io.micronaut.http.context.ServerRequestContext
import reactor.core.publisher.Mono
import reactor.util.context.ContextView

@Controller("/request")
class MessageController {

@Get("/hello-static") // (1)
fun helloStatic(): HttpResponse<String> {
    val request: HttpRequest<*> = ServerRequestContext.currentRequest<Any>() // (1)
        .orElseThrow { RuntimeException("No request present") }
    val name = request.parameters
        .getFirst("name")
        .orElse("Nobody")
    return HttpResponse.ok("Hello $name!!")
        .header("X-My-Header", "Foo")
}

}
```

Using the ServerRequestContext

```groovy
import io.micronaut.http.HttpRequest
import io.micronaut.http.HttpResponse
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Get
import io.micronaut.http.context.ServerRequestContext
import reactor.core.publisher.Mono

@Controller("/request")
class MessageController {

@Get("/hello-static") // (1)
HttpResponse<String> helloStatic() {
    HttpRequest<?> request = ServerRequestContext.currentRequest() // (1)
            .orElseThrow(() -> new RuntimeException("No request present"))
    String name = request.parameters
            .getFirst("name")
            .orElse("Nobody")

    HttpResponse.ok("Hello " + name + "!!")
            .header("X-My-Header", "Foo")
}

}
```

| **1** | The ServerRequestContext is used to retrieve the request. |
|---|---|

|   | Generally ServerRequestContext is available within reactive flow, but the recommended approach is consumed the request as an argument as shown in the previous example. If the request is needed in downstream methods it should be passed as an argument to those methods. There are cases where the context is not propagated because other threads are used to emit the data. |
|---|---|

An alternative for users of Project Reactor to using the ServerRequestContext is to use the contextual features of Project Reactor to retrieve the request. Because the Micronaut Framework uses Project Reactor as it’s default reactive streams implementation, users of Project Reactor can benefit by being able to access the request in the context. For example:

Using the Project Reactor context

```java
import io.micronaut.http.HttpRequest;
import io.micronaut.http.HttpResponse;
import io.micronaut.http.annotation.Controller;
import io.micronaut.http.annotation.Get;
import io.micronaut.http.context.ServerRequestContext;
import reactor.core.publisher.Mono;

@Controller("/request")
public class MessageController {

@Get("/hello-reactor")
public Mono<HttpResponse<String>> helloReactor() {
    return Mono.deferContextual(ctx -> { // (1)
        HttpRequest<?> request = ctx.get(ServerRequestContext.KEY); // (2)
        String name = request.getParameters()
                .getFirst("name")
                .orElse("Nobody");

        return Mono.just(HttpResponse.ok("Hello " + name + "!!")
                .header("X-My-Header", "Foo"));
    });
}

}
```

Using the Project Reactor context

```kotlin
import io.micronaut.http.HttpRequest
import io.micronaut.http.HttpResponse
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Get
import io.micronaut.http.context.ServerRequestContext
import reactor.core.publisher.Mono
import reactor.util.context.ContextView

@Controller("/request")
class MessageController {

@Get("/hello-reactor")
fun helloReactor(): Mono<HttpResponse<String>?>? {
    return Mono.deferContextual { ctx: ContextView ->  // (1)
        val request = ctx.get<HttpRequest<*>>(ServerRequestContext.KEY) // (2)
        val name = request.parameters
            .getFirst("name")
            .orElse("Nobody")
        Mono.just(HttpResponse.ok("Hello $name!!")
                .header("X-My-Header", "Foo"))
    }
}

}
```

Using the Project Reactor context

```groovy
import io.micronaut.http.HttpRequest
import io.micronaut.http.HttpResponse
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Get
import io.micronaut.http.context.ServerRequestContext
import reactor.core.publisher.Mono

@Controller("/request")
class MessageController {

@Get("/hello-reactor")
Mono<HttpResponse<String>> helloReactor() {
    Mono.deferContextual(ctx -> { // (1)
        HttpRequest<?> request = ctx.get(ServerRequestContext.KEY) // (2)
        String name = request.parameters
                .getFirst("name")
                .orElse("Nobody")

        Mono.just(HttpResponse.ok("Hello " + name + "!!")
                .header("X-My-Header", "Foo"))
    })
}

}
```

| **1** | The Mono is created with a reference to the context |
|---|---|
| **2** | The request is retrieved from the context |

Using the context to retrieve the request is the best approach for reactive flows because Project Reactor propagates the context, and it does not rely on a thread local like ServerRequestContext.


## 6.10 Response Status

A Micronaut controller action responds with a 200 HTTP status code by default.

If the action returns an `HttpResponse`, configure the status code for the response with the `status` method.

```java
@Get(value = "/http-response", produces = MediaType.TEXT_PLAIN)
public HttpResponse httpResponse() {
    return HttpResponse.status(HttpStatus.CREATED).body("success");
}
```

```kotlin
@Get(value = "/http-response", produces = [MediaType.TEXT_PLAIN])
fun httpResponse(): HttpResponse<String> {
    return HttpResponse.status<String>(HttpStatus.CREATED).body("success")
}
```

```groovy
@Get(value = "/http-response", produces = MediaType.TEXT_PLAIN)
HttpResponse httpResponse() {
    HttpResponse.status(HttpStatus.CREATED).body("success")
}
```

You can also use the `@Status` annotation.

```java
@Status(HttpStatus.CREATED)
@Get(produces = MediaType.TEXT_PLAIN)
public String index() {
    return "success";
}
```

```kotlin
@Status(HttpStatus.CREATED)
@Get(produces = [MediaType.TEXT_PLAIN])
fun index(): String {
    return "success"
}
```

```groovy
@Status(HttpStatus.CREATED)
@Get(produces = MediaType.TEXT_PLAIN)
String index() {
    "success"
}
```

or even respond with an `HttpStatus`

```java
@Get("/http-status")
public HttpStatus httpStatus() {
    return HttpStatus.CREATED;
}
```

```kotlin
@Get("/http-status")
fun httpStatus(): HttpStatus {
    return HttpStatus.CREATED
}
```

```groovy
@Get("/http-status")
HttpStatus httpStatus() {
    HttpStatus.CREATED
}
```

### Custom HTTP Status Codes

Micronaut supports arbitrary HTTP status codes not part of the predefined `HttpStatus` enum. You can use the API method `HttpResponse#status(int,java.lang.String)`


## 6.11 Response Content-Type

A Micronaut controller action produces `application/json` by default. However, you can change the `Content-Type` of the response with the `@Produces` annotation or the `produces` member of the HTTP method annotations.

```java
import io.micronaut.context.annotation.Requires;
import io.micronaut.http.HttpResponse;
import io.micronaut.http.MediaType;
import io.micronaut.http.annotation.Controller;
import io.micronaut.http.annotation.Get;
import io.micronaut.http.annotation.Produces;

@Controller("/produces")
public class ProducesController {

    @Get // (1)
    public HttpResponse index() {
        return HttpResponse.ok().body("{\"msg\":\"This is JSON\"}");
    }

    @Produces(MediaType.TEXT_HTML)
    @Get("/html") // (2)
    public String html() {
        return "<html><title><h1>HTML</h1></title><body></body></html>";
    }

    @Get(value = "/xml", produces = MediaType.TEXT_XML) // (3)
    public String xml() {
        return "<html><title><h1>XML</h1></title><body></body></html>";
    }
}
```

```kotlin
import io.micronaut.context.annotation.Requires
import io.micronaut.http.HttpResponse
import io.micronaut.http.MediaType
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Get
import io.micronaut.http.annotation.Produces

@Controller("/produces")
class ProducesController {

    @Get // (1)
    fun index(): HttpResponse<*> {
        return HttpResponse.ok<Any>().body("{\"msg\":\"This is JSON\"}")
    }

    @Produces(MediaType.TEXT_HTML)
    @Get("/html") // (2)
    fun html(): String {
        return "<html><title><h1>HTML</h1></title><body></body></html>"
    }

    @Get(value = "/xml", produces = [MediaType.TEXT_XML]) // (3)
    fun xml(): String {
        return "<html><title><h1>XML</h1></title><body></body></html>"
    }
}
```

```groovy
import io.micronaut.context.annotation.Requires
import io.micronaut.http.HttpResponse
import io.micronaut.http.MediaType
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Get
import io.micronaut.http.annotation.Produces

@Controller("/produces")
class ProducesController {

    @Get // (1)
    HttpResponse index() {
        HttpResponse.ok().body('{"msg":"This is JSON"}')
    }

    @Produces(MediaType.TEXT_HTML) // (2)
    @Get("/html")
    String html() {
        "<html><title><h1>HTML</h1></title><body></body></html>"
    }

    @Get(value = "/xml", produces = MediaType.TEXT_XML) // (3)
    String xml() {
        "<html><title><h1>XML</h1></title><body></body></html>"
    }
}
```

| **1** | The default content type is JSON |
|---|---|
| **2** | Annotate a controller action with `@Produces` to change the response content type. |
| **3** | Setting the `produces` member of the method annotation also changes the content type. |


## 6.12 Accepted Request Content-Type

A Micronaut controller action consumes `application/json` by default. Consuming other content types is supported with the `@Consumes` annotation, or the `consumes` member of any HTTP method annotation.

```java
import io.micronaut.context.annotation.Requires;
import io.micronaut.http.HttpResponse;
import io.micronaut.http.MediaType;
import io.micronaut.http.annotation.Consumes;
import io.micronaut.http.annotation.Controller;
import io.micronaut.http.annotation.Post;

@Controller("/consumes")
public class ConsumesController {

    @Post // (1)
    public HttpResponse index() {
        return HttpResponse.ok();
    }

    @Consumes({MediaType.APPLICATION_FORM_URLENCODED, MediaType.APPLICATION_JSON}) // (2)
    @Post("/multiple")
    public HttpResponse multipleConsumes() {
        return HttpResponse.ok();
    }

    @Post(value = "/member", consumes = MediaType.TEXT_PLAIN) // (3)
    public HttpResponse consumesMember() {
        return HttpResponse.ok();
    }
}
```

```kotlin
import io.micronaut.context.annotation.Requires
import io.micronaut.http.HttpResponse
import io.micronaut.http.MediaType
import io.micronaut.http.annotation.Consumes
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Post

@Controller("/consumes")
class ConsumesController {

    @Post // (1)
    fun index(): HttpResponse<*> {
        return HttpResponse.ok<Any>()
    }

    @Consumes(MediaType.APPLICATION_FORM_URLENCODED, MediaType.APPLICATION_JSON) // (2)
    @Post("/multiple")
    fun multipleConsumes(): HttpResponse<*> {
        return HttpResponse.ok<Any>()
    }

    @Post(value = "/member", consumes = [MediaType.TEXT_PLAIN]) // (3)
    fun consumesMember(): HttpResponse<*> {
        return HttpResponse.ok<Any>()
    }
}
```

```groovy
import io.micronaut.context.annotation.Requires
import io.micronaut.http.HttpResponse
import io.micronaut.http.MediaType
import io.micronaut.http.annotation.Consumes
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Post

@Controller("/consumes")
class ConsumesController {

    @Post // (1)
    HttpResponse index() {
        HttpResponse.ok()
    }

    @Consumes([MediaType.APPLICATION_FORM_URLENCODED, MediaType.APPLICATION_JSON]) // (2)
    @Post("/multiple")
    HttpResponse multipleConsumes() {
        HttpResponse.ok()
    }

    @Post(value = "/member", consumes = MediaType.TEXT_PLAIN) // (3)
    HttpResponse consumesMember() {
        HttpResponse.ok()
    }
}
```

| **1** | By default, a controller action consumes request with `Content-Type` of type `application/json`. |
|---|---|
| **2** | The `@Consumes` annotation takes a `String[]` of supported media types for an incoming request. |
| **3** | Content types can also be specified with the `consumes` member of the method annotation. |

### Customizing Processed Content Types

Normally JSON parsing only happens if the content type is `application/json`. The other MediaTypeCodec classes behave similarly in that they have predefined content types they can process. To extend the list of media types that a given codec processes, provide configuration that will be stored in CodecConfiguration:

```properties
micronaut.codec.json.additional-types[0]=text/javascript
micronaut.codec.json.additional-types[1]=...
```

```yaml
micronaut:
  codec:
    json:
      additional-types:
        - text/javascript
        - ...
```

```toml
[micronaut]
  [micronaut.codec]
    [micronaut.codec.json]
      additional-types=[
        "text/javascript",
        "..."
      ]
```

```groovy
micronaut {
  codec {
    json {
      additionalTypes = ["text/javascript", "..."]
    }
  }
}
```

```hocon
{
  micronaut {
    codec {
      json {
        additional-types = ["text/javascript", "..."]
      }
    }
  }
}
```

```json
{
  "micronaut": {
    "codec": {
      "json": {
        "additional-types": ["text/javascript", "..."]
      }
    }
  }
}
```

The currently supported configuration prefixes are `json`, `json-stream`, `text`, and `text-stream`.


## 6.13 Reactive HTTP Request Processing

As mentioned previously, Micronaut framework is built on Netty which is designed around an Event loop model and non-blocking I/O. Micronaut executes code defined in @Controller beans in the same thread as the request thread (an Event Loop thread).

This makes it critical that if you do any blocking I/O operations (for example interactions with Hibernate/JPA or JDBC) that you offload those tasks to a separate thread pool that does not block the Event loop.

For example the following configuration configures the I/O thread pool as a fixed thread pool with 75 threads (similar to what a traditional blocking server such as Tomcat uses in the thread-per-request model):

Configuring the IO thread pool

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

To use this thread pool in a @Controller bean you have a number of options. The simplest is to use the @ExecuteOn annotation, which can be applied only to either a @Controller or @Filter at the type or method level. It indicates the configured thread pool to run method(s) of the controller or filter on:

Using @ExecuteOn

```java
import io.micronaut.docs.http.server.reactive.PersonService;
import io.micronaut.docs.ioc.beans.Person;
import io.micronaut.http.annotation.Controller;
import io.micronaut.http.annotation.Get;
import io.micronaut.scheduling.TaskExecutors;
import io.micronaut.scheduling.annotation.ExecuteOn;

@Controller("/executeOn/people")
public class PersonController {

    private final PersonService personService;

    PersonController(PersonService personService) {
        this.personService = personService;
    }

    @Get("/{name}")
    @ExecuteOn(TaskExecutors.IO) // (1)
    Person byName(String name) {
        return personService.findByName(name);
    }
}
```

Using @ExecuteOn

```kotlin
import io.micronaut.docs.http.server.reactive.PersonService
import io.micronaut.docs.ioc.beans.Person
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Get
import io.micronaut.scheduling.TaskExecutors
import io.micronaut.scheduling.annotation.ExecuteOn

@Controller("/executeOn/people")
class PersonController (private val personService: PersonService) {

    @Get("/{name}")
    @ExecuteOn(TaskExecutors.IO) // (1)
    fun byName(name: String): Person {
        return personService.findByName(name)
    }
}
```

Using @ExecuteOn

```groovy
import io.micronaut.docs.http.server.reactive.PersonService
import io.micronaut.docs.ioc.beans.Person
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Get
import io.micronaut.scheduling.TaskExecutors
import io.micronaut.scheduling.annotation.ExecuteOn

@Controller("/executeOn/people")
class PersonController {

    private final PersonService personService

    PersonController(PersonService personService) {
        this.personService = personService
    }

    @Get("/{name}")
    @ExecuteOn(TaskExecutors.IO) // (1)
    Person byName(String name) {
        personService.findByName(name)
    }
}
```

| **1** | The @ExecuteOn annotation is used to execute the operation on the I/O thread pool |
|---|---|

The value of the @ExecuteOn annotation can be any named executor defined under `micronaut.executors`.

|   | Generally speaking for database operations you want a thread pool configured that matches the maximum number of connections specified in the database connection pool. |
|---|---|

An alternative to the @ExecuteOn annotation is to use the facility provided by the reactive library you have chosen. Reactive implementations such as Project Reactor or RxJava feature a `subscribeOn` method which lets you alter which thread executes user code. For example:

Reactive subscribeOn Example

```java
import io.micronaut.docs.ioc.beans.Person;
import io.micronaut.http.annotation.Controller;
import io.micronaut.http.annotation.Get;
import io.micronaut.scheduling.TaskExecutors;
import jakarta.inject.Named;
import org.reactivestreams.Publisher;
import reactor.core.publisher.Mono;
import reactor.core.scheduler.Scheduler;
import reactor.core.scheduler.Schedulers;
import io.micronaut.core.async.annotation.SingleResult;
import java.util.concurrent.ExecutorService;

@Controller("/subscribeOn/people")
public class PersonController {

    private final Scheduler scheduler;
    private final PersonService personService;

    PersonController(
            @Named(TaskExecutors.IO) ExecutorService executorService, // (1)
            PersonService personService) {
        this.scheduler = Schedulers.fromExecutorService(executorService);
        this.personService = personService;
    }

    @Get("/{name}")
    @SingleResult
    Publisher<Person> byName(String name) {
        return Mono
                .fromCallable(() -> personService.findByName(name)) // (2)
                .subscribeOn(scheduler); // (3)
    }
}
```

Reactive subscribeOn Example

```kotlin
import io.micronaut.docs.ioc.beans.Person
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Get
import io.micronaut.scheduling.TaskExecutors
import java.util.concurrent.ExecutorService
import jakarta.inject.Named
import reactor.core.publisher.Mono
import reactor.core.scheduler.Scheduler
import reactor.core.scheduler.Schedulers

@Controller("/subscribeOn/people")
class PersonController internal constructor(
    @Named(TaskExecutors.IO) executorService: ExecutorService, // (1)
    private val personService: PersonService) {

    private val scheduler: Scheduler = Schedulers.fromExecutorService(executorService)

    @Get("/{name}")
    fun byName(name: String): Mono<Person> {
        return Mono
            .fromCallable { personService.findByName(name) } // (2)
            .subscribeOn(scheduler) // (3)
    }
}
```

Reactive subscribeOn Example

```groovy
import io.micronaut.docs.ioc.beans.Person
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Get
import io.micronaut.scheduling.TaskExecutors
import jakarta.inject.Named
import reactor.core.publisher.Mono
import reactor.core.scheduler.Scheduler
import reactor.core.scheduler.Schedulers
import java.util.concurrent.ExecutorService

@Controller("/subscribeOn/people")
class PersonController {

    private final Scheduler scheduler
    private final PersonService personService

    PersonController(
            @Named(TaskExecutors.IO) ExecutorService executorService, // (1)
            PersonService personService) {
        this.scheduler = Schedulers.fromExecutorService(executorService)
        this.personService = personService
    }

    @Get("/{name}")
    Mono<Person> byName(String name) {
        return Mono
                .fromCallable({ -> personService.findByName(name) }) // (2)
                .subscribeOn(scheduler) // (3)
    }
}
```

| **1** | The configured I/O executor service is injected |
|---|---|
| **2** | The `Mono::fromCallable` method wraps the blocking operation |
| **3** | The Project Reactor `subscribeOn` method schedules the operation on the I/O thread pool |
