---
title: "Micronaut Core (part 9/27)"
source: https://docs.micronaut.io/latest/guide/index.html
domain: micronaut
license: CC-BY-SA-4.0
tags: micronaut framework, micronaut jvm, compile-time injection, microservices framework
fetched: 2026-07-02
part: 9/27
---

## 5.3 Method Adapter Advice

There are cases where you want to introduce a new bean based on the presence of an annotation on a method. An example of this is the @EventListener annotation which produces an implementation of ApplicationEventListener for each annotated method that invokes the annotated method.

For example the following snippet runs the logic contained within the method when the ApplicationContext starts up:

```java
import io.micronaut.context.event.StartupEvent;
import io.micronaut.runtime.event.annotation.EventListener;
...

@EventListener
void onStartup(StartupEvent event) {
    // startup logic here
}
```

The presence of the @EventListener annotation causes the Micronaut framework to create a new class that implements ApplicationEventListener and invokes the `onStartup` method defined in the bean above.

The actual implementation of the @EventListener is trivial; it simply uses the @Adapter annotation to specify which SAM (single abstract method) type it adapts:

```java
import io.micronaut.aop.Adapter;
import io.micronaut.context.event.ApplicationEventListener;
import io.micronaut.core.annotation.Indexed;

import java.lang.annotation.Documented;
import java.lang.annotation.ElementType;
import java.lang.annotation.Inherited;
import java.lang.annotation.Retention;
import java.lang.annotation.Target;

import static java.lang.annotation.RetentionPolicy.RUNTIME;

@Documented
@Retention(RUNTIME)
@Target({ElementType.ANNOTATION_TYPE, ElementType.METHOD})
@Adapter(ApplicationEventListener.class) (1)
@Indexed(ApplicationEventListener.class)
@Inherited
public @interface EventListener {
}
```

| **1** | The @Adapter annotation indicates which SAM type to adapt, in this case ApplicationEventListener. |
|---|---|

|   | The Micronaut framework also automatically aligns the generic types for the SAM interface if they are specified. |
|---|---|

Using this mechanism you can define custom annotations that use the @Adapter annotation and a SAM interface to automatically implement beans for you at compile time.


## 5.4 Bean Life Cycle Advice

Sometimes you may need to apply advice to a bean’s lifecycle. There are 3 types of advice that are applicable in this case:

- Interception of the construction of the bean
- Interception of the bean’s `@PostConstruct` invocation
- Interception of a bean’s `@PreDestroy` invocation

The Micronaut framework supports these 3 use cases by allowing the definition of additional @InterceptorBinding meta-annotations.

Consider the following annotation definition:

AroundConstruct example

```java
import io.micronaut.aop.*;
import io.micronaut.context.annotation.Prototype;
import java.lang.annotation.*;

@Retention(RetentionPolicy.RUNTIME)
@AroundConstruct // (1)
@InterceptorBinding(kind = InterceptorKind.POST_CONSTRUCT) // (2)
@InterceptorBinding(kind = InterceptorKind.PRE_DESTROY) // (3)
@Prototype // (4)
public @interface ProductBean {
}
```

AroundConstruct example

```kotlin
import io.micronaut.aop.AroundConstruct
import io.micronaut.aop.InterceptorBinding
import io.micronaut.aop.InterceptorBindingDefinitions
import io.micronaut.aop.InterceptorKind
import io.micronaut.context.annotation.Prototype

@Retention(AnnotationRetention.RUNTIME)
@AroundConstruct // (1)
@InterceptorBindingDefinitions(
    InterceptorBinding(kind = InterceptorKind.POST_CONSTRUCT), // (2)
    InterceptorBinding(kind = InterceptorKind.PRE_DESTROY) // (3)
)
@Prototype // (4)
annotation class ProductBean
```

AroundConstruct example

```groovy
import io.micronaut.aop.*
import io.micronaut.context.annotation.Prototype
import java.lang.annotation.*

@Retention(RetentionPolicy.RUNTIME)
@AroundConstruct // (1)
@InterceptorBinding(kind = InterceptorKind.POST_CONSTRUCT) // (2)
@InterceptorBinding(kind = InterceptorKind.PRE_DESTROY) // (3)
@Prototype // (4)
@interface ProductBean {
}
```

| **1** | The @AroundConstruct annotation is added to indicate that interception of the constructor should occur |
|---|---|
| **2** | An @InterceptorBinding definition is used to indicate that `@PostConstruct` interception should occur |
| **3** | An @InterceptorBinding definition is used to indicate that `@PreDestroy` interception should occur |
| **4** | The bean is defined as @Prototype so a new instance is required for each injection point |

Note that if you do not need `@PostConstruct` and `@PreDestroy` interception you can simply remove those bindings.

The `@ProductBean` annotation can then be used on the target class:

Using an AroundConstruct meta-annotation

```java
import io.micronaut.context.annotation.Parameter;

import jakarta.annotation.PreDestroy;

@ProductBean // (1)
public class Product {
    private final String productName;
    private boolean active = false;

    public Product(@Parameter String productName) { // (2)
        this.productName = productName;
    }

    public String getProductName() {
        return productName;
    }

    public boolean isActive() {
        return active;
    }

    public void setActive(boolean active) {
        this.active = active;
    }

    @PreDestroy // (3)
    void disable() {
        active = false;
    }
}
```

Using an AroundConstruct meta-annotation

```kotlin
import io.micronaut.context.annotation.Parameter
import jakarta.annotation.PreDestroy

@ProductBean // (1)
class Product(@param:Parameter val productName: String ) { // (2)

    var active: Boolean = false
    @PreDestroy
    fun disable() { // (3)
        active = false
    }
}
```

