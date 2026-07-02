---
title: "Micronaut Core (part 25/27)"
source: https://docs.micronaut.io/latest/guide/index.html
domain: micronaut
license: CC-BY-SA-4.0
tags: micronaut framework, micronaut jvm, compile-time injection, microservices framework
fetched: 2026-07-02
part: 25/27
---

## 17.2.3.5 Health Monitor Task

A continuous health monitor that updates the CurrentHealthStatus in a background thread can be enabled when using EmbeddedServer with the following application configuration:

```properties
micronaut.application.name=foo
micronaut.health.monitor.enabled=true
```

```yaml
micronaut:
  application:
    name: foo
  health:
    monitor:
      enabled: true
```

```toml
[micronaut]
  [micronaut.application]
    name="foo"
  [micronaut.health]
    [micronaut.health.monitor]
      enabled=true
```

```groovy
micronaut {
  application {
    name = "foo"
  }
  health {
    monitor {
      enabled = true
    }
  }
}
```

```hocon
{
  micronaut {
    application {
      name = "foo"
    }
    health {
      monitor {
        enabled = true
      }
    }
  }
}
```

```json
{
  "micronaut": {
    "application": {
      "name": "foo"
    },
    "health": {
      "monitor": {
        "enabled": true
      }
    }
  }
}
```

- Both configuration properties are required to enable the monitor background task.

Similarly to `DefaultHealthAggregator` it also emits log statements for health indicator status and details. To log this use the following logger configuration:

```xml
<logger name="io.micronaut.management.health.monitor.HealthMonitorTask" level="trace" />
```


## 17.2.3.6 Provided Indicators

All the Micronaut framework provided health indicators are exposed on `/health` and `/health/readiness` endpoints.

| Indicator | Configuration Toggle | Default Value |
|---|---|---|
| `DeadlockedThreadsHealthIndicator` Checks for deadlocked threads. | `endpoints.health.deadlocked-threads.enabled` | `true` |
| `DiscoveryClientHealthIndicator` | `endpoints.health.discovery-client-health.enabled` | `true` |
| `DiskSpaceIndicator` Checks if the server’s disk space is less than the configured threshold | `endpoints.health.disk-space.enabled` | `true` |
| `JdbcIndicator` Checks if the JDBC connection is valid | `endpoints.health.jdbc.enabled` | `true` |
| `ServiceHttpClientHealthIndicator` Check if there are available URLs in the load balancer. | `endpoints.health.service-http-client.enabled` | `false` |
| `ServiceReadyHealthIndicator` - Signals when the service is ready to service requests. | `endpoints.health.service-ready-indicator-enabled` | `true` |


## 17.2.3.6.1 Disk Space Health Indicator

A health indicator is provided that determines the health of the application based on the amount of free disk space. Configuration for the disk space health indicator can be provided under the `endpoints.health.disk-space` key.

Disk Space Indicator Configuration Example

```properties
endpoints.health.disk-space.enabled=Boolean
endpoints.health.disk-space.path=String
endpoints.health.disk-space.threshold=String | Long
```

```yaml
endpoints:
  health:
    disk-space:
      enabled: Boolean
      path: String
      threshold: String | Long
```

```toml
[endpoints]
  [endpoints.health]
    [endpoints.health.disk-space]
      enabled="Boolean"
      path="String"
      threshold="String | Long"
```

```groovy
endpoints {
  health {
    diskSpace {
      enabled = "Boolean"
      path = "String"
      threshold = "String | Long"
    }
  }
}
```

```hocon
{
  endpoints {
    health {
      disk-space {
        enabled = "Boolean"
        path = "String"
        threshold = "String | Long"
      }
    }
  }
}
```

```json
{
  "endpoints": {
    "health": {
      "disk-space": {
        "enabled": "Boolean",
        "path": "String",
        "threshold": "String | Long"
      }
    }
  }
}
```

- `path` specifies the path used to determine the disk space
- `threshold` specifies the minimum amount of free space

The threshold can be provided as a string like "10MB" or "200KB", or the number of bytes.


## 17.2.3.6.2 JDBC Health Indicator

The JDBC health indicator determines the health of your application based on the ability to successfully create connections to datasources in the application context. The only configuration option supported is to enable or disable the indicator by the `endpoints.health.jdbc.enabled` key.


## 17.2.3.6.3 Deadlocked Threads

The deadlocked threads health indicator uses the ThreadMXBean to check for deadlocked threads and is part of the `/health` and `/health/liveness` endpoints.

Its only configuration option is to enable or disable the indicator by the `endpoints.health.deadlocked-thread.enabled` key. It is enabled by default.

|   | `ThreadMXBean` is not supported in GraalVM Native Image |
|---|---|

The health status is set to DOWN if any deadlocked threads are found and their ThreadInfo including a formatted stacktrace are given in the details. See below for an example.

