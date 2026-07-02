---
title: "Micronaut Core (part 24/27)"
source: https://docs.micronaut.io/latest/guide/index.html
domain: micronaut
license: CC-BY-SA-4.0
tags: micronaut framework, micronaut jvm, compile-time injection, microservices framework
fetched: 2026-07-02
part: 24/27
---

## 16.3.11 Reactive Context Propagation

The Micronaut framework supports context propagation from Reactor’s context to coroutine context. To enable this propagation you need to include following dependency:

`implementation("org.jetbrains.kotlinx:kotlinx-coroutines-reactor")` `<dependency> <groupId>org.jetbrains.kotlinx</groupId> <artifactId>kotlinx-coroutines-reactor</artifactId> </dependency>`

For more detailed information on how to use the library you can find at the official documentation.

|   | Since Micronaut framework 4, we recommend using the latest Context Propagation API. The ThreadPropagatedContextElement is inspired by Kotlin Coroutines propagation API element `kotlinx.coroutines.ThreadContextElement` and acts similarly by restoring thread locals. |
|---|---|

Following example shows how to propagate Reactor context from the HTTP filter to the controller’s coroutine:

Simple filter which writes into Reactor’s context

```kotlin
@Filter(Filter.MATCH_ALL_PATTERN)
class ReactorHttpServerFilter : HttpServerFilter {

    override fun doFilter(request: HttpRequest<*>, chain: ServerFilterChain): Publisher<MutableHttpResponse<*>> {
        val trackingId = request.headers["X-TrackingId"] as String
        return Mono.from(chain.proceed(request)).contextWrite {
            it.put("reactorTrackingId", trackingId)
        }
    }

    override fun getOrder(): Int = 1
}
```

Access Reactor context by retrieving `ReactorContext` from the coroutine context:

Reading Reactor context in the coroutine

```kotlin
@Get("/data")
suspend fun getTracingId(request: HttpRequest<*>): String {
    val reactorContextView = currentCoroutineContext()[ReactorContext.Key]!!.context
    return reactorContextView.get("reactorTrackingId") as String
}
```

It’s possible to use coroutines Reactor integration to create a filter using a suspended function:

Suspended function filter which writes into Reactor’s context

```kotlin
@Filter(Filter.MATCH_ALL_PATTERN)
class SuspendHttpServerFilter : CoroutineHttpServerFilter {

    override suspend fun filter(request: HttpRequest<*>, chain: ServerFilterChain): MutableHttpResponse<*> {
        val trackingId = request.headers["X-TrackingId"] as String
        //withContext does not merge the current context so data may be lost
        return withContext(Context.of("suspendTrackingId", trackingId).asCoroutineContext()) {
            chain.next(request)
        }
    }

    override fun getOrder(): Int = 0
}

interface CoroutineHttpServerFilter : HttpServerFilter {

    suspend fun filter(request: HttpRequest<*>, chain: ServerFilterChain): MutableHttpResponse<*>

    override fun doFilter(request: HttpRequest<*>, chain: ServerFilterChain): Publisher<MutableHttpResponse<*>> {
        return mono {
            filter(request, chain)
        }
    }

}

suspend fun ServerFilterChain.next(request: HttpRequest<*>): MutableHttpResponse<*> {
    return this.proceed(request).asFlow().single()
}
```


## 16.4 Micronaut for GraalVM

GraalVM is an advanced JDK with ahead-of-time Native Image compilation, to generate native executables of Micronaut applications.

Any Micronaut application can be run on the GraalVM JDK, however special support has been added to Micronaut to support running Micronaut applications using GraalVM’s `native-image` tool.

Micronaut framework currently supports GraalVM version 25.0.2 and the team is improving the support in every new release. Don’t hesitate to report issues however if you find any problem.

Many of Micronaut’s modules and third-party libraries have been verified to work with GraalVM: HTTP server, HTTP client, Function support, Micronaut Data JDBC and JPA, Service Discovery, RabbitMQ, Views, Security, Zipkin, etc. Support for other modules is evolving and will improve over time.

### Getting Started

|   | Only Java and Kotlin projects support using GraalVM’s `native-image` tool. Groovy relies heavily on reflection, which is only partially supported by GraalVM. |
|---|---|

To start using GraalVM, install this JDK. The easiest way to install GraalVM on Linux or Mac is to use SDKMAN!. For other installation options, visit the Downloads page.


## 16.4.1 Microservices as GraalVM native images

### Getting Started with Micronaut Framework and GraalVM

Starting with Micronaut framework 2.2, any Micronaut application can be built into a native image using the Micronaut Gradle or Maven plugins. To get started, create a new application.

Creating a GraalVM Native Microservice

```bash
$ mn create-app hello-world
```

You can use `--build maven` for a Maven build.

#### Building a Native Image Using Docker

To build your native image using Docker and Gradle, run:

Building a Native Image with Docker and Gradle

```bash
$ ./gradlew dockerBuildNative
```

To build your native image using Docker and Maven, run:

Building a Native Image with Docker and Maven

```bash
$ ./mvnw package -Dpackaging=docker-native
```

#### Building a Native Image Without Using Docker

To build your native image without using Docker, install a GraalVM JDK. The easiest way to install GraalVM on Linux or Mac is to use SDKMAN!. For other installation options, visit the Downloads page.

Installing GraalVM 25.0.2 with SDKMAN!

```bash
$ sdk install java 25.0.2-graal
$ sdk use java 25.0.2-graal
```

Once you install GraalVM, the `native-image` tool becomes available.

##### Gradle

You can build a native image with Gradle by running the `nativeCompile` task:

Creating a native image with Gradle

