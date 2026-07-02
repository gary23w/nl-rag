---
title: "Micronaut Core (part 6/27)"
source: https://docs.micronaut.io/latest/guide/index.html
domain: micronaut
license: CC-BY-SA-4.0
tags: micronaut framework, micronaut jvm, compile-time injection, microservices framework
fetched: 2026-07-02
part: 6/27
---

## 4.3 Externalized Configuration with PropertySources

Additional PropertySource instances can be added to the environment prior to initializing the ApplicationContext.

Initializing the Environment

```java
ApplicationContext applicationContext = ApplicationContext.run(
        PropertySource.of(
                "test",
                CollectionUtils.mapOf(
                    "micronaut.server.host", "foo",
                    "micronaut.server.port", 8080
                )
        ),
        "test", "android");
Environment environment = applicationContext.getEnvironment();

assertEquals("foo", environment.getProperty("micronaut.server.host", String.class).orElse("localhost"));
```

Initializing the Environment

```kotlin
val applicationContext = ApplicationContext.run(
    PropertySource.of(
        "test",
        mapOf(
            "micronaut.server.host" to "foo",
            "micronaut.server.port" to 8080
        )
    ),
    "test", "android"
)
val environment = applicationContext.environment

environment.getProperty("micronaut.server.host", String::class.java).orElse("localhost") shouldBe "foo"
```

Initializing the Environment

```groovy
when:
ApplicationContext applicationContext = ApplicationContext.run(
        PropertySource.of(
                "test",
                [
                    "micronaut.server.host": "foo",
                    "micronaut.server.port": 8080
                ]
        ),
        "test", "android")
Environment environment = applicationContext.getEnvironment()

then:
"foo" == environment.getProperty("micronaut.server.host", String.class).orElse("localhost")
```

The PropertySource.of method can be used to create a `PropertySource` from a map of values.

Alternatively one can register a PropertySourceLoader by creating a `META-INF/services/io.micronaut.context.env.PropertySourceLoader` file containing a reference to the class name of the `PropertySourceLoader`.

### Included PropertySource Loaders

Micronaut framework by default contains `PropertySourceLoader` implementations that load properties from the given locations and priority:

1. Command line arguments
2. Properties from `SPRING_APPLICATION_JSON` (for Spring compatibility)
3. Properties from `MICRONAUT_APPLICATION_JSON`
4. Java System Properties
5. OS environment variables
6. Configuration files loaded in order from the system property 'micronaut.config.files' or the environment variable `MICRONAUT_CONFIG_FILES`. The value can be a comma-separated list of paths with the last file having precedence. The files can be referenced from: the file system as an absolute path (without any prefix), the classpath with a `classpath:` prefix.
7. Environment-specific properties from `application-{environment}.{extension}`
8. Application-specific properties from `application.{extension}`

|   | 'micronaut.config.files' will be ignored in bootstrap.yml or application.yml. |
|---|---|

### Importing Additional Configuration

You can import additional configuration directly from a configuration file using `micronaut.config.import`. The value can be a single string, a list, or indexed entries (`micronaut.config.import[0]`, `micronaut.config.import[1]`, …).

Importing additional configuration

```properties
micronaut.config.import[0]=file:///etc/myapp/shared
micronaut.config.import[1]=classpath://overrides.yml
micronaut.config.import[2]=optional:env://MY_APP_INLINE_CONFIG
```

```yaml
micronaut:
  config:
    import:
      - "file:///etc/myapp/shared"
      - "classpath://overrides.yml"
      - "optional:env://MY_APP_INLINE_CONFIG"
```

```toml
[micronaut]
  [micronaut.config]
    import=[
      "file:///etc/myapp/shared",
      "classpath://overrides.yml",
      "optional:env://MY_APP_INLINE_CONFIG"
    ]
```

```groovy
micronaut {
  config {
    'import' = ["file:///etc/myapp/shared", "classpath://overrides.yml", "optional:env://MY_APP_INLINE_CONFIG"]
  }
}
```

```hocon
{
  micronaut {
    config {
      import = ["file:///etc/myapp/shared", "classpath://overrides.yml", "optional:env://MY_APP_INLINE_CONFIG"]
    }
  }
}
```

```json
{
  "micronaut": {
    "config": {
      "import": ["file:///etc/myapp/shared", "classpath://overrides.yml", "optional:env://MY_APP_INLINE_CONFIG"]
    }
  }
}
```

Imports are resolved recursively and support the following protocols:

- `file://` – load from the file system
- `classpath://` – load exactly one matching classpath resource (fails if duplicates are found)
- `classpath*://` – load and merge all matching classpath resources in classpath discovery order
- `env://` – load key/value properties from an environment variable value, using the variable-name suffix (for example `.yml`) or `?extension=yml` / `?extension=json` to select non-properties formats
- `configtree://` – load a directory tree where file paths map to property keys

Prefix any import with `optional:` to skip it when the target is missing. Without `optional:`, an ConfigurationException is thrown if the import cannot be loaded.

