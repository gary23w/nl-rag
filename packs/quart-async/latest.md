---
title: "Quart documentation"
source: https://quart.palletsprojects.com/en/latest/
domain: quart-async
license: CC-BY-SA-4.0
tags: quart async framework, asgi flask compatible, python asynchronous framework, quart websocket support
fetched: 2026-07-02
---

# Quart

Quart is a Fast Python web microframework. Using Quart you can,

> - write JSON APIs e.g. a RESTful API,
> - render and serve HTML e.g. a blog,
> - serve WebSockets e.g. a simple chat,
> - stream responses e.g. serve video,
> - all of the above in a single app,
> - or do pretty much anything over the HTTP or WebSocket protocols.

With all of the above possible using asynchronous (asyncio) libraries/code or synchronous libraries/code.

If you are,

> - new to Python then start by reading Installation instructions,
> - new to Quart then try the Quickstart,
> - new to asyncio see the Introduction to asyncio guide,
> - migrating from Flask see Migration from Flask,
> - looking for a cheatsheet then look here.

Quart is an asyncio reimplementation of the popular Flask microframework API. This means that if you understand Flask you understand Quart. See Flask evolution to learn more about how Quart builds on Flask.

Like Flask Quart has an ecosystem of extensions for more specific needs. In addition a number of the Flask extensions work with Quart.

Quart is developed on Github. If you come across an issue, or have a feature request please open an issue.If you want to contribute a fix or the feature-implementation please do (typo fixes welcome), by proposing a merge request. If you want to ask for help try on discord.

Note

If you can’t find documentation for what you are looking for here, remember that Quart is an implementation of the Flask API and hence the Flask documentation is a great source of help. Quart is also built on the Jinja template engine and the Werkzeug toolkit.

The Flask documentation is so good that you may be better placed consulting it first then returning here to check how Quart differs.

## Tutorials

- Tutorials
  - Installation
  - Quickstart
  - Introduction to asyncio
  - Tutorial: Building a RESTful API
  - Tutorial: Building a simple blog
  - Tutorial: Building a basic chat server
  - Tutorial: Serving video
  - Deploying Quart

## How to guides

- How to guides
  - Background tasks
  - Blueprints
  - Custom Command Line Commands
  - Configuration
  - Developing with Quart
  - Detecting disconnection
  - Customise the Event Loop
  - Using Flask Extensions
  - Migration from Flask
  - JSON Encoding
  - Logging
  - Middleware
  - Consuming the request body
  - Routing
  - Server Sent Events
  - Session Storage
  - Startup and Shutdown
  - Streaming responses
  - Run synchronous code
  - Templates
  - Testing
  - Using Quart Extensions
  - Using HTTP/2
  - Using websockets

## Discussion

- Discussions
  - Async compatibility
  - Background tasks
  - Contexts
  - Design Choices
  - Denial Of Service mitigations
  - Flask evolution
  - Globals
  - Python version support
  - Websockets
