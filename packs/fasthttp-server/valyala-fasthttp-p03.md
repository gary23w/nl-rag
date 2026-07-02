---
title: "fasthttp package (part 3/5)"
source: https://pkg.go.dev/github.com/valyala/fasthttp
domain: fasthttp-server
license: CC-BY-SA-4.0
tags: fasthttp go server, golang high performance http, zero allocation http, fasthttp request context
fetched: 2026-07-02
part: 3/5
---

# fasthttp package

```
Output:
```

#### func (*RequestCtx) HijackSetNoResponse ¶ added in v1.7.1

```
func (ctx *RequestCtx) HijackSetNoResponse(noResponse bool)
```

HijackSetNoResponse changes the behavior of hijacking a request. If HijackSetNoResponse is called with false fasthttp will send a response to the client before calling the HijackHandler (default). If HijackSetNoResponse is called with true no response is send back before calling the HijackHandler supplied in the Hijack function.

#### func (*RequestCtx) Hijacked

```
func (ctx *RequestCtx) Hijacked() bool
```

Hijacked returns true after Hijack is called.

#### func (*RequestCtx) Host

```
func (ctx *RequestCtx) Host() []byte
```

Host returns requested host.

The returned bytes are valid until your request handler returns.

#### func (*RequestCtx) ID

```
func (ctx *RequestCtx) ID() uint64
```

ID returns unique ID of the request.

#### func (*RequestCtx) IfModifiedSince

```
func (ctx *RequestCtx) IfModifiedSince(lastModified time.Time) bool
```

IfModifiedSince returns true if lastModified exceeds 'If-Modified-Since' value from the request header.

The function returns true also 'If-Modified-Since' request header is missing.

#### func (*RequestCtx) Init

```
func (ctx *RequestCtx) Init(req *Request, remoteAddr net.Addr, logger Logger)
```

Init prepares ctx for passing to RequestHandler.

remoteAddr and logger are optional. They are used by RequestCtx.Logger().

This function is intended for custom Server implementations.

#### func (*RequestCtx) Init2

```
func (ctx *RequestCtx) Init2(conn net.Conn, logger Logger, reduceMemoryUsage bool)
```

Init2 prepares ctx for passing to RequestHandler.

conn is used only for determining local and remote addresses.

This function is intended for custom Server implementations. See https://github.com/valyala/httpteleport for details.

#### func (*RequestCtx) IsBodyStream

```
func (ctx *RequestCtx) IsBodyStream() bool
```

IsBodyStream returns true if response body is set via SetBodyStream*.

#### func (*RequestCtx) IsConnect ¶ added in v1.0.0

```
func (ctx *RequestCtx) IsConnect() bool
```

IsConnect returns true if request method is CONNECT.

#### func (*RequestCtx) IsDelete

```
func (ctx *RequestCtx) IsDelete() bool
```

IsDelete returns true if request method is DELETE.

#### func (*RequestCtx) IsGet

```
func (ctx *RequestCtx) IsGet() bool
```

IsGet returns true if request method is GET.

#### func (*RequestCtx) IsHead

```
func (ctx *RequestCtx) IsHead() bool
```

IsHead returns true if request method is HEAD.

#### func (*RequestCtx) IsOptions ¶ added in v1.0.0

```
func (ctx *RequestCtx) IsOptions() bool
```

IsOptions returns true if request method is OPTIONS.

#### func (*RequestCtx) IsPatch ¶ added in v1.0.0

```
func (ctx *RequestCtx) IsPatch() bool
```

IsPatch returns true if request method is PATCH.

#### func (*RequestCtx) IsPost

```
func (ctx *RequestCtx) IsPost() bool
```

IsPost returns true if request method is POST.

#### func (*RequestCtx) IsPut

```
func (ctx *RequestCtx) IsPut() bool
```

IsPut returns true if request method is PUT.

#### func (*RequestCtx) IsTLS

```
func (ctx *RequestCtx) IsTLS() bool
```

IsTLS returns true if the underlying connection is tls.Conn.

tls.Conn is an encrypted connection (aka SSL, HTTPS).

#### func (*RequestCtx) IsTrace ¶ added in v1.0.0

```
func (ctx *RequestCtx) IsTrace() bool
```

IsTrace returns true if request method is TRACE.

#### func (*RequestCtx) LastTimeoutErrorResponse

```
func (ctx *RequestCtx) LastTimeoutErrorResponse() *Response
```

LastTimeoutErrorResponse returns the last timeout response set via TimeoutError* call.

This function is intended for custom server implementations.

#### func (*RequestCtx) LocalAddr

```
func (ctx *RequestCtx) LocalAddr() net.Addr
```

LocalAddr returns server address for the given request.

Always returns non-nil result.

#### func (*RequestCtx) LocalIP

```
func (ctx *RequestCtx) LocalIP() net.IP
```

LocalIP returns the server ip the request came to.

Always returns non-nil result.

#### func (*RequestCtx) Logger

```
func (ctx *RequestCtx) Logger() Logger
```

Logger returns logger, which may be used for logging arbitrary request-specific messages inside RequestHandler.

Each message logged via returned logger contains request-specific information such as request id, request duration, local address, remote address, request method and request url.

It is safe re-using returned logger for logging multiple messages for the current request.

The returned logger is valid until your request handler returns.

Example

¶

```
package main

import (
	"fmt"
	"log"

	"github.com/valyala/fasthttp"
)

func main() {
	requestHandler := func(ctx *fasthttp.RequestCtx) {
		if string(ctx.Path()) == "/top-secret" {
			ctx.Logger().Printf("Alarm! Alien intrusion detected!")
			ctx.Error("Access denied!", fasthttp.StatusForbidden)
			return
		}

		// Logger may be cached in local variables.
		logger := ctx.Logger()

		logger.Printf("Good request from User-Agent %q", ctx.Request.Header.UserAgent())
		fmt.Fprintf(ctx, "Good request to %q", ctx.Path())
		logger.Printf("Multiple log messages may be written during a single request")
	}

	if err := fasthttp.ListenAndServe(":80", requestHandler); err != nil {
		log.Fatalf("error in ListenAndServe: %v", err)
	}
}
```

```
Output:
```

#### func (*RequestCtx) Method

```
func (ctx *RequestCtx) Method() []byte
```

Method return request method.

Returned value is valid until your request handler returns.

#### func (*RequestCtx) MultipartForm

```
func (ctx *RequestCtx) MultipartForm() (*multipart.Form, error)
```

MultipartForm returns request's multipart form.

Returns ErrNoMultipartForm if request's content-type isn't 'multipart/form-data'.

This method is equivalent to MultipartFormWithLimit(0), i.e. no body size limit is applied during multipart parsing.

All uploaded temporary files are automatically deleted after returning from RequestHandler. Either move or copy uploaded files into new place if you want retaining them.

Use SaveMultipartFile function for permanently saving uploaded file.

The returned form is valid until your request handler returns.

See also FormFile and FormValue.

#### func (*RequestCtx) MultipartFormWithLimit ¶ added in v1.70.0

```
func (ctx *RequestCtx) MultipartFormWithLimit(maxBodySize int) (*multipart.Form, error)
```

MultipartFormWithLimit returns request's multipart form and limits the read multipart body size to maxBodySize bytes.

