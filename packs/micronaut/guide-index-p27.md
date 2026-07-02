---
title: "Micronaut Core (part 27/27)"
source: https://docs.micronaut.io/latest/guide/index.html
domain: micronaut
license: CC-BY-SA-4.0
tags: micronaut framework, micronaut jvm, compile-time injection, microservices framework
fetched: 2026-07-02
part: 27/27
---

## 23.1.7 HTTP Server

The Micronaut HTTP server can be considered a Micronaut Module - that is a component of Micronaut that builds on the fundamental building blocks including Dependency Injection and the lifecycle of the ApplicationContext.

The HTTP server includes a set of abstract interfaces and common code contained with the `micronaut-http` and `micronaut-http-server` modules respectively (the former includes HTTP primitives shared across the client and the server).

A default implementation of these interfaces is provided based on the Netty I/O toolkit the architecture of which is described in the image below:

The Netty API is in general a very low-level I/O networking API designed for integrators to use to build clients and servers that present a higher abstraction layer. The Micronaut HTTP server is one such abstraction layer.

An architecture diagram of the Micronaut HTTP server and the components used in its implementation is described below:

The main entry point for running the server is the Micronaut class which implements ApplicationContextBuilder. Typically, the developer places the following call into the `main` entry point of their application:

Defining a

main

entry point

```java
public static void main(String[] args) {
    Micronaut.run(Application.class, args);
}
```

|   | The passed arguments a transformed into a CommandLinePropertySource and available for dependency injection via @Value. |
|---|---|

Executing `run` will start the Micronaut ApplicationContext with the default settings and then search for a bean of type EmbeddedServer which is an interface that exposes information about a runnable server including host and port information. This design decouples Micronaut from the actual server implementation and whilst the default server is Netty (described above), other servers can be implemented by third-parties simply by providing an implementation of EmbeddedServer.

A sequence diagram for how the server is started is illustrated below:

In the case of the Netty implementation the EmbeddedServer interface is implemented by NettyHttpServer.

### Server Configuration

The NettyHttpServer reads the Server Configuration including:

- NettyHttpServerConfiguration - An extended version of HttpServerConfiguration which defines Netty-specific configuration options beyond the host, port etc.
- EventLoopGroupConfiguration - configures one or more Netty EventLoopGroup that can be configured to be either unique to the server or shared with one or more HTTP clients.
- ServerSslConfiguration - Provides configuration for the ServerSslBuilder for to configure the Netty SslContext to use for HTTPS.

### Server Configuration Security Considerations

Netty’s SslContext provides an abstraction which allows using either the JDK-provided `javax.net.ssl.SSLContext` or an OpenSslEngine that requires the developer to additionally add netty-tcnative as a dependency (`netty-tcnative` is a fork of Tomcat’s OpenSSL binding).

The ServerSslConfiguration allows configuring the application to a secure, readable location on disk where valid certificates exist to correctly configure the `javax.net.ssl.TrustManagerFactory` and `javax.net.ssl.KeyManagerFactory` by loading the configurtion from disk.

### Netty Server Initialization

When the NettyHttpServer executes the `start()` sequence, it will perform the following steps:

1. Read the EventLoopGroupConfiguration and create the parent and worker EventLoopGroup instances required to start a Netty server.
2. Compute a platform specific ServerSocketChannel to use (depending on Operating System this could either be Epoll or KQueue, falling back to Java NIO if no native binding is possible)
3. Creates the instance of ServerBootstrap used to initialze the SocketChannel (the connection between client and server).
4. The `SocketChannel` is initialized by a Netty ChannelInitializer that creates the customized Netty ChannelPipeline used to Micronaut to server HTTP/1.1 or HTTP/2 requests depending on configuration.
5. The Netty ServerBootstrap is bound to one or more configured ports, effectively making the server available to receive requests.
6. Two Bean Events are fired, first ServerStartupEvent to indicate the server has started, then finally once all these events are processed a ServiceReadyEvent only if the property `micronaut.application.name` is set.

This startup sequence is illustrated below:

A `NettyHttpServerInitializer` class is used to initialize the ChannelPipeline that handles incoming HTTP/1.1 or HTTP/2 requests.

### ChannelPipeline Security Considerations

The `ChannelPipeline` can be customized by the user by implementing a bean that implements the ChannelPipelineCustomizer interface and adding a new Netty ChannelHandler to the pipeline.

Adding a `ChannelHandler` allows performing tasks such as wire-level logging of incoming and outgoing data packets and may be used when wire-level security requirements are required such as validating the bytes of the incoming request body or outgoing response body.

### Netty Server Routing

Micronaut defines a set of HTTP annotations that allow binding user code to incoming HttpRequest instances and customizing the resulting HttpResponse.

One or many configured RouteBuilder implementations construct instances of UriRoute which is used by the Router components to route incoming requests methods of annotated classes such as:

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

Request binding annotations can be used to bind method parameters to the HTTP body, headers, parameters etc. and the framework will automatically deal with correctly escaping the data before it passed to the receiving method.

An incoming request is received by Netty and a `ChannelPipeline` initialized by `NettyHttpServerInitializer`. The incoming raw packets are transformed into a Netty HttpRequest which is subsequently wrapped in a Micronaut NettyHttpRequest which abstracts over the underlying Netty request.

The `NettyHttpRequest` is passed through the chain of Netty ChannelHandler instances until it arrives at `RoutingInBoundHandler` which uses the aforementioned Router to match the request a method of an annotated @Controller type.

The `RoutingInBoundHandler` delegates to RouteExecutor for actual execution of the route, which deals with all the logic to dispatch to a method of an annotated @Controller type.

Once executed, if the return value is not `null` an appropriate MediaTypeCodec is looked up from the MediaTypeCodecRegistry for the response Content-Type (defaulting to `application/json`). The `MediaTypeCodec` is used to encode the return value into a `byte[]` and include it as the body of the resulting HttpResponse.

The following diagram illustrates this flow for an incoming request:

The `RouteExecutor` will construct a FilterChain to execute one or many HttpServerFilter prior executing the target method of an annotated @Controller type.

Once all of the HttpServerFilter instances have been executed the RouteExecutor will attempt to satisfy the requirements of the target method’s parameters, including any Request binding annotations. If the parameters cannot be satisfied then a `HTTP 400 - Bad Request` HttpStatus response is returned to the calling client.

### Netty Server Routing Security Considerations

A HttpServerFilter instance can be used by the developer to control access to server resources. By not proceeding with the FilterChain an alternative response (such as a `403 - Forbidden`) can be returned to the client barring access to sensitive resources.

Note that the HttpServerFilter interface extends from the Ordered interface since it is frequently the case that multiple filters exist within a FilterChain. By implementing the `getOrder()` method the developer can return an appropriate priority to control ordering. In addition, the ServerFilterPhase enum provides a set of constants developers can use to correctly position a filter, including a `SECURITY` phase where security rules are commonly placed.


## 23.2 Frequently Asked Questions (FAQ)

The following section covers frequently asked questions that you may find yourself asking while considering to use or using Micronaut.

#### Does Micronaut modify my bytecode?

No. Your classes are your classes. Micronaut does not transform classes or modify the bytecode generated from the code you write. Micronaut produces additional classes at compile time in the same package as your original unmodified classes.

#### Why Doesn’t Micronaut use Spring?

When asking why Micronaut doesn’t use Spring, it is typically in reference to the Spring Dependency Injection container.

|   | The Spring ecosystem is very broad and there are many Spring libraries you can use directly in Micronaut without requiring the Spring container. |
|---|---|

The reason Micronaut features its own native JSR-330 compliant dependency injection is that the cost of these features in Spring (and any reflection-based DI/AOP container) is too great in terms of memory consumption and the impact on startup time. To support dependency injection at runtime, Spring:

- Reads the bytecode of every bean it finds at runtime.
- Synthesizes new annotations for each annotation on each bean method, constructor, field etc. to support Annotation metadata.
- Builds Reflective Metadata for each bean for every method, constructor, field, etc.

The result is a progressive degradation of startup time and memory consumption as your application incorporates more features.

