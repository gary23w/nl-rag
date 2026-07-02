---
title: "1. Introduction • Akka HTTP"
source: https://doc.akka.io/libraries/akka-http/current/introduction.html
domain: akka-http-scala
license: CC-BY-SA-4.0
tags: akka http scala, akka actor streams, scala reactive http, akka routing directives
fetched: 2026-07-02
---

# 1. Introduction • Akka HTTP

New to Akka? Start with the Akka SDK.

# 1. Introduction

| Project Info: Akka Http |   |
|---|---|
| Artifact | com.typesafe.akka akka-http 10.7.4 Snapshots are available |
| JDK versions | Eclipse Temurin JDK 11Eclipse Temurin JDK 17Eclipse Temurin JDK 21 |
| Scala versions | 2.13.17, 3.3.7 |
| JPMS module name | akka.http |
| License | BUSL-1.1 |
| Readiness level | Supported, support is available from Lightbend Since 10.0.0, 2016-11-26 |
| Home page | https://akka.io |
| API documentation | API (Scaladoc) API (Javadoc) |
| Forums | Akka Discuss |
| Release notes | Akka release notes |
| Issues | Github issues |
| Sources | https://github.com/akka/akka-http |

The Akka HTTP modules implement a full server- and client-side HTTP stack on top of *akka-actor* and *akka-stream*. It’s not a web-framework but rather a more general toolkit for providing and consuming HTTP-based services. While interaction with a browser is of course also in scope it is not the primary focus of Akka HTTP.

Akka HTTP follows a rather open design and many times offers several different API levels for “doing the same thing”. You get to pick the API level of abstraction that is most suitable for your application. This means that, if you have trouble achieving something using a high-level API, there’s a good chance that you can get it done with a low-level API, which offers more flexibility but might require you to write more application code.

## Philosophy

Akka HTTP has been driven with a clear focus on providing tools for building integration layers rather than application cores. As such it regards itself as a suite of libraries rather than a framework.

A framework, as we’d like to think of the term, gives you a “frame”, in which you build your application. It comes with a lot of decisions already pre-made and provides a foundation including support structures that lets you get started and deliver results quickly. In a way a framework is like a skeleton onto which you put the “flesh” of your application in order to have it come alive. As such frameworks work best if you choose them before you start application development and try to stick to the framework’s “way of doing things” as you go along.

For example, if you are building a browser-facing web application it makes sense to choose a web framework and build your application on top of it because the “core” of the application is the interaction of a browser with your code on the web-server. The framework makers have chosen one “proven” way of designing such applications and let you “fill in the blanks” of a more or less flexible “application-template”. Being able to rely on best-practice architecture like this can be a great asset for getting things done quickly.

However, if your application is not primarily a web application because its core is not browser-interaction but some specialized maybe complex business service and you are merely trying to connect it to the world via a REST/HTTP interface a web-framework might not be what you need. In this case the application architecture should be dictated by what makes sense for the core not the interface layer. Also, you probably won’t benefit from the possibly existing browser-specific framework components like view templating, asset management, JavaScript- and CSS generation/manipulation/minification, localization support, AJAX support, etc.

Akka HTTP was designed specifically as “not-a-framework”, not because we don’t like frameworks, but for use cases where a framework is not the right choice. Akka HTTP is made for building integration layers based on HTTP and as such tries to “stay on the sidelines”. Therefore you normally don’t build your application “on top of” Akka HTTP, but you build your application on top of whatever makes sense and use Akka HTTP merely for the HTTP integration needs.

On the other hand, if you prefer to build your applications with the guidance of a framework, you should give Play Framework a try, which both use Akka internally. If you come from Play and want to try Akka HTTP, we collected a side-by-side comparison to show how some Play routing features map to the Akka HTTP routing DSL.

## Using Akka HTTP

Akka HTTP is provided as independent modules from Akka itself under its own release cycle. Akka HTTP is compatible with Akka >= 2.10.11 and future Akka 2.x versions that are released during the lifetime of Akka HTTP 10.4.x. The modules, however, do *not* depend on `akka-actor` or `akka-stream`, so the user is required to choose an Akka version to run against and add a manual dependency to `akka-stream` of the chosen version.

Note

The Akka dependencies are available from Akka’s secure library repository. To access them you need to use a secure, tokenized URL as specified at https://account.akka.io/token.

Additionally, add the dependencies as below.

**sbt**

```scala
val AkkaVersion = "2.10.11"
val AkkaHttpVersion = "10.7.4"
libraryDependencies ++= Seq(
  "com.typesafe.akka" %% "akka-actor-typed" % AkkaVersion,
  "com.typesafe.akka" %% "akka-stream" % AkkaVersion,
  "com.typesafe.akka" %% "akka-http" % AkkaHttpVersion
)
```

**Gradle**