If maxBodySize <= 0, then no limit is applied.

Call this method before FormValue/FormFile if you need a limit for multipart parsing.

#### func (*RequestCtx) NotFound

```
func (ctx *RequestCtx) NotFound()
```

NotFound resets response and sets '404 Not Found' response status code.

#### func (*RequestCtx) NotModified

```
func (ctx *RequestCtx) NotModified()
```

NotModified resets response and sets '304 Not Modified' response status code.

#### func (*RequestCtx) Path

```
func (ctx *RequestCtx) Path() []byte
```

Path returns requested path.

The returned bytes are valid until your request handler returns.

#### func (*RequestCtx) PostArgs

```
func (ctx *RequestCtx) PostArgs() *Args
```

PostArgs returns POST arguments.

It doesn't return query arguments from RequestURI - use QueryArgs for this.

See also QueryArgs, FormValue and FormFile.

These args are valid until your request handler returns.

#### func (*RequestCtx) PostBody

```
func (ctx *RequestCtx) PostBody() []byte
```

PostBody returns POST request body.

The returned bytes are valid until your request handler returns.

#### func (*RequestCtx) QueryArgs

```
func (ctx *RequestCtx) QueryArgs() *Args
```

QueryArgs returns query arguments from RequestURI.

It doesn't return POST'ed arguments - use PostArgs() for this.

See also PostArgs, FormValue and FormFile.

These args are valid until your request handler returns.

#### func (*RequestCtx) Redirect

```
func (ctx *RequestCtx) Redirect(uri string, statusCode int)
```

Redirect sets 'Location: uri' response header and sets the given statusCode.

statusCode must have one of the following values:

- StatusMovedPermanently (301)
- StatusFound (302)
- StatusSeeOther (303)
- StatusTemporaryRedirect (307)
- StatusPermanentRedirect (308)

All other statusCode values are replaced by StatusFound (302).

The redirect uri may be either absolute or relative to the current request uri. Fasthttp will always send an absolute uri back to the client. To send a relative uri you can use the following code:

```
strLocation = []byte("Location") // Put this with your top level var () declarations.
ctx.Response.Header.SetCanonical(strLocation, "/relative?uri")
ctx.Response.SetStatusCode(fasthttp.StatusMovedPermanently)
```

#### func (*RequestCtx) RedirectBytes

```
func (ctx *RequestCtx) RedirectBytes(uri []byte, statusCode int)
```

RedirectBytes sets 'Location: uri' response header and sets the given statusCode.

statusCode must have one of the following values:

- StatusMovedPermanently (301)
- StatusFound (302)
- StatusSeeOther (303)
- StatusTemporaryRedirect (307)
- StatusPermanentRedirect (308)

All other statusCode values are replaced by StatusFound (302).

The redirect uri may be either absolute or relative to the current request uri. Fasthttp will always send an absolute uri back to the client. To send a relative uri you can use the following code:

```
strLocation = []byte("Location") // Put this with your top level var () declarations.
ctx.Response.Header.SetCanonical(strLocation, "/relative?uri")
ctx.Response.SetStatusCode(fasthttp.StatusMovedPermanently)
```

#### func (*RequestCtx) Referer

```
func (ctx *RequestCtx) Referer() []byte
```

Referer returns request referer.

The returned bytes are valid until your request handler returns.

#### func (*RequestCtx) RemoteAddr

```
func (ctx *RequestCtx) RemoteAddr() net.Addr
```

RemoteAddr returns client address for the given request.

Always returns non-nil result.

#### func (*RequestCtx) RemoteIP

```
func (ctx *RequestCtx) RemoteIP() net.IP
```

RemoteIP returns the client ip the request came from.

Always returns non-nil result.

#### func (*RequestCtx) RemoveUserValue ¶ added in v1.31.0

```
func (ctx *RequestCtx) RemoveUserValue(key any)
```

RemoveUserValue removes the given key and the value under it in Request.

#### func (*RequestCtx) RemoveUserValueBytes ¶ added in v1.31.0

```
func (ctx *RequestCtx) RemoveUserValueBytes(key []byte)
```

RemoveUserValueBytes removes the given key and the value under it in Request.

#### func (*RequestCtx) RequestBodyStream ¶ added in v1.20.0

```
func (ctx *RequestCtx) RequestBodyStream() io.Reader
```

#### func (*RequestCtx) RequestURI

```
func (ctx *RequestCtx) RequestURI() []byte
```

RequestURI returns RequestURI.

The returned bytes are valid until your request handler returns.

#### func (*RequestCtx) ResetBody

```
func (ctx *RequestCtx) ResetBody()
```

ResetBody resets response body contents.

#### func (*RequestCtx) ResetUserValues ¶ added in v1.29.0

```
func (ctx *RequestCtx) ResetUserValues()
```

ResetUserValues allows to reset user values from Request.

#### func (*RequestCtx) SendFile

```
func (ctx *RequestCtx) SendFile(path string)
```

SendFile sends local file contents from the given path as response body.

This is a shortcut to ServeFile(ctx, path).

SendFile logs all the errors via ctx.Logger.

SendFile interprets path as a URI path internally. Percent-encoded sequences may be decoded, and '?' or '#' may be treated as URI delimiters. Use SendFileLiteral if you need literal path semantics.

See also ServeFile, SendFileLiteral, FSHandler and FS.

WARNING: do not pass any user supplied paths to this function! WARNING: if path is based on user input users will be able to request any file on your filesystem! Use fasthttp.FS with a sane Root instead.

#### func (*RequestCtx) SendFileBytes

```
func (ctx *RequestCtx) SendFileBytes(path []byte)
```

SendFileBytes sends local file contents from the given path as response body.

This is a shortcut to ServeFileBytes(ctx, path).

SendFileBytes logs all the errors via ctx.Logger.

See also ServeFileBytes, FSHandler and FS.

WARNING: do not pass any user supplied paths to this function! WARNING: if path is based on user input users will be able to request any file on your filesystem! Use fasthttp.FS with a sane Root instead.

#### func (*RequestCtx) SendFileLiteral ¶ added in v1.70.0

```
func (ctx *RequestCtx) SendFileLiteral(path string)
```

SendFileLiteral sends local file contents from the given path as response body using literal path semantics.

This is a shortcut to ServeFileLiteral(ctx, path).

SendFileLiteral logs all the errors via ctx.Logger.

See also ServeFileLiteral, SendFile, FSHandler and FS.

WARNING: do not pass any user supplied paths to this function! WARNING: if path is based on user input users will be able to request any file on your filesystem! Use fasthttp.FS with a sane Root instead.

#### func (*RequestCtx) SetBody

```
func (ctx *RequestCtx) SetBody(body []byte)
```

SetBody sets response body to the given value.

It is safe re-using body argument after the function returns.

#### func (*RequestCtx) SetBodyStream

```
func (ctx *RequestCtx) SetBodyStream(bodyStream io.Reader, bodySize int)
```

SetBodyStream sets response body stream and, optionally body size.

bodyStream.Close() is called after finishing reading all body data if it implements io.Closer.

If bodySize is >= 0, then bodySize bytes must be provided by bodyStream before returning io.EOF.

If bodySize < 0, then bodyStream is read until io.EOF.

See also SetBodyStreamWriter.

