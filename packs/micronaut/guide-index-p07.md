---
title: "Micronaut Core (part 7/27)"
source: https://docs.micronaut.io/latest/guide/index.html
domain: micronaut
license: CC-BY-SA-4.0
tags: micronaut framework, micronaut jvm, compile-time injection, microservices framework
fetched: 2026-07-02
part: 7/27
---

## Evaluated Expression Language Reference

The Evaluated Expressions syntax supports the following functionality:

- Literal Values
- Math Operators
- Comparison Operators
- Logical Operators
- Ternary Operator
- Type References
- Method Invocation
- Property Access
- Retrieving Beans from Bean Context
- Retrieving Environment Properties

### Literal Values

The following types of literal values are supported:

- `null`
- boolean values (`true`, `false`)
- strings, which need to be surrounded with single quotation mark (`'`)
- numeric values (`int`, `long`, `float`, `double`)

Integer and Long values can also be specified in hexadecimal or octal notation. Float and Double values can also be specified in exponential notation. All numeric values can be negative as well.

Literal values examples

```none
#{ null }
#{ true }
#{ 'string value' }
#{ 10 }
#{ 0xFFL }
#{ 10L }
#{ .123f }
#{ 1E+1d }
#{ 123D }
```

### Math Operators

The supported mathematical operators are `, `-`, `*`, `/`, `%`, `^`. Math operators can only be applied to numeric values (except ` which can be used for string concatenation as well). Mathematical operations are performed in order enforced by standard operator precedence. You can also change evaluation order by using brackets `()`.

`/` and `%` operators can be aliased by `div` and `mod` keywords respectively.

Math operators examples

```none
#{ 1 + 2 }             // 3
#{ 'a' + 'b' + 'c' }   // 'abc'
#{ 7 - 3 }             // 4
#{ 7 * 3 }             // 21
#{ 7 * ( 3 + 1) }      // 28

#{ 15 / 3 }            // 5
#{ 15 div 3 }          // 5

#{ 15 % 3 }            // 0
#{ 15 mod 3 }          // 0

// Unlike in Java, ^ operator means exponentiation
#{ 3 ^ 2 }             // 9
```

### Comparison Operators

The following comparison operators are supported: `==`, `!=`, `>`, `<`, `>=`, `<=`, `matches` Comparison operations are performed in order enforced by standard operator precedence. You can also change evaluation order by using brackets `()`.

Equality check is supported for both primitive types and objects. It is performed using `Object.equals()` method.

`>`, `<`, `>=`, `<=` operations can be applied to numeric types or types that implement `java.lang.Comparable` interface.

`matches` keyword can be used to determine whether a string matches provided regular expression which has to be specified as string literal. The regular expression itself will be checked for validity at compilation time.

Comparison operators examples

```none
#{ 1 + 2 == 3 }         // true
#{ 'abc' != 'abc' }     // false
#{ 7 > 3 }              // true
#{ 7 < 3 }              // false
#{ 7 >= 7 }             // true
#{ 7 <= 8 }             // false

#{ 'AbC' matches '[A-Za-z*'  }      // Compilation failure
#{ 'AbC' matches '[A-Za-z]*'  }     // true
#{ 'AbC' matches '[a-z]*'  }        // false
```

### Logical Operators

The following logical operators are supported:

- `&&` (can be aliased with `and`)
- `||` (can be aliased with `or`),
- `!` (can be aliaded with `not`)
- `empty` / `not empty` (works with strings, collections, arrays, and maps)

Logical operations are performed in order enforced by standard operator precedence. You can also change evaluation order by using brackets `()`.

Logical operators examples

```none
#{ true && false }         // false
#{ true and true }         // true

#{ true || false }         // true
#{ false or false }        // false

#{ !false }                // true
#{ !!true }                // true

#{ empty '' }              // true
#{ not empty '' }          // false
```

### Ternary Operator

A standard ternary operator is supported to allow specifying if-then-else conditional logic in expression

```none
condition ? thenBranch : elseBranch
```

where `condition` evaluation should provide boolean value, and the complexity of `then` and `else` branches is not limited.

Ternary operator examples

```none
#{ 15 > 10 ? 'a' : 'b' }    // 'a'
#{ 15 >= 16 ? 'a' : 'b' }   // 'b'
```

### Dot and Safe Navigation Operator

The dot operator can be used to access methods and properties of a value within an expression. For example:

Dot operator usage

```none
#{ collection.size() > 0 }
#{ foo.bar.name == "Fred" }
```

You can also use the safe dereference operator `?.` to navigate paths in a null safe way:

Safe dereference operator

```none
#{ foo?.bar?.name == "Fred" }
```

|   | When used, the safe dereference operator will also automatically unwrap Java’s `Optional` type. |
|---|---|

### Type References

A predefined syntax construct `T(…)` can be used to reference a class. The value inside brackets should be fully qualified class name (including the package name). The only exception is `java.lang.*` classes which can be referenced directly by only specifying the simple class name. Primitive types can not be referenced.

Type References are evaluated in different ways depending on the context.

#### Simple type reference

A simple type reference is resolved as a `Class<?>` object.

Type reference example

```none
#{ T(java.lang.String) }    // String.class
```

Same rule applies if type reference is specified as a method argument.

