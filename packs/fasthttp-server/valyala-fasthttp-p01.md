---
title: "fasthttp package (part 1/5)"
source: https://pkg.go.dev/github.com/valyala/fasthttp
domain: fasthttp-server
license: CC-BY-SA-4.0
tags: fasthttp go server, golang high performance http, zero allocation http, fasthttp request context
fetched: 2026-07-02
part: 1/5
---

# fasthttp

package

module

Version:

v1.72.0

Opens a new window with list of versions in this module.

Latest

Latest

This package is not in the latest version of its module.

Go to latest

Published: Jun 27, 2026

License:

MIT

Opens a new window with license information.

Imports:

43

Opens a new window with list of imports.

Imported by:

9,851

Opens a new window with list of known importers.


## README

### fasthttp

(Go Reference) (Go Report)

Fast HTTP implementation for Go.

#### fasthttp might not be for you!

fasthttp was designed for some high performance edge cases. **Unless** your server/client needs to handle **thousands of small to medium requests per second** and needs a consistent low millisecond response time fasthttp might not be for you. **For most cases `net/http` is much better** as it's easier to use and can handle more cases. For most cases you won't even notice the performance difference.

#### General info and links

Currently fasthttp is successfully used by VertaMedia in a production serving up to 200K rps from more than 1.5M concurrent keep-alive connections per physical server.

TechEmpower Benchmark round 23 results

Server Benchmarks

Client Benchmarks

Install

Documentation

Examples from docs

Code examples

Awesome fasthttp tools

Switching from net/http to fasthttp

Fasthttp best practices

Related projects

FAQ

#### HTTP server performance comparison with net/http

In short, fasthttp server is up to 6 times faster than net/http. Below are benchmark results.

*GOMAXPROCS=1*

net/http server:

```
$ GOMAXPROCS=1 go test -bench=NetHTTPServerGet -benchmem -benchtime=10s
cpu: Intel(R) Xeon(R) CPU @ 2.20GHz
BenchmarkNetHTTPServerGet1ReqPerConn                      722565             15327 ns/op            3258 B/op         36 allocs/op
BenchmarkNetHTTPServerGet2ReqPerConn                      990067             11533 ns/op            2817 B/op         28 allocs/op
BenchmarkNetHTTPServerGet10ReqPerConn                    1376821              8734 ns/op            2483 B/op         23 allocs/op
BenchmarkNetHTTPServerGet10KReqPerConn                   1691265              7151 ns/op            2385 B/op         21 allocs/op
BenchmarkNetHTTPServerGet1ReqPerConn10KClients            643940             17152 ns/op            3529 B/op         36 allocs/op
BenchmarkNetHTTPServerGet2ReqPerConn10KClients            868576             14010 ns/op            2826 B/op         28 allocs/op
BenchmarkNetHTTPServerGet10ReqPerConn10KClients          1297398              9329 ns/op            2611 B/op         23 allocs/op
BenchmarkNetHTTPServerGet100ReqPerConn10KClients         1467963              7902 ns/op            2450 B/op         21 allocs/op
```

fasthttp server:

```
$ GOMAXPROCS=1 go test -bench=kServerGet -benchmem -benchtime=10s
cpu: Intel(R) Xeon(R) CPU @ 2.20GHz
BenchmarkServerGet1ReqPerConn                    4304683              2733 ns/op               0 B/op          0 allocs/op
BenchmarkServerGet2ReqPerConn                    5685157              2140 ns/op               0 B/op          0 allocs/op
BenchmarkServerGet10ReqPerConn                   7659729              1550 ns/op               0 B/op          0 allocs/op
BenchmarkServerGet10KReqPerConn                  8580660              1422 ns/op               0 B/op          0 allocs/op
BenchmarkServerGet1ReqPerConn10KClients          4092148              3009 ns/op               0 B/op          0 allocs/op
BenchmarkServerGet2ReqPerConn10KClients          5272755              2208 ns/op               0 B/op          0 allocs/op
BenchmarkServerGet10ReqPerConn10KClients         7566351              1546 ns/op               0 B/op          0 allocs/op
BenchmarkServerGet100ReqPerConn10KClients        8369295              1418 ns/op               0 B/op          0 allocs/op
```

