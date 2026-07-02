---
title: "Micronaut Core (part 3/27)"
source: https://docs.micronaut.io/latest/guide/index.html
domain: micronaut
license: CC-BY-SA-4.0
tags: micronaut framework, micronaut jvm, compile-time injection, microservices framework
fetched: 2026-07-02
part: 3/27
---

## Configuration Requirements

The @Requires annotation is very flexible and can be used for a variety of use cases. The following table summarizes some possibilities:

| Requirement | Example |
|---|---|
| Require the presence of one or more classes | `@Requires(classes=javax.servlet.Servlet)` |
| Require the absence of one or more classes | `@Requires(missing=javax.servlet.Servlet)` |
| Require the presence one or more beans | `@Requires(beans=javax.sql.DataSource)` |
| Require the absence of one or more beans | `@Requires(missingBeans=javax.sql.DataSource)` |
| Require the environment to be applied | `@Requires(env="test")` |
| Require the environment to not be applied | `@Requires(notEnv="test")` |
| Require the presence of another configuration package | `@Requires(configuration="foo.bar")` |
| Require the absence of another configuration package | `@Requires(missingConfigurations="foo.bar")` |
| Require particular SDK version | `@Requires(sdk=Sdk.JAVA, value="1.8")` |
| Requires classes annotated with the given annotations to be available to the application via package scanning | `@Requires(entities=javax.persistence.Entity)` |
| Require a property with an optional value | `@Requires(property="data-source.url")` |
| Require a property to not be part of the configuration | `@Requires(missingProperty="data-source.url")` |
| Require the presence of one or more files in the file system | `@Requires(resources="file:/path/to/file")` |
| Require the presence of one or more classpath resources | `@Requires(resources="classpath:myFile.properties")` |
| Require the current operating system to be in the list | `@Requires(os={Requires.Family.WINDOWS})` |
| Require the current operating system to **not** be in the list | `@Requires(notOs={Requires.Family.WINDOWS})` |
| Requires bean to be present in case no beanProperty specified | `@Requires(bean=Config.class)` |
| Requires the specified property of bean to be present | `@Requires(bean=Config.class, beanProperty="enabled")` |

### Additional Notes on Property Requirements.

Adding a requirement on a property has some additional functionality. You can require the property to be a certain value, not be a certain value, and use a default in those checks if it is not set.

```java
@Requires(property="foo") (1)
@Requires(property="foo", value="John") (2)
@Requires(property="foo", value="John", defaultValue="John") (3)
@Requires(property="foo", notEquals="Sally") (4)
```

| **1** | Requires the property to be set |
|---|---|
| **2** | Requires the property to be "John" |
| **3** | Requires the property to be "John" or not set |
| **4** | Requires the property to not be "Sally" or not set |

### Referencing bean properties in @Requires.

You can also reference other beans properties in `@Requires` to conditionally load beans. Similar to `property` requirements, you can specify required `value` or set the value bean property should not be equal to using `notEquals` annotation member. For the bean property to be checked, the bean of type specified in `bean` annotation member should be present within context, otherwise conditional bean will not be loaded.

```java
@Requires(bean=Config.class, beanProperty="foo") (1)
@Requires(bean=Config.class, beanProperty="foo", value="John") (2)
@Requires(bean=Config.class, beanProperty="foo", notEquals="Sally") (3)
```

| **1** | Requires the "foo" property on `Config` bean to be set |
|---|---|
| **2** | Requires the "foo" property on `Config` bean to be "John" |
| **3** | Requires the "foo" property on `Config` bean to not be "Sally" or not set |

Specified bean property is accessed through respective getter method whose presence and availability will be checked at compilation time.

Note that bean property is considered to be present in case it’s value is not null. Keep in mind that primitive properties are initialized with default values such as `false` for boolean and `0` for int, so they are considered to be set even if no value is explicitly specified for them.


## Debugging Conditional Beans

If you have multiple conditions and complex requirements it may become difficult to understand why a particular bean has not been loaded.

To help resolve issues with conditional beans you can enable debug logging for the `io.micronaut.context.condition` package which will log the reasons why beans were not loaded.

logback.xml

```xml
<logger name="io.micronaut.context.condition" level="DEBUG"/>
```

Consult the logging chapter for details howto setup logging.


## 3.12 Bean Replacement

One significant difference between Micronaut’s Dependency Injection system and Spring’s is the way beans are replaced.

In a Spring application, beans have names and are overridden by creating a bean with the same name, regardless of the type of the bean. Spring also has the notion of bean registration order, hence in Spring Boot you have `@AutoConfigureBefore` and `@AutoConfigureAfter` annotations that control how beans override each other.

This strategy leads to problems that are difficult to debug, for example:

- Bean loading order changes, leading to unexpected results
- A bean with the same name overrides another bean with a different type

To avoid these problems, Micronaut’s DI has no concept of bean names or load order. Beans have a type and a Qualifier. You cannot override a bean of a completely different type with another.

A useful benefit of Spring’s approach is that it allows overriding existing beans to customize behaviour. To support the same ability, Micronaut’s DI provides an explicit @Replaces annotation, which integrates nicely with support for Conditional Beans and clearly documents and expresses the intention of the developer.

Any existing bean can be replaced by another bean that declares @Replaces. For example, consider the following class:

JdbcBookService