#### Type check with `instanceof`

A Type Reference can be used as the right-hand side part of the `instanceof` operator

Type check example

```none
#{ 'abc' instanceof T(String) }  // true
```

which is equivalent to the following Java code and will be evaluated as a boolean value:

```none
"abc" instanceof String
```

#### Static method invocation

Type Reference can be used to invoke a static method of a class

Static method invocation

```none
#{ T(Math).random() }
```

### Expression Evaluation Context

By default, the only methods you can invoke inside Evaluated Expressions are static methods using type references.

The available methods can be extended by extended the evaluation context. There are two ways to extend the evaluation context. The first involves registering new context class via a custom TypeElementVisitor.

|   | The TypeElementVisitor has to be on the annotation processor classpath, therefore needs to be defined in a separate module that can be included on this classpath. |
|---|---|

Once a class is registered within evaluation context the methods and properties of the class are available for referencing in evaluated expressions.

Consider the following example:

User-defined evaluated expression context

```java
import jakarta.inject.Singleton;

import java.util.Random;

@Singleton
public class CustomEvaluationContext {
    private Random random = random = new Random();

    public int generateRandom(int min, int max) {
        return random.nextInt(max - min) + min;
    }
}
```

|   | The class should be resolvable as a bean can use `jakarta.inject` annotations to inject other types if necessary. In addition, for performance reasons all evaluation context classes are effectively singleton regardless of the defined scope. |
|---|---|

Registering this class can be achieved with a custom implementation of ExpressionEvaluationContextRegistrar that is registered via service loader as a TypeElementVisitor (create a new `META-INF/services/io.micronaut.inject.visitor.TypeElementVisitor` file referencing the new class) and placed on the annotation processor classpath:

Defining a ExpressionEvaluationContextRegistrar

```java
import io.micronaut.expressions.context.ExpressionEvaluationContextRegistrar;

public class ContextRegistrar implements ExpressionEvaluationContextRegistrar {
    @Override
    public String getContextClassName() {
        return "io.micronaut.docs.expressions.CustomEvaluationContext";
    }
}
```

Method `generateRandom(int, int)` can now be used within Evaluated Expression in the following way:

Usage of user-defined evaluated expression context

```java
package io.micronaut.docs.expressions;

import io.micronaut.context.annotation.Value;
import jakarta.inject.Singleton;

@Singleton
public class ContextConsumer {

    @Value("#{ generateRandom(1, 10) }")
    public int randomField;

}
```

At runtime, the bean will be retrieved from application context and respective method will be invoked.

If a matching method is not found within evaluation context at compilation time, the compilation will fail. A compilation error will also occur if multiple suitable methods are found in the evaluation context, keep that in mind if you provide multiple ExpressionEvaluationContextRegistrar that a conflict can occur as these types are effectively global.

The methods will be considered ambiguous (leading to compilation failure) when their names are the same and list of provided arguments matches multiple methods parameters.

Using a ExpressionEvaluationContextRegistrar makes its methods and properties available for evaluated expressions within any annotation in a global manner.

However, you can also specify evaluation context scoped to concrete annotation or annotation member using @AnnotationExpressionContext.

Usage of annotation level evaluated expression context

```java
package io.micronaut.docs.expressions;

import jakarta.inject.Singleton;
import io.micronaut.context.annotation.AnnotationExpressionContext;

@Singleton
@CustomAnnotation(value = "#{firstValue() + secondValue()}") // (1)
class Example {
}

@Singleton
class AnnotationContext { // (2)
    String firstValue() {
        return "first value";
    }
}

@Singleton
class AnnotationMemberContext { // (3)
    String secondValue() {
        return "second value";
    }
}

@AnnotationExpressionContext(AnnotationContext.class) // (4)
@interface CustomAnnotation {

    @AnnotationExpressionContext(AnnotationMemberContext.class) // (5)
    String value();
}
```

Usage of annotation level evaluated expression context

```groovy
package io.micronaut.docs.expressions;

import jakarta.inject.Singleton;
import io.micronaut.context.annotation.AnnotationExpressionContext;

@Singleton
@CustomAnnotation(value = "#{firstValue() + secondValue()}") // (1)
class Example {
}

@Singleton
class AnnotationContext { // (2)
    String firstValue() {
        return "first value"
    }
}

@Singleton
class AnnotationMemberContext { // (3)
    String secondValue() {
        return "second value"
    }
}

@AnnotationExpressionContext(AnnotationContext.class) // (4)
@interface CustomAnnotation {

    @AnnotationExpressionContext(AnnotationMemberContext.class) // (5)
    String value();
}
```

| **1** | Here two new methods are introduced to the context called `firstValue()` and `secondValue()` only for the scope of the `@CustomAnnotation` |
|---|---|
| **2** | The `firstValue()` method is defined in a bean called `AnnotationContext` |
| **3** | The `secondValue()` method is defined in a bean called `AnnotationMemberContext` |
| **4** | On the `@CustomAnnotation` annotation the methods of the `AnnotationContext` type are exposed to all members of the annotation (type level context). |
| **5** | On the `value()` member of the `@CustomAnnotation` annotation the methods of the `AnnotationContextExample` are made available but scoped only to the `value()` member. |

