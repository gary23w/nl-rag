---
title: "Micronaut Core (part 8/27)"
source: https://docs.micronaut.io/latest/guide/index.html
domain: micronaut
license: CC-BY-SA-4.0
tags: micronaut framework, micronaut jvm, compile-time injection, microservices framework
fetched: 2026-07-02
part: 8/27
---

## 4.8 Using @EachProperty to Drive Configuration

The @ConfigurationProperties annotation is great for a single configuration class, but sometimes you want multiple instances, each with its own distinct configuration. That is where EachProperty comes in.

The @EachProperty annotation creates a `ConfigurationProperties` bean for each sub-property within the given name. As an example consider the following class:

Using @EachProperty

```java
import java.net.URI;
import java.net.URISyntaxException;

import io.micronaut.context.annotation.Parameter;
import io.micronaut.context.annotation.EachProperty;

@EachProperty("test.datasource")  // (1)
public class DataSourceConfiguration {

    private final String name;
    private URI url = new URI("localhost");

    public DataSourceConfiguration(@Parameter String name) // (2)
            throws URISyntaxException {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public URI getUrl() { // (3)
        return url;
    }

    public void setUrl(URI url) {
        this.url = url;
    }
}
```

Using @EachProperty

```kotlin
import io.micronaut.context.annotation.EachProperty
import io.micronaut.context.annotation.Parameter
import java.net.URI
import java.net.URISyntaxException

@EachProperty("test.datasource")  // (1)
class DataSourceConfiguration
@Throws(URISyntaxException::class)
constructor(@param:Parameter val name: String) { // (2)
    var url = URI("localhost") // (3)
}
```

Using @EachProperty

```groovy
import io.micronaut.context.annotation.EachProperty
import io.micronaut.context.annotation.Parameter

@EachProperty("test.datasource") // (1)
class DataSourceConfiguration {

    final String name
    URI url = new URI("localhost") // (3)

    DataSourceConfiguration(@Parameter String name) // (2)
            throws URISyntaxException {
        this.name = name
    }
}
```

| **1** | The `@EachProperty` annotation defines the property name to be handled. |
|---|---|
| **2** | The `@Parameter` annotation can be used to inject the name of the sub-property that defines the name of the bean (which is also the bean qualifier) |
| **3** | Each property of the bean is bound to configuration. |

|   | Micronaut configuration uses kebap case, not lower camel case. For example, using `@EachProperty("my-bean")` works, but `@EachProperty("myBean")` fails. |
|---|---|

The above `DataSourceConfiguration` defines a `url` property to configure one or more data sources. The URLs themselves can be configured using any of the PropertySource instances evaluated to Micronaut:

Providing Configuration to @EachProperty

```java
ApplicationContext applicationContext = ApplicationContext.run(PropertySource.of(
        "test",
        CollectionUtils.mapOf(
                "test.datasource.one.url", "jdbc:mysql://localhost/one",
                "test.datasource.two.url", "jdbc:mysql://localhost/two")
));
```

Providing Configuration to @EachProperty

```kotlin
val applicationContext = ApplicationContext.run(PropertySource.of(
        "test",
        mapOf(
                "test.datasource.one.url" to "jdbc:mysql://localhost/one",
                "test.datasource.two.url" to "jdbc:mysql://localhost/two"
        )
))
```

Providing Configuration to @EachProperty

```groovy
ApplicationContext applicationContext = ApplicationContext.run(PropertySource.of(
        "test",
        [
                "test.datasource.one.url": "jdbc:mysql://localhost/one",
                "test.datasource.two.url": "jdbc:mysql://localhost/two"
        ]
))
```

In the above example two data sources (called `one` and `two`) are defined under the `test.datasource` prefix defined earlier in the `@EachProperty` annotation. Each of these configuration entries triggers the creation of a new `DataSourceConfiguration` bean such that the following test succeeds:

Evaluating Beans Built by @EachProperty

```java
Collection<DataSourceConfiguration> beansOfType = applicationContext.getBeansOfType(DataSourceConfiguration.class);
assertEquals(2, beansOfType.size()); // (1)

DataSourceConfiguration firstConfig = applicationContext.getBean(
        DataSourceConfiguration.class,
        Qualifiers.byName("one") // (2)
);

assertEquals(new URI("jdbc:mysql://localhost/one"), firstConfig.getUrl());
```

Evaluating Beans Built by @EachProperty

```kotlin
val beansOfType = applicationContext.getBeansOfType(DataSourceConfiguration::class.java)
beansOfType.size shouldBe 2 // (1)

val firstConfig = applicationContext.getBean(
        DataSourceConfiguration::class.java,
        Qualifiers.byName("one") // (2)
)

firstConfig.url shouldBe URI("jdbc:mysql://localhost/one")
```

Evaluating Beans Built by @EachProperty

```groovy
when:
Collection<DataSourceConfiguration> beansOfType = applicationContext.getBeansOfType(DataSourceConfiguration.class)

then:
beansOfType.size() == 2 // (1)

when:
DataSourceConfiguration firstConfig = applicationContext.getBean(
        DataSourceConfiguration.class,
        Qualifiers.byName("one") // (2)
)

then:
new URI("jdbc:mysql://localhost/one") == firstConfig.getUrl()
```

| **1** | All beans of type `DataSourceConfiguration` can be retrieved using `getBeansOfType` |
|---|---|
| **2** | Individual beans can be retrieved by using the `byName` qualifier. |

### List-Based Binding

The default behavior of @EachProperty is to bind from a map style of configuration, where the key is the named qualifier of the bean and the value is the data to bind from. For cases where map style configuration doesn’t make sense, it is possible to inform the Micronaut framework that the class is bound from a list. Simply set the `list` member on the annotation to true.