```java
@Singleton
@Requires(beans = DataSource.class)
@Requires(property = "datasource.url")
public class JdbcBookService implements BookService {

    DataSource dataSource;

    public JdbcBookService(DataSource dataSource) {
        this.dataSource = dataSource;
    }
```

JdbcBookService

```kotlin
@Singleton
@Requirements(Requires(beans = [DataSource::class]), Requires(property = "datasource.url"))
class JdbcBookService(internal var dataSource: DataSource) : BookService {
```

JdbcBookService

```groovy
@Singleton
@Requires(beans = DataSource)
@Requires(property = "datasource.url")
class JdbcBookService implements BookService {

    DataSource dataSource
```

You can define a class in `src/test/java` that replaces this class just for your tests:

Using @Replaces

```java
@Replaces(JdbcBookService.class) // (1)
@Singleton
public class MockBookService implements BookService {

    Map<String, Book> bookMap = new LinkedHashMap<>();

    @Override
    public Book findBook(String title) {
        return bookMap.get(title);
    }
}
```

Using @Replaces

```kotlin
@Replaces(JdbcBookService::class) // (1)
@Singleton
class MockBookService : BookService {

    var bookMap: Map<String, Book> = LinkedHashMap()

    override fun findBook(title: String): Book? {
        return bookMap[title]
    }
}
```

Using @Replaces

```groovy
@Replaces(JdbcBookService.class) // (1)
@Singleton
class MockBookService implements BookService {

    Map<String, Book> bookMap = [:]

    @Override
    Book findBook(String title) {
        bookMap.get(title)
    }
}
```

| **1** | The `MockBookService` declares that it replaces `JdbcBookService` |
|---|---|

### Factory Replacement

The `@Replaces` annotation also supports a `factory` argument. That argument allows the replacement of factory beans in their entirety or specific types created by the factory.

For example, it may be desired to replace all or part of the given factory class:

BookFactory

```java
@Factory
public class BookFactory {

    @Singleton
    Book novel() {
        return new Book("A Great Novel");
    }

    @Singleton
    TextBook textBook() {
        return new TextBook("Learning 101");
    }
}
```

BookFactory

```kotlin
@Factory
class BookFactory {

    @Singleton
    internal fun novel(): Book {
        return Book("A Great Novel")
    }

    @Singleton
    internal fun textBook(): TextBook {
        return TextBook("Learning 101")
    }
}
```

BookFactory

```groovy
@Factory
class BookFactory {

    @Singleton
    Book novel() {
        new Book('A Great Novel')
    }

    @Singleton
    TextBook textBook() {
        new TextBook('Learning 101')
    }
}
```

|   | To replace a factory entirely, your factory methods must match the return types of all methods in the replaced factory. |
|---|---|

In this example, `BookFactory#textBook()` is **not** replaced because this factory does not have a factory method that returns a `TextBook`.

CustomBookFactory

```java
@Factory
@Replaces(factory = BookFactory.class)
public class CustomBookFactory {

    @Singleton
    Book otherNovel() {
        return new Book("An OK Novel");
    }
}
```

CustomBookFactory

```kotlin
@Factory
@Replaces(factory = BookFactory::class)
class CustomBookFactory {

    @Singleton
    internal fun otherNovel(): Book {
        return Book("An OK Novel")
    }
}
```

CustomBookFactory

```groovy
@Factory
@Replaces(factory = BookFactory)
class CustomBookFactory {

    @Singleton
    Book otherNovel() {
        new Book('An OK Novel')
    }
}
```

To replace one or more factory methods but retain the rest, apply the `@Replaces` annotation on the method(s) and denote the factory to apply to.

TextBookFactory

```java
@Factory
public class TextBookFactory {

    @Singleton
    @Replaces(value = TextBook.class, factory = BookFactory.class)
    TextBook textBook() {
        return new TextBook("Learning 305");
    }
}
```

TextBookFactory

```kotlin
@Factory
class TextBookFactory {

    @Singleton
    @Replaces(value = TextBook::class, factory = BookFactory::class)
    internal fun textBook(): TextBook {
        return TextBook("Learning 305")
    }
}
```

TextBookFactory

```groovy
@Factory
class TextBookFactory {

    @Singleton
    @Replaces(value = TextBook, factory = BookFactory)
    TextBook textBook() {
        new TextBook('Learning 305')
    }
}
```

The `BookFactory#novel()` method will not be replaced because the TextBook class is defined in the annotation.

### Default Implementation

When exposing an API, you may want to define an implementation of the interface that is used as the default when injecting a particular interface. For this you can use the @DefaultImplementation annotation.

It may also be desirable to not expose the default implementation of an interface as part of the public API by making it package private in Java.

Doing so prevents users from being able to replace the implementation because they will not be able to reference the class.

The @DefaultImplementation annotation allows the framework to establish the implementation to replace if a user creates a bean that declares `@Replaces(YourInterface.class)`.

For example consider:

A public API contract

```java
import io.micronaut.context.annotation.DefaultImplementation;

@DefaultImplementation(DefaultResponseStrategy.class)
public interface ResponseStrategy {
}
```

```kotlin
import io.micronaut.context.annotation.DefaultImplementation

@DefaultImplementation(DefaultResponseStrategy::class)
interface ResponseStrategy
```

```groovy
import io.micronaut.context.annotation.DefaultImplementation

@DefaultImplementation(DefaultResponseStrategy)
interface ResponseStrategy {
}
```

The default implementation

```java
import jakarta.inject.Singleton;

@Singleton
class DefaultResponseStrategy implements ResponseStrategy {

}
```

