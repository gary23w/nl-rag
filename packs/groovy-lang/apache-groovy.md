---
title: "Apache Groovy"
source: https://en.wikipedia.org/wiki/Apache_Groovy
domain: groovy-lang
license: CC-BY-SA-4.0
tags: apache groovy, groovy language, groovy lang, gradle groovy
fetched: 2026-07-02
---

# Apache Groovy

**Apache Groovy** is a Java-syntax-compatible object-oriented programming language for the Java platform. It is both a static and dynamic language with features similar to those of Python, Ruby, and Smalltalk. It can be used as both a programming language and a scripting language for the Java Platform, is compiled to Java virtual machine (JVM) bytecode, and interoperates seamlessly with other Java code and libraries. Groovy uses a curly-bracket syntax similar to Java's. Groovy supports closures, multiline strings, and expressions embedded in strings. Much of Groovy's power lies in its abstract syntax tree (AST) transformations, triggered through annotations.

Groovy 1.0 was released on January 2, 2007, and Groovy 2.0 in July, 2012. Since version 2, Groovy can be compiled statically, offering type inference and performance near that of Java. Groovy 2.4 was the last major release under Pivotal Software's sponsorship which ended in March 2015. Groovy has since changed its governance structure to a Project Management Committee in the Apache Software Foundation.

## History

James Strachan first talked about the development of Groovy on his blog in August 2003. In March 2004, Groovy was submitted to the Java Community Process (JCP) as JSR 241 and accepted by ballot. Several versions were released between 2004 and 2006. After the JCP standardization effort began, the version numbering changed, and a version called "1.0" was released on January 2, 2007. After various betas and release candidates numbered 1.1, on December 7, 2007, Groovy 1.1 Final was released and immediately renumbered as Groovy 1.5 to reflect the many changes made.

In 2007, Groovy won the first prize at JAX 2007 innovation award. In 2008, Grails, a Groovy web framework, won the second prize at JAX 2008 innovation award.

In November 2008, SpringSource acquired the Groovy and Grails company (G2One). In August 2009 VMware acquired SpringSource.

In April 2012, after eight years of inactivity, the Spec Lead changed the status of JSR 241 to dormant.

Strachan had left the project silently a year before the Groovy 1.0 release in 2007. In Oct 2016, Strachan stated "I still love groovy (jenkins pipelines are so groovy!), java, go, typescript and kotlin".

On July 2, 2012, Groovy 2.0 was released, which, among other new features, added static compiling and static type checking.

When the Pivotal Software joint venture was spun-off by EMC Corporation (EMC) and VMware in April 2013, Groovy and Grails formed part of its product portfolio. Pivotal ceased sponsoring Groovy and Grails from April 2015. That same month, Groovy changed its governance structure from a Codehaus repository to a Project Management Committee (PMC) in the Apache Software Foundation via its incubator. Groovy graduated from Apache's incubator and became a top-level project in November 2015.

On February 7, 2020, Groovy 3.0 was released. Version 4.0 was released on January 25, 2022.

## Features

Most valid Java files are also valid Groovy files. Although the two languages are similar, Groovy code can be more compact, because it does not need all the elements that Java needs. This makes it possible for Java programmers to learn Groovy gradually by starting with familiar Java syntax before acquiring more Groovy programming idioms.

Groovy features not available in Java include both static and dynamic typing (with the keyword `def`), operator overloading, native syntax for lists and associative arrays (maps), native support for regular expressions, polymorphic iteration, string interpolation, added helper methods, and the safe navigation operator `?.` to check automatically for null pointers (for example, `variable?.method()`, or `variable?.field`).