*GOMAXPROCS=4*

net/http server:

```
$ GOMAXPROCS=4 go test -bench=NetHTTPServerGet -benchmem -benchtime=10s
cpu: Intel(R) Xeon(R) CPU @ 2.20GHz
BenchmarkNetHTTPServerGet1ReqPerConn-4                   2670654              4542 ns/op            3263 B/op         36 allocs/op
BenchmarkNetHTTPServerGet2ReqPerConn-4                   3376021              3559 ns/op            2823 B/op         28 allocs/op
BenchmarkNetHTTPServerGet10ReqPerConn-4                  4387959              2707 ns/op            2489 B/op         23 allocs/op
BenchmarkNetHTTPServerGet10KReqPerConn-4                 5412049              2179 ns/op            2386 B/op         21 allocs/op
BenchmarkNetHTTPServerGet1ReqPerConn10KClients-4         2226048              5216 ns/op            3289 B/op         36 allocs/op
BenchmarkNetHTTPServerGet2ReqPerConn10KClients-4         2989957              3982 ns/op            2839 B/op         28 allocs/op
BenchmarkNetHTTPServerGet10ReqPerConn10KClients-4        4383570              2834 ns/op            2514 B/op         23 allocs/op
BenchmarkNetHTTPServerGet100ReqPerConn10KClients-4       5315100              2394 ns/op            2419 B/op         21 allocs/op
```

fasthttp server:

```
$ GOMAXPROCS=4 go test -bench=kServerGet -benchmem -benchtime=10s
cpu: Intel(R) Xeon(R) CPU @ 2.20GHz
BenchmarkServerGet1ReqPerConn-4                  7797037              1494 ns/op               0 B/op          0 allocs/op
BenchmarkServerGet2ReqPerConn-4                 13004892               963.7 ns/op             0 B/op          0 allocs/op
BenchmarkServerGet10ReqPerConn-4                22479348               522.6 ns/op             0 B/op          0 allocs/op
BenchmarkServerGet10KReqPerConn-4               25899390               451.4 ns/op             0 B/op          0 allocs/op
BenchmarkServerGet1ReqPerConn10KClients-4        8421531              1469 ns/op               0 B/op          0 allocs/op
BenchmarkServerGet2ReqPerConn10KClients-4       13426772               903.7 ns/op             0 B/op          0 allocs/op
BenchmarkServerGet10ReqPerConn10KClients-4      21899584               513.5 ns/op             0 B/op          0 allocs/op
BenchmarkServerGet100ReqPerConn10KClients-4     25291686               439.4 ns/op             0 B/op          0 allocs/op
```

#### HTTP client comparison with net/http

In short, fasthttp client is up to 4 times faster than net/http. Below are benchmark results.

*GOMAXPROCS=1*

net/http client:

```
$ GOMAXPROCS=1 go test -bench='HTTPClient(Do|GetEndToEnd)' -benchmem -benchtime=10s
cpu: Intel(R) Xeon(R) CPU @ 2.20GHz
BenchmarkNetHTTPClientDoFastServer                        885637             13883 ns/op            3384 B/op         44 allocs/op
BenchmarkNetHTTPClientGetEndToEnd1TCP                     203875             55619 ns/op            6296 B/op         70 allocs/op
BenchmarkNetHTTPClientGetEndToEnd10TCP                    231290             54618 ns/op            6299 B/op         70 allocs/op
BenchmarkNetHTTPClientGetEndToEnd100TCP                   202879             58278 ns/op            6304 B/op         69 allocs/op
BenchmarkNetHTTPClientGetEndToEnd1Inmemory                396764             26878 ns/op            6216 B/op         69 allocs/op
BenchmarkNetHTTPClientGetEndToEnd10Inmemory               396422             28373 ns/op            6209 B/op         68 allocs/op
BenchmarkNetHTTPClientGetEndToEnd100Inmemory              363976             33101 ns/op            6326 B/op         68 allocs/op
BenchmarkNetHTTPClientGetEndToEnd1000Inmemory             208881             51725 ns/op            8298 B/op         84 allocs/op
BenchmarkNetHTTPClientGetEndToEndWaitConn1Inmemory           237          50451765 ns/op            7474 B/op         79 allocs/op
BenchmarkNetHTTPClientGetEndToEndWaitConn10Inmemory          237          50447244 ns/op            7434 B/op         77 allocs/op
BenchmarkNetHTTPClientGetEndToEndWaitConn100Inmemory         238          50067993 ns/op            8639 B/op         82 allocs/op
BenchmarkNetHTTPClientGetEndToEndWaitConn1000Inmemory       1366           7324990 ns/op            4064 B/op         44 allocs/op
```