```kotlin
import jakarta.inject.Singleton

@Singleton
internal class DefaultResponseStrategy : ResponseStrategy
```

```groovy
import jakarta.inject.Singleton

@Singleton
class DefaultResponseStrategy implements ResponseStrategy {

}
```

The custom implementation

```java
import io.micronaut.context.annotation.Replaces;
import jakarta.inject.Singleton;

@Singleton
@Replaces(ResponseStrategy.class)
public class CustomResponseStrategy implements ResponseStrategy {

}
```

```kotlin
import io.micronaut.context.annotation.Replaces
import jakarta.inject.Singleton

@Singleton
@Replaces(ResponseStrategy::class)
class CustomResponseStrategy : ResponseStrategy
```

```groovy
import io.micronaut.context.annotation.Replaces
import jakarta.inject.Singleton

@Singleton
@Replaces(ResponseStrategy)
class CustomResponseStrategy implements ResponseStrategy {

}
```

In the above example, the `CustomResponseStrategy` replaces the `DefaultResponseStrategy` because the DefaultImplementation annotation points to the `DefaultResponseStrategy`.


## 3.13 Bean Configurations

A bean @Configuration is a grouping of multiple bean definitions within a package.

The `@Configuration` annotation is applied at the package level and informs the Micronaut framework that the beans defined with the package form a logical grouping.

The `@Configuration` annotation is typically applied to `package-info` classes. For example:

package-info.groovy

```groovy
@Configuration
package my.package

import io.micronaut.context.annotation.Configuration
```

Where this grouping becomes useful is when the bean configuration is made conditional via the `@Requires` annotation. For example:

package-info.groovy

```groovy
@Configuration
@Requires(beans = javax.sql.DataSource)
package my.package
```

In the above example, all bean definitions within the annotated package are only loaded and made available if a `javax.sql.DataSource` bean is present. This lets you implement conditional autoconfiguration of bean definitions.

|   | Java and Kotlin also support this functionality via `package-info.java`. Kotlin does not support a `package-info.kt` as of version 1.3. |
|---|---|


## 3.14 Life-Cycle Methods


## When The Bean Is Constructed

To invoke a method when the bean is constructed, use the `jakarta.annotation.PostConstruct` annotation:

```java
import jakarta.annotation.PostConstruct; // (1)
import jakarta.inject.Singleton;

@Singleton
public class V8Engine implements Engine {

    private int cylinders = 8;
    private boolean initialized = false; // (2)

    @Override
    public String start() {
        if (!initialized) {
            throw new IllegalStateException("Engine not initialized!");
        }

        return "Starting V8";
    }

    @Override
    public int getCylinders() {
        return cylinders;
    }

    public boolean isInitialized() {
        return initialized;
    }

    @PostConstruct // (3)
    public void initialize() {
        initialized = true;
    }
}
```

```kotlin
import jakarta.annotation.PostConstruct
import jakarta.inject.Singleton

@Singleton
class V8Engine : Engine {

    override val cylinders = 8

    var initialized = false
        private set // (2)

    override fun start(): String {
        check(initialized) { "Engine not initialized!" }

        return "Starting V8"
    }

    @PostConstruct // (3)
    fun initialize() {
        initialized = true
    }
}
```

```groovy
import jakarta.annotation.PostConstruct // (1)
import jakarta.inject.Singleton

@Singleton
class V8Engine implements Engine {

    int cylinders = 8
    boolean initialized = false // (2)

    @Override
    String start() {
        if (!initialized) {
            throw new IllegalStateException("Engine not initialized!")
        }

        return "Starting V8"
    }

    @PostConstruct // (3)
    void initialize() {
        initialized = true
    }
}
```

| **1** | The `PostConstruct` annotation is imported |
|---|---|
| **2** | A field is defined that requires initialization |
| **3** | A method is annotated with `@PostConstruct` and will be invoked once the object is constructed and fully injected. |

To manage when a bean is constructed, see the section on bean scopes.


## When The Bean Is Destroyed

To invoke a method when the bean is destroyed, use the `jakarta.annotation.PreDestroy` annotation:

```java
import jakarta.annotation.PreDestroy; // (1)
import jakarta.inject.Singleton;
import java.util.concurrent.atomic.AtomicBoolean;

@Singleton
public class PreDestroyBean implements AutoCloseable {

    AtomicBoolean stopped = new AtomicBoolean(false);

    @PreDestroy // (2)
    @Override
    public void close() throws Exception {
        stopped.compareAndSet(false, true);
    }
}
```

```kotlin
import jakarta.annotation.PreDestroy // (1)
import jakarta.inject.Singleton
import java.util.concurrent.atomic.AtomicBoolean

@Singleton
class PreDestroyBean : AutoCloseable {

    internal var stopped = AtomicBoolean(false)

    @PreDestroy // (2)
    @Throws(Exception::class)
    override fun close() {
        stopped.compareAndSet(false, true)
    }
}
```

```groovy
import jakarta.annotation.PreDestroy // (1)
import jakarta.inject.Singleton
import java.util.concurrent.atomic.AtomicBoolean

@Singleton
class PreDestroyBean implements AutoCloseable {

    AtomicBoolean stopped = new AtomicBoolean(false)

    @PreDestroy // (2)
    @Override
    void close() throws Exception {
        stopped.compareAndSet(false, true)
    }
}
```