For Microservices and Serverless functions where it is critical that startup time and memory consumption remain low, the above behaviour is an undesirable reality of using the Spring container, hence the designers of Micronaut chose not to use Spring.

#### Does Micronaut support Scala?

Micronaut supports any JVM language that supports the Annotation Processor API. Scala currently does not support this API. However, Groovy also doesn’t support this API and special support has been built that processes the Groovy AST. It may be technically possible to support Scala in the future if a module similar to `inject-groovy` is built, but as of this writing Scala is not supported.

#### Can Micronaut be used for purposes other than Microservices?

Yes. Micronaut is very modular, and you can choose to use just the Dependency Injection and AOP implementation by including the `micronaut-inject-java` (or `micronaut-inject-groovy` for Groovy) dependency in your application.

In fact Micronaut’s support for Serverless Computing uses this exact approach.

#### What are the advantages of Micronaut’s Dependency Injection and AOP implementation?

Micronaut processes your classes and produces all metadata at compile time. This eliminates the need for reflection, cached reflective metadata, and the requirement to analyze your classes at runtime, all of which lead to slower startup performance and greater memory consumption.

In addition, Micronaut builds reflection-free AOP proxies at compile time, which improves performance, reduces stack trace sizes, and reduces memory consumption.

#### Why does Micronaut have its own Consul and Eureka client implementations?

The majority of Consul and Eureka clients that exist are blocking and include many external dependencies that inflate your JAR files.

Micronaut’s DiscoveryClient uses Micronaut’s native HTTP client, greatly reducing the need for external dependencies and providing a reactive API onto both discovery servers.

#### Why am I encountering a NoSuchMethodError occurs loading my beans (Groovy)?

Groovy by default imports classes in the `groovy.lang` package, including one named `@Singleton`, an AST transformation class that makes your class a singleton by adding a private constructor and static retrieval method. This annotation is easily confused with the `jakarta.inject.Singleton` annotation used to define singleton beans in Micronaut. Make sure you use the correct annotation in your Groovy classes.

#### Why is it taking much longer than it should to start the application

Micronaut’s startup time is typically very fast. At the application level however, it is possible to affect startup time. If you are seeing slow startup, review any application startup listeners or `@Context` scope beans that are slowing startup.

Some network issues can also cause slow startup. On the Mac for example, misconfiguration of your `/etc/hosts` file can cause issues. See the following stackoverflow answer.


## 23.3 Using Snapshots

Micronaut milestone and stable releases are distributed to Maven Central.

The following snippet shows how to use Micronaut `SNAPSHOT` versions with Gradle. The latest snapshot will always be the next patch version plus 1 with `-SNAPSHOT` appended. For example if the latest release is "1.0.1", the current snapshot would be "1.0.2-SNAPSHOT".

```groovy
ext {
    micronautVersion = '4.10.0-SNAPSHOT'
}
repositories {
    mavenCentral() (1)
    maven {
      url = "https://central.sonatype.com/repository/maven-snapshots/" (2)
      mavenContent {
        snapshotsOnly()
      }
    }
}
```

| **1** | Micronaut releases are available on Maven Central |
|---|---|
| **2** | Micronaut snapshots are available on Central Sonatype `maven-snapshots` repository. |

In the case of Maven, edit `pom.xml`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
  ...

  <parent>
    <groupId>io.micronaut.platform</groupId>
    <artifactId>micronaut-parent</artifactId>
    <version>4.10.0-SNAPSHOT</version>
  </parent>

  <properties>
    <micronaut.version>4.10.0-SNAPSHOT</micronaut.version> (1)
    ...
  </properties>

  <repositories>
    <repository>
      <id>sonatype-snapshots</id>
      <url>https://central.sonatype.com/repository/maven-snapshots/</url> (2)
    </repository>
  </repositories>

  ...