#### func (*RequestCtx) SetBodyStreamWriter

```
func (ctx *RequestCtx) SetBodyStreamWriter(sw StreamWriter)
```

SetBodyStreamWriter registers the given stream writer for populating response body.

Access to RequestCtx and/or its members is forbidden from sw.

This function may be used in the following cases:

- if response body is too big (more than 10MB).
- if response body is streamed from slow external sources.
- if response body must be streamed to the client in chunks. (aka `http server push`).

Example

¶

```
package main

import (
	"bufio"
	"fmt"
	"log"
	"time"

	"github.com/valyala/fasthttp"
)

func main() {
	// Start fasthttp server for streaming responses.
	if err := fasthttp.ListenAndServe(":8080", responseStreamHandler); err != nil {
		log.Fatalf("unexpected error in server: %v", err)
	}
}

func responseStreamHandler(ctx *fasthttp.RequestCtx) {
	// Send the response in chunks and wait for a second between each chunk.
	ctx.SetBodyStreamWriter(func(w *bufio.Writer) {
		for i := range 10 {
			fmt.Fprintf(w, "this is a message number %d", i)

			// Do not forget flushing streamed data to the client.
			if err := w.Flush(); err != nil {
				return
			}
			time.Sleep(time.Second)
		}
	})
}
```

```
Output:
```

#### func (*RequestCtx) SetBodyString

```
func (ctx *RequestCtx) SetBodyString(body string)
```

SetBodyString sets response body to the given value.

#### func (*RequestCtx) SetConnectionClose

```
func (ctx *RequestCtx) SetConnectionClose()
```

SetConnectionClose sets 'Connection: close' response header and closes connection after the RequestHandler returns.

#### func (*RequestCtx) SetContentType

```
func (ctx *RequestCtx) SetContentType(contentType string)
```

SetContentType sets response Content-Type.

#### func (*RequestCtx) SetContentTypeBytes

```
func (ctx *RequestCtx) SetContentTypeBytes(contentType []byte)
```

SetContentTypeBytes sets response Content-Type.

It is safe modifying contentType buffer after function return.

#### func (*RequestCtx) SetRemoteAddr ¶ added in v1.24.0

```
func (ctx *RequestCtx) SetRemoteAddr(remoteAddr net.Addr)
```

SetRemoteAddr sets remote address to the given value.

Set nil value to restore default behaviour for using connection remote address.

#### func (*RequestCtx) SetStatusCode

```
func (ctx *RequestCtx) SetStatusCode(statusCode int)
```

SetStatusCode sets response status code.

#### func (*RequestCtx) SetUserValue

```
func (ctx *RequestCtx) SetUserValue(key, value any)
```

SetUserValue stores the given value (arbitrary object) under the given key in Request.

The value stored in Request may be obtained by UserValue*.

This functionality may be useful for passing arbitrary values between functions involved in request processing.

All the values are removed from Request after returning from the top RequestHandler. Additionally, Close method is called on each value implementing io.Closer before removing the value from Request.

#### func (*RequestCtx) SetUserValueBytes

```
func (ctx *RequestCtx) SetUserValueBytes(key []byte, value any)
```

SetUserValueBytes stores the given value (arbitrary object) under the given key in Request.

The value stored in Request may be obtained by UserValue*.

This functionality may be useful for passing arbitrary values between functions involved in request processing.

All the values stored in Request are deleted after returning from RequestHandler.

#### func (*RequestCtx) String

```
func (ctx *RequestCtx) String() string
```

String returns unique string representation of the ctx.

The returned value may be useful for logging.

#### func (*RequestCtx) Success

```
func (ctx *RequestCtx) Success(contentType string, body []byte)
```

Success sets response Content-Type and body to the given values.

#### func (*RequestCtx) SuccessString

```
func (ctx *RequestCtx) SuccessString(contentType, body string)
```

SuccessString sets response Content-Type and body to the given values.

#### func (*RequestCtx) TLSConnectionState

```
func (ctx *RequestCtx) TLSConnectionState() *tls.ConnectionState
```

TLSConnectionState returns TLS connection state.

The function returns nil if the underlying connection isn't tls.Conn.

The returned state may be used for verifying TLS version, client certificates, etc.

#### func (*RequestCtx) Time

```
func (ctx *RequestCtx) Time() time.Time
```

Time returns RequestHandler call time.

#### func (*RequestCtx) TimeoutError

```
func (ctx *RequestCtx) TimeoutError(msg string)
```

TimeoutError sets response status code to StatusRequestTimeout and sets body to the given msg.

All response modifications after TimeoutError call are ignored.

TimeoutError MUST be called before returning from RequestHandler if there are references to ctx and/or its members in other goroutines remain.

Usage of this function is discouraged. Prefer eliminating ctx references from pending goroutines instead of using this function.

Example

¶

```
package main

import (
	"fmt"
	"log"
	"math/rand"
	"time"

	"github.com/valyala/fasthttp"
)

func main() {
	requestHandler := func(ctx *fasthttp.RequestCtx) {
		// Emulate long-running task, which touches ctx.
		doneCh := make(chan struct{})
		go func() {
			workDuration := time.Millisecond * time.Duration(rand.Intn(2000))
			time.Sleep(workDuration)

			fmt.Fprintf(ctx, "ctx has been accessed by long-running task\n")
			fmt.Fprintf(ctx, "The requestHandler may be finished by this time.\n")

			close(doneCh)
		}()

		select {
		case <-doneCh:
			fmt.Fprintf(ctx, "The task has been finished in less than a second")
		case <-time.After(time.Second):
			// Since the long-running task is still running and may access ctx,
			// we must call TimeoutError before returning from requestHandler.
			//
			// Otherwise the program will suffer from data races.
			ctx.TimeoutError("Timeout!")
		}
	}

	if err := fasthttp.ListenAndServe(":80", requestHandler); err != nil {
		log.Fatalf("error in ListenAndServe: %v", err)
	}
}
```

```
Output:
```

#### func (*RequestCtx) TimeoutErrorWithCode

```
func (ctx *RequestCtx) TimeoutErrorWithCode(msg string, statusCode int)
```

TimeoutErrorWithCode sets response body to msg and response status code to statusCode.

All response modifications after TimeoutErrorWithCode call are ignored.

TimeoutErrorWithCode MUST be called before returning from RequestHandler if there are references to ctx and/or its members in other goroutines remain.

Usage of this function is discouraged. Prefer eliminating ctx references from pending goroutines instead of using this function.

#### func (*RequestCtx) TimeoutErrorWithResponse

```
func (ctx *RequestCtx) TimeoutErrorWithResponse(resp *Response)
```

TimeoutErrorWithResponse marks the ctx as timed out and sends the given response to the client.

All ctx modifications after TimeoutErrorWithResponse call are ignored.

TimeoutErrorWithResponse MUST be called before returning from RequestHandler if there are references to ctx and/or its members in other goroutines remain.

Usage of this function is discouraged. Prefer eliminating ctx references from pending goroutines instead of using this function.

#### func (*RequestCtx) URI

```
func (ctx *RequestCtx) URI() *URI
```

URI returns requested uri.

This uri is valid until your request handler returns.

#### func (*RequestCtx) UserAgent

```
func (ctx *RequestCtx) UserAgent() []byte
```

