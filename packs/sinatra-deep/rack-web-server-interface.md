---
title: "Rack (web server interface)"
source: https://en.wikipedia.org/wiki/Rack_(web_server_interface)
domain: sinatra-deep
license: CC-BY-SA-4.0
tags: sinatra ruby framework, rack web interface, ruby microframework, sinatra routing dsl
fetched: 2026-07-02
---

# Rack (web server interface)

**Rack** is a modular interface between web servers and web applications developed in the Ruby programming language. With Rack, application programming interfaces (APIs) for web frameworks and middleware are wrapped into a single method call handling HTTP requests and responses.

Rack is used by many Ruby web frameworks and libraries, such as Ruby on Rails and Sinatra. It is available as a Ruby Gem. Many Ruby applications are called "rack-compliant".

Rack has inspired similar frameworks in JavaScript (jack.js), Clojure, Perl (Plack), Common Lisp (Clack), and .NET (OWIN).

## Overview

The characteristics of a Rack application is that the application object responds to the call method. The call method takes in the environment object as argument and returns the Rack response object.

### Environment

Source:

The environment that is taken as argument by the call method refers to an object that has: a) Information on the HTTP Request

This includes the information like:

- HTTP request method
- The URL information(information that would direct to the application, information that directs to the actual location in the application, query string)
- Server information like the server name and server port
- The HTTP metavariables that are received from the client

b) Rack specific information

This includes the information like

- The version of the Rack application that is running
- The URL scheme that is used, that is, if the request that is received is http or https.
- The raw HTTP data.
- A Ruby object for reporting errors.
- Information like if the application object is simultaneously invoked from another thread or process.
- Information on the server expectations and capabilities (capability of the server for connection hijacking).

In case the application is being used as a middleware, the environment can have objects that would provide session information, logging capabilities, information on the size of the data that can be used for read and writes etc. In addition to these, the server can store their own data in the environment.

### Rack response

Source:

The rack server object returns a response which contains three parts: the status, headers and the body.

- The status contains the HTTP status codes such as 200, 404.
- The header contains the response for each and gives the key-value pairs. The keys have to be strings.
- Body contains the final data which is sent by the server to the requester.

Rack::Response provides a convenient interface to create a Rack response. The class Rack::Response is defined in lib/rack/response.rb. To use the Response class, instantiate it from the middleware layer down the stack. It can be used to modify the cookies.

### Middleware in racks

Source:

Rack makes it easy to add a chain of middleware components between the application and the web server. Multiple middleware components can be used in the rack which modifies the request/response before handing it over to the next component. This is called middleware stack.

The Rack server adds multiple middle middleware by default for the functionalities like showing exception with all the details, validating the request and responses according to the Rack spec etc.

## Example application

A Rack-compatible "Hello World" application in Ruby syntax:

```mw
# helloWorld.ru
# The application that has the call method defined.
class HelloWorld
  # Call method that would return the HTTP status code, the content type and the content.
  def call (env)
    [200, {"content-type" => "text/html; charset=utf-8"}, ["Hello World"]]
  end
end

run HelloWorld.new
```

The server for the above code can be initiated using "rackup helloWorld.ru" and can be accessed at http://localhost:9292/ The default port used by the Rack application is 9292.
