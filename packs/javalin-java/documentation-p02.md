---
title: "Documentation (part 2/2)"
source: https://javalin.io/documentation
domain: javalin-java
license: CC-BY-SA-4.0
tags: javalin jvm framework, kotlin java web framework, lightweight jvm framework, javalin jetty embedded
fetched: 2026-07-02
part: 2/2
---

## Server-sent Events

Server-sent events (often also called event source) are very simple in Javalin. You call `config.routes.sse()`, which gives you access to the connected `SseClient`:

- Java
- Kotlin

```java
config.routes.sse("/sse", client -> {
    client.sendEvent("connected", "Hello, SSE");
    client.onClose(() -> System.out.println("Client disconnected"));
    client.close(); // close the client
});
```

```kotlin
config.routes.sse("/sse") { client ->
    client.sendEvent("connected", "Hello, SSE")
    client.onClose { println("Client disconnected") }
    client.close() // close the client
}
```

Clients are automatically closed when leaving the handler, if you need to use the client outside the handler, you can use `client.keepAlive()`:

- Java
- Kotlin

```java
Queue<SseClient> clients = new ConcurrentLinkedQueue<SseClient>();

config.routes.sse("/sse", client -> {
    client.keepAlive();
    client.onClose(() -> clients.remove(client));
    clients.add(client);
});
```

```kotlin
val clients = ConcurrentLinkedQueue<SseClient>()

config.routes.sse("/sse") { client ->
    client.keepAlive()
    client.onClose { clients.remove(client) }
    clients.add(client)
}
```

### SseClient API

```java
sendEvent("myMessage")                      // calls emit("message", "myMessage", noId)
sendEvent("eventName", "myMessage")         // calls emit("eventName", "myMessage", noId)
sendEvent("eventName", "myMessage", "id")   // calls emit("eventName", "myMessage", "id")
sendData("myMessage")                       // calls emit("myMessage", noId) — no event name
sendData("myMessage", "id")                 // calls emit("myMessage", "id")  — no event name
sendComment("myComment")                    // calls emit("myComment")
onClose(runnable)                           // callback which runs when a client closes its connection
keepAlive()                                 // keeps the connection alive. useful if you want to keep a list of clients to broadcast to.
close()                                     // closes the connection
terminated()                                // returns true if the connection has been closed
ctx()                                       // the Context from when the client connected (to fetch query-params, etc)
```

`sendData` emits an SSE message without an `event:` field, so browsers fire the generic `message` event for it (rather than a named event like with `sendEvent`). Data is serialized the same way as `sendEvent` — an `InputStream` is passed through as-is, anything else is serialized via the configured JSON mapper.


## Configuration

You can pass a config object when creating a new instance of Javalin. Most of Javalin’s configuration is available through subconfigs, but there are also a few direct properties and functions:

```java
Javalin.create(config -> {
    config.http // The http layer configuration: etags, request size, timeout, etc
    config.router // The routing configuration: context path, slash treatment, etc
    config.routes // Routes configuration: HTTP handlers, WebSocket handlers, SSE, exceptions, errors
    config.jetty // The embedded Jetty webserver configuration
    config.staticFiles // Static files and webjars configuration
    config.spaRoot // Single Page Application roots configuration
    config.requestLogger // Request Logger configuration: http and websocket loggers
    config.bundledPlugins // Bundled plugins configuration: enable bundled plugins or add custom ones
    config.events // Events configuration: server lifecycle events, handler added events
    config.contextResolver // Context resolver implementation configuration
    config.validation // Default validator configuration
    config.concurrency.useVirtualThreads // Use virtual threads (based on Java Project Loom)
    config.startup.showJavalinBanner // Show the Javalin banner in the logs
    config.startup.showOldJavalinVersionWarning // Show a warning if an old Javalin version is being used
    config.startup.startupWatcherEnabled // Print warning if instance was not started after 5 seconds

    config.jsonMapper(jsonMapper) // Set a custom JsonMapper
    config.fileRenderer(fileRenderer) // Set a custom FileRenderer
    config.resourceHandler(resourceHandler) // Set a custom ResourceHandler for static files (Jetty-free)
    config.registerPlugin(plugin) // Register a plugin
    config.appData(key, data) // Store data on the Javalin instance

    config.unsafe // Advanced/unsafe API providing access to internal Javalin configuration (use with caution)
});
```

All available subconfigs are explained in the sections below.

### HttpConfig

- Java
- Kotlin

```java
Javalin.create(config -> {
    config.http.generateEtags = booleanValue;       // if javalin should generate etags for dynamic responses (not static files)
    config.http.prefer405over404 = booleanValue;    // return 405 instead of 404 if path is mapped to different HTTP method
    config.http.maxRequestSize = longValue;         // the max size of request body that can be accessed without using an InputStream
    config.http.responseBufferSize = intValue;      // the size of the response buffer (default 32kb)
    config.http.defaultContentType = stringValue;   // the default content type
    config.http.asyncTimeout = longValue;           // timeout in milliseconds for async requests (0 means no timeout)
    config.http.strictContentTypes = booleanValue;  // throw exception if e.g content-type is missing/incorrect when attempting to parse JSON
    
    config.http.compressionStrategy = new CompressionStrategy(new Brotli(lvl), new Gzip(lvl));
    config.http.compressionStrategy = new CompressionStrategy(null, new Gzip(lvl));
    config.http.compressionStrategy = new CompressionStrategy(new Brotli(lvl), null);
    config.http.compressionStrategy = new CompressionStrategy(null, null, new Zstd(lvl));
    config.http.compressionStrategy = CompressionStrategy.NONE;
});
```

