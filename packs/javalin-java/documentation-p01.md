---
title: "Documentation (part 1/2)"
source: https://javalin.io/documentation
domain: javalin-java
license: CC-BY-SA-4.0
tags: javalin jvm framework, kotlin java web framework, lightweight jvm framework, javalin jetty embedded
fetched: 2026-07-02
part: 1/2
---

# Documentation

Javalin 7 requires **Java 17+**, and **Jetty 12+**. See the migration guide for details on upgrading from Javalin 6. Javalin follows semantic versioning, meaning there are no breaking changes unless the major (leftmost) digit changes, for example `6.X.X` to `7.X.X`.

If you want to support Javalin, please sponsor or star us:

Want to support us?

Sponsor Javalin

Using AI tools? Check out the AI instructions for Claude Code, Cursor, Copilot, and more.


## Getting Started

Add the dependency:

- Maven
- Gradle
- SBT
- Grape
- Leiningen
- Buildr
- Ivy

```markup
<dependency>
    <groupId>io.javalin</groupId>
    <artifactId>javalin</artifactId>
    <version>7.2.2</version>
</dependency>
```

Not familiar with Maven? Read our Maven tutorial.

```java
implementation("io.javalin:javalin:7.2.2")
```

Not familiar with Gradle? Read our Gradle tutorial.

```java
libraryDependencies += "io.javalin" % "javalin" % "7.2.2"
```

```java
@Grab(group='io.javalin', module='javalin', version='7.2.2')
```

```java
[io.javalin/javalin "7.2.2"]
```

```java
'io.javalin:javalin:jar:7.2.2'
```

```markup
<dependency org="io.javalin" name="javalin" rev="7.2.2" />
```

If you want Javalin with testing tools, Jackson and Logback, you can use the artifact id `javalin-bundle` instead of `javalin`.

Start coding:

- Java
- Kotlin

```java
import io.javalin.Javalin;

void main() {
    var app = Javalin.create(config -> {
        config.routes.get("/", ctx -> ctx.result("Hello World"));
    }).start(7070);
}
```

```kotlin
import io.javalin.Javalin

fun main() {
    val app = Javalin.create { config ->
        config.routes.get("/") { ctx -> ctx.result("Hello World") }
    }.start(7070)
}
```


## Modules

Javalin core is a single `javalin` artifact, with optional satellite modules you add only when you need them. For example, `javalin-bundle` packages the core with Jackson, Logback, and test tools; the per-engine `javalin-rendering-*` artifacts add template rendering; `javalin-micrometer` adds metrics; and `javalin-ssl` provides simplified SSL/TLS setup. Every satellite module tracks the same version as `javalin` itself, and you can use the `javalin-bom` module to pin one version and have every `io.javalin:*` dependency resolve to it automatically. See the full module list at /download#javalin-modules.


## Handlers

Javalin has three main handler types: before-handlers, endpoint-handlers, and after-handlers. (There are also exception-handlers and error-handlers, but we’ll get to them later). The before-, endpoint- and after-handlers require three parts:

- A verb, one of: `before`, `get`, `post`, `query`, `put`, `patch`, `delete`, `after` (… `head`, `options`, `trace`, `connect`)
- A path, ex: `/`, `/hello-world`, `/hello/{name}`
- A handler implementation, ex `ctx -> { ... }`, `MyClass implements Handler`, etc

The `Handler` interface has a void return type. You use a method like `ctx.result(result)`, `ctx.json(obj)`, or `ctx.future(future)` to set the response which will be returned to the user.

If you add multiple before/after handlers for the same path, they will be executed in the order they were added. This can be useful for adding authentication, caching, logging, etc.

You can learn about how Javalin handles concurrency in FAQ - Concurrency.

### Before handlers

Before-handlers are matched before every request (including static files).

- Java
- Kotlin

```java
config.routes.before(ctx -> {
    // runs before all requests
});
config.routes.before("/path/*", ctx -> {
    // runs before request to /path/*
});
```

```kotlin
config.routes.before { ctx ->
    // runs before all requests
}
config.routes.before("/path/*") { ctx ->
    // runs before request to /path/*
}
```

In some cases, you might want to only run a before-handler if the request will be matched (not 404). In this case you can use the `config.routes.beforeMatched` method:

- Java
- Kotlin

```java
config.routes.beforeMatched(ctx -> {
    // runs before all matched requests (including static files)
});
```

```kotlin
config.routes.beforeMatched { ctx ->
    // runs before all matched requests (including static files)
}
```

### Endpoint handlers

Endpoint handlers are the main handler type, and defines your API. You can add a GET handler to serve data to a client, or a POST handler to receive some data. Common methods are supported via `config.routes` (GET, POST, QUERY, PUT, PATCH, DELETE, HEAD, OPTIONS), uncommon operations (TRACE, CONNECT) are supported via `config.routes.addHttpHandler`.

The QUERY method is similar to GET, but allows a request body. This is useful for complex queries that don’t fit in a URL.

Endpoint-handlers are matched in the order they are defined.

- Java
- Kotlin

```java
config.routes.get("/output", ctx -> {
    // some code
    ctx.json(object);
});

config.routes.post("/input", ctx -> {
    // some code
    ctx.status(201);
});
```

```kotlin
config.routes.get("/output") { ctx ->
    // some code
    ctx.json(object)
}

config.routes.post("/input") { ctx ->
    // some code
    ctx.status(201)
}
```

Handler paths can include path-parameters. These are available via `ctx.pathParam("key")`:

