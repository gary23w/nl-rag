---
title: "Micronaut Core (part 4/27)"
source: https://docs.micronaut.io/latest/guide/index.html
domain: micronaut
license: CC-BY-SA-4.0
tags: micronaut framework, micronaut jvm, compile-time injection, microservices framework
fetched: 2026-07-02
part: 4/27
---

## 3.18.4 Bean Fields

By default, Java introspections treat only JavaBean getters/setters or Java 16 record components as bean properties. You can however define classes with public or package protected fields in Java using the `accessKind` member of the @Introspected annotation:

```java
import io.micronaut.core.annotation.Introspected;

@Introspected(accessKind = Introspected.AccessKind.FIELD)
public class User {
    public final String name; // (1)
    public int age = 18; // (2)

    public User(String name) {
        this.name = name;
    }
}
```

```groovy
import io.micronaut.core.annotation.Introspected

@Introspected(accessKind = Introspected.AccessKind.FIELD)
class User {
    public final String name // (1)
    public int age = 18 // (2)

    User(String name) {
        this.name = name
    }
}
```

| **1** | Final fields are treated like read-only properties |
|---|---|
| **2** | Mutable fields are treated like read-write properties |

|   | The `accessKind` accepts an array, so it is possible to allow for both types of accessors but prefer one or the other depending on the order they appear in the annotation. The first one in the list has priority. |
|---|---|

|   | Introspections on fields are not possible in Kotlin because it is not possible to declare fields directly. |
|---|---|


## 3.18.5 Explicit Bean Properties

The @Property annotation can be used on an introspected field or method to make that member an explicit bean property. This is useful when the member does not follow normal JavaBean getter or setter naming rules, or when the property should expose extra metadata such as an external serialized name.

```java
import io.micronaut.core.annotation.Introspected;

@Introspected
class Book {
    private String title;
    private String author = "Ursula Le Guin";

    @Introspected.Property("book_title")
    public String title() {
        return title;
    }

    @Introspected.Property("book_title")
    public void title(String title) {
        this.title = title;
    }

    @Introspected.Property(
        value = "author_name",
        accessKind = Introspected.Property.Access.READ
    )
    public String author() {
        return author;
    }
}
```

```kotlin
import io.micronaut.core.annotation.Introspected

@Introspected
class Book {
    private var title: String? = null
    private val author = "Ursula Le Guin"

    @Introspected.Property("book_title")
    fun title(): String? {
        return title
    }

    @Introspected.Property("book_title")
    fun title(title: String?) {
        this.title = title
    }

    @Introspected.Property(
        value = "author_name",
        accessKind = [Introspected.Property.Access.READ]
    )
    fun author(): String {
        return author
    }
}
```

```groovy
import io.micronaut.core.annotation.Introspected

@Introspected
class Book {
    private String title
    private String author = 'Ursula Le Guin'

    @Introspected.Property('book_title')
    String title() {
        return title
    }

    @Introspected.Property('book_title')
    void title(String title) {
        this.title = title
    }

    @Introspected.Property(
        value = 'author_name',
        accessKind = [Introspected.Property.Access.READ]
    )
    String author() {
        return author
    }
}
```

In the example above, `title()` and `title(String)` are included as read/write bean property accessors even though they are not JavaBean `getTitle` and `setTitle` methods. The `author()` method is included as a read-only property because its `accessKind` only contains `Introspected.Property.Access.READ`.

The `value` member is a shorthand for `name`. The `name` member represents an external property name and is available through the property annotation metadata. It does not change the Micronaut bean property name used with BeanIntrospection lookup methods. If both `value` and `name` are declared, they must contain the same value.

```java
BeanIntrospection<Book> introspection = BeanIntrospection.getIntrospection(Book.class);
BeanProperty<Book, String> property = introspection.getRequiredProperty("title", String.class);
Optional<String> externalName = property.stringValue(Introspected.Property.class, "name");
```

```kotlin
val introspection = BeanIntrospection.getIntrospection(Book::class.java)
val property = introspection.getRequiredProperty("title", String::class.java)
val externalName = property.stringValue(Introspected.Property::class.java, "name")
```

```groovy
BeanIntrospection<Book> introspection = BeanIntrospection.getIntrospection(Book)
BeanProperty<Book, String> property = introspection.getRequiredProperty('title', String)
Optional<String> externalName = property.stringValue(Introspected.Property, 'name')
```

The `accessKind` member controls whether the bean property can be read, written, or both:

- `Introspected.Property.Access.READ` allows the property to be read.
- `Introspected.Property.Access.WRITE` allows the property to be written.
- The default is both `READ` and `WRITE`.

If both a getter and setter exist, Micronaut can still expose a read/write property. Use `accessKind` when a field or method must restrict one side of access, for example read-only or write-only properties. The access declaration applies to the whole bean property. Multiple @Property declarations for the same bean property must declare the same `accessKind`; conflicting declarations are rejected during compilation. When @Property is declared on a field that belongs to the same bean property as getter or setter methods, Micronaut uses the normal bean accessor precedence: getter methods are used for reads and setter methods are used for writes when they are present. The annotated field still contributes the mapped property metadata and can provide field access when a corresponding getter or setter is absent.