@EachProperty List Example

```java
import io.micronaut.context.annotation.EachProperty;
import io.micronaut.context.annotation.Parameter;
import io.micronaut.core.order.Ordered;

import java.time.Duration;

@EachProperty(value = "ratelimits", list = true) // (1)
public class RateLimitsConfiguration implements Ordered { // (2)

    private final Integer index;
    private Duration period;
    private Integer limit;

    RateLimitsConfiguration(@Parameter Integer index) { // (3)
        this.index = index;
    }

    @Override
    public int getOrder() {
        return index;
    }

    public Duration getPeriod() {
        return period;
    }

    public void setPeriod(Duration period) {
        this.period = period;
    }

    public Integer getLimit() {
        return limit;
    }

    public void setLimit(Integer limit) {
        this.limit = limit;
    }
}
```

@EachProperty List Example

```kotlin
import io.micronaut.context.annotation.EachProperty
import io.micronaut.context.annotation.Parameter
import io.micronaut.core.order.Ordered
import java.time.Duration

@EachProperty(value = "ratelimits", list = true) // (1)
class RateLimitsConfiguration
    constructor(@param:Parameter private val index: Int) // (3)
    : Ordered { // (2)

    var period: Duration? = null
    var limit: Int? = null

    override fun getOrder(): Int {
        return index
    }
}
```

@EachProperty List Example

```groovy
import io.micronaut.context.annotation.EachProperty
import io.micronaut.context.annotation.Parameter
import io.micronaut.core.order.Ordered

import java.time.Duration

@EachProperty(value = "ratelimits", list = true) // (1)
class RateLimitsConfiguration implements Ordered { // (2)

    private final Integer index
    Duration period
    Integer limit

    RateLimitsConfiguration(@Parameter Integer index) { // (3)
        this.index = index
    }

    @Override
    int getOrder() {
        index
    }
}
```

| **1** | The `list` member of the annotation is set to `true` |
|---|---|
| **2** | Implement `Ordered` if order matters when retrieving the beans |
| **3** | The index is injected into the constructor |


## 4.9 Using @EachBean to Drive Configuration

The @EachProperty annotation is a great way to drive dynamic configuration, but typically you want to inject that configuration into another bean that depends on it. Injecting a single instance with a hard-coded qualifier is not a great solution, hence `@EachProperty` is typically used in combination with @EachBean:

Using @EachBean

```java
@Factory // (1)
public class DataSourceFactory {

    @EachBean(DataSourceConfiguration.class) // (2)
    DataSource dataSource(DataSourceConfiguration configuration) { // (3)
        URI url = configuration.getUrl();
        return new DataSource(url);
    }
```

Using @EachBean

```kotlin
@Factory // (1)
class DataSourceFactory {

    @EachBean(DataSourceConfiguration::class) // (2)
    internal fun dataSource(configuration: DataSourceConfiguration): DataSource { // (3)
        val url = configuration.url
        return DataSource(url)
    }
```

Using @EachBean

```groovy
@Factory // (1)
class DataSourceFactory {

    @EachBean(DataSourceConfiguration) // (2)
    DataSource dataSource(DataSourceConfiguration configuration) { // (3)
        URI url = configuration.url
        return new DataSource(url)
    }
```

| **1** | The above example defines a bean Factory that creates instances of `javax.sql.DataSource`. |
|---|---|
| **2** | The @EachBean annotation indicates that a new `DataSource` bean will be created for each `DataSourceConfiguration` defined in the previous section. |
| **3** | The `DataSourceConfiguration` instance is injected as a method argument and used to drive the configuration of each `javax.sql.DataSource` |

|   | `@EachBean` requires that the parent bean has a `@Named` qualifier, since the qualifier is inherited by each bean created by `@EachBean`. |
|---|---|

In other words, to retrieve the `DataSource` created by `test.datasource.one` you can do:

Using a Qualifier

```java
Collection<DataSource> beansOfType = applicationContext.getBeansOfType(DataSource.class);
assertEquals(2, beansOfType.size()); // (1)

DataSource firstConfig = applicationContext.getBean(
        DataSource.class,
        Qualifiers.byName("one") // (2)
);
```

Using a Qualifier

```kotlin
val beansOfType = applicationContext.getBeansOfType(DataSource::class.java)
beansOfType.size shouldBe 2 // (1)

val firstConfig = applicationContext.getBean(
        DataSource::class.java,
        Qualifiers.byName("one") // (2)
)
```

Using a Qualifier

```groovy
when:
Collection<DataSource> beansOfType = applicationContext.getBeansOfType(DataSource)

then:
beansOfType.size() == 2 // (1)

when:
DataSource firstConfig = applicationContext.getBean(
        DataSource,
        Qualifiers.byName("one") // (2)
)
```

| **1** | We demonstrate here that there are indeed two data sources. How can we get one in particular? |
|---|---|
| **2** | By using `Qualifiers.byName("one")`, we can select which of the two beans we’d like to reference. |


## 4.10 Immutable Configuration

Since 1.3, Micronaut framework supports the definition of immutable configuration. Immutable configuration with an interface requires the Micronaut Context dependency.

`implementation("io.micronaut:micronaut-context")` `<dependency> <groupId>io.micronaut</groupId> <artifactId>micronaut-context</artifactId> </dependency>`

`micronaut-context` is a transitive dependency of `micronaut-http`. If you use a Micronaut HTTP runtime, your project already includes the `Micronaut-context` dependency.

There are two ways to define immutable configuration. The preferred way is to define an interface annotated with @ConfigurationProperties. For example:

@ConfigurationProperties Example