- Java
- Kotlin

```java
config.routes.get("/hello/{name}", ctx -> { // the {} syntax does not allow slashes ('/') as part of the parameter
    ctx.result("Hello: " + ctx.pathParam("name"));
});
config.routes.get("/hello/<name>", ctx -> { // the <> syntax allows slashes ('/') as part of the parameter
    ctx.result("Hello: " + ctx.pathParam("name"));
});
```

```kotlin
config.routes.get("/hello/{name}") { ctx -> // the {} syntax does not allow slashes ('/') as part of the parameter
    ctx.result("Hello: " + ctx.pathParam("name"))
}
config.routes.get("/hello/<name>") { ctx -> // the <> syntax allows slashes ('/') as part of the parameter
    ctx.result("Hello: " + ctx.pathParam("name"))
}
```

Handler paths can also include wildcard parameters:

- Java
- Kotlin

```java
config.routes.get("/path/*", ctx -> { // will match anything starting with /path/
    ctx.result("You are here because " + ctx.path() + " matches " + ctx.endpoint().path);
});
```

```kotlin
config.routes.get("/path/*") { ctx -> // will match anything starting with /path/
    ctx.result("You are here because " + ctx.path() + " matches " + ctx.endpoint().path)
}
```

However, you cannot extract the value of a wildcard. Use a slash accepting path-parameter (`<param-name>` instead of `{param-name}`) if you need this behavior.

#### Custom HTTP methods

In Javalin 7, `HandlerType` is a record instead of an enum, which means you can create custom HTTP methods dynamically using `HandlerType.findOrCreate("METHOD_NAME")`. This is useful for protocols like WebDAV that use non-standard HTTP methods such as `PROPFIND`, `MKCOL`, `LOCK`, etc.

- Java
- Kotlin

```java
HandlerType PROPFIND = HandlerType.findOrCreate("PROPFIND");

Javalin.create(config -> {
    config.routes.addHttpHandler(PROPFIND, "/webdav/{resource}", ctx -> {
        ctx.result("PROPFIND: " + ctx.pathParam("resource"));
    });
});
```

```kotlin
val PROPFIND = HandlerType.findOrCreate("PROPFIND")

Javalin.create { config ->
    config.routes.addHttpHandler(PROPFIND, "/webdav/{resource}") { ctx ->
        ctx.result("PROPFIND: " + ctx.pathParam("resource"))
    }
}
```

Custom methods work with all Javalin features including path parameters, roles, before/after handlers, and exception handling. Method names must consist of uppercase letters only (e.g. `PROPFIND`, `MKCOL`).

### After handlers

After-handlers run after every request (even if an exception occurred)

- Java
- Kotlin

```java
config.routes.after(ctx -> {
    // run after all requests
});
config.routes.after("/path/*", ctx -> {
    // runs after request to /path/*
});
```

```kotlin
config.routes.after { ctx ->
    // run after all requests
}
config.routes.after("/path/*") { ctx ->
    // runs after request to /path/*
}
```

In some cases, you might want to only run an after-handler if the request will be matched (not 404). In this case you can use the `config.routes.afterMatched` method:

- Java
- Kotlin

```java
config.routes.afterMatched(ctx -> {
    // runs after all matched requests (including static files)
});
```

```kotlin
config.routes.afterMatched { ctx ->
    // runs after all matched requests (including static files)
}
```

### Wrapper handlers

Wrapper-handlers run “around” endpoint handlers. The `HandlerWrapper` functional interface receives an `Endpoint` (with `method`, `path`, and `handler`) and returns a new `Handler` that wraps the original.

This is useful for propagating context like `ThreadLocal` or `ScopedValue`:

- Java
- Kotlin

```java
config.router.handlerWrapper(endpoint -> ctx -> {
    ScopedValue.where(MY_VALUE, "something").run(() -> {
        endpoint.handler.handle(ctx);
    });
});
```

```kotlin
config.router.handlerWrapper { endpoint -> Handler { ctx ->
    ScopedValue.where(MY_VALUE, "something").run {
        endpoint.handler.handle(ctx)
    }
}}
```

You can also wrap only HTTP endpoints (excluding before/after handlers):

- Java
- Kotlin

```java
config.router.handlerWrapper(endpoint -> {
    if (endpoint.method.isHttpMethod()) {
        return ctx -> {
            // wrap logic
            endpoint.handler.handle(ctx);
        };
    }
    return endpoint.handler;
});
```

```kotlin
config.router.handlerWrapper { endpoint ->
    if (endpoint.method.isHttpMethod) {
        Handler { ctx ->
            // wrap logic
            endpoint.handler.handle(ctx)
        }
    } else {
        endpoint.handler
    }
}
```

### Context

The `Context` object provides you with everything you need to handle a http-request. It contains the underlying servlet-request and servlet-response, and a bunch of getters and setters.