Again context classes need to be explicitly defined as beans to make them available for retrieval from application context at runtime.

### Method Invocation

You can invoke both static methods using type references, methods from evaluation context and methods on objects, which means method chaining is supported.

Chaining methods in expression

```java
import io.micronaut.context.annotation.Value;
import jakarta.inject.Singleton;

@Singleton
class CustomEvaluationContext {

    public String stringValue() {
        return "stringValue";
    }

}

@Singleton
class ContextConsumer {

    @Value("#{ #stringValue().length() }")
    public int stringLength;

}
```

Varargs methods invocation is supported as well. Note that if last parameter of a method is an array, you can still invoke it providing list of arguments separated by comma without explicitly wrapping it into array. So in this case it will be treated in same way as if last method argument was explicitly specified as varargs parameter.

Invoking varargs methods in expressions

```java
import io.micronaut.context.annotation.Value;
import jakarta.inject.Singleton;

@Singleton
class CustomEvaluationContext {

    public int countIntegers(int... values) {
        return values.length;
    }

    public int countStrings(String[] values) {
        return values.length;
    }

}

@Singleton
class ContextConsumer {

    @Value("#{ #countIntegers(1, 2, 3) }")
    public int totalIntegers;

    @Value("#{ #countStrings('a', 'b', 'c') }")
    public int totalStrings;

}
```

### Property Access

JavaBean properties can be accessed simply be referencing their names from evaluation context prefixed with `#`. Bean properties can also be chained with dot in the same way as methods.

Accessing bean properties in expressions

```java
import io.micronaut.context.annotation.Value;
import jakarta.inject.Singleton;

@Singleton
class CustomEvaluationContext {

    public String getName() {
        return "Bob";
    }

    public int getAge() {
        return 25;
    }

}

@Singleton
class ContextConsumer {

    @Value("#{ 'Name is ' + #name + ', age is ' + #age }")
    public String value;

}
```

### Retrieving Beans from Bean Context

A predefined syntax construct `ctx[…]` can be used to retrieve beans from bean context. The argument inside square brackets has to be a fully qualified class name (note that `T(…)` wrapper is optional and can be omitted for simplicity).

Retrieving beans from bean context

```none
#{ ctx[T(io.micronaut.example.ContextBean)] }
#{ ctx[io.micronaut.example.ContextBean] }
```

### Retrieving Environment Properties

A syntax construct `env[…]` can be used to retrieve environment properties by name. The expression inside square brackets has to resolve to string value, otherwise compilation will fail. If property value will be absent at runtime, the expression will return `null`

Retrieving Environment Properties

```none
#{ env['test.property'] }
```


## 4.6 Configuration Properties

You can create type-safe configuration by creating classes that are annotated with @ConfigurationProperties.

The Micronaut framework will produce a reflection-free `@ConfigurationProperties` bean and will also at compile time calculate the property paths to evaluate, greatly improving the speed and efficiency of loading `@ConfigurationProperties`.

For example:

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

| **1** | The `@ConfigurationProperties` annotation takes the configuration prefix |
|---|---|
| **2** | You can use `jakarta.validation` annotations to validate the configuration |
| **3** | Default values can be assigned to the property |
| **4** | Static inner classes can provide nested configuration |
| **5** | Optional configuration values can be wrapped in `java.util.Optional` |

Once you have prepared a type-safe configuration it can be injected into your beans like any other bean:

@ConfigurationProperties Dependency Injection

```java
@Singleton
public class EngineImpl implements Engine {
    private final EngineConfig config;

    public EngineImpl(EngineConfig config) { // (1)
        this.config = config;
    }

    @Override
    public int getCylinders() {
        return config.getCylinders();
    }

    @Override
    public String start() {// (2)
        return getConfig().getManufacturer() + " Engine Starting V" + getConfig().getCylinders() +
                " [rodLength=" + getConfig().getCrankShaft().getRodLength().orElse(6d) + "]";
    }

    public final EngineConfig getConfig() {
        return config;
    }
}
```

@ConfigurationProperties Dependency Injection

```kotlin
@Singleton
class EngineImpl(val config: EngineConfig) : Engine {// (1)

    override val cylinders: Int
        get() = config.cylinders

    override fun start(): String {// (2)
        return "${config.manufacturer} Engine Starting V${config.cylinders} [rodLength=${config.crankShaft.rodLength.orElse(6.0)}]"
    }
}
```

@ConfigurationProperties Dependency Injection

```groovy
@Singleton
class EngineImpl implements Engine {
    final EngineConfig config

    EngineImpl(EngineConfig config) { // (1)
        this.config = config
    }

    @Override
    int getCylinders() {
        config.cylinders
    }

    @Override
    String start() { // (2)
        "$config.manufacturer Engine Starting V$config.cylinders [rodLength=${config.crankShaft.rodLength.orElse(6.0d)}]"
    }
}
```

| **1** | Inject the `EngineConfig` bean |
|---|---|
| **2** | Use the configuration properties |

Configuration values can then be supplied from one of the PropertySource instances. For example:

Supply Configuration

```java
Map<String, Object> map = new LinkedHashMap<>(1);
map.put("my.engine.cylinders", "8");
map.put("spec.name", "VehiclePropertiesSpec");
ApplicationContext applicationContext = ApplicationContext.run(map, "test");

Vehicle vehicle = applicationContext.getBean(Vehicle.class);
System.out.println(vehicle.start());
```

