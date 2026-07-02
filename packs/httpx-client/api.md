---
title: "Developer Interface"
source: https://www.python-httpx.org/api/
domain: httpx-client
license: CC-BY-SA-4.0
tags: python httpx, async http client, httpx library
fetched: 2026-07-02
---

# Developer Interface

## Helper Functions

Note

Only use these functions if you're testing HTTPX in a console or making a small number of requests. Using a `Client` will enable HTTP/2 and connection pooling for more efficient and long-lived connections.

httpx.

request

(

method

,

url

,

*

,

params=None

,

content=None

,

data=None

,

files=None

,

json=None

,

headers=None

,

cookies=None

,

auth=None

,

proxy=None

,

timeout=Timeout(timeout=5.0)

,

follow_redirects=False

,

verify=True

,

trust_env=True

)

Sends an HTTP request.

**Parameters:**

- **method** - HTTP method for the new `Request` object: `GET`, `OPTIONS`, `HEAD`, `POST`, `PUT`, `PATCH`, or `DELETE`.
- **url** - URL for the new `Request` object.
- **params** - *(optional)* Query parameters to include in the URL, as a string, dictionary, or sequence of two-tuples.
- **content** - *(optional)* Binary content to include in the body of the request, as bytes or a byte iterator.
- **data** - *(optional)* Form data to include in the body of the request, as a dictionary.
- **files** - *(optional)* A dictionary of upload files to include in the body of the request.
- **json** - *(optional)* A JSON serializable object to include in the body of the request.
- **headers** - *(optional)* Dictionary of HTTP headers to include in the request.
- **cookies** - *(optional)* Dictionary of Cookie items to include in the request.
- **auth** - *(optional)* An authentication class to use when sending the request.
- **proxy** - *(optional)* A proxy URL where all the traffic should be routed.
- **timeout** - *(optional)* The timeout configuration to use when sending the request.
- **follow_redirects** - *(optional)* Enables or disables HTTP redirects.
- **verify** - *(optional)* Either `True` to use an SSL context with the default CA bundle, `False` to disable verification, or an instance of `ssl.SSLContext` to use a custom context.
- **trust_env** - *(optional)* Enables or disables usage of environment variables for configuration.

**Returns:** `Response`

Usage:

```
>>> import httpx
>>> response = httpx.request('GET', 'https://httpbin.org/get')
>>> response
<Response [200 OK]>
```

httpx.

get

(

url

,

*

,

params=None

,

headers=None

,

cookies=None

,

auth=None

,

proxy=None

,

follow_redirects=False

,

verify=True

,

timeout=Timeout(timeout=5.0)

,

trust_env=True

)

Sends a `GET` request.

**Parameters**: See `httpx.request`.

Note that the `data`, `files`, `json` and `content` parameters are not available on this function, as `GET` requests should not include a request body.

httpx.

options

(

url

,

*

,

params=None

,

headers=None

,

cookies=None

,

auth=None

,

proxy=None

,

follow_redirects=False

,

verify=True

,

timeout=Timeout(timeout=5.0)

,

trust_env=True

)

Sends an `OPTIONS` request.

**Parameters**: See `httpx.request`.

Note that the `data`, `files`, `json` and `content` parameters are not available on this function, as `OPTIONS` requests should not include a request body.

httpx.

head

(

url

,

*

,

params=None

,

headers=None

,

cookies=None

,

auth=None

,

proxy=None

,

follow_redirects=False

,

verify=True

,

timeout=Timeout(timeout=5.0)

,

trust_env=True

)

Sends a `HEAD` request.

**Parameters**: See `httpx.request`.

Note that the `data`, `files`, `json` and `content` parameters are not available on this function, as `HEAD` requests should not include a request body.

httpx.

post

(

url

,

*

,

content=None

,

data=None

,

files=None

,

json=None

,

params=None

,

headers=None

,

cookies=None

,

auth=None

,

proxy=None

,

follow_redirects=False

,

verify=True

,

timeout=Timeout(timeout=5.0)

,

trust_env=True

)

Sends a `POST` request.

**Parameters**: See `httpx.request`.

httpx.

put

(

url

,

*

,

content=None

,

data=None

,

files=None

,

json=None

,

params=None

,

headers=None

,

cookies=None

,

auth=None

,

proxy=None

,

follow_redirects=False

,

verify=True

,

timeout=Timeout(timeout=5.0)

,

trust_env=True

)