Using an AroundConstruct meta-annotation

```groovy
import io.micronaut.context.annotation.Parameter
import jakarta.annotation.PreDestroy

@ProductBean // (1)
class Product {
    final String productName
    boolean active = false

    Product(@Parameter String productName) { // (2)
        this.productName = productName
    }

    @PreDestroy // (3)
    void disable() {
        active = false
    }
}
```

| **1** | The `@ProductBean` annotation is defined on a class of type `Product` |
|---|---|
| **2** | The @Parameter annotation indicates that this bean requires an argument to complete constructions |
| **3** | Any `@PreDestroy` or `@PostConstruct` methods are executed last in the interceptor chain |

Now you can define ConstructorInterceptor beans for constructor interception and MethodInterceptor beans for `@PostConstruct` or `@PreDestroy` interception.

The following factory defines a ConstructorInterceptor that intercepts construction of `Product` instances and registers them with a hypothetical `ProductService` validating the product name first:

Defining a constructor interceptor

```java
import io.micronaut.aop.*;
import io.micronaut.context.annotation.Factory;

@Factory
public class ProductInterceptors {
    private final ProductService productService;

    public ProductInterceptors(ProductService productService) {
        this.productService = productService;
    }
}

@InterceptorBean(ProductBean.class)
ConstructorInterceptor<Product> aroundConstruct() { // (1)
    return context -> {
        final Object[] parameterValues = context.getParameterValues(); // (2)
        final Object parameterValue = parameterValues[0];
        if (parameterValue == null || parameterValues[0].toString().isEmpty()) {
            throw new IllegalArgumentException("Invalid product name");
        }
        String productName = parameterValues[0].toString().toUpperCase();
        parameterValues[0] = productName;
        final Product product = context.proceed(); // (3)
        productService.addProduct(product);
        return product;
    };
}
```

Defining a constructor interceptor

```kotlin
import io.micronaut.aop.*
import io.micronaut.context.annotation.Factory

@Factory
class ProductInterceptors(private val productService: ProductService) {
}

@InterceptorBean(ProductBean::class)
fun aroundConstruct(): ConstructorInterceptor<Product> { // (1)
    return ConstructorInterceptor { context: ConstructorInvocationContext<Product> ->
        val parameterValues = context.parameterValues // (2)
        val parameterValue = parameterValues[0]
        require(!(parameterValue == null || parameterValues[0].toString().isEmpty())) { "Invalid product name" }
        val productName = parameterValues[0].toString().uppercase()
        parameterValues[0] = productName
        val product = context.proceed() // (3)
        productService.addProduct(product)
        product
    }
}
```

Defining a constructor interceptor

```groovy
import io.micronaut.aop.*
import io.micronaut.context.annotation.Factory

@Factory
class ProductInterceptors {
    private final ProductService productService

    ProductInterceptors(ProductService productService) {
        this.productService = productService
    }
}

@InterceptorBean(ProductBean.class)
ConstructorInterceptor<Product> aroundConstruct() { // (1)
    return  { context ->
        final Object[] parameterValues = context.parameterValues // (2)
        final Object parameterValue = parameterValues[0]
        if (parameterValue == null || parameterValues[0].toString().isEmpty()) {
            throw new IllegalArgumentException("Invalid product name")
        }
        String productName = parameterValues[0].toString().toUpperCase()
        parameterValues[0] = productName
        final Product product = context.proceed() // (3)
        productService.addProduct(product)
        return product
    }
}
```

| **1** | A new @InterceptorBean is defined that is a ConstructorInterceptor |
|---|---|
| **2** | The constructor parameter values can be retrieved and modified as needed |
| **3** | The constructor can be invoked with the `proceed()` method |

Defining MethodInterceptor instances that interceptor the `@PostConstruct` and `@PreDestroy` methods is no different from defining interceptors for regular methods. Note however that you can use the passed MethodInvocationContext to identify what kind of interception is occurring and adapt the code accordingly like in the following example:

Defining a constructor interceptor

```java
@InterceptorBean(ProductBean.class) // (1)
MethodInterceptor<Product, Object> aroundInvoke() {
    return context -> {
        final Product product = context.getTarget();
        switch (context.getKind()) {
            case POST_CONSTRUCT: // (2)
                product.setActive(true);
                return context.proceed();
            case PRE_DESTROY: // (3)
                productService.removeProduct(product);
                return context.proceed();
            default:
                return context.proceed();
        }
    };
}
```

Defining a constructor interceptor

```kotlin
@InterceptorBean(ProductBean::class)
fun  aroundInvoke(): MethodInterceptor<Product, Any> { // (1)
    return MethodInterceptor { context: MethodInvocationContext<Product, Any> ->
        val product = context.target
        return@MethodInterceptor when (context.kind) {
            InterceptorKind.POST_CONSTRUCT -> { // (2)
                product.active = true
                context.proceed()
            }
            InterceptorKind.PRE_DESTROY -> { // (3)
                productService.removeProduct(product)
                context.proceed()
            }
            else -> context.proceed()
        }
    }
}
```

Defining a constructor interceptor

```groovy
@InterceptorBean(ProductBean.class) // (1)
MethodInterceptor<Product, Object> aroundInvoke() {
    return { context ->
        final Product product = context.getTarget()
        switch (context.kind) {
            case InterceptorKind.POST_CONSTRUCT: // (2)
                product.setActive(true)
                return context.proceed()
            case InterceptorKind.PRE_DESTROY: // (3)
                productService.removeProduct(product)
                return context.proceed()
            default:
                return context.proceed()
        }
    }
}
```