```gradle
def versions = [
  AkkaVersion: "2.10.11",
  ScalaBinary: "2.13"
]
dependencies {
  implementation platform("com.typesafe.akka:akka-http-bom_${versions.ScalaBinary}:10.7.4")

  implementation "com.typesafe.akka:akka-actor-typed_${versions.ScalaBinary}:${versions.AkkaVersion}"
  implementation "com.typesafe.akka:akka-stream_${versions.ScalaBinary}:${versions.AkkaVersion}"
  implementation "com.typesafe.akka:akka-http_${versions.ScalaBinary}"
}
```

**Maven**

```xml
<properties>
  <akka.version>2.10.11</akka.version>
  <scala.binary.version>2.13</scala.binary.version>
</properties>
<dependencyManagement>
  <dependencies>
    <dependency>
      <groupId>com.typesafe.akka</groupId>
      <artifactId>akka-http-bom_${scala.binary.version}</artifactId>
      <version>10.7.4</version>
      <type>pom</type>
      <scope>import</scope>
    </dependency>
  </dependencies>
</dependencyManagement>
<dependencies>
  <dependency>
    <groupId>com.typesafe.akka</groupId>
    <artifactId>akka-actor-typed_${scala.binary.version}</artifactId>
    <version>${akka.version}</version>
  </dependency>
  <dependency>
    <groupId>com.typesafe.akka</groupId>
    <artifactId>akka-stream_${scala.binary.version}</artifactId>
    <version>${akka.version}</version>
  </dependency>
  <dependency>
    <groupId>com.typesafe.akka</groupId>
    <artifactId>akka-http_${scala.binary.version}</artifactId>
  </dependency>
</dependencies>
```

You may download a packaged version of this project from:

- Akka HTTP Quickstart for Scala
- Akka HTTP Quickstart for Java

## Routing DSL for HTTP servers

The high-level, routing API of Akka HTTP provides a DSL to describe HTTP “routes” and how they should be handled. Each route is composed of one or more level of `Directives``Directives` that narrows down to handling one specific type of request.

For example one route might start with matching the `path` of the request, only matching if it is “/hello”, then narrowing it down to only handle HTTP `get` requests and then `complete` those with a string literal, which will be sent back as an HTTP OK with the string as response body.

The `Route` `Route` created using the Route DSL is then “bound” to a port to start serving HTTP requests:

**Scala**

```scala
source/*
 * Copyright (C) 2020-2025 Lightbend Inc. <https://akka.io>
 */

package docs.http.scaladsl

import akka.actor.typed.ActorSystem
import akka.actor.typed.scaladsl.Behaviors
import akka.http.scaladsl.Http
import akka.http.scaladsl.model._
import akka.http.scaladsl.server.Directives._
import akka.http.scaladsl.server.Route.seal

import scala.io.StdIn

object HttpServerRoutingMinimal {

  def main(args: Array[String]): Unit = {

    implicit val system = ActorSystem(Behaviors.empty, "my-system")
    // needed for the future flatMap/onComplete in the end
    implicit val executionContext = system.executionContext

    val route =
      path("hello") {
        get {
          complete(HttpEntity(ContentTypes.`text/html(UTF-8)`, "<h1>Say hello to akka-http</h1>"))
        }
      }

    val bindingFuture = Http().newServerAt("localhost", 8080).bind(route)

    println(s"Server now online. Please navigate to http://localhost:8080/hello\nPress RETURN to stop...")
    StdIn.readLine() // let it run until user presses return
    bindingFuture
      .flatMap(_.unbind()) // trigger unbinding from the port
      .onComplete(_ => system.terminate()) // and shutdown when done
  }
}
```

**Java**

```java
sourceimport akka.actor.typed.ActorSystem;
import akka.actor.typed.javadsl.Behaviors;
import akka.http.javadsl.Http;
import akka.http.javadsl.ServerBinding;
import akka.http.javadsl.server.AllDirectives;
import akka.http.javadsl.server.Route;

import java.util.concurrent.CompletionStage;

public class HttpServerMinimalExampleTest extends AllDirectives {

  public static void main(String[] args) throws Exception {
    // boot up server using the route as defined below
    ActorSystem<Void> system = ActorSystem.create(Behaviors.empty(), "routes");

    final Http http = Http.get(system);

    //In order to access all directives we need an instance where the routes are define.
    HttpServerMinimalExampleTest app = new HttpServerMinimalExampleTest();

    final CompletionStage<ServerBinding> binding =
      http.newServerAt("localhost", 8080)
          .bind(app.createRoute());

    System.out.println("Server online at http://localhost:8080/\nPress RETURN to stop...");
    System.in.read(); // let it run until user presses return

    binding
        .thenCompose(ServerBinding::unbind) // trigger unbinding from the port
        .thenAccept(unbound -> system.terminate()); // and shutdown when done
  }

  private Route createRoute() {
    return concat(
        path("hello", () ->
            get(() ->
                complete("<h1>Say hello to akka-http</h1>"))));
  }
}
```