```kotlin
Javalin.create { config ->
    config.http.generateEtags = booleanValue        // if javalin should generate etags for dynamic responses (not static files)
    config.http.prefer405over404 = booleanValue     // return 405 instead of 404 if path is mapped to different HTTP method
    config.http.maxRequestSize = longValue          // the max size of request body that can be accessed without using an InputStream
    config.http.responseBufferSize = intValue        // the size of the response buffer (default 32kb)
    config.http.defaultContentType = stringValue    // the default content type
    config.http.asyncTimeout = longValue            // timeout in milliseconds for async requests (0 means no timeout)
    config.http.strictContentTypes = booleanValue   // throw exception if e.g content-type is missing/incorrect when attempting to parse JSON

    config.http.compressionStrategy = CompressionStrategy(Brotli(lvl), Gzip(lvl))
    config.http.compressionStrategy = CompressionStrategy(null, Gzip(lvl))
    config.http.compressionStrategy = CompressionStrategy(Brotli(lvl), null)
    config.http.compressionStrategy = CompressionStrategy(null, null, Zstd(lvl))
    config.http.compressionStrategy = CompressionStrategy.NONE
}
```

### ContextResolvers

Some of the methods in `Context` can be configured through the `ContextResolvers` configuration class:

- Java
- Kotlin

```java
Javalin.create(config -> {
    config.contextResolver.ip = ctx -> "custom ip";           // called by Context#ip()
    config.contextResolver.host = ctx -> "custom host";       // called by Context#host()
    config.contextResolver.scheme = ctx -> "custom scheme";   // called by Context#scheme()
    config.contextResolver.url = ctx -> "custom url";         // called by Context#url()
    config.contextResolver.fullUrl = ctx -> "custom fullUrl"; // called by Context#fullUrl()
});
```

```kotlin
Javalin.create { config ->
    config.contextResolver.ip = { ctx -> "custom ip" }           // called by Context#ip()
    config.contextResolver.host = { ctx -> "custom host" }       // called by Context#host()
    config.contextResolver.scheme = { ctx -> "custom scheme" }   // called by Context#scheme()
    config.contextResolver.url = { ctx -> "custom url" }         // called by Context#url()
    config.contextResolver.fullUrl = { ctx -> "custom fullUrl" } // called by Context#fullUrl()
}
```

### JettyConfig

- Java
- Kotlin

```java
Javalin.create(config -> {
    config.jetty.host = "localhost"; // set the host for Jetty
    config.jetty.port = 1234; // set the port for Jetty
    config.jetty.threadPool = new ThreadPool(); // set the thread pool for Jetty
    config.jetty.timeoutStatus = 408; // set the timeout status for Jetty (default 408)
    config.jetty.clientAbortStatus = 499; // set the abort status for Jetty (default 499)
    config.jetty.multipartConfig = new MultipartConfig(); // set the multipart config for Jetty
    config.jetty.modifyWebSocketServletFactory(factory -> {}); // modify the JettyWebSocketServletFactory
    config.jetty.modifyServer(server -> {}); // modify the Jetty Server
    config.jetty.modifyServletContextHandler(handler -> {}); // modify the ServletContextHandler (you can set a SessionHandler here)
    config.jetty.modifyHttpConfiguration(httpConfig -> {}); // modify the HttpConfiguration
    config.jetty.addConnector((server, httpConfig) -> new ServerConnector(server)); // add a connector to the Jetty Server
});
```

```kotlin
Javalin.create { config ->
    config.jetty.host = "localhost" // set the host for Jetty
    config.jetty.port = 1234 // set the port for Jetty
    config.jetty.threadPool = ThreadPool() // set the thread pool for Jetty
    config.jetty.timeoutStatus = 408 // set the timeout status for Jetty (default 408)
    config.jetty.clientAbortStatus = 499 // set the abort status for Jetty (default 499)
    config.jetty.multipartConfig = MultipartConfig() // set the multipart config for Jetty
    config.jetty.modifyWebSocketServletFactory { factory -> } // modify the JettyWebSocketServletFactory
    config.jetty.modifyServer { server -> } // modify the Jetty Server
    config.jetty.modifyServletContextHandler { handler -> } // modify the ServletContextHandler (you can set a SessionHandler here)
    config.jetty.modifyHttpConfiguration { httpConfig -> } // modify the HttpConfiguration
    config.jetty.addConnector { server, httpConfig -> ServerConnector(server) } // add a connector to the Jetty Server
}
```

#### MultipartConfig

Javalin uses standard servlet file upload handling to deal with multipart requests. This allows for configuring the maximum size for each individual file, the maximum size for the entire request, the maximum size of file to handle via in-memory upload and the cache directory to write uploaded files to if they exceed this limit.

All of these values can be configured through the config as follows

- Java
- Kotlin

```java
Javalin.create(config -> {
  config.jetty.multipartConfig.cacheDirectory("c:/temp"); //where to write files that exceed the in memory limit
  config.jetty.multipartConfig.maxFileSize(100, SizeUnit.MB); //the maximum individual file size allowed
  config.jetty.multipartConfig.maxInMemoryFileSize(10, SizeUnit.MB); //the maximum file size to handle in memory
  config.jetty.multipartConfig.maxTotalRequestSize(1, SizeUnit.GB); //the maximum size of the entire multipart request
});
```

