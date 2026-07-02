---
title: "JavaDoc Tool"
source: https://docs.oracle.com/en/java/javase/21/javadoc/javadoc-tool.html
domain: javadoc
license: CC-BY-SA-4.0
tags: javadoc java, documentation generator, api documentation, doc comments
fetched: 2026-07-02
---

## 1 JavaDoc Tool

The JavaDoc tool is a program that reads Java source files and class files into a form that can be analyzed by a pluggable back end, called a doclet.

To use the JavaDoc tool, you must:

- Use source code that contains Java documentation comments.
- Run the `javadoc` tool with a doclet to analyze the documentation comments and any other special tags. If you don’t specify a doclet in the command, the Standard Doclet is used by default.

The content of any generated files is specific to the doclet. The Standard Doclet generates HTML output, but a different doclet could generate other output, such as a report of misspelled words or grammatical errors.

If you specify a doclet other than the Standard Doclet, then the descriptions in this guide might not apply to the operation of that doclet or the files (if any) that are generated.

In addition to the descriptions in this guide, JavaDoc tool users and content developers should use the following documentation:

- For authors writing content API documentation: Documentation Comment Tag Specification for the Standard Doclet
- For users running the tool to generate API documentation: The javadoc Command
- For end-user readers of API documentation: The Help page, in any generated documentation. The content of the Help page will be customized for the content of the API and the command used to generate the documentation. For example, see the Help page for the Java SE and JDK API specification.

### JavaDoc Features

JavaDoc features include enhanced support for code examples, search, summary pages, module system, Doclet API, HTML support, and DocLint.

Enhanced Support for Code Examples

The Standard Doclet provides improved support for code examples, as described in JEP 413: Code Snippets in Java API Documentation. See Programmer's Guide to Snippets for detailed information.

Search

When the JavaDoc tool runs the Standard Doclet, it generates output that enables users to search the generated documentation for elements and additional key phrases defined in the generated API documentation. Search results include matching characters from any position in the search string. The Search facility can also provide page redirection based on user selection.

Note:

The Search feature uses JavaScript. If you disable JavaScript in your browser, you will not be able to use the Search feature. However, all the information in the Search feature is also available in the A-Z Index that is present in any generated API documentation. The A-Z Index is in plain HTML and doesn’t require the use of JavaScript. See

Javadoc Search Specification

for detailed information about using Search.

Summary Pages

The Standard Doclet may generate various additional summary pages based on detailed descriptions of individual declarations contained in the API. These pages include information about new API, deprecated API, constant values, and serialized forms. Find links to these pages in the main navigation bar at the top of each page or in the A-Z Index.

Module System

The `javadoc` tool supports documentation comments in module declarations. Some JavaDoc command-line options enable you to specify the set of modules to document and generate a summary page for any modules being documented. See The javadoc Command for detailed information.

Doclet API

The Doclet API supports all of the latest language features. See the module jdk.javadoc for detailed information.

HTML Support

The Standard Doclet uses current web standards to generate documentation.

Note:

The Standard Doclet doesn’t repair or fix any HTML errors in documentation comments. HTML errors may cause the generated API documentation to fail validation by a conformance checker.

DocLint

DocLint is a feature provided by the JavaDoc tool, as well as the JDK Java compiler, `javac`, to detect and report issues in documentation comments that may cause the output to be not as the author intended. The issues include missing comments, references to undeclared items (perhaps because of a spelling error), accessibility errors, malformed HTML, and syntax errors. Depending on the severity of each issue, it may be reported as either a warning or an error. See The javadoc Command for more information about DocLint.

Note:

While features like DocLint may be helpful in detecting issues, it is strongly recommended that authors always check and proofread the generated API documentation, to make sure that it is as intended.
