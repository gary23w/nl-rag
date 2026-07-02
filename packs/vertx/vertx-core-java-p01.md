---
title: "Vert.x Core (part 1/8)"
source: https://vertx.io/docs/vertx-core/java/
domain: vertx
license: CC-BY-SA-4.0
tags: vert.x toolkit, eclipse vertx, reactive toolkit, event loop server
fetched: 2026-07-02
part: 1/8
---

# Vert.x Core

Core modules

Examples

API docs

# Vert.x Core Manual

At the heart of Vert.x is a set of Java APIs that we call **Vert.x Core**

Repository.

Vert.x core provides functionality for things like:

- Writing TCP clients and servers
- Writing HTTP clients and servers including support for WebSockets
- The Event bus
- Shared data - local maps and clustered distributed maps
- Periodic and delayed actions
- Deploying and undeploying Verticles
- Datagram Sockets
- DNS client
- File system access
- Virtual threads
- High availability
- Native transports
- Clustering

The functionality in core is fairly low level - you won’t find stuff like database access, authorisation or high level web functionality here - that kind of stuff you’ll find in **Vert.x ext** (extensions).

Vert.x core is small and lightweight. You just use the parts you want. It’s also entirely embeddable in your existing applications - we don’t force you to structure your applications in a special way just so you can use Vert.x.

You can use core from any of the other languages that Vert.x supports. But here’s a cool bit - we don’t force you to use the Java API directly from, say, JavaScript or Ruby - after all, different languages have different conventions and idioms, and it would be odd to force Java idioms on Ruby developers (for example). Instead, we automatically generate an **idiomatic** equivalent of the core Java APIs for each language.

From now on we’ll just use the word **core** to refer to Vert.x core.

If you are using Maven or Gradle, add the following dependency to the *dependencies* section of your project descriptor to access the Vert.x Core API:

- Maven (in your `pom.xml`):

```
<dependency>
  <groupId>io.vertx</groupId>
  <artifactId>vertx-core</artifactId>
  <version>5.1.3</version>
</dependency>
```

- Gradle (in your `build.gradle` file):

```
dependencies {
  compile 'io.vertx:vertx-core:5.1.3'
}
```

Let’s discuss the different concepts and features in core.


## In the beginning there was Vert.x

You can’t do much in Vert.x-land unless you can communicate with a `Vertx` object!

It’s the control centre of Vert.x and is how you do pretty much everything, including creating clients and servers, getting a reference to the event bus, setting timers, as well as many other things.

So how do you get an instance?

If you’re embedding Vert.x then you simply create an instance as follows:

```
Vertx vertx = Vertx.vertx();
```

|   | Most applications will only need a single Vert.x instance, but it’s possible to create multiple Vert.x instances if you require, for example, isolation between the event bus or different groups of servers and clients. |
|---|---|

### Specifying options when creating a Vertx object

When creating a Vert.x object you can also specify options if the defaults aren’t right for you:

```
Vertx vertx = Vertx.vertx(new VertxOptions().setWorkerPoolSize(40));
```

The `VertxOptions` object has many settings and allows you to configure things like clustering, high availability, pool sizes and various other settings.

### Creating a clustered Vert.x object

If you’re creating a **clustered Vert.x** (See the section on the event bus for more information on clustering the event bus), then you will normally use the asynchronous variant to create the Vertx object.

This is because it usually takes some time (maybe a few seconds) for the different Vert.x instances in a cluster to group together. During that time, we don’t want to block the calling thread, so we give the result to you asynchronously.


## Are you fluent?

You may have noticed that in the previous examples a **fluent** API was used.

A fluent API is where multiple methods calls can be chained together. For example:

```
request.response().putHeader("Content-Type", "text/plain").end("some text");
```

This is a common pattern throughout Vert.x APIs, so get used to it.

Chaining calls like this allows you to write code that’s a little bit less verbose. Of course, if you don’t like the fluent approach **we don’t force you** to do it that way, you can happily ignore it if you prefer and write your code like this:

```
HttpServerResponse response = request.response();
response.putHeader("Content-Type", "text/plain");
response.end("some text");
```


## Don’t call us, we’ll call you.

The Vert.x APIs are largely *event driven*. This means that when things happen in Vert.x that you are interested in, Vert.x will call you by sending you events.

Some example events are:

- a timer has fired
- some data has arrived on a socket,
- some data has been read from disk
- an exception has occurred
- an HTTP server has received a request

You handle events by providing *handlers* to the Vert.x APIs. For example to receive a timer event every second you would do:

```
vertx.setPeriodic(1000, id -> {
  // This handler will get called every second
  System.out.println("timer fired!");
});
```

Or to receive an HTTP request:

```
server.requestHandler(request -> {
  // This handler will be called every time an HTTP request is received at the server
  request.response().end("hello world!");
});
```

Some time later when Vert.x has an event to pass to your handler Vert.x will call it **asynchronously**.

This leads us to some important concepts in Vert.x:


## Don’t block me!

With very few exceptions (i.e. some file system operations ending in 'Sync'), none of the APIs in Vert.x block the calling thread.

