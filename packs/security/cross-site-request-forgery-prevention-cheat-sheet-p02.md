---
title: "Cross-Site Request Forgery Prevention (part 2/2)"
source: https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html
domain: security
license: CC-BY-SA-4.0 (OWASP) / CC-BY-SA-4.0 (Wikipedia)
tags: security, authentication, password hashing, session token, tls, owasp
fetched: 2026-07-02
part: 2/2
---

## REFERENCE: Sample JEE Filter Demonstrating CSRF Protection

The following JEE web filter provides an example reference for some of the concepts described in this cheatsheet. It implements the following stateless mitigations (OWASP CSRFGuard, cover a stateful approach).

- Verifying same origin with standard headers
- Double submit cookie
- SameSite cookie attribute

**Please note** that this is only a reference sample and is not complete (for example: it doesn't have a block to direct the control flow when origin and referrer header check succeeds nor it has a port/host/protocol level validation for referrer header). Developers are recommended to build their complete mitigation on top of this reference sample. Developers should also implement authentication and authorization mechanisms before checking for CSRF is considered effective.

Full source is located here and provides a runnable POC.


## JavaScript: Automatically Including CSRF Tokens as an AJAX Request Header

The following guidance for JavaScript by default considers **GET**, **HEAD** and **OPTIONS** methods as safe operations. Therefore **GET**, **HEAD**, and **OPTIONS** method AJAX calls need not be appended with a CSRF token header. However, if the verbs are used to perform state changing operations, they will also require a CSRF token header (although this is a bad practice, and should be avoided).

The **POST**, **PUT**, **PATCH**, and **DELETE** methods, being state changing verbs, should have a CSRF token attached to the request. The following guidance will demonstrate how to create overrides in JavaScript libraries to have CSRF tokens included automatically with every AJAX request for the state changing methods mentioned above.

### Storing the CSRF Token Value in the DOM

A CSRF token can be included in the `<meta>` tag as shown below. All subsequent calls in the page can extract the CSRF token from this `<meta>` tag. It can also be stored in a JavaScript variable or anywhere on the DOM. However, it is not recommended to store the CSRF token in cookies or browser local storage.

The following code snippet can be used to include a CSRF token as a `<meta>` tag:

```
<meta name="csrf-token" content="{{ csrf_token() }}">
```

The exact syntax of populating the content attribute would depend on your web application's backend programming language.

### Overriding Defaults to Set Custom Header

Several JavaScript libraries allow you to override default settings to have a header added automatically to all AJAX requests.

#### XMLHttpRequest (Native JavaScript)

XMLHttpRequest's open() method can be overridden to set the `X-CSRF-Token` header whenever the `open()` method is invoked next. The function `csrfSafeMethod()` defined below will filter out the safe HTTP methods and only add the header to unsafe HTTP methods.

This can be done as demonstrated in the following code snippet:

```
<script type="text/javascript">
    const csrf_token = document.querySelector("meta[name='csrf-token']").getAttribute("content");

    const csrfSafeMethod = (method) => {
        // these HTTP methods do not require CSRF protection
        return /^(GET|HEAD|OPTIONS)$/.test(method);
    };

    const originalOpen = XMLHttpRequest.prototype.open;
    XMLHttpRequest.prototype.open = function(...args) {
        const result = originalOpen.apply(this, args);

        if (!csrfSafeMethod(args[0])) {
            this.setRequestHeader('X-CSRF-Token', csrf_token);
        }

        return result;
    };
</script>
```

#### CSRF Prevention in modern Frameworks

Modern Single Page Application (SPA) frameworks like Angular, React, and Vue typically rely on the cookie-to-header pattern to mitigate Cross-Site Request Forgery (CSRF) attacks. This approach leverages the fact that browsers automatically attach cookies to cross-origin requests, but only JavaScript running on the same origin can read values and set custom headers—making it possible to detect and block forged requests. The cookie-to-header pattern works as follows:

1. Server generates a CSRF token: When a user authenticates or loads the app, the server sets a CSRF token in a cookie (e.g., `XSRF-TOKEN`). This cookie is accessible via JavaScript (i.e., not `HttpOnly`) and typically has `SameSite=Lax` or `Strict`.
2. Client reads the token: The SPA (often using a library like Angular's HttpClient or axios in React/Vue) reads the CSRF token from the cookie.
3. Client attaches the token to a custom header: For each state-changing request (`POST`, `PUT`, `DELETE`, etc.), the client sets the token as a custom HTTP header (commonly `X-XSRF-TOKEN` or `X-CSRF-TOKEN`).
4. Server validates the token: The server checks whether the token from the header matches the one from the cookie. If they match, the request is accepted; if not, it is rejected as potentially forged.

Angular provides this pattern out of the box, automatically handling steps 2 and 3 via its HttpClient. In contrast, frameworks like React and Vue require developers to implement this logic manually or with helper libraries such as axios interceptors. This pattern ensures that even if a browser includes cookies with a forged request, the attacker cannot set the matching custom header from another origin.

#### Angular

Angular's HttpClient supports the Cookie-to-Header Pattern used to prevent XSRF attacks. When performing HTTP requests, an interceptor reads a token from a cookie, by default `XSRF-TOKEN`, and sets it as an HTTP header, `X-XSRF-TOKEN`. Further documentation can be found at Angular's documentation for HttpClient XSRF/CSRF security.

```
// app.config.ts
export const appConfig: ApplicationConfig = {
  providers: [
    provideHttpClient(withXsrfConfiguration({})),
    provideRouter(routes, withComponentInputBinding()),
  ],
};
```

This code snippet has been tested with Angular version 19.2.11.

#### React

For React applications, you can use axios interceptors to implement the cookie-to-header pattern:

```
// csrf-protection.js
import axios from 'axios';

// Function to get the CSRF token from cookies
const getCsrfToken = () => {
  const tokenCookie = document.cookie
    .split('; ')
    .find(cookie => cookie.startsWith('XSRF-TOKEN='));

  return tokenCookie ? tokenCookie.split('=')[1] : '';
};

// Create an axios instance with interceptors
const api = axios.create();

// Add a request interceptor to include the CSRF token in headers
api.interceptors.request.use(config => {
  // Only add for state-changing methods
  if (!/^(GET|HEAD|OPTIONS)$/i.test(config.method)) {
    config.headers['X-CSRF-Token'] = getCsrfToken();
  }
  return config;
});

export default api;
```

#### Axios

Axios allows us to set default headers for the POST, PUT, DELETE and PATCH actions.

```
<script type="text/javascript">
    const csrf_token = document.querySelector("meta[name='csrf-token']").getAttribute("content");

    // Set CSRF token for state-changing methods
    axios.defaults.headers.post['X-CSRF-Token'] = csrf_token;
    axios.defaults.headers.put['X-CSRF-Token'] = csrf_token;
    axios.defaults.headers.delete['X-CSRF-Token'] = csrf_token;
    axios.defaults.headers.patch['X-CSRF-Token'] = csrf_token;

    // For TRACE method
    axios.defaults.headers.trace = {
        'X-CSRF-Token': csrf_token
    };

    // Alternative: Using interceptors for all requests
    axios.interceptors.request.use(config => {
        // Only add for state-changing methods
        if (!/^(GET|HEAD|OPTIONS)$/i.test(config.method)) {
            config.headers['X-CSRF-Token'] = csrf_token;
        }
        return config;
    });
</script>
```

This code snippet has been tested with Axios version 1.9.0.

#### jQuery

JQuery exposes an API called `$.ajaxSetup()` which can be used to add the `X-CSRF-Token` header to the AJAX request. API documentation for `$.ajaxSetup()` can be found here. The function `csrfSafeMethod()` defined below will filter out the safe HTTP methods and only add the header to unsafe HTTP methods.

You can configure jQuery to automatically add the token to all request headers by adopting the following code snippet. This provides a simple and convenient CSRF protection for your AJAX based applications:

```
<script type="text/javascript">
    const csrf_token = $('meta[name="csrf-token"]').attr('content');

    const csrfSafeMethod = method => {
        // these HTTP methods do not require CSRF protection
        return /^(GET|HEAD|OPTIONS)$/i.test(method);
    };

    $.ajaxSetup({
        beforeSend: (xhr, settings) => {
            if (!csrfSafeMethod(settings.type) && !settings.crossDomain) {
                xhr.setRequestHeader("X-CSRF-Token", csrf_token);
            }
        }
    });
</script>
```

This code snippet has been tested with jQuery version 3.7.1.

### TypeScript Utilities for CSRF Protection

TypeScript allows you to create strongly typed utilities for CSRF protection. Here's a reusable utility module for CSRF token management:

```
// csrf-protection.ts

/**
 * Configuration options for CSRF protection
 */
interface CSRFOptions {
  /** Cookie name where the CSRF token is stored */
  cookieName: string;
  /** HTTP header name to use when sending the token */
  headerName: string;
  /** HTTP methods that require CSRF protection */
  unsafeMethods: string[];
}

/**
 * Default configuration for CSRF protection
 */
const DEFAULT_CSRF_OPTIONS: CSRFOptions = {
  cookieName: 'XSRF-TOKEN',
  headerName: 'X-CSRF-Token',
  unsafeMethods: ['POST', 'PUT', 'PATCH', 'DELETE']
};

/**
 * CSRF Protection utility class
 */
export class CSRFProtection {
  private options: CSRFOptions;

  constructor(options: Partial<CSRFOptions> = {}) {
    this.options = { ...DEFAULT_CSRF_OPTIONS, ...options };
  }

  /**
   * Extract CSRF token from cookies
   * @returns The CSRF token or empty string if not found
   */
  public getToken(): string {
    const cookieValue = document.cookie
      .split('; ')
      .find(cookie => cookie.startsWith(`${this.options.cookieName}=`));

    return cookieValue ? cookieValue.split('=')[1] : '';
  }

  /**
   * Check if the given HTTP method requires CSRF protection
   */
  public requiresProtection(method: string): boolean {
    return this.options.unsafeMethods.includes(method.toUpperCase());
  }

  /**
   * Add CSRF token to the provided headers object if needed
   */
  public addTokenToHeaders(method: string, headers: Record<string, string>): Record<string, string> {
    if (this.requiresProtection(method)) {
      const token = this.getToken();
      if (token) {
        headers[this.options.headerName] = token;
      }
    }
    return headers;
  }
}

// Usage example:
// const csrfProtection = new CSRFProtection();
// const headers = csrfProtection.addTokenToHeaders('POST', {});
```

#### Angular with TypeScript

Angular is built with TypeScript, making it a natural fit for strongly-typed CSRF protection. The example below shows how to configure Angular's CSRF protection with TypeScript:

```
// app.config.ts
import { ApplicationConfig } from '@angular/core';
import { provideRouter } from '@angular/router';
import { provideHttpClient, withXsrfConfiguration } from '@angular/common/http';

import { routes } from './app.routes';

// Configure CSRF protection with custom options
export const appConfig: ApplicationConfig = {
  providers: [
    provideHttpClient(
      withXsrfConfiguration({
        cookieName: 'XSRF-TOKEN', // Name of cookie containing token
        headerName: 'X-XSRF-TOKEN' // Header name for token submission
      })
    ),
    provideRouter(routes)
  ]
};
```

For a custom HTTP interceptor that handles CSRF tokens:

```
// csrf.interceptor.ts
import { Injectable } from '@angular/core';
import {
  HttpRequest,
  HttpHandler,
  HttpEvent,
  HttpInterceptor
} from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable()
export class CsrfInterceptor implements HttpInterceptor {
  private readonly TOKEN_HEADER_NAME = 'X-CSRF-Token';
  private readonly SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS'];

  constructor() {}

  intercept(request: HttpRequest<unknown>, next: HttpHandler): Observable<HttpEvent<unknown>> {
    // Skip CSRF protection for safe methods
    if (this.SAFE_METHODS.includes(request.method)) {
      return next.handle(request);
    }

    // Get token from cookie
    const token = this.getTokenFromCookie();

    if (token) {
      // Clone the request and add the CSRF token header
      const modifiedRequest = request.clone({
        headers: request.headers.set(this.TOKEN_HEADER_NAME, token)
      });
      return next.handle(modifiedRequest);
    }

    return next.handle(request);
  }

  private getTokenFromCookie(): string {
    const tokenCookie = document.cookie
      .split('; ')
      .find(cookie => cookie.startsWith('XSRF-TOKEN='));

    return tokenCookie ? tokenCookie.split('=')[1] : '';
  }
}
```

#### React with TypeScript

Here's a TypeScript implementation for React applications using axios:

```
// csrf-axios.ts
import axios, { AxiosInstance, AxiosRequestConfig } from 'axios';

/**
 * Create an axios instance with CSRF protection
 */
export function createCSRFProtectedAxios(
  options: {
    baseURL?: string;
    csrfHeaderName?: string;
    csrfCookieName?: string;
  } = {}
): AxiosInstance {
  const {
    baseURL = '',
    csrfHeaderName = 'X-CSRF-Token',
    csrfCookieName = 'XSRF-TOKEN'
  } = options;

  // Create axios instance
  const instance = axios.create({ baseURL });

  // Add CSRF token interceptor
  instance.interceptors.request.use((config: AxiosRequestConfig) => {
    // Only add for non-GET requests
    if (config.method && !['get', 'head', 'options'].includes(config.method.toLowerCase())) {
      const token = getCsrfToken(csrfCookieName);

      if (token && config.headers) {
        config.headers[csrfHeaderName] = token;
      }
    }
    return config;
  });

  return instance;
}

/**
 * Extract CSRF token from cookies
 */
function getCsrfToken(cookieName: string): string {
  const tokenCookie = document.cookie
    .split('; ')
    .find(cookie => cookie.startsWith(`${cookieName}=`));

  return tokenCookie ? tokenCookie.split('=')[1] : '';
}

// USAGE EXAMPLE

// Define api.ts
// import { createCSRFProtectedAxios } from './csrf-axios';
// export const api = createCSRFProtectedAxios({
//   baseURL: '/api',
//   csrfHeaderName: 'X-CSRF-Token'
// });

// In a React component:
// import { api } from './api';
// 
// function UserProfile() {
//   const updateUser = async (userData: UserData) => {
//     try {
//       // CSRF token is automatically added
//       const response = await api.post('/users/profile', userData);
//       return response.data;
//     } catch (error) {
//       console.error('Failed to update profile', error);
//     }
//   };
//   
//   // Rest of component...
// }
```

For React applications using fetch API with TypeScript:

```
// csrf-fetch.ts

/**
 * Interface for CSRF protection options
 */
interface CSRFFetchOptions {
  csrfHeaderName: string;
  csrfCookieName: string;
  baseUrl: string;
}

/**
 * A wrapper around fetch API with CSRF protection
 */
export class CSRFProtectedFetch {
  private options: CSRFFetchOptions;

  constructor(options: Partial<CSRFFetchOptions> = {}) {
    this.options = {
      csrfHeaderName: 'X-CSRF-Token',
      csrfCookieName: 'XSRF-TOKEN',
      baseUrl: '',
      ...options
    };
  }

  /**
   * Performs a fetch request with CSRF protection
   */
  public async fetch<T>(
    url: string, 
    options: RequestInit = {}
  ): Promise<T> {
    const { method = 'GET' } = options;
    const fullUrl = `${this.options.baseUrl}${url}`;

    // Create headers with CSRF token for unsafe methods
    const headers = new Headers(options.headers);

    if (!['GET', 'HEAD', 'OPTIONS'].includes(method.toUpperCase())) {
      const token = this.getCsrfToken();
      if (token) {
        headers.append(this.options.csrfHeaderName, token);
      }
    }

    // Perform request
    const response = await fetch(fullUrl, {
      ...options,
      headers
    });

    if (!response.ok) {
      throw new Error(`Request failed with status ${response.status}`);
    }

    return response.json();
  }

  /**
   * Shorthand for POST requests
   */
  public async post<T>(url: string, data: any, options: RequestInit = {}): Promise<T> {
    return this.fetch<T>(url, {
      ...options,
      method: 'POST',
      body: JSON.stringify(data),
      headers: {
        ...options.headers,
        'Content-Type': 'application/json'
      }
    });
  }

  /**
   * Extract CSRF token from cookies
   */
  private getCsrfToken(): string {
    const tokenCookie = document.cookie
      .split('; ')
      .find(cookie => cookie.startsWith(`${this.options.csrfCookieName}=`));

    return tokenCookie ? tokenCookie.split('=')[1] : '';
  }
}

// USAGE EXAMPLE

// Create an instance
// const api = new CSRFProtectedFetch({
//   baseUrl: '/api',
//   csrfHeaderName: 'X-CSRF-Token'
// });
// 
// // In React component
// const updateUser = async (userData: UserData) => {
//   try {
//     // CSRF token is automatically added
//     return await api.post('/users/profile', userData);
//   } catch (error) {
//     console.error('Failed to update profile', error);
//   }
// };
```

### CSRF

- OWASP Cross-Site Request Forgery (CSRF)
- PortSwigger Web Security Academy
- Mozilla Web Security Cheat Sheet
- Common CSRF Prevention Misconceptions
- Robust Defenses for Cross-Site Request Forgery
- For Java: OWASP CSRF Guard or Spring Security
- For PHP and Apache: CSRFProtector Project
- For Angular: Cross-Site Request Forgery (XSRF) Protection