</project>
```

| **1** | Set the snapshot version. |
|---|---|
| **2** | Micronaut snapshots are available on Sonatype. |


## 23.4 Common Problems

The following section covers common problems developers encounter when using Micronaut.

#### Dependency injection is not working

The most common causes of Dependency Injection failing to work are not having the appropriate annotation processor configured, or an incorrectly configured IDE. See the section on Language Support for how to get setup in your language.

#### A NoSuchMethodError occurs loading beans (Groovy)

By default, Groovy imports classes in the `groovy.lang` package which includes a class called `Singleton`. This is an AST transformation annotation that makes your class a singleton by adding a private constructor and static retrieval method. This annotation is easily confused with the `jakarta.inject.Singleton` annotation used to define singleton beans in Micronaut. Make sure you use the correct annotation in your Groovy classes.

#### It is taking much longer to start my application than it should (*nix OS)

This is likely due to a bug related to `java.net.InetAddress.getLocalHost()` calls causing a long delay. The solution is to edit your `/etc/hosts` file to add an entry containing your host name. To find your host name, run `hostname` in a terminal. Then edit your `/etc/hosts` file to add or change entries like the example below, replacing `<hostname>` with your host name.

```
127.0.0.1       localhost <hostname>
::1             localhost <hostname>
```

To learn more about this issue, see this stackoverflow answer


## 23.5 Breaking Changes

This section documents breaking changes between Micronaut versions

### HTTP client redirect forwarding no longer retains authorization headers cross-origin by default

The Netty HTTP client no longer forwards `Authorization`, `Proxy-Authorization`, or `Cookie` headers on cross-origin redirects by default. This applies to both normal redirects and preserve-body redirects (`307` and `308`).

If needed, this behavior can be customized through `HttpClientConfiguration`.


## 5.0

### Core Changes

#### Duplicate configuration resources now fail fast by default

In Micronaut Framework 5, if a configuration file such as `application.properties` or `application.yml` is present more than once on the classpath, Micronaut now fails fast by default with a ConfigurationException describing the conflicting locations.

See Duplicate Configuration Resources for more options (including merging duplicates).

To restore the previous behavior (first match wins), configure the application context builder:

Restoring FIRST_MATCH behavior

```java
ApplicationContext ctx = ApplicationContext.builder()
    .configurationLoadingStrategy(ResourceLoadStrategy.builder()
        .type(ResourceLoadStrategyType.FIRST_MATCH))
    .start();
```

Restoring FIRST_MATCH behavior

```kotlin
val ctx = ApplicationContext.builder()
    .configurationLoadingStrategy(
        ResourceLoadStrategy.builder()
            .type(ResourceLoadStrategyType.FIRST_MATCH)
    )
    .start()
```

Restoring FIRST_MATCH behavior

```groovy
ApplicationContext ctx = ApplicationContext.builder()
    .configurationLoadingStrategy(ResourceLoadStrategy.builder()
        .type(ResourceLoadStrategyType.FIRST_MATCH))
    .start()
```

#### Adoption of the IANA standard for YAML media types

Micronaut now uses official **application/yaml** media type for YAML format. Before it was **application/x-yaml**. See https://www.rfc-editor.org/rfc/rfc9512.html for details.

#### Update to Jackson 3

Micronaut Jackson Databind uses Jackson 3. If you use Micronaut Jackson Databind, check the Jackson 3 Migration Guide.

Micronaut configuration properties for various Jackson features have been renamed. Please check the configuration reference. Also note that Jackson has renamed a few features upstream, and that various defaults have changed.

#### Update to Apache Groovy 5

Micronaut 5 uses Apache Groovy 5. Check Groovy 5 breaking changes.

#### JSpecify Nullability Annotations

The Micronaut APIs use JSpecify Annotations, and we recommend users to embrace JSpecify nullability annotations.

#### Bean context changes

The default implementations of BeanContext, ApplicationContext and Environment are no longer public and non-final.

There are new options added to ApplicationContextBuilder which allow to modify the behavior of the bean context without overring it:

```java
ApplicationContext myBootstrapContext = ApplicationContext.builder()
    .deducePackage(false)
    .deduceEnvironment(false)
    .eventsEnabled(false)
    .eagerBeansEnabled(false)
    .beansPredicate(reference -> reference.isAnnotationPresent(BootstrapContextCompatible.class))
    .build();
