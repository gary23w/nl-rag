---
title: "http package (part 3/3)"
source: https://pkg.go.dev/net/http
domain: golang
license: BSD-3-Clause
tags: golang, goroutine, go module, go stdlib
fetched: 2026-07-02
part: 3/3
---

# http package

To make a request with a specified context.Context, use NewRequestWithContext and DefaultClient.Do.

#### func ReadResponse

```
func ReadResponse(r *bufio.Reader, req *Request) (*Response, error)
```

ReadResponse reads and returns an HTTP response from r. The req parameter optionally specifies the Request that corresponds to this Response. If nil, a GET request is assumed. Clients must call resp.Body.Close when finished reading resp.Body. After that call, clients can inspect resp.Trailer to find key/value pairs included in the response trailer.

#### func (*Response) Cookies

```
func (r *Response) Cookies() []*Cookie
```

Cookies parses and returns the cookies set in the Set-Cookie headers.

#### func (*Response) Location

```
func (r *Response) Location() (*url.URL, error)
```

Location returns the URL of the response's "Location" header, if present. Relative redirects are resolved relative to Response.Request. ErrNoLocation is returned if no Location header is present.

#### func (*Response) ProtoAtLeast

```
func (r *Response) ProtoAtLeast(major, minor int) bool
```

ProtoAtLeast reports whether the HTTP protocol used in the response is at least major.minor.

#### func (*Response) Write

```
func (r *Response) Write(w io.Writer) error
```

Write writes r to w in the HTTP/1.x server response format, including the status line, headers, body, and optional trailer.

This method consults the following fields of the response r:

```
StatusCode
ProtoMajor
ProtoMinor
Request.Method
TransferEncoding
Trailer
Body
ContentLength
Header, values for non-canonical keys will have unpredictable behavior
```

The Response Body is closed after it is sent.

#### type ResponseController ¶ added in go1.20

```
type ResponseController struct {
	
}
```

A ResponseController is used by an HTTP handler to control the response.

A ResponseController may not be used after the Handler.ServeHTTP method has returned.

#### func NewResponseController ¶ added in go1.20

```
func NewResponseController(rw ResponseWriter) *ResponseController
```

NewResponseController creates a ResponseController for a request.

The ResponseWriter should be the original value passed to the Handler.ServeHTTP method, or have an Unwrap method returning the original ResponseWriter.

If the ResponseWriter implements any of the following methods, the ResponseController will call them as appropriate:

```
Flush()
FlushError() error // alternative Flush returning an error
Hijack() (net.Conn, *bufio.ReadWriter, error)
SetReadDeadline(deadline time.Time) error
SetWriteDeadline(deadline time.Time) error
EnableFullDuplex() error
```

If the ResponseWriter does not support a method, ResponseController returns an error matching ErrNotSupported.

#### func (*ResponseController) EnableFullDuplex ¶ added in go1.21.0

```
func (c *ResponseController) EnableFullDuplex() error
```

EnableFullDuplex indicates that the request handler will interleave reads from Request.Body with writes to the ResponseWriter.

For HTTP/1 requests, the Go HTTP server by default consumes any unread portion of the request body before beginning to write the response, preventing handlers from concurrently reading from the request and writing the response. Calling EnableFullDuplex disables this behavior and permits handlers to continue to read from the request while concurrently writing the response.

For HTTP/2 requests, the Go HTTP server always permits concurrent reads and responses.

#### func (*ResponseController) Flush ¶ added in go1.20

```
func (c *ResponseController) Flush() error
```

Flush flushes buffered data to the client.

#### func (*ResponseController) Hijack ¶ added in go1.20

```
func (c *ResponseController) Hijack() (net.Conn, *bufio.ReadWriter, error)
```

Hijack lets the caller take over the connection. See the Hijacker interface for details.

#### func (*ResponseController) SetReadDeadline ¶ added in go1.20

```
func (c *ResponseController) SetReadDeadline(deadline time.Time) error
```

