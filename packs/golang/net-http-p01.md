---
title: "http package (part 1/3)"
source: https://pkg.go.dev/net/http
domain: golang
license: BSD-3-Clause
tags: golang, goroutine, go module, go stdlib
fetched: 2026-07-02
part: 1/3
---

# http

package

standard library

Version:

go1.26.4

Opens a new window with list of versions in this module.

Latest

Latest

This package is not in the latest version of its module.

Go to latest

Published: Jun 2, 2026

License:

BSD-3-Clause

Opens a new window with license information.

Imports:

48

Opens a new window with list of imports.

Imported by:

1,776,917

Opens a new window with list of known importers.

## Documentation

### Overview

Package http provides HTTP client and server implementations.

Get, Head, Post, and PostForm make HTTP (or HTTPS) requests:

```
resp, err := http.Get("http://example.com/")
...
resp, err := http.Post("http://example.com/upload", "image/jpeg", &buf)
...
resp, err := http.PostForm("http://example.com/form",
	url.Values{"key": {"Value"}, "id": {"123"}})
```

The caller must close the response body when finished with it:

```
resp, err := http.Get("http://example.com/")
if err != nil {
	// handle error
}
defer resp.Body.Close()
body, err := io.ReadAll(resp.Body)
// ...
```

#### Clients and Transports

For control over HTTP client headers, redirect policy, and other settings, create a Client:

```
client := &http.Client{
	CheckRedirect: redirectPolicyFunc,
}

resp, err := client.Get("http://example.com")
// ...

req, err := http.NewRequest("GET", "http://example.com", nil)
// ...
req.Header.Add("If-None-Match", `W/"wyzzy"`)
resp, err := client.Do(req)
// ...
```

For control over proxies, TLS configuration, keep-alives, compression, and other settings, create a Transport:

```
tr := &http.Transport{
	MaxIdleConns:       10,
	IdleConnTimeout:    30 * time.Second,
	DisableCompression: true,
}
client := &http.Client{Transport: tr}
resp, err := client.Get("https://example.com")
```

Clients and Transports are safe for concurrent use by multiple goroutines and for efficiency should only be created once and re-used.

#### Servers

ListenAndServe starts an HTTP server with a given address and handler. The handler is usually nil, which means to use DefaultServeMux. Handle and HandleFunc add handlers to DefaultServeMux:

```
http.Handle("/foo", fooHandler)

http.HandleFunc("/bar", func(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello, %q", html.EscapeString(r.URL.Path))
})

log.Fatal(http.ListenAndServe(":8080", nil))
```

More control over the server's behavior is available by creating a custom Server:

```
s := &http.Server{
	Addr:           ":8080",
	Handler:        myHandler,
	ReadTimeout:    10 * time.Second,
	WriteTimeout:   10 * time.Second,
	MaxHeaderBytes: 1 << 20,
}
log.Fatal(s.ListenAndServe())
```

#### HTTP/2

The http package has transparent support for the HTTP/2 protocol.

Server and DefaultTransport automatically enable HTTP/2 support when using HTTPS. Transport does not enable HTTP/2 by default.

To enable or disable support for HTTP/1, HTTP/2, and/or unencrypted HTTP/2, see the Server.Protocols and Transport.Protocols configuration fields.

To configure advanced HTTP/2 features, see the Server.HTTP2 and Transport.HTTP2 configuration fields.

Alternatively, the following GODEBUG settings are currently supported:

```
GODEBUG=http2client=0  # disable HTTP/2 client support
GODEBUG=http2server=0  # disable HTTP/2 server support
GODEBUG=http2debug=1   # enable verbose HTTP/2 debug logs
GODEBUG=http2debug=2   # ... even more verbose, with frame dumps
```

The "omithttp2" build tag may be used to disable the HTTP/2 implementation contained in the http package.

### Index

- Constants
- Variables
- func CanonicalHeaderKey(s string) string
- func DetectContentType(data []byte) string
- func Error(w ResponseWriter, error string, code int)
- func Handle(pattern string, handler Handler)
- func HandleFunc(pattern string, handler func(ResponseWriter, *Request))
- func ListenAndServe(addr string, handler Handler) error
- func ListenAndServeTLS(addr, certFile, keyFile string, handler Handler) error
- func MaxBytesReader(w ResponseWriter, r io.ReadCloser, n int64) io.ReadCloser
- func NotFound(w ResponseWriter, r *Request)
- func ParseHTTPVersion(vers string) (major, minor int, ok bool)
- func ParseTime(text string) (t time.Time, err error)
- func ProxyFromEnvironment(req *Request) (*url.URL, error)
- func ProxyURL(fixedURL *url.URL) func(*Request) (*url.URL, error)
- func Redirect(w ResponseWriter, r *Request, url string, code int)
- func Serve(l net.Listener, handler Handler) error
- func ServeContent(w ResponseWriter, req *Request, name string, modtime time.Time, ...)
- func ServeFile(w ResponseWriter, r *Request, name string)
- func ServeFileFS(w ResponseWriter, r *Request, fsys fs.FS, name string)
- func ServeTLS(l net.Listener, handler Handler, certFile, keyFile string) error
- func SetCookie(w ResponseWriter, cookie *Cookie)
- func StatusText(code int) string
- type Client
  - func (c *Client) CloseIdleConnections()
  - func (c *Client) Do(req *Request) (*Response, error)
  - func (c *Client) Get(url string) (resp *Response, err error)
  - func (c *Client) Head(url string) (resp *Response, err error)
  - func (c *Client) Post(url, contentType string, body io.Reader) (resp *Response, err error)
  - func (c *Client) PostForm(url string, data url.Values) (resp *Response, err error)
- type ClientConn
  - func (cc *ClientConn) Available() int
  - func (cc *ClientConn) Close() error
  - func (cc *ClientConn) Err() error
  - func (cc *ClientConn) InFlight() int
  - func (cc *ClientConn) Release()
  - func (cc *ClientConn) Reserve() error
  - func (cc *ClientConn) RoundTrip(req *Request) (*Response, error)
  - func (cc *ClientConn) SetStateHook(f func(*ClientConn))
- type CloseNotifierdeprecated
- type ConnState
  - func (c ConnState) String() string
- type Cookie
  - func ParseCookie(line string) ([]*Cookie, error)
  - func ParseSetCookie(line string) (*Cookie, error)
  - func (c *Cookie) String() string
  - func (c *Cookie) Valid() error
- type CookieJar
- type CrossOriginProtection
  - func NewCrossOriginProtection() *CrossOriginProtection
  - func (c *CrossOriginProtection) AddInsecureBypassPattern(pattern string)
  - func (c *CrossOriginProtection) AddTrustedOrigin(origin string) error
  - func (c *CrossOriginProtection) Check(req *Request) error
  - func (c *CrossOriginProtection) Handler(h Handler) Handler
  - func (c *CrossOriginProtection) SetDenyHandler(h Handler)
- type Dir
  - func (d Dir) Open(name string) (File, error)
- type File
- type FileSystem
  - func FS(fsys fs.FS) FileSystem
- type Flusher
- type HTTP2Config
- type Handler
  - func AllowQuerySemicolons(h Handler) Handler
  - func FileServer(root FileSystem) Handler
  - func FileServerFS(root fs.FS) Handler
  - func MaxBytesHandler(h Handler, n int64) Handler
  - func NotFoundHandler() Handler
  - func RedirectHandler(url string, code int) Handler
  - func StripPrefix(prefix string, h Handler) Handler
  - func TimeoutHandler(h Handler, dt time.Duration, msg string) Handler