fasthttp client:

```
$ GOMAXPROCS=1 go test -bench='kClient(Do|GetEndToEnd)' -benchmem -benchtime=10s
cpu: Intel(R) Xeon(R) CPU @ 2.20GHz
BenchmarkClientGetEndToEnd1TCP                    406376             26558 ns/op               0 B/op          0 allocs/op
BenchmarkClientGetEndToEnd10TCP                   517425             23595 ns/op               0 B/op          0 allocs/op
BenchmarkClientGetEndToEnd100TCP                  474800             25153 ns/op               3 B/op          0 allocs/op
BenchmarkClientGetEndToEnd1Inmemory              2563800              4827 ns/op               0 B/op          0 allocs/op
BenchmarkClientGetEndToEnd10Inmemory             2460135              4805 ns/op               0 B/op          0 allocs/op
BenchmarkClientGetEndToEnd100Inmemory            2520543              4846 ns/op               0 B/op          0 allocs/op
BenchmarkClientGetEndToEnd1000Inmemory           2437015              4914 ns/op               2 B/op          0 allocs/op
BenchmarkClientGetEndToEnd10KInmemory            2481050              5049 ns/op               9 B/op          0 allocs/op
```

*GOMAXPROCS=4*

net/http client:

```
$ GOMAXPROCS=4 go test -bench='HTTPClient(Do|GetEndToEnd)' -benchmem -benchtime=10s
cpu: Intel(R) Xeon(R) CPU @ 2.20GHz
BenchmarkNetHTTPClientGetEndToEnd1TCP-4                           767133             16175 ns/op            6304 B/op         69 allocs/op
BenchmarkNetHTTPClientGetEndToEnd10TCP-4                          785198             15276 ns/op            6295 B/op         69 allocs/op
BenchmarkNetHTTPClientGetEndToEnd100TCP-4                         780464             15605 ns/op            6305 B/op         69 allocs/op
BenchmarkNetHTTPClientGetEndToEnd1Inmemory-4                     1356932              8772 ns/op            6220 B/op         68 allocs/op
BenchmarkNetHTTPClientGetEndToEnd10Inmemory-4                    1379245              8726 ns/op            6213 B/op         68 allocs/op
BenchmarkNetHTTPClientGetEndToEnd100Inmemory-4                   1119213             10294 ns/op            6418 B/op         68 allocs/op
BenchmarkNetHTTPClientGetEndToEnd1000Inmemory-4                   504194             31010 ns/op           17668 B/op        102 allocs/op
```

fasthttp client:

```
$ GOMAXPROCS=4 go test -bench='kClient(Do|GetEndToEnd)' -benchmem -benchtime=10s
cpu: Intel(R) Xeon(R) CPU @ 2.20GHz
BenchmarkClientGetEndToEnd1TCP-4                         1474552              8143 ns/op               0 B/op          0 allocs/op
BenchmarkClientGetEndToEnd10TCP-4                        1710270              7186 ns/op               0 B/op          0 allocs/op
BenchmarkClientGetEndToEnd100TCP-4                       1701672              6892 ns/op               4 B/op          0 allocs/op
BenchmarkClientGetEndToEnd1Inmemory-4                    6797713              1590 ns/op               0 B/op          0 allocs/op
BenchmarkClientGetEndToEnd10Inmemory-4                   6663642              1782 ns/op               0 B/op          0 allocs/op
BenchmarkClientGetEndToEnd100Inmemory-4                  6608209              1867 ns/op               0 B/op          0 allocs/op
BenchmarkClientGetEndToEnd1000Inmemory-4                 6254452              2645 ns/op               8 B/op          0 allocs/op
BenchmarkClientGetEndToEnd10KInmemory-4                  6944584              1966 ns/op              17 B/op          0 allocs/op
```

