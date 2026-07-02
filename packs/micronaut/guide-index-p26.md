---
title: "Micronaut Core (part 26/27)"
source: https://docs.micronaut.io/latest/guide/index.html
domain: micronaut
license: CC-BY-SA-4.0
tags: micronaut framework, micronaut jvm, compile-time injection, microservices framework
fetched: 2026-07-02
part: 26/27
---

## 21.1 Resource Bundles

A resource bundle is a Java .properties file that contains locale-specific data.

Given this Resource Bundle:

src/main/resources/io/micronaut/docs/i18n/messages_en.properties

```properties
hello=Hello
hello.name=Hello {0}
```

src/main/resources/io/micronaut/docs/i18n/messages_es.properties

```properties
hello=Hola
hello.name=Hola {0}
```

You can use ResourceBundleMessageSource, an implementation of MessageSource which eases accessing Resource Bundles and provides cache functionality, to access the previous messages.

|   | Do not instantiate a new `ResourceBundleMessageSource` each time you retrieve a message. Instantiate it once, for example in a factory. |
|---|---|

MessageSource Factory Example

```java
import io.micronaut.context.MessageSource;
import io.micronaut.context.annotation.Factory;
import io.micronaut.context.annotation.Requires;
import io.micronaut.context.i18n.ResourceBundleMessageSource;
import io.micronaut.core.order.Ordered;
import jakarta.inject.Singleton;

@Factory
class MessageSourceFactory {
    @Singleton
    MessageSource createMessageSource() {
        return new ResourceBundleMessageSource("io.micronaut.docs.i18n.messages", Ordered.HIGHEST_PRECEDENCE);
    }
}
```

MessageSource Factory Example

```kotlin
import io.micronaut.context.MessageSource
import io.micronaut.context.annotation.Factory
import io.micronaut.context.i18n.ResourceBundleMessageSource
import jakarta.inject.Singleton

@Factory
internal class MessageSourceFactory {
    @Singleton
    fun createMessageSource(): MessageSource = ResourceBundleMessageSource("io.micronaut.docs.i18n.messages")
}
```

MessageSource Factory Example

```groovy
import io.micronaut.context.MessageSource
import io.micronaut.context.annotation.Factory
import io.micronaut.context.i18n.ResourceBundleMessageSource
import io.micronaut.core.order.Ordered
import jakarta.inject.Singleton

@Factory
class MessageSourceFactory {
    @Singleton
    MessageSource createMessageSource() {
        new ResourceBundleMessageSource("io.micronaut.docs.i18n.messages", Ordered.HIGHEST_PRECEDENCE)
    }
}
```

Then you can retrieve the messages supplying the locale:

ResourceBundleMessageSource Example

```java
assertEquals("Hola", messageSource.getMessage("hello", MessageContext.of(new Locale("es"))).get());
assertEquals("Hello", messageSource.getMessage("hello", MessageContext.of(Locale.ENGLISH)).get());
```

ResourceBundleMessageSource Example

```kotlin
Assertions.assertEquals("Hola", messageSource.getMessage("hello", MessageSource.MessageContext.of(Locale("es"))).get())
Assertions.assertEquals("Hello", messageSource.getMessage("hello", MessageSource.MessageContext.of(Locale.ENGLISH)).get())
```

ResourceBundleMessageSource Example

```groovy
expect:
messageSource.getMessage("hello", MessageContext.of(new Locale("es"))).get() == 'Hola'

and:
messageSource.getMessage("hello", MessageContext.of(Locale.ENGLISH)).get() == 'Hello'
```


## 21.2 Localized Message Source

LocalizedMessageSource is a `@RequestScope` bean which you can inject in your Controllers and which uses Micronaut Locale Resolution to resolve the localized message for the current HTTP request.

|   | See the guide for Localize your Application to learn more. |
|---|---|

# 22 Resources

Micronaut Framework provides support for loading resources from files into memory, rooted at the ResourceLoader API. Built-in implementations include

- DefaultFileSystemResourceLoader
- DefaultClassPathResourceLoader
- StringResourceLoader
- Base64ResourceLoader

A convenience class ResourceResolver is provided that leverages both of these implementations. The following example illustrates using the API to read a text file from the classpath.