```java
import io.micronaut.context.annotation.ConfigurationProperties;
import io.micronaut.context.annotation.Requires;
import io.micronaut.core.bind.annotation.Bindable;

import jakarta.validation.constraints.Min;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import java.util.Optional;

@ConfigurationProperties("my.engine") // (1)
public interface EngineConfig {

    @Bindable(defaultValue = "Ford") // (2)
    @NotBlank // (3)
    String getManufacturer();

    @Min(1L)
    int getCylinders();

    @NotNull
    CrankShaft getCrankShaft(); // (4)

    @ConfigurationProperties("crank-shaft")
    interface CrankShaft { // (5)
        Optional<Double> getRodLength(); // (6)
    }
}
```

@ConfigurationProperties Example

```kotlin
import io.micronaut.context.annotation.ConfigurationProperties
import io.micronaut.core.bind.annotation.Bindable
import jakarta.validation.constraints.Min
import jakarta.validation.constraints.NotBlank
import jakarta.validation.constraints.NotNull

@ConfigurationProperties("my.engine") // (1)
interface EngineConfig {

    @get:Bindable(defaultValue = "Ford") // (2)
    @get:NotBlank // (3)
    val manufacturer: String

    @get:Min(1L)
    val cylinders: Int

    @get:NotNull
    val crankShaft: CrankShaft // (4)

    @ConfigurationProperties("crank-shaft")
    interface CrankShaft { // (5)
        val rodLength: Double? // (6)
    }
}
```

@ConfigurationProperties Example

```groovy
import io.micronaut.context.annotation.ConfigurationProperties
import io.micronaut.core.bind.annotation.Bindable

import jakarta.validation.constraints.Min
import jakarta.validation.constraints.NotBlank
import jakarta.validation.constraints.NotNull

@ConfigurationProperties("my.engine") // (1)
interface EngineConfig {

    @Bindable(defaultValue = "Ford") // (2)
    @NotBlank // (3)
    String getManufacturer()

    @Min(1L)
    int getCylinders()

    @NotNull
    CrankShaft getCrankShaft() // (4)

    @ConfigurationProperties("crank-shaft")
    static interface CrankShaft { // (5)
        Optional<Double> getRodLength() // (6)
    }
}
```

| **1** | The @ConfigurationProperties annotation takes the configuration prefix and is declared on an interface |
|---|---|
| **2** | You can use @Bindable to set a default value |
| **3** | Validation annotations can also be used |
| **4** | You can also specify references to other @ConfigurationProperties beans. |
| **5** | You can nest immutable configuration |
| **6** | Optional configuration can be indicated by returning an `Optional` or specifying `@Nullable` |

In this case the Micronaut framework provides a compile-time implementation that delegates all getters to call the `getProperty(..)` method of the Environment interface.

This has the advantage that if the application configuration is refreshed (for example by invoking the `/refresh` endpoint), the injected interface automatically sees the new values.

|   | If you try to specify any other abstract method other than a getter, a compilation error occurs (default methods are supported). |
|---|---|

Another way to implement immutable configuration is to define a class and use the @ConfigurationInject annotation on a constructor of a @ConfigurationProperties or @EachProperty bean.

For example:

@ConfigurationProperties Example

```java
import io.micronaut.context.annotation.Requires;
import io.micronaut.core.bind.annotation.Bindable;
import org.jspecify.annotations.Nullable;
import io.micronaut.context.annotation.ConfigurationInject;
import io.micronaut.context.annotation.ConfigurationProperties;

import jakarta.validation.constraints.Min;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import java.util.Optional;

@ConfigurationProperties("my.engine") // (1)
public class EngineConfig {

    private final String manufacturer;
    private final int cylinders;
    private final CrankShaft crankShaft;

    @ConfigurationInject // (2)
    public EngineConfig(
            @Bindable(defaultValue = "Ford") @NotBlank String manufacturer, // (3)
            @Min(1L) int cylinders, // (4)
            @NotNull CrankShaft crankShaft) {
        this.manufacturer = manufacturer;
        this.cylinders = cylinders;
        this.crankShaft = crankShaft;
    }

    public String getManufacturer() {
        return manufacturer;
    }

    public int getCylinders() {
        return cylinders;
    }

    public CrankShaft getCrankShaft() {
        return crankShaft;
    }

    @ConfigurationProperties("crank-shaft")
    public static class CrankShaft { // (5)
        private final Double rodLength; // (6)

        @ConfigurationInject
        public CrankShaft(@Nullable Double rodLength) {
            this.rodLength = rodLength;
        }

        public Optional<Double> getRodLength() {
            return Optional.ofNullable(rodLength);
        }
    }
}
```

@ConfigurationProperties Example

```kotlin
import io.micronaut.context.annotation.ConfigurationInject
import io.micronaut.context.annotation.ConfigurationProperties
import io.micronaut.core.bind.annotation.Bindable
import java.util.Optional
import jakarta.validation.constraints.Min
import jakarta.validation.constraints.NotBlank
import jakarta.validation.constraints.NotNull

@ConfigurationProperties("my.engine") // (1)
data class EngineConfig @ConfigurationInject // (2)
    constructor(
        @Bindable(defaultValue = "Ford") @NotBlank val manufacturer: String, // (3)
        @Min(1) val cylinders: Int, // (4)
        @NotNull val crankShaft: CrankShaft) {

    @ConfigurationProperties("crank-shaft")
    data class CrankShaft @ConfigurationInject
    constructor(// (5)
            private val rodLength: Double? // (6)
    ) {

        fun getRodLength(): Optional<Double> {
            return Optional.ofNullable(rodLength)
        }
    }
}
```

@ConfigurationProperties Example