#### Install

```
go get -u github.com/valyala/fasthttp
```

#### Switching from net/http to fasthttp

Unfortunately, fasthttp doesn't provide API identical to net/http. See the FAQ for details. There is net/http -> fasthttp handler converter, but it is better to write fasthttp request handlers by hand in order to use all of the fasthttp advantages (especially high performance :) ).

Important points:

- Fasthttp works with RequestHandler functions instead of objects implementing Handler interface. Fortunately, it is easy to pass bound struct methods to fasthttp:
  ```
type MyHandler struct {
	foobar string
}

// request handler in net/http style, i.e. method bound to MyHandler struct.
func (h *MyHandler) HandleFastHTTP(ctx *fasthttp.RequestCtx) {
	// notice that we may access MyHandler properties here - see h.foobar.
	fmt.Fprintf(ctx, "Hello, world! Requested path is %q. Foobar is %q",
		ctx.Path(), h.foobar)
}

// request handler in fasthttp style, i.e. just plain function.
func fastHTTPHandler(ctx *fasthttp.RequestCtx) {
	fmt.Fprintf(ctx, "Hi there! RequestURI is %q", ctx.RequestURI())
}

// pass bound struct method to fasthttp
myHandler := &MyHandler{
	foobar: "foobar",
}
fasthttp.ListenAndServe(":8080", myHandler.HandleFastHTTP)

// pass plain function to fasthttp
fasthttp.ListenAndServe(":8081", fastHTTPHandler)
  ```
- The RequestHandler accepts only one argument - RequestCtx. It contains all the functionality required for http request processing and response writing. Below is an example of a simple request handler conversion from net/http to fasthttp.
  ```
// net/http request handler
requestHandler := func(w http.ResponseWriter, r *http.Request) {
	switch r.URL.Path {
	case "/foo":
		fooHandler(w, r)
	case "/bar":
		barHandler(w, r)
	default:
		http.Error(w, "Unsupported path", http.StatusNotFound)
	}
}
  ```
  ```
// the corresponding fasthttp request handler
requestHandler := func(ctx *fasthttp.RequestCtx) {
	switch string(ctx.Path()) {
	case "/foo":
		fooHandler(ctx)
	case "/bar":
		barHandler(ctx)
	default:
		ctx.Error("Unsupported path", fasthttp.StatusNotFound)
	}
}
  ```
- Fasthttp allows setting response headers and writing response body in an arbitrary order. There is no 'headers first, then body' restriction like in net/http. The following code is valid for fasthttp:
  ```
requestHandler := func(ctx *fasthttp.RequestCtx) {
	// set some headers and status code first
	ctx.SetContentType("foo/bar")
	ctx.SetStatusCode(fasthttp.StatusOK)

	// then write the first part of body
	fmt.Fprintf(ctx, "this is the first part of body\n")

	// then set more headers
	ctx.Response.Header.Set("Foo-Bar", "baz")

	// then write more body
	fmt.Fprintf(ctx, "this is the second part of body\n")

	// then override already written body
	ctx.SetBody([]byte("this is completely new body contents"))

	// then update status code
	ctx.SetStatusCode(fasthttp.StatusNotFound)

	// basically, anything may be updated many times before
	// returning from RequestHandler.
	//
	// Unlike net/http fasthttp doesn't put response to the wire until
	// returning from RequestHandler.
}
  ```
- Fasthttp doesn't provide ServeMux, but there are more powerful third-party routers and web frameworks with fasthttp support: Net/http code with simple ServeMux is trivially converted to fasthttp code:
  - fasthttp-routing
  - router
  - lu
  - atreugo
  - Fiber
  - Gearbox
  ```
// net/http code

m := &http.ServeMux{}
m.HandleFunc("/foo", fooHandlerFunc)
m.HandleFunc("/bar", barHandlerFunc)
m.Handle("/baz", bazHandler)

http.ListenAndServe(":80", m)
  ```
  ```
// the corresponding fasthttp code
m := func(ctx *fasthttp.RequestCtx) {
	switch string(ctx.Path()) {
	case "/foo":
		fooHandlerFunc(ctx)
	case "/bar":
		barHandlerFunc(ctx)
	case "/baz":
		bazHandler.HandlerFunc(ctx)
	default:
		ctx.Error("not found", fasthttp.StatusNotFound)
	}
}

fasthttp.ListenAndServe(":80", m)
  ```
