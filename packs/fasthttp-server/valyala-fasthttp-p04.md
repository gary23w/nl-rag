---
title: "fasthttp package (part 4/5)"
source: https://pkg.go.dev/github.com/valyala/fasthttp
domain: fasthttp-server
license: CC-BY-SA-4.0
tags: fasthttp go server, golang high performance http, zero allocation http, fasthttp request context
fetched: 2026-07-02
part: 4/5
---

# fasthttp package

```
func (resp *Response) BodyInflate() ([]byte, error)
```

BodyInflate returns inflated body data.

This method may be used if the response header contains 'Content-Encoding: deflate' for reading inflated response body. Use Body for reading deflated response body.

#### func (*Response) BodyInflateWithLimit ¶ added in v1.70.0

```
func (resp *Response) BodyInflateWithLimit(maxBodySize int) ([]byte, error)
```

BodyInflateWithLimit returns inflated body data and limits the size of uncompressed body data to maxBodySize bytes.

If maxBodySize <= 0, then no limit is applied.

#### func (*Response) BodyStream ¶ added in v1.46.0

```
func (resp *Response) BodyStream() io.Reader
```

BodyStream returns io.Reader.

You must CloseBodyStream or ReleaseResponse after you use it.

#### func (*Response) BodyUnbrotli ¶ added in v1.13.0

```
func (resp *Response) BodyUnbrotli() ([]byte, error)
```

BodyUnbrotli returns un-brotlied body data.

This method may be used if the response header contains 'Content-Encoding: br' for reading un-brotlied body. Use Body for reading brotlied response body.

#### func (*Response) BodyUnbrotliWithLimit ¶ added in v1.70.0

```
func (resp *Response) BodyUnbrotliWithLimit(maxBodySize int) ([]byte, error)
```

BodyUnbrotliWithLimit returns un-brotlied body data and limits the size of uncompressed body data to maxBodySize bytes.

If maxBodySize <= 0, then no limit is applied.

#### func (*Response) BodyUncompressed ¶ added in v1.38.0

```
func (resp *Response) BodyUncompressed() ([]byte, error)
```

BodyUncompressed returns body data and if needed decompresses it from gzip, deflate, brotli or zstd.

This method may be used if the response header contains 'Content-Encoding' for reading uncompressed response body. Use Body for reading the raw response body.

#### func (*Response) BodyUncompressedWithLimit ¶ added in v1.70.0

```
func (resp *Response) BodyUncompressedWithLimit(maxBodySize int) ([]byte, error)
```

BodyUncompressedWithLimit returns body data and if needed decompresses it from gzip, deflate, brotli or zstd. The size of uncompressed data is limited to maxBodySize bytes.

If maxBodySize <= 0, then no limit is applied.

#### func (*Response) BodyUnzstd ¶ added in v1.53.0

```
func (resp *Response) BodyUnzstd() ([]byte, error)
```

#### func (*Response) BodyUnzstdWithLimit ¶ added in v1.70.0

```
func (resp *Response) BodyUnzstdWithLimit(maxBodySize int) ([]byte, error)
```

BodyUnzstdWithLimit returns un-zstd body data and limits the size of uncompressed body data to maxBodySize bytes.

If maxBodySize <= 0, then no limit is applied.

#### func (*Response) BodyWriteTo

```
func (resp *Response) BodyWriteTo(w io.Writer) error
```

BodyWriteTo writes response body to w.

#### func (*Response) BodyWriter

```
func (resp *Response) BodyWriter() io.Writer
```

BodyWriter returns writer for populating response body.

If used inside RequestHandler, the returned writer must not be used after returning from RequestHandler. Use RequestCtx.Write or SetBodyStreamWriter in this case.

#### func (*Response) CloseBodyStream ¶ added in v1.46.0

```
func (resp *Response) CloseBodyStream() error
```

#### func (*Response) ConnectionClose

```
func (resp *Response) ConnectionClose() bool
```

ConnectionClose returns true if 'Connection: close' header is set.

#### func (*Response) CopyTo

```
func (resp *Response) CopyTo(dst *Response)
```

CopyTo copies resp contents to dst except of body stream.

#### func (*Response) IsBodyStream

```
func (resp *Response) IsBodyStream() bool
```