For `file://`, `classpath://`, and `classpath*://` imports, if no extension is provided, Micronaut probes known configuration extensions (`.properties`, `.json`, `.yml`, and any additional enabled loaders).

For `env://` imports, Micronaut defaults to `.properties` parsing. To import YAML or JSON from an environment variable, either include the format in the variable reference such as `env://MY_APP_INLINE_CONFIG.yml`, or specify it explicitly with `env://MY_APP_INLINE_CONFIG?extension=yml`.

When multiple resources with the same classpath name are present:

- `classpath://` throws a ConfigurationException and reports all matching locations.
- `classpath*://` loads all matches in classpath order and merges them in that same order.

|   | `file:///tmp/bar.properties` (with three slashes) resolves to the absolute path `/tmp/bar.properties`. |
|---|---|

### Implementing a Custom PropertySourceImporter

You can add support for a custom import protocol by implementing PropertySourceImporter and registering it with Java ServiceLoader. Each importer declares its provider with `getProvider()`, converts the parsed ConnectionString into a typed declaration via `newImportDeclaration(..)`, and then reads configuration from `importPropertySource(..)`.

Custom importer implementation

```java
public final class DemoPropertySourceImporter implements PropertySourceImporter<DemoPropertySourceImporter.DemoImport> {

    @Override
    public String getProvider() {
        return "demo";
    }

    @Override
    public DemoImport newImportDeclaration(ConnectionString connectionString) {
        return new DemoImport(connectionString.getPath());
    }

    @Override
    public DemoImport newImportDeclaration(ConvertibleValues<Object> values) {
        return new DemoImport(values.get("path", String.class).orElse("defaults"));
    }

    @Override
    public Optional<PropertySource> importPropertySource(ImportContext<DemoImport> context) {
        if (!"defaults".equals(context.importDeclaration().path())) {
            return Optional.empty();
        }
        return Optional.of(PropertySource.of(
            "demo:defaults",
            Map.of("demo.message", "hello-from-demo-importer")
        ));
    }

    public record DemoImport(String path) {
    }
}
```

Custom importer implementation

```kotlin
class DemoPropertySourceImporter : PropertySourceImporter<DemoPropertySourceImporter.DemoImport> {
    override fun getProvider(): String = "demo"

    override fun newImportDeclaration(connectionString: ConnectionString): DemoImport = DemoImport(connectionString.path)

    override fun newImportDeclaration(values: ConvertibleValues<Any>): DemoImport = DemoImport(values.get("path", String::class.java).orElse("defaults"))

    override fun importPropertySource(context: PropertySourceImporter.ImportContext<DemoImport>): java.util.Optional<PropertySource> {
        if (context.importDeclaration().path != "defaults") {
            return java.util.Optional.empty()
        }
        return java.util.Optional.of(
            PropertySource.of(
                "demo:defaults",
                mapOf("demo.message" to "hello-from-demo-importer")
            )
        )
    }

    data class DemoImport(val path: String)
}
```

Custom importer implementation

```groovy
class DemoPropertySourceImporter implements PropertySourceImporter<DemoPropertySourceImporter.DemoImport> {

    @Override
    String getProvider() {
        return "demo"
    }

    @Override
    DemoImport newImportDeclaration(ConnectionString connectionString) {
        new DemoImport(connectionString.path)
    }

    @Override
    DemoImport newImportDeclaration(ConvertibleValues<Object> values) {
        new DemoImport(values.get("path", String).orElse("defaults"))
    }

    @Override
    Optional<PropertySource> importPropertySource(PropertySourceImporter.ImportContext<DemoImport> context) {
        if (context.importDeclaration().path() != "defaults") {
            return Optional.empty()
        }
        return Optional.of(PropertySource.of("demo:defaults", ["demo.message": "hello-from-demo-importer"]))
    }

    static record DemoImport(String path) {
    }
}
```

Custom importer test

```java
@Test
void importsDemoDefaults() {
    try (ApplicationContext context = ApplicationContext.run()) {
        DemoPropertySourceImporter importer = new DemoPropertySourceImporter();
        DemoPropertySourceImporter.DemoImport declaration = importer.newImportDeclaration(ConnectionString.parse("demo://defaults"));
        PropertySourceImporter.ImportContext<DemoPropertySourceImporter.DemoImport> importContext = new PropertySourceImporter.ImportContext<>() {
            @Override
            public Environment environment() {
                return context.getEnvironment();
            }

            @Override
            public ConnectionString connectionString() {
                return ConnectionString.parse("demo://defaults");
            }

            @Override
            public DemoPropertySourceImporter.DemoImport importDeclaration() {
                return declaration;
            }

            @Override
            public PropertySource.Origin parentOrigin() {
                return PropertySource.Origin.of("classpath:application.yml");
            }

            @Override
            public Optional<PropertySource> importPropertySource(ResourceLoader resourceLoader,
                                                                 String resourcePath,
                                                                 String sourceName,
                                                                 PropertySource.Origin origin) {
                return Optional.empty();
            }

            @Override
            public Optional<PropertySource> importPropertySource(String content,
                                                                 String sourceName,
                                                                 String extension,
                                                                 PropertySource.Origin origin) {
                return Optional.empty();
            }

            @Override
            public Optional<PropertySource> importClasspathPropertySource(String resourcePath,
                                                                          String sourceName,
                                                                          PropertySource.Origin origin,
                                                                          boolean allowMultiple) {
                return Optional.empty();
            }
        };

        Optional<PropertySource> propertySource = importer.importPropertySource(importContext);

        assertTrue(propertySource.isPresent());
        assertEquals("hello-from-demo-importer", propertySource.get().get("demo.message"));
    }
}
```