| **1** | A new @InterceptorBean is defined that is a MethodInterceptor |
|---|---|
| **2** | `@PostConstruct` interception is handled |
| **3** | `@PreDestroy` interception is handled |


## 5.5 Validation Advice

Validation advice is one of the most common advice types you are likely to want to use in your application.

Validation advice is built on Bean Validation JSR 380, a specification of the Java API for bean validation which ensures that the properties of a bean meet specific criteria, using `jakarta.validation` annotations such as `@NotNull`, `@Min`, and `@Max`.

The Micronaut framework provides native support for the `jakarta.validation` annotations with the `micronaut-validation` dependency:

`annotationProcessor("io.micronaut.validation:micronaut-validation-processor")` `<annotationProcessorPaths> <path> <groupId>io.micronaut.validation</groupId> <artifactId>micronaut-validation-processor</artifactId> </path> </annotationProcessorPaths>`

`implementation("io.micronaut.validation:micronaut-validation")` `<dependency> <groupId>io.micronaut.validation</groupId> <artifactId>micronaut-validation</artifactId> </dependency>`

Or full JSR 380 compliance with the `micronaut-hibernate-validator` dependency:

`implementation("io.micronaut:micronaut-hibernate-validator")` `<dependency> <groupId>io.micronaut</groupId> <artifactId>micronaut-hibernate-validator</artifactId> </dependency>`

See the section on Bean Validation for more information on how to apply validation rules to your bean classes.


## 5.6 Cache Advice

Like Spring and Grails, the Micronaut framework provides caching annotations in the io.micronaut.cache package.

The CacheManager interface allows different cache implementations to be plugged in as necessary.

The SyncCache interface provides a synchronous API for caching, whilst the AsyncCache API allows non-blocking operation.


## Cache Annotations

The following cache annotations are supported:

- @Cacheable - Indicates a method is cacheable in the specified cache
- @CachePut - Indicates that the return value of a method invocation should be cached. Unlike `@Cacheable` the original operation is never skipped.
- @CacheInvalidate - Indicates the invocation of a method should cause the invalidation of one or more caches.

Using one of these annotations activates the CacheInterceptor, which in the case of `@Cacheable` caches the return value of the method.

The emitted result is cached if the method return type is a non-blocking type (either CompletableFuture or an instance of Publisher) .

In addition, if the underlying Cache implementation supports non-blocking cache operations, cache values are read without blocking, resulting in non-blocking cache operations.


## Configuring Caches

By default, Caffeine is used to create caches from application configuration. For example:

Cache Configuration Example

```properties
micronaut.caches.my-cache.maximum-size=20
```

```yaml
micronaut:
  caches:
    my-cache:
      maximum-size: 20
```

```toml
[micronaut]
  [micronaut.caches]
    [micronaut.caches.my-cache]
      maximum-size=20
```

```groovy
micronaut {
  caches {
    myCache {
      maximumSize = 20
    }
  }
}
```

```hocon
{
  micronaut {
    caches {
      my-cache {
        maximum-size = 20
      }
    }
  }
}
```

```json
{
  "micronaut": {
    "caches": {
      "my-cache": {
        "maximum-size": 20
      }
    }
  }
}
```

The above example configures a cache called "my-cache" with a maximum size of 20.

|   | Naming Caches Define names of caches under `micronaut.caches` in kebab case (lowercase and hyphen separated); if you use camel case, the names are normalized to kebab case. For example `myCache` becomes `my-cache`. The kebab-case form must be used when referencing caches in the @Cacheable annotation. |
|---|---|

To configure a weigher to be used with the `maximumWeight` configuration, create a bean that implements `io.micronaut.caffeine.cache.Weigher`. To associate a given weigher with only a specific cache, annotate the bean with `@Named(<cache name>)`. Weighers without a named qualifier apply to all caches that don’t have a named weigher. If no beans are found, a default implementation is used.

See the configuration reference for all available configuration options.


## Dynamic Cache Creation

A DynamicCacheManager bean can be registered for use cases where caches cannot be configured ahead of time. When a cache is attempted to be retrieved that was not predefined, the dynamic cache manager is invoked to create and return a cache.

By default, if there is no other dynamic cache manager defined in the application, the Micronaut framework registers an instance of DefaultDynamicCacheManager that creates Caffeine caches with default values.


## Other Cache Implementations

Check the Micronaut Cache project for more information.


## 5.7 Retry Advice

In distributed systems and microservice environments, failure is something you have to plan for, and it is common to want to attempt to retry an operation if it fails. If first you don’t succeed try again!

With this in mind, the Micronaut framework includes a Retryable annotation.


## Retry Dependency

|   | Since Micronaut Framework 4.0 to use the Retry functionality you need to add the following dependency: |
|---|---|

`implementation("io.micronaut:micronaut-retry")` `<dependency> <groupId>io.micronaut</groupId> <artifactId>micronaut-retry</artifactId> </dependency>`


## Simple Retry

The simplest form of retry is just to add the `@Retryable` annotation to a type or method. The default behaviour of `@Retryable` is to retry three times with a linear delay of one second between each retry. (first attempt with 1s delay, second attempt with 2s delay, third attempt with 3s delay).

For example:

Simple Retry Example

```java
@Retryable
public List<Book> listBooks() {
    // ...
```

Simple Retry Example

```kotlin
@Retryable
open fun listBooks(): List<Book> {
    // ...
```

Simple Retry Example

```groovy
@Retryable
List<Book> listBooks() {
    // ...
```

With the above example if the `listBooks()` method throws an Exception, it is retried until the maximum number of attempts is reached.