- Because creating a new channel for every request is just too expensive, so the channel returned by RequestCtx.Done() is only closed when the server is shutting down.
  ```
func main() {
fasthttp.ListenAndServe(":8080", fasthttp.TimeoutHandler(func(ctx *fasthttp.RequestCtx) {
	select {
	case <-ctx.Done():
		// ctx.Done() is only closed when the server is shutting down.
		log.Println("context cancelled")
		return
	case <-time.After(10 * time.Second):
		log.Println("process finished ok")
	}
}, time.Second*2, "timeout"))
}
  ```
- net/http -> fasthttp conversion table:
  - All the pseudocode below assumes w, r and ctx have these types:
  ```
var (
	w http.ResponseWriter
	r *http.Request
	ctx *fasthttp.RequestCtx
)
  ```
  - r.Body **➜** ctx.PostBody()
  - r.URL.Path **➜** ctx.Path()
  - r.URL **➜** ctx.URI()
  - r.Method **➜** ctx.Method()
  - r.Header **➜** ctx.Request.Header
  - r.Header.Get() **➜** ctx.Request.Header.Peek()
  - r.Host **➜** ctx.Host()
  - r.Form **➜** ctx.QueryArgs() + ctx.PostArgs()
  - r.PostForm **➜** ctx.PostArgs()
  - r.FormValue() **➜** ctx.FormValue()
  - r.FormFile() **➜** ctx.FormFile()
  - r.MultipartForm **➜** ctx.MultipartForm() For untrusted multipart input, use ctx.MultipartFormWithLimit() (or a custom Server.FormValueFunc) to enforce a parsing size limit.
  - r.RemoteAddr **➜** ctx.RemoteAddr()
  - r.RequestURI **➜** ctx.RequestURI()
  - r.TLS **➜** ctx.IsTLS()
  - r.Cookie() **➜** ctx.Request.Header.Cookie()
  - r.Referer() **➜** ctx.Referer()
  - r.UserAgent() **➜** ctx.UserAgent()
  - w.Header() **➜** ctx.Response.Header
  - w.Header().Set() **➜** ctx.Response.Header.Set()
  - w.Header().Set("Content-Type") **➜** ctx.SetContentType()
  - w.Header().Set("Set-Cookie") **➜** ctx.Response.Header.SetCookie()
  - w.Write() **➜** ctx.Write(), ctx.SetBody(), ctx.SetBodyStream(), ctx.SetBodyStreamWriter()
  - w.WriteHeader() **➜** ctx.SetStatusCode()
  - w.(http.Hijacker).Hijack() **➜** ctx.Hijack()
  - http.Error() **➜** ctx.Error()
  - http.FileServer() **➜** fasthttp.FSHandler(), fasthttp.FS
  - http.ServeFile() **➜** fasthttp.ServeFile()
  - http.Redirect() **➜** ctx.Redirect()
  - http.NotFound() **➜** ctx.NotFound()
  - http.StripPrefix() **➜** fasthttp.PathRewriteFunc
- *VERY IMPORTANT!* Fasthttp disallows holding references to RequestCtx or to its' members after returning from RequestHandler. Otherwise data races are inevitable. Carefully inspect all the net/http request handlers converted to fasthttp whether they retain references to RequestCtx or to its' members after returning. RequestCtx provides the following *band aids* for this case:
  - Wrap RequestHandler into TimeoutHandler.
  - Call TimeoutError before returning from RequestHandler if there are references to RequestCtx or to its' members. See the example for more details.

Use this brilliant tool - race detector - for detecting and eliminating data races in your program. If you detected data race related to fasthttp in your program, then there is high probability you forgot calling TimeoutError before returning from RequestHandler.

- Blind switching from net/http to fasthttp won't give you performance boost. While fasthttp is optimized for speed, its' performance may be easily saturated by slow RequestHandler. So profile and optimize your code after switching to fasthttp. For instance, use quicktemplate instead of html/template.
- See also fasthttputil, fasthttpadaptor and expvarhandler.

#### Performance optimization tips for multi-core systems