- type HandlerFunc
  - func (f HandlerFunc) ServeHTTP(w ResponseWriter, r *Request)
- type Header
  - func (h Header) Add(key, value string)
  - func (h Header) Clone() Header
  - func (h Header) Del(key string)
  - func (h Header) Get(key string) string
  - func (h Header) Set(key, value string)
  - func (h Header) Values(key string) []string
  - func (h Header) Write(w io.Writer) error
  - func (h Header) WriteSubset(w io.Writer, exclude map[string]bool) error
- type Hijacker
- type MaxBytesError
  - func (e *MaxBytesError) Error() string
- type ProtocolErrordeprecated
  - func (pe *ProtocolError) Error() string
  - func (pe *ProtocolError) Is(err error) bool
- type Protocols
  - func (p Protocols) HTTP1() bool
  - func (p Protocols) HTTP2() bool
  - func (p *Protocols) SetHTTP1(ok bool)
  - func (p *Protocols) SetHTTP2(ok bool)
  - func (p *Protocols) SetUnencryptedHTTP2(ok bool)
  - func (p Protocols) String() string
  - func (p Protocols) UnencryptedHTTP2() bool
- type PushOptions
- type Pusher
- type Request
  - func NewRequest(method, url string, body io.Reader) (*Request, error)
  - func NewRequestWithContext(ctx context.Context, method, url string, body io.Reader) (*Request, error)
  - func ReadRequest(b *bufio.Reader) (*Request, error)
  - func (r *Request) AddCookie(c *Cookie)
  - func (r *Request) BasicAuth() (username, password string, ok bool)
  - func (r *Request) Clone(ctx context.Context) *Request
  - func (r *Request) Context() context.Context
  - func (r *Request) Cookie(name string) (*Cookie, error)
  - func (r *Request) Cookies() []*Cookie
  - func (r *Request) CookiesNamed(name string) []*Cookie
  - func (r *Request) FormFile(key string) (multipart.File, *multipart.FileHeader, error)
  - func (r *Request) FormValue(key string) string
  - func (r *Request) MultipartReader() (*multipart.Reader, error)
  - func (r *Request) ParseForm() error
  - func (r *Request) ParseMultipartForm(maxMemory int64) error
  - func (r *Request) PathValue(name string) string
  - func (r *Request) PostFormValue(key string) string
  - func (r *Request) ProtoAtLeast(major, minor int) bool
  - func (r *Request) Referer() string
  - func (r *Request) SetBasicAuth(username, password string)
  - func (r *Request) SetPathValue(name, value string)
  - func (r *Request) UserAgent() string
  - func (r *Request) WithContext(ctx context.Context) *Request
  - func (r *Request) Write(w io.Writer) error
  - func (r *Request) WriteProxy(w io.Writer) error
- type Response
  - func Get(url string) (resp *Response, err error)
  - func Head(url string) (resp *Response, err error)
  - func Post(url, contentType string, body io.Reader) (resp *Response, err error)
  - func PostForm(url string, data url.Values) (resp *Response, err error)
  - func ReadResponse(r *bufio.Reader, req *Request) (*Response, error)
  - func (r *Response) Cookies() []*Cookie
  - func (r *Response) Location() (*url.URL, error)
  - func (r *Response) ProtoAtLeast(major, minor int) bool
  - func (r *Response) Write(w io.Writer) error
- type ResponseController
  - func NewResponseController(rw ResponseWriter) *ResponseController
  - func (c *ResponseController) EnableFullDuplex() error
  - func (c *ResponseController) Flush() error
  - func (c *ResponseController) Hijack() (net.Conn, *bufio.ReadWriter, error)
  - func (c *ResponseController) SetReadDeadline(deadline time.Time) error
  - func (c *ResponseController) SetWriteDeadline(deadline time.Time) error
- type ResponseWriter
- type RoundTripper
  - func NewFileTransport(fs FileSystem) RoundTripper
  - func NewFileTransportFS(fsys fs.FS) RoundTripper
- type SameSite
- type ServeMux
  - func NewServeMux() *ServeMux
  - func (mux *ServeMux) Handle(pattern string, handler Handler)
  - func (mux *ServeMux) HandleFunc(pattern string, handler func(ResponseWriter, *Request))
  - func (mux *ServeMux) Handler(r *Request) (h Handler, pattern string)
  - func (mux *ServeMux) ServeHTTP(w ResponseWriter, r *Request)
- type Server
  - func (s *Server) Close() error
  - func (s *Server) ListenAndServe() error
  - func (s *Server) ListenAndServeTLS(certFile, keyFile string) error
  - func (s *Server) RegisterOnShutdown(f func())
  - func (s *Server) Serve(l net.Listener) error
  - func (s *Server) ServeTLS(l net.Listener, certFile, keyFile string) error
  - func (s *Server) SetKeepAlivesEnabled(v bool)
  - func (s *Server) Shutdown(ctx context.Context) error
- type Transport
  - func (t *Transport) CancelRequest(req *Request)deprecated
  - func (t *Transport) Clone() *Transport
  - func (t *Transport) CloseIdleConnections()
  - func (t *Transport) NewClientConn(ctx context.Context, scheme, address string) (*ClientConn, error)
  - func (t *Transport) RegisterProtocol(scheme string, rt RoundTripper)
  - func (t *Transport) RoundTrip(req *Request) (*Response, error)

### Examples

- CrossOriginProtection
- FileServer
- FileServer (DotFileHiding)
- FileServer (StripPrefix)
- Get
- Handle
- HandleFunc
- Hijacker
- ListenAndServe
- ListenAndServeTLS
- NotFoundHandler
- Protocols (Http1)
- Protocols (Http1or2)
- ResponseWriter (Trailers)
- ServeMux.Handle
- Server.Shutdown
- StripPrefix

### Constants

View Source

```
const (
	MethodGet     = "GET"
	MethodHead    = "HEAD"
	MethodPost    = "POST"
	MethodPut     = "PUT"
	MethodPatch   = "PATCH" 
	MethodDelete  = "DELETE"
	MethodConnect = "CONNECT"
	MethodOptions = "OPTIONS"
	MethodTrace   = "TRACE"
)
```

Common HTTP methods.

Unless otherwise noted, these are defined in RFC 7231 section 4.3.

View Source