IsBodyStream returns true if body is set via SetBodyStream*.

#### func (*Response) LocalAddr ¶ added in v1.2.0

```
func (resp *Response) LocalAddr() net.Addr
```

LocalAddr returns the local network address. The Addr returned is shared by all invocations of LocalAddr, so do not modify it.

#### func (*Response) ParseNetConn ¶ added in v1.59.0

```
func (resp *Response) ParseNetConn(conn net.Conn)
```

#### func (*Response) Read

```
func (resp *Response) Read(r *bufio.Reader) error
```

Read reads response (including body) from the given r.

io.EOF is returned if r is closed before reading the first header byte.

#### func (*Response) ReadBody ¶ added in v1.32.0

```
func (resp *Response) ReadBody(r *bufio.Reader, maxBodySize int) (err error)
```

ReadBody reads response body from the given r, limiting the body size.

If maxBodySize > 0 and the body size exceeds maxBodySize, then ErrBodyTooLarge is returned.

#### func (*Response) ReadLimitBody

```
func (resp *Response) ReadLimitBody(r *bufio.Reader, maxBodySize int) error
```

ReadLimitBody reads response headers from the given r, then reads the body using the ReadBody function and limiting the body size.

If resp.SkipBody is true then it skips reading the response body.

If maxBodySize > 0 and the body size exceeds maxBodySize, then ErrBodyTooLarge is returned.

io.EOF is returned if r is closed before reading the first header byte.

#### func (*Response) ReleaseBody

```
func (resp *Response) ReleaseBody(size int)
```

ReleaseBody retires the response body if it is greater than "size" bytes.

This permits GC to reclaim the large buffer. If used, must be before ReleaseResponse.

Use this method only if you really understand how it works. The majority of workloads don't need this method.

#### func (*Response) RemoteAddr ¶ added in v1.2.0

```
func (resp *Response) RemoteAddr() net.Addr
```

RemoteAddr returns the remote network address. The Addr returned is shared by all invocations of RemoteAddr, so do not modify it.

#### func (*Response) Reset

```
func (resp *Response) Reset()
```

Reset clears response contents.

#### func (*Response) ResetBody

```
func (resp *Response) ResetBody()
```

ResetBody resets response body.

#### func (*Response) SendFile

```
func (resp *Response) SendFile(path string) error
```

SendFile registers file on the given path to be used as response body when Write is called.

Note that SendFile doesn't set Content-Type, so set it yourself with Header.SetContentType.

#### func (*Response) SetBody

```
func (resp *Response) SetBody(body []byte)
```

SetBody sets response body.

It is safe re-using body argument after the function returns.

#### func (*Response) SetBodyRaw ¶ added in v1.3.0

```
func (resp *Response) SetBodyRaw(body []byte)
```

SetBodyRaw sets response body, but without copying it.

From this point onward the body argument must not be changed.

#### func (*Response) SetBodyStream

```
func (resp *Response) SetBodyStream(bodyStream io.Reader, bodySize int)
```

SetBodyStream sets response body stream and, optionally body size.

If bodySize is >= 0, then the bodyStream must provide exactly bodySize bytes before returning io.EOF.

If bodySize < 0, then bodyStream is read until io.EOF.

bodyStream.Close() is called after finishing reading all body data if it implements io.Closer.

See also SetBodyStreamWriter.

#### func (*Response) SetBodyStreamWriter

```
func (resp *Response) SetBodyStreamWriter(sw StreamWriter)
```

SetBodyStreamWriter registers the given sw for populating response body.

This function may be used in the following cases:

- if response body is too big (more than 10MB).
- if response body is streamed from slow external sources.
- if response body must be streamed to the client in chunks (aka `http server push` or `chunked transfer-encoding`).

See also SetBodyStream.

#### func (*Response) SetBodyString

```
func (resp *Response) SetBodyString(body string)
```

SetBodyString sets response body.

#### func (*Response) SetConnectionClose

```
func (resp *Response) SetConnectionClose()
```

SetConnectionClose sets 'Connection: close' header.

#### func (*Response) SetStatusCode

```
func (resp *Response) SetStatusCode(statusCode int)
```

SetStatusCode sets response status code.

#### func (*Response) StatusCode