```kotlin
Javalin.create { config ->
  config.jetty.multipartConfig.cacheDirectory("c:/temp") //where to write files that exceed the in memory limit
  config.jetty.multipartConfig.maxFileSize(100, SizeUnit.MB) //the maximum individual file size allowed
  config.jetty.multipartConfig.maxInMemoryFileSize(10, SizeUnit.MB) //the maximum file size to handle in memory
  config.jetty.multipartConfig.maxTotalRequestSize(1, SizeUnit.GB) //the maximum size of the entire multipart request
}
```

### RequestLoggerConfig

You can add a HTTP request logger by calling `config.requestLogger.http()`. The method takes a `Context` and the time in milliseconds it took to finish the request:

- Java
- Kotlin

```java
Javalin.create(config -> {
    config.requestLogger.http((ctx, ms) -> {
        // log things here
    });
});
```

```kotlin
Javalin.create { config ->
    config.requestLogger.http { ctx, ms ->
        // log things here
    }
}
```

You can add a WebSocket logger by calling `config.requestLogger.ws()`. The method takes a the same arguments as a normal `config.routes.ws()` call, and can be used to log events of all types. The following example just shows `onMessage`, but `onConnect`, `onError` and `onClose` are all available:

- Java
- Kotlin

```java
Javalin.create(config -> {
    config.requestLogger.ws(ws -> {
        ws.onMessage(ctx -> {
            System.out.println("Received: " + ctx.message());
        });
    });
});
```

```kotlin
Javalin.create { config ->
    config.requestLogger.ws { ws ->
        ws.onMessage { ctx ->
            println("Received: " + ctx.message())
        }
    }
}
```

The logger runs after the WebSocket handler for the endpoint.

### RouterConfig

- Java
- Kotlin

```java
Javalin.create(config -> {
    config.router.contextPath = stringValue; // the context path (ex '/blog' if you are hosting an app on a subpath, like 'mydomain.com/blog')
    config.router.ignoreTrailingSlashes = booleanValue; // treat '/path' and '/path/' as the same path
    config.router.treatMultipleSlashesAsSingleSlash = booleanValue; // treat '/path//subpath' and '/path/subpath' as the same path
    config.router.caseInsensitiveRoutes = booleanValue; // treat '/PATH' and '/path' as the same path
});
```

```kotlin
Javalin.create { config ->
    config.router.contextPath = stringValue // the context path (ex '/blog' if you are hosting an app on a subpath, like 'mydomain.com/blog')
    config.router.ignoreTrailingSlashes = booleanValue // treat '/path' and '/path/' as the same path
    config.router.treatMultipleSlashesAsSingleSlash = booleanValue // treat '/path//subpath' and '/path/subpath' as the same path
    config.router.caseInsensitiveRoutes = booleanValue // treat '/PATH' and '/path' as the same path
}
```

### SpaRootConfig

Single page application (SPA) mode is similar to static file handling. It runs after endpoint matching, and after static file handling. It’s basically a very fancy 404 mapper, which converts any 404’s into a specified page. You can define multiple single page handlers for your application by specifying different root paths.

You can enabled single page mode by doing `config.spaRoot.addFile("/root", "/path/to/file.html")`, and/or `config.spaRoot.addFile("/root", "/path/to/file.html", Location.EXTERNAL)`.

#### Dynamic single page handler

You can also use a `Handler` to serve your single page root (as opposed to a static file):

```java
config.spaRoot.addHandler("/root",  ctx -> {
    ctx.html(...);
});
```

### StaticFileConfig

You can enable static file serving by doing `config.staticFiles.add("/directory", location)`. Static resource handling is done **after** endpoint matching, meaning your own GET endpoints have higher priority. The process looks like this:

```txt
run before-handlers
run endpoint-handlers
if no endpoint-handler found
    run static-file-handlers
    if static-file-found
        static-file-handler sends response
    else
        response is 404
run after-handlers
```

For more advanced use cases, Javalin has a `StaticFileConfig` class:

- Java
- Kotlin

```java
Javalin.create(config -> {
  config.staticFiles.add(staticFiles -> {
    staticFiles.hostedPath = "/";                   // change to host files on a subpath, like '/assets'
    staticFiles.directory = "/public";              // the directory where your files are located
    staticFiles.location = Location.CLASSPATH;      // Location.CLASSPATH (jar) or Location.EXTERNAL (file system)
    staticFiles.precompressMaxSize = 0;             // max size for pre-compression in bytes (-1 to disable, 0 for all sizes)
    staticFiles.aliasCheck = null;                  // you can configure this to enable symlinks (= ContextHandler.ApproveAliases())
    staticFiles.headers = Map.of(...);              // headers that will be set for the files
    staticFiles.skipFileFunction = req -> false;    // you can use this to skip certain files in the dir, based on the HttpServletRequest
    staticFiles.mimeTypes.add(mimeType, ext);       // you can add custom mimetypes for extensions
    staticFiles.roles = Set.of(roles);              // roles that are allowed to access the static files (used in beforeMatched)
  });
});
```

```kotlin
Javalin.create { config ->
  config.staticFiles.add { staticFiles ->
    staticFiles.hostedPath = "/"                    // change to host files on a subpath, like '/assets'
    staticFiles.directory = "/public"               // the directory where your files are located
    staticFiles.location = Location.CLASSPATH       // Location.CLASSPATH (jar) or Location.EXTERNAL (file system)
    staticFiles.precompressMaxSize = 0              // max size for pre-compression in bytes (-1 to disable, 0 for all sizes)
    staticFiles.aliasCheck = null                   // you can configure this to enable symlinks (= ContextHandler.ApproveAliases())
    staticFiles.headers = mapOf(...)                // headers that will be set for the files
    staticFiles.skipFileFunction = { req -> false } // you can use this to skip certain files in the dir, based on the HttpServletRequest
    staticFiles.mimeTypes.add(mimeType, ext)        // you can add custom mimetypes for extensions
    staticFiles.roles = setOf(roles)                // roles that are allowed to access the static files (used in beforeMatched)
  }
}
```