```

Alternatively there is a new way how to create Environment:

```java
Environment myEnv = Environment.create(new ApplicationContextConfiguration() {
    @Override
    public List<String> getEnvironments() {
        return List.of("foobar");
    }
});

ApplicationContext customApplicationContext = ApplicationContext.create(myEnv);
```

#### Bean context performance improvements

The bean context in v5 tries to avoid scanning all available beans as much as possible. The bean definitions are now generated with all posible exposed types (if not explicitly defined by `@Bean(typed=..)`).

Beans added at the runtime require all the exposed types (supertypes and interfaces) explicitly defined:

```java
class FooBar extends Abc implements Resolver<String> {
}

// In v4 this registration will resolve beans by class FooBar, Abc and Resolver
beanContext.registerSingleton(new FooBar());

// In v5 it is necessary to register it in the following way:
context.registerBeanDefinition(
    RuntimeBeanDefinition.builder(new FooBar())
        .singleton(true)
        .exposedTypes(FooBar.class, Abc.class, Resolver.class)
        .typeArguments(Resolver, Argument.of(String))
        .build()
);
```

#### Runtime annotation processors changes

The `@Executable` methods processor processor should be used only to process the executable methods that should be processed at startup. The annotation should be annotated with `@Executable(processOnStartup = true)`. For other use-cases (executable or not) processor should be used.

The incorrect use will result in a warning and an error in the next major version.

Both interfaces are revisited to have better generics and no longer have now deleted `AnnotationProcessor` superclass.

Executable methods annotated with `@Parallel` will not trigger parallel execution of processor. Users who relied on that functionality should handle parallelism separately.

`@Scheduled` is no longer processed in parallel, this reduced the complexity of the method processor and removed unnecessary overhead.

#### HTTP server thread selection now applies across more request stages

Micronaut 5 extends server `thread-selection` handling so that it applies not only to route execution, but also to server filters and request event listeners.

As a result, applications that previously observed different threads for filters, event listeners, and controllers may now see those stages executed more consistently on the executor selected by the server configuration.

The `micronaut.server.netty.redispatch-non-blocking-only` setting now controls whether Micronaut redispatches again after request processing has already moved from the initial non-blocking event-loop thread to a blocking-capable thread:

- `true` skips repeated redispatch once execution is already on a blocking-capable thread. This reduces executor hops and avoids creating additional virtual threads for every filter, event listener, and controller stage.
- `false` applies the configured executor at each stage even if the current thread is already blocking-capable. This more closely matches the previous behavior, but may introduce more thread hops and, when using virtual threads, more virtual thread creation during one request.

If your application depends on specific thread transitions between filters, event listeners, and route handlers, review this setting and test request-processing behavior after upgrading.

#### Jackson Bean Introspection Module removed

|   | This change only affects users using Micronaut Jackson Databind |
|---|---|

Previous versions of Micronaut Core contained a so-called "bean introspection module". This Jackson module hooked into jackson-databind to replace reflective field and method access with Micronaut introspection-based calls. The performance difference is negligible, but the module allows serialization in native images without having to add reflection metadata.

In version 5, we removed this module because it is difficult to maintain. Native image users now have a good alternative to Micronaut Jackson Databind in Micronaut Serialization.

Users who do not wish to use Micronaut Serialization will have to add reflection metadata for the objects they serialize.

If you want to keep using Micronaut Jackson Databind, beware that deserialization of such class works in Micronaut 4:

```java
package example;

import java.util.Objects;

public class Person {
    private final String name;
    private final int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }
}
```

In Micronaut 5, you will need to add `@JsonProperty` annotations to the constructor parameters. This is standard Jackson databind deserialization behavior.

```java
package example;

import com.fasterxml.jackson.annotation.JsonProperty;

import java.util.Objects;

public class Person {
    private final String name;
    private final int age;

    public Person(@JsonProperty("name") String name,
                  @JsonProperty("age") int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }
}
```

To generate a GraalVM Native Image, where you need to de/serialize such as class, you can add the following dependency:

`annotationProcessor("io.micronaut.graal:micronaut-graal")` `<annotationProcessorPaths> <path> <groupId>io.micronaut.graal</groupId> <artifactId>micronaut-graal</artifactId> </path> </annotationProcessorPaths>`

and annotate it with ReflectiveAccess. Read Graal section of the Micronaut core documentation.

```java
package example;