Sends a `PUT` request.

**Parameters**: See `httpx.request`.

httpx.

patch

(

url

,

*

,

content=None

,

data=None

,

files=None

,

json=None

,

params=None

,

headers=None

,

cookies=None

,

auth=None

,

proxy=None

,

follow_redirects=False

,

verify=True

,

timeout=Timeout(timeout=5.0)

,

trust_env=True

)

Sends a `PATCH` request.

**Parameters**: See `httpx.request`.

httpx.

delete

(

url

,

*

,

params=None

,

headers=None

,

cookies=None

,

auth=None

,

proxy=None

,

follow_redirects=False

,

timeout=Timeout(timeout=5.0)

,

verify=True

,

trust_env=True

)

Sends a `DELETE` request.

**Parameters**: See `httpx.request`.

Note that the `data`, `files`, `json` and `content` parameters are not available on this function, as `DELETE` requests should not include a request body.

httpx.

stream

(

method

,

url

,

*

,

params=None

,

content=None

,

data=None

,

files=None

,

json=None

,

headers=None

,

cookies=None

,

auth=None

,

proxy=None

,

timeout=Timeout(timeout=5.0)

,

follow_redirects=False

,

verify=True

,

trust_env=True

)

Alternative to `httpx.request()` that streams the response body instead of loading it into memory at once.

**Parameters**: See `httpx.request`.

See also: Streaming Responses

## `Client`

class

httpx.

Client

(

*

,

auth=None

,

params=None

,

headers=None

,

cookies=None

,

verify=True

,

cert=None

,

trust_env=True

,

http1=True

,

http2=False

,

proxy=None

,

mounts=None

,

timeout=Timeout(timeout=5.0)

,

follow_redirects=False

,

limits=Limits(max_connections=100, max_keepalive_connections=20, keepalive_expiry=5.0)

,

max_redirects=20

,

event_hooks=None

,

base_url=''

,

transport=None

,

default_encoding='utf-8'

)

An HTTP client, with connection pooling, HTTP/2, redirects, cookie persistence, etc.

It can be shared between threads.

Usage:

```
>>> client = httpx.Client()
>>> response = client.get('https://example.org')
```

**Parameters:**

- **auth** - *(optional)* An authentication class to use when sending requests.
- **params** - *(optional)* Query parameters to include in request URLs, as a string, dictionary, or sequence of two-tuples.
- **headers** - *(optional)* Dictionary of HTTP headers to include when sending requests.
- **cookies** - *(optional)* Dictionary of Cookie items to include when sending requests.
- **verify** - *(optional)* Either `True` to use an SSL context with the default CA bundle, `False` to disable verification, or an instance of `ssl.SSLContext` to use a custom context.
- **http2** - *(optional)* A boolean indicating if HTTP/2 support should be enabled. Defaults to `False`.
- **proxy** - *(optional)* A proxy URL where all the traffic should be routed.
- **timeout** - *(optional)* The timeout configuration to use when sending requests.
- **limits** - *(optional)* The limits configuration to use.
- **max_redirects** - *(optional)* The maximum number of redirect responses that should be followed.
- **base_url** - *(optional)* A URL to use as the base when building request URLs.
- **transport** - *(optional)* A transport class to use for sending requests over the network.
- **trust_env** - *(optional)* Enables or disables usage of environment variables for configuration.
- **default_encoding** - *(optional)* The default encoding to use for decoding response text, if no charset information is included in a response Content-Type header. Set to a callable for automatic character set detection. Default: "utf-8".

headers

HTTP headers to include when sending requests.

cookies

Cookie values to include when sending requests.

params

Query parameters to include in the URL when sending requests.

auth

Authentication class used when none is passed at the request-level.

See also Authentication.

request

(

self

,

method

,

url

,

*

,

content=None

,

data=None

,

files=None

,

json=None

,

params=None

,

headers=None

,

cookies=None

,

auth=

,

follow_redirects=

,

timeout=

,

extensions=None

)

Build and send a request.

Equivalent to:

```
request = client.build_request(...)
response = client.send(request, ...)
```

See `Client.build_request()`, `Client.send()` and Merging of configuration for how the various parameters are merged with client-level configuration.

