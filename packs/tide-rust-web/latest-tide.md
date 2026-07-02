---
title: "tide"
source: https://docs.rs/tide/latest/tide/
domain: tide-rust-web
license: CC-BY-SA-4.0
tags: tide rust framework, async-std web framework, rust minimal framework, tide middleware endpoint
fetched: 2026-07-02
---

# Crate tide

Source

Expand description

Tide is a minimal and pragmatic Rust web application framework built for rapid development. It comes with a robust set of features that make building async web applications and APIs easier and more fun.

## §Getting started

In order to build a web app in Rust you need an HTTP server, and an async runtime. After running `cargo init` add the following lines to your `Cargo.toml` file:

```toml
# Example, use the version numbers you need
tide = "0.14.0"
async-std = { version = "1.6.0", features = ["attributes"] }
serde = { version = "1.0", features = ["derive"] }
```

## §Examples

Create an HTTP server that receives a JSON body, validates it, and responds with a confirmation message.

```
use tide::Request;
use tide::prelude::*;

#[derive(Debug, Deserialize)]
struct Animal {
    name: String,
    legs: u8,
}

#[async_std::main]
async fn main() -> tide::Result<()> {
    let mut app = tide::new();
    app.at("/orders/shoes").post(order_shoes);
    app.listen("127.0.0.1:8080").await?;
    Ok(())
}

async fn order_shoes(mut req: Request<()>) -> tide::Result {
    let Animal { name, legs } = req.body_json().await?;
    Ok(format!("Hello, {}! I've put in an order for {} shoes", name, legs).into())
}
```

```sh
$ curl localhost:8080/orders/shoes -d '{ "name": "Chashu", "legs": 4 }'
Hello, Chashu! I've put in an order for 4 shoes

$ curl localhost:8080/orders/shoes -d '{ "name": "Mary Millipede", "legs": 750 }'
number too large to fit in target type
```

See more examples in the examples directory.

## Re-exports

**`pub use http_types as http;`**

## Modules

**convert**

Traits for conversions between types.

**listener**

Types that represent HTTP transports and binding

**log**

Event logging types.

**prelude**

The Tide prelude.

**security**

HTTP Security Headers.

**sessions`sessions`**

Tide session support

**sse**

Server-Sent Events (SSE) types.

**utils**

Miscellaneous utilities.

## Structs

**Body**

A streaming HTTP body.

**Error**

The error type for HTTP operations.

**Next**

The remainder of a middleware chain, including the endpoint.

**Redirect**

A redirection endpoint.

**Request**

An HTTP request.

**Response**

An HTTP response

**ResponseBuilder**

Response Builder

**Route**

A handle to a route.

**Server**

An HTTP server.

## Enums

**StatusCode**

HTTP response status codes.

## Traits

**Endpoint**

An HTTP request handler.

**Middleware**

Middleware that wraps around the remaining middleware chain.

**Status**

Provides the

status

method for

Result

and

Option

.

## Functions

**new**

Create a new Tide server.

**with_state**

Create a new Tide server with shared application scoped state.

## Type Aliases

**Result**

A specialized Result type for Tide.