```
const (
	StatusContinue           = 100 
	StatusSwitchingProtocols = 101 
	StatusProcessing         = 102 
	StatusEarlyHints         = 103 

	StatusOK                   = 200 
	StatusCreated              = 201 
	StatusAccepted             = 202 
	StatusNonAuthoritativeInfo = 203 
	StatusNoContent            = 204 
	StatusResetContent         = 205 
	StatusPartialContent       = 206 
	StatusMultiStatus          = 207 
	StatusAlreadyReported      = 208 
	StatusIMUsed               = 226 

	StatusMultipleChoices  = 300 
	StatusMovedPermanently = 301 
	StatusFound            = 302 
	StatusSeeOther         = 303 
	StatusNotModified      = 304 
	StatusUseProxy         = 305 

	StatusTemporaryRedirect = 307 
	StatusPermanentRedirect = 308 

	StatusBadRequest                   = 400 
	StatusUnauthorized                 = 401 
	StatusPaymentRequired              = 402 
	StatusForbidden                    = 403 
	StatusNotFound                     = 404 
	StatusMethodNotAllowed             = 405 
	StatusNotAcceptable                = 406 
	StatusProxyAuthRequired            = 407 
	StatusRequestTimeout               = 408 
	StatusConflict                     = 409 
	StatusGone                         = 410 
	StatusLengthRequired               = 411 
	StatusPreconditionFailed           = 412 
	StatusRequestEntityTooLarge        = 413 
	StatusRequestURITooLong            = 414 
	StatusUnsupportedMediaType         = 415 
	StatusRequestedRangeNotSatisfiable = 416 
	StatusExpectationFailed            = 417 
	StatusTeapot                       = 418 
	StatusMisdirectedRequest           = 421 
	StatusUnprocessableEntity          = 422 
	StatusLocked                       = 423 
	StatusFailedDependency             = 424 
	StatusTooEarly                     = 425 
	StatusUpgradeRequired              = 426 
	StatusPreconditionRequired         = 428 
	StatusTooManyRequests              = 429 
	StatusRequestHeaderFieldsTooLarge  = 431 
	StatusUnavailableForLegalReasons   = 451 

	StatusInternalServerError           = 500 
	StatusNotImplemented                = 501 
	StatusBadGateway                    = 502 
	StatusServiceUnavailable            = 503 
	StatusGatewayTimeout                = 504 
	StatusHTTPVersionNotSupported       = 505 
	StatusVariantAlsoNegotiates         = 506 
	StatusInsufficientStorage           = 507 
	StatusLoopDetected                  = 508 
	StatusNotExtended                   = 510 
	StatusNetworkAuthenticationRequired = 511 
)
```

HTTP status codes as registered with IANA. See: https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml

View Source

```
const DefaultMaxHeaderBytes = 1 << 20 
```

DefaultMaxHeaderBytes is the maximum permitted size of the headers in an HTTP request. This can be overridden by setting Server.MaxHeaderBytes.

View Source

```
const DefaultMaxIdleConnsPerHost = 2
```

DefaultMaxIdleConnsPerHost is the default value of Transport's MaxIdleConnsPerHost.

View Source

```
const TimeFormat = "Mon, 02 Jan 2006 15:04:05 GMT"
```

TimeFormat is the time format to use when generating times in HTTP headers. It is like time.RFC1123 but hard-codes GMT as the time zone. The time being formatted must be in UTC for Format to generate the correct format.

For parsing this time format, see ParseTime.

View Source

```
const TrailerPrefix = "Trailer:"
```

TrailerPrefix is a magic prefix for ResponseWriter.Header map keys that, if present, signals that the map entry is actually for the response trailers, and not the response headers. The prefix is stripped after the ServeHTTP call finishes and the values are sent in the trailers.

This mechanism is intended only for trailers that are not known prior to the headers being written. If the set of trailers is fixed or known before the header is written, the normal Go trailers mechanism is preferred:

```
https://pkg.go.dev/net/http#ResponseWriter
https://pkg.go.dev/net/http#example-ResponseWriter-Trailers
```

### Variables

View Source

```
var (
	
	
	
	
	
	
	ErrNotSupported = &ProtocolError{"feature not supported"}

	
	
	
	ErrUnexpectedTrailer = &ProtocolError{"trailer header without chunked transfer encoding"}

	
	
	ErrMissingBoundary = &ProtocolError{"no multipart boundary param in Content-Type"}

	
	
	ErrNotMultipart = &ProtocolError{"request Content-Type isn't multipart/form-data"}

	
	
	
	ErrHeaderTooLong = &ProtocolError{"header too long"}

	
	
	
	ErrShortBody = &ProtocolError{"entity body too short"}

	
	
	
	ErrMissingContentLength = &ProtocolError{"missing ContentLength in HEAD response"}
)
```

View Source

```
var (
	
	
	
	ErrBodyNotAllowed = errors.New("http: request method or response status code does not allow body")

	
	
	
	
	
	ErrHijacked = errors.New("http: connection has been hijacked")

	
	
	
	
	ErrContentLength = errors.New("http: wrote more than the declared Content-Length")

	
	
	
	ErrWriteAfterFlush = errors.New("unused")
)
```

Errors used by the HTTP server.

View Source

```
var (
	
	
	
	
	ServerContextKey = &contextKey{"http-server"}

	
	
	
	
	LocalAddrContextKey = &contextKey{"local-addr"}
)
```

View Source

```
var DefaultClient = &Client{}
```

DefaultClient is the default Client and is used by Get, Head, and Post.

View Source

```
var DefaultServeMux = &defaultServeMux
```

DefaultServeMux is the default ServeMux used by Serve.

View Source

```
var ErrAbortHandler = errors.New("net/http: abort Handler")
```

ErrAbortHandler is a sentinel panic value to abort a handler. While any panic from ServeHTTP aborts the response to the client, panicking with ErrAbortHandler also suppresses logging of a stack trace to the server's error log.

View Source

```
var ErrBodyReadAfterClose = errors.New("http: invalid Read on closed Body")
```

ErrBodyReadAfterClose is returned when reading a Request or Response Body after the body has been closed. This typically happens when the body is read after an HTTP Handler calls WriteHeader or Write on its ResponseWriter.

View Source

```
var ErrHandlerTimeout = errors.New("http: Handler timeout")
```

ErrHandlerTimeout is returned on ResponseWriter Write calls in handlers which have timed out.

View Source

```
var ErrLineTooLong = internal.ErrLineTooLong
```

ErrLineTooLong is returned when reading request or response bodies with malformed chunked encoding.

View Source

```
var ErrMissingFile = errors.New("http: no such file")
```

ErrMissingFile is returned by FormFile when the provided file field name is either not present in the request or not a file field.

View Source

```
var ErrNoCookie = errors.New("http: named cookie not present")
```

ErrNoCookie is returned by Request's Cookie method when a cookie is not found.

View Source

```
var ErrNoLocation = errors.New("http: no Location header in response")
```

ErrNoLocation is returned by the Response.Location method when no Location header is present.

View Source

```
var ErrSchemeMismatch = errors.New("http: server gave HTTP response to HTTPS client")
```

ErrSchemeMismatch is returned when a server returns an HTTP response to an HTTPS client.

View Source

```
var ErrServerClosed = errors.New("http: Server closed")
```

ErrServerClosed is returned by the Server.Serve, ServeTLS, ListenAndServe, and ListenAndServeTLS methods after a call to Server.Shutdown or Server.Close.

View Source

```
var ErrSkipAltProtocol = errors.New("net/http: skip alternate protocol")
```

ErrSkipAltProtocol is a sentinel error value defined by Transport.RegisterProtocol.

View Source

```
var ErrUseLastResponse = errors.New("net/http: use last response")
```

ErrUseLastResponse can be returned by Client.CheckRedirect hooks to control how redirects are processed. If returned, the next request is not sent and the most recent response is returned with its body unclosed.

View Source

```
var NoBody = noBody{}
```

NoBody is an io.ReadCloser with no bytes. Read always returns EOF and Close always returns nil. It can be used in an outgoing client request to explicitly signal that a request has zero bytes. An alternative, however, is to simply set Request.Body to nil.

### Functions

#### func CanonicalHeaderKey

```
func CanonicalHeaderKey(s string) string
```

CanonicalHeaderKey returns the canonical format of the header key s. The canonicalization converts the first letter and any letter following a hyphen to upper case; the rest are converted to lowercase. For example, the canonical key for "accept-encoding" is "Accept-Encoding". If s contains a space or invalid header field bytes, it is returned without modifications.

#### func DetectContentType

```
func DetectContentType(data []byte) string
```

