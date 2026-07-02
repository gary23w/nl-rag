---
title: "GitHub (part 2/2)"
source: https://github.com/sindresorhus/ky
domain: ky-fetch
license: CC-BY-SA-4.0
tags: ky fetch, fetch wrapper, javascript http client, request retry
fetched: 2026-07-02
part: 2/2
---

## Tips

### Sending form data

Sending form data in Ky is identical to `fetch`. Just pass a `FormData` instance to the `body` option. The `Content-Type` header will be automatically set to `multipart/form-data`, overriding any existing `Content-Type` header.

```highlight
import ky from 'ky';

// `multipart/form-data`
const formData = new FormData();
formData.append('food', 'fries');
formData.append('drink', 'icetea');

const response = await ky.post(url, {body: formData});
```

If you want to send the data in `application/x-www-form-urlencoded` format, you will need to encode the data with `URLSearchParams`. Like `FormData`, this will override any existing `Content-Type` headers.

```highlight
import ky from 'ky';

// `application/x-www-form-urlencoded`
const searchParams = new URLSearchParams();
searchParams.set('food', 'fries');
searchParams.set('drink', 'icetea');

const response = await ky.post(url, {body: searchParams});
```

#### Modifying FormData in hooks

If you need to modify FormData in a `beforeRequest` hook (for example, to transform field names), delete the `Content-Type` header before creating a new `Request`:

```highlight
import ky from 'ky';

const response = await ky.post(url, {
	body: formData,
	hooks: {
		beforeRequest: [
			({request}) => {
				const newFormData = new FormData();

				// Modify FormData as needed
				for (const [key, value] of formData) {
					newFormData.set(key.toLowerCase(), value);
				}

				// Delete `Content-Type` to let Request regenerate it with correct boundary
				request.headers.delete('content-type');

				return new Request(request, {body: newFormData});
			}
		]
	}
});
```

### Setting a custom `Content-Type`

Ky automatically sets an appropriate `Content-Type` header for each request based on the data in the request body. However, some APIs require custom, non-standard content types, such as `application/x-amz-json-1.1`. Using the `headers` option, you can manually override the content type.

```highlight
import ky from 'ky';

const json = await ky.post('https://example.com', {
	headers: {
		'content-type': 'application/x-amz-json-1.1'
	},
	json: {
		foo: true
	},
}).json();

console.log(json);
//=> {data: '🦄'}
```

### Cancellation

Fetch (and hence Ky) has built-in support for request cancellation through the `AbortController` API. Read more.

Example:

```highlight
import ky from 'ky';

const controller = new AbortController();
const {signal} = controller;

setTimeout(() => {
	controller.abort();
}, 5000);

try {
	console.log(await ky(url, {signal}).text());
} catch (error) {
	if (error.name === 'AbortError') {
		console.log('Fetch aborted');
	} else {
		console.error('Fetch error:', error);
	}
}
```

### Proxy support (Node.js)

#### Native proxy support

Node.js 24.5+ supports automatic proxy configuration via environment variables. Set `NODE_USE_ENV_PROXY=1` or use the `--use-env-proxy` CLI flag.

```highlight
NODE_USE_ENV_PROXY=1 HTTP_PROXY=http://proxy.example.com:8080 node app.js
```

Or:

```highlight
node --use-env-proxy app.js
```

Supported environment variables:

- `HTTP_PROXY` / `http_proxy`: Proxy URL for HTTP requests
- `HTTPS_PROXY` / `https_proxy`: Proxy URL for HTTPS requests
- `NO_PROXY` / `no_proxy`: Comma-separated list of hosts to bypass the proxy

#### Using ProxyAgent

For more control, use `ProxyAgent` or `EnvHttpProxyAgent` with the `dispatcher` option.

```highlight
import ky from 'ky';
import {ProxyAgent} from 'undici';

const proxyAgent = new ProxyAgent('http://proxy.example.com:8080');

const response = await ky('https://example.com', {
	dispatcher: proxyAgent
}).json();
```

Using `EnvHttpProxyAgent` to automatically read proxy settings from environment variables:

```highlight
import ky from 'ky';
import {EnvHttpProxyAgent} from 'undici';

const proxyAgent = new EnvHttpProxyAgent();

const api = ky.extend({
	dispatcher: proxyAgent
});

const response = await api('https://example.com').json();
```

### HTTP/2 support (Node.js)

