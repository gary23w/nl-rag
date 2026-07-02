---
title: "Tornado (web server)"
source: https://en.wikipedia.org/wiki/Tornado_(web_server)
domain: tornado-web
license: CC-BY-SA-4.0
tags: tornado web server, tornado framework, python async server, non-blocking python
fetched: 2026-07-02
---

# Tornado (web server)

**Tornado** is a scalable, non-blocking web server and web application framework written in Python. It was developed for use by FriendFeed; the company was acquired by Facebook in 2009 and Tornado was open-sourced soon after.

## Performance

Tornado is noted for its high performance. Its design enables handling a large number of concurrent connections (i.e., tries to solve the "C10k problem").

## Modules

- An asynchronous MongoDB driver called Motor.
- CouchDB drivers called corduroy and trombi.
- Asynchronous driver for PostgreSQL wrapping psycopg called Momoko

## Example

The following code shows a simple web application that displays "Hello World!" when visited:

```mw
import asyncio

import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([(r"/", MainHandler),])

async def main():
    app = make_app()
    app.listen(8888)
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
```