DetectContentType implements the algorithm described at https://mimesniff.spec.whatwg.org/ to determine the Content-Type of the given data. It considers at most the first 512 bytes of data. DetectContentType always returns a valid MIME type: if it cannot determine a more specific one, it returns "application/octet-stream".

#### func Error

```
func Error(w ResponseWriter, error string, code int)
```

Error replies to the request with the specified error message and HTTP code. It does not otherwise end the request; the caller should ensure no further writes are done to w. The error message should be plain text.

Error deletes the Content-Length header, sets Content-Type to “text/plain; charset=utf-8”, and sets X-Content-Type-Options to “nosniff”. This configures the header properly for the error message, in case the caller had set it up expecting a successful output.

#### func Handle

```
func Handle(pattern string, handler Handler)
```

Handle registers the handler for the given pattern in DefaultServeMux. The documentation for ServeMux explains how patterns are matched.

Example

¶

```
package main

import (
	"fmt"
	"log"
	"net/http"
	"sync"
)

type countHandler struct {
	mu sync.Mutex // guards n
	n  int
}

func (h *countHandler) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	h.mu.Lock()
	defer h.mu.Unlock()
	h.n++
	fmt.Fprintf(w, "count is %d\n", h.n)
}

func main() {
	http.Handle("/count", new(countHandler))
	log.Fatal(http.ListenAndServe(":8080", nil))
}
```

```
Output:
```

#### func HandleFunc

```
func HandleFunc(pattern string, handler func(ResponseWriter, *Request))
```

HandleFunc registers the handler function for the given pattern in DefaultServeMux. The documentation for ServeMux explains how patterns are matched.

Example

¶

```
package main

import (
	"io"
	"log"
	"net/http"
)

func main() {
	h1 := func(w http.ResponseWriter, _ *http.Request) {
		io.WriteString(w, "Hello from a HandleFunc #1!\n")
	}
	h2 := func(w http.ResponseWriter, _ *http.Request) {
		io.WriteString(w, "Hello from a HandleFunc #2!\n")
	}

	http.HandleFunc("/", h1)
	http.HandleFunc("/endpoint", h2)

	log.Fatal(http.ListenAndServe(":8080", nil))
}
```

```
Output:
```

#### func ListenAndServe

```
func ListenAndServe(addr string, handler Handler) error
```

ListenAndServe listens on the TCP network address addr and then calls Serve with handler to handle requests on incoming connections. Accepted connections are configured to enable TCP keep-alives.

The handler is typically nil, in which case DefaultServeMux is used.

ListenAndServe always returns a non-nil error.

Example

¶

```
package main

import (
	"io"
	"log"
	"net/http"
)

func main() {
	// Hello world, the web server

	helloHandler := func(w http.ResponseWriter, req *http.Request) {
		io.WriteString(w, "Hello, world!\n")
	}

	http.HandleFunc("/hello", helloHandler)
	log.Fatal(http.ListenAndServe(":8080", nil))
}
```

```
Output:
```

#### func ListenAndServeTLS

```
func ListenAndServeTLS(addr, certFile, keyFile string, handler Handler) error
```

ListenAndServeTLS acts identically to ListenAndServe, except that it expects HTTPS connections. Additionally, files containing a certificate and matching private key for the server must be provided. If the certificate is signed by a certificate authority, the certFile should be the concatenation of the server's certificate, any intermediates, and the CA's certificate.

Example

¶

```
package main

import (
	"io"
	"log"
	"net/http"
)

func main() {
	http.HandleFunc("/", func(w http.ResponseWriter, req *http.Request) {
		io.WriteString(w, "Hello, TLS!\n")
	})

	// One can use generate_cert.go in crypto/tls to generate cert.pem and key.pem.
	log.Printf("About to listen on 8443. Go to https://127.0.0.1:8443/")
	err := http.ListenAndServeTLS(":8443", "cert.pem", "key.pem", nil)
	log.Fatal(err)
}
```

```
Output:
```

#### func MaxBytesReader

```
func MaxBytesReader(w ResponseWriter, r io.ReadCloser, n int64) io.ReadCloser
```

MaxBytesReader is similar to io.LimitReader but is intended for limiting the size of incoming request bodies. In contrast to io.LimitReader, MaxBytesReader's result is a ReadCloser, returns a non-nil error of type *MaxBytesError for a Read beyond the limit, and closes the underlying reader when its Close method is called.

MaxBytesReader prevents clients from accidentally or maliciously sending a large request and wasting server resources. If possible, it tells the ResponseWriter to close the connection after the limit has been reached.

#### func NotFound

```
func NotFound(w ResponseWriter, r *Request)
```

NotFound replies to the request with an HTTP 404 not found error.

#### func ParseHTTPVersion

```
func ParseHTTPVersion(vers string) (major, minor int, ok bool)
```

ParseHTTPVersion parses an HTTP version string according to RFC 7230, section 2.6. "HTTP/1.0" returns (1, 0, true). Note that strings without a minor version, such as "HTTP/2", are not valid.

#### func ParseTime ¶ added in go1.1

```
func ParseTime(text string) (t time.Time, err error)
```

ParseTime parses a time header (such as the Date: header), trying each of the three formats allowed by HTTP/1.1: TimeFormat, time.RFC850, and time.ANSIC.

#### func ProxyFromEnvironment

```
func ProxyFromEnvironment(req *Request) (*url.URL, error)
```

ProxyFromEnvironment returns the URL of the proxy to use for a given request, as indicated by the environment variables HTTP_PROXY, HTTPS_PROXY and NO_PROXY (or the lowercase versions thereof). Requests use the proxy from the environment variable matching their scheme, unless excluded by NO_PROXY.

The environment values may be either a complete URL or a "host[:port]", in which case the "http" scheme is assumed. An error is returned if the value is a different form.

A nil URL and nil error are returned if no proxy is defined in the environment, or a proxy should not be used for the given request, as defined by NO_PROXY.

As a special case, if req.URL.Host is "localhost" (with or without a port number), then a nil URL and nil error will be returned.

#### func ProxyURL

```
func ProxyURL(fixedURL *url.URL) func(*Request) (*url.URL, error)
```

ProxyURL returns a proxy function (for use in a Transport) that always returns the same URL.

#### func Redirect

```
func Redirect(w ResponseWriter, r *Request, url string, code int)
```

Redirect replies to the request with a redirect to url, which may be a path relative to the request path. Any non-ASCII characters in url will be percent-encoded, but existing percent encodings will not be changed.

The provided code should be in the 3xx range and is usually StatusMovedPermanently, StatusFound or StatusSeeOther.

If the Content-Type header has not been set, Redirect sets it to "text/html; charset=utf-8" and writes a small HTML body. Setting the Content-Type header to any value, including nil, disables that behavior.

#### func Serve

```
func Serve(l net.Listener, handler Handler) error
```

Serve accepts incoming HTTP connections on the listener l, creating a new service goroutine for each. The service goroutines read requests and then call handler to reply to them.

The handler is typically nil, in which case DefaultServeMux is used.

HTTP/2 support is only enabled if the Listener returns *tls.Conn connections and they were configured with "h2" in the TLS Config.NextProtos.

Serve always returns a non-nil error.

#### func ServeContent

```
func ServeContent(w ResponseWriter, req *Request, name string, modtime time.Time, content io.ReadSeeker)
```

ServeContent replies to the request using the content in the provided ReadSeeker. The main benefit of ServeContent over io.Copy is that it handles Range requests properly, sets the MIME type, and handles If-Match, If-Unmodified-Since, If-None-Match, If-Modified-Since, and If-Range requests.

