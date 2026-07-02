---
title: "Javadoc"
source: https://en.wikipedia.org/wiki/Javadoc
domain: javadoc
license: CC-BY-SA-4.0
tags: javadoc java, documentation generator, api documentation, doc comments
fetched: 2026-07-02
---

# Javadoc

**Javadoc** (also capitalized as **JavaDoc** or **javadoc**) is an API documentation generator for the Java programming language. Based on information in Java source code, Javadoc generates documentation formatted as HTML and other formats via extensions. Javadoc was created by Sun Microsystems and is owned by Oracle today.

The content and formatting of a resulting document are controlled via special markup in source code comments. As this markup is de facto standard and ubiquitous for documenting Java code, many IDEs extract and display the Javadoc information while viewing the source code, often via hover over an associated symbol. Some IDEs, like IntelliJ IDEA, NetBeans and Eclipse, support generating Javadoc template comment blocks. The `@tag` syntax of Javadoc markup has been re-used by other documentation generators, including Doxygen, JSDoc, EDoc and HeaderDoc.

Javadoc supports extension via doclets and taglets, which allow for generating different output formats and for static analysis of a codebase. For example, JDiff reports changes between two versions of an API.

Although some criticize Javadoc and API document generators in general, one motivation for creating Javadoc was that more traditional (less automated) API documentation is often out-of-date or does not exist due to business constraints such as limited availability of technical writers.

Javadoc has been part of Java since its first release, and is often updated with each release of the Java Development Kit.

Javadoc and the source code comments used by Javadoc, do not affect the performance of a Java executable since comments are ignored by the compiler.

## Markup

Javadoc ignores comments unless they are specially marked. A Javadoc comment is marked with an extra asterisk after the start of a multi-line comment: `/**`. Following lines are preceded with an `*`, and the entire comment block should be terminated with a `*/`.

An example of a method Javadoc comment follows:

```mw
/**
 * Description of what the method does.
 *
 * @param input Description of parameter.
 * @return Description of return value.
 * @throws Exception Description of exception.
 */
public int methodName(String input) throws Exception { ... }
```

Some HTML tags, such as `<p>`, `<head>`, and `<nav>`, are supported in Javadoc.[1]

## Markdown

From Java 23 onwards, Javadoc supports the Markdown standard CommonMark on comment lines that start with `///` instead of the older multiline format.

## Doclets

A Doclet program works with Javadoc to select which content to include in the documentation, format the presentation of the content and create the file that contains the documentation. A Doclet is written in Java and uses the `Doclet API`,

The `StandardDoclet`[2] included with Javadoc generates API documentation as frame-based HTML files. Other Doclets are available on the web , often for free. These can be used to:

- Create other types of documentation (non-API)
- Output to a format other than HTML, such as PDF
- Output as HTML with additional features such as a search or with embedded UML diagrams generated from the Java classes

## Tags

Some of the available Javadoc tags are listed in the table below:

| Syntax | Usage | Applies to | Since |
|---|---|---|---|
| **@author** *name* | Identifies the author such as "Pat Smith" | Class, Interface, Enum |   |
| {**@docRoot**} | Represents the relative path to the generated document's root directory from any generated page | Class, Interface, Enum, Field, Method |   |
| **@version** *version* | Version information | Module, Package, Class, Interface, Enum |   |
| **@since** *since-text* | Describes when this functionality first existed | Class, Interface, Enum, Field, Method |   |
| **@see** *reference* | Links to other element of documentation | Class, Interface, Enum, Field, Method |   |
| **@param** *name description* | Describes a method parameter | Method |   |
| **@return** *description* | Describes the return value | Method |   |
| **@exception** *classname description* **@throws** *classname description* | Describes an exception that may be thrown from this method | Method |   |
| **@deprecated** *description* | Marks the method as outdated | Class, Interface, Enum, Field, Method |   |
| {**@inheritDoc**} | Copies the description from the overridden method | Overriding Method | 1.4.0 |
| {**@link** **reference**} | Link to other symbol | Class, Interface, Enum, Field, Method |   |
| {**@linkplain** **reference**} | Identical to `{@link}`, except the link's label is displayed in plain text than code font | Class, Interface, Enum, Field, Method |   |
| {**@value** *#STATIC_FIELD*} | Return the value of a static field | Static Field | 1.4.0 |
| {**@code** *literal*} | Formats literal text in the code font; equivalent to **`{@literal}`** | Class, Interface, Enum, Field, Method | 1.5.0 |
| {**@literal** *literal*} | Denotes literal text; the enclosed text is interpreted as not containing HTML markup or nested javadoc tags | Class, Interface, Enum, Field, Method | 1.5.0 |
| {**@serial** *literal*} | Denotes a default serializable field | Field |   |
| {**@serialData** *literal*} | Denotes data written by the `writeObject( )` or `writeExternal( )` methods | Field, Method |   |
| {**@serialField** *literal*} | Denotes an `ObjectStreamField` component | Field |   |
