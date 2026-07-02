---
title: "Micronaut Core (part 1/27)"
source: https://docs.micronaut.io/latest/guide/index.html
domain: micronaut
license: CC-BY-SA-4.0
tags: micronaut framework, micronaut jvm, compile-time injection, microservices framework
fetched: 2026-07-02
part: 1/27
---

# Micronaut Core

- API Reference
- API
- Configuration Reference
- Conf

# Micronaut Core

Core components supporting the Micronaut Framework

**Version:** 5.1.3

# 1 Introduction

The Micronaut Framework is a modern, JVM-based, full stack Java framework designed for building modular, easily testable JVM applications with support for Java, Kotlin, and Groovy.

The Micronaut framework was originally created by a team who had also worked on the Grails framework. The Micronaut framework takes inspiration from lessons learned over the years building real-world applications from monoliths to microservices using Spring, Spring Boot and the Grails framework. The core team continues to develop and maintain the Micronaut project through the support of the Micronaut Foundation.

The Micronaut framework aims to provide all the tools necessary to build JVM applications including:

- Dependency Injection and Inversion of Control (IoC)
- Aspect Oriented Programming (AOP)
- Sensible Defaults and Auto-Configuration

With the Micronaut framework you can build Message-Driven Applications, Command Line Applications, HTTP Servers and more whilst for Microservices in particular Micronaut also provides:

- Distributed Configuration
- Service Discovery
- HTTP Routing
- Client-Side Load Balancing

At the same time, the Micronaut framework aims to avoid the downsides of frameworks like Spring, Spring Boot and Grails by providing:

- Fast startup time
- Reduced memory footprint
- Minimal use of reflection
- Minimal use of proxies
- No runtime bytecode generation
- Easy Unit Testing

Historically, frameworks such as Spring and Grails were not designed to run in scenarios such as serverless functions, Android apps, or low memory footprint microservices. In contrast, the Micronaut framework is designed to be suitable for all of these scenarios.

This goal is achieved through the use of Java’s annotation processors, which are usable on any JVM language that supports them, as well as an HTTP Server (with several runtimes Netty, Jetty, Tomcat, Undertow…) and an HTTP Client (with several runtimes Netty, Java HTTP Client, …). To provide a similar programming model to Spring and Grails, these annotation processors precompile the necessary metadata to perform DI, define AOP proxies and configure your application to run in a low-memory environment.

Many APIs in the Micronaut framework are heavily inspired by Spring and Grails. This is by design, and helps bring developers up to speed quickly.


## 1.1 What's New in Micronaut Framework 5.0.x

Micronaut Framework 5.0.x continues the work started in the first 5.0 milestones and adds a number of improvements across the core container, HTTP stack, configuration system, and developer-facing APIs.

This page is a curated overview of the most important additions on the `5.0.x` line. For upgrade guidance, see Upgrading your Micronaut Application, and for incompatible changes, review Breaking Changes.

### Core Themes in Micronaut Framework 5.0.x

Micronaut Framework 5 modernizes the core platform with newer JVM and language support, including a new JDK 25 baseline, an Apache Groovy 5 baseline, a Kotlin 2.3 baseline, broader support for current JDK capabilities, and deeper investment in compile-time metadata. See also Breaking Changes for version-specific migration notes.

The framework APIs now embrace nullability annotations and specifically JSpecify nullability annotations, with `@NullMarked` adoption across the codebase and stronger static analysis integration. The result is clearer API contracts, improved Kotlin interoperability, and better IDE feedback.

The IoC container and compile-time infrastructure also received substantial work in the 5.0 branch. Bean resolution, qualifier handling, replacement metadata, eager initialization, and runtime annotation processing were refined to reduce runtime work and improve predictability.

### Container, AOP, and Runtime Improvements

The bean context was reworked in several areas during the 5.0 development cycle, including precomputed bean indexes, compile-time `@Replaces` handling, and broader bean context optimizations. Together, these changes continue Micronaut’s focus on startup performance and low runtime overhead.

Micronaut 5 also added support for creating AOP proxies at runtime when build-time proxy generation is not the right fit. This enables integrations such as Byte Buddy-based proxies, JDK dynamic proxies for interfaces, and test-oriented proxy scenarios such as mocks and spies. For background on Micronaut’s AOP model, see Aspect Oriented Programming.

Recent 5.0.x work also improved interoperability with Jakarta APIs by adding support for `jakarta.annotation.Priority`, mapping it to Micronaut ordering semantics for beans and HTTP filters. Related ordering documentation can be found in Injectable Container Types and Filter Order.

On the HTTP side, HTTP/3 support on the Netty stack was promoted to stable. See HTTP/3 Support and HTTP/3 in Clients. The 5.0 line also includes a multipart/form handling refactor that introduces a lower-level, more server-independent form API and improves resource management in higher-level binders. See Forms, Detailed Form API, and File Uploads.