ResourceResolver Example

```java
@Singleton
public class MyResourceLoader {

    private final ResourceResolver resourceResolver;

    public MyResourceLoader(ResourceResolver resourceResolver) {  // (1)
        this.resourceResolver = resourceResolver;
    }

    public Optional<String> getClasspathResourceAsText(String path) throws Exception {
        Optional<URL> url = resourceResolver.getResource("classpath:" + path); // (2)
        if (url.isPresent()) {
            return Optional.of(IOUtils.readText(new BufferedReader(new InputStreamReader(url.get().openStream())))); // (3)
        } else {
            return Optional.empty();
        }
    }
}
```

ResourceResolver Example

```groovy
@Singleton
class MyResourceLoader {

    private final ResourceResolver resourceResolver // (1)

    MyResourceLoader(ResourceResolver resourceResolver) { // (1)
        this.resourceResolver = resourceResolver
    }

    Optional<String> getClasspathResourceAsText(String path) throws Exception {
        Optional<URL> url = resourceResolver.getResource('classpath:' + path) // (2)
        if (url.isPresent()) {
            return Optional.of(IOUtils.readText(new BufferedReader(new InputStreamReader(url.get().openStream()))))  // (3)
        } else {
            return Optional.empty()
        }
    }
}
```

| **1** | Injects an instance of `ResourceResolver` |
|---|---|
| **2** | Uses the `ResourceResolver` API to get a `URL` to a file in the classpath, if it exists. |
| **3** | IOUtils provides further support for I/O operations, in this case reading the file contents into a String. |

Areas of the framework that load resources using `ResourceResolver` include:

- Static HTTP resources
- SSL key and trust stores
- Dynamic configuration

To use a fixed value for a resource instead of loading it from the file system or classpath, the `string:` and `base64:` prefixes. While `string:` returns the value as is (decoded as UTF-8), `base64:` first decodes the value from Base64. This allows you to serve e.g. a small binary as a static HTTP file.

# 23 Appendices


## 23.1 Micronaut Architecture

The following documentation describes the Micronaut framework’s architecture and is designed for those who are looking for information on the internal workings of the Micronaut framework and how it is architected. This is not intended as end-user developer documentation, but for those interested in the inner workings of the Micronaut framework.

This documentation is divided into sections that describe the compiler, introspections, application container, dependency injection and so on.

|   | Since this documentation covers the internal workings of Micronaut, many APIs referenced and described are regarded as internal, non-public API and are annotated as such with the @Internal. Internal APIs can change between patch releases of Micronaut and are not covered by Micronaut’s semantic versioning release policy. |
|---|---|


## 23.1.1 Compiler

The Micronaut Compiler is a set of extensions to existing language compilers:

- Java - the Java Annotation Processing (APT) API is used for Java code.
- Kotlin - KAPT or KSP is used for Kotlin code.
- Groovy - Groovy AST Transformations are used to participate in the compilation of Groovy code.

To keep this documentation simple, the remaining sections will describe the interaction with the Java compiler.

The Micronaut Compiler visits end user code and generates additional bytecode that sits alongside the user code in the same package structure.

The AST of user source is visited using implementations of TypeElementVisitor which are loaded via the standard Java service loader mechanism.

Each TypeElementVisitor implementation can override one or more of the `visit*` methods which receive an instance of Element.

The Element API provides a language-neutral abstraction over the AST and computation of the AnnotationMetadata for a given element (class, method, field etc).


## 23.1.2 Annotation Metadata

Micronaut framework is an implementation of an annotation-based programming model. That is to say annotations form a fundamental part of the API design of the framework.

Given this design decision, a compilation-time model was formulated to address the challenges of evaluating annotations at runtime.

The AnnotationMetadata API is a construct that is used both a compilation time and at runtime by framework components. `AnnotationMetadata` represents the computed fusion of annotation information for a particular type, field, constructor, method or bean property and may include both annotations declared in the source code, but also synthetic meta-annotations that can be used at runtime to implement framework logic.

When visiting source code within the Micronaut Compiler using the Element API for each ClassElement, FieldElement, MethodElement, ConstructorElement and PropertyElement an instance of AnnotationMetadata is computed.