You can call `config.staticFiles.add(...)` multiple times to set up multiple handlers. No configuration is shared between handlers.

WebJars can be enabled by calling `config.staticFiles.enableWebjars()`, they will be available at `/webjars/name/version/file.ext`. WebJars can be found on https://www.webjars.org/. Everything available through NPM is also available through WebJars.

#### Jetty-free static file serving

If you want to serve static files without depending on Jetty’s resource handling, you can use the `JavalinStaticResourceHandler`:

- Java
- Kotlin

```java
Javalin.create(config -> {
    config.resourceHandler(new JavalinStaticResourceHandler());
});
```

```kotlin
Javalin.create { config ->
    config.resourceHandler(JavalinStaticResourceHandler())
}
```

This is useful if you want to use Javalin with a different embedded server, or if you want to avoid Jetty-specific dependencies for static file handling.

If you are building a Single Page Application (SPA), you should have a look at the SpaRootConfig

### Logging

#### Adding a logger

Javalin does not have a logger included, which means that you have to add your own logger. If you don’t know/care a lot about Java loggers, the easiest way to fix this is to add the following dependency to your project:

```markup
<dependency>
    <groupId>org.slf4j</groupId>
    <artifactId>slf4j-simple</artifactId>
    <version>2.0.17</version>
</dependency>
```

### Server setup

Javalin runs on an embedded Jetty.

**Note:** Javalin 7 uses **Jetty 12** (previously Jetty 11), which means servlet packages have changed from `javax.servlet.*` to `jakarta.servlet.*`.

To start and stop the server, use `start()` and `stop`:

```java
Javalin app = Javalin.create()
    .start() // start server (sync/blocking)
    .stop() // stop server (sync/blocking)
```

There is also a convenience method `Javalin.start(config)` that creates and starts a Javalin instance in one call:

- Java
- Kotlin

```java
Javalin app = Javalin.start(config -> {
    config.jetty.port = 8080;
    config.routes.get("/", ctx -> ctx.result("Hello World"));
});
```

```kotlin
val app = Javalin.start { config ->
    config.jetty.port = 8080
    config.routes.get("/") { ctx -> ctx.result("Hello World") }
}
```

The `app.start()` method spawns a user thread, starts the server, and then returns. Your program will not exit until this thread is terminated by calling `app.stop()`.

If you want to do a clean shutdown when the program is exiting, you could use:

```java
Javalin app = Javalin.create(config -> {
    config.events.serverStopping(() -> { /* Your code here */ });
    config.events.serverStopped(() -> { /* Your code here */ });
});

Runtime.getRuntime().addShutdownHook(new Thread(() -> {
	app.stop();
}));
```

Javalin’s default Jetty server includes a `StatisticsHandler`, so graceful shutdown works out of the box. When `app.stop()` is called, the server will wait for active requests to complete before shutting down.

If you are using a custom server, make sure to add a `StatisticsHandler` for graceful shutdown:

- Java
- Kotlin

```java
Javalin.create(config -> {
    config.jetty.modifyServer(server -> server.insertHandler(new StatisticsHandler()));
});
```

```kotlin
Javalin.create { config ->
    config.jetty.modifyServer { server -> server.insertHandler(StatisticsHandler()) }
}
```

#### Setting the Host

The `Javalin#start` method is overloaded to accept the Host (IP) as the first argument:

```java
Javalin.create().start("127.0.0.1", 1235)
```

#### Custom SessionHandler

Read about how to configure sessions in our session tutorial.

#### Custom jetty handlers

You can configure your embedded jetty-server with a handler-chain (example), and Javalin will attach it’s own handlers to the end of this chain.

- Java
- Kotlin

```java
StatisticsHandler statisticsHandler = new StatisticsHandler();
Server server = new Server();
server.setHandler(statisticsHandler);

Javalin app = Javalin.create(config -> { /* your config */ });
app.unsafe.jettyInternal.server = server;
app.start();
```

```kotlin
val statisticsHandler = StatisticsHandler()
val server = Server().apply { handler = statisticsHandler }

val app = Javalin.create { /* your config */ }
app.unsafe.jettyInternal.server = server
app.start()
```

#### SSL/HTTP2

Javalin now has a SSL plugin: https://javalin.io/plugins/ssl-helpers. It’s recommended to use this plugin for setting up SSL and HTTP2/3, as it’s a lot more user-friendly than configuring it manually in Jetty.

To configure SSL or HTTP2 manually in Jetty you need to use a custom server.

An example of a custom server with SSL can be found in the examples, HelloWorldSecure.

A custom HTTP2 server is a bit more work to set up, but we have a repo with a fully functioning example server in both Kotlin and Java: javalin-http2-example

### BundledPluginsConfig

Javalin comes with several bundled plugins that can be enabled through `config.bundledPlugins`:

- Java
- Kotlin