Set `ignoreOtherAccessors` to `true` when the annotated member must be used for its access direction even if another field, getter, or setter exists for the same bean property. For example, an annotated field with the default read/write `accessKind` will be used for both reads and writes instead of same-name getter and setter methods.


## Jackson Annotations

When Jackson annotations are present on an introspected type, Micronaut maps the following annotations to @Property at compile time:

- `com.fasterxml.jackson.annotation.JsonProperty`
- `com.fasterxml.jackson.annotation.JsonGetter`
- `com.fasterxml.jackson.annotation.JsonSetter`

This means Jackson-style property names are visible through Micronaut bean property annotation metadata, and Jackson-annotated methods that do not follow JavaBean naming rules can still be recognized as bean properties.

```java
import com.fasterxml.jackson.annotation.JsonGetter;
import com.fasterxml.jackson.annotation.JsonSetter;
import io.micronaut.core.annotation.Introspected;

@Introspected
class User {
    private String displayName;

    @JsonGetter("display_name")
    public String displayName() {
        return displayName;
    }

    @JsonSetter("display_name")
    public void displayName(String displayName) {
        this.displayName = displayName;
    }
}
```

```kotlin
import com.fasterxml.jackson.annotation.JsonGetter
import com.fasterxml.jackson.annotation.JsonSetter
import io.micronaut.core.annotation.Introspected

@Introspected
class User {
    private var displayName: String? = null

    @JsonGetter("display_name")
    fun displayName(): String? {
        return displayName
    }

    @JsonSetter("display_name")
    fun displayName(displayName: String?) {
        this.displayName = displayName
    }
}
```

```groovy
import com.fasterxml.jackson.annotation.JsonGetter
import com.fasterxml.jackson.annotation.JsonSetter
import io.micronaut.core.annotation.Introspected

@Introspected
class User {
    private String displayName

    @JsonGetter('display_name')
    String displayName() {
        return displayName
    }

    @JsonSetter('display_name')
    void displayName(String displayName) {
        this.displayName = displayName
    }
}
```

The `displayName` methods are treated as a bean property, and the external name `display_name` is available from the mapped @Property metadata. For `JsonGetter` and `JsonSetter`, read and write availability is determined by the available bean property reader and writer. Jackson annotations do not set `ignoreOtherAccessors`, so Micronaut keeps the same accessor precedence as Jackson Databind: getters are preferred for reads and setters are preferred for writes when they exist.

For `JsonProperty`, Micronaut also maps Jackson’s `access` member:

- `JsonProperty.Access.READ_ONLY` maps to `Introspected.Property.Access.READ`.
- `JsonProperty.Access.WRITE_ONLY` maps to `Introspected.Property.Access.WRITE`.
- `JsonProperty.Access.AUTO` and `JsonProperty.Access.READ_WRITE` map to both read and write access.

Because `accessKind` is property-level, multiple Jackson annotations that map to the same bean property must agree on the mapped access.


## 3.18.6 Constructor Methods

For classes with multiple constructors, apply the @Creator annotation to the constructor to use.

```java
import io.micronaut.core.annotation.Creator;
import io.micronaut.core.annotation.Introspected;

import javax.annotation.concurrent.Immutable;

@Introspected
@Immutable
public class Vehicle {

    private final String make;
    private final String model;
    private final int axles;

    public Vehicle(String make, String model) {
        this(make, model, 2);
    }

    @Creator // (1)
    public Vehicle(String make, String model, int axles) {
        this.make = make;
        this.model = model;
        this.axles = axles;
    }

    public String getMake() {
        return make;
    }

    public String getModel() {
        return model;
    }

    public int getAxles() {
        return axles;
    }
}
```

```kotlin
import io.micronaut.core.annotation.Creator
import io.micronaut.core.annotation.Introspected

import javax.annotation.concurrent.Immutable

@Introspected
@Immutable
class Vehicle @Creator constructor(val make: String, val model: String, val axles: Int) { // (1)

    constructor(make: String, model: String) : this(make, model, 2) {}
}
```

```groovy
import io.micronaut.core.annotation.Creator
import io.micronaut.core.annotation.Introspected

import javax.annotation.concurrent.Immutable

@Introspected
@Immutable
class Vehicle {

    final String make
    final String model
    final int axles

    Vehicle(String make, String model) {
        this(make, model, 2)
    }

    @Creator // (1)
    Vehicle(String make, String model, int axles) {
        this.make = make
        this.model = model
        this.axles = axles
    }
}
```

| **1** | The @Creator annotation denotes which constructor to use |
|---|---|

|   | This class has no default constructor, so calls to instantiate without arguments throw an InstantiationException. |
|---|---|


## 3.18.7 Static Creator Methods

The @Creator annotation can be applied to static methods that create class instances.

```java
import io.micronaut.core.annotation.Creator;
import io.micronaut.core.annotation.Introspected;

import javax.annotation.concurrent.Immutable;

@Introspected
@Immutable
public class Business {

    private final String name;

    private Business(String name) {
        this.name = name;
    }

    @Creator // (1)
    public static Business forName(String name) {
        return new Business(name);
    }

    public String getName() {
        return name;
    }
}
```