The `AnnotationMetadata` API tries to address the following challenges:

- Annotations can be inherited from types and interfaces into implementations. To avoid the need to traverse the class/interface hierarchy at runtime Micronaut will at build time compute inherited annotations and deal with member overriding rules
- Annotations can be annotated with other annotations. These annotations are often referred to as meta-annotations or stereotypes. The `AnnotationMetadata` API provides methods to understand whether a particular annotation is declared as meta-annotation and to find out what annotations are meta-annotated with other annotations
- It is often necessary to fuse annotation metadata together from different sources. For example, for JavaBean properties you want to combine the metadata from the private field, public getter and public setters into a single view otherwise you have to run logic to runtime to somehow combine this metadata from 3 distinct sources.
- Repeatable annotations are combined and normalized. If inherited the annotations are combined from parent interfaces or classes providing a single API to evaluate repeatable annotations instead of requiring runtime logic to perform normalization.

When the source for a type is visited an instance of ClassElement is constructed via the ElementFactory API.

The ElementFactory uses an instance of AbstractAnnotationMetadataBuilder which contains language specific implementations to construct `AnnotationMedata` for the underlying native type in the AST. In the case of Java this would be a `javax.model.element.TypeElement`.

The basic flow is visualized below:

Additionally, the AbstractAnnotationMetadataBuilder will load via the standard Java service loader mechanism one or more instances of the following types that allow manipulating how an annotation is represented in the `AnnotationMetadata`:

- AnnotationMapper - A type that can map the value of one annotation to another, retaining the original annotation in the `AnnotationMetadata`
- AnnotationTransformer - A type that can transform the value of one annotation to another, eliminating the original annotation from the `AnnotationMetadata`
- AnnotationRemapper - A type that can transform the values of all annotations in a given package, eliminating the original annotations from the `AnnotationMetadata`

Note that at compilation time the AnnotationMetadata is mutable and can be further altered by implementations of TypeElementVisitor by invoking the `annotate(..)` method of the Element API. However, at runtime the AnnotationMetadata is immutable and fixed. The purpose of this design to allow the compiler to be extended and for Micronaut to be able to interpret different source-level annotation-based programming models.

In practice this effectively allows decoupling the source code level annotation model from what is used at runtime such that different annotations can be used to represent the same annotation.

For example `jakarata.inject.Inject` or Spring’s `@Autowired` are supported as synonyms for `jakarta.inject.Inject` by transforming the source level annotation to `jakarta.inject.Inject` which is the only annotation represented at runtime.

Finally, annotations in Java also allow the definition of default values. These defaults are not retained in individual instances of `AnnotationMetadata` but instead stored in a shared, static application-wide map for later retrieval for annotations known to be used by the application.


## 23.1.3 Bean Introspections

The goal of Bean Introspections is to provide an alternative to reflection and the JDK’s Introspector API that is coupled to the `java.desktop` module in recent versions of Java.

Many libraries in Java need to programmatically discover what methods represent properties of a class in some way and whilst the JavaBeans specification tried to establish a standard convention, the language itself has evolved to include other constructs like Records that represent properties as components.

In addition, other languages like Kotlin and Groovy have native support for class properties that need to be supported at the framework level.

The IntrospectedTypeElementVisitor visits declarations of the @Introspected annotation on types and generates at compilation time implementations of BeanIntrospection that are associated with each annotated type:

This generation happens via the `io.micronaut.inject.beans.visitor.BeanIntrospectionWriter`, an internal class that uses the ASM bytecode generation library to generate an additional class.

For example, given a class called `example.Person` Micronaut generates the following class :

- `example.$Person$Introspection` - an implementation of BeanIntrospection which contains the actual runtime introspection information. Since references are loaded via ServiceLoader an entry in a generated `META-INF/micronaut/io.micronaut.core.beans.BeanIntrospectionReference` referring to this type is also generated at compilation time.

The following example demonstrates usage of the BeanIntrospection API:

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