If the response's Content-Type header is not set, ServeContent first tries to deduce the type from name's file extension and, if that fails, falls back to reading the first block of the content and passing it to DetectContentType. The name is otherwise unused; in particular it can be empty and is never sent in the response.

If modtime is not the zero time or Unix epoch, ServeContent includes it in a Last-Modified header in the response. If the request includes an If-Modified-Since header, ServeContent uses modtime to decide whether the content needs to be sent at all.

The content's Seek method must work: ServeContent uses a seek to the end of the content to determine its size. Note that *os.File implements the io.ReadSeeker interface.

If the caller has set w's ETag header formatted per RFC 7232, section 2.3, ServeContent uses it to handle requests using If-Match, If-None-Match, or If-Range.

If an error occurs when serving the request (for example, when handling an invalid range request), ServeContent responds with an error message. By default, ServeContent strips the Cache-Control, Content-Encoding, ETag, and Last-Modified headers from error responses. The GODEBUG setting httpservecontentkeepheaders=1 causes ServeContent to preserve these headers.

#### func ServeFile

```
func ServeFile(w ResponseWriter, r *Request, name string)
```

ServeFile replies to the request with the contents of the named file or directory.

If the provided file or directory name is a relative path, it is interpreted relative to the current directory and may ascend to parent directories. If the provided name is constructed from user input, it should be sanitized before calling ServeFile.

As a precaution, ServeFile will reject requests where r.URL.Path contains a ".." path element; this protects against callers who might unsafely use filepath.Join on r.URL.Path without sanitizing it and then use that filepath.Join result as the name argument.

As another special case, ServeFile redirects any request where r.URL.Path ends in "/index.html" to the same path, without the final "index.html". To avoid such redirects either modify the path or use ServeContent.

Outside of those two special cases, ServeFile does not use r.URL.Path for selecting the file or directory to serve; only the file or directory provided in the name argument is used.

#### func ServeFileFS ¶ added in go1.22.0

```
func ServeFileFS(w ResponseWriter, r *Request, fsys fs.FS, name string)
```

ServeFileFS replies to the request with the contents of the named file or directory from the file system fsys. The files provided by fsys must implement io.Seeker.

If the provided name is constructed from user input, it should be sanitized before calling ServeFileFS.

As a precaution, ServeFileFS will reject requests where r.URL.Path contains a ".." path element; this protects against callers who might unsafely use filepath.Join on r.URL.Path without sanitizing it and then use that filepath.Join result as the name argument.

As another special case, ServeFileFS redirects any request where r.URL.Path ends in "/index.html" to the same path, without the final "index.html". To avoid such redirects either modify the path or use ServeContent.

Outside of those two special cases, ServeFileFS does not use r.URL.Path for selecting the file or directory to serve; only the file or directory provided in the name argument is used.

#### func ServeTLS ¶ added in go1.9

```
func ServeTLS(l net.Listener, handler Handler, certFile, keyFile string) error
```

ServeTLS accepts incoming HTTPS connections on the listener l, creating a new service goroutine for each. The service goroutines read requests and then call handler to reply to them.

The handler is typically nil, in which case DefaultServeMux is used.

Additionally, files containing a certificate and matching private key for the server must be provided. If the certificate is signed by a certificate authority, the certFile should be the concatenation of the server's certificate, any intermediates, and the CA's certificate.

ServeTLS always returns a non-nil error.

#### func SetCookie

```
func SetCookie(w ResponseWriter, cookie *Cookie)
```

SetCookie adds a Set-Cookie header to the provided ResponseWriter's headers. The provided cookie must have a valid Name. Invalid cookies may be silently dropped.

#### func StatusText

```
func StatusText(code int) string
```

StatusText returns a text for the HTTP status code. It returns the empty string if the code is unknown.

### Types

#### type Client

```
type Client struct {
	
	
	
	Transport RoundTripper

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	CheckRedirect func(req *Request, via []*Request) error

	
	
	
	
	
	
	
	
	
	Jar CookieJar

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	Timeout time.Duration
}
```

A Client is an HTTP client. Its zero value (DefaultClient) is a usable client that uses DefaultTransport.

The Client.Transport typically has internal state (cached TCP connections), so Clients should be reused instead of created as needed. Clients are safe for concurrent use by multiple goroutines.

A Client is higher-level than a RoundTripper (such as Transport) and additionally handles HTTP details such as cookies and redirects.

When following redirects, the Client will forward all headers set on the initial Request except:

- when forwarding sensitive headers like "Authorization", "WWW-Authenticate", and "Cookie" to untrusted targets. These headers will be ignored when following a redirect to a domain that is not a subdomain match or exact match of the initial domain. For example, a redirect from "foo.com" to either "foo.com" or "sub.foo.com" will forward the sensitive headers, but a redirect to "bar.com" will not.
- when forwarding the "Cookie" header with a non-nil cookie Jar. Since each redirect may mutate the state of the cookie jar, a redirect may possibly alter a cookie set in the initial request. When forwarding the "Cookie" header, any mutated cookies will be omitted, with the expectation that the Jar will insert those mutated cookies with the updated values (assuming the origin matches). If Jar is nil, the initial cookies are forwarded without change.

#### func (*Client) CloseIdleConnections ¶ added in go1.12

```
func (c *Client) CloseIdleConnections()
```

CloseIdleConnections closes any connections on its Transport which were previously connected from previous requests but are now sitting idle in a "keep-alive" state. It does not interrupt any connections currently in use.

If Client.Transport does not have a Client.CloseIdleConnections method then this method does nothing.

#### func (*Client) Do

```
func (c *Client) Do(req *Request) (*Response, error)
```

Do sends an HTTP request and returns an HTTP response, following policy (such as redirects, cookies, auth) as configured on the client.

An error is returned if caused by client policy (such as CheckRedirect), or failure to speak HTTP (such as a network connectivity problem). A non-2xx status code doesn't cause an error.

If the returned error is nil, the Response will contain a non-nil Body which the user is expected to close. If the Body is not both read to EOF and closed, the Client's underlying RoundTripper (typically Transport) may not be able to re-use a persistent TCP connection to the server for a subsequent "keep-alive" request.

The request Body, if non-nil, will be closed by the underlying Transport, even on errors. The Body may be closed asynchronously after Do returns.

On error, any Response can be ignored. A non-nil Response with a non-nil error only occurs when CheckRedirect fails, and even then the returned Response.Body is already closed.

Generally Get, Post, or PostForm will be used instead of Do.

If the server replies with a redirect, the Client first uses the CheckRedirect function to determine whether the redirect should be followed. If permitted, a 301, 302, or 303 redirect causes subsequent requests to use HTTP method GET (or HEAD if the original request was HEAD), with no body. A 307 or 308 redirect preserves the original HTTP method and body, provided that the Request.GetBody function is defined. The NewRequest function automatically sets GetBody for common standard library body types.

Any returned error will be of type *url.Error. The url.Error value's Timeout method will report true if the request timed out.

#### func (*Client) Get

```
func (c *Client) Get(url string) (resp *Response, err error)
```

Get issues a GET to the specified URL. If the response is one of the following redirect codes, Get follows the redirect after calling the Client.CheckRedirect function:

```
301 (Moved Permanently)
302 (Found)
303 (See Other)
307 (Temporary Redirect)
308 (Permanent Redirect)
```

An error is returned if the Client.CheckRedirect function fails or if there was an HTTP protocol error. A non-2xx response doesn't cause an error. Any returned error will be of type *url.Error. The url.Error value's Timeout method will report true if the request timed out.

