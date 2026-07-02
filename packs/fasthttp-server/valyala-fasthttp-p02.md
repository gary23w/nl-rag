---
title: "fasthttp package (part 2/5)"
source: https://pkg.go.dev/github.com/valyala/fasthttp
domain: fasthttp-server
license: CC-BY-SA-4.0
tags: fasthttp go server, golang high performance http, zero allocation http, fasthttp request context
fetched: 2026-07-02
part: 2/5
---

## Documentation

### Overview

Package fasthttp provides fast HTTP server and client API.

Fasthttp provides the following features:

1. Optimized for speed. Easily handles more than 100K qps and more than 1M concurrent keep-alive connections on modern hardware.
2. Optimized for low memory usage.
3. Easy 'Connection: Upgrade' support via RequestCtx.Hijack.
4. Server provides the following anti-DoS limits: - The number of concurrent connections. - The number of concurrent connections per client IP. - The number of requests per connection. - Request read timeout. - Response write timeout. - Maximum request header size. - Maximum request body size. - Maximum request execution time. - Maximum keep-alive connection lifetime. - Early filtering out non-GET requests.
5. A lot of additional useful info is exposed to request handler: - Server and client address. - Per-request logger. - Unique request id. - Request start time. - Connection start time. - Request sequence number for the current connection.
6. Client supports automatic retry on idempotent requests' failure.
7. Fasthttp API is designed with the ability to extend existing client and server implementations or to write custom client and server implementations from scratch.

### Index

- Constants
- Variables
- func AcquireTimer(timeout time.Duration) *time.Timer
- func AddMissingPort(addr string, isTLS bool) string
- func AppendBrotliBytes(dst, src []byte) []byte
- func AppendBrotliBytesLevel(dst, src []byte, level int) []byte
- func AppendDeflateBytes(dst, src []byte) []byte
- func AppendDeflateBytesLevel(dst, src []byte, level int) []byte
- func AppendGunzipBytes(dst, src []byte) ([]byte, error)
- func AppendGzipBytes(dst, src []byte) []byte
- func AppendGzipBytesLevel(dst, src []byte, level int) []byte
- func AppendHTMLEscape(dst []byte, s string) []byte
- func AppendHTMLEscapeBytes(dst, s []byte) []byte
- func AppendHTTPDate(dst []byte, date time.Time) []byte
- func AppendIPv4(dst []byte, ip net.IP) []byte
- func AppendInflateBytes(dst, src []byte) ([]byte, error)
- func AppendNormalizedHeaderKey(dst []byte, key string) []byte
- func AppendNormalizedHeaderKeyBytes(dst, key []byte) []byte
- func AppendQuotedArg(dst, src []byte) []byte
- func AppendUint(dst []byte, n int) []byte
- func AppendUnbrotliBytes(dst, src []byte) ([]byte, error)
- func AppendUnquotedArg(dst, src []byte) []byte
- func AppendUnzstdBytes(dst, src []byte) ([]byte, error)
- func AppendZstdBytes(dst, src []byte) []byte
- func AppendZstdBytesLevel(dst, src []byte, level int) []byte
- func CoarseTimeNow() time.Timedeprecated
- func Dial(addr string) (net.Conn, error)
- func DialDualStack(addr string) (net.Conn, error)
- func DialDualStackTimeout(addr string, timeout time.Duration) (net.Conn, error)
- func DialTimeout(addr string, timeout time.Duration) (net.Conn, error)
- func Do(req *Request, resp *Response) error
- func DoDeadline(req *Request, resp *Response, deadline time.Time) error
- func DoRedirects(req *Request, resp *Response, maxRedirectsCount int) error
- func DoTimeout(req *Request, resp *Response, timeout time.Duration) error
- func FileLastModified(path string) (time.Time, error)
- func FlushDNSCache()
- func GenerateTestCertificate(host string) ([]byte, []byte, error)
- func Get(dst []byte, url string) (statusCode int, body []byte, err error)
- func GetDeadline(dst []byte, url string, deadline time.Time) (statusCode int, body []byte, err error)
- func GetTimeout(dst []byte, url string, timeout time.Duration) (statusCode int, body []byte, err error)
- func ListenAndServe(addr string, handler RequestHandler) error
- func ListenAndServeTLS(addr, certFile, keyFile string, handler RequestHandler) error
- func ListenAndServeTLSEmbed(addr string, certData, keyData []byte, handler RequestHandler) error
- func ListenAndServeUNIX(addr string, mode os.FileMode, handler RequestHandler) error
- func NewStreamReader(sw StreamWriter) io.ReadCloser
- func ParseByteRange(byteRange []byte, contentLength int) (startPos, endPos int, err error)
- func ParseHTTPDate(date []byte) (time.Time, error)
- func ParseIPv4(dst net.IP, ipStr []byte) (net.IP, error)
- func ParseUfloat(buf []byte) (float64, error)
- func ParseUint(buf []byte) (int, error)
- func Post(dst []byte, url string, postArgs *Args) (statusCode int, body []byte, err error)
- func ReleaseArgs(a *Args)
- func ReleaseCookie(c *Cookie)
- func ReleaseRequest(req *Request)
- func ReleaseResponse(resp *Response)
- func ReleaseTimer(t *time.Timer)
- func ReleaseURI(u *URI)
- func SaveMultipartFile(fh *multipart.FileHeader, path string) (err error)
- func Serve(ln net.Listener, handler RequestHandler) error
- func ServeConn(c net.Conn, handler RequestHandler) error
- func ServeFS(ctx *RequestCtx, filesystem fs.FS, path string)
- func ServeFSLiteral(ctx *RequestCtx, filesystem fs.FS, path string)
- func ServeFile(ctx *RequestCtx, path string)
- func ServeFileBytes(ctx *RequestCtx, path []byte)
- func ServeFileBytesUncompressed(ctx *RequestCtx, path []byte)
- func ServeFileLiteral(ctx *RequestCtx, path string)
- func ServeFileUncompressed(ctx *RequestCtx, path string)
- func ServeTLS(ln net.Listener, certFile, keyFile string, handler RequestHandler) error
- func ServeTLSEmbed(ln net.Listener, certData, keyData []byte, handler RequestHandler) error
- func SetBodySizePoolLimit(reqBodyLimit, respBodyLimit int)
- func StatusCodeIsRedirect(statusCode int) bool
- func StatusMessage(statusCode int) string
- func VisitHeaderParams(b []byte, f func(key, value []byte) bool)
- func WriteBrotli(w io.Writer, p []byte) (int, error)
- func WriteBrotliLevel(w io.Writer, p []byte, level int) (int, error)
- func WriteDeflate(w io.Writer, p []byte) (int, error)
- func WriteDeflateLevel(w io.Writer, p []byte, level int) (int, error)
- func WriteGunzip(w io.Writer, p []byte) (int, error)
- func WriteGzip(w io.Writer, p []byte) (int, error)
- func WriteGzipLevel(w io.Writer, p []byte, level int) (int, error)
- func WriteInflate(w io.Writer, p []byte) (int, error)
- func WriteMultipartForm(w io.Writer, f *multipart.Form, boundary string) error
- func WriteUnbrotli(w io.Writer, p []byte) (int, error)
- func WriteUnzstd(w io.Writer, p []byte) (int, error)
- func WriteZstdLevel(w io.Writer, p []byte, level int) (int, error)
- type Args
  - func AcquireArgs() *Args
  - func (a *Args) Add(key, value string)
  - func (a *Args) AddBytesK(key []byte, value string)
  - func (a *Args) AddBytesKNoValue(key []byte)
  - func (a *Args) AddBytesKV(key, value []byte)
  - func (a *Args) AddBytesV(key string, value []byte)
  - func (a *Args) AddNoValue(key string)
  - func (a *Args) All() iter.Seq2[[]byte, []byte]
  - func (a *Args) AppendBytes(dst []byte) []byte
  - func (a *Args) CopyTo(dst *Args)
  - func (a *Args) Del(key string)
  - func (a *Args) DelBytes(key []byte)
  - func (a *Args) GetBool(key string) bool
  - func (a *Args) GetUfloat(key string) (float64, error)
  - func (a *Args) GetUfloatOrZero(key string) float64
  - func (a *Args) GetUint(key string) (int, error)
  - func (a *Args) GetUintOrZero(key string) int
  - func (a *Args) Has(key string) bool
  - func (a *Args) HasBytes(key []byte) bool
  - func (a *Args) Len() int
  - func (a *Args) Parse(s string)
  - func (a *Args) ParseBytes(b []byte)
  - func (a *Args) Peek(key string) []byte
  - func (a *Args) PeekBytes(key []byte) []byte
  - func (a *Args) PeekMulti(key string) [][]byte
  - func (a *Args) PeekMultiBytes(key []byte) [][]byte
  - func (a *Args) QueryString() []byte
  - func (a *Args) Reset()
  - func (a *Args) Set(key, value string)
  - func (a *Args) SetBytesK(key []byte, value string)
  - func (a *Args) SetBytesKNoValue(key []byte)
  - func (a *Args) SetBytesKV(key, value []byte)
  - func (a *Args) SetBytesV(key string, value []byte)
  - func (a *Args) SetNoValue(key string)
  - func (a *Args) SetUint(key string, value int)
  - func (a *Args) SetUintBytes(key []byte, value int)
  - func (a *Args) Sort(f func(x, y []byte) int)
  - func (a *Args) SortKeys(f func(x, y []byte) int)
  - func (a *Args) String() string
  - func (a *Args) VisitAll(f func(key, value []byte))deprecated
  - func (a *Args) WriteTo(w io.Writer) (int64, error)
- type BalancingClient
- type CacheKind
- type Client
  - func (c *Client) CloseIdleConnections()
  - func (c *Client) ConnsCount() int
  - func (c *Client) Do(req *Request, resp *Response) error
  - func (c *Client) DoDeadline(req *Request, resp *Response, deadline time.Time) error
  - func (c *Client) DoRedirects(req *Request, resp *Response, maxRedirectsCount int) error
  - func (c *Client) DoTimeout(req *Request, resp *Response, timeout time.Duration) error
  - func (c *Client) Get(dst []byte, url string) (statusCode int, body []byte, err error)
  - func (c *Client) GetDeadline(dst []byte, url string, deadline time.Time) (statusCode int, body []byte, err error)
  - func (c *Client) GetTimeout(dst []byte, url string, timeout time.Duration) (statusCode int, body []byte, err error)
  - func (c *Client) IdleConnsCount() int
  - func (c *Client) Post(dst []byte, url string, postArgs *Args) (statusCode int, body []byte, err error)
- type ConnPoolStrategyType
- type ConnState
  - func (c ConnState) String() string
- type Cookie
  - func AcquireCookie() *Cookie
  - func (c *Cookie) AppendBytes(dst []byte) []byte
  - func (c *Cookie) Cookie() []byte
  - func (c *Cookie) CopyTo(src *Cookie)
  - func (c *Cookie) Domain() []byte
  - func (c *Cookie) Expire() time.Time
  - func (c *Cookie) HTTPOnly() bool
  - func (c *Cookie) Key() []byte
  - func (c *Cookie) MaxAge() int
  - func (c *Cookie) Parse(src string) error
  - func (c *Cookie) ParseBytes(src []byte) error
  - func (c *Cookie) Partitioned() bool
  - func (c *Cookie) Path() []byte
  - func (c *Cookie) Reset()
  - func (c *Cookie) SameSite() CookieSameSite
  - func (c *Cookie) Secure() bool
  - func (c *Cookie) SetDomain(domain string)
  - func (c *Cookie) SetDomainBytes(domain []byte)
  - func (c *Cookie) SetExpire(expire time.Time)
  - func (c *Cookie) SetHTTPOnly(httpOnly bool)
  - func (c *Cookie) SetKey(key string)
  - func (c *Cookie) SetKeyBytes(key []byte)
  - func (c *Cookie) SetMaxAge(seconds int)
  - func (c *Cookie) SetPartitioned(partitioned bool)
  - func (c *Cookie) SetPath(path string)
  - func (c *Cookie) SetPathBytes(path []byte)
  - func (c *Cookie) SetSameSite(mode CookieSameSite)
  - func (c *Cookie) SetSecure(secure bool)
  - func (c *Cookie) SetValue(value string)
  - func (c *Cookie) SetValueBytes(value []byte)
  - func (c *Cookie) String() string
  - func (c *Cookie) Value() []byte
  - func (c *Cookie) WriteTo(w io.Writer) (int64, error)
- type CookieSameSite
- type DialFunc
- type DialFuncWithTimeout
- type ErrBodyStreamWritePanic
- type ErrBrokenChunk
- type ErrDialWithUpstream
  - func (e *ErrDialWithUpstream) Error() string
  - func (e *ErrDialWithUpstream) Unwrap() error
- type ErrNothingRead
- type ErrSmallBuffer
- type EscapeError
  - func (e EscapeError) Error() string
- type FS
  - func (fs *FS) NewRequestHandler() RequestHandler
- type FormValueFunc
- type HijackHandler
- type HostClient
  - func (c *HostClient) AcquireConn(reqTimeout time.Duration, connectionClose bool) (cc *clientConn, err error)
  - func (c *HostClient) AcquireReader(conn net.Conn) *bufio.Reader
  - func (c *HostClient) AcquireWriter(conn net.Conn) *bufio.Writer
  - func (c *HostClient) CloseConn(cc *clientConn)
  - func (c *HostClient) CloseIdleConnections()
  - func (c *HostClient) ConnsCount() int
  - func (c *HostClient) Do(req *Request, resp *Response) error
  - func (c *HostClient) DoDeadline(req *Request, resp *Response, deadline time.Time) error
  - func (c *HostClient) DoRedirects(req *Request, resp *Response, maxRedirectsCount int) error
  - func (c *HostClient) DoTimeout(req *Request, resp *Response, timeout time.Duration) error
  - func (c *HostClient) Get(dst []byte, url string) (statusCode int, body []byte, err error)
  - func (c *HostClient) GetDeadline(dst []byte, url string, deadline time.Time) (statusCode int, body []byte, err error)
  - func (c *HostClient) GetTimeout(dst []byte, url string, timeout time.Duration) (statusCode int, body []byte, err error)
  - func (c *HostClient) IdleConnsCount() int
  - func (c *HostClient) LastUseTime() time.Time
  - func (c *HostClient) PendingRequests() int
  - func (c *HostClient) Post(dst []byte, url string, postArgs *Args) (statusCode int, body []byte, err error)
  - func (c *HostClient) ReleaseConn(cc *clientConn)
  - func (c *HostClient) ReleaseReader(br *bufio.Reader)
  - func (c *HostClient) ReleaseWriter(bw *bufio.Writer)
  - func (c *HostClient) SetMaxConns(newMaxConns int)
- type InvalidHostError
  - func (e InvalidHostError) Error() string
- type LBClient
  - func (cc *LBClient) AddClient(c BalancingClient) int
  - func (cc *LBClient) Do(req *Request, resp *Response) error
  - func (cc *LBClient) DoDeadline(req *Request, resp *Response, deadline time.Time) error
  - func (cc *LBClient) DoTimeout(req *Request, resp *Response, timeout time.Duration) error
  - func (cc *LBClient) RemoveClients(rc func(BalancingClient) bool) int
- type Logger
- type PathRewriteFunc
  - func NewPathPrefixStripper(prefixSize int) PathRewriteFunc
  - func NewPathSlashesStripper(slashesCount int) PathRewriteFunc
  - func NewVHostPathRewriter(slashesCount int) PathRewriteFunc
- type PipelineClient
  - func (c *PipelineClient) Do(req *Request, resp *Response) error
  - func (c *PipelineClient) DoDeadline(req *Request, resp *Response, deadline time.Time) error
  - func (c *PipelineClient) DoTimeout(req *Request, resp *Response, timeout time.Duration) error
  - func (c *PipelineClient) PendingRequests() int
- type ReadCloserWithError
- type Request
  - func AcquireRequest() *Request
  - func (req *Request) AppendBody(p []byte)
  - func (req *Request) AppendBodyString(s string)
  - func (req *Request) Body() []byte
  - func (req *Request) BodyGunzip() ([]byte, error)
  - func (req *Request) BodyGunzipWithLimit(maxBodySize int) ([]byte, error)
  - func (req *Request) BodyInflate() ([]byte, error)
  - func (req *Request) BodyInflateWithLimit(maxBodySize int) ([]byte, error)
  - func (req *Request) BodyStream() io.Reader
  - func (req *Request) BodyUnbrotli() ([]byte, error)
  - func (req *Request) BodyUnbrotliWithLimit(maxBodySize int) ([]byte, error)
  - func (req *Request) BodyUncompressed() ([]byte, error)
  - func (req *Request) BodyUncompressedWithLimit(maxBodySize int) ([]byte, error)
  - func (req *Request) BodyUnzstd() ([]byte, error)
  - func (req *Request) BodyUnzstdWithLimit(maxBodySize int) ([]byte, error)
  - func (req *Request) BodyWriteTo(w io.Writer) error
  - func (req *Request) BodyWriter() io.Writer
  - func (req *Request) CloseBodyStream() error
  - func (req *Request) ConnectionClose() bool
  - func (req *Request) ContinueReadBody(r *bufio.Reader, maxBodySize int, preParseMultipartForm ...bool) error
  - func (req *Request) ContinueReadBodyStream(r *bufio.Reader, maxBodySize int, preParseMultipartForm ...bool) error
  - func (req *Request) CopyTo(dst *Request)
  - func (req *Request) GetTimeOut() time.Duration
  - func (req *Request) Host() []byte
  - func (req *Request) IsBodyStream() bool
  - func (req *Request) MayContinue() bool
  - func (req *Request) MultipartForm() (*multipart.Form, error)
  - func (req *Request) MultipartFormWithLimit(maxBodySize int) (*multipart.Form, error)
  - func (req *Request) PostArgs() *Args
  - func (req *Request) Read(r *bufio.Reader) error
  - func (req *Request) ReadBody(r *bufio.Reader, contentLength, maxBodySize int) (err error)
  - func (req *Request) ReadLimitBody(r *bufio.Reader, maxBodySize int) error
  - func (req *Request) ReleaseBody(size int)
  - func (req *Request) RemoveMultipartFormFiles()
  - func (req *Request) RemoveUserValue(key any)
  - func (req *Request) RemoveUserValueBytes(key []byte)
  - func (req *Request) RequestURI() []byte
  - func (req *Request) Reset()
  - func (req *Request) ResetBody()
  - func (req *Request) ResetUserValues()
  - func (req *Request) SetBody(body []byte)
  - func (req *Request) SetBodyRaw(body []byte)
  - func (req *Request) SetBodyStream(bodyStream io.Reader, bodySize int)
  - func (req *Request) SetBodyStreamWriter(sw StreamWriter)
  - func (req *Request) SetBodyString(body string)
  - func (req *Request) SetConnectionClose()
  - func (req *Request) SetHost(host string)
  - func (req *Request) SetHostBytes(host []byte)
  - func (req *Request) SetRequestURI(requestURI string)
  - func (req *Request) SetRequestURIBytes(requestURI []byte)
  - func (req *Request) SetTimeout(t time.Duration)
  - func (req *Request) SetURI(newURI *URI)
  - func (req *Request) SetUserValue(key, value any)
  - func (req *Request) SetUserValueBytes(key []byte, value any)
  - func (req *Request) String() string
  - func (req *Request) SwapBody(body []byte) []byte
  - func (req *Request) URI() *URI
  - func (req *Request) UserValue(key any) any
  - func (req *Request) UserValueBytes(key []byte) any
  - func (req *Request) VisitUserValues(visitor func([]byte, any))
  - func (req *Request) VisitUserValuesAll(visitor func(any, any))
  - func (req *Request) Write(w *bufio.Writer) error
  - func (req *Request) WriteTo(w io.Writer) (int64, error)