Since version 2, Groovy also supports modularity (shipping only the `jar`s that the project uses, thus reducing the size of Groovy's library), type checking, static compilation, Project Coin syntax enhancements, multicatch blocks and ongoing performance enhancements using the `invokedynamic` instruction introduced in Java 7.

Groovy natively supports markup languages such as XML and HTML by using an inline Document Object Model (DOM) syntax. This feature enables the definition and manipulation of many types of heterogeneous data assets with a uniform and concise syntax and programming methodology.

Unlike Java, a Groovy source code file can be executed as an (uncompiled) script, if it contains code outside any class definition, if it is a class with a *main* method, or if it is a *Runnable* or *GroovyTestCase*. A Groovy script is fully parsed, compiled, and generated before executing (similar to Python and Ruby). This occurs under the hood, and the compiled version is not saved as an artifact of the process.

### GroovyBeans, properties

*GroovyBeans* are Groovy's version of JavaBeans. Groovy implicitly generates getters and setters. In the following code, `setColor(String color)` and `getColor()` are implicitly generated. The last two lines, which appear to access color directly, are actually calling the implicitly generated methods.

```mw
class AGroovyBean {
  String color
}

def myGroovyBean = new AGroovyBean()

myGroovyBean.setColor('baby blue')
assert myGroovyBean.getColor() == 'baby blue'

myGroovyBean.color = 'pewter'
assert myGroovyBean.color == 'pewter'
```

Groovy offers simple, consistent syntax for handling *lists* and *maps*, reminiscent of Java's *array* syntax.

```mw
def movieList = ['Dersu Uzala', 'Ran', 'Seven Samurai']  // Looks like an array, but is a list
assert movieList[2] == 'Seven Samurai'
movieList[3] = 'Casablanca'  // Adds an element to the list
assert movieList.size() == 4

def monthMap = [ 'January' : 31, 'February' : 28, 'March' : 31 ]  // Declares a map
assert monthMap['March'] == 31  // Accesses an entry
monthMap['April'] = 30  // Adds an entry to the map
assert monthMap.size() == 4
```

### Prototype extension

Groovy offers support for prototype extension through `ExpandoMetaClass`, Extension Modules (only in Groovy 2), Objective-C-like Categories and `DelegatingMetaClass`.

`ExpandoMetaClass` offers a domain-specific language (DSL) to express the changes in the class easily, similar to Ruby's open class concept:

```mw
Number.metaClass {
  sqrt = { Math.sqrt(delegate) }
}

assert 9.sqrt() == 3
assert 4.sqrt() == 2
```

Groovy's changes in code through prototyping are not visible in Java, since each attribute/method invocation in Groovy goes through the metaclass registry. The changed code can only be accessed from Java by going to the metaclass registry.

Groovy also allows overriding methods as `getProperty()`, `propertyMissing()` among others, enabling the developer to intercept calls to an object and specify an action for them, in a simplified aspect-oriented way. The following code enables the class `java.lang.String` to respond to the `hex` property:

```mw
enum Color {
  BLACK('#000000'), WHITE('#FFFFFF'), RED('#FF0000'), BLUE('#0000FF')
  String hex
  Color(String hex) { 
    this.hex = hex 
  }
}

String.metaClass.getProperty = { String property ->
  def stringColor = delegate
  if (property == 'hex') {
    Color.values().find { it.name().equalsIgnoreCase stringColor }?.hex
  }
}

assert "WHITE".hex == "#FFFFFF"
assert "BLUE".hex == "#0000FF"
assert "BLACK".hex == "#000000"
assert "GREEN".hex == null
```

The Grails framework uses metaprogramming extensively to enable GORM dynamic finders, like `User.findByName('Josh')` and others.

### Dot and parentheses

Groovy's syntax permits omitting parentheses and dots in some situations. The following groovy code

```mw
take(coffee).with(sugar, milk).and(liquor)
```

can be written as

```mw
take coffee with sugar, milk and liquor
```

enabling the development of domain-specific languages (DSLs) that look like plain English.

### Functional programming

Although Groovy is mostly an object-oriented language, it also offers functional programming features.

#### Closures

According to Groovy's documentation: "Closures in Groovy work similar to a 'method pointer', enabling code to be written and run in a later point in time". Groovy's closures support free variables, i.e. variables that have not been explicitly passed as a parameter to it, but exist in its declaration context, partial application (that it terms 'currying'), delegation, implicit, typed and untyped parameters.

When working on Collections of a determined type, the closure passed to an operation on the collection can be inferred:

```mw
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

/* 
 * Non-zero numbers are coerced to true, so when it % 2 == 0 (even), it is false.
 * The type of the implicit "it" parameter can be inferred as an Integer by the IDE.
 * It could also be written as:
 * list.findAll { Integer i -> i % 2 }
 * list.findAll { i -> i % 2 }
 */
def odds = list.findAll { it % 2 }

assert odds == [1, 3, 5, 7, 9]
```

A group of expressions can be written in a closure block without reference to an implementation and the responding object can be assigned at a later point using delegation:

```mw
// This block of code contains expressions without reference to an implementation
def operations = {
  declare 5
  sum 4
  divide 3
  print
}
```

```mw
/* 
 * This class will handle the operations that can be used in the closure above. Another class
 * could be declared having the same methods, but using, for example, webservice operations
 * in the calculations.
 */
class Expression {
  BigDecimal value

  /* 
   * Though an Integer is passed as a parameter, it is coerced into a BigDecimal, as was 
   * defined. If the class had a 'declare(Integer value)' method, it would be used instead.
   */
  def declare(BigDecimal value) {
    this.value = value
  }
  
  def sum(BigDecimal valueToAdd) {
    this.value += valueToAdd
  }
  
  def divide(BigDecimal divisor) {
    this.value /= divisor
  }
  
  def propertyMissing(String property) {
    if (property == "print") println value
  }
}
```

```mw
// Here is defined who is going to respond the expressions in the block of code above.
operations.delegate = new Expression()
operations()
```

#### Curry

Usually called *partial application*, this Groovy feature allows closures' parameters to be set to a default parameter in any of their arguments, creating a new closure with the bound value. Supplying one argument to the `curry()` method will fix argument one. Supplying N arguments will fix arguments 1 .. N.

```mw
def joinTwoWordsWithSymbol = { symbol, first, second -> first + symbol + second }
assert joinTwoWordsWithSymbol('#', 'Hello', 'World') == 'Hello#World'

def concatWords = joinTwoWordsWithSymbol.curry(' ')
assert concatWords('Hello', 'World') == 'Hello World'

def prependHello = concatWords.curry('Hello')
//def prependHello = joinTwoWordsWithSymbol.curry(' ', 'Hello')
assert prependHello('World') == 'Hello World'
```

Curry can also be used in the reverse direction (fixing the last N arguments) using `rcurry()`.

```mw
def power = { BigDecimal value, BigDecimal power ->
  value**power
}

def square = power.rcurry(2)
def cube = power.rcurry(3)

assert power(2, 2) == 4
assert square(4) == 16
assert cube(3) == 27
```

Groovy also supports lazy evaluation, reduce/fold, infinite structures and immutability, among others.

### JSON and XML processing

On JavaScript Object Notation (JSON) and XML processing, Groovy employs the Builder pattern, making the production of the data structure less verbose. For example, the following XML:

```mw
<languages>
  <language year="1995">
    <name>Java</name>
    <paradigm>object oriented</paradigm>
    <typing>static</typing>
  </language>
  <language year="1995">
    <name>Ruby</name>
    <paradigm>functional, object oriented</paradigm>
    <typing>duck typing, dynamic</typing>
  </language>
  <language year="2003">
    <name>Groovy</name>
    <paradigm>functional, object oriented</paradigm>
    <typing>duck typing, dynamic, static</typing>
  </language>
</languages>
```

can be generated via the following Groovy code:

```mw
def writer = new StringWriter()
def builder = new groovy.xml.MarkupBuilder(writer)
builder.languages {
  language(year: 1995) {
    name "Java"
    paradigm "object oriented"
    typing "static"
  }
  language (year: 1995) {
    name "Ruby"
    paradigm "functional, object oriented"
    typing "duck typing, dynamic"
  }
  language (year: 2003) {
    name "Groovy"
    paradigm "functional, object oriented"
    typing "duck typing, dynamic, static"
  }
}
```

and also can be processed in a streaming way through `StreamingMarkupBuilder`. To change the implementation to JSON, the `MarkupBuilder` can be swapped to `JsonBuilder`.

To parse it and search for a functional language, Groovy's `findAll` method can serve:

```mw
def languages = new XmlSlurper().parseText writer.toString()

// Here is employed Groovy's regex syntax for a matcher (=~) that will be coerced to a 
// boolean value: either true, if the value contains our string, or false otherwise.
def functional = languages.language.findAll { it.paradigm =~ "functional" }
assert functional.collect { it.name } == ["Groovy", "Ruby"]
```

### String interpolation

In Groovy, strings can be interpolated with variables and expressions by using GStrings:

```mw
BigDecimal account = 10.0
def text = "The account shows currently a balance of $account"
assert text == "The account shows currently a balance of 10.0"
```

GStrings containing variables and expressions must be declared using double quotes.

A complex expression must be enclosed in curly brackets. This prevents parts of it from being interpreted as belonging to the surrounding string instead of to the expression:

```mw
BigDecimal minus = 4.0
text = "The account shows currently a balance of ${account - minus}"
assert text == "The account shows currently a balance of 6.0"

// Without the brackets to isolate the expression, this would result:
text = "The account shows currently a balance of $account - minus"
assert text == "The account shows currently a balance of 10.0 - minus"
```

Expression evaluation can be deferred by employing arrow syntax:

```mw
BigDecimal tax = 0.15
text = "The account shows currently a balance of ${->account - account*tax}"
tax = 0.10

// The tax value was changed AFTER declaration of the GString. The expression 
// variables are bound only when the expression must actually be evaluated:
assert text == "The account shows currently a balance of 9.000"
```

### Abstract syntax tree transformation

According to Groovy's own documentation, "When the Groovy compiler compiles Groovy scripts and classes, at some point in the process, the source code will end up being represented in memory in the form of a Concrete Syntax Tree, then transformed into an Abstract Syntax Tree. The purpose of AST Transformations is to let developers hook into the compilation process to be able to modify the AST before it is turned into bytecode that will be run by the JVM. AST Transformations provides Groovy with improved compile-time metaprogramming capabilities allowing powerful flexibility at the language level, without a runtime performance penalty."

Examples of ASTs in Groovy are:

- Category and Mixin transformation
- Immutable AST Macro
- Newify transformation
- Singleton transformation

among others.

The testing framework Spock uses AST transformations to allow the programmer to write tests in a syntax not supported by Groovy, but the relevant code is then manipulated in the AST to valid code. An example of such a test is:

```mw
def "maximum of #a and #b is #c" () {
  expect:
  Math.max (a, b) == c

  where:
  a | b || c
  3 | 5 || 5
  7 | 0 || 7
  0 | 0 || 0
}
```

### Traits

According to Groovy's documentation, "Traits are a structural construct of the language that allows: composition of behaviors, runtime implementation of interfaces, behavior overriding, and compatibility with static type checking/compilation."

Traits can be seen as interfaces carrying both default implementations and state. A trait is defined using the trait keyword:

```mw
trait FlyingAbility { /* declaration of a trait */
  String fly() { "I'm flying!" } /* declaration of a method inside a trait */
}
```

Then, it can be used like a normal interface using the keyword `implements`:

```mw
class Bird implements FlyingAbility {} /* Adds the trait FlyingAbility to the Bird class capabilities */
def bird = new Bird() /* instantiate a new Bird */
assert bird.fly() == "I'm flying!" /* the Bird class automatically gets the behavior of the FlyingAbility trait */
```

Traits allow a wide range of abilities, from simple composition to testing.

## Groovy version history

| Version | Initial release | Latest release | Active support | Bug and security fixes | Notes |
|---|---|---|---|---|---|
| 5.x | 2025 | 5.0.4 (2026) | Active | Yes | Improved performance, enhanced JDK 17+ support and a revamped REPL |
| 4.x | 2022 | 4.0.30 (2026) | No | Yes | Support for native records for JDK16+ |
| 3.x | 2020 | 3.0.25 (2025) | No | Yes | Enhanced for loop, try-with-resources and lambda |
| 2.5.x | 2018 | 2.5.23 (2023) | No | Yes | AST transformations, new CLI builders |
| 2.4.x | 2015 | 2.4.21 (2020) | No | No | Performance improvements and reduced bytecode |

- Groovy has no fixed release cycle; support typically shifts on release of a new major version.
- The latests version can be downloaded from: Download Groovy
- version history is based on

## Adoption

Notable examples of Groovy adoption include:

- Apache OFBiz, the open-source enterprise resource planning (ERP) system, uses Groovy.
- Eucalyptus, a cloud management system, uses a significant amount of Groovy.
- Gradle is a popular build automation tool using Groovy.
- LinkedIn uses Groovy and Grails for some of their subsystems.
- Jenkins, a platform for continuous integration. With version 2, Jenkins includes a *Pipeline* plugin that allows for build instructions to be written in Groovy.
- Sky.com uses Groovy and Grails to serve massive online media content.
- SmartThings, an open platform for smart homes and the consumer Internet of Things, uses a security-oriented subset of Groovy
- SoapUI provides Groovy as a language for webservice tests development.
- Wired.com uses Groovy and Grails for the Product Reviews standalone section of the website.
- XWiki SAS uses Groovy as scripting language in their collaborative open-source product.

## IDE support

Many integrated development environments (IDEs) and text editors support Groovy:

- Android Studio, IDE used for making Android apps
- Atom editor
- Eclipse, through Groovy-Eclipse
- Emacs, using the groovy-emacs-mode project's groovy-mode.
- IntelliJ IDEA, Community Edition, Grails/Griffon in the Ultimate Edition only
- JDeveloper, for use with Oracle ADF
- jEdit, an advanced text editor for the Java platform
- Kate, an advanced text editor for KDE supports Groovy and over 200 other file formats
- NetBeans, since version 6.5
- Notepad++, an advanced text editor for Microsoft Windows
- Sublime Text, a cross platform text editor
- TextMate
- Visual Studio Code
- UltraEdit, general purpose program editor

## Dialects

There is one alternative implementation of Groovy:

- Grooscript converts Groovy code to JavaScript code. Although Grooscript has some limitations compared to Apache Groovy, it can use domain classes in both the server and the client. Plugin support for Grails version 3.0 is provided, as well as online code conversions.
