---
title: "fasthttp package (part 5/5)"
source: https://pkg.go.dev/github.com/valyala/fasthttp
domain: fasthttp-server
license: CC-BY-SA-4.0
tags: fasthttp go server, golang high performance http, zero allocation http, fasthttp request context
fetched: 2026-07-02
part: 5/5
---

# fasthttp package

```
func (h *ResponseHeader) SetServerBytes(server []byte)
```

SetServerBytes sets Server header value.

#### func (*ResponseHeader) SetStatusCode

```
func (h *ResponseHeader) SetStatusCode(statusCode int)
```

SetStatusCode sets response status code.

#### func (*ResponseHeader) SetStatusMessage ¶ added in v1.32.0

```
func (h *ResponseHeader) SetStatusMessage(statusMessage []byte)
```

SetStatusMessage sets response status message bytes.

#### func (*ResponseHeader) SetTrailer ¶ added in v1.32.0

```
func (h *ResponseHeader) SetTrailer(trailer string) error
```

SetTrailer sets header Trailer value for chunked response to indicate which headers will be sent after the body.

Use Set to set the trailer header later.

Trailers are only supported with chunked transfer. Trailers allow the sender to include additional headers at the end of chunked messages.

The following trailers are forbidden: 1. necessary for message framing (e.g., Transfer-Encoding and Content-Length), 2. routing (e.g., Host), 3. request modifiers (e.g., controls and conditionals in Section 5 of [RFC7231]), 4. authentication (e.g., see [RFC7235] and [RFC6265]), 5. response control data (e.g., see Section 7.1 of [RFC7231]), 6. determining how to process the payload (e.g., Content-Encoding, Content-Type, Content-Range, and Trailer)

Return ErrBadTrailer if contain any forbidden trailers.

#### func (*ResponseHeader) SetTrailerBytes ¶ added in v1.32.0

```
func (h *ResponseHeader) SetTrailerBytes(trailer []byte) error
```

SetTrailerBytes sets Trailer header value for chunked response to indicate which headers will be sent after the body.

Use Set to set the trailer header later.

Trailers are only supported with chunked transfer. Trailers allow the sender to include additional headers at the end of chunked messages.

The following trailers are forbidden: 1. necessary for message framing (e.g., Transfer-Encoding and Content-Length), 2. routing (e.g., Host), 3. request modifiers (e.g., controls and conditionals in Section 5 of [RFC7231]), 4. authentication (e.g., see [RFC7235] and [RFC6265]), 5. response control data (e.g., see Section 7.1 of [RFC7231]), 6. determining how to process the payload (e.g., Content-Encoding, Content-Type, Content-Range, and Trailer)

Return ErrBadTrailer if contain any forbidden trailers.

#### func (*ResponseHeader) StatusCode

```
func (h *ResponseHeader) StatusCode() int
```

StatusCode returns response status code.

#### func (*ResponseHeader) StatusMessage ¶ added in v1.32.0

```
func (h *ResponseHeader) StatusMessage() []byte
```

StatusMessage returns response status message.

#### func (*ResponseHeader) String

```
func (h *ResponseHeader) String() string
```

String returns response header representation.

#### func (*ResponseHeader) TrailerHeader ¶ added in v1.32.0

```
func (h *ResponseHeader) TrailerHeader() []byte
```

TrailerHeader returns response trailer header representation.

Trailers will only be received with chunked transfer.

The returned value is valid until the request is released, either though ReleaseRequest or your request handler returning. Do not store references to returned value. Make copies instead.

#### func (*ResponseHeader) Trailers ¶ added in v1.63.0

```
func (h *ResponseHeader) Trailers() iter.Seq[[]byte]
```

Trailers returns an iterator over trailers in h.

The value of trailer may invalid outside the iteration loop.

#### func (*ResponseHeader) VisitAll deprecated

```
func (h *ResponseHeader) VisitAll(f func(key, value []byte))
```

VisitAll calls f for each header.

f must not retain references to key and/or value after returning. Copy key and/or value contents before returning if you need retaining them.

Deprecated: Use All instead.

#### func (*ResponseHeader) VisitAllCookie deprecated

```
func (h *ResponseHeader) VisitAllCookie(f func(key, value []byte))
```

VisitAllCookie calls f for each response cookie.

Cookie name is passed in key and the whole Set-Cookie header value is passed in value on each f invocation. Value may be parsed with Cookie.ParseBytes().