If a result can be provided immediately, it will be returned immediately, otherwise you will usually provide a handler to receive events some time later.

Because none of the Vert.x APIs block threads that means you can use Vert.x to handle a lot of concurrency using just a small number of threads.

With a conventional blocking API the calling thread might block when:

- Reading data from a socket
- Writing data to disk
- Sending a message to a recipient and waiting for a reply.
- … Many other situations

In all the above cases, when your thread is waiting for a result it can’t do anything else - it’s effectively useless.

This means that if you want a lot of concurrency using blocking APIs then you need a lot of threads to prevent your application grinding to a halt.

Threads have overhead in terms of the memory they require (e.g. for their stack) and in context switching.

For the levels of concurrency required in many modern applications, a blocking approach just doesn’t scale.


## Reactor and Multi-Reactor

We mentioned before that Vert.x APIs are event driven - Vert.x passes events to handlers when they are available.

In most cases Vert.x calls your handlers using a thread called an **event loop**.

As nothing in Vert.x or your application blocks, the event loop can merrily run around delivering events to different handlers in succession as they arrive.

Because nothing blocks, an event loop can potentially deliver huge amounts of events in a short amount of time. For example a single event loop can handle many thousands of HTTP requests very quickly.

We call this the Reactor Pattern.

You may have heard of this before - for example Node.js implements this pattern.

In a standard reactor implementation there is a **single event loop** thread which runs around in a loop delivering all events to all handlers as they arrive.

The trouble with a single thread is it can only run on a single core at any one time, so if you want your single threaded reactor application (e.g. your Node.js application) to scale over your multi-core server you have to start up and manage many different processes.

Vert.x works differently here. Instead of a single event loop, each Vertx instance maintains **several event loops**. By default we choose the number based on the number of available cores on the machine, but this can be overridden.

This means a single Vertx process can scale across your server, unlike Node.js.

We call this pattern the **Multi-Reactor Pattern** to distinguish it from the single threaded reactor pattern.

|   | Even though a Vertx instance maintains multiple event loops, any particular handler will never be executed concurrently, and in most cases (with the exception of worker verticles) will always be called using the **exact same event loop**. |
|---|---|


## The Golden Rule - Don’t Block the Event Loop

We already know that the Vert.x APIs are non blocking and won’t block the event loop, but that’s not much help if you block the event loop **yourself** in a handler.

If you do that, then that event loop will not be able to do anything else while it’s blocked. If you block all of the event loops in Vertx instance then your application will grind to a complete halt!

So don’t do it! **You have been warned**.

Examples of blocking include:

- Thread.sleep()
- Waiting on a lock
- Waiting on a mutex or monitor (e.g. synchronized section)
- Doing a long lived database operation and waiting for a result
- Doing a complex calculation that takes some significant time.
- Spinning in a loop

If any of the above stop the event loop from doing anything else for a **significant amount of time** then you should go immediately to the naughty step, and await further instructions.

So… what is a **significant amount of time**?

How long is a piece of string? It really depends on your application and the amount of concurrency you require.

If you have a single event loop, and you want to handle 10000 http requests per second, then it’s clear that each request can’t take more than 0.1 ms to process, so you can’t block for any more time than that.

**The maths is not hard and shall be left as an exercise for the reader.**

If your application is not responsive it might be a sign that you are blocking an event loop somewhere. To help you diagnose such issues, Vert.x will automatically log warnings if it detects an event loop hasn’t returned for some time. If you see warnings like these in your logs, then you should investigate.

```
Thread vertx-eventloop-thread-3 has been blocked for 20458 ms
```

Vert.x will also provide stack traces to pinpoint exactly where the blocking is occurring.

If you want to turn off these warnings or change the settings, you can do that in the `VertxOptions` object before creating the Vertx object.


## Future results

Vert.x 4 use futures to represent asynchronous results.

Any asynchronous method returns a `Future` object for the result of the call: a *success* or a *failure*.

You cannot interact directly with the result of a future, instead you need to set a handler that will be called when the future completes and the result is available, like any other kind of event.

```
FileSystem fs = vertx.fileSystem();

Future<FileProps> future = fs.props("/my_file.txt");

future.onComplete((AsyncResult<FileProps> ar) -> {
  if (ar.succeeded()) {
    FileProps props = ar.result();
    System.out.println("File size = " + props.size());
  } else {
    System.out.println("Failure: " + ar.cause().getMessage());
  }
});
```

|   | Do not confuse *futures* with *promises*. If futures represent the "read-side" of an asynchronous result, promises are the "write-side". They allow you to defer the action of providing a result. In most cases, you don’t need to create promises yourself in a Vert.x application. Future composition and Future coordination provide you with the tools to transform and merge asynchronous results. |
|---|---|

|   | Terminal operations like `onSuccess`, `onFailure` and `onComplete` provide no guarantee whatsoever regarding the invocation order of callbacks. Consider a future on which 2 callbacks are registered: `future.onComplete(ar -> { // Do something }); future.onComplete(ar -> { // May be invoked first });` It is possible that the second callback is invoked before the first one. If you need such guarantee, consider using Future composition with `andThen`. |
|---|---|