The `multiplier` value of the `@Retryable` annotation can be used to configure a multiplier used to calculate the delay between retries, allowing exponential retry support.

To customize retry behaviour, set the `attempts` and `delay` members, For example to configure five attempts with a two seconds delay:

Setting Retry Attempts

```java
@Retryable(attempts = "5",
           delay = "2s")
public Book findBook(String title) {
    // ...
```

Setting Retry Attempts

```kotlin
@Retryable(attempts = "5",
           delay = "2s")
open fun findBook(title: String): Book {
    // ...
```

Setting Retry Attempts

```groovy
@Retryable(attempts = "5",
           delay = "2s")
Book findBook(String title) {
    // ...
```

Notice how both `attempts` and `delay` are defined as strings. This is to support configurability through annotation metadata. For example, you can allow the retry policy to be configured using property placeholder resolution:

Setting Retry via Configuration

```java
@Retryable(attempts = "${book.retry.attempts:3}",
           delay = "${book.retry.delay:1s}")
public Book getBook(String title) {
    // ...
```

Setting Retry via Configuration

```kotlin
@Retryable(attempts = "\${book.retry.attempts:3}",
           delay = "\${book.retry.delay:1s}")
open fun getBook(title: String): Book {
    // ...
```

Setting Retry via Configuration

```groovy
@Retryable(attempts = '${book.retry.attempts:3}',
           delay = '${book.retry.delay:1s}')
Book getBook(String title) {
    // ...
```

With the above in place, if `book.retry.attempts` is specified in configuration it is bound to the value of the `attempts` member of the `@Retryable` annotation via annotation metadata.


## Reactive Retry

`@Retryable` advice can also be applied to methods that return reactive types, such as `Publisher` (Project Reactor's `Flux` or RxJava's `Flowable`). For example:

Applying Retry Policy to Reactive Types

```java
@Retryable
public Publisher<Book> streamBooks() {
    // ...
```

Applying Retry Policy to Reactive Types

```kotlin
@Retryable
open fun streamBooks(): Flux<Book> {
    // ...
```

Applying Retry Policy to Reactive Types

```groovy
@Retryable
Flux<Book> streamBooks() {
    // ...
```

In this case `@Retryable` advice applies the retry policy to the reactive type.


## Circuit Breaker

Retry is useful in a microservice environment, but in some cases excessive retries can overwhelm the system as clients repeatedly re-attempt failing operations.

The Circuit Breaker pattern is designed to resolve this issue by allowing a certain number of failing requests and then opening a circuit that remains open for a period before allowing additional retry attempts.

The CircuitBreaker annotation is a variation of the `@Retryable` annotation that supports a `reset` member which indicates how long the circuit should remain open before it is reset (the default is 20 seconds).

Applying CircuitBreaker Advice

```java
@CircuitBreaker(reset = "30s")
public List<Book> findBooks() {
    // ...
```

Applying CircuitBreaker Advice

```kotlin
@CircuitBreaker(reset = "30s")
open fun findBooks(): List<Book> {
    // ...
```

Applying CircuitBreaker Advice

```groovy
@CircuitBreaker(reset = "30s")
List<Book> findBooks() {
    // ...
```

The above example retries the `findBooks` method three times and then opens the circuit for 30 seconds, rethrowing the original exception and preventing potential downstream traffic such as HTTP requests and I/O operations flooding the system.


## Programmatic Retry

For cases where annotations are not desirable, Micronaut Retry also provides programmatic retry creation through typed policies and injected factory beans.

Create a policy once and derive reusable operations from the injected factory:

Creating a Programmatic Retry Policy

```java
RetryPolicy retryPolicy = RetryPolicy.builder()
    .maxAttempts(5)
    .delay(Duration.ofMillis(5))
    .build();
CircuitBreakerPolicy circuitBreakerPolicy = CircuitBreakerPolicy.builder()
    .maxAttempts(3)
    .delay(Duration.ofMillis(5))
    .resetTimeout(Duration.ofMillis(100))
    .build();
```

Creating a Programmatic Retry Policy

```kotlin
val retryPolicy = RetryPolicy.builder()
    .maxAttempts(5)
    .delay(Duration.ofMillis(5))
    .build()
val circuitBreakerPolicy = CircuitBreakerPolicy.builder()
    .maxAttempts(3)
    .delay(Duration.ofMillis(5))
    .resetTimeout(Duration.ofMillis(100))
    .build()
```

Creating a Programmatic Retry Policy

```groovy
RetryPolicy retryPolicy = RetryPolicy.builder()
    .maxAttempts(5)
    .delay(Duration.ofMillis(5))
    .build()
CircuitBreakerPolicy circuitBreakerPolicy = CircuitBreakerPolicy.builder()
    .maxAttempts(3)
    .delay(Duration.ofMillis(5))
    .resetTimeout(Duration.ofMillis(100))
    .build()
```

The programmatic API uses typed values such as `Duration` and `int` instead of annotation strings.

For synchronous work, execute the supplier directly through `RetryOperations`:

Programmatic Retry for Synchronous Code

```java
public List<Book> listBooks() {
    return retryOperations.execute(() -> {
        if (syncCounter.incrementAndGet() < 3) {
            throw new IllegalStateException("Temporary failure");
        }
        return Collections.singletonList(new Book("The Stand"));
    });
}
```

Programmatic Retry for Synchronous Code

```kotlin
open fun listBooks(): List<Book> = retryOperations.execute {
    if (syncCounter.incrementAndGet() < 3) {
        throw IllegalStateException("Temporary failure")
    }
    listOf(Book("The Stand"))
}
```