Custom importer test

```kotlin
@Test
fun importsDemoDefaults() {
    ApplicationContext.run().use { context ->
        val importer = DemoPropertySourceImporter()
        val declaration = importer.newImportDeclaration(ConnectionString.parse("demo://defaults"))
        val importContext = object : PropertySourceImporter.ImportContext<DemoPropertySourceImporter.DemoImport> {
            override fun environment(): Environment = context.environment

            override fun connectionString(): ConnectionString = ConnectionString.parse("demo://defaults")

            override fun importDeclaration(): DemoPropertySourceImporter.DemoImport = declaration

            override fun parentOrigin(): PropertySource.Origin = PropertySource.Origin.of("classpath:application.yml")

            override fun importPropertySource(
                resourceLoader: ResourceLoader,
                resourcePath: String,
                sourceName: String,
                origin: PropertySource.Origin
            ): java.util.Optional<PropertySource> = java.util.Optional.empty()

            override fun importPropertySource(
                content: String,
                sourceName: String,
                extension: String,
                origin: PropertySource.Origin
            ): java.util.Optional<PropertySource> = java.util.Optional.empty()

            override fun importClasspathPropertySource(
                resourcePath: String,
                sourceName: String,
                origin: PropertySource.Origin,
                allowMultiple: Boolean
            ): java.util.Optional<PropertySource> = java.util.Optional.empty()
        }

        val propertySource = importer.importPropertySource(importContext)

        assertTrue(propertySource.isPresent)
        assertEquals("hello-from-demo-importer", propertySource.get().get("demo.message"))
    }
}
```

Register your implementation in `META-INF/services/io.micronaut.context.env.PropertySourceImporter`:

```none
io.micronaut.docs.config.importer.DemoPropertySourceImporter
```

After registration, the importer is selected when `micronaut.config.import` uses your protocol, for example `demo://defaults`.

If your importer loads remote configuration, RetryablePropertySourceImporter in `micronaut-discovery-core` provides a reusable base class that standardizes retry behavior across both connection-string and map-based imports. It parses the same retry properties from either form and applies them with Micronaut’s programmatic retry support.

Standard retry properties supported by RetryablePropertySourceImporter are:

- `retry-attempts` – maximum number of attempts
- `retry-count` – alias for `retry-attempts`
- `retry-delay` – delay between attempts
- `retry-max-delay` – maximum overall retry delay
- `retry-multiplier` – delay multiplier
- `retry-jitter` – retry jitter factor from `0.0` to `1.0`

|   | `.properties`, `.json`, `.yml` are supported out of the box. For Groovy users `.groovy` is supported as well. |
|---|---|

### Duplicate Configuration Resources

If a configuration file (for example `application.properties` or `application.yml`) is present more than once on the classpath, Micronaut can be configured to:

- fail fast with a clear error describing the conflicting locations,
- take the first match (with optional warning), or
- merge all matching resources.

The behavior can be customized using the ApplicationContextBuilder (including `Micronaut`).

Using FIRST_MATCH

```java
Micronaut.build(args)
    .configurationLoadingStrategy(ResourceLoadStrategy.builder()
        .type(ResourceLoadStrategyType.FIRST_MATCH)
        .warnOnDuplicates(true))
    .start();
```

Using FIRST_MATCH

```kotlin
Micronaut.build(*args)
    .configurationLoadingStrategy(
        ResourceLoadStrategy.builder()
            .type(ResourceLoadStrategyType.FIRST_MATCH)
            .warnOnDuplicates(true)
    )
    .start()
```

Using FIRST_MATCH

```groovy
Micronaut.build(args)
    .configurationLoadingStrategy(ResourceLoadStrategy.builder()
        .type(ResourceLoadStrategyType.FIRST_MATCH)
        .warnOnDuplicates(true))
    .start()
```

To merge duplicates, set the strategy type to `MERGE_ALL`:

Merging duplicates

```java
ApplicationContext ctx = ApplicationContext.builder()
    .configurationLoadingStrategy(ResourceLoadStrategy.builder()
        .type(ResourceLoadStrategyType.MERGE_ALL))
    .start();
```

Merging duplicates

```kotlin
val ctx = ApplicationContext.builder()
    .configurationLoadingStrategy(
        ResourceLoadStrategy.builder()
            .type(ResourceLoadStrategyType.MERGE_ALL)
    )
    .start()
```

Merging duplicates