```java
// Request methods
body()                                // request body as string
bodyAsBytes()                         // request body as array of bytes
bodyAsClass(clazz)                    // request body as specified class (deserialized from JSON)
bodyStreamAsClass(clazz)              // request body as specified class (memory optimized version of above)
bodyValidator(clazz)                  // request body as validator typed as specified class
bodyInputStream()                     // the underlying input stream of the request
uploadedFile("name")                  // uploaded file by name
uploadedFiles("name")                 // all uploaded files by name
uploadedFiles()                       // all uploaded files as list
uploadedFileMap()                     // all uploaded files as a "names by files" map
formParam("name")                     // form parameter by name, as string
formParamAsClass("name", clazz)       // form parameter by name, as validator typed as specified class
formParams("name")                    // list of form parameters by name
formParamMap()                        // map of all form parameters
pathParam("name")                     // path parameter by name as string
pathParamAsClass("name", clazz)       // path parameter as validator typed as specified class
pathParamMap()                        // map of all path parameters
basicAuthCredentials()                // basic auth credentials (or null if not set)
attribute("name", value)              // set an attribute on the request
attribute("name")                     // get an attribute on the request
attributeOrCompute("name", ctx -> {}) // get an attribute or compute it based on the context if absent
attributeMap()                        // map of all attributes on the request
contentLength()                       // content length of the request body
contentType()                         // request content type
cookie("name")                        // request cookie by name
cookieMap()                           // map of all request cookies
header("name")                        // request header by name (can be used with Header.HEADERNAME)
headerAsClass("name", clazz)          // request header by name, as validator typed as specified class
headerMap()                           // map of all request headers
host()                                // host as string
ip()                                  // ip as string
isMultipart()                         // true if the request is multipart
isMultipartFormData()                 // true if the request is multipart/formdata
method()                              // request methods (GET, POST, etc)
path()                                // request path
port()                                // request port
protocol()                            // request protocol
queryParam("name")                    // query param by name as string
queryParamAsClass("name", clazz)      // query param by name, as validator typed as specified class
queryParamsAsClass("name", clazz)     // query param list by name, as validator typed as list of specified class
queryParams("name")                   // list of query parameters by name
queryParamMap()                       // map of all query parameters
queryString()                         // full query string
scheme()                              // request scheme
sessionAttribute("name", value)       // set a session attribute
sessionAttribute("name")              // get a session attribute
consumeSessionAttribute("name")       // get a session attribute, and set value to null
cachedSessionAttribute("name", value) // set a session attribute, and cache the value as a request attribute
cachedSessionAttribute("name")        // get a session attribute, and cache the value as a request attribute
cachedSessionAttributeOrCompute(...)  // same as above, but compute and set if value is absent
sessionAttributeMap()                 // map of all session attributes
url()                                 // request url
fullUrl()                             // request url + query string
contextPath()                         // request context path
userAgent()                           // request user agent
req()                                 // get the underlying HttpServletRequest

// Response methods
result("result")                      // set result stream to specified string (overwrites any previously set result)
result(byteArray)                     // set result stream to specified byte array (overwrites any previously set result)
result(inputStream)                   // set result stream to specified input stream (overwrites any previously set result)
future(futureSupplier)                // set the result to be a future, see async section (overwrites any previously set result)
writeSeekableStream(stream, type)     // write content immediately as seekable stream (useful for audio and video)
result()                              // get current result stream as string (if possible), and reset result stream
resultInputStream()                   // get current result stream
contentType("type")                   // set the response content type
header("name", "value")               // set response header by name (can be used with Header.HEADERNAME)
removeHeader("name")                  // remove a response header by name
redirect("/path", code)               // redirect to the given path with the given status code
status(code)                          // set the response status code
status()                              // get the response status
statusCode()                          // get the response status code as int
cookie("name", "value", maxAge)       // set response cookie by name, with value and max-age (optional).
cookie(cookie)                        // set cookie using javalin Cookie class
removeCookie("name", "/path")         // removes cookie by name and path (optional)
json(obj)                             // calls result(jsonString), and also sets content type to json
jsonStream(obj)                       // calls result(jsonStream), and also sets content type to json
writeJsonStream(stream)               // writes JSON stream directly to response (memory efficient for large collections)
html("html")                          // calls result(string), and also sets content type to html
render("/template.tmpl", model)       // calls html(renderedTemplate)
res()                                 // get the underlying HttpServletResponse

// Other methods
async(runnable)                       // lifts request out of Jetty's ThreadPool, and moves it to Javalin's AsyncThreadPool
async(asyncConfig, runnable)          // same as above, but with additional config
endpoint()                            // get the current Endpoint (method, path, handler)
endpoint().method                     // handler type of the current handler (BEFORE, AFTER, GET, etc)
endpoint().path                       // get the path that was used to match this request (ex, "/hello/{name}")
endpoints()                           // get all endpoints visited during this request (in order)
endpoints().current()                 // get the last endpoint in the stack
endpoints().lastHttpEndpoint()        // get the last HTTP endpoint (useful in AFTER handlers)
endpoints().list()                    // get all endpoints as an unmodifiable list
routeRoles()                          // get the roles for the matched endpoint
appData(typedKey)                     // get data from the Javalin instance (see app data section below)
with(pluginClass)                     // get context plugin by class, see plugin section below
cookieStore()                         // see cookie store section below
skipRemainingHandlers()               // skip all remaining handlers for this request
```

#### App data

App data can be registered on the Javalin instance through `Javalin#create`, then accessed through the `appData(...)` method in `Context`. You need to create a typed key for your data, and then register it on the Javalin instance.

- Java
- Kotlin

```java
// register a custom attribute
var myKey = new Key<MyValue>("my-key");
var app = Javalin.create(config -> {
    config.appData(myKey, myValue);
});
// access a custom attribute
var myValue = ctx.appData(myKey); // var will be inferred to MyValue
// call a custom method on a custom attribute
ctx.appData(myKey).myMethod();
```