- type RequestConfig
- type RequestCtx
  - func (ctx *RequestCtx) Conn() net.Conn
  - func (ctx *RequestCtx) ConnID() uint64
  - func (ctx *RequestCtx) ConnRequestNum() uint64
  - func (ctx *RequestCtx) ConnTime() time.Time
  - func (ctx *RequestCtx) Deadline() (deadline time.Time, ok bool)
  - func (ctx *RequestCtx) Done() <-chan struct{}
  - func (ctx *RequestCtx) EarlyHints() error
  - func (ctx *RequestCtx) Err() error
  - func (ctx *RequestCtx) Error(msg string, statusCode int)
  - func (ctx *RequestCtx) FormFile(key string) (*multipart.FileHeader, error)
  - func (ctx *RequestCtx) FormValue(key string) []byte
  - func (ctx *RequestCtx) Hijack(handler HijackHandler)
  - func (ctx *RequestCtx) HijackSetNoResponse(noResponse bool)
  - func (ctx *RequestCtx) Hijacked() bool
  - func (ctx *RequestCtx) Host() []byte
  - func (ctx *RequestCtx) ID() uint64
  - func (ctx *RequestCtx) IfModifiedSince(lastModified time.Time) bool
  - func (ctx *RequestCtx) Init(req *Request, remoteAddr net.Addr, logger Logger)
  - func (ctx *RequestCtx) Init2(conn net.Conn, logger Logger, reduceMemoryUsage bool)
  - func (ctx *RequestCtx) IsBodyStream() bool
  - func (ctx *RequestCtx) IsConnect() bool
  - func (ctx *RequestCtx) IsDelete() bool
  - func (ctx *RequestCtx) IsGet() bool
  - func (ctx *RequestCtx) IsHead() bool
  - func (ctx *RequestCtx) IsOptions() bool
  - func (ctx *RequestCtx) IsPatch() bool
  - func (ctx *RequestCtx) IsPost() bool
  - func (ctx *RequestCtx) IsPut() bool
  - func (ctx *RequestCtx) IsTLS() bool
  - func (ctx *RequestCtx) IsTrace() bool
  - func (ctx *RequestCtx) LastTimeoutErrorResponse() *Response
  - func (ctx *RequestCtx) LocalAddr() net.Addr
  - func (ctx *RequestCtx) LocalIP() net.IP
  - func (ctx *RequestCtx) Logger() Logger
  - func (ctx *RequestCtx) Method() []byte
  - func (ctx *RequestCtx) MultipartForm() (*multipart.Form, error)
  - func (ctx *RequestCtx) MultipartFormWithLimit(maxBodySize int) (*multipart.Form, error)
  - func (ctx *RequestCtx) NotFound()
  - func (ctx *RequestCtx) NotModified()
  - func (ctx *RequestCtx) Path() []byte
  - func (ctx *RequestCtx) PostArgs() *Args
  - func (ctx *RequestCtx) PostBody() []byte
  - func (ctx *RequestCtx) QueryArgs() *Args
  - func (ctx *RequestCtx) Redirect(uri string, statusCode int)
  - func (ctx *RequestCtx) RedirectBytes(uri []byte, statusCode int)
  - func (ctx *RequestCtx) Referer() []byte
  - func (ctx *RequestCtx) RemoteAddr() net.Addr
  - func (ctx *RequestCtx) RemoteIP() net.IP
  - func (ctx *RequestCtx) RemoveUserValue(key any)
  - func (ctx *RequestCtx) RemoveUserValueBytes(key []byte)
  - func (ctx *RequestCtx) RequestBodyStream() io.Reader
  - func (ctx *RequestCtx) RequestURI() []byte
  - func (ctx *RequestCtx) ResetBody()
  - func (ctx *RequestCtx) ResetUserValues()
  - func (ctx *RequestCtx) SendFile(path string)
  - func (ctx *RequestCtx) SendFileBytes(path []byte)
  - func (ctx *RequestCtx) SendFileLiteral(path string)
  - func (ctx *RequestCtx) SetBody(body []byte)
  - func (ctx *RequestCtx) SetBodyStream(bodyStream io.Reader, bodySize int)
  - func (ctx *RequestCtx) SetBodyStreamWriter(sw StreamWriter)
  - func (ctx *RequestCtx) SetBodyString(body string)
  - func (ctx *RequestCtx) SetConnectionClose()
  - func (ctx *RequestCtx) SetContentType(contentType string)
  - func (ctx *RequestCtx) SetContentTypeBytes(contentType []byte)
  - func (ctx *RequestCtx) SetRemoteAddr(remoteAddr net.Addr)
  - func (ctx *RequestCtx) SetStatusCode(statusCode int)
  - func (ctx *RequestCtx) SetUserValue(key, value any)
  - func (ctx *RequestCtx) SetUserValueBytes(key []byte, value any)
  - func (ctx *RequestCtx) String() string
  - func (ctx *RequestCtx) Success(contentType string, body []byte)
  - func (ctx *RequestCtx) SuccessString(contentType, body string)
  - func (ctx *RequestCtx) TLSConnectionState() *tls.ConnectionState
  - func (ctx *RequestCtx) Time() time.Time
  - func (ctx *RequestCtx) TimeoutError(msg string)
  - func (ctx *RequestCtx) TimeoutErrorWithCode(msg string, statusCode int)
  - func (ctx *RequestCtx) TimeoutErrorWithResponse(resp *Response)
  - func (ctx *RequestCtx) URI() *URI
  - func (ctx *RequestCtx) UserAgent() []byte
  - func (ctx *RequestCtx) UserValue(key any) any
  - func (ctx *RequestCtx) UserValueBytes(key []byte) any
  - func (ctx *RequestCtx) Value(key any) any
  - func (ctx *RequestCtx) VisitUserValues(visitor func([]byte, any))
  - func (ctx *RequestCtx) VisitUserValuesAll(visitor func(any, any))
  - func (ctx *RequestCtx) Write(p []byte) (int, error)
  - func (ctx *RequestCtx) WriteString(s string) (int, error)
- type RequestHandler
  - func CompressHandler(h RequestHandler) RequestHandler
  - func CompressHandlerBrotliLevel(h RequestHandler, brotliLevel, otherLevel int) RequestHandler
  - func CompressHandlerLevel(h RequestHandler, level int) RequestHandler
  - func FSHandler(root string, stripSlashes int) RequestHandler
  - func TimeoutHandler(h RequestHandler, timeout time.Duration, msg string) RequestHandler
  - func TimeoutWithCodeHandler(h RequestHandler, timeout time.Duration, msg string, statusCode int) RequestHandler
- type RequestHeader
  - func (h *RequestHeader) Add(key, value string)
  - func (h *RequestHeader) AddBytesK(key []byte, value string)
  - func (h *RequestHeader) AddBytesKV(key, value []byte)
  - func (h *RequestHeader) AddBytesV(key string, value []byte)
  - func (h *RequestHeader) AddTrailer(trailer string) error
  - func (h *RequestHeader) AddTrailerBytes(trailer []byte) (err error)
  - func (h *RequestHeader) All() iter.Seq2[[]byte, []byte]
  - func (h *RequestHeader) AllInOrder() iter.Seq2[[]byte, []byte]
  - func (h *RequestHeader) AppendBytes(dst []byte) []byte
  - func (h *RequestHeader) ConnectionClose() bool
  - func (h *RequestHeader) ConnectionUpgrade() bool
  - func (h *RequestHeader) ContentEncoding() []byte
  - func (h *RequestHeader) ContentLength() int
  - func (h *RequestHeader) ContentType() []byte
  - func (h *RequestHeader) Cookie(key string) []byte
  - func (h *RequestHeader) CookieBytes(key []byte) []byte
  - func (h *RequestHeader) Cookies() iter.Seq2[[]byte, []byte]
  - func (h *RequestHeader) CopyTo(dst *RequestHeader)
  - func (h *RequestHeader) Del(key string)
  - func (h *RequestHeader) DelAllCookies()
  - func (h *RequestHeader) DelBytes(key []byte)
  - func (h *RequestHeader) DelCookie(key string)
  - func (h *RequestHeader) DelCookieBytes(key []byte)
  - func (h *RequestHeader) DisableNormalizing() bool
  - func (h *RequestHeader) DisableSpecialHeader() bool
  - func (h *RequestHeader) EnableNormalizing() bool
  - func (h *RequestHeader) EnableSpecialHeader() bool
  - func (h *RequestHeader) HasAcceptEncoding(acceptEncoding string) bool
  - func (h *RequestHeader) HasAcceptEncodingBytes(acceptEncoding []byte) bool
  - func (h *RequestHeader) Header() []byte
  - func (h *RequestHeader) Host() []byte
  - func (h *RequestHeader) IsConnect() bool
  - func (h *RequestHeader) IsDelete() bool
  - func (h *RequestHeader) IsGet() bool
  - func (h *RequestHeader) IsHTTP11() bool
  - func (h *RequestHeader) IsHead() bool
  - func (h *RequestHeader) IsOptions() bool
  - func (h *RequestHeader) IsPatch() bool
  - func (h *RequestHeader) IsPost() bool
  - func (h *RequestHeader) IsPut() bool
  - func (h *RequestHeader) IsTrace() bool
  - func (h *RequestHeader) Len() int
  - func (h *RequestHeader) Method() []byte
  - func (h *RequestHeader) MultipartFormBoundary() []byte
  - func (h *RequestHeader) Peek(key string) []byte
  - func (h *RequestHeader) PeekAll(key string) [][]byte
  - func (h *RequestHeader) PeekBytes(key []byte) []byte
  - func (h *RequestHeader) PeekKeys() [][]byte
  - func (h *RequestHeader) PeekTrailerKeys() [][]byte
  - func (h *RequestHeader) Protocol() []byte
  - func (h *RequestHeader) RawHeaders() []byte
  - func (h *RequestHeader) Read(r *bufio.Reader) error
  - func (h *RequestHeader) ReadTrailer(r *bufio.Reader) error
  - func (h *RequestHeader) Referer() []byte
  - func (h *RequestHeader) RequestURI() []byte
  - func (h *RequestHeader) Reset()
  - func (h *RequestHeader) ResetConnectionClose()
  - func (h *RequestHeader) Set(key, value string)
  - func (h *RequestHeader) SetByteRange(startPos, endPos int)
  - func (h *RequestHeader) SetBytesK(key []byte, value string)
  - func (h *RequestHeader) SetBytesKV(key, value []byte)
  - func (h *RequestHeader) SetBytesV(key string, value []byte)
  - func (h *RequestHeader) SetCanonical(key, value []byte)
  - func (h *RequestHeader) SetConnectionClose()
  - func (h *RequestHeader) SetContentEncoding(contentEncoding string)
  - func (h *RequestHeader) SetContentEncodingBytes(contentEncoding []byte)
  - func (h *RequestHeader) SetContentLength(contentLength int)
  - func (h *RequestHeader) SetContentType(contentType string)
  - func (h *RequestHeader) SetContentTypeBytes(contentType []byte)
  - func (h *RequestHeader) SetCookie(key, value string)
  - func (h *RequestHeader) SetCookieBytesK(key []byte, value string)
  - func (h *RequestHeader) SetCookieBytesKV(key, value []byte)
  - func (h *RequestHeader) SetHost(host string)
  - func (h *RequestHeader) SetHostBytes(host []byte)
  - func (h *RequestHeader) SetMethod(method string)
  - func (h *RequestHeader) SetMethodBytes(method []byte)
  - func (h *RequestHeader) SetMultipartFormBoundary(boundary string)
  - func (h *RequestHeader) SetMultipartFormBoundaryBytes(boundary []byte)
  - func (h *RequestHeader) SetNoDefaultContentType(noDefaultContentType bool)
  - func (h *RequestHeader) SetProtocol(protocol string)
  - func (h *RequestHeader) SetProtocolBytes(protocol []byte)
  - func (h *RequestHeader) SetReferer(referer string)
  - func (h *RequestHeader) SetRefererBytes(referer []byte)
  - func (h *RequestHeader) SetRequestURI(requestURI string)
  - func (h *RequestHeader) SetRequestURIBytes(requestURI []byte)
  - func (h *RequestHeader) SetTrailer(trailer string) error
  - func (h *RequestHeader) SetTrailerBytes(trailer []byte) error
  - func (h *RequestHeader) SetUserAgent(userAgent string)
  - func (h *RequestHeader) SetUserAgentBytes(userAgent []byte)
  - func (h *RequestHeader) String() string
  - func (h *RequestHeader) TrailerHeader() []byte
  - func (h *RequestHeader) Trailers() iter.Seq[[]byte]
  - func (h *RequestHeader) UserAgent() []byte
  - func (h *RequestHeader) VisitAll(f func(key, value []byte))deprecated
  - func (h *RequestHeader) VisitAllCookie(f func(key, value []byte))deprecated
  - func (h *RequestHeader) VisitAllInOrder(f func(key, value []byte))deprecated
  - func (h *RequestHeader) VisitAllTrailer(f func(value []byte))deprecated
  - func (h *RequestHeader) Write(w *bufio.Writer) error
  - func (h *RequestHeader) WriteTo(w io.Writer) (int64, error)
- type Resolver
- type Response
  - func AcquireResponse() *Response
  - func (resp *Response) AppendBody(p []byte)
  - func (resp *Response) AppendBodyString(s string)
  - func (resp *Response) Body() []byte
  - func (resp *Response) BodyGunzip() ([]byte, error)
  - func (resp *Response) BodyGunzipWithLimit(maxBodySize int) ([]byte, error)
  - func (resp *Response) BodyInflate() ([]byte, error)
  - func (resp *Response) BodyInflateWithLimit(maxBodySize int) ([]byte, error)
  - func (resp *Response) BodyStream() io.Reader
  - func (resp *Response) BodyUnbrotli() ([]byte, error)
  - func (resp *Response) BodyUnbrotliWithLimit(maxBodySize int) ([]byte, error)
  - func (resp *Response) BodyUncompressed() ([]byte, error)
  - func (resp *Response) BodyUncompressedWithLimit(maxBodySize int) ([]byte, error)
  - func (resp *Response) BodyUnzstd() ([]byte, error)
  - func (resp *Response) BodyUnzstdWithLimit(maxBodySize int) ([]byte, error)
  - func (resp *Response) BodyWriteTo(w io.Writer) error
  - func (resp *Response) BodyWriter() io.Writer
  - func (resp *Response) CloseBodyStream() error
  - func (resp *Response) ConnectionClose() bool
  - func (resp *Response) CopyTo(dst *Response)
  - func (resp *Response) IsBodyStream() bool
  - func (resp *Response) LocalAddr() net.Addr
  - func (resp *Response) ParseNetConn(conn net.Conn)
  - func (resp *Response) Read(r *bufio.Reader) error
  - func (resp *Response) ReadBody(r *bufio.Reader, maxBodySize int) (err error)
  - func (resp *Response) ReadLimitBody(r *bufio.Reader, maxBodySize int) error
  - func (resp *Response) ReleaseBody(size int)
  - func (resp *Response) RemoteAddr() net.Addr
  - func (resp *Response) Reset()
  - func (resp *Response) ResetBody()
  - func (resp *Response) SendFile(path string) error
  - func (resp *Response) SetBody(body []byte)
  - func (resp *Response) SetBodyRaw(body []byte)
  - func (resp *Response) SetBodyStream(bodyStream io.Reader, bodySize int)
  - func (resp *Response) SetBodyStreamWriter(sw StreamWriter)
  - func (resp *Response) SetBodyString(body string)
  - func (resp *Response) SetConnectionClose()
  - func (resp *Response) SetStatusCode(statusCode int)
  - func (resp *Response) StatusCode() int
  - func (resp *Response) String() string
  - func (resp *Response) SwapBody(body []byte) []byte
  - func (resp *Response) Write(w *bufio.Writer) error
  - func (resp *Response) WriteDeflate(w *bufio.Writer) error
  - func (resp *Response) WriteDeflateLevel(w *bufio.Writer, level int) error
  - func (resp *Response) WriteGzip(w *bufio.Writer) error
  - func (resp *Response) WriteGzipLevel(w *bufio.Writer, level int) error
  - func (resp *Response) WriteTo(w io.Writer) (int64, error)
- type ResponseHeader
  - func (h *ResponseHeader) Add(key, value string)
  - func (h *ResponseHeader) AddBytesK(key []byte, value string)
  - func (h *ResponseHeader) AddBytesKV(key, value []byte)
  - func (h *ResponseHeader) AddBytesV(key string, value []byte)
  - func (h *ResponseHeader) AddTrailer(trailer string) error
  - func (h *ResponseHeader) AddTrailerBytes(trailer []byte) (err error)
  - func (h *ResponseHeader) All() iter.Seq2[[]byte, []byte]
  - func (h *ResponseHeader) AppendBytes(dst []byte) []byte
  - func (h *ResponseHeader) ConnectionClose() bool
  - func (h *ResponseHeader) ConnectionUpgrade() bool
  - func (h *ResponseHeader) ContentEncoding() []byte
  - func (h *ResponseHeader) ContentLength() int
  - func (h *ResponseHeader) ContentType() []byte
  - func (h *ResponseHeader) Cookie(cookie *Cookie) bool
  - func (h *ResponseHeader) Cookies() iter.Seq2[[]byte, []byte]
  - func (h *ResponseHeader) CopyTo(dst *ResponseHeader)
  - func (h *ResponseHeader) Del(key string)
  - func (h *ResponseHeader) DelAllCookies()
  - func (h *ResponseHeader) DelBytes(key []byte)
  - func (h *ResponseHeader) DelClientCookie(key string)
  - func (h *ResponseHeader) DelClientCookieBytes(key []byte)
  - func (h *ResponseHeader) DelCookie(key string)
  - func (h *ResponseHeader) DelCookieBytes(key []byte)
  - func (h *ResponseHeader) DisableNormalizing() bool
  - func (h *ResponseHeader) EnableNormalizing() bool
  - func (h *ResponseHeader) Header() []byte
  - func (h *ResponseHeader) IsHTTP11() bool
  - func (h *ResponseHeader) Len() int
  - func (h *ResponseHeader) Peek(key string) []byte
  - func (h *ResponseHeader) PeekAll(key string) [][]byte
  - func (h *ResponseHeader) PeekBytes(key []byte) []byte
  - func (h *ResponseHeader) PeekCookie(key string) []byte
  - func (h *ResponseHeader) PeekKeys() [][]byte
  - func (h *ResponseHeader) PeekTrailerKeys() [][]byte
  - func (h *ResponseHeader) Protocol() []byte
  - func (h *ResponseHeader) Read(r *bufio.Reader) error
  - func (h *ResponseHeader) ReadTrailer(r *bufio.Reader) error
  - func (h *ResponseHeader) Reset()
  - func (h *ResponseHeader) ResetConnectionClose()
  - func (h *ResponseHeader) Server() []byte
  - func (h *ResponseHeader) Set(key, value string)
  - func (h *ResponseHeader) SetBytesK(key []byte, value string)
  - func (h *ResponseHeader) SetBytesKV(key, value []byte)
  - func (h *ResponseHeader) SetBytesV(key string, value []byte)
  - func (h *ResponseHeader) SetCanonical(key, value []byte)
  - func (h *ResponseHeader) SetConnectionClose()
  - func (h *ResponseHeader) SetContentEncoding(contentEncoding string)
  - func (h *ResponseHeader) SetContentEncodingBytes(contentEncoding []byte)
  - func (h *ResponseHeader) SetContentLength(contentLength int)
  - func (h *ResponseHeader) SetContentRange(startPos, endPos, contentLength int)
  - func (h *ResponseHeader) SetContentType(contentType string)
  - func (h *ResponseHeader) SetContentTypeBytes(contentType []byte)
  - func (h *ResponseHeader) SetCookie(cookie *Cookie)
  - func (h *ResponseHeader) SetLastModified(t time.Time)
  - func (h *ResponseHeader) SetNoDefaultContentType(noDefaultContentType bool)
  - func (h *ResponseHeader) SetProtocol(protocol []byte)
  - func (h *ResponseHeader) SetServer(server string)
  - func (h *ResponseHeader) SetServerBytes(server []byte)
  - func (h *ResponseHeader) SetStatusCode(statusCode int)
  - func (h *ResponseHeader) SetStatusMessage(statusMessage []byte)
  - func (h *ResponseHeader) SetTrailer(trailer string) error
  - func (h *ResponseHeader) SetTrailerBytes(trailer []byte) error
  - func (h *ResponseHeader) StatusCode() int
  - func (h *ResponseHeader) StatusMessage() []byte
  - func (h *ResponseHeader) String() string
  - func (h *ResponseHeader) TrailerHeader() []byte
  - func (h *ResponseHeader) Trailers() iter.Seq[[]byte]
  - func (h *ResponseHeader) VisitAll(f func(key, value []byte))deprecated
  - func (h *ResponseHeader) VisitAllCookie(f func(key, value []byte))deprecated
  - func (h *ResponseHeader) VisitAllTrailer(f func(value []byte))deprecated
  - func (h *ResponseHeader) Write(w *bufio.Writer) error
  - func (h *ResponseHeader) WriteTo(w io.Writer) (int64, error)
