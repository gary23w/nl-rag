---
title: "GitHub (part 2/2)"
source: https://github.com/axios/axios
domain: axios-http
license: CC-BY-SA-4.0
tags: axios http, promise http client, javascript ajax, request interceptor
fetched: 2026-07-02
part: 2/2
---

## Cancellation

### AbortController

Since `v0.22.0`, Axios supports AbortController:

```highlight
const controller = new AbortController();

axios
  .get('/foo/bar', {
    signal: controller.signal,
  })
  .then(function (response) {
    //...
  });
// cancel the request
controller.abort();
```

### CancelToken (deprecated)

You can also cancel a request using a *CancelToken*.

> The axios cancel token API is based on the withdrawn cancellable promises proposal.

> This API is deprecated since v0.22.0 and should not be used in new projects.

Create a cancel token with the `CancelToken.source` factory:

```highlight
const CancelToken = axios.CancelToken;
const source = CancelToken.source();

axios
  .get('/user/12345', {
    cancelToken: source.token,
  })
  .catch(function (thrown) {
    if (axios.isCancel(thrown)) {
      console.log('Request canceled', thrown.message);
    } else {
      // handle error
    }
  });

axios.post(
  '/user/12345',
  {
    name: 'new name',
  },
  {
    cancelToken: source.token,
  }
);

// cancel the request (the message parameter is optional)
source.cancel('Operation canceled by the user.');
```

You can also pass an executor function to the `CancelToken` constructor:

```highlight
const CancelToken = axios.CancelToken;
let cancel;

axios.get('/user/12345', {
  cancelToken: new CancelToken(function executor(c) {
    // An executor function receives a cancel function as a parameter
    cancel = c;
  }),
});

// cancel the request
cancel();
```

`CancelToken` also exposes low-level helpers for legacy integrations:

```highlight
const source = axios.CancelToken.source();

const listener = (cancel) => {
  console.log(cancel.message);
};

source.token.subscribe(listener);

const signal = source.token.toAbortSignal();
// Pass `signal` to APIs that accept AbortSignal.

source.cancel('Operation canceled by the user.');
source.token.unsubscribe(listener);
```

Canceled requests reject with `axios.CanceledError`. The legacy `axios.Cancel` export is an alias of `axios.CanceledError`, and cancellation errors include `__CANCEL__` for `axios.isCancel` compatibility.

> Note: You can cancel several requests with the same cancel token or abort controller. If a cancellation token is already cancelled when an Axios request starts, Axios cancels the request immediately without making a real request.

> During the transition period, you can use both cancellation APIs, even for the same request:

```highlight
const controller = new AbortController();
const source = axios.CancelToken.source();

axios.get('/user/12345', {
  cancelToken: source.token,
  signal: controller.signal,
});

controller.abort();
source.cancel('Operation canceled by the user.');
```


## Using `application/x-www-form-urlencoded` format

### URLSearchParams

By default, axios serializes JavaScript objects to `JSON`. To send data as `application/x-www-form-urlencoded`, use the `URLSearchParams` API. It works in most browsers and in Node v10 and later.

```highlight
const params = new URLSearchParams({ foo: 'bar' });
params.append('extraparam', 'value');
axios.post('/foo', params);
```

### Query string (older browsers)

For very old browsers, use a polyfill and make sure it patches the global environment.

Alternatively, you can encode data using the `qs` library:

```highlight
const qs = require('qs');
axios.post('/foo', qs.stringify({ bar: 123 }));
```

With ES modules:

```highlight
import qs from 'qs';
const data = { bar: 123 };
const options = {
  method: 'POST',
  headers: { 'content-type': 'application/x-www-form-urlencoded' },
  data: qs.stringify(data),
  url,
};
axios(options);
```

### Older Node.js versions

For older Node.js engines, use the `querystring` module:

```highlight
const querystring = require('querystring');
axios.post('https://something.com/', querystring.stringify({ foo: 'bar' }));
```

You can also use the `qs` library.

> Note: The `qs` library is preferable if you need to stringify nested objects, as the `querystring` method has known issues with that use case.

### Automatic serialization to URLSearchParams

Axios automatically serializes the data object to urlencoded format if the content-type header is set to "application/x-www-form-urlencoded".