Supply Configuration

```kotlin
val map = mapOf( "my.engine.cylinders" to "8")
val applicationContext = ApplicationContext.run(map, "test")

val vehicle = applicationContext.getBean(Vehicle::class.java)
println(vehicle.start())
```

Supply Configuration

```groovy
ApplicationContext applicationContext = ApplicationContext.run(
        ['my.engine.cylinders': '8'],
        "test"
)

def vehicle = applicationContext.getBean(Vehicle)
println(vehicle.start())
```

The above example prints: `"Ford Engine Starting V8 [rodLength=6.0]"`

You can directly reference configuration properties in `@Requires` annotation to conditionally load beans using the following syntax: `@Requires(bean=Config.class, beanProperty="property", value="true")`

Note for more complex configurations you can structure @ConfigurationProperties beans through inheritance.

For example creating a subclass of `EngineConfig` with `@ConfigurationProperties('bar')` will resolve all properties under the path `my.engine.bar`.

|   | YAML Reserved Words ~~~~~~~~ When using YAML configuration files, certain words are reserved by the YAML specification and will be automatically converted to boolean values. These include: `yes` / `no` `true` / `false` `on` / `off` If you use these words as unquoted property keys in YAML, they will be parsed as booleans instead of strings: `foo: bar: yes: "1" # yes is parsed as true (boolean) no: "2" # no is parsed as false (boolean)` To use these words as property names, you must quote the keys: `foo: bar: "yes": "1" # forces YAML to treat as string "no": "2" # forces YAML to treat as string` This is a limitation of YAML/SnakeYAML parsing and not specific to Micronaut. For more information, see the YAML 1.2 Specification. |
|---|---|


## Includes / Excludes

For the cases where the configuration properties class inherits properties from a parent class, it may be desirable to exclude properties from the parent class. The `includes` and `excludes` members of the @ConfigurationProperties annotation allow for that functionality. The list applies to both local properties and inherited properties.

The names supplied to the includes/excludes list must be the "property" name. For example if a setter method is injected, the property name is the de-capitalized setter name (`setConnectionTimeout` → `connectionTimeout`).


## Change accessors style

Since 3.3, the Micronaut framework supports defining different accessors prefixes for getters and setter other than the default `get` and `set` defined for Java Beans. Annotate your POJO or `@ConfigurationProperties` class with the @AccessorsStyle annotation.

This is useful when you write the getters and setters in a fluent way. For example:

Using

@AccessorsStyle

```java
import io.micronaut.context.annotation.ConfigurationProperties;
import io.micronaut.core.annotation.AccessorsStyle;

@AccessorsStyle(readPrefixes = "", writePrefixes = "") (1)
@ConfigurationProperties("my.engine")
public class EngineConfig {

    private String manufacturer;
    private int cylinders;

    public EngineConfig(String manufacturer, int cylinders) {
        this.manufacturer = manufacturer;
        this.cylinders = cylinders;
    }

    public String manufacturer() { (2)
        return manufacturer;
    }

    public void manufacturer(String manufacturer) { (2)
        this.manufacturer = manufacturer;
    }

    public int cylinders() { (2)
        return cylinders;
    }

    public void cylinders(int cylinders) { (2)
        this.cylinders = cylinders;
    }

}
```

| **1** | The Micronaut framework will use an empty prefix for getters and setters. |
|---|---|
| **2** | Define the getters and setters with an empty prefix. |

Now you can inject `EngineConfig` and use it with `engineConfig.manufacturer()` and `engineConfig.cylinders()` to retrieve the values from configuration.


## Property Type Conversion

The Micronaut framework uses the ConversionService bean to convert values when resolving properties. You can register additional converters for types not supported by Micronaut by defining beans that implement the TypeConverter interface.

The Micronaut framework features some built-in conversions that are useful, which are detailed below.

### Duration Conversion

Durations can be specified by appending the unit with a number. Supported units are `s`, `ms`, `m` etc. The following table summarizes examples:

| Configuration Value | Resulting Value |
|---|---|
| `10ms` | `Duration` of 10 milliseconds |
| `10m` | `Duration` of 10 minutes |
| `10s` | `Duration` of 10 seconds |
| `10d` | `Duration` of 10 days |
| `10h` | `Duration` of 10 hours |
| `10ns` | `Duration` of 10 nanoseconds |
| `PT15M` | `Duration` of 15 minutes using ISO-8601 format |

For example to configure the default HTTP client read timeout:

Using Duration Values

```properties
micronaut.http.client.read-timeout=15s
```

```yaml
micronaut:
  http:
    client:
      read-timeout: 15s
```

```toml
[micronaut]
  [micronaut.http]
    [micronaut.http.client]
      read-timeout="15s"
```

```groovy
micronaut {
  http {
    client {
      readTimeout = "15s"
    }
  }
}
```

```hocon
{
  micronaut {
    http {
      client {
        read-timeout = "15s"
      }
    }
  }
}
```

```json
{
  "micronaut": {
    "http": {
      "client": {
        "read-timeout": "15s"
      }
    }
  }
}
```

### List / Array Conversion