Configuration support expanded significantly in 5.0.x. Micronaut now supports config imports and a `PropertySourceImporter` SPI, enabling configuration loading from sources such as files, classpath locations, environment variables, config trees, and custom importer implementations. See Importing Additional Configuration, Implementing a Custom PropertySourceImporter, and Externalized Configuration with PropertySources.

Configuration metadata also became more useful for tooling. Micronaut 5 can generate JSON Schema documents from `@ConfigurationProperties`, making it easier to drive IDE completion, validation, and external tooling from the same configuration model used by the framework. For the underlying configuration model, see Configuration Properties.

The JSON and serialization stack was updated as well, with work across `JsonMapper`, the update to Jackson 3, and additional configuration coverage so applications can adopt the newer JSON infrastructure more smoothly.

### Resilience and Context Propagation

Micronaut Retry gained programmatic retry and circuit breaker APIs in addition to the existing annotation-driven model documented in Retry Advice. This makes it possible to define typed retry and circuit breaker policies in code and reuse them for synchronous, reactive, and asynchronous flows.

The 5.0.x line also expanded context propagation capabilities, including support for scoped values and continued alignment with modern JDK context propagation patterns. See Context Propagation.

### Summary

For teams adopting Micronaut Framework 5.0.x, the biggest benefits are stronger null-safety, more flexible AOP and retry models, better HTTP and multipart capabilities, richer configuration tooling, and continued improvements to the container’s compile-time-first runtime model.


## 1.2 Upgrading your Micronaut Application

### Upgrading between Micronaut Framework versions

Check Micronaut Upgrade documentation to help you upgrade your Micronaut applications.

To learn what’s new, check the GitHub Release notes for each module you’re interested in. They contain a summary of all changes broken down by type.

### Breaking Changes

Review the section on Breaking Changes and update your affected application code.

# 2 Quick Start

The following sections walk you through a Quick Start on how to use the Micronaut framework to set up a basic "Hello World" application.

Before getting started ensure you have a Java 8 or higher JDK installed, and it is recommended that you use a suitable IDE such as IntelliJ IDEA.


## 2.1 Install the CLI

The Micronaut CLI is an optional but convenient way to create Micronaut applications. The best way to install Micronaut CLI on Unix systems is with SDKMAN which greatly simplifies installing and managing multiple Micronaut versions.

To see all available installation methods, check the Micronaut Starter documentation.


## 2.2 Creating a Server Application

Using the Micronaut CLI you can create a new Micronaut application in either Groovy, Java, or Kotlin (the default is Java).

The following command creates a new "Hello World" server application in Java with a Gradle build:

|   | Applications generated via our CLI include Gradle or Maven wrappers, so it is not even necessary to have Gradle or Maven installed on your machine to begin running the applications. Simply use the `mvnw` or `gradlew` command, as explained further below. |
|---|---|

```bash
$ mn create-app hello-world
```

|   | Supply `--build maven` to create a Maven-based build instead |
|---|---|

If you don’t have the CLI installed then you can also create the same application by visiting Micronaut Launch and clicking the "Generate Project" button or by using the following `curl` command on Unix systems:

```bash
curl https://launch.micronaut.io/hello-world.zip -o hello-world.zip
unzip hello-world.zip
cd hello-world
```

|   | Add `?build=maven` to the URL passed to `curl` to generate a Maven project. |
|---|---|

The previous steps created a new Java application in a directory called `hello-world` featuring a Gradle build. You can run the application with `./gradlew run`:

```bash
$ ./gradlew run
> Task :run
[main] INFO  io.micronaut.runtime.Micronaut - Startup completed in 540ms. Server Running: http://localhost:28933
```

If you have created a Maven-based project, use `./mvnw mn:run` instead.

|   | For Windows the ./ before commands is not needed |
|---|---|

By default, the Micronaut HTTP server is configured to run on port 8080. See the section Running Server on a Specific Port for more options.

To create a service that responds to "Hello World" you first need a controller. The following is an example:

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

| **1** | The @Controller annotation defines the class as a controller mapped to the path `/hello` |
|---|---|
| **2** | The @Get annotation maps the `index` method to all requests that use an HTTP `GET` |
| **3** | A String "Hello World" is returned as the response |

If you use Java, place the previous file in `src/main/java/hello/world`. If you use Groovy, place the previous file in `src/main/groovy/hello/world`. If you use Kotlin, place the previous file in `src/main/kotlin/hello/world`.

If you start the application and send a `GET` request to the `/hello` URI, the text "Hello World" is returned:

```bash
$ curl http://localhost:8080/hello
Hello World
```

|   | See the guide for Creating your First Micronaut Application to learn more. |
|---|---|


## 2.3 Setting up an IDE

The application created in the previous section contains a main class located in `src/main/java` that looks like the following:

```java
import io.micronaut.runtime.Micronaut;

public class Application {

    public static void main(String[] args) {
        Micronaut.run(Application.class);
    }
}
```