```groovy
import io.micronaut.context.annotation.ConfigurationInject
import io.micronaut.context.annotation.ConfigurationProperties
import io.micronaut.core.bind.annotation.Bindable

import jakarta.annotation.Nullable
import jakarta.validation.constraints.Min
import jakarta.validation.constraints.NotBlank
import jakarta.validation.constraints.NotNull

@ConfigurationProperties("my.engine") // (1)
class EngineConfig {

    final String manufacturer
    final int cylinders
    final CrankShaft crankShaft

    @ConfigurationInject // (2)
    EngineConfig(
            @Bindable(defaultValue = "Ford") @NotBlank String manufacturer, // (3)
            @Min(1L) int cylinders, // (4)
            @NotNull CrankShaft crankShaft) {
        this.manufacturer = manufacturer
        this.cylinders = cylinders
        this.crankShaft = crankShaft
    }

    @ConfigurationProperties("crank-shaft")
    static class CrankShaft { // (5)
        private final Double rodLength // (6)

        @ConfigurationInject
        CrankShaft(@Nullable Double rodLength) {
            this.rodLength = rodLength
        }

        Optional<Double> getRodLength() {
            Optional.ofNullable(rodLength)
        }
    }
}
```

| **1** | The @ConfigurationProperties annotation takes the configuration prefix |
|---|---|
| **2** | The @ConfigurationInject annotation is defined on the constructor |
| **3** | You can use @Bindable to set a default value |
| **4** | Validation annotations can be used too |
| **5** | You can nest immutable configuration |
| **6** | Optional configuration can be indicated with `@Nullable` |

The @ConfigurationInject annotation provides a hint to the Micronaut framework to prioritize binding values from configuration instead of injecting beans.

|   | Using this approach, to make the configuration refreshable, add the @Refreshable annotation to the class as well. This allows the bean to be re-created in the case of a runtime configuration refresh event. |
|---|---|

There are a few exceptions to this rule. Micronaut framework will not perform configuration binding for a parameter if any of these conditions is met:

- The parameter is annotated with `@Value` (explicit binding)
- The parameter is annotated with `@Property` (explicit binding)
- The parameter is annotated with `@Parameter` (parameterized bean handling)
- The parameter is annotated with `@Inject` (generic bean injection)
- The type of the parameter is annotated with a bean scope (such as `@Singleton`)

Once you have prepared a type-safe configuration it can be injected into your beans like any other bean:

@ConfigurationProperties Dependency Injection

```java
@Singleton
public class Engine {
    private final EngineConfig config;

    public Engine(EngineConfig config) {// (1)
        this.config = config;
    }

    public int getCylinders() {
        return config.getCylinders();
    }

    public String start() {// (2)
        return getConfig().getManufacturer() + " Engine Starting V" + getConfig().getCylinders() +
                " [rodLength=" + getConfig().getCrankShaft().getRodLength().orElse(6.0d) + "]";
    }

    public final EngineConfig getConfig() {
        return config;
    }
}
```

@ConfigurationProperties Dependency Injection

```kotlin
@Singleton
class Engine(val config: EngineConfig)// (1)
{
    val cylinders: Int
        get() = config.cylinders

    fun start(): String {// (2)
        return  "${config.manufacturer} Engine Starting V${config.cylinders} [rodLength=${config.crankShaft.getRodLength().orElse(6.0)}]"
    }
}
```

@ConfigurationProperties Dependency Injection

```groovy
@Singleton
class Engine {
    private final EngineConfig config

    Engine(EngineConfig config) {// (1)
        this.config = config
    }

    int getCylinders() {
        return config.cylinders
    }

    String start() {// (2)
        return "$config.manufacturer Engine Starting V$config.cylinders [rodLength=${config.crankShaft.rodLength.orElse(6.0d)}]"
    }

    final EngineConfig getConfig() {
        return config
    }
}
```

| **1** | Inject the `EngineConfig` bean |
|---|---|
| **2** | Use the configuration properties |

Configuration values can then be supplied when running the application. For example:

Supply Configuration

```java
ApplicationContext applicationContext = ApplicationContext.run(Map.of(
    "spec.name", "VehicleImmutableSpec",
        "my.engine.cylinders", "8",
        "my.engine.crank-shaft.rod-length", "7.0"
));

Vehicle vehicle = applicationContext.getBean(Vehicle.class);
System.out.println(vehicle.start());
```

Supply Configuration

```kotlin
val map = mapOf(
        "my.engine.cylinders" to "8",
        "my.engine.crank-shaft.rod-length" to "7.0"
)
val applicationContext = ApplicationContext.run(map)

val vehicle = applicationContext.getBean(Vehicle::class.java)
println(vehicle.start())
```

Supply Configuration

```groovy
ApplicationContext applicationContext = ApplicationContext.run(
        "my.engine.cylinders": "8",
        "my.engine.crank-shaft.rod-length": "7.0"
)

Vehicle vehicle = applicationContext.getBean(Vehicle)
System.out.println(vehicle.start())
```

The above example prints: `"Ford Engine Starting V8 [rodLength=7B.0]"`

#### Using Java Record Classes to define immutable configuration

For Java language applications, it’s also possible to use Java Record Classes for immutable configuration with @ConfigurationProperties. For example:

Java Record Example

```java
import io.micronaut.context.annotation.ConfigurationProperties;
import io.micronaut.context.annotation.Requires;
import org.jspecify.annotations.NonNull;
import jakarta.validation.constraints.NotNull;
import java.math.BigDecimal;

@ConfigurationProperties("vat")
public record ValueAddedTaxConfiguration(
    @NonNull @NotNull BigDecimal percentage) { // (1)
}
```

