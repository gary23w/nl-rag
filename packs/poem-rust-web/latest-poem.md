---
title: "poem"
source: https://docs.rs/poem/latest/poem/
domain: poem-rust-web
license: CC-BY-SA-4.0
tags: poem rust framework, rust openapi framework, rust async web, poem endpoint middleware
fetched: 2026-07-02
---

# Crate poem

Source

Expand description

Poem is a full-featured and easy-to-use web framework with the Rust programming language.

- Quickstart
- Endpoint
- Extractors
- Routing
- Responses
- Handling errors
- Middleware
- Crate features

## §Quickstart

```
use poem::{IntoResponse, Route, Server, get, handler, listener::TcpListener, web::Path};

#[handler]
fn hello(Path(name): Path<String>) -> String {
    format!("hello: {}", name)
}

#[tokio::main]
async fn main() -> Result<(), std::io::Error> {
    let app = Route::new().at("/hello/:name", get(hello));
    Server::new(TcpListener::bind("0.0.0.0:3000"))
        .run(app)
        .await
}
```

## §Endpoint

The `Endpoint` trait represents a type that can handle HTTP requests, and it returns a `Result<T: IntoResponse, Error>` type.

The `handler` macro is used to convert a function into an endpoint.

```
use poem::{
    Endpoint, Request, Result, error::NotFoundError, handler, http::StatusCode,
    test::TestClient,
};

#[handler]
fn return_str() -> &'static str {
    "hello"
}

#[handler]
fn return_err() -> Result<&'static str, NotFoundError> {
    Err(NotFoundError)
}

let resp = TestClient::new(return_str).get("/").send().await;
resp.assert_status_is_ok();
resp.assert_text("hello").await;

let resp = TestClient::new(return_err).get("/").send().await;
resp.assert_status(StatusCode::NOT_FOUND);
```

## §Extractors

The extractor is used to extract something from the HTTP request.

`Poem` provides some commonly used extractors for extracting something from HTTP requests.

In the following example, the `index` function uses 3 extractors to extract the remote address, HTTP method and URI.

```
use poem::{
    handler,
    http::{Method, Uri},
    web::RemoteAddr,
};

#[handler]
fn index(remote_addr: &RemoteAddr, method: Method, uri: &Uri) {}
```

By default, the extractor will return a `400 Bad Request` when an error occurs, but sometimes you may want to change this behavior, so you can handle the error yourself.

In the following example, when the `Query` extractor fails, it will return a `500 Internal Server` response and the reason for the error.

```
use poem::{
    IntoResponse, Response, Result, error::ParseQueryError, handler, http::StatusCode,
    web::Query,
};
use serde::Deserialize;

#[derive(Debug, Deserialize)]
struct Params {
    name: String,
}

#[handler]
fn index(res: Result<Query<Params>>) -> Result<impl IntoResponse> {
    match res {
        Ok(Query(params)) => Ok(params.name.into_response()),
        Err(err) if err.is::<ParseQueryError>() => Ok(Response::builder()
            .status(StatusCode::INTERNAL_SERVER_ERROR)
            .body(err.to_string())),
        Err(err) => Err(err),
    }
}
```

## §Routing

There are three available routes.

- `Route` Routing for path
- `RouteDomain` Routing for domain
- `RouteMethod` Routing for HTTP method

```
use poem::{Route, get, handler, post, web::Path};

#[handler]
async fn get_user(id: Path<String>) {}

#[handler]
async fn delete_user(id: Path<String>) {}

#[handler]
async fn create_user() {}

let app = Route::new()
    .at("/user/:id", get(get_user).delete(delete_user))
    .at("/user", post(create_user));
```

You can create custom extractors, see also `FromRequest`.

## §Responses

All types that can be converted to HTTP response `Response` should implement `IntoResponse`.

In the following example, the `string_response` and `status_response` functions return the `String` and `StatusCode` types, because `Poem` has implemented the `IntoResponse` trait for them.

The `no_response` function does not return a value. We can think that its return type is `()`, and `Poem` also implements `IntoResponse` for `()`, which is always converted to `200 OK`.

The `result_response` function returns a `Result` type, which means that an error may occur.

```
use poem::{Result, handler, http::StatusCode};

#[handler]
fn string_response() -> String {
    todo!()
}

#[handler]
fn status_response() -> StatusCode {
    todo!()
}

#[handler]
fn no_response() {}

#[handler]
fn result_response() -> Result<String> {
    todo!()
}
```

## §Handling errors

The following example returns customized content when `NotFoundError` occurs.