get

(

self

,

url

,

*

,

params=None

,

headers=None

,

cookies=None

,

auth=

,

follow_redirects=

,

timeout=

,

extensions=None

)

Send a `GET` request.

**Parameters**: See `httpx.request`.

head

(

self

,

url

,

*

,

params=None

,

headers=None

,

cookies=None

,

auth=

,

follow_redirects=

,

timeout=

,

extensions=None

)

Send a `HEAD` request.

**Parameters**: See `httpx.request`.

options

(

self

,

url

,

*

,

params=None

,

headers=None

,

cookies=None

,

auth=

,

follow_redirects=

,

timeout=

,

extensions=None

)

Send an `OPTIONS` request.

**Parameters**: See `httpx.request`.

post

(

self

,

url

,

*

,

content=None

,

data=None

,

files=None

,

json=None

,

params=None

,

headers=None

,

cookies=None

,

auth=

,

follow_redirects=

,

timeout=

,

extensions=None

)

Send a `POST` request.

**Parameters**: See `httpx.request`.

put

(

self

,

url

,

*

,

content=None

,

data=None

,

files=None

,

json=None

,

params=None

,

headers=None

,

cookies=None

,

auth=

,

follow_redirects=

,

timeout=

,

extensions=None

)

Send a `PUT` request.

**Parameters**: See `httpx.request`.

patch

(

self

,

url

,

*

,

content=None

,

data=None

,

files=None

,

json=None

,

params=None

,

headers=None

,

cookies=None

,

auth=

,

follow_redirects=

,

timeout=

,

extensions=None

)

Send a `PATCH` request.

**Parameters**: See `httpx.request`.

delete

(

self

,

url

,

*

,

params=None

,

headers=None

,

cookies=None

,

auth=

,

follow_redirects=

,

timeout=

,

extensions=None

)

Send a `DELETE` request.

**Parameters**: See `httpx.request`.

stream

(

self

,

method

,

url

,

*

,

content=None

,

data=None

,

files=None

,

json=None

,

params=None

,

headers=None

,

cookies=None

,

auth=

,

follow_redirects=

,

timeout=

,

extensions=None

)

Alternative to `httpx.request()` that streams the response body instead of loading it into memory at once.

**Parameters**: See `httpx.request`.

See also: Streaming Responses

build_request

(

self

,

method

,

url

,

*

,

content=None

,

data=None

,

files=None

,

json=None

,

params=None

,

headers=None

,

cookies=None

,

timeout=

,

extensions=None

)

Build and return a request instance.

- The `params`, `headers` and `cookies` arguments are merged with any values set on the client.
- The `url` argument is merged with any `base_url` set on the client.

See also: Request instances

send

(

self

,

request

,

*

,

stream=False

,

auth=

,

follow_redirects=

)

Send a request.

The request is sent as-is, unmodified.

Typically you'll want to build one with `Client.build_request()` so that any client-level configuration is merged into the request, but passing an explicit `httpx.Request()` is supported as well.

See also: Request instances

close

(

self

)

Close transport and proxies.

## `AsyncClient`

class

httpx.

AsyncClient

(

*

,

auth=None

,

params=None

,

headers=None

,

cookies=None

,

verify=True

,

cert=None

,

http1=True

,

http2=False

,

proxy=None

,

mounts=None

,

timeout=Timeout(timeout=5.0)

,

follow_redirects=False

,

limits=Limits(max_connections=100, max_keepalive_connections=20, keepalive_expiry=5.0)

,

max_redirects=20

,

event_hooks=None

,

base_url=''

,

transport=None

,

trust_env=True

,

default_encoding='utf-8'

)

An asynchronous HTTP client, with connection pooling, HTTP/2, redirects, cookie persistence, etc.

It can be shared between tasks.

Usage:

```
>>> async with httpx.AsyncClient() as client:
>>>     response = await client.get('https://example.org')
```

**Parameters:**