```json
{
    "name": "example-app",
    "status": "DOWN",
    "details": {
        "deadlockedThreads": {
            "name": "example-app",
            "status": "DOWN",
            "details": [
                {
                    "threadId": "60",
                    "threadName": "Thread-0",
                    "threadState": "BLOCKED",
                    "daemon": "false",
                    "priority": "5",
                    "suspended": "false",
                    "inNative": "false",
                    "lockName": "java.lang.Object@7d10b1ca",
                    "lockOwnerName": "Thread-1",
                    "lockOwnerId": "61",
                    "lockedSynchronizers": [],
                    "stackTrace": "app//com.example.Deadlock.lambda$new$0(Deadlock.java:27)\n-  blocked on java.lang.Object@7d10b1ca\n-  locked java.lang.Object@4505ea74\napp//com.example.Deadlock$$Lambda/0x000001906948b360.run(Unknown Source)\njava.base@21/java.lang.Thread.runWith(Thread.java:1596)\njava.base@21/java.lang.Thread.run(Thread.java:1583)\n"
                },
                {
                    "threadId": "61",
                    "threadName": "Thread-1",
                    "threadState": "BLOCKED",
                    "daemon": "false",
                    "priority": "5",
                    "suspended": "false",
                    "inNative": "false",
                    "lockName": "java.lang.Object@4505ea74",
                    "lockOwnerName": "Thread-0",
                    "lockOwnerId": "60",
                    "lockedSynchronizers": [],
                    "stackTrace": "app//com.example.Deadlock.lambda$new$1(Deadlock.java:43)\n-  blocked on java.lang.Object@4505ea74\n-  locked java.lang.Object@7d10b1ca\napp//com.example.Deadlock$$Lambda/0x000001906948b580.run(Unknown Source)\njava.base@21/java.lang.Thread.runWith(Thread.java:1596)\njava.base@21/java.lang.Thread.run(Thread.java:1583)\n"
                }
            ]
        }
    }
}
```


## 17.2.4 The Metrics Endpoint

The Micronaut framework can expose application metrics via integration with Micrometer.

|   | Using the CLI If you create your project using the Micronaut CLI, supply one of the micrometer features to enable metrics and preconfigure the selected registry in your project. For example: $ mn create-app my-app --features micrometer-atlas |
|---|---|

The metrics endpoint returns information about the "metrics" of the application. To execute the metrics endpoint, send a GET request to `/metrics`. This returns a list of available metric names.

You can get specific metrics by using `/metrics/[name]` such as `/metrics/jvm.memory.used`.

See the documentation for Micronaut Micrometer for a list of registries and information on how to configure, expose and customize metrics output.


## 17.2.5 The Refresh Endpoint

The refresh endpoint refreshes the application state, causing all Refreshable beans in the context to be destroyed and reinstantiated upon further requests. This is accomplished by publishing a RefreshEvent in the Application Context.

To execute the refresh endpoint, send a POST request to /refresh.

```bash
$ curl -X POST http://localhost:8080/refresh
```

When executed without a body, the endpoint first refreshes the Environment and performs a diff to detect any changes, and then only performs the refresh if changes are detected. To skip this check and refresh all `@Refreshable` beans regardless of environment changes (e.g., to force refresh of cached responses from third-party services), add a `force` parameter in the POST request body.

```bash
$ curl -X POST http://localhost:8080/refresh -H 'Content-Type: application/json' -d '{"force": true}'
```


## Configuration

To configure the refresh endpoint, supply configuration through `endpoints.refresh`.

Beans Endpoint Configuration Example

```properties
endpoints.refresh.enabled=Boolean
endpoints.refresh.sensitive=Boolean
```

```yaml
endpoints:
  refresh:
    enabled: Boolean
    sensitive: Boolean
```

```toml
[endpoints]
  [endpoints.refresh]
    enabled="Boolean"
    sensitive="Boolean"
```

```groovy
endpoints {
  refresh {
    enabled = "Boolean"
    sensitive = "Boolean"
  }
}
```

```hocon
{
  endpoints {
    refresh {
      enabled = "Boolean"
      sensitive = "Boolean"
    }
  }
}
```

```json
{
  "endpoints": {
    "refresh": {
      "enabled": "Boolean",
      "sensitive": "Boolean"
    }
  }
}
```


## 17.2.6 The Routes Endpoint

The routes endpoint returns information about URIs available to be called for your application. By default, the data returned includes the URI, allowed method, content types produced, and information about the method that would be executed.

To execute the routes endpoint, send a GET request to /routes.


## Configuration

To configure the routes endpoint, supply configuration through `endpoints.routes`.

Routes Endpoint Configuration Example

```properties
endpoints.routes.enabled=Boolean
endpoints.routes.sensitive=Boolean
```

```yaml
endpoints:
  routes:
    enabled: Boolean
    sensitive: Boolean
```

```toml
[endpoints]
  [endpoints.routes]
    enabled="Boolean"
    sensitive="Boolean"
```

```groovy
endpoints {
  routes {
    enabled = "Boolean"
    sensitive = "Boolean"
  }
}
```

```hocon
{
  endpoints {
    routes {
      enabled = "Boolean"
      sensitive = "Boolean"
    }
  }
}
```

```json
{
  "endpoints": {
    "routes": {
      "enabled": "Boolean",
      "sensitive": "Boolean"
    }
  }
}
```


## Customization

The routes endpoint is composed of a route data collector and a route data implementation. The route data collector (RouteDataCollector) is responsible for returning a publisher that returns the data used in the response. The route data (RouteData) is responsible for returning data about an individual route.

To override the default behavior for either of the helper classes, either extend the default implementations (DefaultRouteDataCollector, DefaultRouteData), or implement the relevant interface directly. To ensure your implementation is used instead of the default, add the @Replaces annotation to your class with the value being the default implementation.


## 17.2.7 The Loggers Endpoint

The loggers endpoint returns information about the available loggers in the application and permits configuring their log level.

|   | The loggers endpoint is disabled by default and must be explicitly enabled with the setting `endpoints.loggers.enabled=true`. |
|---|---|