Programmatic Retry for Synchronous Code

```groovy
List<Book> listBooks() {
    retryOperations.execute {
        if (syncCounter.incrementAndGet() < 3) {
            throw new IllegalStateException('Temporary failure')
        }
        [new Book('The Stand')]
    }
}
```

Reactive retry is also supported. Pass a supplier so each retry attempt creates a fresh `Publisher`:

Programmatic Retry for Reactive Code

```java
public Publisher<Book> streamBooks() {
    return retryOperations.executePublisher(() -> Flux.defer(() -> {
        if (reactiveCounter.incrementAndGet() < 3) {
            return Flux.error(new IllegalStateException("Temporary failure"));
        }
        return Flux.just(new Book("The Stand"));
    }));
}
```

Programmatic Retry for Reactive Code

```kotlin
open fun streamBooks(): Publisher<Book> = retryOperations.executePublisher {
    Flux.defer {
        if (reactiveCounter.incrementAndGet() < 3) {
            Flux.error(IllegalStateException("Temporary failure"))
        } else {
            Flux.just(Book("The Stand"))
        }
    }
}
```

Programmatic Retry for Reactive Code

```groovy
Publisher<Book> streamBooks() {
    retryOperations.executePublisher {
        Flux.defer {
            if (reactiveCounter.incrementAndGet() < 3) {
                Flux.error(new IllegalStateException('Temporary failure'))
            } else {
                Flux.just(new Book('The Stand'))
            }
        }
    }
}
```

For asynchronous work, pass a supplier that creates a new `CompletionStage` for each attempt:

Programmatic Retry for Asynchronous Code

```java
public CompletionStage<Book> findBook(String title) {
    return retryOperations.executeCompletionStage(() -> CompletableFuture.supplyAsync(() -> {
        if (asyncCounter.incrementAndGet() < 3) {
            throw new IllegalStateException("Temporary failure");
        }
        return new Book(title);
    }));
}
```

Programmatic Retry for Asynchronous Code

```kotlin
open fun findBook(title: String): CompletionStage<Book> = retryOperations.executeCompletionStage {
    CompletableFuture.supplyAsync {
        if (asyncCounter.incrementAndGet() < 3) {
            throw IllegalStateException("Temporary failure")
        }
        Book(title)
    }
}
```

Programmatic Retry for Asynchronous Code

```groovy
CompletionStage<Book> findBook(String title) {
    retryOperations.executeCompletionStage {
        CompletableFuture.supplyAsync {
            if (asyncCounter.incrementAndGet() < 3) {
                throw new IllegalStateException('Temporary failure')
            }
            new Book(title)
        }
    }
}
```


## Programmatic Circuit Breaker

Programmatic circuit breakers are created in the same way, using a typed `CircuitBreakerPolicy` and an injected `CircuitBreakerOperationsFactory`. The resulting `CircuitBreakerOperations` instance owns the shared breaker state.

Programmatic Circuit Breaker

```java
public Book findBookWithCircuitBreaker(String title) {
    return circuitBreakerOperations.execute(() -> {
        if (circuitCounter.incrementAndGet() < 4) {
            throw new IllegalStateException("Circuit failure");
        }
        return new Book(title);
    });
}
```

Programmatic Circuit Breaker

```kotlin
open fun findBookWithCircuitBreaker(title: String): Book = circuitBreakerOperations.execute {
    if (circuitCounter.incrementAndGet() < 4) {
        throw IllegalStateException("Circuit failure")
    }
    Book(title)
}
```

Programmatic Circuit Breaker

```groovy
Book findBookWithCircuitBreaker(String title) {
    circuitBreakerOperations.execute {
        if (circuitCounter.incrementAndGet() < 4) {
            throw new IllegalStateException('Circuit failure')
        }
        new Book(title)
    }
}
```


## Factory Bean Retry

When @Retryable is applied to bean factory methods, it behaves as if the annotation was placed on the type being returned. The retry behavior applies when the methods on the returned object are invoked. Note that the bean factory method itself is **not** retried. If you want the functionality of creating the bean to be retried, it should be delegated to another singleton that has the @Retryable annotation applied.

For example:

```java
@Factory (1)
public class Neo4jDriverFactory {
    ...
    @Retryable(ServiceUnavailableException.class) (2)
    @Bean(preDestroy = "close")
    public Driver buildDriver() {
        ...
    }
}
```

| **1** | A factory bean is created that defines methods that create beans |
|---|---|
| **2** | The @Retryable annotation is used to catch exceptions thrown from methods executed on the `Driver`. |


## Retry Events

You can register RetryEventListener instances as beans to listen for RetryEvent events that are published every time an operation is retried.

In addition, you can register event listeners for CircuitOpenEvent to be notified when a circuit breaker circuit is opened, or CircuitClosedEvent for when a circuit is closed.


## 5.8 Scheduled Tasks

Like Spring and Grails, the Micronaut framework features a Scheduled annotation for scheduling background tasks.

|   | See the guide for Schedule Periodic Tasks inside your Micronaut Applications to learn more. |
|---|---|


## Using the @Scheduled Annotation

The Scheduled annotation can be added to any method of a bean, and you should set one of the `fixedRate`, `fixedDelay`, or `cron` members. Scheduling requires the Micronaut Context dependency:

`implementation("io.micronaut:micronaut-context")` `<dependency> <groupId>io.micronaut</groupId> <artifactId>micronaut-context</artifactId> </dependency>`

`micronaut-context` is a transitive dependency of `micronaut-http`. If you use a Micronaut HTTP runtime, your project already includes the `Micronaut-context` dependency.