SetReadDeadline sets the deadline for reading the entire request, including the body. Reads from the request body after the deadline has been exceeded will return an error. A zero value means no deadline.

Setting the read deadline after it has been exceeded will not extend it.

#### func (*ResponseController) SetWriteDeadline ¶ added in go1.20

```
func (c *ResponseController) SetWriteDeadline(deadline time.Time) error
```

SetWriteDeadline sets the deadline for writing the response. Writes to the response body after the deadline has been exceeded will not block, but may succeed if the data has been buffered. A zero value means no deadline.

Setting the write deadline after it has been exceeded will not extend it.

#### type ResponseWriter

```
type ResponseWriter interface {
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	Header() Header

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	Write([]byte) (int, error)

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	WriteHeader(statusCode int)
}
```

A ResponseWriter interface is used by an HTTP handler to construct an HTTP response.

A ResponseWriter may not be used after Handler.ServeHTTP has returned.

Example (Trailers)

¶

HTTP Trailers are a set of key/value pairs like headers that come after the HTTP response, instead of before.

```
package main

import (
	"io"
	"net/http"
)

func main() {
	mux := http.NewServeMux()
	mux.HandleFunc("/sendstrailers", func(w http.ResponseWriter, req *http.Request) {
		// Before any call to WriteHeader or Write, declare
		// the trailers you will set during the HTTP
		// response. These three headers are actually sent in
		// the trailer.
		w.Header().Set("Trailer", "AtEnd1, AtEnd2")
		w.Header().Add("Trailer", "AtEnd3")

		w.Header().Set("Content-Type", "text/plain; charset=utf-8") // normal header
		w.WriteHeader(http.StatusOK)

		w.Header().Set("AtEnd1", "value 1")
		io.WriteString(w, "This HTTP response has both headers before this text and trailers at the end.\n")
		w.Header().Set("AtEnd2", "value 2")
		w.Header().Set("AtEnd3", "value 3") // These will appear as trailers.
	})
}
```

```
Output:
```

#### type RoundTripper

```
type RoundTripper interface {
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	RoundTrip(*Request) (*Response, error)
}
```

RoundTripper is an interface representing the ability to execute a single HTTP transaction, obtaining the Response for a given Request.

A RoundTripper must be safe for concurrent use by multiple goroutines.

```
var DefaultTransport RoundTripper = &Transport{
	Proxy: ProxyFromEnvironment,
	DialContext: defaultTransportDialContext(&net.Dialer{
		Timeout:   30 * time.Second,
		KeepAlive: 30 * time.Second,
	}),
	ForceAttemptHTTP2:     true,
	MaxIdleConns:          100,
	IdleConnTimeout:       90 * time.Second,
	TLSHandshakeTimeout:   10 * time.Second,
	ExpectContinueTimeout: 1 * time.Second,
}
```

DefaultTransport is the default implementation of Transport and is used by DefaultClient. It establishes network connections as needed and caches them for reuse by subsequent calls. It uses HTTP proxies as directed by the environment variables HTTP_PROXY, HTTPS_PROXY and NO_PROXY (or the lowercase versions thereof).

#### func NewFileTransport

```
func NewFileTransport(fs FileSystem) RoundTripper
```

NewFileTransport returns a new RoundTripper, serving the provided FileSystem. The returned RoundTripper ignores the URL host in its incoming requests, as well as most other properties of the request.

The typical use case for NewFileTransport is to register the "file" protocol with a Transport, as in:

```
t := &http.Transport{}
t.RegisterProtocol("file", http.NewFileTransport(http.Dir("/")))
c := &http.Client{Transport: t}
res, err := c.Get("file:///etc/passwd")
...
```

#### func NewFileTransportFS ¶ added in go1.22.0

```
func NewFileTransportFS(fsys fs.FS) RoundTripper
```

NewFileTransportFS returns a new RoundTripper, serving the provided file system fsys. The returned RoundTripper ignores the URL host in its incoming requests, as well as most other properties of the request. The files provided by fsys must implement io.Seeker.

