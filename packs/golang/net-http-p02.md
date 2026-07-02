---
title: "http package (part 2/3)"
source: https://pkg.go.dev/net/http
domain: golang
license: BSD-3-Clause
tags: golang, goroutine, go module, go stdlib
fetched: 2026-07-02
part: 2/3
---

# http package

```
type Header map[string][]string
```

A Header represents the key-value pairs in an HTTP header.

The keys should be in canonical form, as returned by CanonicalHeaderKey.

#### func (Header) Add

```
func (h Header) Add(key, value string)
```

Add adds the key, value pair to the header. It appends to any existing values associated with key. The key is case insensitive; it is canonicalized by CanonicalHeaderKey.

#### func (Header) Clone ¶ added in go1.13

```
func (h Header) Clone() Header
```

Clone returns a copy of h or nil if h is nil.

#### func (Header) Del

```
func (h Header) Del(key string)
```

Del deletes the values associated with key. The key is case insensitive; it is canonicalized by CanonicalHeaderKey.

#### func (Header) Get

```
func (h Header) Get(key string) string
```

Get gets the first value associated with the given key. If there are no values associated with the key, Get returns "". It is case insensitive; textproto.CanonicalMIMEHeaderKey is used to canonicalize the provided key. Get assumes that all keys are stored in canonical form. To use non-canonical keys, access the map directly.

#### func (Header) Set

```
func (h Header) Set(key, value string)
```

Set sets the header entries associated with key to the single element value. It replaces any existing values associated with key. The key is case insensitive; it is canonicalized by textproto.CanonicalMIMEHeaderKey. To use non-canonical keys, assign to the map directly.

#### func (Header) Values ¶ added in go1.14

```
func (h Header) Values(key string) []string
```

Values returns all values associated with the given key. It is case insensitive; textproto.CanonicalMIMEHeaderKey is used to canonicalize the provided key. To use non-canonical keys, access the map directly. The returned slice is not a copy.

#### func (Header) Write

```
func (h Header) Write(w io.Writer) error
```

Write writes a header in wire format.

#### func (Header) WriteSubset

```
func (h Header) WriteSubset(w io.Writer, exclude map[string]bool) error
```

WriteSubset writes a header in wire format. If exclude is not nil, keys where exclude[key] == true are not written. Keys are not canonicalized before checking the exclude map.

#### type Hijacker

```
type Hijacker interface {
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	Hijack() (net.Conn, *bufio.ReadWriter, error)
}
```

The Hijacker interface is implemented by ResponseWriters that allow an HTTP handler to take over the connection.

The default ResponseWriter for HTTP/1.x connections supports Hijacker, but HTTP/2 connections intentionally do not. ResponseWriter wrappers may also not support Hijacker. Handlers should always test for this ability at runtime.

Example

¶

```
package main

import (
	"fmt"
	"log"
	"net/http"
)

func main() {
	http.HandleFunc("/hijack", func(w http.ResponseWriter, r *http.Request) {
		hj, ok := w.(http.Hijacker)
		if !ok {
			http.Error(w, "webserver doesn't support hijacking", http.StatusInternalServerError)
			return
		}
		conn, bufrw, err := hj.Hijack()
		if err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}
		// Don't forget to close the connection:
		defer conn.Close()
		bufrw.WriteString("Now we're speaking raw TCP. Say hi: ")
		bufrw.Flush()
		s, err := bufrw.ReadString('\n')
		if err != nil {
			log.Printf("error reading string: %v", err)
			return
		}
		fmt.Fprintf(bufrw, "You said: %q\nBye.\n", s)
		bufrw.Flush()
	})
}
```

```
Output:
```

#### type MaxBytesError ¶ added in go1.19

```
type MaxBytesError struct {
	Limit int64
}
```

MaxBytesError is returned by MaxBytesReader when its read limit is exceeded.

#### func (*MaxBytesError) Error ¶ added in go1.19

```
func (e *MaxBytesError) Error() string
```

#### type ProtocolError deprecated

```
type ProtocolError struct {
	ErrorString string
}
```

ProtocolError represents an HTTP protocol error.

Deprecated: Not all errors in the http package related to protocol errors are of type ProtocolError.

#### func (*ProtocolError) Error

```
func (pe *ProtocolError) Error() string
```

#### func (*ProtocolError) Is ¶ added in go1.21.0

```
func (pe *ProtocolError) Is(err error) bool
```

Is lets http.ErrNotSupported match errors.ErrUnsupported.

