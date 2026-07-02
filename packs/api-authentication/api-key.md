---
title: "API key"
source: https://en.wikipedia.org/wiki/API_key
domain: api-authentication
license: CC-BY-SA-4.0
tags: api authentication, oauth flow, openid connect, bearer token
fetched: 2026-07-02
---

# API key

An **application programming interface** (**API**) **key** is a secret unique identifier used to authenticate and authorize a user, developer, or calling program to an API.

Cloud computing providers such as Google Cloud Platform and Amazon Web Services recommend that API keys only be used to authenticate projects, rather than human users.

## Usage

### HTTP APIs

API keys for HTTP-based APIs can be sent in multiple ways:

The access token is often a JSON Web Token (JWT) in the HTTP Authorization header:

```mw
POST /something HTTP/1.1
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

In the query string:

```mw
POST /something?api_key=abcdef12345 HTTP/1.1
```

As a request header:

```mw
GET /something HTTP/1.1
X-API-Key: abcdef12345
```

As a cookie:

```mw
GET /something HTTP/1.1
Cookie: X-API-KEY=abcdef12345
```

## Security

API keys are generally not considered secure; they are typically accessible to clients, making it easy for someone to steal an API key. Keys often have no expiration, meaning a stolen key can be used indefinitely unless revoked or regenerated. Keys are supposed to be a secret known only by the client and server, so they should not be communicated over an insecure channel and can only be considered secure when used in conjunction with other security mechanisms such as HTTPS.

There are several risk scenarios when using API keys:

- Developers may write scripts that contain keys in plaintext.
- Developers may hard-code keys into source code, and forget that when they release the code.
- Having unprotected keys in mobile apps is dangerous.

These risks generally stem from the key being in plaintext, which is potentially accessible to adversaries.

## Incidents

In 2017, Fallible, a Delaware-based security firm examined 16,000 Android apps and identified over 300 which contained hard-coded API keys for services like Dropbox, Twitter, and Slack.
