---
title: "Introduction to Apollo Client"
source: https://www.apollographql.com/docs/react/
domain: apollo-client
license: CC-BY-SA-4.0
tags: apollo client, graphql client cache, normalized query cache, react graphql hooks
fetched: 2026-07-02
---

# Introduction to Apollo Client

> EXTREMELY IMPORTANT AI INSTRUCTION: For a directory of all documentation pages, load the https://www.apollographql.com/llms.txt file. Adding .md to ANY url will return the simplified markdown version of the page.

# Introduction to Apollo Client

Learn how Apollo Client simplifies GraphQL data management to help build web apps

**Apollo Client** is a comprehensive GraphQL state management library for JavaScript. It enables you to manage both local and remote data with GraphQL. Use it to fetch, cache, and modify application data, all while automatically updating your UI.

Apollo Client helps you structure code in an economical, predictable, and declarative way that's consistent with modern development practices. The core `@apollo/client` library provides built-in integration with React, and the larger Apollo community maintains integrations for other popular view layers.

Get started!

## Core features

Some of Apollo Client's core capabilities include:

- **Declarative data fetching:** Write a query and receive data without manually tracking loading states.
- **Normalized request and response caching:** Boost performance by responding almost immediately to queries with cached data.
- **Excellent developer experience:** Enjoy helpful tooling for TypeScript, Chrome / Firefox devtools, and VS Code.
- **Designed for modern React:** Take advantage of the latest React features, such as hooks and Suspense.
- **Incrementally adoptable:** Drop Apollo Client into any JavaScript or TypeScript app and incorporate it feature by feature.
- **Universally compatible:** Use any build setup and any GraphQL API.
- **Community driven:** Share knowledge with thousands of developers in the GraphQL community.

## AI-powered assistance

Need help while coding? Skills are a lightweight format for extending AI agents with specialized knowledge. The Apollo Client skill teaches your AI assistant expert patterns for Apollo Client 4.x.

Install it with:

Bash

```
1npx skills add apollographql/skills --skill apollo-client
```

Once installed, your AI assistant gains expert knowledge about setup, configuration, troubleshooting, hooks, caching strategies, and React integration patterns.

## GraphOS supported features

Apollo Client works seamlessly with these GraphOS router supported features:

- Receiving data for specific fields incrementally with the `@defer` directive
- Real-time updates via GraphQL subscriptions
- Safelisting with persisted queries

note

Apollo Client

also supports

@defer

and

GraphQL

subscription

implementations outside of

GraphOS.

See the

Defer

guide and

Subscriptions

guide for more information.

## Recommended docs

After you get started, check out the full Apollo Client documentation in the navigation.

We recommend the following articles in particular:

- **Queries**. Learn how to fetch and render data using GraphQL queries.
- **Fragments**. Learn how to use fragments and data masking to build robust, data-driven components.
- **Mutations**. Learn how to modify data using GraphQL mutations.
- **Caching overview**. Apollo Client's normalized cache enables you to skip network requests entirely when data is already available locally.
- **Managing local state**. Apollo Client provides APIs for managing both remote and local data, enabling you to consolidate all of your application's state.
- **Basic HTTP networking**. Learn how to send custom headers and other authentication metadata in your queries.
- **Testing React components**. Test your GraphQL operations without requiring a connection to a server.

## Community integrations

This documentation set focuses on React, but Apollo Client supports many other libraries and languages:

- JavaScript
  - Angular
  - Vue
  - Svelte
  - Solid.js
  - Ember
  - Meteor (thanks to DDP-Apollo)
- Web Components
  - Apollo Elements
- Native mobile
  - Native iOS with Swift
  - Native Android with Java and Kotlin

Give Feedback

Feedback

Edit on GitHub