#### type Protocols ¶ added in go1.24.0

```
type Protocols struct {
	
}
```

Protocols is a set of HTTP protocols. The zero value is an empty set of protocols.

The supported protocols are:

- HTTP1 is the HTTP/1.0 and HTTP/1.1 protocols. HTTP1 is supported on both unsecured TCP and secured TLS connections.
- HTTP2 is the HTTP/2 protcol over a TLS connection.
- UnencryptedHTTP2 is the HTTP/2 protocol over an unsecured TCP connection.

Example (Http1)

¶

```
package main

import (
	"log"
	"net/http"
)

func main() {
	srv := http.Server{
		Addr: ":8443",
	}

	// Serve only HTTP/1.
	srv.Protocols = new(http.Protocols)
	srv.Protocols.SetHTTP1(true)

	log.Fatal(srv.ListenAndServeTLS("cert.pem", "key.pem"))
}
```

```
Output:
```

Example (Http1or2)

¶

```
package main

import (
	"log"
	"net/http"
)

func main() {
	t := http.DefaultTransport.(*http.Transport).Clone()

	// Use either HTTP/1 and HTTP/2.
	t.Protocols = new(http.Protocols)
	t.Protocols.SetHTTP1(true)
	t.Protocols.SetHTTP2(true)

	cli := &http.Client{Transport: t}
	res, err := cli.Get("http://www.google.com/robots.txt")
	if err != nil {
		log.Fatal(err)
	}
	res.Body.Close()
}
```

```
Output:
```

#### func (Protocols) HTTP1 ¶ added in go1.24.0

```
func (p Protocols) HTTP1() bool
```

HTTP1 reports whether p includes HTTP/1.

#### func (Protocols) HTTP2 ¶ added in go1.24.0

```
func (p Protocols) HTTP2() bool
```

HTTP2 reports whether p includes HTTP/2.

#### func (*Protocols) SetHTTP1 ¶ added in go1.24.0

```
func (p *Protocols) SetHTTP1(ok bool)
```

SetHTTP1 adds or removes HTTP/1 from p.

#### func (*Protocols) SetHTTP2 ¶ added in go1.24.0

```
func (p *Protocols) SetHTTP2(ok bool)
```

SetHTTP2 adds or removes HTTP/2 from p.

#### func (*Protocols) SetUnencryptedHTTP2 ¶ added in go1.24.0

```
func (p *Protocols) SetUnencryptedHTTP2(ok bool)
```

SetUnencryptedHTTP2 adds or removes unencrypted HTTP/2 from p.

#### func (Protocols) String ¶ added in go1.24.0

```
func (p Protocols) String() string
```

#### func (Protocols) UnencryptedHTTP2 ¶ added in go1.24.0

```
func (p Protocols) UnencryptedHTTP2() bool
```

UnencryptedHTTP2 reports whether p includes unencrypted HTTP/2.

#### type PushOptions ¶ added in go1.8

```
type PushOptions struct {
	
	
	Method string

	
	
	
	Header Header
}
```

PushOptions describes options for Pusher.Push.

#### type Pusher ¶ added in go1.8

```
type Pusher interface {
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	Push(target string, opts *PushOptions) error
}
```

Pusher is the interface implemented by ResponseWriters that support HTTP/2 server push. For more background, see https://tools.ietf.org/html/rfc7540#section-8.2.

#### type Request

```
type Request struct {
	
	
	Method string

	
	
	
	
	
	
	
	
	
	
	
	
	URL *url.URL

	
	
	
	
	
	Proto      string 
	ProtoMajor int    
	ProtoMinor int    

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	Header Header

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	Body io.ReadCloser

	
	
	
	
	
	
	GetBody func() (io.ReadCloser, error)

	
	
	
	
	
	
	
	ContentLength int64

	
	
	
	
	
	TransferEncoding []string

	
	
	
	
	
	
	
	
	
	
	Close bool

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	Host string

	
	
	
	
	Form url.Values

	
	
	
	
	
	PostForm url.Values

	
	
	
	MultipartForm *multipart.Form

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	Trailer Header

	
	
	
	
	
	
	
	RemoteAddr string

	
	
	
	
	RequestURI string

	
	
	
	
	
	
	
	TLS *tls.ConnectionState

	
	
	
	
	
	
	
	
	
	Cancel <-chan struct{}

	
	
	
	Response *Response

	
	
	Pattern string
	
}
```

A Request represents an HTTP request received by a server or to be sent by a client.