|   | Remember that the scope of a bean impacts behaviour. A `@Singleton` bean shares state (the fields of the instance) each time the scheduled method is executed, while for a `@Prototype` bean a new instance is created for each execution. |
|---|---|

### Scheduling at a Fixed Rate

To schedule a task at a fixed rate, use the `fixedRate` member. For example:

Fixed Rate Example

```java
@Scheduled(fixedRate = "5m")
void everyFiveMinutes() {
    System.out.println("Executing everyFiveMinutes()");
}
```

Fixed Rate Example

```kotlin
@Scheduled(fixedRate = "5m")
internal fun everyFiveMinutes() {
    println("Executing everyFiveMinutes()")
}
```

Fixed Rate Example

```groovy
@Scheduled(fixedRate = "5m")
void everyFiveMinutes() {
    println "Executing everyFiveMinutes()"
}
```

The task above executes every five minutes.

### Scheduling with a Fixed Delay

To schedule a task, so it runs five minutes after the termination of the previous task use the `fixedDelay` member. For example:

Fixed Delay Example

```java
@Scheduled(fixedDelay = "5m")
void fiveMinutesAfterLastExecution() {
    System.out.println("Executing fiveMinutesAfterLastExecution()");
}
```

Fixed Delay Example

```kotlin
@Scheduled(fixedDelay = "5m")
internal fun fiveMinutesAfterLastExecution() {
    println("Executing fiveMinutesAfterLastExecution()")
}
```

Fixed Delay Example

```groovy
@Scheduled(fixedDelay = "5m")
void fiveMinutesAfterLastExecution() {
    println "Executing fiveMinutesAfterLastExecution()"
}
```

### Scheduling a Cron Task

To schedule a Cron task use the `cron` member:

Cron Example

```java
@Scheduled(cron = "0 15 10 ? * MON")
void everyMondayAtTenFifteenAm() {
    System.out.println("Executing everyMondayAtTenFifteenAm()");
}
```

Cron Example

```kotlin
@Scheduled(cron = "0 15 10 ? * MON")
internal fun everyMondayAtTenFifteenAm() {
    println("Executing everyMondayAtTenFifteenAm()")
}
```

Cron Example

```groovy
@Scheduled(cron = "0 15 10 ? * MON")
void everyMondayAtTenFifteenAm() {
    println "Executing everyMondayAtTenFifteenAm()"
}
```

The above example runs the task every Monday morning at 10:15AM in the time zone of the server.

### Scheduling with only an Initial Delay

To schedule a task, so it runs once after the server starts, use the `initialDelay` member:

Initial Delay Example

```java
@Scheduled(initialDelay = "1m")
void onceOneMinuteAfterStartup() {
    System.out.println("Executing onceOneMinuteAfterStartup()");
}
```

Initial Delay Example

```kotlin
@Scheduled(initialDelay = "1m")
internal fun onceOneMinuteAfterStartup() {
    println("Executing onceOneMinuteAfterStartup()")
}
```

Initial Delay Example

```groovy
@Scheduled(initialDelay = "1m")
void onceOneMinuteAfterStartup() {
    println "Executing onceOneMinuteAfterStartup()"
}
```

The above example only runs once, one minute after the server starts.


## Programmatically Scheduling Tasks

To programmatically schedule tasks, use the TaskScheduler bean which can be injected as follows:

```java
@Inject
@Named(TaskExecutors.SCHEDULED)
TaskScheduler taskScheduler;
```

```kotlin
@Inject
@Named(TaskExecutors.SCHEDULED)
lateinit var taskScheduler: TaskScheduler
```

```groovy
@Inject
@Named(TaskExecutors.SCHEDULED)
TaskScheduler taskScheduler
```

To make your application’s tasks configurable, you can use annotation metadata and property placeholder configuration. For example:

Allow tasks to be configured

```java
@Scheduled(fixedRate = "${my.task.rate:5m}",
        initialDelay = "${my.task.delay:1m}")
void configuredTask() {
    System.out.println("Executing configuredTask()");
}
```

Allow tasks to be configured

```kotlin
@Scheduled(fixedRate = "\${my.task.rate:5m}",
        initialDelay = "\${my.task.delay:1m}")
internal fun configuredTask() {
    println("Executing configuredTask()")
}
```

Allow tasks to be configured

```groovy
@Scheduled(fixedRate = '${my.task.rate:5m}',
        initialDelay = '${my.task.delay:1m}')
void configuredTask() {
    println "Executing configuredTask()"
}
```

The above example allows the task execution frequency to be configured with the property `my.task.rate`, and the initial delay to be configured with the property `my.task.delay`.


## Configuring the Scheduled Task Thread Pool

Tasks executed by `@Scheduled` are run by default on a ScheduledExecutorService configured to have twice the number of threads as available processors.

You can configure this thread pool in your configuration file (e.g `application.yml`):

Configuring Scheduled Task Thread Pool

```properties
micronaut.executors.scheduled.type=scheduled
micronaut.executors.scheduled.core-pool-size=30
```

```yaml
micronaut:
  executors:
    scheduled:
      type: scheduled
      core-pool-size: 30
```

```toml
[micronaut]
  [micronaut.executors]
    [micronaut.executors.scheduled]
      type="scheduled"
      core-pool-size=30
```

```groovy
micronaut {
  executors {
    scheduled {
      type = "scheduled"
      corePoolSize = 30
    }
  }
}
```

```hocon
{
  micronaut {
    executors {
      scheduled {
        type = "scheduled"
        core-pool-size = 30
      }
    }
  }
}
```

```json
{
  "micronaut": {
    "executors": {
      "scheduled": {
        "type": "scheduled",
        "core-pool-size": 30
      }
    }
  }
}
```

