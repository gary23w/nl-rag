---
title: "Micronaut Core (part 15/27)"
source: https://docs.micronaut.io/latest/guide/index.html
domain: micronaut
license: CC-BY-SA-4.0
tags: micronaut framework, micronaut jvm, compile-time injection, microservices framework
fetched: 2026-07-02
part: 15/27
---

## 6.25.3.1 HttpServerFilter Example

Suppose you wish to trace each request to the "Hello World" example using some external system. This system could be a database or a distributed tracing service, and may require I/O operations.

You should not block the underlying Netty event loop in your filter; instead the filter should proceed with execution once any I/O is complete.

As an example, consider this `TraceService` that uses Project Reactor to compose an I/O operation:

A TraceService Example using Reactive Streams

```java
import io.micronaut.http.HttpRequest;
import org.reactivestreams.Publisher;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import jakarta.inject.Singleton;
import reactor.core.publisher.Mono;
import reactor.core.scheduler.Schedulers;

@Singleton
public class TraceService {
    private static final Logger LOG = LoggerFactory.getLogger(TraceService.class);
    public Publisher<Boolean> trace(HttpRequest<?> request) {
        return Mono.fromCallable(() -> { // (1)
            LOG.debug("Tracing request: {}", request.getUri());
            // trace logic here, potentially performing I/O (2)
            return true;
        }).subscribeOn(Schedulers.boundedElastic()) // (3)
                .flux();
    }
}
```

A TraceService Example using Reactive Streams

```kotlin
import io.micronaut.http.HttpRequest
import org.slf4j.LoggerFactory
import jakarta.inject.Singleton
import reactor.core.publisher.Flux
import reactor.core.publisher.Mono
import reactor.core.scheduler.Schedulers

@Singleton
class TraceService {

    private val LOG = LoggerFactory.getLogger(TraceService::class.java)

    internal fun trace(request: HttpRequest<*>): Flux<Boolean> {
        return Mono.fromCallable {
            // (1)
            LOG.debug("Tracing request: {}", request.uri)
            // trace logic here, potentially performing I/O (2)
            true
        }.subscribeOn(Schedulers.boundedElastic()) // (3)
            .flux()
    }
}
```

A TraceService Example using Reactive Streams

```groovy
import io.micronaut.http.HttpRequest
import org.slf4j.Logger
import org.slf4j.LoggerFactory

import jakarta.inject.Singleton
import reactor.core.publisher.Flux
import reactor.core.publisher.Mono
import reactor.core.scheduler.Schedulers

import java.util.concurrent.Callable

@Singleton
class TraceService {

    private static final Logger LOG = LoggerFactory.getLogger(TraceService.class)

    Flux<Boolean> trace(HttpRequest<?> request) {
        Mono.fromCallable(() ->  {  // (1)
            LOG.debug('Tracing request: {}', request.uri)
            // trace logic here, potentially performing I/O (2)
            return true
        }).flux().subscribeOn(Schedulers.boundedElastic()) // (3)

    }
}
```

| **1** | The Mono type creates logic that executes potentially blocking operations to write the trace data from the request |
|---|---|
| **2** | Since this is just an example, the logic does nothing yet |
| **3** | The `Schedulers.boundedElastic` executes the logic |

The following code sample shows how to implement the HttpServerFilter interface.

An Example HttpServerFilter

```java
import io.micronaut.context.annotation.Requires;
import io.micronaut.http.HttpRequest;
import io.micronaut.http.MutableHttpResponse;
import io.micronaut.http.annotation.Filter;
import io.micronaut.http.filter.HttpServerFilter;
import io.micronaut.http.filter.ServerFilterChain;
import org.reactivestreams.Publisher;
import reactor.core.publisher.Flux;

@Filter("/hello/**") // (1)
public class TraceFilter implements HttpServerFilter { // (2)
    private final TraceService traceService;
    public TraceFilter(TraceService traceService) { // (3)
        this.traceService = traceService;
    }
    @Override
    public Publisher<MutableHttpResponse<?>> doFilter(HttpRequest<?> request,
                                                      ServerFilterChain chain) {
        return Flux.from(traceService
                .trace(request)) // (4)
                .switchMap(aBoolean -> chain.proceed(request)) // (5)
                .doOnNext(res ->
                    res.getHeaders().add("X-Trace-Enabled", "true") // (6)
                );
    }
}
```

An Example HttpServerFilter

```kotlin
import io.micronaut.http.HttpRequest
import io.micronaut.http.MutableHttpResponse
import io.micronaut.http.annotation.Filter
import io.micronaut.http.filter.HttpServerFilter
import io.micronaut.http.filter.ServerFilterChain
import org.reactivestreams.Publisher
```

An Example HttpServerFilter

