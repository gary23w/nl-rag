---
title: "Micronaut Core (part 2/27)"
source: https://docs.micronaut.io/latest/guide/index.html
domain: micronaut
license: CC-BY-SA-4.0
tags: micronaut framework, micronaut jvm, compile-time injection, microservices framework
fetched: 2026-07-02
part: 2/27
---

## Qualifying By Name

To qualify by name, use the Named annotation. For example, consider the following classes:

```java
public interface Engine { // (1)
    int getCylinders();
    String start();
}

@Singleton
public class V6Engine implements Engine {  // (2)
    @Override
    public String start() {
        return "Starting V6";
    }

    @Override
    public int getCylinders() {
        return 6;
    }
}

@Singleton
public class V8Engine implements Engine {  // (3)
    @Override
    public String start() {
        return "Starting V8";
    }

    @Override
    public int getCylinders() {
        return 8;
    }

}

@Singleton
public class Vehicle {
    private final Engine engine;

    @Inject
    public Vehicle(@Named("v8") Engine engine) {// (4)
        this.engine = engine;
    }

    public String start() {
        return engine.start();// (5)
    }
}
```

```kotlin
interface Engine { // (1)
    val cylinders: Int
    fun start(): String
}

@Singleton
class V6Engine : Engine {  // (2)

    override var cylinders: Int = 6

    override fun start(): String {
        return "Starting V6"
    }
}

@Singleton
class V8Engine : Engine {

    override var cylinders: Int = 8

    override fun start(): String {
        return "Starting V8"
    }

}

@Singleton
class Vehicle @Inject
constructor(@param:Named("v8") private val engine: Engine) { // (4)

    fun start(): String {
        return engine.start() // (5)
    }
}
```

```groovy
interface Engine { // (1)
    int getCylinders()
    String start()
}

@Singleton
class V6Engine implements Engine { // (2)
    int cylinders = 6

    @Override
    String start() {
        "Starting V6"
    }
}

@Singleton
class V8Engine implements Engine { // (3)
    int cylinders = 8

    @Override
    String start() {
        "Starting V8"
    }
}

@Singleton
class Vehicle {
    final Engine engine

    @Inject Vehicle(@Named('v8') Engine engine) { // (4)
        this.engine = engine
    }

    String start() {
        engine.start() // (5)
    }
}
```

| **1** | The `Engine` interface defines the common contract |
|---|---|
| **2** | The `V6Engine` class is the first implementation |
| **3** | The `V8Engine` class is the second implementation |
| **4** | The jakarta.inject.Named annotation indicates that the `V8Engine` implementation is required |
| **5** | Calling the start method prints: `"Starting V8"` |

Micronaut framework is capable of injecting `V8Engine` in the previous example, because:

`@Named` qualifier value (`v8`) + type being injected simple name (`Engine`) == (case-insensitive) == The simple name of a bean of type `Engine` (`V8Engine`)

You can also declare @Named at the class level of a bean to explicitly define the name of the bean.


## Qualifying By Annotation

In addition to being able to qualify by name, you can build your own qualifiers using the Qualifier annotation. For example, consider the following annotation:

```java
import jakarta.inject.Qualifier;
import java.lang.annotation.Retention;

import static java.lang.annotation.RetentionPolicy.RUNTIME;

@Qualifier
@Retention(RUNTIME)
public @interface V8 {
}
```

```kotlin
import jakarta.inject.Qualifier
import java.lang.annotation.Retention
import java.lang.annotation.RetentionPolicy.RUNTIME

@Qualifier
@Retention(RUNTIME)
annotation class V8
```

```groovy
import jakarta.inject.Qualifier
import java.lang.annotation.Retention

import static java.lang.annotation.RetentionPolicy.RUNTIME

@Qualifier
@Retention(RUNTIME)
@interface V8 {
}
```

The above annotation is itself annotated with the `@Qualifier` annotation to designate it as a qualifier. You can then use the annotation at any injection point in your code. For example:

```java
@Inject Vehicle(@V8 Engine engine) {
    this.engine = engine;
}
```

```kotlin
@Inject constructor(@V8 val engine: Engine) {
```

```groovy
@Inject Vehicle(@V8 Engine engine) {
    this.engine = engine
}
```


## Qualifying By Annotation Members

Since Micronaut framework 3.0, annotation qualifiers can also use annotation members to resolve the correct bean to inject. For example, consider the following annotation:

```java
import io.micronaut.context.annotation.NonBinding;
import jakarta.inject.Qualifier;
import java.lang.annotation.Retention;

import static java.lang.annotation.RetentionPolicy.RUNTIME;

@Qualifier // (1)
@Retention(RUNTIME)
public @interface Cylinders {
    int value();

    @NonBinding // (2)
    String description() default "";
}
```

```kotlin
import io.micronaut.context.annotation.NonBinding
import jakarta.inject.Qualifier
import kotlin.annotation.Retention

@Qualifier // (1)
@Retention(AnnotationRetention.RUNTIME)
annotation class Cylinders(
    val value: Int,
    @get:NonBinding // (2)
    val description: String = ""
)
```

```groovy
import io.micronaut.context.annotation.NonBinding
import jakarta.inject.Qualifier
import java.lang.annotation.Retention

import static java.lang.annotation.RetentionPolicy.RUNTIME

@Qualifier // (1)
@Retention(RUNTIME)
@interface Cylinders {
    int value();

    @NonBinding // (2)
    String description() default "";
}
```

| **1** | The `@Cylinders` annotation is meta-annotated with `@Qualifier` |
|---|---|
| **2** | The annotation has two members. The @NonBinding annotation is used to exclude the `description` member from being considered during dependency resolution. |