When you run this server, you can either open the page in a browser, at the following url: http://localhost:8080/hello, or call it in your terminal, via `curl http://localhost:8080/hello`.

## Marshalling

Transforming request and response bodies between over-the-wire formats and objects to be used in your application is done separately from the route declarations, in marshallers, which are pulled in implicitly using the “magnet” pattern. This means that you can `complete` a request with any kind of object as long as there is an implicit marshaller available in scope.

Default marshallers are provided for simple objects like String or ByteString, and you can define your own for example for JSON. An additional module provides JSON serialization using the spray-json library (see JSON Support for details):

**sbt**

```scala
val AkkaHttpVersion = "10.7.4"
libraryDependencies += "com.typesafe.akka" %% "akka-http-spray-json" % AkkaHttpVersion
```

**Gradle**

```gradle
def versions = [
  ScalaBinary: "2.13"
]
dependencies {
  implementation platform("com.typesafe.akka:akka-http-bom_${versions.ScalaBinary}:10.7.4")

  implementation "com.typesafe.akka:akka-http-spray-json_${versions.ScalaBinary}"
}
```

**Maven**

```xml
<properties>
  <scala.binary.version>2.13</scala.binary.version>
</properties>
<dependencyManagement>
  <dependencies>
    <dependency>
      <groupId>com.typesafe.akka</groupId>
      <artifactId>akka-http-bom_${scala.binary.version}</artifactId>
      <version>10.7.4</version>
      <type>pom</type>
      <scope>import</scope>
    </dependency>
  </dependencies>
</dependencyManagement>
<dependencies>
  <dependency>
    <groupId>com.typesafe.akka</groupId>
    <artifactId>akka-http-spray-json_${scala.binary.version}</artifactId>
  </dependency>
</dependencies>
```

JSON support is possible in `akka-http` by the use of Jackson, an external artifact (see JSON Support for details):

**sbt**

```scala
val AkkaHttpVersion = "10.7.4"
libraryDependencies += "com.typesafe.akka" %% "akka-http-jackson" % AkkaHttpVersion
```

**Gradle**

```gradle
def versions = [
  ScalaBinary: "2.13"
]
dependencies {
  implementation platform("com.typesafe.akka:akka-http-bom_${versions.ScalaBinary}:10.7.4")

  implementation "com.typesafe.akka:akka-http-jackson_${versions.ScalaBinary}"
}
```

**Maven**

```xml
<properties>
  <scala.binary.version>2.13</scala.binary.version>
</properties>
<dependencyManagement>
  <dependencies>
    <dependency>
      <groupId>com.typesafe.akka</groupId>
      <artifactId>akka-http-bom_${scala.binary.version}</artifactId>
      <version>10.7.4</version>
      <type>pom</type>
      <scope>import</scope>
    </dependency>
  </dependencies>
</dependencyManagement>
<dependencies>
  <dependency>
    <groupId>com.typesafe.akka</groupId>
    <artifactId>akka-http-jackson_${scala.binary.version}</artifactId>
  </dependency>
</dependencies>
```

A common use case is to reply to a request using a model object having the marshaller transform it into JSON. In this case shown by two separate routes. The first route queries an asynchronous database and marshals the `Future[Option[Item]]``CompletionStage<Optional<Item>>` result into a JSON response. The second unmarshals an `Order` from the incoming request, saves it to the database and replies with an OK when done.

**Scala**

```scala
source/*
 * Copyright (C) 2020-2025 Lightbend Inc. <https://akka.io>
 */

package docs.http.scaladsl

import akka.actor.typed.ActorSystem
import akka.actor.typed.scaladsl.Behaviors
import akka.http.scaladsl.Http
import akka.Done
import akka.http.scaladsl.server.Route
import akka.http.scaladsl.server.Directives._
import akka.http.scaladsl.model.StatusCodes
// for JSON serialization/deserialization following dependency is required:
// "com.typesafe.akka" %% "akka-http-spray-json" % "10.1.7"
import akka.http.scaladsl.marshallers.sprayjson.SprayJsonSupport._
import spray.json.DefaultJsonProtocol._
import spray.json.RootJsonFormat

import scala.io.StdIn

import scala.concurrent.ExecutionContext
import scala.concurrent.Future

object SprayJsonExample {

  // needed to run the route
  implicit val system: ActorSystem[_] = ActorSystem(Behaviors.empty, "SprayExample")
  // needed for the future map/flatmap in the end and future in fetchItem and saveOrder
  implicit val executionContext: ExecutionContext = system.executionContext

  var orders: List[Item] = Nil

  // domain model
  final case class Item(name: String, id: Long)
  final case class Order(items: List[Item])

  // formats for unmarshalling and marshalling
  implicit val itemFormat: RootJsonFormat[Item] = jsonFormat2(Item.apply)
  implicit val orderFormat: RootJsonFormat[Order] = jsonFormat1(Order.apply)

  // (fake) async database query api
  def fetchItem(itemId: Long): Future[Option[Item]] = Future {
    orders.find(o => o.id == itemId)
  }
  def saveOrder(order: Order): Future[Done] = {
    orders = order.items ::: orders
    Future { Done }
  }

  def main(args: Array[String]): Unit = {
    val route: Route =
      concat(
        get {
          pathPrefix("item" / LongNumber) { id =>
            // there might be no item for a given id
            val maybeItem: Future[Option[Item]] = fetchItem(id)

            onSuccess(maybeItem) {
              case Some(item) => complete(item)
              case None       => complete(StatusCodes.NotFound)
            }
          }
        },
        post {
          path("create-order") {
            entity(as[Order]) { order =>
              val saved: Future[Done] = saveOrder(order)
              onSuccess(saved) { _ => // we are not interested in the result value `Done` but only in the fact that it was successful
                complete("order created")
              }
            }
          }
        }
      )

    val bindingFuture = Http().newServerAt("localhost", 8080).bind(route)
    println(s"Server online at http://localhost:8080/\nPress RETURN to stop...")
    StdIn.readLine() // let it run until user presses return
    bindingFuture
      .flatMap(_.unbind()) // trigger unbinding from the port
      .onComplete(_ => system.terminate()) // and shutdown when done
  }
}
```