To get a collection of all loggers by name with their configured and effective log levels, send a GET request to /loggers. This also provides a list of the available log levels.

```bash
$ curl http://localhost:8080/loggers

{
    "levels": [
        "ALL", "TRACE", "DEBUG", "INFO", "WARN", "ERROR", "OFF", "NOT_SPECIFIED"
    ],
    "loggers": {
        "ROOT": {
            "configuredLevel": "INFO",
            "effectiveLevel": "INFO"
        },
        "io": {
            "configuredLevel": "NOT_SPECIFIED",
            "effectiveLevel": "INFO"
        },
        "io.micronaut": {
            "configuredLevel": "NOT_SPECIFIED",
            "effectiveLevel": "INFO"
        },
        // etc...
    }
}
```

To get the log levels of a particular logger, include the logger name in your GET request. For example, to access the log levels of the logger 'io.micronaut.http':

```bash
$ curl http://localhost:8080/loggers/io.micronaut.http

{
    "configuredLevel": "NOT_SPECIFIED",
    "effectiveLevel": "INFO"
}
```

If the named logger does not exist, it is created with an unspecified (i.e. `NOT_SPECIFIED`) configured log level (its effective log level is usually that of the root logger).

To update the log level of a single logger, send a POST request to the named logger URL and include a body providing the log level to configure.

```bash
$ curl -i -X POST \
       -H "Content-Type: application/json" \
       -d '{ "configuredLevel": "ERROR" }' \
       http://localhost:8080/loggers/ROOT

HTTP/1.1 200 OK

$ curl http://localhost:8080/loggers/ROOT

{
    "configuredLevel": "ERROR",
    "effectiveLevel": "ERROR"
}
```


## Configuration

To configure the loggers endpoint, supply configuration through `endpoints.loggers`.

Loggers Endpoint Configuration Example

```properties
endpoints.loggers.enabled=Boolean
endpoints.loggers.sensitive=Boolean
```

```yaml
endpoints:
  loggers:
    enabled: Boolean
    sensitive: Boolean
```

```toml
[endpoints]
  [endpoints.loggers]
    enabled="Boolean"
    sensitive="Boolean"
```

```groovy
endpoints {
  loggers {
    enabled = "Boolean"
    sensitive = "Boolean"
  }
}
```

```hocon
{
  endpoints {
    loggers {
      enabled = "Boolean"
      sensitive = "Boolean"
    }
  }
}
```

```json
{
  "endpoints": {
    "loggers": {
      "enabled": "Boolean",
      "sensitive": "Boolean"
    }
  }
}
```

|   | By default, the endpoint doesn’t allow changing the log level by unauthorized users (even if `sensitive` is set to `false`). To allow this you must set `endpoints.loggers.write-sensitive` to `false`. |
|---|---|


## Customization

The loggers endpoint is composed of two customizable parts: a LoggersManager and a LoggingSystem. See the logging section of the documentation for information on customizing the logging system.

The LoggersManager is responsible for retrieving and setting log levels. If the default implementation is not sufficient for your use case, simply provide your own implementation and replace the DefaultLoggersManager with the @Replaces annotation.


## 17.2.8 The Caches Endpoint

The caches endpoint documentation is available at the micronaut-cache project.


## 17.2.9 The Server Stop Endpoint

The stop endpoint shuts down the application server.

To execute the stop endpoint, send a POST request to /stop.


## Configuration

To configure the stop endpoint, supply configuration through `endpoints.stop`.

Stop Endpoint Configuration Example

```properties
endpoints.stop.enabled=Boolean
endpoints.stop.sensitive=Boolean
```

```yaml
endpoints:
  stop:
    enabled: Boolean
    sensitive: Boolean
```

```toml
[endpoints]
  [endpoints.stop]
    enabled="Boolean"
    sensitive="Boolean"
```

```groovy
endpoints {
  stop {
    enabled = "Boolean"
    sensitive = "Boolean"
  }
}
```

```hocon
{
  endpoints {
    stop {
      enabled = "Boolean"
      sensitive = "Boolean"
    }
  }
}
```

```json
{
  "endpoints": {
    "stop": {
      "enabled": "Boolean",
      "sensitive": "Boolean"
    }
  }
}
```

|   | By default, the stop endpoint is disabled and must be explicitly enabled to be used. |
|---|---|


## 17.2.10 The Environment Endpoint

The environment endpoint returns information about the Environment and its PropertySources.


## Configuration

To enable and configure the environment endpoint, supply configuration through `endpoints.env`.

Environment Endpoint Configuration Example

```properties
endpoints.env.enabled=Boolean
endpoints.env.sensitive=Boolean
endpoints.env.active-keys=List<String>
```

```yaml
endpoints:
  env:
    enabled: Boolean
    sensitive: Boolean
    active-keys: List<String>
```

```toml
[endpoints]
  [endpoints.env]
    enabled="Boolean"
    sensitive="Boolean"
    active-keys="List<String>"
```

```groovy
endpoints {
  env {
    enabled = "Boolean"
    sensitive = "Boolean"
    activeKeys = "List<String>"
  }
}
```

```hocon
{
  endpoints {
    env {
      enabled = "Boolean"
      sensitive = "Boolean"
      active-keys = "List<String>"
    }
  }
}
```

```json
{
  "endpoints": {
    "env": {
      "enabled": "Boolean",
      "sensitive": "Boolean",
      "active-keys": "List<String>"
    }
  }
}
```