You can then use the `@Cylinders` annotation on any bean and the members that are not annotated with @NonBinding are considered during dependency resolution:

```java
@Singleton
@Cylinders(value = 6, description = "6-cylinder V6 engine")  // (1)
public class V6Engine implements Engine { // (2)

    @Override
    public int getCylinders() {
        return 6;
    }

    @Override
    public String start() {
        return "Starting V6";
    }
}
```

```kotlin
@Singleton
@Cylinders(value = 6, description = "6-cylinder V6 engine") // (1)
class V6Engine : Engine { // (2)
    // (2)
    override val cylinders: Int
        get() = 6

    override fun start(): String {
        return "Starting V6"
    }
}
```

```groovy
@Singleton
@Cylinders(value = 6, description = "6-cylinder V6 engine")  // (1)
class V6Engine implements Engine { // (2)

    @Override
    int getCylinders() {
        return 6
    }

    @Override
    String start() {
        return "Starting V6"
    }
}
```

| **1** | Here the `value` member is set to 6 for the `V6Engine` type |
|---|---|
| **2** | The class implements an `Engine` interface |

```java
@Singleton
@Cylinders(value = 8, description = "8-cylinder V8 engine") // (1)
public class V8Engine implements Engine { // (2)
    @Override
    public int getCylinders() {
        return 8;
    }

    @Override
    public String start() {
        return "Starting V8";
    }
}
```

```kotlin
@Singleton
@Cylinders(value = 8, description = "8-cylinder V8 engine") // (1)
class V8Engine : Engine { // (2)
    override val cylinders: Int
        get() = 8

    override fun start(): String {
        return "Starting V8"
    }
}
```

```groovy
@Singleton
@Cylinders(value = 8, description = "8-cylinder V8 engine") // (1)
class V8Engine implements Engine { // (2)
    @Override
    int getCylinders() {
        return 8
    }

    @Override
    String start() {
        return "Starting V8"
    }
}
```

| **1** | Here the `value` member is set to 8 for the `V8Engine` type |
|---|---|
| **2** | The class implements an `Engine` interface |

You can then use the `@Cylinders` qualifier on any injection point to select the correct bean to inject. For example:

```java
@Inject Vehicle(@Cylinders(8) Engine engine) {
    this.engine = engine;
}
```

```kotlin
@Singleton
class Vehicle(@param:Cylinders(8) val engine: Engine) {
    fun start(): String {
        return engine.start()
    }
}
```

```groovy
@Inject Vehicle(@Cylinders(8) Engine engine) {
    this.engine = engine
}
```


## Qualifying by Generic Type Arguments

Since Micronaut framework 3.0, it is possible to select which bean to inject based on the generic type arguments of the class or interface. Consider the following example:

```java
public interface CylinderProvider {
    int getCylinders();
}
```

```kotlin
interface CylinderProvider {
    val cylinders: Int
}
```

```groovy
interface CylinderProvider {
    int getCylinders()
}
```

The `CylinderProvider` interface provides the number of cylinders.

```java
public interface Engine<T extends CylinderProvider> { // (1)
    default int getCylinders() {
        return getCylinderProvider().getCylinders();
    }

    default String start() {
        return "Starting " + getCylinderProvider().getClass().getSimpleName();
    }

    T getCylinderProvider();
}
```

```kotlin
interface Engine<T : CylinderProvider> { // (1)
    val cylinders: Int
        get() = cylinderProvider.cylinders

    fun start(): String {
        return "Starting ${cylinderProvider.javaClass.simpleName}"
    }

    val cylinderProvider: T
}
```

```groovy
interface Engine<T extends CylinderProvider> { // (1)
    default int getCylinders() { getCylinderProvider().cylinders }

    default String start() { "Starting ${getCylinderProvider().class.simpleName}" }

    T getCylinderProvider()
}
```

| **1** | The engine class defines a generic type argument `<T>` that must be an instance of `CylinderProvider` |
|---|---|

You can define implementations of the `Engine` interface with different generic type arguments. For example for a V6 engine:

```java
public class V6 implements CylinderProvider {
    @Override
    public int getCylinders() {
        return 6;
    }
}
```

```kotlin
class V6 : CylinderProvider {
    override val cylinders: Int = 6
}
```

```groovy
class V6 implements CylinderProvider {
    @Override
    int getCylinders() { 6 }
}
```

The above defines a `V6` class that implements the `CylinderProvider` interface.

```java
@Singleton
public class V6Engine implements Engine<V6> {  // (1)
    @Override
    public V6 getCylinderProvider() {
        return new V6();
    }
}
```

```kotlin
@Singleton
class V6Engine : Engine<V6> { // (1)
    override val cylinderProvider: V6
        get() = V6()
}
```

```groovy
@Singleton
class V6Engine implements Engine<V6> {  // (1)
    @Override
    V6 getCylinderProvider() { new V6() }
}
```

| **1** | The `V6Engine` implements `Engine` providing `V6` as a generic type parameter |
|---|---|

And a V8 engine:

```java
public class V8 implements CylinderProvider {
    @Override
    public int getCylinders() {
        return 8;
    }
}
```

```kotlin
class V8 : CylinderProvider {
    override val cylinders: Int = 8
}
```

```groovy
class V8 implements CylinderProvider {
    @Override
    int getCylinders() { 8 }
}
```

The above defines a `V8` class that implements the `CylinderProvider` interface.

```java
@Singleton
public class V8Engine implements Engine<V8> {  // (1)
    @Override
    public V8 getCylinderProvider() {
        return new V8();
    }
}
```

```kotlin
@Singleton
class V8Engine : Engine<V8> { // (1)
    override val cylinderProvider: V8
        get() = V8()
}
```