Undici supports HTTP/2, but it's not enabled by default. Create a custom dispatcher with the `allowH2` option:

```highlight
import ky from 'ky';
import {Agent, Pool} from 'undici';

const agent = new Agent({
	factory(origin, options) {
		return new Pool(origin, {
			...options,
			allowH2: true
		});
	}
});

const response = await ky('https://example.com', {
	dispatcher: agent
}).json();
```

Combine proxy and HTTP/2:

```highlight
import ky from 'ky';
import {ProxyAgent} from 'undici';

const proxyAgent = new ProxyAgent({
	uri: 'http://proxy.example.com:8080',
	allowH2: true
});

const response = await ky('https://example.com', {
	dispatcher: proxyAgent
}).json();
```

### Streaming request bodies

To send a `ReadableStream` as the request body, you must pass `duplex: 'half'` per the Fetch spec. Ky can't set this automatically as it changes request semantics for all requests, not just streaming ones.

```highlight
import ky from 'ky';

const stream = new ReadableStream({
	start(controller) {
		controller.enqueue(new TextEncoder().encode('hello'));
		controller.close();
	},
});

const response = await ky.post('https://example.com/upload', {
	body: stream,
	duplex: 'half',
});
```

Note

When retries are enabled (the default), Ky buffers the entire streaming body in memory to support replaying it. Set `retry: {limit: 0}` to skip this if retries aren't needed.

### Consuming Server-Sent Events (SSE)

Use `parse-sse`:

```highlight
import ky from 'ky';
import {parseServerSentEvents} from 'parse-sse';

const response = await ky('https://api.example.com/events');

for await (const event of parseServerSentEvents(response)) {
	console.log(event.data);
}
```

### Pagination

Use `fetch-extras` with Ky for paginating API responses:

```highlight
import ky from 'ky';
import {paginate} from 'fetch-extras';

const url = 'https://api.github.com/repos/sindresorhus/ky/commits';

for await (const commit of paginate(url, {fetchFunction: ky})) {
	console.log(commit.sha);
}
```

### Extending types

Ky's TypeScript types are intentionally defined as type aliases rather than interfaces to prevent global module augmentation, which can lead to type conflicts and unexpected behavior across your codebase. If you need to add custom properties to Ky's types like `KyResponse` or `HTTPError`, create local wrapper types instead:

```highlight
import ky, {HTTPError, isHTTPError} from 'ky';

interface CustomError extends HTTPError {
	customProperty: unknown;
}

const api = ky.extend({
	hooks: {
		beforeError: [
			async ({error}) => {
				if (isHTTPError(error)) {
					(error as CustomError).customProperty = 'value';
				}

				return error;
			}
		]
	}
});

// Use with type assertion
const data = (error as CustomError).customProperty;
```

This approach keeps your types scoped to where they're needed without polluting the global namespace.


## FAQ

#### How do I use this in Node.js?

Node.js supports `fetch` natively, so you can just use this package directly.

#### How do I use this with a web app (React, Vue.js, etc.) that uses server-side rendering (SSR)?

Node.js supports `fetch` natively, so you can use Ky directly. The main consideration is that server-side requests require absolute URLs, while client-side requests can use relative URLs. Handle this with a conditional `baseUrl`:

```highlight
const api = ky.create({
	baseUrl: globalThis.window === undefined
		? (process.env.BASE_URL ?? 'http://localhost:3000')
		: undefined,
});
```

#### What's the difference between `baseUrl` and `prefix`?

**`baseUrl`** follows standard URL resolution rules — the same behavior as `new URL(input, baseUrl)`. A leading slash on the input means origin-root, overriding any path in the base URL.

**`prefix`** does plain string joining before URL resolution. The leading slash on the input is stripped, so it always appends to the prefix regardless.

Use `baseUrl` in almost all cases. Use `prefix` only when you want origin-relative inputs like `/users` to be treated as page-relative.

```highlight
// On https://example.com

// baseUrl: standard URL resolution
ky('users',  {baseUrl: '/api/'});
//=> https://example.com/api/users

ky('/users', {baseUrl: '/api/'});
//=> https://example.com/users  ← leading slash wins

// prefix: always appends
ky('users',  {prefix: '/api'});
//=> https://example.com/api/users

ky('/users', {prefix: '/api'});
//=> https://example.com/api/users  ← leading slash ignored
```

#### How do I test a browser library that uses this?

Use a test runner that can run in the browser, like Vitest or Playwright.

