---
title: "Introduction to Iris"
source: https://www.iris-go.com/docs/
domain: iris-go
license: CC-BY-SA-4.0
tags: iris go framework, golang web framework, go http framework, iris mvc router
fetched: 2026-07-02
---

# Introduction to Iris 

Iris is a fast, simple yet fully featured and very efficient web framework for Go. It provides a beautifully expressive and easy to use foundation for your next website or API.

## Why Iris? 

Iris is built for developers who want to build simple, reliable, and efficient web applications. It's designed to be minimal, flexible, and ships with excellent documentation.

### Key Features 

- **Optimized Router**: Blazing fast HTTP router with zero dynamic memory allocation
- **MVC Support**: First-class support for MVC patterns
- **Websocket API**: Full-featured websocket support
- **Sessions**: Built-in session handling
- **Dependency Injection**: Powerful dependency injection container
- **Authentication**: OAuth, OAuth2, JWT support out of the box
- **API Documentation**: Auto-generated Swagger/OpenAPI documentation
- **Middleware**: Rich middleware ecosystem
- **View Engines**: Multiple template engine support
- **Highly Testable**: Built with testing in mind

## Getting Started 

To start using Iris, first make sure you have Go installed on your system, then:

bash

```bash
go get github.com/kataras/iris/v12@latest
```

1

Create your first Iris web application:

go

```go
package main

import "github.com/kataras/iris/v12"

func main() {
    app := iris.New()
    
    app.Get("/", func(ctx iris.Context) {
        ctx.JSON(iris.Map{
            "message": "Hello from Iris!",
        })
    })
    
    app.Listen(":8080")
}
```

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15