```groovy
@Singleton
class V8Engine implements Engine<V8> {  // (1)
    @Override
    V8 getCylinderProvider() { new V8() }
}
```

| **1** | The `V8Engine` implements `Engine` providing `V8` as a generic type parameter |
|---|---|

You can then use the generic arguments when defining the injection point and Micronaut framework will pick the correct bean to inject based on the specific generic type arguments:

```java
@Inject
public Vehicle(Engine<V8> engine) {
    this.engine = engine;
}
```

```kotlin
@Singleton
class Vehicle(val engine: Engine<V8>) {
```

```groovy
@Inject
Vehicle(Engine<V8> engine) {
    this.engine = engine
}
```

In the above example the `V8Engine` bean is injected.


## Primary and Secondary Beans

Primary is a qualifier that indicates that a bean is the primary bean to be selected in the case of multiple interface implementations.

Consider the following example:

```java
public interface ColorPicker {
    String color();
}
```

```kotlin
interface ColorPicker {
    fun color(): String
}
```

```groovy
interface ColorPicker {
    String color()
}
```

`ColorPicker` is implemented by these classes:

The Primary Bean

```java
import io.micronaut.context.annotation.Primary;
import jakarta.inject.Singleton;

@Primary
@Singleton
class Green implements ColorPicker {

    @Override
    public String color() {
        return "green";
    }
}
```

The Primary Bean

```kotlin
import io.micronaut.context.annotation.Primary
import jakarta.inject.Singleton

@Primary
@Singleton
class Green: ColorPicker {
    override fun color(): String {
        return "green"
    }
}
```

The Primary Bean

```groovy
import io.micronaut.context.annotation.Primary
import jakarta.inject.Singleton

@Primary
@Singleton
class Green implements ColorPicker {

    @Override
    String color() {
        return "green"
    }
}
```

The `Green` bean class implements `ColorPicker` and is annotated with `@Primary`.

Another Bean of the Same Type

```java
import jakarta.inject.Singleton;

@Singleton
public class Blue implements ColorPicker {

    @Override
    public String color() {
        return "blue";
    }
}
```

Another Bean of the Same Type

```kotlin
import jakarta.inject.Singleton

@Singleton
class Blue: ColorPicker {
    override fun color(): String {
        return "blue"
    }
}
```

Another Bean of the Same Type

```groovy
import jakarta.inject.Singleton

@Singleton
class Blue implements ColorPicker {

    @Override
    String color() {
        return "blue"
    }
}
```

The `Blue` bean class also implements `ColorPicker` and hence you have two possible candidates when injecting the `ColorPicker` interface. Since `Green` is the primary, it will always be favoured.

```java
@Controller("/testPrimary")
public class TestController {

    protected final ColorPicker colorPicker;

    public TestController(ColorPicker colorPicker) { // (1)
        this.colorPicker = colorPicker;
    }

    @Get
    public String index() {
        return colorPicker.color();
    }
}
```

```kotlin
@Controller("/test")
class TestController(val colorPicker: ColorPicker) { // (1)

    @Get
    fun index(): String {
        return colorPicker.color()
    }
}
```

```groovy
@Controller("/test")
class TestController {

    protected final ColorPicker colorPicker

    TestController(ColorPicker colorPicker) { // (1)
        this.colorPicker = colorPicker
    }

    @Get
    String index() {
        colorPicker.color()
    }
}
```

| **1** | Although there are two `ColorPicker` beans, `Green` gets injected due to the `@Primary` annotation. |
|---|---|

If multiple possible candidates are present and no `@Primary` is defined a NonUniqueBeanException is thrown.

In addition to `@Primary`, there is also a Secondary annotation which causes the opposite effect and allows de-prioritizing a bean.

|   | See the guide for Micronaut Patterns - Composite to learn more. |
|---|---|


## Injecting Any Bean

If you are not particular about which bean gets injected then you can use the @Any qualifier which will inject the first available bean, for example:

Injecting Any Instance

```java
@Inject @Any
Engine engine;
```

Injecting Any Instance

```kotlin
@Inject
@field:Any
lateinit var engine: Engine
```

Injecting Any Instance

```groovy
@Inject @Any
Engine engine
```

The @Any qualifier is typically used in conjunction with the BeanProvider interface to allow more dynamic use cases. For example the following `Vehicle` implementation will start the `Engine` if the bean is present:

Using BeanProvider with Any

```java
import io.micronaut.context.BeanProvider;
import io.micronaut.context.annotation.Any;
import jakarta.inject.Singleton;

@Singleton
public class Vehicle {
    final BeanProvider<Engine> engineProvider;

    public Vehicle(@Any BeanProvider<Engine> engineProvider) { // (1)
        this.engineProvider = engineProvider;
    }
    void start() {
        engineProvider.ifPresent(Engine::start); // (2)
    }
}
```

Using BeanProvider with Any

```kotlin
import io.micronaut.context.BeanProvider
import io.micronaut.context.annotation.Any
import jakarta.inject.Singleton

@Singleton
class Vehicle(@param:Any val engineProvider: BeanProvider<Engine>) { // (1)
    fun start() {
        engineProvider.ifPresent { it.start() } // (2)
    }
    fun startAll() {
        if (engineProvider.isPresent) { // (1)
            engineProvider.forEach { it.start() } // (2)
        }
}
```

Using BeanProvider with Any

```groovy
import io.micronaut.context.BeanProvider
import io.micronaut.context.annotation.Any
import jakarta.inject.Singleton

@Singleton
class Vehicle {
    final BeanProvider<Engine> engineProvider

    Vehicle(@Any BeanProvider<Engine> engineProvider) { // (1)
        this.engineProvider = engineProvider
    }
    void start() {
        engineProvider.ifPresent(Engine::start) // (2)
    }
}
```