| **1** | A BeanIntrospection is looked up by type. When this occurs the introspection will be searched for amongst the BeanIntrospectionReference instances loaded via ServiceLoader. |
|---|---|
| **2** | The `instantiate` method allows creating instances |
| **3** | Properties for bean can be loaded via one of the available methods, in this case `getRequiredProperty` |
| **4** | The referenced BeanProperty can be used to write mutable properties |
| **5** | And read readable properties |

|   | The `Person` class is only initialized when the `getBeanType()` method is called. If the class is not present on the classpath then a `NoClassDefFoundError` will occur, to prevent this the developer can call the `isPresent()` method on the BeanIntrospectionReference prior to trying to obtain the type. |
|---|---|

An implementation of BeanIntrospection performs two critical functions:

1. The introspection holds Bean metadata about the properties and constructor arguments for a particular type that is abstracted away from the actual implementation (JavaBean property, Java 17+ Record, Kotlin data classes, Groovy properties etc.) and which also provide access to AnnotationMetadata without needing to use reflection to load the annotations themselves.
2. The introspection enables the ability to instantiate and read/write bean properties without the use of Java reflection, based purely on the subset of build-time generated information.

Optimized reflection-free method dispatch is generated by overriding the `dispatchOne` method of AbstractInitializableBeanIntrospection, for example:

```java
protected final Object dispatchOne(int propertyIndex, Object bean, Object value
) {
    switch(propertyIndex) { (1)
    case 0:
        return ((Person) bean).getName(); (2)
    case 1:
        ((Person) bean).setName((String) value); (3)
        return null;
    default:
        throw this.unknownDispatchAtIndexException(propertyIndex); (4)
    }
}
```

| **1** | Each read or write method is assigned an index |
|---|---|
| **2** | The index is used in read methods to obtain the value directly without relying on reflection |
| **3** | The index is used for write methods to set a property without using reflection |
| **4** | If no property exists at the index an exception is thrown, though this is implementation detail and the codepath should never arrive to this point. |

|   | The approach to use a dispatch method with an index was used to avoid the need to generate a class per method (which would consume more memory) or introduce the overhead of lambdas. |
|---|---|

In order to enable type instantiation the `io.micronaut.inject.beans.visitor.BeanIntrospectionWriter` will also generate an implementation of the `instantiateInternal` method which contains the reflection-free code to instantiate a given type based on known valid argument types:

```java
public Object instantiateInternal(Object[] args) {
    return new Person(
        (String)args[0],
        (Integer)args[1]
    );
}
```


## 23.1.4 Bean Definitions

Micronaut framework is an implementation of the JSR-330 specification for Dependency Injection.

Dependency Injection (or Inversion of Control) is a widely adopted and common pattern in Java that allows loosely decoupling components to allow applications to be easily extended and tested.

The way in which objects are wired together is decoupled from the objects themselves in this model by a separate programming model. In the case of Micronaut this model is based on annotations defined within the JSR-330 specification plus an extended set of annotations located within the io.micronaut.context.annotation package.

These annotations are visited by the Micronaut Compiler which traverses the source code language AST and builds a model used to wire objects together at runtime.

|   | It is important to note that the actual object wiring is deferred until runtime. |
|---|---|

For Java code BeanDefinitionInjectProcessor (which is a Java Annotation Processor) is invoked from the Java compiler for each class annotated with a bean definition annotation.

|   | What constitutes a bean defining annotation is complex as it takes into account meta-annotations, but in general it is any annotation annotated with a JSR-330 bean `@Scope` |
|---|---|

The `BeanDefinitionInjectProcessor` will visit each bean in the user code source and generate additional byte code using the ASM byte code generation library that sits alongside the annotated class in the same package.

|   | For historic reasons the dependency injection processor does not use the TypeElementVisitor API but will likely do so in the future |
|---|---|

Byte code generation is implemented in the BeanDefinitionWriter which contains methods to "visit" different aspects of the way is bean is defined (the BeanDefinition).

The following diagram illustrates the flow:

For example given the following type:

```java
@Singleton
public class Vehicle {
    private final Engine engine;

    public Vehicle(Engine engine) {// (3)
        this.engine = engine;
    }

    public String start() {
        return engine.start();
    }
}
```

