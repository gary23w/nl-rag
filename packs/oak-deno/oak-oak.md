---
title: "@oak/oak"
source: https://jsr.io/@oak/oak
domain: oak-deno
license: CC-BY-SA-4.0
tags: oak deno framework, deno middleware framework, deno web server, oak context router
fetched: 2026-07-02
---

# @oak/oak@17.2.0Built and signed on GitHub ActionsBuilt and signed on GitHub Actions

latest

oakserver/oak

Works with

This package works with Cloudflare Workers, Node.js, Deno, Bun

•

JSR Score

94%

•

Downloads

13,391/wk

•

Published

7 months ago (17.2.0)

A middleware framework for handling HTTP with Deno, Node.js, Bun and Cloudflare Workers 🐿️🦕🥟⚙️

A middleware framework for handling HTTP with Deno CLI, Deno Deploy, Cloudflare Workers, Node.js, and Bun.

oak is inspired by koa.

## Example server

A minimal router server which responds with content on `/`.

### Deno CLI and Deno Deploy

```
import { Application } from "jsr:@oak/oak/application";
import { Router } from "jsr:@oak/oak/router";

const router = new Router();
router.get("/", (ctx) => {
  ctx.response.body = `<!DOCTYPE html>
    <html>
      <head><title>Hello oak!</title><head>
      <body>
        <h1>Hello oak!</h1>
      </body>
    </html>
  `;
});

const app = new Application();
app.use(router.routes());
app.use(router.allowedMethods());

app.listen({ port: 8080 });
```

### Node.js and Bun

You will have to install the package and then:

```
import { Application } from "@oak/oak/application";
import { Router } from "@oak/oak/router";

const router = new Router();
router.get("/", (ctx) => {
  ctx.response.body = `<!DOCTYPE html>
    <html>
      <head><title>Hello oak!</title><head>
      <body>
        <h1>Hello oak!</h1>
      </body>
    </html>
  `;
});

const app = new Application();
app.use(router.routes());
app.use(router.allowedMethods());

app.listen({ port: 8080 });
```

### Cloudflare Workers

You will have to install the package and then:

```
import { Application } from "@oak/oak/application";
import { Router } from "@oak/oak/router";

const router = new Router();
router.get("/", (ctx) => {
  ctx.response.body = `<!DOCTYPE html>
    <html>
      <head><title>Hello oak!</title><head>
      <body>
        <h1>Hello oak!</h1>
      </body>
    </html>
  `;
});

const app = new Application();
app.use(router.routes());
app.use(router.allowedMethods());

export default { fetch: app.fetch };
```

Built and signed on

GitHub Actions

View transparency log
