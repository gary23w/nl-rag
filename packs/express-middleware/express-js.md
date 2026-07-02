---
title: "Express.js"
source: https://en.wikipedia.org/wiki/Express.js
domain: express-middleware
license: CC-BY-SA-4.0
tags: express middleware, express router, request handler chain, node web middleware
fetched: 2026-07-02
---

# Express.js

**Express.js**, or simply **Express**, is a back end web application framework for Node.js, released as free and open-source software under the MIT License. It is designed for building web applications and APIs. It has been called the de facto standard server framework for Node.js.

The original author, TJ Holowaychuk, described it as a Sinatra-inspired server, meaning that it is relatively minimal with many features available as plugins. Express is the back-end component of popular development stacks like the MEAN, MERN or MEVN stack, together with the MongoDB database software and a JavaScript front-end framework or library.

## History

Express.js was founded by TJ Holowaychuk. The initial versions were created in early 2010, and milestone version 1 was released later that year.

In June 2014, rights to manage the project were acquired by StrongLoop. StrongLoop was acquired by IBM in September 2015; in January 2016, IBM announced that it would place Express.js under the stewardship of the Node.js Foundation incubator.

In July 2014, work began towards milestone version 5. After ten years of development it was released in October 2024.

## Features

- Robust routing
- HTTP helpers (redirection, caching, etc.)
- Asynchronous programming
- Long-term support of legacy versions

## Popularity

Express.js is used by Fox Sports, PayPal, Uber and IBM.

## Example

The following program will respond to HTTP GET requests with the text "Hi, your request has been received", and listen to the port the program is running on (in this case, port 2000).

```mw
// Importing the Express library.
const express = require('express');

// Initializing the app.
const app = express();

// Getting the path request and sending the response with text.
app.get('/', (req, res) => {
    res.send('Hi, your request has been received');
});

// Listening on port 2000.
app.listen(2000, () => {
    console.log('listening at http://localhost:2000');
});
```