**Java**

```java
sourceimport akka.Done;
import akka.NotUsed;
import akka.actor.typed.ActorSystem;
import akka.actor.typed.javadsl.Behaviors;
import akka.http.javadsl.ConnectHttp;
import akka.http.javadsl.Http;
import akka.http.javadsl.ServerBinding;
import akka.http.javadsl.marshallers.jackson.Jackson;
import akka.http.javadsl.model.HttpRequest;
import akka.http.javadsl.model.HttpResponse;
import akka.http.javadsl.model.StatusCodes;
import akka.http.javadsl.server.AllDirectives;
import akka.http.javadsl.server.Route;
import akka.stream.javadsl.Flow;
import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;

import java.util.List;
import java.util.Optional;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.CompletionStage;

import static akka.http.javadsl.server.PathMatchers.longSegment;

public class JacksonExampleTest extends AllDirectives {

  public static void main(String[] args) throws Exception {
    // boot up server using the route as defined below
    ActorSystem<Void> system = ActorSystem.create(Behaviors.empty(), "routes");

    final Http http = Http.get(system);

    //In order to access all directives we need an instance where the routes are define.
    JacksonExampleTest app = new JacksonExampleTest();

    final CompletionStage<ServerBinding> binding =
        http.newServerAt("localhost", 8080)
            .bind(app.createRoute());

    System.out.println("Server online at http://localhost:8080/\nPress RETURN to stop...");
    System.in.read(); // let it run until user presses return

    binding
      .thenCompose(ServerBinding::unbind) // trigger unbinding from the port
      .thenAccept(unbound -> system.terminate()); // and shutdown when done
  }

  // (fake) async database query api
  private CompletionStage<Optional<Item>> fetchItem(long itemId) {
    return CompletableFuture.completedFuture(Optional.of(new Item("foo", itemId)));
  }

  // (fake) async database query api
  private CompletionStage<Done> saveOrder(final Order order) {
    return CompletableFuture.completedFuture(Done.getInstance());
  }

  private Route createRoute() {

    return concat(
      get(() ->
        pathPrefix("item", () ->
          path(longSegment(), (Long id) -> {
            final CompletionStage<Optional<Item>> futureMaybeItem = fetchItem(id);
            return onSuccess(futureMaybeItem, maybeItem ->
              maybeItem.map(item -> completeOK(item, Jackson.marshaller()))
                .orElseGet(() -> complete(StatusCodes.NOT_FOUND, "Not Found"))
            );
          }))),
      post(() ->
        path("create-order", () ->
          entity(Jackson.unmarshaller(Order.class), order -> {
            CompletionStage<Done> futureSaved = saveOrder(order);
            return onSuccess(futureSaved, done ->
              complete("order created")
            );
          })))
    );
  }

  private static class Item {

    final String name;
    final long id;

    @JsonCreator
    Item(@JsonProperty("name") String name,
         @JsonProperty("id") long id) {
      this.name = name;
      this.id = id;
    }

    public String getName() {
      return name;
    }

    public long getId() {
      return id;
    }
  }

  private static class Order {

    final List<Item> items;

    @JsonCreator
    Order(@JsonProperty("items") List<Item> items) {
      this.items = items;
    }

    public List<Item> getItems() {
      return items;
    }
  }
}
```

When you run this server, you can update the inventory via `curl -H "Content-Type: application/json" -X POST -d '{"items":[{"name":"hhgtg","id":42}]}' http://localhost:8080/create-order` on your terminal - adding an item named `"hhgtg"` and having an `id=42`; and then view the inventory either in a browser, at a url like: http://localhost:8080/item/42 - or on the terminal, via `curl http://localhost:8080/item/42`.