UserAgent returns User-Agent header value from the request.

The returned bytes are valid until your request handler returns.

#### func (*RequestCtx) UserValue

```
func (ctx *RequestCtx) UserValue(key any) any
```

UserValue returns the value stored via SetUserValue* under the given key.

#### func (*RequestCtx) UserValueBytes

```
func (ctx *RequestCtx) UserValueBytes(key []byte) any
```

UserValueBytes returns the value stored via SetUserValue* under the given key.

#### func (*RequestCtx) Value ¶ added in v1.1.0

```
func (ctx *RequestCtx) Value(key any) any
```

Value returns the value associated with this context for key, or nil if no value is associated with key. Successive calls to Value with the same key returns the same result.

This method is present to make RequestCtx implement the context interface. This method is the same as calling ctx.UserValue(key).

#### func (*RequestCtx) VisitUserValues

```
func (ctx *RequestCtx) VisitUserValues(visitor func([]byte, any))
```

VisitUserValues calls visitor for each existing userValue with a key that is a string or []byte.

visitor must not retain references to key and value after returning. Make key and/or value copies if you need storing them after returning.

#### func (*RequestCtx) VisitUserValuesAll ¶ added in v1.41.0

```
func (ctx *RequestCtx) VisitUserValuesAll(visitor func(any, any))
```

VisitUserValuesAll calls visitor for each existing userValue.

visitor must not retain references to key and value after returning. Make key and/or value copies if you need storing them after returning.

#### func (*RequestCtx) Write

```
func (ctx *RequestCtx) Write(p []byte) (int, error)
```

Write writes p into response body.

#### func (*RequestCtx) WriteString

```
func (ctx *RequestCtx) WriteString(s string) (int, error)
```

WriteString appends s to response body.

#### type RequestHandler

```
type RequestHandler func(ctx *RequestCtx)
```

RequestHandler must process incoming requests.

RequestHandler must call ctx.TimeoutError() before returning if it keeps references to ctx and/or its members after the return. Consider wrapping RequestHandler into TimeoutHandler if response time must be limited.

#### func CompressHandler

```
func CompressHandler(h RequestHandler) RequestHandler
```

CompressHandler returns RequestHandler that transparently compresses response body generated by h if the request contains 'gzip' or 'deflate' 'Accept-Encoding' header.

#### func CompressHandlerBrotliLevel ¶ added in v1.13.0

```
func CompressHandlerBrotliLevel(h RequestHandler, brotliLevel, otherLevel int) RequestHandler
```

CompressHandlerBrotliLevel returns RequestHandler that transparently compresses response body generated by h if the request contains a 'br', 'gzip' or 'deflate' 'Accept-Encoding' header.

brotliLevel is the desired compression level for brotli.

- CompressBrotliNoCompression
- CompressBrotliBestSpeed
- CompressBrotliBestCompression
- CompressBrotliDefaultCompression

otherLevel is the desired compression level for gzip and deflate.

- CompressNoCompression
- CompressBestSpeed
- CompressBestCompression
- CompressDefaultCompression
- CompressHuffmanOnly

#### func CompressHandlerLevel

```
func CompressHandlerLevel(h RequestHandler, level int) RequestHandler
```

CompressHandlerLevel returns RequestHandler that transparently compresses response body generated by h if the request contains a 'gzip' or 'deflate' 'Accept-Encoding' header.

Level is the desired compression level:

- CompressNoCompression
- CompressBestSpeed
- CompressBestCompression
- CompressDefaultCompression
- CompressHuffmanOnly

#### func FSHandler

```
func FSHandler(root string, stripSlashes int) RequestHandler
```

FSHandler returns request handler serving static files from the given root folder.

stripSlashes indicates how many leading slashes must be stripped from requested path before searching requested file in the root folder. Examples:

- stripSlashes = 0, original path: "/foo/bar", result: "/foo/bar"
- stripSlashes = 1, original path: "/foo/bar", result: "/bar"
- stripSlashes = 2, original path: "/foo/bar", result: ""

The returned request handler automatically generates index pages for directories without index.html.

The returned handler caches requested file handles for FSHandlerCacheDuration. Make sure your program has enough 'max open files' limit aka 'ulimit -n' if root folder contains many files.

Do not create multiple request handler instances for the same (root, stripSlashes) arguments - just reuse a single instance. Otherwise goroutine leak will occur.

Example

¶

```
package main

import (
	"bytes"
	"log"

	"github.com/valyala/fasthttp"
)

// Setup file handlers (aka 'file server config').
var (
	// Handler for serving images from /img/ path,
	// i.e. /img/foo/bar.jpg will be served from
	// /var/www/images/foo/bar.jpb .
	imgPrefix  = []byte("/img/")
	imgHandler = fasthttp.FSHandler("/var/www/images", 1)

	// Handler for serving css from /static/css/ path,
	// i.e. /static/css/foo/bar.css will be served from
	// /home/dev/css/foo/bar.css .
	cssPrefix  = []byte("/static/css/")
	cssHandler = fasthttp.FSHandler("/home/dev/css", 2)

	// Handler for serving the rest of requests,
	// i.e. /foo/bar/baz.html will be served from
	// /var/www/files/foo/bar/baz.html .
	filesHandler = fasthttp.FSHandler("/var/www/files", 0)
)

// Main request handler.
func requestHandler(ctx *fasthttp.RequestCtx) {
	path := ctx.Path()
	switch {
	case bytes.HasPrefix(path, imgPrefix):
		imgHandler(ctx)
	case bytes.HasPrefix(path, cssPrefix):
		cssHandler(ctx)
	default:
		filesHandler(ctx)
	}
}

func main() {
	if err := fasthttp.ListenAndServe(":80", requestHandler); err != nil {
		log.Fatalf("Error in server: %v", err)
	}
}
```

```
Output:
```

#### func TimeoutHandler

```
func TimeoutHandler(h RequestHandler, timeout time.Duration, msg string) RequestHandler
```

TimeoutHandler creates RequestHandler, which returns StatusRequestTimeout error with the given msg to the client if h didn't return during the given duration.

The returned handler may return StatusTooManyRequests error with the given msg to the client if there are more than Server.Concurrency concurrent handlers h are running at the moment.

#### func TimeoutWithCodeHandler ¶ added in v1.4.0

```
func TimeoutWithCodeHandler(h RequestHandler, timeout time.Duration, msg string, statusCode int) RequestHandler
```

TimeoutWithCodeHandler creates RequestHandler, which returns an error with the given msg and status code to the client if h didn't return during the given duration.

The returned handler may return StatusTooManyRequests error with the given msg to the client if there are more than Server.Concurrency concurrent handlers h are running at the moment.

#### type RequestHeader

```
type RequestHeader struct {
	
}
```

RequestHeader represents HTTP request header.

It is forbidden copying RequestHeader instances. Create new instances instead and use CopyTo.

RequestHeader instance MUST NOT be used from concurrently running goroutines.

#### func (*RequestHeader) Add

```
func (h *RequestHeader) Add(key, value string)
```

Add adds the given 'key: value' header.

Multiple headers with the same key may be added with this function. Use Set for setting a single header for the given key.

If the header is set as a Trailer (forbidden trailers will not be set, see AddTrailer for more details), it will be sent after the chunked request body.