The typical use case for NewFileTransportFS is to register the "file" protocol with a Transport, as in:

```
fsys := os.DirFS("/")
t := &http.Transport{}
t.RegisterProtocol("file", http.NewFileTransportFS(fsys))
c := &http.Client{Transport: t}
res, err := c.Get("file:///etc/passwd")
...
```

#### type SameSite ¶ added in go1.11

```
type SameSite int
```

SameSite allows a server to define a cookie attribute making it impossible for the browser to send this cookie along with cross-site requests. The main goal is to mitigate the risk of cross-origin information leakage, and provide some protection against cross-site request forgery attacks.

See https://tools.ietf.org/html/draft-ietf-httpbis-cookie-same-site-00 for details.

```
const (
	SameSiteDefaultMode SameSite = iota + 1
	SameSiteLaxMode
	SameSiteStrictMode
	SameSiteNoneMode
)
```

#### type ServeMux

```
type ServeMux struct {
	
}
```

ServeMux is an HTTP request multiplexer. It matches the URL of each incoming request against a list of registered patterns and calls the handler for the pattern that most closely matches the URL.

#### Patterns

Patterns can match the method, host and path of a request. Some examples:

- "/index.html" matches the path "/index.html" for any host and method.
- "GET /static/" matches a GET request whose path begins with "/static/".
- "example.com/" matches any request to the host "example.com".
- "example.com/{$}" matches requests with host "example.com" and path "/".
- "/b/{bucket}/o/{objectname...}" matches paths whose first segment is "b" and whose third segment is "o". The name "bucket" denotes the second segment and "objectname" denotes the remainder of the path.

In general, a pattern looks like

```
[METHOD ][HOST]/[PATH]
```

All three parts are optional; "/" is a valid pattern. If METHOD is present, it must be followed by at least one space or tab.

Literal (that is, non-wildcard) parts of a pattern match the corresponding parts of a request case-sensitively.

A pattern with no method matches every method. A pattern with the method GET matches both GET and HEAD requests. Otherwise, the method must match exactly.

A pattern with no host matches every host. A pattern with a host matches URLs on that host only.

A path can include wildcard segments of the form {NAME} or {NAME...}. For example, "/b/{bucket}/o/{objectname...}". The wildcard name must be a valid Go identifier. Wildcards must be full path segments: they must be preceded by a slash and followed by either a slash or the end of the string. For example, "/b_{bucket}" is not a valid pattern.

Normally a wildcard matches only a single path segment, ending at the next literal slash (not %2F) in the request URL. But if the "..." is present, then the wildcard matches the remainder of the URL path, including slashes. (Therefore it is invalid for a "..." wildcard to appear anywhere but at the end of a pattern.) The match for a wildcard can be obtained by calling Request.PathValue with the wildcard's name. A trailing slash in a path acts as an anonymous "..." wildcard.

The special wildcard {$} matches only the end of the URL. For example, the pattern "/{$}" matches only the path "/", whereas the pattern "/" matches every path.

For matching, both pattern paths and incoming request paths are unescaped segment by segment. So, for example, the path "/a%2Fb/100%25" is treated as having two segments, "a/b" and "100%". The pattern "/a%2fb/" matches it, but the pattern "/a/b/" does not.

#### Precedence

If two or more patterns match a request, then the most specific pattern takes precedence. A pattern P1 is more specific than P2 if P1 matches a strict subset of P2’s requests; that is, if P2 matches all the requests of P1 and more. If neither is more specific, then the patterns conflict. There is one exception to this rule, for backwards compatibility: if two patterns would otherwise conflict and one has a host while the other does not, then the pattern with the host takes precedence. If a pattern passed to ServeMux.Handle or ServeMux.HandleFunc conflicts with another pattern that is already registered, those functions panic.

