---
title: "Web template system"
source: https://en.wikipedia.org/wiki/Web_template_system
domain: mustache-templating
license: CC-BY-SA-4.0
tags: mustache templating, mustache template system, logic-less templates, web template rendering
fetched: 2026-07-02
---

# Web template system

A **web template system** in web publishing allows web designers and developers to work with *web templates* to automatically generate custom web pages, such as the results from a search. This reuses static web page elements while defining dynamic elements based on web request parameters.

Web templates support static content, providing basic structure and appearance. Developers can implement templates from content management systems, web application frameworks, and HTML editors.

## Overview

A *web template system* is composed of the following:

- A template engine: the primary processing element of the system;
- *Content resource*: any of various kinds of input data streams, such as from a relational database, XML files, LDAP directory, and other kinds of local or networked data;
- *Template resource*: *web template*s specified according to a template language;

The template and content resources are processed and combined by the template engine to mass-produce web documents, each with a similar visual format. For purposes of this article, web documents include any of various output formats for transmission over the web via HTTP, HTTPS, or another Internet protocol.

### Template engine

A template processor (also known as a template engine or template parser) is software designed to combine *template*s with data (defined by a data model) to produce resulting documents or programs. The language that the templates are written in is known as a template language or templating language. For purposes of this article, a result document is any kind of formatted output, including documents, web pages, or source code (in source code generation), either in whole or in fragments. A template engine is ordinarily included as a part of a web template system or application framework, and may be used also as a preprocessor or filter.

## Example

With the model typically held in a relational database, the remaining components of the MVC architecture are the control and view. In the simplest of systems these two are not separated. However, adapting the separation of concerns principle one can completely decouple the relationships.

For example, the view template may look like this:

```mw
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
   <head><title>Sites</title></head>
   <body><h1 data-xp="title"><!-- placeholder --></h1></body>
</html>
```

Then, the control template loads the view, and then uses XPath addressing to insert components from a database, for instance:

```mw
<?php
$doc = new DOMDocument;
$doc->preserveWhiteSpace = false;
$doc->Load('view.html');
$titlenode = $doc->createTextNode("Like this");
$xpath = new DOMXPath($doc);
$xpath->registerNamespace("h", "http://www.w3.org/1999/xhtml"); 
$query = "//h:*[@data-xp='title']/comment()";
$entries = $xpath->query($query);
foreach ($entries as $entry) {
    $entry->parentNode->replaceChild($titlenode, $entry);
}
echo $doc->saveXML();
?>
```

## Kinds of template systems

A web browser and web server are a client–server architecture. Sites often also use a web cache to improve performance. In many implementations, template files contain variables or placeholders that are replaced with data supplied by an application when the page is generated.

- Server-side – run-time substitution happens on the web server
- Client-side – run-time substitution happens in the web browser
- Edge-side – run-time substitution happens on a proxy between web server and browser
- Outside server – static web pages are produced offline and uploaded to the web server; no run-time substitution
- Distributed – run-time substitution happens on multiple servers

Template languages may be:

- Embedded or event-driven.
- Simple, iterable, programmable, or complex.
- Defined by a consortium, privately defined, or de facto defined by an open implementation. Ownership influences the stability and credibility of a specification. However, in most jurisdictions, language specification cannot be copyrighted, so control is seldom absolute.

The source code of the template engine can be proprietary or open source.

Many template systems are a component of a larger programming platform or framework. They are referred to as the "platform's template system". Some template systems have the option of substituting a different template language or engine.

### Language support

Programming languages such as Perl, Ruby, C, and Java support template processing either natively, or through add-on libraries and modules. JavaServer Pages (JSP), PHP, and Active Server Pages (ASP with VBScript, JScript or other languages) are examples, themselves, of web template engines. These technologies are typically used in server-side templating systems, but could be adapted for use on an "edge-side" proxy or for static page generation.

### Static site generators

Static site generators are engines that use flat text input files like markdown and asciidoc to generate a static web page. Examples of this include Jekyll (Liquid, Ruby), Hugo (Go templates), and Pelican (Jinja2, Python).

Some hosted website builders, including Wix, Weebly, and Duda, provide template-based systems that allow users to create static and dynamic web pages through graphical user interfaces rather than traditional programming.

### Static HTML Editors

HTML editors often use web template systems to produce only static web pages. These can be viewed as a ready-made web design, used to mass-produce "cookie-cutter" websites for rapid deployment. They also commonly include themes in place of CSS styles. In general, the template language is used only with the editor's software.

FrontPage and Dreamweaver were once the most popular editors with template sub-systems. A Flash web template uses Macromedia Flash to create visually interactive sites.