```kotlin
import io.micronaut.runtime.Micronaut

object Application {

    @JvmStatic
    fun main(args: Array<String>) {
        Micronaut.run(Application.javaClass)
    }
}
```

```groovy
import io.micronaut.runtime.Micronaut

class Application {

    static void main(String... args) {
        Micronaut.run Application
    }
}
```

This is the class that is run when starting the application via Gradle/Maven or via deployment. You can also run the main class directly within your IDE.


## 2.3.1 IntelliJ IDEA

To import a Micronaut project into IntelliJ IDEA, open the `build.gradle` or `pom.xml` file and follow the instructions to import the project.

For IntelliJ IDEA, if you plan to use the IntelliJ compiler, enable annotation processing under "Build, Execution, Deployment → Compiler → Annotation Processors" by ticking the "Enable annotation processing" checkbox:

Once you have enabled annotation processing in IntelliJ you can run the application and tests directly within the IDE without the need of an external build tool such as Gradle or Maven.

|   | See the guide for Using IntelliJ IDEA to Develop Micronaut Applications to learn more. |
|---|---|


## 2.3.2 Visual Studio Code

The Micronaut framework can easily be set up within Visual Studio Code by installing the following two extensions:

- The Microsoft Extension Pack for Java
- Tools for Micronaut® framework

These extensions can be installed by clicking on the **Install** button in the banner of the pages linked above, or, by searching for the extensions within VS Code.

Once they are installed they will give you access to a host of Micronaut specific features such as:

- An application creation wizard
- Viewing beans and REST endpoints
- Composing REST queries and running them
- Support for the Micronaut Expression Language
- A Micronaut Tools Activity view for running and monitoring your applications
- Support for using the Micronaut Control Panel
- Debugging your application
- Support for packaging your application as a container
- Support for connecting to and working with an Oracle Database
- Advanced support for deploying your applications to Oracle Cloud Infrastructure
- Advanced support for creating Micronaut Data entities, repositories and controllers from existing database schemas
- Test creation for Micronaut Data controllers endpoints

Once the extensions are installed just type `code .` in any Micronaut project directory and the project will be opened within VS Code.

|   | For macOS, you need to install the `code` command by following these instructions. |
|---|---|


## 2.3.3 Eclipse

To use Eclipse IDE, it is recommended you import your Micronaut project into Eclipse using either Gradle BuildShip for Gradle or M2Eclipse for Maven.

|   | The Micronaut framework requires Eclipse IDE 4.9 or higher |
|---|---|

### Eclipse and Gradle

Once you have set up Eclipse 4.9 or higher with Gradle BuildShip, first run the `gradle eclipse` task from the root of your project, then import the project by selecting `File → Import` and choosing `Gradle → Existing Gradle Project` and navigating to the root directory of your project (where the `build.gradle` file is located).

### Eclipse and Maven

For Eclipse 4.9 and above with Maven you need the following Eclipse plugins:

- M2Eclipse for Maven
- Maven integration with Eclipse JDT Annotation Processor Toolkit

Once these are installed, import the project by selecting `File → Import` and choosing `Maven → Existing Maven Project` and navigating to the root directory of your project (where the `pom.xml` file is located).

Then enable annotation processing by opening `Eclipse → Preferences` and navigating to `Maven → Annotation Processing` and selecting the option `Automatically configure JDT APT`.


## 2.3.4 Apache NetBeans

Apache NetBeans can open Maven and Gradle projects out of the box.

Make sure that the **Java Web and EE** feature is enabled at `Tools → Plugins → Installed`, in order to have additional support for Micronaut, like code completion for configuration and data elements.


## 2.4 Creating a Client

As mentioned previously, the Micronaut framework includes both an HTTP server and an HTTP client. A low-level HTTP client is provided which you can use to test the `HelloController` created in the previous section.

Testing Hello World

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

Testing Hello World

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

Testing Hello World

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

| **1** | The EmbeddedServer is configured as a shared test field |
|---|---|
| **2** | A HttpClient instance shared field is also defined |
| **3** | The test uses the `toBlocking()` method to make a blocking call |
| **4** | The `retrieve` method returns the controller response as a `String` |

In addition to a low-level client, the Micronaut framework features a declarative, compile-time HTTP client, powered by the Client annotation.

To create a client, create an interface annotated with `@Client`, for example:

src/main/java/hello/world/HelloClient.java

```java
import io.micronaut.http.MediaType;
import io.micronaut.http.annotation.Get;
import io.micronaut.http.client.annotation.Client;
import org.reactivestreams.Publisher;
import io.micronaut.core.async.annotation.SingleResult;

@Client("/hello") // (1)
public interface HelloClient {

    @Get(consumes = MediaType.TEXT_PLAIN) // (2)
    @SingleResult
    Publisher<String> hello(); // (3)
}
```

src/main/java/hello/world/HelloClient.java

