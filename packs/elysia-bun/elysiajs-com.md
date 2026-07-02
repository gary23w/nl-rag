---
title: "Elysia - Ergonomic Framework for Humans"
source: https://elysiajs.com/
domain: elysia-bun
license: CC-BY-SA-4.0
tags: elysia bun framework, bun runtime web, typescript bun framework, elysia end to end typing
fetched: 2026-07-02
---

### Our Principle

## Design for Humans

Our goal is to design an ergonomic, sensible, and productive framework that even beginners can use easily

Designed to avoid unnecessary complexity and type complexity for you to focus on building

A framework that feels just like JavaScript

typescript

```typescript
import { Elysia, file } from 'elysia'

new Elysia()
	.get('/', 'Hello World')
	.get('/image', file('mika.webp'))
	.get('/stream', function* () {
		yield 'Hello'
		yield 'World'
	})
	.ws('/realtime', {
		message(ws, message) {
			ws.send('got:' + message)
		}
	})
	.listen(3000)
```

### 21x

faster than Express

### 6x

faster than Fastify

1. Elysia Bun2,454,631 reqs/s
2. Gin Go676,019
3. Spring Java506,087
4. Fastify Node415,600
5. Express Node113,117
6. Nest Node105,064

Measured in requests/second. Result from TechEmpower Benchmark Round 22 (2023-10-17) in PlainText

### It's all about

## Single Source of Truth

Schema is the only source of truth for your entire server. From request validation, type inference, OpenAPI documentation, client-server communication. Every part of Elysia is design for complete type integrity.

# Request Validation

Elysia validates, and normalize requests against your schema, ensuring that only valid data reaches your handlers.

Elysia also infers types directly from your schema, ensuring that your handlers always receive the correct types in both runtime, and type-level.

typescript

```typescript
import { Elysia
, t
 } from 'elysia'

new Elysia
()
	.put
('/', ({ body
: { file
 } }) => file
, {
		body
: t
.Object
({
			file
: t
.File
({ type
: 'image' })
		})
	})
```

# Advance Type Inference

Every part of Elysia is designed to be completely type-safe far more advance type inference than any other frameworks.

Elysia also infers type from your schema, provide an auto-completion for models or extends Elysia with your own custom property all while ensuring complete type integrity.

typescript

```typescript
import { Elysia
 } from 'elysia'
import { auth
 } from './auth'

new Elysia
()
	.use
(auth
)
	.get
('/profile', ({ user
 }) => user
, {
        auth
: true
	})
```

typescript

```typescript
import { Elysia, t } from 'elysia'

export const auth = new Elysia()
	.macro('auth', {
		cookie: t.Object({
			ssid: t.String()
		}),
		resolve({ cookie, status }) {
			if(!cookie.ssid.value) return status(401)

			return {
				user: cookie.ssid.value
			}
		}
	})
```

# Client-Server Communication

Elysia can share types between client and server similar to tRPC, ensuring that both sides are always in sync.

Taking a step further, Elysia also handle multiple HTTP status and arrange them using discriminated union, allowing you to handle all possible error cases with ease.

typescript

```typescript
import { treaty
 } from '@elysia/eden'
import type { App
 } from 'server'

const api
 = treaty
<App
>('api.elysiajs.com')

const { data
 } = await api
.profile.patch({
    age
: 21
})
```

# OpenAPI Documentation

Elysia generates OpenAPI documentation from your schema in 1 line. Ensuring your API documentation are always accurate and up-to-date.

typescript

```typescript
import { Elysia } from 'elysia'
import { openapi } from '@elysia/openapi'

new Elysia()
	.use(openapi())
```

### Introducing our most powerful feature yet

## TypeScript to OpenAPI

Elysia can generate OpenAPI specifications directly from your TypeScript code without any annotations, without any configuration and CLI running.

Allowing you to turn your actual code from any library like Prisma, Drizzle and every TypeScript library into your own API documentation.

typescript

```typescript
import { Elysia } from 'elysia'
import { openapi, fromTypes } from '@elysia/openapi'

export const app = new Elysia()
	.use(
		openapi({
			// ↓ Where magic happens 
			references: fromTypes()
		})
	)
```

## Bring your own Validator

### With support for Standard Schema

Elysia offers a robust built-in validation, but you can also bring your favorite validator, like Zod, Valibot, ArkType, Effect and more