```
func (resp *Response) StatusCode() int
```

StatusCode returns response status code.

#### func (*Response) String

```
func (resp *Response) String() string
```

String returns response representation.

Returns error message instead of response representation on error.

Use Write instead of String for performance-critical code.

#### func (*Response) SwapBody

```
func (resp *Response) SwapBody(body []byte) []byte
```

SwapBody swaps response body with the given body and returns the previous response body.

It is forbidden to use the body passed to SwapBody after the function returns.

#### func (*Response) Write

```
func (resp *Response) Write(w *bufio.Writer) error
```

Write writes response to w.

Write doesn't flush response to w for performance reasons.

See also WriteTo.

#### func (*Response) WriteDeflate

```
func (resp *Response) WriteDeflate(w *bufio.Writer) error
```

WriteDeflate writes response with deflated body to w.

The method deflates response body and sets 'Content-Encoding: deflate' header before writing response to w.

WriteDeflate doesn't flush response to w for performance reasons.

#### func (*Response) WriteDeflateLevel

```
func (resp *Response) WriteDeflateLevel(w *bufio.Writer, level int) error
```

WriteDeflateLevel writes response with deflated body to w.

Level is the desired compression level:

- CompressNoCompression
- CompressBestSpeed
- CompressBestCompression
- CompressDefaultCompression
- CompressHuffmanOnly

The method deflates response body and sets 'Content-Encoding: deflate' header before writing response to w.

WriteDeflateLevel doesn't flush response to w for performance reasons.

#### func (*Response) WriteGzip

```
func (resp *Response) WriteGzip(w *bufio.Writer) error
```

WriteGzip writes response with gzipped body to w.

The method gzips response body and sets 'Content-Encoding: gzip' header before writing response to w.

WriteGzip doesn't flush response to w for performance reasons.

#### func (*Response) WriteGzipLevel

```
func (resp *Response) WriteGzipLevel(w *bufio.Writer, level int) error
```

WriteGzipLevel writes response with gzipped body to w.

Level is the desired compression level:

- CompressNoCompression
- CompressBestSpeed
- CompressBestCompression
- CompressDefaultCompression
- CompressHuffmanOnly

The method gzips response body and sets 'Content-Encoding: gzip' header before writing response to w.

WriteGzipLevel doesn't flush response to w for performance reasons.

#### func (*Response) WriteTo

```
func (resp *Response) WriteTo(w io.Writer) (int64, error)
```

WriteTo writes response to w. It implements io.WriterTo.

#### type ResponseHeader

```
type ResponseHeader struct {
	
}
```

ResponseHeader represents HTTP response header.

It is forbidden copying ResponseHeader instances. Create new instances instead and use CopyTo.

ResponseHeader instance MUST NOT be used from concurrently running goroutines.

#### func (*ResponseHeader) Add

```
func (h *ResponseHeader) Add(key, value string)
```

Add adds the given 'key: value' header.

Multiple headers with the same key may be added with this function. Use Set for setting a single header for the given key.

the Content-Type, Content-Length, Connection, Server, Transfer-Encoding and Date headers can only be set once and will overwrite the previous value, while Set-Cookie will not clear previous cookies.

If the header is set as a Trailer (forbidden trailers will not be set, see AddTrailer for more details), it will be sent after the chunked response body.

#### func (*ResponseHeader) AddBytesK

```
func (h *ResponseHeader) AddBytesK(key []byte, value string)
```

AddBytesK adds the given 'key: value' header.

Multiple headers with the same key may be added with this function. Use SetBytesK for setting a single header for the given key.

the Content-Type, Content-Length, Connection, Server, Transfer-Encoding and Date headers can only be set once and will overwrite the previous value, while Set-Cookie will not clear previous cookies.

If the header is set as a Trailer (forbidden trailers will not be set, see AddTrailer for more details), it will be sent after the chunked response body.

#### func (*ResponseHeader) AddBytesKV

```
func (h *ResponseHeader) AddBytesKV(key, value []byte)
```

AddBytesKV adds the given 'key: value' header.

Multiple headers with the same key may be added with this function. Use SetBytesKV for setting a single header for the given key.