```groovy
import io.micronaut.http.HttpRequest
import io.micronaut.http.MutableHttpResponse
import io.micronaut.http.annotation.Filter
import io.micronaut.http.filter.HttpServerFilter
import io.micronaut.http.filter.ServerFilterChain
import org.reactivestreams.Publisher

@Filter("/hello/**") // (1)
class TraceFilter implements HttpServerFilter { // (2)

    private final TraceService traceService

    TraceFilter(TraceService traceService) { // (3)
        this.traceService = traceService
    }

    @Override
    Publisher<MutableHttpResponse<?>> doFilter(HttpRequest<?> request,
                                               ServerFilterChain chain) {
        traceService
                .trace(request) // (3)
                .switchMap({ aBoolean -> chain.proceed(request) }) // (4)
                .doOnNext({ res ->
                    res.headers.add("X-Trace-Enabled", "true") // (5)
                })
    }
}
```

| **1** | The Filter annotation defines the URI pattern(s) the filter matches |
|---|---|
| **2** | The class implements the HttpServerFilter interface |
| **3** | The previously defined `TraceService` is injected via constructor |
| **4** | `TraceService` is invoked to trace the request |
| **5** | If the call succeeds, the filter resumes request processing using Project Reactor's `switchMap` method, which invokes the `proceed` method of the ServerFilterChain |
| **6** | Finally, the Project Reactor's `doOnNext` method adds a `X-Trace-Enabled` header to the response. |

The previous example demonstrates some key concepts such as executing logic in a non-blocking manner before proceeding with the request and modifying the outgoing response.

|   | The examples use Project Reactor, however you can use any reactive framework that supports the Reactive streams specifications |
|---|---|


## 6.25.3.2 HttpServerFilter Error States

The publisher returned from `chain.proceed` should never emit an error. In the cases where an upstream filter emitted an error or the route itself threw an exception, the error response should be emitted instead of the exception. In some cases it may be desirable to know the cause of the error response and for this purpose an attribute exists on the response if it was created as a result of an exception being emitted or thrown. The original cause is stored as the attribute EXCEPTION.


## 6.26 Advanced body access

Micronaut HTTP server version 4.5.0 introduced a new, more advanced API to access the bytes of an incoming request. When an HttpRequest implements ServerHttpRequest, the new `byteBody()` method returns a ByteBody with buffered, reactive and blocking APIs.

When an HTTP request comes in, it starts out with an unparsed and unclaimed stream of bytes as its `byteBody()`. After all request filters have run, typically an argument binder matching the `@Body` parameter of the controller will "claim" the `byteBody()` and e.g. parse the JSON. Finally, the body is closed at the end of the request lifecycle, discarding any data if it has not been claimed by the argument binder.

|   | The FilterBodyParser API allows you to get a Map representation of a request’s body whose content type is either application/x-www-form-urlencoded or application/json. |
|---|---|


## 6.26.1 Primary operations

`ByteBody` itself does not offer direct access to the data. To begin processing, there must be a *primary operation* that converts the body into another form that can be used in the application programming model.

A normal `ByteBody` has two groups of streaming primary operations. `toInputStream()` gives access to the body as a regular `InputStream`. The `toByteArrayPublisher()` and `toByteBufferPublisher()` methods return a reactive stream of byte arrays or `ByteBuffer`s.

|   | `InputStream` is blocking API, and the netty event loop must never be blocked. If you wish to read from the body using an `InputStream`, take care to do so only on another thread, or to annotate your filter with `@ExecuteOn(TaskExecutors.BLOCKING)`. |
|---|---|

If you need full access to the body, the `buffer()` method returns a `CompletableFuture` that completes with an `AvailableByteBody` when the full body has been received. `AvailableByteBody` has a few more convenient primary operations: `toByteArray()`, `toByteBuffer()` and `toString(Charset)`.

Buffering is limited to the number of bytes configured in the `micronaut.server.max-request-buffer-size` property.


## 6.26.2 Splitting

Because the framework will not buffer the whole body in memory by default, after an ByteBody has been claimed (a primary operation has been performed), the data is "gone", and the same ByteBody cannot be claimed again. That means that if a filter were to claim the `ServerHttpRequest.byteBody()` directly (e.g. to print it to a log), controllers could not access it anymore. The argument binder for the `@Body` argument would throw an exception.

To resolve this exclusivity problem, an `ByteBody` can be *split* before it is claimed. The split operation essentially duplicates the body stream so that the two consumers (logging and argument binding) can process it independently. A body can be `split` any number of times, but only before the primary operation.

While `ServerHttpRequest.byteBody()` returns a normal `ByteBody` — cleanup is done by the HTTP server if the body is not consumed—the body returned by `split` is a `CloseableByteBody`. The caller **must** ensure that the new instance is closed, otherwise there can be resource and memory leaks, stalled connections, or other issues.

#### Backpressure

When there are two consumers of the same stream of input data, the problem of backpressure coordination necessarily comes up.

Backpressure in an HTTP server describes the behavior when the "downstream" consumers cannot consume data as fast as the "upstream" supplier (i.e. the HTTP client sending the request) is sending it. To avoid having to buffer large amounts of incoming data, the server will apply backpressure (make the client send its data more slowly) when downstream consumers cannot keep up.

A `split` operation now introduces two consumers. Depending on use case, different approaches of dealing with the backpressure of each downstream consumer may be appropriate. For example, if the two consumers write the body data to two separate files at the same time, it’s best to use the backpressure of the slowest consumer to avoid buffering data. But in another example, when one consumer is a filter that needs access to all the body data, and the other consumer is the controller, the filter needs to complete before the controller even reads any data, so we should instead be guided by the fastest of the two consumers.