With seamless support for type inference, and OpenAPI. You will feel right at home .

ts

```ts
import { Elysia, t } from 'elysia'

new Elysia()
	// Try hover body  ↓
	.post('/user', ({ body }) => body, {
		body: t.Object({
			name: t.Literal('SaltyAom'),
			age: t.Number(),
			friends: t.Array(t.String())
		})
	})
```

ts

```ts
import { Elysia } from 'elysia'
import { z } from 'zod'

new Elysia()
	// Try hover body  ↓
	.post('/user', ({ body }) => body, {
		body: z.object({
			name: z.literal('SaltyAom'),
			age: z.number(),
			friends: z.array(z.string())
		})
	})
```

ts

```ts
import { Elysia } from 'elysia'
import * as v from 'valibot'

new Elysia()
	// Try hover body  ↓
	.post('/user', ({ body }) => body, {
		body: v.object({
			name: v.literal('SaltyAom'),
			age: v.number(),
			friends: v.array(v.string())
		})
	})
```

ts

```ts
import { Elysia } from 'elysia'
import { type } from 'arktype'

new Elysia()
	// Try hover body  ↓
	.post('/user', ({ body }) => body, {
		body: type({
			name: '"Elysia"',
			age: 'number',
			friends: 'string[]'
		})
	})
```

ts

```ts
import { Elysia } from 'elysia'
import { Schema } from 'effect'

new Elysia()
	// Try hover body  ↓
	.post('/user', ({ body }) => body, {
		body: Schema.standardSchemaV1(
			Schema.Struct({
				name: Schema.Literal('Elysia'),
				age: Schema.Number,
				friends: Schema.Array(Schema.String)
			})
		)
	})
```

11.88ms

POST /character/:id/chat

Playback

Request

Validation

Transaction

Upload

Sync

##### For DevOps

## OpenTelemetry

Elysia has 1st party support for OpenTelemetry. Instrumentation is built-in, so you can easily monitor your services regardless of the platform.

typescript

```typescript
import { treaty
 } from '@elysia/eden'
import type { App
 } from 'server'

const api
 = treaty
<App
>('api.elysiajs.com')

const { data
 } = await api
.profile.patch({
    age
: 21
})
```

##### For Frontend

## End-to-end Type Safety

Like tRPC, Elysia provides type-safety from the backend to the frontend without code generation. The interaction between frontend and backend is both type-checked at compile and runtime.

## Test with Confidence

### Type safe with auto-completion

Elysia provides a type-safe layer to interact with and test your server, from routes to parameters.

With auto-completion, you can easily write tests for the server without any hassle.

typescript

```typescript
import { treaty
 } from '@elysia/eden'
import { app
 } from './index'
import { test
, expect
 } from 'bun:test'

const server
 = treaty
(app
)

test
('should handle duplicated user', async () => {
	const { error
 } = await server
.user
.put
({Argument of type '{ username: string; }' is not assignable to parameter of type '{ username: string; password: string; }'.
  Property 'password' is missing in type '{ username: string; }' but required in type '{ username: string; password: string; }'.
	    username
: 'mika',
	})

	expect
(error
?.value
).toEqual
({
		success
: false,
		message
: 'Username already taken'
	})
})
```

## Your code, Your Runtime

### Elysia is optimized for Bun,

### but not vendor lock-in to Bun

### Elysia is built on Web-Standard

### allowing you to run Elysia anywhere

## What people say about

Elysia

Aqueel

@AqueelMiq

Jetfuel on bun at X! @shlomiatar who built the framework has an eye for picking the right tools for the job.

Shlomi Atar

@shlomiatar

also a shoutout to @saltyAom and the phenomenal Elysia js that is powering our server driven UI. Incredible work.

htmx.org

@htmx_org

htmx works great w/ @bunjavascript, @elysia and @tursodatabase btw

nuqs

@nuqs47ng

I’m a Node.js + Fastify diehard, but the Bun + Elysia combo looks very promising 👀

Erwin

@Erwin_AI

Already using Elysia (+Bun) anywhere I can. Wouldn't want to back to node+express even if you'd pay me a mil.

Jarred Sumner

@jarredsumner

You can use Express with Bun, but often we see people using Elysia, Hono, or Bun.serve() directly.

Runyasak Ch. 💚

@runyasak

