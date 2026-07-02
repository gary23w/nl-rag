---
title: "Micronaut Core (part 23/27)"
source: https://docs.micronaut.io/latest/guide/index.html
domain: micronaut
license: CC-BY-SA-4.0
tags: micronaut framework, micronaut jvm, compile-time injection, microservices framework
fetched: 2026-07-02
part: 23/27
---

## 11.3 Google Cloud Run

To deploy to Google Cloud Run we recommend using JIB to containerize your application.

|   | Using the CLI Creating an application with JIB: $ mn create-app my-app --features jib Or with Micronaut Launch $ curl https://launch.micronaut.io/example.zip\?features\=jib -o example.zip $ unzip example.zip -d example |
|---|---|

With JIB setup to deploy your application to Google Container Registry, run:

```bash
$ ./gradlew jib
```

You are now ready to deploy your application:

```bash
$ gcloud run deploy --image gcr.io/[PROJECT ID]/example --platform=managed --allow-unauthenticated
```

Where `[PROJECT ID]` is your project ID. You will be asked to specify a region and will see output like the following:

```none
Service name: (example):
Deploying container to Cloud Run service [example] in project [PROJECT_ID] region [us-central1]

✓ Deploying... Done.
  ✓ Creating Revision...
  ✓ Routing traffic...
  ✓ Setting IAM Policy...
Done.
Service [example] revision [example-00004] has been deployed and is serving 100 percent of traffic at https://example-9487r97234-uc.a.run.app
```

The URL is the URL of your Cloud Run application.


## 11.4 Azure Function

Support for Azure Function is implemented in the Micronaut Azure subproject.

#### Simple Functions with Azure Function

You can implement Azure Functions with the Micronaut framework that directly implement the Azure Function Java SDK. See the documentation on Azure Functions for more information.

|   | Using the CLI To create an Azure Function: $ mn create-function-app my-app --features azure-function Or with Micronaut Launch $ curl https://launch.micronaut.io/create/function/example\?features\=azure-function -o example.zip $ unzip example.zip -d example |
|---|---|

#### HTTP Functions with Azure Function

You can deploy regular Micronaut applications that use @Controller etc. using Micronaut’s support for Azure HTTP Functions. See the documentation on Azure HTTP Functions for more information.

|   | Using the CLI To create an Azure HTTP Function: $ mn create-app my-app --features azure-function Or with Micronaut Launch $ curl https://launch.micronaut.io/example.zip\?features\=azure-function -o example.zip $ unzip example.zip -d example |
|---|---|

# 12 Message-Driven Microservices

In the past, with monolithic applications, message listeners that listened to messages from messaging systems would frequently be embedded in the same application unit.

In Microservice architectures it is common to have individual Microservice applications that are driven by a message system such as RabbitMQ or Kafka.

In fact a Message-driven Microservice may not even feature an HTTP endpoint or HTTP server (although this can be valuable from a health check and visibility perspective).


## 12.1 Kafka Support

Apache Kafka is a distributed stream processing platform that can be used for a range of messaging requirements in addition to stream processing and real-time data handling.

The Micronaut framework features dedicated support for defining both Kafka `Producer` and `Consumer` instances. Micronaut applications built with Kafka can be deployed with or without the presence of an HTTP server.

With Micronaut’s efficient compile-time AOP and cloud native features, writing efficient Kafka consumer applications that use very little resources is a breeze.

See the documentation for Micronaut Kafka for more information on how to build Kafka applications with Micronaut.


## 12.2 RabbitMQ Support

RabbitMQ is the most widely deployed open source message broker.

The Micronaut framework features dedicated support for defining both RabbitMQ publishers and consumers. Micronaut applications built with RabbitMQ can be deployed with or without an HTTP server.

With Micronaut framework’s efficient compile-time AOP, using RabbitMQ has never been easier. Support has been added for publisher confirms and RPC through reactive streams.

See the documentation for Micronaut RabbitMQ for more information on how to build RabbitMQ applications with Micronaut.


## 12.3 Nats.io Support

Nats.io is a simple, secure, and high-performance open source messaging system for cloud native applications, IoT messaging, and microservices architectures.

The Micronaut framework features dedicated support for defining both Nats.io publishers and consumers. Micronaut applications built with Nats.io can be deployed with or without an HTTP server.

With Micronaut’s efficient compile-time AOP, using Nats.io has never been easier. Support has been added for publisher confirms and RPC through reactive streams.

See the documentation for Micronaut Nats for more information on how to build Nats.io applications with Micronaut.

# 13 Standalone Command Line Applications

In certain cases you may wish to create standalone command-line (CLI) applications that interact with your Microservice infrastructure.

Examples of applications like this include scheduled tasks, batch applications and general command line applications.

In this case having a robust way to parse command line options and positional parameters is important.


## 13.1 Picocli Support

Picocli is a command line parser that supports usage help with ANSI colors, autocomplete, and nested subcommands. It has an annotations API to create command line applications with almost no code, and a programmatic API for dynamic uses like creating Domain Specific Languages.

See the documentation for the Picocli integration for more information.

# 14 Configurations

Micronaut framework features several built-in configurations that enable integration with common databases and other servers.


## 14.1 Configurations for Reactive Programming

Project Reactor is used internally by Micronaut. However, to use Reactor or other reactive libraries (e.g. RxJava) types in your controller and/or HTTP Client methods you need to include dependencies.


## 14.1.1 Reactor Support

To add support for Reactor, add the following module:

`implementation("io.micronaut.reactor:micronaut-reactor")` `<dependency> <groupId>io.micronaut.reactor</groupId> <artifactId>micronaut-reactor</artifactId> </dependency>`