```highlight
const data = {
  x: 1,
  arr: [1, 2, 3],
  arr2: [1, [2], 3],
  users: [
    { name: 'Peter', surname: 'Griffin' },
    { name: 'Thomas', surname: 'Anderson' },
  ],
};

await axios.postForm('https://postman-echo.com/post', data, {
  headers: { 'content-type': 'application/x-www-form-urlencoded' },
});
```

The server receives these fields:

```highlight
  {
    x: '1',
    'arr[]': [ '1', '2', '3' ],
    'arr2[0]': '1',
    'arr2[1][0]': '2',
    'arr2[2]': '3',
    'arr3[]': [ '1', '2', '3' ],
    'users[0][name]': 'Peter',
    'users[0][surname]': 'griffin',
    'users[1][name]': 'Thomas',
    'users[1][surname]': 'Anderson'
  }
```

If your backend body parser, such as `body-parser` for `express.js`, supports nested object decoding, the server receives the same object structure:

```highlight
const app = express();

app.use(bodyParser.urlencoded({ extended: true })); // support encoded bodies

app.post('/', function (req, res, next) {
  // echo body as JSON
  res.send(JSON.stringify(req.body));
});

server = app.listen(3000);
```


## Using `multipart/form-data` format

### FormData

To send data as `multipart/form-data`, pass a FormData instance as the payload. You do not need to set the `Content-Type` header. Axios detects it from the payload type. For browser, web worker, and React Native `FormData`, leave `Content-Type` unset so the runtime can add the multipart boundary.

```highlight
const formData = new FormData();
formData.append('foo', 'bar');

axios.post('https://httpbin.org/post', formData);
```

In node.js, use the `form-data` library:

```highlight
const FormData = require('form-data');

const form = new FormData();
form.append('my_field', 'my value');
form.append('my_buffer', Buffer.alloc(10));
form.append('my_file', fs.createReadStream('/foo/bar.jpg'));

axios.post('https://example.com', form);
```

In node.js, when a `FormData` object provides `getHeaders()`, axios copies all returned headers by default for v1 compatibility. If the `FormData` object is custom or not fully trusted, set `formDataHeaderPolicy: 'content-only'` to copy only `Content-Type` and `Content-Length`, and set any other request headers explicitly with the request `headers` config.

### Automatic serialization to FormData

Since `v0.27.0`, Axios can serialize an object to FormData if the request `Content-Type` header is set to `multipart/form-data`.

This request submits data as FormData in browsers and Node.js:

```highlight
import axios from 'axios';

axios
  .post(
    'https://httpbin.org/post',
    { x: 1 },
    {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    }
  )
  .then(({ data }) => console.log(data));
```

The Node.js build uses the `form-data` polyfill by default.

You can override the FormData class with the `env.FormData` config option, but most applications do not need this:

```highlight
const axios = require('axios');
var FormData = require('form-data');

axios
  .post(
    'https://httpbin.org/post',
    { x: 1, buf: Buffer.alloc(10) },
    {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    }
  )
  .then(({ data }) => console.log(data));
```

The Axios FormData serializer supports these special endings:

- `{}` - serialize the value with JSON.stringify
- `[]` - unwrap the array-like object as separate fields with the same key

> Note: Arrays and FileList objects are unwrapped by default.

FormData serializer supports additional options via `config.formSerializer: object` property to handle rare cases:

- `visitor: Function` - user-defined visitor function that Axios calls recursively to serialize the data object to a `FormData` object by following custom rules.
- `dots: boolean = false` - use dot notation instead of brackets to serialize arrays and objects;
- `metaTokens: boolean = true` - add the special ending (e.g `user{}: '{"name": "John"}'`) in the FormData key. A backend body parser can use this meta-information to parse the value as JSON.
- `indexes: null|false|true = false` - controls how Axios adds indexes to unwrapped keys of `flat` array-like objects.
  - `null` - don't add brackets (`arr: 1`, `arr: 2`, `arr: 3`)
  - `false`(default) - add empty brackets (`arr[]: 1`, `arr[]: 2`, `arr[]: 3`)
  - `true` - add brackets with indexes (`arr[0]: 1`, `arr[1]: 2`, `arr[2]: 3`)