Lists and arrays can be specified in Java properties files as comma-separated values, or in YAML using native YAML lists. The generic types are used to convert the values. For example in YAML:

Specifying lists or arrays in YAML

```properties
my.app.integers[0]=1
my.app.integers[1]=2
my.app.urls[0]=http://foo.com
my.app.urls[1]=http://bar.com
```

```yaml
my:
  app:
    integers:
      - 1
      - 2
    urls:
      - http://foo.com
      - http://bar.com
```

```toml
[my]
  [my.app]
    integers=[
      1,
      2
    ]
    urls=[
      "http://foo.com",
      "http://bar.com"
    ]
```

```groovy
my {
  app {
    integers = [1, 2]
    urls = ["http://foo.com", "http://bar.com"]
  }
}
```

```hocon
{
  my {
    app {
      integers = [1, 2]
      urls = ["http://foo.com", "http://bar.com"]
    }
  }
}
```

```json
{
  "my": {
    "app": {
      "integers": [1, 2],
      "urls": ["http://foo.com", "http://bar.com"]
    }
  }
}
```

For the above example configurations you can define properties to bind to with the target type supplied via generics:

```java
List<Integer> integers;
List<URL> urls;
```

### Readable Bytes

You can annotate any setter parameter with @ReadableBytes to allow the value to be set using a shorthand syntax for specifying bytes, kilobytes etc. For example the following is taken from HttpClientConfiguration:

Using

@ReadableBytes

```java
public void setMaxContentLength(@ReadableBytes int maxContentLength) {
    this.maxContentLength = maxContentLength;
}
```

With the above in place you can set `micronaut.http.client.max-content-length` using the following values:

| Configuration Value | Resulting Value |
|---|---|
| `10mb` | 10 megabytes |
| `10kb` | 10 kilobytes |
| `10gb` | 10 gigabytes |
| `1024` | A raw byte length |

### Formatting Dates

The @Format annotation can be used on setters to specify the date format to use when binding `java.time` date objects.

Using

@Format

for Dates

```java
public void setMyDate(@Format("yyyy-MM-dd") LocalDate date) {
    this.myDate = date;
}
```


## Configuration Builder

Many frameworks and tools already use builder-style classes to construct configuration.

You can use the @ConfigurationBuilder annotation to populate a builder-style class with configuration values. ConfigurationBuilder can be applied to fields or methods in a class annotated with @ConfigurationProperties.

Since there is no consistent way to define builders in the Java world, one or more method prefixes can be specified in the annotation to support builder methods like `withXxx` or `setXxx`. If the builder methods have no prefix, assign an empty string to the parameter.

A configuration prefix can also be specified to tell the Micronaut framework where to look for configuration values. By default, builder methods use the configuration prefix specified in a class-level @ConfigurationProperties annotation.

For example:

@ConfigurationBuilder Example

```java
import io.micronaut.context.annotation.ConfigurationBuilder;
import io.micronaut.context.annotation.ConfigurationProperties;

@ConfigurationProperties("my.engine") // (1)
class EngineConfig {

    @ConfigurationBuilder(prefixes = "with") // (2)
    EngineImpl.Builder builder = EngineImpl.builder();

    @ConfigurationBuilder(prefixes = "with", configurationPrefix = "crank-shaft") // (3)
    CrankShaft.Builder crankShaft = CrankShaft.builder();

    private SparkPlug.Builder sparkPlug = SparkPlug.builder();

    SparkPlug.Builder getSparkPlug() {
        return sparkPlug;
    }

    @ConfigurationBuilder(prefixes = "with", configurationPrefix = "spark-plug") // (4)
    void setSparkPlug(SparkPlug.Builder sparkPlug) {
        this.sparkPlug = sparkPlug;
    }
}
```

@ConfigurationBuilder Example

```kotlin
import io.micronaut.context.annotation.ConfigurationBuilder
import io.micronaut.context.annotation.ConfigurationProperties

@ConfigurationProperties("my.engine") // (1)
internal class EngineConfig {

    @ConfigurationBuilder(prefixes = ["with"])  // (2)
    val builder = EngineImpl.builder()

    @ConfigurationBuilder(prefixes = ["with"], configurationPrefix = "crank-shaft") // (3)
    val crankShaft = CrankShaft.builder()

    @set:ConfigurationBuilder(prefixes = ["with"], configurationPrefix = "spark-plug") // (4)
    var sparkPlug = SparkPlug.builder()
}
```

@ConfigurationBuilder Example

```groovy
import io.micronaut.context.annotation.ConfigurationBuilder
import io.micronaut.context.annotation.ConfigurationProperties

@ConfigurationProperties('my.engine') // (1)
class EngineConfig {

    @ConfigurationBuilder(prefixes = "with") // (2)
    EngineImpl.Builder builder = EngineImpl.builder()

    @ConfigurationBuilder(prefixes = "with", configurationPrefix = "crank-shaft") // (3)
    CrankShaft.Builder crankShaft = CrankShaft.builder()

    SparkPlug.Builder sparkPlug = SparkPlug.builder()

    @ConfigurationBuilder(prefixes = "with", configurationPrefix = "spark-plug") // (4)
    void setSparkPlug(SparkPlug.Builder sparkPlug) {
        this.sparkPlug = sparkPlug
    }
}
```