```kotlin
import io.micronaut.http.MediaType
import io.micronaut.http.annotation.Get
import io.micronaut.http.client.annotation.Client
import io.micronaut.core.async.annotation.SingleResult
import org.reactivestreams.Publisher

@Client("/hello") // (1)
interface HelloClient {

    @Get(consumes = [MediaType.TEXT_PLAIN]) // (2)
    @SingleResult
    fun hello(): Publisher<String>  // (3)
}
```

src/main/java/hello/world/HelloClient.java

```groovy
import io.micronaut.http.annotation.Get
import io.micronaut.http.client.annotation.Client
import org.reactivestreams.Publisher
import io.micronaut.core.async.annotation.SingleResult

@Client("/hello") // (1)
interface HelloClient {

    @Get(consumes = MediaType.TEXT_PLAIN) // (2)
    @SingleResult
    Publisher<String> hello() // (3)
}
```

| **1** | The `@Client` annotation is used with a value that is a relative path to the current server |
|---|---|
| **2** | The same @Get annotation used on the server is used to define the client mapping |
| **3** | A `Publisher` annotated with `SingleResult` is returned with the value read from the server |

To test the `HelloClient`, retrieve it from the ApplicationContext associated with the server:

Testing HelloClient

```java
import io.micronaut.test.extensions.junit5.annotation.MicronautTest;
import org.junit.jupiter.api.Test;

import jakarta.inject.Inject;
import reactor.core.publisher.Mono;

import static org.junit.jupiter.api.Assertions.assertEquals;

@MicronautTest // (1)
public class HelloClientSpec {

    @Inject
    HelloClient client; // (2)

    @Test
    public void testHelloWorldResponse() {
        assertEquals("Hello World", Mono.from(client.hello()).block());// (3)
    }
}
```

Testing HelloClient

```kotlin
import io.micronaut.context.annotation.Property
import io.micronaut.test.extensions.junit5.annotation.MicronautTest
import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.Test
import jakarta.inject.Inject
import reactor.core.publisher.Mono

@MicronautTest // (1)
class HelloClientSpec {

    @Inject
    lateinit var client: HelloClient // (2)

    @Test
    fun testHelloWorldResponse() {
        assertEquals("Hello World", Mono.from(client.hello()).block())// (3)
    }
}
```

Testing HelloClient

```groovy
import io.micronaut.test.extensions.spock.annotation.MicronautTest
import reactor.core.publisher.Mono
import spock.lang.Specification

import jakarta.inject.Inject

@MicronautTest // (1)
class HelloClientSpec extends Specification {

    @Inject HelloClient client // (2)

    void "test hello world response"() {
        expect:
        Mono.from(client.hello()).block() == "Hello World" // (3)
    }

}
```

| **1** | The `@MicronautTest` annotation defines the test |
|---|---|
| **2** | The `HelloClient` is injected from the ApplicationContext |
| **3** | The client is invoked using the Project Reactor `Mono::block` method |

The Client annotation produces an implementation automatically for you at compile time without the using proxies or runtime reflection.

The Client annotation is very flexible. See the section on the Micronaut HTTP Client for more information.


## 2.5 Deploying the Application

To deploy a Micronaut application you create an executable JAR file by running `./gradlew assemble` or `./mvnw package`.

The constructed JAR file can then be executed with `java -jar`. For example:

```bash
$ java -jar build/libs/hello-world-0.1-all.jar
```

if building with Gradle, or

```bash
$ java -jar target/hello-world.jar
```

if building with Maven.

The executable JAR can be run locally, or deployed to a virtual machine or managed Cloud service that supports executable JARs.

To publish a layered application to a Docker container registry, configure your Docker image name in `build.gradle` for Gradle:

```groovy
dockerBuild {
    images = ["[REPO_URL]/[NAMESPACE]/my-image:$project.version"]
}
```

Then use `dockerPush` to push a built image of the application:

```bash
$ ./gradlew dockerPush
```

For Maven, define the following plugin in your POM:

```xml
<plugin>
  <groupId>com.google.cloud.tools</groupId>
  <artifactId>jib-maven-plugin</artifactId>
  <configuration>
    <to>
      <image>docker.io/my-company/my-image:${project.version}</image>
    </to>
  </configuration>
</plugin>
```

Then invoke the `deploy` lifecycle phase specifying the packaging type as either `docker` or `docker-native`:

```bash
$ ./mvnw deploy -Dpackaging=docker
```

### Deployment Guides

See the following guides to learn more about deploying Micronaut Applications:

- Create an Executable Jar of a Micronaut Application
- Creating Your First Micronaut Graal Application
- Building a Docker Image of your Micronaut Application

# 3 Dependency Injection

Dependency Injection (often referred to as Inversion of Control) is a pattern that allows your code to remain independent of configuration and allows the definition of loosely coupled applications. Reducing coupling increases the ability to test your application by ensuring code is not tied directly to an external systems (like a database).

Unlike other frameworks which rely on runtime reflection and proxies, the Micronaut framework uses compile time data to implement dependency injection.