| **1** | The `percentage` field defines a configuration property for "vat" |
|---|---|

|   | From a performance perspective Java records are better than interfaces. |
|---|---|


## Customizing accessors

As already explained in Change accessors style, it is also possible to customize the accessors when creating immutable configuration properties:

```java
import io.micronaut.context.annotation.ConfigurationProperties;
import io.micronaut.core.annotation.AccessorsStyle;
import io.micronaut.core.bind.annotation.Bindable;

import jakarta.validation.constraints.Min;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import java.util.Optional;

@ConfigurationProperties("my.engine") (1)
@AccessorsStyle(readPrefixes = "read") (2)
public interface EngineConfigAccessors {

    @Bindable(defaultValue = "Ford")
    @NotBlank
    String readManufacturer(); (3)

    @Min(1L)
    int readCylinders(); (3)

    @NotNull
    CrankShaft readCrankShaft(); (3)

    @ConfigurationProperties("crank-shaft")
    @AccessorsStyle(readPrefixes = "read") (4)
    interface CrankShaft {
        Optional<Double> readRodLength(); (5)
    }
}
```

| **1** | The @ConfigurationProperties annotation takes the configuration prefix and is declared on an interface |
|---|---|
| **2** | The @AccessorsStyle annotation defines the `readPrefixes` as `read`. |
| **3** | The getters are all prefixed with `read`. |
| **4** | Nested immutable configuration can also be annotated with @ConfigurationProperties. |
| **5** | The getter is prefixed with `read`. |


## 4.11 Bootstrap Configuration

Most application configuration is stored in your configuration file (e.g `application.yml`), environment-specific files like `application-{environment}.{extension}`, environment and system properties, etc. These configure the application context. But during application startup, before the application context is created, a "bootstrap" context can be created to store configuration necessary to retrieve additional configuration for the main context. Typically, that additional configuration is in some remote source.

The bootstrap context is enabled depending on the following conditions. The conditions are checked in the following order:

- If The BOOTSTRAP_CONTEXT_PROPERTY system property is set, that value determines if the bootstrap context is enabled.
- If The application context builder option bootstrapEnvironment is set, that value determines if the bootstrap context is enabled.
- If a BootstrapPropertySourceLocator bean is present the bootstrap context is enabled. Normally this comes from the `micronaut-discovery-client` dependency. If you provide a custom ConfigurationClient for distributed configuration, make sure that dependency is present so the bootstrap/distributed configuration infrastructure is loaded.

Configuration properties that must be present before application context configuration properties are resolved, for example when using distributed configuration, are stored in a bootstrap configuration file. Once it is determined the bootstrap context is enabled (as described above), the bootstrap configuration files are read using the same rules as regular application configuration. See the property source documentation for the details. The only difference is the prefix (`bootstrap` instead of `application`).

The file name prefix `bootstrap` is configurable with a system property micronaut.bootstrap.name.

|   | The bootstrap context configuration is carried over to the main context automatically, so it is not necessary for configuration properties to be duplicated in the main context. In addition, the bootstrap context configuration has a higher precedence than the main context, meaning if a configuration property appears in both contexts, then the value will be taken from the bootstrap context first. |
|---|---|

That means if a configuration property is needed in both places, it should go into the bootstrap context configuration.

See the distributed configuration section of the documentation for the list of integrations with common distributed configuration solutions.

### Bootstrap Context Beans

In order for a bean to be resolvable in the bootstrap context it must be annotated with @BootstrapContextCompatible. If any given bean is not annotated then it will not be able to be resolved in the bootstrap context. Typically, any bean that is participating in the process of retrieving distributed configuration needs to be annotated.

For example, if you implement custom distributed configuration that is resolved during bootstrap, any supporting beans it depends on must be bootstrap-compatible, and the application must include the discovery client infrastructure, typically by adding the `io.micronaut.discovery:micronaut-discovery-client` dependency.


## 4.12 JMX Support

Micronaut framework provides basic support for JMX.

For more information, see the documentation for the micronaut-jmx project.

# 5 Aspect Oriented Programming

Aspect-Oriented Programming (AOP) has historically had many incarnations and some very complicated implementations. Generally AOP can be thought of as a way to define cross-cutting concerns (logging, transactions, tracing, etc.) separate from application code in the form of aspects that define advice.

There are typically two forms of advice:

- Around Advice - decorates a method or class
- Introduction Advice - introduces new behaviour to a class.

In modern Java applications, declaring advice typically takes the form of an annotation. The most well-known annotation advice in the Java world is probably `@Transactional`, which demarcates transaction boundaries in Spring and Grails applications.

The disadvantage of traditional approaches to AOP is the heavy reliance on runtime proxy creation and reflection, which slows application performance, makes debugging harder and increases memory consumption.

Micronaut framework tries to address these concerns by providing a simple compile-time AOP API that does not use reflection.


## 5.1 Around Advice

The most common type of advice you may want to apply is "Around" advice, which lets you decorate a method’s behaviour.


## Writing Around Advice

The first step is to define an annotation that will trigger a MethodInterceptor:

Around Advice Annotation Example

```java
import io.micronaut.aop.Around;
import java.lang.annotation.*;
import static java.lang.annotation.ElementType.*;
import static java.lang.annotation.RetentionPolicy.RUNTIME;

@Documented
@Retention(RUNTIME) // (1)
@Target({TYPE, METHOD}) // (2)
@Around // (3)
public @interface NotNull {
}
```

Around Advice Annotation Example

