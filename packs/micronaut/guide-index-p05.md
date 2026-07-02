---
title: "Micronaut Core (part 5/27)"
source: https://docs.micronaut.io/latest/guide/index.html
domain: micronaut
license: CC-BY-SA-4.0
tags: micronaut framework, micronaut jvm, compile-time injection, microservices framework
fetched: 2026-07-02
part: 5/27
---

## 3.24 Modifying Class Annotations With A Mixin

There are scenarios where a class cannot be accessed to add or remove annotations for the annotation processor

The most used scenario is to modify the annotations when the class is imported with @ClassImport or a scenario when classes are generated and cannot be modified.

It’s possible to define a mixin class by annotating it with @Mixin and specifying which class does it reference.

All the annotations of the mixin will be copied to the original class and all the annotations of the constructor with matching parameters, fields of the same name and methods of the same name with matching parameters will be copied.

In this example we have a simple bean class included in an external library for which we want to apply Micronaut Serialization:

```java
package my.external.library;

class MyBean {
    String name;
}
```

To add serialization annotations we can create a mixin that is referencing the original class:

```java
package example;

import com.fasterxml.jackson.annotation.JsonProperty;
import io.micronaut.context.annotation.Mixin;
import io.micronaut.core.annotation.Introspected;

@Mixin(my.external.library.MyBean.class) (1)
@Introspected(accessKind = Introspected.AccessKind.FIELD) (2)
class MyBeanMixin {
    @JsonProperty("hello") (3)
    String name; (4)
}
```

| **1** | The @Mixin is defined referencing the bean from the external library |
|---|---|
| **2** | The extra annotation that will be copied to the referenced class |
| **3** | The extra annotation of the field `name` that will be copied to the field of the referenced class |
| **4** | The field name must match the field name of the referenced class |

|   | Mixins currently supported only for the Java language. |
|---|---|

Following the example from Importing Classes from Libraries of importing Jakarta Inject TCK, most of the beans from the TCK have the correct Jakarta Inject annotations except one bean which is not annotated at all, to fix that we can create a mixin to fix that:

```java
package example;

import io.micronaut.context.annotation.Bean;
import io.micronaut.context.annotation.ClassImport;
import io.micronaut.context.annotation.Mixin;
import org.atinject.tck.auto.FuelTank;

@Mixin(FuelTank.class)
@Bean
class FuelTankMixin {
}

@ClassImport(packages = {"org.atinject.tck.auto", "org.atinject.tck.auto.accessories"})
class BeanImportTest {
}
```

The mixin supports copying only specific annotations by defining `includeAnnotations`, the set of annotations or packages that should be copied. Alternatively there is `excludeAnnotation` that will copy only annotations not excluded.

Each mixin point (constructor, method, field, parameter) can have specific rules of copying using @Filter.

The annotation @Filter also support removing existing annotations of the original class.

In this example all the Jakarta Validation are removed from the original method referenced by the mixin:

```java
package example;

import com.fasterxml.jackson.annotation.JsonProperty;
import io.micronaut.context.annotation.Executable;
import io.micronaut.context.annotation.Mixin;
import io.micronaut.core.annotation.Introspected;

@Mixin(MyBean.class) (1)
@Introspected(accessKind = Introspected.AccessKind.FIELD) (2)
class MyBeanMixin {
    String name;

    @Executable
    @JsonProperty("hello") (3)
    @Mixin.Filter(removeAnnotations = "jakarta.validation") (4)
    public String getXyz() {
        return name;
    }
}
```

| **1** | The @Mixin is defined referencing the bean from the external library |
|---|---|
| **2** | The extra annotation that will be copied to the referenced class |
| **3** | The extra annotation of the method `getXyz` that will be copied to the same method of the referenced class |
| **4** | The definition to remove all the annotations with a full name prefixed by `jakarta.validation` |

|   | Mixins only modify the Micronaut annotations metadata model. Original classes are not modified in any way. |
|---|---|


## 3.25 Nullability Annotations

In Java, you can use annotations showing whether a variable can or cannot be null. Such annotations aren’t part of the standard library.