#### func (*RequestHeader) AddBytesK

```
func (h *RequestHeader) AddBytesK(key []byte, value string)
```

AddBytesK adds the given 'key: value' header.

Multiple headers with the same key may be added with this function. Use SetBytesK for setting a single header for the given key.

If the header is set as a Trailer (forbidden trailers will not be set, see AddTrailer for more details), it will be sent after the chunked request body.

#### func (*RequestHeader) AddBytesKV

```
func (h *RequestHeader) AddBytesKV(key, value []byte)
```

AddBytesKV adds the given 'key: value' header.

Multiple headers with the same key may be added with this function. Use SetBytesKV for setting a single header for the given key.

the Content-Type, Content-Length, Connection, Transfer-Encoding, Host and User-Agent headers can only be set once and will overwrite the previous value, while the Cookie header will not clear previous cookies.

If the header is set as a Trailer (forbidden trailers will not be set, see AddTrailer for more details), it will be sent after the chunked request body.

#### func (*RequestHeader) AddBytesV

```
func (h *RequestHeader) AddBytesV(key string, value []byte)
```

AddBytesV adds the given 'key: value' header.

Multiple headers with the same key may be added with this function. Use SetBytesV for setting a single header for the given key.

If the header is set as a Trailer (forbidden trailers will not be set, see AddTrailer for more details), it will be sent after the chunked request body.

#### func (*RequestHeader) AddTrailer ¶ added in v1.32.0

```
func (h *RequestHeader) AddTrailer(trailer string) error
```

AddTrailer add Trailer header value for chunked response to indicate which headers will be sent after the body.

Use Set to set the trailer header later.

Trailers are only supported with chunked transfer. Trailers allow the sender to include additional headers at the end of chunked messages.

The following trailers are forbidden: 1. necessary for message framing (e.g., Transfer-Encoding and Content-Length), 2. routing (e.g., Host), 3. request modifiers (e.g., controls and conditionals in Section 5 of [RFC7231]), 4. authentication (e.g., see [RFC7235] and [RFC6265]), 5. response control data (e.g., see Section 7.1 of [RFC7231]), 6. determining how to process the payload (e.g., Content-Encoding, Content-Type, Content-Range, and Trailer)

Return ErrBadTrailer if contain any forbidden trailers.

#### func (*RequestHeader) AddTrailerBytes ¶ added in v1.32.0

```
func (h *RequestHeader) AddTrailerBytes(trailer []byte) (err error)
```

AddTrailerBytes add Trailer header value for chunked response to indicate which headers will be sent after the body.

Use Set to set the trailer header later.

Trailers are only supported with chunked transfer. Trailers allow the sender to include additional headers at the end of chunked messages.

The following trailers are forbidden: 1. necessary for message framing (e.g., Transfer-Encoding and Content-Length), 2. routing (e.g., Host), 3. request modifiers (e.g., controls and conditionals in Section 5 of [RFC7231]), 4. authentication (e.g., see [RFC7235] and [RFC6265]), 5. response control data (e.g., see Section 7.1 of [RFC7231]), 6. determining how to process the payload (e.g., Content-Encoding, Content-Type, Content-Range, and Trailer)

Return ErrBadTrailer if contain any forbidden trailers.

#### func (*RequestHeader) All ¶ added in v1.63.0

```
func (h *RequestHeader) All() iter.Seq2[[]byte, []byte]
```

All returns an iterator over key-value pairs in h.

The key and value may invalid outside the iteration loop. Copy key and/or value contents for each iteration if you need retaining them.

To get the headers in order they were received use AllInOrder.

Making modifications to the RequestHeader during the iteration loop leads to undefined behavior and can cause panics.

#### func (*RequestHeader) AllInOrder ¶ added in v1.63.0

```
func (h *RequestHeader) AllInOrder() iter.Seq2[[]byte, []byte]
```

AllInOrder returns an iterator over key-value pairs in h in the order they were received.

The key and value may invalid outside the iteration loop. Copy key and/or value contents for each iteration if you need retaining them.

The returned iterator is slightly slower than All because it has to reparse the raw headers to get the order.

Making modifications to the RequestHeader during the iteration loop leads to undefined behavior and can cause panics.

#### func (*RequestHeader) AppendBytes

```
func (h *RequestHeader) AppendBytes(dst []byte) []byte
```

AppendBytes appends request header representation to dst and returns the extended dst.

#### func (*RequestHeader) ConnectionClose

```
func (h *RequestHeader) ConnectionClose() bool
```

ConnectionClose returns true if 'Connection: close' header is set.

#### func (*RequestHeader) ConnectionUpgrade

```
func (h *RequestHeader) ConnectionUpgrade() bool
```

ConnectionUpgrade returns true if 'Connection: Upgrade' header is set.

#### func (*RequestHeader) ContentEncoding ¶ added in v1.38.0

```
func (h *RequestHeader) ContentEncoding() []byte
```

ContentEncoding returns Content-Encoding header value.

#### func (*RequestHeader) ContentLength

```
func (h *RequestHeader) ContentLength() int
```

ContentLength returns Content-Length header value.

It may be negative: -1 means Transfer-Encoding: chunked. -2 means Transfer-Encoding: identity.

#### func (*RequestHeader) ContentType

```
func (h *RequestHeader) ContentType() []byte
```

ContentType returns Content-Type header value.

#### func (*RequestHeader) Cookie

```
func (h *RequestHeader) Cookie(key string) []byte
```

Cookie returns cookie for the given key.

#### func (*RequestHeader) CookieBytes

```
func (h *RequestHeader) CookieBytes(key []byte) []byte
```

CookieBytes returns cookie for the given key.

#### func (*RequestHeader) Cookies ¶ added in v1.63.0

```
func (h *RequestHeader) Cookies() iter.Seq2[[]byte, []byte]
```

Cookies returns an iterator over key-value pairs request cookie in h.

The key and value may invalid outside the iteration loop. Copy key and/or value contents for each iteration if you need retaining them.

Making modifications to the RequestHeader during the iteration loop leads to undefined behavior and can cause panics.

#### func (*RequestHeader) CopyTo

```
func (h *RequestHeader) CopyTo(dst *RequestHeader)
```

CopyTo copies all the headers to dst.

#### func (*RequestHeader) Del

```
func (h *RequestHeader) Del(key string)
```

Del deletes header with the given key.

#### func (*RequestHeader) DelAllCookies

```
func (h *RequestHeader) DelAllCookies()
```

DelAllCookies removes all the cookies from request headers.

#### func (*RequestHeader) DelBytes

```
func (h *RequestHeader) DelBytes(key []byte)
```

DelBytes deletes header with the given key.

#### func (*RequestHeader) DelCookie

```
func (h *RequestHeader) DelCookie(key string)
```

DelCookie removes cookie under the given key.

#### func (*RequestHeader) DelCookieBytes

```
func (h *RequestHeader) DelCookieBytes(key []byte)
```

DelCookieBytes removes cookie under the given key.

#### func (*RequestHeader) DisableNormalizing

```
func (h *RequestHeader) DisableNormalizing() bool
```

DisableNormalizing disables header names' normalization.

By default all the header names are normalized by uppercasing the first letter and all the first letters following dashes, while lowercasing all the other letters. Examples:

- CONNECTION -> Connection
- conteNT-tYPE -> Content-Type
- foo-bar-baz -> Foo-Bar-Baz

Disable header names' normalization only if know what are you doing. The previous setting is returned.

#### func (*RequestHeader) DisableSpecialHeader ¶ added in v1.48.0

```
func (h *RequestHeader) DisableSpecialHeader() bool
```

DisableSpecialHeader disables special header processing. fasthttp will not set any special headers for you, such as Host, Content-Type, User-Agent, etc. You must set everything yourself. If RequestHeader.Read() is called, special headers will be ignored. This can be used to control case and order of special headers. This is generally not recommended. The previous setting is returned.

#### func (*RequestHeader) EnableNormalizing ¶ added in v1.16.0

```
func (h *RequestHeader) EnableNormalizing() bool
```

EnableNormalizing enables header names' normalization.

Header names are normalized by uppercasing the first letter and all the first letters following dashes, while lowercasing all the other letters. Examples:

- CONNECTION -> Connection
- conteNT-tYPE -> Content-Type
- foo-bar-baz -> Foo-Bar-Baz

This is enabled by default unless disabled using DisableNormalizing(). The previous setting is returned.

#### func (*RequestHeader) EnableSpecialHeader ¶ added in v1.48.0

```
func (h *RequestHeader) EnableSpecialHeader() bool
```

EnableSpecialHeader enables special header processing. fasthttp will send Host, Content-Type, User-Agent, etc headers for you. This is suggested and enabled by default. The previous setting is returned.

#### func (*RequestHeader) HasAcceptEncoding

```
func (h *RequestHeader) HasAcceptEncoding(acceptEncoding string) bool
```

HasAcceptEncoding returns true if the header contains the given Accept-Encoding value.

#### func (*RequestHeader) HasAcceptEncodingBytes

```
func (h *RequestHeader) HasAcceptEncodingBytes(acceptEncoding []byte) bool
```

HasAcceptEncodingBytes returns true if the header contains the given Accept-Encoding value.

#### func (*RequestHeader) Header

```
func (h *RequestHeader) Header() []byte
```

Header returns request header representation.

Headers that set as Trailer will not represent. Use TrailerHeader for trailers.

The returned value is valid until the request is released, either though ReleaseRequest or your request handler returning. Do not store references to returned value. Make copies instead.

#### func (*RequestHeader) Host

```
func (h *RequestHeader) Host() []byte
```

Host returns Host header value.

#### func (*RequestHeader) IsConnect ¶ added in v1.0.0

```
func (h *RequestHeader) IsConnect() bool
```

IsConnect returns true if request method is CONNECT.

#### func (*RequestHeader) IsDelete

```
func (h *RequestHeader) IsDelete() bool
```

IsDelete returns true if request method is DELETE.

#### func (*RequestHeader) IsGet

```
func (h *RequestHeader) IsGet() bool
```

IsGet returns true if request method is GET.

#### func (*RequestHeader) IsHTTP11

```
func (h *RequestHeader) IsHTTP11() bool
```

IsHTTP11 returns true if the header is HTTP/1.1.

#### func (*RequestHeader) IsHead

```
func (h *RequestHeader) IsHead() bool
```

IsHead returns true if request method is HEAD.

#### func (*RequestHeader) IsOptions ¶ added in v1.0.0

```
func (h *RequestHeader) IsOptions() bool
```

IsOptions returns true if request method is OPTIONS.

#### func (*RequestHeader) IsPatch ¶ added in v1.0.0

```
func (h *RequestHeader) IsPatch() bool
```

IsPatch returns true if request method is PATCH.

#### func (*RequestHeader) IsPost

```
func (h *RequestHeader) IsPost() bool
```

IsPost returns true if request method is POST.

#### func (*RequestHeader) IsPut

```
func (h *RequestHeader) IsPut() bool
```

IsPut returns true if request method is PUT.

#### func (*RequestHeader) IsTrace ¶ added in v1.0.0

```
func (h *RequestHeader) IsTrace() bool
```

IsTrace returns true if request method is TRACE.

#### func (*RequestHeader) Len

```
func (h *RequestHeader) Len() int
```

Len returns the number of headers set, i.e. the number of times f is called in VisitAll.

#### func (*RequestHeader) Method

```
func (h *RequestHeader) Method() []byte
```

Method returns HTTP request method.

#### func (*RequestHeader) MultipartFormBoundary

```
func (h *RequestHeader) MultipartFormBoundary() []byte
```

MultipartFormBoundary returns boundary part from 'multipart/form-data; boundary=...' Content-Type.

#### func (*RequestHeader) Peek

```
func (h *RequestHeader) Peek(key string) []byte
```

Peek returns header value for the given key.

The returned value is valid until the request is released, either though ReleaseRequest or your request handler returning. Do not store references to returned value. Make copies instead.

#### func (*RequestHeader) PeekAll ¶ added in v1.41.0

```
func (h *RequestHeader) PeekAll(key string) [][]byte
```

PeekAll returns all header value for the given key.

The returned value is valid until the request is released, either though ReleaseRequest or your request handler returning. Any future calls to the Peek* will modify the returned value. Do not store references to returned value. Make copies instead.

#### func (*RequestHeader) PeekBytes

```
func (h *RequestHeader) PeekBytes(key []byte) []byte
```

PeekBytes returns header value for the given key.

The returned value is valid until the request is released, either though ReleaseRequest or your request handler returning. Do not store references to returned value. Make copies instead.

#### func (*RequestHeader) PeekKeys ¶ added in v1.42.0

```
func (h *RequestHeader) PeekKeys() [][]byte
```

PeekKeys return all header keys.

The returned value is valid until the request is released, either though ReleaseRequest or your request handler returning. Any future calls to the Peek* will modify the returned value. Do not store references to returned value. Make copies instead.

#### func (*RequestHeader) PeekTrailerKeys ¶ added in v1.42.0

```
func (h *RequestHeader) PeekTrailerKeys() [][]byte
```

PeekTrailerKeys return all trailer keys.

The returned value is valid until the request is released, either though ReleaseResponse or your request handler returning. Any future calls to the Peek* will modify the returned value. Do not store references to returned value. Make copies instead.

#### func (*RequestHeader) Protocol ¶ added in v1.21.0

```
func (h *RequestHeader) Protocol() []byte
```

Protocol returns HTTP protocol.

#### func (*RequestHeader) RawHeaders ¶ added in v1.1.0

```
func (h *RequestHeader) RawHeaders() []byte
```

RawHeaders returns raw header key/value bytes.

Depending on server configuration, header keys may be normalized to capital-case in place.

This copy is set aside during parsing, so empty slice is returned for all cases where parsing did not happen. Similarly, request line is not stored during parsing and can not be returned.

The slice is not safe to use after the handler returns.

#### func (*RequestHeader) Read

```
func (h *RequestHeader) Read(r *bufio.Reader) error
```

Read reads request header from r.

io.EOF is returned if r is closed before reading the first header byte.

#### func (*RequestHeader) ReadTrailer ¶ added in v1.32.0

```
func (h *RequestHeader) ReadTrailer(r *bufio.Reader) error
```

ReadTrailer reads response trailer header from r.