## Future composition

`compose` can be used for chaining futures:

- when the current future succeeds, apply the given function, that returns a future. When this returned future completes, the composition succeeds.
- when the current future fails, the composition fails

```
FileSystem fs = vertx.fileSystem();

Future<Void> future = fs
  .createFile("/foo")
  .compose(v -> {
    // When the file is created (fut1), execute this:
    return fs.writeFile("/foo", Buffer.buffer());
  })
  .compose(v -> {
    // When the file is written (fut2), execute this:
    return fs.move("/foo", "/bar");
  });
```

In this example, 3 operations are chained together:

1. a file is created
2. data is written in this file
3. the file is moved

When these 3 steps are successful, the final future (`future`) will succeed. However, if one of the steps fails, the final future will fail.

Beyond this, `Future` offers more: `map`, `recover`, `otherwise`, `andThen` and even a `flatMap` which is an alias of `compose`


## Future coordination

Coordination of multiple futures can be achieved with Vert.x `futures`. It supports concurrent composition (run several async operations in parallel) and sequential composition (chain async operations).

`Future.all` takes several futures arguments (up to 6) and returns a future that is *succeeded* when all the futures are *succeeded* and *failed* when at least one of the futures is failed:

```
Future<HttpServer> httpServerFuture = httpServer.listen();

Future<NetServer> netServerFuture = netServer.listen();

Future.all(httpServerFuture, netServerFuture).onComplete(ar -> {
  if (ar.succeeded()) {
    // All servers started
  } else {
    // At least one server failed
  }
});
```

The operations run concurrently, the `Handler` attached to the returned future is invoked upon completion of the composition. When one of the operation fails (one of the passed future is marked as a failure), the resulting future is marked as failed too. When all the operations succeed, the resulting future is completed with a success.

On success, the `resultAt` method guarantees the results in the same order specified in the call to `Future.all`. In the example above, regardless of which item completed first, the `httpServer` result can be accessed using `resultAt(0)` and the `netServer` result can be accessed using `resultAt(1)`.

Alternatively, you can pass a list (potentially empty) of futures:

```
Future.all(Arrays.asList(future1, future2, future3));
```

While the `all` composition *waits* until all futures are successful (or one fails), the `any` composition *waits* for the first succeeded future. `Future.any` takes several futures arguments (up to 6) and returns a future that is succeeded when one of the futures is, and failed when all the futures are failed:

```
Future.any(future1, future2).onComplete(ar -> {
  if (ar.succeeded()) {
    // At least one is succeeded
  } else {
    // All failed
  }
});
```

A list of futures can be used also:

```
Future.any(Arrays.asList(f1, f2, f3));
```

The `join` composition *waits* until all futures are completed, either with a success or a failure. `Future.join` takes several futures arguments (up to 6) and returns a future that is succeeded when all the futures are succeeded, and failed when all the futures are completed and at least one of them is failed:

```
Future.join(future1, future2, future3).onComplete(ar -> {
  if (ar.succeeded()) {
    // All succeeded
  } else {
    // All completed and at least one failed
  }
});
```

A list of futures can be used also:

```
Future.join(Arrays.asList(future1, future2, future3));
```

### CompletionStage interoperability

The Vert.x `Future` API offers compatibility *from* and *to* `CompletionStage` which is the JDK interface for composable asynchronous operations.

We can go from a Vert.x `Future` to a `CompletionStage` using the `toCompletionStage` method, as in:

```
Future<String> future = vertx.createDnsClient().lookup("vertx.io");
future.toCompletionStage().whenComplete((ip, err) -> {
  if (err != null) {
    System.err.println("Could not resolve vertx.io");
    err.printStackTrace();
  } else {
    System.out.println("vertx.io => " + ip);
  }
});
```

We can conversely go from a `CompletionStage` to Vert.x `Future` using `Future.fromCompletionStage`. There are 2 variants:

1. the first variant takes just a `CompletionStage` and calls the `Future` methods from the thread that resolves the `CompletionStage` instance, and
2. the second variant takes an extra `Context` parameter to call the `Future` methods on a Vert.x context.

|   | In most cases the variant with a `CompletionStage` and a `Context` is the one you will want to use to respect the Vert.x threading model, since Vert.x `Future` are more likely to be used with Vert.x code, libraries and clients. |
|---|---|

Here is an example of going from a `CompletionStage` to a Vert.x `Future` and dispatching on a context:

```
Future.fromCompletionStage(completionStage, vertx.getOrCreateContext())
  .flatMap(str -> {
    String key = UUID.randomUUID().toString();
    return storeInDb(key, str);
  })
  .onSuccess(str -> {
    System.out.println("We have a result: " + str);
  })
  .onFailure(err -> {
    System.err.println("We have a problem");
    err.printStackTrace();
  });
```


## Verticles

Vert.x comes with a simple, scalable, *actor-like* deployment and concurrency model out of the box that you can use to save you writing your own.

**This model is entirely optional and Vert.x does not force you to create your applications in this way if you don’t want to.**.