To use the Reactor HTTP client, add the following dependency:

`implementation("io.micronaut.reactor:micronaut-reactor-http-client")` `<dependency> <groupId>io.micronaut.reactor</groupId> <artifactId>micronaut-reactor-http-client</artifactId> </dependency>`

For more information see the documentation for Micronaut Reactor.


## 14.1.2 RxJava 3 Support

To add support for RxJava 3, add the following module:

`implementation("io.micronaut.rxjava3:micronaut-rxjava3")` `<dependency> <groupId>io.micronaut.rxjava3</groupId> <artifactId>micronaut-rxjava3</artifactId> </dependency>`

To use the RxJava 3 HTTP client, add the following dependency:

`implementation("io.micronaut.rxjava3:micronaut-rxjava3-http-client")` `<dependency> <groupId>io.micronaut.rxjava3</groupId> <artifactId>micronaut-rxjava3-http-client</artifactId> </dependency>`

For more information see the documentation for Micronaut RxJava 3.


## 14.2 Configurations for Data Access

This table summarizes the configuration modules and dependencies to add to your build to enable them:

| Dependency | Description |
|---|---|
| `io.micronaut.sql:micronaut-jdbc-dbcp` | Configures SQL DataSources using Commons DBCP |
| `io.micronaut.sql:micronaut-jdbc-hikari` | Configures SQL DataSources using Hikari Connection Pool |
| `io.micronaut.sql:micronaut-jdbc-tomcat` | Configures SQL DataSources using Tomcat Connection Pool |
| `io.micronaut.sql:micronaut-hibernate-jpa` | Configures Hibernate/JPA `EntityManagerFactory` beans |
| `io.micronaut.mongodb:micronaut-mongo-reactive` | Configures the MongoDB Reactive Driver |
| `io.micronaut.neo4j:micronaut-neo4j-bolt` | Configures the Bolt Java Driver for Neo4j |
| `io.micronaut.sql:micronaut-vertx-mysql-client` | Configures the Reactive MySQL Client |
| `io.micronaut.sql:micronaut-vertx-pg-client` | Configures the Reactive Postgres Client |
| `io.micronaut.redis:micronaut-redis-lettuce` | Configures the Lettuce driver for Redis |
| `io.micronaut.cassandra:micronaut-cassandra` | Configures the Datastax Java Driver for Cassandra |

For example, to add support for MongoDB, add the following dependency:

build.gradle

```groovy
compile "io.micronaut.mongodb:micronaut-mongo-reactive"
```

The following sections go into more detail about configuration options and the exposed beans for each implementation.


## 14.2.1 Configuring a SQL Data Source

JDBC DataSources can be configured for one of three currently provided implementations - Apache DBCP2, Hikari, and Tomcat are supported by default.


## Configuring a JDBC DataSource

|   | Using the CLI If you create your project using the Micronaut CLI, supply one of the `jdbc-tomcat`, `jdbc-hikari`, or `jdbc-dbcp` features to preconfigure a simple JDBC connection pool in your project, along with a default H2 database driver: $ mn create-app my-app --features jdbc-tomcat |
|---|---|

To get started, add a dependency for one of the JDBC configurations that corresponds to the implementation you will use. Choose one of the following:

`runtimeOnly("io.micronaut.sql:micronaut-jdbc-tomcat")` `<dependency> <groupId>io.micronaut.sql</groupId> <artifactId>micronaut-jdbc-tomcat</artifactId> <scope>runtime</scope> </dependency>`

`runtimeOnly("io.micronaut.sql:micronaut-jdbc-hikari")` `<dependency> <groupId>io.micronaut.sql</groupId> <artifactId>micronaut-jdbc-hikari</artifactId> <scope>runtime</scope> </dependency>`

`runtimeOnly("io.micronaut.sql:micronaut-jdbc-dbcp")` `<dependency> <groupId>io.micronaut.sql</groupId> <artifactId>micronaut-jdbc-dbcp</artifactId> <scope>runtime</scope> </dependency>`

`runtimeOnly("io.micronaut.sql:micronaut-jdbc-ucp")` `<dependency> <groupId>io.micronaut.sql</groupId> <artifactId>micronaut-jdbc-ucp</artifactId> <scope>runtime</scope> </dependency>`

Also, add a JDBC driver dependency to your build. For example to add the H2 In-Memory Database:

`runtimeOnly("com.h2database:h2")` `<dependency> <groupId>com.h2database</groupId> <artifactId>h2</artifactId> <scope>runtime</scope> </dependency>`

For more information see the Configuring JDBC section of the Micronaut SQL libraries project.


## 14.2.2 Configuring Hibernate

#### Setting up a Hibernate/JPA EntityManager

|   | Using the CLI If you create your project using the Micronaut CLI, supply the `hibernate-jpa` feature to include a Hibernate JPA configuration in your project: $ mn create-app my-app --features hibernate-jpa |
|---|---|

The Micronaut framework includes support for configuring a Hibernate / JPA `EntityManager` that builds on the SQL DataSource support.

Once you have configured one or more DataSources to use Hibernate, add the `hibernate-jpa` dependency to your build:

`implementation("io.micronaut.sql:micronaut-hibernate-jpa")` `<dependency> <groupId>io.micronaut.sql</groupId> <artifactId>micronaut-hibernate-jpa</artifactId> </dependency>`

For more information see the Configuring Hibernate section of the Micronaut SQL libraries project.


## 14.2.3 Configuring MongoDB

#### Setting up the Native MongoDB Driver