```bash
$ ./gradlew nativeCompile
```

The native executable file is created in the *build/native/nativeCompile* directory. You can then run it from that directory: `./build/native/nativeCompile/hello-world`.

It is possible to pass additional build arguments to `native-image` using the Gradle plugin for Native Image building. Add the following configuration to *build.gradle*:

build.gradle

```groovy
graalvmNative {
    binaries {
        main {
            imageName.set('myApp') (1)
            buildArgs.add('-Ob') (2)
        }
    }
}
```

| **1** | Use `imageName.set()` to specify a custom name. |
|---|---|
| **2** | Use `buildArgs.add()` to pass extra build arguments to `native-image`. For example, `-Ob` enables the quick build mode. |

##### Maven

To create a native image with Maven, use the `native-image` packaging format:

Creating a native image with Maven

```bash
$ ./mvnw package -Dpackaging=native-image
```

The native executable file is created in the *target/* directory. You can then run it from that directory: `./target/hello-world`.

It is possible to pass additional build arguments to `native-image` using the Maven plugin for Native Image building. Declare the plugin as following:

pom.xml

```xml
<plugin>
    <groupId>org.graalvm.buildtools</groupId>
    <artifactId>native-maven-plugin</artifactId>
    <version>${native-maven-plugin.version}</version>
    <configuration>
        <!-- <1> -->
        <imageName>myApp</imageName>
        <buildArgs>
              <!-- <2> -->
          <buildArg>-Ob</buildArg>
        </buildArgs>
    </configuration>
</plugin>
```

| **1** | Use `<imageName>` to specify a custom name. |
|---|---|
| **2** | Use `buildArg` to pass extra build arguments to `native-image`. For example, `-Ob` enables the quick build mode. |

### Understanding Micronaut Framework and GraalVM

The Micronaut framework itself does not rely on reflection or dynamic class loading, so it works automatically with GraalVM Native Image. However certain third-party libraries used by Micronaut may require additional input about uses of reflection.

The Micronaut framework includes an annotation processor that helps to generate reflection configuration that is automatically picked up by the `native-image` tool:

`annotationProcessor("io.micronaut:micronaut-graal")` `<annotationProcessorPaths> <path> <groupId>io.micronaut</groupId> <artifactId>micronaut-graal</artifactId> </path> </annotationProcessorPaths>`

This processor generates additional classes that implement the GraalReflectionConfigurer interface and programmatically register reflection configuration.

For example, see the following class:

```java
package example;

import io.micronaut.core.annotation.ReflectiveAccess;

@ReflectiveAccess
class Test {
    ...
}
```

The above example results in the public methods, declared fields, and declared constructors of `example.Test` being registered for reflective access.

If you have more advanced requirements and wish to include only certain fields or methods, use the annotation on any constructor, field, or method to include only the specific field, constructor, or method.

### Adding Additional Classes for Reflective Access

The Micronaut framework provides several annotations to specify additional classes that should be included in the generated reflection configuration, such as:

- @ReflectiveAccess - An annotation that can be declared on a specific type, constructor, method, or field to enable reflective access just for the annotated element.
- @TypeHint - An annotation that allows to bulk configuration of reflective access to one or many types.
- @ReflectionConfig - A repeatable annotation that directly models the reflection configuration in JSON format.

The `@ReflectiveAccess` annotation is typically used on a particular type, constructor, method, or field whilst the latter two are typically used on a module or `Application` class to include classes that are needed reflectively. See the following example from Micronaut’s Jackson module with `@TypeHint`:

Using the

@TypeHint

annotation

```java
@TypeHint(
    value = { (1)
        PropertyNamingStrategy.UpperCamelCaseStrategy.class,
        ArrayList.class,
        LinkedHashMap.class,
        HashSet.class
    },
    accessType = TypeHint.AccessType.ALL_DECLARED_CONSTRUCTORS (2)
)
```

| **1** | The `value` member specifies which classes require reflection. |
|---|---|
| **2** | The `accessType` member specifies if only class loading access is needed or whether full reflection on all public members is needed. |

Alternatively, use the `@ReflectionConfig` annotation which is repeatable and allows distinct configuration per type:

Using the

@ReflectionConfig

annotation

```java
@ReflectionConfig(
    type = PropertyNamingStrategy.UpperCamelCaseStrategy.class,
    accessType = TypeHint.AccessType.ALL_DECLARED_CONSTRUCTORS
)
@ReflectionConfig(
    type = ArrayList.class,
    accessType = TypeHint.AccessType.ALL_DECLARED_CONSTRUCTORS
)
@ReflectionConfig(
    type = LinkedHashMap.class,
    accessType = TypeHint.AccessType.ALL_DECLARED_CONSTRUCTORS
)
@ReflectionConfig(
    type = HashSet.class,
    accessType = TypeHint.AccessType.ALL_DECLARED_CONSTRUCTORS
)
```

### Generating Native Images

GraalVM’s `native-image` command generates native images. You can use this command manually to generate your native image. For example:

The

native-image

command

```bash
native-image --class-path build/libs/hello-world-0.1-all.jar (1)
```

| **1** | The `class-path` argument refers to the Micronaut shaded JAR. |
|---|---|

Once the image is built, run the application using its name:

Running the native application

```bash
$ ./hello-world
15:15:15.153 [main] INFO  io.micronaut.runtime.Micronaut - Startup completed in 14ms. Server Running: http://localhost:8080
```

As you can see, the native image startup completes in milliseconds, and memory consumption does not include the overhead of the JVM (a native Micronaut application runs with just 20MB of memory).

### Resource File Generation

Starting with Micronaut framework 3.0, the automatic generation of the *resource-config.json* file is now integrated into the Gradle and Maven plugins.


## 16.4.2 GraalVM and Micronaut FAQ

#### How does Micronaut Framework manage to run on GraalVM?

The Micronaut framework features a Dependency Injection and Aspect-Oriented Programming runtime that uses no reflection. This makes it easier for Micronaut applications to run on GraalVM since there are compatibility concerns particularly around reflection in Native Image.

#### How can I make a Micronaut application that uses Picocli run on GraalVM?

Picocli provides a `picocli-codegen` module with a tool for generating a GraalVM reflection configuration file. The tool can be run manually or automatically as part of the build. The module’s README has usage instructions with code snippets for configuring Gradle and Maven to generate a `cli-reflect.json` file automatically as part of the build. Add the generated file to the `-H:ReflectionConfigurationFiles` option when running the `native-image` tool.

#### What about other third-party libraries?

The Micronaut framework cannot guarantee that third-party libraries work with GraalVM Native Image. It is up to each individual library to implement support.

#### I Get a "Class XXX is instantiated reflectively…" exception. What do I do?

If you get an error such as:

```
Class myclass.Foo[] is instantiated reflectively but was never registered. Register the class by using org.graalvm.nativeimage.RuntimeReflection
```

You may need to manually tweak the generated *reflect.json* file. For regular classes you need to add an entry into the array:

```json
[
    {
        "name" : "myclass.Foo",
        "allDeclaredConstructors" : true
    },
    ...
]
```

Learn more about providing reflection configuration in the Native Image Reachability documentation. For arrays, this must use the Java JVM internal array representation. For example:

```json
[
    {
        "name" : "[Lmyclass.Foo;",
        "allDeclaredConstructors" : true
    },
    ...
]
```

#### What if I want to set the maximum heap size with `-Xmx`, but I get an `OutOfMemoryError`?

If you set the maximum heap size in the Dockerfile that you use to build your native image, you will probably get a runtime error like this:

```
java.lang.OutOfMemoryError: Direct buffer memory
```

The problem is that Netty tries to allocate 16MB of memory per chunk with its default settings for `io.netty.allocator.pageSize` and `io.netty.allocator.maxOrder`:

```java
int defaultChunkSize = DEFAULT_PAGE_SIZE << DEFAULT_MAX_ORDER; // 8192 << 11 = 16MB
```

The simplest solution is to specify `io.netty.allocator.maxOrder` explicitly in your Dockerfile’s entrypoint. See below a working example with `-Xmx64m`:

```dockerfile
ENTRYPOINT ["/app/application", "-Xmx64m", "-Dio.netty.allocator.maxOrder=8"]
```

To go further, you can also experiment with `io.netty.allocator.numHeapArenas` or `io.netty.allocator.numDirectArenas`. You can find more information about Netty’s `PooledByteBufAllocator` in the official documentation.

# 17 Management & Monitoring

|   | Using the CLI If you create your project using the Micronaut CLI, supply the `management` feature to configure the management endpoints in your project: $ mn create-app my-app --features management |
|---|---|

Inspired by Spring Boot and Grails, the Micronaut `management` dependency adds support for monitoring of your application via **endpoints**: special URIs that return details about the health and state of your application. The `management` endpoints are also integrated with Micronaut’s `security` dependency, allowing for sensitive data to be restricted to authenticated users in your security system (see Built-in Endpoints Access in the Security section).

To use the `management` features described in this section, add this dependency to your build:

`implementation("io.micronaut:micronaut-management")` `<dependency> <groupId>io.micronaut</groupId> <artifactId>micronaut-management</artifactId> </dependency>`


## 17.1 Creating Endpoints

In addition to the Built-In Endpoints, the `management` dependency also provides support for creating custom endpoints. These can be enabled and configured like the built-in endpoints, and can be used to retrieve and return any metrics or other application data.


## 17.1.1 The Endpoint Annotation

An Endpoint can be created by annotating a class with the Endpoint annotation, and supplying it with (at minimum) an endpoint id.

FooEndpoint.java

```java
@Endpoint("foo")
class FooEndpoint {
    ...
}
```

If a single `String` argument is supplied to the annotation, it is used as the endpoint id.

It is possible to supply additional (named) arguments to the annotation. Other possible arguments to `@Endpoint` are described in the table below:

| Argument | Description | Endpoint Example |
|---|---|---|
| `String id` | The endpoint id (or name) | `@Endpoint(id = "foo")` |
| `String prefix` | Prefix used for configuring the endpoint (see Endpoint Configuration) | `@Endpoint(prefix = "foo")` |
| `boolean defaultEnabled` | Sets whether the endpoint is enabled when no configuration is set (see Endpoint Configuration) | `@Endpoint(defaultEnabled = false)` |
| `boolean defaultSensitive` | Sets whether the endpoint is sensitive if no configuration is set (see Endpoint Configuration) | `@Endpoint(defaultSensitive = false)` |


## Example of custom Endpoint

The following example `Endpoint` class creates an endpoint accessible at `/date`:

CurrentDateEndpoint

```java
import io.micronaut.management.endpoint.annotation.Endpoint;

@Endpoint(id = "date",
          prefix = "custom",
          defaultEnabled = true,
          defaultSensitive = false)
public class CurrentDateEndpoint {

//.. endpoint methods

}
```

CurrentDateEndpoint

```kotlin
import io.micronaut.management.endpoint.annotation.Endpoint

@Endpoint(id = "date", prefix = "custom", defaultEnabled = true, defaultSensitive = false)
class CurrentDateEndpoint {

//.. endpoint methods

}
```

CurrentDateEndpoint

```groovy
import io.micronaut.management.endpoint.annotation.Endpoint

@Endpoint(id = "date",
          prefix = "custom",
          defaultEnabled = true,
          defaultSensitive = false)
class CurrentDateEndpoint {

//.. endpoint methods

}
```


## 17.1.2 Endpoint Methods

Endpoints respond to `GET` ("read"), `POST` ("write") and `DELETE` ("delete") requests. To return a response from an endpoint, annotate its public method(s) with one of the following annotations:

| Annotation | Description |
|---|---|
| Read | Responds to `GET` requests |
| Write | Responds to `POST` requests |
| Delete | Responds to `DELETE` requests |


## Read Methods

Annotating a method with the Read annotation causes it to respond to `GET` requests.

CurrentDateEndpoint

```java
import io.micronaut.management.endpoint.annotation.Endpoint;

import io.micronaut.management.endpoint.annotation.Read;

@Endpoint(id = "date",
          prefix = "custom",
          defaultEnabled = true,
          defaultSensitive = false)
public class CurrentDateEndpoint {

private Date currentDate;

@Read
public Date currentDate() {
    return currentDate;
}

}
```

CurrentDateEndpoint

```kotlin
import io.micronaut.management.endpoint.annotation.Endpoint

import io.micronaut.management.endpoint.annotation.Read

@Endpoint(id = "date", prefix = "custom", defaultEnabled = true, defaultSensitive = false)
class CurrentDateEndpoint {

private var currentDate: Date? = null

@Read
fun currentDate(): Date? {
    return currentDate
}

}
```

CurrentDateEndpoint

```groovy
import io.micronaut.management.endpoint.annotation.Endpoint

import io.micronaut.management.endpoint.annotation.Read

@Endpoint(id = "date",
          prefix = "custom",
          defaultEnabled = true,
          defaultSensitive = false)
class CurrentDateEndpoint {

private Date currentDate

@Read
Date currentDate() {
    currentDate
}

}
```

The above method responds to the following request:

```bash
$ curl -X GET localhost:55838/date

1526085903689
```

The Read annotation accepts an optional `produces` argument, which sets the media type returned from the method (default is `application/json`):

CurrentDateEndpoint

```java
import io.micronaut.management.endpoint.annotation.Endpoint;

import io.micronaut.management.endpoint.annotation.Read;

import io.micronaut.http.MediaType;
import io.micronaut.management.endpoint.annotation.Selector;

@Endpoint(id = "date",
          prefix = "custom",
          defaultEnabled = true,
          defaultSensitive = false)
public class CurrentDateEndpoint {

private Date currentDate;

@Read(produces = MediaType.TEXT_PLAIN) //(1)
public String currentDatePrefix(@Selector String prefix) {
    return prefix + ": " + currentDate;
}

}
```

CurrentDateEndpoint

```kotlin
import io.micronaut.management.endpoint.annotation.Endpoint

import io.micronaut.management.endpoint.annotation.Read

import io.micronaut.http.MediaType
import io.micronaut.management.endpoint.annotation.Selector

@Endpoint(id = "date", prefix = "custom", defaultEnabled = true, defaultSensitive = false)
class CurrentDateEndpoint {

private var currentDate: Date? = null

@Read(produces = [MediaType.TEXT_PLAIN]) //(1)
fun currentDatePrefix(@Selector prefix: String): String {
    return "$prefix: $currentDate"
}

}
```

CurrentDateEndpoint

```groovy
import io.micronaut.management.endpoint.annotation.Endpoint

import io.micronaut.management.endpoint.annotation.Read

import io.micronaut.http.MediaType
import io.micronaut.management.endpoint.annotation.Selector

@Endpoint(id = "date",
          prefix = "custom",
          defaultEnabled = true,
          defaultSensitive = false)
class CurrentDateEndpoint {

private Date currentDate

@Read(produces = MediaType.TEXT_PLAIN) //(1)
String currentDatePrefix(@Selector String prefix) {
    "$prefix: $currentDate"
}

}
```

| **1** | Supported media types are represented by MediaType |
|---|---|

The above method responds to the following request:

```bash
$ curl -X GET localhost:8080/date/the_date_is

the_date_is: Fri May 11 19:24:21 CDT
```


## Write Methods

Annotating a method with the Write annotation causes it to respond to `POST` requests.

CurrentDateEndpoint

```java
import io.micronaut.management.endpoint.annotation.Endpoint;

import io.micronaut.management.endpoint.annotation.Write;

import io.micronaut.http.MediaType;
import io.micronaut.management.endpoint.annotation.Selector;

@Endpoint(id = "date",
          prefix = "custom",
          defaultEnabled = true,
          defaultSensitive = false)
public class CurrentDateEndpoint {

private Date currentDate;

@Write
public String reset() {
    currentDate = new Date();

    return "Current date reset";
}

}
```

CurrentDateEndpoint

```kotlin
import io.micronaut.management.endpoint.annotation.Endpoint

import io.micronaut.management.endpoint.annotation.Write

import io.micronaut.http.MediaType
import io.micronaut.management.endpoint.annotation.Selector

@Endpoint(id = "date", prefix = "custom", defaultEnabled = true, defaultSensitive = false)
class CurrentDateEndpoint {

private var currentDate: Date? = null

@Write
fun reset(): String {
    currentDate = Date()

    return "Current date reset"
}

}
```

CurrentDateEndpoint

```groovy
import io.micronaut.management.endpoint.annotation.Endpoint

import io.micronaut.management.endpoint.annotation.Write

import io.micronaut.http.MediaType
import io.micronaut.management.endpoint.annotation.Selector

@Endpoint(id = "date",
          prefix = "custom",
          defaultEnabled = true,
          defaultSensitive = false)
class CurrentDateEndpoint {

private Date currentDate

@Write
String reset() {
    currentDate = new Date()

    return "Current date reset"
}

}
```

The above method responds to the following request:

```bash
$ curl -X POST http://localhost:39357/date

Current date reset
```

The Write annotation accepts an optional `consumes` argument, which sets the media type accepted by the method (default is `application/json`):

MessageEndpoint

```java
import io.micronaut.context.annotation.Requires;
import io.micronaut.management.endpoint.annotation.Endpoint;

import io.micronaut.management.endpoint.annotation.Write;

import io.micronaut.http.MediaType;

@Endpoint(id = "message", defaultSensitive = false)
public class MessageEndpoint {

String message;

@Write(consumes = MediaType.APPLICATION_FORM_URLENCODED, produces = MediaType.TEXT_PLAIN)
public String updateMessage(String newMessage) {
    this.message = newMessage;

    return "Message updated";
}

}
```

MessageEndpoint

```kotlin
import io.micronaut.context.annotation.Requires
import io.micronaut.management.endpoint.annotation.Endpoint

import io.micronaut.management.endpoint.annotation.Write

import io.micronaut.http.MediaType

@Endpoint(id = "message", defaultSensitive = false)
class MessageEndpoint {

internal var message: String? = null

@Write(consumes = [MediaType.APPLICATION_FORM_URLENCODED], produces = [MediaType.TEXT_PLAIN])
fun updateMessage(newMessage: String): String {  //(1)
    this.message = newMessage

    return "Message updated"
}

}
```

MessageEndpoint

```groovy
import io.micronaut.management.endpoint.annotation.Endpoint

import io.micronaut.management.endpoint.annotation.Write

import io.micronaut.http.MediaType

@Endpoint(id = "message", defaultSensitive = false)
class MessageEndpoint {

String message

@Write(consumes = MediaType.APPLICATION_FORM_URLENCODED, produces = MediaType.TEXT_PLAIN)
String updateMessage(String newMessage) {  //(1)
    message = newMessage

    return "Message updated"
}

}
```

The above method responds to the following request:

```bash
$ curl -X POST http://localhost:65013/message -H 'Content-Type: application/x-www-form-urlencoded' -d $'newMessage=A new message'

Message updated
```


## Delete Methods

Annotating a method with the Delete annotation causes it to respond to `DELETE` requests.

MessageEndpoint

```java
import io.micronaut.context.annotation.Requires;
import io.micronaut.management.endpoint.annotation.Endpoint;

import io.micronaut.management.endpoint.annotation.Delete;

@Endpoint(id = "message", defaultSensitive = false)
public class MessageEndpoint {

String message;

@Delete
public String deleteMessage() {
    this.message = null;

    return "Message deleted";
}

}
```

MessageEndpoint

```kotlin
import io.micronaut.context.annotation.Requires
import io.micronaut.management.endpoint.annotation.Endpoint

import io.micronaut.management.endpoint.annotation.Delete

@Endpoint(id = "message", defaultSensitive = false)
class MessageEndpoint {

internal var message: String? = null

@Delete
fun deleteMessage(): String {
    this.message = null

    return "Message deleted"
}

}
```

MessageEndpoint

```groovy
import io.micronaut.management.endpoint.annotation.Endpoint

import io.micronaut.management.endpoint.annotation.Delete

@Endpoint(id = "message", defaultSensitive = false)
class MessageEndpoint {

String message

@Delete
String deleteMessage() {
    message = null

    return "Message deleted"
}

}
```

The above method responds to the following request:

```bash
$ curl -X DELETE http://localhost:65013/message

Message deleted
```


## 17.1.3 Endpoint Sensitivity

Endpoint sensitivity can be controlled for the entire endpoint through the endpoint annotation and configuration. Individual methods can be configured independently of the endpoint as a whole, however. The @Sensitive annotation can be applied to methods to control their sensitivity.

AlertsEndpoint

```java
@Endpoint(id = "alerts", defaultSensitive = false) // (1)
public class AlertsEndpoint {

    private final List<String> alerts = new CopyOnWriteArrayList<>();

    @Read
    List<String> getAlerts() {
        return alerts;
    }

    @Delete
    @Sensitive(true)  // (2)
    void clearAlerts() {
        alerts.clear();
    }

    @Write(consumes = MediaType.TEXT_PLAIN)
    @Sensitive(property = "add.sensitive", defaultValue = true) // (3)
    void addAlert(@Body String alert) {
        alerts.add(alert);
    }
}
```

AlertsEndpoint

```kotlin
import io.micronaut.context.annotation.Requires
import io.micronaut.http.MediaType
import io.micronaut.http.annotation.Body
import io.micronaut.management.endpoint.annotation.Delete
import io.micronaut.management.endpoint.annotation.Endpoint
import io.micronaut.management.endpoint.annotation.Read
import io.micronaut.management.endpoint.annotation.Sensitive
import io.micronaut.management.endpoint.annotation.Write
import java.util.concurrent.CopyOnWriteArrayList

@Endpoint(id = "alerts", defaultSensitive = false) // (1)
class AlertsEndpoint {

    private val alerts: MutableList<String> = CopyOnWriteArrayList()

    @Read
    fun getAlerts(): List<String> {
        return alerts
    }

    @Delete
    @Sensitive(true)  // (2)
    fun clearAlerts() {
        alerts.clear()
    }

    @Write(consumes = [MediaType.TEXT_PLAIN])
    @Sensitive(property = "add.sensitive", defaultValue = true)  // (3)
    fun addAlert(@Body alert: String) {
        alerts.add(alert)
    }
}
```

AlertsEndpoint

```groovy
import io.micronaut.http.annotation.Body
import io.micronaut.management.endpoint.annotation.Delete
import io.micronaut.management.endpoint.annotation.Endpoint
import io.micronaut.management.endpoint.annotation.Read
import io.micronaut.management.endpoint.annotation.Sensitive
import io.micronaut.management.endpoint.annotation.Write

import java.util.concurrent.CopyOnWriteArrayList

@Endpoint(id = "alerts", defaultSensitive = false) // (1)
class AlertsEndpoint {

    private final List<String> alerts = new CopyOnWriteArrayList<>();

    @Read
    List<String> getAlerts() {
        alerts
    }

    @Delete
    @Sensitive(true) // (2)
    void clearAlerts() {
        alerts.clear()
    }

    @Write(consumes = MediaType.TEXT_PLAIN)
    @Sensitive(property = "add.sensitive", defaultValue = true) // (3)
    void addAlert(@Body String alert) {
        alerts << alert
    }
}
```

| **1** | The endpoint is not sensitive by default, and the default prefix of `endpoints` is used. |
|---|---|
| **2** | This method is always sensitive, regardless of any other factors |
| **3** | The `property` value is appended to the prefix and id to look up a configuration value |

If the configuration key `endpoints.alerts.add.sensitive` is set, that value determines the sensitivity of the `addAlert` method.

1. `endpoint` is the first token because that is the default value for `prefix` in the endpoint annotation and is not set explicitly in this example.
2. `alerts` is the next token because that is the endpoint id
3. `add.sensitive` is the next token because that is the value set to the `property` member of the @Sensitive annotation.

If the configuration key is not set, the `defaultValue` is used (defaults to `true`).


## 17.1.4 Endpoint Configuration

Endpoints with the `endpoints` prefix can be configured through their default endpoint id. If an endpoint exists with the id of `foo`, it can be configured through `endpoints.foo`. In addition, default values can be provided through the `all` prefix.

For example, consider the following endpoint.

FooEndpoint.java

```java
@Endpoint("foo")
class FooEndpoint {
    ...
}
```

By default, the endpoint is enabled. To disable it, set `endpoints.foo.enabled` to false. If `endpoints.foo.enabled` is not set and `endpoints.all.enabled` is `false`, the endpoint will be disabled.

The configuration values for the endpoint override those for `all`. If `endpoints.foo.enabled` is `true` and `endpoints.all.enabled` is `false`, the endpoint will be enabled.

For all endpoints, the following configuration values can be set.

```properties
endpoints.<any endpoint id>.enabled=Boolean
endpoints.<any endpoint id>.sensitive=Boolean
```

```yaml
endpoints:
  <any endpoint id>:
    enabled: Boolean
    sensitive: Boolean
```

```toml
[endpoints]
  sensitive="Boolean"
```

```groovy
endpoints {
  <any endpoint id> {
    enabled = "Boolean"
    sensitive = "Boolean"
  }
}
```

```hocon
{
  endpoints {
    <any endpoint id> {
      enabled = "Boolean"
      sensitive = "Boolean"
    }
  }
}
```

```json
{
  "endpoints": {
    "<any endpoint id>": {
      "enabled": "Boolean",
      "sensitive": "Boolean"
    }
  }
}
```

|   | The base path for all endpoints is `/` by default. If you prefer the endpoints to be available under a different base path, configure `endpoints.all.path`. For example, if the value is set to `/endpoints/`, the foo endpoint will be accessible at `/endpoints/foo`, relative to the context path. Note that the leading and trailing `/` are required for `endpoints.all.path` unless `micronaut.server.context-path` is set, in which case the leading `/` isn’t necessary. |
|---|---|


## 17.2 Built-In Endpoints

When the `management` dependency is added to your project, the following built-in endpoints are enabled by default:

| Endpoint | URI | Description |
|---|---|---|
| BeansEndpoint | `/beans` | Returns information about the loaded bean definitions in the application (see BeansEndpoint) |
| HealthEndpoint | `/health` | Returns information about the "health" of the application (see HealthEndpoint) |
| InfoEndpoint | `/info` | Returns static information from the state of the application (see InfoEndpoint) |
| LoggersEndpoint | `/loggers` | Returns information about available loggers and permits changing the configured log level (see LoggersEndpoint) |
| MetricsEndpoint | `/metrics` | Return the application metrics. Requires the `micrometer-core` configuration on the classpath. |
| RefreshEndpoint | `/refresh` | Refreshes the application state (see RefreshEndpoint) |
| RoutesEndpoint | `/routes` | Returns information about URIs available to be called for your application (see RoutesEndpoint) |
| ThreadDumpEndpoint | `/threaddump` | Returns information about the current threads in the application. |

In addition, the following built-in endpoint(s) are provided by the `management` dependency but are not enabled by default:

| Endpoint | URI | Description |
|---|---|---|
| EnvironmentEndpoint | `/env` | Returns information about the environment and its property sources (see EnvironmentEndpoint) |
| CachesEndpoint | `/caches` | Returns information about the caches and permits invalidating them (see CachesEndpoint) |
| ServerStopEndpoint | `/stop` | Shuts down the application server (see ServerStopEndpoint) |

|   | It is possible to open all endpoints for unauthenticated access defining `endpoints.all.sensitive: false` but this should be used with care because private and sensitive information will be exposed. |
|---|---|

### Management Port

By default, all management endpoints are exposed over the same port as the application. You can alter this behaviour by specifying the `endpoints.all.port` setting:

```properties
endpoints.all.port=8085
```

```yaml
endpoints:
  all:
    port: 8085
```

```toml
[endpoints]
  [endpoints.all]
    port=8085
```

```groovy
endpoints {
  all {
    port = 8085
  }
}
```

```hocon
{
  endpoints {
    all {
      port = 8085
    }
  }
}
```

```json
{
  "endpoints": {
    "all": {
      "port": 8085
    }
  }
}
```

In the above example the management endpoints are exposed only over port 8085.

### JMX

The Micronaut framework provides functionality to register endpoints with JMX. See the section on JMX to get started.


## 17.2.1 The Beans Endpoint

The beans endpoint returns information about the loaded bean definitions in the application. The bean data returned by default is an object where the key is the bean definition class name and the value is an object of properties about the bean.

To execute the beans endpoint, send a GET request to /beans.


## Configuration

To configure the beans endpoint, supply configuration through `endpoints.beans`.

Beans Endpoint Configuration Example

```properties
endpoints.beans.enabled=Boolean
endpoints.beans.sensitive=Boolean
```

```yaml
endpoints:
  beans:
    enabled: Boolean
    sensitive: Boolean
```

```toml
[endpoints]
  [endpoints.beans]
    enabled="Boolean"
    sensitive="Boolean"
```

```groovy
endpoints {
  beans {
    enabled = "Boolean"
    sensitive = "Boolean"
  }
}
```

```hocon
{
  endpoints {
    beans {
      enabled = "Boolean"
      sensitive = "Boolean"
    }
  }
}
```

```json
{
  "endpoints": {
    "beans": {
      "enabled": "Boolean",
      "sensitive": "Boolean"
    }
  }
}
```


## Customization

The beans endpoint is composed of a bean definition data collector and a bean data implementation. The bean definition data collector (BeanDefinitionDataCollector) is responsible for returning a publisher that returns the data used in the response. The bean definition data (BeanDefinitionData) is responsible for returning data about an individual bean definition.

To override the default behavior for either of the helper classes, either extend the default implementations (DefaultBeanDefinitionDataCollector, DefaultBeanDefinitionData), or implement the relevant interface directly. To ensure your implementation is used instead of the default, add the @Replaces annotation to your class with the value being the default implementation.


## 17.2.2 The Info Endpoint

The info endpoint returns static information from the state of the application. The info exposed can be provided by any number of "info sources".

To execute the info endpoint, send a GET request to /info.


## Configuration

To configure the info endpoint, supply configuration through `endpoints.info`.

Info Endpoint Configuration Example

```properties
endpoints.info.enabled=Boolean
endpoints.info.sensitive=Boolean
```

```yaml
endpoints:
  info:
    enabled: Boolean
    sensitive: Boolean
```

```toml
[endpoints]
  [endpoints.info]
    enabled="Boolean"
    sensitive="Boolean"
```

```groovy
endpoints {
  info {
    enabled = "Boolean"
    sensitive = "Boolean"
  }
}
```

```hocon
{
  endpoints {
    info {
      enabled = "Boolean"
      sensitive = "Boolean"
    }
  }
}
```

```json
{
  "endpoints": {
    "info": {
      "enabled": "Boolean",
      "sensitive": "Boolean"
    }
  }
}
```


## Customization

The info endpoint consists of an info aggregator and any number of info sources. To add an info source, create a bean class that implements InfoSource. If your info source needs to retrieve data from Java properties files, extend the PropertiesInfoSource interface which provides a helper method for this purpose.

All info source beans are collected together with the info aggregator. To provide your own implementation of the info aggregator, create a class that implements InfoAggregator and register it as a bean. To ensure your implementation is used instead of the default, add the @Replaces annotation to your class with the value being the default implementation.

The default info aggregator returns a map containing the combined properties returned by all the info sources. This map is returned as JSON from the /info endpoint.


## Provided Info Sources

### Configuration Info Source

The ConfigurationInfoSource returns configuration properties under the `info` key. In addition to string, integer and boolean values, more complex properties can be exposed as maps in the JSON output (if the configuration format supports it).

Info Source Example (

application.groovy

)

```groovy
info.demo.string = "demo string"
info.demo.number = 123
info.demo.map = [key: 'value', other_key: 123]
```

The above config results in the following JSON response from the info endpoint:

```json
{
  "demo": {
    "string": "demo string",
    "number": 123,
    "map": {
      "key": "value",
      "other_key": 123
    }
  }
}
```

#### Configuration

The configuration info source can be disabled using the `endpoints.info.config.enabled` property.

### Git Info Source

If a `git.properties` file is available on the classpath, the GitInfoSource exposes the values in that file under the `git` key. Generating of a `git.properties` file must be configured as part of your build. One easy option for Gradle users is the Gradle Git Properties Plugin. Maven users can use the Maven Git Commit ID Plugin.

#### Configuration

To specify an alternate path or name of the properties file, supply a custom value in the `endpoints.info.git.location` property.

The git info source can be disabled using the `endpoints.info.git.enabled` property.

### Build Info Source

If a `META-INF/build-info.properties` file is available on the classpath, the BuildInfoSource exposes the values in that file under the `build` key. Generating a `build-info.properties` file must be configured as part of your build. One easy option for Gradle users is the Gradle Build Info Plugin. An option for Maven users is the Spring Boot Maven Plugin

#### Configuration

To specify an alternate path/name of the properties file, supply a custom value in the `endpoints.info.build.location` property.

The build info source can be disabled using the `endpoints.info.build.enabled` property.


## 17.2.3 The Health Endpoint

The health endpoint returns information about the "health" of the application, which is determined by any number of "health indicators".

Send a GET request to `/health` to execute the health endpoint. Additionally, the health endpoint exposes `/health/liveness` and `/health/readiness` health indicators.

A positive liveness check (`/health/liveness`) means the application is running and not stuck. If it fails, the application might need to be restarted.

A positive readiness check (`/health/readiness`) means the application is fully initialized and ready to handle requests.

|   | See the guide for Exposing a Health Endpoint for your Micronaut Application to learn more. |
|---|---|


## 17.2.3.1 Health Endpoint Configuration

To configure the health endpoint, supply configuration through `endpoints.health`.

Health Endpoint Configuration Example

```properties
endpoints.health.enabled=Boolean
endpoints.health.sensitive=Boolean
endpoints.health.details-visible=String
endpoints.health.status.http-mapping=Map<String, HttpStatus>
```

```yaml
endpoints:
  health:
    enabled: Boolean
    sensitive: Boolean
    details-visible: String
    status:
      http-mapping: Map<String, HttpStatus>
```

```toml
[endpoints]
  [endpoints.health]
    enabled="Boolean"
    sensitive="Boolean"
    details-visible="String"
    [endpoints.health.status]
      http-mapping="Map<String, HttpStatus>"
```

```groovy
endpoints {
  health {
    enabled = "Boolean"
    sensitive = "Boolean"
    detailsVisible = "String"
    status {
      httpMapping = "Map<String, HttpStatus>"
    }
  }
}
```

```hocon
{
  endpoints {
    health {
      enabled = "Boolean"
      sensitive = "Boolean"
      details-visible = "String"
      status {
        http-mapping = "Map<String, HttpStatus>"
      }
    }
  }
}
```

```json
{
  "endpoints": {
    "health": {
      "enabled": "Boolean",
      "sensitive": "Boolean",
      "details-visible": "String",
      "status": {
        "http-mapping": "Map<String, HttpStatus>"
      }
    }
  }
}
```

- `details-visible` is one of DetailsVisibility

The `details-visible` setting controls whether health detail will be exposed to users who are not authenticated. If the details-visible parameter is configured as ANONYMOUS, while the sensitive flag is set to true, the resulting outcome will be 401 Unauthorized.

For example, setting:

Using

details-visible

```properties
endpoints.health.details-visible=ANONYMOUS
```

```yaml
endpoints:
  health:
    details-visible: ANONYMOUS
```

```toml
[endpoints]
  [endpoints.health]
    details-visible="ANONYMOUS"
```

```groovy
endpoints {
  health {
    detailsVisible = "ANONYMOUS"
  }
}
```

```hocon
{
  endpoints {
    health {
      details-visible = "ANONYMOUS"
    }
  }
}
```

```json
{
  "endpoints": {
    "health": {
      "details-visible": "ANONYMOUS"
    }
  }
}
```

exposes detailed information from the various health indicators about the health status of the application to anonymous unauthenticated users.


## 17.2.3.2 Health Status Codes

The `endpoints.health.status.http-mapping` setting controls which status codes to return for each health status. The defaults are described in the table below:

| Status | HTTP Code |
|---|---|
| UP | OK (200) |
| UNKNOWN | OK (200) |
| DOWN | SERVICE_UNAVAILABLE (503) |

You can provide custom mappings in your configuration file (e.g `application.yml`):

Custom Health Status Codes

```properties
endpoints.health.status.http-mapping.DOWN=200
```

```yaml
endpoints:
  health:
    status:
      http-mapping:
        DOWN: 200
```

```toml
[endpoints]
  [endpoints.health]
    [endpoints.health.status]
      [endpoints.health.status.http-mapping]
        DOWN=200
```

```groovy
endpoints {
  health {
    status {
      httpMapping {
        DOWN = 200
      }
    }
  }
}
```

```hocon
{
  endpoints {
    health {
      status {
        http-mapping {
          DOWN = 200
        }
      }
    }
  }
}
```

```json
{
  "endpoints": {
    "health": {
      "status": {
        "http-mapping": {
          "DOWN": 200
        }
      }
    }
  }
}
```

The above returns OK (200) even when the HealthStatus is DOWN.


## 17.2.3.3 Health Logging

The DefaultHealthAggregator also emits log statements for health indicator status and details. To log this information use `Level.DEBUG` for just health indicator status or use Level.TRACE for both status and details. For example:

```xml
<logger name="io.micronaut.management.health.aggregator.DefaultHealthAggregator" level="trace" /> (1)
```

| **1** | Use `level="debug"` for health indicator status, use `level="trace"` to add health indicator details |
|---|---|


## 17.2.3.4 Custom Health Indicator

The health endpoint consists of a health aggregator and any number of health indicators. To add a health indicator, create a bean class that implements HealthIndicator. It is recommended to also use either @Liveness or @Readiness qualifier. If no qualifier is used, the health indicator will be part of /health and /health/readiness endpoints. A base class AbstractHealthIndicator is available to subclass to make the process easier.

All health indicator beans are collected together with the health aggregator. To provide your own implementation of the health aggregator, create a class that implements HealthAggregator and register it as a bean. To ensure your implementation is used instead of the default, add the @Replaces annotation to your class with the value being the default implementation DefaultHealthAggregator.

The default health aggregator returns an overall status calculated based on the health statuses of the indicators. A health status consists of several pieces of information.

| Name | The name of the status |
|---|---|
| Description | The description of the status |
| Operational | Whether the functionality the indicator represents is functional |
| Severity | How severe the status is. A higher number is more severe |

The "worst" status is returned as the overall status. A non-operational status is selected over an operational status. A higher severity is selected over a lower severity.