f must not retain references to key and/or value after returning.

Deprecated: Use Cookies instead.

#### func (*ResponseHeader) VisitAllTrailer deprecated added in v1.32.0

```
func (h *ResponseHeader) VisitAllTrailer(f func(value []byte))
```

VisitAllTrailer calls f for each response Trailer.

f must not retain references to value after returning.

Deprecated: Use Trailers instead.

#### func (*ResponseHeader) Write

```
func (h *ResponseHeader) Write(w *bufio.Writer) error
```

Write writes response header to w.

#### func (*ResponseHeader) WriteTo

```
func (h *ResponseHeader) WriteTo(w io.Writer) (int64, error)
```

WriteTo writes response header to w.

WriteTo implements io.WriterTo interface.

#### type RetryIfErrFunc ¶ added in v1.56.0

```
type RetryIfErrFunc func(request *Request, attempts int, err error) (resetTimeout bool, retry bool)
```

RetryIfErrFunc defines an interface used for implementing the following functionality: When the client encounters an error during a request, the behavior—whether to retry and whether to reset the request timeout—should be determined based on the return value of this interface.

attempt indicates which attempt the current retry is due to a failure of. The first request counts as the first attempt.

err represents the error encountered while attempting the `attempts`-th request.

resetTimeout indicates whether to reuse the `Request`'s timeout as the timeout interval, rather than using the timeout after subtracting the time spent on previous failed requests. This return value is meaningful only when you use `Request.SetTimeout`, `DoTimeout`, or `DoDeadline`.

retry indicates whether to retry the current request. If it is false, the request function will immediately return with the `err`.

#### type RetryIfErrUpstreamFunc ¶ added in v1.71.0

```
type RetryIfErrUpstreamFunc func(request *Request, attempts int, err error, upstream string) (resetTimeout bool, retry bool)
```

RetryIfErrUpstreamFunc works just like a RetryIfErrFunc and also provides information about which upstream caused the error, if known.

Upstream information is a <host>:<port> format.

#### type RetryIfFunc ¶ added in v1.14.0

```
type RetryIfFunc func(request *Request) bool
```

RetryIfFunc defines the signature of the retry if function. Request argument passed to RetryIfFunc, if there are any request errors.

#### type RoundTripper ¶ added in v1.49.0

```
type RoundTripper interface {
	RoundTrip(hc *HostClient, req *Request, resp *Response) (retry bool, err error)
}
```

RoundTripper wraps every request/response.

```
var DefaultTransport RoundTripper = &transport{}
```

#### type ServeHandler ¶ added in v1.1.0

```
type ServeHandler func(c net.Conn) error
```

ServeHandler must process tls.Config.NextProto negotiated requests.

#### type Server

```
type Server struct {

	
	
	
	Logger Logger

	
	
	
	
	Handler RequestHandler

	
	
	
	
	
	
	
	
	
	ErrorHandler func(ctx *RequestCtx, err error)

	
	
	
	HeaderReceived func(header *RequestHeader) RequestConfig

	
	
	
	
	
	
	
	
	
	ContinueHandler func(header *RequestHeader) bool

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	ExpectHandler func(ctx *RequestCtx) int

	
	
	
	ConnState func(net.Conn, ConnState)

	
	
	
	
	
	
	
	
	
	TLSConfig *tls.Config

	
	
	
	
	
	
	
	
	FormValueFunc FormValueFunc

	
	
	
	Name string

	
	
	
	
	
	
	Concurrency int

	
	
	
	
	
	
	
	ReadBufferSize int

	
	
	
	WriteBufferSize int

	
	
	
	
	
	
	ReadTimeout time.Duration

	
	
	
	
	
	WriteTimeout time.Duration

	
	
	
	IdleTimeout time.Duration

	
	
	
	
	MaxConnsPerIP int

	
	
	
	
	
	
	MaxRequestsPerConn int

	
	
	
	MaxKeepaliveDuration time.Duration

	
	
	MaxIdleWorkerDuration time.Duration

	
	
	
	TCPKeepalivePeriod time.Duration

	
	
	
	
	
	MaxRequestBodySize int

	
	
	
	SleepWhenConcurrencyLimitsExceeded time.Duration

	
	
	
	
	
	
	DisableKeepalive bool

	
	
	
	
	
	TCPKeepalive bool

	
	
	
	
	
	
	
	
	ReduceMemoryUsage bool

	
	
	
	
	
	
	
	GetOnly bool

	
	
	
	
	
	
	DisablePreParseMultipartForm bool

	
	
	
	
	
	
	
	
	LogAllErrors bool

	
	
	
	
	
	
	SecureErrorLogMessage bool

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	DisableHeaderNamesNormalizing bool

	
	
	
	
	
	
	
	NoDefaultServerHeader bool

	
	
	
	
	
	NoDefaultDate bool

	
	
	
	
	
	NoDefaultContentType bool

	
	
	
	
	
	KeepHijackedConns bool

	
	CloseOnShutdown bool

	
	
	
	StreamRequestBody bool
	
}
```