The model does not claim to be a strict actor-model implementation, but it does share similarities especially with respect to concurrency, scaling and deployment.

To use this model, you write your code as set of **verticles**.

Verticles are chunks of code that get deployed and run by Vert.x. A Vert.x instance maintains N event loop threads (where N by default is core*2) by default. Verticles can be written in any of the languages that Vert.x supports and a single application can include verticles written in multiple languages.

You can think of a verticle as a bit like an actor in the Actor Model.

An application would typically be composed of many verticle instances running in the same Vert.x instance at the same time. The different verticle instances communicate with each other by sending messages on the event bus.

### Writing Verticles

Verticle classes must implement the `Deployable` interface.

They can implement it directly if you like, but usually it’s simpler to extend the abstract class `VerticleBase`.

Here’s an example verticle:

```
class MyVerticle extends VerticleBase {

  // Called when verticle is deployed
  public Future<?> start() throws Exception {
    return super.start();
  }

  // Optional - called when verticle is un-deployed
  public Future<?> stop() throws Exception {
    return super.stop();
  }
}
```

Normally you would override the start method like in the example above.

When Vert.x deploys the verticle it will call the start method, and when future returned by the method has completed the verticle will be considered started.

You can also optionally override the stop method. This will be called by Vert.x when the verticle is un-deployed and when the future returned by the method has completed the verticle will be considered stopped.

Here’s a more elaborated example:

```
class MyVerticle extends VerticleBase {

  private HttpServer server;

  @Override
  public Future<?> start() {
    server = vertx.createHttpServer().requestHandler(req -> {
      req.response()
        .putHeader("content-type", "text/plain")
        .end("Hello from Vert.x!");
    });

    // Now bind the server:
    return server.listen(8080);
  }
}
```

You can even write a one-liner Verticle:

```
Deployable verticle = context -> vertx
  .createHttpServer()
  .requestHandler(req -> req.response()
    .putHeader("content-type", "text/plain")
    .end("Hello from Vert.x!"))
  .listen(8080);
```

|   | You don’t need to manually stop the HTTP server started by a verticle, in the verticle’s stop method. Vert.x will automatically stop any running server when the verticle is un-deployed. |
|---|---|

### What happened to Vert.x 4 Verticle and AbstractVerticle contracts?

The contract defined by `Verticle` and `AbstractVerticle` wasn’t convenient anymore with Vert.x 5 future based model:

```
class MyVerticle extends AbstractVerticle {
  @Override
  public void start(Promise<Void> startPromise) throws Exception {
    Future<String> future = bindService();

    // Requires to write
    future.onComplete(ar -> {
      if (ar.succeeded()) {
        startPromise.complete();
      } else {
        startPromise.fail(ar.cause());
      }
    });

    // Or
    future
      .<Void>mapEmpty()
      .onComplete(startPromise);
  }
}
```

Nevertheless, `Verticle` and `AbstractVerticle` are not deprecated in Vert.x 5. It is fine to use them, however it is not the default recommended choice anymore.

### Verticle Types

There are two different types of verticles:

**Standard Verticles**

These are the most common and useful type - they are always executed using an event loop thread. We’ll discuss this more in the next section.

**Worker Verticles**

These run using a thread from the worker pool. An instance is never executed concurrently by more than one thread.

### Standard verticles

Standard verticles are assigned an event loop thread when they are created and the start method is called with that event loop. When you call any other methods that takes a handler on a core API from an event loop then Vert.x will guarantee that those handlers, when called, will be executed on the same event loop.

This means we can guarantee that all the code in your verticle instance is always executed on the same event loop (as long as you don’t create your own threads and call it!).

This means you can write all the code in your application as single threaded and let Vert.x worry about the threading and scaling. No more worrying about synchronized and volatile any more, and you also avoid many other cases of race conditions and deadlock so prevalent when doing hand-rolled 'traditional' multi-threaded application development.

### Worker verticles

A worker verticle is just like a standard verticle but it’s executed using a thread from the Vert.x worker thread pool, rather than using an event loop.

Worker verticles are designed for calling blocking code, as they won’t block any event loops.

If you don’t want to use a worker verticle to run blocking code, you can also run inline blocking code directly while on an event loop.

If you want to deploy a verticle as a worker verticle you do that with `setThreadingModel`.

```
DeploymentOptions options = new DeploymentOptions().setThreadingModel(ThreadingModel.WORKER);
vertx.deployVerticle(new MyOrderProcessorVerticle(), options);
```

Worker verticle instances are never executed concurrently by Vert.x by more than one thread, but can executed by different threads at different times.

### Virtual thread verticles

A virtual thread verticle is just like a standard verticle but it’s executed using virtual threads, rather than using an event loop.

Virtual thread verticles are designed to use an async/await model with Vert.x futures.

If you want to deploy a verticle as a virtual thread verticle you do that with `setThreadingModel`.

```
DeploymentOptions options = new DeploymentOptions().setThreadingModel(ThreadingModel.VIRTUAL_THREAD);
vertx.deployVerticle(new MyOrderProcessorVerticle(), options);
```