- defaults are false for `enabled` and true for `sensitive`
- `active-keys` defaults to ["activeEnvironments", "packages", "propertySources"]

The `active-keys` property allows you to customize which sections of the environment information are displayed. You can specify one or more of the following values:

- `activeEnvironments`
- `packages`
- `propertySources`

For example, to only show active environments and packages:

```properties
endpoints.env.active-keys[0]=activeEnvironments
endpoints.env.active-keys[1]=packages
```

```yaml
endpoints:
  env:
    active-keys:
      - activeEnvironments
      - packages
```

```toml
[endpoints]
  [endpoints.env]
    active-keys=[
      "activeEnvironments",
      "packages"
    ]
```

```groovy
endpoints {
  env {
    activeKeys = ["activeEnvironments", "packages"]
  }
}
```

```hocon
{
  endpoints {
    env {
      active-keys = ["activeEnvironments", "packages"]
    }
  }
}
```

```json
{
  "endpoints": {
    "env": {
      "active-keys": ["activeEnvironments", "packages"]
    }
  }
}
```

If you provide an empty list, no sections will be displayed.


## Masking sensitive information

By default, the endpoint will mask all values. To customize this masking you need to supply a Bean that implements EnvironmentEndpointFilter.

This first example will mask all values except for those that are prefixed by `safe`

First example of environment masking

```java
@Singleton
public class OnlySafePrefixedEnvFilter implements EnvironmentEndpointFilter {
    private static final Pattern SAFE_PREFIX_PATTERN = Pattern.compile("safe.*", Pattern.CASE_INSENSITIVE);

    @Override
    public void specifyFiltering(@NotNull EnvironmentFilterSpecification specification) {
        specification
                .maskAll() // All values will be masked apart from the supplied patterns
                .exclude(SAFE_PREFIX_PATTERN);
    }
}
```

It is also possible to allow all values in plain text using maskNone--, and then specify name patterns that will be masked, ie:

Deny instead of allow

```java
@Singleton
public class AllPlainExceptSecretOrMatchEnvFilter implements EnvironmentEndpointFilter {
    // Mask anything starting with `sekrt`
    private static final Pattern SECRET_PREFIX_PATTERN = Pattern.compile("sekrt.*", Pattern.CASE_INSENSITIVE);

    // Mask anything exactly matching `exact-match`
    private static final String EXACT_MATCH = "exact-match";

    // Mask anything that starts with `private.`
    private static final Predicate<String> PREDICATE_MATCH = name -> name.startsWith("private.");

    @Override
    public void specifyFiltering(@NotNull EnvironmentFilterSpecification specification) {
        specification
                .maskNone() // All values will be in plain-text apart from the supplied patterns
                .exclude(SECRET_PREFIX_PATTERN)
                .exclude(EXACT_MATCH)
                .exclude(PREDICATE_MATCH);
    }
}
```

Sensible defaults can be applied by calling the legacyMasking-- method. This will show all values apart from those that contain the words `password`, `credential`, `certificate`, `key`, `secret` or `token` anywhere in their name.


## Getting information about the environment

To execute the endpoint, send a `GET` request to `/env`.


## Getting information about a particular `PropertySource`

To execute the endpoint, send a `GET` request to `/env/{propertySourceName}`.


## 17.2.11 The ThreadDump Endpoint

The threaddump endpoint returns information about the threads running in your application.

To execute the threaddump endpoint, send a GET request to /threaddump.


## Configuration

To configure the threaddump endpoint, supply configuration through `endpoints.threaddump`.

Threaddump Endpoint Configuration Example

```properties
endpoints.threaddump.enabled=Boolean
endpoints.threaddump.sensitive=Boolean
```

```yaml
endpoints:
  threaddump:
    enabled: Boolean
    sensitive: Boolean
```

```toml
[endpoints]
  [endpoints.threaddump]
    enabled="Boolean"
    sensitive="Boolean"
```

```groovy
endpoints {
  threaddump {
    enabled = "Boolean"
    sensitive = "Boolean"
  }
}
```

```hocon
{
  endpoints {
    threaddump {
      enabled = "Boolean"
      sensitive = "Boolean"
    }
  }
}
```

```json
{
  "endpoints": {
    "threaddump": {
      "enabled": "Boolean",
      "sensitive": "Boolean"
    }
  }
}
```


## Customization

The thread dump endpoint delegates to a ThreadInfoMapper) that is responsible for transforming the `java.lang.management.ThreadInfo` objects into any other to be sent for serialization.

# 18 Security

The Micronaut framework has a full-featured security solution for all common security patterns.

See the documentation for Micronaut Security for more information on how to secure your applications.

# 19 Multi-Tenancy

See the Micronaut Multitenancy documentation to learn about Micronaut’s support for common tasks such as tenant resolution for multi-tenancy-aware Micronaut applications.

# 20 Micronaut CLI

The Micronaut CLI is the recommended way to create new Micronaut projects. The CLI includes commands for generating specific categories of projects, allowing you to choose between build tools, test frameworks, and even pick the language to use in your application. The CLI also provides commands for generating artifacts such as controllers, client interfaces, and serverless functions.

|   | We have a website that can be used to generate projects instead of the CLI. Check out Micronaut Launch to get started! |
|---|---|

When Micronaut framework is installed on your computer, you can call the CLI with the `mn` command.

```bash
$ mn create-app my-app
```