These two approaches are already the two most important SplitBackpressureModes. The full list of options is as follows:

- `SplitBackpressureMode.SLOWEST` uses the backpressure of the *slowest* of the two consumers (first example)
- `SplitBackpressureMode.FASTEST` uses the backpressure of the *fastest* of the two consumers (second example)
- `SplitBackpressureMode.ORIGINAL` uses the backpressure of the original consumer (the one `split()` was called on)
- `SplitBackpressureMode.NEW` uses the backpressure of the new consumer (the one `split()` returns)

The argument-less `split()` method uses `SLOWEST`, but you should pick the mode that is most appropriate for your use case.

#### Discarding

Some consumers end up not needing the body after all. For example, if a `POST` request cannot be matched to a controller route, the body is not needed and can be discarded. How discarding is implemented in the server depends on HTTP version. For HTTP/1, the server might close the connection or simply drop the data (which can still save some decompression overhead). For HTTP/2 the server can close the input of the request stream, instructing the client to send no more data.

When there are multiple consumers, discard behavior is dependent on use case. In the above scenario of an unmatched request, when there is a filter that is also subscribed to the body data, it may be appropriate to drop the request in some cases (e.g. for logging) but may be necessary to still receive all the data in others.

To signal that the upstream may discard the body, you can call `ByteBody.allowDiscard()`. Only if all consumers call `allowDiscard()` (or `close()` without a primary operation) may the remaining data actually be discarded. Before that, *all* consumers, even those that called `allowDiscard()`, will still receive all data. For the logging use case, you can call `allowDiscard()` and be assured that you will still log the full body if the controller needs it.


## 6.26.3 Example

This example adds a filter that will log the body bytes as they come in.

A simple controller

```java
import io.micronaut.context.annotation.Requires;
import io.micronaut.core.annotation.Introspected;
import io.micronaut.http.annotation.Body;
import io.micronaut.http.annotation.Controller;
import io.micronaut.http.annotation.Post;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

@Controller("/person")
public class BodyLogController {
    private static final Logger LOG = LoggerFactory.getLogger(BodyLogController.class);

    @Post
    void create(@Body Person person) { // (1)
        LOG.info("Creating person {}", person);
    }

    @Introspected
    record Person(String firstName, String lastName) {
    }
}
```

Logging filter

```java
import io.micronaut.context.annotation.Requires;
import io.micronaut.http.ServerHttpRequest;
import io.micronaut.http.annotation.RequestFilter;
import io.micronaut.http.annotation.ServerFilter;
import io.micronaut.http.body.ByteBody;
import io.micronaut.http.body.CloseableByteBody;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import reactor.core.publisher.Flux;

import java.util.Base64;

@ServerFilter("/person")
public class BodyLogFilter {
    private static final Logger LOG = LoggerFactory.getLogger(BodyLogFilter.class);

    @RequestFilter
    public void logBody(ServerHttpRequest<?> request) { // (2)
        try (CloseableByteBody ourCopy = // (4)
                 request.byteBody()
                     .split(ByteBody.SplitBackpressureMode.SLOWEST) // (3)
                     .allowDiscard()) { // (5)
            Flux.from(ourCopy.toByteArrayPublisher()) // (6)
                .onErrorComplete(ByteBody.BodyDiscardedException.class) // (7)
                .subscribe(array -> LOG.info("Received body: {}", Base64.getEncoder().encodeToString(array))); // (8)
        }
    }
}
```

| **1** | The `@Body Person person` parameter is the final consumer of the `ServerHttpRequest.byteBody()`. The argument binder will internally perform a primary operation on the body, parse the JSON, and convert it to the `Person` object. |
|---|---|
| **2** | The `logBody` filter will be called before the controller. However, it is programmed asynchronously, so the actual logging may happen later as data is received. |
| **3** | `split` the body so that we can work with it without interfering with the argument binder in <1>. We use `SLOWEST` mode to prevent buffering: We don’t want to overwhelm the controller with data because the logging is usually very fast, but at the same time we don’t want to overwhelm the logging if it is unexpectedly slower than the controller. |
| **4** | The newly split body is in a try-with-resources statement to ensure that it is properly closed and there is no data leak. |
| **5** | We call `allowDiscard()` to signal that if the controller does not need the body after all, the logging filter is fine with dropping it entirely. Without this call, the full body would always be logged, even if the body is discarded. |
| **6** | Convert our copy of the body to a project reactor stream of `byte[]`. |
| **7** | Since we called `allowDiscard()`, there may be a `BodyDiscardedException` if the upstream decides that the body can be dropped. We ignore that exception. |
| **8** | Finally, subscribe to the reactive stream, and log any incoming data. Note that `subscribe` is asynchronous: It will return immediately and then call the lambda with the log statement as data comes in. |

If you run this example, you should see log output like this:

```none
16:29:30.562 [default-nioEventLoopGroup-1-3] INFO  i.m.docs.server.body.BodyLogFilter - Received body: eyJmaXJzdE5hbWUiOiAiSm9uYXMiLCAibGFzdE5hbWUiOiAiS29ucmFkIn0=
16:29:30.604 [default-nioEventLoopGroup-1-3] INFO  i.m.d.server.body.BodyLogController - Creating person Person[firstName=Jonas, lastName=Konrad]
```

With a short body like this, the log will only show one "packet". With more packets, the log statement will be called multiple times:

```none
16:29:30.562 [default-nioEventLoopGroup-1-3] INFO  i.m.docs.server.body.BodyLogFilter - Received body: ...
16:29:30.584 [default-nioEventLoopGroup-1-3] INFO  i.m.docs.server.body.BodyLogFilter - Received body: ...
16:29:30.642 [default-nioEventLoopGroup-1-3] INFO  i.m.docs.server.body.BodyLogFilter - Received body: ...
16:29:30.773 [default-nioEventLoopGroup-1-3] INFO  i.m.d.server.body.BodyLogController - Creating person Person[firstName=..., lastName=...]
16:29:30.708 [default-nioEventLoopGroup-1-3] INFO  i.m.docs.server.body.BodyLogFilter - Received body: ...
```

Note that the logging in the above example is asynchronous, so the log statements may be interleaved as shown.


## 6.27 HTTP Sessions

See the documentation for Micronaut Session for information about supporting HTTP sessions in your applications.


## 6.28 Server Sent Events

The Micronaut HTTP server supports emitting Server Sent Events (SSE) using the Event API.

To emit events from the server, return a Reactive Streams Publisher that emits objects of type Event.

The Publisher itself could publish events from a background task, via an event system, etc.

Imagine for an example an event stream of news headlines; you may define a data class as follows:

Headline

```java
public class Headline {

    private String title;
    private String description;

    public Headline() {}

    public Headline(String title, String description) {
        this.title = title;
        this.description = description;
    }

    public String getTitle() {
        return title;
    }

    public String getDescription() {
        return description;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public void setDescription(String description) {
        this.description = description;
    }
}
```

Headline

```kotlin
class Headline {

    var title: String? = null
    var description: String? = null

    constructor()

    constructor(title: String, description: String) {
        this.title = title
        this.description = description
    }
}
```

Headline

```groovy
class Headline {

    String title
    String description

    Headline() {}

    Headline(String title, String description) {
        this.title = title;
        this.description = description;
    }
}
```

To emit news headline events, write a controller that returns a Publisher of Event instances using whichever Reactive library you prefer. The example below uses Project Reactor's Flux via the `generate` method:

Publishing Server Sent Events from a Controller

```java
import io.micronaut.http.MediaType;
import io.micronaut.http.annotation.Controller;
import io.micronaut.http.annotation.Get;
import io.micronaut.http.sse.Event;
import io.micronaut.scheduling.TaskExecutors;
import io.micronaut.scheduling.annotation.ExecuteOn;
import org.reactivestreams.Publisher;
import reactor.core.publisher.Flux;

@Controller("/headlines")
public class HeadlineController {

    @ExecuteOn(TaskExecutors.IO)
    @Get(produces = MediaType.TEXT_EVENT_STREAM)
    public Publisher<Event<Headline>> index() { // (1)
        String[] versions = {"1.0", "2.0"}; // (2)
        return Flux.generate(() -> 0, (i, emitter) -> { // (3)
            if (i < versions.length) {
                emitter.next( // (4)
                    Event.of(new Headline("Micronaut " + versions[i] + " Released", "Come and get it"))
                );
            } else {
                emitter.complete(); // (5)
            }
            return ++i;
        });
    }
}
```

Publishing Server Sent Events from a Controller

```kotlin
import io.micronaut.http.MediaType
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Get
import io.micronaut.http.sse.Event
import io.micronaut.scheduling.TaskExecutors
import io.micronaut.scheduling.annotation.ExecuteOn
import org.reactivestreams.Publisher
import reactor.core.publisher.Flux
import reactor.core.publisher.SynchronousSink
import java.util.concurrent.Callable
import java.util.function.BiFunction

@Controller("/headlines")
class HeadlineController {

    @ExecuteOn(TaskExecutors.IO)
    @Get(produces = [MediaType.TEXT_EVENT_STREAM])
    fun index(): Publisher<Event<Headline>> { // (1)
        val versions = arrayOf("1.0", "2.0") // (2)
        return Flux.generate(
            { 0 },
            BiFunction { i: Int, emitter: SynchronousSink<Event<Headline>> ->  // (3)
                if (i < versions.size) {
                    emitter.next( // (4)
                        Event.of(
                            Headline(
                                "Micronaut " + versions[i] + " Released", "Come and get it"
                            )
                        )
                    )
                } else {
                    emitter.complete() // (5)
                }
                return@BiFunction i + 1
            })
    }
}
```

Publishing Server Sent Events from a Controller