```kotlin
import io.micronaut.core.annotation.Creator
import io.micronaut.core.annotation.Introspected

import javax.annotation.concurrent.Immutable

@Introspected
@Immutable
class Business private constructor(val name: String) {
    companion object {

        @Creator // (1)
        fun forName(name: String): Business {
            return Business(name)
        }
    }

}
```

```groovy
import io.micronaut.core.annotation.Creator
import io.micronaut.core.annotation.Introspected

import javax.annotation.concurrent.Immutable

@Introspected
@Immutable
class Business {

    final String name

    private Business(String name) {
        this.name = name
    }

    @Creator // (1)
    static Business forName(String name) {
        new Business(name)
    }
}
```

| **1** | The @Creator annotation is applied to the static method which instantiates the class |
|---|---|

|   | There can be multiple "creator" methods annotated. If there is one without arguments, it will be the default construction method. The first method with arguments will be used as the primary construction method. |
|---|---|


## 3.18.8 Builders

If a type can only be constructed via the builder pattern then you can use the `builder` member of the @Introspected annotation to generate a dynamic builder. For example given this class:

```java
@ReflectiveAccess
@Introspected(builder = @Introspected.IntrospectionBuilder(
    builderClass = Person.Builder.class
))
public class Person {
    private final String name;
    private final int age;
    private Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    public static Builder builder() {
        return new Builder();
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        Person person = (Person) o;

        if (age != person.age) return false;
        return Objects.equals(name, person.name);
    }

    @Override
    public int hashCode() {
        int result = name != null ? name.hashCode() : 0;
        result = 31 * result + age;
        return result;
    }

    public static final class Builder {
        private String name;
        private int age;

        public Builder name(String name) {
            this.name = name;
            return this;
        }

        public Builder age(int age) {
            this.age = age;
            return this;
        }

        public Person build() {
            Objects.requireNonNull(name);
            if (age < 1) {
                throw new IllegalArgumentException("Age must be a positive number");
            }
            return new Person(name, age);
        }
    }
}
```

```groovy
import io.micronaut.core.annotation.Introspected
@CompileStatic
@Introspected(builder = @Introspected.IntrospectionBuilder(
        builderClass = Person.Builder.class
))
@EqualsAndHashCode
class Person {
    final String name
    final int age

    private Person(String name, int age) {
        this.name = name
        this.age = age
    }

    static Builder builder() {
        new Builder()
    }

    static final class Builder {
        private String name
        private int age

        Builder name(String name) {
            this.name = name
            this
        }

        Builder age(int age) {
            this.age = age
            this
        }

        Person build() {
            Objects.requireNonNull(name)
            if (age < 1) {
                throw new IllegalArgumentException("Age must be a positive number")
            }
            new Person(name, age)
        }
    }
}
```

You can use the `builder()` method of the BeanIntrospection API to construct the instance:

```java
BeanIntrospection<Person> introspection = BeanIntrospection.getIntrospection(Person.class);
BeanIntrospection.Builder<Person> builder = introspection.builder();
Person person = builder
    .with("age", 25)
    .with("name", "Fred")
    .build();
```

```groovy
BeanIntrospection<Person> introspection = BeanIntrospection.getIntrospection(Person.class);
BeanIntrospection.Builder<Person> builder = introspection.builder()
Person person = builder
        .with("age", 25)
        .with("name", "Fred")
        .build()
```

|   | The `builder()` method also works regardless if the type uses a builder and can be used as a general abstraction for object construction. Note however that there is a slight performance overhead vs direct instantiation via the `instantiate()` method, hence the `hasBuilder()` method can be checked if optimized code paths are needed. |
|---|---|

|   | Introspection Builder does not work with Groovy `@Builder` AST. |
|---|---|


## 3.18.9 Introspect Enums

It is possible to introspect enums as well. Add the annotation to the enum, and it can be constructed through the standard `valueOf` method.


## 3.18.10 Use the @Introspected Annotation on a Configuration Class

If the class to introspect is already compiled and not under your control, an alternative option is to define a configuration class with the `classes` member of the @Introspected annotation set.

```java
import io.micronaut.core.annotation.Introspected;

@Introspected(classes = Person.class)
public class PersonConfiguration {
}
```

```kotlin
import io.micronaut.core.annotation.Introspected

@Introspected(classes = [Person::class])
class PersonConfiguration
```

```groovy
import io.micronaut.core.annotation.Introspected

@Introspected(classes = Person)
class PersonConfiguration {
}
```

In the above example the `PersonConfiguration` class generates introspections for the `Person` class.

|   | You can also use the `packages` member of the @Introspected which package scans at compile time and generates introspections for all classes within a package. Note however this feature is currently regarded as experimental. |
|---|---|


## 3.18.11 Write an AnnotationMapper to Introspect Existing Annotations

If there is an existing annotation that you wish to introspect by default you can write an AnnotationMapper.

An example of this is EntityIntrospectedAnnotationMapper which ensures all beans annotated with `javax.persistence.Entity` are introspectable by default.

|   | The `AnnotationMapper` must be on the annotation processor classpath. |
|---|---|


## 3.18.12 The BeanWrapper API

A BeanProperty provides raw access to read and write a property value for a given class and does not provide any automatic type conversion.

It is expected that the values you pass to the `set` and `get` methods match the underlying property type, otherwise an exception will occur.