The logic for the marshalling and unmarshalling JSON in this example is provided by the “spray-json”“Jackson” library. See JSON Support)JSON Support) for more information about integration with this library.

## Streaming

One of the strengths of Akka HTTP is that streaming data is at its heart meaning that both request and response bodies can be streamed through the server achieving constant memory usage even for very large requests or responses. Streaming responses will be backpressured by the remote client so that the server will not push data faster than the client can handle, streaming requests means that the server decides how fast the remote client can push the data of the request body.

Example that streams random numbers as long as the client accepts them:

**Scala**

```scala
source/*
 * Copyright (C) 2020-2025 Lightbend Inc. <https://akka.io>
 */

package docs.http.scaladsl

import akka.actor.typed.ActorSystem
import akka.actor.typed.scaladsl.Behaviors
import akka.stream.scaladsl._
import akka.util.ByteString
import akka.http.scaladsl.Http
import akka.http.scaladsl.model.{ HttpEntity, ContentTypes }
import akka.http.scaladsl.server.Directives._
import scala.util.Random
import scala.io.StdIn

object HttpServerStreamingRandomNumbers {

  def main(args: Array[String]): Unit = {

    implicit val system = ActorSystem(Behaviors.empty, "RandomNumbers")
    // needed for the future flatMap/onComplete in the end
    implicit val executionContext = system.executionContext

    // streams are re-usable so we can define it here
    // and use it for every request
    val numbers = Source.fromIterator(() =>
      Iterator.continually(Random.nextInt()))

    val route =
      path("random") {
        get {
          complete(
            HttpEntity(
              ContentTypes.`text/plain(UTF-8)`,
              // transform each number to a chunk of bytes
              numbers.map(n => ByteString(s"$n\n"))
            )
          )
        }
      }

    val bindingFuture = Http().newServerAt("localhost", 8080).bind(route)
    println(s"Server online at http://localhost:8080/\nPress RETURN to stop...")
    StdIn.readLine() // let it run until user presses return
    bindingFuture
      .flatMap(_.unbind()) // trigger unbinding from the port
      .onComplete(_ => system.terminate()) // and shutdown when done
  }
}
```

**Java**

```java
sourceimport akka.NotUsed;
import akka.actor.typed.ActorSystem;
import akka.actor.typed.javadsl.Behaviors;
import akka.http.javadsl.ConnectHttp;
import akka.http.javadsl.Http;
import akka.http.javadsl.ServerBinding;
import akka.http.javadsl.model.*;
import akka.http.javadsl.server.AllDirectives;
import akka.http.javadsl.server.Route;
import akka.stream.javadsl.Flow;
import akka.stream.javadsl.Source;
import akka.util.ByteString;

import java.util.Random;
import java.util.concurrent.CompletionStage;
import java.util.stream.Stream;

public class HttpServerStreamRandomNumbersTest extends AllDirectives {

  public static void main(String[] args) throws Exception {
    // boot up server using the route as defined below
    ActorSystem<Void> system = ActorSystem.create(Behaviors.empty(), "routes");

    final Http http = Http.get(system);

    //In order to access all directives we need an instance where the routes are define.
    HttpServerStreamRandomNumbersTest app = new HttpServerStreamRandomNumbersTest();

    final CompletionStage<ServerBinding> binding =
        http.newServerAt("localhost", 8080)
                .bind(app.createRoute());

    System.out.println("Server online at http://localhost:8080/\nPress RETURN to stop...");
    System.in.read(); // let it run until user presses return

    binding
        .thenCompose(ServerBinding::unbind) // trigger unbinding from the port
        .thenAccept(unbound -> system.terminate()); // and shutdown when done
  }

  private Route createRoute() {
    final Random rnd = new Random();
    // streams are re-usable so we can define it here
    // and use it for every request
    Source<Integer, NotUsed> numbers = Source.fromIterator(() -> Stream.generate(rnd::nextInt).iterator());

    return concat(
        path("random", () ->
            get(() ->
                complete(HttpEntities.create(ContentTypes.TEXT_PLAIN_UTF8,
                    // transform each number to a chunk of bytes
                    numbers.map(x -> ByteString.fromString(x + "\n")))))));
  }
}
```

Connecting to this service with a slow HTTP client would backpressure so that the next random number is produced on demand with constant memory usage on the server. This can be seen using curl and limiting the rate `curl --limit-rate 50b 127.0.0.1:8080/random`

Akka HTTP routes easily interact with actors. In this example one route allows for placing bids in a fire-and-forget style while the second route contains a request-response interaction with an actor. The resulting response is rendered as JSON and returned when the response arrives from the actor.

**Scala**