|   | Using the CLI If you create your project using the Micronaut CLI, supply the `mongo-reactive` feature to configure the native MongoDB driver in your project: $ mn create-app my-app --features mongo-reactive |
|---|---|

The Micronaut framework can automatically configure the native MongoDB Java driver. To use this, add the following dependency to your build:

`implementation("io.micronaut.mongodb:micronaut-mongo-reactive")` `<dependency> <groupId>io.micronaut.mongodb</groupId> <artifactId>micronaut-mongo-reactive</artifactId> </dependency>`

Then configure the URI of the MongoDB server in your configuration file (e.g `application.yml`):

Configuring a MongoDB server

```properties
mongodb.uri=mongodb://username:password@localhost:27017/databaseName
```

```yaml
mongodb:
  uri: mongodb://username:password@localhost:27017/databaseName
```

```toml
[mongodb]
  uri="mongodb://username:password@localhost:27017/databaseName"
```

```groovy
mongodb {
  uri = "mongodb://username:password@localhost:27017/databaseName"
}
```

```hocon
{
  mongodb {
    uri = "mongodb://username:password@localhost:27017/databaseName"
  }
}
```

```json
{
  "mongodb": {
    "uri": "mongodb://username:password@localhost:27017/databaseName"
  }
}
```

|   | The `mongodb.uri` follows the MongoDB Connection String format. |
|---|---|

A non-blocking Reactive Streams MongoClient is then available for dependency injection.

To use the blocking driver, add a dependency to your build on the mongo-java-driver:

```groovy
runtimeOnly "org.mongodb:mongo-java-driver"
```

Then the blocking MongoClient will be available for injection.

See the Micronaut MongoDB documentation for further information on configuring and using MongoDB within Micronaut.


## 14.2.4 Configuring Neo4j

The Micronaut Framework features dedicated support for automatically configuring the Neo4j Bolt Driver for the popular Neo4j Graph Database.

|   | Using the CLI If you create your project using the Micronaut CLI, supply the `neo4j-bolt` feature to configure the Neo4j Bolt driver in your project: $ mn create-app my-app --features neo4j-bolt |
|---|---|

To configure the Neo4j Bolt driver, first add the `neo4j-bolt` module to your build:

`implementation("io.micronaut:micronaut-neo4j-bolt")` `<dependency> <groupId>io.micronaut</groupId> <artifactId>micronaut-neo4j-bolt</artifactId> </dependency>`

Then configure the URI of the Neo4j server in your configuration file (e.g `application.yml`):

Configuring

neo4j.uri

```properties
neo4j.uri=bolt://localhost
```

```yaml
neo4j:
  uri: bolt://localhost
```

```toml
[neo4j]
  uri="bolt://localhost"
```

```groovy
neo4j {
  uri = "bolt://localhost"
}
```

```hocon
{
  neo4j {
    uri = "bolt://localhost"
  }
}
```

```json
{
  "neo4j": {
    "uri": "bolt://localhost"
  }
}
```

|   | The `neo4j.uri` setting must be in the format as described in the Connection URIs section of the Neo4j documentation |
|---|---|

Once you have the above configuration in place you can inject an instance of the `org.neo4j.driver.v1.Driver` bean, which features both a synchronous blocking API and a non-blocking API based on `CompletableFuture`.

See the Micronaut Neo4j documentation for further information on configuring and using Neo4j within Micronaut.


## 14.2.5 Configuring Postgres

The Micronaut framework supports a reactive and non-blocking client to connect to Postgres using vertx-pg-client, which can handle many database connections with a single thread.


## Configuring the Reactive Postgres Client

|   | Using the CLI If you create your project using the Micronaut CLI, supply the `vertx-pg-client` feature to configure the Reactive Postgres client in your project: $ mn create-app my-app --features vertx-pg-client |
|---|---|

To configure the Reactive Postgres client, first add the `vertx-pg-client` module to your build:

build.gradle

```groovy
compile "io.micronaut.sql:micronaut-vertx-pg-client"
```

For more information see the Configuring Reactive Postgres section of the Micronaut SQL libraries project.


## 14.2.6 Configuring Redis

The Micronaut framework features automatic configuration of the Lettuce driver for Redis via the `redis-lettuce` module.


## Configuring Lettuce

|   | Using the CLI If you create your project using the Micronaut CLI, supply the `redis-lettuce` feature to configure the Lettuce driver in your project: $ mn create-app my-app --features redis-lettuce |
|---|---|

To configure the Lettuce driver, first add the `redis-lettuce` module to your build:

build.gradle

```groovy
compile "io.micronaut.redis:micronaut-redis-lettuce"
```

Then configure the URI of the Redis server in your configuration file (e.g `application.yml`):

Configuring

redis.uri

```properties
redis.uri=redis://localhost
```

```yaml
redis:
  uri: redis://localhost
```

```toml
[redis]
  uri="redis://localhost"
```

```groovy
redis {
  uri = "redis://localhost"
}
```

```hocon
{
  redis {
    uri = "redis://localhost"
  }
}
```

```json
{
  "redis": {
    "uri": "redis://localhost"
  }
}
```

|   | The `redis.uri` setting must be in the format as described in the Connection URIs section of the Lettuce wiki |
|---|---|

You can also specify multiple Redis URIs using `redis.uris`, in which case a `RedisClusterClient` is created instead.

For more information and further documentation see the Micronaut Redis documentation.


## 14.2.7 Configuring Cassandra

|   | Using the CLI If you create your project using the Micronaut CLI, supply the `cassandra` feature to include Cassandra configuration in your project: $ mn create-app my-app --features cassandra |
|---|---|

For more information see the Micronaut Cassandra Module documentation.


## 14.2.8 Configuring Liquibase