```groovy
ApplicationContext ctx = ApplicationContext.builder()
    .configurationLoadingStrategy(ResourceLoadStrategy.builder()
        .type(ResourceLoadStrategyType.MERGE_ALL))
    .start()
```

When using `MERGE_ALL`, you can optionally specify a merge order based on artifact (JAR) name patterns:

MERGE_ALL with mergeOrder

```java
ApplicationContext ctx = ApplicationContext.builder()
    .configurationLoadingStrategy(ResourceLoadStrategy.builder()
        .type(ResourceLoadStrategyType.MERGE_ALL)
        .mergeOrder("lib-.*\\.jar", "app-.*\\.jar"))
    .start();
```

MERGE_ALL with mergeOrder

```kotlin
val ctx = ApplicationContext.builder()
    .configurationLoadingStrategy(
        ResourceLoadStrategy.builder()
            .type(ResourceLoadStrategyType.MERGE_ALL)
            .mergeOrder("lib-.*\\.jar", "app-.*\\.jar")
    )
    .start()
```

MERGE_ALL with mergeOrder

```groovy
ApplicationContext ctx = ApplicationContext.builder()
    .configurationLoadingStrategy(ResourceLoadStrategy.builder()
        .type(ResourceLoadStrategyType.MERGE_ALL)
        .mergeOrder('lib-.*\\.jar', 'app-.*\\.jar'))
    .start()
```

|   | `mergeOrder` is only supported when the strategy type is `MERGE_ALL`. When resources are merged, later resources override earlier ones when the same property key is present. |
|---|---|

Note that if you want full control of where your application loads configuration from you can disable the default `PropertySourceLoader` implementations listed above by calling the `enableDefaultPropertySources(false)` method of the ApplicationContextBuilder interface when starting your application.

In this case only explicit PropertySource instances that you add via the `propertySources(..)` method of the ApplicationContextBuilder interface will be used.

### Supplying Configuration via Command Line

Configuration can be supplied at the command line using Gradle or our Maven plugin. For example:

Gradle

```bash
$ ./gradlew run --args="-endpoints.health.enabled=true -config.property=test"
```

Maven

```bash
$ ./mvnw mn:run -Dmn.appArgs="-endpoints.health.enabled=true -config.property=test"
```

For the configuration to be a part of the context, the args from the main method must be passed to the context builder. For example:

```java
import io.micronaut.runtime.Micronaut;

public class Application {

    public static void main(String[] args) {
        Micronaut.run(Application.class, args); // passing args
    }
}
```

### Secrets and Sensitive Configuration

It is important to note that it is not recommended to store sensitive configuration such as passwords and tokens within configuration files that can potentially be checked into source control systems.

It is good practise to instead externalize sensitive configuration completely from the application code using preferably an external secret manager system (there are many options here, many provided by Cloud providers) or environment variables that are set during the deployment of the application. You can also use property placeholders (see the following section), to customize names of the environment variables to use and supply default values:

Using Property Value Placeholders to Define Secure Configuration

```properties
datasources.default.url=${JDBC_URL:`jdbc:mysql://localhost:3306/db`}
datasources.default.username=${JDBC_USER:root}
datasources.default.password=${JDBC_PASSWORD:}
datasources.default.dialect=MYSQL
datasources.default.driverClassName=${JDBC_DRIVER:com.mysql.cj.jdbc.Driver}
```

```yaml
datasources:
  default:
    url: ${JDBC_URL:`jdbc:mysql://localhost:3306/db`}
    username: ${JDBC_USER:root}
    password: ${JDBC_PASSWORD:}
    dialect: MYSQL
    driverClassName: ${JDBC_DRIVER:com.mysql.cj.jdbc.Driver}
```

```toml
[datasources]
  [datasources.default]
    url="${JDBC_URL:`jdbc:mysql://localhost:3306/db`}"
    username="${JDBC_USER:root}"
    password="${JDBC_PASSWORD:}"
    dialect="MYSQL"
    driverClassName="${JDBC_DRIVER:com.mysql.cj.jdbc.Driver}"
```

```groovy
datasources {
  'default' {
    url = "${JDBC_URL:`jdbc:mysql://localhost:3306/db`}"
    username = "${JDBC_USER:root}"
    password = "${JDBC_PASSWORD:}"
    dialect = "MYSQL"
    driverClassName = "${JDBC_DRIVER:com.mysql.cj.jdbc.Driver}"
  }
}
```

```hocon
{
  datasources {
    default {
      url = "${JDBC_URL:`jdbc:mysql://localhost:3306/db`}"
      username = "${JDBC_USER:root}"
      password = "${JDBC_PASSWORD:}"
      dialect = "MYSQL"
      driverClassName = "${JDBC_DRIVER:com.mysql.cj.jdbc.Driver}"
    }
  }
}
```

```json
{
  "datasources": {
    "default": {
      "url": "${JDBC_URL:`jdbc:mysql://localhost:3306/db`}",
      "username": "${JDBC_USER:root}",
      "password": "${JDBC_PASSWORD:}",
      "dialect": "MYSQL",
      "driverClassName": "${JDBC_DRIVER:com.mysql.cj.jdbc.Driver}"
    }
  }
}
```

To securely externalize configuration consider using a secrets manager system supported by the Micronaut framework such as:

- AWS Secrets Manager.
- Google Cloud Secrets Manager.
- HashiCorp Vault
- Kubernetes Secrets.
- Oracle Cloud Vault.

### Property Value Placeholders

As mentioned in the previous section, the Micronaut framework includes a property placeholder syntax to reference configuration properties both within configuration values and with any Micronaut annotation. See @Value and the section on Configuration Injection.

|   | Programmatic usage is also possible via the PropertyPlaceholderResolver interface. |
|---|---|

The basic syntax is to wrap a reference to a property in `${…}`. For example:

Defining Property Placeholders

```properties
myapp.endpoint=http://${micronaut.server.host}:${micronaut.server.port}/foo
```

```yaml
myapp:
  endpoint: http://${micronaut.server.host}:${micronaut.server.port}/foo