```kotlin
// register a custom attribute
val myKey = Key<MyValue>("my-key")
val app = Javalin.create { config ->
    config.appData(myKey, myValue)
}
// access a custom attribute
val myValue = ctx.appData(myKey) // val will be inferred to MyValue
// call a custom method on a custom attribute
ctx.appData(myKey).myMethod()
```

It can be helpful to store the key as a static field, but you can also recreate the key every time you need it.

The `CookieStore` class provides a convenient way for sharing information between handlers, request, or even servers:

```java
ctx.cookieStore().set(key, value); // store any type of value
ctx.cookieStore().get(key);        // read any type of value
ctx.cookieStore().clear();         // clear the cookie-store
```

The cookieStore works like this:

1. The first handler that matches the incoming request will populate the cookie-store-map with the data currently stored in the cookie (if any).
2. This map can now be used as a state between handlers on the same request-cycle, pretty much in the same way as `ctx.attribute()`
3. At the end of the request-cycle, the cookie-store-map is serialized, base64-encoded and written to the response as a cookie. This allows you to share the map between requests and servers (in case you are running multiple servers behind a load-balancer)

##### Example:

- Java
- Kotlin

```java
var serverOneApp = Javalin.create(config -> {
    config.routes.post("/cookie-storer", ctx -> {
        ctx.cookieStore().set("string", "Hello world!");
        ctx.cookieStore().set("i", 42);
        ctx.cookieStore().set("list", Arrays.asList("One", "Two", "Three"));
    });
});
var serverTwoApp = Javalin.create(config -> {
    config.routes.get("/cookie-reader", ctx -> { // runs on a different server than serverOneApp
        String string = ctx.cookieStore().get("string");
        int i = ctx.cookieStore().get("i");
        List<String> list = ctx.cookieStore().get("list");
    });
});
```

```kotlin
val serverOneApp = Javalin.create { config ->
    config.routes.post("/cookie-storer") { ctx ->
        ctx.cookieStore().set("string", "Hello world!")
        ctx.cookieStore().set("i", 42)
        ctx.cookieStore().set("list", listOf("One", "Two", "Three"))
    }
}
val serverTwoApp = Javalin.create { config ->
    config.routes.get("/cookie-reader") { ctx -> // runs on a different server than serverOneApp
        val string = ctx.cookieStore().get("string")
        val i = ctx.cookieStore().get("i")
        val list = ctx.cookieStore().get("list")
    }
}
```

Since the client stores the cookie, the `get` request to `serverTwoApp` will be able to retrieve the information that was passed in the `post` to `serverOneApp`.

Please note that cookies have a max-size of 4kb.


## WebSockets

Javalin has a very intuitive way of handling WebSockets. You declare an endpoint with a path and configure the different event handlers in a lambda:

- Java
- Kotlin

```java
config.routes.ws("/websocket/{path}", ws -> {
    ws.onConnect(ctx -> System.out.println("Connected"));
});
```

```kotlin
config.routes.ws("/websocket/{path}") { ws ->
    ws.onConnect { ctx -> println("Connected") }
}
```

There are a total of six events supported:

```java
ws.onConnect(WsConnectContext)
ws.onError(WsErrorContext)
ws.onClose(WsCloseContext)
ws.onMessage(WsMessageContext)
ws.onBinaryMessage(WsBinaryMessageContext)
ws.onUpgrade(WsUpgradeLogger)
```

The different flavors of `WsContext` expose different things, for example, `WsMessageContext` has the method `.message()` which gives you the message that the client sent. The differences between the different contexts is small, and a full overview can be seen in the WsContext section.

You can learn about how Javalin handles WebSocket concurrency in FAQ - Concurrency.

### WsBefore

The `config.routes.wsBefore` adds a handler that runs before a WebSocket handler. You can have as many before-handlers as you want per WebSocket endpoint, and all events are supported.

- Java
- Kotlin

```java
config.routes.wsBefore(ws -> {
    // runs before all WebSocket requests
});
config.routes.wsBefore("/path/*", ws -> {
    // runs before websocket requests to /path/*
});
```

```kotlin
config.routes.wsBefore { ws ->
    // runs before all WebSocket requests
}
config.routes.wsBefore("/path/*") { ws ->
    // runs before websocket requests to /path/*
}
```

### WsEndpoint

A WebSocket endpoint is declared with `config.routes.ws(path, handler)`. WebSocket handlers require unique paths.

- Java
- Kotlin

```java
config.routes.ws("/websocket/{path}", ws -> {
    ws.onConnect(ctx -> System.out.println("Connected"));
    ws.onMessage(ctx -> {
        User user = ctx.messageAsClass(User.class); // convert from json
        ctx.send(user); // convert to json and send back
    });
    ws.onBinaryMessage(ctx -> System.out.println("Message"))
    ws.onClose(ctx -> System.out.println("Closed"));
    ws.onError(ctx -> System.out.println("Errored"));
});
```

```kotlin
config.routes.ws("/websocket/{path}") { ws ->
    ws.onConnect { ctx -> println("Connected") }
    ws.onMessage { ctx ->
        val user = ctx.messageAsClass<User>(); // convert from json
        ctx.send(user); // convert to json and send back
    }
    ws.onBinaryMessage { ctx -> println("Message") }
    ws.onClose { ctx -> println("Closed") }
    ws.onError { ctx -> println("Errored") }
}
```

### WsAfter

The `config.routes.wsAfter` adds a handler that runs after a WebSocket handler. You can have as many after-handlers as you want per WebSocket endpoint, and all events are supported.

- Java
- Kotlin