```kotlin
@Singleton
class Vehicle(private val engine: Engine) { // (3)
    fun start(): String {
        return engine.start()
    }
}
```

```groovy
@Singleton
class Vehicle {
    final Engine engine

    Vehicle(Engine engine) { // (3)
        this.engine = engine
    }

    String start() {
        engine.start()
    }
}
```

The following is generated:

- A `example.$Vehicle$Definition$Reference` class that implements the BeanDefinitionReference interface that allows the application to soft load the bean definition without loading all metadata or the class itself (in the case where the introspected class is itself not on the classpath). Since references are loaded via ServiceLoader an entry in a generated `META-INF/services/io.micronaut.inject.BeanDefinitionReference` referring to this type is also generated at compilation time.
- A `example.$Vehicle$Definition` which contains the actual BeanDefinition information.

A BeanDefinition is a type that holds metadata about the particular type including:

- Class level AnnotationMetadata
- The computed JSR-330 `@Scope` and `@Qualifier`
- Knowledge of the available InjectionPoint instances
- References to any ExecutableMethod defined

In addition, the `BeanDefinition` contains logic which knows how the bean is wired together, including how the type is constructed and fields and/or methods injected.

During compilation the ASM byte code library is used to fill out the details of the `BeanDefinition`, including a `build` method that, for the previous example, looks like:

```java
public Vehicle build(
    BeanResolutionContext resolution, (1)
    BeanContext context,
    BeanDefinition definition) {
    Vehicle bean = new Vehicle(
        (Engine) super.getBeanForConstructorArgument( (2)
            resolution,
            context,
            0, (3)
            (Qualifier)null)
    );
    return bean;
}
```

| **1** | The `BeanResolutionContext` is passed around to track circular bean references and improve error reporting. |
|---|---|
| **2** | The type is instantiated and each constructor argument looked up by calling methods of AbstractInitializableBeanDefinition |
| **3** | In this case the index of the constructor argument is tracked |

|   | Special handling is required when a Java field or method has `private` access. In this case Micronaut has no option but to fall back to using Java reflection to perform dependency injection. |
|---|---|

### Configuration Properties Handling

The Micronaut Compiler handles beans declared with the meta-annotation @ConfigurationReader such as @ConfigurationProperties and @EachProperty distinctly to other beans.

In order to support binding Application Configuration to types annotated with one of the aforementioned annotations each discovered mutable bean property is dynamically annotated with the @Property annotation with the computed and normalized property name.

For example given the below type:

@ConfigurationProperties Example

```java
import io.micronaut.context.annotation.ConfigurationProperties;

import io.micronaut.context.annotation.Requires;
import jakarta.validation.constraints.Min;
import jakarta.validation.constraints.NotBlank;
import java.util.Optional;

@ConfigurationProperties("my.engine") // (1)
public class EngineConfig {

    public String getManufacturer() {
        return manufacturer;
    }

    public void setManufacturer(String manufacturer) {
        this.manufacturer = manufacturer;
    }

    public int getCylinders() {
        return cylinders;
    }

    public void setCylinders(int cylinders) {
        this.cylinders = cylinders;
    }

    public CrankShaft getCrankShaft() {
        return crankShaft;
    }

    public void setCrankShaft(CrankShaft crankShaft) {
        this.crankShaft = crankShaft;
    }

    @NotBlank // (2)
    private String manufacturer = "Ford"; // (3)

    @Min(1L)
    private int cylinders;

    private CrankShaft crankShaft = new CrankShaft();

    @ConfigurationProperties("crank-shaft")
    public static class CrankShaft { // (4)

        private Optional<Double> rodLength = Optional.empty(); // (5)

        public Optional<Double> getRodLength() {
            return rodLength;
        }

        public void setRodLength(Optional<Double> rodLength) {
            this.rodLength = rodLength;
        }
    }
}
```

@ConfigurationProperties Example

```kotlin
import io.micronaut.context.annotation.ConfigurationProperties
import java.util.Optional
import jakarta.validation.constraints.Min
import jakarta.validation.constraints.NotBlank

@ConfigurationProperties("my.engine") // (1)
class EngineConfig {

    @NotBlank // (2)
    var manufacturer = "Ford" // (3)

    @Min(1L)
    var cylinders: Int = 0

    var crankShaft = CrankShaft()

    @ConfigurationProperties("crank-shaft")
    class CrankShaft { // (4)
        var rodLength: Optional<Double> = Optional.empty() // (5)
    }
}
```

