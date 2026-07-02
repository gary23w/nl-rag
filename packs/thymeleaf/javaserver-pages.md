---
title: "Jakarta Server Pages"
source: https://en.wikipedia.org/wiki/JavaServer_Pages
domain: thymeleaf
license: CC-BY-SA-4.0
tags: thymeleaf engine, thymeleaf template, java templating, natural templates
fetched: 2026-07-02
---

# Jakarta Server Pages

(Redirected from

JavaServer Pages

)

**Jakarta Server Pages** (**JSP**; formerly **JavaServer Pages**) is a collection of technologies that helps software developers create dynamically generated web pages based on HTML, XML, SOAP, or other document types. Released in 1999 by Sun Microsystems, JSP is similar to PHP and ASP, but uses the Java programming language.

To deploy and run Jakarta Server Pages, a compatible web server with a servlet container, such as Apache Tomcat or Jetty, is required.

## Overview

Architecturally, JSP may be viewed as a high-level abstraction of Jakarta Servlets. JSPs are translated into servlets at runtime, therefore JSP is a Servlet; each JSP servlet is cached and re-used until the original JSP is modified.

Jakarta Server Pages can be used independently or as the view component of a server-side model–view–controller design, normally with JavaBeans as the model and Java servlets (or a framework such as Apache Struts) as the controller. This is a type of Model 2 architecture.

JSP allows Java code and certain predefined actions to be interleaved with static web markup content, such as HTML. The resulting page is compiled and executed on the server to deliver a document. The compiled pages, as well as any dependent Java libraries, contain Java bytecode rather than machine code. Like any other .jar or Java program, code must be executed within a Java virtual machine (JVM) that interacts with the server's host operating system to provide an abstract, platform-neutral environment.

JSPs are usually used to deliver HTML and XML documents, but through the use of OutputStream, they can deliver other types of data as well.

The Web container creates JSP implicit objects like request, response, session, application, config, page, pageContext, out and exception. JSP Engine creates these objects during translation phase.

## Syntax

### Directives, scriptlets, and expressions declaration

JSPs use several delimiters for scripting functions. The most basic is `<% ... %>`, which encloses a JSP *scriptlet.* A scriptlet is a fragment of Java code that runs when the user requests the page.

Other common delimiters include `<%= ... %>` for *expressions,* where the scriptlet and delimiters are replaced with the result of evaluating the expression, and *directives*, denoted with `<%@ ... %>`.

Java code is not required to be complete or self-contained within a single scriptlet block. It can straddle markup content, provided that the page as a whole is syntactically correct. For example, any Java *if/for/while* blocks opened in one scriptlet must be correctly closed in a later scriptlet for the page to successfully compile. This allows code to be intermingled and can result in poor programming practices.

Content that falls inside a split block of Java code (spanning multiple scriptlets) is subject to that code. Content inside an *if* block will only appear in the output when the *if* condition evaluates to true. Likewise, content inside a loop construct may appear multiple times in the output, depending upon how many times the loop body runs.

#### Example

The following would be a valid for loop in a JSP page:

```mw
<p>Counting to three:</p>
<% for (int i = 1; i < 4; i++) { %>
    <p>This number is <%= i %>.</p>
<% } %>
<p>OK.</p>
```

The output displayed in the user's web browser would be:

```
Counting to three:

This number is 1.

This number is 2.

This number is 3.

OK.
```

### Standard JSP Tags

#### The useBean Tag

The JSP `useBean` tag enables the developer to access and create a Javabean. Although using the `useBean` tag looks similar to an HTML tag, all JSP tags for JavaBeans use XML syntax. Therefore the code containing the `useBean` tag is case-sensitive.

The `useBean` tag contains several attributes. The `id` attribute declares the name that is used for gaining access to the bean. The `class` attribute declares the package and class for the bean. The `scope` declares the object responsible for storing the bean. The value for the scope defines the duration for which the bean is available for the rest of the java application to use. The scope can be one of the following four values:

- The `page` scope implies that the bean is located in the implicitly defined `PageContext` object, and is only available for the current page. By default, all beans have a scope of `page`.
- The `request` scope implies that the bean can be found in the `HttpServletRequest` object. This bean can be accessed by all other JSPs and servlets that have access to the current request object.
- The `session` scope implies that the bean can be found in the `HttpSession` object. This bean can be accessed by all other JSPs and servlets that have access to the specified `HttpSession` object.
- The `application` scope implies that the bean can be found in the `ServletContext` object. This bean can be accessed by all other JSPs and servlets that have access to the specified `ServletContext` object.

#### The getProperty and setProperty Tags

After a bean has been created using the `useBean` tag, the `getProperty` and `setProperty` tags can be used for getting and setting the properties of the bean. The JSP `getProperty` is used to get the property of created bean. The JSP `setProperty` tag is used to set the properties for a bean. For the `getProperty` and `setProperty` tags, the name attribute is used to specify the bean's name. So the name attribute must match the id attribute provided by the `useBean` tag.

### Expression Language

Version 2.0 of the JSP specification added support for the Expression Language (EL), used to access data and functions in Java objects. In JSP 2.1, it was folded into the Unified Expression Language, which is also used in JavaServer Faces.

The JSP Expression Language uses a compact syntax which enables the developer to get attributes and JavaBean properties from a given request object. When using EL, a dollar sign ("$") must be added at the beginning of the code. The dollar symbol is followed by an opening brace ("{"), as well as a closing brace ("}"). The code is then written between the opening and closing braces.

#### Example

The following is an example of EL syntax:

The value of `variable` in the object `javabean` is `${javabean.variable}`.

### Additional tags

The JSP syntax adds additional tags, called JSP actions, to invoke built-in functionality. Additionally, the technology allows for the creation of custom JSP *tag libraries* that act as extensions to the standard JSP syntax. One such library is the JSTL.

#### Jakarta Standard Tag Library

Jakarta Standard Tag Library (JSTL) supports common tasks that must be performed in JSPs. Examples includes iteration and conditionals (the equivalent of "for" and "if" statements in Java).

Out of all the libraries in JSTL, the JSTL core library is most commonly used. A taglib directive must be used to specify the URI of the JSTL core library using a prefix. Although there are many different choices for the prefix, the "c" prefix is commonly used for this library.

### XML-compliant JSP

JSP pages may also be written in fully valid XML syntax. Such JSP files commonly use the alternative `.jspx` file extension, which usually causes the application server to validate the XML syntax.

Since the usual JSP syntax `<% ... %>` is not valid in XML, a developer must use alternative tags provided by JSP. For example, the common `<%@ page .. %>` directive may instead be written as a `<jsp:directive.page .. />` tag, and tag libraries are imported using XML namespaces, instead of the usual `<%@ taglib .. %>` tag.

## Compiler

A **JavaServer Pages compiler** is a program that parses JSPs and transforms them into executable Java Servlets. A program of this type is usually embedded into the application server and run automatically the first time a JSP is accessed, but pages may also be precompiled for better performance, or compiled as a part of the build process to test for errors.

Some JSP containers support configuring how often the container checks JSP file timestamps to see whether the page has changed. Typically, this timestamp would be set to a short interval (perhaps seconds) during software development, and a longer interval (perhaps minutes, or even never) for a deployed Web application.

## Criticism

According to Joel Murach and Michael Urban, authors of the book "Murach's Java Servlets and JSP", embedding Java code in JSP is generally bad practice. A better approach would be to migrate the back-end logic embedded in the JSP to the Java code in the `Servlet`. In this scenario, the `Servlet` is responsible for processing, and the JSP is responsible for displaying the HTML, maintaining a clear separation of concerns.

In 2000, Jason Hunter, author of "Java Servlet Programming" described a number of "problems" with JavaServer Pages. Nevertheless, he wrote that while JSP may not be the "best solution for the Java Platform" it was the "Java solution that is most like the non-Java solution," by which he meant Microsoft's Active Server Pages. Later, he added a note to his site saying that JSP had improved since 2000, but also cited its competitors, Apache Velocity and Tea (template language). Today, several alternatives and a number of JSP-oriented pages in larger web apps are considered to be technical debt.