This is a similar approach taken by tools such as Google Dagger, which is designed primarily with Android in mind. Micronaut, on the other hand, is designed for building server-side microservices and provides many of the same tools and utilities as other frameworks but without using reflection or caching excessive amounts of reflection metadata.

The goals of the Micronaut IoC container are summarized as:

- Use reflection as a last resort
- Avoid runtime-generated proxies
- Optimize start-up time
- Reduce memory footprint
- Provide clear, understandable error handling

Note that the IoC part of the Micronaut framework can be used completely independently of Micronaut for whatever application type you wish to build.

To do so, configure your build to include the `micronaut-inject-java` dependency as an annotation processor.

If you are creating custom compile-time annotations or annotation mappers, see Annotation Metadata for additional requirements around `AnnotationMapper`, `NamedAnnotationMapper`, and `TypedAnnotationMapper`.

The easiest way to do this is with Micronaut’s Gradle or Maven plugins. For example with Gradle:

Configuring Gradle

```groovy
plugins {
    id 'io.micronaut.library' version '4.4.4' // get latest version from https://plugins.gradle.org/plugin/io.micronaut.library
}

version "0.1"
group "com.example"

repositories {
    mavenCentral()
}

micronaut {
    version = "5.1.3" (2)
}
```

| **1** | Define the Micronaut Library plugin |
|---|---|
| **2** | Specify the Micronaut framework version to use |

The entry point for IoC is then the ApplicationContext interface, which includes a `run` method. The following example demonstrates using it:

Running the

ApplicationContext

```java
try (ApplicationContext context = ApplicationContext.run()) { (1)
    MyBean myBean = context.getBean(MyBean.class); (2)
    // do something with your bean
}
```

| **1** | Run the ApplicationContext |
|---|---|
| **2** | Retrieve a bean from the `ApplicationContext` |

|   | The example uses Java try-with-resources syntax to ensure the ApplicationContext is cleanly shutdown when the application exits. |
|---|---|


## 3.1 Defining Beans

A bean is an object whose lifecycle is managed by the Micronaut IoC container. That lifecycle may include creation, execution, and destruction. Micronaut implements the JSR-330 (jakarta.inject) - Dependency Injection for Java specification, hence to use Micronaut you simply use the annotations provided by jakarta.inject.

The following is a simple example:

```java
public interface Engine { // (1)
    int getCylinders();
    String start();
}

@Singleton// (2)
public class V8Engine implements Engine {
    private int cylinders = 8;

    @Override
    public String start() {
        return "Starting V8";
    }

    @Override
    public int getCylinders() {
        return cylinders;
    }

    public void setCylinders(int cylinders) {
        this.cylinders = cylinders;
    }
}

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
interface Engine {
    // (1)
    val cylinders: Int

    fun start(): String
}

@Singleton// (2)
class V8Engine : Engine {

    override var cylinders = 8

    override fun start(): String {
        return "Starting V8"
    }
}

@Singleton
class Vehicle(private val engine: Engine) { // (3)
    fun start(): String {
        return engine.start()
    }
}
```