To configure the Micronaut integration with Liquibase, please follow these instructions.


## 14.2.9 Configuring Flyway

To configure the Micronaut integration with Flyway, please follow these instructions

# 15 Logging

The Micronaut framework uses Slf4j to log messages. The default implementation for applications created via Micronaut Launch is Logback. Any other Slf4j implementation is supported, however.


## 15.1 Logging Messages

To log messages, use the Slf4j `LoggerFactory` to get a logger for your class.

```java
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class LoggerExample {

    private static Logger logger = LoggerFactory.getLogger(LoggerExample.class);

    public static void main(String[] args) {
        logger.debug("Debug message");
        logger.info("Info message");
        logger.error("Error message");
    }
}
```


## 15.2 Configuration

Log levels can be configured via properties defined in your configuration file (e.g. `application.yml`) (and environment variables) with the `logger.levels` prefix:

```properties
logger.levels.foo.bar=ERROR
```

```yaml
logger:
  levels:
    foo.bar: ERROR
```

```toml
[logger]
  [logger.levels]
    "foo.bar"="ERROR"
```

```groovy
logger {
  levels {
    foo.bar = "ERROR"
  }
}
```

```hocon
{
  logger {
    levels {
      "foo.bar" = "ERROR"
    }
  }
}
```

```json
{
  "logger": {
    "levels": {
      "foo.bar": "ERROR"
    }
  }
}
```

The same configuration can be achieved by setting the environment variable `LOGGER_LEVELS_FOO_BAR`. Note that there is currently no way to set log levels for unconventional prefixes such as `foo.barBaz`.

#### Custom Logback XML Configuration

```properties
logger.config=/foo/custom-logback.xml
```

```yaml
logger:
  config: /foo/custom-logback.xml
```

```toml
[logger]
  config="/foo/custom-logback.xml"
```

```groovy
logger {
  config = "/foo/custom-logback.xml"
}
```

```hocon
{
  logger {
    config = "/foo/custom-logback.xml"
  }
}
```

```json
{
  "logger": {
    "config": "/foo/custom-logback.xml"
  }
}
```

You can also set a custom Logback XML configuration file to be used via `logger.config`. The file is first checked on the classpath and then on the file system.

#### Disabling a Logger with Properties

To disable a logger, you need to set the logger level to `OFF`:

```properties
logger.levels.io.verbose.logger.who.CriedWolf=false
```

```yaml
logger:
  levels:
    io.verbose.logger.who.CriedWolf: OFF
```

```toml
[logger]
  [logger.levels]
    "io.verbose.logger.who.CriedWolf"=false
```

```groovy
logger {
  levels {
    io.verbose.logger.who.CriedWolf = false
  }
}
```

```hocon
{
  logger {
    levels {
      "io.verbose.logger.who.CriedWolf" = false
    }
  }
}
```

```json
{
  "logger": {
    "levels": {
      "io.verbose.logger.who.CriedWolf": false
    }
  }
}
```

- This will disable ALL logging for the class `io.verbose.logger.who.CriedWolf`

Note that the ability to control log levels via config is controlled via the LoggingSystem interface. Currently, the Micronaut framework includes a single implementation that allows setting log levels for the Logback library. If you use another library, you should provide a bean that implements this interface.


## 15.3 Logback

To use the logback library, add the following dependency to your build.

`implementation("ch.qos.logback:logback-classic")` `<dependency> <groupId>ch.qos.logback</groupId> <artifactId>logback-classic</artifactId> </dependency>`

|   | Logback 1.3.x+ included a breaking binary change that may prevent it working with 3.8.x of the Micronaut framework. If you are using Logback 1.3.x+ and are experiencing issues, please downgrade to Logback 1.2.x. |
|---|---|

If it does not exist yet, place a logback.xml file in the resources folder and modify the content for your needs. For example:

src/main/resources/logback.xml

```xml
<configuration>

    <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
        <encoder>
            <pattern>%cyan(%d{HH:mm:ss.SSS}) %gray([%thread]) %highlight(%-5level) %magenta(%logger{36}) - %msg%n
            </pattern>
        </encoder>
    </appender>

    <root level="info">
        <appender-ref ref="STDOUT"/>
    </root>

</configuration>
```

To change the log level for specific classes or package names, you can add such a logger entry to the configuration section:

```xml
<configuration>
    ...
    <logger name="io.micronaut.context" level="TRACE"/>
    ...
</configuration>
```


## 15.4 Logging System

The Micronaut framework has a notion of a logging system. In short, it is a simple API to be able to set log levels in the logging implementation at runtime. Default implementations are provided for Logback and Log4j2. The behavior of the logging system can be overridden by creating your own implementation of LoggingSystem and replace the implementation being used with the @Replaces annotation.

# 16 Language Support

Micronaut framework supports any JVM language that implements the Java Annotation Processor API.

Although Groovy does not support this API, special support has been built using AST transformations. The current list of supported languages is: Java, Groovy, and Kotlin (via the `kapt` tool).

|   | Theoretically any language that supports a way to analyze the AST at compile time could be supported. The io.micronaut.inject.writer package includes language-neutral classes that build BeanDefinition classes at compile time using the ASM tool. |
|---|---|

The following sections cover language-specific features and considerations for using Micronaut.


## 16.1 Micronaut for Java

For Java, Micronaut framework uses a Java BeanDefinitionInjectProcessor annotation processor to process classes at compile time and produce BeanDefinition classes.

The major advantage here is that you pay a slight cost at compile time, but at runtime Micronaut framework is largely reflection-free, fast, and consumes very little memory.


## 16.1.1 Using Micronaut with Java 9+