the Content-Type, Content-Length, Connection, Server, Transfer-Encoding and Date headers can only be set once and will overwrite the previous value, while the Set-Cookie header will not clear previous cookies.

If the header is set as a Trailer (forbidden trailers will not be set, see AddTrailer for more details), it will be sent after the chunked response body.

#### func (*ResponseHeader) AddBytesV

```
func (h *ResponseHeader) AddBytesV(key string, value []byte)
```

AddBytesV adds the given 'key: value' header.

Multiple headers with the same key may be added with this function. Use SetBytesV for setting a single header for the given key.

the Content-Type, Content-Length, Connection, Server, Transfer-Encoding and Date headers can only be set once and will overwrite the previous value, while Set-Cookie will not clear previous cookies.

If the header is set as a Trailer (forbidden trailers will not be set, see AddTrailer for more details), it will be sent after the chunked response body.

#### func (*ResponseHeader) AddTrailer ¶ added in v1.32.0

```
func (h *ResponseHeader) AddTrailer(trailer string) error
```

AddTrailer add Trailer header value for chunked response to indicate which headers will be sent after the body.

Use Set to set the trailer header later.

Trailers are only supported with chunked transfer. Trailers allow the sender to include additional headers at the end of chunked messages.

The following trailers are forbidden: 1. necessary for message framing (e.g., Transfer-Encoding and Content-Length), 2. routing (e.g., Host), 3. request modifiers (e.g., controls and conditionals in Section 5 of [RFC7231]), 4. authentication (e.g., see [RFC7235] and [RFC6265]), 5. response control data (e.g., see Section 7.1 of [RFC7231]), 6. determining how to process the payload (e.g., Content-Encoding, Content-Type, Content-Range, and Trailer)

Return ErrBadTrailer if contain any forbidden trailers.

#### func (*ResponseHeader) AddTrailerBytes ¶ added in v1.32.0

```
func (h *ResponseHeader) AddTrailerBytes(trailer []byte) (err error)
```

AddTrailerBytes add Trailer header value for chunked response to indicate which headers will be sent after the body.

Use Set to set the trailer header later.

Trailers are only supported with chunked transfer. Trailers allow the sender to include additional headers at the end of chunked messages.

The following trailers are forbidden: 1. necessary for message framing (e.g., Transfer-Encoding and Content-Length), 2. routing (e.g., Host), 3. request modifiers (e.g., controls and conditionals in Section 5 of [RFC7231]), 4. authentication (e.g., see [RFC7235] and [RFC6265]), 5. response control data (e.g., see Section 7.1 of [RFC7231]), 6. determining how to process the payload (e.g., Content-Encoding, Content-Type, Content-Range, and Trailer)

Return ErrBadTrailer if contain any forbidden trailers.

#### func (*ResponseHeader) All ¶ added in v1.63.0

```
func (h *ResponseHeader) All() iter.Seq2[[]byte, []byte]
```

All returns an iterator over key-value pairs in h.

The key and value may invalid outside the iteration loop. Copy key and/or value contents for each iteration if you need retaining them.

Making modifications to the ResponseHeader during the iteration loop leads to undefined behavior and can cause panics.

#### func (*ResponseHeader) AppendBytes

```
func (h *ResponseHeader) AppendBytes(dst []byte) []byte
```

AppendBytes appends response header representation to dst and returns the extended dst.

#### func (*ResponseHeader) ConnectionClose

```
func (h *ResponseHeader) ConnectionClose() bool
```

ConnectionClose returns true if 'Connection: close' header is set.

#### func (*ResponseHeader) ConnectionUpgrade

```
func (h *ResponseHeader) ConnectionUpgrade() bool
```

ConnectionUpgrade returns true if 'Connection: Upgrade' header is set.

#### func (*ResponseHeader) ContentEncoding ¶ added in v1.38.0

```
func (h *ResponseHeader) ContentEncoding() []byte
```

ContentEncoding returns Content-Encoding header value.

#### func (*ResponseHeader) ContentLength

```
func (h *ResponseHeader) ContentLength() int
```

ContentLength returns Content-Length header value.

It may be negative: -1 means Transfer-Encoding: chunked. -2 means Transfer-Encoding: identity.

#### func (*ResponseHeader) ContentType

```
func (h *ResponseHeader) ContentType() []byte
```