```groovy
import io.micronaut.http.MediaType
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Get
import io.micronaut.http.sse.Event
import io.micronaut.scheduling.TaskExecutors
import io.micronaut.scheduling.annotation.ExecuteOn
import org.reactivestreams.Publisher
import reactor.core.publisher.Flux

@Controller("/headlines")
class HeadlineController {

    @ExecuteOn(TaskExecutors.IO)
    @Get(produces = MediaType.TEXT_EVENT_STREAM)
    Publisher<Event<Headline>> index() { // (1)
        String[] versions = ["1.0", "2.0"] // (2)
        Flux.generate(() -> 0, (i, emitter) -> {
            if (i < versions.length) {
                emitter.next( // (4)
                        Event.of(new Headline("Micronaut ${versions[i]} Released", "Come and get it"))
                )
            } else {
                emitter.complete() // (5)
            }
            return i + 1
        })
    }
}
```

| **1** | The controller method returns a Publisher of Event |
|---|---|
| **2** | A headline is emitted for each version of Micronaut |
| **3** | The Flux type’s `generate` method generates a Publisher. The `generate` method accepts an initial value and a lambda that accepts the value and a Emitter. Note that this example executes on the same thread as the controller action, but you could use `subscribeOn` or map an existing "hot" Flux. |
| **4** | The Emitter interface `onNext` method emits objects of type Event. The Event.of(ET) factory method constructs the event. |
| **5** | The Emitter interface `onComplete` method indicates when to finish sending server sent events. |

|   | You typically want to schedule SSE event streams on a separate executor. The previous example uses @ExecuteOn to execute the stream on the I/O executor. |
|---|---|

The above example sends back a response of type `text/event-stream` and for each Event emitted the `Headline` type previously will be converted to JSON resulting in responses such as:

Server Sent Event Response Output

```json
 data: {"title":"Micronaut 1.0 Released","description":"Come and get it"}
 data: {"title":"Micronaut 2.0 Released","description":"Come and get it"}
```

You can use the methods of the Event interface to customize the Server Sent Event data sent back, including associating event ids, comments, retry timeouts, etc.


## 6.29 WebSocket Support

The Micronaut framework features dedicated support for creating WebSocket clients and servers. The io.micronaut.websocket.annotation package includes annotations for defining both clients and servers.

|   | Since Micronaut Framework 4.0. `io.micronaut:micronaut-http-server` no longer exposes `micronaut-websocket` transitively. To use annotations such as @ServerWebSocket, add the `micronaut-websocket` dependency to your application classpath: |
|---|---|

`implementation("io.micronaut:micronaut-websocket")` `<dependency> <groupId>io.micronaut</groupId> <artifactId>micronaut-websocket</artifactId> </dependency>`


## 6.29.1 Using @ServerWebSocket

The @ServerWebSocket annotation can be applied to any class that should map to a WebSocket URI. The following example is a simple chat WebSocket implementation:

WebSocket Chat Example

```java
import io.micronaut.websocket.WebSocketBroadcaster;
import io.micronaut.websocket.WebSocketSession;
import io.micronaut.websocket.annotation.OnClose;
import io.micronaut.websocket.annotation.OnMessage;
import io.micronaut.websocket.annotation.OnOpen;
import io.micronaut.websocket.annotation.ServerWebSocket;

import java.util.function.Predicate;

@ServerWebSocket("/chat/{topic}/{username}") // (1)
public class ChatServerWebSocket {

    private final WebSocketBroadcaster broadcaster;

    public ChatServerWebSocket(WebSocketBroadcaster broadcaster) {
        this.broadcaster = broadcaster;
    }

    @OnOpen // (2)
    public void onOpen(String topic, String username, WebSocketSession session) {
        String msg = "[" + username + "] Joined!";
        broadcaster.broadcastSync(msg, isValid(topic, session));
    }

    @OnMessage // (3)
    public void onMessage(String topic, String username,
                          String message, WebSocketSession session) {
        String msg = "[" + username + "] " + message;
        broadcaster.broadcastSync(msg, isValid(topic, session)); // (4)
    }

    @OnClose // (5)
    public void onClose(String topic, String username, WebSocketSession session) {
        String msg = "[" + username + "] Disconnected!";
        broadcaster.broadcastSync(msg, isValid(topic, session));
    }

    private Predicate<WebSocketSession> isValid(String topic, WebSocketSession session) {
        return s -> s != session &&
                topic.equalsIgnoreCase(s.getUriVariables().get("topic", String.class, null));
    }
}
```

WebSocket Chat Example

```kotlin
import io.micronaut.websocket.WebSocketBroadcaster
import io.micronaut.websocket.WebSocketSession
import io.micronaut.websocket.annotation.OnClose
import io.micronaut.websocket.annotation.OnMessage
import io.micronaut.websocket.annotation.OnOpen
import io.micronaut.websocket.annotation.ServerWebSocket

import java.util.function.Predicate

@ServerWebSocket("/chat/{topic}/{username}") // (1)
class ChatServerWebSocket(private val broadcaster: WebSocketBroadcaster) {

    @OnOpen // (2)
    fun onOpen(topic: String, username: String, session: WebSocketSession) {
        val msg = "[$username] Joined!"
        broadcaster.broadcastSync(msg, isValid(topic, session))
    }

    @OnMessage // (3)
    fun onMessage(topic: String, username: String,
                  message: String, session: WebSocketSession) {
        val msg = "[$username] $message"
        broadcaster.broadcastSync(msg, isValid(topic, session)) // (4)
    }

    @OnClose // (5)
    fun onClose(topic: String, username: String, session: WebSocketSession) {
        val msg = "[$username] Disconnected!"
        broadcaster.broadcastSync(msg, isValid(topic, session))
    }

    private fun isValid(topic: String, session: WebSocketSession): Predicate<WebSocketSession> {
        return Predicate<WebSocketSession> {
            (it !== session && topic.equals(it.uriVariables.get("topic", String::class.java).orElse(null), ignoreCase = true))
        }
    }
}
```