A Micronaut framework CLI project can be identified by the `micronaut-cli.yml` file, which is included at the project root if it was generated via the CLI. This file will include the project’s profile, default package, and other variables. The project’s default package is evaluated based on the project name.

```bash
$ mn create-app my-demo-app
```

results in the default package being `my.demo.app`.

You can supply your own default package when creating the application by prefixing the application name with the package:

```bash
$ mn create-app example.my-demo-app
```

results in the default package being `example`.


## Interactive Mode

If you run `mn` without any arguments, the Micronaut CLI launches in interactive mode. This is a shell-like mode which lets you run multiple CLI commands without re-initializing the CLI runtime, and is especially suitable when you use code-generation commands (such as `create-controller`), create multiple projects, or are just exploring CLI features. Tab-completion is enabled, enabling you to hit the `TAB` key to see possible options for a given command or flag.

```bash
$ mn
| Starting interactive mode...
| Enter a command name to run. Use TAB for completion:
mn>
```


## Help and Info

General usage information can be viewed using the `help` flag on a command.

```bash
mn> create-app -h
Usage: mn create-app [-hivVx] [--list-features] [-b=BUILD-TOOL] [--jdk=<javaVersion>] [-l=LANG]
                     [-t=TEST] [-f=FEATURE[,FEATURE...]]... [NAME]
Creates an application
      [NAME]               The name of the application to create.
  -b, --build=BUILD-TOOL   Which build tool to configure. Possible values: gradle, gradle_kotlin,
                             maven.
  -f, --features=FEATURE[,FEATURE...]
  -h, --help               Show this help message and exit.
  -i, --inplace            Create a service using the current directory
      --jdk, --java-version=<javaVersion>
                           The JDK version the project should target
  -l, --lang=LANG          Which language to use. Possible values: java, groovy, kotlin.
      --list-features      Output the available features and their descriptions
  -t, --test=TEST          Which test framework to use. Possible values: junit, spock, kotest.
```

A list of available features can be viewed using the `--list-features` flag on any of the create commands.

```bash
mn> create-app --list-features
Available Features
(+) denotes the feature is included by default
  Name                             Description
  -------------------------------  ---------------
  Cache
  cache-caffeine                   Adds support for cache using Caffeine (https://github.com/ben-manes/caffeine)
  cache-ehcache                    Adds support for cache using EHCache (https://www.ehcache.org/)
  cache-hazelcast                  Adds support for cache using Hazelcast (https://hazelcast.org/)
  cache-infinispan                 Adds support for cache using Infinispan (https://infinispan.org/)
```


## 20.1 Creating a Project

Creating a project is the primary usage of the CLI. The primary command for creating a new project is `create-app`, which creates a standard server application that communicates over HTTP. For other types of application, see the documentation below.

| Command | Description | Options | Example |
|---|---|---|---|
| `create-app` | Creates a basic Micronaut application. | `-l`, `--lang` `-t`, `--test` `-b`, `--build` `-f`, `--features` `-i`, `--inplace` | `mn create-app my-project --features mongo-reactive,security-jwt --build maven` |
| `create-cli-app` | Creates a command-line Micronaut application. | `-l`, `--lang` `-t`, `--test` `-b`, `--build` `-f`, `--features` `-i`, `--inplace` | `mn create-cli-app my-project --features http-client,jdbc-hikari --build maven --lang kotlin --test kotest` |
| `create-function-app` | Creates a Micronaut serverless function, using AWS by default. | `-l`, `--lang` `-t`, `--test` `-b`, `--build` `-f`, `--features` `-i`, `--inplace` | `mn create-function-app my-lambda-function --lang groovy --test spock` |
| `create-messaging-app` | Creates a Micronaut application that only communicates via a messaging protocol. Uses Kafka by default but can be switched to RabbitMQ with `--features rabbitmq`. | `-l`, `--lang` `-t`, `--test` `-b`, `--build` `-f`, `--features` `-i`, `--inplace` | `mn create-messaging-app my-broker --lang groovy --test spock` |
| `create-grpc-app` | Creates a Micronaut application that uses gRPC. | `-l`, `--lang` `-t`, `--test` `-b`, `--build` `-f`, `--features` `-i`, `--inplace` | `mn create-grpc-app my-grpc-app --lang groovy --test spock` |


## Create Command Flags

The create-* commands generate a basic Micronaut project, with optional flags to specify features, language, test framework, and build tool. All projects except functions include a default `Application` class for starting the application.

| Flag | Description | Example |
|---|---|---|
| `-l`, `--lang` | Language to use for the project (one of `java`, `groovy`, `kotlin` - default is `java`) | `--lang groovy` |
| `-t`, `--test` | Test framework to use for the project (one of `junit`, `spock` - default is `junit`) | `--test spock` |
| `-b`, `--build` | Build tool (one of `gradle`, `gradle_kotlin`, `maven` - default is `gradle` for the languages `java` and `groovy`; default is `gradle_kotlin` for language `kotlin`) | `--build maven` |
| `-f`, `--features` | Features to use for the project, comma-separated | `--features security-jwt,mongo-reactive` or `-f security-jwt -f mongo-reactive` |
| `-i`, `--inplace` | If present, generates the project in the current directory (project name is optional if this flag is set) | `--inplace` |

Once created, the application can be started using the `Application` class, or the appropriate build tool task.

Starting a Gradle project

```bash
$ ./gradlew run
```

Starting a Maven project

```bash
$ ./mvnw mn:run
```

### Language/Test Features

