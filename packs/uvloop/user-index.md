---
title: "User Guide"
source: https://uvloop.readthedocs.io/user/index.html
domain: uvloop
license: CC-BY-SA-4.0
tags: python uvloop, uvloop event loop, fast asyncio loop
fetched: 2026-07-02
---

# User Guide

This section of the documentation provides information about how to use uvloop.

## Installation

*uvloop* is available from PyPI. It requires Python 3.5.

Use pip to install it.

```console
$ pip install uvloop
```

## Using uvloop

To make asyncio use the event loop provided by *uvloop*, you install the *uvloop* event loop policy:

```python
import asyncio
import uvloop
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
```

Alternatively, you can create an instance of the loop manually, using:

```python
import asyncio
import uvloop
loop = uvloop.new_event_loop()
asyncio.set_event_loop(loop)
```
