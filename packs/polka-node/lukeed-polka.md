---
title: "GitHub"
source: https://github.com/lukeed/polka
domain: polka-node
license: CC-BY-SA-4.0
tags: polka node microframework, minimal node router, node.js http server, polka middleware chain
fetched: 2026-07-02
---

# GitHub

lukeed

/

polka

Public

- Uh oh! There was an error while loading. Please reload this page.
- Notifications You must be signed in to change notification settings
- Fork 175
- Star

Branches

Tags

Open more actions menu

## Folders and files

| Name | Name | Last commit message | Last commit date |
|---|---|---|---|
| Latest commit History208 Commits208 Commits |   |   |   |
| .github | .github |   |   |
| bench | bench |   |   |
| examples | examples |   |   |
| packages | packages |   |   |
| tests | tests |   |   |
| .editorconfig | .editorconfig |   |   |
| .gitignore | .gitignore |   |   |
| lerna.json | lerna.json |   |   |
| license | license |   |   |
| package.json | package.json |   |   |
| polka.png | polka.png |   |   |
| readme.md | readme.md |   |   |
|   |   |   |   |

## Repository files navigation

# Polka

A micro web server so fast, it'll make you dance! 👯

> **Black Lives Matter.** ✊🏽✊🏾✊🏿 Support the Equal Justice Initiative, Campaign Zero, or Educate Yourself.

Polka is an extremely minimal, highly performant Express.js alternative. Yes, you're right, Express is *already* super fast & not *that* big 🤔 — but Polka shows that there was (somehow) room for improvement!

Essentially, Polka is just a native HTTP server with added support for routing, middleware, and sub-applications. That's it! 🎉

And, of course, in mandatory bullet-point format:

- 33-50% faster than Express for simple applications
- Middleware support, including Express middleware you already know & love
- Nearly identical application API & route pattern definitions
- ~90 LOC for Polka, 120 including its router

## Install

```
$ npm install --save polka
```

## Usage

```highlight
const polka = require('polka');

function one(req, res, next) {
  req.hello = 'world';
  next();
}

function two(req, res, next) {
  req.foo = '...needs better demo 😔';
  next();
}

polka()
  .use(one, two)
  .get('/users/:id', (req, res) => {
    console.log(`~> Hello, ${req.hello}`);
    res.end(`User: ${req.params.id}`);
  })
  .listen(3000, () => {
    console.log(`> Running on localhost:3000`);
  });
```

## API

Polka extends Trouter which means it inherits its API, too!

### polka(options)

Returns an instance of Polka~!

#### options.server

Type: `Server`

A custom, instantiated server that the Polka instance should attach its `handler` to. This is useful if you have initialized a server elsewhere in your application and want Polka to use *it* instead of creating a new `http.Server`.

Polka *only* updates the server when `polka.listen` is called. At this time, Polka will create a `http.Server` if a server was not already provided via `options.server`.

> **Important:** The `server` key will be `undefined` until `polka.listen` is invoked, unless a server was provided.

#### options.onError

Type: `Function`

A catch-all error handler; executed whenever a middleware throws an error. Change this if you don't like default behavior.

Its signature is `(err, req, res, next)`, where `err` is the `String` or `Error` thrown by your middleware.

> **Caution:** Use `next()` to bypass certain errors **at your own risk!** You must be certain that the exception will be handled elsewhere or *can* be safely ignored. Otherwise your response will never terminate!

#### options.onNoMatch

Type: `Function`

A handler when no route definitions were matched. Change this if you don't like default behavior, which sends a `404` status & `Not found` response.

Its signature is `(req, res)` and requires that you terminate the response.

### use(base, ...fn)

Attach middleware(s) and/or sub-application(s) to the server. These will execute *before* your routes' handlers.

**Important:** If a `base` pathname is provided, all functions within the same `use()` block will *only* execute when the `req.path` matches the `base` path.

#### base

Type: `String` Default: `undefined`

The base path on which the following middleware(s) or sub-application should be mounted.

#### fn

Type: `Function|Array`

You may pass one or more functions at a time. Each function must have the standardized `(req, res, next)` signature.

You may also pass a sub-application, which *must* be accompanied by a `base` pathname.

Please see `Middleware` and Express' middleware examples for more info.

### parse(req)

Returns: `Object` or `undefined`

As of `v0.5.0`, this is an alias of the `@polka/url` module. For nearly all cases, you'll notice no changes.

But, for whatever reason, you can quickly swap in `parseurl` again:

```highlight
const app = polka();
app.parse = require('parseurl');
//=> Done!
```

### listen()

Returns: `Polka`

Boots (or creates) the underlying `http.Server` for the first time. All arguments are passed to `server.listen` directly with no changes.