The field semantics differ slightly between client and server usage. In addition to the notes on the fields below, see the documentation for Request.Write and RoundTripper.

#### func NewRequest

```
func NewRequest(method, url string, body io.Reader) (*Request, error)
```

NewRequest wraps NewRequestWithContext using context.Background.

#### func NewRequestWithContext ¶ added in go1.13

```
func NewRequestWithContext(ctx context.Context, method, url string, body io.Reader) (*Request, error)
```

NewRequestWithContext returns a new Request given a method, URL, and optional body.

If the provided body is also an io.Closer, the returned Request.Body is set to body and will be closed (possibly asynchronously) by the Client methods Do, Post, and PostForm, and Transport.RoundTrip.

NewRequestWithContext returns a Request suitable for use with Client.Do or Transport.RoundTrip. To create a request for use with testing a Server Handler, either use the net/http/httptest.NewRequest function, use ReadRequest, or manually update the Request fields. For an outgoing client request, the context controls the entire lifetime of a request and its response: obtaining a connection, sending the request, and reading the response headers and body. See the Request type's documentation for the difference between inbound and outbound request fields.

If body is of type *bytes.Buffer, *bytes.Reader, or *strings.Reader, the returned request's ContentLength is set to its exact value (instead of -1), GetBody is populated (so 307 and 308 redirects can replay the body), and Body is set to NoBody if the ContentLength is 0.

#### func ReadRequest

```
func ReadRequest(b *bufio.Reader) (*Request, error)
```

ReadRequest reads and parses an incoming request from b.

ReadRequest is a low-level function and should only be used for specialized applications; most code should use the Server to read requests and handle them via the Handler interface. ReadRequest only supports HTTP/1.x requests. For HTTP/2, use golang.org/x/net/http2.

#### func (*Request) AddCookie

```
func (r *Request) AddCookie(c *Cookie)
```

AddCookie adds a cookie to the request. Per RFC 6265 section 5.4, AddCookie does not attach more than one Cookie header field. That means all cookies, if any, are written into the same line, separated by semicolon. AddCookie only sanitizes c's name and value, and does not sanitize a Cookie header already present in the request.

#### func (*Request) BasicAuth ¶ added in go1.4

```
func (r *Request) BasicAuth() (username, password string, ok bool)
```

BasicAuth returns the username and password provided in the request's Authorization header, if the request uses HTTP Basic Authentication. See RFC 2617, Section 2.

#### func (*Request) Clone ¶ added in go1.13

```
func (r *Request) Clone(ctx context.Context) *Request
```

Clone returns a deep copy of r with its context changed to ctx. The provided ctx must be non-nil.

Clone only makes a shallow copy of the Body field.

For an outgoing client request, the context controls the entire lifetime of a request and its response: obtaining a connection, sending the request, and reading the response headers and body.

#### func (*Request) Context ¶ added in go1.7

```
func (r *Request) Context() context.Context
```

Context returns the request's context. To change the context, use Request.Clone or Request.WithContext.

The returned context is always non-nil; it defaults to the background context.

For outgoing client requests, the context controls cancellation.

For incoming server requests, the context is canceled when the client's connection closes, the request is canceled (with HTTP/2), or when the ServeHTTP method returns.

#### func (*Request) Cookie

```
func (r *Request) Cookie(name string) (*Cookie, error)
```

Cookie returns the named cookie provided in the request or ErrNoCookie if not found. If multiple cookies match the given name, only one cookie will be returned.

#### func (*Request) Cookies

```
func (r *Request) Cookies() []*Cookie
```

Cookies parses and returns the HTTP cookies sent with the request.

#### func (*Request) CookiesNamed ¶ added in go1.23.0

```
func (r *Request) CookiesNamed(name string) []*Cookie
```

CookiesNamed parses and returns the named HTTP cookies sent with the request or an empty slice if none matched.

#### func (*Request) FormFile

```
func (r *Request) FormFile(key string) (multipart.File, *multipart.FileHeader, error)
```

FormFile returns the first file for the provided form key. FormFile calls Request.ParseMultipartForm and Request.ParseForm if necessary.

#### func (*Request) FormValue

```
func (r *Request) FormValue(key string) string
```

FormValue returns the first value for the named component of the query. The precedence order:

1. application/x-www-form-urlencoded form body (POST, PUT, PATCH only)
2. query parameters (always)
3. multipart/form-data form body (always)

