---
title: "Inversion of control"
source: https://en.wikipedia.org/wiki/Inversion_of_control
domain: spring-framework-lib
license: CC-BY-SA-4.0
tags: spring framework, java dependency injection, spring ioc container, spring bean container
fetched: 2026-07-02
---

# Inversion of control

In software design, **inversion of control** (**IoC**) is a design principle in which custom-written portions of a computer program receive the flow of control from an external source (e.g. a framework). The term "inversion" is historical: a software architecture with this design "inverts" control as compared to procedural programming. In procedural programming, a program's custom code calls reusable libraries to take care of generic tasks, but with inversion of control, it is the external code or framework that is in control and calls the custom code.

Inversion of control has been widely used by application development frameworks since the rise of GUI environments and continues to be used both in GUI environments and in web server application frameworks. Inversion of control makes the framework extensible by the methods defined by the application programmer.

Event-driven programming is often implemented using IoC so that the custom code need only be concerned with the handling of events, while the event loop and dispatch of events/messages is handled by the framework or the runtime environment. In web server application frameworks, dispatch is usually called routing, and handlers may be called endpoints.

## Alternative meaning

The phrase "inversion of control" has separately also come to be used in the community of Java programmers to refer specifically to the patterns of dependency injection (passing services to objects that need them) that occur with "IoC containers" in Java frameworks such as the Spring Framework. In this different sense, "inversion of control" refers to granting the framework control over the implementations of dependencies that are used by application objects rather than to the original meaning of granting the framework control flow (control over the time of execution of application code, e.g. callbacks).

## Overview

As an example, with traditional programming, the main function of an application might make function calls into a menu library to display a list of available commands and query the user to select one. The library thus would return the chosen option as the value of the function call, and the main function uses this value to execute the associated command. This style was common in text-based interfaces. For example, an email client may show a screen with commands to load new mail, answer the current mail, create new mail, etc., and the program execution would block until the user presses a key to select a command.

With inversion of control, on the other hand, the program would be written using a software framework that knows common behavioral and graphical elements, such as windowing systems, menus, controlling the mouse, and toolbars. The custom code "fills in the blanks" for the framework, such as supplying a table of menu items and registering a code subroutine for each item, but it is the framework that monitors the user's actions and invokes the subroutine when a menu item is selected. In the mail client example, the framework could follow both the keyboard and mouse inputs and call the command invoked by the user by either means and at the same time monitor the network interface to find out if new messages arrive and refresh the screen when some network activity is detected. The same framework could be used as the skeleton for a spreadsheet program or a text editor. Conversely, the framework knows nothing about Web browsers, spreadsheets, or text editors; implementing their functionality takes custom code.

Inversion of control carries the strong connotation that the reusable code and the problem-specific code are developed independently even though they operate together in an application. Callbacks, schedulers, event loops, and the template method are examples of design patterns that follow the inversion of control principle, although the term is most commonly used in the context of object-oriented programming. (Dependency injection is an example of the separate, specific idea of "inverting control over the implementations of dependencies" popularised by Java frameworks.)

Inversion of control is sometimes referred to as the "Hollywood Principle: Don't call us, we'll call you," reflecting how frameworks dictate execution flow.

## Background

The etymology of the phrase has been traced back to 1988, but it is closely related to the concept of **program inversion** described by Michael Jackson in his Jackson Structured Programming methodology in the 1970s. A bottom-up parser can be seen as an inversion of a top-down parser: in the one case, the control lies with the parser, while in the other case, it lies with the receiving application.

The term was used by Michael Mattsson in a thesis (with its original meaning of a framework calling application code instead of vice versa) and was then taken from there by Stefano Mazzocchi and popularized by him in 1999 in a defunct Apache Software Foundation project, Avalon, in which it referred to a parent object passing in a child object's dependencies in addition to controlling execution flow. The phrase was further popularized in 2004 by Robert C. Martin and Martin Fowler, the latter of whom traces the term's origins to the 1980s.

## Description

In traditional programming, the flow of the business logic is determined by objects that are statically bound to one another. With inversion of control, the flow depends on the object graph that is built up during program execution. Such a dynamic flow is made possible by object interactions that are defined through abstractions. This run-time binding is achieved by mechanisms such as dependency injection or a service locator. In IoC, the code could also be linked statically during compilation, but finding the code to execute by reading its description from external configuration instead of with a direct reference in the code itself.

In dependency injection, a dependent object or module is coupled to the object it needs at run time. Which particular object will satisfy the dependency during program execution typically cannot be known at compile time using static analysis. While described in terms of object interaction here, the principle can apply to other programming methodologies besides object-oriented programming.

In order for the running program to bind objects to one another, the objects must possess compatible interfaces. For example, class `A` may delegate behavior to interface `I` which is implemented by class `B`; the program instantiates `A` and `B`, and then injects `B` into `A`.

## Use

- The Mesa Programming environment for XDE, 1985
- Visual Basic (classic), 1991.
- HTML DOM event
- The Spring Framework
- ASP.NET Core
- Template method pattern

## Example code

### HTML DOM events

Web browsers implement inversion of control for DOM events in HTML. The application developer uses `document.addEventListener()` to register a callback.

```mw
<!doctype html>
<html lang="en">
<head>
     <meta charset="utf-8">
     <title>DOM Level 2</title>
</head>
<body>
     <h1>DOM Level 2 Event handler</h1>     
     <div id="output"></div>

     <script>
          var listener = function () {
               document.getElementById("output").innerHTML = "<p>The registered listener was called.</p>";
          }          
          document.addEventListener("click", listener, true);

          document.getElementById("output").innerHTML = "<p>The event handler has been registered. If you click the page, your web browser will call the event handler.</p>"
     </script>
</body>
</html>
```

### Web application frameworks

This example code for an ASP.NET Core web application creates a web application host, registers an endpoint, and then passes control to the framework:

```mw
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();
app.MapGet("/", () => "Hello World!");
app.Run();
```