#### How do I add authentication headers to every request?

Use the `beforeRequest` hook to attach headers before each request:

```highlight
const api = ky.create({
	hooks: {
		beforeRequest: [
			({request}) => {
				request.headers.set('Authorization', `Bearer ${getToken()}`);
			}
		]
	}
});
```

#### How do I implement token refresh on 401 responses?

Configure `retry` to retry on 401, then use the `beforeRetry` hook to refresh the token:

```highlight
const api = ky.create({
	retry: {statusCodes: [401]},
	hooks: {
		beforeRetry: [
			async ({request}) => {
				const token = await refreshToken();
				request.headers.set('Authorization', `Bearer ${token}`);
			}
		]
	}
});
```

#### How do I mock Ky in tests?

Use MSW to intercept requests at the network level without modifying your code. Alternatively, pass a custom `fetch` to your Ky instance:

```highlight
const api = ky.create({
	fetch: async () => new Response(JSON.stringify({name: 'Test'}), {
		headers: {
			'Content-Type': 'application/json'
		},
	}),
});
```

#### How do I retry based on the response body?

Use `ky.retry()` in an `afterResponse` hook. This lets you force a retry even when the status code is 2xx:

```highlight
import ky from 'ky';

const response = await ky('https://example.com', {
	hooks: {
		afterResponse: [
			async ({response}) => {
				const data = await response.json();

				if (data.status === 'pending') {
					return ky.retry();
				}
			}
		]
	}
});
```

The retry respects `retry.limit` and is observable in `beforeRetry` hooks.

#### How do I stop retrying early?

Throw from a `beforeRetry` hook to stop retrying and propagate the error, or return `ky.stop` to stop silently (the request resolves with `undefined`):

```highlight
import ky, {isHTTPError} from 'ky';

const response = await ky('https://example.com', {
	hooks: {
		beforeRetry: [
			({error}) => {
				if (isHTTPError(error) && error.response.status === 400) {
					throw error; // Stop retrying, propagate the error
				}
			}
		]
	}
});
```

#### How do I only throw on certain HTTP errors?

For simple status-based filtering, pass a function to `throwHttpErrors`:

```highlight
import ky from 'ky';

// Only throw on 5xx errors; 4xx responses are returned normally
const api = ky.create({
	throwHttpErrors: status => status >= 500,
});

const response = await api('https://example.com/resource');

if (response.status === 404) {
	// Handle "not found" as normal app flow
}
```

If you need to access the response body in the non-throwing path, use `throwHttpErrors: false` and throw manually in an `afterResponse` hook:

```highlight
import ky, {HTTPError} from 'ky';

const api = ky.create({
	throwHttpErrors: false,
	hooks: {
		afterResponse: [
			({request, options, response}) => {
				if (response.status >= 500) {
					throw new HTTPError(response, request, options);
				}
			}
		]
	}
});
```

#### How do I use this without a bundler like Webpack?

Make sure your code is running as a JavaScript module (ESM), for example by using a `<script type="module">` tag in your HTML document. Then Ky can be imported directly by that module without a bundler or other tools.

```highlight
<script type="module">
import ky from 'https://unpkg.com/ky/distribution/index.js';

const json = await ky('https://jsonplaceholder.typicode.com/todos/1').json();

console.log(json.title);
//=> 'delectus aut autem'
</script>
```

#### How is it different from `got`?

Got is maintained by the same people as Ky, so you probably want Ky instead. It's smaller, works in the browser too, and is more stable since it's built on Fetch.

#### How is it different from `axios`?

Axios predates the Fetch API and has a lot of legacy baggage. Ky is built on Fetch, which means it's smaller, more standards-compliant, and works everywhere Fetch does (browsers, Node.js, Bun, Deno). Ky also has a more modern API with better TypeScript support.

#### What does `ky` mean?

It's just a random short npm package name I managed to get. It does, however, have a meaning in Japanese:

> A form of text-able slang, KY is an abbreviation for 空気読めない (kuuki yomenai), which literally translates into “cannot read the air.” It's a phrase applied to someone who misses the implied meaning.


## Browser support

The latest version of Chrome, Firefox, and Safari.


## Node.js support

Node.js 22 and later.


## Related

- fetch-extras - Useful utilities for working with Fetch
- ky-hooks-change-case - Ky hooks to modify cases on requests and responses of objects


## Maintainers

- Sindre Sorhus
- Seth Holladay
- Szymon Marczak