@ConfigurationProperties Example

```groovy
import io.micronaut.context.annotation.ConfigurationProperties

import jakarta.validation.constraints.Min
import jakarta.validation.constraints.NotBlank

@ConfigurationProperties('my.engine') // (1)
class EngineConfig {

    @NotBlank // (2)
    String manufacturer = "Ford" // (3)

    @Min(1L)
    int cylinders

    CrankShaft crankShaft = new CrankShaft()

    @ConfigurationProperties('crank-shaft')
    static class CrankShaft { // (4)
        Optional<Double> rodLength = Optional.empty() // (5)
    }
}
```

The `setManufacturer(String)` method will be annotated with `@Property(name="my.engine.manufacturer")` the value of which will be resolved from the configured Environment.

The `injectBean` method of AbstractInitializableBeanDefinition is subsequently overridden with logic to handle looking up the normalized property name `my.engine.manufacturer` from the current BeanContext and inject the value if it is present in a reflection-free manner.

|   | Property names are normalized into kebab case (lower case hyphen separated) which is the format used to store their values. |
|---|---|

Configuration Properties Injection

```java
@Generated
protected Object injectBean(
    BeanResolutionContext resolution,
    BeanContext context,
    Object bean) {
    if (this.containsProperties(resolution, context)) { (1)
        EngineConfig engineConfig = (EngineConfig) bean;
        if (this.containsPropertyValue(resolution, context, "my.engine.manufacturer")) { (2)
            String value = (String) super.getPropertyValueForSetter( (3)
                resolution,
                context,
                "setManufacturer",
                Argument.of(String.class, "manufacturer"), (4)
                "my.engine.manufacturer", (5)
                (String)null (6)
            )
            engineConfig.setManufacturer(value);
        }
    }
}
```

| **1** | A top level check to see if any properties exist with the prefix defined in the @ConfigurationProperties annotation is added. |
|---|---|
| **2** | A check is performed to see if the property actually exists |
| **3** | If it does the value is looked up by calling the `getPropertyValueForSetter` method of AbstractInitializableBeanDefinition |
| **4** | An instance of Argument is created which is used for conversion to the target type (in this case `String`). The Argument may also contain generics information. |
| **5** | The computed and normalized path to the property |
| **6** | The default value if the Bindable annotation is used to specify a default. |


## 23.1.5 AOP Proxies

Micronaut supports annotation-based Aspect Oriented Programming (AOP) which allows decorating or introducing type behaviour through the use of interceptors defined in user code.

|   | The use of the AOP terminogy originates from AspectJ and historical use in Spring. |
|---|---|

Any annotation defined by the framework can be meta-annotated with the @InterceptorBinding annotation which supports different kinds of interception including:

- `AROUND` - A annotation can be used to decorate an existing method invocation
- `AROUND_CONSTRUCT` - An annotation can be used to intercept the construction of any type
- `INTRODUCTION` - An annotation can be used to "introduce" new behaviour to abstract or interface types
- `POST_CONSTRUCT` - An annotation can be used to intercept `@PostConstruct` calls which are invoked after the object is instantiated.
- `PRE_DESTROY` - An annotation can be used to intercept `@PreDestroy` calls which are invoked after the object is about to be disposed of.

One or many instances of Interceptor can be associated with an @InterceptorBinding allowing the user to implement behaviour that applies cross-cutting concerns.

At an implementation level, the Micronaut Compiler will visit types that are meta-annotated with @InterceptorBinding and construct a new instance of AopProxyWriter which uses the ASM bytecode generation library to generate a subclass (or an implementation in the case of interfaces) of the annotated type.

|   | Micronaut at no point modifies existing user byte code, the use of build-time generated proxies allows Micronaut to generate additional code that sits alongside user code and enhances behaviour. This approach does have limitations however, for example it is required that annotated types are non-final and AOP advice cannot be applied to final or effectively final types such as Java 17 Records. |
|---|---|