As an example of the general rule, "/images/thumbnails/" is more specific than "/images/", so both can be registered. The former matches paths beginning with "/images/thumbnails/" and the latter will match any other path in the "/images/" subtree.

As another example, consider the patterns "GET /" and "/index.html": both match a GET request for "/index.html", but the former pattern matches all other GET and HEAD requests, while the latter matches any request for "/index.html" that uses a different method. The patterns conflict.

#### Trailing-slash redirection

Consider a ServeMux with a handler for a subtree, registered using a trailing slash or "..." wildcard. If the ServeMux receives a request for the subtree root without a trailing slash, it redirects the request by adding the trailing slash. This behavior can be overridden with a separate registration for the path without the trailing slash or "..." wildcard. For example, registering "/images/" causes ServeMux to redirect a request for "/images" to "/images/", unless "/images" has been registered separately.

#### Request sanitizing

ServeMux also takes care of sanitizing the URL request path and the Host header, stripping the port number and redirecting any request containing . or .. segments or repeated slashes to an equivalent, cleaner URL. Escaped path elements such as "%2e" for "." and "%2f" for "/" are preserved and aren't considered separators for request routing.

#### Compatibility

The pattern syntax and matching behavior of ServeMux changed significantly in Go 1.22. To restore the old behavior, set the GODEBUG environment variable to "httpmuxgo121=1". This setting is read once, at program startup; changes during execution will be ignored.

The backwards-incompatible changes include:

- Wildcards are just ordinary literal path segments in 1.21. For example, the pattern "/{x}" will match only that path in 1.21, but will match any one-segment path in 1.22.
- In 1.21, no pattern was rejected, unless it was empty or conflicted with an existing pattern. In 1.22, syntactically invalid patterns will cause ServeMux.Handle and ServeMux.HandleFunc to panic. For example, in 1.21, the patterns "/{" and "/a{x}" match themselves, but in 1.22 they are invalid and will cause a panic when registered.
- In 1.22, each segment of a pattern is unescaped; this was not done in 1.21. For example, in 1.22 the pattern "/%61" matches the path "/a" ("%61" being the URL escape sequence for "a"), but in 1.21 it would match only the path "/%2561" (where "%25" is the escape for the percent sign).
- When matching patterns to paths, in 1.22 each segment of the path is unescaped; in 1.21, the entire path is unescaped. This change mostly affects how paths with %2F escapes adjacent to slashes are treated. See https://go.dev/issue/21955 for details.

#### func NewServeMux

```
func NewServeMux() *ServeMux
```

NewServeMux allocates and returns a new ServeMux.

#### func (*ServeMux) Handle

```
func (mux *ServeMux) Handle(pattern string, handler Handler)
```

Handle registers the handler for the given pattern. If the given pattern conflicts with one that is already registered or if the pattern is invalid, Handle panics.

See ServeMux for details on valid patterns and conflict rules.

Example

¶

```
package main

import (
	"fmt"
	"net/http"
)

type apiHandler struct{}

func (apiHandler) ServeHTTP(http.ResponseWriter, *http.Request) {}

func main() {
	mux := http.NewServeMux()
	mux.Handle("/api/", apiHandler{})
	mux.HandleFunc("/", func(w http.ResponseWriter, req *http.Request) {
		// The "/" pattern matches everything, so we need to check
		// that we're at the root here.
		if req.URL.Path != "/" {
			http.NotFound(w, req)
			return
		}
		fmt.Fprintf(w, "Welcome to the home page!")
	})
}
```

```
Output:
```

#### func (*ServeMux) HandleFunc

```
func (mux *ServeMux) HandleFunc(pattern string, handler func(ResponseWriter, *Request))
```

HandleFunc registers the handler function for the given pattern. If the given pattern conflicts with one that is already registered or if the pattern is invalid, HandleFunc panics.

See ServeMux for details on valid patterns and conflict rules.

#### func (*ServeMux) Handler ¶ added in go1.1

```
func (mux *ServeMux) Handler(r *Request) (h Handler, pattern string)
```