WebSocket Chat Example

```groovy
import io.micronaut.websocket.WebSocketBroadcaster
import io.micronaut.websocket.WebSocketSession
import io.micronaut.websocket.annotation.OnClose
import io.micronaut.websocket.annotation.OnMessage
import io.micronaut.websocket.annotation.OnOpen
import io.micronaut.websocket.annotation.ServerWebSocket

import java.util.function.Predicate

@ServerWebSocket("/chat/{topic}/{username}") // (1)
class ChatServerWebSocket {

    private final WebSocketBroadcaster broadcaster

    ChatServerWebSocket(WebSocketBroadcaster broadcaster) {
        this.broadcaster = broadcaster
    }

    @OnOpen // (2)
    void onOpen(String topic, String username, WebSocketSession session) {
        String msg = "[$username] Joined!"
        broadcaster.broadcastSync(msg, isValid(topic, session))
    }

    @OnMessage // (3)
    void onMessage(String topic, String username,
                   String message, WebSocketSession session) {
        String msg = "[$username] $message"
        broadcaster.broadcastSync(msg, isValid(topic, session)) // (4)
    }

    @OnClose // (5)
    void onClose(String topic, String username, WebSocketSession session) {
        String msg = "[$username] Disconnected!"
        broadcaster.broadcastSync(msg, isValid(topic, session))
    }

    private Predicate<WebSocketSession> isValid(String topic, WebSocketSession session) {
        return { s -> s != session && topic.equalsIgnoreCase(s.uriVariables.get("topic", String, null)) }
    }
}
```

| **1** | The @ServerWebSocket annotation defines the path the WebSocket is mapped under. The URI can be a URI template. |
|---|---|
| **2** | The @OnOpen annotation declares the method to invoke when the WebSocket is opened. |
| **3** | The @OnMessage annotation declares the method to invoke when a message is received. |
| **4** | You can use a WebSocketBroadcaster to broadcast messages to every WebSocket session. You can filter which sessions to send to with a `Predicate`. Also, you could use the WebSocketSession instance to send a message to it with `WebSocketSession::send`. |
| **5** | The @OnClose annotation declares the method to invoke when the WebSocket is closed. |

|   | A working example of WebSockets in action can be found at Micronaut Guides. |
|---|---|

For binding, method arguments to each WebSocket method can be:

- A variable from the URI template (in the above example `topic` and `username` are URI template variables)
- An instance of WebSocketSession

### The @OnClose Method

The @OnClose method can optionally receive a CloseReason. The `@OnClose` method is invoked prior to the session closing.

### The @OnMessage Method

The @OnMessage method can define a parameter for the message body. The parameter can be one of the following:

- A Netty `WebSocketFrame`
- Any Java primitive or simple type (such as `String`). In fact, any type that can be converted from `ByteBuf` (you can register additional TypeConverter beans to support a custom type).
- A `byte[]`, a `ByteBuf` or a Java NIO `ByteBuffer`.
- A POJO. In this case, it will be decoded by default as JSON using JsonMediaTypeCodec. You can register a custom codec and define the content type of the handler using the @Consumes annotation.
- A WebSocketPongMessage. This is a special case: The method will not receive regular messages, but instead handle WebSocket pongs that arrive as a reply to a ping sent to the client.

### The @OnError Method

A method annotated with @OnError can be added to implement custom error handling. The `@OnError` method can define a parameter that receives the exception type to be handled. If no `@OnError` handling is present and an unrecoverable exception occurs, the WebSocket is automatically closed.

### Using @ExecuteOn For Blocking Methods

The callback methods of a @ServerWebSocket are invoked on the main Netty server event loop by default. If you do any blocking I/O operations in your WebSocket handler methods, then you must offload those tasks to a separate thread pool in the same manner as with HTTP. As with a @Controller or @Filter, the @ExecuteOn annotation can be applied to a @ServerWebSocket handler at either the type or method level.

### Non-Blocking Message Handling

The previous example uses the `broadcastSync` method of the WebSocketBroadcaster interface which blocks until the broadcast is complete. A similar `sendSync` method exists in WebSocketSession to send a message to a single receiver in a blocking manner. You can however implement non-blocking WebSocket servers by instead returning a Publisher or a Future from each WebSocket handler method. For example:

WebSocket Chat Example