| **1** | The `PreDestroy` annotation is imported |
|---|---|
| **2** | A method is annotated with `@PreDestroy` and will be invoked when the context is closed. |

For factory beans, the `preDestroy` value in the Bean annotation tells Micronaut framework which method to invoke.

```java
import io.micronaut.context.annotation.Bean;
import io.micronaut.context.annotation.Factory;

import jakarta.inject.Singleton;

@Factory
public class ConnectionFactory {

    @Bean(preDestroy = "stop") // (1)
    @Singleton
    public Connection connection() {
        return new Connection();
    }
}
```

```kotlin
import io.micronaut.context.annotation.Bean
import io.micronaut.context.annotation.Factory

import jakarta.inject.Singleton

@Factory
class ConnectionFactory {

    @Bean(preDestroy = "stop") // (1)
    @Singleton
    fun connection(): Connection {
        return Connection()
    }
}
```

```groovy
import io.micronaut.context.annotation.Bean
import io.micronaut.context.annotation.Factory

import jakarta.inject.Singleton

@Factory
class ConnectionFactory {

    @Bean(preDestroy = "stop") // (1)
    @Singleton
    Connection connection() {
        new Connection()
    }
}
```

```java
import java.util.concurrent.atomic.AtomicBoolean;

public class Connection {

    AtomicBoolean stopped = new AtomicBoolean(false);

    public void stop() { // (2)
        stopped.compareAndSet(false, true);
    }

}
```

```kotlin
import java.util.concurrent.atomic.AtomicBoolean

class Connection {

    internal var stopped = AtomicBoolean(false)

    fun stop() { // (2)
        stopped.compareAndSet(false, true)
    }

}
```

```groovy
import java.util.concurrent.atomic.AtomicBoolean

class Connection {

    AtomicBoolean stopped = new AtomicBoolean(false)

    void stop() { // (2)
        stopped.compareAndSet(false, true)
    }

}
```

| **1** | The `preDestroy` value is set on the annotation |
|---|---|
| **2** | The annotation value matches the method name |

|   | Simply implementing the `Closeable` or `AutoCloseable` interface is not enough for a bean to be closed with the context. One of the above methods must be used. |
|---|---|


## Dependent Beans

Dependent beans are the beans used in the construction of your bean. If the dependent bean’s scope is `@Prototype` or unknown, it will be destroyed along with your instance.


## 3.15 Graceful Shutdown

In some deployments, it is desirable to "gracefully" shut down an application, that is, to stop accepting new work but to finish in-progress tasks. In the Micronaut framework, a graceful shutdown means the following:

- No new HTTP connections will be accepted
- Existing connections will serve no new requests, but in-progress requests will still be served
- Scheduled tasks will stop running, but in-progress tasks will finish uninterrupted

If the `micronaut.lifecycle.graceful-shutdown.enabled` config property is set to `true`, a graceful shutdown is triggered automatically when the context stops (`ApplicationContext.stop()`). There is also a programmatic GracefulShutdownManager API if you want more control over the shutdown process.

Graceful shutdown status can be read using the health management endpoint. This also returns the number of still-active tasks (e.g. connections or running scheduled tasks).

If you want to add graceful shutdown support to your own beans, implement GracefulShutdownCapable. You will implement a `shutdownGracefully` method that triggers shutdown and returns a future that should complete once the graceful shutdown is complete (e.g. all clients have closed their connection). You can also optionally implement `reportActiveTasks` to give a number of active tasks for the health endpoint.


## 3.16 Context Events

The Micronaut framework supports a general event system through the context. The ApplicationEventPublisher API publishes events and the ApplicationEventListener API is used to listen to events. The event system is not limited to events that Micronaut publishes and supports custom events created by users. Context Events require Micronaut Context dependency:

`implementation("io.micronaut:micronaut-context")` `<dependency> <groupId>io.micronaut</groupId> <artifactId>micronaut-context</artifactId> </dependency>`

`micronaut-context` is a transitive dependency of `micronaut-http`. If you use a Micronaut HTTP runtime, your project already includes the `Micronaut-context` dependency.

### Publishing Events

The ApplicationEventPublisher API supports events of any type, although all events that the Micronaut framework publishes extend ApplicationEvent.

To publish an event, use dependency injection to obtain an instance of ApplicationEventPublisher where the generic type is the type of event and invoke the `publishEvent` method with your event object.

"Publishing an Event

```java
public class SampleEvent {
    private String message = "Something happened";

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
}

import io.micronaut.context.event.ApplicationEventPublisher;
import jakarta.inject.Inject;
import jakarta.inject.Singleton;

@Singleton
public class SampleEventEmitterBean {

    @Inject
    ApplicationEventPublisher<SampleEvent> eventPublisher;

    public void publishSampleEvent() {
        eventPublisher.publishEvent(new SampleEvent());
    }

}
```

"Publishing an Event

```kotlin
data class SampleEvent(val message: String = "Something happened")

import io.micronaut.context.event.ApplicationEventPublisher
import jakarta.inject.Inject
import jakarta.inject.Singleton

@Singleton
class SampleEventEmitterBean {

    @Inject
    internal var eventPublisher: ApplicationEventPublisher<SampleEvent>? = null

    fun publishSampleEvent() {
        eventPublisher!!.publishEvent(SampleEvent())
    }

}
```

"Publishing an Event

