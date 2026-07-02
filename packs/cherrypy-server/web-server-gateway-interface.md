---
title: "Web Server Gateway Interface"
source: https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface
domain: cherrypy-server
license: CC-BY-SA-4.0
tags: cherrypy python framework, object oriented web framework, python wsgi server, cherrypy http toolkit
fetched: 2026-07-02
---

# Web Server Gateway Interface

The **Web Server Gateway Interface** (**WSGI**, pronounced *whiskey* or *WIZ-ghee*) is a simple calling convention for web servers to forward requests to web applications or frameworks written in the Python programming language. The current version of WSGI, version 1.0.1, is specified in Python Enhancement Proposal (PEP) 3333.

WSGI was originally specified as PEP-333 in 2003. PEP-3333, published in 2010, updates the specification for Python 3.

## Background

In 2003, Python web frameworks were typically written against only CGI, FastCGI, mod_python, or some other custom API of a specific web server. To quote PEP 333:

> Python currently boasts a wide variety of web application frameworks, such as Zope, Quixote, Webware, SkunkWeb, PSO, and Twisted Web -- to name just a few. This wide variety of choices can be a problem for new Python users, because generally speaking, their choice of web framework will limit their choice of usable web servers, and vice versa... By contrast, although Java has just as many web application frameworks available, Java's "servlet" API makes it possible for applications written with any Java web application framework to run in any web server that supports the servlet API.

WSGI was thus created as an implementation-neutral interface between web servers and web applications or frameworks to promote common ground for portable web application development.

## Specification overview

The WSGI has two sides:

- the server/gateway side. This is often running full web server software such as Apache or Nginx, or is a lightweight application server that can communicate with a webserver, such as flup.
- the application/framework side. This is a Python callable, supplied by the Python program or framework.

Between the server and the application, there may be one or more *WSGI middleware components*, which implement both sides of the API, typically in Python code.

WSGI does not specify how the Python interpreter should be started, nor how the application object should be loaded or configured, and different frameworks and webservers achieve this in different ways.

## WSGI middleware

A WSGI middleware component is a Python callable that is itself a WSGI application, but may handle requests by delegating to other WSGI applications. These applications can themselves be WSGI middleware components.

A middleware component can perform such functions as:

- Routing a request to different application objects based on the target URL, after changing the environment variables accordingly.
- Allowing multiple applications or frameworks to run side-by-side in the same process
- Load balancing and remote processing, by forwarding requests and responses over a network
- Performing content post-processing, such as applying XSLT stylesheets

## Examples

### Example application

A WSGI-compatible "Hello, World!" application written in Python:

```mw
def application(environ, start_response):
    start_response("200 OK", [("Content-Type", "text/plain")])
    yield b"Hello, World!\n"
```

Where:

- Line 1 defines a function named `application`, which takes two parameters, `environ` and `start_response`. `environ` is a dictionary containing CGI environment variables as well as other request parameters and metadata under well-defined keys. `start_response` is a callable itself, taking two positional parameters, `status` and `response_headers`.
- Line 2 calls `start_response`, specifying "200 OK" as the HTTP status and a "Content-Type" response header.
- Line 3 makes the function into a generator. The body of the response is returned as an iterable of byte strings.

### Example of calling an application

A full example of a WSGI network server is outside the scope of this article. Below is a sketch of how one would call a WSGI application and retrieve its HTTP status line, response headers, and response body, as Python objects. Details of how to construct the `environ` dict have been omitted.

```mw
from io import BytesIO

def call_application(app, environ):
    status = None
    headers = None
    body = BytesIO()

    def start_response(rstatus, rheaders):
        nonlocal status, headers
        status, headers = rstatus, rheaders

    app_iter = app(environ, start_response)
    try:
        for data in app_iter:
            assert (
                status is not None and headers is not None
            ), "start_response() was not called"
            body.write(data)
    finally:
        if hasattr(app_iter, "close"):
            app_iter.close()
    return status, headers, body.getvalue()

environ = {...}  # "environ" dict
status, headers, body = call_application(app, environ)
```

## WSGI-compatible applications and frameworks

Numerous web frameworks support WSGI:

- bjoern
- BlueBream
- bobo
- Bottle
- CherryPy
- Django
- Eventlet
- FastWSGI
- Flask
- Falcon (web framework)
- Gevent-FastCGI
- Google App Engine's webapp2
- Gunicorn
- prestans
- mod_wsgi for use with Apache
- netius
- pycnic
- Paste component WebOb is specifically a WSGI extension. It was adopted by the Pylons project.
- Pylons
- Pyramid
- restlite
- Socketify
- Tornado
- Trac
- TurboGears
- Uliweb
- uWSGI
- Waitress
- web.py
- web2py
- weblayer
- Werkzeug
- Radicale

Currently wrappers are available for FastCGI, CGI, SCGI, AJP (using flup), twisted.web, Apache (using mod_wsgi or mod_python), Nginx (using ngx_http_uwsgi_module), Nginx Unit (using the Python language module), and Microsoft IIS (using WFastCGI, isapi-wsgi, PyISAPIe, or an ASP gateway).