```java
@OnMessage
public Publisher<Message> onMessage(String topic, String username,
                                    Message message, WebSocketSession session) {
    String text = "[" + username + "] " + message.getText();
    Message newMessage = new Message(text);
    return broadcaster.broadcast(newMessage, isValid(topic, session));
}
```

WebSocket Chat Example

```kotlin
@OnMessage
fun onMessage(topic: String, username: String,
              message: Message, session: WebSocketSession): Publisher<Message> {
    val text = "[" + username + "] " + message.text
    val newMessage = Message(text)
    return broadcaster.broadcast(newMessage, isValid(topic, session))
}
```

WebSocket Chat Example

```groovy
@OnMessage
Publisher<Message> onMessage(String topic, String username,
                             Message message, WebSocketSession session) {
    String text = "[$username] $message.text"
    Message newMessage = new Message(text)
    broadcaster.broadcast(newMessage, isValid(topic, session))
}
```

The example above uses `broadcast`, which creates an instance of Publisher and returns the value to Micronaut. The Micronaut framework sends the message asynchronously based on the Publisher interface. The similar `send` method sends a single message asynchronously via Micronaut return value.

For sending messages asynchronously outside Micronaut annotated handler methods, you can use `broadcastAsync` and `sendAsync` methods in their respective WebSocketBroadcaster and WebSocketSession interfaces. For blocking sends, the `broadcastSync` and `sendSync` methods can be used.

### @ServerWebSocket and Scopes

By default, the `@ServerWebSocket` instance is shared for all WebSocket connections. Extra care must be taken to synchronize local state to avoid thread safety issues.

If you prefer to have an instance for each connection, annotate the class with @Prototype. This lets you retrieve the WebSocketSession from the `@OnOpen` handler and assign it to a field of the `@ServerWebSocket` instance.

### Sharing Sessions with the HTTP Session

The WebSocketSession is by default backed by an in-memory map. If you add the `session` module you can however share sessions between the HTTP server and the WebSocket server.

|   | When sessions are backed by a persistent store such as Redis, after each message is processed the session is updated to the backing store. |
|---|---|

|   | Using the CLI If you created your project using Application Type `Micronaut Application`, you can use the `create-websocket-server` command with the Micronaut CLI to create a class annotated with ServerWebSocket. $ mn create-websocket-server MyChat \| Rendered template WebsocketServer.java to destination src/main/java/example/MyChatServer.java |
|---|---|

### Connection Timeouts

By default, Micronaut framework times out idle connections with no activity after five minutes. Normally this is not a problem as browsers automatically reconnect WebSocket sessions, however you can control this behaviour by setting the `micronaut.server.idle-timeout` setting (a negative value results in no timeout):

Setting the Connection Timeout for the Server

```properties
micronaut.server.idle-timeout=30m
```

```yaml
micronaut:
  server:
    idle-timeout: 30m
```

```toml
[micronaut]
  [micronaut.server]
    idle-timeout="30m"
```

```groovy
micronaut {
  server {
    idleTimeout = "30m"
  }
}
```

```hocon
{
  micronaut {
    server {
      idle-timeout = "30m"
    }
  }
}
```

```json
{
  "micronaut": {
    "server": {
      "idle-timeout": "30m"
    }
  }
}
```

If you use Micronaut’s WebSocket client you may also wish to set the timeout on the client:

Setting the Connection Timeout for the Client

```properties
micronaut.http.client.read-idle-timeout=30m
```

```yaml
micronaut:
  http:
    client:
      read-idle-timeout: 30m
```

```toml
[micronaut]
  [micronaut.http]
    [micronaut.http.client]
      read-idle-timeout="30m"
```

```groovy
micronaut {
  http {
    client {
      readIdleTimeout = "30m"
    }
  }
}
```

```hocon
{
  micronaut {
    http {
      client {
        read-idle-timeout = "30m"
      }
    }
  }
}
```

```json
{
  "micronaut": {
    "http": {
      "client": {
        "read-idle-timeout": "30m"
      }
    }
  }
}
```


## 6.29.2 Using @ClientWebSocket

The @ClientWebSocket annotation can be used with the WebSocketClient interface to define WebSocket clients.

You can inject a reference to a WebSocketClient using the @Client annotation:

```java
@Inject
@Client("http://localhost:8080")
WebSocketClient webSocketClient;
```

This lets you use the same service discovery and load balancing features for WebSocket clients.

Once you have a reference to the WebSocketClient interface you can use the `connect` method to obtain a connected instance of a bean annotated with @ClientWebSocket.

For example consider the following implementation:

WebSocket Chat Example