```
use poem::{
    EndpointExt, IntoResponse, Response, Route, error::NotFoundError, handler, http::StatusCode,
};

#[handler]
fn foo() {}

#[handler]
fn bar() {}

let app =
    Route::new()
        .at("/foo", foo)
        .at("/bar", bar)
        .catch_error(|err: NotFoundError| async move {
            Response::builder()
                .status(StatusCode::NOT_FOUND)
                .body("custom not found")
        });
```

## §Middleware

You can call the `with` method on the `Endpoint` to apply a middleware to an endpoint. It actually converts the original endpoint to a new endpoint.

```
use poem::{EndpointExt, Route, handler, middleware::Tracing};

#[handler]
fn index() {}

let app = Route::new().at("/", index).with(Tracing);
```

You can create your own middleware, see also `Middleware`.

## §Crate features

To avoid compiling unused dependencies, `Poem` gates certain features, all of which are disabled by default:

| Feature | Description |
|---|---|
| server | Server and listener APIs(enable by default) |
| compression | Support decompress request body and compress response body |
| cookie | Support for Cookie |
| csrf | Support for Cross-Site Request Forgery (CSRF) protection |
| multipart | Support for Multipart |
| native-tls | Support for HTTP server over TLS with `native-tls` |
| openssl-tls | Support for HTTP server over TLS with `openssl-tls` |
| opentelemetry | Support for opentelemetry |
| prometheus | Support for Prometheus |
| redis-session | Support for RedisSession |
| rustls | Support for HTTP server over TLS with `rustls` |
| session | Support for session |
| sse | Support Server-Sent Events (SSE) |
| tempfile | Support for `tempfile` |
| test | Test utilities to test your endpoints. |
| tower-compat | Adapters for `tower::Layer` and `tower::Service`. |
| websocket | Support for WebSocket |
| anyhow | Integrate with the `anyhow` crate. |
| eyre06 | Integrate with version 0.6.x of the `eyre` crate. |
| i18n | Support for internationalization |
| acme-native-roots | Support for ACME(Automatic Certificate Management Environment) |
| acme-webpki-roots | Support for ACME using webpki TLS roots rather than native TLS roots |
| tokio-metrics | Integrate with the `tokio-metrics` crate. |
| embed | Integrate with `rust-embed` crate. |
| xml | Integrate with `quick-xml` crate. |
| yaml | Integrate with `serde-yaml` crate. |
| sonic-rs | Uses `sonic-rs` instead of `serde_json`. Pls, checkout `sonic-rs` requirements to properly enable `sonic-rs` capabilities |

## Re-exports

**`pub use endpoint::Endpoint;`**

**`pub use endpoint::EndpointExt;`**

**`pub use endpoint::IntoEndpoint;`**

**`pub use error::Error;`**

**`pub use error::Result;`**

**`pub use middleware::Middleware;`**

**`pub use web::FromRequest;`**

**`pub use web::IntoResponse;`**

**`pub use web::RequestBody;`**

## Modules

**endpoint**

Endpoint related types.

**error**

Some common error types.

**http**

A general purpose library of common HTTP types

**i18n`i18n`**

Internationalization related types.

**listener`server`**

Commonly used listeners.

**middleware**

Commonly used middleware.

**session`session`**

Session management.

**test`test`**

Test utilities to test your endpoints.

**web**

Commonly used as the type of extractor or response.

## Structs

**Body**

A body object for requests and responses.

**OnUpgrade**

A future for a possible HTTP upgrade.

**PathPattern**

Container that can be used to obtain path pattern from the request.

**Request**

Represents an HTTP request.

**RequestBuilder**

An request builder.

**RequestParts**

Component parts of an HTTP Request.

**Response**

Represents an HTTP response.

**ResponseBuilder**

An response builder.

**ResponseParts**

Component parts of an HTTP Response.

**Route**

Routing object

**RouteDomain**

Routing object for

HOST

header

**RouteMethod**

Routing object for HTTP methods

**RouteScheme**

Routing object for request scheme

**Server`server`**

An HTTP Server.

**Upgraded**

An upgraded HTTP connection.

## Enums

**Addr**

An network address.

## Functions

**connect**

A helper function, similar to

RouteMethod::new().connect(ep)

.

**delete**

A helper function, similar to

RouteMethod::new().delete(ep)

.

**get**

A helper function, similar to

RouteMethod::new().get(ep)

.

**head**

A helper function, similar to

RouteMethod::new().head(ep)

.

**options**

A helper function, similar to

RouteMethod::new().options(ep)

.

**patch**

A helper function, similar to

RouteMethod::new().patch(ep)

.

**post**

A helper function, similar to

RouteMethod::new().post(ep)

.

**put**

A helper function, similar to

RouteMethod::new().put(ep)

.

**trace**

A helper function, similar to

RouteMethod::new().trace(ep)

.

## Attribute Macros

**handler**

Wrap an asynchronous function as an

Endpoint

.