| **1** | Use `@Any` to inject the BeanProvider |
|---|---|
| **2** | Call the `start` method if the underlying bean is present using the `ifPresent` method |

If there are multiple beans you can also adapt the behaviour. The following example starts all the engines installed in the `Vehicle` if any are present:

Using BeanProvider with Any

```java
void startAll() {
    if (engineProvider.isPresent()) { // (1)
        engineProvider.stream().forEach(Engine::start); // (2)
    }
}
```

Using BeanProvider with Any

```kotlin
fun startAll() {
    if (engineProvider.isPresent) { // (1)
        engineProvider.forEach { it.start() } // (2)
    }
```

Using BeanProvider with Any

```groovy
void startAll() {
    if (engineProvider.isPresent()) { // (1)
        engineProvider.each {it.start() } // (2)
    }
}
```

| **1** | Check if any beans present |
|---|---|
| **2** | If so iterate over each one via the `stream().forEach(..)` method, starting the engines |


## 3.8 Limiting Injectable Types

By default, when you annotate a bean with a scope such as `@Singleton` the bean class and all interfaces it implements and super classes it extends from become injectable via `@Inject`.

Consider the following example from the previous section on defining beans:

```java
@Singleton
public class V8Engine implements Engine {  // (3)
    @Override
    public String start() {
        return "Starting V8";
    }

    @Override
    public int getCylinders() {
        return 8;
    }

}
```

```kotlin
@Singleton
class V8Engine : Engine {

    override var cylinders: Int = 8

    override fun start(): String {
        return "Starting V8"
    }

}
```

```groovy
@Singleton
class V8Engine implements Engine { // (3)
    int cylinders = 8

    @Override
    String start() {
        "Starting V8"
    }
}
```

In the above case other classes in your application can choose to either inject the interface `Engine` or the concrete implementation `V8Engine`.

If this is undesirable you can use the `typed` member of the @Bean annotation to limit the exposed types. For example:

```java
@Singleton
@Bean(typed = Engine.class) // (1)
public class V8Engine implements Engine {  // (2)
    @Override
    public String start() {
        return "Starting V8";
    }

    @Override
    public int getCylinders() {
        return 8;
    }
}
```

```kotlin
@Singleton
@Bean(typed = [Engine::class]) // (1)
class V8Engine : Engine { // (2)
    override fun start(): String {
        return "Starting V8"
    }

    override val cylinders: Int = 8
}
```

```groovy
@Singleton
@Bean(typed = Engine) // (1)
class V8Engine implements Engine {  // (2)
    @Override
    String start() { "Starting V8" }

    @Override
    int getCylinders() { 8 }
}
```

| **1** | `@Bean(typed=..)` is used to only allow injection the interface `Engine` and not the concrete type |
|---|---|
| **2** | The class must implement the class or interface defined by `typed` otherwise a compilation error will occur |

The following test demonstrates the behaviour of `typed` using programmatic lookup and the BeanContext API:

```java
@MicronautTest
public class EngineSpec {
    @Inject
    BeanContext beanContext;

    @Test
    public void testEngine() {
        assertThrows(NoSuchBeanException.class, () ->
                beanContext.getBean(V8Engine.class) // (1)
        );
        final Engine engine = beanContext.getBean(Engine.class); // (2)
        assertTrue(engine instanceof V8Engine);
    }
}
```

```kotlin
@MicronautTest
class EngineSpec {
    @Inject
    lateinit var beanContext: BeanContext

    @Test
    fun testEngine() {
        assertThrows(NoSuchBeanException::class.java) {
            beanContext.getBean(V8Engine::class.java) // (1)
        }

        val engine = beanContext.getBean(Engine::class.java) // (2)
        assertTrue(engine is V8Engine)
    }
}
```

```groovy
class EngineSpec extends Specification {
    @Shared @AutoCleanup
    ApplicationContext beanContext = ApplicationContext.run()

    void 'test engine'() {
        when:'the class is looked up'
        beanContext.getBean(V8Engine) // (1)

        then:'a no such bean exception is thrown'
        thrown(NoSuchBeanException)

        and:'it is possible to lookup by the typed interface'
        beanContext.getBean(Engine) instanceof V8Engine // (2)
    }
}
```

| **1** | Trying to lookup `V8Engine` throws a NoSuchBeanException |
|---|---|
| **2** | Whilst looking up the `Engine` interface succeeds |


## 3.9 Scopes

Micronaut framework features an extensible bean scoping mechanism based on JSR-330. The following default scopes are supported:


## 3.9.1 Built-In Scopes

| Type | Description |
|---|---|
| @Singleton | Singleton scope indicates only one instance of the bean will exist |
| @Context | Context scope indicates that the bean will be created at the same time as the `ApplicationContext` (eager initialization) |
| @Prototype | Prototype scope indicates that a new instance of the bean is created each time it is injected |
| @Infrastructure | Infrastructure scope represents a bean that cannot be overridden or replaced using @Replaces because it is critical to the functioning of the system. |
| @ThreadLocal | `@ThreadLocal` scope is a custom scope that associates a bean per thread via a ThreadLocal |
| @Refreshable | `@Refreshable` scope is a custom scope that allows a bean’s state to be refreshed via the `/refresh` endpoint. |
| @RequestScope | `@RequestScope` scope is a custom scope that indicates a new instance of the bean is created and associated with each HTTP request |

|   | The @Prototype annotation is a synonym for @Bean because the default scope is prototype. |
|---|---|

Additional scopes can be added by defining a `@Singleton` bean that implements the CustomScope interface.

Note that when starting an ApplicationContext, by default `@Singleton`-scoped beans are created lazily and on-demand. This is by design to optimize startup time.