|   | this feature requires Java 21 |
|---|---|

### Deploying verticles programmatically

You can deploy a verticle using one of the `deployVerticle` method, specifying a verticle name, or you can pass in a verticle instance you have already created yourself.

```
VerticleBase myVerticle = new MyVerticle();
vertx.deployVerticle(myVerticle);
```

You can also deploy verticles by specifying the verticle **name**.

The verticle name is used to look up the specific `VerticleFactory` that will be used to instantiate the actual verticle instance(s).

Here’s an example of deploying some a Java Verticle using its class name:

```
vertx.deployVerticle("com.mycompany.MyOrderProcessorVerticle");
```

### Rules for mapping a verticle name to a verticle factory

When deploying verticle(s) using a name, the name is used to select the actual verticle factory that will instantiate the verticle(s).

Verticle names can have a prefix - which is a string followed by a colon, which when present will be used to lookup the factory, e.g.

```
 groovy:com.mycompany.SomeGroovyCompiledVerticle // Use the Groovy verticle factory
```

When prefix is absent, Vert.x will look for a suffix and use that to lookup the factory, e.g.

```
 SomeScript.groovy // Will use the Groovy verticle factory
```

If no prefix or suffix is present, Vert.x will assume it’s a Java fully qualified class name (FQCN) and try and instantiate that.

### How are Verticle Factories located?

Most Verticle factories are loaded from the classpath and registered at Vert.x startup.

You can also programmatically register and unregister verticle factories using `registerVerticleFactory` and `unregisterVerticleFactory` if you wish.

### Waiting for deployment to complete

Verticle deployment is asynchronous and may complete some time after the call to deploy has returned.

If you want to be notified when deployment is complete you can deploy specifying a completion handler:

```
vertx
  .deployVerticle(new MyOrderProcessorVerticle())
  .onComplete(res -> {
    if (res.succeeded()) {
      System.out.println("Deployment id is: " + res.result());
    } else {
      System.out.println("Deployment failed!");
    }
  });
```

The completion handler will be passed a result containing the deployment ID string, if deployment succeeded.

This deployment ID can be used later if you want to undeploy the deployment.

### Un-deploying verticle deployments

Deployments can be un-deployed with `undeploy`.

Un-deployment is itself asynchronous so if you want to be notified when un-deployment is complete you can deploy specifying a completion handler:

```
vertx
  .undeploy(deploymentID)
  .onComplete(res -> {
    if (res.succeeded()) {
      System.out.println("Undeployed ok");
    } else {
      System.out.println("Undeploy failed!");
    }
  });
```

### Specifying number of verticle instances

When deploying a verticle using a verticle, you can specify the number of verticle instances that you want to deploy, you also need to pass a `Callable<Deployable>` so Vert.x can instantiate your verticle instances.

```
DeploymentOptions options = new DeploymentOptions().setInstances(16);
vertx.deployVerticle(() -> new MyOrderProcessorVerticle(), options);
```

This is useful for scaling easily across multiple cores. For example, you might have a web-server verticle to deploy and multiple cores on your machine, so you want to deploy multiple instances to utilise all the cores.

### Passing configuration to a verticle

Configuration in the form of JSON can be passed to a verticle at deployment time:

```
JsonObject config = new JsonObject().put("name", "tim").put("directory", "/blah");
DeploymentOptions options = new DeploymentOptions().setConfig(config);
vertx.deployVerticle(new MyOrderProcessorVerticle(), options);
```

This configuration is then available via the `Context` object or directly using the `config` method. The configuration is returned as a JSON object so you can retrieve data as follows:

```
System.out.println("Configuration: " + config().getString("name"));
```

### Accessing environment variables in a Verticle

Environment variables and system properties are accessible using the Java API:

```
System.getProperty("prop");
System.getenv("HOME");
```

### Causing Vert.x to exit

Threads maintained by Vert.x instances are not daemon threads so they will prevent the JVM from exiting.

If you are embedding Vert.x and you have finished with it, you can call `close` to close it down.

This will shut-down all internal thread pools and close other resources, and will allow the JVM to exit.

### The Context object

When Vert.x provides an event to a handler or calls the start or stop methods of a `Verticle`, the execution is associated with a `Context`. Usually a context is an **event-loop context** and is tied to a specific event loop thread. So executions for that context always occur on that exact same event loop thread. In the case of worker verticles and running inline blocking code a worker context will be associated with the execution which will use a thread from the worker thread pool.

To retrieve the context, use the `getOrCreateContext` method:

```
Context context = vertx.getOrCreateContext();
```

If the current thread has a context associated with it, it reuses the context object. If not a new instance of context is created. You can test the *type* of context you have retrieved:

```
Context context = vertx.getOrCreateContext();
if (context.isEventLoopContext()) {
  System.out.println("Context attached to Event Loop");
} else if (context.isWorkerContext()) {
  System.out.println("Context attached to Worker Thread");
} else if (! Context.isOnVertxThread()) {
  System.out.println("Context not attached to a thread managed by vert.x");
}
```