|   | Since Micronaut Framework 5, we recommend you use JSpecify Annotations instead of the Micronaut Nullability Annotations for better [Kotlin interoperability](https://kotlinlang.org/docs/whatsnew21.html#change-of-jspecify-nullability-mismatch-diagnostics-severity-to-strict) and [IDE](https://www.jetbrains.com/idea/whatsnew/#page__content-jspecify-support)/Tooling support. Indeed, since 5.0 Micronaut’s APIs use JSpecify annotations. |
|---|---|


## Micronaut’s Nullability Annotations

Micronaut framework provides first-class nullability annotations:

- @NonNull — the annotated element must never be null.
- @Nullable — the annotated element may be null.
- @NullMarked — sets a default non-null policy within the annotated scope (package, type, or method), unless overridden.

These annotations are designed for use on parameters, return values, fields, and type-use positions (for example, generic type arguments).

|   | Micronaut will default to the non-null policy in most of the places if not defined explicitly as nullable |
|---|---|

Optional request parameter in a controller

```java
package example;

import org.jspecify.annotations.Nullable;
import io.micronaut.http.annotation.Controller;
import io.micronaut.http.annotation.Get;
import io.micronaut.http.annotation.QueryValue;

@Controller("/greet") (1)
class GreetingController {

    @Get (2)
    String hello(@QueryValue @Nullable String nickname) { (3)
        return nickname == null ? "Hello" : "Hello, " + nickname; (4)
    }
}
```

| **1** | Defines a controller mapped to the /greet path. |
|---|---|
| **2** | Exposes an HTTP GET endpoint. |
| **3** | Marks the query parameter as optional with `org.jspecify.annotations.Nullable[]` requests may omit it. |
| **4** | Null-safe handling when the parameter is not provided. |

Optional dependency in a factory-produced bean

```java
package example;

import io.micronaut.context.annotation.Factory;
import org.jspecify.annotations.Nullable;
import jakarta.inject.Singleton;

@Factory (1)
class ClientFactory {

    @Singleton (2)
    Client client(@Nullable OptionalDependency optional) { (3)
        return new Client(optional); (4)
    }
}

final class Client {
    private final OptionalDependency optional;

    Client(@Nullable OptionalDependency optional) { (5)
        this.optional = optional;
    }

    String description() {
        return optional == null ? "No optional dependency" : "Has optional dependency";
    }
}

interface OptionalDependency {}
```

| **1** | Declares a factory class that produces beans. |
|---|---|
| **2** | Defines a bean-producing method with singleton scope. |
| **3** | The dependency is optional and annotated with `org.jspecify.annotations.Nullable`; if no bean of that type exists, injection does not fail and null is injected. |
| **4** | The produced bean is created regardless of whether the optional dependency is present. |
| **5** | The consumer explicitly declares the constructor parameter as nullable and handles a potential null value. |

**Why does the Micronaut framework add its own set of nullability annotations instead of using one of the existing nullability annotations libraries?**

Throughout the history of the framework, we used other nullability annotation libraries. However, licensing issues made us change nullability annotations several times. To avoid having to change nullability annotations in the future, we added our own set of nullability annotations in Micronaut framework 2.4

**Are Micronaut Nullability annotations recognized by Kotlin?**

Kotlin does not recognize Micronaut framework’s nullability annotations. However, Micronaut supports other nullability annotations via AnnotationMapper.

|   | Micronaut framework supports other known nullability annotations from: Android, FindBugs, Javax, Eclipse, JetBrains, JSpecify |
|---|---|

To better support Kotlin, we recommended to use JSpecify or any other Kotlin recognizable nullability annotations.


## 3.25.1 JSpecify Nullability Annotations

Micronaut supports JSpecify annotations as an alternative to its own. Internally they are simply remapped to the Micronaut ones.

- `org.jspecify.annotations.Nullable` — the annotated value may be null.
- `org.jspecify.annotations.NonNull` — expresses a not-null contract for the annotated element.
- `org.jspecify.annotations.NullMarked` — sets a default non-null policy within the annotated scope (package, type, or method), unless overridden.

|   | There is a difference how the annotations should be put on an array field. Micronaut supports `@io.micronaut.core.annotation.Nullable String[] myField` but for JSpecify the correct syntax is `String @org.jspecify.annotations.Nullable [] myField`, the opposite will only mark the array component as nullable. |
|---|---|

|   | You may mix JSpecify with Micronaut’s nullability annotations; however, prefer a single, consistent approach within a module or package to keep intent clear and reduce ambiguity. |
|---|---|

|   | Adopt `@NullMarked` on a package or type to make non-null the default, then annotate only the exceptional cases with `@Nullable`. |
|---|---|

The following class uses JSpecify to declare non-null by default with `@NullMarked`, and annotates only the few nullable cases:

```java
import org.jspecify.annotations.NullMarked;
import org.jspecify.annotations.Nullable;
import org.jspecify.annotations.NonNull;
import jakarta.inject.Singleton;

@Singleton
@NullMarked
final class AccountService {

    // Non-null by default due to @NullMarked
    String greet(String name) {
        return "Hello, " + name;
    }

    // Nullable return and parameter explicitly marked
    @Nullable
    String findNickname(@Nullable String userId) {
        if (userId == null) {
            return null;
        }
        // Lookup may return null if not found
        return null;
    }
}
```


## 3.26 Micronaut Beans And Spring

Micronaut framework has integrations with Spring in several forms. See the Micronaut Spring Documentation for more information.


## 3.27 Android Support

Since Micronaut dependency injection is based on annotation processors and doesn’t rely on reflection, it can be used on Android when using the Android plugin 3.0.0 or higher.

This lets you use the same application framework for both your Android client and server implementation.


## Configuring Your Android Build

To get started, add the Micronaut annotation processors to the processor classpath using the `annotationProcessor` dependency configuration.

Include the Micronaut `micronaut-inject-java` dependency in both the `annotationProcessor` and `compileOnly` scopes of your Android build configuration:

Example Android build.gradle

```groovy
dependencies {
    ...
    annotationProcessor "io.micronaut:micronaut-inject-java:5.1.3"
    compileOnly "io.micronaut:micronaut-inject-java:5.1.3"
    ...
}
```

If you use `lint` as part of your build you may also need to disable the invalid packages check since Android includes a hard-coded check that regards the `jakarta.inject` package as invalid unless you use Dagger:

Configure lint within build.gradle

```groovy
android {
    ...
    lintOptions {
        lintOptions { warning 'InvalidPackage' }
    }
}
```

You can find more information on configuring annotations processors in the Android documentation.

|   | Micronaut `inject-java` dependency uses Android Java 8 support features. |
|---|---|


## Enabling Dependency Injection

Once you have configured the classpath correctly, the next step is start the ApplicationContext.

The following example demonstrates creating a subclass of android.app.Application for that purpose:

Example Android Application Class

```java
import android.app.Activity;
import android.app.Application;
import android.os.Bundle;

import io.micronaut.context.ApplicationContext;
import io.micronaut.context.env.Environment;

public class BaseApplication extends Application { (1)

    private ApplicationContext ctx;

    @Override
    public void onCreate() {
        super.onCreate();
        ctx = ApplicationContext.run(MainActivity.class, Environment.ANDROID); (2)
        registerActivityLifecycleCallbacks(new ActivityLifecycleCallbacks() { (3)
            @Override
            public void onActivityCreated(Activity activity, Bundle bundle) {
                ctx.inject(activity);
            }
            ... // shortened for brevity; it is not necessary to implement other methods
        });
    }
}
```

| **1** | Extend the `android.app.Application` class |
|---|---|
| **2** | Run the `ApplicationContext` with the `ANDROID` environment |
| **3** | Register an `ActivityLifecycleCallbacks` instance to allow dependency injection of Android `Activity` instances |

# 4 Application Configuration

Micronaut features a flexible configuration mechanism that allows reading configuration from a variety of sources into a unified model that can be bound to Java types annotated with @ConfigurationProperties.

Configuration can by default be provided in Java properties files or JSON with the ability to add support for more formats (such as YAML or Groovy configuration) by adding additional third-party libraries to your classpath. The convention is to search for a file named `application.properties` or `application.json` with support for other formats requiring additional dependencies as described by the following table:

| Format | File | Dependency Required |
|---|---|---|
| YAML | `application.yml` | `org.yaml:snakeyaml` |
| Groovy Config | `application.groovy` | `io.micronaut.groovy:micronaut-runtime-groovy` |
| HOCON | `application.conf` | `io.micronaut.kotlin:micronaut-kotlin-runtime` |
| TOML | `application.toml` | `io.micronaut.toml:micronaut-toml` |

In addition, Micronaut framework allows overriding any property via system properties or environment variables.

Each source of configuration is modeled with the PropertySource interface and the mechanism is extensible, allowing the implementation of additional PropertySourceLoader implementations.

Micronaut also supports in-file configuration imports via `micronaut.config.import`, which allows one configuration source to load additional sources recursively. See Property Sources for protocol-specific syntax (`file`, `classpath`, `env`, `configtree`) and optional import behavior.


## 4.1 The Environment

The application environment is modelled by the Environment interface, which allows specifying one or many unique environment names when creating an ApplicationContext.

Initializing the Environment

```java
ApplicationContext applicationContext = ApplicationContext.run("test", "android");
Environment environment = applicationContext.getEnvironment();

assertTrue(environment.getActiveNames().contains("test"));
assertTrue(environment.getActiveNames().contains("android"));
```

Initializing the Environment

```kotlin
val applicationContext = ApplicationContext.run("test", "android")
val environment = applicationContext.environment

environment.activeNames.shouldContain("test")
environment.activeNames.shouldContain("android")
```

Initializing the Environment

```groovy
when:
ApplicationContext applicationContext = ApplicationContext.run("test", "android")
Environment environment = applicationContext.getEnvironment()

then:
environment.activeNames.contains("test")
environment.activeNames.contains("android")
```

The active environment names allow loading different configuration files depending on the environment, and also using the @Requires annotation to conditionally load beans or bean @Configuration packages.

In addition, the Micronaut framework attempts to detect the current environments. For example within a Spock or JUnit test the TEST environment is automatically active.

Additional active environments can be specified using the `micronaut.environments` system property or the `MICRONAUT_ENVIRONMENTS` environment variable. These are specified as a comma-separated list. For example:

Specifying environments

```bash
$ java -Dmicronaut.environments=foo,bar -jar myapp.jar
```

The above activates environments called `foo` and `bar`.

It is also possible to enable the detection of the Cloud environment the application is deployed to (this feature is disabled by default since Micronaut framework 4). See the section on Cloud Configuration for more information.


## 4.1.1 Environment Priority

The Micronaut framework loads property sources based on the environments specified, and if the same property key exists in multiple property sources specific to an environment, the environment order determines which value to use.

The Micronaut framework uses the following hierarchy for environment processing (lowest to highest priority):

- Deduced environments
- Environments from the `micronaut.environments` system property
- Environments from the `MICRONAUT_ENVIRONMENTS` environment variable
- Environments specified explicitly through the application context builder This also applies to `@MicronautTest(environments = …)`


## 4.1.2 Disabling Environment Detection

Automatic detection of environments can be disabled by setting the `micronaut.env.deduction` system property or the `MICRONAUT_ENV_DEDUCTION` environment variable to `false`. This prevents the Micronaut framework from detecting current environments, while still using any environments that are specifically provided as shown above.

Disabling environment detection via system property

```bash
$  java -Dmicronaut.env.deduction=false -jar myapp.jar
```

Alternatively, you can disable environment deduction using the ApplicationContextBuilder `deduceEnvironment` method when setting up your application.

Using ApplicationContextBuilder to disable environment deduction

```java
@Test
void testDisableEnvironmentDeductionViaBuilder() {
    ApplicationContext ctx = ApplicationContext.builder()
            .deduceEnvironment(false)
            .properties(Collections.singletonMap("micronaut.server.port", -1))
            .start();
    assertFalse(ctx.getEnvironment().getActiveNames().contains(Environment.TEST));
    ctx.close();
}
```

Using ApplicationContextBuilder to disable environment deduction

```kotlin
"test disable environment deduction via builder" {
    val ctx = ApplicationContext.builder().deduceEnvironment(false).start()
    ctx.environment.activeNames.shouldNotContain(Environment.TEST)
    ctx.close()
}
```

Using ApplicationContextBuilder to disable environment deduction

```groovy
void "test disable environment deduction via builder"() {
    when:
    ApplicationContext ctx = ApplicationContext.builder().deduceEnvironment(false).start()

    then:
    !ctx.environment.activeNames.contains(Environment.TEST)

    cleanup:
    ctx.close()
}
```


## 4.1.3 Default Environment

The Micronaut framework supports the concept of one or many default environments. A default environment is one that is only applied if no other environments are explicitly specified or deduced. Environments can be explicitly specified either through the application context builder `Micronaut.build().environments(…)`, through the `micronaut.environments` system property, or the `MICRONAUT_ENVIRONMENTS` environment variable. Environments can be deduced to automatically apply the environment appropriate for cloud deployments. If an environment is found through any of the above means, the default environment will **not** be applied.

To set the default environments, include a public static class that implements ApplicationContextConfigurer and is annotated with ContextConfigurer:

```java
public class Application {

    @ContextConfigurer
    public static class DefaultEnvironmentConfigurer implements ApplicationContextConfigurer {
        @Override
        public void configure(@NonNull ApplicationContextBuilder builder) {
            builder.defaultEnvironments(defaultEnvironment);
        }
    }

    public static void main(String[] args) {
        Micronaut.run(Application.class, args);
    }
}
```

|   | Previously, we recommended using `Micronaut.defaultEnvironments("dev")` however this does not allow the Ahead of Time (AOT) compiler to detect the default environments. |
|---|---|

Since Micronaut framework 2.3 a banner is shown when the application starts. It is enabled by default, and it also shows the Micronaut version.

```shell
$ ./gradlew run
 __  __ _                                  _
|  \/  (_) ___ _ __ ___  _ __   __ _ _   _| |_
| |\/| | |/ __| '__/ _ \| '_ \ / _` | | | | __|
| |  | | | (__| | | (_) | | | | (_| | |_| | |_
|_|  |_|_|\___|_|  \___/|_| |_|\__,_|\__,_|\__|
  Micronaut (5.1.3)

17:07:22.997 [main] INFO  io.micronaut.runtime.Micronaut - Startup completed in 611ms. Server Running: http://localhost:8080
```

To customize the banner with your own ASCII Art (just plain ASCII at this moment), create the file `src/main/resources/micronaut-banner.txt` and it will be used instead.

To disable it, modify your `Application` class:

```java
public class Application {

    public static void main(String[] args) {
        Micronaut.build(args)
                 .banner(false) (1)
                 .start();
    }
}
```

| **1** | Disable the banner |
|---|---|