ContentType returns Content-Type header value.

#### func (*ResponseHeader) Cookie

```
func (h *ResponseHeader) Cookie(cookie *Cookie) bool
```

Cookie fills cookie for the given cookie.Key.

Returns false if cookie with the given cookie.Key is missing.

#### func (*ResponseHeader) Cookies ¶ added in v1.63.0

```
func (h *ResponseHeader) Cookies() iter.Seq2[[]byte, []byte]
```

Cookies returns an iterator over key-value paired response cookie in h.

Cookie name is passed in key and the whole Set-Cookie header value is passed in value for each iteration. Value may be parsed with Cookie.ParseBytes().

The key and value may invalid outside the iteration loop. Copy key and/or value contents for each iteration if you need retaining them.

Making modifications to the ResponseHeader during the iteration loop leads to undefined behavior and can cause panics.

#### func (*ResponseHeader) CopyTo

```
func (h *ResponseHeader) CopyTo(dst *ResponseHeader)
```

CopyTo copies all the headers to dst.

#### func (*ResponseHeader) Del

```
func (h *ResponseHeader) Del(key string)
```

Del deletes header with the given key.

#### func (*ResponseHeader) DelAllCookies

```
func (h *ResponseHeader) DelAllCookies()
```

DelAllCookies removes all the cookies from response headers.

#### func (*ResponseHeader) DelBytes

```
func (h *ResponseHeader) DelBytes(key []byte)
```

DelBytes deletes header with the given key.

#### func (*ResponseHeader) DelClientCookie

```
func (h *ResponseHeader) DelClientCookie(key string)
```

DelClientCookie instructs the client to remove the given cookie. This doesn't work for a cookie with specific domain or path, you should delete it manually like:

```
c := AcquireCookie()
c.SetKey(key)
c.SetDomain("example.com")
c.SetPath("/path")
c.SetExpire(CookieExpireDelete)
h.SetCookie(c)
ReleaseCookie(c)
```

Use DelCookie if you want just removing the cookie from response header.

#### func (*ResponseHeader) DelClientCookieBytes

```
func (h *ResponseHeader) DelClientCookieBytes(key []byte)
```

DelClientCookieBytes instructs the client to remove the given cookie. This doesn't work for a cookie with specific domain or path, you should delete it manually like:

```
c := AcquireCookie()
c.SetKey(key)
c.SetDomain("example.com")
c.SetPath("/path")
c.SetExpire(CookieExpireDelete)
h.SetCookie(c)
ReleaseCookie(c)
```

Use DelCookieBytes if you want just removing the cookie from response header.

#### func (*ResponseHeader) DelCookie

```
func (h *ResponseHeader) DelCookie(key string)
```

DelCookie removes cookie under the given key from response header.

Note that DelCookie doesn't remove the cookie from the client. Use DelClientCookie instead.

#### func (*ResponseHeader) DelCookieBytes

```
func (h *ResponseHeader) DelCookieBytes(key []byte)
```

DelCookieBytes removes cookie under the given key from response header.

Note that DelCookieBytes doesn't remove the cookie from the client. Use DelClientCookieBytes instead.

#### func (*ResponseHeader) DisableNormalizing

```
func (h *ResponseHeader) DisableNormalizing() bool
```

DisableNormalizing disables header names' normalization.

By default all the header names are normalized by uppercasing the first letter and all the first letters following dashes, while lowercasing all the other letters. Examples:

- CONNECTION -> Connection
- conteNT-tYPE -> Content-Type
- foo-bar-baz -> Foo-Bar-Baz

Disable header names' normalization only if know what are you doing. The previous setting is returned.

#### func (*ResponseHeader) EnableNormalizing ¶ added in v1.16.0

```
func (h *ResponseHeader) EnableNormalizing() bool
```

EnableNormalizing enables header names' normalization.

Header names are normalized by uppercasing the first letter and all the first letters following dashes, while lowercasing all the other letters. Examples:

- CONNECTION -> Connection
- conteNT-tYPE -> Content-Type
- foo-bar-baz -> Foo-Bar-Baz

This is enabled by default unless disabled using DisableNormalizing(). The previous setting is returned.

#### func (*ResponseHeader) Header

