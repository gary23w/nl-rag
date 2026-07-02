---
title: "Vert.x"
source: https://en.wikipedia.org/wiki/Vert.x
domain: vertx
license: CC-BY-SA-4.0
tags: vert.x toolkit, eclipse vertx, reactive toolkit, event loop server
fetched: 2026-07-02
---

# Vert.x

**Eclipse Vert.x** is a polyglot event-driven application framework that runs on the Java virtual machine.

Similar environments written in other programming languages include Node.js for JavaScript, Twisted for Python, Perl Object Environment for Perl, libevent for C, reactPHP and amphp for PHP and EventMachine for Ruby.

## History

Vert.x was started by Tim Fox in 2011 while he was employed by VMware.

Fox initially named the project "Node.x", a play on the naming of Node.js, with the "x" representing the fact that the new project was polyglot in nature, and didn't simply support JavaScript. The project was later renamed to "Vert.x" to avoid any potential legal issues as "Node" was a trademark owned by Joyent Inc. The new name was also a play on the name node, as a vertex is a synonym for a node in mathematics.

In December 2012, after he left their employment, VMware served legal papers on Tim Fox to take control of the Vert.x trademark, domain name, blog, GitHub account, and Google Group from the Vert.x community

After much discussion with other parties, in January 2013, VMware was persuaded that it would be in the best interests of the Vert.x community to move the project and associated IP to the Eclipse Foundation, a neutral legal entity.

In August 2013, the core Vert.x project completed its move to the Eclipse Foundation. The other projects that make up the Vert.x stack did not migrate to Eclipse but continued to use the "Vert.x" trademark with tacit approval of the Eclipse Foundation.

In May 2014, Vert.x won the award for "Most Innovative Java Technology" at the JAX Innovation awards.

On January 12, 2016, Tim Fox stepped down as the lead of the Vert.x project. and Julien Viet, a long-time contributor, took his place.

### Language support

- As of version 2.1.4 (2014), Vert.x exposes its API in Java, JavaScript, Groovy, Ruby, Python, Scala, Clojure and Ceylon.
- As of version 3.7.0 (2019), Vert.x exposes its API in Java, JavaScript, Groovy, Ruby, Scala, Kotlin and Ceylon.
- As of version 3.9.1 (2020), Vert.x exposes its API in Java, JavaScript, Groovy, Ruby, Scala and Kotlin.
- As of version 4.0.0 (2020), Vert.x exposes its API in Java, Groovy and Kotlin.

## Architecture

Vert.x uses low level IO library Netty.

The application framework includes these features:

- Polyglot. Application components can be written in Java, JavaScript, Groovy, Ruby, Scala, Kotlin and Ceylon.
- Simple concurrency model. All code is single threaded, freeing from the hassle of multi-threaded programming.
- Simple, asynchronous programming model for writing truly scalable non-blocking applications.
- Distributed event bus that spans the client and server side. The event bus even penetrates into in-browser JavaScript allowing to create so-called real-time web applications.
- Actor model and public repository, to re-use and share components.

## Examples

A web server serving "Hello from Vert.x!" could be written in Java:

```mw
import io.vertx.core.AbstractVerticle;

public class Server extends AbstractVerticle {
    public void start() {
        vertx.createHttpServer().requestHandler(req -> {
            req.response()
                .putHeader("content-type", "text/plain")
                .end("Hello from Vert.x!");
        }).listen(8080);
    }
}
```

And in JavaScript:

```mw
vertx.createHttpServer()
  .requestHandler(function (req) {
    req.response()
      .putHeader("content-type", "text/plain")
      .end("Hello from Vert.x!");
}).listen(8080);
```

Both cases will result in a web server serving content in a highly scalable manner.