```groovy
class SampleEvent {
    String message = "Something happened"
}

import io.micronaut.context.event.ApplicationEventPublisher
import jakarta.inject.Inject
import jakarta.inject.Singleton

@Singleton
class SampleEventEmitterBean {

    @Inject
    ApplicationEventPublisher<SampleEvent> eventPublisher

    void publishSampleEvent() {
        eventPublisher.publishEvent(new SampleEvent())
    }

}
```

|   | Publishing an event is **synchronous** by default! The `publishEvent` method will not return until all listeners have been executed. Move this work off to a thread pool if it is time-intensive. |
|---|---|

### Listening for Events

To listen to an event, register a bean that implements ApplicationEventListener where the generic type is the type of event.

Listening for Events with

ApplicationEventListener

```java
import io.micronaut.context.event.ApplicationEventListener;
import io.micronaut.docs.context.events.SampleEvent;
import jakarta.inject.Singleton;

@Singleton
public class SampleEventListener implements ApplicationEventListener<SampleEvent> {
    private int invocationCounter = 0;

    @Override
    public void onApplicationEvent(SampleEvent event) {
        invocationCounter++;
    }

    public int getInvocationCounter() {
        return invocationCounter;
    }
}

import io.micronaut.context.ApplicationContext;
import io.micronaut.docs.context.events.SampleEventEmitterBean;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class SampleEventListenerSpec {

    @Test
    void testEventListenerIsNotified() {
        try (ApplicationContext context = ApplicationContext.run()) {
            SampleEventEmitterBean emitter = context.getBean(SampleEventEmitterBean.class);
            SampleEventListener listener = context.getBean(SampleEventListener.class);
            assertEquals(0, listener.getInvocationCounter());
            emitter.publishSampleEvent();
            assertEquals(1, listener.getInvocationCounter());
        }
    }
}
```

Listening for Events with

ApplicationEventListener

```kotlin
import io.micronaut.context.event.ApplicationEventListener
import io.micronaut.docs.context.events.SampleEvent
import jakarta.inject.Singleton

@Singleton
class SampleEventListener : ApplicationEventListener<SampleEvent> {
    var invocationCounter = 0

    override fun onApplicationEvent(event: SampleEvent) {
        invocationCounter++
    }
}

import io.kotest.matchers.shouldBe
import io.kotest.core.spec.style.AnnotationSpec
import io.micronaut.context.ApplicationContext
import io.micronaut.docs.context.events.SampleEventEmitterBean

class SampleEventListenerSpec : AnnotationSpec() {

    @Test
    fun testEventListenerWasNotified() {
        val context = ApplicationContext.run()
        val emitter = context.getBean(SampleEventEmitterBean::class.java)
        val listener = context.getBean(SampleEventListener::class.java)
        listener.invocationCounter.shouldBe(0)
        emitter.publishSampleEvent()
        listener.invocationCounter.shouldBe(1)

        context.close()
    }
}
```

Listening for Events with

ApplicationEventListener

```groovy
import io.micronaut.context.event.ApplicationEventListener
import io.micronaut.docs.context.events.SampleEvent
import jakarta.inject.Singleton

@Singleton
class SampleEventListener implements ApplicationEventListener<SampleEvent> {
    int invocationCounter = 0

    @Override
    void onApplicationEvent(SampleEvent event) {
        invocationCounter++
    }
}

import io.micronaut.context.ApplicationContext
import io.micronaut.docs.context.events.SampleEventEmitterBean
import spock.lang.Specification

class SampleEventListenerSpec extends Specification {

    void "test event listener is notified"() {
        given:
        ApplicationContext context = ApplicationContext.run()
        SampleEventEmitterBean emitter = context.getBean(SampleEventEmitterBean)
        SampleEventListener listener = context.getBean(SampleEventListener)

        expect:
        listener.invocationCounter == 0

        when:
        emitter.publishSampleEvent()

        then:
        listener.invocationCounter == 1

        cleanup:
        context.close()
    }
}
```

|   | The supports method can be overridden to further clarify events to be processed. |
|---|---|

Alternatively, use the @EventListener annotation if you do not wish to implement an interface or utilize one of the built-in events like StartupEvent and ShutdownEvent:

Listening for Events with

@EventListener

```java
import io.micronaut.docs.context.events.SampleEvent;
import io.micronaut.context.event.StartupEvent;
import io.micronaut.context.event.ShutdownEvent;
import io.micronaut.runtime.event.annotation.EventListener;

@Singleton
public class SampleEventListener {
    private int invocationCounter = 0;

    @EventListener
    public void onSampleEvent(SampleEvent event) {
        invocationCounter++;
    }

    @EventListener
    public void onStartupEvent(StartupEvent event) {
        // startup logic here
    }

    @EventListener
    public void onShutdownEvent(ShutdownEvent event) {
        // shutdown logic here
    }

    public int getInvocationCounter() {
        return invocationCounter;
    }
}
```

Listening for Events with

@EventListener

```kotlin
import io.micronaut.docs.context.events.SampleEvent
import io.micronaut.context.event.StartupEvent
import io.micronaut.context.event.ShutdownEvent
import io.micronaut.runtime.event.annotation.EventListener

@Singleton
class SampleEventListener {
    var invocationCounter = 0

    @EventListener
    internal fun onSampleEvent(event: SampleEvent) {
        invocationCounter++
    }

    @EventListener
    internal fun onStartupEvent(event: StartupEvent) {
        // startup logic here
    }

    @EventListener
    internal fun onShutdownEvent(event: ShutdownEvent) {
        // shutdown logic here
    }
}
```