Many *server-side template systems* have an option to publish output pages on the server, where the published pages are static. This is common on content management systems, like Vignette, but is not considered out-server generation. In the majority of cases, this "publish option" doesn't interfere with the *template system*, and it can be made by external software, as Wget.

### Server-side systems

People began to use server-side dynamic pages generated from templates with pre-existent software adapted for this task. This early software was the preprocessors and macro languages, adapted for the web use, running on CGI. Next, a simple but relevant technology was the direct execution made on extension modules, started with SSI.

Many *template systems* are typically used as *server-side template systems*:

| System label/name | Platform/framework | Notes |
|---|---|---|
| Blade | PHP | Public. Part of Laravel |
| CheetahTemplate | Python | Public. Embedded complex language. |
| Django | Python | Use the "Django template language". |
| EJS (Embedded JavaScript) | JavaScript | Public. Embedded complex language. |
| FreeMarker | Java | Public. |
| Facelets | Jakarta EE | Public. Part of Jakarta Faces |
| Genshi | Python | Public |
| Haml | Ruby or Other | Public. |
| Hamlets | Java | Public. |
| Jinja2 | Python | Public. Embedded complex language. |
| Kid | Python |   |
| Lasso | LassoSoft, LLC | Proprietary. Interpreted Programming Language and Server |
| Mustache | ActionScript, C++, Clojure, CoffeeScript, ColdFusion, D, Erlang, Fantom, Go, Java, server-side JavaScript, Lua, .NET, Objective-C, ooc, Perl, PHP, Python, Ruby, Scala, Tcl | Public. |
| Basic Server Side Includes (SSI) | The basic directives fix a "standard". | Embedded simple language, if exclude `exec` directive. |
| Smarty | PHP | Public. Embedded complex language. |
| Template Toolkit | Perl | Public. Embedded complex language. |
| Template Attribute Language (TAL) | Zope, Python, Java, Perl, PHP, XSLT | Public; a.k.a. Zope Page Templates (ZPT); see also TAL Expression Syntax (TALES), Macro Expansion TAL (METAL) |
| Tiles | Java | Public. Supports multiple template languages (JSP, Velocity, Freemarker, Mustache) from various frameworks (servlet, portlets, struts, spring). |
| Thymeleaf | Java | Public. |
| Topsite | Python | Public. *"As of 2008-02-20, this project is no longer under active development."* |
| Twig | PHP |   |
| PHPlib | PHPlib | Public. Embedded iterable language. |
| WebMacro | Java | Public. Embedded iterable language. |
| WebObjects | Java | Use the WebObjects Builder as engine. |
| Velocity | Java | Public. Use VTL - Velocity Template Language. |
| Vignette | Proprietary. | Commercial solution. Embedded complex language. |
| XSLT (standard language) | Any with an XSLT parser | Standard. Event-driven programmable language. |
| XQuery (standard language) | Any with an XQuery parser | Standard. Embedded programmable language. |

Technically, the methodology of embedding programming languages within HTML (or XML, etc.), used in many "server-side included script languages" are also templates. All of them are Embedded complex languages.

| System label/name | Notes |
|---|---|
| Active Server Pages (ASP) | Proprietary (Microsoft platform). See also: VBScript, Javascript, PerlScript, etc. extensions for ASP. |
| eRuby | Public (Ruby). |
| ColdFusion Markup Language (CFM) | Public (Lucee, Railo, OpenBD). Proprietary (Adobe ColdFusion). |
| Jakarta Server Pages (JSP) | Public, Jakarta EE. |
| Active Perl | Public. |
| PHP | Public. |
| OpenACS | Public (Tcl). |

There are also preprocessors used as server-side template engines. Examples:

| Preprocessor | Notes |
|---|---|
| C preprocessor | Public. Embedded iterable language. |
| M4 | Public. Embedded complex language. |

### Edge-side systems

As for edge-side template and inclusion systems, "edge-side" refers to web servers that reside in the space between the client (browser) and the originating server. They are often referred to as "reverse-proxy" servers. These servers are generally tasked with reducing the load and traffic on originating servers by caching content such as images and page fragments, and delivering this to the browser in an efficient manner.

Basic Edge Side Includes (ESI) is an SSI-like language. ESI has been implemented for content delivery networks. The ESI template language may also be implemented in web browsers using JavaScript and Ajax, or via a browser "plug-in".

### Client-side systems

Many web browsers can apply an XSLT stylesheet to XML data that transforms the data into an XHTML document, thereby providing template functionality in the browser itself. Other systems implement template functionality in the browser using JavaScript or another client-side scripting language, including:

- Mustache
- Squirrelly
- Handlebars

### Distributed systems

The most simple form is transclusions (HTML frames). In other cases dynamic web pages are needed.

Examples:

- Ajax
- Rich Internet application