```scala
source/*
 * Copyright (C) 2020-2025 Lightbend Inc. <https://akka.io>
 */

package docs.http.scaladsl

import akka.actor.typed.scaladsl.AskPattern._
import akka.actor.typed.scaladsl.Behaviors
import akka.actor.typed.{ ActorRef, ActorSystem }
import akka.http.scaladsl.Http
import akka.http.scaladsl.marshallers.sprayjson.SprayJsonSupport._
import akka.http.scaladsl.model.StatusCodes
import akka.http.scaladsl.server.Directives._
import akka.util.Timeout
import spray.json.DefaultJsonProtocol._
import spray.json.RootJsonFormat

import scala.concurrent.duration._
import scala.concurrent.{ ExecutionContext, Future }
import scala.io.StdIn

object HttpServerWithActorInteraction {

  object Auction {

    sealed trait Message

    case class Bid(userId: String, offer: Int) extends Message

    case class GetBids(replyTo: ActorRef[Bids]) extends Message

    case class Bids(bids: List[Bid])

    def apply: Behaviors.Receive[Message] = apply(List.empty)

    def apply(bids: List[Bid]): Behaviors.Receive[Message] = Behaviors.receive {
      case (ctx, bid @ Bid(userId, offer)) =>
        ctx.log.info(s"Bid complete: $userId, $offer")
        apply(bids :+ bid)
      case (_, GetBids(replyTo)) =>
        replyTo ! Bids(bids)
        Behaviors.same
    }

  }

  // these are from spray-json
  implicit val bidFormat: RootJsonFormat[Auction.Bid] = jsonFormat2(Auction.Bid.apply)
  implicit val bidsFormat: RootJsonFormat[Auction.Bids] = jsonFormat1(Auction.Bids.apply)

  def main(args: Array[String]): Unit = {
    implicit val system: ActorSystem[Auction.Message] = ActorSystem(Auction.apply, "auction")
    // needed for the future flatMap/onComplete in the end
    implicit val executionContext: ExecutionContext = system.executionContext

    val auction: ActorRef[Auction.Message] = system
    import Auction._

    val route =
      path("auction") {
        concat(
          put {
            parameters("bid".as[Int], "user") { (bid, user) =>
              // place a bid, fire-and-forget
              auction ! Bid(user, bid)
              complete(StatusCodes.Accepted, "bid placed")
            }
          },
          get {
            implicit val timeout: Timeout = 5.seconds

            // query the actor for the current auction state
            val bids: Future[Bids] = auction.ask(GetBids(_))
            complete(bids)
          }
        )
      }

    val bindingFuture = Http().newServerAt("localhost", 8080).bind(route)
    println(s"Server online at http://localhost:8080/\nPress RETURN to stop...")
    StdIn.readLine() // let it run until user presses return
    bindingFuture
      .flatMap(_.unbind()) // trigger unbinding from the port
      .onComplete(_ => system.terminate()) // and shutdown when done

  }
}
```

**Java**

```java
source
import akka.NotUsed;
import akka.actor.typed.ActorRef;
import akka.actor.typed.ActorSystem;
import akka.actor.typed.Behavior;
import akka.actor.typed.javadsl.AbstractBehavior;
import akka.actor.typed.javadsl.ActorContext;
import akka.actor.typed.javadsl.Behaviors;
import akka.actor.typed.javadsl.Receive;
import akka.http.javadsl.ConnectHttp;
import akka.http.javadsl.Http;
import akka.http.javadsl.ServerBinding;
import akka.http.javadsl.marshallers.jackson.Jackson;
import akka.http.javadsl.model.HttpRequest;
import akka.http.javadsl.model.HttpResponse;
import akka.http.javadsl.model.StatusCodes;
import akka.http.javadsl.server.AllDirectives;
import akka.http.javadsl.server.Route;
import akka.http.javadsl.unmarshalling.StringUnmarshallers;
import akka.stream.javadsl.Flow;

import java.time.Duration;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.CompletionStage;

import static akka.actor.typed.javadsl.AskPattern.ask;

public class HttpServerActorInteractionExample extends AllDirectives {

  private final ActorSystem<Auction.Message> system;
  private final ActorRef<Auction.Message> auction;

  public static void main(String[] args) throws Exception {
    // boot up server using the route as defined below
    ActorSystem<Auction.Message> system = ActorSystem.create(Auction.create(), "routes");

    final Http http = Http.get(system);

    //In order to access all directives we need an instance where the routes are define.
    HttpServerActorInteractionExample app = new HttpServerActorInteractionExample(system);

    final CompletionStage<ServerBinding> binding =
      http.newServerAt("localhost", 8080)
        .bind(app.createRoute());

    System.out.println("Server online at http://localhost:8080/\nPress RETURN to stop...");
    System.in.read(); // let it run until user presses return

    binding
      .thenCompose(ServerBinding::unbind) // trigger unbinding from the port
      .thenAccept(unbound -> system.terminate()); // and shutdown when done
  }

  private HttpServerActorInteractionExample(final ActorSystem<Auction.Message> system) {
    this.system = system;
    this.auction = system;
  }

  private Route createRoute() {
    return concat(
      path("auction", () -> concat(
        put(() ->
          parameter(StringUnmarshallers.INTEGER, "bid", bid ->
            parameter("user", user -> {
              // place a bid, fire-and-forget
              auction.tell(new Auction.Bid(user, bid));
              return complete(StatusCodes.ACCEPTED, "bid placed");
            })
          )),
        get(() -> {
          // query the actor for the current auction state
          CompletionStage<Auction.Bids> bids = ask(auction, Auction.GetBids::new, Duration.ofSeconds(5), system.scheduler());
          return completeOKWithFuture(bids, Jackson.marshaller());
        }))));
  }

  static class Auction extends AbstractBehavior<Auction.Message> {
    interface Message {}

    static class Bid implements Message {
      public final String userId;
      public final int offer;

      Bid(String userId, int offer) {
        this.userId = userId;
        this.offer = offer;
      }
    }

    static class GetBids implements Message {
      final ActorRef<Bids> replyTo;

      GetBids(ActorRef<Bids> replyTo) {
        this.replyTo = replyTo;
      }
    }

    static class Bids {
      public final List<Bid> bids;

      Bids(List<Bid> bids) {
        this.bids = bids;
      }
    }

    public Auction(ActorContext<Message> context) {
      super(context);
    }

    private List<Bid> bids = new ArrayList<>();

    public static Behavior<Message> create() {
      return Behaviors.setup(Auction::new);
    }

    @Override
    public Receive<Message> createReceive() {
      return newReceiveBuilder()
        .onMessage(Bid.class, this::onBid)
        .onMessage(GetBids.class, this::onGetBids)
        .build();
    }

    private Behavior<Message> onBid(Bid bid) {
      bids.add(bid);
      getContext().getLog().info("Bid complete: {}, {}", bid.userId, bid.offer);
      return this;
    }

    private Behavior<Message> onGetBids(GetBids getBids) {
      getBids.replyTo.tell(new Bids(bids));
      return this;
    }
  }
}
```