To provide additional type conversion smarts the BeanWrapper interface allows wrapping an existing bean instance and setting and getting properties from the bean, plus performing type conversion as necessary.

```java
final BeanWrapper<Person> wrapper = BeanWrapper.getWrapper(new Person("Fred")); // (1)

wrapper.setProperty("age", "20"); // (2)
int newAge = wrapper.getRequiredProperty("age", int.class); // (3)

System.out.println("Person's age now " + newAge);
```

```kotlin
val wrapper = BeanWrapper.getWrapper(Person("Fred")) // (1)

wrapper.setProperty("age", "20") // (2)
val newAge = wrapper.getRequiredProperty("age", Int::class.java) // (3)

println("Person's age now $newAge")
```

```groovy
final BeanWrapper<Person> wrapper = BeanWrapper.getWrapper(new Person("Fred")) // (1)

wrapper.setProperty("age", "20") // (2)
int newAge = wrapper.getRequiredProperty("age", Integer) // (3)

println("Person's age now $newAge")
```

| **1** | Use the static `getWrapper` method to obtain a BeanWrapper for a bean instance. |
|---|---|
| **2** | You can set properties, and the BeanWrapper will perform type conversion, or throw ConversionErrorException if conversion is not possible. |
| **3** | You can retrieve a property using `getRequiredProperty` and request the appropriate type. If the property doesn’t exist a IntrospectionException is thrown, and if it cannot be converted a ConversionErrorException is thrown. |


## 3.18.13 Kotlin and Bean Introspection

You can annotate a Kotlin Data Class with @Introspected:

Kotlin Data Class annotated with @Introspected

```kotlin
@Introspected
data class UserDataClass(val name: String)
```

and instantiate it with the BeanIntrospection API:

Kotlin Data Class instantiated via BeanIntrospection API

|   | Kotlin Inline Value Classes are not supported yet by the BeanIntrospection API. |
|---|---|


## 3.19 Bean Mappers

Since 4.1.x the @Mapper annotation can be used on any abstract method to automatically create a mapping between one type and another. Since 4.8.x the annotation can also be used for merging beans.

Inspired by similar functionality in libraries like Map Struct, a `Mapper` uses the Bean Introspection and Expressions features, built into the Micronaut Framework, which are already reflection free.

|   | For Mapping, base and target types need to be introspected. |
|---|---|

### @Mapper Example

Given the following types:

```java
@Introspected
public record ContactForm(String firstName, String lastName) {
}
```

```kotlin
@Introspected
data class ContactForm(val firstName: String, val lastName: String)
```

```groovy
@Introspected
class ContactForm {
    String firstName
    String lastName
}
```

```java
@Introspected
public record ContactEntity(Long id, String firstName, String lastName) {
}
```

```kotlin
@Introspected
data class ContactEntity(var id: Long? = null, val firstName: String, val lastName: String)
```

```groovy
@Introspected
class ContactEntity {
    Long id
    String firstName
    String lastName
}
```

You can write an interface to define a mapping between both types by simply annotating a method with @Mapper.

```java
import io.micronaut.context.annotation.Mapper;

public interface ContactMappers {
    @Mapper
    ContactEntity toEntity(ContactForm contactForm);
}
```

```kotlin
import io.micronaut.context.annotation.Mapper

interface ContactMappers {
    @Mapper
    fun toEntity(contactForm: ContactForm) : ContactEntity
}
```

```groovy
import io.micronaut.context.annotation.Mapper

interface ContactMappers {
    @Mapper
    ContactEntity toEntity(ContactForm contactForm)
}
```

The Micronaut compiler generates an implementation the previous an interface at compilation-time.

You can then inject a bean of type `ContactMappers` and easily map from one type to another.

```java
ContactMappers contactMappers = context.getBean(ContactMappers.class);
ContactEntity contactEntity = contactMappers.toEntity(new ContactForm("John", "Snow"));
assertEquals("John", contactEntity.firstName());
assertEquals("Snow", contactEntity.lastName());
```

```kotlin
val contactMappers = context.getBean(ContactMappers::class.java)
val entity : ContactEntity = contactMappers.toEntity(ContactForm("John", "Snow"))
Assertions.assertEquals("John", entity.firstName)
Assertions.assertEquals("Snow", entity.lastName)
```

```groovy
ContactMappers contactMappers = context.getBean(ContactMappers)
ContactEntity contactEntity = contactMappers.toEntity(new ContactForm(firstName: "John", lastName: "Snow"))
assertEquals("John", contactEntity.firstName)
assertEquals("Snow", contactEntity.lastName)
```

### @Mapping Example

Each abstract method can define a single @Mapper annotation or one or many @Mapping annotations to define how properties map onto the target type.

For example, given the following type:

```java
import io.micronaut.core.annotation.Introspected;

@Introspected
public record Product(
    String name,
    double price,
    String manufacturer) {
}
```

```kotlin
@Introspected
data class Product(val name: String, val price: Double, val manufacturer: String)
```

```groovy
import groovy.transform.Canonical
import io.micronaut.core.annotation.Introspected

@Canonical
@Introspected
class Product {
    String name
    double price
    String manufacturer
}
```

It is common to want to alter this type’s representation in HTTP responses. For example, consider this response type:

```java
import io.micronaut.core.annotation.Introspected;

@Introspected
public record ProductDTO(String name, String price, String distributor) {
}
```

```kotlin
@Introspected
data class ProductDTO(val name: String, val price: String, val distributor: String)
```

```groovy
import io.micronaut.core.annotation.Introspected;

@Introspected
@Canonical
class ProductDTO {
    String name
    String price
    String distributor
}
```

Here the `price` property is of a different type and an extra property exists called `distributor`. You could write manual logic to deal the mapping and these differences, or you could define a mapping:

```java
import io.micronaut.context.annotation.Mapper.Mapping;
import jakarta.inject.Singleton;

@Singleton
public interface ProductMappers {
    @Mapping(
        to = "price",
        from = "#{product.price * 2}",
        format = "$#.00"
    )
    @Mapping(
        to = "distributor",
        from = "#{this.getDistributor()}"
    )
    ProductDTO toProductDTO(Product product);

    default String getDistributor() {
        return "Great Product Company";
    }
}
```

```kotlin
import io.micronaut.context.annotation.Mapper.Mapping
import jakarta.inject.Singleton

@Singleton
abstract class ProductMappers {
    @Mapping(to = "price", from = "#{product.price * 2}", format = "$#.00")
    @Mapping(to = "distributor", from = "#{this.getDistributor()}")
    abstract fun toProductDTO(product: Product): ProductDTO
    fun getDistributor() : String = "Great Product Company"
}
```

```groovy
import io.micronaut.context.annotation.Mapper.Mapping
import jakarta.inject.Singleton

@Singleton
interface ProductMappers {
    @Mapping(
        to = "price",
        from = "#{product.price * 2}",
        format = '$#.00'
    )
    @Mapping(
        to = "distributor",
        from = "#{this.getDistributor()}"
    )
    ProductDTO toProductDTO(Product product);

    default String getDistributor() {
        return "Great Product Company"
    }
}
```

The `from` member can be used to define either a property name on the source type or an expression that reads values from the method argument and transforms them in whatever way you choose, including invoking other methods of the instance.

|   | A `@Mapping` definition is only needed if you need to apply a transformation for the mapping to be successful. Other properties will be automatically mapped and converted. |
|---|---|

You can retrieve from the context or inject a bean of type `ProductMappers`. Then, you can use the `toProductDTO` method to map from the Product type to the ProductDTO type:

```java
ProductMappers productMappers = context.getBean(ProductMappers.class);

ProductDTO productDTO = productMappers.toProductDTO(new Product(
    "MacBook",
    910.50,
    "Apple"
));

assertEquals("MacBook", productDTO.name());
assertEquals("$1821.00", productDTO.price());
assertEquals("Great Product Company", productDTO.distributor());
```

```kotlin
val productMappers = context.getBean(ProductMappers::class.java)
val (name, price, distributor) = productMappers.toProductDTO(
    Product(
        "MacBook",
        910.50,
        "Apple"
    )
)
Assertions.assertEquals("MacBook", name)
Assertions.assertEquals("$1821.00", price)
Assertions.assertEquals("Great Product Company", distributor)
```

```groovy
given:
ProductMappers productMappers = context.getBean(ProductMappers.class)

when:
ProductDTO productDTO = productMappers.toProductDTO(new Product(
        "MacBook",
        910.50,
        "Apple"
))

then:
productDTO.name == 'MacBook'
productDTO.price == '$1821.00'
productDTO.distributor == "Great Product Company"
```


## 3.19.1 Bean Mappers Merging

Given the following types:

```java
@Introspected
record ChristmasPresent(
    String packagingColor,
    String type,
    Float weight,
    String greetingCard
) {
}

@Introspected
record PresentPackaging(
    Float weight,
    String color
) {
}

@Introspected
record Present(
    Float weight,
    String type
) {
}
```

```groovy
@Canonical
@Introspected
class ChristmasPresent {
    String packagingColor
    String type
    Float weight
    String greetingCard
}

@Canonical
@Introspected
class PresentPackaging {
    Float weight
    String color
}

@Canonical
@Introspected
class Present {
    Float weight
    String type
}
```

You can write an interface and method to merge the types by simply specifying two or more arguments to the method and annotating the method with @Mapper. Optionally, define custom mapping rules using @Mapping.

```java
import io.micronaut.context.annotation.Mapper.Mapping;

public interface ChristmasMappers {

    @Mapping(from = "packaging.color", to = "packagingColor")
    @Mapping(from = "#{packaging.weight + present.weight}", to = "weight")
    @Mapping(from = "#{'Merry christmas'}", to = "greetingCard")
    ChristmasPresent merge(PresentPackaging packaging, Present present);

}
```

```groovy
import io.micronaut.context.annotation.Mapper.Mapping

interface ChristmasMappers {

    @Mapping(from = "packaging.color", to = "packagingColor")
    @Mapping(from = "#{packaging.weight + present.weight}", to = "weight")
    @Mapping(from = "#{'Merry christmas'}", to = "greetingCard")
    ChristmasPresent merge(PresentPackaging packaging, Present present)

}
```

You can then inject the type `ChristmasMappers` and easily merge the types.