If this presents a problem for your use case you have the option of using the @Context annotation which binds the lifecycle of your object to the lifecycle of the ApplicationContext. In other words when the ApplicationContext is started your bean will be created.

Alternatively, annotate any `@Singleton`-scoped bean with @Parallel which allows parallel initialization of your bean without impacting overall startup time.

|   | If your bean fails to initialize in parallel, the application will be automatically shut down. |
|---|---|


## 3.9.1.1 Eager Initialization of Singletons

Eager initialization of `@Singleton` beans maybe desirable in certain scenarios, such as on AWS Lambda where more CPU resources are assigned to Lambda construction than execution.

You can specify whether to eagerly initialize `@Singleton`-scoped beans using the ApplicationContextBuilder interface:

Enabling Eager Initialization of Singletons

```java
public class Application {

    public static void main(String[] args) {
        Micronaut.build(args)
            .eagerInitSingletons(true) (1)
            .mainClass(Application.class)
            .start();
    }
}
```

| **1** | Setting eager init to `true` initializes all singletons |
|---|---|

When you use Micronaut framework in environments such as Serverless Functions, you will not have an Application class, and instead you extend a Micronaut-provided class. In those cases, Micronaut provides methods which you can override to enhance the ApplicationContextBuilder

Override of newApplicationContextBuilder()

```java
public class MyFunctionHandler extends MicronautRequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {
...
    @Nonnull
    @Override
    protected ApplicationContextBuilder newApplicationContextBuilder() {
        ApplicationContextBuilder builder = super.newApplicationContextBuilder();
        builder.eagerInitSingletons(true);
        return builder;
    }
    ...
}
```

@ConfigurationReader beans such as @EachProperty or @ConfigurationProperties are singleton beans. To eagerly init configuration but keep other `@Singleton`-scoped bean creation lazy, use `eagerInitConfiguration`:

Enabling Eager Initialization of Configuration

```java
public class Application {

    public static void main(String[] args) {
        Micronaut.build(args)
            .eagerInitConfiguration(true) (1)
            .mainClass(Application.class)
            .start();
    }
}
```

| **1** | Setting eager init to true initializes all configuration reader beans. |
|---|---|


## 3.9.2 Refreshable Scope

The Refreshable scope is a custom scope that allows a bean’s state to be refreshed via:

- `/refresh` endpoint.
- Publication of a RefreshEvent.

The following example illustrates `@Refreshable` scope behavior.

```java
@Refreshable // (1)
static class WeatherService {
    private String forecast;

    @PostConstruct
    public void init() {
        forecast = "Scattered Clouds " + new SimpleDateFormat("dd/MMM/yy HH:mm:ss.SSS").format(new Date());// (2)
    }

    public String latestForecast() {
        return forecast;
    }
}
```

```kotlin
@Refreshable // (1)
open class WeatherService {
    private var forecast: String? = null

    @PostConstruct
    open fun init() {
        forecast = "Scattered Clouds " + SimpleDateFormat("dd/MMM/yy HH:mm:ss.SSS").format(Date())// (2)
    }

    open fun latestForecast(): String? {
        return forecast
    }
}
```

```groovy
@Refreshable // (1)
static class WeatherService {

    String forecast

    @PostConstruct
    void init() {
        forecast = "Scattered Clouds ${new SimpleDateFormat("dd/MMM/yy HH:mm:ss.SSS").format(new Date())}" // (2)
    }

    String latestForecast() {
        return forecast
    }
}
```

| **1** | The `WeatherService` is annotated with `@Refreshable` scope which stores an instance until a refresh event is triggered |
|---|---|
| **2** | The value of the `forecast` property is set to a fixed value when the bean is created and won’t change until the bean is refreshed |

If you invoke `latestForecast()` twice, you will see identical responses such as `"Scattered Clouds 01/Feb/18 10:29.199"`.

When the `/refresh` endpoint is invoked or a RefreshEvent is published, the instance is invalidated and a new instance is created the next time the object is requested. For example:

```java
applicationContext.publishEvent(new RefreshEvent());
```

```kotlin
applicationContext.publishEvent(RefreshEvent())
```

```groovy
applicationContext.publishEvent(new RefreshEvent())
```


## 3.9.3 Scopes on Meta Annotations

Scopes can be defined on meta annotations that you can then apply to your classes. Consider the following example meta annotation:

Driver.java Annotation

```java
import io.micronaut.context.annotation.Requires;

import jakarta.inject.Singleton;
import java.lang.annotation.Documented;
import java.lang.annotation.Retention;

import static java.lang.annotation.RetentionPolicy.RUNTIME;

@Requires(classes = Car.class) // (1)
@Singleton // (2)
@Documented
@Retention(RUNTIME)
public @interface Driver {
}
```

Driver.java Annotation

```kotlin
import io.micronaut.context.annotation.Requires
import jakarta.inject.Singleton
import kotlin.annotation.AnnotationRetention.RUNTIME

@Requires(classes = [Car::class]) // (1)
@Singleton // (2)
@MustBeDocumented
@Retention(RUNTIME)
annotation class Driver
```

Driver.java Annotation

```groovy
import io.micronaut.context.annotation.Requires

import jakarta.inject.Singleton
import java.lang.annotation.Documented
import java.lang.annotation.Retention

import static java.lang.annotation.RetentionPolicy.RUNTIME

@Requires(classes = Car.class) // (1)
@Singleton // (2)
@Documented
@Retention(RUNTIME)
@interface Driver {
}
```

| **1** | The scope declares a requirement on a `Car` class using Requires |
|---|---|
| **2** | The annotation is declared as `@Singleton` |

In the example above the `@Singleton` annotation is applied to the `@Driver` annotation which results in every class that is annotated with `@Driver` being regarded as singleton.