```java
Javalin.create(config -> {
    config.bundledPlugins.enableRouteOverview("/routes");                   // HTML/JSON overview of all routes
    config.bundledPlugins.enableRouteOverview("/routes", roles);            // route overview with access roles
    config.bundledPlugins.enableBasicAuth("username", "password");          // basic auth for all routes
    config.bundledPlugins.enableGlobalHeaders(headers -> { ... });         // add global response headers
    config.bundledPlugins.enableCors(cors -> { ... });                     // enable CORS
    config.bundledPlugins.enableHttpAllowedMethodsOnRoutes();              // auto Access-Control-Allow-Methods for OPTIONS
    config.bundledPlugins.enableDevLogging();                               // development request/response logger
    config.bundledPlugins.enableDevLogging(devCfg -> { ... });             // dev logger with custom config
    config.bundledPlugins.enableRedirectToLowercasePaths();                // redirect /Users/John to /users/John
    config.bundledPlugins.enableSslRedirects();                            // redirect HTTP to HTTPS
});
```

```kotlin
Javalin.create { config ->
    config.bundledPlugins.enableRouteOverview("/routes")                    // HTML/JSON overview of all routes
    config.bundledPlugins.enableRouteOverview("/routes", roles)             // route overview with access roles
    config.bundledPlugins.enableBasicAuth("username", "password")           // basic auth for all routes
    config.bundledPlugins.enableGlobalHeaders { headers -> }               // add global response headers
    config.bundledPlugins.enableCors { cors -> }                           // enable CORS
    config.bundledPlugins.enableHttpAllowedMethodsOnRoutes()               // auto Access-Control-Allow-Methods for OPTIONS
    config.bundledPlugins.enableDevLogging()                                // development request/response logger
    config.bundledPlugins.enableDevLogging { devCfg -> }                   // dev logger with custom config
    config.bundledPlugins.enableRedirectToLowercasePaths()                 // redirect /Users/John to /users/John
    config.bundledPlugins.enableSslRedirects()                             // redirect HTTP to HTTPS
}
```


## Lifecycle events

Javalin has events for server start/stop, as well as for when handlers are added. The snippet below shows all of them in action:

- Java
- Kotlin

```java
Javalin app = Javalin.create(config -> {
    config.events.serverStarting(() -> { ... });
    config.events.serverStarted(() -> { ... });
    config.events.serverStartFailed(() -> { ... });
    config.events.serverStopping(() -> { ... });
    config.events.serverStopped(() -> { ... });
    config.events.serverStopFailed(() -> { ... });
    config.events.handlerAdded(handlerMetaInfo -> { ... });
    config.events.wsHandlerAdded(wsHandlerMetaInfo -> { ... });
});

app.start() // serverStarting -> (serverStarted || serverStartFailed)
app.stop() // serverStopping -> (serverStopped || serverStopFailed)
```

```kotlin
val app = Javalin.create { config ->
    config.events.serverStarting { ... }
    config.events.serverStarted { ... }
    config.events.serverStartFailed { ... }
    config.events.serverStopping { ... }
    config.events.serverStopped { ... }
    config.events.serverStopFailed { ... }
    config.events.handlerAdded { handlerMetaInfo -> }
    config.events.wsHandlerAdded { wsHandlerMetaInfo -> }
}

app.start() // serverStarting -> (serverStarted || serverStartFailed)
app.stop() // serverStopping -> (serverStopped || serverStopFailed)
```


## Plugins

Javalin has a plugin system, which lets you add functionality to Javalin. You do this by extending the `Plugin` class and overriding the methods you’re interested in.

See the plugins page for more information about plugins.


## FAQ

Frequently asked questions.

### Request lifecycle

The Javalin request lifecycle is pretty straightforward. The following snippet covers every place you can hook into:

```java
config.routes.before              // runs first, can throw exception (which will skip any endpoint handlers)
config.routes.beforeMatched       // runs after a matching endpoint is found, can throw exception
config.routes.get/post/patch/etc  // runs third, can throw exception
config.routes.afterMatched        // runs after the endpoint handler (only if a match was found)
config.routes.error               // runs fifth, can throw exception
config.routes.after               // runs sixth, can throw exception
config.routes.exception           // runs any time a handler throws (cannot throw exception)
JavalinConfig#requestLogger       // runs after response is written to client
```

### Rate limiting

There is a very simple rate limiter included in Javalin, available via `RateLimitPlugin`. First, register the plugin, then call it in your endpoint `Handler` functions via `ctx.with(RateLimitPlugin.class)`:

- Java
- Kotlin

```java
Javalin.create(config -> {
    config.registerPlugin(new RateLimitPlugin(cfg -> {
        // optional: customize the key function (default: ip + method + path)
        cfg.keyFunction = ctx -> ctx.ip();
    }));
    config.routes.get("/", ctx -> {
        ctx.with(RateLimitPlugin.class).requestPerTimeUnit(5, TimeUnit.MINUTES); // throws if rate limit is exceeded
        ctx.result("Hello, rate-limited World!");
    });
});
```

```kotlin
Javalin.create { config ->
    config.registerPlugin(RateLimitPlugin { cfg ->
        // optional: customize the key function (default: ip + method + path)
        cfg.keyFunction = { ctx -> ctx.ip() }
    })
    config.routes.get("/") { ctx ->
        ctx.with(RateLimitPlugin::class).requestPerTimeUnit(5, TimeUnit.MINUTES) // throws if rate limit is exceeded
        ctx.result("Hello, rate-limited World!")
    }
}
```

Different endpoints can have different rate limits. It works as follows:

- A map of maps holds counter per key.
- On each request the counter for that key is incremented.
- If the counter exceeds the number of requests specified, an exception is thrown.
- All counters are cleared periodically on every timeunit that you specified.