```

```toml
[myapp]
  endpoint="http://${micronaut.server.host}:${micronaut.server.port}/foo"
```

```groovy
myapp {
  endpoint = "http://${micronaut.server.host}:${micronaut.server.port}/foo"
}
```

```hocon
{
  myapp {
    endpoint = "http://${micronaut.server.host}:${micronaut.server.port}/foo"
  }
}
```

```json
{
  "myapp": {
    "endpoint": "http://${micronaut.server.host}:${micronaut.server.port}/foo"
  }
}
```

The above example embeds references to the `micronaut.server.host` and `micronaut.server.port` properties.

You can specify default values by defining a value after the `:` character. For example:

Using Default Values

```properties
myapp.endpoint=http://${micronaut.server.host:localhost}:${micronaut.server.port:8080}/foo
```

```yaml
myapp:
  endpoint: http://${micronaut.server.host:localhost}:${micronaut.server.port:8080}/foo
```

```toml
[myapp]
  endpoint="http://${micronaut.server.host:localhost}:${micronaut.server.port:8080}/foo"
```

```groovy
myapp {
  endpoint = "http://${micronaut.server.host:localhost}:${micronaut.server.port:8080}/foo"
}
```

```hocon
{
  myapp {
    endpoint = "http://${micronaut.server.host:localhost}:${micronaut.server.port:8080}/foo"
  }
}
```

```json
{
  "myapp": {
    "endpoint": "http://${micronaut.server.host:localhost}:${micronaut.server.port:8080}/foo"
  }
}
```

The above example defaults to `localhost` and port `8080` if no value is found (rather than throwing an exception). Note that if the default value contains a `:` character, you must escape it using backticks:

Using Backticks

```properties
myapp.endpoint=${server.address:`http://localhost:8080`}/foo
```

```yaml
myapp:
  endpoint: ${server.address:`http://localhost:8080`}/foo
```

```toml
[myapp]
  endpoint="${server.address:`http://localhost:8080`}/foo"
```

```groovy
myapp {
  endpoint = "${server.address:`http://localhost:8080`}/foo"
}
```

```hocon
{
  myapp {
    endpoint = "${server.address:`http://localhost:8080`}/foo"
  }
}
```

```json
{
  "myapp": {
    "endpoint": "${server.address:`http://localhost:8080`}/foo"
  }
}
```

The above example looks for a `server.address` property and defaults to `http://localhost:8080`. This default value is escaped with backticks since it has a `:` character.

### Property Value Binding

Note that these property references should be in kebab case (lowercase and hyphen-separated) when placing references in code or in placeholder values. For example, use `micronaut.server.default-charset` and not `micronaut.server.defaultCharset`.

The Micronaut framework still allows specifying the latter in configuration, but normalizes the properties into kebab case form to optimize memory consumption and reduce complexity when resolving properties. The following table summarizes how properties are normalized from different sources:

| Configuration Value | Resulting Properties | Property Source |
|---|---|---|
| `myApp.myStuff` | `my-app.my-stuff` | Properties, YAML etc. |
| `my-app.myStuff` | `my-app.my-stuff` | Properties, YAML etc. |
| `myApp.my-stuff` | `my-app.my-stuff` | Properties, YAML etc. |
| `MYAPP_MYSTUFF` | `myapp.mystuff`, `myapp-mystuff` | Environment Variable |
| `MY_APP_MY_STUFF` | `my.app.my.stuff`, `my.app.my-stuff`, `my.app-my.stuff`, `my.app-my-stuff`, `my-app.my.stuff`, `my-app.my-stuff`, `my-app-my.stuff`, `my-app-my-stuff` | Environment Variable |

Environment variables are treated specially to allow more flexibility. Note that there is no way to reference an environment variable with camel-case.

|   | Because the number of properties generated is exponential based on the number of `_` characters in an environment variable, it is recommended to refine which, if any, environment variables are included in configuration if the number of environment variables with multiple underscores is high. |
|---|---|

|   | Because of the way characters are treated in environment variables, it is not possible to target a poperty with in the name. Per the above, properties should be in kebab case to maintain the ability to target the property with environment variables. |
|---|---|