```java
config.routes.wsAfter(ws -> {
    // runs after all WebSocket requests
});
config.routes.wsAfter("/path/*", ws -> {
    // runs after websocket requests to /path/*
});
```

```kotlin
config.routes.wsAfter { ws ->
    // runs after all WebSocket requests
}
config.routes.wsAfter("/path/*") { ws ->
    // runs after websocket requests to /path/*
}
```

### WsBeforeUpgrade

The `config.routes.wsBeforeUpgrade` adds a handler that runs before the WebSocket upgrade is attempted. This is an HTTP handler (not a WsConfig handler), so you have access to the regular `Context`. It’s useful for authentication, validation, or rejecting upgrade requests before they happen.

- Java
- Kotlin

```java
config.routes.wsBeforeUpgrade(ctx -> {
    // runs before all WebSocket upgrade requests
});
config.routes.wsBeforeUpgrade("/path/*", ctx -> {
    // runs before websocket upgrade requests to /path/*
    if (!isAuthenticated(ctx)) {
        throw new UnauthorizedResponse();
    }
});
```

```kotlin
config.routes.wsBeforeUpgrade { ctx ->
    // runs before all WebSocket upgrade requests
}
config.routes.wsBeforeUpgrade("/path/*") { ctx ->
    // runs before websocket upgrade requests to /path/*
    if (!isAuthenticated(ctx)) {
        throw UnauthorizedResponse()
    }
}
```

### WsAfterUpgrade

The `config.routes.wsAfterUpgrade` adds a handler that runs after the WebSocket upgrade is attempted. Like `wsBeforeUpgrade`, this is an HTTP handler with access to the regular `Context`.

- Java
- Kotlin

```java
config.routes.wsAfterUpgrade(ctx -> {
    // runs after all WebSocket upgrade requests
});
config.routes.wsAfterUpgrade("/path/*", ctx -> {
    // runs after websocket upgrade requests to /path/*
});
```

```kotlin
config.routes.wsAfterUpgrade { ctx ->
    // runs after all WebSocket upgrade requests
}
config.routes.wsAfterUpgrade("/path/*") { ctx ->
    // runs after websocket upgrade requests to /path/*
}
```

### WsContext

The `WsContext` object provides you with everything you need to handle a websocket-request. It contains the underlying websocket session and servlet-request, and convenience methods for sending messages to the client.

```java
// Session methods
send(obj)                               // serialize object to json string and send it to client
send("message")                         // send string to client
send(byteBuffer)                        // send bytes to client
sendAsClass(obj, clazz)                 // serialize object to json string and send it to client

// Upgrade Context methods (getters)
endpoint().path                         // get the path that was used to match this request (ex, "/hello/{name}")
host()                                  // host as string

queryParam("name")                      // query param by name as string
queryParamAsClass("name", clazz)        // query param parameter by name, as validator typed as specified class
queryParams("name")                     // list of query parameters by name
queryParamMap()                         // map of all query parameters
queryString()                           // full query string

pathParam("name")                       // path parameter by name as string
pathParamAsClass("name", clazz)         // path parameter as validator typed as specified class
pathParamMap()                          // map of all path parameters

header("name")                          // request header by name (can be used with Header.HEADERNAME)
headerAsClass("name", clazz)            // request header by name, as validator typed as specified class
headerMap()                             // map of all request headers

cookie("name")                          // request cookie by name
cookieMap()                             // map of all request cookies

attribute("name", value)                // set an attribute on the request
attribute("name")                       // get an attribute on the request
attributeMap()                          // map of all attributes on the request

sessionAttribute("name")                // get a session attribute
sessionAttributeMap()                   // map of all session attributes

sendPing()                              // send a ping to the client
sendPing(bytes)                         // send a ping with data to the client
enableAutomaticPings()                  // enable automatic pinging to avoid timeouts
enableAutomaticPings(1, HOURS, bytes)   // enable automatic pinging with custom interval and/or data
disableAutomaticPings()                 // disable automatic pinging

closeSession()                          // close the session
closeSession(closeStatus)               // close the session with a CloseStatus
closeSession(400, "reason")             // close the session with a status and reason
```

#### WsMessageContext

```java
message()                               // receive a string message from the client
messageAsClass(clazz)                   // deserialize message from client
```

#### WsBinaryMessageContext

```java
data()                                  // receive a byte array of data from the client
offset()                                // the offset of the data
length()                                // the length of the data
```

#### WsCloseContext

```java
status()                                // the int status for why connection was closed
reason()                                // the string reason for why connection was closed
```

#### WsErrorContext

```java
error()                                 // the throwable error that occurred
```

#### WsConnectContext

The `WsConnectContext` class doesn’t add anything to the base `WsContext`


## Handler groups

You can group your endpoints by using the `apiBuilder()` and `path()` methods. The `apiBuilder()` methods creates a temporary static instance of Javalin, so that you can skip the `app.` or `router.` prefix before your handlers. This is equivalent to calling `ApiBuilder.get(app/router, ...)`, which translates to `app/router.get(...)`. It is **not** a global singleton that holds static information, so you can use this safely in multiple locations and from multiple threads.

You can import all the HTTP methods with `import static io.javalin.apibuilder.ApiBuilder.*`.

- Java
- Kotlin

```java
config.routes.apiBuilder(() -> {
    path("/users", () -> {
        get(UserController::getAllUsers);
        post(UserController::createUser);
        path("/{id}", () -> {
            get(UserController::getUser);
            patch(UserController::updateUser);
            delete(UserController::deleteUser);
        });
        ws("/events", UserController::webSocketEvents);
    });
});
```