For example given the following annotation:

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

| **1** | The retention policy of the annotation must be `RUNTIME` |
|---|---|
| **2** | Generally you want to be able to apply advice at the class or method level so the target types are `TYPE` and `METHOD` |
| **3** | The @Around annotation is used here which itself is annotated with `@InterceptorBinding(kind=AROUND)` and can be thought of as a simple shortcut for defining an @InterceptorBinding for `AROUND` advice. |

When this annotation is used on a type or method, for example:

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

The compiler will visit the type and the AopProxyWriter will generate additional bytecode using the ASM bytecode generation library.

During compilation the AopProxyWriter instance essentially proxies the `BeanDefinitionWriter` (see Bean Definitions), decorating the existing bytecode generation with additional behaviour. This is illustrated with the below diagram:

The BeanDefinitionWriter will generate the regular classes generated for every bean including:

- `$NotNullExample$Definition.class` - The original undecorated bean definition (see Bean Definitions)
- `$NotNullExample$Definition$Exec.class` - An implementation of ExecutableMethodsDefinition containing logic that allows dispatching to each intercepted method without using reflection.

And the AopProxyWriter will decorate this behaviour and generate 3 additional classes:

- `$NotNullExample$Definition$Intercepted.class` - A subclass of the decorated class that holds references to applied MethodInterceptor instances and overrides all the intercepted methods, constructing the MethodInterceptorChain instance and invoking the applied interceptors
- `$NotNullExample$Definition$Intercepted$Definition.class` - A BeanDefinition that subclasses the original undecorated bean definition. (see Bean Definitions)
- `$NotNullExample$Definition$Intercepted$Definition$Reference.class` - A BeanDefinitionReference that is capable of soft loading the intercepted BeanDefinition. (see Bean Definitions)

The majority of the classes generated are metadata for loading and resolving the BeanDefinition. The actual build time proxy is the class that ends with `$Intercepted`. This class implements the Intercepted interface and subclasses the proxied type, overriding any non-final and non-private methods to invoke the MethodInterceptorChain.

An implementation will create a constructor which is used to wire in the dependencies on the intercepted type that looks like:

An intercepted type constructor

```java
@Generated
class $NotNullExample$Definition$Intercepted
extends NotNullExample implements Intercepted { (1)
    private final Interceptor[][] $interceptors = new Interceptor[1][];
    private final ExecutableMethod[] $proxyMethods = new ExecutableMethod[1];

    public $NotNullExample$Definition$Intercepted(
        BeanResolutionContext resolution,
        BeanContext context,
        Qualifier qualifier,
        List<Interceptor> interceptors) {
        Exec executableMethods = new Exec(true); (2)
        this.$proxyMethods[0] = executableMethods.getExecutableMethodByIndex(0); (3)
        this.$interceptors[0] = InterceptorChain
            .resolveAroundInterceptors(
                context,
                this.$proxyMethods[0],
                interceptors
        );  (4)
    }
}
```

| **1** | The `@Generated` subclass extends from the decorated type and implements the Intercepted interface |
|---|---|
| **2** | An instance of ExecutableMethodsDefinition is constructed to resolve reflection-free dispatchers to the original method. |
| **3** | An internal array called `$proxyMethods` holds a reference for to each ExecutableMethod instance used to proxy the invocation. |
| **4** | An internal array called `$interceptors` holds references to which Interceptor instances apply to each method since an @InterceptorBinding can be type or method level these may differ for each method. |

Each non-final and non-private method of the proxied type that has an @InterceptorBinding associated with it (either type level or method level) is overridden with logic that proxies the original method, for example:

```java
@Overrides
public void doWork(String taskName) {
    ExecutableMethod method = this.$proxyMethods[0];
    Interceptor[] interceptors = this.$interceptors[0]; (1)
    MethodInterceptorChain chain = new MethodInterceptorChain( (2)
        interceptors,
        this,
        method,
        new Object[]{taskName}
    );
    chain.proceed(); (3)
}
```