By default, the create commands generate a Java application, with JUnit configured as the test framework. All the options chosen and features applied are stored as properties in the `micronaut-cli.yml` file, as shown below:

micronaut-cli.yml

```yaml
applicationType: default
defaultPackage: com.example
testFramework: junit
sourceLanguage: java
buildTool: gradle
features: [annotation-api, app-name, application, gradle, http-client, java, junit, logback, netty-server, shade, yaml]
```

Some commands rely on the data in this file to determine if they should be executable. For example, the `create-kafka-listener` command requires `kafka` to be one of the features in the list.

|   | The values in `micronaut-cli.yml` are used by the CLI for code generation. After a project is generated, you can edit these values to change the project defaults, however you must supply the required dependencies and/or configuration to use your chosen language/framework. For example, you could change the `testFramework` property to `spock` to cause the CLI to generate Spock tests when running commands (such as `create-controller`), but you need to add the Spock dependency to your build. |
|---|---|

#### Groovy

To create an app with Groovy support (which uses Spock by default), supply the appropriate language via the `lang` flag:

```bash
$ mn create-app my-groovy-app --lang groovy
```

This includes the Groovy and Spock dependencies in your project, and writes the appropriates values in `micronaut-cli.yml`.

#### Kotlin

To create an app with Kotlin support (which uses Kotest by default), supply the appropriate language via the `lang` flag:

```bash
$ mn create-app my-kotlin-app --lang kotlin
```

This includes the Kotlin and Kotest dependencies in your project, and writes the appropriates values in `micronaut-cli.yml`.

### Build Tool

By default, `create-app` creates a Gradle project, with a `build.gradle` file in the project root directory. To create an app using the Maven build tool, supply the appropriate option via the `build` flag:

```bash
$ mn create-app my-maven-app --build maven
```


## Create-Cli-App

The `create-cli-app` command generates a Micronaut command line application project, with optional flags to specify language, test framework, features, profile, and build tool. By default, the project includes the `picocli` feature to support command line option parsing. The project will include a `*Command` class (based on the project name, e.g. `hello-world` generates `HelloWorldCommand`), and an associated test which instantiates the command and verifies that it can parse command line options.

Once created, the application can be started using the `*Command` class, or the appropriate build tool task.

Starting a Gradle project

```bash
$ ./gradlew run
```

Starting a Maven project

```bash
$ ./mvnw mn:run
```


## Create Function App

The `create-function-app` command generates a Micronaut function project, optimized for serverless environments, with optional flags to specify language, test framework, features, and build tool. The project will include a `*Function` class (based on the project name, e.g. `hello-world` generates `HelloWorldFunction`), and an associated test which instantiates the function and verifies that it can receive requests.

|   | Currently, AWS Lambda, Micronaut Azure, and Google Cloud are the supported cloud providers for Micronaut functions. To use other providers, add one in the features: `--features azure-function` or `--features google-cloud-function`. |
|---|---|


## Contribute

The CLI source code is at https://github.com/micronaut-projects/micronaut-starter. Information about how to contribute and other resources are there.


## 20.1.1 Comparing Versions

The easiest way to see version dependency updates and other changes for a new version of Micronaut is to produce one clean application using the older version and another using the newer version of the `mn` CLI, and then comparing those directories.


## 20.2 Features

Features consist of additional dependencies and configuration to enable specific functionality in your application. Micronaut profiles define a large number of features, including features for many of the configurations provided by Micronaut, such as the Data Access Configurations

```bash
$ mn create-app my-demo-app --features mongo-reactive
```

This adds the necessary dependencies and configuration for the MongoDB Reactive Driver in your application. You can view the available features using the `--list-features` flag for whichever create command you use.

```bash
$ mn create-app --list-features # Output will be supported features for the create-app command
$ mn create-function-app --list-features # Output will be supported features for the create-function-app command, different from above.
```


## 20.3 Commands

You can view a full list of available commands using the help flag, for example:

```bash
$ mn -h
Usage: mn [-hvVx] [COMMAND]
Micronaut CLI command line interface for generating projects and services.
Application generation commands are: (1)

*  create-app NAME
*  create-cli-app NAME
*  create-function-app NAME
*  create-grpc-app NAME
*  create-messaging-app NAME

Options:
  -h, --help         Show this help message and exit.
  -v, --verbose      Create verbose output.
  -V, --version      Print version information and exit.
  -x, --stacktrace   Show full stack trace when exceptions occur.

Commands: (2)
  create-app               Creates an application
  create-cli-app           Creates a CLI application
  create-function-app      Creates a Cloud Function
  create-grpc-app          Creates a gRPC application
  create-messaging-app     Creates a messaging application
  create-job               Creates a job with scheduled method
  create-bean              Creates a singleton bean
  create-websocket-client  Creates a Websocket client
  create-client            Creates a client interface
  create-controller        Creates a controller and associated test
  feature-diff             Produces the diff of an original project with an original project with
                             additional features.
  create-websocket-server  Creates a Websocket server
  create-test              Creates a simple test for the project's testing framework
```

| **1** | Here you can see the project generation commands lists |
|---|---|
| **2** | All commands available in the current directory are listed here |
| **3** | **Note:** the things listed after the project creation commands (always available) depend on the current directory context |

All the code-generation commands honor the values written in `micronaut-cli.yml`. For example, assume the following `micronaut-cli.yml` file.

micronaut-cli.yml

```yaml
defaultPackage: example
---
testFramework: spock
sourceLanguage: java
```