Handler returns the handler to use for the given request, consulting r.Method, r.Host, and r.URL.Path. It always returns a non-nil handler. If the path is not in its canonical form, the handler will be an internally-generated handler that redirects to the canonical path. If the host contains a port, it is ignored when matching handlers.

The path and host are used unchanged for CONNECT requests.

Handler also returns the registered pattern that matches the request or, in the case of internally-generated redirects, the path that will match after following the redirect.

If there is no registered handler that applies to the request, Handler returns a “page not found” or “method not supported” handler and an empty pattern.

Handler does not modify its argument. In particular, it does not populate named path wildcards, so r.PathValue will always return the empty string.

#### func (*ServeMux) ServeHTTP

```
func (mux *ServeMux) ServeHTTP(w ResponseWriter, r *Request)
```

ServeHTTP dispatches the request to the handler whose pattern most closely matches the request URL.

#### type Server

```
type Server struct {
	
	
	
	
	Addr string

	Handler Handler 

	
	
	DisableGeneralOptionsHandler bool

	
	
	
	
	
	
	
	TLSConfig *tls.Config

	
	
	
	
	
	
	
	
	ReadTimeout time.Duration

	
	
	
	
	
	
	ReadHeaderTimeout time.Duration

	
	
	
	
	
	WriteTimeout time.Duration

	
	
	
	
	IdleTimeout time.Duration

	
	
	
	
	
	MaxHeaderBytes int

	
	
	
	
	
	
	
	
	
	
	
	
	TLSNextProto map[string]func(*Server, *tls.Conn, Handler)

	
	
	
	ConnState func(net.Conn, ConnState)

	
	
	
	
	ErrorLog *log.Logger

	
	
	
	
	
	
	BaseContext func(net.Listener) context.Context

	
	
	
	
	ConnContext func(ctx context.Context, c net.Conn) context.Context

	
	HTTP2 *HTTP2Config

	
	
	
	
	
	
	
	
	
	Protocols *Protocols
	
}
```

A Server defines parameters for running an HTTP server. The zero value for Server is a valid configuration.

#### func (*Server) Close ¶ added in go1.8

```
func (s *Server) Close() error
```

Close immediately closes all active net.Listeners and any connections in state StateNew, StateActive, or StateIdle. For a graceful shutdown, use Server.Shutdown.

Close does not attempt to close (and does not even know about) any hijacked connections, such as WebSockets.

Close returns any error returned from closing the Server's underlying Listener(s).

#### func (*Server) ListenAndServe

```
func (s *Server) ListenAndServe() error
```

ListenAndServe listens on the TCP network address s.Addr and then calls Serve to handle requests on incoming connections. Accepted connections are configured to enable TCP keep-alives.

If s.Addr is blank, ":http" is used.

ListenAndServe always returns a non-nil error. After Server.Shutdown or Server.Close, the returned error is ErrServerClosed.

#### func (*Server) ListenAndServeTLS

```
func (s *Server) ListenAndServeTLS(certFile, keyFile string) error
```

ListenAndServeTLS listens on the TCP network address s.Addr and then calls ServeTLS to handle requests on incoming TLS connections. Accepted connections are configured to enable TCP keep-alives.

Filenames containing a certificate and matching private key for the server must be provided if neither the Server's TLSConfig.Certificates nor TLSConfig.GetCertificate are populated. If the certificate is signed by a certificate authority, the certFile should be the concatenation of the server's certificate, any intermediates, and the CA's certificate.

If s.Addr is blank, ":https" is used.

ListenAndServeTLS always returns a non-nil error. After Server.Shutdown or Server.Close, the returned error is ErrServerClosed.

#### func (*Server) RegisterOnShutdown ¶ added in go1.9

```
func (s *Server) RegisterOnShutdown(f func())
```

RegisterOnShutdown registers a function to call on Server.Shutdown. This can be used to gracefully shutdown connections that have undergone ALPN protocol upgrade or that have been hijacked. This function should start protocol-specific graceful shutdown, but should not wait for shutdown to complete.