### Android

Due to Jetty 11+ not working on Android, Javalin 5+ (which uses Jetty 11 or 12) is not compatible, but Javalin 4 is. You can find the docs for Javalin 4 here. You can check the status of Jetty 11+ on Android here.

### Concurrency

If your JRE supports project Loom, Javalin will use a `newVirtualThreadPerTaskExecutor` for serving requests if you set the `config.concurrency.useVirtualThreads = true` config option. Otherwise, a `QueuedThreadPool` with 250 threads will be used.

Each incoming request is handled by a dedicated thread, so all Handler implementations should be thread-safe. This default configuration allows Javalin to handle up to 250 concurrent requests, which is generally more than enough (keep in mind, most requests are much shorter than 1 second).

If your application involves numerous long-running requests, consider exploring Asynchronous requests or investigate setting up Javalin with project Loom, detailed in the Loomylin repository.

In cases where you use `ctx.future()` or `ctx.async()`, the thread will be returned to the thread pool while the asynchronous task is running. Consequently, the request might be handled by a different thread when the asynchronous task is completed.

If you are uncertain whether your application requires asynchronous requests, it’s likely not necessary. The default configuration provides similar performance to Jetty, which can handle over a million plaintext requests per second.

#### WebSocket Message Ordering

WebSocket operates over TCP, so messages will arrive at the server in the order that they were sent by the client. Javalin then handles the messages from a given WebSocket connection sequentially. Therefore, the order that messages are handled is guaranteed to be the same as the order the client sent them in.

However, different connections will be handled in parallel on multiple threads, so the WebSocket event handlers should be thread-safe.

### Testing

People often ask how to test Javalin apps. Since Javalin is just a library, you can instantiate and start the server programmatically. This means testing is really up to you. There is a tutorial at /tutorials/testing which goes through some different types of tests (unit tests, functional/integration tests, ui/end-to-end tests). You can read it to get some ideas for how to test your app.

### Javadoc

There is a Javadoc available at javadoc.io. Please contribute to the Javadoc if you can.

### Deploying

To deploy Javalin, simply create a jar with dependencies, then launch the jar with `java -jar filename.jar`. That’s it. Javalin has an embedded server, so you don’t need an application server.

Deploying Javalin to:

- Heroku (tutorial)
- AWS / Lambda (example)

### Other web servers

Javalin is primarily meant to be used with the embedded Jetty server, but if you want to run Javalin on another web server (such as Tomcat), you can use Maven or Gradle to exclude Jetty, and attach Javalin as a servlet.

### Uploads

Uploaded files are easily accessible via `ctx.uploadedFiles()`:

- Java
- Kotlin

```java
config.routes.post("/upload", ctx -> {
    ctx.uploadedFiles("files").forEach(uploadedFile ->
        FileUtil.streamToFile(uploadedFile.content(), "upload/" + uploadedFile.filename()));
});
```

```kotlin
config.routes.post("/upload") { ctx ->
    ctx.uploadedFiles("files").forEach { uploadedFile ->
        FileUtil.streamToFile(uploadedFile.content(), "upload/${uploadedFile.filename()}")
    }
}
```

The corresponding HTML might look something like this:

```markup
<form method="post" action="/upload" enctype="multipart/form-data">
    <input type="file" name="files" multiple>
    <button>Submit</button>
</form>
```

### Asynchronous requests

While the default ThreadPool (250 threads) is enough for most use cases, sometimes slow operations should be run asynchronously. Luckily it’s very easy in Javalin, just pass a `Supplier<CompletableFuture>` to `ctx.future()`. Javalin will automatically switch between sync and async modes to handle the different tasks.

#### Using Futures

Let’s look at a real world example. Imagine that we have a random cat fact API that we want to call on behalf of a client. We’ll start by creating a simple method to call the API, which returns a `CompletableFuture<String>` which will resolve either to a cat fact or an error. This is possible by using Java’s native `HttpClient`:

- Java
- Kotlin

```java
private static CompletableFuture<HttpResponse<String>> getRandomCatFactFuture() {
    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create("https://catfact.ninja/fact"))
        .build();
    return httpClient.sendAsync(request, ofString());
}
```

```kotlin
private fun getRandomCatFactFuture(): CompletableFuture<HttpResponse<String>> {
    val request = HttpRequest.newBuilder()
        .uri(URI.create("https://catfact.ninja/fact"))
        .build()
    return httpClient.sendAsync(request, ofString())
}
```

Now we can use this method in our Javalin app to return cat facts to the client asynchronously:

- Java
- Kotlin

```java
config.routes.get("/cat-facts", ctx -> {
    ctx.future(() -> {
        return getRandomCatFactFuture()
            .thenAccept(response -> ctx.html(response.body()).status(response.statusCode()))
            .exceptionally(throwable -> {
                ctx.status(500).result("Could not get cat facts" + throwable.getMessage());
                return null;
            })
    });
});
```

```kotlin
config.routes.get("/cat-facts") { ctx ->
    ctx.future {
        getRandomCatFactFuture()
            .thenAccept { response -> ctx.html(response.body()).status(response.statusCode()) }
            .exceptionally { throwable ->
                ctx.status(500).result("Could not get cat facts: ${throwable.message}")
                null
            }
    }
}
```

By calling `ctx.future(supplier)` you are not putting Javalin in an async state. It’s a simple setter method, which makes it possible for Javalin to call the given supplier and switch into async mode at an appropriate time.