```groovy
interface Engine { // (1)
    int getCylinders()
    String start()
}

@Singleton // (2)
class V8Engine implements Engine {
    int cylinders = 8

    @Override
    String start() {
        "Starting V8"
    }
}

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

| **1** | A common `Engine` interface is defined |
|---|---|
| **2** | A `V8Engine` implementation is defined and marked with `Singleton` scope |
| **3** | The `Engine` is injected via constructor injection |

To perform dependency injection, run the BeanContext using the `run()` method and lookup a bean using `getBean(Class)`, as per the following example:

```java
final ApplicationContext context = ApplicationContext.run(Map.of("spec.name", "VehicleIntroSpec"));
Vehicle vehicle = context.getBean(Vehicle.class);
System.out.println(vehicle.start());
```

```kotlin
val context = ApplicationContext.run()
val vehicle = context.getBean(Vehicle::class.java)
println(vehicle.start())
```

```groovy
ApplicationContext context = ApplicationContext.run()
Vehicle vehicle = context.getBean(Vehicle)
println vehicle.start()
```

The Micronaut framework automatically discovers dependency injection metadata on the classpath and wires the beans together according to injection points you define.


## 3.2 How Does it Work?

At this point, you may be wondering how Micronaut framework performs the above dependency injection without requiring reflection.

The key is a set of AST transformations (for Groovy) and annotation processors (for Java) that generate classes that implement the BeanDefinition interface.

Micronaut framework uses the ASM bytecode library to generate classes, and because Micronaut knows ahead of time the injection points, there is no need to scan all methods, fields, constructors, etc. at runtime like other frameworks such as Spring do.

Also, since reflection is not used when constructing the bean, the JVM can inline and optimize the code far better, resulting in better runtime performance and reduced memory consumption. This is particularly important for non-singleton scopes where application performance depends on bean creation performance.

In addition, with Micronaut framework your application startup time and memory consumption are not affected by the size of your codebase in the same way as with a framework that uses reflection. Reflection-based IoC frameworks load and cache reflection data for every single field, method, and constructor in your code. Thus, as your code grows in size so do your memory requirements, whilst with Micronaut this is not the case.


## 3.3 Debugging Dependency Injection

To help you easily understand what Micronaut is doing at startup and when a particular bean is created Micronaut includes a dependency injection tracing feature which can be activated in a number of different ways including via the ApplicationContextBuilder API.

The simplest way to activate injection trace mode is using an environment variable. For example if you are running your application locally you can do:

Activating Injection Trace Mode

```bash
MICRONAUT_INJECT_TRACE=.+ ./gradlew run
```

Or for Maven:

Activating Injection Trace Mode

```bash
MICRONAUT_INJECT_TRACE=.+ ./mvnw mn:run
```

Trace mode will output useful information such as:

- The Configuration profile of the application
- The applicable configuration and where it came from
- The beans that are created, where they were created and how long was taken to create the bean.


## 3.4 The BeanContext

The BeanContext is a container object for all your bean definitions (it also implements BeanDefinitionRegistry).

It is also the point of initialization for Micronaut. Generally speaking however, you don’t interact directly with the `BeanContext` API and can simply use `jakarta.inject` annotations and the annotations in the io.micronaut.context.annotation package for your dependency injection needs.


## 3.5 Dependency Injection Types

The Micronaut framework supports the following types of dependency injection:

- Constructor injection (with an access level of public, protected, or default - and in case of multiple constructors, you can specify the one to be chosen, annotating it with `@Inject`)
- Field injection
- JavaBean property injection
- Method parameter injection

|   | Classes or particular fields, methods can be excluded by adding an annotation @Vetoed |
|---|---|

|   | See the guide for Micronaut Dependency Injection Types to learn more. |
|---|---|


## 3.5.1 Constructor Injection

Constructor injection is when dependencies are injected into the constructor for a type.

Constructor injection is the preferred and recommended injection type because Constructor injection:

- Allows immutable types
- Doesn’t require an additional annotation
- Is less likely to result in a `NullPointerException`
- More clearly expresses the dependencies of a particular type in one place.

The example in the next section uses constructor injection. Note that if you have multiple constructors you can disambiguate which constructor to invoke with the `jakarta.inject.Inject` annotation or the @Creator annotation:

Example of Constructor Injection

```java
package io.micronaut.docs.ioc.injection.ctor;

import io.micronaut.core.annotation.Creator;
import jakarta.inject.Inject;
import jakarta.inject.Singleton;

@Singleton
class Vehicle {
    private final Engine engine;

    @Inject // (1)
    Vehicle(Engine engine) {
        this.engine = engine;
    }

    Vehicle() {
        this.engine = Engine.create(6);
    }

    void start() {
        engine.start();
    }
}

@Singleton
record Engine(int cylinders) {

    @Creator // (2)
    static Engine getDefault() {
        return new Engine(8);
    }

    static Engine create(int cylinders) {
        return new Engine(cylinders);
    }

    void start() {
        System.out.println("Vrooom! " + cylinders);
    }
}
```

Example of Constructor Injection

```groovy
package io.micronaut.docs.ioc.injection.ctor

import io.micronaut.core.annotation.Creator
import jakarta.inject.Inject
import jakarta.inject.Singleton

@Singleton
class Vehicle {
    private final Engine engine

    @Inject // (1)
    Vehicle(Engine engine) {
        this.engine = engine
    }

    Vehicle() {
        this.engine = Engine.create(6)
    }

    void start() {
        engine.start()
    }
}

@Singleton
record Engine(int cylinders) {

    @Creator // (2)
    static Engine getDefault() {
        return new Engine(8)
    }

    static Engine create(int cylinders) {
        return new Engine(cylinders)
    }

    void start() {
        println("Vrooom! $cylinders")
    }
}
```

| **1** | Multiple constructors are defined so `@Inject` is used to select the correct constructor. |
|---|---|
| **2** | The @Creator annotation can also be used to select a `static` factory method to use as a constructor. |

In the above example retrieving the `Vehicle` type from the BeanContext will result in calling the `Vehicle(Engine engine)` constructor which will in turn resolve the `Engine` using the `getDefault()` method since it is annotated with `@Creator`.

|   | If no `@Inject` or `@Creator` is specified Micronaut will try to locate the first `public` constructor in the class otherwise a compilation error will occur. |
|---|---|

If there are multiple possible candidates for a particular constructor argument a qualifier can be specified (such as `jakarta.inject.Named`) to disambiguate the injection. If it is not possible to disambiguate then the result will be a NonUniqueBeanException. See the Qualifiers section for more information.

|   | If you use `@Inject` on a `private` constructor then the type will be instantiated via the Java reflection API which is not recommended. |
|---|---|


## 3.5.2 Field Injection

You can inject non-final Java fields by annotating the field with `jakarta.inject.Inject`, for example:

Example of Field Injection

```java
package io.micronaut.docs.ioc.injection.field;