As of `v0.5.0`, this method no longer returns a Promise. Instead, the current Polka instance is returned directly, allowing for chained operations.

```highlight
// Could not do this before 0.5.0
const { server, handler } = polka().listen();

// Or this!
const app = polka().listen(PORT, onAppStart);

app.use('users', require('./users'))
  .get('/', (req, res) => {
    res.end('Pretty cool!');
  });
```

### handler(req, res, parsed)

The main Polka `IncomingMessage` handler. It receives all requests and tries to match the incoming URL against known routes.

If the `req.url` is not immediately matched, Polka will look for sub-applications or middleware groups matching the `req.url`'s `base` path. If any are found, they are appended to the loop, running *after* any global middleware.

> **Note:** Any middleware defined within a sub-application is run *after* the main app's (aka, global) middleware and *before* the sub-application's route handler.

At the end of the loop, if a middleware hasn't yet terminated the response (or thrown an error), the route handler will be executed, if found — otherwise a `(404) Not found` response is returned, configurable via `options.onNoMatch`.

#### req

Type: `IncomingMessage`

#### res

Type: `ServerResponse`

#### parsed

Type: `Object`

Optionally provide a parsed URL object. Useful if you've already parsed the incoming path. Otherwise, `app.parse` (aka `parseurl`) will run by default.

## Routing

Routes are used to define how an application responds to varying HTTP methods and endpoints.

> If you're coming from Express, there's nothing new here! However, do check out Comparisons for some pattern changes.

### Basics

Each route is comprised of a path pattern, a HTTP method, and a handler (aka, what you want to do).

In code, this looks like:

```highlight
app.METHOD(pattern, handler);
```

wherein:

- `app` is an instance of `polka`
- `METHOD` is any valid HTTP/1.1 method, lowercased
- `pattern` is a routing pattern (string)
- `handler` is the function to execute when `pattern` is matched

Also, a single pathname (or `pattern`) may be reused with multiple METHODs.

The following example demonstrates some simple routes.

```highlight
const app = polka();

app.get('/', (req, res) => {
  res.end('Hello world!');
});

app.get('/users', (req, res) => {
  res.end('Get all users!');
});

app.post('/users', (req, res) => {
  res.end('Create a new User!');
});

app.put('/users/:id', (req, res) => {
  res.end(`Update User with ID of ${req.params.id}`);
});

app.delete('/users/:id', (req, res) => {
  res.end(`CY@ User ${req.params.id}!`);
});
```

### Patterns

Unlike the very popular `path-to-regexp`, Polka uses string comparison to locate route matches. While faster & more memory efficient, this does also prevent complex pattern matching.

However, have no fear! 💥 All the basic and most commonly used patterns are supported. You probably only ever used these patterns in the first place. 😉

> See Comparisons for the list of `RegExp`-based patterns that Polka does not support.

The supported pattern types are:

- static (`/users`)
- named parameters (`/users/:id`)
- nested parameters (`/users/:id/books/:title`)
- optional parameters (`/users/:id?/books/:title?`)
- any match / wildcards (`/users/*`)

### Parameters

Any named parameters included within your route `pattern` will be automatically added to your incoming `req` object. All parameters will be found within `req.params` under the same name they were given.

> **Important:** Your parameter names should be unique, as shared names will overwrite each other!

```highlight
app.get('/users/:id/books/:title', (req, res) => {
  let { id, title } = req.params;
  res.end(`User: ${id} && Book: ${title}`);
});
```

```highlight
$ curl /users/123/books/Narnia
#=> User: 123 && Book: Narnia
```

### Methods

Any valid HTTP/1.1 method is supported! However, only the most common methods are used throughout this documentation for demo purposes.

> **Note:** For a full list of valid METHODs, please see this list.

### Handlers

Request handlers accept the incoming `IncomingMessage` and the formulating `ServerResponse`.

Every route definition must contain a valid `handler` function, or else an error will be thrown at runtime.

> **Important:** You must *always* terminate a `ServerResponse`!

It's a **very good** practice to *always* terminate your response (`res.end`) inside a handler, even if you expect a middleware to do it for you. In the event a response is/was not terminated, the server will hang & eventually exit with a `TIMEOUT` error.

> **Note:** This is a native `http` behavior.

#### Async Handlers

If using Node 7.4 or later, you may leverage native `async` and `await` syntax! 😻

No special preparation is needed — simply add the appropriate keywords.

```highlight
const app = polka();

const sleep = ms => new Promise(r => setTimeout(r, ms));

async function authenticate(req, res, next) {
  let token = req.headers['authorization'];
  if (!token) return (res.statusCode=401,res.end('No token!'));
  req.user = await Users.find(token); // <== fake
  next(); // done, woot!
}

app
  .use(authenticate)
  .get('/', async (req, res) => {
    // log middleware's findings
    console.log('~> current user', req.user);
    // force sleep, because we can~!
    await sleep(500);
    // send greeting
    res.end(`Hello, ${req.user.name}`);
  });
```