```kotlin
import io.micronaut.aop.Around
import kotlin.annotation.AnnotationRetention.RUNTIME
import kotlin.annotation.AnnotationTarget.CLASS
import kotlin.annotation.AnnotationTarget.FILE
import kotlin.annotation.AnnotationTarget.FUNCTION
import kotlin.annotation.AnnotationTarget.PROPERTY_GETTER
import kotlin.annotation.AnnotationTarget.PROPERTY_SETTER

@MustBeDocumented
@Retention(RUNTIME) // (1)
@Target(CLASS, FILE, FUNCTION, PROPERTY_GETTER, PROPERTY_SETTER) // (2)
@Around // (3)
annotation class NotNull
```

Around Advice Annotation Example

```groovy
import io.micronaut.aop.Around
import java.lang.annotation.*
import static java.lang.annotation.ElementType.*
import static java.lang.annotation.RetentionPolicy.RUNTIME

@Documented
@Retention(RUNTIME) // (1)
@Target([TYPE, METHOD]) // (2)
@Around // (3)
@interface NotNull {
}
```

| **1** | The retention policy of the annotation should be `RUNTIME` |
|---|---|
| **2** | Generally you want to be able to apply advice at the class or method level so the target types are `TYPE` and `METHOD` |
| **3** | The @Around annotation is added to tell the Micronaut framework that the annotation is Around advice |

The next step to defining Around advice is to implement a MethodInterceptor. For example the following interceptor disallows parameters with `null` values:

MethodInterceptor Example

```java
import io.micronaut.aop.InterceptorBean;
import io.micronaut.aop.MethodInterceptor;
import io.micronaut.aop.MethodInvocationContext;
import org.jspecify.annotations.Nullable;
import io.micronaut.core.type.MutableArgumentValue;

import jakarta.inject.Singleton;
import java.util.Map;
import java.util.Objects;
import java.util.Optional;

@Singleton
@InterceptorBean(NotNull.class) // (1)
public class NotNullInterceptor implements MethodInterceptor<Object, Object> { // (2)
    @Nullable
    @Override
    public Object intercept(MethodInvocationContext<Object, Object> context) {
        Optional<Map.Entry<String, MutableArgumentValue<?>>> nullParam = context.getParameters()
            .entrySet()
            .stream()
            .filter(entry -> {
                MutableArgumentValue<?> argumentValue = entry.getValue();
                return Objects.isNull(argumentValue.getValue());
            })
            .findFirst(); // (3)
        if (nullParam.isPresent()) {
            throw new IllegalArgumentException("Null parameter [" + nullParam.get().getKey() + "] not allowed"); // (4)
        }
        return context.proceed(); // (5)
    }
}
```

MethodInterceptor Example

```kotlin
import io.micronaut.aop.InterceptorBean
import io.micronaut.aop.MethodInterceptor
import io.micronaut.aop.MethodInvocationContext
import java.util.Objects
import jakarta.inject.Singleton

@Singleton
@InterceptorBean(NotNull::class) // (1)
class NotNullInterceptor : MethodInterceptor<Any, Any> { // (2)
    override fun intercept(context: MethodInvocationContext<Any, Any>): Any? {
        val nullParam = context.parameters
                .entries
                .stream()
                .filter { entry ->
                    val argumentValue = entry.value
                    Objects.isNull(argumentValue.value)
                }
                .findFirst() // (3)
        return if (nullParam.isPresent) {
            throw IllegalArgumentException("Null parameter [${nullParam.get().key}] not allowed") // (4)
        } else {
            context.proceed() // (5)
        }
    }
}
```

MethodInterceptor Example

```groovy
import io.micronaut.aop.InterceptorBean
import io.micronaut.aop.MethodInterceptor
import io.micronaut.aop.MethodInvocationContext
import org.jspecify.annotations.Nullable
import io.micronaut.core.type.MutableArgumentValue

import jakarta.inject.Singleton

@Singleton
@InterceptorBean(NotNull) // (1)
class NotNullInterceptor implements MethodInterceptor<Object, Object> { // (2)
    @Nullable
    @Override
    Object intercept(MethodInvocationContext<Object, Object> context) {
        Optional<Map.Entry<String, MutableArgumentValue<?>>> nullParam = context.parameters
            .entrySet()
            .stream()
            .filter({entry ->
                MutableArgumentValue<?> argumentValue = entry.value
                return Objects.isNull(argumentValue.value)
            })
            .findFirst() // (3)
        if (nullParam.present) {
            throw new IllegalArgumentException("Null parameter [${nullParam.get().key}] not allowed") // (4)
        }
        return context.proceed() // (5)
    }
}
```

| **1** | The @InterceptorBean annotation is used to indicate what annotation the interceptor is associated with. Note that @InterceptorBean is meta-annotated with a default scope of `@Singleton` therefore if you want a new interceptor created and associated with each intercepted bean you should annotate the interceptor with @Prototype. |
|---|---|
| **2** | An interceptor implements the MethodInterceptor interface. |
| **3** | The passed MethodInvocationContext is used to find the first parameter that is `null` |
| **4** | If a `null` parameter is found an exception is thrown |
| **5** | Otherwise proceed() is called to proceed with the method invocation. |

|   | Micronaut AOP interceptors use no reflection which improves performance and reducing stack trace sizes, thus improving debugging. |
|---|---|

Apply the annotation to target classes to put the new `MethodInterceptor` to work:

Around Advice Usage Example

```java
import jakarta.inject.Singleton;

@Singleton
public class NotNullExample {

    @NotNull
    void doWork(String taskName) {
        System.out.println("Doing job: " + taskName);
    }
}
```

Around Advice Usage Example

```kotlin
import jakarta.inject.Singleton

@Singleton
open class NotNullExample {

    @NotNull
    open fun doWork(taskName: String?) {
        println("Doing job: $taskName")
    }
}
```