#### func (*Server) Serve

```
func (s *Server) Serve(l net.Listener) error
```

Serve accepts incoming connections on the Listener l, creating a new service goroutine for each. The service goroutines read requests and then call s.Handler to reply to them.

HTTP/2 support is only enabled if the Listener returns *tls.Conn connections and they were configured with "h2" in the TLS Config.NextProtos.

Serve always returns a non-nil error and closes l. After Server.Shutdown or Server.Close, the returned error is ErrServerClosed.

#### func (*Server) ServeTLS ¶ added in go1.9

```
func (s *Server) ServeTLS(l net.Listener, certFile, keyFile string) error
```

ServeTLS accepts incoming connections on the Listener l, creating a new service goroutine for each. The service goroutines perform TLS setup and then read requests, calling s.Handler to reply to them.

Files containing a certificate and matching private key for the server must be provided if neither the Server's TLSConfig.Certificates, TLSConfig.GetCertificate nor config.GetConfigForClient are populated. If the certificate is signed by a certificate authority, the certFile should be the concatenation of the server's certificate, any intermediates, and the CA's certificate.

ServeTLS always returns a non-nil error. After Server.Shutdown or Server.Close, the returned error is ErrServerClosed.

#### func (*Server) SetKeepAlivesEnabled ¶ added in go1.3

```
func (s *Server) SetKeepAlivesEnabled(v bool)
```

SetKeepAlivesEnabled controls whether HTTP keep-alives are enabled. By default, keep-alives are always enabled. Only very resource-constrained environments or servers in the process of shutting down should disable them.

#### func (*Server) Shutdown ¶ added in go1.8

```
func (s *Server) Shutdown(ctx context.Context) error
```

Shutdown gracefully shuts down the server without interrupting any active connections. Shutdown works by first closing all open listeners, then closing all idle connections, and then waiting indefinitely for connections to return to idle and then shut down. If the provided context expires before the shutdown is complete, Shutdown returns the context's error, otherwise it returns any error returned from closing the Server's underlying Listener(s).

When Shutdown is called, Serve, ServeTLS, ListenAndServe, and ListenAndServeTLS immediately return ErrServerClosed. Make sure the program doesn't exit and waits instead for Shutdown to return.

Shutdown does not attempt to close nor wait for hijacked connections such as WebSockets. The caller of Shutdown should separately notify such long-lived connections of shutdown and wait for them to close, if desired. See Server.RegisterOnShutdown for a way to register shutdown notification functions.

Once Shutdown has been called on a server, it may not be reused; future calls to methods such as Serve will return ErrServerClosed.

Example

¶

```
package main

import (
	"context"
	"log"
	"net/http"
	"os"
	"os/signal"
)

func main() {
	var srv http.Server

	idleConnsClosed := make(chan struct{})
	go func() {
		sigint := make(chan os.Signal, 1)
		signal.Notify(sigint, os.Interrupt)
		<-sigint

		// We received an interrupt signal, shut down.
		if err := srv.Shutdown(context.Background()); err != nil {
			// Error from closing listeners, or context timeout:
			log.Printf("HTTP server Shutdown: %v", err)
		}
		close(idleConnsClosed)
	}()

	if err := srv.ListenAndServe(); err != http.ErrServerClosed {
		// Error starting or closing listener:
		log.Fatalf("HTTP server ListenAndServe: %v", err)
	}

	<-idleConnsClosed
}
```

```
Output:
```

#### type Transport