To control how environment properties participate in configuration, call the respective methods on the `Micronaut` builder.

Application class

```java
import io.micronaut.runtime.Micronaut;

public class Application {

    public static void main(String[] args) {
        Micronaut.build(args)
                .mainClass(Application.class)
                .environmentPropertySource(false)
                //or
                .environmentVariableIncludes("THIS_ENV_ONLY")
                //or
                .environmentVariableExcludes("EXCLUDED_ENV")
                .start();
    }
}
```

Application class

```kotlin
import io.micronaut.runtime.Micronaut

object Application {

    @JvmStatic
    fun main(args: Array<String>) {
        Micronaut.build()
                .mainClass(Application::class.java)
                .environmentPropertySource(false)
                //or
                .environmentVariableIncludes("THIS_ENV_ONLY")
                //or
                .environmentVariableExcludes("EXCLUDED_ENV")
                .start()
    }
}
```

Application class

```groovy
import io.micronaut.runtime.Micronaut

class Application {

    static void main(String[] args) {
        Micronaut.build()
                .mainClass(Application)
                .environmentPropertySource(false)
                //or
                .environmentVariableIncludes("THIS_ENV_ONLY")
                //or
                .environmentVariableExcludes("EXCLUDED_ENV")
                .start()
    }
}
```

|   | The configuration above does not have any impact on property placeholders. It is still possible to reference an environment variable in a placeholder regardless of whether environment configuration is disabled, or even if the specific property is explicitly excluded. |
|---|---|

### Using Random Properties

You can use `random` values by using the following properties. These can be used in configuration files as variables like the following.

```properties
micronaut.application.name=myapplication
micronaut.application.instance.id=${random.shortuuid}
```

```yaml
micronaut:
  application:
    name: myapplication
    instance:
      id: ${random.shortuuid}
```

```toml
[micronaut]
  [micronaut.application]
    name="myapplication"
    [micronaut.application.instance]
      id="${random.shortuuid}"
```

```groovy
micronaut {
  application {
    name = "myapplication"
    instance {
      id = "${random.shortuuid}"
    }
  }
}
```

```hocon
{
  micronaut {
    application {
      name = "myapplication"
      instance {
        id = "${random.shortuuid}"
      }
    }
  }
}
```

```json
{
  "micronaut": {
    "application": {
      "name": "myapplication",
      "instance": {
        "id": "${random.shortuuid}"
      }
    }
  }
}
```

| Property | Value |
|---|---|
| random.port | An available random port number |
| random.int | Random int |
| random.integer | Random int |
| random.long | Random long |
| random.float | Random float |
| random.shortuuid | Random UUID of only 10 chars in length (Note: As this isn’t full UUID, collision COULD occur) |
| random.uuid | Random UUID with dashes |
| random.uuid2 | Random UUID without dashes |

The `random.int`, `random.integer`, `random.long` and `random.float` properties supports a range suffix whose syntax is one of as follows:

- `(max)` where max is an exclusive value
- `[min,max]` where min being inclusive and max being exclusive values.

```properties
instance.id=${random.int[5,10]}
instance.count=${random.int(5)}
```

```yaml
instance:
  id: ${random.int[5,10]}
  count: ${random.int(5)}
```

```toml
[instance]
  id="${random.int[5,10]}"
  count="${random.int(5)}"
```

```groovy
instance {
  id = "${random.int[5,10]}"
  count = "${random.int(5)}"
}
```

```hocon
{
  instance {
    id = "${random.int[5,10]}"
    count = "${random.int(5)}"
  }
}
```

```json
{
  "instance": {
    "id": "${random.int[5,10]}",
    "count": "${random.int(5)}"
  }
}
```

|   | The range could vary from negative to positive as well. |
|---|---|

### Fail Fast Property Injection

For beans that inject required properties, the injection and potential failure will not occur until the bean is requested. To verify at startup that the properties exist and can be injected, the bean can be annotated with @Context. Context-scoped beans are injected at startup, and startup fails if any required properties are missing or cannot be converted to the required type.

|   | It is recommended to use this feature sparingly to ensure fast startup. |
|---|---|


## 4.4 Configuration Injection

You can inject configuration values into beans using the @Value annotation.

### Using the `@Value` Annotation

Consider the following example:

@Value Example

```java
import io.micronaut.context.annotation.Requires;
import io.micronaut.context.annotation.Value;
import org.jspecify.annotations.Nullable;

import jakarta.inject.Singleton;

@Singleton
public class EngineImpl implements Engine {

    @Value("${my.engine.cylinders:6}") // (1)
    protected int cylinders;

    @Nullable
    @Value("${my.engine.description}")
    protected String description;

    @Override
    public int getCylinders() {
        return cylinders;
    }

    @Override
    public String start() {// (2)
        return "Starting V" + getCylinders() + " Engine";
    }

    @Override
    public String getDescription() {
        return description;
    }

}
```

@Value Example

