---
title: "Spring Boot"
source: https://en.wikipedia.org/wiki/Spring_Boot
domain: spring-boot
license: CC-BY-SA-4.0
tags: spring boot, spring framework, java backend, spring mvc
fetched: 2026-07-02
---

# Spring Boot

**Spring Boot** is an open-source Java framework used for programming standalone, production-grade Spring-based applications with a bundle of libraries that make project startup and management easier. Spring Boot is a convention-over-configuration extension for the Spring Java platform intended to help minimize configuration concerns while creating Spring-based applications. The application can still be adjusted for specific needs, but the initial Spring Boot project provides a preconfigured "opinionated view" of the best configuration to use with the Spring platform and selected third-party libraries.

Spring Boot can be used to build microservices, web applications, and console applications.

## Features

- Embedded Tomcat, Jetty or Undertow web application server.
- Provides opinionated 'starter' Project Object Models (POMs) for the build tool. The only build tools supported are Maven and Gradle.
- Automatic configuration of the Spring Application.
- Provides production-ready functionality such as metrics, health checks, and externalized configuration.
- No code generation is required.
- No XML configuration is required.
- Optional support for Kotlin and Apache Groovy in addition to Java.

## Bootstrapping DispatcherServlet

Spring Boot does not require manual configuration of the `DispatcherServlet`, since it automatically configures the application based on the configuration it detects.

### SpringBootServletInitializer

Spring Boot has a class `SpringBootServletInitializer`, which is a specialization of the `WebApplicationInitializer`. This `SpringBootServletInitializer` is an out-of-the-box implementation of `WebApplicationInitializer`, which eliminates the need for the developer to construct their own implementation of the `WebApplicationInitializer` class.

## Configuration properties

The configuration properties for the Spring Boot application can be specified in the `application.properties` or `application.yml` file. Examples of properties that can be included in this file include the `server.port` and `spring.application.name` properties.

## Autoconfiguration

### @SpringBootApplication

Spring Boot has an annotation, `@SpringBootApplication`, which allows the Spring Boot application to autoconfigure third-party libraries and detected features found on the classpath. As an example, the class that has the `@SpringBootApplication` annotation can extend the `SpringBootServerInitializer` class if the application is packaged and deployed as a WAR file.

The `@SpringBootApplication` annotation combines three Spring-specific annotations: `@SpringBootConfiguration`, `@EnableAutoConfiguration` and `@ComponentScan`.

#### @SpringBootConfiguration

The `@SpringBootConfiguration` annotation is a specialization of the Spring-specific `@Configuration` annotation. The class with the `@SpringBootConfiguration` is marked as the configuration class for the Spring Boot application.

#### @EnableAutoConfiguration

The `@EnableAutoConfiguration` annotation is Spring-specific annotation that enables the Spring Boot automatic configuration.

## Actuator

The Spring Boot Actuator allows for monitoring and management capabilities for the Spring Boot Application. A major advantage of using the Spring Boot Actuator is that it implements a number of production-ready features without requiring the developer to construct their own implementations.

If Maven is used as the build tool, then the `spring-boot-starter-actuator` dependency can be specified in the `pom.xml` configuration file.

## Integration with Spring Framework Modules

Spring Boot has a number of existing Spring Framework Modules.

### Spring Security

Spring Boot has integration with the Spring Security Module. The simplest way for integrating Spring Boot with Spring Security is to declare the starter dependency in the build configuration file.

If Maven is used as the build tool, then the dependency with artifact ID `spring-boot-starter-security` dependency can be specified in the `pom.xml` configuration file.

## Application servers

By default, Spring boot provides embedded web servers (such as Tomcat) out-of-the-box. However, Spring Boot can also be deployed as a WAR file on a standalone WildFly application server.

If Maven is used as the build tool, there is a `wildfly-maven-plugin` Maven plugin that allows for automatic deployment of the generated WAR file.