The Micronaut framework is built with Java 8 but works fine with Java 9 and above. The classes that Micronaut generates sit alongside existing classes in the same package, hence do not violate anything regarding the Java module system.

There are some considerations when using Java 9+ with Micronaut.

### The javax.annotation package

|   | Using the CLI If you create your project using the Micronaut CLI, the `javax.annotation` dependency is added to your project automatically if you use Java 9+. |
|---|---|

The `javax.annotation`, which includes `@PostConstruct`, `@PreDestroy`, etc. has been moved from the core JDK to a module. In general annotations in this package should be avoided and instead the `jakarta.annotation` equivalents used.


## 16.1.2 Incremental Annotation Processing with Gradle

The Micronaut framework supports Gradle incremental annotation processing which speeds up builds by compiling only classes that have changed, avoiding a full recompilation.

However, the support is disabled by default since the Micronaut framework allows the definition of custom meta-annotations (to for example define custom AOP advice) that need to be configured for processing.

The following example demonstrates how to enable and configure incremental annotation processing for annotations you have defined under the `com.example` package:

Enabling Incremental Annotation Processing

```groovy
tasks.withType(JavaCompile) {
    options.compilerArgs = [
        '-Amicronaut.processing.incremental=true',
        '-Amicronaut.processing.annotations=com.example.*',
    ]
}
```

|   | If you do not enable processing for your custom annotations, they will be ignored by Micronaut, which may break your application. |
|---|---|


## 16.1.3 Using Project Lombok

Project Lombok is a popular java library that adds a number of useful AST transformations to the Java language via annotation processors.

Since both the Micronaut framework and Lombok use annotation processors, special care must be taken when configuring Lombok to ensure that the Lombok processor runs **before** Micronaut’s processor.

If you use Gradle, add the following dependencies:

Configuring Lombok in Gradle

```groovy
compileOnly 'org.projectlombok:lombok:1.18.24'
annotationProcessor "org.projectlombok:lombok:1.18.24"
...
// Micronaut processor defined after Lombok
annotationProcessor "io.micronaut:micronaut-inject-java"
```

Or if using Maven:

Configuring Lombok in Maven

```xml
<dependencies>
  <dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <version>1.18.24</version>
    <scope>provided</scope>
  </dependency>
</dependencies>
...
<annotationProcessorPaths combine.self="override">
  <path>
    <!-- must precede micronaut-inject-java -->
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <version>1.18.24</version>
  </path>
  <path>
    <groupId>io.micronaut</groupId>
    <artifactId>micronaut-inject-java</artifactId>
    <version>${micronaut.version}</version>
  </path>
  <path>
    <groupId>io.micronaut.validation</groupId>
    <artifactId>micronaut-validation-processor</artifactId>
    <version>${micronaut.version}</version>
  </path>
</annotationProcessorPaths>
```

|   | In both cases (Gradle and Maven) the Micronaut processor must be configured after the Lombok processor. Reversing the order of the declared dependencies will not work. |
|---|---|


## 16.1.4 Configuring an IDE

You can use any IDE to develop Micronaut applications, if you depend on your configured build tool (Gradle or Maven) to build the application.

However, running tests within the IDE is currently possible with IntelliJ IDEA or Eclipse 4.9 or higher.

See the section on IDE Setup in the Quick start for more information on how to configure IntelliJ and Eclipse.


## 16.1.5 Retaining Parameter Names

By default, with Java, the parameter name data for method parameters is not retained at compile time. This can be a problem for the Micronaut framework if you do not define parameter names explicitly and depend on an external JAR that is already compiled.

Consider this interface:

Client Interface

```java
interface HelloOperations {
    @Get("/hello/{name}")
    String hello(String name);
}
```

At compile time the parameter name `name` is lost and becomes `arg0` when compiled against or read via reflection later. To avoid this problem you have two options. You can either declare the parameter name explicitly:

Client Interface

```java
interface HelloOperations {
    @Get("/hello/{name}")
    String hello(@QueryValue("name") String name);
}
```

Or alternatively it is recommended that you compile all bytecode with `-parameters` flag to `javac`. See Obtaining Names of Method Parameters. For example in `build.gradle`:

build.gradle

```groovy
compileJava.options.compilerArgs += '-parameters'
```


## 16.2 Micronaut for Groovy

Groovy has first-class support in Micronaut.


## Groovy-Specific Modules

Additional modules exist specific to Groovy that improve the overall experience. These are detailed in the table below:

| Dependency | Description |
|---|---|
| `io.micronaut:micronaut-inject-groovy` | Includes AST transformations to generate bean definitions. Should be `compileOnly` on your classpath. |
| `io.micronaut:micronaut-runtime-groovy` | Adds the ability to specify configuration under `src/main/resources` in Groovy format (i.e. `application.groovy`) |
| `io.micronaut:micronaut-function-groovy` | Includes AST transforms that make it easier to write Functions for AWS Lambda |

The most common module you need is `micronaut-inject-groovy`, which enables DI and AOP for Groovy classes.


## Groovy Support in the CLI

The Micronaut Command Line Interface includes special support for Groovy. To create a Groovy application, use the `groovy` lang option. For example:

Create a Micronaut Groovy application

```bash
$ mn create-app hello-world --lang groovy
```

The above generates a Groovy project, built with Gradle. Use the `-build maven` flag to generate a project built with Maven instead.

Once you have created an application with the `groovy` feature, commands like `create-controller`, `create-client` etc. generate Groovy files instead of Java. The following example demonstrates this when using interactive mode of the CLI:

Create a bean