Listening for Events with

@EventListener

```groovy
import io.micronaut.docs.context.events.SampleEvent
import io.micronaut.context.event.StartupEvent
import io.micronaut.context.event.ShutdownEvent
import io.micronaut.runtime.event.annotation.EventListener

@Singleton
class SampleEventListener {
    int invocationCounter = 0

    @EventListener
    void onSampleEvent(SampleEvent event) {
        invocationCounter++
    }

    @EventListener
    void onStartupEvent(StartupEvent event) {
        // startup logic here
    }

    @EventListener
    void onShutdownEvent(ShutdownEvent event) {
        // shutdown logic here
    }
}
```

If your listener performs work that might take a while, use the @Async annotation to run the operation on a separate thread:

Asynchronously listening for Events with

@EventListener

```java
import io.micronaut.docs.context.events.SampleEvent;
import io.micronaut.runtime.event.annotation.EventListener;
import io.micronaut.scheduling.annotation.Async;

@Singleton
public class SampleEventListener {
    private AtomicInteger invocationCounter = new AtomicInteger(0);

    @EventListener
    @Async
    public void onSampleEvent(SampleEvent event) {
        invocationCounter.getAndIncrement();
    }

    public int getInvocationCounter() {
        return invocationCounter.get();
    }
}

import io.micronaut.context.ApplicationContext;
import io.micronaut.docs.context.events.SampleEventEmitterBean;
import org.junit.jupiter.api.Test;

import static java.util.concurrent.TimeUnit.SECONDS;
import static org.awaitility.Awaitility.await;
import static org.hamcrest.Matchers.equalTo;
import static org.junit.jupiter.api.Assertions.assertEquals;

class SampleEventListenerSpec {

    @Test
    void testEventListenerIsNotified() {
        try (ApplicationContext context = ApplicationContext.run()) {
            SampleEventEmitterBean emitter = context.getBean(SampleEventEmitterBean.class);
            SampleEventListener listener = context.getBean(SampleEventListener.class);
            assertEquals(0, listener.getInvocationCounter());
            emitter.publishSampleEvent();
            await().atMost(5, SECONDS).until(listener::getInvocationCounter, equalTo(1));
        }
    }
}
```

Asynchronously listening for Events with

@EventListener

```kotlin
import io.micronaut.docs.context.events.SampleEvent
import io.micronaut.runtime.event.annotation.EventListener
import io.micronaut.scheduling.annotation.Async
import java.util.concurrent.atomic.AtomicInteger

@Singleton
open class SampleEventListener {

    var invocationCounter = AtomicInteger(0)

    @EventListener
    @Async
    open fun onSampleEvent(event: SampleEvent) {
        println("Incrementing invocation counter...")
        invocationCounter.getAndIncrement()
    }
}

import io.kotest.assertions.nondeterministic.eventually
import io.kotest.matchers.shouldBe
import io.kotest.core.spec.style.AnnotationSpec
import io.micronaut.context.ApplicationContext
import io.micronaut.docs.context.events.SampleEventEmitterBean
import kotlin.time.DurationUnit
import kotlin.time.ExperimentalTime
import kotlin.time.toDuration

@ExperimentalTime
class SampleEventListenerSpec : AnnotationSpec() {

    @Test
    suspend fun testEventListenerWasNotified() {
        val context = ApplicationContext.run()
        val emitter = context.getBean(SampleEventEmitterBean::class.java)
        val listener = context.getBean(SampleEventListener::class.java)
        listener.invocationCounter.get().shouldBe(0)
        emitter.publishSampleEvent()

        eventually(5.toDuration(DurationUnit.SECONDS)) {
            println("Current value of counter: " + listener.invocationCounter.get())
            listener.invocationCounter.get().shouldBe(1)
        }

        context.close()
    }
}
```

Asynchronously listening for Events with

@EventListener

```groovy
import io.micronaut.docs.context.events.SampleEvent
import io.micronaut.runtime.event.annotation.EventListener
import io.micronaut.scheduling.annotation.Async

@Singleton
class SampleEventListener {
    AtomicInteger invocationCounter = new AtomicInteger(0)

    @EventListener
    @Async
    void onSampleEvent(SampleEvent event) {
        invocationCounter.getAndIncrement()
    }
}

import io.micronaut.context.ApplicationContext
import io.micronaut.docs.context.events.SampleEventEmitterBean
import spock.lang.Specification
import spock.util.concurrent.PollingConditions

class SampleEventListenerSpec extends Specification {

    void "test event listener is notified"() {
        given:
        def context = ApplicationContext.run()
        def emitter = context.getBean(SampleEventEmitterBean)
        def listener = context.getBean(SampleEventListener)

        expect:
        listener.invocationCounter.get() == 0

        when:
        emitter.publishSampleEvent()

        then:
        new PollingConditions(timeout: 5).eventually {
            listener.invocationCounter.get() == 1
        }

        cleanup:
        context.close()
    }
}
```

The event listener by default runs on the `scheduled` executor. You can configure this thread pool as required in your configuration file (e.g `application.yml`):

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


## 3.17 Bean Events

You can hook into the creation of beans using one of the following interfaces:

- BeanInitializedEventListener - allows modifying or replacing a bean after properties have been set but prior to `@PostConstruct` event hooks.
- BeanCreatedEventListener - allows modifying or replacing a bean after the bean is fully initialized and all `@PostConstruct` hooks called.