The `ctx.future()` method works great if you are using a `CompletableFuture` based API, like Java’s `HttpClient`, but if you have long running tasks which aren’t `CompletableFuture` based, you might want to try the `ctx.async(runnable)` (see next section).

#### Executing blocking tasks asynchronously

If you want to execute a blocking task outside of the server ThreadPool, you can use `ctx.async()`. The snippet below shows the available overloads for the method:

```plaintext
async(runnableTask)             // Javalin's default executor, no timeout or timeout callback
async(asyncConfig, runnableTask) // custom executor, timeout, and timeout callback via AsyncTaskConfig
```

Javalin will immediately start an async context and run the task on a dedicated executor service. It will resume the normal request flow (after-handlers, request-logging) once the task is done.

The snippet below shows a full example with a custom timeout, timeout handler, and a task:

- Java
- Kotlin

```java
config.routes.get("/async", ctx -> {
    ctx.async(cfg -> {
        cfg.timeout = 1000;                                    // timeout in ms
        cfg.onTimeout(c -> c.result("Request took too long")); // timeout callback
    }, () -> ctx.result(someSlowResult));                      // some long running task
});
```

```kotlin
config.routes.get("/async") { ctx ->
    ctx.async({ cfg ->
        cfg.timeout = 1000                                     // timeout in ms
        cfg.onTimeout { c -> c.result("Request took too long") } // timeout callback
    }) { ctx.result(someSlowResult) }                          // some long running task
}
```

### Configuring the JSON mapper

To configure the JsonMapper, you need to pass an object which implements the `JsonMapper` interface to `config.jsonMapper()`.

The `JsonMapper` interface has five optional methods:

```java
String toJsonString(Object obj, Type type) { // basic method for mapping to json
InputStream toJsonStream(Object obj, Type type) { // more memory efficient method for mapping to json
writeToOutputStream(Stream<*> stream, OutputStream outputStream) { // most memory efficient method for mapping to json
<T> T fromJsonString(String json, Type targetType) { // basic method for mapping from json
<T> T fromJsonStream(InputStream json, Type targetType) { // more memory efficient method for mapping from json
```

#### The default JSON mapper (Jackson)

Javalin uses Jackson as the default JSON mapper. It’s a fast and feature-rich mapper, and has the following modules enabled if they are available on the classpath:

```plaintext
com.fasterxml.jackson.module.kotlin.KotlinModule // Kotlin support
com.fasterxml.jackson.datatype.jsr310.JavaTimeModule // Java date/time support
org.ktorm.jackson.KtormModule // Ktorm support
com.fasterxml.jackson.datatype.eclipsecollections.EclipseCollectionsModule // Eclipse Collections support
```

If you need further config, you can update the default settings like this:

- Java
- Kotlin

```java
config.jsonMapper(new JavalinJackson().updateMapper(mapper -> {
    mapper.setSerializationInclusion(JsonInclude.Include.NON_NULL);
}));
```

```kotlin
config.jsonMapper(JavalinJackson().updateMapper { mapper ->
    mapper.setSerializationInclusion(JsonInclude.Include.NON_NULL)
})
```

#### GSON example

- Java
- Kotlin

```java
Gson gson = new GsonBuilder().create();
JsonMapper gsonMapper = new JsonMapper() {
    @Override
    public String toJsonString(@NotNull Object obj, @NotNull Type type) {
        return gson.toJson(obj, type);
    }

    @Override
    public <T> T fromJsonString(@NotNull String json, @NotNull Type targetType) {
        return gson.fromJson(json, targetType);
    }
};
Javalin app = Javalin.create(config -> config.jsonMapper(gsonMapper)).start(7070);
```

```kotlin
val gson = GsonBuilder().create()

val gsonMapper = object : JsonMapper {

    override fun <T : Any> fromJsonString(json: String, targetType: Type): T =
        gson.fromJson(json, targetType)

    override fun toJsonString(obj: Any, type: Type) =
        gson.toJson(obj)

}

val app = Javalin.create { it.jsonMapper(gsonMapper) }.start(7070)
```

### Adding other Servlets and Filters to Javalin

Javalin is designed to work with other `Servlet` and `Filter` instances running on the Jetty Server. Filters are pretty straightforward to add, since they don’t finish the request. If you need to add a servlet there’s an example in the repo: /src/test/java/io/javalin/examples/HelloWorldServlet.java#L21-L29

You can also use it to build simple proxy using `AsyncProxyServlet` that is part of Jetty:

```java
// Add org.eclipse.jetty:jetty-proxy to maven/gradle dependencies (Javalin 7 uses Jetty 12)
Javalin.create(config -> {
    config.jetty.modifyServletContextHandler(handler -> {
        ServletHolder proxyServlet = new ServletHolder(AsyncProxyServlet.Transparent.class);
        proxyServlet.setInitParameter("proxyTo", "https://javalin.io/");
        proxyServlet.setInitParameter("prefix", "/proxy");
        handler.addServlet(proxyServlet, "/proxy/*");
    });
}).start(7000);
```

After opening `http://localhost:7000/proxy/` you will see Javalin site (but with broken styles because of file paths).

### Views and Templates

Each Javalin instance has a `FileRenderer` attached to it. The `FileRenderer` interface has one method:

```java
String render(String filePath, Map<String, Object> model, Context context)
```

This method is called when you call `Context#render`. It can be configured through the config passed to `Javalin.create()`:

- Java
- Kotlin

```java
config.fileRenderer((filePath, model, context) -> "Rendered template");
```

```kotlin
config.fileRenderer { filePath, model, context -> "Rendered template" }
```