```
type Transport struct {

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	Proxy func(*Request) (*url.URL, error)

	
	
	
	OnProxyConnectResponse func(ctx context.Context, proxyURL *url.URL, connectReq *Request, connectRes *Response) error

	
	
	
	
	
	
	
	
	DialContext func(ctx context.Context, network, addr string) (net.Conn, error)

	
	
	
	
	
	
	
	
	
	
	Dial func(network, addr string) (net.Conn, error)

	
	
	
	
	
	
	
	
	
	
	DialTLSContext func(ctx context.Context, network, addr string) (net.Conn, error)

	
	
	
	
	
	
	DialTLS func(network, addr string) (net.Conn, error)

	
	
	
	
	TLSClientConfig *tls.Config

	
	
	TLSHandshakeTimeout time.Duration

	
	
	
	
	
	DisableKeepAlives bool

	
	
	
	
	
	
	
	
	DisableCompression bool

	
	
	MaxIdleConns int

	
	
	
	MaxIdleConnsPerHost int

	
	
	
	
	
	MaxConnsPerHost int

	
	
	
	
	IdleConnTimeout time.Duration

	
	
	
	
	ResponseHeaderTimeout time.Duration

	
	
	
	
	
	
	
	ExpectContinueTimeout time.Duration

	
	
	
	
	
	
	
	
	
	
	
	
	
	TLSNextProto map[string]func(authority string, c *tls.Conn) RoundTripper

	
	
	
	ProxyConnectHeader Header

	
	
	
	
	
	
	
	GetProxyConnectHeader func(ctx context.Context, proxyURL *url.URL, target string) (Header, error)

	
	
	
	
	
	MaxResponseHeaderBytes int64

	
	
	
	WriteBufferSize int

	
	
	
	ReadBufferSize int

	
	
	
	
	
	ForceAttemptHTTP2 bool

	
	HTTP2 *HTTP2Config

	
	
	
	
	
	
	
	
	Protocols *Protocols
	
}
```

Transport is an implementation of RoundTripper that supports HTTP, HTTPS, and HTTP proxies (for either HTTP or HTTPS with CONNECT).

By default, Transport caches connections for future re-use. This may leave many open connections when accessing many hosts. This behavior can be managed using Transport.CloseIdleConnections method and the Transport.MaxIdleConnsPerHost and Transport.DisableKeepAlives fields.

Transports should be reused instead of created as needed. Transports are safe for concurrent use by multiple goroutines.

A Transport is a low-level primitive for making HTTP and HTTPS requests. For high-level functionality, such as cookies and redirects, see Client.

Transport uses HTTP/1.1 for HTTP URLs and either HTTP/1.1 or HTTP/2 for HTTPS URLs, depending on whether the server supports HTTP/2, and how the Transport is configured. The DefaultTransport supports HTTP/2. To explicitly enable HTTP/2 on a transport, set Transport.Protocols.

Responses with status codes in the 1xx range are either handled automatically (100 expect-continue) or ignored. The one exception is HTTP status code 101 (Switching Protocols), which is considered a terminal status and returned by Transport.RoundTrip. To see the ignored 1xx responses, use the httptrace trace package's ClientTrace.Got1xxResponse.

Transport only retries a request upon encountering a network error if the connection has already been used successfully and if the request is idempotent and either has no body or has its Request.GetBody defined. HTTP requests are considered idempotent if they have HTTP methods GET, HEAD, OPTIONS, or TRACE; or if their Header map contains an "Idempotency-Key" or "X-Idempotency-Key" entry. If the idempotency key value is a zero-length slice, the request is treated as idempotent but the header is not sent on the wire.

#### func (*Transport) CancelRequest deprecated added in go1.1

```
func (t *Transport) CancelRequest(req *Request)
```

CancelRequest cancels an in-flight request by closing its connection. CancelRequest should only be called after Transport.RoundTrip has returned.

Deprecated: Use Request.WithContext to create a request with a cancelable context instead. CancelRequest cannot cancel HTTP/2 requests. This may become a no-op in a future release of Go.

#### func (*Transport) Clone ¶ added in go1.13

```
func (t *Transport) Clone() *Transport
```

Clone returns a deep copy of t's exported fields.

#### func (*Transport) CloseIdleConnections

```
func (t *Transport) CloseIdleConnections()
```