The `BeanInitializedEventListener` interface is commonly used in combination with Factory beans. Consider the following example:

```java
public class V8Engine implements Engine {
    private final int cylinders = 8;
    private double rodLength; // (1)

    public V8Engine(double rodLength) {
        this.rodLength = rodLength;
    }

    @Override
    public String start() {
        return "Starting V" + getCylinders() + " [rodLength=" + getRodLength() + ']';
    }

    @Override
    public final int getCylinders() {
        return cylinders;
    }

    public double getRodLength() {
        return rodLength;
    }

    public void setRodLength(double rodLength) {
        this.rodLength = rodLength;
    }
}

@Factory
public class EngineFactory {

    private V8Engine engine;
    private double rodLength = 5.7;

    @PostConstruct
    public void initialize() {
        engine = new V8Engine(rodLength); // (2)
    }

    @Singleton
    public Engine v8Engine() {
        return engine;// (3)
    }

    public void setRodLength(double rodLength) {
        this.rodLength = rodLength;
    }
}

@Singleton
public class EngineInitializer implements BeanInitializedEventListener<EngineFactory> { // (4)
    @Override
    public EngineFactory onInitialized(BeanInitializingEvent<EngineFactory> event) {
        EngineFactory engineFactory = event.getBean();
        engineFactory.setRodLength(6.6);// (5)
        return engineFactory;
    }
}
```

```kotlin
class V8Engine(var rodLength: Double) : Engine {  // (1)

    override val cylinders = 8

    override fun start(): String {
        return "Starting V$cylinders [rodLength=$rodLength]"
    }
}

@Factory
class EngineFactory {

    private var engine: V8Engine? = null
    private var rodLength = 5.7

    @PostConstruct
    fun initialize() {
        engine = V8Engine(rodLength) // (2)
    }

    @Singleton
    fun v8Engine(): Engine? {
        return engine// (3)
    }

    fun setRodLength(rodLength: Double) {
        this.rodLength = rodLength
    }
}

@Singleton
class EngineInitializer : BeanInitializedEventListener<EngineFactory> { // (4)
    override fun onInitialized(event: BeanInitializingEvent<EngineFactory>): EngineFactory {
        val engineFactory = event.bean
        engineFactory.setRodLength(6.6) // (5)
        return engineFactory
    }
}
```

```groovy
class V8Engine implements Engine {
    final int cylinders = 8
    double rodLength // (1)

    @Override
    String start() {
        return "Starting V$cylinders [rodLength=$rodLength]"
    }
}

@Factory
class EngineFactory {
    private V8Engine engine
    double rodLength = 5.7

    @PostConstruct
    void initialize() {
        engine = new V8Engine(rodLength: rodLength) // (2)
    }

    @Singleton
    Engine v8Engine() {
        return engine // (3)
    }
}

@Singleton
class EngineInitializer implements BeanInitializedEventListener<EngineFactory> { // (4)
    @Override
    EngineFactory onInitialized(BeanInitializingEvent<EngineFactory> event) {
        EngineFactory engineFactory = event.bean
        engineFactory.rodLength = 6.6 // (5)
        return engineFactory
    }
}
```

| **1** | The `V8Engine` class defines a `rodLength` property |
|---|---|
| **2** | The `EngineFactory` initializes the value of `rodLength` and creates the instance |
| **3** | The created instance is returned as a Bean |
| **4** | The `BeanInitializedEventListener` interface is implemented to listen for the initialization of the factory |
| **5** | Within the `onInitialized` method the `rodLength` is overridden prior to the engine being created by the factory bean. |

The BeanCreatedEventListener interface is more typically used to decorate or enhance a fully initialized bean, for example by creating a proxy.

|   | Bean event listeners are initialized **before** type converters. If your event listener relies on type conversion either by relying on a configuration properties bean or by any other mechanism, you may see errors related to type conversion. |
|---|---|


## 3.18 Bean Introspection

Since Micronaut framework 1.1, a compile-time replacement for the JDK’s Introspector class has been included.

The BeanIntrospector and BeanIntrospection interfaces allow looking up bean introspections to instantiate and read/write bean properties without using reflection or caching reflective metadata, which consume excessive memory for large beans.


## 3.18.1 Making a Bean Available for Introspection

Unlike the JDK’s Introspector, every class is not automatically available for introspection. To make a class available for introspection you must at a minimum enable Micronaut’s annotation processor (`micronaut-inject-java` for Java and Kotlin and `micronaut-inject-groovy` for Groovy) in your build and ensure you have a runtime time dependency on `micronaut-core`.

`annotationProcessor("io.micronaut:micronaut-inject-java")` `<annotationProcessorPaths> <path> <groupId>io.micronaut</groupId> <artifactId>micronaut-inject-java</artifactId> </path> </annotationProcessorPaths>`

|   | For Kotlin, add the `micronaut-inject-java` dependency in `kapt` scope, and for Groovy add `micronaut-inject-groovy` in `compileOnly` scope. |
|---|---|

`runtimeOnly("io.micronaut:micronaut-core")` `<dependency> <groupId>io.micronaut</groupId> <artifactId>micronaut-core</artifactId> <scope>runtime</scope> </dependency>`

Once your build is configured you have a few ways to generate introspection data.


## 3.18.2 Use the @Introspected Annotation

The @Introspected annotation can be used on any class to make it available for introspection. Simply annotate the class with @Introspected:

