---
title: "👋 Welcome"
source: https://docs.gofiber.io/
domain: fiber-framework
license: CC-BY-SA-4.0
tags: fiber framework, fiber golang, go web framework, fasthttp server
fetched: 2026-07-02
---

# 👋 Welcome

Version: v3.x

# 👋 Welcome

Welcome to Fiber's online API documentation, complete with examples to help you start building web applications right away!

**Fiber** is an Express-inspired **web framework** built on top of Fasthttp, the **fastest** HTTP engine for Go. It is designed to facilitate rapid development with **zero memory allocations** and a strong focus on **performance**. Fiber also ships batteries included: built-in middleware, officially maintained integrations, storage drivers, and template engines cover most production needs (see Explore the Ecosystem below).

These docs cover **Fiber v3**.

tip

Coming from Fiber v2? See What's New in v3 for the migration guide and the CLI migration tool.

## Installation

First, download and install Go. Version `1.25` or higher is required.

Install Fiber using the `go get` command:

```bash
go get github.com/gofiber/fiber/v3
```

## Hello, World

Create a file named `server.go` with the simplest **Fiber** application you can write:

```go
package main

import (
    "log"

    "github.com/gofiber/fiber/v3"
)

func main() {
    app := fiber.New()

    app.Get("/", func(c fiber.Ctx) error {
        return c.SendString("Hello, World!")
    })

    log.Fatal(app.Listen(":3000"))
}
```

Run it:

```bash
go run server.go
```

Browse to `http://localhost:3000` and you should see `Hello, World!` displayed on the page.

## Basic Routing

Routing determines how an application responds to a client request at a particular endpoint, a combination of path and HTTP request method (`GET`, `PUT`, `POST`, etc.).

Route definitions follow the structure below:

```go
func (app *App) Get(path string, handler any, handlers ...any) Router
```

- `app` is an instance of **Fiber**
- `Get` is an HTTP request method; `Post`, `Put`, `Delete`, and the other methods work the same way
- `path` is a virtual path on the server
- `handler` is a function executed when the route is matched; the canonical form is `func(fiber.Ctx) error`, and a route can register multiple handlers

For an interactive breakdown of every part of a route definition, see the anatomy of a route.

A simple route and a route with a parameter:

```go
app.Get("/", func(c fiber.Ctx) error {
    return c.SendString("Hello, World!")
})
```

```go
app.Get("/:value", func(c fiber.Ctx) error {
    return c.SendString("value: " + c.Params("value"))
    
})
```

See the routing guide for optional parameters, wildcards, constraints, route groups, and the full list of supported handler types.

## Static Files

To serve static files such as **images**, **CSS**, and **JavaScript** files, register the static middleware:

```go
import "github.com/gofiber/fiber/v3/middleware/static"

app.Use("/", static.New("./public"))
```

Files in the `./public` directory are now reachable in the browser, for example at `http://localhost:3000/css/style.css`.

## Using Middleware

Middleware runs before or after your handlers and takes care of cross-cutting concerns. Registering one is a single `app.Use` call; here is the logger middleware printing every request:

```go
import "github.com/gofiber/fiber/v3/middleware/logger"

app.Use(logger.New())
```

Middleware for logging, CORS, rate limiting, sessions, compression, panic recovery, and much more ships with Fiber itself; the ecosystem section below shows where to find it all.

## Zero Allocation

caution

Fiber is optimized for **high performance**, so values returned from **fiber.Ctx** are **not** immutable by default and **will** be reused across requests. Use context values only within the handler, and do not keep any references after the handler returns.

If you need to persist a context value beyond the handler, make a copy of its **underlying buffer** using the copy builtin:

```go
func handler(c fiber.Ctx) error {
    
    result := c.Params("foo")

    
    buffer := make([]byte, len(result))
    copy(buffer, result)
    resultCopy := string(buffer)
    

    
}
```

Alternatively, you can enable the `Immutable` setting. This makes all values returned from the context immutable, allowing you to persist them anywhere, at the cost of some performance:

```go
app := fiber.New(fiber.Config{
    Immutable: true,
})
```

For details, see Immutable in the configuration reference and the GetString and GetBytes helpers.

## Explore the Ecosystem

Fiber is more than the core module. When your application grows, these officially maintained building blocks are one import away:

- **Built-in middleware**: 30+ middleware for logging, CORS, security headers, caching, rate limiting, and more live in the core module; browse the middleware overview.
- **Contrib packages**: officially maintained integrations with external dependencies, such as JWT, WebSocket, OpenTelemetry, Casbin, and structured logging adapters.
- **Storage drivers**: a growing list of backends (Redis, Postgres, MongoDB, S3, and more) behind one interface, ready to plug into the session, limiter, cache, and idempotency middleware.
- **Template engines**: server-side rendering through the Views interface, with engines like html, django, handlebars, and pug.
- **HTTP client**: a built-in client, also built on Fasthttp, for calling other services with the same performance philosophy.
- **Recipes**: runnable example projects (Docker, GORM, JWT auth, clean architecture, and more) to copy a working starting point from.

## Next Steps

Ready to go deeper? These guides and references cover the everyday tasks:

- Routing: parameters, wildcards, constraints, and route groups
- Context: reading requests and sending responses
- Error handling: custom error handlers and status codes
- Request binding and validation: map request data onto structs safely
- Templates: render views with your favorite template engine
- Configuration: every option accepted by `fiber.New`
- Testing: test handlers without a running server using `app.Test`
- Learning resources: tutorials and hands-on challenges

## Community and Help

Stuck or have questions? Join the Discord server or check the FAQ. Fiber is developed in the open on GitHub; issues, discussions, and contributions are welcome.