## Middleware

Middleware are functions that run in between (hence "middle") receiving the request & executing your route's `handler` response.

> Coming from Express? Use any middleware you already know & love! 🎉

The middleware signature receives the request (`req`), the response (`res`), and a callback (`next`).

These can apply mutations to the `req` and `res` objects, and unlike Express, have access to `req.params`, `req.path`, `req.search`, and `req.query`!

Most importantly, a middleware ***must*** either call `next()` or terminate the response (`res.end`). Failure to do this will result in a never-ending response, which will eventually crash the `http.Server`.

```highlight
// Log every request
function logger(req, res, next) {
  console.log(`~> Received ${req.method} on ${req.url}`);
  next(); // move on
}

function authorize(req, res, next) {
  // mutate req; available later
  req.token = req.headers['authorization'];
  req.token ? next() : ((res.statusCode=401) && res.end('No token!'));
}

polka().use(logger, authorize).get('*', (req, res) => {
  console.log(`~> user token: ${req.token}`);
  res.end('Hello, valid user');
});
```

```highlight
$ curl /
# ~> Received GET on /
#=> (401) No token!

$ curl -H "authorization: secret" /foobar
# ~> Received GET on /foobar
# ~> user token: secret
#=> (200) Hello, valid user
```

### Middleware Sequence

In Polka, middleware functions are organized into tiers.

Unlike Express, Polka middleware are tiered into "global", "filtered", and "route-specific" groups.

- Global middleware are defined via `.use('/', ...fn)` or `.use(...fn)`, which are synonymous. *Because* every request's `pathname` begins with a `/`, this tier is always triggered.
- Sub-group or "filtered" middleware are defined with a base `pathname` that's more specific than `'/'`. For example, defining `.use('/users', ...fn)` will run on any `/users/**/*` request. These functions will execute *after* "global" middleware but before the route-specific handler.
- Route handlers match specific paths and execute last in the chain. They must also match the `method` action.

Once the chain of middleware handler(s) has been composed, Polka will iterate through them sequentially until all functions have run, until a chain member has terminated the response early, or until a chain member has thrown an error.

Contrast this with Express, which does not tier your middleware and instead iterates through your entire application in the sequence that you composed it.

```highlight
// Express
express()
  .get('/', get)
  .use(foo)
  .get('/users/123', user)
  .use('/users', users)

// Polka
Polka()
  .get('/', get)
  .use(foo)
  .get('/users/123', user)
  .use('/users', users)
```

```highlight
$ curl {APP}/
# Express :: [get]
# Polka   :: [foo, get]

$ curl {APP}/users/123
# Express :: [foo, user]
# Polka   :: [foo, users, user]
```

### Middleware Errors

If an error arises within a middleware, the loop will be exited. This means that no other middleware will execute & neither will the route handler.

Similarly, regardless of `statusCode`, an early response termination will also exit the loop & prevent the route handler from running.

There are three ways to "throw" an error from within a middleware function.

> **Hint:** None of them use `throw` 😹

1. **Pass any string to `next()`** This will exit the loop & send a `500` status code, with your error string as the response body. polka() .use((req, res, next) => next('💩')) .get('*', (req, res) => res.end('wont run')); $ curl / #=> (500) 💩
2. **Pass an `Error` to `next()`** This is similar to the above option, but gives you a window in changing the `statusCode` to something other than the `500` default. function oopsies(req, res, next) { let err = new Error('Try again'); err.code = 422; next(err); } $ curl / #=> (422) Try again
3. **Terminate the response early** Once the response has been ended, there's no reason to continue the loop! This approach is the most versatile as it allows to control every aspect of the outgoing `res`. function oopsies(req, res, next) { if (true) { // something bad happened~ res.writeHead(400, { 'Content-Type': 'application/json', 'X-Error-Code': 'Please dont do this IRL' }); let json = JSON.stringify({ error:'Missing CSRF token' }); res.end(json); } else { next(); // never called FYI } } $ curl / #=> (400) {"error":"Missing CSRF token"}

## Benchmarks

Quick comparison between various frameworks using `wrk` on `Node v10.4.0`. Results are taken with the following command, after one warm-up run:

```
$ wrk -t4 -c4 -d10s http://localhost:3000/users/123
```

Additional benchmarks between Polka and Express (using various Node versions) can be found here.

> **Important:** Time is mostly spent in *your application code* rather than Express or Polka code! Switching from Express to Polka will (likely) not show such drastic performance gains.