```kotlin
config.routes.apiBuilder {
    path("/users") {
        get(UserController::getAllUsers)
        post(UserController::createUser)
        path("/{id}") {
            get(UserController::getUser)
            patch(UserController::updateUser)
            delete(UserController::deleteUser)
        }
        ws("/events", UserController::webSocketEvents)
    }
}
```

Note that `path()` prefixes your paths with `/` (if you don’t add it yourself). This means that `path("api", ...)` and `path("/api", ...)` are equivalent.

### Scoping roles with path()

You can attach `RouteRole`s to every endpoint inside a `path()` block by passing a `Collection<RouteRole>` as the second argument. Roles applied at an outer `path(...)` are inherited by nested `path(...)` blocks, and any roles supplied at a nested level are merged (and deduplicated) with the inherited ones. This applies to HTTP handlers as well as `ws(...)` and `sse(...)`.

- Java
- Kotlin

```java
config.routes.apiBuilder(() -> {
    path("/users", List.of(Role.LOGGED_IN), () -> {
        get(UserController::getAllUsers);                         // requires LOGGED_IN
        post(UserController::createUser);                         // requires LOGGED_IN
        path("/{id}", List.of(Role.ADMIN), () -> {
            get(UserController::getUser);                         // requires LOGGED_IN + ADMIN
            patch(UserController::updateUser);                    // requires LOGGED_IN + ADMIN
            delete(UserController::deleteUser);                   // requires LOGGED_IN + ADMIN
        });
        ws("/events", UserController::webSocketEvents);           // requires LOGGED_IN
    });
});
```

```kotlin
config.routes.apiBuilder {
    path("/users", listOf(Role.LOGGED_IN)) {
        get(UserController::getAllUsers)                          // requires LOGGED_IN
        post(UserController::createUser)                          // requires LOGGED_IN
        path("/{id}", listOf(Role.ADMIN)) {
            get(UserController::getUser)                          // requires LOGGED_IN + ADMIN
            patch(UserController::updateUser)                     // requires LOGGED_IN + ADMIN
            delete(UserController::deleteUser)                    // requires LOGGED_IN + ADMIN
        }
        ws("/events", UserController::webSocketEvents)            // requires LOGGED_IN
    }
}
```

### CrudHandler

The `CrudHandler` is an interface that can be used within an `apiBuilder()` call:

- Java
- Kotlin

```java
config.routes.apiBuilder(() -> {
    crud("users/{user-id}", new UserController());
});
```

```kotlin
config.routes.apiBuilder {
    crud("users/{user-id}", UserController())
}
```

It implements the five most common crud operations:

```kotlin
interface CrudHandler {
    getAll(ctx)
    getOne(ctx, resourceId)
    create(ctx)
    update(ctx, resourceId)
    delete(ctx, resourceId)
}
```


## Validation

You can use Javalin’s `Validator` class for query, form, and path parameters, as well as headers and the request body:

- Java
- Kotlin

```java
ctx.queryParamAsClass("paramName", MyClass.class)   // creates a Validator<MyClass> for the value of queryParam("paramName")
ctx.formParamAsClass("paramName", MyClass.class)    // creates a Validator<MyClass> for the value of formParam("paramName")
ctx.pathParamAsClass("paramName", MyClass.class)    // creates a Validator<MyClass> for the value of pathParam("paramName")
ctx.headerAsClass("headerName", MyClass.class)      // creates a Validator<MyClass> for the value of header("paramName")
ctx.bodyValidator(MyClass.class)                    // creates a Validator<MyClass> for the value of body()
```

```kotlin
ctx.queryParamAsClass<MyClass>("paramName")         // creates a Validator<MyClass> for the value of queryParam("paramName")
ctx.formParamAsClass<MyClass>("paramName")          // creates a Validator<MyClass> for the value of formParam("paramName")
ctx.pathParamAsClass<MyClass>("paramName")          // creates a Validator<MyClass> for the value of pathParam("paramName")
ctx.headerAsClass<MyClass>("headerName")            // creates a Validator<MyClass> for the value of header("paramName")
ctx.bodyValidator<MyClass>()                        // creates a Validator<MyClass> for the value of body()
```

You can also create your own validator manually through `Validator.create(clazz, value, fieldName)`.

### Validator API

```java
allowNullable()                     // turn the Validator into a NullableValidator (must be called first)
check(predicate, "error")           // add a check with a ValidationError("error") to the Validator
check(predicate, validationError)   // add a check with a ValidationError to the Validator (can have args for localization)
get()                               // return the validated value as the specified type, or throw ValidationException
getOrThrow(exceptionFunction)       // return the validated value as the specified type, or throw custom exception
getOrDefault()                      // return default-value if value is null, else call get()
errors()                            // get all the errors of the Validator (as map("fieldName", List<ValidationError>))
```

### Validation examples

- Java
- Kotlin