FormValue calls Request.ParseMultipartForm and Request.ParseForm if necessary and ignores any errors returned by these functions. If key is not present, FormValue returns the empty string. To access multiple values of the same key, call ParseForm and then inspect Request.Form directly.

#### func (*Request) MultipartReader

```
func (r *Request) MultipartReader() (*multipart.Reader, error)
```

MultipartReader returns a MIME multipart reader if this is a multipart/form-data or a multipart/mixed POST request, else returns nil and an error. Use this function instead of Request.ParseMultipartForm to process the request body as a stream.

#### func (*Request) ParseForm

```
func (r *Request) ParseForm() error
```

ParseForm populates r.Form and r.PostForm.

For all requests, ParseForm parses the raw query from the URL and updates r.Form.

For POST, PUT, and PATCH requests, it also reads the request body, parses it as a form and puts the results into both r.PostForm and r.Form. Request body parameters take precedence over URL query string values in r.Form.

If the request Body's size has not already been limited by MaxBytesReader, the size is capped at 10MB.

For other HTTP methods, or when the Content-Type is not application/x-www-form-urlencoded, the request Body is not read, and r.PostForm is initialized to a non-nil, empty value.

Request.ParseMultipartForm calls ParseForm automatically. ParseForm is idempotent.

#### func (*Request) ParseMultipartForm

```
func (r *Request) ParseMultipartForm(maxMemory int64) error
```

ParseMultipartForm parses a request body as multipart/form-data. The whole request body is parsed and up to a total of maxMemory bytes of its file parts are stored in memory, with the remainder stored on disk in temporary files. ParseMultipartForm calls Request.ParseForm if necessary. If ParseForm returns an error, ParseMultipartForm returns it but also continues parsing the request body. After one call to ParseMultipartForm, subsequent calls have no effect.

#### func (*Request) PathValue ¶ added in go1.22.0

```
func (r *Request) PathValue(name string) string
```

PathValue returns the value for the named path wildcard in the ServeMux pattern that matched the request. It returns the empty string if the request was not matched against a pattern or there is no such wildcard in the pattern.

#### func (*Request) PostFormValue ¶ added in go1.1

```
func (r *Request) PostFormValue(key string) string
```

PostFormValue returns the first value for the named component of the POST, PUT, or PATCH request body. URL query parameters are ignored. PostFormValue calls Request.ParseMultipartForm and Request.ParseForm if necessary and ignores any errors returned by these functions. If key is not present, PostFormValue returns the empty string.

#### func (*Request) ProtoAtLeast

```
func (r *Request) ProtoAtLeast(major, minor int) bool
```

ProtoAtLeast reports whether the HTTP protocol used in the request is at least major.minor.

#### func (*Request) Referer

```
func (r *Request) Referer() string
```

Referer returns the referring URL, if sent in the request.

Referer is misspelled as in the request itself, a mistake from the earliest days of HTTP. This value can also be fetched from the Header map as Header["Referer"]; the benefit of making it available as a method is that the compiler can diagnose programs that use the alternate (correct English) spelling req.Referrer() but cannot diagnose programs that use Header["Referrer"].

#### func (*Request) SetBasicAuth

```
func (r *Request) SetBasicAuth(username, password string)
```

SetBasicAuth sets the request's Authorization header to use HTTP Basic Authentication with the provided username and password.

With HTTP Basic Authentication the provided username and password are not encrypted. It should generally only be used in an HTTPS request.

The username may not contain a colon. Some protocols may impose additional requirements on pre-escaping the username and password. For instance, when used with OAuth2, both arguments must be URL encoded first with url.QueryEscape.

#### func (*Request) SetPathValue ¶ added in go1.22.0

```
func (r *Request) SetPathValue(name, value string)
```

SetPathValue sets name to value, so that subsequent calls to r.PathValue(name) return value.

#### func (*Request) UserAgent

```
func (r *Request) UserAgent() string
```

UserAgent returns the client's User-Agent, if sent in the request.

#### func (*Request) WithContext ¶ added in go1.7

```
func (r *Request) WithContext(ctx context.Context) *Request
```

WithContext returns a shallow copy of r with its context changed to ctx. The provided ctx must be non-nil.

For outgoing client request, the context controls the entire lifetime of a request and its response: obtaining a connection, sending the request, and reading the response headers and body.

To create a new request with a context, use NewRequestWithContext. To make a deep copy of a request with a new context, use Request.Clone.

#### func (*Request) Write

```
func (r *Request) Write(w io.Writer) error
```

