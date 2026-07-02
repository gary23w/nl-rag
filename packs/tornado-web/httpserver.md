---
title: "tornado.httpserver"
source: https://www.tornadoweb.org/en/stable/httpserver.html
domain: tornado-web
license: CC-BY-SA-4.0
tags: tornado web server, tornado framework, python async server, non-blocking python
fetched: 2026-07-02
---

# `tornado.httpserver` — Non-blocking HTTP server

A non-blocking, single-threaded HTTP server.

Typical applications have little direct interaction with the `HTTPServer` class except to start a server at the beginning of the process (and even that is often done indirectly via `tornado.web.Application.listen`).

Changed in version 4.0: The `HTTPRequest` class that used to live in this module has been moved to `tornado.httputil.HTTPServerRequest`. The old name remains as an alias.

## HTTP Server

***class*tornado.httpserver.HTTPServer(*request_callback: httputil.HTTPServerConnectionDelegate | Callable[[httputil.HTTPServerRequest], None]*, *no_keep_alive: bool = False*, *xheaders: bool = False*, *ssl_options: Dict[str, Any] | ssl.SSLContext = None*, *protocol: str | None = None*, *decompress_request: bool = False*, *chunk_size: int | None = None*, *max_header_size: int | None = None*, *idle_connection_timeout: float | None = None*, *body_timeout: float | None = None*, *max_body_size: int | None = None*, *max_buffer_size: int | None = None*, *trusted_downstream: List[str] | None = None*)[source]**

A non-blocking, single-threaded HTTP server.

A server is defined by a subclass of `HTTPServerConnectionDelegate`, or, for backwards compatibility, a callback that takes an `HTTPServerRequest` as an argument. The delegate is usually a `tornado.web.Application`.

`HTTPServer` supports keep-alive connections by default (automatically for HTTP/1.1, or for HTTP/1.0 when the client requests `Connection: keep-alive`).

If `xheaders` is `True`, we support the `X-Real-Ip`/`X-Forwarded-For` and `X-Scheme`/`X-Forwarded-Proto` headers, which override the remote IP and URI scheme/protocol for all requests. These headers are useful when running Tornado behind a reverse proxy or load balancer. The `protocol` argument can also be set to `https` if Tornado is run behind an SSL-decoding proxy that does not set one of the supported `xheaders`.

By default, when parsing the `X-Forwarded-For` header, Tornado will select the last (i.e., the closest) address on the list of hosts as the remote host IP address. To select the next server in the chain, a list of trusted downstream hosts may be passed as the `trusted_downstream` argument. These hosts will be skipped when parsing the `X-Forwarded-For` header.

To make this server serve SSL traffic, send the `ssl_options` keyword argument with an `ssl.SSLContext` object. For compatibility with older versions of Python `ssl_options` may also be a dictionary of keyword arguments for the `ssl.SSLContext.wrap_socket` method.:

```
ssl_ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_ctx.load_cert_chain(os.path.join(data_dir, "mydomain.crt"),
                        os.path.join(data_dir, "mydomain.key"))
HTTPServer(application, ssl_options=ssl_ctx)
```

`HTTPServer` initialization follows one of three patterns (the initialization methods are defined on `tornado.tcpserver.TCPServer`):

1. `listen`: single-process: async def main(): server = HTTPServer() server.listen(8888) await asyncio.Event().wait() asyncio.run(main()) In many cases, `tornado.web.Application.listen` can be used to avoid the need to explicitly create the `HTTPServer`. While this example does not create multiple processes on its own, when the `reuse_port=True` argument is passed to `listen()` you can run the program multiple times to create a multi-process service.
2. `add_sockets`: multi-process: sockets = bind_sockets(8888) tornado.process.fork_processes(0) async def post_fork_main(): server = HTTPServer() server.add_sockets(sockets) await asyncio.Event().wait() asyncio.run(post_fork_main()) The `add_sockets` interface is more complicated, but it can be used with `tornado.process.fork_processes` to run a multi-process service with all worker processes forked from a single parent. `add_sockets` can also be used in single-process servers if you want to create your listening sockets in some way other than `bind_sockets`. Note that when using this pattern, nothing that touches the event loop can be run before `fork_processes`.
3. `bind`/`start`: simple **deprecated** multi-process: server = HTTPServer() server.bind(8888) server.start(0) # Forks multiple sub-processes IOLoop.current().start() This pattern is deprecated because it requires interfaces in the `asyncio` module that have been deprecated since Python 3.10. Support for creating multiple processes in the `start` method will be removed in a future version of Tornado.

Changed in version 4.0: Added `decompress_request`, `chunk_size`, `max_header_size`, `idle_connection_timeout`, `body_timeout`, `max_body_size` arguments. Added support for `HTTPServerConnectionDelegate` instances as `request_callback`.

Changed in version 4.1: `HTTPServerConnectionDelegate.start_request` is now called with two arguments `(server_conn, request_conn)` (in accordance with the documentation) instead of one `(request_conn)`.

Changed in version 4.2: `HTTPServer` is now a subclass of `tornado.util.Configurable`.

Changed in version 4.5: Added the `trusted_downstream` argument.

Changed in version 5.0: The `io_loop` argument has been removed.

The public interface of this class is mostly inherited from `TCPServer` and is documented under that class.

***async*close_all_connections() → None[source]**

Close all open connections and asynchronously wait for them to finish.

This method is used in combination with `stop` to support clean shutdowns (especially for unittests). Typical usage would call `stop()` first to stop accepting new connections, then `await close_all_connections()` to wait for existing connections to finish.

This method does not currently close open websocket connections.

Note that this method is a coroutine and must be called with `await`.