Server implements HTTP server.

Default Server settings should satisfy the majority of Server users. Adjust Server settings only if you really understand the consequences.

It is forbidden copying Server instances. Create new Server instances instead.

It is safe to call Server methods from concurrently running goroutines.

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
	// This function will be called by the server for each incoming request.
	//
	// RequestCtx provides a lot of functionality related to http request
	// processing. See RequestCtx docs for details.
	requestHandler := func(ctx *fasthttp.RequestCtx) {
		fmt.Fprintf(ctx, "Hello, world! Requested path is %q", ctx.Path())
	}

	// Create custom server.
	s := &fasthttp.Server{
		Handler: requestHandler,

		// Every response will contain 'Server: My super server' header.
		Name: "My super server",

		// Other Server settings may be set here.
	}

	// Start the server listening for incoming requests on the given address.
	//
	// ListenAndServe returns only on error, so usually it blocks forever.
	if err := s.ListenAndServe("127.0.0.1:80"); err != nil {
		log.Fatalf("error in ListenAndServe: %v", err)
	}
}
```

```
Output:
```

#### func (*Server) AppendCert ¶ added in v1.0.0

```
func (s *Server) AppendCert(certFile, keyFile string) error
```

AppendCert appends certificate and keyfile to TLS Configuration.

This function allows programmer to handle multiple domains in one server structure. See examples/multidomain.

#### func (*Server) AppendCertEmbed ¶ added in v1.0.0

```
func (s *Server) AppendCertEmbed(certData, keyData []byte) error
```

AppendCertEmbed does the same as AppendCert but using in-memory data.

#### func (*Server) GetCurrentConcurrency ¶ added in v1.1.0

```
func (s *Server) GetCurrentConcurrency() uint32
```

GetCurrentConcurrency returns a number of currently served connections.

This function is intended be used by monitoring systems.

#### func (*Server) GetOpenConnectionsCount ¶ added in v1.1.0

```
func (s *Server) GetOpenConnectionsCount() int32
```

GetOpenConnectionsCount returns a number of opened connections.

This function is intended be used by monitoring systems.

#### func (*Server) GetRejectedConnectionsCount ¶ added in v1.52.0

```
func (s *Server) GetRejectedConnectionsCount() uint32
```

GetRejectedConnectionsCount returns a number of rejected connections.

This function is intended be used by monitoring systems.

#### func (*Server) ListenAndServe

```
func (s *Server) ListenAndServe(addr string) error
```

ListenAndServe serves HTTP requests from the given TCP4 addr.

Pass custom listener to Serve if you need listening on non-TCP4 media such as IPv6.

Accepted connections are configured to enable TCP keep-alives.

#### func (*Server) ListenAndServeTLS

```
func (s *Server) ListenAndServeTLS(addr, certFile, keyFile string) error
```

ListenAndServeTLS serves HTTPS requests from the given TCP4 addr.

certFile and keyFile are paths to TLS certificate and key files.

Pass custom listener to Serve if you need listening on non-TCP4 media such as IPv6.

If the certFile or keyFile has not been provided to the server structure, the function will use the previously added TLS configuration.

Accepted connections are configured to enable TCP keep-alives.

#### func (*Server) ListenAndServeTLSEmbed

```
func (s *Server) ListenAndServeTLSEmbed(addr string, certData, keyData []byte) error
```

ListenAndServeTLSEmbed serves HTTPS requests from the given TCP4 addr.

certData and keyData must contain valid TLS certificate and key data.

Pass custom listener to Serve if you need listening on arbitrary media such as IPv6.

If the certFile or keyFile has not been provided the server structure, the function will use previously added TLS configuration.

Accepted connections are configured to enable TCP keep-alives.

#### func (*Server) ListenAndServeUNIX

```
func (s *Server) ListenAndServeUNIX(addr string, mode os.FileMode) error
```

ListenAndServeUNIX serves HTTP requests from the given UNIX addr.

The function deletes existing file at addr before starting serving.

The server sets the given file mode for the UNIX addr.

#### func (*Server) NextProto ¶ added in v1.1.0

```
func (s *Server) NextProto(key string, nph ServeHandler)
```

NextProto adds nph to be processed when key is negotiated when TLS connection is established.

This function can only be called before the server is started.

#### func (*Server) Serve

```
func (s *Server) Serve(ln net.Listener) error
```

Serve serves incoming connections from the given listener.

Serve blocks until the given listener returns permanent error.

#### func (*Server) ServeConn

```
func (s *Server) ServeConn(c net.Conn) error
```

ServeConn serves HTTP requests from the given connection.

ServeConn returns nil if all requests from the c are successfully served. It returns non-nil error otherwise.

Connection c must immediately propagate all the data passed to Write() to the client. Otherwise requests' processing may hang.

ServeConn closes c before returning.

#### func (*Server) ServeTLS

```
func (s *Server) ServeTLS(ln net.Listener, certFile, keyFile string) error
```

ServeTLS serves HTTPS requests from the given listener.

certFile and keyFile are paths to TLS certificate and key files.

If the certFile or keyFile has not been provided the server structure, the function will use previously added TLS configuration.

#### func (*Server) ServeTLSEmbed

```
func (s *Server) ServeTLSEmbed(ln net.Listener, certData, keyData []byte) error
```

ServeTLSEmbed serves HTTPS requests from the given listener.

certData and keyData must contain valid TLS certificate and key data.

If the certFile or keyFile has not been provided the server structure, the function will use previously added TLS configuration.

#### func (*Server) Shutdown ¶ added in v1.0.0

```
func (s *Server) Shutdown() error
```

Shutdown gracefully shuts down the server without interrupting any active connections. Shutdown works by first closing all open listeners and then waiting indefinitely for all connections to return to idle and then shut down.

When Shutdown is called, Serve, ListenAndServe, and ListenAndServeTLS immediately return nil. Make sure the program doesn't exit and waits instead for Shutdown to return.

Shutdown does not close keepalive connections so it's recommended to set ReadTimeout and IdleTimeout to something else than 0.

#### func (*Server) ShutdownWithContext ¶ added in v1.42.0

```
func (s *Server) ShutdownWithContext(ctx context.Context) (err error)
```

ShutdownWithContext gracefully shuts down the server without interrupting any active connections. ShutdownWithContext works by first closing all open listeners and then waiting for all connections to return to idle or context timeout and then shut down.

When ShutdownWithContext is called, Serve, ListenAndServe, and ListenAndServeTLS immediately return nil. Make sure the program doesn't exit and waits instead for Shutdown to return.

ShutdownWithContext does not close keepalive connections so it's recommended to set ReadTimeout and IdleTimeout to something else than 0.

When ShutdownWithContext returns errors, any operation to the Server is unavailable.

#### type StreamWriter

```
type StreamWriter func(w *bufio.Writer)
```

StreamWriter must write data to w.

Usually StreamWriter writes data to w in a loop (aka 'data streaming').

StreamWriter must return immediately if w returns error.

Since the written data is buffered, do not forget calling w.Flush when the data must be propagated to reader.

#### type TCPDialer ¶ added in v1.2.0

```
type TCPDialer struct {
	
	
	
	
	
	
	
	
	
	
	
	Resolver Resolver

	
	
	
	LocalAddr *net.TCPAddr

	
	
	
	
	
	
	Concurrency int

	
	DNSCacheDuration time.Duration

	
	DisableDNSResolution bool
	
}
```

TCPDialer contains options to control a group of Dial calls.

#### func (*TCPDialer) Dial ¶ added in v1.2.0

```
func (d *TCPDialer) Dial(addr string) (net.Conn, error)
```

Dial dials the given TCP addr using tcp4.

This function has the following additional features comparing to net.Dial:

- It reduces load on DNS resolver by caching resolved TCP addressed for DNSCacheDuration.
- It dials all the resolved TCP addresses in round-robin manner until connection is established. This may be useful if certain addresses are temporarily unreachable.
- It returns ErrDialTimeout if connection cannot be established during DefaultDialTimeout seconds. Use DialTimeout for customizing dial timeout.

This dialer is intended for custom code wrapping before passing to Client.Dial or HostClient.Dial.

For instance, per-host counters and/or limits may be implemented by such wrappers.

The addr passed to the function must contain port. Example addr values:

- foobar.baz:443
- foo.bar:80
- aaa.com:8080

#### func (*TCPDialer) DialDualStack ¶ added in v1.2.0

```
func (d *TCPDialer) DialDualStack(addr string) (net.Conn, error)
```

DialDualStack dials the given TCP addr using both tcp4 and tcp6.

This function has the following additional features comparing to net.Dial:

- It reduces load on DNS resolver by caching resolved TCP addressed for DNSCacheDuration.
- It dials all the resolved TCP addresses in round-robin manner until connection is established. This may be useful if certain addresses are temporarily unreachable.
- It returns ErrDialTimeout if connection cannot be established during DefaultDialTimeout seconds. Use DialDualStackTimeout for custom dial timeout.

This dialer is intended for custom code wrapping before passing to Client.Dial or HostClient.Dial.

For instance, per-host counters and/or limits may be implemented by such wrappers.

The addr passed to the function must contain port. Example addr values:

- foobar.baz:443
- foo.bar:80
- aaa.com:8080

#### func (*TCPDialer) DialDualStackTimeout ¶ added in v1.2.0

```
func (d *TCPDialer) DialDualStackTimeout(addr string, timeout time.Duration) (net.Conn, error)
```

DialDualStackTimeout dials the given TCP addr using both tcp4 and tcp6 using the given timeout.

This function has the following additional features comparing to net.Dial:

- It reduces load on DNS resolver by caching resolved TCP addressed for DNSCacheDuration.
- It dials all the resolved TCP addresses in round-robin manner until connection is established. This may be useful if certain addresses are temporarily unreachable.

This dialer is intended for custom code wrapping before passing to Client.DialTimeout or HostClient.DialTimeout.

For instance, per-host counters and/or limits may be implemented by such wrappers.

The addr passed to the function must contain port. Example addr values:

- foobar.baz:443
- foo.bar:80
- aaa.com:8080

#### func (*TCPDialer) DialTimeout ¶ added in v1.2.0

```
func (d *TCPDialer) DialTimeout(addr string, timeout time.Duration) (net.Conn, error)
```

DialTimeout dials the given TCP addr using tcp4 using the given timeout.

This function has the following additional features comparing to net.Dial:

- It reduces load on DNS resolver by caching resolved TCP addressed for DNSCacheDuration.
- It dials all the resolved TCP addresses in round-robin manner until connection is established. This may be useful if certain addresses are temporarily unreachable.

This dialer is intended for custom code wrapping before passing to Client.DialTimeout or HostClient.DialTimeout.

For instance, per-host counters and/or limits may be implemented by such wrappers.

The addr passed to the function must contain port. Example addr values:

- foobar.baz:443
- foo.bar:80
- aaa.com:8080

#### func (*TCPDialer) FlushDNSCache ¶ added in v1.67.0

```
func (d *TCPDialer) FlushDNSCache()
```

FlushDNSCache clears all cached DNS entries, forcing fresh DNS lookups on subsequent dials. This is useful when you want to ensure fresh DNS resolution, for example after network changes.

#### type URI

```
type URI struct {

	
	
	
	
	
	
	
	DisablePathNormalizing bool
	
}
```

URI represents URI :) .

It is forbidden copying URI instances. Create new instance and use CopyTo instead.

URI instance MUST NOT be used from concurrently running goroutines.

#### func AcquireURI

```
func AcquireURI() *URI
```

AcquireURI returns an empty URI instance from the pool.

Release the URI with ReleaseURI after the URI is no longer needed. This allows reducing GC load.

#### func (*URI) AppendBytes

```
func (u *URI) AppendBytes(dst []byte) []byte
```

AppendBytes appends full uri to dst and returns the extended dst.

#### func (*URI) CopyTo

```
func (u *URI) CopyTo(dst *URI)
```

CopyTo copies uri contents to dst.

#### func (*URI) FullURI

```
func (u *URI) FullURI() []byte
```

FullURI returns full uri in the form {Scheme}://{Host}{RequestURI}#{Hash}.

The returned bytes are valid until the next URI method call.

#### func (*URI) Hash

```
func (u *URI) Hash() []byte
```

Hash returns URI hash, i.e. qwe of http://aaa.com/foo/bar?baz=123#qwe .

The returned bytes are valid until the next URI method call.

#### func (*URI) Host

```
func (u *URI) Host() []byte
```

Host returns host part, i.e. aaa.com of http://aaa.com/foo/bar?baz=123#qwe .

Host is always lowercased.

The returned bytes are valid until the next URI method call.

#### func (*URI) LastPathSegment

```
func (u *URI) LastPathSegment() []byte
```

LastPathSegment returns the last part of uri path after '/'.

Examples:

- For /foo/bar/baz.html path returns baz.html.
- For /foo/bar/ returns empty byte slice.
- For /foobar.js returns foobar.js.

The returned bytes are valid until the next URI method call.

#### func (*URI) Parse

```
func (u *URI) Parse(host, uri []byte) error
```

Parse initializes URI from the given host and uri.

host may be nil. In this case uri must contain fully qualified uri, i.e. with scheme and host. http is assumed if scheme is omitted.

uri may contain e.g. RequestURI without scheme and host if host is non-empty.

#### func (*URI) Password ¶ added in v1.5.0

```
func (u *URI) Password() []byte
```

Password returns URI password.

The returned bytes are valid until the next URI method call.

#### func (*URI) Path

```
func (u *URI) Path() []byte
```

Path returns URI path, i.e. /foo/bar of http://aaa.com/foo/bar?baz=123#qwe .

The returned path is always urldecoded and normalized, i.e. '//f%20obar/baz/../zzz' becomes '/f obar/zzz'.

The returned bytes are valid until the next URI method call.

#### func (*URI) PathOriginal

```
func (u *URI) PathOriginal() []byte
```

PathOriginal returns the original path from requestURI passed to URI.Parse().

The returned bytes are valid until the next URI method call.

#### func (*URI) QueryArgs

```
func (u *URI) QueryArgs() *Args
```

QueryArgs returns query args.

The returned args are valid until the next URI method call.

#### func (*URI) QueryString

```
func (u *URI) QueryString() []byte
```

QueryString returns URI query string, i.e. baz=123 of http://aaa.com/foo/bar?baz=123#qwe .

The returned bytes are valid until the next URI method call.

#### func (*URI) RequestURI

```
func (u *URI) RequestURI() []byte
```

RequestURI returns RequestURI - i.e. URI without Scheme and Host.

#### func (*URI) Reset

```
func (u *URI) Reset()
```

Reset clears uri.

#### func (*URI) Scheme

```
func (u *URI) Scheme() []byte
```

Scheme returns URI scheme, i.e. http of http://aaa.com/foo/bar?baz=123#qwe .

Returned scheme is always lowercased.

The returned bytes are valid until the next URI method call.

#### func (*URI) SetHash

```
func (u *URI) SetHash(hash string)
```

SetHash sets URI hash.

#### func (*URI) SetHashBytes

```
func (u *URI) SetHashBytes(hash []byte)
```

SetHashBytes sets URI hash.

#### func (*URI) SetHost

```
func (u *URI) SetHost(host string)
```

SetHost sets host for the uri.

#### func (*URI) SetHostBytes

```
func (u *URI) SetHostBytes(host []byte)
```

SetHostBytes sets host for the uri.

#### func (*URI) SetPassword ¶ added in v1.5.0

```
func (u *URI) SetPassword(password string)
```

SetPassword sets URI password.

#### func (*URI) SetPasswordBytes ¶ added in v1.5.0

```
func (u *URI) SetPasswordBytes(password []byte)
```

SetPasswordBytes sets URI password.

#### func (*URI) SetPath

```
func (u *URI) SetPath(path string)
```

SetPath sets URI path.

#### func (*URI) SetPathBytes

```
func (u *URI) SetPathBytes(path []byte)
```

SetPathBytes sets URI path.

#### func (*URI) SetQueryString

```
func (u *URI) SetQueryString(queryString string)
```

SetQueryString sets URI query string.

#### func (*URI) SetQueryStringBytes

```
func (u *URI) SetQueryStringBytes(queryString []byte)
```

SetQueryStringBytes sets URI query string.

#### func (*URI) SetScheme

```
func (u *URI) SetScheme(scheme string)
```

SetScheme sets URI scheme, i.e. http, https, ftp, etc.

#### func (*URI) SetSchemeBytes

```
func (u *URI) SetSchemeBytes(scheme []byte)
```

SetSchemeBytes sets URI scheme, i.e. http, https, ftp, etc.

#### func (*URI) SetUsername ¶ added in v1.5.0

```
func (u *URI) SetUsername(username string)
```

SetUsername sets URI username.

#### func (*URI) SetUsernameBytes ¶ added in v1.5.0

```
func (u *URI) SetUsernameBytes(username []byte)
```

SetUsernameBytes sets URI username.

#### func (*URI) String

```
func (u *URI) String() string
```

String returns full uri.

#### func (*URI) Update

```
func (u *URI) Update(newURI string)
```

Update updates uri.

The following newURI types are accepted:

- Absolute, i.e. http://foobar.com/aaa/bb?cc . In this case the original uri is replaced by newURI.
- Absolute without scheme, i.e. //foobar.com/aaa/bb?cc. In this case the original scheme is preserved.
- Missing host, i.e. /aaa/bb?cc . In this case only RequestURI part of the original uri is replaced.
- Relative path, i.e. xx?yy=abc . In this case the original RequestURI is updated according to the new relative path.

#### func (*URI) UpdateBytes

```
func (u *URI) UpdateBytes(newURI []byte)
```

UpdateBytes updates uri.

The following newURI types are accepted:

- Absolute, i.e. http://foobar.com/aaa/bb?cc . In this case the original uri is replaced by newURI.
- Absolute without scheme, i.e. //foobar.com/aaa/bb?cc. In this case the original scheme is preserved.
- Missing host, i.e. /aaa/bb?cc . In this case only RequestURI part of the original uri is replaced.
- Relative path, i.e. xx?yy=abc . In this case the original RequestURI is updated according to the new relative path.

#### func (*URI) Username ¶ added in v1.5.0

```
func (u *URI) Username() []byte
```

Username returns URI username

The returned bytes are valid until the next URI method call.

#### func (*URI) WriteTo

```
func (u *URI) WriteTo(w io.Writer) (int64, error)
```

WriteTo writes full uri to w.

WriteTo implements io.WriterTo interface.


## Source Files

View all Source files

- args.go
- b2s.go
- brotli.go
- bytesconv.go
- bytesconv_64.go
- bytesconv_table.go
- client.go
- coarsetime.go
- compress.go
- cookie.go
- doc.go
- fs.go
- header.go
- headers.go
- headerscanner.go
- http.go
- ipv6.go
- lbclient.go
- methods.go
- nocopy.go
- peripconn.go
- round2_64.go
- s2b.go
- server.go
- status.go
- stream.go
- streaming.go
- strings.go
- tcpdialer.go
- timer.go
- tls.go
- uri.go
- uri_unix.go
- userdata.go
- workerpool.go
- zstd.go


## Directories

| Path | Synopsis |
|---|---|
| examples |   |
| client command |   |
| fileserver command Example static file server. | Example static file server. |
| helloworldserver command |   |
| host_client command |   |
| letsencrypt command |   |
| multidomain command |   |
| expvarhandler Package expvarhandler provides fasthttp-compatible request handler serving expvars. | Package expvarhandler provides fasthttp-compatible request handler serving expvars. |
| fasthttpadaptor Package fasthttpadaptor provides helper functions for converting net/http request handlers to fasthttp request handlers. | Package fasthttpadaptor provides helper functions for converting net/http request handlers to fasthttp request handlers. |
| fasthttpproxy Package fasthttpproxy provides SOCKS5 and HTTP proxy support for fasthttp. | Package fasthttpproxy provides SOCKS5 and HTTP proxy support for fasthttp. |
| fasthttputil Package fasthttputil provides utility functions for fasthttp. | Package fasthttputil provides utility functions for fasthttp. |
| pprofhandler Package pprofhandler provides a fasthttp handler similar to net/http/pprof. | Package pprofhandler provides a fasthttp handler similar to net/http/pprof. |
| prefork Package prefork provides a way to prefork a fasthttp server. | Package prefork provides a way to prefork a fasthttp server. |
| reuseport Package reuseport provides TCP net.Listener with SO_REUSEPORT support. | Package reuseport provides TCP net.Listener with SO_REUSEPORT support. |
| stackless Package stackless provides functionality that may save stack space for high number of concurrently running goroutines. | Package stackless provides functionality that may save stack space for high number of concurrently running goroutines. |
| tcplisten Package tcplisten provides customizable TCP net.Listener with various performance-related options: | Package tcplisten provides customizable TCP net.Listener with various performance-related options: |

Click to show internal directories.

Click to hide internal directories.