Started using @elysia to create a Discord Bot and found the type system beautifully easy. DX is fantastic and coding is fun! Use @DrizzleORM with PostgreSQL. So much easier than I've used before. ElysiaJS has proved to me that great performance and DX can live together. 😎

Herrington Darkholme

@hd_nvim

Was introduced to @elysia today and it looks pretty solid. end-to-end type safety/guard/swapper are killer features of the modern web! (and it's fast)

scalar.com

@scalar

so excited to be part of the amazing @elysia community!

José Donato 🦋

@josedonato__

handling tables with ~350k rows like it's nothing. Working on allowing @ag_grid server side row model when connecting a custom backend to @openbb_finance Terminal Pro. Backend in @elysia + @bunjsproject.

Bewinxed

@Bewinxed

Elysia single handedly carrying js backends I have been using it almost exclusively for all my projects

MikroORM

@MikroORM

I've been playing a bit with @bunjavascript and @elysia, need to do a few more tweaks before the release, but next version should work more natively with bun when it comes to TS support detection, e.g. the CLI works without ts-node installed.

Marc Laventure

@MarcLaventure

both engineering+monetary contributions are paramount for OSS we proudly sponsor dozens of projects: @elysia @LitestarAPI @honojs @daveshanley @kevin_jahns @MarijnJH & help maintain repos+contribute to OSS at blistering cadence. it's @scalar's ethos to be a catalyst for OSS

meabed

@Meabed

I am building something with Bun + ElysiaJS and the speed and ergonomics are way out of this world!!!! I can't go back to express + node... Bun Hot reload an HTTP server and test runner is instantaneous!!! Elysia is a breath of fresh air + inferred types + openapi + plugins + file handling + ai sdk + typed client.... The dev experience is 100x - if you try you won't ever go back!!

haxiom.io

@haxiom_io

One diff ElysiaJS made in our org is that it makes it easy to refactor fearlessly. You can be pretty certain if things won't work simply because TypeScript will tell you that your types don't match

ꜱᴛᴀᴄɪᴀ

@stacia__x

ElysiaJS was the first framework that truly sparked my interest in JS/TS. I used to avoid it entirely. I usually stick to Python, mostly using FastAPI. When I tried ElysiaJS for the first time (v1.1), I immediately felt it provides an amazing dev experience. Love ElysiaJS 😘

Micky

@Rasmic

I’m ngl we don’t talk about @elysia enough

## Because of You

Elysia is not owned by an organization, driven by volunteers, and community. Elysia is possible by these awesome sponsors.

#### Gold Sponsors 💛

- (Sponsor avatar)Jarred Sumnerfor 3 years
- (Sponsor avatar)San Francisco Compute Companyfor 2 years
- (Sponsor avatar)CodeRabbitfor a year
- (Sponsor avatar)Better Authfor 10 months
- (Sponsor avatar)Comp AIfor 10 months
- (Sponsor avatar)Muxfor 6 months
- (Sponsor avatar)Zephyr Cloud IOfor 5 months
- (Sponsor avatar)Photonfor 4 months

#### Silver Sponsors 🤍

- (Sponsor avatar)Scalarfor 3 years

#### Generous Sponsors 💞

- (Sponsor avatar)_typedevfor 3 years
- (Sponsor avatar)DOM CHAROENYOSfor 2 years
- (Sponsor avatar)Naoki Takahashifor 2 years
- (Sponsor avatar)Khyber Senfor 2 years
- (Sponsor avatar)MeCodefor 2 years
- (Sponsor avatar)yoyoismeefor 2 years
- (Sponsor avatar)Firat Özcanfor 2 years
- (Sponsor avatar)TranspaCleanfor a year
- (Sponsor avatar)Pitsanu Kittipittayakornfor 10 months
- (Sponsor avatar)Alex Ozerovfor 10 months
- (Sponsor avatar)Siriwat Kfor 9 months
- (Sponsor avatar)Elysia Root L.C.for 14 days
- (Sponsor avatar)frankwangfor 5 months
- And you

#### Individual Sponsors 💕

- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)
- (Sponsor avatar)

Thank you for making Elysia possible

We can only develop Elysia full-time thanks to your support.

Become a sponsor

With love from our community

### Ask about Elysia

### Elysia

#### Ergonomic Framework for Humans

##### Speed

Top Performance

##### Type Safety

Best in class

##### Developer Experience

Exceptional

##### OpenAPI Support

One of a kind