Note that in this case it is not possible to alter the scope when the annotation is applied. For example, the following will not override the scope declared by `@Driver` and is invalid:

Declaring Another Scope

```java
@Driver
@Prototype
class Foo {}
```

For the scope to be overridable, instead use the DefaultScope annotation on `@Driver` which allows a default scope to be specified if none other is present:

Using @DefaultScope

```java
@Requires(classes = Car.class)
@DefaultScope(Singleton.class) (1)
@Documented
@Retention(RUNTIME)
public @interface Driver {
}
```

```groovy
@Requires(classes = Car.class)
@DefaultScope(Singleton.class) (1)
@Documented
@Retention(RUNTIME)
@interface Driver {
}
```

```kotlin
@Requires(classes = [Car::class])
@DefaultScope(Singleton::class) (1)
@Documented
@Retention(RUNTIME)
annotation class Driver
```

| **1** | DefaultScope declares the scope to use if none is specified |
|---|---|


## 3.10 Bean Factories

In many cases, you may want to make available as a bean a class that is not part of your codebase such as those provided by third-party libraries. In this case, you cannot annotate the compiled class. Instead, implement a @Factory.

A factory is a class annotated with the Factory annotation that provides one or more methods annotated with a bean scope annotation. Which annotation you use depends on what scope you want the bean to be in. See the section on bean scopes for more information.

|   | The factory has the default scope singleton and will be destroyed with the context. If you want to dispose the factory after it produces a bean, use @Prototype scope. |
|---|---|

The return types of methods annotated with a bean scope annotation are the bean types. This is best illustrated by an example:

```java
@Singleton
class CrankShaft {
}

class V8Engine implements Engine {
    private final int cylinders = 8;
    private final CrankShaft crankShaft;

    public V8Engine(CrankShaft crankShaft) {
        this.crankShaft = crankShaft;
    }

    @Override
    public String start() {
        return "Starting V8";
    }
}

@Factory
class EngineFactory {

    @Singleton
    Engine v8Engine(CrankShaft crankShaft) {
        return new V8Engine(crankShaft);
    }
}
```

```kotlin
@Singleton
internal class CrankShaft

internal class V8Engine(private val crankShaft: CrankShaft) : Engine {
    private val cylinders = 8

    override fun start(): String {
        return "Starting V8"
    }
}

@Factory
internal class EngineFactory {

    @Singleton
    fun v8Engine(crankShaft: CrankShaft): Engine {
        return V8Engine(crankShaft)
    }
}
```

```groovy
@Singleton
class CrankShaft {
}

class V8Engine implements Engine {
    final int cylinders = 8
    final CrankShaft crankShaft

    V8Engine(CrankShaft crankShaft) {
        this.crankShaft = crankShaft
    }

    @Override
    String start() {
        "Starting V8"
    }
}

@Factory
class EngineFactory {

    @Singleton
    Engine v8Engine(CrankShaft crankShaft) {
        new V8Engine(crankShaft)
    }
}
```

In this case, a `V8Engine` is created by the `EngineFactory` class' `v8Engine` method. Note that you can inject parameters into the method, and they will be resolved as beans. The resulting `V8Engine` bean will be a singleton.

A factory can have multiple methods annotated with bean scope annotations, each one returning a distinct bean type.

|   | If you take this approach you should not invoke other bean methods internally within the class. Instead, inject the types via parameters. |
|---|---|

|   | To allow the resulting bean to participate in the application context shutdown process, annotate the method with @Bean and set the `preDestroy` argument to the name of the method to be called to close the bean. |
|---|---|

### Beans from Fields

With Micronaut framework 3.0 or above it is also possible to produce beans from fields by declaring the @Bean annotation on a field.

Whilst generally this approach should be discouraged in favour for factory methods, which provide more flexibility it does simplify testing code. For example with bean fields you can easily produce mocks in your test code:

```java
import io.micronaut.context.annotation.*;
import io.micronaut.test.extensions.junit5.annotation.MicronautTest;
import org.junit.jupiter.api.Test;
import jakarta.inject.Inject;

import static org.junit.jupiter.api.Assertions.assertEquals;

@MicronautTest
public class VehicleMockSpec {
    @Requires(beans = VehicleMockSpec.class)
    @Bean @Replaces(Engine.class)
    Engine mockEngine = () -> "Mock Started"; // (1)

    @Inject Vehicle vehicle; // (2)

    @Test
    void testStartEngine() {
        final String result = vehicle.start();
        assertEquals("Mock Started", result); // (3)
    }
}
```

```kotlin
import io.micronaut.context.annotation.Bean
import io.micronaut.context.annotation.Replaces
import io.micronaut.test.annotation.MockBean
import io.micronaut.test.extensions.junit5.annotation.MicronautTest
import org.junit.jupiter.api.Assertions
import org.junit.jupiter.api.Test
import jakarta.inject.Inject

@MicronautTest
class VehicleMockSpec {
    @MockBean(Engine::class)
    val mockEngine: Engine = object : Engine { // (1)
        override fun start(): String {
            return "Mock Started"
        }
    }

    @Inject
    lateinit var vehicle : Vehicle // (2)

    @Test
    fun testStartEngine() {
        val result = vehicle.start()
        Assertions.assertEquals("Mock Started", result) // (3)
    }
}
```

```groovy
import io.micronaut.context.annotation.*
import io.micronaut.test.extensions.spock.annotation.MicronautTest
import spock.lang.Specification
import jakarta.inject.Inject

@MicronautTest
class VehicleMockSpec extends Specification {
    @Requires(beans=VehicleMockSpec.class)
    @Bean @Replaces(Engine.class)
    Engine mockEngine = {-> "Mock Started" } as Engine  // (1)

    @Inject Vehicle vehicle // (2)

    void "test start engine"() {
        given:
        final String result = vehicle.start()

        expect:
        result == "Mock Started" // (3)
    }
}
```