- type RetryIfErrFunc
- type RetryIfErrUpstreamFunc
- type RetryIfFunc
- type RoundTripper
- type ServeHandler
- type Server
  - func (s *Server) AppendCert(certFile, keyFile string) error
  - func (s *Server) AppendCertEmbed(certData, keyData []byte) error
  - func (s *Server) GetCurrentConcurrency() uint32
  - func (s *Server) GetOpenConnectionsCount() int32
  - func (s *Server) GetRejectedConnectionsCount() uint32
  - func (s *Server) ListenAndServe(addr string) error
  - func (s *Server) ListenAndServeTLS(addr, certFile, keyFile string) error
  - func (s *Server) ListenAndServeTLSEmbed(addr string, certData, keyData []byte) error
  - func (s *Server) ListenAndServeUNIX(addr string, mode os.FileMode) error
  - func (s *Server) NextProto(key string, nph ServeHandler)
  - func (s *Server) Serve(ln net.Listener) error
  - func (s *Server) ServeConn(c net.Conn) error
  - func (s *Server) ServeTLS(ln net.Listener, certFile, keyFile string) error
  - func (s *Server) ServeTLSEmbed(ln net.Listener, certData, keyData []byte) error
  - func (s *Server) Shutdown() error
  - func (s *Server) ShutdownWithContext(ctx context.Context) (err error)
- type StreamWriter
- type TCPDialer
  - func (d *TCPDialer) Dial(addr string) (net.Conn, error)
  - func (d *TCPDialer) DialDualStack(addr string) (net.Conn, error)
  - func (d *TCPDialer) DialDualStackTimeout(addr string, timeout time.Duration) (net.Conn, error)
  - func (d *TCPDialer) DialTimeout(addr string, timeout time.Duration) (net.Conn, error)
  - func (d *TCPDialer) FlushDNSCache()
- type URI
  - func AcquireURI() *URI
  - func (u *URI) AppendBytes(dst []byte) []byte
  - func (u *URI) CopyTo(dst *URI)
  - func (u *URI) FullURI() []byte
  - func (u *URI) Hash() []byte
  - func (u *URI) Host() []byte
  - func (u *URI) LastPathSegment() []byte
  - func (u *URI) Parse(host, uri []byte) error
  - func (u *URI) Password() []byte
  - func (u *URI) Path() []byte
  - func (u *URI) PathOriginal() []byte
  - func (u *URI) QueryArgs() *Args
  - func (u *URI) QueryString() []byte
  - func (u *URI) RequestURI() []byte
  - func (u *URI) Reset()
  - func (u *URI) Scheme() []byte
  - func (u *URI) SetHash(hash string)
  - func (u *URI) SetHashBytes(hash []byte)
  - func (u *URI) SetHost(host string)
  - func (u *URI) SetHostBytes(host []byte)
  - func (u *URI) SetPassword(password string)
  - func (u *URI) SetPasswordBytes(password []byte)
  - func (u *URI) SetPath(path string)
  - func (u *URI) SetPathBytes(path []byte)
  - func (u *URI) SetQueryString(queryString string)
  - func (u *URI) SetQueryStringBytes(queryString []byte)
  - func (u *URI) SetScheme(scheme string)
  - func (u *URI) SetSchemeBytes(scheme []byte)
  - func (u *URI) SetUsername(username string)
  - func (u *URI) SetUsernameBytes(username []byte)
  - func (u *URI) String() string
  - func (u *URI) Update(newURI string)
  - func (u *URI) UpdateBytes(newURI []byte)
  - func (u *URI) Username() []byte
  - func (u *URI) WriteTo(w io.Writer) (int64, error)

### Examples

- FS
- FSHandler
- HostClient
- LBClient
- ListenAndServe
- RequestCtx.Hijack
- RequestCtx.Logger
- RequestCtx.SetBodyStreamWriter
- RequestCtx.TimeoutError
- Serve
- Server

### Constants

View Source

```
const (
	CompressBrotliNoCompression   = 0
	CompressBrotliBestSpeed       = brotli.BestSpeed
	CompressBrotliBestCompression = brotli.BestCompression

	
	
	
	CompressBrotliDefaultCompression = 4
)
```

Supported compression levels.

View Source

```
const (
	CompressNoCompression      = flate.NoCompression
	CompressBestSpeed          = flate.BestSpeed
	CompressBestCompression    = flate.BestCompression
	CompressDefaultCompression = 6  
	CompressHuffmanOnly        = -2 
)
```

Supported compression levels.

View Source

```
const (
	HeaderAccept                          = "Accept"
	HeaderAcceptCH                        = "Accept-CH"
	HeaderAcceptCharset                   = "Accept-Charset"
	HeaderAcceptCHLifetime                = "Accept-CH-Lifetime"
	HeaderAcceptEncoding                  = "Accept-Encoding"
	HeaderAcceptLanguage                  = "Accept-Language"
	HeaderAcceptPatch                     = "Accept-Patch"
	HeaderAcceptPushPolicy                = "Accept-Push-Policy"
	HeaderAcceptRanges                    = "Accept-Ranges"
	HeaderAcceptSignature                 = "Accept-Signature"
	HeaderAccessControlAllowCredentials   = "Access-Control-Allow-Credentials"
	HeaderAccessControlAllowHeaders       = "Access-Control-Allow-Headers"
	HeaderAccessControlAllowMethods       = "Access-Control-Allow-Methods"
	HeaderAccessControlAllowOrigin        = "Access-Control-Allow-Origin"
	HeaderAccessControlExposeHeaders      = "Access-Control-Expose-Headers"
	HeaderAccessControlMaxAge             = "Access-Control-Max-Age"
	HeaderAccessControlRequestHeaders     = "Access-Control-Request-Headers"
	HeaderAccessControlRequestMethod      = "Access-Control-Request-Method"
	HeaderAge                             = "Age"
	HeaderAllow                           = "Allow"
	HeaderAltSvc                          = "Alt-Svc"
	HeaderAuthorization                   = "Authorization"
	HeaderCacheControl                    = "Cache-Control"
	HeaderClearSiteData                   = "Clear-Site-Data"
	HeaderConnection                      = "Connection"
	HeaderContentDisposition              = "Content-Disposition"
	HeaderContentDPR                      = "Content-DPR"
	HeaderContentEncoding                 = "Content-Encoding"
	HeaderContentLanguage                 = "Content-Language"
	HeaderContentLength                   = "Content-Length"
	HeaderContentLocation                 = "Content-Location"
	HeaderContentRange                    = "Content-Range"
	HeaderContentSecurityPolicy           = "Content-Security-Policy"
	HeaderContentSecurityPolicyReportOnly = "Content-Security-Policy-Report-Only"
	HeaderContentType                     = "Content-Type"
	HeaderCookie                          = "Cookie"
	HeaderCookie2                         = "Cookie2"
	HeaderCrossOriginResourcePolicy       = "Cross-Origin-Resource-Policy"
	HeaderDate                            = "Date"
	HeaderDNT                             = "DNT"
	HeaderDPR                             = "DPR"
	HeaderEarlyData                       = "Early-Data"
	HeaderETag                            = "ETag"
	HeaderExpect                          = "Expect"
	HeaderExpectCT                        = "Expect-CT"
	HeaderExpires                         = "Expires"
	HeaderFeaturePolicy                   = "Feature-Policy"
	HeaderForwarded                       = "Forwarded"
	HeaderFrom                            = "From"
	HeaderHost                            = "Host"
	HeaderIfMatch                         = "If-Match"
	HeaderIfModifiedSince                 = "If-Modified-Since"
	HeaderIfNoneMatch                     = "If-None-Match"
	HeaderIfRange                         = "If-Range"
	HeaderIfUnmodifiedSince               = "If-Unmodified-Since"
	HeaderIndex                           = "Index"
	HeaderKeepAlive                       = "Keep-Alive"
	HeaderLargeAllocation                 = "Large-Allocation"
	HeaderLastEventID                     = "Last-Event-ID"
	HeaderLastModified                    = "Last-Modified"
	HeaderLocation                        = "Location"
	HeaderMaxForwards                     = "Max-Forwards"
	HeaderNEL                             = "NEL"
	HeaderOrigin                          = "Origin"
	HeaderPingFrom                        = "Ping-From"
	HeaderPingTo                          = "Ping-To"
	HeaderPragma                          = "Pragma"
	HeaderProxyAuthenticate               = "Proxy-Authenticate"
	HeaderProxyAuthorization              = "Proxy-Authorization"
	HeaderProxyConnection                 = "Proxy-Connection"
	HeaderPublicKeyPins                   = "Public-Key-Pins"
	HeaderPublicKeyPinsReportOnly         = "Public-Key-Pins-Report-Only"
	HeaderPushPolicy                      = "Push-Policy"
	HeaderRange                           = "Range"
	HeaderReferer                         = "Referer"
	HeaderReferrerPolicy                  = "Referrer-Policy"
	HeaderReportTo                        = "Report-To"
	HeaderRetryAfter                      = "Retry-After"
	HeaderSaveData                        = "Save-Data"
	HeaderSecWebSocketAccept              = "Sec-WebSocket-Accept"
	HeaderSecWebSocketExtensions          = "Sec-WebSocket-Extensions" 
	HeaderSecWebSocketKey                 = "Sec-WebSocket-Key"
	HeaderSecWebSocketProtocol            = "Sec-WebSocket-Protocol"
	HeaderSecWebSocketVersion             = "Sec-WebSocket-Version"
	HeaderServer                          = "Server"
	HeaderServerTiming                    = "Server-Timing"
	HeaderSetCookie                       = "Set-Cookie"
	HeaderSignature                       = "Signature"
	HeaderSignedHeaders                   = "Signed-Headers"
	HeaderSourceMap                       = "SourceMap"
	HeaderStrictTransportSecurity         = "Strict-Transport-Security"
	HeaderTE                              = "TE"
	HeaderTimingAllowOrigin               = "Timing-Allow-Origin"
	HeaderTk                              = "Tk"
	HeaderTrailer                         = "Trailer"
	HeaderTransferEncoding                = "Transfer-Encoding"
	HeaderUpgrade                         = "Upgrade"
	HeaderUpgradeInsecureRequests         = "Upgrade-Insecure-Requests"
	HeaderUserAgent                       = "User-Agent"
	HeaderVary                            = "Vary"
	HeaderVia                             = "Via"
	HeaderViewportWidth                   = "Viewport-Width"
	HeaderWarning                         = "Warning"
	HeaderWidth                           = "Width"
	HeaderWWWAuthenticate                 = "WWW-Authenticate"
	HeaderXContentTypeOptions             = "X-Content-Type-Options"
	HeaderXDNSPrefetchControl             = "X-DNS-Prefetch-Control"
	HeaderXDownloadOptions                = "X-Download-Options"
	HeaderXForwardedFor                   = "X-Forwarded-For"
	HeaderXForwardedHost                  = "X-Forwarded-Host"
	HeaderXForwardedProto                 = "X-Forwarded-Proto"
	HeaderXFrameOptions                   = "X-Frame-Options"
	HeaderXPermittedCrossDomainPolicies   = "X-Permitted-Cross-Domain-Policies"
	HeaderXPingback                       = "X-Pingback"
	HeaderXPoweredBy                      = "X-Powered-By"
	HeaderXRequestedWith                  = "X-Requested-With"
	HeaderXRobotsTag                      = "X-Robots-Tag"
	HeaderXUACompatible                   = "X-UA-Compatible"
	HeaderXXSSProtection                  = "X-XSS-Protection"
)
```

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

HTTP methods were copied from net/http.

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

HTTP status codes were stolen from net/http.

View Source

```
const (
	CompressZstdSpeedNotSet = iota
	CompressZstdBestSpeed
	CompressZstdDefault
	CompressZstdSpeedBetter
	CompressZstdBestCompression
)
```

View Source

```
const DefaultConcurrency = 256 * 1024
```