The default `FileRenderer` of Javalin is a singleton named `JavalinRenderer`, see the section below for more information.

### Default implementations

Javalin offers separate per-engine artifacts for template rendering (e.g. `javalin-rendering-freemarker`, `javalin-rendering-velocity`, `javalin-rendering-thymeleaf`, etc.), which follow the same version as the `javalin` artifact. You can learn more about this at /plugins/rendering.

### Vue support (JavalinVue)

If you don’t want to deal with NPM and frontend builds, Javalin has support for simplified Vue.js development.

**Note:** In Javalin 7, JavalinVue is now a plugin. You need to register it using `config.registerPlugin(new JavalinVuePlugin(...))`.

**Note:** The `LoadableData` JavaScript class is no longer included by default. If you want to use `LoadableData`, you need to explicitly enable it:

- Java
- Kotlin

```java
config.registerPlugin(new JavalinVuePlugin(vue -> {
    vue.enableLoadableData = true;
}));
```

```kotlin
config.registerPlugin(JavalinVuePlugin { vue ->
    vue.enableLoadableData = true
})
```

This requires you to make a layout template, `src/main/resources/vue/layout.html`:

```markup
<head>
    <script src="/webjars/vue/2.6.10/dist/vue.min.js"></script>
    @componentRegistration
</head>
<body>
<main id="main-vue" v-cloak>
    @routeComponent
</main>
<script>
    new Vue({el: "#main-vue"});
</script>
</body>
```

When you put `.vue` files in `src/main/resources/vue`, Javalin will scan the folder and register the components in your `<head>` tag.

Javalin will also put path-parameters in the Vue instance, which you can access like this:

```markup
<template id="thread-view">
    <div>{{ $javalin.pathParams["user"] }}</div>
</template>
<script>
    Vue.component("thread-view", {
        template: "#thread-view"
    });
</script>
```

To map a path to a Vue component you use the `VueComponent` class:

```java
config.routes.get("/messages",        new VueComponent("inbox-view"));
config.routes.get("/messages/{user}", new VueComponent("thread-view"));
```

This will give you a lot of the benefits of a modern frontend architecture, with very few of the downsides.

There are more extensive docs at /plugins/javalinvue, and there is an in-depth tutorial at /tutorials/simple-frontends-with-javalin-and-vue.

### Jetty debug logs

If you encounter `TimeoutExceptions` and `ClosedChannelExceptions` in your DEBUG logs, this is nothing to worry about. Typically, a browser will keep the HTTP connection open until the server terminates it. When this happens is decided by the server’s `idleTimeout` setting, which is 30 seconds by default in Jetty/Javalin. This is not a bug.

### Java lang Error handling

Javalin has a default error handler for `java.lang.Error` that will log the error and return a 500. The default error handler can be overridden using `config.router`:

- Java
- Kotlin

```java
Javalin.create(config -> {
    config.router.javaLangErrorHandler((res, error) -> {
        res.setStatus(HttpStatus.INTERNAL_SERVER_ERROR.getCode());
        JavalinLogger.error("Exception occurred while servicing http-request", error);
    });
});
```

```kotlin
Javalin.create { config ->
    config.router.javaLangErrorHandler { res, error ->
        res.status = HttpStatus.INTERNAL_SERVER_ERROR.code
        JavalinLogger.error("Exception occurred while servicing http-request", error)
    }
}
```

### Minecraft

A lot of people use Javalin for Minecraft servers, and they often have issues with Jetty and WebSockets.

Please consider consulting our Minecraft tutorial if you’re working with Javalin and a Minecraft server.

#### Relocation

Using relocate is not required, but it can easily conflict with other plugin dependencies. If this is a publicly released plugin, this step is recommended to make Javalin work on a different Minecraft Server.

Usually jetty causes the conflict, you can add gradle script to `build.gradle` following after adding the `shadow-jar` gradle plugin:

```groovy
shadowJar {
    relocate 'org.eclipse.jetty', 'shadow.org.eclipse.jetty'
}
```

#### Custom classloader

If you encounter some dependency missing errors such as `java.lang.NoClassDefFoundError` and `java.lang.ClassNotFoundException`, try to solve it by:

```java
ClassLoader classLoader = Thread.currentThread().getContextClassLoader();
Thread.currentThread().setContextClassLoader(RemoteAPI.class.getClassLoader());
Javalin app = Javalin.create().start(PORT);
Thread.currentThread().setContextClassLoader(classLoader);
```

RemoteAPI can usually use the class loader of the main class of the plugin. On Bukkit and Spigot it is a class extends `org.bukkit.plugin.java#JavaPlugin`, on BungeeCord and WaterFall it is a class extends `net.md_5.bungee.api.plugin#Plugin`. Get it via `{your plugin's main class}.class.getClassLoader()` .

After switching the class loader, you may still receive a missing dependency error from Javalin. You only need to add the corresponding dependency as prompted in the Javalin log.

#### Relevant issues

- https://github.com/javalin/javalin/issues/358 (with solution)
- https://github.com/javalin/javalin/issues/232
- https://github.com/javalin/javalin/issues/1462

### Documentation for previous versions

Docs for 6.7.0 (last 6.X version) can be found here. Docs for 5.6.X (last 5.X version) can be found here. Docs for 4.6.X (last 4.X version) can be found here. Docs for 3.13.X (last 3.X version) can be found here. Docs for 2.8.0 (last 2.X version) can be found here. Docs for 1.7.0 (last 1.X version) can be found here.

You've reached the end of the docs, congratulations.