- `maxDepth: number = 100` - maximum object nesting depth the serializer will recurse into. If the input object exceeds this depth, an `AxiosError` with `code: 'ERR_FORM_DATA_DEPTH_EXCEEDED'` is thrown instead of overflowing the call stack. This protects server applications from DoS attacks via deeply nested payloads. Set to `Infinity` to disable the limit and restore pre-fix behaviour.
- `Blob: typeof Blob` - Blob constructor used when converting ArrayBuffer-like values for spec-compliant `FormData`. Override it only for runtimes that provide a compatible `Blob` constructor under a different binding.

```highlight
// Raise the limit for a schema that genuinely nests deeper than 100 levels:
axios.postForm('/api', data, { formSerializer: { maxDepth: 200 } });

// Same protection applies to params serialization:
axios.get('/api', { params: data, paramsSerializer: { maxDepth: 200 } });
```

Given this object:

```highlight
const obj = {
  x: 1,
  arr: [1, 2, 3],
  arr2: [1, [2], 3],
  users: [
    { name: 'Peter', surname: 'Griffin' },
    { name: 'Thomas', surname: 'Anderson' },
  ],
  'obj2{}': [{ x: 1 }],
};
```

The Axios serializer appends these fields:

```highlight
const formData = new FormData();
formData.append('x', '1');
formData.append('arr[]', '1');
formData.append('arr[]', '2');
formData.append('arr[]', '3');
formData.append('arr2[0]', '1');
formData.append('arr2[1][0]', '2');
formData.append('arr2[2]', '3');
formData.append('users[0][name]', 'Peter');
formData.append('users[0][surname]', 'Griffin');
formData.append('users[1][name]', 'Thomas');
formData.append('users[1][surname]', 'Anderson');
formData.append('obj2{}', '[{"x":1}]');
```

Axios supports `postForm`, `putForm`, and `patchForm` as shortcuts for the matching HTTP methods with the `Content-Type` header preset to `multipart/form-data`.


## Posting files

Submit a single file:

```highlight
await axios.postForm('https://httpbin.org/post', {
  myVar: 'foo',
  file: document.querySelector('#fileInput').files[0],
});
```

or multiple files as `multipart/form-data`:

```highlight
await axios.postForm('https://httpbin.org/post', {
  'files[]': document.querySelector('#fileInput').files,
});
```

`FileList` object can be passed directly:

```highlight
await axios.postForm('https://httpbin.org/post', document.querySelector('#fileInput').files);
```

Axios sends all files with the same field name: `files[]`.


## HTML form posting (browser)

Pass an HTML Form element as a payload to submit it as `multipart/form-data` content.

```highlight
await axios.postForm('https://httpbin.org/post', document.querySelector('#htmlForm'));
```

`FormData` and `HTMLForm` objects can also be posted as `JSON` by explicitly setting the `Content-Type` header to `application/json`:

```highlight
await axios.post('https://httpbin.org/post', document.querySelector('#htmlForm'), {
  headers: {
    'Content-Type': 'application/json',
  },
});
```

For example, the Form

```highlight
<form id="form">
  <input type="text" name="foo" value="1" />
  <input type="text" name="deep.prop" value="2" />
  <input type="text" name="deep prop spaced" value="3" />
  <input type="text" name="baz" value="4" />
  <input type="text" name="baz" value="5" />

  <select name="user.age">
    <option value="value1">Value 1</option>
    <option value="value2" selected>Value 2</option>
    <option value="value3">Value 3</option>
  </select>

  <input type="submit" value="Save" />
</form>
```

submits this JSON object:

```highlight
{
  "foo": "1",
  "deep": {
    "prop": {
      "spaced": "3"
    }
  },
  "baz": [
    "4",
    "5"
  ],
  "user": {
    "age": "value2"
  }
}
```

Sending `Blobs`/`Files` as JSON (`base64`) is not currently supported.


## Progress capturing

Axios can capture request upload and download progress in browsers and Node.js. Progress events are limited to `3` times per second.