| **1** | The ExecutableMethod and array of Interceptor instances for the method is located. |
|---|---|
| **2** | A new MethodInterceptorChain is constructed with the interceptors, a reference to the intercepted instance, the method and the arguments. |
| **3** | The `proceed()` method is invoked on the MethodInterceptorChain. |

Note that the default behaviour of the @Around annotation is to invoke the original overridden method of the target type by calling the super implementation via a generated synthetic bridge method that allows access to the super implementation (in the above case `NotNullExample`).

In this arrangement the proxy and the proxy target are the same object, with interceptors being invoked and the call to `proceed()` invoke the original implementation via a call to `super.doWork()` in the case above.

However, this behaviour can be customized using the @Around annotation.

By setting `@Around(proxyTarget=true)` the generated code will also implement the InterceptedProxy interface which defines a single method called `interceptedTarget()` that resolves the target object the proxy should delegate method calls to.

|   | The default behaviour (`proxyTarget=false`) is more efficient memory wise as only a single BeanDefinition is required and a single instance of the proxied type. |
|---|---|

The evaluation of the proxy target is eager and done when the proxy is first created, however it can be made lazy by setting `@Around(lazy=true, proxyTarget=true)` in which case the proxy will only be retrieved when a proxied method is invoked.

The difference in behaviour between proxying the target with `proxyTarget=true` is illustrated in the following diagram:

The sequence on the left hand side of the diagram (`proxyTarget=false`) invokes the proxied method via a call to `super` whilst the sequence on the right looks up a proxy target from the BeanContext and invokes the method on the target.

One final customization option is `@Around(hotswap=true)` which triggers the compiler to produce a compile-time proxy that implements HotSwappableInterceptedProxy which defines a single method called `swap(..)` that allows swapping out the target of the proxy with a new instance (to allow this to be thread safe the generated code uses a `ReentrantReadWriteLock`).

### Security Considerations

Method interception via `AROUND` advice is typically used to define logic that addresses cross-cutting concerns, one of which is security.

When multiple Interceptor instances apply to a single method it may be important from a security perspective that these interceptors execute in a specific order.

The Interceptor interface extends the Ordered interface to enable the developer to control interceptor ordering by overriding the `getOrder()` method.

When the MethodInterceptorChain is constructed and multiple interceptors are present they are ordered with `HIGHEST` priority interceptors executed first.

To aid the developer who defines their own Around Advice the InterceptPhase enumeration defines various constants that can be used to correctly declare the value of `getOrder()` (for example security typically falls within the `VALIDATE` phase).

|   | Trace level logging can be enabled for the `io.micronaut.aop.chain` package to debug resolved interceptor order. |
|---|---|


## 23.1.6 Application Context

Once the job of the Micronaut Compiler is complete and the required classes generated, it is up to the BeanContext to load the classes for runtime execution.

Whilst the standard Java service loader mechanism is used to define instances of BeanDefinitionReference, the instances themselves are instead loaded with SoftServiceLoader which is a more lenient implementation that allows checking if the service is actually present before loading and also allows parallel loading of services.

The BeanContext performs the following steps:

1. Soft load all BeanDefinitionReference instances in parallel
2. Instantiate all beans annotated with @Context (beans scoped to the whole context)
3. Run each ExecutableMethodProcessor for each discovered processed ExecutableMethod. A method is regarded as "processed" if it is meta-annotated with `@Executable(processOnStartup = true)`
4. Publish an event on type StartupEvent for when the context is started.

The basic flow is illustrated below:

The ApplicationContext is a specialized version of the BeanContext that adds the notion of one or more active environments (encapsulated by Environment) and conditional bean loading based on this environment.

The Environment is loaded from one or more defined PropertySource instances that are discovered via the standard Java service loader mechanism by loading instances of PropertySourceLoader.

A developer can extend Micronaut to load a PropertySource through an entirely custom mechanism by adding another implementation and the associated `META-INF/services/io.micronaut.context.env.PropertySourceLoader` file referencing this class.

A high level different between a BeanContext and an ApplicationContext is illustrated below:

As seen above the ApplicationContext loads the Environment which is used for multiple purposes including:

- Enabling and disabling beans through Bean Requirements
- Allowing dependency injection of configuration via @Value or @Property
- Allowing binding of Configuration Properties