With the above settings, the `create-bean` command (by default) generates a Java class with an associated Spock test, in the `example` package. Commands accept arguments and these defaults can be overridden on a per-command basis.


## Base Commands

These commands are always available within the context of a micronaut project.

### Create-Bean

| Flag | Description | Example |
|---|---|---|
| `-l`, `--lang` | The language used for the bean class | `--lang groovy` |
| `-f`, `--force` | Whether to overwrite existing files | `--force` |

The `create-bean` command generates a simple Singleton class. It does not create an associated test.

```bash
$ mn create-bean EmailService
| Rendered template Bean.java to destination src/main/java/example/EmailService.java
```

### Create-Job

| Flag | Description | Example |
|---|---|---|
| `-l`, `--lang` | The language used for the job class | `--lang groovy` |
| `-f`, `--force` | Whether to overwrite existing files | `--force` |

The `create-job` command generates a simple Scheduled class. It follows a `*Job` convention for generating the class name. It does not create an associated test.

```bash
$ mn create-job UpdateFeeds --lang groovy
| Rendered template Job.groovy to destination src/main/groovy/example/UpdateFeedsJob.groovy
```

### Create-Controller

| Flag | Description | Example |
|---|---|---|
| `-l`, `--lang` | The language used for the controller | `--lang groovy` |
| `-f`, `--force` | Whether to overwrite existing files | `--force` |

The `create-controller` command generates a Controller class. It follows a `*Controller` convention for generating the class name. It creates an associated test that runs the application and instantiates an HTTP client, which can make requests against the controller.

```bash
$ mn create-controller Book
| Rendered template Controller.java to destination src/main/java/example/BookController.java
| Rendered template ControllerTest.java to destination src/test/java/example/BookControllerTest.java
```

### Create-Client

| Flag | Description | Example |
|---|---|---|
| `-l`, `--lang` | The language used for the client | `--lang groovy` |
| `-f`, `--force` | Whether to overwrite existing files | `--force` |

The `create-client` command generates a simple Client interface. It follows a `*Client` convention for generating the class name. It does not create an associated test.

```bash
$ mn create-client Book
| Rendered template Client.java to destination src/main/java/example/BookClient.java
```

### Create-Websocket-Server

| Flag | Description | Example |
|---|---|---|
| `-l`, `--lang` | The language used for the server | `--lang groovy` |
| `-f`, `--force` | Whether to overwrite existing files | `--force` |

The `create-websocket-server` command generates a simple ServerWebSocket class. It follows a `*Server` convention for generating the class name. It does not create an associated test.

```bash
$ mn create-websocket-server MyChat
| Rendered template WebsocketServer.java to destination src/main/java/example/MyChatServer.java
```

### Create-Websocket-Client

| Flag | Description | Example |
|---|---|---|
| `-l`, `--lang` | The language used for the client | `--lang groovy` |
| `-f`, `--force` | Whether to overwrite existing files | `--force` |

The `create-websocket-client` command generates a simple WebSocketClient abstract class. It follows a `*Client` convention for generating the class name. It does not create an associated test.

```bash
$ mn create-websocket-client MyChat
| Rendered template WebsocketClient.java to destination src/main/java/example/MyChatClient.java
```


## CLI Project Commands

### Create-Command

| Flag | Description | Example |
|---|---|---|
| `-l`, `--lang` | The language used for the command | `--lang groovy` |
| `-f`, `--force` | Whether to overwrite existing files | `--force` |

The `create-command` command generates a standalone application that can be executed as a picocli Command. It follows a `*Command` convention for generating the class name. It creates an associated test that runs the application and verifies that a command line option was set.

```bash
$ mn create-command print
| Rendered template Command.java to destination src/main/java/example/PrintCommand.java
| Rendered template CommandTest.java to destination src/test/java/example/PrintCommandTest.java
```

This list is just a small subset of the code generation commands in the Micronaut CLI. To see all context-sensitive commands the CLI has available (and under what circumstances they apply), check out the micronaut-starter project and find the classes that extend `CodeGenCommand`. The `applies` method dictates whether a command is available or not.


## 20.4 Reloading

Reloading (or "hot-loading") refers to the framework reinitializing classes (and parts of the application) when changes to the source files are detected.

Since Micronaut prioritizes startup time and most Micronaut apps can start up within seconds, a productive workflow can often be had by restarting the application as changes are made; for example, by running a test class within an IDE.

However, to have your changes automatically reloaded, Micronaut supports automatic restart and the use of third-party reloading agents.


## 20.4.1 Automatic Restart

There are various ways to achieve reloading of classes on the JVM, and all have their advantages and disadvantages. The following are possible ways to achieve reloading without restarting the JVM:

- **JVM Agents** - A JVM agent like JRebel can be used, however these can produce unusual errors, may not support all JDK versions, and can result in cached or stale classes.
- **ClassLoader Reloading** - ClassLoader-based reloading is a popular solution used by most JVM frameworks; however it once again can lead to cached or stale classes, memory leaks, and weird errors if the incorrect classloader is used.
- **Debugger HotSwap** - The Java debugger supports hotswapping of changes at runtime, but only supports a few use cases.

Given the problems with existing solutions and a lack of a way built into the JVM to reload changes, the safest and best solution to reloading, and the one recommended by the Micronaut team, is to use automatic application restart via a third-party tool.

Micronaut’s startup time is fast and automatic restart leads to a clean slate without potential hard to debug problems or memory leaks cropping up.