```highlight
await axios.post(url, data, {
  onUploadProgress: function (axiosProgressEvent) {
    /*{
      loaded: number;
      total?: number;
      progress?: number; // in range [0..1]
      bytes: number; // how many bytes have been transferred since the last trigger (delta)
      estimated?: number; // estimated time in seconds
      rate?: number; // upload speed in bytes
      upload: true; // upload sign
    }*/
  },

  onDownloadProgress: function (axiosProgressEvent) {
    /*{
      loaded: number;
      total?: number;
      progress?: number;
      bytes: number;
      estimated?: number;
      rate?: number; // download speed in bytes
      download: true; // download sign
    }*/
  },
});
```

You can also track stream upload/download progress in node.js:

```highlight
const { data } = await axios.post(SERVER_URL, readableStream, {
  onUploadProgress: ({ progress }) => {
    console.log((progress * 100).toFixed(2));
  },

  headers: {
    'Content-Length': contentLength,
  },

  maxRedirects: 0, // avoid buffering the entire stream
});
```

> Note: Capturing FormData upload progress is not currently supported in node.js environments.

> Warning: Set `maxRedirects: 0` when uploading streams in node.js. The follow-redirects package buffers the entire stream in RAM and does not follow the "backpressure" algorithm.


## Rate limiting

Download and upload rate limits can only be set for the http adapter (node.js):

```highlight
const { data } = await axios.post(LOCAL_SERVER_URL, myBuffer, {
  onUploadProgress: ({ progress, rate }) => {
    console.log(`Upload [${(progress * 100).toFixed(2)}%]: ${(rate / 1024).toFixed(2)}KB/s`);
  },

  maxRate: [100 * 1024], // 100KB/s limit
});
```


## AxiosHeaders

Axios includes an `AxiosHeaders` class for working with headers through a Map-like API. HTTP header names are case-insensitive, but Axios keeps the original header case for style and for servers that incorrectly depend on case. Directly manipulating the headers object still works, but it is deprecated.

### Working with headers

An `AxiosHeaders` instance can contain several internal value types that control setting and merging. Axios gets the final headers object with string values by calling `toJSON`.

> Note: By JSON here we mean an object consisting only of string values intended to be sent over the network.

The header value can be one of the following types:

- `string` - normal string value sent to the server
- `null` - skip header when rendering to JSON
- `false` - skip header when rendering to JSON. Also indicates that the `set` method must be called with `rewrite` set to `true` to overwrite this value (Axios uses this internally to allow users to opt out of installing certain headers like `User-Agent` or `Content-Type`)
- `undefined` - value is not set

> Note: The header value is considered set if it is not equal to undefined.

The headers object is always initialized inside interceptors and transformers:

```highlight
axios.interceptors.request.use((request: InternalAxiosRequestConfig) => {
  request.headers.set('My-header', 'value');

  request.headers.set({
    'My-set-header1': 'my-set-value1',
    'My-set-header2': 'my-set-value2',
  });

  request.headers.set('User-Agent', false); // prevent Axios from setting this header later

  request.headers.setContentType('text/plain');

  request.headers['My-set-header2'] = 'newValue'; // direct access is deprecated

  return request;
});
```

You can iterate over an `AxiosHeaders` instance using a `for...of` statement:

```highlight
const headers = new AxiosHeaders({
  foo: '1',
  bar: '2',
  baz: '3',
});

for (const [header, value] of headers) {
  console.log(header, value);
}

// foo 1
// bar 2
// baz 3
```

### Preserving a specific header case

Header names are case-insensitive, but `AxiosHeaders` keeps the case of the first matching key it sees. If you need a specific case for non-standard case-sensitive servers, define a case preset with `undefined` and then set the value later:

```highlight
const api = axios.create();

api.defaults.headers.common = {
  'content-type': undefined,
  accept: undefined,
};

await api.put(url, data, {
  headers: {
    'Content-Type': 'application/octet-stream',
    Accept: 'application/json',
  },
});
```

You can also compose the same behavior with `AxiosHeaders.concat`:

```highlight
const headers = axios.AxiosHeaders.concat(
  { 'content-type': undefined },
  { 'Content-Type': 'application/octet-stream' }
);

await axios.put(url, data, { headers });
```

### new AxiosHeaders(headers?)

Constructs a new `AxiosHeaders` instance.

```
constructor(headers?: RawAxiosHeaders | AxiosHeaders | string);
```

If the headers object is a string, Axios parses it as raw HTTP headers.