Around Advice Usage Example

```groovy
import jakarta.inject.Singleton

@Singleton
class NotNullExample {

    @NotNull
    void doWork(String taskName) {
        println "Doing job: $taskName"
    }
}
```

Whenever the type `NotNullExample` is injected into a class, a compile-time-generated proxy is injected that decorates method calls with the `@NotNull` advice defined earlier. You can verify that the advice works by writing a test. The following test verifies that the expected exception is thrown when the argument is `null`:

Around Advice Test

Around Advice Test

```kotlin
@Test
fun testNotNull() {
    val applicationContext = ApplicationContext.run()
    val exampleBean = applicationContext.getBean(NotNullExample::class.java)

    val exception = shouldThrow<IllegalArgumentException> {
        exampleBean.doWork(null)
    }
    exception.message shouldBe "Null parameter [taskName] not allowed"
    applicationContext.close()
}
```

Around Advice Test

```groovy
void "test not null"() {
    when:
    def applicationContext = ApplicationContext.run()
    def exampleBean = applicationContext.getBean(NotNullExample)

    exampleBean.doWork(null)

    then:
    IllegalArgumentException e = thrown()
    e.message == 'Null parameter [taskName] not allowed'

    cleanup:
    applicationContext.close()
}
```

|   | Since Micronaut injection happens at compile time, generally the advice should be packaged in a dependent JAR file that is on the classpath when the above test is compiled. It should not be in the same codebase since you don’t want the test to be compiled before the advice itself is compiled. |
|---|---|


## Customizing Proxy Generation

The default behaviour of the Around annotation is to generate a proxy at compile time that is a subclass of the proxied class. In other words, in the previous example a compile-time subclass of the `NotNullExample` class will be produced where proxied methods are decorated with interceptor handling, and the original behaviour is invoked via a call to `super`.

This behaviour is more efficient as only one instance of the bean is required, however depending on the use case you may wish to alter this behaviour. The `@Around` annotation supports various attributes that allow you to alter this behaviour, including:

- `proxyTarget` (defaults to `false`) - If set to `true`, instead of a subclass that calls `super`, the proxy delegates to the original bean instance
- `hotswap` (defaults to `false`) - Same as `proxyTarget=true`, but in addition the proxy implements HotSwappableInterceptedProxy which wraps each method call in a `ReentrantReadWriteLock` and allows swapping the target instance at runtime.
- `lazy` (defaults to `false`) - By default the Micronaut framework eagerly initializes the proxy target when the proxy is created. If set to `true` the proxy target is instead resolved lazily for each method call.


## AOP Advice on @Factory Beans

The semantics of AOP advice when applied to Bean Factories differs from regular beans, with the following rules applying:

1. AOP advice applied at the class level of a @Factory bean applies the advice to the factory itself and not to any beans defined with the @Bean annotation.
2. AOP advice applied on a method annotated with a bean scope applies the AOP advice to the bean that the factory produces.

Consider the following two examples:

AOP Advice at the type level of a

@Factory

```java
@Timed
@Factory
public class MyFactory {

    @Prototype
    public MyBean myBean() {
        return new MyBean();
    }
}
```

AOP Advice at the type level of a

@Factory

```kotlin
@Timed
@Factory
open class MyFactory {

    @Prototype
    open fun myBean(): MyBean {
        return MyBean()
    }
}
```

AOP Advice at the type level of a

@Factory

```groovy
@Timed
@Factory
class MyFactory {

    @Prototype
    MyBean myBean() {
        new MyBean()
    }
}
```

The above example logs the time it takes to create the `MyBean` bean.

Now consider this example:

AOP Advice at the method level of a

@Factory

```java
@Factory
public class MyFactory {

    @Prototype
    @Timed
    public MyBean myBean() {
        return new MyBean();
    }
}
```

AOP Advice at the method level of a

@Factory

```kotlin
@Factory
open class MyFactory {

    @Prototype
    @Timed
    open fun myBean(): MyBean {
        return MyBean()
    }
}
```

AOP Advice at the method level of a

@Factory

```groovy
@Factory
class MyFactory {

    @Prototype
    @Timed
    MyBean myBean() {
        new MyBean()
    }
}
```

The above example logs the time it takes to execute the public methods of the `MyBean` bean, but not the bean creation.

The rationale for this behaviour is that you may at times wish to apply advice to a factory and at other times apply advice to the bean produced by the factory.

Note that there is currently no way to apply advice at the method level to a @Factory bean, and all advice for factories must be applied at the type level. You can control which methods have advice applied by defining methods as non-public which do not have advice applied.


## 5.2 Introduction Advice

Introduction advice is distinct from Around advice in that it involves providing an implementation instead of decorating.

Examples of introduction advice includes Spring Data which implements persistence logic for you.

Micronaut Client annotation is another example of introduction advice where the Micronaut framework implements HTTP client interfaces for you at compile time.

The way you implement Introduction advice is very similar to how you implement Around advice.

You start by defining an annotation that powers the introduction advice. As an example, say you want to implement advice to return a stubbed value for every method in an interface (a common requirement in testing frameworks). Consider the following `@Stub` annotation:

Introduction Advice Annotation Example

```java
import io.micronaut.aop.Introduction;
import io.micronaut.context.annotation.Bean;

import java.lang.annotation.Documented;
import java.lang.annotation.Retention;
import java.lang.annotation.Target;

import static java.lang.annotation.ElementType.ANNOTATION_TYPE;
import static java.lang.annotation.ElementType.METHOD;
import static java.lang.annotation.ElementType.TYPE;
import static java.lang.annotation.RetentionPolicy.RUNTIME;

@Introduction // (1)
@Bean // (2)
@Documented
@Retention(RUNTIME)
@Target({TYPE, ANNOTATION_TYPE, METHOD})
public @interface Stub {
    String value() default "";
}
```

