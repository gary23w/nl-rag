---
title: "Template processor"
source: https://en.wikipedia.org/wiki/Template_processor
domain: bottle-py
license: CC-BY-SA-4.0
tags: bottle framework, bottle python, python microframework, wsgi application
fetched: 2026-07-02
---

# Template processor

A **template processor** (also known as a **template engine** or **template parser**) is software designed to combine *template*s with data (defined by a data model) to produce resulting documents or programs. The language that the templates are written in is known as a **template language** or **templating language**. For purposes of this article, a result document is any kind of formatted output, including documents, web pages, or source code (in source code generation), either in whole or in fragments. A template engine is ordinarily included as a part of a web template system or application framework, and may be used also as a preprocessor or filter.

## Typical features

Template engines typically include features common to most high-level programming languages, with an emphasis on features for processing plain text.

Such features include:

- variables and functions
- text replacement
- file inclusion (or transclusion)
- conditional evaluation and loops

## Embedded template engines

While template processors are typically a separate piece of software, used as part of a system or framework, simple templating languages are commonly included in the string processing features of general-purpose programming languages, and in text processing programs, notably text editors or word processors. The templating languages are generally simple substitution-only languages, in contrast to the more sophisticated facilities in full-blown template processors, but may contain some logic.

Simple examples include ‘printf’ print format strings, found in many programming languages, and snippets, found in a number of text editors and source code editors. In word processors, templates are a common feature, while automatic filling in of the templates is often referred to as mail merge.

An illustrative example of the complementary nature of parsing and templating is the `s` (substitute) command in the sed text processor, originating from search-and-replace in the ed text editor. Substitution commands are of the form `s/regexp/replacement/`, where `regexp` is a regular expression, for parsing input, and `replacement` is a simple template for output, either literal text, or a format string containing the characters `&` for "entire match" or the special escape sequences `\1` through `\9` for the *n*th sub-expression. For example, `s/(cat|dog)s?/\1s/g` replaces all occurrences of "cat" or "dog" with "cats" or "dogs", without duplicating an existing "s": `(cat|dog)` is the 1st (and only) sub-expression in the regexp, and `\1` in the format string substitutes this into the output.

## System elements

All template processing systems consist of at least these primary elements:

- an associated **data model**;
- one or more **source templates**;
- a processor or **template engine**;
- generated output in the form of **result documents**.

### Data model

This may be a relational database, a source file such as XML, an alternate format of flat file database, a spreadsheet or any of other various sources of preformatted data. Some template processing systems are limited in the types of data that can be used. Others are designed for maximum flexibility and allow many different types of data.

### Source template

Source templates are traditionally specified:

- according to a pre-existing programming language;
- according to a specially defined template language;
- according to the features of a hosting software application; or
- according to a hybrid combination of some or all of the above.

### Template engine

The template engine is responsible for:

- connecting to the data model;
- processing the code specified in the source templates; and
- directing the output to a specific pipeline, text file, or stream.

Additionally some template engines allow additional configuration options.

### Result documents

These may consist of an entire document or a document fragment.

## Uses

Template processing is used in various contexts for different purposes. The specific purpose is ordinarily contingent upon the software application or template engine in use. However, the flexibility of template processing systems often enables unconventional uses for purposes not originally intended by the original designers.

### Template engine

A **template engine** is a specific kind of template processing module that exhibits all of the major features of a modern programming language. The term *template engine* evolved as a generalized description of programming languages whose primary or exclusive purpose was to process templates and data to output text. The use of this term is most notably applied to web development using a web template system, and it is also applied to other contexts as well.

### Document generation

Document generation frameworks typically use template processing as the central model for generating documents.

### Source code generation

Source code generation tools support generation of source code (as the result documents) from abstract data models (e.g., UML, relational data, domain-specific enterprise data stores) for particular application domains, particular organizations, or in simplifying the production process for computer programmers.

### Software functionality

A web template engine processes web templates and source data (typically from a relational database) to produce one or more output web pages or page fragments. It is ordinarily included as a part of a web template system or application framework. Currently, template processing software is most frequently used in the context of development for the web.

## Comparison

XSLT is a template processing model designed by W3C. It is designed primarily for transformations on XML data (into web documents or other output).

Programming languages such as Perl, Python, PHP, Ruby, C#, Java, and Go support template processing either natively, or through add-on libraries and modules. JavaServer Pages, Active Server Pages, Genshi (for Python), and eRuby are examples of template engines designed specifically for web application development.

Moreover, template processing is sometimes included as a sub-feature of software packages like text editors, IDEs and relational database management systems.

## Benefits of using template engines

- encourages organization of source code into operationally-distinct layers (see e.g., MVC)
- enhances productivity by reducing unnecessary reproduction of effort
- enhances teamwork by allowing separation of work based on skill-set (e.g., artistic vs. technical)