import jakarta.inject.Inject;
import jakarta.inject.Singleton;

@Singleton
class Vehicle {
    @Inject Engine engine; // (1)

    void start() {
        engine.start();
    }
}

@Singleton
class Engine {
    void start() {
        System.out.println("Vrooom!" );
    }
}
```

Example of Field Injection

```groovy
package io.micronaut.docs.ioc.injection.field

import jakarta.inject.Inject
import jakarta.inject.Singleton

@Singleton
class Vehicle {
    @Inject Engine engine // (1)

    void start() {
        engine.start()
    }
}

@Singleton
class Engine {
    void start() {
        println("Vrooom!" )
    }
}
```

| **1** | The field is annotated with `jakarta.inject.Inject`. |
|---|---|
| **2** | Note that for Kotlin instead of an optional type (a type ending with `?`) you can use `lateinit var` |

Trying to inject a field that is declared `final` will result in a compilation error. Field injection should be seen as inferior to constructor injection as explained in the previous sections since it can result in the code being less-structured, harder to read and harder to test.

|   | If the field is `private` scope or inaccessible then the field will be injected using the Java reflection API which is not recommended. |
|---|---|


## 3.5.3 Method Injection

You can inject methods by annotating the method with `jakarta.inject.Inject`. For each argument of the method Micronaut will attempt to resolve the method argument as a bean. If any of the methods are not resolvable a NoSuchBeanException will be thrown.

Example of Method Injection

```java
package io.micronaut.docs.ioc.injection.method;

import jakarta.inject.Inject;
import jakarta.inject.Singleton;

@Singleton
class Vehicle {
    private Engine engine;

    @Inject // (1)
    void initialize(Engine engine) {
        this.engine = engine;
    }

    void start() {
        engine.start();
    }
}

@Singleton
class Engine {
    void start() {
        System.out.println("Vrooom!" );
    }
}
```

Example of Method Injection

```groovy
package io.micronaut.docs.ioc.injection.method

import jakarta.inject.Inject
import jakarta.inject.Singleton

@Singleton
class Vehicle {
    private Engine engine

    @Inject // (1)
    void initialize(Engine engine) {
        this.engine = engine
    }

    void start() {
        engine.start()
    }
}

@Singleton
class Engine {
    void start() {
        println("Vrooom!")
    }
}
```

| **1** | The method is annotated with `jakarta.inject.Inject` and will therefore be injected |
|---|---|

|   | If the method is `private` scope or inaccessible then the method will be injected using the Java reflection API which is not recommended. |
|---|---|

Method injection can be useful if you need post construction initializers, however in general should be avoided in favour of constructor injection where possible.


## 3.5.4 Nullable Injection

Occasionally it is desirable for injection to be optional (ie. not fail with a NoSuchBeanException if there is no candidate bean available).

For example if you are trying to build an extensible system where a default implementation is provided by the type but consumers of your API can provide a bean that, if available, will be injected.

One way to make injection optional is to annotate the injected type with `org.jspecify.annotations.Nullable` which will result in `null` being injected by the framework if the bean is unavailable:

Example of Injecting

null

```java
package io.micronaut.docs.ioc.injection.nullable;

import org.jspecify.annotations.Nullable;
import jakarta.inject.Inject;
import jakarta.inject.Singleton;

@Singleton
class Vehicle {
    private final Engine engine;

    Vehicle(@Nullable Engine engine) { // (1)
        this.engine = engine != null ? engine : Engine.create(6); // (2)
    }
    void start() {
        engine.start();
    }

    public Engine getEngine() {
        return engine;
    }
}

record Engine(int cylinders) {

    static Engine create(int cylinders) {
        return new Engine(cylinders);
    }

    void start() {
        System.out.println("Vrooom! " + cylinders);
    }
}
```

Example of Injecting

null

```groovy
package io.micronaut.docs.ioc.injection.nullable

import org.jspecify.annotations.Nullable
import jakarta.inject.Singleton

@Singleton
class Vehicle {
    private final Engine engine

    Vehicle(@Nullable Engine engine) { // (1)
        this.engine = engine ?: Engine.create(6) // (2)
    }
    void start() {
        engine.start()
    }
}

record Engine(int cylinders) {

    static Engine create(int cylinders) {
        return new Engine(cylinders)
    }

    void start() {
        println("Vrooom! $cylinders")
    }
}
```

| **1** | Here the constructor argument is annotated with `org.jspecify.annotations.Nullable` |
|---|---|
| **2** | Since there is no bean available `null` is injected and the code has to handle the possibility that the argument could be `null. |

Using `org.jspecify.annotations.Nullable` has the following considerations:

- Can be used with any of the injection types (constructor, method or field injection)
- Somewhere the code has to handle what happens if `null` is injected, for constructors this is easy since the constructor can handle the `null`, but for fields and methods a `@PostConstruct` method would need to be implemented to handle `null` if `null` is not desirable.
- Finally, `@Nullable` cannot be used on primitive types like `int`, `long` etc. when using configuration injection. To handle primitives you need to specify `@Bindable(defaultValue="..")` and provide a default value.