```highlight
const headers = new AxiosHeaders(`
Host: www.bing.com
User-Agent: curl/7.54.0
Accept: */*`);

console.log(headers);

// Object [AxiosHeaders] {
//   host: 'www.bing.com',
//   'user-agent': 'curl/7.54.0',
//   accept: '*/*'
// }
```

### AxiosHeaders#set

```highlight
set(headerName, value: Axios, rewrite?: boolean);
set(headerName, value, rewrite?: (this: AxiosHeaders, value: string, name: string, headers: RawAxiosHeaders) => boolean);
set(headers?: RawAxiosHeaders | AxiosHeaders | string, rewrite?: boolean);
set(headers?: Iterable<[string, AxiosHeaderValue]>, rewrite?: boolean);
```

The `rewrite` argument controls the overwriting behavior:

- `false` - do not overwrite if the header's value is set (is not `undefined`)
- `undefined` (default) - overwrite the header unless its value is set to `false`
- `true` - rewrite anyway

The option can also accept a user-defined function that determines whether to overwrite the value.

Empty or whitespace-only header names are ignored.

Iterable key/value pairs, such as a `Map`, are accepted:

```highlight
const headers = new AxiosHeaders();

headers.set(
  new Map([
    ['X-Trace-Id', 'abc123'],
    ['Accept', 'application/json'],
  ])
);
```

Returns `this`.

### AxiosHeaders#get(header)

```
  get(headerName: string, matcher?: true | AxiosHeaderMatcher): AxiosHeaderValue;
  get(headerName: string, parser: RegExp): RegExpExecArray | null;
```

Returns the internal value of the header. It can take an extra argument to parse the header's value with `RegExp.exec`, matcher function or internal key-value parser.

```highlight
const headers = new AxiosHeaders({
  'Content-Type': 'multipart/form-data; boundary=Asrf456BGe4h',
});

console.log(headers.get('Content-Type'));
// multipart/form-data; boundary=Asrf456BGe4h

console.log(headers.get('Content-Type', true)); // parse key-value pairs from a string separated with \s,;= delimiters:
// [Object: null prototype] {
//   'multipart/form-data': undefined,
//    boundary: 'Asrf456BGe4h'
// }

console.log(
  headers.get('Content-Type', (value, name, headers) => {
    return String(value).replace(/a/g, 'ZZZ');
  })
);
// multipZZZrt/form-dZZZtZZZ; boundZZZry=Asrf456BGe4h

console.log(headers.get('Content-Type', /boundary=(\w+)/)?.[0]);
// boundary=Asrf456BGe4h
```

Returns the value of the header.

### AxiosHeaders#has(header, matcher?)

```
has(header: string, matcher?: AxiosHeaderMatcher): boolean;
```

Returns `true` if the header is set (has no `undefined` value).

### AxiosHeaders#delete(header, matcher?)

```
delete(header: string | string[], matcher?: AxiosHeaderMatcher): boolean;
```

Returns `true` if at least one header has been removed.

### AxiosHeaders#clear(matcher?)

```
clear(matcher?: AxiosHeaderMatcher): boolean;
```

Removes all headers. Unlike the `delete` method matcher, this optional matcher matches the header name rather than the value.

```highlight
const headers = new AxiosHeaders({
  foo: '1',
  'x-foo': '2',
  'x-bar': '3',
});

console.log(headers.clear(/^x-/)); // true

console.log(headers.toJSON()); // [Object: null prototype] { foo: '1' }
```

Returns `true` if at least one header has been cleared.

### AxiosHeaders#normalize(format);

If the headers object was changed directly, it can have duplicates with the same name but in different cases. This method normalizes the headers object by combining duplicate keys into one. Axios uses this method internally after calling each interceptor. Set `format` to true for converting header names to lowercase and capitalizing the initial letters (`cOntEnt-type` => `Content-Type`)

```highlight
const headers = new AxiosHeaders({
  foo: '1',
});

headers.Foo = '2';
headers.FOO = '3';