🔗

| Property | Type | Description | Default value |
|---|---|---|---|
| `micronaut.executors.*.n-threads` | java.lang.Integer | number of threads |   |
| `micronaut.executors.*.type` | ExecutorType | the type |   |
| `micronaut.executors.*.parallelism` | java.lang.Integer | the parallelism |   |
| `micronaut.executors.*.core-pool-size` | java.lang.Integer | the core pool size |   |
| `micronaut.executors.*.virtual` | java.lang.Boolean | whether to use virtual threads |   |
| `micronaut.executors.*.thread-factory-class` | java.lang.Class | the thread factory class |   |
| `micronaut.executors.*.name` | java.lang.String | Sets the executor name. |   |
| `micronaut.executors.*.number-of-threads` | java.lang.Integer | Sets the number of threads for FIXED. Default value (2 * Number of processors available to the Java virtual machine). |   |


## Handling Exceptions

By default, the Micronaut framework includes a DefaultTaskExceptionHandler bean that implements the TaskExceptionHandler interface and simply logs the exception if an error occurs invoking a scheduled task.

If you have custom requirements you can replace this bean with your own implementation (for example to send an email or shutdown the context to fail fast). To do so, write your own TaskExceptionHandler and annotate it with `@Replaces(DefaultTaskExceptionHandler.class)`.


## 5.9 Bridging Spring AOP

Although the Micronaut framework’s design is based on a compile-time approach and does not rely on Spring dependency injection, there is still a lot of value in the Spring ecosystem that does not depend directly on the Spring container.

You may wish to use existing Spring projects within the Micronaut framework and configure beans to be used within the Micronaut framework.

You may also wish to leverage existing AOP advice from Spring. One example of this is Spring’s support for declarative transactions with `@Transactional`.

The Micronaut framework provides support for Spring-based transaction management without requiring Spring itself. Simply add the `spring` module to your application dependencies:

`implementation("io.micronaut.spring:micronaut-spring")` `<dependency> <groupId>io.micronaut.spring</groupId> <artifactId>micronaut-spring</artifactId> </dependency>`

This also requires adding the `spring-annotation` module dependency as an annotation processor:

`annotationProcessor("io.micronaut.spring:micronaut-spring-annotation")` `<annotationProcessorPaths> <path> <groupId>io.micronaut.spring</groupId> <artifactId>micronaut-spring-annotation</artifactId> </path> </annotationProcessorPaths>`

|   | If you use Micronaut’s Hibernate support you already get this dependency and a `HibernateTransactionManager` is configured for you. |
|---|---|

This is done by intercepting method calls annotated with Spring’s `@Transactional` with TransactionInterceptor.

The benefit here is you can use Micronaut’s compile-time, reflection-free AOP to declare programmatic Spring transactions. For example:

Using @Transactional

```java
import org.springframework.transaction.annotation.Transactional;
...

@Transactional
public Book saveBook(String title) {
    ...
}
```

# 6 The HTTP Server

|   | Using the CLI If you create your project using the Micronaut CLI `create-app` command, the `http-server` dependency is included by default. |
|---|---|

Micronaut framework includes both non-blocking HTTP server and client APIs based on Netty.

The goal of the HTTP server is to make it as easy as possible to expose services to be consumed by HTTP clients and web pages, regardless of the language they are written in. There is support for rendering HTML from a variety of templating frameworks in the Micronaut Views module. To use the HTTP server you need the `http-server-netty` dependency in your build:

`implementation("io.micronaut:micronaut-http-server-netty")` `<dependency> <groupId>io.micronaut</groupId> <artifactId>micronaut-http-server-netty</artifactId> </dependency>`

A "Hello World" server application can be seen below:

```java
import io.micronaut.http.MediaType;
import io.micronaut.http.annotation.Controller;
import io.micronaut.http.annotation.Get;

@Controller("/hello") // (1)
public class HelloController {

    @Get(produces = MediaType.TEXT_PLAIN) // (2)
    public String index() {
        return "Hello World"; // (3)
    }
}
```

```kotlin
import io.micronaut.http.MediaType
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Get

@Controller("/hello") // (1)
class HelloController {

    @Get(produces = [MediaType.TEXT_PLAIN]) // (2)
    fun index(): String {
        return "Hello World" // (3)
    }
}
```

```groovy
import io.micronaut.http.MediaType
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Get

@Controller('/hello') // (1)
class HelloController {

    @Get(produces = MediaType.TEXT_PLAIN) // (2)
    String index() {
        'Hello World' // (3)
    }
}
```

| **1** | The class is defined as a controller with the @Controller annotation mapped to the path `/hello` |
|---|---|
| **2** | The method responds to a GET requests to `/hello` and returns a response with a `text/plain` content type |
| **3** | By defining a method named `index`, by convention the method is exposed via the `/hello` URI |


## 6.1 Running the Embedded Server

To run the server, create an `Application` class with a `static void main` method, for example:

Micronaut Application Class

```java
import io.micronaut.runtime.Micronaut;

public class Application {

    public static void main(String[] args) {
        Micronaut.run(Application.class);
    }
}
```

Micronaut Application Class

```kotlin
import io.micronaut.runtime.Micronaut

object Application {

    @JvmStatic
    fun main(args: Array<String>) {
        Micronaut.run(Application.javaClass)
    }
}
```

Micronaut Application Class

```groovy
import io.micronaut.runtime.Micronaut

class Application {

    static void main(String... args) {
        Micronaut.run Application
    }
}
```

To run the application from a unit test, use the EmbeddedServer interface:

Micronaut Test Case