```bash
$ mn
| Starting interactive mode...
| Enter a command name to run. Use TAB for completion:
mn>

create-bean          create-client        create-controller
create-job           help

mn> create-bean helloBean
| Rendered template Bean.groovy to destination src/main/groovy/hello/world/HelloBean.groovy
```

The above example demonstrates creating a Groovy bean that looks like the following:

Micronaut Bean

```groovy
package hello.world

import jakarta.inject.Singleton

@Singleton
class HelloBean {

}
```

|   | Groovy automatically imports `groovy.lang.Singleton` which can be confusing as it conflicts with `jakarta.inject.Singleton`. Make sure you use `jakarta.inject.Singleton` when declaring a Micronaut singleton bean to avoid surprising behavior. |
|---|---|

We can also create a client - don’t forget Micronaut framework can act as a client or a server!

Create a client

```bash
mn> create-client hello
| Rendered template Client.groovy to destination src/main/groovy/hello/world/HelloClient.groovy
```

Micronaut Client

```groovy
package hello.world

import io.micronaut.http.client.annotation.Client
import io.micronaut.http.annotation.Get
import io.micronaut.http.HttpStatus

@Client("hello")
interface HelloClient {

    @Get
    HttpStatus index()
}
```

Now let’s create a controller:

Create a controller

```bash
mn> create-controller hello
| Rendered template Controller.groovy to destination src/main/groovy/hello/world/HelloController.groovy
| Rendered template ControllerSpec.groovy to destination src/test/groovy/hello/world/HelloControllerSpec.groovy
mn>
```

Micronaut Controller

```groovy
package hello.world

import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Get
import io.micronaut.http.HttpStatus

@Controller("/hello")
class HelloController {

    @Get
    HttpStatus index() {
        return HttpStatus.OK
    }
}
```

As you can see from the output from the CLI, a Spock test was also generated for you which demonstrates how to test the controller:

HelloControllerSpec.groovy

```groovy
...
    void "test index"() {
        given:
        HttpResponse response = client.toBlocking().exchange("/hello")

        expect:
        response.status == HttpStatus.OK
    }
...
```

Notice how you use the Micronaut framework both as client and as a server to test itself.


## Programmatic Routes with GroovyRouterBuilder

If you prefer to build your routes programmatically (similar to Grails `UrlMappings`), a special `io.micronaut.web.router.GroovyRouteBuilder` exists that has some enhancements to make the DSL better.

The following example shows `GroovyRouteBuilder` in action:

Using GroovyRouteBuilder

```groovy
@Singleton
static class MyRoutes extends GroovyRouteBuilder {

    MyRoutes(ApplicationContext beanContext) {
        super(beanContext)
    }

    @Inject
    void bookResources(BookController bookController, AuthorController authorController) {
        GET(bookController) {
            POST("/hello{/message}", bookController.&hello) (1)
        }
        GET(bookController, ID) { (2)
            GET(authorController)
        }
    }
}
```

| **1** | You can use injected controllers to create routes by convention and Groovy method references to create routes to methods |
|---|---|
| **2** | The `ID` property can be used to reference to include an `{id}` URI variable |

The above example results in the following routes:

- `/book` - Maps to `BookController.index()`
- `/book/hello/{message}` - Maps to `BookController.hello(String)`
- `/book/{id}` - Maps to `BookController.show(String id)`
- `/book/{id}/author` - Maps to `AuthorController.index`


## Serverless Functions with Groovy

A microservice application is just one way to use Micronaut. You can also use it for serverless functions like on AWS Lambda.

With the `function-groovy` module, the Micronaut framework features enhanced support for functions written in Groovy.

See the section on Serverless Functions for more information.


## 16.3 Micronaut for Kotlin

|   | The Command Line Interface for Micronaut framework includes special support for Kotlin. To create a Kotlin application use the `kotlin` lang option. For example: |
|---|---|

Create a Micronaut Kotlin application

```bash
$ mn create-app hello-world --lang kotlin
```

Since the 4.0 release, Micronaut framework offers support for Kotlin via Kapt or Kotlin Symbol Processing API.


## 16.3.1 Kotlin support via KAPT or KSP

Micronaut framework has offered support for Kotlin via Kapt.

With version 4.0, Micronaut framework supports Kotlin also via Kotlin Symbol Processing (KSP) API.

Please note that KAPT is in maintenance mode. Micronaut framework 4 includes experimental support for KSP which Kotlin users should consider migrating in the future.

> kapt is in maintenance mode. We are keeping it up-to-date with recent Kotlin and Java releases but have no plans to implement new features.

KAPT supports existing Java annotation processors by generating Java stubs and feeding them into the Java annotation processors.

By skipping the generation of stubs, KSP offers several advantages:

- Faster compilation.
- Better support Kotlin native syntax.

|   | If you use other annotation processors besides the Micronaut annotation processors, they will not work with KSP. |
|---|---|


## 16.3.2 Kotlin Annotation Processing (KAPT)

The Kapt compiler plugin includes support for Java annotation processors. To use Kotlin in your Micronaut application, add the proper dependencies to configure and run kapt on your `kt` source files. Kapt creates Java "stub" classes for your Kotlin classes, which can then be processed by Micronaut’s Java annotation processor. The stubs are not included in the final compiled application.

|   | Learn more about kapt and its features from the official documentation. |
|---|---|

The Micronaut annotation processors are declared in the `kapt` scope when using Gradle. For example:

Example build.gradle

```groovy
dependencies {
    compile "org.jetbrains.kotlin:kotlin-stdlib-jdk8:$kotlinVersion" (1)
    compile "org.jetbrains.kotlin:kotlin-reflect:$kotlinVersion"
    kapt "io.micronaut:micronaut-inject-java" (2)
    kaptTest "io.micronaut:micronaut-inject-java" (3)
    ...
}
```

