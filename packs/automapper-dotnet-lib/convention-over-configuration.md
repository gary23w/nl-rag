---
title: "Convention over configuration"
source: https://en.wikipedia.org/wiki/Convention_over_configuration
domain: automapper-dotnet-lib
license: CC-BY-SA-4.0
tags: automapper mapping, dotnet object mapping, automapper dto, automapper profile config
fetched: 2026-07-02
---

# Convention over configuration

**Convention over configuration** (also known as **coding by convention**) is a software design paradigm used by software frameworks that attempts to decrease the number of decisions that a developer using the framework is required to make without necessarily losing flexibility and don't repeat yourself (DRY) principles.

The concept was introduced by David Heinemeier Hansson to describe the philosophy of the Ruby on Rails web framework, but is related to earlier ideas like the concept of "sensible defaults" and the principle of least astonishment in user interface design.

The phrase essentially means a developer only needs to specify unconventional aspects of the application. For example, if there is a class Sales in the model, the corresponding table in the database is called "sales" by default. It is only if one deviates from this convention, such as the table "product sales", that one needs to write code regarding these names.

When the convention implemented by the tool matches the desired behavior, it behaves as expected without having to write configuration files. Only when the desired behavior deviates from the implemented convention is explicit configuration required.

Ruby on Rails' use of the phrase is particularly focused on its default project file and directory structure, which prevent developers from having to write XML configuration files to specify which modules the framework should load, which was common in many earlier frameworks.

## Disadvantages

Disadvantages of the convention over configuration approach can occur due to conflicts with other software design principles, like the Zen of Python's "explicit is better than implicit." A software framework based on convention over configuration often involves a domain-specific language with a limited set of constructs or an inversion of control in which the developer can only affect behavior using a limited set of hooks, both of which can make implementing behaviors not easily expressed by the provided conventions more difficult than when using a software library that does not try to decrease the number of decisions developers have to make or require inversion of control.

Other methods of decreasing the number of decisions a developer needs to make include programming idioms and configuration libraries with a multilayered architecture.

## Motivation

Some frameworks need multiple configuration files, each with many settings. These provide information specific to each project, ranging from URLs to mappings between classes and database tables. Many configuration files with many parameters are often difficult to maintain.

For example, early versions of the Java persistence mapper Hibernate mapped entities and their fields to the database by describing these relationships in XML files. Most of this information could have been revealed by conventionally mapping class names to the identically named database tables and the fields to their columns, respectively. Later versions did away with the XML configuration file and instead employed these very conventions, deviations from which can be indicated through the use of Java annotations (see JavaBeans specification, linked below).

## Usage

Many modern frameworks use a *convention over configuration* approach.

The concept is older, however, dating back to the concept of a default, and can be spotted more recently in the roots of Java libraries. For example, the JavaBeans specification relies on it heavily. To quote the JavaBeans specification 1.01:

> "As a general rule we don't want to invent an enormous java.beans.everything class that people have to inherit from. Instead we'd like the JavaBeans runtimes to provide default behaviour for 'normal' objects, but to allow objects to override a given piece of default behaviour by inheriting from some specific java.beans.something interface."