```java
import io.micronaut.http.HttpRequest;
import io.micronaut.http.client.HttpClient;
import io.micronaut.http.client.annotation.Client;
import io.micronaut.runtime.server.EmbeddedServer;
import io.micronaut.test.extensions.junit5.annotation.MicronautTest;
import org.junit.jupiter.api.Test;

import jakarta.inject.Inject;

import static org.junit.jupiter.api.Assertions.assertEquals;

@MicronautTest
public class HelloControllerSpec {

    @Inject
    EmbeddedServer server; // (1)

    @Inject
    @Client("/")
    HttpClient client; // (2)

    @Test
    void testHelloWorldResponse() {
        String response = client.toBlocking() // (3)
                .retrieve(HttpRequest.GET("/hello"));
        assertEquals("Hello World", response); // (4)
    }
}
```

Micronaut Test Case

```kotlin
import io.micronaut.http.client.HttpClient
import io.micronaut.http.client.annotation.Client
import io.micronaut.runtime.server.EmbeddedServer
import io.micronaut.test.extensions.junit5.annotation.MicronautTest
import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.Test
import jakarta.inject.Inject

@MicronautTest
class HelloControllerSpec {

    @Inject
    lateinit var server: EmbeddedServer // (1)

    @Inject
    @field:Client("/")
    lateinit var client: HttpClient // (2)

    @Test
    fun testHelloWorldResponse() {
        val rsp: String = client.toBlocking() // (3)
                .retrieve("/hello")
        assertEquals("Hello World", rsp) // (4)
    }
}
```

Micronaut Test Case

```groovy
import io.micronaut.http.HttpRequest
import io.micronaut.http.client.HttpClient
import io.micronaut.http.client.annotation.Client
import io.micronaut.runtime.server.EmbeddedServer
import io.micronaut.test.extensions.spock.annotation.MicronautTest
import spock.lang.Specification

import jakarta.inject.Inject

@MicronautTest
class HelloControllerSpec extends Specification {

    @Inject
    EmbeddedServer embeddedServer // (1)

    @Inject
    @Client("/")
    HttpClient client // (2)

    void "test hello world response"() {
        expect:
            client.toBlocking() // (3)
                    .retrieve(HttpRequest.GET('/hello')) == "Hello World" // (4)
    }
}
```

| **1** | The `EmbeddedServer` is run and the Spock `@AutoCleanup` annotation ensures the server is stopped after the specification completes. |
|---|---|
| **2** | The `EmbeddedServer` interface provides the `URL` of the server under test which runs on a random port. |
| **3** | The test uses the Micronaut HTTP client to make the call |
| **4** | The `retrieve` method returns the response of the controller as a `String` |

|   | Without explicit port configuration, the port will be 8080, unless the application is run under the `test` environment where the port is random. When the application context starts from the context of a test class, the test environment is added automatically. |
|---|---|


## 6.2 Running Server on a Specific Port

By default, the server runs on port 8080. However, you can set the server to run on a specific port:

```properties
micronaut.server.port=8086
```

```yaml
micronaut:
  server:
    port: 8086
```

```toml
[micronaut]
  [micronaut.server]
    port=8086
```

```groovy
micronaut {
  server {
    port = 8086
  }
}
```

```hocon
{
  micronaut {
    server {
      port = 8086
    }
  }
}
```

```json
{
  "micronaut": {
    "server": {
      "port": 8086
    }
  }
}
```

|   | This is also configurable from an environment variable, e.g. `MICRONAUT_SERVER_PORT=8086` |
|---|---|

To run on a random port:

```properties
micronaut.server.port=-1
```

```yaml
micronaut:
  server:
    port: -1
```

```toml
[micronaut]
  [micronaut.server]
    port=-1
```

```groovy
micronaut {
  server {
    port = -1
  }
}
```

```hocon
{
  micronaut {
    server {
      port = -1
    }
  }
}
```

```json
{
  "micronaut": {
    "server": {
      "port": -1
    }
  }
}
```

|   | Setting an explicit port may cause tests to fail if multiple servers start simultaneously on the same port. To prevent that, specify a random port in the test environment configuration. |
|---|---|


## 6.3 HTTP Routing

The @Controller annotation used in the previous section is one of several annotations that allow you to control the construction of HTTP routes.


## URI Paths

The value of the `@Controller` annotation is an RFC-6570 URI template, so you can embed URI variables within the path using the syntax defined by the URI template specification.

|   | Many other frameworks, including Spring, implement the URI template specification |
|---|---|

The actual implementation is handled by the UriMatchTemplate class, which extends UriTemplate.

You can use this class in your applications to build URIs, for example:

Using a UriTemplate

```java
UriMatchTemplate template = UriMatchTemplate.of("/hello/{name}");

assertTrue(template.match("/hello/John").isPresent()); // (1)
assertEquals("/hello/John", template.expand( // (2)
        Collections.singletonMap("name", "John")
));
```

Using a UriTemplate

```kotlin
val template = UriMatchTemplate.of("/hello/{name}")

template.match("/hello/John").isPresent.shouldBeTrue() // (1)
template.expand(mapOf("name" to "John")) shouldBe "/hello/John"  // (2)
```

Using a UriTemplate

```groovy
given:
UriMatchTemplate template = UriMatchTemplate.of("/hello/{name}")

expect:
template.match("/hello/John").isPresent() // (1)
template.expand(["name": "John"]) == "/hello/John" // (2)
```

| **1** | Use the `match` method to match a path |
|---|---|
| **2** | Use the `expand` method to expand a template into a URI |

You can use UriTemplate to build paths to include in your responses.