When you run this server, you can add an auction bid via `curl -X PUT "http://localhost:8080/auction?bid=22&user=MartinO"` on the terminal; and then you can view the auction status either in a browser, at the url http://localhost:8080/auction, or, on the terminal, via `curl http://localhost:8080/auction`.

More details on how JSON marshalling and unmarshalling works can be found in the JSON Support section.

Read more about the details of the high level APIs in the section High-level Server-Side API.

## Low-level HTTP server APIs

The low-level Akka HTTP server APIs allows for handling connections or individual requests by accepting `HttpRequest``HttpRequest` s and answering them by producing `HttpResponse``HttpResponse` s. This is provided by the `akka-http-core` module, which is included automatically when you depend on `akka-http` but can also be used on its own. APIs for handling such request-responses as function calls and as a `Flow<HttpRequest, HttpResponse, ?>``Flow[HttpRequest, HttpResponse, _]` are available.

**Scala**

```scala
source/*
 * Copyright (C) 2020-2025 Lightbend Inc. <https://akka.io>
 */

package docs.http.scaladsl

import akka.actor.typed.ActorSystem
import akka.actor.typed.scaladsl.Behaviors
import akka.http.scaladsl.Http
import akka.http.scaladsl.model.HttpMethods._
import akka.http.scaladsl.model._

import scala.concurrent.ExecutionContext
import scala.io.StdIn

object HttpServerLowLevel {

  def main(args: Array[String]): Unit = {
    implicit val system = ActorSystem(Behaviors.empty, "lowlevel")
    // needed for the future map/flatmap in the end
    implicit val executionContext: ExecutionContext = system.executionContext

    val requestHandler: HttpRequest => HttpResponse = {
      case HttpRequest(GET, Uri.Path("/"), _, _, _) =>
        HttpResponse(entity = HttpEntity(
          ContentTypes.`text/html(UTF-8)`,
          "<html><body>Hello world!</body></html>"))

      case HttpRequest(GET, Uri.Path("/ping"), _, _, _) =>
        HttpResponse(entity = "PONG!")

      case HttpRequest(GET, Uri.Path("/crash"), _, _, _) =>
        sys.error("BOOM!")

      case r: HttpRequest =>
        r.discardEntityBytes() // important to drain incoming HTTP Entity stream
        HttpResponse(404, entity = "Unknown resource!")
    }

    val bindingFuture = Http().newServerAt("localhost", 8080).bindSync(requestHandler)
    println(s"Server online at http://localhost:8080/\nPress RETURN to stop...")
    StdIn.readLine() // let it run until user presses return
    bindingFuture
      .flatMap(_.unbind()) // trigger unbinding from the port
      .onComplete(_ => system.terminate()) // and shutdown when done

  }
}
```

**Java**