```java
// VALIDATE A SINGLE QUERY PARAMETER WITH A DEFAULT VALUE /////////////////////////////////////////////
Integer myValue = ctx.queryParamAsClass("value", Integer.class).getOrDefault(788) // validate value
ctx.result(value) // return validated value to the client
// GET ?value=a would yield HTTP 400 - {"my-qp":[{"message":"TYPE_CONVERSION_FAILED","args":{},"value":"a"}]}
// GET ?value=1 would yield HTTP 200 - 1 (the validated value)
// GET ?        would yield HTTP 200 - 788 (the default value)

// VALIDATE TWO DEPENDENT QUERY PARAMETERS ////////////////////////////////////////////////////////////
Instant fromDate = ctx.queryParamAsClass("from", Instant.class).get();
Instant toDate = ctx.queryParamAsClass("to", Instant.class)
    .check(it -> it.isAfter(fromDate), "'to' has to be after 'from'")
    .get();

// VALIDATE A JSON BODY ///////////////////////////////////////////////////////////////////////////////
MyObject myObject = ctx.bodyValidator(MyObject.class)
    .check(obj -> obj.myObjectProperty == someValue, "THINGS_MUST_BE_EQUAL")
    .get();

// VALIDATE WITH CUSTOM VALIDATIONERROR ///////////////////////////////////////////////////////////////
ctx.queryParamAsClass("param", Integer.class)
    .check({ it > 5 }, new ValidationError("OVER_LIMIT", Map.of("limit", 5)))
    .get();
// GET ?param=10 would yield HTTP 400 - {"param":[{"message":"OVER_LIMIT","args":{"limit":5},"value":10}]}
```

```kotlin
// VALIDATE A SINGLE QUERY PARAMETER WITH A DEFAULT VALUE /////////////////////////////////////////////
val myValue = ctx.queryParamAsClass<Int>("value").getOrDefault(788) // validate value
ctx.result(value) // return validated value to the client
// GET ?value=a would yield HTTP 400 - {"my-qp":[{"message":"TYPE_CONVERSION_FAILED","args":{},"value":"a"}]}
// GET ?value=1 would yield HTTP 200 - 1 (the validated value)
// GET ?        would yield HTTP 200 - 788 (the default value)

// VALIDATE TWO DEPENDENT QUERY PARAMETERS ////////////////////////////////////////////////////////////
val fromDate = ctx.queryParamAsClass<Instant>("from").get()
val toDate = ctx.queryParamAsClass<Instant>("to")
    .check({ it.isAfter(fromDate) }, "'to' has to be after 'from'")
    .get()

// VALIDATE A JSON BODY ///////////////////////////////////////////////////////////////////////////////
val myObject = ctx.bodyValidator<MyObject>()
    .check({ it.myObjectProperty == someValue }, "THINGS_MUST_BE_EQUAL")
    .get()

// VALIDATE WITH CUSTOM VALIDATIONERROR ///////////////////////////////////////////////////////////////
ctx.queryParamAsClass<Int>("param")
    .check({ it > 5 }, ValidationError("OVER_LIMIT", args = mapOf("limit" to 5)))
    .get()
// GET ?param=10 would yield HTTP 400 - {"param":[{"message":"OVER_LIMIT","args":{"limit":5},"value":10}]}
```

### Collecting multiple errors

- Java
- Kotlin

```java
Validator<Integer> ageValidator = ctx.queryParamAsClass("age", Integer.class)
    .check(n -> !n.contains("-"), "ILLEGAL_CHARACTER")

// Empty map if no errors, otherwise a map with the key "age" and failed check messages in the list.
Map<String, List<Integer>> errors = ageValidator.errors();

// Merges all errors from all validators in the list. Empty map if no errors exist.
Map<String, List<Object>> manyErrors = JavalinValidation.collectErrors(ageValidator, otherValidator, ...)
```

```kotlin
val ageValidator = ctx.queryParamAsClass<Int>("age")
    .check({ !it.contains("-") }, "ILLEGAL_CHARACTER")

// Empty map if no errors, otherwise a map with the key "age" and failed check messages in the list.
val errors = ageValidator.errors()

// Merges all errors from all validators in the list. Empty map if no errors exist.
val manyErrors = listOf(ageValidator, otherValidator, ...).collectErrors()
```

### ValidationException

When a `Validator` throws, it is mapped by:

```kotlin
config.routes.exception(ValidationException::class.java) { e, ctx ->
    ctx.json(e.errors).status(400)
}
```

You can override this by doing:

- Java
- Kotlin

```java
config.routes.exception(ValidationException.class, (e, ctx) -> {
    // your code
});
```

```kotlin
config.routes.exception(ValidationException::class.java) { e, ctx ->
    // your code
}
```

### Custom converters

If you need to validate a non-included class, you have to register a custom converter:

- Java
- Kotlin

```java
Javalin.create(config -> {
    config.validation.register(Instant.class, v -> Instant.ofEpochMilli(Long.parseLong(v)));
});
```

```kotlin
Javalin.create { config ->
    config.validation.register(Instant::class.java) { Instant.ofEpochMilli(it.toLong()) }
}
```


## Access management

Javalin used to have a functional interface `AccessManager`, which let you set per-endpoint authentication and/or authorization. In Javalin 6, this has been replaced with the `beforeMatched` handler. You can read more about this in the Javalin 5 to 6 migration guide.

To manage access in Javalin 7, you would do something like this:

- Java
- Kotlin

```java
config.routes.beforeMatched(ctx -> {
    var userRole = getUserRole(ctx); // some user defined function that returns a user role
    if (!ctx.routeRoles().contains(userRole)) { // routeRoles are provided through the Context interface
        throw new UnauthorizedResponse(); // request will have to be explicitly stopped by throwing an exception
    }
});
```

```kotlin
config.routes.beforeMatched { ctx ->
    val userRole = getUserRole(ctx) // some user defined function that returns a user role
    if (!ctx.routeRoles().contains(userRole)) { // routeRoles are provided through the Context interface
        throw UnauthorizedResponse() // request will have to be explicitly stopped by throwing an exception
    }
}
```