| **1** | The `@ConfigurationProperties` annotation takes the configuration prefix |
|---|---|
| **2** | The first builder can be configured without the class configuration prefix; it inherits from the above. |
| **3** | The second builder can be configured with the class configuration prefix + the `configurationPrefix` value. |
| **4** | The third builder demonstrates that the annotation can be applied to a method as well as a property. |

|   | By default, only single-argument builder methods are supported. For methods with no arguments, set the `allowZeroArgs` parameter of the annotation to `true`. |
|---|---|

Like in the previous example, we can construct an `EngineImpl`. Since we are using a builder, we can use a factory class to build the engine from the builder.

Factory Bean

```java
import io.micronaut.context.annotation.Factory;

import jakarta.inject.Singleton;

@Factory
class EngineFactory {

    @Singleton
    EngineImpl buildEngine(EngineConfig engineConfig) {
        return engineConfig.builder.build(engineConfig.crankShaft, engineConfig.getSparkPlug());
    }
}
```

Factory Bean

```kotlin
import io.micronaut.context.annotation.Factory
import jakarta.inject.Singleton

@Factory
internal class EngineFactory {

    @Singleton
    fun buildEngine(engineConfig: EngineConfig): EngineImpl {
        return engineConfig.builder.build(engineConfig.crankShaft, engineConfig.sparkPlug)
    }
}
```

Factory Bean

```groovy
import io.micronaut.context.annotation.Factory

import jakarta.inject.Singleton

@Factory
class EngineFactory {

    @Singleton
    EngineImpl buildEngine(EngineConfig engineConfig) {
        engineConfig.builder.build(engineConfig.crankShaft, engineConfig.sparkPlug)
    }
}
```

The engine that was returned can then be injected anywhere an engine is required.

Configuration values can be supplied from one of the PropertySource instances. For example:

Supply Configuration

```java
        Map<String, Object> properties = new HashMap<>();
        properties.put("spec.name", "VehicleBuilderSpec");
        properties.put("my.engine.cylinders"             ,"4");
        properties.put("my.engine.manufacturer"          , "Subaru");
        properties.put("my.engine.crank-shaft.rod-length", 4);
        properties.put("my.engine.spark-plug.name"       , "6619 LFR6AIX");
        properties.put("my.engine.spark-plug.type"       , "Iridium");
        properties.put("my.engine.spark-plug.companyName", "NGK");
        ApplicationContext applicationContext = ApplicationContext.run(properties, "test");

        Vehicle vehicle = applicationContext.getBean(Vehicle.class);
        System.out.println(vehicle.start());
```

Supply Configuration

```kotlin
        val applicationContext = ApplicationContext.run(
                mapOf(
                        "my.engine.cylinders" to "4",
                        "my.engine.manufacturer" to "Subaru",
                        "my.engine.crank-shaft.rod-length" to 4,
                        "my.engine.spark-plug.name" to "6619 LFR6AIX",
                        "my.engine.spark-plug.type" to "Iridium",
                        "my.engine.spark-plug.company" to "NGK"
                ),
                "test"
        )

        val vehicle = applicationContext.getBean(Vehicle::class.java)
        println(vehicle.start())
```

Supply Configuration

```groovy
        ApplicationContext applicationContext = ApplicationContext.run(
                ['my.engine.cylinders'             : '4',
                 'my.engine.manufacturer'          : 'Subaru',
                 'my.engine.crank-shaft.rod-length': 4,
                 'my.engine.spark-plug.name'       : '6619 LFR6AIX',
                 'my.engine.spark-plug.type'       : 'Iridium',
                 'my.engine.spark-plug.companyName': 'NGK'
                ],
                "test"
        )

        Vehicle vehicle = applicationContext.getBean(Vehicle)
        println(vehicle.start())
```

The above example prints: `"Subaru Engine Starting V4 [rodLength=4.0, sparkPlug=Iridium(NGK 6619 LFR6AIX)]"`


## MapFormat

For some use cases it may be desirable to accept a map of arbitrary configuration properties that can be supplied to a bean, especially if the bean represents a third-party API where not all the possible configuration properties are known. For example, a datasource may accept a map of configuration properties specific to a particular database driver, allowing the user to specify any desired options in the map without coding each property explicitly.

For this purpose, the MapFormat annotation lets you bind a map to a single configuration property, and specify whether to accept a flat map of keys to values, or a nested map (where the values may be additional maps).

@MapFormat Example

```java
import io.micronaut.context.annotation.ConfigurationProperties;
import io.micronaut.context.annotation.Requires;
import io.micronaut.core.convert.format.MapFormat;

import jakarta.validation.constraints.Min;
import java.util.Map;

@ConfigurationProperties("my.engine")
public class EngineConfig {

    @Min(1L)
    private int cylinders;

    @MapFormat(transformation = MapFormat.MapTransformation.FLAT) //(1)
    private Map<Integer, String> sensors;

    public int getCylinders() {
        return cylinders;
    }

    public void setCylinders(int cylinders) {
        this.cylinders = cylinders;
    }

    public Map<Integer, String> getSensors() {
        return sensors;
    }

    public void setSensors(Map<Integer, String> sensors) {
        this.sensors = sensors;
    }
}
```

@MapFormat Example