io.EOF is returned if r is closed before reading the first byte.

#### func (*RequestHeader) Referer

```
func (h *RequestHeader) Referer() []byte
```

Referer returns Referer header value.

#### func (*RequestHeader) RequestURI

```
func (h *RequestHeader) RequestURI() []byte
```

RequestURI returns RequestURI from the first HTTP request line.

#### func (*RequestHeader) Reset

```
func (h *RequestHeader) Reset()
```

Reset clears request header.

#### func (*RequestHeader) ResetConnectionClose

```
func (h *RequestHeader) ResetConnectionClose()
```

ResetConnectionClose clears 'Connection: close' header if it exists.

#### func (*RequestHeader) Set

```
func (h *RequestHeader) Set(key, value string)
```

Set sets the given 'key: value' header.

Please note that the Cookie header will not clear previous cookies, delete cookies before calling in order to reset cookies.

If the header is set as a Trailer (forbidden trailers will not be set, see SetTrailer for more details), it will be sent after the chunked request body.

Use Add for setting multiple header values under the same key.

#### func (*RequestHeader) SetByteRange

```
func (h *RequestHeader) SetByteRange(startPos, endPos int)
```

SetByteRange sets 'Range: bytes=startPos-endPos' header.

- If startPos is negative, then 'bytes=-startPos' value is set.
- If endPos is negative, then 'bytes=startPos-' value is set.

#### func (*RequestHeader) SetBytesK

```
func (h *RequestHeader) SetBytesK(key []byte, value string)
```

SetBytesK sets the given 'key: value' header.

Please note that the Cookie header will not clear previous cookies, delete cookies before calling in order to reset cookies.

If the header is set as a Trailer (forbidden trailers will not be set, see SetTrailer for more details), it will be sent after the chunked request body.

Use AddBytesK for setting multiple header values under the same key.

#### func (*RequestHeader) SetBytesKV

```
func (h *RequestHeader) SetBytesKV(key, value []byte)
```

SetBytesKV sets the given 'key: value' header.

Please note that the Cookie header will not clear previous cookies, delete cookies before calling in order to reset cookies.

If the header is set as a Trailer (forbidden trailers will not be set, see SetTrailer for more details), it will be sent after the chunked request body.

Use AddBytesKV for setting multiple header values under the same key.

#### func (*RequestHeader) SetBytesV

```
func (h *RequestHeader) SetBytesV(key string, value []byte)
```

SetBytesV sets the given 'key: value' header.

Please note that the Cookie header will not clear previous cookies, delete cookies before calling in order to reset cookies.

If the header is set as a Trailer (forbidden trailers will not be set, see SetTrailer for more details), it will be sent after the chunked request body.

Use AddBytesV for setting multiple header values under the same key.

#### func (*RequestHeader) SetCanonical

```
func (h *RequestHeader) SetCanonical(key, value []byte)
```

SetCanonical sets the given 'key: value' header assuming that key is in canonical form.

Please note that the Cookie header will not clear previous cookies, delete cookies before calling in order to reset cookies.

If the header is set as a Trailer (forbidden trailers will not be set, see SetTrailer for more details), it will be sent after the chunked request body.

#### func (*RequestHeader) SetConnectionClose

```
func (h *RequestHeader) SetConnectionClose()
```

SetConnectionClose sets 'Connection: close' header.

#### func (*RequestHeader) SetContentEncoding ¶ added in v1.38.0

```
func (h *RequestHeader) SetContentEncoding(contentEncoding string)
```

SetContentEncoding sets Content-Encoding header value.

#### func (*RequestHeader) SetContentEncodingBytes ¶ added in v1.38.0

```
func (h *RequestHeader) SetContentEncodingBytes(contentEncoding []byte)
```

SetContentEncodingBytes sets Content-Encoding header value.

#### func (*RequestHeader) SetContentLength

```
func (h *RequestHeader) SetContentLength(contentLength int)
```

SetContentLength sets Content-Length header value.

Negative content-length sets 'Transfer-Encoding: chunked' header.

#### func (*RequestHeader) SetContentType

```
func (h *RequestHeader) SetContentType(contentType string)
```

SetContentType sets Content-Type header value.

#### func (*RequestHeader) SetContentTypeBytes

```
func (h *RequestHeader) SetContentTypeBytes(contentType []byte)
```

SetContentTypeBytes sets Content-Type header value.

#### func (*RequestHeader) SetCookie

```
func (h *RequestHeader) SetCookie(key, value string)
```

SetCookie sets 'key: value' cookies.

#### func (*RequestHeader) SetCookieBytesK

```
func (h *RequestHeader) SetCookieBytesK(key []byte, value string)
```

SetCookieBytesK sets 'key: value' cookies.

#### func (*RequestHeader) SetCookieBytesKV

```
func (h *RequestHeader) SetCookieBytesKV(key, value []byte)
```

SetCookieBytesKV sets 'key: value' cookies.

#### func (*RequestHeader) SetHost

```
func (h *RequestHeader) SetHost(host string)
```

SetHost sets Host header value.

#### func (*RequestHeader) SetHostBytes

```
func (h *RequestHeader) SetHostBytes(host []byte)
```

SetHostBytes sets Host header value.

#### func (*RequestHeader) SetMethod

```
func (h *RequestHeader) SetMethod(method string)
```

SetMethod sets HTTP request method.

#### func (*RequestHeader) SetMethodBytes

```
func (h *RequestHeader) SetMethodBytes(method []byte)
```

SetMethodBytes sets HTTP request method.

#### func (*RequestHeader) SetMultipartFormBoundary

```
func (h *RequestHeader) SetMultipartFormBoundary(boundary string)
```

SetMultipartFormBoundary sets the following Content-Type: 'multipart/form-data; boundary=...' where ... is substituted by the given boundary.

#### func (*RequestHeader) SetMultipartFormBoundaryBytes

```
func (h *RequestHeader) SetMultipartFormBoundaryBytes(boundary []byte)
```

SetMultipartFormBoundaryBytes sets the following Content-Type: 'multipart/form-data; boundary=...' where ... is substituted by the given boundary.

#### func (*RequestHeader) SetNoDefaultContentType ¶ added in v1.34.0

```
func (h *RequestHeader) SetNoDefaultContentType(noDefaultContentType bool)
```

SetNoDefaultContentType allows you to control if a default Content-Type header will be set (false) or not (true).

#### func (*RequestHeader) SetProtocol ¶ added in v1.21.0

```
func (h *RequestHeader) SetProtocol(protocol string)
```

SetProtocol sets HTTP request protocol.

#### func (*RequestHeader) SetProtocolBytes ¶ added in v1.21.0

```
func (h *RequestHeader) SetProtocolBytes(protocol []byte)
```

SetProtocolBytes sets HTTP request protocol.

#### func (*RequestHeader) SetReferer

```
func (h *RequestHeader) SetReferer(referer string)
```

SetReferer sets Referer header value.

#### func (*RequestHeader) SetRefererBytes

```
func (h *RequestHeader) SetRefererBytes(referer []byte)
```

SetRefererBytes sets Referer header value.

#### func (*RequestHeader) SetRequestURI

```
func (h *RequestHeader) SetRequestURI(requestURI string)
```