console.log(headers.toJSON()); // [Object: null prototype] { foo: '1', Foo: '2', FOO: '3' }
console.log(headers.normalize().toJSON()); // [Object: null prototype] { foo: '3' }
console.log(headers.normalize(true).toJSON()); // [Object: null prototype] { Foo: '3' }
```

Returns `this`.

### AxiosHeaders#concat(...targets)

```
concat(...targets: Array<AxiosHeaders | RawAxiosHeaders | string | undefined | null>): AxiosHeaders;
```

Merges the instance with targets into a new `AxiosHeaders` instance. If the target is a string, Axios parses it as raw HTTP headers.

Returns a new `AxiosHeaders` instance.

### AxiosHeaders#toJSON(asStrings?)

```
toJSON(asStrings: true): Record<string, string>;
toJSON(asStrings?: false): Record<string, string | string[]>;
```

Resolves all internal header values into a new null prototype object. Set `asStrings` to true to resolve arrays as a string containing all elements, separated by commas.

### AxiosHeaders#toString()

```
toString(): string;
```

Returns the headers as a CRLF-free HTTP header block, one `name: value` pair per line.

### AxiosHeaders.from(thing?)

```
from(thing?: AxiosHeaders | RawAxiosHeaders | string): AxiosHeaders;
```

Returns a new `AxiosHeaders` instance created from the raw headers passed in, or returns the given headers object if it's already an `AxiosHeaders` instance.

### AxiosHeaders.concat(...targets)

```
concat(...targets: Array<AxiosHeaders | RawAxiosHeaders | string | undefined | null>): AxiosHeaders;
```

Returns a new `AxiosHeaders` instance created by merging the target objects.

### Shortcuts

The following shortcuts are available:

- `setContentType`, `getContentType`, `hasContentType`
- `setContentLength`, `getContentLength`, `hasContentLength`
- `setAccept`, `getAccept`, `hasAccept`
- `setUserAgent`, `getUserAgent`, `hasUserAgent`
- `setContentEncoding`, `getContentEncoding`, `hasContentEncoding`


## Fetch adapter

Axios introduced the fetch adapter in `v1.7.0`. By default, Axios uses it when the `xhr` and `http` adapters are not available in the build or not supported by the environment. To use it by default, select it explicitly:

```highlight
const { data } = axios.get(url, {
  adapter: 'fetch', // by default ['xhr', 'http', 'fetch']
});
```

You can create a separate instance for this:

```highlight
const fetchAxios = axios.create({
  adapter: 'fetch',
});

const { data } = fetchAxios.get(url);
```

The adapter supports the same features as the `xhr` adapter, including upload and download progress capturing. It also supports response types such as `stream` and `formdata` when the environment supports them.

When `auth` is omitted, the fetch adapter can read HTTP Basic auth credentials from the request URL, for example `https://user:pass@example.com`. Percent-encoded URL credentials are decoded before the `Authorization` header is generated, and `auth` takes precedence over URL-embedded credentials.

### Custom fetch

Since `v1.12.0`, you can configure the fetch adapter to use a custom fetch API instead of environment globals. Pass a custom `fetch` function, `Request`, and `Response` constructors through `env` config. This helps in custom environments and app frameworks.

When using a custom fetch, you may also need to set custom `Request` and `Response` constructors. If you do not set them, Axios uses the global objects. If your custom fetch API does not provide these objects and the globals are incompatible with it, pass `null` to disable them inside the fetch adapter.

> Note: Setting `Request` and `Response` to `null` prevents the fetch adapter from capturing upload and download progress.

Basic example:

```highlight
import customFetchFunction from 'customFetchModule';

const instance = axios.create({
  adapter: 'fetch',
  onDownloadProgress(e) {
    console.log('downloadProgress', e);
  },
  env: {
    fetch: customFetchFunction,
    Request: null, // undefined -> use the global constructor
    Response: null,
  },
});
```

#### Using with Tauri

A minimal example of setting up Axios for use in a Tauri app with a platform fetch function that ignores CORS policy for requests.

```highlight
import { fetch } from '@tauri-apps/plugin-http';
import axios from 'axios';

const instance = axios.create({
  adapter: 'fetch',
  onDownloadProgress(e) {
    console.log('downloadProgress', e);
  },
  env: {
    fetch,
  },
});

const { data } = await instance.get('https://google.com');
```

#### Using with SvelteKit

SvelteKit uses a custom fetch function for server rendering in `load` functions. It also uses relative paths, which are incompatible with the standard URL API. Configure Axios to use SvelteKit's custom fetch API:

```highlight
export async function load({ fetch }) {
  const { data: post } = await axios.get('https://jsonplaceholder.typicode.com/posts/1', {
    adapter: 'fetch',
    env: {
      fetch,
      Request: null,
      Response: null,
    },
  });

  return { post };
}
```

#### HTTP/2 support

Axios supports HTTP/2 through the Node.js `http` adapter, introduced in v1.13.0.

Support depends on the runtime environment. Axios relies on Node.js APIs, so HTTP/2 works in supported Node.js versions but may not work in other environments such as Bun or Deno.

Options like `httpVersion` and `http2Options` are adapter-specific and may not behave the same way in every environment.

Note: HTTP/2 redirects are currently not supported by the HTTP/2 adapter.

```highlight
const form = new FormData();

form.append('foo', '123');

const { data, headers, status } = await axios.post('https://httpbin.org/post', form, {
  onUploadProgress(e) {
    console.log('upload progress', e);
  },
  onDownloadProgress(e) {
    console.log('download progress', e);
  },
  responseType: 'arraybuffer',
});
```


## Semver

Axios follows semver since `v1.0.0`.


## Promises

axios depends on a native ES6 Promise implementation to be supported. If your environment doesn't support ES6 Promises, you can polyfill.


## TypeScript

axios includes TypeScript definitions and a type guard for axios errors.

```highlight
let user: User = null;
try {
  const { data } = await axios.get('/user?ID=12345');
  user = data.userDetails;
} catch (error) {
  if (axios.isAxiosError(error)) {
    handleAxiosError(error);
  } else {
    handleUnexpectedError(error);
  }
}
```

Use `axios.isCancel<T>()` to narrow cancellation errors to `CanceledError<T>`:

```highlight
const controller = new AbortController();

try {
  await axios.get<User>('/user?ID=12345', { signal: controller.signal });
} catch (error) {
  if (axios.isCancel<User>(error)) {
    handleCancellation(error);
  }
}
```

Because axios publishes an ESM default export and a CJS `module.exports`, TypeScript has a few caveats. The recommended setting is `"moduleResolution": "node16"`, which is implied by `"module": "node16"`. This requires TypeScript 4.7 or greater. If you use ESM, your settings should be fine. If you compile TypeScript to CJS and can't use `"moduleResolution": "node 16"`, enable `esModuleInterop`. If you use TypeScript to type check CJS JavaScript code, your only option is to use `"moduleResolution": "node16"`.

You can also create a custom instance with typed interceptors:

```highlight
import axios, { AxiosInstance, InternalAxiosRequestConfig } from 'axios';

const apiClient: AxiosInstance = axios.create({
  baseURL: 'https://api.example.com',
  timeout: 10000,
});

apiClient.interceptors.request.use((config: InternalAxiosRequestConfig) => {
  // Add auth token
  return config;
});
```


## Online one-click setup

You can use Gitpod, a free online IDE for open source projects, to contribute or run the examples online.

(Open in Gitpod)


## Contributing

### Local setup

As a supply-chain hardening measure, this repository ships a project-level `.npmrc` that sets `ignore-scripts=true`. This blocks npm lifecycle scripts (`preinstall`, `install`, `postinstall`, `prepare`) from any direct or transitive dependency when you run `npm install` or `npm ci` inside the repo. See THREATMODEL.md (threat T-S2) for the rationale.

One consequence: the repository's own `prepare` hook (which installs Husky's git hooks) will **not** run automatically. After your first install, enable the git hooks manually:

```highlight
npm ci
npm rebuild husky && npx husky
```

Run those two commands once per fresh checkout. You do **not** need to re-run them after every subsequent `npm install`.

Do not remove `ignore-scripts=true` from `.npmrc` to "fix" this. That reopens the lifecycle-script attack surface for every other package in the tree. All CI workflows already invoke npm with `--ignore-scripts`, so local behaviour matches CI.


## Resources

- Changelog
- Ecosystem
- Contributing Guide
- Code of Conduct


## Credits

axios is heavily inspired by the $http service in AngularJS. It provides a standalone `$http`-like service for use outside AngularJS.


## License

(License: MIT)