```kotlin
import io.micronaut.context.annotation.ConfigurationProperties
import io.micronaut.core.convert.format.MapFormat
import jakarta.validation.constraints.Min

@ConfigurationProperties("my.engine")
class EngineConfig {

    @Min(1L)
    var cylinders: Int = 0

    @MapFormat(transformation = MapFormat.MapTransformation.FLAT) //(1)
    var sensors: Map<Int, String>? = null
}
```

@MapFormat Example

```groovy
import io.micronaut.context.annotation.ConfigurationProperties
import io.micronaut.core.convert.format.MapFormat

import jakarta.validation.constraints.Min

@ConfigurationProperties('my.engine')
class EngineConfig {

    @Min(1L)
    int cylinders

    @MapFormat(transformation = MapFormat.MapTransformation.FLAT) //(1)
    Map<Integer, String> sensors
}
```

| **1** | Note the `transformation` argument to the annotation; possible values are `MapTransformation.FLAT` (for flat maps) and `MapTransformation.NESTED` (for nested maps) |
|---|---|

EngineImpl

```java
@Singleton
public class EngineImpl implements Engine {

    @Inject
    EngineConfig config;

    @Override
    public Map getSensors() {
        return config.getSensors();
    }

    @Override
    public String start() {
        return "Engine Starting V" + getConfig().getCylinders() +
               " [sensors=" + getSensors().size() + "]";
    }

    public EngineConfig getConfig() {
        return config;
    }

    public void setConfig(EngineConfig config) {
        this.config = config;
    }
}
```

EngineImpl

```kotlin
@Singleton
class EngineImpl : Engine {

    override val sensors: Map<*, *>?
        get() = config!!.sensors

    @Inject
    var config: EngineConfig? = null

    override fun start(): String {
        return "Engine Starting V${config!!.cylinders} [sensors=${sensors!!.size}]"
    }
}
```

EngineImpl

```groovy
@Singleton
class EngineImpl implements Engine {

    @Inject EngineConfig config

    @Override
    Map getSensors() {
        config.sensors
    }

    @Override
    String start() {
        "Engine Starting V$config.cylinders [sensors=${sensors.size()}]"
    }
}
```

Now a map of properties can be supplied to the `my.engine.sensors` configuration property.

Use Map Configuration

```java
Map<String, Object> map = new LinkedHashMap<>(2);
map.put("my.engine.cylinders", "8");

Map<Integer, String> map1 = new LinkedHashMap<>(2);
map1.put(0, "thermostat");
map1.put(1, "fuel pressure");

map.put("my.engine.sensors", map1);

map.put( "spec.name", "VehicleMapFormatSpec");

ApplicationContext applicationContext = ApplicationContext.run(map, "test");

Vehicle vehicle = applicationContext.getBean(Vehicle.class);
System.out.println(vehicle.start());
```

Use Map Configuration

```kotlin
val subMap = mapOf(
    0 to "thermostat",
    1 to "fuel pressure"
)
val map = mapOf(
    "my.engine.cylinders" to "8",
    "my.engine.sensors" to subMap
)

val applicationContext = ApplicationContext.run(map, "test")

val vehicle = applicationContext.getBean(Vehicle::class.java)
println(vehicle.start())
```

Use Map Configuration

```groovy
ApplicationContext applicationContext = ApplicationContext.run(
        ['my.engine.cylinders': '8',
         'my.engine.sensors'  : [0: 'thermostat',
                                 1: 'fuel pressure']],
        "test"
)

def vehicle = applicationContext.getBean(Vehicle)
println(vehicle.start())
```

The above example prints: `"Engine Starting V8 [sensors=2]"`

|   | See the guide for @Configuration and @ConfigurationBuilder to learn more. |
|---|---|


## 4.7 Custom Type Converters

The Micronaut framework includes an extensible type conversion mechanism. To add additional type converters you register beans of type TypeConverter.

The following example shows how to use one of the built-in converters (Map to an Object) or create your own.

Consider the following ConfigurationProperties:

```java
@ConfigurationProperties(MyConfigurationProperties.PREFIX)
public class MyConfigurationProperties {

    public static final String PREFIX = "myapp";

    protected LocalDate updatedAt;

    public LocalDate getUpdatedAt() {
        return updatedAt;
    }
}
```

```kotlin
@ConfigurationProperties(MyConfigurationProperties.PREFIX)
class MyConfigurationProperties {

    var updatedAt: LocalDate? = null
        protected set

    companion object {
        const val PREFIX = "myapp"
    }
}
```

```groovy
@ConfigurationProperties(MyConfigurationProperties.PREFIX)
class MyConfigurationProperties {

    public static final String PREFIX = "myapp"

    protected LocalDate updatedAt

    LocalDate getUpdatedAt() {
        updatedAt
    }
}
```

The type `MyConfigurationProperties` has a property named `updatedAt` of type LocalDate.

To bind this property from a map via configuration:

```java
private static ApplicationContext ctx;

@BeforeAll
static void setupCtx() {
    ctx = ApplicationContext.run(
            new LinkedHashMap<>() {{
                put("myapp.updatedAt", // (1)
                        new LinkedHashMap<String, Integer>() {{
                            put("day", 28);
                            put("month", 10);
                            put("year", 1982);
                        }}
                );
            }}
    );
}

@AfterAll
static void teardownCtx() {
    if(ctx != null) {
        ctx.stop();
    }
}
```