DefaultConcurrency is the maximum number of concurrent connections the Server may serve by default (i.e. if Server.Concurrency isn't set).

View Source

```
const DefaultDNSCacheDuration = time.Minute
```

DefaultDNSCacheDuration is the duration for caching resolved TCP addresses by Dial* functions.

View Source

```
const DefaultDialTimeout = 3 * time.Second
```

DefaultDialTimeout is timeout used by Dial and DialDualStack for establishing TCP connections.

View Source

```
const DefaultLBClientTimeout = time.Second
```

DefaultLBClientTimeout is the default request timeout used by LBClient when calling LBClient.Do.

The timeout may be overridden via LBClient.Timeout.

View Source

```
const DefaultMaxConnsPerHost = 512
```

DefaultMaxConnsPerHost is the maximum number of concurrent connections http client may establish per host by default (i.e. if Client.MaxConnsPerHost isn't set).

View Source

```
const DefaultMaxIdemponentCallAttempts = 5
```

DefaultMaxIdemponentCallAttempts is the default idempotent calls attempts count.

View Source

```
const DefaultMaxIdleConnDuration = 10 * time.Second
```

DefaultMaxIdleConnDuration is the default duration before idle keep-alive connection is closed.

View Source

```
const DefaultMaxPendingRequests = 1024
```

DefaultMaxPendingRequests is the default value for PipelineClient.MaxPendingRequests.

View Source

```
const DefaultMaxRequestBodySize = 4 * 1024 * 1024
```

DefaultMaxRequestBodySize is the maximum request body size the server reads by default.

See Server.MaxRequestBodySize for details.

View Source

```
const FSCompressedFileSuffix = ".fasthttp.gz"
```

FSCompressedFileSuffix is the suffix FS adds to the original file names when trying to store compressed file under the new file name. See FS.Compress for details.

View Source

```
const FSHandlerCacheDuration = 10 * time.Second
```

FSHandlerCacheDuration is the default expiration duration for inactive file handlers opened by FS.

### Variables

View Source

```
var (
	
	
	ErrMissingLocation = errors.New("missing Location header for http redirect")
	
	
	ErrTooManyRedirects = errors.New("too many redirects detected when doing the request")

	
	ErrHostClientRedirectToDifferentScheme = errors.New("HostClient can't follow redirects to a different protocol," +
		" please use Client instead")
)
```

View Source

```
var (
	
	
	
	
	
	ErrNoFreeConns = errors.New("no free connections available to host")

	
	
	
	
	
	
	
	ErrConnectionClosed = errors.New("the server closed connection before returning the first response byte. " +
		"Make sure the server returns 'Connection: close' response header before closing the connection")

	
	
	ErrConnPoolStrategyNotImpl = errors.New("connection pool strategy is not implement")
)
```

View Source

```
var (
	
	CookieExpireDelete = time.Date(2009, time.November, 10, 23, 0, 0, 0, time.UTC)

	
	CookieExpireUnlimited = zeroTime
)
```

View Source

```
var (
	ErrNoCookies          = errors.New("no cookies found")
	ErrInvalidCookieValue = errors.New("invalid cookie value")
)
```

View Source

```
var (
	ErrBadTrailer                    = errors.New("contain forbidden trailer")
	ErrReadingResponseHeaders        = errors.New("error when reading response headers")
	ErrReadingResponseTrailer        = errors.New("error when reading response trailer")
	ErrResponseFirstLineMissingSpace = errors.New("cannot find whitespace in the first line of response")
	ErrUnexpectedStatusCodeChar      = errors.New("unexpected char at the end of status code")
	ErrMissingRequestMethod          = errors.New("cannot find http request method")
	ErrUnsupportedRequestMethod      = errors.New("unsupported http request method")
	ErrExtraWhitespaceInRequestLine  = errors.New("extra whitespace in request line")
	ErrEmptyRequestURI               = errors.New("requestURI cannot be empty")
	ErrDuplicateContentLength        = errors.New("duplicate Content-Length header")
	ErrUnsupportedTransferEncoding   = errors.New("unsupported Transfer-Encoding")
	ErrNonNumericChars               = errors.New("non-numeric chars found")
	ErrNeedMore                      = errors.New("need more data: cannot find trailing lf")
	ErrSmallReadBuffer               = errors.New("small read buffer. Increase ReadBufferSize")
)
```

View Source

```
var (
	
	
	ErrPerIPConnLimit = errors.New("too many connections per ip")

	
	
	ErrConcurrencyLimit = errors.New("cannot serve the connection because Server.Concurrency concurrent connections are served")
)
```

View Source

```
var ErrAlreadyServing = errors.New("Server is already serving connections")
```

ErrAlreadyServing is deprecated.

Deprecated: ErrAlreadyServing is never returned from Serve. See issue #633.

View Source

```
var ErrBodyTooLarge = errors.New("body size exceeds the given limit")
```

ErrBodyTooLarge is returned if either request or response body exceeds the given limit.

View Source

```
var ErrContentEncodingUnsupported = errors.New("unsupported Content-Encoding")
```

View Source

```
var ErrDialTimeout = errors.New("dialing to the given TCP address timed out")
```

ErrDialTimeout is returned when TCP dialing is timed out.

View Source

```
var ErrGetOnly = errors.New("non-GET request received")
```

ErrGetOnly is returned when server expects only GET requests, but some other type of request came (Server.GetOnly option is true).

View Source

```
var ErrMissingFile = errors.New("there is no uploaded file associated with the given key")
```

ErrMissingFile may be returned from FormFile when the is no uploaded file associated with the given multipart form key.

View Source

```
var ErrNoArgValue = errors.New("no Args value for the given key")
```

ErrNoArgValue is returned when Args value with the given key is missing.

View Source

```
var ErrNoAvailableClients = errors.New("no available clients")
```

ErrNoAvailableClients is returned by LBClient methods when no clients are available, for example after every client has been removed.

View Source

```
var ErrNoMultipartForm = errors.New("request Content-Type has bad boundary or is not multipart/form-data")
```

ErrNoMultipartForm means that the request's Content-Type isn't 'multipart/form-data'.

View Source

```
var ErrPipelineOverflow = errors.New("pipelined requests' queue has been overflowed. Increase MaxConns and/or MaxPendingRequests")
```

ErrPipelineOverflow may be returned from PipelineClient.Do* if the requests' queue is overflowed.

View Source

```
var ErrTLSHandshakeTimeout = errors.New("tls handshake timed out")
```

ErrTLSHandshakeTimeout indicates there is a timeout from tls handshake.

View Source

```
var ErrTimeout = &timeoutError{}
```

ErrTimeout is returned from timed out calls.

View Source

```
var ErrorInvalidURI = errors.New("invalid uri")
```

View Source

```
var FSCompressedFileSuffixes = map[string]string{
	"gzip": ".fasthttp.gz",
	"br":   ".fasthttp.br",
	"zstd": ".fasthttp.zst",
}
```

FSCompressedFileSuffixes is the suffixes FS adds to the original file names depending on encoding when trying to store compressed file under the new file name. See FS.Compress for details.

This map is read during FSHandler initialization (which runs in a sync.Once). It is not safe for concurrent modification. Set any custom suffixes in an init() function or before the first call to FS.NewRequestHandler, and do not modify the map afterwards.

View Source

```
var (

	
	
	
	
	NetHttpFormValueFunc = func(ctx *RequestCtx, key string) []byte {
		v := ctx.PostArgs().Peek(key)
		if len(v) > 0 {
			return v
		}
		mf, err := ctx.MultipartForm()
		if err == nil && mf.Value != nil {
			vv := mf.Value[key]
			if len(vv) > 0 {
				return []byte(vv[0])
			}
		}
		v = ctx.QueryArgs().Peek(key)
		if len(v) > 0 {
			return v
		}
		return nil
	}
)
```

### Functions

#### func AcquireTimer ¶ added in v1.2.0

```
func AcquireTimer(timeout time.Duration) *time.Timer
```

AcquireTimer returns a time.Timer from the pool and updates it to send the current time on its channel after at least timeout.

The returned Timer may be returned to the pool with ReleaseTimer when no longer needed. This allows reducing GC load.

#### func AddMissingPort ¶ added in v1.43.0

```
func AddMissingPort(addr string, isTLS bool) string
```

AddMissingPort adds a port to a host if it is missing. A literal IPv6 address in hostport must be enclosed in square brackets, as in "[::1]:80", "[::1%lo0]:80".

#### func AppendBrotliBytes ¶ added in v1.13.0

```
func AppendBrotliBytes(dst, src []byte) []byte
```

AppendBrotliBytes appends brotlied src to dst and returns the resulting dst.

#### func AppendBrotliBytesLevel ¶ added in v1.13.0

```
func AppendBrotliBytesLevel(dst, src []byte, level int) []byte
```

AppendBrotliBytesLevel appends brotlied src to dst using the given compression level and returns the resulting dst.

Supported compression levels are:

- CompressBrotliNoCompression
- CompressBrotliBestSpeed
- CompressBrotliBestCompression
- CompressBrotliDefaultCompression

#### func AppendDeflateBytes

```
func AppendDeflateBytes(dst, src []byte) []byte
```

AppendDeflateBytes appends deflated src to dst and returns the resulting dst.

#### func AppendDeflateBytesLevel

```
func AppendDeflateBytesLevel(dst, src []byte, level int) []byte
```

AppendDeflateBytesLevel appends deflated src to dst using the given compression level and returns the resulting dst.

Supported compression levels are:

- CompressNoCompression
- CompressBestSpeed
- CompressBestCompression
- CompressDefaultCompression
- CompressHuffmanOnly

#### func AppendGunzipBytes

```
func AppendGunzipBytes(dst, src []byte) ([]byte, error)
```

AppendGunzipBytes appends gunzipped src to dst and returns the resulting dst.

#### func AppendGzipBytes

```
func AppendGzipBytes(dst, src []byte) []byte
```

AppendGzipBytes appends gzipped src to dst and returns the resulting dst.

#### func AppendGzipBytesLevel

```
func AppendGzipBytesLevel(dst, src []byte, level int) []byte
```

AppendGzipBytesLevel appends gzipped src to dst using the given compression level and returns the resulting dst.

Supported compression levels are:

- CompressNoCompression
- CompressBestSpeed
- CompressBestCompression
- CompressDefaultCompression
- CompressHuffmanOnly

#### func AppendHTMLEscape

```
func AppendHTMLEscape(dst []byte, s string) []byte
```

AppendHTMLEscape appends html-escaped s to dst and returns the extended dst.

#### func AppendHTMLEscapeBytes

```
func AppendHTMLEscapeBytes(dst, s []byte) []byte
```

AppendHTMLEscapeBytes appends html-escaped s to dst and returns the extended dst.

#### func AppendHTTPDate

```
func AppendHTTPDate(dst []byte, date time.Time) []byte
```

AppendHTTPDate appends HTTP-compliant (RFC1123) representation of date to dst and returns the extended dst.

#### func AppendIPv4

```
func AppendIPv4(dst []byte, ip net.IP) []byte
```

AppendIPv4 appends string representation of the given ip v4 to dst and returns the extended dst.

#### func AppendInflateBytes

```
func AppendInflateBytes(dst, src []byte) ([]byte, error)
```

AppendInflateBytes appends inflated src to dst and returns the resulting dst.

#### func AppendNormalizedHeaderKey

```
func AppendNormalizedHeaderKey(dst []byte, key string) []byte
```

AppendNormalizedHeaderKey appends normalized header key (name) to dst and returns the resulting dst.

Normalized header key starts with uppercase letter. The first letters after dashes are also uppercased. All the other letters are lowercased. Examples:

- coNTENT-TYPe -> Content-Type
- HOST -> Host
- foo-bar-baz -> Foo-Bar-Baz

#### func AppendNormalizedHeaderKeyBytes

```
func AppendNormalizedHeaderKeyBytes(dst, key []byte) []byte
```

AppendNormalizedHeaderKeyBytes appends normalized header key (name) to dst and returns the resulting dst.

Normalized header key starts with uppercase letter. The first letters after dashes are also uppercased. All the other letters are lowercased. Examples:

- coNTENT-TYPe -> Content-Type
- HOST -> Host
- foo-bar-baz -> Foo-Bar-Baz

#### func AppendQuotedArg

```
func AppendQuotedArg(dst, src []byte) []byte
```

AppendQuotedArg appends url-encoded src to dst and returns appended dst.

#### func AppendUint

```
func AppendUint(dst []byte, n int) []byte
```

AppendUint appends n to dst and returns the extended dst.

#### func AppendUnbrotliBytes ¶ added in v1.13.0

```
func AppendUnbrotliBytes(dst, src []byte) ([]byte, error)
```

AppendUnbrotliBytes appends unbrotlied src to dst and returns the resulting dst.

#### func AppendUnquotedArg

```
func AppendUnquotedArg(dst, src []byte) []byte
```

AppendUnquotedArg appends url-decoded src to dst and returns appended dst.

dst may point to src. In this case src will be overwritten.

#### func AppendUnzstdBytes ¶ added in v1.53.0

```
func AppendUnzstdBytes(dst, src []byte) ([]byte, error)
```

AppendUnzstdBytes appends unzstd src to dst and returns the resulting dst.

#### func AppendZstdBytes ¶ added in v1.53.0

```
func AppendZstdBytes(dst, src []byte) []byte
```

AppendZstdBytes appends zstd src to dst and returns the resulting dst.

#### func AppendZstdBytesLevel ¶ added in v1.53.0

```
func AppendZstdBytesLevel(dst, src []byte, level int) []byte
```

#### func CoarseTimeNow deprecated

```
func CoarseTimeNow() time.Time
```

CoarseTimeNow returns the current time truncated to the nearest second.

Deprecated: This is slower than calling time.Now() directly. This is now time.Now().Truncate(time.Second) shortcut.

#### func Dial

```
func Dial(addr string) (net.Conn, error)
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

#### func DialDualStack

```
func DialDualStack(addr string) (net.Conn, error)
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

#### func DialDualStackTimeout

```
func DialDualStackTimeout(addr string, timeout time.Duration) (net.Conn, error)
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

#### func DialTimeout

```
func DialTimeout(addr string, timeout time.Duration) (net.Conn, error)
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

#### func Do

```
func Do(req *Request, resp *Response) error
```

Do performs the given http request and fills the given http response.

Request must contain at least non-zero RequestURI with full url (including scheme and host) or non-zero Host header + RequestURI.

Client determines the server to be requested in the following order:

- from RequestURI if it contains full url with scheme and host;
- from Host header otherwise.

The function doesn't follow redirects. Use Get* for following redirects.

Response is ignored if resp is nil.

ErrNoFreeConns is returned if all DefaultMaxConnsPerHost connections to the requested host are busy.

It is recommended obtaining req and resp via AcquireRequest and AcquireResponse in performance-critical code.

#### func DoDeadline

```
func DoDeadline(req *Request, resp *Response, deadline time.Time) error
```

DoDeadline performs the given request and waits for response until the given deadline.

Request must contain at least non-zero RequestURI with full url (including scheme and host) or non-zero Host header + RequestURI.

Client determines the server to be requested in the following order:

- from RequestURI if it contains full url with scheme and host;
- from Host header otherwise.

The function doesn't follow redirects. Use Get* for following redirects.

Response is ignored if resp is nil.

ErrTimeout is returned if the response wasn't returned until the given deadline.

ErrNoFreeConns is returned if all DefaultMaxConnsPerHost connections to the requested host are busy.

It is recommended obtaining req and resp via AcquireRequest and AcquireResponse in performance-critical code.

#### func DoRedirects ¶ added in v1.10.0

```
func DoRedirects(req *Request, resp *Response, maxRedirectsCount int) error
```

DoRedirects performs the given http request and fills the given http response, following up to maxRedirectsCount redirects. When the redirect count exceeds maxRedirectsCount, ErrTooManyRedirects is returned.

Request must contain at least non-zero RequestURI with full url (including scheme and host) or non-zero Host header + RequestURI.

Client determines the server to be requested in the following order:

- from RequestURI if it contains full url with scheme and host;
- from Host header otherwise.

Response is ignored if resp is nil.

ErrNoFreeConns is returned if all DefaultMaxConnsPerHost connections to the requested host are busy.

It is recommended obtaining req and resp via AcquireRequest and AcquireResponse in performance-critical code.

#### func DoTimeout

```
func DoTimeout(req *Request, resp *Response, timeout time.Duration) error
```

DoTimeout performs the given request and waits for response during the given timeout duration.

Request must contain at least non-zero RequestURI with full url (including scheme and host) or non-zero Host header + RequestURI.

Client determines the server to be requested in the following order:

- from RequestURI if it contains full url with scheme and host;
- from Host header otherwise.

The function doesn't follow redirects. Use Get* for following redirects.

Response is ignored if resp is nil.

ErrTimeout is returned if the response wasn't returned during the given timeout.

ErrNoFreeConns is returned if all DefaultMaxConnsPerHost connections to the requested host are busy.

It is recommended obtaining req and resp via AcquireRequest and AcquireResponse in performance-critical code.

#### func FileLastModified

```
func FileLastModified(path string) (time.Time, error)
```

FileLastModified returns last modified time for the file.

#### func FlushDNSCache ¶ added in v1.67.0

```
func FlushDNSCache()
```

FlushDNSCache clears all cached DNS entries for the default dialer, forcing fresh DNS lookups on subsequent Dial* calls. This is useful when you want to ensure fresh DNS resolution, for example after network changes.

#### func GenerateTestCertificate ¶ added in v1.20.0

```
func GenerateTestCertificate(host string) ([]byte, []byte, error)
```

GenerateTestCertificate generates a test certificate and private key based on the given host.

#### func Get

```
func Get(dst []byte, url string) (statusCode int, body []byte, err error)
```

Get returns the status code and body of url.

The contents of dst will be replaced by the body and returned, if the dst is too small a new slice will be allocated.

The function follows redirects. Use Do* for manually handling redirects.

#### func GetDeadline

```
func GetDeadline(dst []byte, url string, deadline time.Time) (statusCode int, body []byte, err error)
```

GetDeadline returns the status code and body of url.

The contents of dst will be replaced by the body and returned, if the dst is too small a new slice will be allocated.

The function follows redirects. Use Do* for manually handling redirects.

ErrTimeout error is returned if url contents couldn't be fetched until the given deadline.

#### func GetTimeout

```
func GetTimeout(dst []byte, url string, timeout time.Duration) (statusCode int, body []byte, err error)
```

GetTimeout returns the status code and body of url.

The contents of dst will be replaced by the body and returned, if the dst is too small a new slice will be allocated.

The function follows redirects. Use Do* for manually handling redirects.

ErrTimeout error is returned if url contents couldn't be fetched during the given timeout.

#### func ListenAndServe

```
func ListenAndServe(addr string, handler RequestHandler) error
```

ListenAndServe serves HTTP requests from the given TCP addr using the given handler.

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
	// The server will listen for incoming requests on this address.
	listenAddr := "127.0.0.1:80"

	// This function will be called by the server for each incoming request.
	//
	// RequestCtx provides a lot of functionality related to http request
	// processing. See RequestCtx docs for details.
	requestHandler := func(ctx *fasthttp.RequestCtx) {
		fmt.Fprintf(ctx, "Hello, world! Requested path is %q", ctx.Path())
	}

	// Start the server with default settings.
	// Create Server instance for adjusting server settings.
	//
	// ListenAndServe returns only on error, so usually it blocks forever.
	if err := fasthttp.ListenAndServe(listenAddr, requestHandler); err != nil {
		log.Fatalf("error in ListenAndServe: %v", err)
	}
}
```

```
Output:
```

#### func ListenAndServeTLS

```
func ListenAndServeTLS(addr, certFile, keyFile string, handler RequestHandler) error
```

ListenAndServeTLS serves HTTPS requests from the given TCP addr using the given handler.

certFile and keyFile are paths to TLS certificate and key files.

#### func ListenAndServeTLSEmbed

```
func ListenAndServeTLSEmbed(addr string, certData, keyData []byte, handler RequestHandler) error
```

ListenAndServeTLSEmbed serves HTTPS requests from the given TCP addr using the given handler.

certData and keyData must contain valid TLS certificate and key data.

#### func ListenAndServeUNIX

```
func ListenAndServeUNIX(addr string, mode os.FileMode, handler RequestHandler) error
```

ListenAndServeUNIX serves HTTP requests from the given UNIX addr using the given handler.

The function deletes existing file at addr before starting serving.

The server sets the given file mode for the UNIX addr.

#### func NewStreamReader

```
func NewStreamReader(sw StreamWriter) io.ReadCloser
```

NewStreamReader returns a reader, which replays all the data generated by sw.

The returned reader may be passed to Response.SetBodyStream.

Close must be called on the returned reader after all the required data has been read. Otherwise goroutine leak may occur.

See also Response.SetBodyStreamWriter.

#### func ParseByteRange

```
func ParseByteRange(byteRange []byte, contentLength int) (startPos, endPos int, err error)
```

ParseByteRange parses 'Range: bytes=...' header value.

It follows https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35 .

#### func ParseHTTPDate

```
func ParseHTTPDate(date []byte) (time.Time, error)
```

ParseHTTPDate parses HTTP-compliant (RFC1123) date.

#### func ParseIPv4

```
func ParseIPv4(dst net.IP, ipStr []byte) (net.IP, error)
```

ParseIPv4 parses ip address from ipStr into dst and returns the extended dst.

#### func ParseUfloat

```
func ParseUfloat(buf []byte) (float64, error)
```

ParseUfloat parses unsigned float from buf.

#### func ParseUint

```
func ParseUint(buf []byte) (int, error)
```

ParseUint parses uint from buf.

#### func Post

```
func Post(dst []byte, url string, postArgs *Args) (statusCode int, body []byte, err error)
```

Post sends POST request to the given url with the given POST arguments.

The contents of dst will be replaced by the body and returned, if the dst is too small a new slice will be allocated.

The function follows redirects. Use Do* for manually handling redirects.

Empty POST body is sent if postArgs is nil.

#### func ReleaseArgs

```
func ReleaseArgs(a *Args)
```

ReleaseArgs returns the object acquired via AcquireArgs to the pool.

Do not access the released Args object, otherwise data races may occur.

#### func ReleaseCookie

```
func ReleaseCookie(c *Cookie)
```

ReleaseCookie returns the Cookie object acquired with AcquireCookie back to the pool.

Do not access released Cookie object, otherwise data races may occur.

#### func ReleaseRequest

```
func ReleaseRequest(req *Request)
```

ReleaseRequest returns req acquired via AcquireRequest to request pool.

It is forbidden accessing req and/or its' members after returning it to request pool.

#### func ReleaseResponse

```
func ReleaseResponse(resp *Response)
```

ReleaseResponse return resp acquired via AcquireResponse to response pool.

It is forbidden accessing resp and/or its' members after returning it to response pool.

#### func ReleaseTimer ¶ added in v1.2.0

```
func ReleaseTimer(t *time.Timer)
```

ReleaseTimer returns the time.Timer acquired via AcquireTimer to the pool and prevents the Timer from firing.

Do not access the released time.Timer or read from its channel otherwise data races may occur.

#### func ReleaseURI

```
func ReleaseURI(u *URI)
```

ReleaseURI releases the URI acquired via AcquireURI.

The released URI mustn't be used after releasing it, otherwise data races may occur.

#### func SaveMultipartFile

```
func SaveMultipartFile(fh *multipart.FileHeader, path string) (err error)
```

SaveMultipartFile saves multipart file fh under the given filename path.

The path is used as-is and must be a server-trusted destination filename. Do not pass the attacker-controlled fh.Filename directly without validating it and constraining it to the intended destination directory.

#### func Serve

```
func Serve(ln net.Listener, handler RequestHandler) error
```

Serve serves incoming connections from the given listener using the given handler.

Serve blocks until the given listener returns permanent error.

Example

¶

```
package main

import (
	"fmt"
	"log"
	"net"

	"github.com/valyala/fasthttp"
)

func main() {
	// Create network listener for accepting incoming requests.
	//
	// Note that you are not limited by TCP listener - arbitrary
	// net.Listener may be used by the server.
	// For example, unix socket listener or TLS listener.
	ln, err := net.Listen("tcp4", "127.0.0.1:8080")
	if err != nil {
		log.Fatalf("error in net.Listen: %v", err)
	}

	// This function will be called by the server for each incoming request.
	//
	// RequestCtx provides a lot of functionality related to http request
	// processing. See RequestCtx docs for details.
	requestHandler := func(ctx *fasthttp.RequestCtx) {
		fmt.Fprintf(ctx, "Hello, world! Requested path is %q", ctx.Path())
	}

	// Start the server with default settings.
	// Create Server instance for adjusting server settings.
	//
	// Serve returns on ln.Close() or error, so usually it blocks forever.
	if err := fasthttp.Serve(ln, requestHandler); err != nil {
		log.Fatalf("error in Serve: %v", err)
	}
}
```

```
Output:
```

#### func ServeConn

```
func ServeConn(c net.Conn, handler RequestHandler) error
```

ServeConn serves HTTP requests from the given connection using the given handler.

ServeConn returns nil if all requests from the c are successfully served. It returns non-nil error otherwise.

Connection c must immediately propagate all the data passed to Write() to the client. Otherwise requests' processing may hang.

ServeConn closes c before returning.

#### func ServeFS ¶ added in v1.51.0

```
func ServeFS(ctx *RequestCtx, filesystem fs.FS, path string)
```

ServeFS returns HTTP response containing compressed file contents from the given fs.FS's path.

HTTP response may contain uncompressed file contents in the following cases:

- Missing 'Accept-Encoding: gzip' request header.
- No write access to directory containing the file.

Directory contents is returned if path points to directory.

ServeFS interprets path as a URI path internally. Percent-encoded sequences may be decoded, and '?' or '#' may be treated as URI delimiters. Use ServeFSLiteral if you need literal path semantics.

See also ServeFile, ServeFSLiteral.

#### func ServeFSLiteral ¶ added in v1.70.0

```
func ServeFSLiteral(ctx *RequestCtx, filesystem fs.FS, path string)
```

ServeFSLiteral returns HTTP response containing compressed file contents from the given fs.FS's path using literal path semantics.

Reserved URI characters in path such as '%', '?' and '#' are preserved instead of being interpreted during internal request URI processing.

HTTP response may contain uncompressed file contents in the following cases:

- Missing 'Accept-Encoding: gzip' request header.
- No write access to directory containing the file.

Directory contents is returned if path points to directory.

See also ServeFS, ServeFileLiteral.

#### func ServeFile

```
func ServeFile(ctx *RequestCtx, path string)
```

ServeFile returns HTTP response containing compressed file contents from the given path.

HTTP response may contain uncompressed file contents in the following cases:

- Missing 'Accept-Encoding: gzip' request header.
- No write access to directory containing the file.

Directory contents is returned if path points to directory.

Use ServeFileUncompressed is you don't need serving compressed file contents.

ServeFile interprets path as a URI path internally. Percent-encoded sequences may be decoded, and '?' or '#' may be treated as URI delimiters. Use ServeFileLiteral if you need literal path semantics.

See also RequestCtx.SendFile, ServeFileLiteral.

WARNING: do not pass any user supplied paths to this function! WARNING: if path is based on user input users will be able to request any file on your filesystem! Use fasthttp.FS with a sane Root instead.

#### func ServeFileBytes

```
func ServeFileBytes(ctx *RequestCtx, path []byte)
```

ServeFileBytes returns HTTP response containing compressed file contents from the given path.

HTTP response may contain uncompressed file contents in the following cases:

- Missing 'Accept-Encoding: gzip' request header.
- No write access to directory containing the file.

Directory contents is returned if path points to directory.

Use ServeFileBytesUncompressed is you don't need serving compressed file contents.

See also RequestCtx.SendFileBytes, ServeFileLiteral.

WARNING: do not pass any user supplied paths to this function! WARNING: if path is based on user input users will be able to request any file on your filesystem! Use fasthttp.FS with a sane Root instead.

#### func ServeFileBytesUncompressed

```
func ServeFileBytesUncompressed(ctx *RequestCtx, path []byte)
```

ServeFileBytesUncompressed returns HTTP response containing file contents from the given path.

Directory contents is returned if path points to directory.

ServeFileBytes may be used for saving network traffic when serving files with good compression ratio.

See also RequestCtx.SendFileBytes.

WARNING: do not pass any user supplied paths to this function! WARNING: if path is based on user input users will be able to request any file on your filesystem! Use fasthttp.FS with a sane Root instead.

#### func ServeFileLiteral ¶ added in v1.70.0

```
func ServeFileLiteral(ctx *RequestCtx, path string)
```

ServeFileLiteral returns HTTP response containing compressed file contents from the given path using literal path semantics.

Reserved URI characters in path such as '%', '?' and '#' are preserved instead of being interpreted during internal request URI processing.

HTTP response may contain uncompressed file contents in the following cases:

- Missing 'Accept-Encoding: gzip' request header.
- No write access to directory containing the file.

Directory contents is returned if path points to directory.

Use ServeFileUncompressed if you don't need serving compressed file contents.

See also RequestCtx.SendFileLiteral, ServeFile.

WARNING: do not pass any user supplied paths to this function! WARNING: if path is based on user input users will be able to request any file on your filesystem! Use fasthttp.FS with a sane Root instead.

#### func ServeFileUncompressed

```
func ServeFileUncompressed(ctx *RequestCtx, path string)
```

ServeFileUncompressed returns HTTP response containing file contents from the given path.

Directory contents is returned if path points to directory.

ServeFile may be used for saving network traffic when serving files with good compression ratio.

See also RequestCtx.SendFile.

WARNING: do not pass any user supplied paths to this function! WARNING: if path is based on user input users will be able to request any file on your filesystem! Use fasthttp.FS with a sane Root instead.

#### func ServeTLS

```
func ServeTLS(ln net.Listener, certFile, keyFile string, handler RequestHandler) error
```

ServeTLS serves HTTPS requests from the given net.Listener using the given handler.

certFile and keyFile are paths to TLS certificate and key files.

#### func ServeTLSEmbed

```
func ServeTLSEmbed(ln net.Listener, certData, keyData []byte, handler RequestHandler) error
```

ServeTLSEmbed serves HTTPS requests from the given net.Listener using the given handler.

certData and keyData must contain valid TLS certificate and key data.

#### func SetBodySizePoolLimit ¶ added in v1.34.0

```
func SetBodySizePoolLimit(reqBodyLimit, respBodyLimit int)
```

SetBodySizePoolLimit set the max body size for bodies to be returned to the pool. If the body size is larger it will be released instead of put back into the pool for reuse.

#### func StatusCodeIsRedirect ¶ added in v1.6.0

```
func StatusCodeIsRedirect(statusCode int) bool
```

StatusCodeIsRedirect returns true if the status code indicates a redirect.

#### func StatusMessage

```
func StatusMessage(statusCode int) string
```

StatusMessage returns HTTP status message for the given status code.

#### func VisitHeaderParams ¶ added in v1.52.0

```
func VisitHeaderParams(b []byte, f func(key, value []byte) bool)
```

VisitHeaderParams calls f for each parameter in the given header bytes. It stops processing when f returns false or an invalid parameter is found. Parameter values may be quoted, in which case \ is treated as an escape character, and the value is unquoted before being passed to value. See: https://www.rfc-editor.org/rfc/rfc9110#section-5.6.6

f must not retain references to key and/or value after returning. Copy key and/or value contents before returning if you need retaining them.

#### func WriteBrotli ¶ added in v1.13.0

```
func WriteBrotli(w io.Writer, p []byte) (int, error)
```

WriteBrotli writes brotlied p to w and returns the number of compressed bytes written to w.

#### func WriteBrotliLevel ¶ added in v1.13.0

```
func WriteBrotliLevel(w io.Writer, p []byte, level int) (int, error)
```

WriteBrotliLevel writes brotlied p to w using the given compression level and returns the number of compressed bytes written to w.

Supported compression levels are:

- CompressBrotliNoCompression
- CompressBrotliBestSpeed
- CompressBrotliBestCompression
- CompressBrotliDefaultCompression

#### func WriteDeflate

```
func WriteDeflate(w io.Writer, p []byte) (int, error)
```

WriteDeflate writes deflated p to w and returns the number of compressed bytes written to w.

#### func WriteDeflateLevel

```
func WriteDeflateLevel(w io.Writer, p []byte, level int) (int, error)
```

WriteDeflateLevel writes deflated p to w using the given compression level and returns the number of compressed bytes written to w.

Supported compression levels are:

- CompressNoCompression
- CompressBestSpeed
- CompressBestCompression
- CompressDefaultCompression
- CompressHuffmanOnly

#### func WriteGunzip

```
func WriteGunzip(w io.Writer, p []byte) (int, error)
```

WriteGunzip writes ungzipped p to w and returns the number of uncompressed bytes written to w.

#### func WriteGzip

```
func WriteGzip(w io.Writer, p []byte) (int, error)
```

WriteGzip writes gzipped p to w and returns the number of compressed bytes written to w.

#### func WriteGzipLevel

```
func WriteGzipLevel(w io.Writer, p []byte, level int) (int, error)
```

WriteGzipLevel writes gzipped p to w using the given compression level and returns the number of compressed bytes written to w.

Supported compression levels are:

- CompressNoCompression
- CompressBestSpeed
- CompressBestCompression
- CompressDefaultCompression
- CompressHuffmanOnly

#### func WriteInflate

```
func WriteInflate(w io.Writer, p []byte) (int, error)
```

WriteInflate writes inflated p to w and returns the number of uncompressed bytes written to w.

#### func WriteMultipartForm

```
func WriteMultipartForm(w io.Writer, f *multipart.Form, boundary string) error
```

WriteMultipartForm writes the given multipart form f with the given boundary to w.

#### func WriteUnbrotli ¶ added in v1.13.0

```
func WriteUnbrotli(w io.Writer, p []byte) (int, error)
```

WriteUnbrotli writes unbrotlied p to w and returns the number of uncompressed bytes written to w.

#### func WriteUnzstd ¶ added in v1.53.0

```
func WriteUnzstd(w io.Writer, p []byte) (int, error)
```

WriteUnzstd writes unzstd p to w and returns the number of uncompressed bytes written to w.

#### func WriteZstdLevel ¶ added in v1.53.0

```
func WriteZstdLevel(w io.Writer, p []byte, level int) (int, error)
```

### Types

#### type Args

```
type Args struct {
	
}
```

Args represents query arguments.

It is forbidden copying Args instances. Create new instances instead and use CopyTo().

Args instance MUST NOT be used from concurrently running goroutines.

#### func AcquireArgs

```
func AcquireArgs() *Args
```

AcquireArgs returns an empty Args object from the pool.

The returned Args may be returned to the pool with ReleaseArgs when no longer needed. This allows reducing GC load.

#### func (*Args) Add

```
func (a *Args) Add(key, value string)
```

Add adds 'key=value' argument.

Multiple values for the same key may be added.

#### func (*Args) AddBytesK

```
func (a *Args) AddBytesK(key []byte, value string)
```

AddBytesK adds 'key=value' argument.

Multiple values for the same key may be added.

#### func (*Args) AddBytesKNoValue ¶ added in v1.1.0

```
func (a *Args) AddBytesKNoValue(key []byte)
```

AddBytesKNoValue adds only 'key' as argument without the '='.

Multiple values for the same key may be added.

#### func (*Args) AddBytesKV

```
func (a *Args) AddBytesKV(key, value []byte)
```

AddBytesKV adds 'key=value' argument.

Multiple values for the same key may be added.

#### func (*Args) AddBytesV

```
func (a *Args) AddBytesV(key string, value []byte)
```

AddBytesV adds 'key=value' argument.

Multiple values for the same key may be added.

#### func (*Args) AddNoValue ¶ added in v1.1.0

```
func (a *Args) AddNoValue(key string)
```

AddNoValue adds only 'key' as argument without the '='.

Multiple values for the same key may be added.

#### func (*Args) All ¶ added in v1.63.0

```
func (a *Args) All() iter.Seq2[[]byte, []byte]
```

All returns an iterator over key-value pairs from args.

The key and value may invalid outside the iteration loop. Make copies if you need to use them after the loop ends.

Making modifications to the Args during the iteration loop leads to undefined behavior and can cause panics.

#### func (*Args) AppendBytes

```
func (a *Args) AppendBytes(dst []byte) []byte
```

AppendBytes appends query string to dst and returns the extended dst.

#### func (*Args) CopyTo

```
func (a *Args) CopyTo(dst *Args)
```

CopyTo copies all args to dst.

#### func (*Args) Del

```
func (a *Args) Del(key string)
```

Del deletes argument with the given key from query args.

#### func (*Args) DelBytes

```
func (a *Args) DelBytes(key []byte)
```

DelBytes deletes argument with the given key from query args.

#### func (*Args) GetBool

```
func (a *Args) GetBool(key string) bool
```

GetBool returns boolean value for the given key.

true is returned for "1", "t", "T", "true", "TRUE", "True", "y", "yes", "Y", "YES", "Yes", otherwise false is returned.

#### func (*Args) GetUfloat

```
func (a *Args) GetUfloat(key string) (float64, error)
```

GetUfloat returns ufloat value for the given key.

#### func (*Args) GetUfloatOrZero

```
func (a *Args) GetUfloatOrZero(key string) float64
```

GetUfloatOrZero returns ufloat value for the given key.

Zero (0) is returned on error.

#### func (*Args) GetUint

```
func (a *Args) GetUint(key string) (int, error)
```

GetUint returns uint value for the given key.

#### func (*Args) GetUintOrZero

```
func (a *Args) GetUintOrZero(key string) int
```

GetUintOrZero returns uint value for the given key.

Zero (0) is returned on error.

#### func (*Args) Has

```
func (a *Args) Has(key string) bool
```

Has returns true if the given key exists in Args.

#### func (*Args) HasBytes

```
func (a *Args) HasBytes(key []byte) bool
```

HasBytes returns true if the given key exists in Args.

#### func (*Args) Len

```
func (a *Args) Len() int
```

Len returns the number of query args.

#### func (*Args) Parse

```
func (a *Args) Parse(s string)
```

Parse parses the given string containing query args.

#### func (*Args) ParseBytes

```
func (a *Args) ParseBytes(b []byte)
```

ParseBytes parses the given b containing query args.

#### func (*Args) Peek

```
func (a *Args) Peek(key string) []byte
```

Peek returns query arg value for the given key.

The returned value is valid until the Args is reused or released (ReleaseArgs). Do not store references to the returned value. Make copies instead.

#### func (*Args) PeekBytes

```
func (a *Args) PeekBytes(key []byte) []byte
```

PeekBytes returns query arg value for the given key.

The returned value is valid until the Args is reused or released (ReleaseArgs). Do not store references to the returned value. Make copies instead.

#### func (*Args) PeekMulti

```
func (a *Args) PeekMulti(key string) [][]byte
```

PeekMulti returns all the arg values for the given key.

#### func (*Args) PeekMultiBytes

```
func (a *Args) PeekMultiBytes(key []byte) [][]byte
```

PeekMultiBytes returns all the arg values for the given key.

#### func (*Args) QueryString

```
func (a *Args) QueryString() []byte
```

QueryString returns query string for the args.

The returned value is valid until the Args is reused or released (ReleaseArgs). Do not store references to the returned value. Make copies instead.

#### func (*Args) Reset

```
func (a *Args) Reset()
```

Reset clears query args.

#### func (*Args) Set

```
func (a *Args) Set(key, value string)
```

Set sets 'key=value' argument.

#### func (*Args) SetBytesK

```
func (a *Args) SetBytesK(key []byte, value string)
```

SetBytesK sets 'key=value' argument.

#### func (*Args) SetBytesKNoValue ¶ added in v1.1.0

```
func (a *Args) SetBytesKNoValue(key []byte)
```

SetBytesKNoValue sets 'key' argument.

#### func (*Args) SetBytesKV

```
func (a *Args) SetBytesKV(key, value []byte)
```

SetBytesKV sets 'key=value' argument.

#### func (*Args) SetBytesV

```
func (a *Args) SetBytesV(key string, value []byte)
```

SetBytesV sets 'key=value' argument.

#### func (*Args) SetNoValue ¶ added in v1.1.0

```
func (a *Args) SetNoValue(key string)
```

SetNoValue sets only 'key' as argument without the '='.

Only key in argument, like key1&key2.

#### func (*Args) SetUint

```
func (a *Args) SetUint(key string, value int)
```

SetUint sets uint value for the given key.

#### func (*Args) SetUintBytes

```
func (a *Args) SetUintBytes(key []byte, value int)
```

SetUintBytes sets uint value for the given key.

#### func (*Args) Sort ¶ added in v1.1.0

```
func (a *Args) Sort(f func(x, y []byte) int)
```

Sort sorts Args by key and then value using 'f' as comparison function.

For example args.Sort(bytes.Compare).

#### func (*Args) SortKeys ¶ added in v1.69.0

```
func (a *Args) SortKeys(f func(x, y []byte) int)
```

SortKeys sorts Args by key only using 'f' as comparison function.

For example args.SortKeys(bytes.Compare).

#### func (*Args) String

```
func (a *Args) String() string
```

String returns string representation of query args.

#### func (*Args) VisitAll deprecated

```
func (a *Args) VisitAll(f func(key, value []byte))
```

VisitAll calls f for each existing arg.

f must not retain references to key and value after returning. Make key and/or value copies if you need storing them after returning.

Deprecated: Use All instead.

#### func (*Args) WriteTo

```
func (a *Args) WriteTo(w io.Writer) (int64, error)
```

WriteTo writes query string to w.

WriteTo implements io.WriterTo interface.

#### type BalancingClient

```
type BalancingClient interface {
	DoDeadline(req *Request, resp *Response, deadline time.Time) error
	PendingRequests() int
}
```

BalancingClient is the interface for clients, which may be passed to LBClient.Clients.

#### type CacheKind ¶ added in v1.51.0

```
type CacheKind uint8
```

#### type Client

```
type Client struct {

	
	Transport RoundTripper

	
	
	
	DialTimeout DialFuncWithTimeout

	
	
	
	
	
	
	Dial DialFunc

	
	
	
	TLSConfig *tls.Config

	
	
	
	
	
	
	RetryIf RetryIfFunc

	
	
	
	
	RetryIfErr RetryIfErrFunc

	
	
	RetryIfErrUpstream RetryIfErrUpstreamFunc

	
	ConfigureClient func(hc *HostClient) error

	
	
	
	Name string

	
	
	
	MaxConnsPerHost int

	
	
	
	
	MaxIdleConnDuration time.Duration

	
	
	
	MaxConnDuration time.Duration

	
	
	
	MaxIdemponentCallAttempts int

	
	
	
	
	ReadBufferSize int

	
	
	
	WriteBufferSize int

	
	
	
	ReadTimeout time.Duration

	
	
	
	WriteTimeout time.Duration

	
	
	
	
	
	
	
	
	MaxResponseBodySize int

	
	
	
	MaxConnWaitTimeout time.Duration

	
	ConnPoolStrategy ConnPoolStrategyType

	
	
	NoDefaultUserAgentHeader bool

	
	
	
	
	
	
	
	DialDualStack bool

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	DisableHeaderNamesNormalizing bool

	
	
	
	
	
	
	
	DisablePathNormalizing bool

	
	StreamResponseBody bool
	
}
```

Client implements http client.

Copying Client by value is prohibited. Create new instance instead.

It is safe calling Client methods from concurrently running goroutines.

The fields of a Client should not be changed while it is in use.

#### func (*Client) CloseIdleConnections ¶ added in v1.17.0

```
func (c *Client) CloseIdleConnections()
```

CloseIdleConnections closes any connections which were previously connected from previous requests but are now sitting idle in a "keep-alive" state. It does not interrupt any connections currently in use.

#### func (*Client) ConnsCount ¶ added in v1.72.0

```
func (c *Client) ConnsCount() int
```

ConnsCount returns total connection count across all HostClients managed by Client.

#### func (*Client) Do

```
func (c *Client) Do(req *Request, resp *Response) error
```

Do performs the given http request and fills the given http response.

Request must contain at least non-zero RequestURI with full url (including scheme and host) or non-zero Host header + RequestURI.

Client determines the server to be requested in the following order:

- from RequestURI if it contains full url with scheme and host;
- from Host header otherwise.

Response is ignored if resp is nil.

The function doesn't follow redirects. Use Get* for following redirects.

ErrNoFreeConns is returned if all Client.MaxConnsPerHost connections to the requested host are busy.

It is recommended obtaining req and resp via AcquireRequest and AcquireResponse in performance-critical code.

#### func (*Client) DoDeadline

```
func (c *Client) DoDeadline(req *Request, resp *Response, deadline time.Time) error
```

DoDeadline performs the given request and waits for response until the given deadline.

Request must contain at least non-zero RequestURI with full url (including scheme and host) or non-zero Host header + RequestURI.

Client determines the server to be requested in the following order:

- from RequestURI if it contains full url with scheme and host;
- from Host header otherwise.

The function doesn't follow redirects. Use Get* for following redirects.

Response is ignored if resp is nil.

ErrTimeout is returned if the response wasn't returned until the given deadline. Immediately returns ErrTimeout if the deadline has already been reached.

ErrNoFreeConns is returned if all Client.MaxConnsPerHost connections to the requested host are busy.

It is recommended obtaining req and resp via AcquireRequest and AcquireResponse in performance-critical code.

#### func (*Client) DoRedirects ¶ added in v1.10.0

```
func (c *Client) DoRedirects(req *Request, resp *Response, maxRedirectsCount int) error
```

DoRedirects performs the given http request and fills the given http response, following up to maxRedirectsCount redirects. When the redirect count exceeds maxRedirectsCount, ErrTooManyRedirects is returned.

Request must contain at least non-zero RequestURI with full url (including scheme and host) or non-zero Host header + RequestURI.

Client determines the server to be requested in the following order:

- from RequestURI if it contains full url with scheme and host;
- from Host header otherwise.

Response is ignored if resp is nil.

ErrNoFreeConns is returned if all DefaultMaxConnsPerHost connections to the requested host are busy.

It is recommended obtaining req and resp via AcquireRequest and AcquireResponse in performance-critical code.

#### func (*Client) DoTimeout

```
func (c *Client) DoTimeout(req *Request, resp *Response, timeout time.Duration) error
```

DoTimeout performs the given request and waits for response during the given timeout duration.

Request must contain at least non-zero RequestURI with full url (including scheme and host) or non-zero Host header + RequestURI.

Client determines the server to be requested in the following order:

- from RequestURI if it contains full url with scheme and host;
- from Host header otherwise.

The function doesn't follow redirects. Use Get* for following redirects.

Response is ignored if resp is nil.

ErrTimeout is returned if the response wasn't returned during the given timeout. Immediately returns ErrTimeout if timeout value is negative.

ErrNoFreeConns is returned if all Client.MaxConnsPerHost connections to the requested host are busy.

It is recommended obtaining req and resp via AcquireRequest and AcquireResponse in performance-critical code.

#### func (*Client) Get

```
func (c *Client) Get(dst []byte, url string) (statusCode int, body []byte, err error)
```

Get returns the status code and body of url.

The contents of dst will be replaced by the body and returned, if the dst is too small a new slice will be allocated.

The function follows redirects. Use Do* for manually handling redirects.

#### func (*Client) GetDeadline

```
func (c *Client) GetDeadline(dst []byte, url string, deadline time.Time) (statusCode int, body []byte, err error)
```

GetDeadline returns the status code and body of url.

The contents of dst will be replaced by the body and returned, if the dst is too small a new slice will be allocated.

The function follows redirects. Use Do* for manually handling redirects.

ErrTimeout error is returned if url contents couldn't be fetched until the given deadline.

#### func (*Client) GetTimeout

```
func (c *Client) GetTimeout(dst []byte, url string, timeout time.Duration) (statusCode int, body []byte, err error)
```

GetTimeout returns the status code and body of url.

The contents of dst will be replaced by the body and returned, if the dst is too small a new slice will be allocated.

The function follows redirects. Use Do* for manually handling redirects.

ErrTimeout error is returned if url contents couldn't be fetched during the given timeout.

#### func (*Client) IdleConnsCount ¶ added in v1.72.0

```
func (c *Client) IdleConnsCount() int
```

IdleConnsCount returns total idle connection count across all HostClients managed by Client.

#### func (*Client) Post

```
func (c *Client) Post(dst []byte, url string, postArgs *Args) (statusCode int, body []byte, err error)
```

Post sends POST request to the given url with the given POST arguments.

The contents of dst will be replaced by the body and returned, if the dst is too small a new slice will be allocated.

The function follows redirects. Use Do* for manually handling redirects.

Empty POST body is sent if postArgs is nil.

#### type ConnPoolStrategyType ¶ added in v1.35.0

```
type ConnPoolStrategyType int
```

ConnPoolStrategyType define strategy of connection pool enqueue/dequeue.

```
const (
	FIFO ConnPoolStrategyType = iota
	LIFO
)
```

#### type ConnState ¶ added in v1.0.0

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

#### func (ConnState) String ¶ added in v1.0.0

```
func (c ConnState) String() string
```

```
type Cookie struct {
	
}
```

Cookie represents HTTP response cookie.

Do not copy Cookie objects. Create new object and use CopyTo instead.

Cookie instance MUST NOT be used from concurrently running goroutines.

#### func AcquireCookie

```
func AcquireCookie() *Cookie
```

AcquireCookie returns an empty Cookie object from the pool.

The returned object may be returned back to the pool with ReleaseCookie. This allows reducing GC load.

#### func (*Cookie) AppendBytes

```
func (c *Cookie) AppendBytes(dst []byte) []byte
```

AppendBytes appends cookie representation to dst and returns the extended dst.

#### func (*Cookie) Cookie

```
func (c *Cookie) Cookie() []byte
```

Cookie returns cookie representation.

The returned value is valid until the Cookie reused or released (ReleaseCookie). Do not store references to the returned value. Make copies instead.

#### func (*Cookie) CopyTo

```
func (c *Cookie) CopyTo(src *Cookie)
```

CopyTo copies src cookie to c.

#### func (*Cookie) Domain

```
func (c *Cookie) Domain() []byte
```

Domain returns cookie domain.

The returned value is valid until the Cookie reused or released (ReleaseCookie). Do not store references to the returned value. Make copies instead.

#### func (*Cookie) Expire

```
func (c *Cookie) Expire() time.Time
```

Expire returns cookie expiration time.

CookieExpireUnlimited is returned if cookie doesn't expire.

#### func (*Cookie) HTTPOnly

```
func (c *Cookie) HTTPOnly() bool
```

HTTPOnly returns true if the cookie is http only.

#### func (*Cookie) Key

```
func (c *Cookie) Key() []byte
```

Key returns cookie name.

The returned value is valid until the Cookie reused or released (ReleaseCookie). Do not store references to the returned value. Make copies instead.

#### func (*Cookie) MaxAge ¶ added in v1.0.0

```
func (c *Cookie) MaxAge() int
```

MaxAge returns the seconds until the cookie is meant to expire or 0 if no max age.

#### func (*Cookie) Parse

```
func (c *Cookie) Parse(src string) error
```

Parse parses Set-Cookie header.

#### func (*Cookie) ParseBytes

```
func (c *Cookie) ParseBytes(src []byte) error
```

ParseBytes parses Set-Cookie header.

#### func (*Cookie) Partitioned ¶ added in v1.53.0

```
func (c *Cookie) Partitioned() bool
```

Partitioned returns true if the cookie is partitioned.

#### func (*Cookie) Path

```
func (c *Cookie) Path() []byte
```

Path returns cookie path.

#### func (*Cookie) Reset

```
func (c *Cookie) Reset()
```

Reset clears the cookie.

#### func (*Cookie) SameSite ¶ added in v1.1.0

```
func (c *Cookie) SameSite() CookieSameSite
```

SameSite returns the SameSite mode.

#### func (*Cookie) Secure

```
func (c *Cookie) Secure() bool
```

Secure returns true if the cookie is secure.

#### func (*Cookie) SetDomain

```
func (c *Cookie) SetDomain(domain string)
```

SetDomain sets cookie domain.

#### func (*Cookie) SetDomainBytes

```
func (c *Cookie) SetDomainBytes(domain []byte)
```

SetDomainBytes sets cookie domain.

#### func (*Cookie) SetExpire

```
func (c *Cookie) SetExpire(expire time.Time)
```

SetExpire sets cookie expiration time.

Set expiration time to CookieExpireDelete for expiring (deleting) the cookie on the client.

By default cookie lifetime is limited by browser session.

#### func (*Cookie) SetHTTPOnly

```
func (c *Cookie) SetHTTPOnly(httpOnly bool)
```

SetHTTPOnly sets cookie's httpOnly flag to the given value.

#### func (*Cookie) SetKey

```
func (c *Cookie) SetKey(key string)
```

SetKey sets cookie name.

#### func (*Cookie) SetKeyBytes

```
func (c *Cookie) SetKeyBytes(key []byte)
```

SetKeyBytes sets cookie name.

#### func (*Cookie) SetMaxAge ¶ added in v1.0.0

```
func (c *Cookie) SetMaxAge(seconds int)
```

SetMaxAge sets cookie expiration time based on seconds. This takes precedence over any absolute expiry set on the cookie.

'max-age' is set when the maxAge is non-zero. That is, if maxAge = 0, the 'max-age' is unset. If maxAge < 0, it indicates that the cookie should be deleted immediately, equivalent to 'max-age=0'. This behavior is consistent with the Go standard library's net/http package.

#### func (*Cookie) SetPartitioned ¶ added in v1.53.0

```
func (c *Cookie) SetPartitioned(partitioned bool)
```

SetPartitioned sets the cookie's Partitioned flag to the given value. Set value Partitioned to true will set Secure to true and Path to / also to avoid browser rejection.

#### func (*Cookie) SetPath

```
func (c *Cookie) SetPath(path string)
```

SetPath sets cookie path.

#### func (*Cookie) SetPathBytes

```
func (c *Cookie) SetPathBytes(path []byte)
```

SetPathBytes sets cookie path.

#### func (*Cookie) SetSameSite ¶ added in v1.1.0

```
func (c *Cookie) SetSameSite(mode CookieSameSite)
```

SetSameSite sets the cookie's SameSite flag to the given value. Set value CookieSameSiteNoneMode will set Secure to true also to avoid browser rejection.

#### func (*Cookie) SetSecure

```
func (c *Cookie) SetSecure(secure bool)
```

SetSecure sets cookie's secure flag to the given value.

#### func (*Cookie) SetValue

```
func (c *Cookie) SetValue(value string)
```

SetValue sets cookie value.

#### func (*Cookie) SetValueBytes

```
func (c *Cookie) SetValueBytes(value []byte)
```

SetValueBytes sets cookie value.

#### func (*Cookie) String

```
func (c *Cookie) String() string
```

String returns cookie representation.

#### func (*Cookie) Value

```
func (c *Cookie) Value() []byte
```

Value returns cookie value.

The returned value is valid until the Cookie reused or released (ReleaseCookie). Do not store references to the returned value. Make copies instead.

#### func (*Cookie) WriteTo

```
func (c *Cookie) WriteTo(w io.Writer) (int64, error)
```

WriteTo writes cookie representation to w.

WriteTo implements io.WriterTo interface.

#### type CookieSameSite ¶ added in v1.1.0

```
type CookieSameSite int
```

CookieSameSite is an enum for the mode in which the SameSite flag should be set for the given cookie. See https://tools.ietf.org/html/draft-ietf-httpbis-cookie-same-site-00 for details.

```
const (
	
	CookieSameSiteDisabled CookieSameSite = iota
	
	CookieSameSiteDefaultMode
	
	CookieSameSiteLaxMode
	
	CookieSameSiteStrictMode
	
	
	CookieSameSiteNoneMode 
)
```

#### type DialFunc

```
type DialFunc func(addr string) (net.Conn, error)
```

DialFunc must establish connection to addr.

There is no need in establishing TLS (SSL) connection for https. The client automatically converts connection to TLS if HostClient.IsTLS is set.

TCP address passed to DialFunc always contains host and port. Example TCP addr values:

- foobar.com:80
- foobar.com:443
- foobar.com:8080

#### type DialFuncWithTimeout ¶ added in v1.52.0

```
type DialFuncWithTimeout func(addr string, timeout time.Duration) (net.Conn, error)
```

DialFuncWithTimeout must establish connection to addr. Unlike DialFunc, it also accepts a timeout.

There is no need in establishing TLS (SSL) connection for https. The client automatically converts connection to TLS if HostClient.IsTLS is set.

TCP address passed to DialFuncWithTimeout always contains host and port. Example TCP addr values:

- foobar.com:80
- foobar.com:443
- foobar.com:8080

#### type ErrBodyStreamWritePanic ¶ added in v1.7.0

```
type ErrBodyStreamWritePanic struct {
	
}
```

ErrBodyStreamWritePanic is returned when panic happens during writing body stream.

#### type ErrBrokenChunk ¶ added in v1.1.0

```
type ErrBrokenChunk struct {
	
}
```

ErrBrokenChunk is returned when server receives a broken chunked body (Transfer-Encoding: chunked).

#### type ErrDialWithUpstream ¶ added in v1.53.0

```
type ErrDialWithUpstream struct {
	Upstream string
	
}
```

ErrDialWithUpstream wraps dial error with upstream info.

Should use errors.As to get upstream information from error:

```
hc := fasthttp.HostClient{Addr: "foo.com,bar.com"}
err := hc.Do(req, res)

var dialErr *fasthttp.ErrDialWithUpstream
if errors.As(err, &dialErr) {
	upstream = dialErr.Upstream // 34.206.39.153:80
}
```

#### func (*ErrDialWithUpstream) Error ¶ added in v1.53.0

```
func (e *ErrDialWithUpstream) Error() string
```

#### func (*ErrDialWithUpstream) Unwrap ¶ added in v1.53.0

```
func (e *ErrDialWithUpstream) Unwrap() error
```

#### type ErrNothingRead ¶ added in v1.15.0

```
type ErrNothingRead struct {
	
}
```

ErrNothingRead is returned when a keep-alive connection is closed, either because the remote closed it or because of a read timeout.

#### type ErrSmallBuffer

```
type ErrSmallBuffer struct {
	
}
```

ErrSmallBuffer is returned when the provided buffer size is too small for reading request and/or response headers.

ReadBufferSize value from Server or clients should reduce the number of such errors.

#### type EscapeError ¶ added in v1.31.0

```
type EscapeError string
```

#### func (EscapeError) Error ¶ added in v1.31.0

```
func (e EscapeError) Error() string
```

#### type FS

```
type FS struct {

	
	FS fs.FS

	
	
	
	PathRewrite PathRewriteFunc

	
	
	
	
	
	
	PathNotFound RequestHandler

	
	
	
	
	
	CompressedFileSuffixes map[string]string

	
	
	
	CleanStop chan struct{}

	
	Root string

	
	
	CompressRoot string

	
	
	
	
	
	CompressedFileSuffix string

	
	
	
	
	
	
	
	
	
	IndexNames []string

	
	
	
	CacheDuration time.Duration

	
	
	
	
	AllowEmptyRoot bool

	
	
	
	
	
	CompressBrotli bool

	
	
	
	
	
	CompressZstd bool

	
	
	
	
	
	
	
	
	GenerateIndexPages bool

	
	
	
	
	
	
	
	
	
	
	Compress bool

	
	
	
	AcceptByteRange bool

	
	
	
	SkipCache bool
	
}
```

FS represents settings for request handler serving static files from the local filesystem.

It is prohibited copying FS values. Create new values instead.

Example

¶

```
package main

import (
	"log"

	"github.com/valyala/fasthttp"
)

func main() {
	fs := &fasthttp.FS{
		// Path to directory to serve.
		Root: "/var/www/static-site",

		// Generate index pages if client requests directory contents.
		GenerateIndexPages: true,

		// Enable transparent compression to save network traffic.
		Compress: true,
	}

	// Create request handler for serving static files.
	h := fs.NewRequestHandler()

	// Start the server.
	if err := fasthttp.ListenAndServe(":8080", h); err != nil {
		log.Fatalf("error in ListenAndServe: %v", err)
	}
}
```

```
Output:
```

#### func (*FS) NewRequestHandler

```
func (fs *FS) NewRequestHandler() RequestHandler
```

NewRequestHandler returns new request handler with the given FS settings.

The returned handler caches requested file handles for FS.CacheDuration. Make sure your program has enough 'max open files' limit aka 'ulimit -n' if FS.Root folder contains many files.

Do not create multiple request handlers from a single FS instance - just reuse a single request handler.

#### type FormValueFunc ¶ added in v1.44.0

```
type FormValueFunc func(*RequestCtx, string) []byte
```

FormValueFunc customizes how RequestCtx.FormValue resolves a value.

#### type HijackHandler

```
type HijackHandler func(c net.Conn)
```

HijackHandler must process the hijacked connection c.

If KeepHijackedConns is disabled, which is by default, the connection c is automatically closed after returning from HijackHandler.

The connection c must not be used after returning from the handler, if KeepHijackedConns is disabled.

When KeepHijackedConns enabled, fasthttp will not Close() the connection, you must do it when you need it. You must not use c in any way after calling Close().

#### type HostClient

```
type HostClient struct {

	
	Transport RoundTripper

	
	
	
	DialTimeout DialFuncWithTimeout

	
	
	
	
	
	
	Dial DialFunc

	
	TLSConfig *tls.Config

	
	
	
	
	
	RetryIf RetryIfFunc

	
	
	
	
	RetryIfErr RetryIfErrFunc

	
	
	RetryIfErrUpstream RetryIfErrUpstreamFunc

	
	
	
	
	
	
	
	
	
	Addr string

	
	Name string

	
	
	
	
	
	
	
	MaxConns int

	
	
	
	MaxConnDuration time.Duration

	
	
	
	
	MaxIdleConnDuration time.Duration

	
	
	
	
	
	
	MaxIdemponentCallAttempts int

	
	
	
	
	ReadBufferSize int

	
	
	
	WriteBufferSize int

	
	
	
	ReadTimeout time.Duration

	
	
	
	WriteTimeout time.Duration

	
	
	
	
	
	
	MaxResponseBodySize int

	
	
	
	MaxConnWaitTimeout time.Duration

	
	ConnPoolStrategy ConnPoolStrategyType

	
	
	NoDefaultUserAgentHeader bool

	
	
	
	
	
	
	
	
	DialDualStack bool

	
	IsTLS bool

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	DisableHeaderNamesNormalizing bool

	
	
	
	
	
	
	
	DisablePathNormalizing bool

	
	
	
	
	
	
	SecureErrorLogMessage bool

	
	StreamResponseBody bool
	
}
```

HostClient balances http requests among hosts listed in Addr.

HostClient may be used for balancing load among multiple upstream hosts. While multiple addresses passed to HostClient.Addr may be used for balancing load among them, it would be better using LBClient instead, since HostClient may unevenly balance load among upstream hosts.

It is forbidden copying HostClient instances. Create new instances instead.

It is safe calling HostClient methods from concurrently running goroutines.

Example

¶

```
package main

import (
	"log"

	"github.com/valyala/fasthttp"
)

func main() {
	// Prepare a client, which fetches webpages via HTTP proxy listening
	// on the localhost:8080.
	c := &fasthttp.HostClient{
		Addr: "localhost:8080",
	}

	// Fetch google page via local proxy.
	statusCode, body, err := c.Get(nil, "http://google.com/foo/bar")
	if err != nil {
		log.Fatalf("Error when loading google page through local proxy: %v", err)
	}
	if statusCode != fasthttp.StatusOK {
		log.Fatalf("Unexpected status code: %d. Expecting %d", statusCode, fasthttp.StatusOK)
	}
	useResponseBody(body)

	// Fetch foobar page via local proxy. Reuse body buffer.
	statusCode, body, err = c.Get(body, "http://foobar.com/google/com")
	if err != nil {
		log.Fatalf("Error when loading foobar page through local proxy: %v", err)
	}
	if statusCode != fasthttp.StatusOK {
		log.Fatalf("Unexpected status code: %d. Expecting %d", statusCode, fasthttp.StatusOK)
	}
	useResponseBody(body)
}

func useResponseBody(body []byte) {
	// Do something with body :)
}
```

```
Output:
```

#### func (*HostClient) AcquireConn ¶ added in v1.59.0

```
func (c *HostClient) AcquireConn(reqTimeout time.Duration, connectionClose bool) (cc *clientConn, err error)
```

#### func (*HostClient) AcquireReader ¶ added in v1.59.0

```
func (c *HostClient) AcquireReader(conn net.Conn) *bufio.Reader
```

#### func (*HostClient) AcquireWriter ¶ added in v1.59.0

```
func (c *HostClient) AcquireWriter(conn net.Conn) *bufio.Writer
```

#### func (*HostClient) CloseConn ¶ added in v1.59.0

```
func (c *HostClient) CloseConn(cc *clientConn)
```

#### func (*HostClient) CloseIdleConnections ¶ added in v1.17.0

```
func (c *HostClient) CloseIdleConnections()
```

CloseIdleConnections closes any connections which were previously connected from previous requests but are now sitting idle in a "keep-alive" state. It does not interrupt any connections currently in use.

#### func (*HostClient) ConnsCount ¶ added in v1.22.0

```
func (c *HostClient) ConnsCount() int
```

ConnsCount returns connection count of HostClient.

#### func (*HostClient) Do

```
func (c *HostClient) Do(req *Request, resp *Response) error
```

Do performs the given http request and sets the corresponding response.

Request must contain at least non-zero RequestURI with full url (including scheme and host) or non-zero Host header + RequestURI.

The function doesn't follow redirects. Use Get* for following redirects.

Response is ignored if resp is nil.

ErrNoFreeConns is returned if all HostClient.MaxConns connections to the host are busy.

It is recommended obtaining req and resp via AcquireRequest and AcquireResponse in performance-critical code.

#### func (*HostClient) DoDeadline

```
func (c *HostClient) DoDeadline(req *Request, resp *Response, deadline time.Time) error
```

DoDeadline performs the given request and waits for response until the given deadline.

Request must contain at least non-zero RequestURI with full url (including scheme and host) or non-zero Host header + RequestURI.

The function doesn't follow redirects. Use Get* for following redirects.

Response is ignored if resp is nil.

ErrTimeout is returned if the response wasn't returned until the given deadline. Immediately returns ErrTimeout if the deadline has already been reached.

ErrNoFreeConns is returned if all HostClient.MaxConns connections to the host are busy.

It is recommended obtaining req and resp via AcquireRequest and AcquireResponse in performance-critical code.

#### func (*HostClient) DoRedirects ¶ added in v1.10.0

```
func (c *HostClient) DoRedirects(req *Request, resp *Response, maxRedirectsCount int) error
```

DoRedirects performs the given http request and fills the given http response, following up to maxRedirectsCount redirects. When the redirect count exceeds maxRedirectsCount, ErrTooManyRedirects is returned.

Request must contain at least non-zero RequestURI with full url (including scheme and host) or non-zero Host header + RequestURI.

Client determines the server to be requested in the following order:

- from RequestURI if it contains full url with scheme and host;
- from Host header otherwise.

Response is ignored if resp is nil.

ErrNoFreeConns is returned if all DefaultMaxConnsPerHost connections to the requested host are busy.

It is recommended obtaining req and resp via AcquireRequest and AcquireResponse in performance-critical code.

#### func (*HostClient) DoTimeout

```
func (c *HostClient) DoTimeout(req *Request, resp *Response, timeout time.Duration) error
```

DoTimeout performs the given request and waits for response during the given timeout duration.

Request must contain at least non-zero RequestURI with full url (including scheme and host) or non-zero Host header + RequestURI.

The function doesn't follow redirects. Use Get* for following redirects.

Response is ignored if resp is nil.

ErrTimeout is returned if the response wasn't returned during the given timeout. Immediately returns ErrTimeout if timeout value is negative.

ErrNoFreeConns is returned if all HostClient.MaxConns connections to the host are busy.

It is recommended obtaining req and resp via AcquireRequest and AcquireResponse in performance-critical code.

#### func (*HostClient) Get

```
func (c *HostClient) Get(dst []byte, url string) (statusCode int, body []byte, err error)
```

Get returns the status code and body of url.

The contents of dst will be replaced by the body and returned, if the dst is too small a new slice will be allocated.

The function follows redirects. Use Do* for manually handling redirects.

#### func (*HostClient) GetDeadline

```
func (c *HostClient) GetDeadline(dst []byte, url string, deadline time.Time) (statusCode int, body []byte, err error)
```

GetDeadline returns the status code and body of url.

The contents of dst will be replaced by the body and returned, if the dst is too small a new slice will be allocated.

The function follows redirects. Use Do* for manually handling redirects.

ErrTimeout error is returned if url contents couldn't be fetched until the given deadline.

#### func (*HostClient) GetTimeout

```
func (c *HostClient) GetTimeout(dst []byte, url string, timeout time.Duration) (statusCode int, body []byte, err error)
```

GetTimeout returns the status code and body of url.

The contents of dst will be replaced by the body and returned, if the dst is too small a new slice will be allocated.

The function follows redirects. Use Do* for manually handling redirects.

ErrTimeout error is returned if url contents couldn't be fetched during the given timeout.

#### func (*HostClient) IdleConnsCount ¶ added in v1.72.0

```
func (c *HostClient) IdleConnsCount() int
```

IdleConnsCount returns idle connection count of HostClient.

#### func (*HostClient) LastUseTime

```
func (c *HostClient) LastUseTime() time.Time
```

LastUseTime returns time the client was last used.

#### func (*HostClient) PendingRequests

```
func (c *HostClient) PendingRequests() int
```

PendingRequests returns the current number of requests the client is executing.

This function may be used for balancing load among multiple HostClient instances.

#### func (*HostClient) Post

```
func (c *HostClient) Post(dst []byte, url string, postArgs *Args) (statusCode int, body []byte, err error)
```

Post sends POST request to the given url with the given POST arguments.

The contents of dst will be replaced by the body and returned, if the dst is too small a new slice will be allocated.

The function follows redirects. Use Do* for manually handling redirects.

Empty POST body is sent if postArgs is nil.

#### func (*HostClient) ReleaseConn ¶ added in v1.59.0

```
func (c *HostClient) ReleaseConn(cc *clientConn)
```

#### func (*HostClient) ReleaseReader ¶ added in v1.59.0

```
func (c *HostClient) ReleaseReader(br *bufio.Reader)
```

#### func (*HostClient) ReleaseWriter ¶ added in v1.59.0

```
func (c *HostClient) ReleaseWriter(bw *bufio.Writer)
```

#### func (*HostClient) SetMaxConns ¶ added in v1.2.0

```
func (c *HostClient) SetMaxConns(newMaxConns int)
```

SetMaxConns sets up the maximum number of connections which may be established to all hosts listed in Addr.

#### type InvalidHostError ¶ added in v1.31.0

```
type InvalidHostError string
```

#### func (InvalidHostError) Error ¶ added in v1.31.0

```
func (e InvalidHostError) Error() string
```

#### type LBClient

```
type LBClient struct {

	
	
	
	
	
	
	
	
	
	HealthCheck func(req *Request, resp *Response, err error) bool

	
	
	Clients []BalancingClient

	
	
	
	Timeout time.Duration
	
}
```

LBClient balances requests among available LBClient.Clients.

It has the following features:

- Balances load among available clients using 'least loaded' + 'least total' hybrid technique.
- Dynamically decreases load on unhealthy clients.

It is forbidden copying LBClient instances. Create new instances instead.

It is safe calling LBClient methods from concurrently running goroutines.

Example

¶

```
// Requests will be spread among these servers.
servers := []string{
	"google.com:80",
	"foobar.com:8080",
	"127.0.0.1:123",
}

// Prepare clients for each server
var lbc fasthttp.LBClient
for _, addr := range servers {
	c := &fasthttp.HostClient{
		Addr: addr,
	}
	lbc.Clients = append(lbc.Clients, c)
}

// Send requests to load-balanced servers
var req fasthttp.Request
var resp fasthttp.Response
for i := range 10 {
	url := fmt.Sprintf("http://abcedfg/foo/bar/%d", i)
	req.SetRequestURI(url)
	if err := lbc.Do(&req, &resp); err != nil {
		log.Fatalf("Error when sending request: %v", err)
	}
	if resp.StatusCode() != fasthttp.StatusOK {
		log.Fatalf("unexpected status code: %d. Expecting %d", resp.StatusCode(), fasthttp.StatusOK)
	}

	useResponseBody(resp.Body())
}
```

#### func (*LBClient) AddClient ¶ added in v1.35.0

```
func (cc *LBClient) AddClient(c BalancingClient) int
```

AddClient adds a new client to the balanced clients and returns the new total number of clients.

#### func (*LBClient) Do

```
func (cc *LBClient) Do(req *Request, resp *Response) error
```

Do calculates timeout using LBClient.Timeout and calls DoTimeout on the least loaded client.

#### func (*LBClient) DoDeadline

```
func (cc *LBClient) DoDeadline(req *Request, resp *Response, deadline time.Time) error
```

DoDeadline calls DoDeadline on the least loaded client.

#### func (*LBClient) DoTimeout

```
func (cc *LBClient) DoTimeout(req *Request, resp *Response, timeout time.Duration) error
```

DoTimeout calculates deadline and calls DoDeadline on the least loaded client.

#### func (*LBClient) RemoveClients ¶ added in v1.35.0

```
func (cc *LBClient) RemoveClients(rc func(BalancingClient) bool) int
```

RemoveClients removes clients using the provided callback. If rc returns true, the passed client will be removed. Returns the new total number of clients.

#### type Logger

```
type Logger interface {
	
	Printf(format string, args ...any)
}
```

Logger is used for logging formatted messages.

#### type PathRewriteFunc

```
type PathRewriteFunc func(ctx *RequestCtx) []byte
```

PathRewriteFunc must return new request path based on arbitrary ctx info such as ctx.Path().

Path rewriter is used in FS for translating the current request to the local filesystem path relative to FS.Root.

The returned path must not contain '..' path segments due to security reasons, since such paths may refer files outside FS.Root.

The returned path may refer to ctx members. For example, ctx.Path().

#### func NewPathPrefixStripper

```
func NewPathPrefixStripper(prefixSize int) PathRewriteFunc
```

NewPathPrefixStripper returns path rewriter, which removes prefixSize bytes from the path prefix.

Examples:

- prefixSize = 0, original path: "/foo/bar", result: "/foo/bar"
- prefixSize = 3, original path: "/foo/bar", result: "o/bar"
- prefixSize = 7, original path: "/foo/bar", result: "r"

The returned path rewriter may be used as FS.PathRewrite .

#### func NewPathSlashesStripper

```
func NewPathSlashesStripper(slashesCount int) PathRewriteFunc
```

NewPathSlashesStripper returns path rewriter, which strips slashesCount leading slashes from the path.

Examples:

- slashesCount = 0, original path: "/foo/bar", result: "/foo/bar"
- slashesCount = 1, original path: "/foo/bar", result: "/bar"
- slashesCount = 2, original path: "/foo/bar", result: ""

The returned path rewriter may be used as FS.PathRewrite .

#### func NewVHostPathRewriter

```
func NewVHostPathRewriter(slashesCount int) PathRewriteFunc
```

NewVHostPathRewriter returns path rewriter, which strips slashesCount leading slashes from the path and prepends the path with request's host, thus simplifying virtual hosting for static files.

Examples:

- host=foobar.com, slashesCount=0, original path="/foo/bar". Resulting path: "/foobar.com/foo/bar"
- host=img.aaa.com, slashesCount=1, original path="/images/123/456.jpg" Resulting path: "/img.aaa.com/123/456.jpg"

#### type PipelineClient

```
type PipelineClient struct {

	
	
	
	Logger Logger

	
	
	
	Dial DialFunc

	
	TLSConfig *tls.Config

	
	Addr string

	
	Name string

	
	
	
	MaxConns int

	
	
	
	
	MaxPendingRequests int

	
	
	
	
	MaxBatchDelay time.Duration

	
	
	
	
	MaxIdleConnDuration time.Duration

	
	
	
	
	ReadBufferSize int

	
	
	
	WriteBufferSize int

	
	
	
	ReadTimeout time.Duration

	
	
	
	WriteTimeout time.Duration

	
	
	NoDefaultUserAgentHeader bool

	
	
	
	
	
	
	
	
	DialDualStack bool

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	DisableHeaderNamesNormalizing bool

	
	
	
	
	
	
	
	DisablePathNormalizing bool

	
	IsTLS bool
	
}
```

PipelineClient pipelines requests over a limited set of concurrent connections to the given Addr.

This client may be used in highly loaded HTTP-based RPC systems for reducing context switches and network level overhead. See https://en.wikipedia.org/wiki/HTTP_pipelining for details.

It is forbidden copying PipelineClient instances. Create new instances instead.

It is safe calling PipelineClient methods from concurrently running goroutines.

#### func (*PipelineClient) Do

```
func (c *PipelineClient) Do(req *Request, resp *Response) error
```

Do performs the given http request and sets the corresponding response.

Request must contain at least non-zero RequestURI with full url (including scheme and host) or non-zero Host header + RequestURI.

The function doesn't follow redirects. Use Get* for following redirects.

Response is ignored if resp is nil.

It is recommended obtaining req and resp via AcquireRequest and AcquireResponse in performance-critical code.

#### func (*PipelineClient) DoDeadline

```
func (c *PipelineClient) DoDeadline(req *Request, resp *Response, deadline time.Time) error
```

DoDeadline performs the given request and waits for response until the given deadline.

Request must contain at least non-zero RequestURI with full url (including scheme and host) or non-zero Host header + RequestURI.

The function doesn't follow redirects.

Response is ignored if resp is nil.

ErrTimeout is returned if the response wasn't returned until the given deadline.

It is recommended obtaining req and resp via AcquireRequest and AcquireResponse in performance-critical code.

#### func (*PipelineClient) DoTimeout

```
func (c *PipelineClient) DoTimeout(req *Request, resp *Response, timeout time.Duration) error
```

DoTimeout performs the given request and waits for response during the given timeout duration.

Request must contain at least non-zero RequestURI with full url (including scheme and host) or non-zero Host header + RequestURI.

The function doesn't follow redirects.

Response is ignored if resp is nil.

ErrTimeout is returned if the response wasn't returned during the given timeout.

It is recommended obtaining req and resp via AcquireRequest and AcquireResponse in performance-critical code.

#### func (*PipelineClient) PendingRequests

```
func (c *PipelineClient) PendingRequests() int
```

PendingRequests returns the current number of pending requests pipelined to the server.

This number may exceed MaxPendingRequests*MaxConns by up to two times, since each connection to the server may keep up to MaxPendingRequests requests in the queue before sending them to the server.

This function may be used for balancing load among multiple PipelineClient instances.

#### type ReadCloserWithError ¶ added in v1.53.0

```
type ReadCloserWithError interface {
	io.Reader
	CloseWithError(err error) error
}
```

#### type Request

```
type Request struct {

	
	
	
	Header RequestHeader

	
	UseHostHeader bool

	
	
	
	
	DisableRedirectPathNormalizing bool
	
}
```

Request represents HTTP request.

It is forbidden copying Request instances. Create new instances and use CopyTo instead.

Request instance MUST NOT be used from concurrently running goroutines.

#### func AcquireRequest

```
func AcquireRequest() *Request
```

AcquireRequest returns an empty Request instance from request pool.

The returned Request instance may be passed to ReleaseRequest when it is no longer needed. This allows Request recycling, reduces GC pressure and usually improves performance.

#### func (*Request) AppendBody

```
func (req *Request) AppendBody(p []byte)
```

AppendBody appends p to request body.

It is safe re-using p after the function returns.

#### func (*Request) AppendBodyString

```
func (req *Request) AppendBodyString(s string)
```

AppendBodyString appends s to request body.

#### func (*Request) Body

```
func (req *Request) Body() []byte
```

Body returns request body.

The returned value is valid until the request is released, either though ReleaseRequest or your request handler returning. Do not store references to returned value. Make copies instead.

#### func (*Request) BodyGunzip

```
func (req *Request) BodyGunzip() ([]byte, error)
```

BodyGunzip returns un-gzipped body data.

This method may be used if the request header contains 'Content-Encoding: gzip' for reading un-gzipped body. Use Body for reading gzipped request body.

#### func (*Request) BodyGunzipWithLimit ¶ added in v1.70.0

```
func (req *Request) BodyGunzipWithLimit(maxBodySize int) ([]byte, error)
```

BodyGunzipWithLimit returns un-gzipped body data and limits the size of uncompressed body data to maxBodySize bytes.

If maxBodySize <= 0, then no limit is applied.

#### func (*Request) BodyInflate

```
func (req *Request) BodyInflate() ([]byte, error)
```

BodyInflate returns inflated body data.

This method may be used if the response header contains 'Content-Encoding: deflate' for reading inflated request body. Use Body for reading deflated request body.

#### func (*Request) BodyInflateWithLimit ¶ added in v1.70.0

```
func (req *Request) BodyInflateWithLimit(maxBodySize int) ([]byte, error)
```

BodyInflateWithLimit returns inflated body data and limits the size of uncompressed body data to maxBodySize bytes.

If maxBodySize <= 0, then no limit is applied.

#### func (*Request) BodyStream ¶ added in v1.46.0

```
func (req *Request) BodyStream() io.Reader
```

BodyStream returns io.Reader.

You must CloseBodyStream or ReleaseRequest after you use it.

#### func (*Request) BodyUnbrotli ¶ added in v1.13.0

```
func (req *Request) BodyUnbrotli() ([]byte, error)
```

BodyUnbrotli returns un-brotlied body data.

This method may be used if the request header contains 'Content-Encoding: br' for reading un-brotlied body. Use Body for reading brotlied request body.

#### func (*Request) BodyUnbrotliWithLimit ¶ added in v1.70.0

```
func (req *Request) BodyUnbrotliWithLimit(maxBodySize int) ([]byte, error)
```

BodyUnbrotliWithLimit returns un-brotlied body data and limits the size of uncompressed body data to maxBodySize bytes.

If maxBodySize <= 0, then no limit is applied.

#### func (*Request) BodyUncompressed ¶ added in v1.38.0

```
func (req *Request) BodyUncompressed() ([]byte, error)
```

BodyUncompressed returns body data and if needed decompresses it from gzip, deflate, brotli or zstd.

This method may be used if the response header contains 'Content-Encoding' for reading uncompressed request body. Use Body for reading the raw request body.

#### func (*Request) BodyUncompressedWithLimit ¶ added in v1.70.0

```
func (req *Request) BodyUncompressedWithLimit(maxBodySize int) ([]byte, error)
```

BodyUncompressedWithLimit returns body data and if needed decompresses it from gzip, deflate, brotli or zstd. The size of uncompressed data is limited to maxBodySize bytes.

If maxBodySize <= 0, then no limit is applied.

#### func (*Request) BodyUnzstd ¶ added in v1.53.0

```
func (req *Request) BodyUnzstd() ([]byte, error)
```

#### func (*Request) BodyUnzstdWithLimit ¶ added in v1.70.0

```
func (req *Request) BodyUnzstdWithLimit(maxBodySize int) ([]byte, error)
```

BodyUnzstdWithLimit returns un-zstd body data and limits the size of uncompressed body data to maxBodySize bytes.

If maxBodySize <= 0, then no limit is applied.

#### func (*Request) BodyWriteTo

```
func (req *Request) BodyWriteTo(w io.Writer) error
```

BodyWriteTo writes request body to w.

#### func (*Request) BodyWriter

```
func (req *Request) BodyWriter() io.Writer
```

BodyWriter returns writer for populating request body.

#### func (*Request) CloseBodyStream ¶ added in v1.46.0

```
func (req *Request) CloseBodyStream() error
```

#### func (*Request) ConnectionClose

```
func (req *Request) ConnectionClose() bool
```

ConnectionClose returns true if 'Connection: close' header is set.

#### func (*Request) ContinueReadBody

```
func (req *Request) ContinueReadBody(r *bufio.Reader, maxBodySize int, preParseMultipartForm ...bool) error
```

ContinueReadBody reads request body if request header contains 'Expect: 100-continue'.

The caller must send StatusContinue response before calling this method.

If maxBodySize > 0 and the body size exceeds maxBodySize, then ErrBodyTooLarge is returned.

#### func (*Request) ContinueReadBodyStream ¶ added in v1.20.0

```
func (req *Request) ContinueReadBodyStream(r *bufio.Reader, maxBodySize int, preParseMultipartForm ...bool) error
```

ContinueReadBodyStream reads request body if request header contains 'Expect: 100-continue'.

The caller must send StatusContinue response before calling this method.

If maxBodySize > 0 and the body size exceeds maxBodySize, then ErrBodyTooLarge is returned.

#### func (*Request) CopyTo

```
func (req *Request) CopyTo(dst *Request)
```

CopyTo copies req contents to dst except of body stream.

#### func (*Request) GetTimeOut ¶ added in v1.57.0

```
func (req *Request) GetTimeOut() time.Duration
```

GetTimeOut retrieves the timeout duration set for the Request.

This method returns a time.Duration that determines how long the request can wait before it times out. In the default use case, the timeout applies to the entire request lifecycle, including both receiving the response headers and the response body.

#### func (*Request) Host

```
func (req *Request) Host() []byte
```

Host returns the host for the given request.

#### func (*Request) IsBodyStream

```
func (req *Request) IsBodyStream() bool
```

IsBodyStream returns true if body is set via SetBodyStream*.

#### func (*Request) MayContinue

```
func (req *Request) MayContinue() bool
```

MayContinue returns true if the request contains 'Expect: 100-continue' header.

The caller must do one of the following actions if MayContinue returns true:

- Either send StatusExpectationFailed response if request headers don't satisfy the caller.
- Or send StatusContinue response before reading request body with ContinueReadBody.
- Or close the connection.

#### func (*Request) MultipartForm

```
func (req *Request) MultipartForm() (*multipart.Form, error)
```

MultipartForm returns request's multipart form.

Returns ErrNoMultipartForm if request's Content-Type isn't 'multipart/form-data'.

This method is equivalent to MultipartFormWithLimit(0), i.e. no body size limit is applied during multipart parsing.

RemoveMultipartFormFiles must be called after returned multipart form is processed.

#### func (*Request) MultipartFormWithLimit ¶ added in v1.70.0

```
func (req *Request) MultipartFormWithLimit(maxBodySize int) (*multipart.Form, error)
```

MultipartFormWithLimit returns request's multipart form and limits the read multipart body size to maxBodySize bytes.

If maxBodySize <= 0, then no limit is applied.

Returns ErrNoMultipartForm if request's Content-Type isn't 'multipart/form-data'.

RemoveMultipartFormFiles must be called after returned multipart form is processed.

#### func (*Request) PostArgs

```
func (req *Request) PostArgs() *Args
```

PostArgs returns POST arguments.

#### func (*Request) Read

```
func (req *Request) Read(r *bufio.Reader) error
```

Read reads request (including body) from the given r.

RemoveMultipartFormFiles or Reset must be called after reading multipart/form-data request in order to delete temporarily uploaded files.

If MayContinue returns true, the caller must:

- Either send StatusExpectationFailed response if request headers don't satisfy the caller.
- Or send StatusContinue response before reading request body with ContinueReadBody.
- Or close the connection.

io.EOF is returned if r is closed before reading the first header byte.

#### func (*Request) ReadBody ¶ added in v1.32.0

```
func (req *Request) ReadBody(r *bufio.Reader, contentLength, maxBodySize int) (err error)
```

ReadBody reads request body from the given r, limiting the body size.

If maxBodySize > 0 and the body size exceeds maxBodySize, then ErrBodyTooLarge is returned.

#### func (*Request) ReadLimitBody

```
func (req *Request) ReadLimitBody(r *bufio.Reader, maxBodySize int) error
```

ReadLimitBody reads request from the given r, limiting the body size.

If maxBodySize > 0 and the body size exceeds maxBodySize, then ErrBodyTooLarge is returned.

RemoveMultipartFormFiles or Reset must be called after reading multipart/form-data request in order to delete temporarily uploaded files.

If MayContinue returns true, the caller must:

- Either send StatusExpectationFailed response if request headers don't satisfy the caller.
- Or send StatusContinue response before reading request body with ContinueReadBody.
- Or close the connection.

io.EOF is returned if r is closed before reading the first header byte.

#### func (*Request) ReleaseBody

```
func (req *Request) ReleaseBody(size int)
```

ReleaseBody retires the request body if it is greater than "size" bytes.

This permits GC to reclaim the large buffer. If used, must be before ReleaseRequest.

Use this method only if you really understand how it works. The majority of workloads don't need this method.

#### func (*Request) RemoveMultipartFormFiles

```
func (req *Request) RemoveMultipartFormFiles()
```

RemoveMultipartFormFiles removes multipart/form-data temporary files associated with the request.

#### func (*Request) RemoveUserValue ¶ added in v1.62.0

```
func (req *Request) RemoveUserValue(key any)
```

RemoveUserValue removes the given key and the value under it in Request.

#### func (*Request) RemoveUserValueBytes ¶ added in v1.62.0

```
func (req *Request) RemoveUserValueBytes(key []byte)
```

RemoveUserValueBytes removes the given key and the value under it in Request.

#### func (*Request) RequestURI

```
func (req *Request) RequestURI() []byte
```

RequestURI returns request's URI.

#### func (*Request) Reset

```
func (req *Request) Reset()
```

Reset clears request contents.

#### func (*Request) ResetBody

```
func (req *Request) ResetBody()
```

ResetBody resets request body.

#### func (*Request) ResetUserValues ¶ added in v1.62.0

```
func (req *Request) ResetUserValues()
```

ResetUserValues allows to reset user values from Request Context.

#### func (*Request) SetBody

```
func (req *Request) SetBody(body []byte)
```

SetBody sets request body.

It is safe re-using body argument after the function returns.

#### func (*Request) SetBodyRaw ¶ added in v1.17.0

```
func (req *Request) SetBodyRaw(body []byte)
```

SetBodyRaw sets response body, but without copying it.

From this point onward the body argument must not be changed.

#### func (*Request) SetBodyStream

```
func (req *Request) SetBodyStream(bodyStream io.Reader, bodySize int)
```

SetBodyStream sets request body stream and, optionally body size.

If bodySize is >= 0, then the bodyStream must provide exactly bodySize bytes before returning io.EOF.

If bodySize < 0, then bodyStream is read until io.EOF.

bodyStream.Close() is called after finishing reading all body data if it implements io.Closer.

Note that GET and HEAD requests cannot have body.

See also SetBodyStreamWriter.

#### func (*Request) SetBodyStreamWriter

```
func (req *Request) SetBodyStreamWriter(sw StreamWriter)
```

SetBodyStreamWriter registers the given sw for populating request body.

This function may be used in the following cases:

- if request body is too big (more than 10MB).
- if request body is streamed from slow external sources.
- if request body must be streamed to the server in chunks (aka `http client push` or `chunked transfer-encoding`).

Note that GET and HEAD requests cannot have body.

See also SetBodyStream.

#### func (*Request) SetBodyString

```
func (req *Request) SetBodyString(body string)
```

SetBodyString sets request body.

#### func (*Request) SetConnectionClose

```
func (req *Request) SetConnectionClose()
```

SetConnectionClose sets 'Connection: close' header.

#### func (*Request) SetHost

```
func (req *Request) SetHost(host string)
```

SetHost sets host for the request.

#### func (*Request) SetHostBytes

```
func (req *Request) SetHostBytes(host []byte)
```

SetHostBytes sets host for the request.

#### func (*Request) SetRequestURI

```
func (req *Request) SetRequestURI(requestURI string)
```

SetRequestURI sets RequestURI.

#### func (*Request) SetRequestURIBytes

```
func (req *Request) SetRequestURIBytes(requestURI []byte)
```

SetRequestURIBytes sets RequestURI.

#### func (*Request) SetTimeout ¶ added in v1.42.0

```
func (req *Request) SetTimeout(t time.Duration)
```

SetTimeout sets timeout for the request.

The following code:

```
req.SetTimeout(t)
c.Do(&req, &resp)
```

is equivalent to

```
c.DoTimeout(&req, &resp, t)
```

#### func (*Request) SetURI ¶ added in v1.32.0

```
func (req *Request) SetURI(newURI *URI)
```

SetURI initializes request URI. Use this method if a single URI may be reused across multiple requests. Otherwise, you can just use SetRequestURI() and it will be parsed as new URI. The URI is copied and can be safely modified later.

#### func (*Request) SetUserValue ¶ added in v1.62.0

```
func (req *Request) SetUserValue(key, value any)
```

SetUserValue stores the given value (arbitrary object) under the given key in Request.

The value stored in Request may be obtained by UserValue*.

This functionality may be useful for passing arbitrary values between functions involved in request processing.

All the values are removed from Request after returning from the top RequestHandler. Additionally, Close method is called on each value implementing io.Closer before removing the value from Request.

#### func (*Request) SetUserValueBytes ¶ added in v1.62.0

```
func (req *Request) SetUserValueBytes(key []byte, value any)
```

SetUserValueBytes stores the given value (arbitrary object) under the given key in Request.

The value stored in Request may be obtained by UserValue*.

This functionality may be useful for passing arbitrary values between functions involved in request processing.

All the values stored in Request are deleted after returning from RequestHandler.

#### func (*Request) String

```
func (req *Request) String() string
```

String returns request representation.

Returns error message instead of request representation on error.

Use Write instead of String for performance-critical code.

#### func (*Request) SwapBody

```
func (req *Request) SwapBody(body []byte) []byte
```

SwapBody swaps request body with the given body and returns the previous request body.

It is forbidden to use the body passed to SwapBody after the function returns.

#### func (*Request) URI

```
func (req *Request) URI() *URI
```

URI returns request URI.

#### func (*Request) UserValue ¶ added in v1.62.0

```
func (req *Request) UserValue(key any) any
```

UserValue returns the value stored via SetUserValue* under the given key.

#### func (*Request) UserValueBytes ¶ added in v1.62.0

```
func (req *Request) UserValueBytes(key []byte) any
```

UserValueBytes returns the value stored via SetUserValue* under the given key.

#### func (*Request) VisitUserValues ¶ added in v1.62.0

```
func (req *Request) VisitUserValues(visitor func([]byte, any))
```

VisitUserValues calls visitor for each existing userValue with a key that is a string or []byte.

visitor must not retain references to key and value after returning. Make key and/or value copies if you need storing them after returning.

#### func (*Request) VisitUserValuesAll ¶ added in v1.62.0

```
func (req *Request) VisitUserValuesAll(visitor func(any, any))
```

VisitUserValuesAll calls visitor for each existing userValue.

visitor must not retain references to key and value after returning. Make key and/or value copies if you need storing them after returning.

#### func (*Request) Write

```
func (req *Request) Write(w *bufio.Writer) error
```

Write writes request to w.

Write doesn't flush request to w for performance reasons.

See also WriteTo.

#### func (*Request) WriteTo

```
func (req *Request) WriteTo(w io.Writer) (int64, error)
```

WriteTo writes request to w. It implements io.WriterTo.

#### type RequestConfig ¶ added in v1.5.0

```
type RequestConfig struct {
	
	
	
	ReadTimeout time.Duration
	
	
	
	WriteTimeout time.Duration
	
	
	MaxRequestBodySize int
}
```

RequestConfig configure the per request deadline and body limits.

#### type RequestCtx

```
type RequestCtx struct {

	
	
	
	Response Response

	
	
	
	Request Request
	
}
```

RequestCtx contains incoming request and manages outgoing response.

It is forbidden copying RequestCtx instances.

RequestHandler should avoid holding references to incoming RequestCtx and/or its members after the return. If holding RequestCtx references after the return is unavoidable (for instance, ctx is passed to a separate goroutine and ctx lifetime cannot be controlled), then the RequestHandler MUST call ctx.TimeoutError() before return.

It is unsafe modifying/reading RequestCtx instance from concurrently running goroutines. The only exception is TimeoutError*, which may be called while other goroutines accessing RequestCtx.

#### func (*RequestCtx) Conn ¶ added in v1.1.0

```
func (ctx *RequestCtx) Conn() net.Conn
```

Conn returns a reference to the underlying net.Conn.

WARNING: Only use this method if you know what you are doing!

Reading from or writing to the returned connection will end badly!

#### func (*RequestCtx) ConnID

```
func (ctx *RequestCtx) ConnID() uint64
```

ConnID returns unique connection ID.

This ID may be used to match distinct requests to the same incoming connection.

#### func (*RequestCtx) ConnRequestNum

```
func (ctx *RequestCtx) ConnRequestNum() uint64
```

ConnRequestNum returns request sequence number for the current connection.

Sequence starts with 1.

#### func (*RequestCtx) ConnTime

```
func (ctx *RequestCtx) ConnTime() time.Time
```

ConnTime returns the time the server started serving the connection the current request came from.

#### func (*RequestCtx) Deadline ¶ added in v1.1.0

```
func (ctx *RequestCtx) Deadline() (deadline time.Time, ok bool)
```

Deadline returns the time when work done on behalf of this context should be canceled. Deadline returns ok==false when no deadline is set. Successive calls to Deadline return the same results.

This method always returns 0, false and is only present to make RequestCtx implement the context interface.

#### func (*RequestCtx) Done ¶ added in v1.1.0

```
func (ctx *RequestCtx) Done() <-chan struct{}
```

Done returns a channel that's closed when work done on behalf of this context should be canceled. Done may return nil if this context can never be canceled. Successive calls to Done return the same value.

Note: Because creating a new channel for every request is just too expensive, so RequestCtx.s.done is only closed when the server is shutting down.

#### func (*RequestCtx) EarlyHints ¶ added in v1.61.0

```
func (ctx *RequestCtx) EarlyHints() error
```

EarlyHints allows the server to hint to the browser what resources a page would need so the browser can preload them while waiting for the server's full response. Only Link headers already written to the response will be transmitted as Early Hints.

This is a HTTP/2+ feature but all browsers will either understand it or safely ignore it.

NOTE: Older HTTP/1.1 non-browser clients may face compatibility issues.

See: https://developer.chrome.com/docs/web-platform/early-hints and https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Link#syntax

Example:

```
func(ctx *fasthttp.RequestCtx) {
   ctx.Response.Header.Add("Link", "<https://fonts.google.com>; rel=preconnect")
   ctx.EarlyHints()
   time.Sleep(5*time.Second) // some time-consuming task
   ctx.SetStatusCode(fasthttp.StatusOK)
   ctx.SetBody([]byte("<html><head></head><body><h1>Hello from Fasthttp</h1></body></html>"))
}
```

#### func (*RequestCtx) Err ¶ added in v1.1.0

```
func (ctx *RequestCtx) Err() error
```

Err returns a non-nil error value after Done is closed, successive calls to Err return the same error. If Done is not yet closed, Err returns nil. If Done is closed, Err returns a non-nil error explaining why: Canceled if the context was canceled (via server Shutdown) or DeadlineExceeded if the context's deadline passed.

Note: Because creating a new channel for every request is just too expensive, so RequestCtx.s.done is only closed when the server is shutting down.

#### func (*RequestCtx) Error

```
func (ctx *RequestCtx) Error(msg string, statusCode int)
```

Error sets response status code to the given value and sets response body to the given message.

Warning: this will reset the response headers and body already set!

#### func (*RequestCtx) FormFile

```
func (ctx *RequestCtx) FormFile(key string) (*multipart.FileHeader, error)
```

FormFile returns uploaded file associated with the given multipart form key.

The file is automatically deleted after returning from RequestHandler, so either move or copy uploaded file into new place if you want retaining it.

Use SaveMultipartFile function for permanently saving uploaded file.

The returned file header is valid until your request handler returns.

For multipart requests with untrusted input, call MultipartFormWithLimit() before FormFile.

#### func (*RequestCtx) FormValue

```
func (ctx *RequestCtx) FormValue(key string) []byte
```

FormValue returns form value associated with the given key.

The value is searched in the following places:

- Query string.
- POST or PUT body.

There are more fine-grained methods for obtaining form values:

- QueryArgs for obtaining values from query string.
- PostArgs for obtaining values from POST or PUT body.
- MultipartForm for obtaining values from multipart form.
- FormFile for obtaining uploaded files.

The returned value is valid until your request handler returns.

For multipart requests with untrusted input, either call MultipartFormWithLimit() before FormValue or provide a custom Server.FormValueFunc that uses MultipartFormWithLimit().

#### func (*RequestCtx) Hijack

```
func (ctx *RequestCtx) Hijack(handler HijackHandler)
```

Hijack registers the given handler for connection hijacking.

The handler is called after returning from RequestHandler and sending http response. The current connection is passed to the handler. The connection is automatically closed after returning from the handler.

The server skips calling the handler in the following cases:

- 'Connection: close' header exists in either request or response.
- Unexpected error during response writing to the connection.

The server stops processing requests from hijacked connections.

Server limits such as Concurrency, ReadTimeout, WriteTimeout, etc. aren't applied to hijacked connections.

The handler must not retain references to ctx members.

Arbitrary 'Connection: Upgrade' protocols may be implemented with HijackHandler. For instance,

- WebSocket ( https://en.wikipedia.org/wiki/WebSocket )
- HTTP/2.0 ( https://en.wikipedia.org/wiki/HTTP/2 )

Example

¶

```
package main

import (
	"fmt"
	"log"
	"net"

	"github.com/valyala/fasthttp"
)

func main() {
	// hijackHandler is called on hijacked connection.
	hijackHandler := func(c net.Conn) {
		fmt.Fprintf(c, "This message is sent over a hijacked connection to the client %s\n", c.RemoteAddr())
		fmt.Fprintf(c, "Send me something and I'll echo it to you\n")
		var buf [1]byte
		for {
			if _, err := c.Read(buf[:]); err != nil {
				log.Printf("error when reading from hijacked connection: %v", err)
				return
			}
			fmt.Fprintf(c, "You sent me %q. Waiting for new data\n", buf[:])
		}
	}

	// requestHandler is called for each incoming request.
	requestHandler := func(ctx *fasthttp.RequestCtx) {
		path := ctx.Path()
		switch {
		case string(path) == "/hijack":
			// Note that the connection is hijacked only after
			// returning from requestHandler and sending http response.
			ctx.Hijack(hijackHandler)

			// The connection will be hijacked after sending this response.
			fmt.Fprintf(ctx, "Hijacked the connection!")
		case string(path) == "/":
			fmt.Fprintf(ctx, "Root directory requested")
		default:
			fmt.Fprintf(ctx, "Requested path is %q", path)
		}
	}

	if err := fasthttp.ListenAndServe(":80", requestHandler); err != nil {
		log.Fatalf("error in ListenAndServe: %v", err)
	}
}
```