```
func (h *ResponseHeader) Header() []byte
```

Header returns response header representation.

Headers that set as Trailer will not represent. Use TrailerHeader for trailers.

The returned value is valid until the request is released, either though ReleaseRequest or your request handler returning. Do not store references to returned value. Make copies instead.

#### func (*ResponseHeader) IsHTTP11

```
func (h *ResponseHeader) IsHTTP11() bool
```

IsHTTP11 returns true if the header is HTTP/1.1.

#### func (*ResponseHeader) Len

```
func (h *ResponseHeader) Len() int
```

Len returns the number of headers set, i.e. the number of times f is called in VisitAll.

#### func (*ResponseHeader) Peek

```
func (h *ResponseHeader) Peek(key string) []byte
```

Peek returns header value for the given key.

The returned value is valid until the response is released, either though ReleaseResponse or your request handler returning. Do not store references to the returned value. Make copies instead.

#### func (*ResponseHeader) PeekAll ¶ added in v1.41.0

```
func (h *ResponseHeader) PeekAll(key string) [][]byte
```

PeekAll returns all header value for the given key.

The returned value is valid until the request is released, either though ReleaseResponse or your request handler returning. Any future calls to the Peek* will modify the returned value. Do not store references to returned value. Make copies instead.

#### func (*ResponseHeader) PeekBytes

```
func (h *ResponseHeader) PeekBytes(key []byte) []byte
```

PeekBytes returns header value for the given key.

The returned value is valid until the response is released, either though ReleaseResponse or your request handler returning. Do not store references to returned value. Make copies instead.

#### func (*ResponseHeader) PeekCookie ¶ added in v1.0.0

```
func (h *ResponseHeader) PeekCookie(key string) []byte
```

PeekCookie is able to returns cookie by a given key from response.

#### func (*ResponseHeader) PeekKeys ¶ added in v1.42.0

```
func (h *ResponseHeader) PeekKeys() [][]byte
```

PeekKeys return all header keys.

The returned value is valid until the request is released, either though ReleaseRequest or your request handler returning. Any future calls to the Peek* will modify the returned value. Do not store references to returned value. Make copies instead.

#### func (*ResponseHeader) PeekTrailerKeys ¶ added in v1.42.0

```
func (h *ResponseHeader) PeekTrailerKeys() [][]byte
```

PeekTrailerKeys return all trailer keys.

The returned value is valid until the request is released, either though ReleaseResponse or your request handler returning. Any future calls to the Peek* will modify the returned value. Do not store references to returned value. Make copies instead.

#### func (*ResponseHeader) Protocol ¶ added in v1.32.0

```
func (h *ResponseHeader) Protocol() []byte
```

Protocol returns HTTP protocol.

#### func (*ResponseHeader) Read

```
func (h *ResponseHeader) Read(r *bufio.Reader) error
```

Read reads response header from r.

io.EOF is returned if r is closed before reading the first header byte.

#### func (*ResponseHeader) ReadTrailer ¶ added in v1.32.0

```
func (h *ResponseHeader) ReadTrailer(r *bufio.Reader) error
```

ReadTrailer reads response trailer header from r.

io.EOF is returned if r is closed before reading the first byte.

#### func (*ResponseHeader) Reset

```
func (h *ResponseHeader) Reset()
```

Reset clears response header.

#### func (*ResponseHeader) ResetConnectionClose

```
func (h *ResponseHeader) ResetConnectionClose()
```

ResetConnectionClose clears 'Connection: close' header if it exists.

#### func (*ResponseHeader) Server

```
func (h *ResponseHeader) Server() []byte
```

Server returns Server header value.

#### func (*ResponseHeader) Set

```
func (h *ResponseHeader) Set(key, value string)
```

Set sets the given 'key: value' header.

Please note that the Set-Cookie header will not clear previous cookies, use SetCookie instead to reset cookies.

If the header is set as a Trailer (forbidden trailers will not be set, see SetTrailer for more details), it will be sent after the chunked response body.

Use Add for setting multiple header values under the same key.

#### func (*ResponseHeader) SetBytesK

```
func (h *ResponseHeader) SetBytesK(key []byte, value string)
```

SetBytesK sets the given 'key: value' header.