import java.util.Objects;
import com.fasterxml.jackson.annotation.JsonProperty;
import io.micronaut.core.annotation.ReflectiveAccess;

@ReflectiveAccess
public class Person {
    private final String name;
    private final int age;

    public Person(@JsonProperty("name") String name,
                  @JsonProperty("age") int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }
}
```


## 4.0.0

### Core Changes

#### Further Micronaut Modularization

The `micronaut-runtime` module has been split into separate modules depending on the application’s use case:

##### Micronaut Discovery Core

`micronaut-discovery-core` - The base service discovery features are now a separate module. If your application listens for events such as ServiceReadyEvent or HeartBeatEvent this module should be added to the application classpath.

`implementation("io.micronaut:micronaut-discovery-core")` `<dependency> <groupId>io.micronaut</groupId> <artifactId>micronaut-discovery-core</artifactId> </dependency>`

##### Micronaut Retry

`micronaut-retry` - The retry implementation including annotations such as @Retryable is now a separate module that can be optionally included in a Micronaut application.

In addition, since `micronaut-retry` is now optional declarative clients annotated with @Client no longer invoke fallbacks by default. To restore the previous behaviour add `micronaut-retry` to your classpath and annotate any declarative clients with @Recoverable.

To use the Retry functionality, add the following dependency:

`implementation("io.micronaut:micronaut-retry")` `<dependency> <groupId>io.micronaut</groupId> <artifactId>micronaut-retry</artifactId> </dependency>`

#### Calling `registerSingleton(bean)` no longer overrides existing beans

If you call `registerSingleton(bean)` on the BeanContext it will no longer override existing beans if the type and qualifier match; instead, two beans will exist which may lead to a NonUniqueBeanException.

If you require replacing an existing bean you must formalize the replacement using the RuntimeBeanDefinition API, for example:

```java
context.registerBeanDefinition(
    RuntimeBeanDefinition.builder(Codec.class, ()-> new OverridingCodec())
            .singleton(true)
            // the type of the bean to replace
            .replaces(ToBeReplacedCodec.class)
            .build()
);
```

#### WebSocket No Longer Required

`io.micronaut:micronaut-http-server` no longer exposes `micronaut-websocket` transitively. If you are using annotations such as @ServerWebSocket, you should add the `micronaut-websocket` dependency to your application classpath:

`implementation("io.micronaut:micronaut-websocket")` `<dependency> <groupId>io.micronaut</groupId> <artifactId>micronaut-websocket</artifactId> </dependency>`

#### Reactor Instrumentation Moved to Reactor Module

The instrumentation features for Reactor have been moved to the `micronaut-reactor` module. If you require instrumentation of reactive code paths (for distributed tracing for example) you should make sure your application depends on `micronaut-reactor`:

`implementation("io.micronaut.reactor:micronaut-reactor")` `<dependency> <groupId>io.micronaut.reactor</groupId> <artifactId>micronaut-reactor</artifactId> </dependency>`

#### Validation Support Moved to Validation Module

The validation features have been moved to a separate module. Moreover, the new validation module requires you to use `micronaut-validation-processor` in the annotation processor classpath.

`annotationProcessor("io.micronaut.validation:micronaut-validation-processor")` `<annotationProcessorPaths> <path> <groupId>io.micronaut.validation</groupId> <artifactId>micronaut-validation-processor</artifactId> </path> </annotationProcessorPaths>`

`implementation("io.micronaut.validation:micronaut-validation")` `<dependency> <groupId>io.micronaut.validation</groupId> <artifactId>micronaut-validation</artifactId> </dependency>`

#### Session Support Moved to Session Module

The Session handling features have been moved to their own module. If you use the HTTP session module, change the maven coordinates from `io.micronaut:micronaut-session` to `io.micronaut.session:micronaut-session`.

`implementation("io.micronaut.session:micronaut-session")` `<dependency> <groupId>io.micronaut.session</groupId> <artifactId>micronaut-session</artifactId> </dependency>`

#### Kotlin Flow Support Moved to Kotlin Module

Support for the Kotlin `Flow` type has been moved to the `micronaut-kotlin` module. If your application uses Kotlin `Flow` you should ensure the `micronaut-kotlin-runtime` module is on your application classpath:

`implementation("io.micronaut.kotlin:micronaut-kotlin-runtime")` `<dependency> <groupId>io.micronaut.kotlin</groupId> <artifactId>micronaut-kotlin-runtime</artifactId> </dependency>`

#### Compilation Time API Split into new module

In order to keep the runtime small all types and interfaces that are used at compilation time only (like the `io.micronaut.inject.ast` API) have been moved into a separate module:

`implementation("io.micronaut:micronaut-core-processor")` `<dependency> <groupId>io.micronaut</groupId> <artifactId>micronaut-core-processor</artifactId> </dependency>`

If you are using types and interfaces from this module you should take care to split the compilation time and runtime logic of your module into separate modules.

#### ASM No Longer Shaded

ASM is no longer shaded into the `io.micronaut.asm` package. If you depend on this library you should directly depend on the latest version of ASM.

#### Caffeine No Longer Shaded

Caffeine is no longer shaded into the `io.micronaut.caffeine` package. If you depend on this library you should directly depend on the latest version of Caffeine.

#### Environment Deduction Disabled by Default

In previous versions of the Micronaut framework, probes were used to attempt to deduce the running environment and establish whether the application was running in the Cloud. These probes involved network calls resulting in issues with startup performance and security concerns. These probes are disabled by default and can be re-enabled as necessary by calling `ApplicationContextBuilder.deduceCloudEnvironment(true)`, setting the system property `micronaut.env.cloud-deduction` to `true` or setting the environment `MICRONAUT_ENV_CLOUD_DEDUCTION` to `true` if your application still requires this functionality.

#### Update to Groovy 4

Micronaut now uses Groovy 4. This means that Groovy 4 is now the minimum version required to run Groovy Micronaut applications. There have been several core differences in Groovy parsing and behavior for version 4 which can be found in the breaking changes section of the 4.0.0 release notes.

#### SnakeYAML no longer a direct dependency

SnakeYAML is no longer a direct dependency, if you need YAML configuration you should add SnakeYAML to your classpath explicitly

#### `javax.annotation` no longer a directory dependency

The `javax.annotation` library is no longer a directory dependency. Any references to types in the `javax.anotation` package should be changed to `jakarta.annotation`

#### Kotlin base version updated to 1.8.21

Kotlin has been updated to 1.8.21, which may cause issues when compiling or linking to Kotlin libraries.

#### Bean Introspection changes

Before, when both METHOD and FIELD were set as the access kind, the bean introspection would choose the same access type to get and set the property value. In Micronaut 4, the accessors can be of different kinds: a field to get and a method to set, and vice versa.

#### Annotations with retention CLASS are excluded at runtime

Annotations with the retention CLASS are not available in the annotation metadata at the runtime.

#### Interceptors with multiple interceptor bindings annotations

Interceptors with multiple interceptor binding annotations now require the same set of annotations to be present at the intercepted point. In the Micronaut 3 an interceptor with multiple binding annotations would need at least one of the binding annotations to be present at the intercepted point.

#### `ConversionService` and `ConversionService.SHARED` is no longer mutable

New type converters can be added to MutableConversionService retrieved from the bean context or by declaring a bean of type TypeConverter. To register a type converter into `ConversionService.SHARED`, the registration needs to be done via the service loader.

#### `ExceptionHandler` with POJO response type no longer results in an error response

Previously if you had an ExceptionHandler such as:

```java
@Singleton
public class MyExceptionHandler implements ExceptionHandler<MyException, String> {