- **auth** - *(optional)* An authentication class to use when sending requests.
- **params** - *(optional)* Query parameters to include in request URLs, as a string, dictionary, or sequence of two-tuples.
- **headers** - *(optional)* Dictionary of HTTP headers to include when sending requests.
- **cookies** - *(optional)* Dictionary of Cookie items to include when sending requests.
- **verify** - *(optional)* Either `True` to use an SSL context with the default CA bundle, `False` to disable verification, or an instance of `ssl.SSLContext` to use a custom context.
- **http2** - *(optional)* A boolean indicating if HTTP/2 support should be enabled. Defaults to `False`.
- **proxy** - *(optional)* A proxy URL where all the traffic should be routed.
- **timeout** - *(optional)* The timeout configuration to use when sending requests.
- **limits** - *(optional)* The limits configuration to use.
- **max_redirects** - *(optional)* The maximum number of redirect responses that should be followed.
- **base_url** - *(optional)* A URL to use as the base when building request URLs.
- **transport** - *(optional)* A transport class to use for sending requests over the network.
- **trust_env** - *(optional)* Enables or disables usage of environment variables for configuration.
- **default_encoding** - *(optional)* The default encoding to use for decoding response text, if no charset information is included in a response Content-Type header. Set to a callable for automatic character set detection. Default: "utf-8".

headers

HTTP headers to include when sending requests.

cookies

Cookie values to include when sending requests.

params

Query parameters to include in the URL when sending requests.

auth

Authentication class used when none is passed at the request-level.

See also Authentication.

async

request

(

self

,

method

,

url

,

*

,

content=None

,

data=None

,

files=None

,

json=None

,

params=None

,

headers=None

,

cookies=None

,

auth=

,

follow_redirects=

,

timeout=

,

extensions=None

)

Build and send a request.

Equivalent to:

```
request = client.build_request(...)
response = await client.send(request, ...)
```

See `AsyncClient.build_request()`, `AsyncClient.send()` and Merging of configuration for how the various parameters are merged with client-level configuration.

async

get

(

self

,

url

,

*

,

params=None

,

headers=None

,

cookies=None

,

auth=

,

follow_redirects=

,

timeout=

,

extensions=None

)

Send a `GET` request.

**Parameters**: See `httpx.request`.

async

head

(

self

,

url

,

*

,

params=None

,

headers=None

,

cookies=None

,

auth=

,

follow_redirects=

,

timeout=

,

extensions=None

)

Send a `HEAD` request.

**Parameters**: See `httpx.request`.

async

options

(

self

,

url

,

*

,

params=None

,

headers=None

,

cookies=None

,

auth=

,

follow_redirects=

,

timeout=

,

extensions=None

)

Send an `OPTIONS` request.

**Parameters**: See `httpx.request`.

async

post

(

self

,

url

,

*

,

content=None

,

data=None

,

files=None

,

json=None

,

params=None

,

headers=None

,

cookies=None

,

auth=

,

follow_redirects=

,

timeout=

,

extensions=None

)

Send a `POST` request.

**Parameters**: See `httpx.request`.

async

put

(

self

,

url

,

*

,

content=None

,

data=None

,

files=None

,

json=None

,

params=None

,

headers=None

,

cookies=None

,

auth=

,

follow_redirects=

,

timeout=

,

extensions=None

)

Send a `PUT` request.

**Parameters**: See `httpx.request`.

async

patch

(

self

,

url

,

*

,

content=None

,

data=None

,

files=None

,

json=None

,

params=None

,

headers=None

,

cookies=None

,

auth=

,

follow_redirects=

,

timeout=

,

extensions=None

)

Send a `PATCH` request.

**Parameters**: See `httpx.request`.

async

delete

(

self

,

url

,

*

,

params=None

,

headers=None

,

cookies=None

,

auth=

,

follow_redirects=

,

timeout=

,

extensions=None

)

Send a `DELETE` request.

**Parameters**: See `httpx.request`.

stream

(

self

,

method

,

url

,

*

,

content=None

,

data=None

,

files=None

,

json=None

,

params=None

,

headers=None

,

cookies=None

,

auth=

,

follow_redirects=

,

timeout=

,

extensions=None

)

Alternative to `httpx.request()` that streams the response body instead of loading it into memory at once.

**Parameters**: See `httpx.request`.

See also: Streaming Responses

build_request

(

self

,

method

,

url

,

*

,

content=None

,

data=None

,

files=None

,

json=None

,

params=None

,

headers=None

,

cookies=None

,

timeout=

,

extensions=None

)

Build and return a request instance.

- The `params`, `headers` and `cookies` arguments are merged with any values set on the client.
- The `url` argument is merged with any `base_url` set on the client.