Please note that the Set-Cookie header will not clear previous cookies, use SetCookie instead to reset cookies.

If the header is set as a Trailer (forbidden trailers will not be set, see SetTrailer for more details), it will be sent after the chunked response body.

Use AddBytesK for setting multiple header values under the same key.

#### func (*ResponseHeader) SetBytesKV

```
func (h *ResponseHeader) SetBytesKV(key, value []byte)
```

SetBytesKV sets the given 'key: value' header.

Please note that the Set-Cookie header will not clear previous cookies, use SetCookie instead to reset cookies.

If the header is set as a Trailer (forbidden trailers will not be set, see SetTrailer for more details), it will be sent after the chunked response body.

Use AddBytesKV for setting multiple header values under the same key.

#### func (*ResponseHeader) SetBytesV

```
func (h *ResponseHeader) SetBytesV(key string, value []byte)
```

SetBytesV sets the given 'key: value' header.

Please note that the Set-Cookie header will not clear previous cookies, use SetCookie instead to reset cookies.

If the header is set as a Trailer (forbidden trailers will not be set, see SetTrailer for more details), it will be sent after the chunked response body.

Use AddBytesV for setting multiple header values under the same key.

#### func (*ResponseHeader) SetCanonical

```
func (h *ResponseHeader) SetCanonical(key, value []byte)
```

SetCanonical sets the given 'key: value' header assuming that key is in canonical form.

Please note that the Set-Cookie header will not clear previous cookies, use SetCookie instead to reset cookies.

If the header is set as a Trailer (forbidden trailers will not be set, see SetTrailer for more details), it will be sent after the chunked response body.

#### func (*ResponseHeader) SetConnectionClose

```
func (h *ResponseHeader) SetConnectionClose()
```

SetConnectionClose sets 'Connection: close' header.

#### func (*ResponseHeader) SetContentEncoding ¶ added in v1.38.0

```
func (h *ResponseHeader) SetContentEncoding(contentEncoding string)
```

SetContentEncoding sets Content-Encoding header value.

#### func (*ResponseHeader) SetContentEncodingBytes ¶ added in v1.38.0

```
func (h *ResponseHeader) SetContentEncodingBytes(contentEncoding []byte)
```

SetContentEncodingBytes sets Content-Encoding header value.

#### func (*ResponseHeader) SetContentLength

```
func (h *ResponseHeader) SetContentLength(contentLength int)
```

SetContentLength sets Content-Length header value.

Content-Length may be negative: -1 means Transfer-Encoding: chunked. -2 means Transfer-Encoding: identity.

#### func (*ResponseHeader) SetContentRange

```
func (h *ResponseHeader) SetContentRange(startPos, endPos, contentLength int)
```

SetContentRange sets 'Content-Range: bytes startPos-endPos/contentLength' header.

#### func (*ResponseHeader) SetContentType

```
func (h *ResponseHeader) SetContentType(contentType string)
```

SetContentType sets Content-Type header value.

#### func (*ResponseHeader) SetContentTypeBytes

```
func (h *ResponseHeader) SetContentTypeBytes(contentType []byte)
```

SetContentTypeBytes sets Content-Type header value.

#### func (*ResponseHeader) SetCookie

```
func (h *ResponseHeader) SetCookie(cookie *Cookie)
```

SetCookie sets the given response cookie.

It is safe re-using the cookie after the function returns.

#### func (*ResponseHeader) SetLastModified

```
func (h *ResponseHeader) SetLastModified(t time.Time)
```

SetLastModified sets 'Last-Modified' header to the given value.

#### func (*ResponseHeader) SetNoDefaultContentType ¶ added in v1.16.0

```
func (h *ResponseHeader) SetNoDefaultContentType(noDefaultContentType bool)
```

SetNoDefaultContentType allows you to control if a default Content-Type header will be set (false) or not (true).

#### func (*ResponseHeader) SetProtocol ¶ added in v1.32.0

```
func (h *ResponseHeader) SetProtocol(protocol []byte)
```

SetProtocol sets response protocol bytes.

#### func (*ResponseHeader) SetServer

```
func (h *ResponseHeader) SetServer(server string)
```

SetServer sets Server header value.

#### func (*ResponseHeader) SetServerBytes