- Use reuseport listener.
- Run a separate server instance per CPU core with GOMAXPROCS=1.
- Pin each server instance to a separate CPU core using taskset.
- Ensure the interrupts of multiqueue network card are evenly distributed between CPU cores. See this article for details.
- Use the latest version of Go as each version contains performance improvements.

#### Fasthttp best practices

- Do not allocate objects and `[]byte` buffers - just reuse them as much as possible. Fasthttp API design encourages this.
- sync.Pool is your best friend.
- Profile your program in production. `go tool pprof --alloc_objects your-program mem.pprof` usually gives better insights for optimization opportunities than `go tool pprof your-program cpu.pprof`.
- Write tests and benchmarks for hot paths.
- Avoid conversion between `[]byte` and `string`, since this may result in memory allocation+copy - see this wiki page for more details.
- Verify your tests and production code under race detector on a regular basis.
- Prefer quicktemplate instead of html/template in your webserver.

#### Unsafe Zero-Allocation Conversions

In performance-critical code, converting between `[]byte` and `string` using standard Go allocations can be inefficient. To address this, `fasthttp` uses **unsafe**, zero-allocation helpers:

> ⚠️ **Warning:** These conversions break Go's type safety. Use only when you're certain the converted value will not be mutated, as violating immutability can cause undefined behavior.

##### `UnsafeString(b []byte) string`

Converts a `[]byte` to a `string` **without memory allocation**.

```
// UnsafeString returns a string pointer without allocation
func UnsafeString(b []byte) string {
    // #nosec G103
    return *(*string)(unsafe.Pointer(&b))
}
```

##### `UnsafeBytes(s string) []byte`

Converts a `string` to a `[]byte` **without memory allocation**.

```
// UnsafeBytes returns a byte pointer without allocation.
func UnsafeBytes(s string) []byte {
    // #nosec G103
    return unsafe.Slice(unsafe.StringData(s), len(s))
}
```

##### Use Cases & Caveats

- These functions are ideal for performance-sensitive scenarios where allocations must be avoided (e.g., request/response processing loops).
- **Do not** mutate the `[]byte` returned from `UnsafeBytes(s string)` if the original string is still in use, as strings are immutable in Go and may be shared across the runtime.
- Use samples guarded with `#nosec G103` comments to suppress static analysis warnings about unsafe operations.

#### Tricks with `[]byte` buffers

The following tricks are used by fasthttp. Use them in your code too.

- Standard Go functions accept nil buffers

```
var (
	// both buffers are uninitialized
	dst []byte
	src []byte
)
dst = append(dst, src...)  // is legal if dst is nil and/or src is nil
copy(dst, src)  // is legal if dst is nil and/or src is nil
(string(src) == "")  // is true if src is nil
(len(src) == 0)  // is true if src is nil
src = src[:0]  // works like a charm with nil src

// this for loop doesn't panic if src is nil
for i, ch := range src {
	doSomething(i, ch)
}
```

So throw away nil checks for `[]byte` buffers from you code. For example,

```
srcLen := 0
if src != nil {
	srcLen = len(src)
}
```

becomes

```
srcLen := len(src)
```

- String may be appended to `[]byte` buffer with `append`

```
dst = append(dst, "foobar"...)
```

- `[]byte` buffer may be extended to its' capacity.

```
buf := make([]byte, 100)
a := buf[:10]  // len(a) == 10, cap(a) == 100.
b := a[:100]  // is valid, since cap(a) == 100.
```

- All fasthttp functions accept nil `[]byte` buffer

```
statusCode, body, err := fasthttp.Get(nil, "http://google.com/")
uintBuf := fasthttp.AppendUint(nil, 1234)
```

- String and `[]byte` buffers may converted without memory allocations

```
func b2s(b []byte) string {
    return *(*string)(unsafe.Pointer(&b))
}

func s2b(s string) (b []byte) {
    bh := (*reflect.SliceHeader)(unsafe.Pointer(&b))
    sh := (*reflect.StringHeader)(unsafe.Pointer(&s))
    bh.Data = sh.Data
    bh.Cap = sh.Len
    bh.Len = sh.Len
    return b
}
```

##### Warning:

This is an **unsafe** way, the result string and `[]byte` buffer share the same bytes.