If you’re using `apiBuilder`, you can also scope roles to a `path()` block to apply them to every endpoint inside.

The roles are set when you declare your endpoints:

- Java
- Kotlin

```java
config.routes.get("/public", ctx -> ctx.result("Hello public"), Role.OPEN);
config.routes.get("/private", ctx -> ctx.result("Hello private"), Role.LOGGED_IN);
```

```kotlin
config.routes.get("/public", { ctx -> ctx.result("Hello public") }, Role.OPEN)
config.routes.get("/private", { ctx -> ctx.result("Hello private") }, Role.LOGGED_IN)
```


## Default responses

Javalin comes with a built in class called `HttpResponseException`, which can be used for default responses. If the client accepts JSON, a JSON object is returned. Otherwise a plain text response is returned.

```java
config.routes.post("/", ctx -> { throw new ForbiddenResponse("Off limits!"); });
```

If client accepts JSON:

```java
{
    "title": "Off limits!",
    "status": 403,
    "type": "https://javalin.io/documentation#forbiddenresponse",
    "details": []
}
```

Otherwise:

```
Forbidden
```

You can include a `Map<String, String>` of details if you wish.

### RedirectResponse

Returns a 302 Found response with the default title `Redirected`.

### BadRequestResponse

Returns a 400 Bad Request response with the default title `Bad request`.

### UnauthorizedResponse

Returns a 401 Unauthorized response with the default title `Unauthorized`.

### ForbiddenResponse

Returns a 403 Forbidden response with the default title `Forbidden`.

### NotFoundResponse

Returns a 404 Not Found response with the default title `Not found`.

### MethodNotAllowedResponse

Returns a 405 Method Not Allowed response with the default title `Method not allowed`.

### ConflictResponse

Returns a 409 Conflict response with the default title `Conflict`.

### GoneResponse

Returns a 410 Gone response with the default title `Gone`.

### TooManyRequestsResponse

Returns a 429 Too Many Requests response with the default title `Too many requests`.

### InternalServerErrorResponse

Returns a 500 Internal Server Error response with the default title `Internal server error`.

### BadGatewayResponse

Returns a 502 Bad Gateway response with the default title `Bad gateway`.

### ServiceUnavailableResponse

Returns a 503 Service Unavailable response with the default title `Service unavailable`.

### GatewayTimeoutResponse

Returns a 504 Gateway Timeout response with the default title `Gateway timeout`.


## Exception Mapping

All handlers (before, endpoint, after, ws) can throw `Exception` (and any subclass of `Exception`). The `config.routes.exception()` and `config.routes.wsException()` methods give you a way of handling these exceptions:

- Java
- Kotlin

```java
Javalin.create(config -> {
    // HTTP exceptions
    config.routes.exception(NullPointerException.class, (e, ctx) -> {
        // handle nullpointers here
    });

    config.routes.exception(Exception.class, (e, ctx) -> {
        // handle general exceptions here
        // will not trigger if more specific exception-mapper found
    });

    // WebSocket exceptions
    config.routes.wsException(NullPointerException.class, (e, ctx) -> {
        // handle nullpointers here
    });

    config.routes.wsException(Exception.class, (e, ctx) -> {
        // handle general exceptions here
        // will not trigger if more specific exception-mapper found
    });
});
```

```kotlin
Javalin.create { config ->
    // HTTP exceptions
    config.routes.exception(NullPointerException::class.java) { e, ctx ->
        // handle nullpointers here
    }

    config.routes.exception(Exception::class.java) { e, ctx ->
        // handle general exceptions here
        // will not trigger if more specific exception-mapper found
    }

    // WebSocket exceptions
    config.routes.wsException(NullPointerException::class.java) { e, ctx ->
        // handle nullpointers here
    }

    config.routes.wsException(Exception::class.java) { e, ctx ->
        // handle general exceptions here
        // will not trigger if more specific exception-mapper found
    }
}
```


## Error Mapping

HTTP Error mapping is similar to exception mapping, but it operates on HTTP status codes instead of Exceptions:

- Java
- Kotlin

```java
Javalin.create(config -> {
    config.routes.error(404, ctx -> {
        ctx.result("Generic 404 message");
    });
});
```

```kotlin
Javalin.create { config ->
    config.routes.error(404) { ctx ->
        ctx.result("Generic 404 message")
    }
}
```

It can make sense to use them together:

- Java
- Kotlin

```java
Javalin.create(config -> {
    config.routes.exception(FileNotFoundException.class, (e, ctx) -> {
        ctx.status(404);
    });
    config.routes.error(404, ctx -> {
        ctx.result("Generic 404 message");
    });
});
```

```kotlin
Javalin.create { config ->
    config.routes.exception(FileNotFoundException::class.java) { e, ctx ->
        ctx.status(404)
    }
    config.routes.error(404) { ctx ->
        ctx.result("Generic 404 message")
    }
}
```

You can also include the content type when declaring your error mappers:

- Java
- Kotlin

```java
Javalin.create(config -> {
    config.routes.error(404, "html", ctx -> {
        ctx.html("Generic 404 message");
    });
});
```

```kotlin
Javalin.create { config ->
    config.routes.error(404, "html") { ctx ->
        ctx.html("Generic 404 message")
    }
}
```

This can be useful if you, for example, want one set of error handlers for HTML, and one for JSON.