```
Native
    Thread Stats   Avg      Stdev     Max   +/- Stdev
        Latency     1.96ms  119.06us   5.33ms   92.57%
        Req/Sec    12.78k   287.46    13.13k    90.00%
      508694 requests in 10.00s, 50.45MB read
    Requests/sec:  50867.22
    Transfer/sec:      5.05MB

Polka
    Thread Stats   Avg      Stdev     Max   +/- Stdev
        Latency     1.98ms  119.26us   4.45ms   92.87%
        Req/Sec    12.68k   287.74    13.05k    94.06%
      509817 requests in 10.10s, 50.56MB read
    Requests/sec:  50475.67
    Transfer/sec:      5.01MB

Rayo
    Thread Stats   Avg      Stdev     Max   +/- Stdev
        Latency     2.02ms  116.55us   6.66ms   92.55%
        Req/Sec    12.43k   262.32    12.81k    91.58%
      499795 requests in 10.10s, 49.57MB read
    Requests/sec:  49481.55
    Transfer/sec:      4.91MB

Fastify
    Thread Stats   Avg      Stdev     Max   +/- Stdev
        Latency     2.10ms  138.04us   5.46ms   91.50%
        Req/Sec    11.96k   414.14    15.82k    95.04%
      479518 requests in 10.10s, 66.31MB read
    Requests/sec:  47476.75
    Transfer/sec:      6.57MB

Koa
    Thread Stats   Avg      Stdev     Max   +/- Stdev
        Latency     2.95ms  247.10us   6.91ms   72.18%
        Req/Sec     8.52k   277.12     9.09k    70.30%
      342518 requests in 10.10s, 47.36MB read
    Requests/sec:  33909.82
    Transfer/sec:      4.69MB

Express
    Thread Stats   Avg      Stdev     Max   +/- Stdev
        Latency     4.91ms  484.52us  10.65ms   89.71%
        Req/Sec     5.11k   350.75     9.69k    98.51%
      204520 requests in 10.10s, 40.57MB read
    Requests/sec:  20249.80
    Transfer/sec:      4.02MB
```

## Comparisons

Polka's API aims to be *very* similar to Express since most Node.js developers are already familiar with it. If you know Express, you already know Polka! 💃

There are, however, a few main differences. Polka does not support or offer:

1. **Polka uses a tiered middleware system.** Express maintains the sequence of your route & middleware declarations during its runtime, which can pose a problem when composing sub-applications. Typically, this forces you to duplicate groups of logic. Please see Middleware Sequence for an example and additional details.
2. **Any built-in view/rendering engines.** Most templating engines can be incorporated into middleware functions or used directly within a route handler.
3. **The ability to `throw` from within middleware.** However, all other forms of middleware-errors are supported. (See Middleware Errors.) function middleware(res, res, next) { // pass an error message to next() next('uh oh'); // pass an Error to next() next(new Error('🙀')); // send an early, customized error response res.statusCode = 401; res.end('Who are you?'); }
4. **Express-like response helpers... yet! (#14)** Express has a nice set of response helpers. While Polka relies on the native Node.js response methods, it would be very easy/possible to attach a global middleware that contained a similar set of helpers. (*TODO*)
5. **`RegExp`-based route patterns.** Polka's router uses string comparison to match paths against patterns. It's a lot quicker & more efficient. The following routing patterns **are not** supported: app.get('/ab?cd', _ => {}); app.get('/ab+cd', _ => {}); app.get('/ab*cd', _ => {}); app.get('/ab(cd)?e', _ => {}); app.get(/a/, _ => {}); app.get(/.*fly$/, _ => {}); The following routing patterns **are** supported: app.get('/users', _ => {}); app.get('/users/:id', _ => {}); app.get('/users/:id?', _ => {}); app.get('/users/:id/books/:title', _ => {}); app.get('/users/*', _ => {});
6. **Polka instances are not (directly) the request handler.** Most packages in the Express ecosystem expect you to pass your `app` directly into the package. This is because `express()` returns a middleware signature directly. In the Polka-sphere, this functionality lives in your application's `handler` instead. Here's an example with `supertest`, a popular testing utility for Express apps. const request = require('supertest'); const send = require('@polka/send-type'); const express = require('express')(); const polka = require('polka')(); express.get('/user', (req, res) => { res.status(200).json({ name: 'john' }); }); polka.get('/user', (req, res) => { send(res, 200, { name: 'john' }); }); function isExpected(app) { request(app) .get('/user') .expect('Content-Type', /json/) .expect('Content-Length', '15') .expect(200); } // Express: Pass in the entire application directly isExpected(express); // Polka: Pass in the application `handler` instead isExpected(polka.handler);

## License

MIT © Luke Edwards