| **1** | A bean is defined from a field that replaces the existing `Engine`. |
|---|---|
| **2** | The `Vehicle` is injected. |
| **3** | The code asserts that the mock implementation is called. |

Note that only public or package protected fields are supported on non-primitive types. If the field is `static`, `private`, or `protected` a compilation error will occur.

|   | If the bean method/field includes a scope or a qualifier any scope or qualifiers from the type will be omitted. |
|---|---|

|   | Qualifiers from the factory instance aren’t inherited to the beans. |
|---|---|

#### Primitive Beans and Arrays

Since Micronaut framework 3.1 it is possible to define and inject primitive types and array types from factories.

For example:

```java
import io.micronaut.context.annotation.Bean;
import io.micronaut.context.annotation.Factory;
import jakarta.inject.Named;

@Factory
class CylinderFactory {
    @Bean
    @Named("V8") // (1)
    final int v8 = 8;

    @Bean
    @Named("V6") // (1)
    final int v6 = 6;
}
```

```kotlin
import io.micronaut.context.annotation.Bean
import io.micronaut.context.annotation.Factory
import jakarta.inject.Named

@Factory
class CylinderFactory {
    @get:Bean
    @get:Named("V8") // (1)
    val v8 = 8

    @get:Bean
    @get:Named("V6") // (1)
    val v6 = 6
}
```

```groovy
import io.micronaut.context.annotation.Bean
import io.micronaut.context.annotation.Factory
import jakarta.inject.Named

@Factory
class CylinderFactory {
    @Bean
    @Named("V8") // (1)
    final int v8 = 8

    @Bean
    @Named("V6") // (1)
    final int v6 = 6
}
```

| **1** | Two primitive integer beans are defined with different names |
|---|---|

Primitive beans can be injected like any other bean:

```java
import jakarta.inject.Named;
import jakarta.inject.Singleton;

@Singleton
public class V8Engine {
    private final int cylinders;

    public V8Engine(@Named("V8") int cylinders) { // (1)
        this.cylinders = cylinders;
    }

    public int getCylinders() {
        return cylinders;
    }
}
```

```kotlin
import jakarta.inject.Named
import jakarta.inject.Singleton

@Singleton
class V8Engine(
    @param:Named("V8") val cylinders: Int // (1)
)
```

```groovy
import jakarta.inject.Named
import jakarta.inject.Singleton

@Singleton
class V8Engine {
    private final int cylinders

    V8Engine(@Named("V8") int cylinders) { // (1)
        this.cylinders = cylinders
    }

    int getCylinders() {
        return cylinders
    }
}
```

Note that primitive beans and primitive array beans have the following limitations:

- AOP advice cannot be applied to primitives or wrapper types
- Due to the above custom scopes that proxy are not supported
- The `@Bean(preDestroy=..)` member is not supported

### Programmatically Disabling Beans

Factory methods can throw DisabledBeanException to conditionally disable beans. Using @Requires should always be the preferred method to conditionally create beans; throwing an exception in a factory method should only be done if using @Requires is not possible.

For example:

```java
public interface Engine {
    Integer getCylinders();
}

@EachProperty("engines")
public class EngineConfiguration implements Toggleable {

    private boolean enabled = true;
    private Integer cylinders;

    @NotNull
    public Integer getCylinders() {
        return cylinders;
    }

    public void setCylinders(Integer cylinders) {
        this.cylinders = cylinders;
    }

    @Override
    public boolean isEnabled() {
        return enabled;
    }

    public void setEnabled(boolean enabled) {
        this.enabled = enabled;
    }

}

@Factory
public class EngineFactory {

    @EachBean(EngineConfiguration.class)
    public Engine buildEngine(EngineConfiguration engineConfiguration) {
        if (engineConfiguration.isEnabled()) {
            return engineConfiguration::getCylinders;
        } else {
            throw new DisabledBeanException("Engine configuration disabled");
        }
    }
}
```

```kotlin
interface Engine {
    fun getCylinders(): Int
}

@EachProperty("engines")
class EngineConfiguration : Toggleable {

    var enabled = true

    @NotNull
    val cylinders: Int? = null

    override fun isEnabled(): Boolean {
        return enabled
    }
}

@Factory
class EngineFactory {

    @EachBean(EngineConfiguration::class)
    fun buildEngine(engineConfiguration: EngineConfiguration): Engine? {
        return if (engineConfiguration.isEnabled) {
            object : Engine {
                override fun getCylinders(): Int {
                    return engineConfiguration.cylinders!!
                }
            }
        } else {
            throw DisabledBeanException("Engine configuration disabled")
        }
    }
}
```

```groovy
interface Engine {
    Integer getCylinders()
}

@EachProperty("engines")
class EngineConfiguration implements Toggleable {
    boolean enabled = true
    @NotNull
    Integer cylinders
}

@Factory
class EngineFactory {

    @EachBean(EngineConfiguration)
    Engine buildEngine(EngineConfiguration engineConfiguration) {
        if (engineConfiguration.enabled) {
            (Engine) { -> engineConfiguration.cylinders }
        } else {
            throw new DisabledBeanException("Engine configuration disabled")
        }
    }
}
```

### Injection Point

A common use case with factories is to take advantage of annotation metadata from the point at which an object is injected such that behaviour can be modified based on said metadata.

Consider an annotation such as the following:

```java
@Documented
@Retention(RUNTIME)
@Target(ElementType.PARAMETER)
public @interface Cylinders {
    int value() default 8;
}
```