    @Override
    public String handle(HttpRequest request, MyException exception) {
        return "caught!";
    }
}
```

This would result in an internal server error response with `caught!` as the body. This now returns an OK response. If you want to return a POJO response as an error, you should use the `HttpResponse` type:

```java
@Singleton
public class MyExceptionHandler implements ExceptionHandler<MyException, HttpResponse<String>> {

    @Override
    public HttpResponse<String> handle(HttpRequest request, MyException exception) {
        return HttpResponse.badRequest("caught!");
    }
}
```

#### `HttpContentProcessor` superseded by `MessageBodyHandler` API

The netty-specific `HttpContentProcessor` API has been replaced by a new, experimental `MessageBodyHandler` API that does not rely on netty and is more powerful. There is no compatibility layer, so the old `HttpContentProcessor` will stop working and need to be rewritten.

#### `@Body` annotation on controller parameters

Before 4.0, the binding logic for controller parameters was more lax. A bare parameter, e.g. `void test(String title)`, could either match a part of the request body (`foo` if the request body is `{"title":"foo"}`), come from a query parameter, or could bind to the full request body (`{"x":"y"}` if the request body is `{"x":"y"}`).

Binding from the full body to these bare parameters is no longer supported. If you wish to bind the full body, the parameter *must* be annotated with `@Body`.

Additionally, it is no longer permitted to mix body component binding with full body binding. For example, `void test(@Body Bean bean, String title)` will not work anymore if `title` needs to come from the body that is already bound to `bean`.

These changes also apply to functions that are exposed using `micronaut-function-web`.

#### Delayed body access

When accessing the request body in two places, for example once as a normal controller `@Body` parameter and then in an error handler, Micronaut HTTP is now stricter about allowed types. If in doubt, for the second body access, call `HttpRequest.getBody()` and you will get the same body type the first access requested.

#### `text/plain` messages are more restrictive about allowed types

For `text/plain` request and response body reading and writing, in 3.x any type was allowed. For writing, the object was converted using `toString`, and for reading, the object was converted using `ConversionService`. For example, if you have a controller that returns an `Instant` as `text/plain`, it would write it using `toString` like `2023-05-25T13:25:02.925Z`. In the other direction, if you have a controller with a `@Body Instant instant` parameter, the same text would be converted to `Instant` using `ConversionService`.

This is not permitted anymore for 4.x, except for some restricted types. The recommended fix is to move to `application/json` as the content type. `toString` is not a stable serialization format, JSON is more reliable.

Alternatively, you can set the `micronaut.http.legacy-text-conversion` configuration option to `true` to restore the old behavior.

#### `OncePerRequestHttpServerFilter` removed

Since Micronaut 3.0 the `OncePerRequestHttpServerFilter` class was deprecated and marked for removal. This class is now removed. Implement HttpServerFilter instead, and replace any usages of `micronaut.once` attributes with a custom attribute name.

#### CORS support with the `@CrossOrigin` annotation

Micronaut Framework 4 changes `@CrossOrigin` behavior to match configuration-based CORS behavior. A method annotated with `@CrossOrigin` allows any origin if you don’t specify any value for the `allowedOrigins` and `allowedOriginsRegex` members.

Micronaut Framework 5 changes the default value of `@CrossOrigin.allowCredentials` from `true` to `false`. If your application relies on credentialed cross-origin requests, set `allowCredentials = true` explicitly.

#### `@EachBean` requires a `@Named qualifier

`@EachBean` throws a "multiple possible bean candidates found" exception if any parent bean lacks a name qualifier.

#### Manual Context Propagation

In Micronaut Framework 4, users need to extend the propagation context manually.

#### Micronaut 3 libraries not compatible with Micronaut 4 applications

In order for Micronaut 3 library beans to be discoverable in an application running Micronaut 4, the library must be recompiled with Micronaut 4 - https://github.com/micronaut-projects/micronaut-core/discussions/9758

#### @Retryable Default Exception Type

The default exception type used by `@Retryable` has changed. Previously, `@Retryable` would retry only when a `RuntimeException` (or subclass) was thrown. In Micronaut 5, the default has been changed to `Exception`. As a result, checked exceptions will now also trigger retry behavior. If the previous behavior is desired, configure the retryable annotation explicitly:

```java
@Retryable(includes = RuntimeException.class)
```