**Please make sure not to modify the bytes in the `[]byte` buffer if the string still survives!**

- fasthttp - various useful helpers for projects based on fasthttp.
- fasthttp-routing - fast and powerful routing package for fasthttp servers.
- http2 - HTTP/2 implementation for fasthttp.
- router - a high performance fasthttp request router that scales well.
- fasthttp-auth - Authorization middleware for fasthttp using Casbin.
- fastws - Bloatless WebSocket package made for fasthttp to handle Read/Write operations concurrently.
- gramework - a web framework made by one of fasthttp maintainers.
- lu - a high performance go middleware web framework which is based on fasthttp.
- websocket - Gorilla-based websocket implementation for fasthttp.
- websocket - Event-based high-performance WebSocket library for zero-allocation websocket servers and clients.
- fasthttpsession - a fast and powerful session package for fasthttp servers.
- atreugo - High performance and extensible micro web framework with zero memory allocations in hot paths.
- kratgo - Simple, lightweight and ultra-fast HTTP Cache to speed up your websites.
- kit-plugins - go-kit transport implementation for fasthttp.
- Fiber - An Expressjs inspired web framework running on Fasthttp.
- Gearbox - ⚙ gearbox is a web framework written in Go with a focus on high performance and memory optimization.
- http2curl - A tool to convert fasthttp requests to curl command line.
- OpenTelemetry Golang Compile Time Instrumentation - A tool to monitor fasthttp application without changing any code with OpenTelemetry APIs.
- protoc-gen-httpgo - A protoc plugin that generates fasthttp server and client code.

#### FAQ

- *Why creating yet another http package instead of optimizing net/http?* Because net/http API limits many optimization opportunities. For example:
  - net/http Request object lifetime isn't limited by request handler execution time. So the server must create a new request object per each request instead of reusing existing objects like fasthttp does.
  - net/http headers are stored in a `map[string][]string`. So the server must parse all the headers, convert them from `[]byte` to `string` and put them into the map before calling user-provided request handler. This all requires unnecessary memory allocations avoided by fasthttp.
  - net/http client API requires creating a new response object per each request.
- *Why fasthttp API is incompatible with net/http?* Because net/http API limits many optimization opportunities. See the answer above for more details. Also certain net/http API parts are suboptimal for use:
  - Compare net/http connection hijacking to fasthttp connection hijacking.
  - Compare net/http Request.Body reading to fasthttp request body reading.
- *Why fasthttp doesn't support HTTP/2.0 and WebSockets?* HTTP/2.0 support is in progress. WebSockets has been done already. Third parties also may use RequestCtx.Hijack for implementing these goodies.
- *Are there known net/http advantages comparing to fasthttp?* Yes:
  - net/http supports HTTP/2.0 starting from go1.6.
  - net/http API is stable, while fasthttp API constantly evolves.
  - net/http handles more HTTP corner cases.
  - net/http can stream both request and response bodies
  - net/http can handle bigger bodies as it doesn't read the whole body into memory
  - net/http should contain less bugs, since it is used and tested by much wider audience.
- *Why fasthttp API prefers returning `[]byte` instead of `string`?* Because `[]byte` to `string` conversion isn't free - it requires memory allocation and copy. Feel free wrapping returned `[]byte` result into `string()` if you prefer working with strings instead of byte slices. But be aware that this has non-zero overhead.
- *Which GO versions are supported by fasthttp?* We support the same versions the Go team supports. Currently that is Go 1.25.x and newer. Older versions might work, but won't officially be supported.
- *Please provide real benchmark data and server information* See this issue.
- *Are there plans to add request routing to fasthttp?* There are no plans to add request routing into fasthttp. Use third-party routers and web frameworks with fasthttp support:
  - fasthttp-routing
  - router
  - gramework
  - lu
  - atreugo
  - Fiber
  - Gearbox
- *I detected data race in fasthttp!* Cool! File a bug. But before doing this check the following in your code:
  - Make sure there are no references to RequestCtx or to its' members after returning from RequestHandler.
  - Make sure you call TimeoutError before returning from RequestHandler if there are references to RequestCtx or to its' members, which may be accessed by other goroutines.
- *I didn't find an answer for my question here* Try exploring these questions.