When err is nil, resp always contains a non-nil resp.Body. Caller should close resp.Body when done reading from it.

To make a request with custom headers, use NewRequest and Client.Do.

To make a request with a specified context.Context, use NewRequestWithContext and Client.Do.

#### func (*Client) Head

```
func (c *Client) Head(url string) (resp *Response, err error)
```

Head issues a HEAD to the specified URL. If the response is one of the following redirect codes, Head follows the redirect after calling the Client.CheckRedirect function:

```
301 (Moved Permanently)
302 (Found)
303 (See Other)
307 (Temporary Redirect)
308 (Permanent Redirect)
```

To make a request with a specified context.Context, use NewRequestWithContext and Client.Do.

#### func (*Client) Post

```
func (c *Client) Post(url, contentType string, body io.Reader) (resp *Response, err error)
```

Post issues a POST to the specified URL.

Caller should close resp.Body when done reading from it.

If the provided body is an io.Closer, it is closed after the request.

To set custom headers, use NewRequest and Client.Do.

To make a request with a specified context.Context, use NewRequestWithContext and Client.Do.

See the Client.Do method documentation for details on how redirects are handled.

#### func (*Client) PostForm

```
func (c *Client) PostForm(url string, data url.Values) (resp *Response, err error)
```

PostForm issues a POST to the specified URL, with data's keys and values URL-encoded as the request body.

The Content-Type header is set to application/x-www-form-urlencoded. To set other headers, use NewRequest and Client.Do.

When err is nil, resp always contains a non-nil resp.Body. Caller should close resp.Body when done reading from it.

See the Client.Do method documentation for details on how redirects are handled.

To make a request with a specified context.Context, use NewRequestWithContext and Client.Do.

#### type ClientConn ¶ added in go1.26.0

```
type ClientConn struct {
	
}
```

A ClientConn is a client connection to an HTTP server.

Unlike a Transport, a ClientConn represents a single connection. Most users should use a Transport rather than creating client connections directly.

#### func (*ClientConn) Available ¶ added in go1.26.0

```
func (cc *ClientConn) Available() int
```

Available reports the number of requests that may be sent to the connection without blocking. It returns 0 if the connection is closed.

#### func (*ClientConn) Close ¶ added in go1.26.0

```
func (cc *ClientConn) Close() error
```

Close closes the connection. Outstanding RoundTrip calls are interrupted.

#### func (*ClientConn) Err ¶ added in go1.26.0

```
func (cc *ClientConn) Err() error
```

Err reports any fatal connection errors. It returns nil if the connection is usable. If it returns non-nil, the connection can no longer be used.

#### func (*ClientConn) InFlight ¶ added in go1.26.0

```
func (cc *ClientConn) InFlight() int
```

InFlight reports the number of requests in flight, including reserved requests. It returns 0 if the connection is closed.

#### func (*ClientConn) Release ¶ added in go1.26.0

```
func (cc *ClientConn) Release()
```

Release releases an unused concurrency slot reserved by Reserve. If there are no reserved concurrency slots, it has no effect.

#### func (*ClientConn) Reserve ¶ added in go1.26.0

```
func (cc *ClientConn) Reserve() error
```

Reserve reserves a concurrency slot on the connection. If Reserve returns nil, one additional RoundTrip call may be made without waiting for an existing request to complete.

The reserved concurrency slot is accounted as an in-flight request. A successful call to RoundTrip will decrement the Available count and increment the InFlight count.

Each successful call to Reserve should be followed by exactly one call to RoundTrip or Release, which will consume or release the reservation.

If the connection is closed or at its concurrency limit, Reserve returns an error.

#### func (*ClientConn) RoundTrip ¶ added in go1.26.0

```
func (cc *ClientConn) RoundTrip(req *Request) (*Response, error)
```

RoundTrip implements the RoundTripper interface.

The request is sent on the client connection, regardless of the URL being requested or any proxy settings.

If the connection is at its concurrency limit, RoundTrip waits for the connection to become available before sending the request.

#### func (*ClientConn) SetStateHook ¶ added in go1.26.0

```
func (cc *ClientConn) SetStateHook(f func(*ClientConn))
```

SetStateHook arranges for f to be called when the state of the connection changes. At most one call to f is made at a time. If the connection's state has changed since it was created, f is called immediately in a separate goroutine. f may be called synchronously from RoundTrip or Response.Body.Close.

If SetStateHook is called multiple times, the new hook replaces the old one. If f is nil, no further calls will be made to f after SetStateHook returns.

f is called when Available increases (more requests may be sent on the connection), InFlight decreases (existing requests complete), or Err begins returning non-nil (the connection is no longer usable).

#### type CloseNotifier deprecated added in go1.1

```
type CloseNotifier interface {
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	CloseNotify() <-chan bool
}
```

The CloseNotifier interface is implemented by ResponseWriters which allow detecting when the underlying connection has gone away.

This mechanism can be used to cancel long operations on the server if the client has disconnected before the response is ready.

Deprecated: the CloseNotifier interface predates Go's context package. New code should use Request.Context instead.

#### type ConnState ¶ added in go1.3

```
type ConnState int
```

A ConnState represents the state of a client connection to a server. It's used by the optional Server.ConnState hook.

```
const (
	
	
	
	
	StateNew ConnState = iota

	
	
	
	
	
	
	
	
	
	
	
	StateActive

	
	
	
	
	StateIdle

	
	
	StateHijacked

	
	
	
	StateClosed
)
```

#### func (ConnState) String ¶ added in go1.3

```
func (c ConnState) String() string
```

```
type Cookie struct {
	Name   string
	Value  string
	Quoted bool 

	Path       string    
	Domain     string    
	Expires    time.Time 
	RawExpires string    

	
	
	
	MaxAge      int
	Secure      bool
	HttpOnly    bool
	SameSite    SameSite
	Partitioned bool
	Raw         string
	Unparsed    []string 
}
```

A Cookie represents an HTTP cookie as sent in the Set-Cookie header of an HTTP response or the Cookie header of an HTTP request.

See https://tools.ietf.org/html/rfc6265 for details.

#### func ParseCookie ¶ added in go1.23.0

```
func ParseCookie(line string) ([]*Cookie, error)
```

ParseCookie parses a Cookie header value and returns all the cookies which were set in it. Since the same cookie name can appear multiple times the returned Values can contain more than one value for a given key.

#### func ParseSetCookie ¶ added in go1.23.0

```
func ParseSetCookie(line string) (*Cookie, error)
```

ParseSetCookie parses a Set-Cookie header value and returns a cookie. It returns an error on syntax error.

#### func (*Cookie) String

```
func (c *Cookie) String() string
```

String returns the serialization of the cookie for use in a Cookie header (if only Name and Value are set) or a Set-Cookie response header (if other fields are set). If c is nil or c.Name is invalid, the empty string is returned.

#### func (*Cookie) Valid ¶ added in go1.18

```
func (c *Cookie) Valid() error
```

Valid reports whether the cookie is valid.

#### type CookieJar

```
type CookieJar interface {
	
	
	
	SetCookies(u *url.URL, cookies []*Cookie)

	
	
	
	Cookies(u *url.URL) []*Cookie
}
```

A CookieJar manages storage and use of cookies in HTTP requests.

Implementations of CookieJar must be safe for concurrent use by multiple goroutines.

The net/http/cookiejar package provides a CookieJar implementation.

#### type CrossOriginProtection ¶ added in go1.25.0

```
type CrossOriginProtection struct {
	
}
```