CloseIdleConnections closes any connections which were previously connected from previous requests but are now sitting idle in a "keep-alive" state. It does not interrupt any connections currently in use.

#### func (*Transport) NewClientConn ¶ added in go1.26.0

```
func (t *Transport) NewClientConn(ctx context.Context, scheme, address string) (*ClientConn, error)
```

NewClientConn creates a new client connection to the given address.

If scheme is "http", the connection is unencrypted. If scheme is "https", the connection uses TLS.

The protocol used for the new connection is determined by the scheme, Transport.Protocols configuration field, and protocols supported by the server. See Transport.Protocols for more details.

If Transport.Proxy is set and indicates that a request sent to the given address should use a proxy, the new connection uses that proxy.

NewClientConn always creates a new connection, even if the Transport has an existing cached connection to the given host.

The new connection is not added to the Transport's connection cache, and will not be used by Transport.RoundTrip. It does not count against the MaxIdleConns and MaxConnsPerHost limits.

The caller is responsible for closing the new connection.

#### func (*Transport) RegisterProtocol

```
func (t *Transport) RegisterProtocol(scheme string, rt RoundTripper)
```

RegisterProtocol registers a new protocol with scheme. The Transport will pass requests using the given scheme to rt. It is rt's responsibility to simulate HTTP request semantics.

RegisterProtocol can be used by other packages to provide implementations of protocol schemes like "ftp" or "file".

If rt.RoundTrip returns ErrSkipAltProtocol, the Transport will handle the Transport.RoundTrip itself for that one request, as if the protocol were not registered.

#### func (*Transport) RoundTrip

```
func (t *Transport) RoundTrip(req *Request) (*Response, error)
```

RoundTrip implements the RoundTripper interface.

For higher-level HTTP client support (such as handling of cookies and redirects), see Get, Post, and the Client type.

Like the RoundTripper interface, the error types returned by RoundTrip are unspecified.


## Source Files

View all Source files

- client.go
- clientconn.go
- clone.go
- cookie.go
- csrf.go
- doc.go
- filetransport.go
- fs.go
- h2_bundle.go
- h2_error.go
- header.go
- http.go
- jar.go
- mapping.go
- method.go
- pattern.go
- request.go
- response.go
- responsecontroller.go
- roundtrip.go
- routing_index.go
- routing_tree.go
- servemux121.go
- server.go
- sniff.go
- socks_bundle.go
- status.go
- transfer.go
- transport.go
- transport_default_other.go


## Directories

| Path | Synopsis |
|---|---|
| cgi Package cgi implements CGI (Common Gateway Interface) as specified in RFC 3875. | Package cgi implements CGI (Common Gateway Interface) as specified in RFC 3875. |
| cookiejar Package cookiejar implements an in-memory RFC 6265-compliant http.CookieJar. | Package cookiejar implements an in-memory RFC 6265-compliant http.CookieJar. |
| fcgi Package fcgi implements the FastCGI protocol. | Package fcgi implements the FastCGI protocol. |
| httptest Package httptest provides utilities for HTTP testing. | Package httptest provides utilities for HTTP testing. |
| httptrace Package httptrace provides mechanisms to trace the events within HTTP client requests. | Package httptrace provides mechanisms to trace the events within HTTP client requests. |
| httputil Package httputil provides HTTP utility functions, complementing the more common ones in the net/http package. | Package httputil provides HTTP utility functions, complementing the more common ones in the net/http package. |
| internal Package internal contains HTTP internals shared by net/http and net/http/httputil. | Package internal contains HTTP internals shared by net/http and net/http/httputil. |
| ascii |   |
| httpcommon |   |
| testcert Package testcert contains a test-only localhost certificate. | Package testcert contains a test-only localhost certificate. |
| pprof Package pprof serves via its HTTP server runtime profiling data in the format expected by the pprof visualization tool. | Package pprof serves via its HTTP server runtime profiling data in the format expected by the pprof visualization tool. |

Click to show internal directories.

Click to hide internal directories.