```kotlin
lateinit var ctx: ApplicationContext

@BeforeEach
fun setup() {
    ctx = ApplicationContext.run(
        mapOf(
            "myapp.updatedAt" to mapOf( // (1)
                "day" to 28,
                "month" to 10,
                "year" to 1982
            )
        )
    )
}

@AfterEach
fun teardown() {
    ctx?.close()
}
```

```groovy
@AutoCleanup
@Shared
ApplicationContext ctx = ApplicationContext.run(
        "myapp.updatedAt": [day: 28, month: 10, year: 1982]  // (1)
)
```

| **1** | Note how we match the `myapp` prefix and `updatedAt` property name in our `MyConfigurationProperties` class above |
|---|---|

This won’t work by default, since there is no built-in conversion from `Map` to `LocalDate`. To resolve this, define a custom TypeConverter:

```java
import io.micronaut.context.annotation.Prototype;
import io.micronaut.core.convert.ConversionContext;
import io.micronaut.core.convert.ConversionService;
import io.micronaut.core.convert.TypeConverter;

import java.time.DateTimeException;
import java.time.LocalDate;
import java.util.Map;
import java.util.Optional;

@Prototype
public class MapToLocalDateConverter implements TypeConverter<Map, LocalDate> { // (1)

    private final ConversionService  conversionService;

    public MapToLocalDateConverter(ConversionService conversionService) { // (2)
        this.conversionService = conversionService;
    }

    @Override
    public Optional<LocalDate> convert(Map propertyMap, Class<LocalDate> targetType, ConversionContext context) {
        Optional<Integer> day = conversionService.convert(propertyMap.get("day"), Integer.class);
        Optional<Integer> month = conversionService.convert(propertyMap.get("month"), Integer.class);
        Optional<Integer> year = conversionService.convert(propertyMap.get("year"), Integer.class);
        if (day.isPresent() && month.isPresent() && year.isPresent()) {
            try {
                return Optional.of(LocalDate.of(year.get(), month.get(), day.get())); // (3)
            } catch (DateTimeException e) {
                context.reject(propertyMap, e); // (4)
                return Optional.empty();
            }
        }

        return Optional.empty();
    }
}
```

```kotlin
import io.micronaut.context.annotation.Prototype
import io.micronaut.core.convert.ConversionContext
import io.micronaut.core.convert.ConversionService
import io.micronaut.core.convert.TypeConverter
import java.time.DateTimeException
import java.time.LocalDate
import java.util.Optional
import jakarta.inject.Singleton

@Prototype
class MapToLocalDateConverter : TypeConverter<Map<*, *>, LocalDate> { // (1)
    override fun convert(propertyMap: Map<*, *>, targetType: Class<LocalDate>, context: ConversionContext): Optional<LocalDate> {
        val day = ConversionService.SHARED.convert(propertyMap["day"]!!, Int::class.java)
        val month = ConversionService.SHARED.convert(propertyMap["month"], Int::class.java)
        val year = ConversionService.SHARED.convert(propertyMap["year"], Int::class.java)
        if (day.isPresent && month.isPresent && year.isPresent) {
            try {
                return Optional.of(LocalDate.of(year.get(), month.get(), day.get())) // (2)
            } catch (e: DateTimeException) {
                context.reject(propertyMap, e) // (3)
                return Optional.empty()
            }
        }

        return Optional.empty()
    }
}
```

```groovy
import io.micronaut.core.convert.ConversionService
import io.micronaut.core.convert.TypeConverter

import java.time.DateTimeException
import java.time.LocalDate

@Prototype
class MapToLocalDateConverter implements TypeConverter<Map, LocalDate> { // (1)

    final ConversionService  conversionService

    MapToLocalDateConverter(ConversionService conversionService) { // (2)
        this.conversionService = conversionService;
    }

    @Override
    Optional<LocalDate> convert(Map propertyMap, Class<LocalDate> targetType, ConversionContext context) {
        Optional<Integer> day = conversionService.convert(propertyMap.day, Integer)
        Optional<Integer> month = conversionService.convert(propertyMap.month, Integer)
        Optional<Integer> year = conversionService.convert(propertyMap.year, Integer)
        if (day.present && month.present && year.present) {
            try {
                return Optional.of(LocalDate.of(year.get(), month.get(), day.get())) // (3)
            } catch (DateTimeException e) {
                context.reject(propertyMap, e) // (4)
                return Optional.empty()
            }
        }
        return Optional.empty()
    }
}
```

| **1** | The class implements TypeConverter which has two generic arguments, the type you are converting from, and the type you are converting to |
|---|---|
| **2** | The constructor injects a bean of type `ConversionService`, introduced in Micronaut 4, instead of making static calls to `ConversionService.SHARED` used in previous versions |
| **3** | The implementation delegates to the injected conversion service to convert the values from the Map used to create a `LocalDate` |
| **4** | If an exception occurs during binding, call `reject(..)` which propagates additional information to the container |

|   | It’s possible to add a custom type converter into `ConversionService.SHARED` by registering it in a TypeConverterRegistrar via the service loader. |
|---|---|