CrossOriginProtection implements protections against Cross-Site Request Forgery (CSRF) by rejecting non-safe cross-origin browser requests.

Cross-origin requests are currently detected with the Sec-Fetch-Site header, available in all browsers since 2023, or by comparing the hostname of the Origin header with the Host header.

The GET, HEAD, and OPTIONS methods are safe methods and are always allowed. It's important that applications do not perform any state changing actions due to requests with safe methods.

Requests without Sec-Fetch-Site or Origin headers are currently assumed to be either same-origin or non-browser requests, and are allowed.

The zero value of CrossOriginProtection is valid and has no trusted origins or bypass patterns.

Example

¶

```
package main

import (
	"io"
	"log"
	"net/http"
	"time"
)

func main() {
	mux := http.NewServeMux()

	mux.HandleFunc("/hello", func(w http.ResponseWriter, req *http.Request) {
		io.WriteString(w, "request allowed\n")
	})

	srv := http.Server{
		Addr:         ":8080",
		ReadTimeout:  15 * time.Second,
		WriteTimeout: 15 * time.Second,
		// Use CrossOriginProtection.Handler to block all non-safe cross-origin
		// browser requests to mux.
		Handler: http.NewCrossOriginProtection().Handler(mux),
	}

	log.Fatal(srv.ListenAndServe())
}
```

```
Output:
```

#### func NewCrossOriginProtection ¶ added in go1.25.0

```
func NewCrossOriginProtection() *CrossOriginProtection
```

NewCrossOriginProtection returns a new CrossOriginProtection value.

#### func (*CrossOriginProtection) AddInsecureBypassPattern ¶ added in go1.25.0

```
func (c *CrossOriginProtection) AddInsecureBypassPattern(pattern string)
```

AddInsecureBypassPattern permits all requests that match the given pattern.

The pattern syntax and precedence rules are the same as ServeMux. Only requests that match the pattern directly are permitted. Those that ServeMux would redirect to a pattern (e.g. after cleaning the path or adding a trailing slash) are not.

AddInsecureBypassPattern panics if the pattern conflicts with one already registered, or if the pattern is syntactically invalid (for example, an improperly formed wildcard).

AddInsecureBypassPattern can be called concurrently with other methods or request handling, and applies to future requests.

#### func (*CrossOriginProtection) AddTrustedOrigin ¶ added in go1.25.0

```
func (c *CrossOriginProtection) AddTrustedOrigin(origin string) error
```

AddTrustedOrigin allows all requests with an Origin header which exactly matches the given value.

Origin header values are of the form "scheme://host[:port]".

AddTrustedOrigin can be called concurrently with other methods or request handling, and applies to future requests.

#### func (*CrossOriginProtection) Check ¶ added in go1.25.0

```
func (c *CrossOriginProtection) Check(req *Request) error
```

Check applies cross-origin checks to a request. It returns an error if the request should be rejected.

#### func (*CrossOriginProtection) Handler ¶ added in go1.25.0

```
func (c *CrossOriginProtection) Handler(h Handler) Handler
```

Handler returns a handler that applies cross-origin checks before invoking the handler h.

If a request fails cross-origin checks, the request is rejected with a 403 Forbidden status or handled with the handler passed to CrossOriginProtection.SetDenyHandler.

#### func (*CrossOriginProtection) SetDenyHandler ¶ added in go1.25.0

```
func (c *CrossOriginProtection) SetDenyHandler(h Handler)
```

SetDenyHandler sets a handler to invoke when a request is rejected. The default error handler responds with a 403 Forbidden status.

SetDenyHandler can be called concurrently with other methods or request handling, and applies to future requests.

Check does not call the error handler.

#### type Dir

```
type Dir string
```

A Dir implements FileSystem using the native file system restricted to a specific directory tree.

While the FileSystem.Open method takes '/'-separated paths, a Dir's string value is a directory path on the native file system, not a URL, so it is separated by filepath.Separator, which isn't necessarily '/'.

Note that Dir could expose sensitive files and directories. Dir will follow symlinks pointing out of the directory tree, which can be especially dangerous if serving from a directory in which users are able to create arbitrary symlinks. Dir will also allow access to files and directories starting with a period, which could expose sensitive directories like .git or sensitive files like .htpasswd. To exclude files with a leading period, remove the files/directories from the server or create a custom FileSystem implementation.

An empty Dir is treated as ".".

#### func (Dir) Open

```
func (d Dir) Open(name string) (File, error)
```

Open implements FileSystem using os.Open, opening files for reading rooted and relative to the directory d.

#### type File

```
type File interface {
	io.Closer
	io.Reader
	io.Seeker
	Readdir(count int) ([]fs.FileInfo, error)
	Stat() (fs.FileInfo, error)
}
```

A File is returned by a FileSystem's Open method and can be served by the FileServer implementation.

The methods should behave the same as those on an *os.File.

#### type FileSystem

```
type FileSystem interface {
	Open(name string) (File, error)
}
```

A FileSystem implements access to a collection of named files. The elements in a file path are separated by slash ('/', U+002F) characters, regardless of host operating system convention. See the FileServer function to convert a FileSystem to a Handler.

This interface predates the fs.FS interface, which can be used instead: the FS adapter function converts an fs.FS to a FileSystem.

#### func FS ¶ added in go1.16

```
func FS(fsys fs.FS) FileSystem
```

FS converts fsys to a FileSystem implementation, for use with FileServer and NewFileTransport. The files provided by fsys must implement io.Seeker.

#### type Flusher

```
type Flusher interface {
	
	Flush()
}
```

The Flusher interface is implemented by ResponseWriters that allow an HTTP handler to flush buffered data to the client.

The default HTTP/1.x and HTTP/2 ResponseWriter implementations support Flusher, but ResponseWriter wrappers may not. Handlers should always test for this ability at runtime.

Note that even for ResponseWriters that support Flush, if the client is connected through an HTTP proxy, the buffered data may not reach the client until the response completes.

#### type HTTP2Config ¶ added in go1.24.0

```
type HTTP2Config struct {
	
	
	
	
	
	MaxConcurrentStreams int

	
	
	
	
	
	
	
	
	
	StrictMaxConcurrentRequests bool

	
	
	
	
	
	MaxDecoderHeaderTableSize int

	
	
	
	
	MaxEncoderHeaderTableSize int

	
	
	
	
	MaxReadFrameSize int

	
	
	
	
	MaxReceiveBufferPerConnection int

	
	
	
	
	MaxReceiveBufferPerStream int

	
	
	
	SendPingTimeout time.Duration

	
	
	
	PingTimeout time.Duration

	
	
	
	WriteByteTimeout time.Duration

	
	
	PermitProhibitedCipherSuites bool

	
	
	
	
	CountError func(errType string)
}
```

HTTP2Config defines HTTP/2 configuration parameters common to both Transport and Server.

#### type Handler

```
type Handler interface {
	ServeHTTP(ResponseWriter, *Request)
}
```

A Handler responds to an HTTP request.

Handler.ServeHTTP should write reply headers and data to the ResponseWriter and then return. Returning signals that the request is finished; it is not valid to use the ResponseWriter or read from the Request.Body after or concurrently with the completion of the ServeHTTP call.

Depending on the HTTP client software, HTTP protocol version, and any intermediaries between the client and the Go server, it may not be possible to read from the Request.Body after writing to the ResponseWriter. Cautious handlers should read the Request.Body first, and then reply.

Except for reading the body, handlers should not modify the provided Request.

