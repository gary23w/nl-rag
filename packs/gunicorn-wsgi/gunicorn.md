---
title: "Gunicorn"
source: https://en.wikipedia.org/wiki/Gunicorn
domain: gunicorn-wsgi
license: CC-BY-SA-4.0
tags: python gunicorn, gunicorn wsgi server, wsgi worker python
fetched: 2026-07-02
---

# Gunicorn

The **Gunicorn** "Green Unicorn" (pronounced jee-unicorn or gun-i-corn) is a Python Web Server Gateway Interface (WSGI) HTTP server. It is a pre-fork worker model, ported from Ruby's Unicorn project. The Gunicorn server is broadly compatible with a number of web frameworks, simply implemented, light on server resources and fairly fast. It is often paired with Nginx, as the two have complementary features.

## Architecture

Server model

- Central master process to manage the workers
- Requests are handled by worker processes
- Components:
  - Master
  - Sync workers
  - Async workers
  - Tornado workers
  - AsyncIO workers

## Features

- Natively supports WSGI, web2py, Django and Paster
- Automatic worker process management
- Simple Python configuration
- Multiple worker configurations
- Various server hooks for extensibility
- Compatible with Python 2.6+ and Python 3.2+