| **1** | Add the Kotlin standard libraries |
|---|---|
| **2** | Add the `micronaut-inject-java` dependency under the `kapt` scope, so classes in `src/main` are processed |
| **3** | Add the `micronaut-inject-java` dependency under the `kaptTest` scope, so classes in `src/test` are processed. |

With a `build.gradle` file similar to the above, you can now run your Micronaut application using the `run` task (provided by the Application plugin):

```bash
$ ./gradlew run
```


## 16.3.3 Kotlin Symbol Processing (KSP)

You can build Micronaut applications with Kotlin and KSP:

> Kotlin Symbol Processing (KSP) is an API that you can use to develop lightweight compiler plugins. KSP provides a simplified compiler plugin API that leverages the power of Kotlin while keeping the learning curve at a minimum. Compared to kapt, annotation processors that use KSP can run up to 2 times faster.

If you use the Micronaut Gradle Plugin, you can build Micronaut applications with Kotlin and KSP. You need to apply the `com.google.devtools.ksp` Gradle plugin.

build.gradle.kts

```kotlin
plugins {
    id("org.jetbrains.kotlin.jvm") version "1.9.20"
    id("com.google.devtools.ksp") version "1.9.20-1.0.13"
    id("org.jetbrains.kotlin.plugin.allopen") version "1.9.20"
    id("io.micronaut.application") version "4.4.4" // get latest version from https://plugins.gradle.org/plugin/io.micronaut.application
}
version = "0.1"
group = "example.micronaut"
repositories {
    mavenCentral()
}
dependencies {
    runtimeOnly("ch.qos.logback:logback-classic")
    runtimeOnly("org.yaml:snakeyaml")
    implementation("io.micronaut:micronaut-jackson-databind")
    testImplementation("io.micronaut:micronaut-http-client")
}
application {
    mainClass.set("example.micronaut.Application")
}
graalvmNative.toolchainDetection.set(false)
micronaut {
    runtime("netty")
    testRuntime("junit5")
    processing {
        incremental(true)
        annotations("example.micronaut.*")
    }
}
```

If you don’t use the Micronaut Gradle Plugin, in addition to applying the `com.google.devtools.ksp` Gradle plugin, you have to add `micronaut-inject-kotlin` with the `ksp` configuration.

```kotlin
ksp(platform("io.micronaut.platform:micronaut-platform:$micronautVersion"))
ksp("io.micronaut:micronaut-inject-kotlin")
kspTest(platform("io.micronaut.platform:micronaut-platform:$micronautVersion"))
kspTest("io.micronaut:micronaut-inject-kotlin")
```

Unfortunately, KSP doesn’t see the changes in the classes made by other compiler plugins, which breaks integration with the `allopen` plugin. To make the integration work, we have introduced an experimental KSP property `kotlin.allopen.annotations` for the annotation processor. The property expects a list of annotations that are open, separated by `|`. It’s also supported to use the system property of the same name, but that might be unreliable considering build daemons can be cached.

Kotlin All-Open plugin configuration

```groovy
allOpen {
    annotations("io.micronaut.docs.aop.around.OpenSingleton", "io.micronaut.docs.aop.around.AnotherOpenSingleton")
}
```

KSP configuration - repeat all the annotations that are included in Kotlin All-Open configuration

```groovy
ksp {
    arg("kotlin.allopen.annotations", "io.micronaut.docs.aop.around.OpenSingleton|io.micronaut.docs.aop.around.AnotherOpenSingleton")
}
```

|   | Kotlin All-Open plugin supports only class level annotations - it’s not possible to open a class just by a method annotation |
|---|---|


## 16.3.4 Controller in Kotlin

An example controller written in Kotlin can be seen below:

src/main/kotlin/example/HelloController.kt

```kotlin
package example

import io.micronaut.http.annotation.*

@Controller("/")
class HelloController {

    @Get("/hello/{name}")
    fun hello(name: String): String {
        return "Hello $name"
    }
}
```


## 16.3.5 Kotlin, Kapt and IntelliJ

As of this writing, IntelliJ’s built-in compiler does not directly support Kapt and annotation processing. You must instead configure Intellij to run Gradle (or Maven) compilation as a build step before running your tests or application class.

First, edit the run configuration for tests or for the application and select "Run Gradle task" as a build step:

Then add the `classes` task as task to execute for the application or for tests the `testClasses` task:

Now when you run tests or start the application, the Micronaut framework will generate classes at compile time.

Alternatively, you can delegate IntelliJ build/run actions to Gradle completely:


## 16.3.6 Incremental Annotation Processing with Gradle and Kapt

To enable Gradle incremental annotation processing with Kapt, the arguments as specified in Incremental Annotation Processing with Gradle must be sent to Kapt.

The following example demonstrates how to enable and configure incremental annotation processing for annotations you have defined under the `com.example` and `io.example` packages:

Enabling Incremental Annotation Processing in Kapt

```kotlin
kapt {
    arguments {
        arg("micronaut.processing.incremental", true)
        arg("micronaut.processing.annotations", "com.example.*,io.example.*")
    }
}
```

|   | If you do not enable processing for your custom annotations, they will be ignored by Micronaut, which may break your application. |
|---|---|


## 16.3.7 Kotlin and AOP Advice

The Micronaut framework provides a compile-time AOP API that does not use reflection. When you use any Micronaut AOP Advice, it creates a subclass at compile-time to provide the AOP behaviour. This can be a problem because Kotlin classes are final by default. If the application was created with the Micronaut CLI, the Kotlin all-open plugin is configured for you to automatically change your classes to `open` when an AOP annotation is used. To configure it yourself, add the Around class to the list of supported annotations.