If ServeHTTP panics, the server (the caller of ServeHTTP) assumes that the effect of the panic was isolated to the active request. It recovers the panic, logs a stack trace to the server error log, and either closes the network connection or sends an HTTP/2 RST_STREAM, depending on the HTTP protocol. To abort a handler so the client sees an interrupted response but the server doesn't log an error, panic with the value ErrAbortHandler.

#### func AllowQuerySemicolons ¶ added in go1.17

```
func AllowQuerySemicolons(h Handler) Handler
```

AllowQuerySemicolons returns a handler that serves requests by converting any unescaped semicolons in the URL query to ampersands, and invoking the handler h.

This restores the pre-Go 1.17 behavior of splitting query parameters on both semicolons and ampersands. (See golang.org/issue/25192). Note that this behavior doesn't match that of many proxies, and the mismatch can lead to security issues.

AllowQuerySemicolons should be invoked before Request.ParseForm is called.

#### func FileServer

```
func FileServer(root FileSystem) Handler
```

FileServer returns a handler that serves HTTP requests with the contents of the file system rooted at root.

As a special case, the returned file server redirects any request ending in "/index.html" to the same path, without the final "index.html".

To use the operating system's file system implementation, use http.Dir:

```
http.Handle("/", http.FileServer(http.Dir("/tmp")))
```

To use an fs.FS implementation, use http.FileServerFS instead.

Example

¶

```
package main

import (
	"log"
	"net/http"
)

func main() {
	// Simple static webserver:
	log.Fatal(http.ListenAndServe(":8080", http.FileServer(http.Dir("/usr/share/doc"))))
}
```

```
Output:
```

Example (DotFileHiding)

¶

```
package main

import (
	"io"
	"io/fs"
	"log"
	"net/http"
	"strings"
)

// containsDotFile reports whether name contains a path element starting with a period.
// The name is assumed to be a delimited by forward slashes, as guaranteed
// by the http.FileSystem interface.
func containsDotFile(name string) bool {
	parts := strings.Split(name, "/")
	for _, part := range parts {
		if strings.HasPrefix(part, ".") {
			return true
		}
	}
	return false
}

// dotFileHidingFile is the http.File use in dotFileHidingFileSystem.
// It is used to wrap the Readdir method of http.File so that we can
// remove files and directories that start with a period from its output.
type dotFileHidingFile struct {
	http.File
}

// Readdir is a wrapper around the Readdir method of the embedded File
// that filters out all files that start with a period in their name.
func (f dotFileHidingFile) Readdir(n int) (fis []fs.FileInfo, err error) {
	files, err := f.File.Readdir(n)
	for _, file := range files { // Filters out the dot files
		if !strings.HasPrefix(file.Name(), ".") {
			fis = append(fis, file)
		}
	}
	if err == nil && n > 0 && len(fis) == 0 {
		err = io.EOF
	}
	return
}

// dotFileHidingFileSystem is an http.FileSystem that hides
// hidden "dot files" from being served.
type dotFileHidingFileSystem struct {
	http.FileSystem
}

// Open is a wrapper around the Open method of the embedded FileSystem
// that serves a 403 permission error when name has a file or directory
// with whose name starts with a period in its path.
func (fsys dotFileHidingFileSystem) Open(name string) (http.File, error) {
	if containsDotFile(name) { // If dot file, return 403 response
		return nil, fs.ErrPermission
	}

	file, err := fsys.FileSystem.Open(name)
	if err != nil {
		return nil, err
	}
	return dotFileHidingFile{file}, nil
}

func main() {
	fsys := dotFileHidingFileSystem{http.Dir(".")}
	http.Handle("/", http.FileServer(fsys))
	log.Fatal(http.ListenAndServe(":8080", nil))
}
```

```
Output:
```

Example (StripPrefix)

¶

```
package main

import (
	"net/http"
)

func main() {
	// To serve a directory on disk (/tmp) under an alternate URL
	// path (/tmpfiles/), use StripPrefix to modify the request
	// URL's path before the FileServer sees it:
	http.Handle("/tmpfiles/", http.StripPrefix("/tmpfiles/", http.FileServer(http.Dir("/tmp"))))
}
```

```
Output:
```

#### func FileServerFS ¶ added in go1.22.0

```
func FileServerFS(root fs.FS) Handler
```

FileServerFS returns a handler that serves HTTP requests with the contents of the file system fsys. The files provided by fsys must implement io.Seeker.

As a special case, the returned file server redirects any request ending in "/index.html" to the same path, without the final "index.html".

```
http.Handle("/", http.FileServerFS(fsys))
```

#### func MaxBytesHandler ¶ added in go1.18

```
func MaxBytesHandler(h Handler, n int64) Handler
```

MaxBytesHandler returns a Handler that runs h with its ResponseWriter and Request.Body wrapped by a MaxBytesReader.

#### func NotFoundHandler

```
func NotFoundHandler() Handler
```

NotFoundHandler returns a simple request handler that replies to each request with a “404 page not found” reply.

Example

¶

```
package main

import (
	"fmt"
	"log"
	"net/http"
)

func newPeopleHandler() http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintln(w, "This is the people handler.")
	})
}

func main() {
	mux := http.NewServeMux()

	// Create sample handler to returns 404
	mux.Handle("/resources", http.NotFoundHandler())

	// Create sample handler that returns 200
	mux.Handle("/resources/people/", newPeopleHandler())

	log.Fatal(http.ListenAndServe(":8080", mux))
}
```

```
Output:
```

#### func RedirectHandler

```
func RedirectHandler(url string, code int) Handler
```

RedirectHandler returns a request handler that redirects each request it receives to the given url using the given status code.

The provided code should be in the 3xx range and is usually StatusMovedPermanently, StatusFound or StatusSeeOther.

#### func StripPrefix

```
func StripPrefix(prefix string, h Handler) Handler
```

StripPrefix returns a handler that serves HTTP requests by removing the given prefix from the request URL's Path (and RawPath if set) and invoking the handler h. StripPrefix handles a request for a path that doesn't begin with prefix by replying with an HTTP 404 not found error. The prefix must match exactly: if the prefix in the request contains escaped characters the reply is also an HTTP 404 not found error.

Example

¶

```
package main

import (
	"net/http"
)

func main() {
	// To serve a directory on disk (/tmp) under an alternate URL
	// path (/tmpfiles/), use StripPrefix to modify the request
	// URL's path before the FileServer sees it:
	http.Handle("/tmpfiles/", http.StripPrefix("/tmpfiles/", http.FileServer(http.Dir("/tmp"))))
}
```

```
Output:
```

#### func TimeoutHandler

```
func TimeoutHandler(h Handler, dt time.Duration, msg string) Handler
```

TimeoutHandler returns a Handler that runs h with the given time limit.

The new Handler calls h.ServeHTTP to handle each request, but if a call runs for longer than its time limit, the handler responds with a 503 Service Unavailable error and the given message in its body. (If msg is empty, a suitable default message will be sent.) After such a timeout, writes by h to its ResponseWriter will return ErrHandlerTimeout.

TimeoutHandler supports the Pusher interface but does not support the Hijacker or Flusher interfaces.

#### type HandlerFunc

```
type HandlerFunc func(ResponseWriter, *Request)
```

The HandlerFunc type is an adapter to allow the use of ordinary functions as HTTP handlers. If f is a function with the appropriate signature, HandlerFunc(f) is a Handler that calls f.

#### func (HandlerFunc) ServeHTTP

```
func (f HandlerFunc) ServeHTTP(w ResponseWriter, r *Request)
```

ServeHTTP calls f(w, r).

#### type Header
