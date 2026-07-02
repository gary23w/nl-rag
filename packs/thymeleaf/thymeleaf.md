---
title: "Thymeleaf"
source: https://en.wikipedia.org/wiki/Thymeleaf
domain: thymeleaf
license: CC-BY-SA-4.0
tags: thymeleaf engine, thymeleaf template, java templating, natural templates
fetched: 2026-07-02
---

# Thymeleaf

**Thymeleaf** is a Java XML/XHTML/HTML5 template engine that can work both in web (servlet-based) and non-web environments. It is better suited for serving XHTML/HTML5 at the view layer of MVC-based web applications, but it can process any XML file even in offline environments. It provides full Spring Framework integration.

In web applications Thymeleaf aims to be a complete substitute for JavaServer Pages (JSP), and implements the concept of *Natural Templates*: template files that can be directly opened in browsers and that still display correctly as web pages.

Thymeleaf is open-source software, licensed under the Apache License 2.0.

## Features

From the project's website:

- Java template engine for XML, XHTML and HTML5.
- Works both in web and non-web (offline) environments. No hard dependency on the Servlet API.
- Based on modular feature sets called *dialects*.
  - Dialect features (e.g.: evaluation, iteration, etc.) are applied by linking them to template's tags and/or attributes.
  - Two dialects available out-of-the-box: Standard and SpringStandard (for Spring MVC apps, same syntax as Standard).
  - Developers can extend and create custom dialects.
- Several template modes:
  - **XML**: validating against a DTD or not.
  - **XHTML 1.0 and 1.1**: validating against standard DTDs or not.
  - **HTML5**: both XML-formed code and legacy-based HTML5. Legacy non-XML code will be automatically cleaned and converted to XML form.
- Full (and extensible) **internationalization** support.
- Configurable, high performance **parsed template cache** that reduces input/output to the minimum.
- Automatic DOCTYPE translations –from template DTD to result DTD– for (optional) validation of both template and result code.
- Extremely extensible: can be used as a template engine framework if needed.
- Complete documentation including several example applications.

## Thymeleaf example

The following example produces an HTML5 table with rows for each item of a *List<Product>* variable called *allProducts*.

```mw
<table>
  <thead>
    <tr>
      <th th:text="#{msgs.headers.name}">Name</th>
      <th th:text="#{msgs.headers.price}">Price</th>
    </tr>
  </thead>
  <tbody>
    <tr th:each="prod : ${allProducts}">
      <td th:text="${prod.name}">Oranges</td>
      <td th:text="${#numbers.formatDecimal(prod.price,1,2)}">0.99</td>
    </tr>
  </tbody>
</table>
```

This piece of code includes:

- Internationalization expressions: *#{ ... } rh*
- Variable/model-attribute evaluation expressions: *${ ... }*
- Utility functions: *#numbers.formatDecimal( ... )*

Also, this fragment of (X)HTML code can be perfectly displayed by a browser as a prototype, without being processed at all: it is a *natural template*.