When you have retrieved the context object, you can run code in this context asynchronously. In other words, you submit a task that will be eventually run in the same context, but later:

```
vertx.getOrCreateContext().runOnContext( (v) -> {
  System.out.println("This will be executed asynchronously in the same context");
});
```

When several handlers run in the same context, they may want to share data. The context object offers methods to store and retrieve data shared in the context. For instance, it lets you pass data to some action run with `runOnContext`:

```
final Context context = vertx.getOrCreateContext();
context.put("data", "hello");
context.runOnContext((v) -> {
  String hello = context.get("data");
});
```

The context object also let you access verticle configuration using the `config` method. Check the Passing configuration to a verticle section for more details about this configuration.

### Executing periodic and delayed actions

It’s very common in Vert.x to want to perform an action after a delay, or periodically.

In standard verticles you can’t just make the thread sleep to introduce a delay, as that will block the event loop thread.

Instead, you use Vert.x timers. Timers can be **one-shot** or **periodic**. We’ll discuss both

#### One-shot Timers

A one shot timer calls an event handler after a certain delay, expressed in milliseconds.

To set a timer to fire once you use `setTimer` method passing in the delay and a handler

```
long timerID = vertx.setTimer(1000, id -> {
  System.out.println("And one second later this is printed");
});

System.out.println("First this is printed");
```

The return value is a unique timer id which can later be used to cancel the timer. The handler is also passed the timer id.

#### Periodic Timers

You can also set a timer to fire periodically by using `setPeriodic`.

There will be an initial delay equal to the period.

The return value of `setPeriodic` is a unique timer id (long). This can be later used if the timer needs to be cancelled.

The argument passed into the timer event handler is also the unique timer id:

Keep in mind that the timer will fire on a periodic basis. If your periodic treatment takes a long amount of time to proceed, your timer events could run continuously or even worse : stack up.

In this case, you should consider using `setTimer` instead. Once your treatment has finished, you can set the next timer.

```
long timerID = vertx.setPeriodic(1000, id -> {
  System.out.println("And every second this is printed");
});

System.out.println("First this is printed");
```

#### Cancelling timers

To cancel a periodic timer, call `cancelTimer` specifying the timer id. For example:

```
vertx.cancelTimer(timerID);
```

#### Timer as a Future

`Timer` combines one-shot timer and in a single API.

```
Future<String> timer = vertx
  .timer(10, TimeUnit.SECONDS)
  .map(v -> "Success");

timer.onSuccess(value -> {
  System.out.println("Timer fired: " + value);
});
timer.onFailure(cause -> {
  System.out.println("Timer cancelled: " + cause.getMessage());
});
```

The future succeeds when the timer fires, conversely `cancelling` the timer fails the future.

#### Automatic clean-up in verticles

If you’re creating timers from inside verticles, those timers will be automatically closed when the verticle is undeployed.

### Verticle worker pool

Verticles use the Vert.x worker pool for executing blocking actions, i.e `executeBlocking` or worker verticle.

A different worker pool can be specified in deployment options:

```
vertx.deployVerticle(new MyOrderProcessorVerticle(), new DeploymentOptions().setWorkerPoolName("the-specific-pool"));
```


## The Event Bus

The `event bus` is the **nervous system** of Vert.x.

There is a single event bus instance for every Vert.x instance and it is obtained using the method `eventBus`.

The event bus allows different parts of your application to communicate with each other, irrespective of what language they are written in, and whether they’re in the same Vert.x instance, or in a different Vert.x instance.

It can even be bridged to allow client-side JavaScript running in a browser to communicate on the same event bus.

The event bus forms a distributed peer-to-peer messaging system spanning multiple server nodes and multiple browsers.

The event bus supports publish/subscribe, point-to-point, and request-response messaging.

The event bus API is very simple. It basically involves registering handlers, unregistering handlers and sending and publishing messages.

First some theory:

### The Theory

#### Addressing

Messages are sent on the event bus to an **address**.

Vert.x doesn’t bother with any fancy addressing schemes. In Vert.x an address is simply a string. Any string is valid. However, it is wise to use some kind of scheme, *e.g.* using periods to demarcate a namespace.

Some examples of valid addresses are europe.news.feed1, acme.games.pacman, sausages, and X.

#### Handlers

Messages are received by handlers. You register a handler at an address.

Many different handlers can be registered at the same address.

A single handler can be registered at many different addresses.

#### Publish / subscribe messaging

The event bus supports **publishing** messages.

Messages are published to an address. Publishing means delivering the message to all handlers that are registered at that address.

This is the familiar **publish/subscribe** messaging pattern.

#### Point-to-point and Request-Response messaging

The event bus also supports **point-to-point** messaging.

Messages are sent to an address. Vert.x will then route them to just one of the handlers registered at that address.

If there is more than one handler registered at the address, one will be chosen using a non-strict round-robin algorithm.

With point-to-point messaging, an optional reply handler can be specified when sending the message.

When a message is received by a recipient, and has been handled, the recipient can optionally decide to reply to the message. If they do so, the reply handler will be called.