```java
ChristmasMappers mappers = context.getBean(ChristmasMappers.class);

ChristmasPresent result = mappers.merge(
    new PresentPackaging(1f, "red"),
    new Present(10f, "teddy bear")
);

assertEquals(11f, result.weight());
assertEquals("red", result.packagingColor());
assertEquals("teddy bear", result.type());
assertEquals("Merry christmas", result.greetingCard());
```

```groovy
given:
ChristmasMappers mappers = context.getBean(ChristmasMappers.class)

when:
ChristmasPresent result = mappers.merge(
        new PresentPackaging(1f, "red"),
        new Present(10f, "teddy bear")
)

then:
11 == result.weight
"red" == result.packagingColor
"teddy bear" == result.type
"Merry christmas" == result.greetingCard
```


## 3.19.1.1 Merging Strategy

And much more is possible! See more mapping examples in the following snippet.

```java
public interface AdditionalMappers {

    @Mapper // (1)
    ChristmasPresent merge(PresentPackaging packaging, Present present, Card christmasCard);

    @Mapping(
        from = "#{updateFields.get('christmasCard') + '!!'}", to = "greetingCard"
    ) // (2)
    ChristmasPresent update(ChristmasPresent present, Map<String, Object> updateFields);

    @Mapper(
        mergeStrategy = "add-numbers",
        value = {
            @Mapping(from = "packaging.color", to = "packagingColor")
        }
    ) // (3)
    ChristmasPresent mergeWithMergeStrategy(PresentPackaging packaging, Present present);

    @Singleton
    @Named("add-numbers")
    class MyMergeStrategy implements MergeStrategy {
        @Override
        public Object merge(Object currentValue, Object value, Object valueOwner, String propertyName, String mappedPropertyName) {
            if (currentValue instanceof Float a && value instanceof Float b) {
                return a + b;
            }
            return value;
        }
    }

    @ReflectiveAccess
    @Introspected
    record Card(
        String greetingCard
    ) {
    }

}
```

```groovy
interface AdditionalMappers {

    @Mapper // (1)
    ChristmasPresent merge(PresentPackaging packaging, Present present, Card christmasCard)

    @Mapping(
        from = "#{updateFields.get('christmasCard') + '!!'}", to = "greetingCard"
    ) // (2)
    ChristmasPresent update(ChristmasPresent present, Map<String, Object> updateFields)

    @Mapper(mergeStrategy = "add-numbers") // (3)
    @Mapping(from = "packaging.color", to = "packagingColor")
    ChristmasPresent mergeWithMergeStrategy(PresentPackaging packaging, Present present)

    @Singleton
    @Named("add-numbers")
    class MyMergeStrategy implements MergeStrategy {
        @Override
        Object merge(Object currentValue, Object value, Object valueOwner, String propertyName, String mappedPropertyName) {
            if (currentValue instanceof Float && value instanceof Float) {
                return (Float) (currentValue + value)
            }
            return value
        }
    }

    @Canonical
    @Introspected
    class Card {
        String greetingCard
    }

}
```

| **1** | Merge three or more types. |
|---|---|
| **2** | Create mappings that specify `Map` as a parameter and define mappings for this parameter. |
| **3** | Define a custom merge strategy as a singleton and use it for mapping. |


## 3.20 Bean Validation

See the Micronaut Validation documentation.


## 3.21 Bean Annotation Metadata

The methods provided by Java’s AnnotatedElement API in general don’t provide the ability to introspect annotations without loading the annotations themselves. Nor do they provide any ability to introspect annotation stereotypes (often called meta-annotations; an annotation stereotype is where an annotation is annotated with another annotation, essentially inheriting its behaviour).

To solve this problem many frameworks produce runtime metadata or perform expensive reflection to analyze the annotations of a class.

The Micronaut framework instead produces this annotation metadata at compile time, avoiding expensive reflection and saving memory.

The BeanContext API can be used to obtain a reference to a BeanDefinition which implements the AnnotationMetadata interface.

For example the following code obtains all bean definitions annotated with a particular stereotype:

Lookup Bean Definitions by Stereotype

```java
BeanContext beanContext = ... // obtain the bean context
Collection<BeanDefinition> definitions =
    beanContext.getBeanDefinitions(Qualifiers.byStereotype(Controller.class))

for (BeanDefinition definition : definitions) {
    AnnotationValue<Controller> controllerAnn = definition.getAnnotation(Controller.class);
    // do something with the annotation
}
```

The above example finds all BeanDefinition instances annotated with `@Controller` whether `@Controller` is used directly or inherited via an annotation stereotype.

Note that the `getAnnotation` method and the variations of the method return an AnnotationValue type and not a Java annotation. This is by design, and you should generally try to work with this API when reading annotation values, since synthesizing a proxy implementation is worse from a performance and memory consumption perspective.

If you require a reference to an annotation instance you can use the `synthesize` method, which creates a runtime proxy that implements the annotation interface:

Synthesizing Annotation Instances

```java
Controller controllerAnn = definition.synthesize(Controller.class);
```

This approach is not recommended however, as it requires reflection and increases memory consumption due to the use of runtime generated proxies, and should be used as a last resort, for example if you need an instance of the annotation to integrate with a third-party library.

### Annotation Inheritance

The Micronaut framework will respect the rules defined in Java’s AnnotatedElement API with regard to annotation inheritance:

- Annotations meta-annotated with Inherited will be available via the `getAnnotation*` methods of the AnnotationMetadata API whilst those directly declared are available via the `getDeclaredAnnotation*` methods.
- Annotations not meta-annotated with Inherited will not be included in the metadata

The Micronaut framework differs from the AnnotatedElement API in that it extends these rules to methods and method parameters such that:

- Any annotations annotated with AnnotatedElement and present on a method of interface or super class `A` that is overridden by child interface or class `B` will be inherited into the AnnotationMetadata retrievable via the ExecutableMethod API from a BeanDefinition or an AOP interceptor.
- Any annotations annotated with Inherited and present on a method parameter of interface or super class `A` that is overridden by child interface or class `B` will be inherited into the AnnotationMetadata retrievable via the Argument interface from the `getArguments` method of the ExecutableMethod API.

In general behaviour which you may wish to override is not inherited by default including Bean Scopes, Bean Qualifiers, Bean Conditions, Validation Rules and so on.

If you wish a particular scope, qualifier, or set of requirements to be inherited when subclassing then you can define a meta-annotation that is annotated with `@Inherited`. For example:

Defining Inherited Meta Annotations

```java
import io.micronaut.context.annotation.AliasFor;
import io.micronaut.context.annotation.Requires;
import io.micronaut.core.annotation.AnnotationMetadata;
import jakarta.inject.Named;
import jakarta.inject.Singleton;

import java.lang.annotation.Inherited;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;

@Inherited // (1)
@Retention(RetentionPolicy.RUNTIME)
@Requires(property = "datasource.url") // (2)
@Named // (3)
@Singleton // (4)
public @interface SqlRepository {
    @AliasFor(annotation = Named.class, member = AnnotationMetadata.VALUE_MEMBER) // (5)
    String value() default "";
}
```

Defining Inherited Meta Annotations

```kotlin
import io.micronaut.context.annotation.Requires
import jakarta.inject.Named
import jakarta.inject.Singleton
import java.lang.annotation.Inherited

@Inherited // (1)
@kotlin.annotation.Retention(AnnotationRetention.RUNTIME)
@Requires(property = "datasource.url") // (2)
@Named // (3)
@Singleton // (4)
annotation class SqlRepository(
    val value: String = ""
)
```

Defining Inherited Meta Annotations

```groovy
import io.micronaut.context.annotation.AliasFor
import io.micronaut.context.annotation.Requires
import io.micronaut.core.annotation.AnnotationMetadata
import jakarta.inject.Named
import jakarta.inject.Singleton

import java.lang.annotation.Inherited
import java.lang.annotation.Retention
import java.lang.annotation.RetentionPolicy

@Inherited // (1)
@Retention(RetentionPolicy.RUNTIME)
@Requires(property = "datasource.url") // (2)
@Named // (3)
@Singleton // (4)
@interface SqlRepository {
    @AliasFor(annotation = Named.class, member = AnnotationMetadata.VALUE_MEMBER) // (5)
    String value() default "";
}
```

| **1** | The annotation is declared as `@Inherited` |
|---|---|
| **2** | Bean Conditions will be inherited by child classes |
| **3** | Bean Qualifiers will be inherited by child classes |
| **4** | Bean Scopes will be inherited by child classes |
| **5** | You can also alias annotations and they will be inherited |

With this meta-annotation in place you can add the annotation to a super class:

Using Inherited Meta Annotations on a Super Class

```java
@SqlRepository
public abstract class BaseSqlRepository {
}
```

Using Inherited Meta Annotations on a Super Class

```kotlin
@SqlRepository
abstract class BaseSqlRepository
```

Using Inherited Meta Annotations on a Super Class

```groovy
@SqlRepository
abstract class BaseSqlRepository {
}
```

And then a subclass will inherit all the annotations:

Inherting Annotations in a Child Class

```java
import jakarta.inject.Named;
import javax.sql.DataSource;

@Named("bookRepository")
public class BookRepository extends BaseSqlRepository {
    private final DataSource dataSource;

    public BookRepository(DataSource dataSource) {
        this.dataSource = dataSource;
    }
}
```

Inherting Annotations in a Child Class

```kotlin
import jakarta.inject.Named
import javax.sql.DataSource

@Named("bookRepository")
class BookRepository(private val dataSource: DataSource) : BaseSqlRepository()
```

Inherting Annotations in a Child Class

```groovy
import jakarta.inject.Named
import javax.sql.DataSource

@Named("bookRepository")
class BookRepository extends BaseSqlRepository {
    private final DataSource dataSource

    BookRepository(DataSource dataSource) {
        this.dataSource = dataSource
    }
}
```

|   | A child class must at least have one bean definition annotation such as a scope or qualifier. |
|---|---|

### Aliasing / Mapping Annotations

There are times when you may want to alias the value of an annotation member to the value of another annotation member. To do this, use the @AliasFor annotation.

A common use case is for example when an annotation defines the `value()` member, but also supports other members. for example the @Client annotation:

The @Client Annotation

```java
public @interface Client {

    /**
     * @return The URL or service ID of the remote service
     */
    @AliasFor(member = "id") (1)
    String value() default "";

    /**
     * @return The ID of the client
     */
    @AliasFor(member = "value") (2)
    String id() default "";
}
```