```java
import io.micronaut.http.HttpRequest;
import io.micronaut.websocket.WebSocketSession;
import io.micronaut.websocket.annotation.ClientWebSocket;
import io.micronaut.websocket.annotation.OnMessage;
import io.micronaut.websocket.annotation.OnOpen;
import org.reactivestreams.Publisher;
import io.micronaut.core.async.annotation.SingleResult;
import java.util.Collection;
import java.util.concurrent.ConcurrentLinkedQueue;
import java.util.concurrent.Future;

@ClientWebSocket("/chat/{topic}/{username}") // (1)
public abstract class ChatClientWebSocket implements AutoCloseable { // (2)

    private WebSocketSession session;
    private HttpRequest request;
    private String topic;
    private String username;
    private Collection<String> replies = new ConcurrentLinkedQueue<>();

    @OnOpen
    public void onOpen(String topic, String username,
                       WebSocketSession session, HttpRequest request) { // (3)
        this.topic = topic;
        this.username = username;
        this.session = session;
        this.request = request;
    }

    public String getTopic() {
        return topic;
    }

    public String getUsername() {
        return username;
    }

    public Collection<String> getReplies() {
        return replies;
    }

    public WebSocketSession getSession() {
        return session;
    }

    public HttpRequest getRequest() {
        return request;
    }

    @OnMessage
    public void onMessage(String message) {
        replies.add(message); // (4)
    }
```

WebSocket Chat Example

```kotlin
import io.micronaut.http.HttpRequest
import io.micronaut.websocket.WebSocketSession
import io.micronaut.websocket.annotation.ClientWebSocket
import io.micronaut.websocket.annotation.OnMessage
import io.micronaut.websocket.annotation.OnOpen
import reactor.core.publisher.Mono
import java.util.concurrent.ConcurrentLinkedQueue
import java.util.concurrent.Future

@ClientWebSocket("/chat/{topic}/{username}") // (1)
abstract class ChatClientWebSocket : AutoCloseable { // (2)

    var session: WebSocketSession? = null
        private set
    var request: HttpRequest<*>? = null
        private set
    var topic: String? = null
        private set
    var username: String? = null
        private set
    private val replies = ConcurrentLinkedQueue<String>()

    @OnOpen
    fun onOpen(topic: String, username: String,
               session: WebSocketSession, request: HttpRequest<*>) { // (3)
        this.topic = topic
        this.username = username
        this.session = session
        this.request = request
    }

    fun getReplies(): Collection<String> {
        return replies
    }

    @OnMessage
    fun onMessage(message: String) {
        replies.add(message) // (4)
    }
```

WebSocket Chat Example

```groovy
import io.micronaut.http.HttpRequest
import io.micronaut.websocket.WebSocketSession
import io.micronaut.websocket.annotation.ClientWebSocket
import io.micronaut.websocket.annotation.OnMessage
import io.micronaut.websocket.annotation.OnOpen
import org.reactivestreams.Publisher
import reactor.core.publisher.Mono
import java.util.concurrent.ConcurrentLinkedQueue
import java.util.concurrent.Future
import io.micronaut.core.async.annotation.SingleResult

@ClientWebSocket("/chat/{topic}/{username}") // (1)
abstract class ChatClientWebSocket implements AutoCloseable { // (2)

    private WebSocketSession session
    private HttpRequest request
    private String topic
    private String username
    private Collection<String> replies = new ConcurrentLinkedQueue<>()

    @OnOpen
    void onOpen(String topic, String username,
                WebSocketSession session, HttpRequest request) { // (3)
        this.topic = topic
        this.username = username
        this.session = session
        this.request = request
    }

    String getTopic() {
        topic
    }

    String getUsername() {
        username
    }

    Collection<String> getReplies() {
        replies
    }

    WebSocketSession getSession() {
        session
    }

    HttpRequest getRequest() {
        request
    }

    @OnMessage
    void onMessage(String message) {
        replies << message // (4)
    }
```

| **1** | The class is abstract (more on that later) and is annotated with @ClientWebSocket |
|---|---|
| **2** | The client must implement `AutoCloseable` and you should ensure that the connection is closed at some point. |
| **3** | You can use the same annotations as on the server, in this case `@OnOpen` to obtain a reference to the underlying session. |
| **4** | The `@OnMessage` annotation defines the method that receives responses from the server. |

You can also define abstract methods that start with either `send` or `broadcast` and these methods will be implemented for you at compile time. For example:

WebSocket Send Methods

```java
public abstract void send(String message);
```

Note by returning `void` this tells the Micronaut framework that the method is a blocking send. You can instead define methods that return either futures or a Publisher:

WebSocket Send Methods

```java
public abstract reactor.core.publisher.Mono<String> send(String message);
```

The above example defines a send method that returns a Mono.

WebSocket Send Methods

```java
public abstract java.util.concurrent.Future<String> sendAsync(String message);
```

The above example defines a send method that executes asynchronously and returns a Future to access the results.

Once you have defined a client class you can connect to the client socket and start sending messages:

Connecting a Client WebSocket

```java
ChatClientWebSocket chatClient = webSocketClient
    .connect(ChatClientWebSocket.class, "/chat/football/fred")
    .blockFirst();
chatClient.send("Hello World!");
```

|   | For illustration purposes we use `blockFirst()` to obtain the client. It is however possible to combine `connect` (which returns a Flux) to perform non-blocking interaction via WebSocket. |
|---|---|

|   | Using the CLI If you created your project using the Micronaut CLI and the default (`service`) profile, you can use the `create-websocket-client` command to create an abstract class with WebSocketClient. $ mn create-websocket-client MyChat \| Rendered template WebsocketClient.java to destination src/main/java/example/MyChatClient.java |
|---|---|