```kotlin
import io.micronaut.context.annotation.Value

import jakarta.inject.Singleton

@Singleton
class EngineImpl : Engine {

    @Value("\${my.engine.cylinders:6}") // (1)
    override var cylinders: Int = 0
        protected set

    override fun start(): String { // (2)
        return "Starting V$cylinders Engine"
    }
}
```

@Value Example

```groovy
import io.micronaut.context.annotation.Value

import jakarta.inject.Singleton

@Singleton
class EngineImpl implements Engine {

    @Value('${my.engine.cylinders:6}') // (1)
    protected int cylinders

    @Override
    int getCylinders() {
        cylinders
    }

    @Override
    String start() { // (2)
        "Starting V$cylinders Engine"
    }
}
```

| **1** | The `@Value` annotation accepts a string that can have embedded placeholder values (the default value can be provided by specifying a value after the colon `:` character). Also try to avoid setting the member visibility to `private`, since this requires the Micronaut Framework to use reflection. Prefer to use `protected`. |
|---|---|
| **2** | The injected value can then be used within code. |

Note that `@Value` can also be used to inject a static value. For example the following injects the number 10:

Static @Value Example

```groovy
@Value("10")
int number;
```

This is even more useful when used to compose injected values combining static content and placeholders. For example to set up a URL:

Placeholders with @Value

```groovy
@Value("http://${my.host}:${my.port}")
URL url;
```

In the above example the URL is constructed from two placeholder properties that must be present in configuration: `my.host` and `my.port`.

Remember that to specify a default value in a placeholder expression, you use the colon `:` character. However, if the default you specify includes a colon, you must escape the value with backticks. For example:

Placeholders with @Value

```groovy
@Value("${my.url:`http://foo.com`}")
URL url;
```

Note that there is nothing special about `@Value` itself regarding the resolution of property value placeholders.

Due to Micronaut’s extensive support for annotation metadata you can use property placeholder expressions on any annotation. For example, to make the path of a `@Controller` configurable you can do:

```java
@Controller("${hello.controller.path:/hello}")
class HelloController {
    ...
}
```

In the above case, if `hello.controller.path` is specified in configuration the controller will be mapped to the specified path, otherwise it will be mapped to `/hello`.

You can also make the target server for @Client configurable (although service discovery approaches are often better), for example:

```java
@Client("${my.server.url:`http://localhost:8080`}")
interface HelloClient {
    ...
}
```

In the above example the property `my.server.url` can be used to configure the client, otherwise the client falls back to a localhost address.

### Using the `@Property` Annotation

Recall that the @Value annotation receives a String value which can be a mix of static content and placeholder expressions. This can lead to confusion if you attempt to do the following:

Incorrect usage of

@Value

```groovy
@Value("my.url")
String url;
```

In the above case the literal string value `my.url` is injected and set to the `url` field and **not** the value of the `my.url` property from your application configuration. This is because `@Value` only resolves placeholders within the value specified to it.

To inject a specific property name, you may be better off using @Property:

Using @Property

```java
import io.micronaut.context.annotation.Property;

import io.micronaut.context.annotation.Requires;
import jakarta.inject.Inject;
import jakarta.inject.Singleton;

@Singleton
public class Engine {

    @Property(name = "my.engine.cylinders") // (1)
    protected int cylinders; // (2)

    private String manufacturer;

    public int getCylinders() {
        return cylinders;
    }

    public String getManufacturer() {
        return manufacturer;
    }

    @Inject
    public void setManufacturer(@Property(name = "my.engine.manufacturer") String manufacturer) { // (3)
        this.manufacturer = manufacturer;
    }

}
```

Using @Property

```kotlin
import io.micronaut.context.annotation.Property

import jakarta.inject.Inject
import jakarta.inject.Singleton

@Singleton
class Engine {

    @field:Property(name = "my.engine.cylinders") // (1)
    protected var cylinders: Int = 0 // (2)

    @set:Inject
    @setparam:Property(name = "my.engine.manufacturer") // (3)
    var manufacturer: String? = null

    fun cylinders(): Int {
        return cylinders
    }
}
```

Using @Property

```groovy
import io.micronaut.context.annotation.Property

import jakarta.inject.Singleton

@Singleton
class Engine {

    @Property(name = "my.engine.cylinders") // (1)
    protected int cylinders // (2)

    @Property(name = "my.engine.manufacturer") //(3)
    String manufacturer

    int getCylinders() {
        cylinders
    }
}
```

| **1** | The `my.engine.cylinders` property is resolved from configuration and injected into the field. |
|---|---|
| **2** | Fields subject to injection should not be private because expensive reflection must be used |
| **3** | The `@Property` annotation is used to inject through the setter |

|   | Because it is not possible to define a default value with `@Property`, if the value doesn’t exist or cannot be converted to the required type, bean instantiation will fail. |
|---|---|

The above instead injects the value of the `my.engine.cylinders` property resolved from application configuration. If the property cannot be found in configuration, an exception is thrown. As with other types of injection, the injection point can also be annotated with `@Nullable` to make the injection optional.

You can also use this feature to resolve sub maps. For example, consider the following configuration:

```properties
datasources.default.name=mydb
jpa.default.properties.hibernate.hbm2ddl.auto=update
jpa.default.properties.hibernate.show_sql=true
```

```yaml
datasources:
  default:
    name: 'mydb'