```java
sourceimport akka.actor.typed.ActorSystem;
import akka.actor.typed.javadsl.Behaviors;
import akka.http.javadsl.ConnectHttp;
import akka.http.javadsl.Http;
import akka.http.javadsl.ServerBinding;
import akka.http.javadsl.model.ContentTypes;
import akka.http.javadsl.model.HttpResponse;
import akka.http.javadsl.model.StatusCodes;
import akka.stream.SystemMaterializer;
import akka.util.ByteString;

import java.util.concurrent.CompletionStage;

public class HttpServerLowLevelExample {

  public static void main(String[] args) throws Exception {
    ActorSystem<Void> system = ActorSystem.create(Behaviors.empty(), "lowlevel");

    try {
      CompletionStage<ServerBinding> serverBindingFuture =
        Http.get(system).newServerAt("localhost", 8080).bindSync(
          request -> {
            if (request.getUri().path().equals("/"))
              return HttpResponse.create().withEntity(ContentTypes.TEXT_HTML_UTF8,
                ByteString.fromString("<html><body>Hello world!</body></html>"));
            else if (request.getUri().path().equals("/ping"))
              return HttpResponse.create().withEntity(ByteString.fromString("PONG!"));
            else if (request.getUri().path().equals("/crash"))
              throw new RuntimeException("BOOM!");
            else {
              request.discardEntityBytes(system);
              return HttpResponse.create().withStatus(StatusCodes.NOT_FOUND).withEntity("Unknown resource!");
            }
          });

      System.out.println("Server online at http://localhost:8080/\nPress RETURN to stop...");
      System.in.read(); // let it run until user presses return

      serverBindingFuture
        .thenCompose(ServerBinding::unbind) // trigger unbinding from the port
        .thenAccept(unbound -> system.terminate()); // and shutdown when done

    } catch (RuntimeException e) {
      system.terminate();
    }
  }
}
```

Read more details about the low level APIs in the section Core Server API.

## HTTP Client API

The client APIs provide methods for calling an HTTP server using the same `HttpRequest``HttpRequest` and `HttpResponse``HttpResponse` abstractions that Akka HTTP server uses but adds the concept of connection pools to allow multiple requests to the same server to be handled more performantly by re-using TCP connections to the server.

Example simple request:

**Scala**

```scala
source/*
 * Copyright (C) 2020-2025 Lightbend Inc. <https://akka.io>
 */

package docs.http.scaladsl

import akka.actor.typed.ActorSystem
import akka.actor.typed.scaladsl.Behaviors
import akka.http.scaladsl.Http
import akka.http.scaladsl.model._

import scala.concurrent.Future
import scala.util.{ Failure, Success }

object HttpClientSingleRequest {
  def main(args: Array[String]): Unit = {
    implicit val system = ActorSystem(Behaviors.empty, "SingleRequest")
    // needed for the future flatMap/onComplete in the end
    implicit val executionContext = system.executionContext

    val responseFuture: Future[HttpResponse] = Http().singleRequest(HttpRequest(uri = "http://akka.io"))

    responseFuture
      .onComplete {
        case Success(res) => println(res)
        case Failure(_)   => sys.error("something wrong")
      }
  }
}
```

**Java**

```java
sourceimport akka.actor.typed.ActorSystem;
import akka.actor.typed.javadsl.Behaviors;
import akka.http.javadsl.Http;
import akka.http.javadsl.model.*;
import akka.http.javadsl.server.examples.petstore.Pet;
import akka.stream.SystemMaterializer;

import java.util.concurrent.CompletionStage;

public class ClientSingleRequestExample {

  public static void main(String[] args) {
    final ActorSystem<Void> system = ActorSystem.create(Behaviors.empty(), "SingleRequest");

    final CompletionStage<HttpResponse> responseFuture =
      Http.get(system)
        .singleRequest(HttpRequest.create("https://akka.io"));
  }
}
```

Read more about the details of the client APIs in the section Consuming HTTP-based Services (Client-Side).

## The modules that make up Akka HTTP

Akka HTTP is structured into several modules:

**akka-http**

Higher-level functionality, like (un)marshalling, (de)compression as well as a powerful DSL for defining HTTP-based APIs on the server-side, this is the recommended way to write HTTP servers with Akka HTTP. Details can be found in the section

High-level Server-Side API

**akka-http-core**

A complete, mostly low-level, server- and client-side implementation of HTTP (incl. WebSockets) Details can be found in sections

Core Server API

and

Consuming HTTP-based Services (Client-Side)

**akka-http-testkit**

A test harness and set of utilities for verifying server-side service implementations

**akka-http-spray-json**

Predefined glue-code for (de)serializing custom types from/to JSON with

spray-json

Details can be found here:

JSON Support

**akka-http-xml**

Predefined glue-code for (de)serializing custom types from/to XML with

scala-xml

Details can be found here:

XML Support

**akka-http-jackson**

Predefined glue-code for (de)serializing custom types from/to JSON with

jackson

**akka-http-jwt**

Provides directives for validating and extracting JSON Web Tokens (JWT) from requests. Details can be found in the section

JWT Directives

Found an error in this documentation? The source code for this page can be found

here

. Please feel free to edit and contribute a pull request.