| **1** | The `value` member also sets the `id` member |
|---|---|
| **2** | The `id` member also sets the `value` member |

With these aliases in place, whether you define `@Client("foo")` or `@Client(id="foo")`, both the `value` and `id` members will be set, making it easier to parse and work with the annotation.

If you do not have control over the annotation, another approach is to use an AnnotationMapper. To create an `AnnotationMapper`, do the following:

- Implement the AnnotationMapper interface
- Define a `META-INF/services/io.micronaut.inject.annotation.AnnotationMapper` file referencing the implementation class
- Add the JAR file containing the implementation to the `annotationProcessor` classpath (`kapt` for Kotlin)

|   | Because `AnnotationMapper` implementations must be on the annotation processor classpath, they should generally be in a project that includes few external dependencies to avoid polluting the annotation processor classpath. |
|---|---|

The following is an example `AnnotationMapper` that improves the introspection capabilities of JPA entities.

EntityIntrospectedAnnotationMapper Mapper Example

```java
public class EntityIntrospectedAnnotationMapper implements NamedAnnotationMapper {
    @Override
    public String getName() {
        return "javax.persistence.Entity";
    }

    @Override
    public List<AnnotationValue<?>> map(AnnotationValue<Annotation> annotation, VisitorContext visitorContext) { (1)
        (2)
        return Arrays.asList(
                AnnotationValue.builder(Introspected.class).build(),
                AnnotationValue.builder(ReflectiveAccess.class).build()
        );
    }
}
```

| **1** | The `map` method receives a AnnotationValue with the values for the annotation. |
|---|---|
| **2** | One or more annotations can be returned. |

|   | The example above implements the NamedAnnotationMapper interface which allows annotations to be mixed with runtime code. To operate against a concrete annotation type, use TypedAnnotationMapper instead. However, TypedAnnotationMapper requires both the mapper and the annotation class itself to be available on the annotation processor classpath of the consuming project. If the annotation and mapper are defined in regular application code and not packaged as an annotation-processor-visible dependency, use NamedAnnotationMapper instead. |
|---|---|


## 3.22 Importing Beans from Libraries

You can use the @Import annotation to import beans from external, already compiled libraries that use JSR-330 annotations.

|   | Bean import is currently only supported in the Java language as other languages have limitations on classpath scanning during source code processing. |
|---|---|

For example, to import the JSR-330 TCK into an application, add a dependency on the TCK:

`implementation("io.micronaut:jakarta.inject-tck:2.0.1")` `<dependency> <groupId>io.micronaut</groupId> <artifactId>jakarta.inject-tck</artifactId> <version>2.0.1</version> </dependency>`

Then define the `@Import` annotation on your `Application` class:

```java
package example;

import io.micronaut.context.annotation.Import;

@Import( (1)
        packages = { (2)
                "org.atinject.tck.auto",
                "org.atinject.tck.auto.accessories"},
        annotated = "*") (3)
public class Application {
}
```

| **1** | The @Import is defined |
|---|---|
| **2** | The `packages` to import are defined. Note that the Micronaut framework will not recurse through sub-packages so sub-packages need to be listed explicitly |
| **3** | By default, Micronaut framework will only import classes that feature a scope or a qualifier. By using `*` you can make every type a bean. |

|   | In general `@Import` should be used in applications rather than libraries since if two libraries import the same beans the result will likely be a NonUniqueBeanException |
|---|---|


## 3.23 Importing Classes from Libraries

As an alternative to the @Import annotation the @ClassImport annotation allows to process already compiled classes as if they were ordinary non-compiled classes. Internally all the type visitors will be run, allowing to create necessary metadata.

|   | Class import is currently only supported in the Java language as other languages have limitations on classpath scanning during source code processing. |
|---|---|

For example, to import the JSR-330 TCK into an application, add a dependency on the TCK:

`implementation("io.micronaut:jakarta.inject-tck:2.0.1")` `<dependency> <groupId>io.micronaut</groupId> <artifactId>jakarta.inject-tck</artifactId> <version>2.0.1</version> </dependency>`

Then define the `@ClassImport` annotation on your `Application` class:

```java
package example;

import io.micronaut.context.annotation.ClassImport;
import io.micronaut.context.annotation.Bean;

@ClassImport( (1)
        packages = { (2)
                "org.atinject.tck.auto",
                "org.atinject.tck.auto.accessories"},
        annotate = Bean.class) (3)
public class Application {
}
```

| **1** | The @ClassImport is defined |
|---|---|
| **2** | The `packages` to import are defined. Note that the Micronaut framework will not recurse through sub-packages so sub-packages need to be listed explicitly |
| **3** | The `annotate` allows to specify which annotation should be added to all the classes in the packages. |

In the same way, it’s possible to import classes required for Micronaut Serialization or Micronaut Validation.

```java
package example;

import io.micronaut.context.annotation.ClassImport;
import io.micronaut.serde.annotation.Serdeable;

@ClassImport(
        packages = "my.external.library",
        annotate = Serdeable.class)
public class Application {
}
```

|   | At this moment, Micronaut doesn’t support reimporting classes already processed by the Micronaut annotation processor. |
|---|---|