Introduction Advice Annotation Example

```kotlin
import io.micronaut.aop.Introduction
import io.micronaut.context.annotation.Bean
import kotlin.annotation.AnnotationRetention.RUNTIME
import kotlin.annotation.AnnotationTarget.ANNOTATION_CLASS
import kotlin.annotation.AnnotationTarget.CLASS
import kotlin.annotation.AnnotationTarget.FILE
import kotlin.annotation.AnnotationTarget.FUNCTION
import kotlin.annotation.AnnotationTarget.PROPERTY_GETTER
import kotlin.annotation.AnnotationTarget.PROPERTY_SETTER

@Introduction // (1)
@Bean // (2)
@MustBeDocumented
@Retention(RUNTIME)
@Target(CLASS, FILE, ANNOTATION_CLASS, FUNCTION, PROPERTY_GETTER, PROPERTY_SETTER)
annotation class Stub(val value: String = "")
```

Introduction Advice Annotation Example

```groovy
import io.micronaut.aop.Introduction
import io.micronaut.context.annotation.Bean

import java.lang.annotation.Documented
import java.lang.annotation.Retention
import java.lang.annotation.Target

import static java.lang.annotation.ElementType.ANNOTATION_TYPE
import static java.lang.annotation.ElementType.METHOD
import static java.lang.annotation.ElementType.TYPE
import static java.lang.annotation.RetentionPolicy.RUNTIME

@Introduction // (1)
@Bean // (2)
@Documented
@Retention(RUNTIME)
@Target([TYPE, ANNOTATION_TYPE, METHOD])
@interface Stub {
    String value() default ""
}
```

| **1** | The introduction advice is annotated with Introduction |
|---|---|
| **2** | The Bean annotation is added so that all types annotated with `@Stub` become beans |

The `StubIntroduction` class referred to in the previous example must then implement the MethodInterceptor interface, just like around advice.

The following is an example implementation:

StubIntroduction

```java
import io.micronaut.aop.*;
import org.jspecify.annotations.Nullable;
import jakarta.inject.Singleton;

@Singleton
@InterceptorBean(Stub.class) // (1)
public class StubIntroduction implements MethodInterceptor<Object, Object> { // (2)

    @Nullable
    @Override
    public Object intercept(MethodInvocationContext<Object, Object> context) {
        return context.getValue( // (3)
                Stub.class,
                context.getReturnType().getType()
        ).orElse(null); // (4)
    }
}
```

StubIntroduction

```kotlin
import io.micronaut.aop.*
import jakarta.inject.Singleton

@Singleton
@InterceptorBean(Stub::class) // (1)
class StubIntroduction : MethodInterceptor<Any, Any> { // (2)

    override fun intercept(context: MethodInvocationContext<Any, Any>): Any? {
        return context.getValue<Any>( // (3)
                Stub::class.java,
                context.returnType.type
        ).orElse(null) // (4)
    }
}
```

StubIntroduction

```groovy
import io.micronaut.aop.MethodInterceptor
import io.micronaut.aop.MethodInvocationContext
import io.micronaut.aop.InterceptorBean
import org.jspecify.annotations.Nullable
import jakarta.inject.Singleton

@Singleton
@InterceptorBean(Stub) // (1)
class StubIntroduction implements MethodInterceptor<Object,Object> { // (2)

    @Nullable
    @Override
    Object intercept(MethodInvocationContext<Object, Object> context) {
        context.getValue( // (3)
                Stub,
                context.returnType.type
        ).orElse(null) // (4)
    }
}
```

| **1** | The InterceptorBean annotation is used to associate the interceptor with the `@Stub` annotation |
|---|---|
| **2** | The class is annotated with `@Singleton` and implements the MethodInterceptor interface |
| **3** | The value of the `@Stub` annotation is read from the context and an attempt made to convert the value to the return type |
| **4** | Otherwise `null` is returned |

To now use this introduction advice in an application, annotate your abstract classes or interfaces with `@Stub`:

StubExample

```java
@Stub
public interface StubExample {

    @Stub("10")
    int getNumber();

    LocalDateTime getDate();
}
```

StubExample

```kotlin
@Stub
interface StubExample {

    @get:Stub("10")
    val number: Int

    val date: LocalDateTime?
}
```

StubExample

```groovy
@Stub
interface StubExample {

    @Stub("10")
    int getNumber()

    LocalDateTime getDate()
}
```

All abstract methods delegate to the `StubIntroduction` class to be implemented.

The following test demonstrates the behaviour or `StubIntroduction`:

Testing Introduction Advice

```java
StubExample stubExample = applicationContext.getBean(StubExample.class);

assertEquals(10, stubExample.getNumber());
assertNull(stubExample.getDate());
```

Testing Introduction Advice

```kotlin
val stubExample = applicationContext.getBean(StubExample::class.java)

stubExample.number.shouldBe(10)
stubExample.date.shouldBe(null)
```

Testing Introduction Advice

```groovy
when:
def stubExample = applicationContext.getBean(StubExample)

then:
stubExample.number == 10
stubExample.date == null
```

Note that if the introduction advice cannot implement the method, call the `proceed` method of the MethodInvocationContext. This lets other introduction advice interceptors implement the method, and an `UnsupportedOperationException` will be thrown if no advice can implement the method.

In addition, if multiple introduction advice are present you may wish to override the `getOrder()` method of MethodInterceptor to control the priority of advice.

The following sections cover core advice types provided by Micronaut.