```java
import io.micronaut.core.annotation.Introspected;

@Introspected
public class Person {

    private String name;
    private int age = 18;

    public Person(String name) {
        this.name = name;
    }

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

```kotlin
import io.micronaut.core.annotation.Introspected

@Introspected
data class Person(var name : String) {
    var age : Int = 18
}
```

```groovy
import groovy.transform.Canonical
import io.micronaut.core.annotation.Introspected

@Introspected
@Canonical
class Person {

    String name
    int age = 18

    Person(String name) {
        this.name = name
    }
}
```

Once introspection data has been produced at compile time, retrieve it via the BeanIntrospection API:

```java
final BeanIntrospection<Person> introspection = BeanIntrospection.getIntrospection(Person.class); // (1)
Person person = introspection.instantiate("John"); // (2)
System.out.println("Hello " + person.getName());

final BeanProperty<Person, String> property = introspection.getRequiredProperty("name", String.class); // (3)
property.set(person, "Fred"); // (4)
String name = property.get(person); // (5)
System.out.println("Hello " + person.getName());
```

```kotlin
val introspection = BeanIntrospection.getIntrospection(Person::class.java) // (1)
val person : Person = introspection.instantiate("John") // (2)
print("Hello ${person.name}")

val property : BeanProperty<Person, String> = introspection.getRequiredProperty("name", String::class.java) // (3)
property.set(person, "Fred") // (4)
val name = property.get(person) // (5)
print("Hello ${person.name}")
```

```groovy
def introspection = BeanIntrospection.getIntrospection(Person) // (1)
Person person = introspection.instantiate("John") // (2)
println("Hello $person.name")

BeanProperty<Person, String> property = introspection.getRequiredProperty("name", String) // (3)
property.set(person, "Fred") // (4)
String name = property.get(person) // (5)
println("Hello $person.name")
```

| **1** | You can retrieve a BeanIntrospection with the static `getIntrospection` method |
|---|---|
| **2** | Once you have a BeanIntrospection you can instantiate a bean with the `instantiate` method. |
| **3** | A BeanProperty can be retrieved from the introspection |
| **4** | Use the `set` method to set the property value |
| **5** | Use the `get` method to retrieve the property value |

It’s possible to apply the introspection to all the classes in one package. Simply create `package-info` file and annotate the package with @Introspected.

```java
@Introspected
@AccessorsStyle(readPrefixes = "", writePrefixes = "")
package io.micronaut.docs.ioc.introspection.pck.foobar;

import io.micronaut.core.annotation.AccessorsStyle;
import io.micronaut.core.annotation.Introspected;
```

```groovy
@Introspected
@AccessorsStyle(readPrefixes = "", writePrefixes = "")
package io.micronaut.docs.ioc.introspection.pck.foobar

import io.micronaut.core.annotation.AccessorsStyle
import io.micronaut.core.annotation.Introspected
```

|   | The package should contain only classes that can be introspected. |
|---|---|

|   | Only classes located directly within the package are processed; subpackages are ignored. |
|---|---|


## 3.18.3 Use @Introspected with @AccessorsStyle

It is possible to use the `@AccessorsStyle` annotation with `@Introspected`:

```java
import io.micronaut.core.annotation.AccessorsStyle;
import io.micronaut.core.annotation.Introspected;

@Introspected
@AccessorsStyle(readPrefixes = "", writePrefixes = "") // (1)
public class Person {

    private String name;
    private int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String name() { // (2)
        return name;
    }

    public void name(String name) { // (2)
        this.name = name;
    }

    public int age() { // (2)
        return age;
    }

    public void age(int age) { // (2)
        this.age = age;
    }
}
```

```kotlin
import io.micronaut.core.annotation.AccessorsStyle
import io.micronaut.core.annotation.Introspected

@Introspected
@AccessorsStyle(readPrefixes = [""], writePrefixes = [""]) // (1)
class Person(private var name: String, private var age: Int) {
    fun name(): String { // (2)
        return name
    }

    fun name(name: String) { // (2)
        this.name = name
    }

    fun age(): Int { // (2)
        return age
    }

    fun age(age: Int) { // (2)
        this.age = age
    }
}
```

```groovy
import io.micronaut.core.annotation.AccessorsStyle
import io.micronaut.core.annotation.Introspected

@Introspected
@AccessorsStyle(readPrefixes = "", writePrefixes = "") // (1)
class Person {

    private String name
    private int age

    Person(String name, int age) {
        this.name = name
        this.age = age
    }

    String name() { // (2)
        return name
    }

    void name(String name) { // (2)
        this.name = name
    }

    int age() { // (2)
        return age
    }

    void age(int age) { // (2)
        this.age = age
    }
}
```

| **1** | Annotate the class with `@AccessorsStyle` to define empty read and write prefixes for getters and setters. |
|---|---|
| **2** | Define the getters and setters without a prefix. |

Now it is possible to retrieve the compile time generated introspection using the BeanIntrospection API:

```kotlin
        val introspection = BeanIntrospection.getIntrospection(Person::class.java)
        val person = introspection.instantiate("John", 42)

        Assertions.assertEquals("John", person.name())
        Assertions.assertEquals(42, person.age())
```

```groovy
        BeanIntrospection<Person> introspection = BeanIntrospection.getIntrospection(Person)
        Person person = introspection.instantiate('John', 42)

        person.name() == 'John'
        person.age() == 42
```