### Maven Restart

To have automatic application restarts with Maven, use the Micronaut Maven plugin (included by default when creating new Maven projects) and run the following command:

Using the Micronaut Maven Plugin

```bash
$ ./mvnw mn:run
```

Every time you change a class, the plugin automatically restarts the server.

### Gradle Restart

Gradle automatic restart can be activated when using the Micronaut Gradle plugin by activating Gradle’s support for continuous builds via the `-t` flag:

Using Gradle for Automatic Restart

```bash
./gradlew run -t
```

Every time you make a change to class or resources, Gradle recompiles and restarts the application.


## 20.4.2 JRebel

JRebel is a proprietary reloading solution that involves an agent library, as well as sophisticated IDE support. The JRebel documentation includes detailed steps for IDE integration and usage. In this section, we show how to install and configure the agent for Maven and Gradle projects.

|   | Using the CLI If you create your project using the Micronaut CLI, supply the `jrebel` feature to preconfigure JRebel reloading in your project. Note that you need to install JRebel and supply the correct path to the agent in the `gradle.properties` file (for Gradle) or `pom.xml` (for Maven). The necessary steps are described below. $ mn create-app my-app --features jrebel |
|---|---|


## Install/configure JRebel Agent

The simplest way to install JRebel is to download the "standalone" installation package from the JRebel download page. Unzip the downloaded file to a convenient location, for example `~/bin/jrebel`

The installation directory contains a `lib` directory with the agent files. For the appropriate agent based on your operating system, see the table below:

| OS | Agent |
|---|---|
| Windows 64-bit JDK | `[jrebel directory]\lib\jrebel64.dll` |
| Windows 32-bit JDK | `[jrebel directory]\lib\jrebel32.dll` |
| Mac OS X 64-bit JDK | `[jrebel directory]/lib/libjrebel64.dylib` |
| Mac OS X 32-bit JDK | `[jrebel directory]/lib/libjrebel32.dylib` |
| Linux 64-bit JDK | `[jrebel directory]/lib/libjrebel64.so` |
| Linux 32-bit JDK | `[jrebel directory]/lib/libjrebel32.so` |

Note the path to the appropriate agent, and add the value to your project build.

### Gradle

Add the path to `gradle.properties` (create the file if necessary), as the `rebelAgent` property.

gradle.properties

```properties
#Assuming installation path of ~/bin/jrebel/
rebelAgent= -agentpath:~/bin/jrebel/lib/libjrebel64.dylib
```

Add the appropriate JVM arg to `build.gradle` (not necessary if using the CLI feature)

```groovy
run.dependsOn(generateRebel)
if (project.hasProperty('rebelAgent')) {
    run.jvmArgs += rebelAgent
}
```

You can start the application with `./gradlew run`, and it will include the agent. See the section on Gradle Reloading or IDE Reloading to set up the recompilation.

### Maven

Configure the Micronaut Maven Plugin accordingly:

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <!-- ... -->
  <build>
    <plugins>
      <!-- ... -->
      <plugin>
        <groupId>io.micronaut.maven</groupId>
        <artifactId>micronaut-maven-plugin</artifactId>
          <configuration>
            <jvmArguments>-agentpath:~/bin/jrebel/lib/jrebel6/lib/libjrebel64.dylib</jvmArguments>
          </configuration>
      </plugin>
      <plugin>
        <groupId>org.zeroturnaround</groupId>
        <artifactId>jrebel-maven-plugin</artifactId>
        <version>1.1.10</version>
        <executions>
          <execution>
            <id>generate-rebel-xml</id>
            <phase>process-resources</phase>
            <goals>
              <goal>generate</goal>
            </goals>
          </execution>
        </executions>
      </plugin>
      <!-- ... -->
    </plugins>
  </build>
</project>
```


## 20.4.3 Recompiling with Gradle

Gradle supports continuous builds, letting you run a task that will be rerun whenever source files change. To use this with a reloading agent (configured as described above), run the application normally (with the agent), and then run a recompilation task in a separate terminal with continuous mode enabled.

Run the app

```bash
$ ./gradlew run
```

Run the recompilation

```bash
$ ./gradlew -t classes
```

The `classes` task will be rerun every time a source file is modified, allowing the reloading agent to pick up the change.


## 20.4.4 Recompiling with an IDE

If you use a build tool such as Maven which does not support automatic recompilation on file changes, you may use your IDE to recompile classes in combination with a reloading agent (as configured in the above sections).

### IntelliJ

IntelliJ unfortunately does not have an automatic rebuild option that works for a running application. However, you can trigger a "rebuild" of the project with `CMD-F9` (Mac) or `CTRL-F9` (Windows/Linux).

### Eclipse

Under the `Project` menu, check the `Build Automatically` option. This will trigger a recompilation of the project whenever file changes are saved to disk.


## 20.5 Proxy Configuration

To configure the CLI to use an HTTP proxy there are two steps. Configuration options can be passed to the cli through the `MN_OPTS` environment variable.

For example on *nix systems:

```bash
export MN_OPTS="-Dhttps.proxyHost=127.0.0.1 -Dhttps.proxyPort=3128 -Dhttp.proxyUser=test -Dhttp.proxyPassword=test"
```

The profile dependencies are resolved over HTTPS so the proxy port and host are configured with `https.`, however the user and password are specified with `http.`.

For Windows systems the environment variable can be configured under `My Computer/Advanced/Environment Variables`.

# 21 Internationalization