```kotlin
@MustBeDocumented
@Retention(AnnotationRetention.RUNTIME)
@Target(AnnotationTarget.VALUE_PARAMETER)
annotation class Cylinders(val value: Int = 8)
```

```groovy
@Documented
@Retention(RUNTIME)
@Target(ElementType.PARAMETER)
@interface Cylinders {
    int value() default 8
}
```

The above annotation could be used to customize the type of engine we want to inject into a vehicle at the point at which the injection point is defined:

```java
@Singleton
class Vehicle {

    private final Engine engine;

    Vehicle(@Cylinders(6) Engine engine) {
        this.engine = engine;
    }

    String start() {
        return engine.start();
    }
}
```

```kotlin
@Singleton
internal class Vehicle(@param:Cylinders(6) private val engine: Engine) {
    fun start(): String {
        return engine.start()
    }
}
```

```groovy
@Singleton
class Vehicle {

    private final Engine engine

    Vehicle(@Cylinders(6) Engine engine) {
        this.engine = engine
    }

    String start() {
        return engine.start()
    }
}
```

The above `Vehicle` class specifies an annotation value of `@Cylinders(6)` indicating an `Engine` of six cylinders is required.

To implement this use case, define a factory that accepts the InjectionPoint instance to analyze the defined annotation values:

```java
@Factory
class EngineFactory {

    @Prototype
    Engine v8Engine(InjectionPoint<?> injectionPoint, CrankShaft crankShaft) { // (1)
        final int cylinders = injectionPoint
                .getAnnotationMetadata()
                .intValue(Cylinders.class).orElse(8); // (2)
        switch (cylinders) { // (3)
            case 6:
                return new V6Engine(crankShaft);
            case 8:
                return new V8Engine(crankShaft);
            default:
                throw new IllegalArgumentException("Unsupported number of cylinders specified: " + cylinders);
        }
    }
}
```

```kotlin
@Factory
internal class EngineFactory {

    @Prototype
    fun v8Engine(injectionPoint: InjectionPoint<*>, crankShaft: CrankShaft): Engine { // (1)
        val cylinders = injectionPoint
                .annotationMetadata
                .intValue(Cylinders::class.java).orElse(8) // (2)
        return when (cylinders) { // (3)
            6 -> V6Engine(crankShaft)
            8 -> V8Engine(crankShaft)
            else -> throw IllegalArgumentException("Unsupported number of cylinders specified: $cylinders")
        }
    }
}
```

```groovy
@Factory
class EngineFactory {

    @Prototype
    Engine v8Engine(InjectionPoint<?> injectionPoint, CrankShaft crankShaft) { // (1)
        final int cylinders = injectionPoint
                .getAnnotationMetadata()
                .intValue(Cylinders.class).orElse(8) // (2)
        switch (cylinders) { // (3)
            case 6:
                return new V6Engine(crankShaft)
            case 8:
                return new V8Engine(crankShaft)
            default:
                throw new IllegalArgumentException("Unsupported number of cylinders specified: $cylinders")
        }
    }
}
```

| **1** | The factory method defines a parameter of type InjectionPoint. |
|---|---|
| **2** | The annotation metadata is used to obtain the value of the `@Cylinder` annotation |
| **3** | The value is used to construct an engine, throwing an exception if an engine cannot be constructed. |

|   | It is important to note that the factory is declared as @Prototype scope so the method is invoked for each injection point. If the `V8Engine` and `V6Engine` types are required to be singletons, the factory should use a Map to ensure the objects are only constructed once. |
|---|---|


## 3.11 Conditional Beans

At times, you may want a bean to load conditionally based on various potential factors including the classpath, the configuration, the presence of other beans, etc.

The Requires annotation provides the ability to define one or many conditions on a bean.

Consider the following example:

Using @Requires

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

Using @Requires

```kotlin
@Singleton
@Requirements(Requires(beans = [DataSource::class]), Requires(property = "datasource.url"))
class JdbcBookService(internal var dataSource: DataSource) : BookService {
```

Using @Requires

```groovy
@Singleton
@Requires(beans = DataSource)
@Requires(property = "datasource.url")
class JdbcBookService implements BookService {

    DataSource dataSource
```

The above bean defines two requirements. The first indicates that a `DataSource` bean must be present for the bean to load. The second requirement ensures that the `datasource.url` property is set before loading the `JdbcBookService` bean.

If multiple beans require the same combination of requirements, you can define a meta-annotation with the requirements:

Using a @Requires meta-annotation

```java
@Documented
@Retention(RetentionPolicy.RUNTIME)
@Target({ElementType.PACKAGE, ElementType.TYPE})
@Requires(beans = DataSource.class)
@Requires(property = "datasource.url")
public @interface RequiresJdbc {
}
```

Using a @Requires meta-annotation

```kotlin
@Documented
@Retention(AnnotationRetention.RUNTIME)
@Target(AnnotationTarget.CLASS, AnnotationTarget.FILE)
@Requirements(Requires(beans = [DataSource::class]), Requires(property = "datasource.url"))
annotation class RequiresJdbc
```

Using a @Requires meta-annotation

```groovy
@Documented
@Retention(RetentionPolicy.RUNTIME)
@Target([ElementType.PACKAGE, ElementType.TYPE])
@Requires(beans = DataSource)
@Requires(property = "datasource.url")
@interface RequiresJdbc {
}
```

In the above example the `RequiresJdbc` annotation can be used on the `JdbcBookService` instead:

Using a meta-annotation

```java
@RequiresJdbc
public class JdbcBookService implements BookService {
    ...
}
```

If you have multiple beans that need to fulfill a given requirement before loading, you may want to consider a bean configuration group, as explained in the next section.