If you prefer not to or cannot use the `all-open` plugin, you must declare the classes that are annotated with an AOP annotation to be open:

```java
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Get
import io.micronaut.http.HttpStatus
import io.micronaut.validation.Validated
import jakarta.validation.constraints.NotBlank

@Validated
@Controller("/email")
open class EmailController { (1)

    @Get("/send")
    fun index(@NotBlank recipient: String, (1)
              @NotBlank subject: String): HttpStatus {
        return HttpStatus.OK
    }
}
```

| **1** | if you use `@Validated` AOP Advice, you need to use `open` at class and method level. |
|---|---|

|   | The `all-open` plugin does not handle methods. If you declare an AOP annotation on a method, you must manually declare it as open. |
|---|---|


## 16.3.8 Kotlin and Retaining Parameter Names

Like with Java, the parameter name data for method parameters is not retained at compile time when using Kotlin. This can be a problem for the Micronaut framework if you do not define parameter names explicitly and depend on an external JAR that is already compiled.

To enable retention of parameter name data with Kotlin, set the `javaParameters` option to `true` in your `build.gradle`:

configuration in Gradle

```groovy
compileTestKotlin {
    kotlinOptions {
        javaParameters = true
    }
}
```

|   | If you use interfaces with default methods add `freeCompilerArgs = ["-Xjvm-default=all"]` for the Micronaut framework to recognize them. |
|---|---|

Or if using Maven configure the Micronaut Maven Plugin accordingly:

configuration in Maven

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <!-- ... -->
  <build>
    <plugins>
      <!-- ... -->
      <plugin>
        <artifactId>kotlin-maven-plugin</artifactId>
        <groupId>org.jetbrains.kotlin</groupId>
        <configuration>
            <javaParameters>true</javaParameters>
            <!-- ... -->
        </configuration>
        <!-- ... -->
      </plugin>
      <!-- ... -->
    </plugins>
  </build>
</project>
```


## 16.3.9 Coroutines Support

Kotlin coroutines allow you to create asynchronous applications with imperative style code. A Micronaut controller action can be a `suspend` function:

Controller suspend function example

```kotlin
@Get("/simple", produces = [MediaType.TEXT_PLAIN])
suspend fun simple(): String { (1)
    return "Hello"
}
```

| **1** | The function is marked as `suspend`, though in reality it won’t be suspended. |
|---|---|

| **1** | The function is marked as `suspend`. |
|---|---|
| **2** | The `delay` is called to make sure that a function is suspended and the response is returned from a different thread. |

Controller suspend function example

```kotlin
@Status(HttpStatus.CREATED) (1)
@Get("/status")
suspend fun status() {
}
```

| **1** | `suspend` function also works when all we want is to return a status. |
|---|---|

Controller suspend function example

```kotlin
@Status(HttpStatus.CREATED)
@Get("/statusDelayed")
suspend fun statusDelayed() {
    delay(1)
}
```

You can also use `Flow` type for streaming server and client. A streaming controller can return `Flow`, for example:

Streaming JSON on the Server with Flow

```kotlin
@Get(value = "/headlinesWithFlow", processes = [MediaType.APPLICATION_JSON_STREAM])
internal fun streamHeadlinesWithFlow(): Flow<Headline> = (1)
    flow { (2)
        repeat(100) { (3)
            with (Headline()) {
                text = "Latest Headline at ${ZonedDateTime.now()}"
                emit(this) (4)
                delay(1_000) (5)
            }
        }
    }
```

| **1** | A method `streamHeadlinesWithFlow` is defined that produces `application/x-json-stream` |
|---|---|
| **2** | A `Flow` is created using `flow` |
| **3** | This `Flow` emits 100 messages |
| **4** | Emitting happens with `emit` `suspend` function |
| **5** | There is a one second *delay* between messages |

A streaming client can simply return a `Flow`, for example:

Streaming client with Flow

```kotlin
import io.micronaut.http.MediaType
import io.micronaut.http.annotation.Get
import io.micronaut.http.client.annotation.Client
import kotlinx.coroutines.flow.Flow
@Client("/streaming")
interface HeadlineFlowClient {
```

| **1** | The `@Get` method is defined as processing responses of type `APPLICATION_JSON_STREAM` |
|---|---|
| **2** | The return type is `Flow` |


## 16.3.10 Coroutine Tracing Context Propagation

The Micronaut framework supports tracing context propagation. If you use `suspend` functions all the way from your controller actions down to all your services, you don’t have to do anything special. However, when you create coroutines within a regular function, tracing propagation won’t happen automatically. You have to use a `HttpCoroutineContextFactory<CoroutineTracingDispatcher>` to create a new `CoroutineTracingDispatcher` and use it as a `CoroutineContext`.

Following example shows how this might look like:

```kotlin
@Controller
class SimpleController(
    private val coroutineTracingDispatcherFactory: HttpCoroutineContextFactory<CoroutineTracingDispatcher>
) {
    @Get("/runParallelly")
    fun runParallelly(): String = runBlocking {
        val a = async(Dispatchers.Default + coroutineTracingDispatcherFactory.create()) {
            val traceId = MDC.get("traceId")
            println("$traceId: Calculating sth...")
            calculateSth()
        }
        val b = async(Dispatchers.Default + coroutineTracingDispatcherFactory.create()) {
            val traceId = MDC.get("traceId")
            println("$traceId: Calculating sth else...")
            calculateSthElse()
        }

        a.await() + b.await()
    }
}
```