jpa:
  default:
    properties:
      hibernate:
        hbm2ddl:
          auto: update
        show_sql: true
```

```toml
[datasources]
  [datasources.default]
    name="mydb"
[jpa]
  [jpa.default]
    [jpa.default.properties]
      [jpa.default.properties.hibernate]
        show_sql=true
        [jpa.default.properties.hibernate.hbm2ddl]
          auto="update"
```

```groovy
datasources {
  'default' {
    name = "mydb"
  }
}
jpa {
  'default' {
    properties {
      hibernate {
        hbm2ddl {
          auto = "update"
        }
        show_sql = true
      }
    }
  }
}
```

```hocon
{
  datasources {
    default {
      name = "mydb"
    }
  }
  jpa {
    default {
      properties {
        hibernate {
          hbm2ddl {
            auto = "update"
          }
          show_sql = true
        }
      }
    }
  }
}
```

```json
{
  "datasources": {
    "default": {
      "name": "mydb"
    }
  },
  "jpa": {
    "default": {
      "properties": {
        "hibernate": {
          "hbm2ddl": {
            "auto": "update"
          },
          "show_sql": true
        }
      }
    }
  }
}
```

To resolve a flattened map containing only the properties starting with `hibernate`, use `@Property`, for example:

Using

@Property

```java
@Property(name = "jpa.default.properties")
Map<String, String> jpaProperties;
```

The injected map will contain the keys `hibernate.hbm2ddl.auto` and `hibernate.show_sql` and their values.

|   | The @MapFormat annotation can be used to customize the injected map depending on whether you want nested keys or flat keys, and it allows customization of the key style via the StringConvention enum. |
|---|---|


## 4.5 Expression Language

Since 4.0, Micronaut framework supports embedding evaluated expressions in annotation values using `#{…}` syntax which allows to achieve even more flexibility while configuring your application.

Evaluated Expression example

```groovy
@Value("#{ T(Math).random() }")
double injectedValue;
```

Expressions can be defined whenever an annotation member accepts a string or an array of strings.

|   | Expressions are currently not supported for "type use" annotations (that declare `ElementType.TYPE_USE`). |
|---|---|

Evaluated Expression in array

```java
@Singleton
@Requires(env = {"dev", "#{ 'test' }"})
public class EvaluatedExpressionInArray {}
```

You can also embed one or more expressions in a string template in a similar manner to embedding properties with the `${…}` syntax.

Evaluated Expression template

```groovy
@Value("http://#{'hostname'}/#{'path'}")
String url;
```

Evaluated Expressions are validated and compiled at build time which guarantees type safety at runtime.

Once an application is running expressions are evaluated on demand as part of annotation metadata resolution. The usage of expressions does not impact performance as evaluation process is completely reflection free.

Note that, for security reasons expressions cannot be dynamically compiled at runtime from potentially untrusted input. All expressions are compiled and checked statically during the compilation process of the application with errors reported as compilation failures.

In general, expressions can be treated as statement written using a programming language with reduced set of available features. Even though the complexity of expression is only limited by the list of supported syntax constructs, it is in general not recommended to place complex logic inside an expression as there are usually better ways to achieve the same result.


## Using Expressions in Micronaut framework

Expressions can be used anywhere throughout the Micronaut framework and associated modules, but as an example, you can use them to implement simple scheduled job control, for example:

Job Control with Expressions

```java
import io.micronaut.scheduling.annotation.Scheduled;
import jakarta.inject.Singleton;

@Singleton
public class ExampleJob {
    private boolean jobRan = false;
    private boolean paused = true;

    @Scheduled(
        fixedRate = "1s",
        condition = "#{!this.paused}") // (1)
    void run() {
        System.out.println("Job Running");
        this.jobRan = true;
    }

    public boolean isPaused() {
        return paused;
    } // (2)

    public boolean hasJobRun() {
        return jobRan;
    }

    public void unpause() {
        paused = false;
    }

    public void pause() {
        paused = true;
    }

}
```

Job Control with Expressions

```groovy
import io.micronaut.scheduling.annotation.Scheduled
import jakarta.inject.Singleton

@Singleton
class ExampleJob {
    boolean paused = true // (2)
    private boolean jobRan = false

    @Scheduled(
            fixedRate = "1s",
            condition = '#{!this.paused}') // (1)
    void run() {
        println("Job Running")
        this.jobRan = true
    }

    boolean hasJobRun() {
        return jobRan
    }

    void unpause() {
        paused = false
    }

    void pause() {
        paused = true
    }
}
```

| **1** | Here the `condition` member of the @Scheduled annotation is used to only execute the job if a pre-condition is met. |
|---|---|
| **2** | The `condition` invokes a method of the type that checks if the job is paused. Other methods can be used to pause and resume execution of the job as desired. |

|   | You can also use expressions to perform conditional routing using the @RouteCondition annotation. |
|---|---|