When the reply is received back by the sender, it too can be replied to. This can be repeated *ad infinitum*, and allows a dialog to be set up between two different verticles.

This is a common messaging pattern called the **request-response** pattern.

#### Best-effort delivery

Vert.x does its best to deliver messages and won’t consciously throw them away. This is called **best-effort** delivery.

However, in case of failure of all or parts of the event bus, there is a possibility messages might be lost.

If your application cares about lost messages, you should code your handlers to be idempotent, and your senders to retry after recovery.

#### Types of messages

Out of the box Vert.x allows any primitive/simple type, String, or `buffers` to be sent as messages.

However, it’s a convention and common practice in Vert.x to send messages as JSON

JSON is very easy to create, read and parse in all the languages that Vert.x supports, so it has become a kind of *lingua franca* for Vert.x.

However, you are not forced to use JSON if you don’t want to.

The event bus is very flexible and also supports sending arbitrary objects over the event bus. You can do this by defining a `codec` for the objects you want to send.

### The Event Bus API

Let’s jump into the API.

#### Getting the event bus

You get a reference to the event bus as follows:

```
EventBus eb = vertx.eventBus();
```

There is a single instance of the event bus per Vert.x instance.

#### Registering Handlers

This simplest way to register a handler is using `consumer`. Here’s an example:

```
EventBus eb = vertx.eventBus();

eb.consumer("news.uk.sport", message -> {
  System.out.println("I have received a message: " + message.body());
});
```

When a message arrives for your handler, your handler will be called, passing in the `message`.

The object returned from call to consumer() is an instance of `MessageConsumer`.

This object can subsequently be used to unregister the handler, or use the handler as a stream.

Alternatively you can use `consumer` to return a MessageConsumer with no handler set, and then set the handler on that. For example:

```
EventBus eb = vertx.eventBus();

MessageConsumer<String> consumer = eb.consumer("news.uk.sport");
consumer.handler(message -> {
  System.out.println("I have received a message: " + message.body());
});
```

When registering a handler on a clustered event bus, it can take some time for the registration to reach all nodes of the cluster.

If you want to be notified when this has completed, you can use the `completion future` on the MessageConsumer object.

```
consumer.completion().onComplete(res -> {
  if (res.succeeded()) {
    System.out.println("The handler registration has reached all nodes");
  } else {
    System.out.println("Registration failed!");
  }
});
```

#### Un-registering Handlers

To unregister a handler, call `unregister`.

If you are on a clustered event bus, un-registering can take some time to propagate across the nodes. If you want to be notified when this is complete, use the future returned by `unregister`.

```
consumer
  .unregister()
  .onComplete(res -> {
    if (res.succeeded()) {
      System.out.println("The handler un-registration has reached all nodes");
    } else {
      System.out.println("Un-registration failed!");
    }
  });
```

#### Publishing messages

Publishing a message is simple. Just use `publish` specifying the address to publish it to.

```
eventBus.publish("news.uk.sport", "Yay! Someone kicked a ball");
```

That message will then be delivered to all handlers registered against the address news.uk.sport.

#### Sending messages

Sending a message will result in only one handler registered at the address receiving the message. This is the point-to-point messaging pattern. The handler is chosen in a non-strict round-robin fashion.

You can send a message with `send`.

```
eventBus.send("news.uk.sport", "Yay! Someone kicked a ball");
```

#### Setting headers on messages

Messages sent over the event bus can also contain headers. This can be specified by providing a `DeliveryOptions` when sending or publishing:

```
DeliveryOptions options = new DeliveryOptions();
options.addHeader("some-header", "some-value");
eventBus.send("news.uk.sport", "Yay! Someone kicked a ball", options);
```

#### Message ordering

Vert.x will deliver messages to any particular handler in the same order they were sent from any particular sender.

#### The Message object

The object you receive in a message handler is a `Message`.

The `body` of the message corresponds to the object that was sent or published.

The headers of the message are available with `headers`.

#### Acknowledging messages / sending replies

When using `send` the event bus attempts to deliver the message to a `MessageConsumer` registered with the event bus.

In some cases it’s useful for the sender to know when the consumer has received the message and "processed" it using **request-response** pattern.

To acknowledge that the message has been processed, the consumer can reply to the message by calling `reply`.

When this happens it causes a reply to be sent back to the sender and the reply handler is invoked with the reply.

An example will make this clear:

The receiver:

```
MessageConsumer<String> consumer = eventBus.consumer("news.uk.sport");
consumer.handler(message -> {
  System.out.println("I have received a message: " + message.body());
  message.reply("how interesting!");
});
```

The sender:

```
eventBus
  .request("news.uk.sport", "Yay! Someone kicked a ball across a patch of grass")
  .onComplete(ar -> {
    if (ar.succeeded()) {
      System.out.println("Received reply: " + ar.result().body());
    }
  });
```

The reply can contain a message body which can contain useful information.

What the "processing" actually means is application-defined and depends entirely on what the message consumer does and is not something that the Vert.x event bus itself knows or cares about.

Some examples:

- A simple message consumer which implements a service which returns the time of the day would acknowledge with a message containing the time of day in the reply body
- A message consumer which implements a persistent queue, might acknowledge with `true` if the message was successfully persisted in storage, or `false` if not.
- A message consumer which processes an order might acknowledge with `true` when the order has been successfully processed so it can be deleted from the database

#### Sending with timeouts

When sending a message with a reply handler, you can specify a timeout in the `DeliveryOptions`.

If a reply is not received within that time, the reply handler will be called with a failure.

The default timeout is 30 seconds.

#### Send Failures

Message sends can fail for other reasons, including:

- There are no handlers available to send the message to
- The recipient has explicitly failed the message using `fail`

In all cases, the reply handler will be called with the specific failure.

#### Message Codecs

You can send any object you like across the event bus if you define and register a `message codec` for it.

Message codecs have a name and you specify that name in the `DeliveryOptions` when sending or publishing the message:

```
eventBus.registerCodec(myCodec);

DeliveryOptions options = new DeliveryOptions().setCodecName(myCodec.name());

eventBus.send("orders", new MyPOJO(), options);
```

If you always want the same codec to be used for a particular type then you can register a default codec for it, then you don’t have to specify the codec on each send in the delivery options:

```
eventBus.registerDefaultCodec(MyPOJO.class, myCodec);

eventBus.send("orders", new MyPOJO());
```

You unregister a message codec with `unregisterCodec`.

Message codecs don’t always have to encode and decode as the same type. For example you can write a codec that allows a MyPOJO class to be sent, but when that message is sent to a handler it arrives as a MyOtherPOJO class.

Vert.x has built-in codecs for certain data types:

- basic types (string, byte array, byte, int, long, double, boolean, short, char), or
- some Vert.x data types (buffers, JSON array, JSON objects), or
- types implementing the `ClusterSerializable` interface, or
- types implementing the `java.io.Serializable` interface.

|   | In clustered mode, `ClusterSerializable` and `java.io.Serializable` objects are rejected by default, for security reasons. You can define which classes are allowed for encoding and decoding by providing functions which inspect the name of the class: `EventBus.clusterSerializableChecker()`, and `EventBus.serializableChecker()`. |
|---|---|

#### Clustered Event Bus

The event bus doesn’t just exist in a single Vert.x instance. By clustering different Vert.x instances together on your network they can form a single, distributed event bus.

If you’re creating your Vert.x instance programmatically, you get a clustered event bus by configuring the Vert.x instance as clustered:

```
VertxOptions options = new VertxOptions();
Vertx
  .clusteredVertx(options)
  .onComplete(res -> {
    if (res.succeeded()) {
      Vertx vertx = res.result();
      EventBus eventBus = vertx.eventBus();
      System.out.println("We now have a clustered event bus: " + eventBus);
    } else {
      System.out.println("Failed: " + res.cause());
    }
  });
```

You should also make sure you have one of the `ClusterManager` implementations on your classpath.

### Automatic clean-up in verticles

If you’re registering event bus handlers from inside verticles, those handlers will be automatically unregistered when the verticle is undeployed.


## Configuring the event bus

The event bus can be configured.It is particularly useful when the event bus is clustered. Under the hood the event bus uses TCP connections to send and receive messages, so the `EventBusOptions` let you configure all aspects of these TCP connections. As the event bus acts as a server and client, the configuration is close to `NetClientOptions` and `NetServerOptions`.

```
VertxOptions options = new VertxOptions()
    .setEventBusOptions(new EventBusOptions()
        .setSsl(true)
        .setKeyCertOptions(new JksOptions().setPath("keystore.jks").setPassword("wibble"))
        .setTrustOptions(new JksOptions().setPath("keystore.jks").setPassword("wibble"))
        .setClientAuth(ClientAuth.REQUIRED)
    );

Vertx
  .clusteredVertx(options)
  .onComplete(res -> {
    if (res.succeeded()) {
      Vertx vertx = res.result();
      EventBus eventBus = vertx.eventBus();
      System.out.println("We now have a clustered event bus: " + eventBus);
    } else {
      System.out.println("Failed: " + res.cause());
    }
  });
```

The previous snippet depicts how you can use SSL connections for the event bus, instead of plain TCP connections.

|   | To enforce the security in clustered mode, you **must** configure the cluster manager to use encryption or enforce security. Refer to the documentation of the cluster manager for further details. |
|---|---|

The event bus configuration needs to be consistent in all the cluster nodes.

The `EventBusOptions` also lets you specify whether the event bus is clustered, the port and host.

When used in containers, you can also configure the public host and port:

```
VertxOptions options = new VertxOptions()
    .setEventBusOptions(new EventBusOptions()
        .setClusterPublicHost("whatever")
        .setClusterPublicPort(1234)
    );

Vertx
  .clusteredVertx(options)
  .onComplete(res -> {
    if (res.succeeded()) {
      Vertx vertx = res.result();
      EventBus eventBus = vertx.eventBus();
      System.out.println("We now have a clustered event bus: " + eventBus);
    } else {
      System.out.println("Failed: " + res.cause());
    }
  });
```