SetRequestURI sets RequestURI for the first HTTP request line. RequestURI must be properly encoded. Use URI.RequestURI for constructing proper RequestURI if unsure.

#### func (*RequestHeader) SetRequestURIBytes

```
func (h *RequestHeader) SetRequestURIBytes(requestURI []byte)
```

SetRequestURIBytes sets RequestURI for the first HTTP request line. RequestURI must be properly encoded. Use URI.RequestURI for constructing proper RequestURI if unsure.

#### func (*RequestHeader) SetTrailer ¶ added in v1.32.0

```
func (h *RequestHeader) SetTrailer(trailer string) error
```

SetTrailer sets header Trailer value for chunked response to indicate which headers will be sent after the body.

Use Set to set the trailer header later.

Trailers are only supported with chunked transfer. Trailers allow the sender to include additional headers at the end of chunked messages.

The following trailers are forbidden: 1. necessary for message framing (e.g., Transfer-Encoding and Content-Length), 2. routing (e.g., Host), 3. request modifiers (e.g., controls and conditionals in Section 5 of [RFC7231]), 4. authentication (e.g., see [RFC7235] and [RFC6265]), 5. response control data (e.g., see Section 7.1 of [RFC7231]), 6. determining how to process the payload (e.g., Content-Encoding, Content-Type, Content-Range, and Trailer)

Return ErrBadTrailer if contain any forbidden trailers.

#### func (*RequestHeader) SetTrailerBytes ¶ added in v1.32.0

```
func (h *RequestHeader) SetTrailerBytes(trailer []byte) error
```

SetTrailerBytes sets Trailer header value for chunked response to indicate which headers will be sent after the body.

Use Set to set the trailer header later.

Trailers are only supported with chunked transfer. Trailers allow the sender to include additional headers at the end of chunked messages.

The following trailers are forbidden: 1. necessary for message framing (e.g., Transfer-Encoding and Content-Length), 2. routing (e.g., Host), 3. request modifiers (e.g., controls and conditionals in Section 5 of [RFC7231]), 4. authentication (e.g., see [RFC7235] and [RFC6265]), 5. response control data (e.g., see Section 7.1 of [RFC7231]), 6. determining how to process the payload (e.g., Content-Encoding, Content-Type, Content-Range, and Trailer)

Return ErrBadTrailer if contain any forbidden trailers.

#### func (*RequestHeader) SetUserAgent

```
func (h *RequestHeader) SetUserAgent(userAgent string)
```

SetUserAgent sets User-Agent header value.

#### func (*RequestHeader) SetUserAgentBytes

```
func (h *RequestHeader) SetUserAgentBytes(userAgent []byte)
```

SetUserAgentBytes sets User-Agent header value.

#### func (*RequestHeader) String

```
func (h *RequestHeader) String() string
```

String returns request header representation.

#### func (*RequestHeader) TrailerHeader ¶ added in v1.32.0

```
func (h *RequestHeader) TrailerHeader() []byte
```

TrailerHeader returns request trailer header representation.

Trailers will only be received with chunked transfer.

The returned value is valid until the request is released, either though ReleaseRequest or your request handler returning. Do not store references to returned value. Make copies instead.

#### func (*RequestHeader) Trailers ¶ added in v1.63.0

```
func (h *RequestHeader) Trailers() iter.Seq[[]byte]
```

Trailers returns an iterator over trailers in h.

The value of trailer may invalid outside the iteration loop.

#### func (*RequestHeader) UserAgent

```
func (h *RequestHeader) UserAgent() []byte
```

UserAgent returns User-Agent header value.

#### func (*RequestHeader) VisitAll deprecated

```
func (h *RequestHeader) VisitAll(f func(key, value []byte))
```

VisitAll calls f for each header.

f must not retain references to key and/or value after returning. Copy key and/or value contents before returning if you need retaining them.

To get the headers in order they were received use VisitAllInOrder.

Deprecated: Use All instead.

#### func (*RequestHeader) VisitAllCookie deprecated

```
func (h *RequestHeader) VisitAllCookie(f func(key, value []byte))
```

VisitAllCookie calls f for each request cookie.

f must not retain references to key and/or value after returning.

Deprecated: Use Cookies instead.

#### func (*RequestHeader) VisitAllInOrder deprecated added in v1.1.0

```
func (h *RequestHeader) VisitAllInOrder(f func(key, value []byte))
```

VisitAllInOrder calls f for each header in the order they were received.

f must not retain references to key and/or value after returning. Copy key and/or value contents before returning if you need retaining them.

This function is slightly slower than VisitAll because it has to reparse the raw headers to get the order.

Deprecated: Use AllInOrder instead.

#### func (*RequestHeader) VisitAllTrailer deprecated added in v1.32.0

```
func (h *RequestHeader) VisitAllTrailer(f func(value []byte))
```

VisitAllTrailer calls f for each response Trailer.

f must not retain references to value after returning.

Deprecated: Use Trailers instead.

#### func (*RequestHeader) Write

```
func (h *RequestHeader) Write(w *bufio.Writer) error
```

Write writes request header to w.

#### func (*RequestHeader) WriteTo

```
func (h *RequestHeader) WriteTo(w io.Writer) (int64, error)
```

WriteTo writes request header to w.

WriteTo implements io.WriterTo interface.

#### type Resolver ¶ added in v1.7.0

```
type Resolver interface {
	LookupIPAddr(context.Context, string) (names []net.IPAddr, err error)
}
```

Resolver represents interface of the tcp resolver.

#### type Response

```
type Response struct {

	
	
	
	Header ResponseHeader

	
	
	ImmediateHeaderFlush bool

	
	
	StreamBody bool

	
	
	
	
	
	SkipBody bool
	
}
```

Response represents HTTP response.

It is forbidden copying Response instances. Create new instances and use CopyTo instead.

Response instance MUST NOT be used from concurrently running goroutines.

#### func AcquireResponse

```
func AcquireResponse() *Response
```

AcquireResponse returns an empty Response instance from response pool.

The returned Response instance may be passed to ReleaseResponse when it is no longer needed. This allows Response recycling, reduces GC pressure and usually improves performance.

#### func (*Response) AppendBody

```
func (resp *Response) AppendBody(p []byte)
```

AppendBody appends p to response body.

It is safe re-using p after the function returns.

#### func (*Response) AppendBodyString

```
func (resp *Response) AppendBodyString(s string)
```

AppendBodyString appends s to response body.

#### func (*Response) Body

```
func (resp *Response) Body() []byte
```

Body returns response body.

The returned value is valid until the response is released, either though ReleaseResponse or your request handler returning. Do not store references to returned value. Make copies instead.

#### func (*Response) BodyGunzip

```
func (resp *Response) BodyGunzip() ([]byte, error)
```

BodyGunzip returns un-gzipped body data.

This method may be used if the response header contains 'Content-Encoding: gzip' for reading un-gzipped body. Use Body for reading gzipped response body.

#### func (*Response) BodyGunzipWithLimit ¶ added in v1.70.0

```
func (resp *Response) BodyGunzipWithLimit(maxBodySize int) ([]byte, error)
```

BodyGunzipWithLimit returns un-gzipped body data and limits the size of uncompressed body data to maxBodySize bytes.

If maxBodySize <= 0, then no limit is applied.

#### func (*Response) BodyInflate