See also: Request instances

async

send

(

self

,

request

,

*

,

stream=False

,

auth=

,

follow_redirects=

)

Send a request.

The request is sent as-is, unmodified.

Typically you'll want to build one with `AsyncClient.build_request()` so that any client-level configuration is merged into the request, but passing an explicit `httpx.Request()` is supported as well.

See also: Request instances

async

aclose

(

self

)

Close transport and proxies.

## `Response`

*An HTTP response.*

- `def __init__(...)`
- `.status_code` - **int**
- `.reason_phrase` - **str**
- `.http_version` - `"HTTP/2"` or `"HTTP/1.1"`
- `.url` - **URL**
- `.headers` - **Headers**
- `.content` - **bytes**
- `.text` - **str**
- `.encoding` - **str**
- `.is_redirect` - **bool**
- `.request` - **Request**
- `.next_request` - **Optional[Request]**
- `.cookies` - **Cookies**
- `.history` - **List[Response]**
- `.elapsed` - **timedelta**
- The amount of time elapsed between sending the request and calling `close()` on the corresponding response received for that request. total_seconds() to correctly get the total elapsed seconds.
- `def .raise_for_status()` - **Response**
- `def .json()` - **Any**
- `def .read()` - **bytes**
- `def .iter_raw([chunk_size])` - **bytes iterator**
- `def .iter_bytes([chunk_size])` - **bytes iterator**
- `def .iter_text([chunk_size])` - **text iterator**
- `def .iter_lines()` - **text iterator**
- `def .close()` - **None**
- `def .next()` - **Response**
- `def .aread()` - **bytes**
- `def .aiter_raw([chunk_size])` - **async bytes iterator**
- `def .aiter_bytes([chunk_size])` - **async bytes iterator**
- `def .aiter_text([chunk_size])` - **async text iterator**
- `def .aiter_lines()` - **async text iterator**
- `def .aclose()` - **None**
- `def .anext()` - **Response**

## `Request`

*An HTTP request. Can be constructed explicitly for more control over exactly what gets sent over the wire.*

```
>>> request = httpx.Request("GET", "https://example.org", headers={'host': 'example.org'})
>>> response = client.send(request)
```

- `def __init__(method, url, [params], [headers], [cookies], [content], [data], [files], [json], [stream])`
- `.method` - **str**
- `.url` - **URL**
- `.content` - **byte**, **byte iterator**, or **byte async iterator**
- `.headers` - **Headers**
- `.cookies` - **Cookies**

## `URL`

*A normalized, IDNA supporting URL.*

```
>>> url = URL("https://example.org/")
>>> url.host
'example.org'
```

- `def __init__(url, **kwargs)`
- `.scheme` - **str**
- `.authority` - **str**
- `.host` - **str**
- `.port` - **int**
- `.path` - **str**
- `.query` - **str**
- `.raw_path` - **str**
- `.fragment` - **str**
- `.is_ssl` - **bool**
- `.is_absolute_url` - **bool**
- `.is_relative_url` - **bool**
- `def .copy_with([scheme], [authority], [path], [query], [fragment])` - **URL**

## `Headers`

*A case-insensitive multi-dict.*

```
>>> headers = Headers({'Content-Type': 'application/json'})
>>> headers['content-type']
'application/json'
```

- `def __init__(self, headers, encoding=None)`
- `def copy()` - **Headers**

## `Cookies`

*A dict-like cookie store.*

```
>>> cookies = Cookies()
>>> cookies.set("name", "value", domain="example.org")
```

- `def __init__(cookies: [dict, Cookies, CookieJar])`
- `.jar` - **CookieJar**
- `def extract_cookies(response)`
- `def set_cookie_header(request)`
- `def set(name, value, [domain], [path])`
- `def get(name, [domain], [path])`
- `def delete(name, [domain], [path])`
- `def clear([domain], [path])`
- *Standard mutable mapping interface*

## `Proxy`

*A configuration of the proxy server.*

```
>>> proxy = Proxy("http://proxy.example.com:8030")
>>> client = Client(proxy=proxy)
```

- `def __init__(url, [ssl_context], [auth], [headers])`
- `.url` - **URL**
- `.auth` - **tuple[str, str]**
- `.headers` - **Headers**
- `.ssl_context` - **SSLContext**