## 3.6 Injectable Container Types

In addition to being able to inject beans, Micronaut framework natively supports injecting the following types:

| Type | Description | Example |
|---|---|---|
| java.util.Optional | An `Optional` of a bean. `empty()` is injected if the bean doesn’t exist | `Optional<Engine>` |
| java.util.Collection | An `Collection` or subtype of `Collection` (e.g. `List`, `Set`, etc.) | `Collection<Engine>` |
| java.util.Map | An `Map` or subtype of `Map` (e.g. `LinkedHashMap`, `TreeMap`, etc.) where the key is the qualifier | `Map<String, Engine>` |
| java.util.stream.Stream | A lazy `Stream` of beans | `Stream<Engine>` |
| Array | A native array of beans of a given type | `Engine[]` |
| Provider | A `jakarta.inject.Provider` if a circular dependency requires it, or to instantiate a prototype for each `get` call. | `Provider<Engine>` |
| BeanProvider | A `io.micronaut.context.BeanProvider` if a circular dependency requires it or to instantiate a prototype for each `get` call. | `BeanProvider<Engine>` |

|   | There are 3 different provider types supported, however the `BeanProvider` is the one we suggest to use. |
|---|---|

|   | When injecting a `java.lang.Collection`, or `java.util.stream.Stream`, `Array` of beans into a bean matching the injection type, then the owning bean will not be a member of the injected collection. A common pattern demonstrating this is aggregation. For example: `@Singleton class AggregateEngine implements Engine { @Inject List<Engine> engines; @Override public void start() { engines.forEach(Engine::start); } ... }` In this example, the injected member variable `engines` will not contain an instance of `AggregateEngine` |
|---|---|

|   | A prototype bean will have one instance created per place the bean is injected. When a prototype bean is injected as a provider, each call to `get()` creates a new instance. |
|---|---|

### Collection Ordering

When injecting a collection of beans, they are not ordered by default. Implement the Ordered interface to inject an ordered collection. If the requested bean type does not implement Ordered, Micronaut framework searches for the @Order annotation on beans.

The @Order annotation is especially useful for ordering beans created by factories where the bean type is a class in a third-party library. In this example, both `LowRateLimit` and `HighRateLimit` implement the `RateLimit` interface.

Factory with @Order

```java
import io.micronaut.context.annotation.Factory;
import io.micronaut.core.annotation.Order;

import jakarta.inject.Singleton;
import java.time.Duration;

@Factory
public class RateLimitsFactory {

    @Singleton
    @Order(20)
    LowRateLimit rateLimit2() {
        return new LowRateLimit(Duration.ofMinutes(50), 100);
    }

    @Singleton
    @Order(10)
    HighRateLimit rateLimit1() {
        return new HighRateLimit(Duration.ofMinutes(50), 1000);
    }
}
```

Factory with @Order

```kotlin
import io.micronaut.context.annotation.Factory
import io.micronaut.core.annotation.Order
import java.time.Duration
import jakarta.inject.Singleton

@Factory
class RateLimitsFactory {

    @Singleton
    @Order(20)
    fun rateLimit2(): LowRateLimit {
        return LowRateLimit(Duration.ofMinutes(50), 100)
    }

    @Singleton
    @Order(10)
    fun rateLimit1(): HighRateLimit {
        return HighRateLimit(Duration.ofMinutes(50), 1000)
    }
}
```

Factory with @Order

```groovy
import io.micronaut.context.annotation.Factory
import io.micronaut.core.annotation.Order

import jakarta.inject.Singleton
import java.time.Duration

@Factory
class RateLimitsFactory {

    @Singleton
    @Order(20)
    LowRateLimit rateLimit2() {
        new LowRateLimit(Duration.ofMinutes(50), 100);
    }

    @Singleton
    @Order(10)
    HighRateLimit rateLimit1() {
        new HighRateLimit(Duration.ofMinutes(50), 1000);
    }
}
```

When a collection of `RateLimit` beans are requested from the context, they are returned in ascending order based on the value in the annotation. Micronaut maps jakarta.annotation.Priority to @Order at build time, so @Priority values are treated the same as @Order and follow the same ascending numeric precedence (lower numbers mean higher precedence).

### Injecting a Bean by Order

When injecting a single instance of a bean the @Order annotation can also be used to define which bean has the highest precedence and hence should be injected. Micronaut also maps jakarta.annotation.Priority to @Order at build time, so the same mapped @Priority numeric semantics determine which bean has the highest precedence for single-bean injection.

|   | The Ordered interface is not taken into account when selecting a single instance as this would require instantiating the bean to resolve the order. |
|---|---|


## 3.7 Bean Qualifiers

If you have multiple possible implementations for a given interface to inject, you need to use a qualifier.

Once again Micronaut framework leverages JSR-330 and the Qualifier and Named annotations to support this use case.