Write writes an HTTP/1.1 request, which is the header and body, in wire format. This method consults the following fields of the request:

```
Host
URL
Method (defaults to "GET")
Header
ContentLength
TransferEncoding
Body
```

If Body is present, Content-Length is <= 0 and Request.TransferEncoding hasn't been set to "identity", Write adds "Transfer-Encoding: chunked" to the header. Body is closed after it is sent.

#### func (*Request) WriteProxy

```
func (r *Request) WriteProxy(w io.Writer) error
```

WriteProxy is like Request.Write but writes the request in the form expected by an HTTP proxy. In particular, Request.WriteProxy writes the initial Request-URI line of the request with an absolute URI, per section 5.3 of RFC 7230, including the scheme and host. In either case, WriteProxy also writes a Host header, using either r.Host or r.URL.Host.

#### type Response

```
type Response struct {
	Status     string 
	StatusCode int    
	Proto      string 
	ProtoMajor int    
	ProtoMinor int    

	
	
	
	
	
	
	
	
	
	Header Header

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	Body io.ReadCloser

	
	
	
	
	ContentLength int64

	
	
	TransferEncoding []string

	
	
	
	Close bool

	
	
	
	
	
	
	
	Uncompressed bool

	
	
	
	
	
	
	
	
	
	
	
	
	Trailer Header

	
	
	
	Request *Request

	
	
	
	
	TLS *tls.ConnectionState
}
```

Response represents the response from an HTTP request.

The Client and Transport return Responses from servers once the response headers have been received. The response body is streamed on demand as the Body field is read.

#### func Get

```
func Get(url string) (resp *Response, err error)
```

Get issues a GET to the specified URL. If the response is one of the following redirect codes, Get follows the redirect, up to a maximum of 10 redirects:

```
301 (Moved Permanently)
302 (Found)
303 (See Other)
307 (Temporary Redirect)
308 (Permanent Redirect)
```

An error is returned if there were too many redirects or if there was an HTTP protocol error. A non-2xx response doesn't cause an error. Any returned error will be of type *url.Error. The url.Error value's Timeout method will report true if the request timed out.

When err is nil, resp always contains a non-nil resp.Body. Caller should close resp.Body when done reading from it.

Get is a wrapper around DefaultClient.Get.

To make a request with custom headers, use NewRequest and DefaultClient.Do.

To make a request with a specified context.Context, use NewRequestWithContext and DefaultClient.Do.

Example

¶

```
package main

import (
	"fmt"
	"io"
	"log"
	"net/http"
)

func main() {
	res, err := http.Get("http://www.google.com/robots.txt")
	if err != nil {
		log.Fatal(err)
	}
	body, err := io.ReadAll(res.Body)
	res.Body.Close()
	if res.StatusCode > 299 {
		log.Fatalf("Response failed with status code: %d and\nbody: %s\n", res.StatusCode, body)
	}
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("%s", body)
}
```

```
Output:
```

#### func Head

```
func Head(url string) (resp *Response, err error)
```

Head issues a HEAD to the specified URL. If the response is one of the following redirect codes, Head follows the redirect, up to a maximum of 10 redirects:

```
301 (Moved Permanently)
302 (Found)
303 (See Other)
307 (Temporary Redirect)
308 (Permanent Redirect)
```

Head is a wrapper around DefaultClient.Head.

To make a request with a specified context.Context, use NewRequestWithContext and DefaultClient.Do.

#### func Post

```
func Post(url, contentType string, body io.Reader) (resp *Response, err error)
```

Post issues a POST to the specified URL.

Caller should close resp.Body when done reading from it.

If the provided body is an io.Closer, it is closed after the request.

Post is a wrapper around DefaultClient.Post.

To set custom headers, use NewRequest and DefaultClient.Do.

See the Client.Do method documentation for details on how redirects are handled.

To make a request with a specified context.Context, use NewRequestWithContext and DefaultClient.Do.

#### func PostForm

```
func PostForm(url string, data url.Values) (resp *Response, err error)
```

PostForm issues a POST to the specified URL, with data's keys and values URL-encoded as the request body.

The Content-Type header is set to application/x-www-form-urlencoded. To set other headers, use NewRequest and DefaultClient.Do.

When err is nil, resp always contains a non-nil resp.Body. Caller should close resp.Body when done reading from it.

PostForm is a wrapper around DefaultClient.PostForm.

See the Client.Do method documentation for details on how redirects are handled.
